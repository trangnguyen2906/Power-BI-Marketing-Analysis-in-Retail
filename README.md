# 📊 Marketing Performance and Customer Feedback Analysis of ShopEasy using Power BI
- **Tools Used:** SQL, Python, Power BI 
- **DBMS:** SQL Server

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

- Understand **why engagement and conversions are declining**

- Identify **weak points in the customer journey** and **content strategy**

- Make data-driven decisions to **improve marketing effectiveness, CVR and customer satisfaction**

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

### 📌 Data Structure & Relationships

### 🔷 1. Tables Used

The dataset includes 6 main tables:

1. `fact_customer_funnel` – Tracks customer behavior across different funnel stages  
2. `fact_customer_reviews` – Stores unprocessed customer feedback with rating and text  
3. `fact_engagement` – Captures campaign-level engagement metrics like views, clicks, likes  
4. `dim_customers` – Contains demographic details of customers  
5. `dim_products` – Includes product details like category and price  
6. `dim_geography` – Lists country and city-level geographic info


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


### 🔷 3. Data Relationships
![data modeling](https://drive.google.com/uc?export=view&id=1lygirzBWmKxOc97asVBnVOyU4dErwA-L)

---

## ⚒️ Main Process

### 1️⃣ Data Cleaning & Preprocessing

The dataset was sourced directly from SQL Server (`mkt_analysis` database), but instead of importing raw tables, **custom SQL transformations** were embedded directly in Power BI via **Power Query Advanced Editor**.

This approach allowed the data to be **cleaned, deduplicated, standardized**, and **enriched** before loading into Power BI, optimizing both performance and model clarity.


<details>
<summary>👤 <code>dim_customers</code></summary>

- Merged customer records with geographic data to enrich with `Country` and `City`.

</details>

<details>
<summary>📦 <code>dim_products</code></summary>

- Introduced a `PriceCategory` column classifying products as **Low**, **Medium**, or **High** price tiers based on business rules.

</details>

<details>
<summary>🔁 <code>fact_customer_funnel</code></summary>

- Cleaned and deduplicated user journey data using SQL `ROW_NUMBER()` and `PARTITION BY` to keep only the first valid touchpoint per combination.  
- Missing duration values were imputed using the average duration (with `AVG() OVER`).  
- Standardized funnel stage names to uppercase for consistency.

</details>

<details>
<summary>📊 <code>fact_engagement</code></summary>

- Parsed combined view/click fields into numeric columns (`Views`, `Clicks`) using SQL string functions.  
- Normalized content type labels (e.g., "Video", "Blog", "Newsletter").  
- Reformatted engagement dates to standard `yyyy-MM-dd`.

</details>

📎 **Full SQL transformation logic** is documented in [`transform_data.sql`](transform_data.sql)

<details>
<summary>🗣️ <code>fact_customer_reviews_sentiment</code></summary>

The `customer_reviews` table was **not imported directly** into Power BI. Instead, it was extracted using **Python** (`pyodbc`), then transformed to enrich sentiment features using **VADER sentiment analysis**.

#### ✅ Why VADER?

VADER (Valence Aware Dictionary and Sentiment Reasoner) is a **lexicon and rule-based sentiment analysis tool** designed for **short, informal text**, like customer reviews. It was selected for this project because:

- It works well on short, customer-generated reviews  
- It captures both **polarity** (positive/negative) and **intensity**  
- It’s **fast, interpretable**, and **does not require labeled training data**

#### Steps Performed:

- **Fetched** review data from SQL Server into a Pandas DataFrame  
- **Extended VADER's lexicon** with domain-specific terms (e.g., “top-notch”, “quick delivery”)  
- Generated: `SentimentScore` - Compound polarity score from VADER  
    - > 0.05 → Positive  
    - < -0.05 → Negative  
    - Between -0.05 and 0.05 → Neutral  
  - `SentimentCategory`: Combined logic from sentiment score and customer `Rating`  
  - `SentimentGroup`: Binned score ranges (e.g., `0.5 to 1.0`, `-0.49 to 0.0`)

📂 Transformed dataset saved as [`fact_customer_reviews_sentiment.csv`](fact_customer_reviews_sentiment.csv)  

</details>

⚙️ Full script available in [`customer_review_sentiment.py`](customer_review_sentiment.py)


![Transformed Schema](https://drive.google.com/uc?export=view&id=16nf6jIISLTwTMzbGTQ2uDuIs0_h_5b0r)

### 2️⃣ Power BI Visualization
The dashboard is divided into **four main pages**, each offering a specific business insight:

📈 **PAGE 1: Overview & Performance Summary**
- Tracks key KPIs like Conversion Rate, Views, Clicks, and Likes.

- Visualizes monthly trends and content performance.

**🔄 PAGE 2: Funnel & Product Conversion**
- Analyzes drop-off at each funnel stage.

- Breaks down product conversion rates across months.

**📣 PAGE 3: Engagement & Campaign Insights**
- Monitors campaign activity, total reach, and engagement rate.

- Shows product engagement by type (Views, Clicks, Likes).

**💬 PAGE 4: Customer Feedback & Sentiment**
- Sentiment analysis from review data, classified by score and rating.

- Highlights review distribution by sentiment, rating, and country.
  
---


## 📊 Key Insights & Visualizations  

### 1️⃣ Dashboard 1 Preview  

![Dashboard Page 1](https://drive.google.com/uc?export=view&id=1WLtF4zyPq1VRNU0bUqu10Z7gQMP7UXva)

### ✅ Conversion Rate Trend (2023–2025)

- **2023:** **Peaked above 20% in January**, followed by a steady decline through Q2–Q3. Moderate recovery began in Q4, continuing through December.

- **2024:** Started with a sharp drop in January, struggled through mid-year, then saw a modest Q4 rebound.

- **2025:** Stayed flat until Q3, then saw a significant rise in September and December, consistent with prior seasonal trends.

**🔄 Trend:** Across all 3 years, conversion rates **consistently improve in Q4 to early Q1**, suggesting a **strong seasonal uplift pattern**.

**📌 Insight:** Seasonal campaigns or year-end promotions may be driving Q4–Q1 performance gains. Mid-year dips could reflect weaker campaigns, lower audience intent, or less optimized funnels during off-peak periods.

**📌 Recommendations**:
- **Double Down on Q4–Q1 Campaigns:**
    + Allocate more budget and creative resources toward campaigns in Q4 and early Q1, where conversion performance historically peaks.
    + Launch high-intent offers, limited-time discounts, or year-end bundles to maximize ROI during this period.
- **Strengthen Funnel Optimization in Q2–Q3**
    + Audit and improve mid-year funnel stages, such as landing page experience or lead nurturing emails, to counter the recurring dip.

### 📉 Engagement Metrics Overview
**➡️ Trend:** Steady year-over-year decline in views, clicks, and likes across all three years.
  
**📌 Insight:** Audience reach and engagement have weakened, potentially due to reduced content freshness, changes in platform visibility, or customer fatigue.

**📌 Recommendations**:

- **A/B Test Content Types:** Run regular experiments on copy, visuals, and format to find optimal engagement drivers.

### 🎯 Content-Type Performance Shift

- 2023: **Top = Social Media**, followed by Blog > Video > Newsletter.

- 2024: Social and Blog close; Newsletter improves.

- 2025: Blog leads, Newsletter rises to 2nd; **Social Media drops to last.**

**📈 Trend:** From social-first to preference for longer-form content like Blog & Newsletter.

**💡 Insight:** Preference has shifted toward personalized, in-depth, and emotionally engaging content types.

**📌 Recommendations**:
- **Invest in Blog and Newsletter production** – align with emerging user preferences.

- **Optimize newsletter design and targeting** – maintain momentum and grow subscriber base.

- **Audit Social Media strategy** – low returns may indicate misaligned content or channel fatigue.

### 2️⃣ Dashboard 2 Preview 

![Dashboard Page 2](https://drive.google.com/uc?export=view&id=1pkvEPw7VFZCBaPWcERVkywa1uAy8KqzK)

### 📉 Journey Funnel Efficiency
- Click-through rate (CTR) is relatively stable (~50%), but a high drop-off rate (~28–31%) remains a concern.

- 2023 had the best funnel performance, with highest click and purchase percentages.

### 🔍 Seasonal Product Conversion Analysis
#### ❄️ 1. Winter Products
- **🧤 Includes:** Ski Boots, Ice Skates, Hockey Stick, Football Helmet

- **🔍 Observations:**
  
    + **Ski Boots** showed excellent early traction, **100% CVR** in Jan, **40% in Aug**, but dropped sharply to **0% from Sep to Dec**, which contradicts the expected winter peak (Q4–Q1).
    
    + **Ice Skates** performed more in line with seasonal expectations, with **increasing conversions in Nov (20%) and Dec (25%).**
    
    + **Hockey Stick and Football Helmet** displayed typical cold-season behavior, peaking in Jan and Dec respectively.

- **❓ Key Marketing Question:**
  
    + Why was **no follow-up campaign for Ski Boots** maintained from Sep to Dec, despite the ongoing winter demand?
    
    + Could this be due to **promotion gaps, targeting misalignment, or inventory limitations**?

#### ☀️ 2. Summer Products
- **🏄 Includes:** Surfboard, Kayak, Swim Goggles, Cycling Helmet

- **🔍 Observations:**
  
    + **Surfboard** experienced a sharp spike in May (150%), but no activity in Jun–Jul, which are peak summer months -> **Unusual pattern.**
    
    + **Kayak and Cycling Helmet** had mild momentum in Jun–Jul, but **conversion lacked consistency.**
    
    + **Swim Goggles**, surprisingly, **recorded 0% CVR across all summer months**, despite relevance.

- **❓ Key Marketing Question:**
  
    + Were summer campaigns launched too early (May), with **no continuation into the core season**?
    
    + Was there a misalignment in budget allocation, promotion cadence, or product availability during summer?
 
#### 🧘 3. Year-Round / Wellness Products
- **Includes:** Yoga Mat, Fitness Tracker, Dumbbells, Boxing Gloves, Running Shoes

- **🔍 Observations:**

    + **Yoga Mat** aligned with expected fitness trends,  peaking in Jan (40%) and Jul (30.8%).
    
    + **Fitness Tracker** had decent engagement but was inconsistent month-to-month.
    
    + **Boxing Gloves, Dumbbells, and Running Shoes** had persistently low conversion, with many zero-CVR months, despite their evergreen relevance.

- **❓ Key Marketing Question:**
  
    + Why are year-round wellness products seeing such **inconsistent performance**?
    
    + Should the team explore **bundle strategies** (e.g. Boxing Gloves + Fitness Tracker) or **niche retargeting for wellness audiences**?

### 3️⃣ Dashboard 3 Preview  

![Dashboard Page 3](https://drive.google.com/uc?export=view&id=161VmAd9I-AlGrC9R5a4jHKWsbSdIvstP)

### 🔍 Key Observations

- **High Engagement ≠ High Conversion**:
  
   + Products like **Running Shoes** (25.7%) and **Boxing Gloves** (24.7%) captured strong attention, yet failed to convert **(CVR < 8%).** → Indicates a mid-to-bottom funnel breakdown.

- **Disjoint Between Engagement Timing & Conversion Intent** :
  
   + **Surfboard** peaked in engagement in May (28.8%) but fell just before summer peak (Jul–Aug), when CVR dropped to 0%.


### ✅ Recommendations

- **Bridge Funnel Gaps for High-Interest Products**  
     + Retarget and recover carts for products like **Running Shoes** and **Boxing Gloves** that attract but don’t convert.
       
     + Audit checkout UX and trust signals for friction points (e.g., for Swim Goggles).

- **Align Engagement with Purchase Seasonality**  
    + Extend campaigns (e.g., **Surfboard**) deeper into summer, not just in May.
      
    + For **Yoga Mat**,... sustain momentum across the year with mid-year bundles (e.g., Dumbbells or Fitness Tracker).

- **Reinstate Video-Driven Promotions in Q2–Q3**  
    + Reintroduce **video, demo, influencer** content for emotion-driven summer products like **Kayak** and **Swim Goggles**.
  
### 4️⃣ Dashboard 4 Preview  

![Dashboard Page 4](https://drive.google.com/uc?export=view&id=1x27mWlJMOdBpKRo5GAwQKVsFuMk783uu)

### 🔍 Key Observations
- **Strong Positivity, But Mid-Range Satisfaction:**
     + While positivity rate is high (61.63%), the average rating score is moderate at 3.69, suggesting many reviews are lukewarm.
     + A large number of 3-star reviews (290) and 4-star reviews (431) imply room for experience upgrades.
- **High Rate of Conflict or Negative Feedback:**
     + **196 conflicted negative** and **226 negative reviews** (≈31% combined).
     + Common themes in low-rated reviews:

          _ **Product mismatch** (“color was different from what was shown”)
          
          _ **Durability issues** (e.g., “product broke after a week” for Ski Boots, Fitness Tracker)
          
          _ **Poor customer support** (e.g., “terrible customer service, would not buy again”)
        
- **Switzerland & France Show Polarization**

    + Switzerland has the lowest review volume but among the lowest satisfaction scores → potential silent churn risk.
    
    + France shows high satisfaction (avg. rating ~3.75) but with very low engagement (few total reviews), implying potential for growth with more localized outreach.

- **Spain Is a Volume Driver:**

    + Spain dominates review volume (250+ reviews) with high-range satisfaction score (~3.77).



---

## 🔎 Final Conclusion & Recommendations

### 🎯 Goal 1: Improve Marketing Effectiveness

✅ **Key Issues:**  
- Engagement metrics have declined over time, especially for Social Media.  
- Campaign timing is often misaligned with actual purchase seasons.  
- Video content, which performs well for high-emotion products, dropped significantly during summer.

🔧 **Recommendations**  
✔️ **Realign budget and campaign timing with intent**  
- Prioritize more budget and creatives in Q4–Q1 where CVR peaks historically.  
- Extend seasonal campaigns to cover full purchase windows (e.g., Surfboard from May through August).  

✔️ **Match content format to evolving user preferences**  
- Invest more in Blogs and Newsletters – which are outperforming in engagement.  
- Reinstate video/influencer content for visual-heavy products like Kayak, Swim Goggles, Surfboard.  

✔️ **Personalize and localize messaging**  
- Capitalize on markets like France and Spain with tailored outreach.  
- Use geographic-specific engagement trends to guide retargeting.


### 🎯 Goal 2: Increase Conversion Rate (CVR)

✅ **Key Issues:**  
- Products with strong engagement (e.g., Boxing Gloves, Running Shoes) fail to convert (CVR < 8%).  
- Funnel gaps exist where seasonal products lose momentum mid-campaign (e.g., Ski Boots in Sept–Dec).  
- Lack of structured retargeting and cart recovery strategies.

🔧 **Recommendations**  
✔️ **Fix engagement-to-conversion gaps**  
- Deploy retargeting and cart recovery for high-engagement, low-CVR products.  
- Audit checkout UX and trust signals (especially for Swim Goggles) for friction points.  

✔️ **Leverage smart bundling or cross-sell tactics**  
- Combine weaker converters with high-interest products (e.g., Boxing Gloves + Fitness Tracker).

✔️ **Synchronize campaigns with actual buyer behavior**  
- Avoid early campaign peaking (e.g., Surfboard in May); extend through peak seasons.

### 🎯 Goal 3: Improve Customer Satisfaction

✅ **Key Issues:**  
- High positivity rate (61.63%) but average rating is just 3.69 – lots of lukewarm feedback.  
- About 31% of reviews are negative or conflicted.  
- Recurring pain points include product mismatch, low durability, and poor support.

🔧 **Recommendations**  
✔️ **Act on product and service pain points**  
- Address mismatch and durability complaints (e.g., Ski Boots, Fitness Tracker).  
- Improve post-purchase support, especially for customers leaving 3-star reviews.

✔️ **Leverage positive feedback for user-generated contents and credibility**  
- Use high-volume, high-rating markets like Spain (250+ reviews, 3.77 avg.) for social proof and testimonials.

✔️ **Proactively reduce churn risk in silent markets**  
- Monitor countries like Switzerland with low reviews and low ratings – consider reactivation campaigns or feedback surveys.

By executing across all three goal areas, ShopEasy can build a stronger customer journey from awareness → consideration → purchase → advocacy, ultimately improving ROI and long-term satisfaction.
