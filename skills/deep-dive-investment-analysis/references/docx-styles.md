# Document Styling Reference — docx-js Implementation

This file contains the complete code templates for font configuration, heading styles, color palette, and table formatting used in IC Memo and Pass report generation.

Read this file when building the Word document. All code examples are for the `docx` npm package (docx-js).

## Font Configuration

The report uses a dual-font specification:
- **Chinese text**: SimSun (宋体)
- **English and numbers**: Times New Roman

Word automatically switches fonts by character type using the `ascii` / `eastAsia` / `hAnsi` properties.

### Global Default Font + Heading Styles

```javascript
const doc = new Document({
  styles: {
    default: {
      document: {
        run: {
          font: {
            ascii: "Times New Roman",       // English + numbers
            eastAsia: "SimSun",             // Chinese (宋体)
            hAnsi: "Times New Roman",       // Latin extended
            cs: "Times New Roman",          // Complex scripts
          },
          size: 24,  // 12pt body text (unit: half-points)
        }
      }
    },
    paragraphStyles: [
      {
        id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: {
          size: 44, bold: true,  // 22pt
          font: { ascii: "Times New Roman", eastAsia: "SimSun", hAnsi: "Times New Roman" },
          color: "1B3A5C",
        },
        paragraph: { spacing: { before: 240, after: 240 }, outlineLevel: 0 }
      },
      {
        id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: {
          size: 36, bold: true,  // 18pt
          font: { ascii: "Times New Roman", eastAsia: "SimSun", hAnsi: "Times New Roman" },
          color: "2E75B6",
        },
        paragraph: { spacing: { before: 180, after: 180 }, outlineLevel: 1 }
      },
      {
        id: "Heading3", name: "Heading 3", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: {
          size: 28, bold: true,  // 14pt
          font: { ascii: "Times New Roman", eastAsia: "SimSun", hAnsi: "Times New Roman" },
          color: "2E75B6",
        },
        paragraph: { spacing: { before: 120, after: 120 }, outlineLevel: 2 }
      },
    ]
  },
  sections: [{ /* ... */ }]
});
```

### Inline TextRun Font Override

When creating individual TextRuns that need explicit font control (e.g., inside table cells or captions):

```javascript
// Standard body text — inherits global default, no override needed
new TextRun({ text: "自由现金流 (Free Cash Flow) 达到 $12.5B" })

// Caption text — override size and style only, font inherited
new TextRun({
  text: "图 1: 投资筛选评分卡 (Figure 1: Investment Hurdle Scorecard)",
  size: 20,      // 10pt
  italics: true,
  color: "7F8C8D",
})

// Table cell text — smaller size
new TextRun({
  text: "Content",
  size: 22,      // 11pt
})

// Bold emphasis within body text
new TextRun({
  text: "关键发现 (Key Finding)",
  bold: true,
})
```

## Style Hierarchy Summary

| Element | Font Size | Weight | Color | Notes |
|---------|----------|--------|-------|-------|
| Cover Title | 28pt (56) | Bold | #1B3A5C | Center-aligned |
| Section (H1) | 22pt (44) | Bold | #1B3A5C | `pageBreakBefore: true` |
| Subsection (H2) | 18pt (36) | Bold | #2E75B6 | |
| Sub-sub (H3) | 14pt (28) | Bold | #2E75B6 | |
| Body | 12pt (24) | Normal | #333333 | Default |
| Caption | 10pt (20) | Italic | #7F8C8D | Below charts |
| Table text | 11pt (22) | Normal | #333333 | |
| Table header | 11pt (22) | Bold | #FFFFFF | White on navy background |
| Header/Footer | 9pt (18) | Normal | #7F8C8D | |

Half-point values shown in parentheses (docx-js `size` unit).

## Color Palette

