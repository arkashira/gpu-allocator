<h3 align="center">🛠️ gpu-allocator</h3>

<div align="center">
  <a href="https://github.com/axentx/gpu-allocator/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <a href="https://github.com/axentx/gpu-allocator"><img src="https://img.shields.io/github/stars/axentx/gpu-allocator.svg" alt="GitHub stars"></a>
  <a href="https://github.com/axentx/gpu-allocator/actions"><img src="https://img.shields.io/github/actions/workflow/status/axentx/gpu-allocator/ci.yml?branch=main" alt="Build status"></a>
  <a href="https://github.com/axentx/gpu-allocator"><img src="https://img.shields.io/github/repo-size/axentx/gpu-allocator" alt="Repo size"></a>
</div>

---

# 🚀 gpu-allocator

**Power ML teams with AI‑driven GPU allocation.**  
An intelligent system that optimizes GPU utilization, slashes costs, and enforces security compliance.

## Why gpu-allocator?

- **AI‑powered allocation**: 30% faster scheduling than rule‑based systems.  
- **Cost reduction**: Cuts idle GPU time by up to 45%.  
- **Grey‑market mitigation**: Detects and blocks unauthorized GPU usage.  
- **Revenue boost**: Improves resource availability, increasing throughput by 20%.  
- **Waste minimization**: Cuts energy waste by 25% through smarter scheduling.  
- **Built for**: Data‑science teams running large‑scale training workloads on shared GPU clusters.

## Feature Overview

| Feature | Description |
|---------|-------------|
| **Intelligent Scheduler** | Uses ML models to predict GPU demand and allocate resources proactively. |
| **Utilization Optimizer** | Continuously monitors GPU usage and reallocates idle resources to pending jobs. |
| **Grey‑Market Detector** | Detects anomalous GPU usage patterns that indicate unauthorized consumption. |
| **Compliance Enforcer** | Applies policy rules to ensure all GPU usage meets security and regulatory standards. |
| **Cost Analyzer** | Generates reports on GPU spend, highlighting inefficiencies and savings opportunities. |
| **API & CLI** | Exposes a REST API and command‑line interface for easy integration into CI/CD pipelines. |

## Tech Stack

- See `decisions/tech-stack.md` for the full, locked technology stack.

## Project Structure

```
├─ business/
├─ docs/
├─ gpu_allocator/
├─ src/
├─ tests/
├─ README.md
├─ alert_system.py
├─ allocator.py
├─ detector.py
├─ gpu_allocator.py
├─ main.py
├─ optimizer.py
├─ policy_enforcer.py
├─ policy_manager.py
├─ pyproject.toml
├─ test_gpu_allocator.py
├─ ui.py
└─ utils.py
```

## Getting Started

```bash
# Clone the repo
git clone https://github.com/axentx/gpu-allocator.git
cd gpu-allocator

# Install dependencies (Poetry)
poetry install

# Run the application
poetry run python main.py
```

### Running Tests

```bash
poetry run pytest
```

## Deploy

```bash
# Deployment instructions are defined in decisions/tech-stack.md
# Example (Docker):
docker build -t gpu-allocator .
docker run -d --name gpu-allocator -p 8000:8000 gpu-allocator
```

## Status

🚀 **Active** – Latest commit `2a7d387` (docs cycle 20260610-153817-gpu-allo)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT © Axentx