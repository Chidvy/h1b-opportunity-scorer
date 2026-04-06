\# 🎯 H-1B Opportunity Scorer



A live data app that scores employer H-1B sponsorship quality using 114,000+ U.S. Department of Labor labor certification filings.



\*\*\[🚀 Live App](https://h1b-opportunity-scorer.streamlit.app)\*\* | Built by \[Chidvi Meduri](https://github.com/Chidvy)



\---



\## What It Does



Most job seekers applying for H-1B sponsorship have no way to evaluate whether an employer is actually a strong sponsor — until it's too late.



This tool analyzes public DOL LCA disclosure data to score every employer across four dimensions:



| Signal | Weight | What It Measures |

|--------|--------|-----------------|

| Certification Rate | 40% | % of H-1B applications approved |

| Wage Premium | 30% | How much above prevailing wage they pay |

| Wage Level | 20% | Seniority of roles (Level I–IV) |

| Hiring Volume | 10% | Scale of H-1B sponsorship activity |



\---



\## Features



\- 🔍 Search any employer by name

\- 📊 See score, certification rate, average wage, and seniority level

\- 🏆 Browse top 1000 ranked H-1B sponsors

\- 🎛️ Filter by minimum score, filings, wage, and sort by any metric



\---



\## Data Source



\- \*\*U.S. Department of Labor\*\* — LCA Disclosure Data FY2025 Q4

\- 114,000+ H-1B filings

\- Source: \[dol.gov](https://www.dol.gov/agencies/eta/foreign-labor/performance)



\---



\## Tech Stack



\- Python, Pandas

\- Streamlit

\- DOL Public Data 



\---



\## Run Locally

```bash

git clone https://github.com/Chidvy/h1b-opportunity-scorer.git

cd h1b-opportunity-scorer

pip install -r requirements.txt

streamlit run app.py

```



\---



\*Not affiliated with the U.S. Department of Labor. Data is public and updated quarterly.\*

