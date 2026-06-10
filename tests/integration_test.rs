"""
gpu_allocator.allocator
~~~~~~~~~~~~~~~~~~~~~~~

A tiny, thread‑safe GPU allocator that can be used in unit tests or
in a real node‑level service.

Features
--------
* Optional automatic discovery via ``nvidia-smi``.
* Deterministic allocation order (FIFO from the discovered list).
* Simple API: ``allocate(client_id=None)``, ``release(gpu_id)``, ``status()``.
* Raises clear exceptions for misuse.
"""

from __future__ import annotations

import subprocess
import threading
from typing import Dict, Iterable, List, Optional, Set

__all__ = ["GPUAllocator"]


class GPUAllocator:
    """
    Allocate and release GPU IDs on a single node.

    Parameters
    ----------
    gpu_ids : Iterable[int] | None
        Explicit list of GPU IDs to manage.  If ``None`` the allocator will
        attempt to discover GPUs via ``nvidia-smi``; if discovery fails
        it raises ``RuntimeError``.
    max_gpus : int | None
        Optional cap on the number of GPUs exposed.  Useful for tests that
        want to simulate a smaller pool.
    """

    # ------------------------------------------------------------------ #
    # Construction / discovery
    # ------------------------------------------------------------------ #
    def __init__(
        self,
        gpu_ids: Optional[Iterable[int]] = None,
        max_gpus: Optional[int] = None,
    ) -> None:
        self._lock = threading.RLock()

        if gpu_ids is None:
            gpu_ids = self._discover()
            if not gpu_ids:
                raise RuntimeError(
                    "No GPUs discovered and no explicit list supplied"
                )

        # Canonical list of IDs – preserve order for deterministic allocation
        self._gpus: List[int] = list(gpu_ids)
        if max_gpus is not None:
            self._gpus = self._gpus[:max_gpus]

        # State
        self._free: Set[int] = set(self._gpus)          # free GPUs
        self._allocations: Dict[int, Optional[str]] = {}  # gpu_id -> client_id

    # ------------------------------------------------------------------ #
    # Public API
    # ------------------------------------------------------------------ #
    def allocate(self, client_id: Optional[str] = None) -> int:
        """
        Allocate a single free GPU.

        Parameters
        ----------
        client_id : str | None
            Optional identifier of the requesting job.  Stored only for
            introspection; the allocator does not enforce uniqueness.

        Returns
        -------
        int
            The allocated GPU ID.

        Raises
        ------
        RuntimeError
            If no GPUs are free.
        """
        with self._lock:
