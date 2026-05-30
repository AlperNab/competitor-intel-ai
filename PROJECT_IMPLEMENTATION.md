# Competitor Intel Ai — Standalone Real GUI Implementation

This folder is now its own runnable project app. It does not depend on the root all-project dashboard at runtime.

## Run

```bash
./run_gui.sh
```

Windows:

```powershell
.\run_gui_windows.ps1
```

Default URL: `http://127.0.0.1:9110`

## What is inside this project folder

- `app/` — FastAPI backend for this project.
- `static/` — elegant browser GUI.
- `plugins/competitor-intel-ai.json` — this project’s own feature/customization/input schema.
- `project_config.json` — readable copy of the same project-specific configuration.
- `data/` — local SQLite jobs, uploads, exports.
- `tests/` — verifies this project has a registered real local engine.

## Project-specific scope

- Domain: `Business / Competitive Intelligence`
- Target user: `Domain operator, business owner, analyst, or team member who needs this workflow executed reliably.`
- Core job: Competitor URL → sales/marketing intelligence
- Suite: `General Automation Suite`

## Deep features applied

- site snapshot
- positioning extraction
- pricing intelligence
- feature gap matrix
- ICP inference
- battlecard
- alert monitoring
- evidence citations

## Customization controls

- `execution_mode` — Execution mode (select)
- `your_product_profile` — your product profile (select)
- `icp` — ICP (text)
- `region` — region (text)
- `competitor_list` — competitor list (textarea)
- `sales_angle` — sales angle (text)
- `pricing_model` — pricing model (select)
- `monitoring_frequency` — monitoring frequency (text)
- `output_format` — output format (select)
- `language` — language (select)
- `privacy_mode` — privacy mode (select)
- `confidence_threshold` — Confidence threshold (slider)

## Input fields

- `competitor_url` — Competitor URL (text) required
- `work_brief` — Work brief / source text / URL / instructions (textarea) required

## External data policy

The local deterministic core is real and executable. Live external systems are not simulated. If Shopify, ATS, ERP, OCR/STT, maps, SERP, market data, medical databases, tax/customs databases, or other live systems are required, this project reports the missing connector/API requirement instead of inventing data.

---

## Final UX/UI Layer

This project now uses the **Automation Command Center** pattern.

**UX workflow:** Brief/data intake → structured analysis → action plan → export

**Domain components:**
- Brief analyzer
- KPI cards
- Workflow board
- Decision checklist
- Report builder

**Quick actions:**
- Structure input
- Generate action plan
- Build scorecard
- Prepare final report

**No fake-data policy:** external/live actions require real connectors or API keys. Missing connectors are reported instead of simulated.
