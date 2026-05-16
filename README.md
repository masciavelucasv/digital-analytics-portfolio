# Digital Analytics Portfolio — E-commerce Performance Analysis

> Built as part of a Digital Analyst job application, this project demonstrates 
> hands-on skills in e-commerce performance analysis, experimentation, and 
> data-driven insight delivery.

## Overview

This repository contains an end-to-end analysis of e-commerce campaign performance
using a dataset of 8,000 customer records across multiple advertising channels,
campaign types, and platforms. The focus is on the core KPIs relevant to digital
sales: Conversion Rate (CR), Cost Per Acquisition (CPA), and funnel drop-off.

## Key Analyses

- **CR & CPA by channel and campaign type** — identifying best and worst performing segments
- **Conversion funnel** — measuring drop-off from visits → email opens → clicks → conversions
- **A/B testing** — t-test comparing CR across top two channels with significance testing
- **Correlation matrix** — understanding relationships between spend, engagement, and conversion
- **Loyalty segmentation** — impact of loyalty points and repeat purchases on CR and CPA

## Tech Stack

- Python (pandas, NumPy, matplotlib, seaborn, scipy)
- Jupyter Notebook / VS Code
- Git & GitHub

## How to Run

```bash
git clone https://github.com/masciavelucasv/digital-analytics-portfolio.git
cd digital-analytics-portfolio
pip install -r requirements.txt
python analysis/ecommerce_analysis.py
```

## Key Findings

## Key Findings

### CR & CPA by Channel
- CR is **remarkably consistent across all channels** (10.31%–10.66%), suggesting 
  the dataset may be synthetic or that channel mix is well-optimised
- **Social Media** leads on CR (10.66%) with the lowest total spend (£7.5M)
- **Referral** drives the most conversions (1,518) but at the highest spend (£8.6M)
- CPA is broadly similar across channels (~£5,100), with **PPC slightly most efficient** (£5,088)

### CR & CPA by Campaign Type
- **Conversion campaigns** have the lowest CPA (£5,001) and most conversions (1,939) — 
  best ROI overall
- **Awareness campaigns** are the most expensive per acquisition (£5,227) — 
  expected given their top-of-funnel nature
- CR difference across campaign types is minimal (<0.2pp)

### Funnel Drop-off
- Only **38.3%** of website visitors open emails — biggest opportunity for improvement
- Email-to-click rate is **47.1%** (of openers) — reasonable engagement once opened
- Overall site-to-conversion rate is just **3.54%** — typical for e-commerce but worth optimising

### A/B Test — Referral vs PPC
- No statistically significant difference in CR (p = 0.57)
- Cannot conclude one channel outperforms the other — more data or longer test needed

### Loyalty Segmentation
- **Low loyalty customers convert at the highest rate (10.61%)** but cost the most 
  to acquire (£5,281 CPA) — likely new customers targeted via paid campaigns
- **Mid loyalty segment is most cost-efficient** (£5,063 CPA, 2,906 conversions)
- Investing in loyalty programme could shift customers from Low → Mid and reduce CPA

## Fix the FutureWarning
```python

## Author

**Luca Masciave**  
MSc Applied Economics and Data Analysis — Jönköping International Business School  
[GitHub](https://github.com/masciavelucasv) | masciavelucasv@gmail.com
