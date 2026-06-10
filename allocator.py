import heapq

class GPUAllocator:
    def __init__(self):
        self.gpu_pool = []  # Available GPUs
        self.task_queue = []  # Priority queue for tasks

    def add_gpu(self, gpu_id, capacity):
        """Add a GPU to the pool."""
        self.gpu_pool.append((gpu_id, capacity))

    def add_task(self, task_id, priority, required_capacity):
        """Add a task to the priority queue."""
        heapq.heappush(self.task_queue, (priority, task_id, required_capacity))

    def allocate_gpu(self):
        """Allocate a GPU to the highest priority task."""
        if not self.task_queue:
            return None  # No tasks to allocate

        priority, task_id, required_capacity = self.task_queue[0]
        for gpu_id, capacity in self.gpu_pool:
            if capacity >= required_capacity:
                # Allocate the GPU to the task
                self.gpu_pool.remove((gpu_id, capacity))
                heapq.heappop(self.task_queue)
                return gpu_id, task_id

        # No suitable GPU found
        print("error: GPU request could not be allocated")
        return None