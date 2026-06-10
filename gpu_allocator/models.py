from __future__ import annotations
from typing import List, Literal, Optional
from pydantic import BaseModel, Field, validator


class AllocationRequest(BaseModel):
    """Incoming request to allocate GPUs."""
    job_id: str = Field(..., description="Unique identifier for the job")
    requested_gpus: int = Field(..., gt=0, description="Number of GPUs requested")
    priority: Literal["high", "medium", "low"] = Field(
        "medium", description="Scheduling priority"
    )

    @validator("job_id")
    def non_empty(cls, v: str) -> str:
        if not v.strip():
            raise ValueError("job_id must be non‑empty")
        return v


class AllocationResult(BaseModel):
    """Result returned to the caller."""
    job_id: str
    granted_gpus: int
    error_margin_pct: float
    status: Literal["allocated", "rejected"]
    message: Optional[str] = None


class AllocationState(BaseModel):
    """Snapshot broadcast over WebSocket."""
    total_gpus: int
    used_gpus: int
    allocations: List[AllocationResult] = Field(default_factory=list)

    @property
    def free_gpus(self) -> int:
        return self.total_gpus - self.used_gpus