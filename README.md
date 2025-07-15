# 📊 Marketing Analysis in Retail using Power BI
Author: [Your Name]  
Date: YYYY-MM-DD  
Tools Used: SQL/ Power BI/ Python  

---

## 📑 Table of Contents  
1. [📌 Background & Overview](#-background--overview)  
2. [📂 Dataset Description & Data Structure](#-dataset-description--data-structure)  
3. [🧠 Design Thinking Process](#-design-thinking-process)  
4. [📊 Key Insights & Visualizations](#-key-insights--visualizations)  
5. [🔎 Final Conclusion & Recommendations](#-final-conclusion--recommendations)

---

## 📌 Background & Overview  

### 📖 What is this project about? 
 
### 🚨 Business Problem

ShopEasy, a growing online retail business, is facing a serious **drop in customer engagement and conversion rates**, despite launching several new marketing campaigns.

This project analyzes **customer behavior and marketing performance** using Power BI to help ShopEasy:

- Understand why engagement and conversions are declining

- Identify weak points in the customer journey and content strategy

- Make data-driven decisions to improve marketing effectiveness, CVR and customer satisfaction

### 🔍 Business Questions
This project helps answer critical business questions, such as:

- What’s causing the drop in conversion rates despite high traffic?

- Which content types (blog, video, social media) drive the most engagement?

- At what point in the customer journey do users drop off?


### 👥 Who is this project for?
✔️ **Marketing Team:** Refine content and improve campaign ROI

✔️ **CXP Team:** Address recurring complaints and satisfaction gaps

✔️ **BI & data analysts:** Track trends and measure performance impact

---

## 📂 Dataset Description & Data Structure  

### 📌 Data Source  
- Source: ShopEasy dataset
- Size: > 5000 rows
- Format: .csv

## 🗂️ Part 2: Data Structure & Relationships

### 🔷 1. Tables Used

The dataset includes 6 main tables:

1. `fact_customer_funnel` – Tracks customer behavior across different funnel stages  
2. `fact_customer_reviews` – Stores unprocessed customer feedback with rating and text  
3. `fact_engagement` – Captures campaign-level engagement metrics like views, clicks, likes  
4. `dim_customers` – Contains demographic details of customers  
5. `dim_products` – Includes product details like category and price  
6. `dim_geography` – Lists country and city-level geographic info

---

### 🔷 2. Table Schema & Data Snapshot

<details>
<summary>📍 <strong>fact_customer_funnel</strong></summary>

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| JourneyID   | INT       | Unique ID for each customer session |
| CustomerID  | INT       | Linked to dim_customers |
| ProductID   | INT       | Linked to dim_products |
| VisitDate   | DATE      | Date of visit |
| Stage       | TEXT      | Funnel stage (Homepage, ProductPage, Checkout) |
| Action      | TEXT      | Action taken (View, Click, Drop-off) |
| Duration    | FLOAT     | Time spent on stage (seconds) |

</details>

<details>
<summary>📝 <strong>fact_customer_reviews</strong></summary>

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| ReviewID    | INT       | Unique ID for each review |
| CustomerID  | INT       | Linked to dim_customers |
| ProductID   | INT       | Linked to dim_products |
| ReviewDate  | DATE      | Date the review was submitted |
| Rating      | INT       | Star rating (1 to 5) |
| ReviewText  | TEXT      | Raw review text from customers |

📌 *Example review texts (raw):*  
- “Average experience, nothing special.”  
- “The quality is top-notch.”  
- “Customer support was very helpful.”

</details>

<details>
<summary>👤 <strong>dim_customers</strong></summary>

| Column Name  | Data Type | Description |
|--------------|-----------|-------------|
| CustomerID   | INT       | Unique customer identifier |
| CustomerName | TEXT      | Full name |
| Email        | TEXT      | Contact email |
| Gender       | TEXT      | Gender |
| Age          | INT       | Age of customer |

</details>

<details>
<summary>📊 <strong>fact_engagement</strong></summary>

| Column Name    | Data Type | Description |
|----------------|-----------|-------------|
| EngagementID   | INT       | Unique ID per interaction |
| ContentID      | INT       | ID for the content type |
| CampaignID     | INT       | Marketing campaign identifier |
| ProductID      | INT       | Linked to dim_products |
| ContentType    | TEXT      | Format: Blog, Video, Social, etc. |
| Views          | INT       | Number of views |
| Clicks         | INT       | Number of clicks |
| Likes          | INT       | Number of likes |
| EngagementDate | DATE      | Date of engagement |

</details>

<details>
<summary>📦 <strong>dim_products</strong></summary>

| Column Name   | Data Type | Description |
|---------------|-----------|-------------|
| ProductID     | INT       | Unique product ID |
| ProductName   | TEXT      | Product title |
| Category      | TEXT      | Product category |
| Price         | FLOAT     | Price in USD |
| PriceCategory | TEXT      | Price tier (High, Medium, Low) |

</details>

<details>
<summary>🌍 <strong>dim_geography</strong></summary>

| Column Name | Data Type | Description |
|-------------|-----------|-------------|
| GeographyID | INT       | Unique region ID |
| Country     | TEXT      | Country name |
| City        | TEXT      | City name |

</details>

---

### 🔷 3. Data Relationships

  
---

#### 3️⃣ Data Relationships:  
Describe the connections between tables—e.g., one-to-many, many-to-many.  

👉🏻 Include a screenshot of Data Modeling to visualize relationships.  

---

## ⚒️ Main Process

1️⃣ Data Cleaning & Preprocessing 
2️⃣ Exploratory Data Analysis (EDA)  
3️⃣ SQL/ Python Analysis 

- In each step, show your Code

- Include query/ code execution screenshots or result samples

- Explain its purpose and its findings


4️⃣ Power BI Visualization  (applicable for PBI Projects)

---


## 📊 Key Insights & Visualizations  

### 🔍 Dashboard Preview  

#### 1️⃣ Dashboard 1 Preview  

![Page 1 – Dashboard Overview](https://drive.google.com/uc?export=view&id=1KKrXr7qWo4-fgRfQc3jvX7RpVU-RUu3G)


#### 2️⃣ Dashboard 2 Preview 

![Page 2 – Funnel & Conversion](https://drive.google.com/uc?export=view&id=1IzoFH04QadHnKLemFnQL68GzwTy3HYeQ)


#### 3️⃣ Dashboard 3 Preview  

![Page 3 – Engagement & Campaigns](https://drive.google.com/uc?export=view&id=1S9TNNJEhPVDQGWgHxAGX5S2af_tYnHsQ)

  
####  Dashboard 4 Preview  

![Page 4 – Customer Feedback & Sentiment](https://drive.google.com/uc?export=view&id=1-M3ulE4JJHozYSQ5OHwyonWuKZdlRWbB)
---

## 🔎 Final Conclusion & Recommendations  

👉🏻 Based on the insights and findings above, we would recommend the [stakeholder team] to consider the following:  

📌 Key Takeaways:  
✔️ Recommendation 1  
✔️ Recommendation 2  
✔️ Recommendation 3
