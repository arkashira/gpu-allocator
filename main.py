from allocator import GPUAllocator
from optimizer import GPUOptimizer

def main():
    allocator = GPUAllocator()
    optimizer = GPUOptimizer(allocator)

    # Example usage
    allocator.add_gpu("GPU-1", 1000)
    allocator.add_task("Task-1", 1, 500)
    allocated_gpu = allocator.allocate_gpu()
    if allocated_gpu:
        print(f"Allocated {allocated_gpu[0]} to {allocated_gpu[1]}")
    else:
        print("No allocation possible.")

if __name__ == "__main__":
    main()