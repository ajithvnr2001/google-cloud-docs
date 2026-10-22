---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-join-and-swap-columns/
title: Join and swap two columns \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:38.823756+00:00
---

# Join and swap two columns  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-join-and-swap-columns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Join and swap two columns Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to join column values and swap column names when you prepare data in the Wrangler workspace of the Cloud Data Fusion Studio.

## Join two columns

The Wrangler workspace supports joining two columns of the same or different data types. The `JOIN` operation's output is stored in a new column containing the joined fields from both columns. Wrangler doesn't support joining columns of the boolean and bytes data types with other columns.

To join two columns, follow these steps:

  1. [Go to Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, select the checkbox by two column names.
  3. Click the arrow_drop_down expander arrow by one of the column names.
  4. Select **Join two columns** , and select an option—for example, **Custom selection**.
  5. Choose an order, delimiter, and new column name for the `JOIN` operation's output.
  6. Click **Join**.



Wrangler joins the columns and adds the `merge` directive to the recipe. When you run the data pipeline, the transformation is applied to all values in the column.

## Swap two column names

The Wrangler workspace supports swapping (or interchanging) two column names. Only the column names interchange, the values in the column rows don't change.

To swap two column names, follow these steps:

  1. [Go to Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, select the checkbox by two column names.
  3. Click the arrow_drop_down expander arrow by one of the column names.
  4. Select **Swap two column names**



Wrangler swaps the column names and adds the `swap` directive to the recipe.

## What's next

  * Learn more about [Wrangler directives](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#apply_directives).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
