---
name: deep-dive-investment-analysis
description: "Perform institutional-grade deep-dive investment analysis and generate IC Memo reports as Word (.docx) files. Use this skill whenever the user provides a ticker, asset name, or asks for investment analysis, IC memo, buy-side research, stock deep-dive, value investing analysis, or risk assessment on any equity, ETF, or asset. Also trigger when the user mentions 'IC memo', 'investment committee', 'variant perception', 'moat analysis', 'margin of safety', 'consensus trap', or similar institutional investing terminology. The skill produces a professionally formatted Word document with charts, tables, and structured analysis following a dual-persona framework (Investment Analyst + Risk Management Officer). Buy verdicts have no page limit; depth of analysis determines length."
---

# Deep-Dive Investment Analysis Skill

Generate institutional-grade IC Memo reports as professional Word documents (.docx), with embedded charts and tables for readability. Buy verdicts have no page limit — depth of analysis determines length. Pass verdicts target ~10–15 pages.

## Overview

This skill operates a **dual-persona investment intelligence system** rooted in Deep Value Investing principles. It produces a rigorous, structured analysis through two independent personas before synthesizing a final verdict.

## Workflow

1. **Receive ticker/asset** from the user
2. **Gather data** — If the **FMP Financial Data** connector is available (check via tool_search), use it as the **primary data source** for structured financial data. Supplement with web search for news, narrative, and qualitative information. See Data Gathering section for the full priority list.
3. **Run Phase 1: Screening & Hurdle Rate** — prosecute the case against 5 institutional hurdles
4. **Run Phase 2: Decision Logic** — adversarial debate between Analyst and RMO personas
5. **Read the docx skill** at `/mnt/skills/public/docx/SKILL.md` for Word document creation best practices — do this BEFORE generating any files
6. **Run Phase 3: Output** — generate charts via `scripts/charts.py`, then build the Word document deliverable

## Critical Rules

- **Language**: The final report body MUST be in **Simplified Chinese**. Include English equivalents in parentheses after all technical terms, e.g., `自由现金流 (Free Cash Flow)`.
- **Charts Language**: ALL chart content (titles, labels, legends, axis text) MUST be in **English only**. This is critical — Chinese characters will render as garbled squares (mojibake) in matplotlib on most server environments due to missing CJK fonts. The report body uses Chinese, but every PNG chart must be purely English.
- **Page limit**: For **Buy** verdicts, there is **no page limit** — write as much as the analysis demands. Every section should be thorough and well-developed; depth of reasoning is the priority, not brevity. For **Pass** verdicts, target ~10–15 pages. In both cases, maintain high signal-to-noise ratio — more depth, not more fluff.
- **Charts**: Charts are embedded inline within their corresponding chapters (not collected separately). Buy reports: 6 required + up to 3 optional (6–9 total). Pass reports: 2 required + up to 2 conditional (2–4 total). See Chart Placement Maps in Document Generation Instructions for exact positions.
- **Dual Persona Independence**: The Analyst (The Engine) and RMO (The Brake) must form conclusions INDEPENDENTLY before the adversarial debate.
- **Second-Level Thinking**: For every piece of information, ask "So what?" and "What is priced in?"
- **Zero tolerance for speculation**: All claims must be evidence-backed.
- **Data insufficiency**: If web search returns insufficient data for a given ticker (e.g., small-cap, non-US listed, pre-IPO, or recently listed companies), do NOT fabricate analysis. Instead, clearly inform the user which data points are missing, which hurdles cannot be properly evaluated, and suggest alternative data sources or a narrower scope of analysis. A partial report with honest gaps is better than a complete report built on assumptions.

## Phase 1: Screening & Hurdle Rate

Prosecute the investment case against these 5 hurdles. For each, extract specific evidence and render a **Pass/Fail verdict**.

### Hurdle 1: Business Quality (The Moat)
- Evidence: pricing power, supply chain dominance, barriers to entry vs. peers
- Test: Is the advantage *structurally* durable, or merely cyclical?

### Hurdle 2: Financial Integrity (The Numbers)
- Evidence: multi-year ROIC trends, FCF conversion rates, balance sheet health
- Test: Is this a genuine capital compounder, or accounting-engineered earnings?

