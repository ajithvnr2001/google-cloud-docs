---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-filter-data/
title: Filter data \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:39.160462+00:00
---

# Filter data  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-filter-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Filter data Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to filter when you prepare data in the Wrangler workspace of the Cloud Data Fusion Studio. In Wrangler, you can filter rows of data in columns of any data type, except the boolean type. You keep or remove rows based on a condition that you configure.

To keep or remove rows based on a condition, follow these steps:

  1. [Go to Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, go to a column name and click the arrow_drop_down expander arrow.
  3. Select **Filter** and select an option—for example, **Keep rows** and **If value contains**.
  4. Specify the condition.
  5. Click **Apply**.



The values change based on the filter. Wrangler adds the `filter-rows-on` directive to the recipe. When you run the data pipeline, the transformation is applied to values in the column.

## Keep rows

If you choose to keep rows based on a condition, rows that don't meet the condition are removed. Only the rows that meet the condition remain in the dataset. For example, if you select **value is** and enter the condition `Customer`, Wrangler keeps rows containing the string `Customer` and removes rows with other values.

## Remove rows

If you choose to remove rows based on a condition, rows that meet the condition are removed from the dataset. For example, if you remove rows and select **value is empty** , Wrangler removes rows from the column that have empty or null values.

## Supported filter conditions

You can filter rows based on the following conditions:

Condition | Description  
---|---  
**value is empty** | Keeps or removes values with empty values.  
**value is** | Keeps or removes values with the exact specified value. For columns containing the string data type, you can choose to ignore letter case. The default is to include case in the condition.  
**value contains** | Keeps or removes values that contain the specified value.  
**value starts with** | Keeps or removes values that start with the specified value.  
**value ends with** | Keeps or removes values that end with the specified value.  
**matches regex** | Keeps or removes values that match the regular expression.  
**custom condition** | Keeps or removes values that match the custom condition.  
  
## What's next

  * Learn more about [Wrangler directives](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#apply_directives).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
