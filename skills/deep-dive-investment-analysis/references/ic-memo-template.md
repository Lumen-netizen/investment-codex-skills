# IC Memo Master Template Reference

Use this structure for a Buy IC Memo. Preserve the main section order and numbering where applicable; omit or merge optional material that does not affect the decision and renumber cleanly. Present conclusions and evidence.

## Section 0: Cover Page

Required fields (formatted as a styled cover page, not body text):
- **Title**: `{Asset / Theme} IC Memo`
- **Ticker / Universe**: The asset identifier (e.g., NVDA, HBM, SPY)
- **Date / Time / Timezone**: `YYYY-MM-DD, HH:MM, actual timezone`
- **Author**: `Chen Research` (or the user-specified author)
- **Classification**: `CONFIDENTIAL — Internal Use Only`

Design: Center-aligned, use the primary navy color (#1B3A5C) for title, add a horizontal rule separator. Include a subtitle line with ticker and date.

## Section 1: Executive Decision Box

This is the most critical section — it must be scannable in 30 seconds.

### 1.1 One-line Call
Format: `【决策】: Buy (with Add or another position action only if requested)`
One sentence maximum explaining the conviction.

### 1.2 Position Intent
If execution or portfolio guidance is requested, present as a compact table; otherwise state only the research horizon and omit unsupported sizing or instrument recommendations:

| 维度 (Dimension) | 建议 (Recommendation) |
|---|---|
| 时间范围 (Time Horizon) | 1–3w / 1–6m / 6–12m / 2–5y |
| 表达方式 (Expression) | Equity / Options / Pairs / Basket |
| 仓位规模 (Sizing) | Starter / Core / Max |
| 风险预算 (Risk Budget) | X bps or % NAV |

### 1.3 What Must Be True (论点成立的必要条件)
List the few decisive claims with observable, testable conditions; do not force an exact count.

### 1.4 Thesis Invalidation (论点失效条件)
Split into:
- **硬性失效 (Hard Invalidation)**: Fundamental break / financing failure / policy change tied to the model; add price-based stops only when execution analysis is requested
- **软性失效 (Soft Invalidation)**: Signal drift / adoption stall / spread widening

### 1.5 Valuation and Residual Uncertainty (估值与剩余不确定性)

Summarize the current price, valuation date, conditional per-share value range, return horizon, margin of safety and most important unresolved risk. Explain briefly what would change the verdict. Support these figures in Sections 6 and 7.

## Section 2: The Setup (背景设定)

### 2.1 What Happened (发生了什么)
- 1–3 bullet event headlines. If no recent events provided, use web search results.
- Focus on: "What CHANGED" — not what was said. Changes in incentives, constraints, or cost curves.

### 2.2 Why the Market Cares (市场为何关注)
- Pricing object: growth / margin / duration / risk premium / narrative fragility
- Immediate transmission: flows, vol, positioning, cross-asset linkages

### 2.3 What the Tape Says (市场技术面信号，按需)
- Price path: T0, T+1, T+1w
- Vol/skew: IV, skew, term structure
- Flows: CTA, passive, HF de-grossing, retail

## Section 3: GRDS Lens (系统分析框架)

Use the lenses that explain the company and its industry; omit unsupported or irrelevant lenses. Connect each retained mechanism to operating drivers, duration, capital requirements or risk.

### 3.1 Game Theory (博弈论分析)
- Who are the players? (Gov, hyperscalers, suppliers, rivals, regulators)
- What are their constraints and credible threats?
- Who is forced? Who is optional?

### 3.2 Reflexivity (反身性分析)
- How does price affect behavior (capex, buybacks, regulation, adoption)?
- Where does "belief" drive spending? Where does spending validate belief?
- What feedback loop is strengthening or breaking?

### 3.3 Dynamics (动态分析)
- Rate of change: what is slow, what is accelerating?
- Time-to-impact for supply, demand, policy, capacity
- Convexity points: small change → big outcome

### 3.4 Systems (系统依赖分析)
- Map dependencies (e.g., compute → power → cooling → networking → HBM → packaging)
- Identify bottlenecks and substitution limits
- Hidden couplings (rates, FX, geopolitics, regulation)

## Section 4: Alpha Protocol (阿尔法策略)

### 4.1 Consensus Snapshot (市场共识概览)
Separate dated, sourced analyst consensus from price-implied assumptions and this research hypothesis. If analyst consensus evidence is unavailable, state that limitation. Reverse valuation may produce several feasible assumption combinations.

### 4.2 Potential Consensus Gap (可能的共识遗漏)
- Is there an evidence-supported narrative mistake?
- What variable is being linearized that is actually non-linear?
- What is being ignored because it is hard to model?

### 4.3 Variant View (差异化观点)
Explain a supported difference, its per-share value effect and falsifier. Accept that consensus is reasonable or no edge is identifiable; do not invent a contrary view. Explain the realization path and horizon when a gap exists.

### 4.4 Alpha Source (阿尔法来源)
If an edge is supported, identify its primary source; otherwise state that no identifiable edge was established:
- Information (faster / broader / higher signal)
- Interpretation (better causal model)
- Positioning (others forced / crowded)
- Time (can hold longer than the market)
- Structure (options convexity / pairs)

### 4.5 Path Dependency (路径依赖)
- "Right" milestones over time
- "Wrong" early warning signs

## Section 5: Key Findings and Evidence (核心发现与证据)

Present decision-relevant findings and source-backed facts, not a checklist of work performed. Summarize material alternative explanations and why the adopted interpretation is better supported; avoid repeating other sections.

### 5.1 Decision-Relevant Evidence (关键证据)
1. Findings supported by filings, transcripts and relevant developments
2. Material facts with dates, definitions and sources
3. Key scenario implications, referring to Section 7 for calculations
4. Counterarguments (steelman the bear case)

### 5.2 Structural Findings (结构性发现，按需)
1. Structural break detection (per Appendix checklist)
2. Incentive reading: political theater vs. real constraints
3. Second-order expectations: who reacts to whom (Reflexivity)

## Section 6: Model of the World (核心驱动模型)

### 6.1 Value Driver Tree (价值驱动树)
- Revenue drivers
- Margin drivers
- Capital intensity
- Competitive moat / decay rate

### 6.2 Valuation Method and Shareholder Bridge (估值方法与每股归属)
Explain method choice and relevant limits using the current handbook. Reconcile normalized earnings, reinvestment, competitive duration and financing to shareholder value. Show material inputs, sources, formulas, units, dates and diluted shares. Use a full EV-to-equity bridge where applicable, or the corresponding shareholder reconciliation for other methods. Use cross-checks only when they reveal a meaningful blind spot.

### 6.3 Bottleneck Map (瓶颈图谱)
- What limits growth? (e.g., HBM, CoWoS, power, export controls, talent)
- Substitutes and switching costs

### 6.4 Regime Sensitivities (宏观敏感性)
- Rates / real yields
- FX exposure
- Policy sensitivity
- Risk-on / risk-off beta

## Section 7: Scenarios and Payoff Map (情景分析与收益图谱)

### 7.1 Scenario Table (情景表)
Present coherent scenarios as a formatted table. The rows below are examples; adapt them to the company. Distinguish present value from future target price and identify the return horizon. Show the operating, investment, financing and dilution assumptions that produce each result. Include probabilities only when defensible, labeled as estimates; otherwise omit the probability column.

| 情景 (Scenario) | 每股现值与估值日 (Present Value / As-of Date) | 相对现值折价 (Discount to Value) | 关键假设 (Key Assumptions) |
|---|---|---|---|
| 上行情景 (Upside) | [币种、金额、日期] | [计算值] | [经营、资本、融资与股数假设] |
| 基准情景 (Base) | [币种、金额、日期] | [计算值] | [同口径假设] |
| 下行情景 (Downside) | [币种、金额、日期] | [计算值] | [失败损失及融资影响] |

Discount to positive present value V is `(V - current price) / V`; it is not a holding-period return. If V is zero or negative, omit the percentage and explain the absolute value gap. If quoting upside relative to price instead, label `(V - current price) / current price` separately.

When future price outcomes can be supported, add a separate table:

| 情景 (Scenario) | 未来每股目标价与日期 (Future Price / Date) | 期间分配 (Distributions) | 持有期总回报 (Holding-period Total Return) |
|---|---|---|---|
| [对应情景] | [币种、金额、日期] | [同币种现金分配及假设] | [(未来价格 + 期间分配 - 买入价) / 买入价] |

Label this simple return as before fees/taxes and without reinvestment; use an explicit cash-flow/IRR calculation when timing or reinvestment matters. State the horizon and any annualization separately. Use scenario return rather than probability-weighted expected return for individual rows. Add probabilities only when defensible. Do not infer a future target price or return directly from today's discounted value.

### 7.2 Payoff Shapes (收益形态)
- Linear vs. convex payoff structure
- Left tail and right tail risk assessment

### 7.3 Probabilities (概率估计)
If probabilities are used, explain their basis, uncertainty and update conditions. Otherwise explain the bounds of the scenario range. Analyze the dominant sensitivities and combinations that reverse the decision; a DCF heatmap is useful only when DCF is appropriate.

## Section 8: Trade Construction (交易构建，按需)

Include only when the user requests execution or portfolio guidance. Do not infer sizing from valuation alone. If omitted, retain valuation-based reconsideration conditions in the decision and monitoring sections.

### 8.1 Primary Expression (主要交易工具)
Instrument + rationale for selection

### 8.2 Hedging Logic (对冲逻辑)
- What risk is being hedged: macro, vol, factor, policy?
- Cheapest hedge vs. cleanest hedge

### 8.3 Execution Plan (执行计划)
- Entry zones (价格区间)
- Add rules (加仓规则)
- Stop rules (止损规则)
- Profit-taking rules (止盈规则)
- Event calendar (关键日期)

## Section 9: Risk Ledger (风险台账)

### 9.1 Known Risks (已知风险)
Categorize as: Fundamental / Policy / Positioning / Liquidity

### 9.2 Unknown Unknowns (未知风险 — 压力测试)
- What could invalidate the entire analytical framework?
- What is the "model blind spot"?

### 9.3 Monitoring Dashboard (监控仪表盘)
List the few decision-relevant observable facts, timeframe and model-linked thresholds. Use directional and persistence conditions when numeric thresholds lack support.

## Appendix: Structural Break Checklist (结构性变化检查清单)

Optional diagnostic prompts; include findings only when relevant:
1. Is this a new cost curve or just a new headline? (成本曲线是否真正改变？)
2. What constraint moved: compute, power, capital, policy, time? (什么约束条件发生了变化？)
3. Does the stock price movement reflect narrative shift or emotional reaction? Is the market reacting to first-order facts or second-order fear? (股价反映的是叙事转变还是情绪反应？)
4. Who is forced to trade here? (rules, VaR, CTA, passive) (谁在被动交易？)
5. If consensus is wrong, where will it show up first? (data, orders, margins, capex) (如果共识错误，最先在哪里显现？)

## Sources and Limitations

Provide traceable sources for material claims and valuation inputs, their dates and unresolved gaps. Identify the handbook version used as methodology; it does not establish current company facts.
