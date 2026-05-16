# -*- coding: utf-8 -*-
"""
Created on Sat May 16 17:58:03 2026

@author: masci
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# ── 0. LOAD & BASIC CHECK ───────────────────────────────────────────
df = pd.read_csv("your_file.csv")
df.columns = df.columns.str.lower().str.strip()
print(df.describe())

# ── 1. DERIVED METRICS ──────────────────────────────────────────────
df['cpa'] = df['adspend'] / df['conversion'].replace(0, np.nan)  # avoid div/0
df['cr']  = df['conversionrate'] * 100
df['ctr'] = df['clickthroughrate'] * 100

# ── 2. CR & CPA BY CHANNEL ──────────────────────────────────────────
channel = df.groupby('campaignchannel').agg(
    avg_cr   = ('cr', 'mean'),
    avg_cpa  = ('cpa', 'mean'),
    avg_ctr  = ('ctr', 'mean'),
    total_spend = ('adspend', 'sum'),
    conversions = ('conversion', 'sum')
).round(2).sort_values('avg_cr', ascending=False)

print("\n--- CR & CPA by Channel ---")
print(channel)

# ── 3. CR & CPA BY CAMPAIGN TYPE ────────────────────────────────────
campaign = df.groupby('campaigntype').agg(
    avg_cr  = ('cr', 'mean'),
    avg_cpa = ('cpa', 'mean'),
    total_spend = ('adspend', 'sum'),
    conversions = ('conversion', 'sum')
).round(2).sort_values('avg_cr', ascending=False)

print("\n--- CR & CPA by Campaign Type ---")
print(campaign)

# ── 4. FUNNEL ANALYSIS ──────────────────────────────────────────────
funnel = {
    'Website Visits':  df['websitevisits'].sum(),
    'Email Opens':     df['emailopens'].sum(),
    'Email Clicks':    df['emailclicks'].sum(),
    'Conversions':     df['conversion'].sum()
}

funnel_df = pd.Series(funnel)
funnel_pct = (funnel_df / funnel_df.iloc[0] * 100).round(2)

print("\n--- Funnel Drop-off ---")
print(pd.DataFrame({'Volume': funnel_df, 'Rate vs Top (%)': funnel_pct}))

# ── 5. VISUALISATIONS ───────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle("E-Commerce Performance Dashboard", fontsize=16, fontweight='bold')

# 5a. CR by Channel
channel['avg_cr'].sort_values().plot(kind='barh', ax=axes[0,0], color='steelblue', edgecolor='black')
axes[0,0].set_title("Avg Conversion Rate by Channel (%)")
axes[0,0].set_xlabel("CR (%)")

# 5b. CPA by Channel
channel['avg_cpa'].sort_values().plot(kind='barh', ax=axes[0,1], color='coral', edgecolor='black')
axes[0,1].set_title("Avg CPA by Channel")
axes[0,1].set_xlabel("CPA (£)")

# 5c. Funnel
axes[0,2].bar(funnel_df.index, funnel_df.values, color='steelblue', edgecolor='black')
axes[0,2].set_title("Conversion Funnel")
axes[0,2].set_ylabel("Volume")
axes[0,2].tick_params(axis='x', rotation=20)

# 5d. CR by Campaign Type
campaign['avg_cr'].sort_values().plot(kind='barh', ax=axes[1,0], color='mediumseagreen', edgecolor='black')
axes[1,0].set_title("Avg CR by Campaign Type (%)")
axes[1,0].set_xlabel("CR (%)")

# 5e. Ad Spend vs CR scatter
axes[1,1].scatter(df['adspend'], df['cr'], alpha=0.3, color='steelblue')
axes[1,1].set_title("Ad Spend vs Conversion Rate")
axes[1,1].set_xlabel("Ad Spend")
axes[1,1].set_ylabel("CR (%)")

# 5f. CR distribution
axes[1,2].hist(df['cr'], bins=30, color='mediumpurple', edgecolor='black')
axes[1,2].set_title("CR Distribution")
axes[1,2].set_xlabel("CR (%)")
axes[1,2].set_ylabel("Frequency")

plt.tight_layout()
plt.savefig("ecommerce_dashboard.png", dpi=150, bbox_inches='tight')
plt.show()

# ── 6. CORRELATION MATRIX ───────────────────────────────────────────
numeric_cols = ['adspend', 'cr', 'ctr', 'websitevisits', 'pagespervisit',
                'timeonsite', 'socialshares', 'emailopens', 'emailclicks',
                'previouspurchases', 'loyaltypoints', 'conversion']

plt.figure(figsize=(14, 10))
sns.heatmap(df[numeric_cols].corr(), annot=True, fmt=".2f",
            cmap="coolwarm", linewidths=0.5, annot_kws={"size": 8})
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig("correlation_matrix.png", dpi=150)
plt.show()

# ── 7. A/B TEST — TOP 2 CHANNELS ────────────────────────────────────
top2 = df['campaignchannel'].value_counts().head(2).index.tolist()
group_a = df[df['campaignchannel'] == top2[0]]['cr']
group_b = df[df['campaignchannel'] == top2[1]]['cr']

t_stat, p_value = stats.ttest_ind(group_a, group_b)
print(f"\n--- A/B Test: {top2[0]} vs {top2[1]} ---")
print(f"Mean CR {top2[0]}: {group_a.mean():.2f}%")
print(f"Mean CR {top2[1]}: {group_b.mean():.2f}%")
print(f"T-statistic: {t_stat:.3f} | P-value: {p_value:.4f}")
print("Significant difference ✅" if p_value < 0.05 else "No significant difference ❌")

# ── 8. LOYALTY & REPEAT PURCHASE IMPACT ─────────────────────────────
df['loyalty_segment'] = pd.cut(df['loyaltypoints'],
                                bins=[0, 1000, 3000, 5000],
                                labels=['Low', 'Mid', 'High'])

loyalty = df.groupby('loyalty_segment').agg(
    avg_cr  = ('cr', 'mean'),
    avg_cpa = ('cpa', 'mean'),
    conversions = ('conversion', 'sum')
).round(2)

print("\n--- CR & CPA by Loyalty Segment ---")
print(loyalty)