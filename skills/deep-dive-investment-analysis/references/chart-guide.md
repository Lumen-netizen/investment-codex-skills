# Chart Guide

Choose charts and diagrams when they make the analysis easier to understand. There is no required count, minimum or fixed set of types; a text-and-table report is complete when it communicates the findings well. With incomplete data, use clear prose or a table and disclose the gap; conceptual diagrams may explain mechanisms if labeled illustrative. Do not invent probabilities or risk scores to fill a chart schema. Place each chart beside its supporting analysis. For `dcf-heatmap` and `football-field`, supply `currency` as an English currency code such as USD, CNY or HKD (default USD for compatibility); all prices must use that currency and the same valuation date. `current_price` is optional. Heatmap `prices` rows follow `growth_rates` and columns follow `wacc_rates`. Scenario `return_pct` is the stated-horizon scenario return, not discount to current intrinsic value; `probability` is optional. When showing present-value gaps, label them as valuation gaps; choose prose, a table or a valuation chart as appropriate.


The bundled `scripts/charts.py` is an optional convenience. Use another suitable chart or diagram tool when needed:

```bash
python scripts/charts.py <chart-type> <data-json-path> <output-png-path>
```

Chart types supported by this helper (not a report checklist):

- `financial-trends`: `{ "title": "...", "years": [...], "series": [{"name": "...", "values": [...], "color": "#..."}] }`
- `valuation-compare`: `{ "title": "...", "items": [{"name": "...", "value": 123, "color": "#..."}], "unit": "x" }`
- `scenario-payoff`: `{ "title": "...", "scenarios": [{"name": "...", "probability": 50, "return_pct": 15, "color": "#..."}] }`
- `risk-dashboard`: `{ "title": "...", "risks": [{"name": "...", "severity": 7}] }`
- `revenue-segments`: `{ "title": "...", "years": [...], "segments": {"Segment A": [...], "Segment B": [...]} }`
- `geo-revenue`: `{ "title": "...", "years": [...], "regions": {"US": [...], "China": [...]} }`
- `dcf-heatmap`: `{ "title": "...", "wacc_rates": [...], "growth_rates": [...], "prices": [[...]], "current_price": 175, "currency": "USD" }`
- `football-field`: `{ "title": "...", "methods": [{"name": "DCF", "low": 140, "high": 200}], "current_price": 175, "currency": "USD" }`

If `matplotlib` is missing and chart generation is required, install it only after getting any needed approval for network access.
