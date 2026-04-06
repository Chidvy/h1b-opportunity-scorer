import streamlit as st
import pandas as pd

st.set_page_config(page_title="H-1B Opportunity Scorer", page_icon="🎯", layout="wide")

@st.cache_data
def load_data():
    scores = pd.read_csv('employer_scores.csv')
    return scores

df = load_data()

st.title("🎯 H-1B Opportunity Scorer")
st.markdown("**Search any employer to see their H-1B sponsorship quality score based on DOL public data.**")
st.caption("Data source: U.S. Department of Labor LCA Disclosure Data FY2025 · 114,000+ H-1B filings")

st.divider()

search = st.text_input("🔍 Search employer name", placeholder="e.g. Amazon, Google, Deloitte...")

if search:
    results = df[df['EMPLOYER_NAME'].str.contains(search, case=False, na=False)]
    results = results.sort_values('TOTAL_CASES', ascending=False)

    if len(results) == 0:
        st.warning(f"No results found for '{search}'. Try a shorter keyword.")
    else:
        st.markdown(f"**{len(results)} employer record(s) found for '{search}'**")

        top = results.iloc[0]

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            score_color = "🟢" if top['SCORE'] >= 75 else "🟡" if top['SCORE'] >= 55 else "🔴"
            st.metric("Opportunity Score", f"{score_color} {top['SCORE']}/100")
        with col2:
            st.metric("Certification Rate", f"{top['CERT_RATE']}%")
        with col3:
            st.metric("Avg Annual Wage", f"${int(top['AVG_WAGE']):,}")
        with col4:
            st.metric("Total H-1B Filings", f"{int(top['TOTAL_CASES']):,}")

        level_map = {1: "Level I (Entry)", 2: "Level II (Qualified)",
                     3: "Level III (Experienced)", 4: "Level IV (Senior)"}
        avg_level = round(top['AVG_LEVEL'])
        st.info(f"**Typical role seniority:** {level_map.get(avg_level, 'Level II')}")

        score = top['SCORE']
        if score >= 80:
            st.success("✅ Strong sponsor — high approval rate, competitive wages, active filer.")
        elif score >= 65:
            st.warning("⚠️ Moderate sponsor — good approval rate but wages or volume may vary.")
        else:
            st.error("❌ Weaker sponsor — lower approval rate or below-market wages.")

        if len(results) > 1:
            with st.expander(f"See all {len(results)} matching entities"):
                st.dataframe(
                    results[['EMPLOYER_NAME','SCORE','CERT_RATE','AVG_WAGE','TOTAL_CASES','AVG_LEVEL']].reset_index(drop=True),
                    use_container_width=True
                )

st.divider()
st.markdown("### 🏆 Top 1000 H-1B Sponsors (min. 10 filings)")
top500 = df.sort_values('SCORE', ascending=False).head(1000)
st.dataframe(
    top1000[['EMPLOYER_NAME','SCORE','CERT_RATE','AVG_WAGE','TOTAL_CASES','AVG_LEVEL']].reset_index(drop=True),
    use_container_width=True
)

st.divider()
st.caption("Built by Chidvi Meduri · MS Business Analytics · Data sourced from dol.gov · Not affiliated with DOL")