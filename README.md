# 🎯 H-1B Sponsorship Intelligence Tool

> **Which companies actually sponsor H-1B visas — and which ones are worth your time?**

A live data app that cuts through the noise. Search any employer and instantly see their H-1B sponsorship track record using 114,000+ real U.S. Department of Labor filings.

**[🚀 Live App](https://h1b-sponsorship-tracker.streamlit.app)**

 | Built by [Chidvi Meduri](https://github.com/Chidvy)

---

## The Problem

Every H-1B visa seeker faces the same blind spot:

- A company says they sponsor visas — but how often do they actually get approved?
- Are they paying competitive wages or just meeting the minimum?
- Are they sponsoring senior roles or only entry-level positions?
- Do they file 2 cases a year or 2,000?

Public data exists to answer all of this. Most people just don't know where to look.

---

## The Solution

This tool pulls directly from DOL's LCA disclosure database and scores every H-1B sponsoring employer on four dimensions:

| Signal | Weight | What It Tells You |
|--------|--------|-------------------|
| ✅ Certification Rate | 40% | Are their applications actually getting approved? |
| 💰 Wage Premium | 30% | Do they pay above what DOL says they should? |
| 📈 Wage Level | 20% | Are they hiring senior talent or just entry-level? |
| 📊 Sponsorship Volume | 10% | Are they an active, committed H-1B sponsor? |

**Score of 80+** = Strong sponsor. High approvals, competitive pay, active filer.
**Score of 60–79** = Moderate. Worth evaluating but dig deeper.
**Score below 60** = Proceed with caution.

---

## Features

- 🔍 **Search any employer** — see their full sponsorship profile instantly
- 🏆 **Top 1000 H-1B sponsors** ranked by sponsorship quality
- 🎛️ **Filter by** minimum score, wage, filing volume, and seniority
- 📋 **Data-backed** — every score sourced directly from DOL public records

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
This project was built to solve a real problem I face as an H-1B visa seeker navigating the US job market.

[LinkedIn](#) · [GitHub](https://github.com/Chidvy)

---

*Not affiliated with the U.S. Department of Labor. All data is publicly available and updated quarterly.*