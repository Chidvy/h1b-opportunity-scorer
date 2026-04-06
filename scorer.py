import pandas as pd

FILE_PATH = r"C:\Users\medur\OneDrive\Apps\Desktop\LCA_Disclosure_Data_FY2025_Q4.xlsx"

print("Loading full dataset... (~2 mins)")
df = pd.read_excel(FILE_PATH, engine='openpyxl')

# Keep H-1B only
df = df[df['VISA_CLASS'] == 'H-1B'].copy()
print(f"H-1B records: {len(df)}")

# Normalize wages to annual
def to_annual(row):
    wage = row['WAGE_RATE_OF_PAY_FROM']
    unit = str(row['WAGE_UNIT_OF_PAY']).strip().lower()
    if unit == 'hour':
        return wage * 2080
    elif unit == 'week':
        return wage * 52
    elif unit == 'bi-weekly':
        return wage * 26
    elif unit == 'month':
        return wage * 12
    else:
        return wage  # already annual

df['WAGE_ANNUAL'] = df.apply(to_annual, axis=1)

def to_annual_pw(row):
    wage = row['PREVAILING_WAGE']
    unit = str(row['PW_UNIT_OF_PAY']).strip().lower()
    if unit == 'hour':
        return wage * 2080
    elif unit == 'week':
        return wage * 52
    elif unit == 'bi-weekly':
        return wage * 26
    elif unit == 'month':
        return wage * 12
    else:
        return wage

df['PW_ANNUAL'] = df.apply(to_annual_pw, axis=1)

# Wage level score
level_map = {'I': 1, 'II': 2, 'III': 3, 'IV': 4}
df['LEVEL_SCORE'] = df['PW_WAGE_LEVEL'].map(level_map).fillna(2)

# Per-employer scoring
def score_employer(group):
    total = len(group)
    certified = (group['CASE_STATUS'] == 'Certified').sum()
    cert_rate = certified / total if total > 0 else 0

    valid_wages = group[(group['WAGE_ANNUAL'] > 30000) & (group['PW_ANNUAL'] > 30000)]
    if len(valid_wages) > 0:
        wage_premium = (valid_wages['WAGE_ANNUAL'] / valid_wages['PW_ANNUAL']).mean()
        wage_premium = min(wage_premium, 2.0)  # cap at 2x
    else:
        wage_premium = 1.0

    avg_level = group['LEVEL_SCORE'].mean() / 4.0
    volume = min(total / 100, 1.0)

    score = (cert_rate * 40) + \
            ((wage_premium - 1.0) * 30) + \
            (avg_level * 20) + \
            (volume * 10)

    return pd.Series({
        'SCORE': round(score, 1),
        'CERT_RATE': round(cert_rate * 100, 1),
        'AVG_WAGE': round(valid_wages['WAGE_ANNUAL'].mean() if len(valid_wages) > 0 else 0, 0),
        'TOTAL_CASES': total,
        'AVG_LEVEL': round(group['LEVEL_SCORE'].mean(), 1)
    })

print("Scoring employers...")
employer_scores = df.groupby('EMPLOYER_NAME').apply(score_employer).reset_index()
employer_scores = employer_scores.sort_values('SCORE', ascending=False)
# Minimum 10 cases to get a score
employer_scores = employer_scores[employer_scores['TOTAL_CASES'] >= 10]

# Cap avg wage at $500k to filter data errors
employer_scores = employer_scores[employer_scores['AVG_WAGE'] <= 500000]

print("\n--- TOP 20 EMPLOYERS ---")
print(employer_scores.head(20).to_string())

print("\n--- SAMPLE SEARCH: 'amazon' ---")
result = employer_scores[employer_scores['EMPLOYER_NAME'].str.contains('AMAZON', case=False, na=False)]
print(result)

# Save for app use
employer_scores.to_csv('employer_scores.csv', index=False)
df.to_csv('lca_clean.csv', index=False)
print("\nSaved: employer_scores.csv and lca_clean.csv")