### Hurdle 3: Management Stewardship (The People)
- Evidence: capital allocation history (buybacks/dividends vs. empire building), insider ownership
- Test: Do insiders have skin in the game?

### Hurdle 4: Valuation Logic (The Price)
- Evidence: Invert price action. Compare Wall Street Consensus vs. Intrinsic Reality.
- Test: Is there a substantial Margin of Safety (Price < Value)?

### Hurdle 5: The "Kill" Criteria (Risk Control)
- Evidence: strongest bear case, regulatory headwinds, unknown unknowns
- Test: Why are smart investors selling? If downside is uncapped → automatic FAIL.

## Phase 2: Decision Logic — Adversarial Debate

Run the adversarial debate between two independent personas. This debate process must be **documented in the final report** as a dedicated chapter (see Debate Chapter below).

**Persona 1 — Senior Investment Analyst (The Engine)**:
- Profile: World-class strategist focused on superior returns via hard facts and cold logic
- Objectives: Variant Perception, Alpha Generation, Systemic Robustness
- Construct a bold, high-conviction thesis

**Persona 2 — Risk Management Officer (The Brake)**:
- Profile: Seasoned veteran using interdisciplinary wisdom and Devil's Advocate logic
- Objectives: Stress-Testing, Logical Hygiene, Pre-Mortem
- Challenge every assumption. Run a pre-mortem: "It's 3 years later and this failed. How did it die?"

**Final Verdict**: Only if the thesis SURVIVES the RMO's scrutiny → **Buy**. Otherwise → **Pass**.

### Debate Chapter Structure (required in both Buy and Pass reports)

This chapter is inserted **after the Executive Decision Box** and **before The Setup** (in Buy reports) or before the Hurdle Results (in Pass reports). It makes the adversarial reasoning process transparent to the reader.

**Section title**: `投资辩论纪要 (Investment Debate Minutes)`

The chapter must contain these 5 parts:

**Part 1 — Analyst's Thesis (分析师核心论点)**
The Analyst presents 3–5 key claims that form the investment thesis. Each claim should be a specific, testable assertion (not vague optimism). Format as numbered propositions.

**Part 2 — RMO Challenge (风控官逐条质疑)**
The RMO challenges each of the Analyst's claims with specific counterevidence, historical analogies, or logical weaknesses. For each claim, the RMO must identify: what could go wrong, what assumption is most fragile, and what data would disprove it. This is NOT a token exercise — the RMO should genuinely try to break the thesis.

**Part 3 — Analyst Response & Concessions (分析师回应与让步)**
The Analyst responds to each challenge. Some points may survive intact; others may require modification or concession. This is where intellectual honesty shows — the Analyst should explicitly acknowledge which concerns are valid and adjust the thesis accordingly. Track what changed vs. what held firm.

**Part 4 — Debate Scorecard (辩论记分卡)**
A summary table tracking the outcome of each claim through the debate process. See the Debate Formatting section below for the table format.

**Part 5 — Final Ruling (最终裁定)**
Summarize: which claims survived the stress test, which were modified, which were abandoned. State the final verdict (Buy or Pass) with the **confidence level** (High / Medium / Low) and the **key residual risk** that the debate could not fully resolve. For Buy verdicts, explain why the thesis is strong enough despite the RMO's valid concerns. For Pass verdicts, explain which specific challenges the Analyst could not adequately answer.

### Debate Formatting in the Report
- Use a **dialogue/exchange format** to make the back-and-forth readable — clearly label each speaker (投资分析师 / 风控官)
- Use color coding in tables or text: Analyst's claims in navy (#1B3A5C), RMO challenges in red (#C0392B), resolutions in green (#27AE60) or gray (#7F8C8D) for concessions
- Include a **Debate Scorecard table** summarizing the outcome:

| # | Analyst Claim | RMO Challenge | Outcome |
|---|---------------|---------------|---------|
| 1 | [claim] | [challenge] | Survived / Modified / Abandoned |
| 2 | ... | ... | ... |

## Phase 3: Output — The Deliverable

