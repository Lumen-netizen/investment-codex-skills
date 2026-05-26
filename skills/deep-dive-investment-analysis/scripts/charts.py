#!/usr/bin/env python3
"""
Chart Generation Utilities for IC Memo Reports

Usage: python3 charts.py <chartType> <dataJsonPath> <outputPngPath>

Chart Types:
  hurdle-scorecard  — Pass/Fail scorecard for 5 hurdles
  financial-trends  — Multi-year line/bar chart for revenue, FCF, ROIC
  valuation-compare — Bar chart comparing current vs intrinsic value or peer P/E
  scenario-payoff   — Scenario payoff map (bull/base/bear)
  risk-dashboard    — Horizontal bar chart of risk factors

IMPORTANT: All chart text (titles, labels, legends, axis) MUST be in English.
Chinese characters will render as garbled squares due to missing CJK fonts.
The Word document body handles Chinese text; charts are English-only.

The sanitize_text() function auto-extracts English from mixed input, but callers
should always provide English text in the JSON data to begin with.
"""

import json
import sys
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ─── Color Palette ───
COLORS = {
    'navy':      '#1B3A5C',
    'blue':      '#2E75B6',
    'red':       '#C0392B',
    'green':     '#27AE60',
    'gray':      '#7F8C8D',
    'lightGray': '#F5F5F5',
    'white':     '#FFFFFF',
    'darkText':  '#333333',
    'lightRed':  '#FFEBEE',
    'lightGreen':'#E8F5E9',
    'orange':    '#E67E22',
    'yellow':    '#F1C40F',
}

# ─── Font Size Constants (tuned for Word embedding at ~580px width) ───
FONT = {
    'title':       22,   # Chart main title
    'axis_label':  14,   # X/Y axis titles like "Expected Return (%)"
    'tick_label':  14,   # Tick labels on axes / row labels
    'bar_text':    14,   # Text on or near bars (verdict, score, return %)
    'annotation':  11,   # Data point annotations on line charts
    'legend':      12,   # Legend text
    'value_label': 14,   # Value labels on bar tops
}

DPI = 180  # Higher DPI for crisp rendering when embedded in Word

plt.rcParams['font.family'] = ['DejaVu Sans', 'sans-serif']
plt.rcParams['axes.unicode_minus'] = False


# ─── CJK Sanitizer ───

# Regex to detect any CJK character (CJK Unified, Extension A/B, Compatibility, etc.)
_CJK_RE = re.compile(
    r'[\u4e00-\u9fff'        # CJK Unified Ideographs
    r'\u3400-\u4dbf'          # CJK Extension A
    r'\U00020000-\U0002a6df'  # CJK Extension B
    r'\u3000-\u303f'          # CJK Symbols and Punctuation
    r'\uff00-\uffef'          # Fullwidth Forms
    r'\u2e80-\u2eff'          # CJK Radicals Supplement
    r'\u3100-\u312f'          # Bopomofo
    r'\u31a0-\u31bf'          # Bopomofo Extended
    r']'
)


def sanitize_text(text):
    """
    Remove CJK characters from text to prevent mojibake in charts.
    
    Extraction priority:
      1. Parenthesized English: "中文 (English Text)" → "English Text"
      2. ASCII fragments: "AI资本开支Slowdown" → "AI Slowdown"
      3. Pure CJK with no English: returns "[untranslated]" as last resort
    """
    if not text or not isinstance(text, str):
        return text or ''

    # Fast path — no CJK at all, return as-is
    if not _CJK_RE.search(text):
        return text

    # Strategy 1: Extract content inside parentheses (handles "中文 (English)" pattern)
    paren_match = re.search(r'\(([^)]+)\)', text)
    if paren_match:
        extracted = paren_match.group(1).strip()
        # Verify the extracted part is actually English (not nested Chinese)
        if not _CJK_RE.search(extracted):
            return extracted

    # Strategy 2: Collect all ASCII/Latin fragments
    ascii_parts = re.findall(r'[A-Za-z0-9$%&@#.,;:!?\-+=/\'"~_ ]+', text)
    cleaned = ' '.join(p.strip() for p in ascii_parts if p.strip())
    # Collapse multiple spaces
    cleaned = re.sub(r' {2,}', ' ', cleaned).strip()
    if cleaned and len(cleaned) >= 2:
        return cleaned

    # Strategy 3: Nothing usable — return placeholder
    return '[untranslated]'


