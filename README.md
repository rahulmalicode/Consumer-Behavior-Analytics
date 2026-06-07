🛍️ Consumer Behavior & Shopping Analytics
### Python • PostgreSQL • Power BI • End-to-End Business Analytics Project

---

## 📌 Project Overview

A leading retail company wants to better understand its customers' shopping behavior
in order to improve sales, customer satisfaction, and long-term loyalty. The management
team has noticed changes in purchasing patterns across demographics, product categories,
and sales channels (online vs. offline).

This project analyzes the company's consumer behavior dataset to answer the overarching
business question:

> **"How can the company leverage consumer shopping data to identify trends, improve
> customer engagement, and optimize marketing and product strategies?"**

---

## 📂 Dataset

| Detail         | Info                                      |
|----------------|-------------------------------------------|
| Source         | Consumer Behavior and Shopping Habits     |
| Records        | 3,900+ rows                               |
| Format         | CSV                                       |
| Key Columns    | customer ID, age, gender, item_purchased , category, purchase_amount , location, size, color, season, review_rating, subscription_status, shipping_type, discount_applied, previous_purchases, payment_method, frequency_of_purchases, age_group, purchase_frequency_days |

---

## 🔧 Tools & Technologies

| Tool            | Purpose                                      |
|-----------------|----------------------------------------------|
| Python (pandas) | Data loading, EDA, data cleaning |
| PostgreSQL      | Advanced SQL queries & business analysis     |
| Power BI        | Interactive dashboard & data visualization   |
| Gamma           | Business presentation / report (PPT)         |


---

## 🔄 Project Workflow

```
Raw Dataset (CSV)
      │
      ▼
 Python (EDA & Cleaning)
      │
      ▼
 PostgreSQL (SQL Analysis)
      │
      ▼
 Power BI (Dashboard)
      │
      ▼
 Gamma (Report & PPT)
      │
      ▼
 Business Recommendations
```

---

## 📋 Step-by-Step Process

### Step 1 — Data Loading & EDA (Python)
- Loaded the dataset using `pandas`
- Explored shape, data types, null values, and duplicates
- Analysed distributions of age, purchase amount, category, season


### Step 2 — Data Cleaning (Python)
- Handled missing values and null entries
- Fixed incorrect data types (e.g., converting categorical columns)
- Removed duplicate records
- Standardised column names for PostgreSQL import
- Exported cleaned dataset as `customer`

### Step 3 — SQL Analysis (PostgreSQL)
- Imported cleaned dataset directly to PostgreSQL
- Wrote business-focused SQL queries covering:
  - Revenue analysis by category and channel
  - Customer segmentation (New / Returning / Loyal)
  - Discount impact on purchase amount and satisfaction
  - Highest average review rating
  - Repeat purchase behaviour analysis

### Step 4 — Dashboard (Power BI)
- Connected Power BI directly to PostgreSQL database
- Built an interactive dashboard:
  -  Revenue By age Group
  -  Sales By age Group
  -  Revenue and Sale by Category
- Added slicers , card , clustered bar chart , clustered column chart ,Donut chart

### Step 5 — Report & Presentation (Gamma)
- Created a business report summarising key findings
- Built a professional PPT with strategic recommendations
- Designed for a non-technical management audience

---

## 📊 Power BI Dashboard

<img width="1067" height="571" alt="Dashboard" src="https://github.com/user-attachments/assets/b4c60c90-12c4-4882-b84d-392f82a56fee" />

---

## 🔍 Key Findings

- Male gender contributes more than the female in total_revenue
- "Gloves" ,"Sandals","Boots","Hat","Skirt" - are the top 5 products with the highest average review rating
- Express shipping has more average purchasing amount than standard shipping
- Non subscribers adds more total_revenue than subscribers
- "Hat","Sneakers","Coat","Sweater","Pants" - 5 products have the highest percentage of purchases with discounts applied
- Segment customers into New, Returning, and Loyal



## 🏷️ Tags
`python` `sql` `postgresql` `power-bi` `data-analysis` `business-analyst`
`consumer-behavior` `eda` `data-visualization` `portfolio-project` `retail-analytics`
