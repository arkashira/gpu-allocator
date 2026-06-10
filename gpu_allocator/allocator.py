# gpu_allocator/allocator.py
"""
Simple, thread‑safe GPU allocator.

The allocator manages a fixed pool of GPU IDs (0 … pool_size‑1).  
Allocation is first‑come, first‑served; the lowest‑available ID is returned.
"""

from __future__ import annotations

import threading
from typing import Dict, List, Set


class GpuAllocator:
    """
    Allocate and free GPU IDs from a fixed pool.

    Parameters
    ----------
    pool_size : int
        Total number of GPUs available in the pool.
    """

    def __init__(self, pool_size: int):
        if pool_size <= 0:
            raise ValueError("pool_size must be positive")
        self._pool_size: int = pool_size
        self._lock = threading.Lock()
        # All GPUs start as free
        self._free: Set[int] = set(range(pool_size))
        self._used: Set[int] = set()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def allocate(self) -> int:
        """
        Allocate a free GPU.

        Returns
        -------
        int
            The allocated GPU ID.

        Raises
        ------
        RuntimeError
            If no GPUs are available.
        """
        with self._lock:
            if not self._free:
                raise RuntimeError("No GPUs available for allocation")
            gpu_id = self._free.pop()
            self._used.add(gpu_id)
            return gpu_id

    def free(self, gpu_id: int) -> None:
        """
        Release a previously allocated GPU.

        Parameters
        ----------
        gpu_id : int
            The GPU ID to free.

        Raises
        ------
        ValueError
            If the GPU ID was not allocated or is out of range.
        """
        with self._lock:
            if gpu_id not in self._used:
                raise ValueError(f"GPU {gpu_id} is not allocated")
            self._used.remove(gpu_id)
            self._free.add(gpu_id)

    def status(self) -> Dict[str, object]:
        """
        Return current allocation status.

        Returns
        -------
        dict
            {
                "total": int,
                "free": int,
                "used": int,
                "allocated_ids": List[int]
            }
        """
        with self._lock:
            return {
                "total": self._pool_size,
                "free": len(self._free),
                "used": len(self._used),
                "allocated_ids": sorted(self._used),
            }

    # ------------------------------------------------------------------
    # Convenience helpers
    # ------------------------------------------------------------------
    de