### If verdict is "Pass":
Generate an **evidence-based rebuttal report** (~10–15 pages) in docx format with the following structure:
- Cover → Executive Decision (Pass) → **Debate Minutes** → Hurdle Results & Evidence → Rebuttal Analysis → Risk Summary
- The Debate Minutes chapter is essential — it shows the reader that the bull case was genuinely considered and stress-tested before being rejected
- **Charts in Pass reports**: Charts are embedded inline within the chapter they support (not collected at the end). See the Chart Placement Map below for which charts go where. Insert each chart immediately after the paragraph that references it, followed by a caption line.

### If verdict is "Buy":
Generate the **full IC Memo** in docx format following the template in `references/ic-memo-template.md`, with the **Debate Minutes** chapter inserted between Section 1 (Executive Decision Box) and Section 2 (The Setup). There is **no page limit** — let the depth of analysis determine the length. Every section in the template should be developed thoroughly with evidence, reasoning chains, and supporting data. Key sections that typically benefit from extended treatment include the Debate Minutes, GRDS Lens (game theory and reflexivity require detailed player mapping), Alpha Protocol (variant view needs strong argumentation), Model of the World (value driver tree and bottleneck map), and Risk Ledger (unknown unknowns deserve serious exploration).

## Document Generation Instructions

Read `/mnt/skills/public/docx/SKILL.md` FIRST for docx-js best practices.

### Document Structure & Formatting
- **Paper**: US Letter (12240 × 15840 DXA), 1-inch margins
- **Font**: Dual-font — **SimSun (宋体)** for Chinese, **Times New Roman** for English/numbers. Set via `ascii` + `eastAsia` in docx-js font config. Body 12pt.
- **Colors**: Primary #1B3A5C (navy), Accent #2E75B6 (blue), Alert #C0392B (red), Success #27AE60 (green), Neutral #7F8C8D (gray)
- **Headers/Footers**: Header with "CONFIDENTIAL — Internal Use Only" + document title. Footer with page numbers.
- **Table of Contents**: Include after cover page
- **Style Hierarchy**: Cover 28pt → H1 22pt → H2 18pt → H3 14pt → Body 12pt → Caption 10pt → Table 11pt

For complete implementation code (font config, heading styles, color palette, table formatting, cover page layout, header/footer), read `references/docx-styles.md` before writing any document generation code.

### Required Charts (generate as PNG images, embed via ImageRun)

Use the bundled Python chart generator script at `scripts/charts.py` (requires matplotlib: `pip install matplotlib --break-system-packages`). Generate charts as PNG files, then embed them in the docx via `ImageRun`.

**CRITICAL — ENGLISH ONLY IN CHART DATA**: All JSON data passed to `charts.py` must use English text for titles, labels, names, and scores. Do NOT pass Chinese text. The script has a safety sanitizer that attempts to extract English from mixed text, but the correct approach is to always write chart data in English from the start. The report body is in Chinese; charts are English-only.

**Example — WRONG**: `{"name": "客户集中度 (Customer Concentration)"}` — relies on sanitizer  
**Example — RIGHT**: `{"name": "Customer Concentration"}` — clean English input

**Chart 1 — Hurdle Scorecard** (`hurdle-scorecard`): Visual Pass/Fail for all 5 hurdles with color coding.
**Chart 2 — Financial Trends** (`financial-trends`): Multi-year revenue, FCF, ROIC as line chart.
**Chart 3 — Valuation Comparison** (`valuation-compare`): Current vs. intrinsic value or peer P/E bar chart.
**Chart 4 — Scenario Payoff Map** (`scenario-payoff`): Bull/Base/Bear with probability-weighted returns.
**Chart 5 — Risk Dashboard** (`risk-dashboard`): Horizontal bar chart of risk factor severity.
**Chart 6 — Revenue Segments** (`revenue-segments`): Stacked area chart of revenue by business segment over time.
**Chart 7 — Geographic Revenue** (`geo-revenue`): Stacked bar chart of revenue by geography over time.
**Chart 8 — DCF Sensitivity** (`dcf-heatmap`): Heatmap of implied share prices across WACC × terminal growth rate.
**Chart 9 — Valuation Football Field** (`football-field`): Range bars showing valuation from multiple methodologies with current price line.

### Chart Placement Map — Buy Report (IC Memo)

