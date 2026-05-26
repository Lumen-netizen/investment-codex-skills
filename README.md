# Investment Codex Skills

Personal Codex skills for investment research workflows.

## Skills

- `investment-research-collaboration`: Human-AI investment research collaboration protocol for iterative thesis development.
- `deep-dive-investment-analysis`: Institutional-grade deep-dive investment analysis and Chinese IC Memo report generation.

## Structure

Each skill lives under `skills/<skill-name>/` and keeps the standard Codex skill layout:

- `SKILL.md`
- optional `agents/openai.yaml`
- optional `references/`
- optional `scripts/`
- optional `assets/`

## Install Locally

Copy the desired skill folder into your Codex skills directory, for example:

```powershell
Copy-Item -Recurse .\skills\deep-dive-investment-analysis $env:USERPROFILE\.codex\skills\
```
