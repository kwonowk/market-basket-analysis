***
# Identifying purchasing combinations
🥑 Organic Avocados and 🍌 Bananas anyone?
***

<br>

## 📖 Overview

This project utilizes Market Basket Analysis (MBA), a data mining technique for affinity analysis, to explore grocery shopping data, identifying patterns in product associations. By analyzing how frequently certain products are purchased together, we gain insights into consumer behavior, helping tailor marketing strategies more effectively.

## ❓ Key questions

**Purchase combinations**

- Which product groups are purchased together most frequently?
- How do purchasing patterns for these product groups vary at different times of the day?

**Purchase timing and frequency**
- What are the peak purchasing times during the week?
- Which products are most commonly reordered by customers?
- How frequently are products reordered on average?

**Individual product analysis**
- Which products are typically bought as standalone items?
- What are the products that customers rarely or never reorder?
- Are there products that are seldom or never purchased?

## 💾 Data

**Description** 
- Anonymized dataset containing a sample of over 3 million grocery orders from more than 200,000 users

**Source** 
- [Instacart](https://tech.instacart.com/3-million-instacart-orders-open-sourced-d40d29ead6f2)

**Size (merged)**
- 32,434,489 rows * 12 columns

**Structure**
```
data
├── aisles.csv
├── departments.csv
├── orders.csv
├── products.csv
└── order_products.csv 
```

## 🧭 Methodology

Tools highlighted with `pre-formatting` for clarity

1. Exploratory Data Analysis (EDA)
    - Utilize `pandas` for data manipulation and `matplotlib` for visualizing data trends and distributions
    - 
2. Market Basket Analysis using apriori algorithm
    - Compare the performance of different MBA algorithms using `efficient_apriori`, `mlxtend`, and `pyFIM` on a sample dataset to select the most efficient tool in terms of processing speed
    - Construct a “support-confidence” trade-off graph to visually aid the decision-making process for desired parameter setting
    - Conduct hourly analysis to explore how purchasing patterns vary throughout the day

## ⏭️ Next steps

- Create interactive data visualization with Streamlit
- Replicate the analysis using different data visualization tools