| Purpose | Hex | Usage |
|---------|-----|-------|
| Primary (Navy) | `#1B3A5C` | Section titles, cover, Analyst claims |
| Accent (Blue) | `#2E75B6` | Subsection titles, links |
| Alert (Red) | `#C0392B` | Risk/Fail indicators, RMO challenges, Kill Switch |
| Success (Green) | `#27AE60` | Pass indicators, survived claims |
| Neutral (Gray) | `#7F8C8D` | Captions, secondary text, concessions |
| Dark Text | `#333333` | Body text |
| Light Gray BG | `#F5F5F5` | Alternating table rows |
| Light Green BG | `#E8F5E9` | Pass cells in tables |
| Light Red BG | `#FFEBEE` | Fail cells in tables |

## Table Formatting

```javascript
const border = { style: BorderStyle.SINGLE, size: 1, color: "CCCCCC" };
const borders = { top: border, bottom: border, left: border, right: border };

// Header row cell
new TableCell({
  borders,
  width: { size: colWidth, type: WidthType.DXA },
  shading: { fill: "1B3A5C", type: ShadingType.CLEAR },  // Navy background
  margins: { top: 80, bottom: 80, left: 120, right: 120 },
  children: [new Paragraph({
    children: [new TextRun({
      text: "Column Header",
      bold: true,
      color: "FFFFFF",  // White text
      size: 22,         // 11pt
    })]
  })]
})

// Alternating body rows
// Even rows: no shading (white)
// Odd rows:  shading: { fill: "F5F5F5", type: ShadingType.CLEAR }

// Pass/Fail conditional cells
// Pass: shading: { fill: "E8F5E9", type: ShadingType.CLEAR }
// Fail: shading: { fill: "FFEBEE", type: ShadingType.CLEAR }
```

## Cover Page Layout

```javascript
// Cover page section — separate from body sections
{
  properties: {
    page: {
      size: { width: 12240, height: 15840 },
      margin: { top: 4320, right: 1440, bottom: 1440, left: 1440 }  // Extra top margin for centered look
    }
  },
  children: [
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { after: 200 },
      children: [new TextRun({
        text: "{ASSET} IC Memo",
        bold: true,
        size: 56,  // 28pt
        color: "1B3A5C",
        font: { ascii: "Times New Roman", eastAsia: "SimSun", hAnsi: "Times New Roman" },
      })]
    }),
    // Horizontal rule
    new Paragraph({
      border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "2E75B6", space: 1 } },
      spacing: { after: 400 },
      children: []
    }),
    // Subtitle: ticker, date, author
    new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [new TextRun({
        text: "Ticker: {TICKER}  |  Date: YYYY-MM-DD  |  Classification: CONFIDENTIAL",
        size: 22,  // 11pt
        color: "7F8C8D",
      })]
    }),
    // Author
    new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 200 },
      children: [new TextRun({
        text: "Chen Research (Investment Analyst) & Leslie (Risk Officer)",
        size: 24,  // 12pt
        color: "333333",
      })]
    }),
  ]
}
```

## Header and Footer

```javascript
headers: {
  default: new Header({
    children: [new Paragraph({
      children: [
        new TextRun({
          text: "CONFIDENTIAL — Internal Use Only",
          size: 18,  // 9pt
          color: "7F8C8D",
          font: { ascii: "Times New Roman", eastAsia: "SimSun", hAnsi: "Times New Roman" },
        }),
        new TextRun("\t"),
        new TextRun({
          text: "{ASSET} IC Memo",
          size: 18,
          color: "7F8C8D",
        }),
      ],
      tabStops: [{ type: TabStopType.RIGHT, position: TabStopPosition.MAX }],
    })]
  })
},
footers: {
  default: new Footer({
    children: [new Paragraph({
      alignment: AlignmentType.CENTER,
      children: [
        new TextRun({ text: "Page ", size: 18, color: "7F8C8D" }),
        new TextRun({ children: [PageNumber.CURRENT], size: 18, color: "7F8C8D" }),
      ]
    })]
  })
}
```
