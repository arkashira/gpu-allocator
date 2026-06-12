import argparse
import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Job:
    id: int
    gpu_id: int = None

@dataclass
class GPU:
    id: int
    available: bool = True

def load_config(file_path: str) -> Dict:
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return {}

def parse_config(config: Dict) -> (List[Job], List[GPU]):
    jobs = [Job(id=job['id']) for job in config.get('jobs', [])]
    gpus = [GPU(id=gpu['id']) for gpu in config.get('gpus', [])]
    return jobs, gpus

def schedule(jobs: List[Job], gpus: List[GPU]) -> Dict:
    gpu_allocations = {}
    for job in jobs:
        for gpu in gpus:
            if gpu.available:
                gpu_allocations[job.id] = gpu.id
                gpu.available = False
                break
        else:
            # If no available GPU is found, do not allocate
            pass
    return gpu_allocations

def main():
    parser = argparse.ArgumentParser(description='GPU Allocator')
    parser.add_argument('--config', help='Path to configuration file')
    args = parser.parse_args()
    if args.config:
        config = load_config(args.config)
        jobs, gpus = parse_config(config)
        gpu_allocations = schedule(jobs, gpus)
        if gpu_allocations:
            print(json.dumps(gpu_allocations))
        else:
            print(json.dumps({}))
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