Charts are embedded **inline within the chapter they support**, not collected in a separate section. Insert each chart immediately after the paragraph that discusses the relevant topic, followed by a caption line (9pt italic, gray).

| Chart | Insert In | Why Here | Required? |
|-------|-----------|----------|-----------|
| **Hurdle Scorecard** | Section 1.5 Debate Minutes — after the Debate Scorecard table (1.5.4), as a visual summary of the 5 hurdles | The debate concludes with a verdict; this chart is the visual "score card" of what passed and what failed | ✅ Required |
| **Financial Trends** | Section 6.1 Value Driver Tree — after discussing revenue/margin drivers | Directly supports the narrative on financial trajectory and capital compounding quality | ✅ Required |
| **Revenue Segments** | Section 6.1 Value Driver Tree — after Financial Trends, showing revenue composition | Reveals concentration risk and which business lines are driving growth | ✅ Required |
| **Geographic Revenue** | Section 6.1 Value Driver Tree — after Revenue Segments, if geographic data is available | Shows geographic concentration risk (e.g., China exposure). Skip if data unavailable | 🔶 Optional |
| **Football Field** | Section 4.3 Variant View — after presenting the non-consensus valuation argument | This is the strongest visual evidence for "the market is mispricing this asset" | ✅ Required |
| **Valuation Comparison** | Section 4.1 Consensus Snapshot — when comparing against peers | Shows where the asset sits relative to sector peers. Can be omitted if Football Field already covers this | 🔶 Optional |
| **Scenario Payoff** | Section 7.1 Scenario Table — immediately after the scenario table | Transforms the table into a visual that makes probability-weighted return intuitive | ✅ Required |
| **DCF Sensitivity** | Section 7.1 Scenario Table — after Scenario Payoff, if DCF model is built | Shows how sensitive the valuation is to key assumptions. Requires self-built simplified DCF | 🔶 Optional |
| **Risk Dashboard** | Section 9.1 Known Risks — after listing the risk categories | One glance at which risks are severe vs. manageable; anchors the entire risk discussion | ✅ Required |

**Summary**: Buy report = 6 required + up to 3 optional = **6–9 charts total**

### Chart Placement Map — Pass Report

Pass reports are simpler but charts should still be embedded inline, not collected at the end. The principle is: **place the chart right where it strengthens the argument for rejection**.

| Chart | Insert In | Why Here | Required? |
|-------|-----------|----------|-----------|
| **Hurdle Scorecard** | Debate Minutes — after the Debate Scorecard table | The most important visual in a Pass report: instantly shows which hurdles failed and why the thesis was rejected | ✅ Required |
| **Risk Dashboard** | Risk Summary — at the beginning of the section | Reinforces the conclusion that risk outweighs reward | ✅ Required |
| **Financial Trends** | Hurdle Results & Evidence — when discussing Hurdle 2 (Financial Integrity) | If rejection is partly due to deteriorating financials (FCF decline, ROIC erosion), this chart directly supports that argument. Skip if financials were not a factor | 🔶 Conditional |
| **Valuation Comparison** | Rebuttal Analysis — when arguing against the bull case valuation | If rejection is partly due to overvaluation (Hurdle 4 failed), show the data. Skip if valuation was not the issue | 🔶 Conditional |

**Summary**: Pass report = 2 required + up to 2 conditional = **2–4 charts total**

**Conditional chart rule**: Include a conditional chart only if the corresponding hurdle was a factor in the Pass decision. The chart's caption should explicitly reference which hurdle it relates to.

### Chart Generation Pattern
```bash
# 1. Create a JSON data file — ALL TEXT IN ENGLISH
echo '{"title":"Investment Hurdle Scorecard","hurdles":[{"name":"Business Quality (Moat)","verdict":"Pass","score":"Strong"}]}' > data.json
# 2. Run the chart generator
python3 scripts/charts.py hurdle-scorecard data.json hurdle_chart.png
```

