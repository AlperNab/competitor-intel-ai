# Competitor Intel Ai

This folder has been upgraded into a **standalone real GUI project**.

Run the project GUI:

```bash
./run_gui.sh
```

Windows:

```powershell
.\run_gui_windows.ps1
```

Default local URL: `http://127.0.0.1:9110`

This project includes its own FastAPI backend, browser GUI, provider settings, local/cloud LLM routing, encrypted API-key storage, file uploads, job history, exports, and a project-specific plugin configuration.

See `PROJECT_IMPLEMENTATION.md` and `project_config.json` for the applied project-specific features and customization controls.

---

## Original README

# competitor-intel-ai

> **Competitor URL → complete competitive intelligence report.** Positioning analysis, ICP, pricing signals, feature gaps, messaging weaknesses, battle card for your sales team.

[![PyPI](https://img.shields.io/pypi/v/competitor-intel-ai?style=flat)](https://pypi.org/project/competitor-intel-ai/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Quickstart

```bash
pip install competitor-intel-ai

python -m competitor_intel_ai https://competitor.com

# With your product context for a battle card
python -m competitor_intel_ai https://competitor.com \
  --product "AI transcription SaaS" \
  --icp "founders and small teams"
```

## What you get

- Their positioning strategy and primary value prop
- ICP: company size, industries, buyer persona
- Pricing model and tier signals
- Core features vs differentiators vs obvious gaps
- Observable weaknesses with evidence and exploitation strategy
- Messaging gaps — topics they ignore that you can own
- SEO keyword themes
- **Battle card** — headline, your differentiators, trap questions to ask in deals, objection handlers

## License
MIT © [Alper Nabil Gabra Zakher](https://github.com/AlperNab)
