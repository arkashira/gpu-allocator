"""
GPU Allocator package.

Provides a tiny FastAPI service that allocates GPU slots to incoming
requests, validates input, enforces a ≤5 % error‑margin between the
requested and granted GPU count and pushes real‑time allocation updates
over a WebSocket.
"""
__all__ = ["engine", "models", "api"]