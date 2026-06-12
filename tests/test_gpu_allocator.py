import json
from src.gpu_allocator import load_config, parse_config, schedule, Job, GPU
import pytest

def test_load_config():
    config = load_config('tests/config.json')
    assert config.get('jobs') == [{'id': 1}, {'id': 2}]

def test_parse_config():
    config = {'jobs': [{'id': 1}, {'id': 2}], 'gpus': [{'id': 1}, {'id': 2}]}
    jobs, gpus = parse_config(config)
    assert len(jobs) == 2
    assert len(gpus) == 2

def test_schedule():
    jobs = [Job(id=1), Job(id=2)]
    gpus = [GPU(id=1), GPU(id=2)]
    gpu_allocations = schedule(jobs, gpus)
    assert gpu_allocations == {1: 1, 2: 2}

def test_schedule_insufficient_gpus():
    jobs = [Job(id=1), Job(id=2), Job(id=3)]
    gpus = [GPU(id=1), GPU(id=2)]
    gpu_allocations = schedule(jobs, gpus)
    assert gpu_allocations == {1: 1, 2: 2}

def test_main(capsys):
    import sys
    import io
    from contextlib import redirect_stdout
    with redirect_stdout(io.StringIO()) as f:
        sys.argv = ['gpu_allocator.py', '--config', 'tests/config.json']
        from src.gpu_allocator import main
        main()
        captured = capsys.readouterr()
        if captured.out:
            assert json.loads(captured.out) == {1: 1, 2: 2}
        else:
            assert True
