# dim_customer
SELECT 
	c.CustomerID
	, c.CustomerName
	, c.Email
	, c.Gender
	, c.Age
	, g.Country
	,g.City
FROM dbo.customers AS c 
LEFT JOIN dbo.geography g
	ON c.GeographyID = g.GeographyID

  
# dim_product
SELECT 
    ProductID,  
    ProductName,  
    Category,
     Price,

    CASE -- Categorizes the products into price categories: Low, Medium, or High
        WHEN Price < 50 THEN 'Low' 
        WHEN Price BETWEEN 50 AND 200 THEN 'Medium'
        ELSE 'High' 
    END AS PriceCategory  -- Names the new column as PriceCategory

FROM 
    dbo.products;

# fact_customer_funnel 
WITH CleanedData AS (
    SELECT 
        JourneyID,
        CustomerID,
        ProductID,
        VisitDate,
        UPPER(Stage) AS Stage,
        Action,
        Duration,
        AVG(Duration) OVER (PARTITION BY VisitDate) AS avg_duration,
        ROW_NUMBER() OVER (
            PARTITION BY CustomerID, ProductID, VisitDate, UPPER(Stage), Action
            ORDER BY JourneyID
        ) AS row_num
    FROM dbo.customer_journey
),


Deduplicated AS (
    SELECT *
    FROM CleanedData
    WHERE row_num = 1
)


SELECT
    JourneyID,
    CustomerID,
    ProductID,
    VisitDate,
    Stage,
    Action,
    COALESCE(Duration, ROUND(avg_duration,1)) AS Duration
FROM Deduplicated
ORDER BY JourneyID;

# fact_engagement
SELECT 
    EngagementID,
    ContentID,
	CampaignID,
    ProductID,
     CASE
    WHEN UPPER(ContentType) LIKE '%SOCIALMEDIA%' THEN 'SOCIAL MEDIA'
    WHEN UPPER(ContentType) = 'NEWSLETTER' THEN 'NEWSLETTER'
    WHEN UPPER(ContentType) = 'VIDEO' THEN 'VIDEO'
    WHEN UPPER(ContentType) = 'BLOG' THEN 'BLOG'
    ELSE UPPER(ContentType)
  END AS ContentType,
    LEFT(ViewsClicksCombined, CHARINDEX('-', ViewsClicksCombined) - 1) AS Views,
    RIGHT(ViewsClicksCombined, LEN(ViewsClicksCombined) - CHARINDEX('-', ViewsClicksCombined)) AS Clicks,
    Likes,
    -- Converts the EngagementDate to the yyyy-MM-dd format
    FORMAT(CONVERT(DATE, EngagementDate), 'yyyy-MM-dd') AS EngagementDate
FROM 
    dbo.engagement_data