Each chart type expects specific JSON data structures (all strings in English):
- `hurdle-scorecard`: `{ hurdles: [{ name, verdict: "Pass"|"Fail", score }], title }`
- `financial-trends`: `{ years: [...], series: [{ name, values, color }], title }`
- `valuation-compare`: `{ items: [{ name, value, color }], title, unit }`
- `scenario-payoff`: `{ scenarios: [{ name, probability, return_pct, color }], title }`
- `risk-dashboard`: `{ risks: [{ name, severity (1-10) }], title }`
- `revenue-segments`: `{ years: [...], segments: { "Segment A": [...], ... }, title }`
- `geo-revenue`: `{ years: [...], regions: { "US": [...], "China": [...], ... }, title }`
- `dcf-heatmap`: `{ wacc_rates: [...], growth_rates: [...], prices: [[...]], current_price: 175, title }`
- `football-field`: `{ methods: [{ name, low, high }], current_price: 175, title }`

Then embed in docx (use width 600 for full-width charts):
```javascript
new Paragraph({
  children: [new ImageRun({
    type: "png",
    data: fs.readFileSync("hurdle_chart.png"),
    transformation: { width: 600, height: 320 },
    altText: { title: "Chart Title", description: "Chart description", name: "chart" }
  })]
})
```

### Table Formatting
Color-coded tables: navy header (#1B3A5C, white text), alternating white/#F5F5F5 rows, Pass cells #E8F5E9, Fail cells #FFEBEE, border #CCCCCC 1pt. See `references/docx-styles.md` for code.

### Content Depth Guide — Buy Verdict (no page limit)

Each section should be written to the depth the analysis demands. The table below provides **minimum** depth guidance, not maximums.

| Section | Min. Pages | Depth Guidance |
|---------|-----------|----------------|
| Cover + TOC | 1–2 | Standard |
| Executive Decision Box | 1–2 | Position sizing rationale must be specific and quantified |
| **Debate Minutes** | **3–5+** | **The adversarial exchange is a core differentiator of this report. Each of the Analyst's 3–5 claims must be challenged, responded to, and resolved. Include the Debate Scorecard table. Do not shortchange this section.** |
| The Setup | 2–4 | Every recent catalyst explained with "what changed" analysis; tape reading with specific data |
| GRDS Lens | 4–6+ | This is the analytical backbone — each of the 4 sub-sections (Game Theory, Reflexivity, Dynamics, Systems) deserves its own thorough treatment with player mapping, feedback loops, and dependency chains |
| Alpha Protocol | 3–5+ | Consensus trap must be precisely identified; variant view must be argued with evidence, not assertion; path dependency should include concrete milestones |
| Key Deliverables | 2–4 | Full fact table, detailed scenario grid with sensitivities, steelman counterarguments |
| Model of the World | 3–5+ | Value driver tree with quantified breakdown; bottleneck map with substitution analysis; regime sensitivities with historical context |
| Scenarios & Payoff | 2–4 | Each scenario (Bull/Base/Bear) deserves a paragraph of assumptions, not just a table row; payoff shape analysis with convexity discussion |
| Trade Construction | 1–3 | Specific entry/add/stop/profit rules; hedging rationale; event calendar with dates |
| Risk Ledger | 3–5+ | Known risks categorized and quantified; unknown unknowns explored seriously (not token gestures); monitoring dashboard with specific thresholds and data sources |
| Appendix | 1–2 | Structural break checklist answered for this specific asset |
| **Minimum Total** | **~28+** | **Write until the analysis is complete, not until a page count is hit. Charts are embedded inline within their chapters (not a separate section), adding ~3–5 pages distributed across the report.** |

### Page Budget — Pass Verdict (~15 pages)
| Section | Pages |
|---------|-------|
| Cover + TOC | 1–2 |
| Executive Decision (Pass) | 1 |
| **Debate Minutes** (includes Hurdle Scorecard chart inline) | **2–3** |
| Hurdle Results & Evidence (may include Financial Trends chart inline) | 3–4 |
| Rebuttal Analysis (may include Valuation Compare chart inline) | 2–3 |
| Risk Summary (includes Risk Dashboard chart inline) | 2–3 |
| **Total** | **~10–15** |

## Data Gathering

**Data source priority**: If the **FMP Financial Data** connector is available, always use it first for structured financial data — it returns clean, numeric data that is directly usable for charts and analysis. Use web search to supplement with news, narrative context, and qualitative information that FMP does not cover.

### Priority 1 — FMP Financial Data (structured, use first)

| Data Need | FMP Tool(s) | Used For |
|-----------|-------------|----------|
| Income, revenue, margins | `income-statement` | Financial Trends chart, Hurdle 2, Value Driver Tree |
| Cash flow, FCF | `cashflow-statement` | Financial Trends chart, Hurdle 2 |
| Balance sheet, debt | `balance-sheet-statement` | Hurdle 2 (balance sheet health) |
| Key ratios (ROIC, ROE, P/E, EV/EBITDA) | `key-metrics`, `metrics-ratios` | Hurdle 2, Valuation Compare chart |
| Real-time quote, 52-week range | `quote` | Football Field chart, The Setup |
| Revenue by business segment | `revenue-product-segmentation` | Revenue Segments chart |
| Revenue by geography | `revenue-geographic-segments` | Geographic Revenue chart |
| Peer companies | `peers` | Hurdle 1 (competitive comparison), Valuation |
| Analyst price targets | `price-target-consensus`, `price-target-summary` | Football Field chart, Consensus Snapshot |
| Analyst grades/ratings | `grades`, `grades-summary` | Consensus Snapshot |
| Insider trading | `latest-insider-trade`, `search-insider-trades` | Hurdle 3 (skin in the game) |
| Company profile | `profile-symbol` | Overview, industry classification |
| Earnings history | `earnings-company` | The Setup, Financial Trends |
| DCF valuation | `dcf-advanced` | DCF Heatmap baseline |
| Executive compensation | `executive-compensation` | Hurdle 3 |
| Shares float | `shares-float` | Liquidity risk |
| Historical prices | `historical-price-eod-full` | The Setup (price action) |

### Priority 2 — Web Search (narrative, news, qualitative)

Use web search for information FMP does not provide (always use the current year, not a hardcoded year):
1. Recent news and catalysts (last 30 days) — `{ticker} latest news`
2. Earnings call commentary and guidance — `{ticker} earnings call highlights`
3. Competitive landscape and strategy shifts — `{ticker} competitive landscape`
4. Regulatory developments and policy risks — `{ticker} regulatory risk`
5. Sector/industry macro trends — `{sector} industry outlook`
6. Management commentary and strategic direction — `{ticker} CEO strategy`
7. Bear case arguments — `{ticker} bear case risks`

### When FMP is not available

If FMP connector is not detected, fall back to web search for all data. Financial data quality will be lower (text-based rather than structured), and some charts (Revenue Segments, Geographic Revenue) may not be possible if granular segment data cannot be found. Note this limitation in the report.

## Quality Checklist (before finalizing)

- [ ] All content in Simplified Chinese with English technical terms in parentheses
- [ ] All chart data JSON uses English only (no Chinese text passed to charts.py)
- [ ] Charts embedded inline per Chart Placement Map: Buy = 6 required + optionals; Pass = 2 required + conditionals
- [ ] Each chart has a caption line (9pt italic, gray) explaining the key takeaway
- [ ] Pass/Fail verdicts for all 5 hurdles with specific evidence cited
- [ ] **Debate Minutes chapter** is present with all 5 parts: Analyst thesis (3–5 claims), RMO challenges, Analyst responses/concessions, Debate Scorecard table, Final Ruling with confidence level
- [ ] Debate is substantive — RMO challenges are genuine, not token; concessions are honest
- [ ] Executive Decision Box is complete (Call, Position Intent, What Must Be True, Kill Switch)
- [ ] GRDS framework: all 4 sub-sections (Game Theory, Reflexivity, Dynamics, Systems) developed in depth
- [ ] Scenarios table with Bull/Base/Bear — each scenario has a full paragraph of assumptions, not just a row
- [ ] Trade Construction with specific entry/add/stop/profit-taking rules and event calendar
- [ ] Risk Ledger with known risks categorized AND unknown unknowns seriously explored
- [ ] Monitoring dashboard lists 5–10 specific trackable variables with thresholds
- [ ] Document validates with `python scripts/office/validate.py`
- [ ] Buy verdict: every section meets minimum depth per Content Depth Guide; Pass verdict: ≤ 15 pages
