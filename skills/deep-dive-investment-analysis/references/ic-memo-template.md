# IC Memo Master Template Reference

This template defines the exact structure for the institutional-grade IC Memo.
Follow section numbering exactly. Each section maps to a specific analytical function.

## Section 0: Cover Page

Required fields (formatted as a styled cover page, not body text):
- **Title**: `{Asset / Theme} IC Memo`
- **Ticker / Universe**: The asset identifier (e.g., NVDA, HBM, SPY)
- **Date / Time / Timezone**: `YYYY-MM-DD, HH:MM, PT`
- **Author**: `Chen Research (Investment Analyst) & Leslie (Risk Officer)`
- **Classification**: `CONFIDENTIAL — Internal Use Only`

Design: Center-aligned, use the primary navy color (#1B3A5C) for title, add a horizontal rule separator. Include a subtitle line with ticker and date.

## Section 1: Executive Decision Box

This is the most critical section — it must be scannable in 30 seconds.

### 1.1 One-line Call
Format: `【决策】: Buy / Add / Hold / Reduce / Hedge / Avoid`
One sentence maximum explaining the conviction.

### 1.2 Position Intent
Present as a compact table:

| 维度 (Dimension) | 建议 (Recommendation) |
|---|---|
| 时间范围 (Time Horizon) | 1–3w / 1–6m / 6–12m / 2–5y |
| 表达方式 (Expression) | Equity / Options / Pairs / Basket |
| 仓位规模 (Sizing) | Starter / Core / Max |
| 风险预算 (Risk Budget) | X bps or % NAV |

### 1.3 What Must Be True (论点成立的三个必要条件)
Exactly 3 claims, each as a numbered bullet with clear, testable criteria.

### 1.4 Kill Switch (止损触发条件)
Split into:
- **硬性失效 (Hard Invalidation)**: Specific price level / fundamental break / policy change
- **软性失效 (Soft Invalidation)**: Signal drift / adoption stall / spread widening

### 1.5 Investment Debate Minutes (投资辩论纪要)

This section documents the adversarial debate process between the Investment Analyst and the Risk Management Officer. It is the core differentiator of this report — it shows the reader how the final verdict was stress-tested through rigorous intellectual combat.

#### 1.5.1 Analyst's Core Thesis (分析师核心论点)
Present 3–5 numbered propositions that form the investment thesis. Each claim must be specific and testable — not vague directional statements.

Format:
- **Claim 1**: [Specific assertion with supporting evidence]
- **Claim 2**: [Specific assertion with supporting evidence]
- **Claim 3**: [Specific assertion with supporting evidence]
- (Up to 5 claims)

#### 1.5.2 RMO Challenge (风控官逐条质疑)
For each claim above, the RMO provides a specific, evidence-backed challenge. This is NOT a token exercise — each challenge should genuinely attempt to break the claim.

For each challenge, address:
- What could go wrong with this claim?
- What assumption is most fragile?
- What data or event would disprove it?
- Historical analogy where a similar thesis failed?

#### 1.5.3 Analyst Response & Concessions (分析师回应与让步)
The Analyst responds to each RMO challenge. Responses should be honest:
- **Survived**: The claim holds — explain why the RMO's concern, while valid in theory, does not apply here or is already mitigated
- **Modified**: The claim is adjusted — explain what changed and the revised version
- **Conceded**: The concern is valid and unresolvable — acknowledge it as a residual risk

#### 1.5.4 Debate Scorecard (辩论记分卡)
Present as a summary table:

| # | Analyst Claim | RMO Challenge | Outcome | Notes |
|---|---------------|---------------|---------|-------|
| 1 | [claim summary] | [challenge summary] | Survived / Modified / Abandoned | [key takeaway] |
| 2 | ... | ... | ... | ... |

#### 1.5.5 Final Ruling (最终裁定)
- **Verdict**: Buy / Pass
- **Confidence Level**: High / Medium / Low (with justification)
- **Surviving thesis**: The refined version of the investment case after debate
- **Key residual risk**: The most important concern that the debate could not fully resolve
- **What would change the verdict**: Specific conditions under which the opposite conclusion would be warranted

## Section 2: The Setup (背景设定)

### 2.1 What Happened (发生了什么)
- 1–3 bullet event headlines. If no recent events provided, use web search results.
- Focus on: "What CHANGED" — not what was said. Changes in incentives, constraints, or cost curves.

### 2.2 Why the Market Cares (市场为何关注)
- Pricing object: growth / margin / duration / risk premium / narrative fragility
- Immediate transmission: flows, vol, positioning, cross-asset linkages

### 2.3 What the Tape Says (市场技术面信号)
- Price path: T0, T+1, T+1w
- Vol/skew: IV, skew, term structure
- Flows: CTA, passive, HF de-grossing, retail

## Section 3: GRDS Lens (系统分析框架)

The analytical backbone — ensures the memo is "system-first" not "news-first."

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
What the market thinks. What is already priced. The "easy story."

### 4.2 Consensus Trap (共识陷阱)
- The narrative mistake
- What variable is being linearized that is actually non-linear?
- What is being ignored because it is hard to model?

### 4.3 Variant View (差异化观点)
1–2 paragraphs of your non-consensus claim. Why now — timing catalyst or mispricing window.

### 4.4 Alpha Source (阿尔法来源)
Pick the primary edge source:
- Information (faster / broader / higher signal)
- Interpretation (better causal model)
- Positioning (others forced / crowded)
- Time (can hold longer than the market)
- Structure (options convexity / pairs)

### 4.5 Path Dependency (路径依赖)
- "Right" milestones over time
- "Wrong" early warning signs

## Section 5: Key Output Deliverables (核心交付物)

### 5.1 Basic Outputs (基础分析)
1. Coverage sweep (news, filings, transcripts, research)
2. Fact table extraction (numbers, dates, quotes)
3. Scenario grid (base/bull/bear + sensitivities)
4. Counterarguments (steelman the bear case)

### 5.2 Advanced Outputs (高阶分析)
1. Structural break detection (per Appendix checklist)
2. Incentive reading: political theater vs. real constraints
3. Second-order expectations: who reacts to whom (Reflexivity)

## Section 6: Model of the World (核心驱动模型)

### 6.1 Value Driver Tree (价值驱动树)
- Revenue drivers
- Margin drivers
- Capital intensity
- Competitive moat / decay rate

### 6.2 Bottleneck Map (瓶颈图谱)
- What limits growth? (e.g., HBM, CoWoS, power, export controls, talent)
- Substitutes and switching costs

### 6.3 Regime Sensitivities (宏观敏感性)
- Rates / real yields
- FX exposure
- Policy sensitivity
- Risk-on / risk-off beta

## Section 7: Scenarios and Payoff Map (情景分析与收益图谱)

### 7.1 Scenario Table (情景表)
Present as a formatted table:

| 情景 (Scenario) | 概率 (Prob) | 目标价 (Target) | 回报 (Return) | 关键假设 (Key Assumptions) |
|---|---|---|---|---|
| 牛市 (Bull) | X% | $XXX | +XX% | ... |
| 基准 (Base) | X% | $XXX | +XX% | ... |
| 熊市 (Bear) | X% | $XXX | -XX% | ... |

### 7.2 Payoff Shapes (收益形态)
- Linear vs. convex payoff structure
- Left tail and right tail risk assessment

### 7.3 Probabilities (概率估计)
State confidence level and what would update the probabilities.

## Section 8: Trade Construction (交易构建)

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
List 5–10 specific, trackable variables with thresholds.

## Appendix: Structural Break Checklist (结构性变化检查清单)

5 diagnostic questions:
1. Is this a new cost curve or just a new headline? (成本曲线是否真正改变？)
2. What constraint moved: compute, power, capital, policy, time? (什么约束条件发生了变化？)
3. Does the stock price movement reflect narrative shift or emotional reaction? Is the market reacting to first-order facts or second-order fear? (股价反映的是叙事转变还是情绪反应？)
4. Who is forced to trade here? (rules, VaR, CTA, passive) (谁在被动交易？)
5. If consensus is wrong, where will it show up first? (data, orders, margins, capex) (如果共识错误，最先在哪里显现？)