def sanitize_data(data):
    """Recursively sanitize all string values in a data structure to remove CJK."""
    if isinstance(data, str):
        return sanitize_text(data)
    elif isinstance(data, dict):
        return {k: sanitize_data(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [sanitize_data(item) for item in data]
    return data


def verify_no_cjk(data, path="root"):
    """Debug helper: warn if CJK characters remain after sanitization."""
    if isinstance(data, str):
        if _CJK_RE.search(data):
            print(f"  WARNING: CJK still present at {path}: {repr(data[:80])}")
    elif isinstance(data, dict):
        for k, v in data.items():
            verify_no_cjk(v, f"{path}.{k}")
    elif isinstance(data, list):
        for i, v in enumerate(data):
            verify_no_cjk(v, f"{path}[{i}]")


# ─── Chart 1: Hurdle Scorecard ───

def generate_hurdle_scorecard(data, output_path):
    """Horizontal bar scorecard showing Pass/Fail for each hurdle."""
    data = sanitize_data(data)
    verify_no_cjk(data, "hurdle-scorecard")
    hurdles = data.get('hurdles', [])
    title = data.get('title', 'Investment Hurdle Scorecard')

    fig, ax = plt.subplots(figsize=(10, max(4.5, len(hurdles) * 0.9 + 1)))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    names = [h['name'] for h in hurdles]
    verdicts = [h['verdict'] for h in hurdles]
    scores_text = [h.get('score', '') for h in hurdles]
    bar_vals = [85 if v == 'Pass' else 35 for v in verdicts]
    bar_colors = [COLORS['green'] if v == 'Pass' else COLORS['red'] for v in verdicts]

    y_pos = np.arange(len(names))
    bar_max = 75  # Reserve right side for score text
    ax.barh(y_pos, [bar_max]*len(names), height=0.6, color=COLORS['lightGray'], zorder=1)
    bar_display = [bar_max * 0.95 if v == 'Pass' else bar_max * 0.40 for v in verdicts]
    ax.barh(y_pos, bar_display, height=0.6, color=bar_colors, zorder=2)

    for i, (v, s) in enumerate(zip(verdicts, scores_text)):
        ax.text(3, i, v, va='center', ha='left',
                fontsize=FONT['bar_text'], fontweight='bold', color='white', zorder=3)
        # Score text placed to the right of bar area, always visible
        ax.text(bar_max + 2, i, s, va='center', ha='left',
                fontsize=FONT['bar_text'] - 1, fontweight='bold',
                color=COLORS['green'] if v == 'Pass' else COLORS['red'], zorder=3)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=FONT['tick_label'], color=COLORS['darkText'])
    ax.invert_yaxis()
    ax.set_xlim(0, 100)
    ax.set_xticks([])
    ax.set_title(title, fontsize=FONT['title'], fontweight='bold', color=COLORS['navy'], pad=18)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(left=False)

    plt.tight_layout()
    fig.savefig(output_path, dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close(fig)


# ─── Chart 2: Financial Trends ───

def generate_financial_trends(data, output_path):
    """Multi-line chart for financial trends (revenue, FCF, ROIC, etc.)."""
    data = sanitize_data(data)
    verify_no_cjk(data, "financial-trends")
    years = data.get('years', [])
    series = data.get('series', [])
    title = data.get('title', 'Financial Trends')

    fig, ax = plt.subplots(figsize=(10, 5.5))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    for s in series:
        color = s.get('color', COLORS['blue'])
        ax.plot(years, s['values'], marker='o', markersize=7, linewidth=2.5,
                label=s['name'], color=color)
        for x, y in zip(years, s['values']):
            label = f'{y/1e9:.1f}B' if y >= 1e9 else f'{y/1e6:.0f}M' if y >= 1e6 else f'{y:.1f}'
            ax.annotate(label, (x, y), textcoords="offset points", xytext=(0, 14),
                       ha='center', fontsize=FONT['annotation'], color=color)

    ax.set_title(title, fontsize=FONT['title'], fontweight='bold', color=COLORS['navy'], pad=18)
    ax.legend(loc='upper left', frameon=True, framealpha=0.9, fontsize=FONT['legend'])
    ax.grid(axis='y', alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_xlabel('Year', fontsize=FONT['axis_label'], color=COLORS['gray'])
    ax.tick_params(axis='both', labelsize=FONT['tick_label'] - 1)

    plt.tight_layout()
    fig.savefig(output_path, dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close(fig)


# ─── Chart 3: Valuation Comparison ───

def generate_valuation_compare(data, output_path):
    """Vertical bar chart comparing valuation metrics across items."""
    data = sanitize_data(data)
    verify_no_cjk(data, "valuation-compare")
    items = data.get('items', [])
    title = data.get('title', 'Valuation Comparison')
    unit = data.get('unit', '')

    fig, ax = plt.subplots(figsize=(10, 5.5))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    names = [i['name'] for i in items]
    values = [i['value'] for i in items]
    colors = [i.get('color', COLORS['blue']) for i in items]

    x = np.arange(len(names))
    bars = ax.bar(x, values, width=0.6, color=colors, zorder=2)

    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(values)*0.02,
                f'{val:.1f}{unit}', ha='center', va='bottom',
                fontsize=FONT['value_label'], fontweight='bold', color=COLORS['darkText'])

    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=FONT['tick_label'], color=COLORS['darkText'])
    ax.set_title(title, fontsize=FONT['title'], fontweight='bold', color=COLORS['navy'], pad=18)
    ax.grid(axis='y', alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.set_ylim(0, max(values) * 1.25)
    ax.tick_params(axis='y', labelsize=FONT['tick_label'] - 1)

    plt.tight_layout()
    fig.savefig(output_path, dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close(fig)


# ─── Chart 4: Scenario Payoff Map ───

def generate_scenario_payoff(data, output_path):
    """Horizontal bar chart showing bull/base/bear scenario returns."""
    data = sanitize_data(data)
    verify_no_cjk(data, "scenario-payoff")
    scenarios = data.get('scenarios', [])
    title = data.get('title', 'Scenario Payoff Map')

    fig, ax = plt.subplots(figsize=(10, max(4.5, len(scenarios) * 1.4 + 1)))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    names = [f"{s['name']}\n({s.get('probability', '?')}%)" for s in scenarios]
    returns = [s['return_pct'] for s in scenarios]
    colors = [s.get('color', COLORS['green'] if s['return_pct'] >= 0 else COLORS['red']) for s in scenarios]

    y_pos = np.arange(len(names))
    bars = ax.barh(y_pos, returns, height=0.5, color=colors, zorder=2)

    for i, (bar, ret) in enumerate(zip(bars, returns)):
        sign = '+' if ret >= 0 else ''
        offset = 3 if ret >= 0 else -3
        ha = 'left' if ret >= 0 else 'right'
        ax.text(ret + offset, i, f'{sign}{ret}%', va='center', ha=ha,
                fontsize=FONT['bar_text'], fontweight='bold', color=COLORS['darkText'])

    ax.axvline(x=0, color=COLORS['gray'], linewidth=1, linestyle='--', zorder=1)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=FONT['tick_label'], color=COLORS['darkText'])
    ax.invert_yaxis()
    ax.set_title(title, fontsize=FONT['title'], fontweight='bold', color=COLORS['navy'], pad=18)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(left=False)
    ax.set_xlabel('Expected Return (%)', fontsize=FONT['axis_label'], color=COLORS['gray'])
    ax.tick_params(axis='x', labelsize=FONT['tick_label'] - 1)

    max_abs = max(abs(r) for r in returns) if returns else 50
    ax.set_xlim(-max_abs * 1.5, max_abs * 1.5)

    plt.tight_layout()
    fig.savefig(output_path, dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close(fig)


# ─── Chart 5: Risk Dashboard ───

def generate_risk_dashboard(data, output_path):
    """Horizontal bar chart of risk factors with severity coloring."""
    data = sanitize_data(data)
    verify_no_cjk(data, "risk-dashboard")
    risks = data.get('risks', [])
    title = data.get('title', 'Risk Dashboard')

    fig, ax = plt.subplots(figsize=(10, max(4.5, len(risks) * 0.65 + 1.5)))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    names = [r['name'] for r in risks]
    severities = [min(10, max(0, r['severity'])) for r in risks]

    def severity_color(s):
        if s >= 7: return COLORS['red']
        if s >= 4: return COLORS['orange']
        return COLORS['green']

    colors = [severity_color(s) for s in severities]
    y_pos = np.arange(len(names))

    ax.barh(y_pos, [10]*len(names), height=0.55, color=COLORS['lightGray'], zorder=1)
    bars = ax.barh(y_pos, severities, height=0.55, color=colors, zorder=2)

    for i, s in enumerate(severities):
        ax.text(s + 0.25, i, f'{s:.0f}/10', va='center', ha='left',
                fontsize=FONT['bar_text'], fontweight='bold', color=severity_color(s))

    ax.set_yticks(y_pos)
    ax.set_yticklabels(names, fontsize=FONT['tick_label'], color=COLORS['darkText'])
    ax.invert_yaxis()
    ax.set_xlim(0, 12.5)
    ax.set_xticks([])
    ax.set_title(title, fontsize=FONT['title'], fontweight='bold', color=COLORS['navy'], pad=18)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.tick_params(left=False)

    legend_patches = [
        mpatches.Patch(color=COLORS['green'], label='Low (1-3)'),
        mpatches.Patch(color=COLORS['orange'], label='Medium (4-6)'),
        mpatches.Patch(color=COLORS['red'], label='High (7-10)'),
    ]
    ax.legend(handles=legend_patches, loc='lower right', fontsize=FONT['legend'], frameon=True)

    plt.tight_layout()
    fig.savefig(output_path, dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close(fig)


# ─── Chart 6: Revenue Segment Stacked Area ───

def generate_revenue_segments(data, output_path):
    """Stacked area chart showing revenue breakdown by business segment over time."""
    data = sanitize_data(data)
    verify_no_cjk(data, "revenue-segments")
    years = data.get('years', [])
    segments = data.get('segments', {})
    title = data.get('title', 'Revenue by Segment — Stacked Area')

    SEGMENT_COLORS = ['#1B3A5C', '#2E75B6', '#27AE60', '#E67E22', '#C0392B', '#8E44AD', '#7F8C8D', '#F1C40F']

    fig, ax = plt.subplots(figsize=(10, 5.5))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    labels = list(segments.keys())
    values = list(segments.values())
    ax.stackplot(years, *values, labels=labels,
                 colors=SEGMENT_COLORS[:len(labels)], alpha=0.85)

    ax.set_title(title, fontsize=FONT['title'], fontweight='bold', color=COLORS['navy'], pad=18)
    ax.set_xlabel('Year', fontsize=FONT['axis_label'], color=COLORS['gray'])
    ax.set_ylabel(data.get('y_label', 'Revenue ($B)'), fontsize=FONT['axis_label'], color=COLORS['gray'])
    ax.legend(loc='upper left', fontsize=FONT['legend'], frameon=True, framealpha=0.9)
    ax.grid(axis='y', alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(axis='both', labelsize=FONT['tick_label'] - 1)

    plt.tight_layout()
    fig.savefig(output_path, dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close(fig)


# ─── Chart 7: Geographic Revenue Stacked Bar ───

def generate_geo_revenue(data, output_path):
    """Stacked bar chart showing revenue breakdown by geography over time."""
    data = sanitize_data(data)
    verify_no_cjk(data, "geo-revenue")
    years = data.get('years', [])
    regions = data.get('regions', {})
    title = data.get('title', 'Revenue by Geography — Stacked Bar')

    GEO_COLORS = ['#1B3A5C', '#2E75B6', '#27AE60', '#E67E22', '#C0392B', '#8E44AD', '#7F8C8D']

    fig, ax = plt.subplots(figsize=(10, 5.5))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    x = np.arange(len(years))
    width = 0.55
    bottom = np.zeros(len(years))

    for i, (region, vals) in enumerate(regions.items()):
        ax.bar(x, vals, width, bottom=bottom, label=region,
               color=GEO_COLORS[i % len(GEO_COLORS)], alpha=0.88)
        bottom += np.array(vals)

    # Total label on top
    for i, total in enumerate(bottom):
        unit = data.get('unit', '$')
        ax.text(i, total + max(bottom) * 0.02, f'{unit}{total:.0f}B',
                ha='center', va='bottom', fontsize=FONT['value_label'] - 1,
                fontweight='bold', color=COLORS['darkText'])

    ax.set_xticks(x)
    ax.set_xticklabels(years, fontsize=FONT['tick_label'])
    ax.set_ylabel(data.get('y_label', 'Revenue ($B)'), fontsize=FONT['axis_label'], color=COLORS['gray'])
    ax.set_title(title, fontsize=FONT['title'], fontweight='bold', color=COLORS['navy'], pad=18)
    ax.legend(loc='upper left', fontsize=FONT['legend'], frameon=True, framealpha=0.9)
    ax.grid(axis='y', alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.tick_params(axis='y', labelsize=FONT['tick_label'] - 1)

    plt.tight_layout()
    fig.savefig(output_path, dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close(fig)


# ─── Chart 8: DCF Sensitivity Heatmap ───

def generate_dcf_heatmap(data, output_path):
    """Heatmap showing implied share prices across WACC and terminal growth rate assumptions."""
    data = sanitize_data(data)
    verify_no_cjk(data, "dcf-heatmap")
    wacc_rates = data.get('wacc_rates', [])
    growth_rates = data.get('growth_rates', [])
    prices = np.array(data.get('prices', []))
    current_price = data.get('current_price', 0)
    title = data.get('title', 'DCF Sensitivity — Implied Share Price')

    from matplotlib.colors import TwoSlopeNorm

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('white')

    norm = TwoSlopeNorm(vmin=prices.min(), vcenter=current_price, vmax=prices.max())
    im = ax.imshow(prices, cmap='RdYlGn', norm=norm, aspect='auto')

    for i in range(len(growth_rates)):
        for j in range(len(wacc_rates)):
            val = prices[i, j]
            color = 'white' if abs(val - current_price) > (prices.max() - prices.min()) * 0.3 else COLORS['darkText']
            ax.text(j, i, f'${val:.0f}', ha='center', va='center',
                    fontsize=FONT['bar_text'], fontweight='bold', color=color)

    ax.set_xticks(range(len(wacc_rates)))
    ax.set_xticklabels([f'{r}%' for r in wacc_rates], fontsize=FONT['tick_label'])
    ax.set_yticks(range(len(growth_rates)))
    ax.set_yticklabels([f'{r}%' for r in growth_rates], fontsize=FONT['tick_label'])
    ax.set_xlabel(data.get('x_label', 'WACC (Discount Rate)'), fontsize=FONT['axis_label'], color=COLORS['gray'])
    ax.set_ylabel(data.get('y_label', 'Terminal Growth Rate'), fontsize=FONT['axis_label'], color=COLORS['gray'])

    display_title = f'{title} (Current: ${current_price})' if current_price else title
    ax.set_title(display_title, fontsize=FONT['title'], fontweight='bold', color=COLORS['navy'], pad=18)

    cbar = plt.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label('Implied Price ($)', fontsize=FONT['legend'])
    cbar.ax.tick_params(labelsize=FONT['legend'] - 1)

    plt.tight_layout()
    fig.savefig(output_path, dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close(fig)


# ─── Chart 9: Valuation Football Field ───

def generate_football_field(data, output_path):
    """Horizontal range bar chart showing valuation ranges from multiple methodologies."""
    data = sanitize_data(data)
    verify_no_cjk(data, "football-field")
    methods = data.get('methods', [])
    current_price = data.get('current_price', 0)
    title = data.get('title', 'Valuation Football Field')

    FF_COLORS = ['#2E75B6', '#1B3A5C', '#27AE60', '#E67E22', '#8E44AD', '#7F8C8D', '#C0392B', '#F1C40F']

    fig, ax = plt.subplots(figsize=(10, max(5, len(methods) * 0.75 + 1.5)))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')

    y_pos = np.arange(len(methods))
    all_lows = [m['low'] for m in methods]
    all_highs = [m['high'] for m in methods]
    x_min = min(all_lows) * 0.88
    x_max = max(all_highs) * 1.08
    label_offset = (x_max - x_min) * 0.02

    for i, m in enumerate(methods):
        lo, hi = m['low'], m['high']
        ax.barh(i, hi - lo, left=lo, height=0.5,
                color=FF_COLORS[i % len(FF_COLORS)], alpha=0.75, zorder=2)
        ax.text(lo - label_offset, i, f'${lo:.0f}', ha='right', va='center',
                fontsize=FONT['bar_text'] - 1, color=COLORS['darkText'])
        ax.text(hi + label_offset, i, f'${hi:.0f}', ha='left', va='center',
                fontsize=FONT['bar_text'] - 1, color=COLORS['darkText'])

    if current_price:
        ax.axvline(x=current_price, color=COLORS['red'], linewidth=2.5,
                   linestyle='--', zorder=3, label=f'Current Price ${current_price}')
        ax.legend(fontsize=FONT['legend'], loc='lower right', frameon=True)

    ax.set_yticks(y_pos)
    ax.set_yticklabels([m['name'] for m in methods], fontsize=FONT['tick_label'], color=COLORS['darkText'])
    ax.invert_yaxis()
    ax.set_xlim(x_min, x_max)
    ax.set_xlabel('Implied Share Price ($)', fontsize=FONT['axis_label'], color=COLORS['gray'])
    ax.set_title(title, fontsize=FONT['title'], fontweight='bold', color=COLORS['navy'], pad=18)
    ax.grid(axis='x', alpha=0.3)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.tick_params(left=False, axis='x', labelsize=FONT['tick_label'] - 1)

    plt.tight_layout()
    fig.savefig(output_path, dpi=DPI, bbox_inches='tight', facecolor='white')
    plt.close(fig)


# ─── Data Validation ───

REQUIRED_FIELDS = {
    'hurdle-scorecard': {'hurdles': list},
    'financial-trends': {'years': list, 'series': list},
    'valuation-compare': {'items': list},
    'scenario-payoff': {'scenarios': list},
    'risk-dashboard': {'risks': list},
    'revenue-segments': {'years': list, 'segments': dict},
    'geo-revenue': {'years': list, 'regions': dict},
    'dcf-heatmap': {'wacc_rates': list, 'growth_rates': list, 'prices': list},
    'football-field': {'methods': list},
}

ITEM_FIELDS = {
    'hurdle-scorecard': ('hurdles', ['name', 'verdict']),
    'financial-trends': ('series', ['name', 'values']),
    'valuation-compare': ('items', ['name', 'value']),
    'scenario-payoff': ('scenarios', ['name', 'return_pct']),
    'risk-dashboard': ('risks', ['name', 'severity']),
    'football-field': ('methods', ['name', 'low', 'high']),
}


def validate_data(chart_type, data):
    """Validate JSON data has required fields. Returns list of error messages."""
    errors = []
    required = REQUIRED_FIELDS.get(chart_type, {})
    for field, expected_type in required.items():
        if field not in data:
            errors.append(f"Missing required field: '{field}'")
        elif not isinstance(data[field], expected_type):
            errors.append(f"Field '{field}' should be {expected_type.__name__}, got {type(data[field]).__name__}")
        elif len(data[field]) == 0:
            errors.append(f"Field '{field}' is empty — need at least 1 item")

    # Check item-level fields
    if chart_type in ITEM_FIELDS and not errors:
        list_key, required_keys = ITEM_FIELDS[chart_type]
        items = data.get(list_key, [])
        for i, item in enumerate(items):
            for key in required_keys:
                if key not in item:
                    errors.append(f"{list_key}[{i}] missing required field: '{key}'")

    return errors


# ─── CLI Entry ───
GENERATORS = {
    'hurdle-scorecard': generate_hurdle_scorecard,
    'financial-trends': generate_financial_trends,
    'valuation-compare': generate_valuation_compare,
    'scenario-payoff': generate_scenario_payoff,
    'risk-dashboard': generate_risk_dashboard,
    'revenue-segments': generate_revenue_segments,
    'geo-revenue': generate_geo_revenue,
    'dcf-heatmap': generate_dcf_heatmap,
    'football-field': generate_football_field,
}

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Usage: python3 charts.py <chartType> <dataJsonPath> <outputPngPath>')
        print(f'Types: {", ".join(GENERATORS.keys())}')
        sys.exit(1)

    chart_type, data_path, output_path = sys.argv[1], sys.argv[2], sys.argv[3]

    if chart_type not in GENERATORS:
        print(f'ERROR: Unknown chart type: "{chart_type}"')
        print(f'Available types: {", ".join(GENERATORS.keys())}')
        sys.exit(1)

    try:
        with open(data_path, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f'ERROR: Data file not found: {data_path}')
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f'ERROR: Invalid JSON in {data_path}: {e}')
        sys.exit(1)

    # Validate data structure
    validation_errors = validate_data(chart_type, data)
    if validation_errors:
        print(f'ERROR: Invalid data for chart type "{chart_type}":')
        for err in validation_errors:
            print(f'  - {err}')
        print(f'\nExpected format for "{chart_type}":')
        expected = {
            'hurdle-scorecard': '{ "hurdles": [{"name": "...", "verdict": "Pass|Fail", "score": "..."}], "title": "..." }',
            'financial-trends': '{ "years": [...], "series": [{"name": "...", "values": [...], "color": "#..."}], "title": "..." }',
            'valuation-compare': '{ "items": [{"name": "...", "value": 123, "color": "#..."}], "title": "...", "unit": "x" }',
            'scenario-payoff': '{ "scenarios": [{"name": "...", "probability": 50, "return_pct": 15, "color": "#..."}], "title": "..." }',
            'risk-dashboard': '{ "risks": [{"name": "...", "severity": 7}], "title": "..." }',
            'revenue-segments': '{ "years": [...], "segments": {"Segment A": [...], "Segment B": [...]}, "title": "..." }',
            'geo-revenue': '{ "years": [...], "regions": {"US": [...], "China": [...]}, "title": "..." }',
            'dcf-heatmap': '{ "wacc_rates": [8,9,10], "growth_rates": [2,3,4], "prices": [[...],[...]], "current_price": 175, "title": "..." }',
            'football-field': '{ "methods": [{"name": "DCF", "low": 140, "high": 200}], "current_price": 175, "title": "..." }',
        }
        print(f'  {expected.get(chart_type, "See documentation")}')
        sys.exit(1)

    GENERATORS[chart_type](data, output_path)
    print(f'Chart saved to: {output_path}')
