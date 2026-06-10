import pytest
from gpu_allocator import GPU, GPUAllocator, GPUAllocationError


def make_allocator() -> GPUAllocator:
    """Create a deterministic allocator with 3 GPUs."""
    gpus = [
        GPU(id="gpu0", total_memory_gb=16),
        GPU(id="gpu1", total_memory_gb=8),
        GPU(id="gpu2", total_memory_gb=32),
    ]
    return GPUAllocator(gpus)


def test_round_robin_allocation():
    alloc = make_allocator()
    # 1st → gpu0
    gpu = alloc.allocate(4)
    assert gpu.id == "gpu0"
    assert gpu.used_memory_gb == 4
    # 2nd → gpu1
    gpu = alloc.allocate(2)
    assert gpu.id == "gpu1"
    # 3rd → gpu2
    gpu = alloc.allocate(8)
