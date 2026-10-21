---
url: https://docs.cloud.google.com/data-studio/use-blending-to-reaggregate-data/
title: Use blending to reaggregate data \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:50.189621+00:00
---

# Use blending to reaggregate data  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/use-blending-to-reaggregate-data/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Use blending to reaggregate data Stay organized with collections  Save and categorize content based on your preferences. 

Reaggregation is a common need in data visualization. This article will help you understand the concept of reaggregation and how to achieve it in Data Studio using data blending.

One example of reaggregation is calculating the **average of averages**. For example, say you have a table of stock price changes:

**Sector** |  **Ticker** |  **Price Change**  
---|---|---  
Tech  |  GOOG  |  +6   
Tech  |  AAPL  |  +5   
Tech  |  MSFT  |  -3   
Tech  |  NFLX  |  -1   
Energy  |  E1  |  +2   
Energy  |  E2  |  +10   
Energy  |  E3  |  -3   
Finance  |  F1  |  -6   
  
The average price change for this data is a simple [aggregation](https://docs.cloud.google.com/data-studio/aggregation).

**Average of Price Change**  
---  
**1.25**  
  
To calculate the average price change for every sector, you'd group this table by the _Sector_ dimension.

**Sector** |  **Average of Price Change**  
---|---  
Tech  |  **1.75**  
Energy  |  **3**  
Finance  |  **-6**  
  
To reaggregate this data, you'd apply another aggregation function, for example, applying average again:

**Average of Average of Price Change**  
---  
**-0.42**  
  
## **Reaggregation in Data Studio**

To reaggregate metrics in Data Studio, use [data blending](https://docs.cloud.google.com/data-studio/how-blends-work). Blending lets you work around the fact that previously aggregated fields are set to the AUTO field type. You can't change this field type, nor can you apply another aggregation function to such fields.

For example, to find the average change of stock prices per sector in Data Studio, you'd create a blend configuration that joins the same data source with itself. Use _Sector_ as the join key, and include the _Average Price Change_ metric in both the left and right data sources, as shown in the following examples:

![The Blend Data panel with the Stock Data - Sheet1 Data source blended with itself uses Sector as the join key and Price Change as the selected metric.](https://docs.cloud.google.com/static/data-studio/images/reaggregation-40-2019-10-04.png)

![1](https://docs.cloud.google.com/static/data-studio/images/1-med-11-25-2014-image.png)_Sector_ ![2](https://docs.cloud.google.com/static/data-studio/images/2-med-11-25-2014-image.png)_Average Price Change_

This blended data source lets you apply new aggregations on the previously aggregated _Price Change_ field.

### Blending disaggregates data

Blending data creates a new table from the columns that you select in the blend configuration. Metrics in the new table are treated as unaggregated numbers.

Because _Price Change_ is no longer an aggregated metric, you can now apply a new aggregation function on it. The following table shows the results of creating a new metric AVG( _Price Change_ ) with the previously aggregated numbers:

![A table chart displays the Price Change metric value -0.42.](https://docs.cloud.google.com/static/data-studio/images/reaggregation-43-2019-10-04-rge.png)

![1](https://docs.cloud.google.com/static/data-studio/images/1-med-11-25-2014-image.png)_Price Change_

This new metric reaggregates the numbers **1.75, 3** and **-6** and displays their average: **-0.42**.

## Create a ratio column using blending

Another use for blending is to create ratio metrics with already aggregated numbers. Say you want to create a ratio column that divides one metric by another.

In this example, we'll use two fields; _Clicks_ and _Impressions_ , coming from two different data sources.

**Website** |  **Clicks**  
---|---  
google.com  |  300   
facebook.com  |  400   
twitter.com  |  200   
**Website** |  **Impressions**  
---|---  
google.com  |  2000   
facebook.com  |  2500   
twitter.com  |  2000   
  
You can create a ratio column with a calculated field _Clicks/Impressions_ by blending these two data sources.

**Website** |  **Clicks** |  **Impressions** |  **Clicks / Impressions**  
---|---|---|---  
google.com  |  300  |  2000  |  0.15   
facebook.com  |  400  |  2500  |  0.16   
twitter.com  |  200  |  2000  |  0.1   
**Grand Total** |  900  |  6500  |  **0.41**  
  
All the rows of _Clicks/Impressions_ have correct information except the summary row which shows the sum of the ratio column ``**`SUM( Clicks / Impressions )`**``. This happens because _Clicks/Impressions_ is calculated for each row [0.15, 0.16, 0.1] and then the `SUM` function is applied to it. [0.15 + 0.16 + 0.1 = 0.41 ].

The correct result is **900/6500 = 0.14.** You can do this by calculating the ratio column values using the formula **`SUM( Clicks ) / SUM( Impressions )`.**

**Website** |  **Clicks** |  **Impressions** |  **SUM(Clicks) / SUM(Impressions)**  
---|---|---|---  
google.com  |  300  |  2000  |  0.15   
facebook.com  |  400  |  2500  |  0.16   
twitter.com  |  200  |  2000  |  0.1   
**Grand Total** |  900  |  6500  |  **0.14**  
  
In this case, the summary row shows **`SUM( SUM( Clicks ) / SUM( Impressions ) )`. `SUM( Clicks )`** [900] is divided by ``**`SUM( Impressions )`**`` [6500] to give **0.14.** The ``**`SUM`**`` function is then applied to it again. The result is still **0.14**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
