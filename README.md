# 🎯 H-1B Sponsorship Tracker

> **Most job seekers apply to companies that sponsor H-1B visas.**
> **This tool tells you which ones are actually worth applying to.**

There's a difference.

Any company can say they sponsor H-1B visas. Public government data tells a different story — approval rates, wage levels, filing volume, how much above prevailing wage they actually pay.

**[🚀 Live App](https://h1b-sponsorship-tracker.streamlit.app)** | **[LinkedIn](https://www.linkedin.com/in/durga-c-meduri)** | Built by [Chidvi Meduri](https://github.com/Chidvy)

---

## Why This Exists

Every H-1B visa seeker faces the same blind spot when job searching:

- A company claims they sponsor visas — but what's their actual approval rate?
- Are they paying competitive wages or just clearing the DOL minimum?
- Are they sponsoring senior roles or only entry-level positions?
- Do they file 2 cases a year or 2,000?

**No existing tool — not LinkedIn, not Glassdoor, not Indeed — answers these questions with data.**

This tool does.

---

## What Makes It Different

Most H-1B resources show you a list of companies that have *ever* filed. That's not useful.

This tool scores every employer across **4 data-driven signals**:

| Signal | Weight | What It Tells You |
|--------|--------|-------------------|
| ✅ Certification Rate | 40% | Are their applications actually getting approved? |
| 💰 Wage Premium | 30% | Do they pay above what DOL says they should? |
| 📈 Wage Level | 20% | Are they hiring senior talent or entry-level only? |
| 📊 Sponsorship Volume | 10% | Are they an active, committed H-1B sponsor? |

The result: **a single score per employer, backed by 114,000+ real government filings.**

---

## What the Data Reveals

| Employer | Score | Avg Wage | Approval Rate |
|----------|-------|----------|---------------|
| Netflix | 89.1 | $441K | 100% |
| HubSpot | 86.8 | $433K | 96.9% |
| OpenAI | 85.3 | $332K | 95.7% |
| Meta | 73.2 | $217K | high volume |
| Amazon | 69.8 | $177K | 99.6% |
| Microsoft | 65.9 | $175K | 1,854 filings |
| Apple | 64.4 | $185K | needs scrutiny |
| TCS | 61.6 | $95K | high volume, low wages |
| Wipro | 61.6 | $100K | high volume, low wages |

**Score 80+** → Strong sponsor. Apply with confidence.
**Score 65–79** → Moderate. Worth evaluating, dig deeper.
**Score below 65** → Proceed carefully. Volume ≠ quality.

---

## Features

- 🔍 **Search any employer** — instant sponsorship profile
- 🏆 **Top 1000 H-1B sponsors** ranked by quality score
- 🎛️ **Filter by** minimum score, wage, filing volume, seniority
- 📋 **100% data-backed** — every score sourced from DOL public records

---

## Data Source

**U.S. Department of Labor — LCA Disclosure Data FY2025 Q4**
- 114,000+ H-1B filings analyzed
- Covers H-1B, H-1B1, and E-3 visa classes
- Updated quarterly by DOL
- Source: [dol.gov/agencies/eta/foreign-labor/performance](https://www.dol.gov/agencies/eta/foreign-labor/performance)

---

## Tech Stack

`Python` · `Pandas` · `Streamlit` · `DOL Public Data`

---

## Run Locally
```bash
git clone https://github.com/Chidvy/h1b-opportunity-scorer.git
cd h1b-opportunity-scorer
pip install -r requirements.txt
streamlit run app.py
```

---

## About the Builder

Built by **Chidvi Meduri** — MS Business Analytics, UMass Boston.
Certified in Power BI (PL-300) and AWS Cloud Practitioner.

This project was built to solve a real problem I face as an H-1B visa seeker navigating the US job market. If this helped you — star the repo and share it with someone who needs it.

**[LinkedIn](https://www.linkedin.com/in/durga-c-meduri)** · **[GitHub](https://github.com/Chidvy)**

---

*Not affiliated with the U.S. Department of Labor. All data is publicly available and updated quarterly.*
