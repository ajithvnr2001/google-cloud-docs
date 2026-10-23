---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-manage-columns/
title: Rename, copy, delete, or keep columns \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:26.141927+00:00
---

# Rename, copy, delete, or keep columns  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-manage-columns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Rename, copy, delete, or keep columns Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to rename, copy, delete, or keep columns when you prepare data in the Wrangler workspace of the Cloud Data Fusion Studio.

## Rename a column

To rename a column in the Wrangler workspace, click a column name and enter a new name. Wrangler adds the `rename` directive to the recipe.

## Copy a column

To understand the impact of using a new directive on a dataset, you can copy a column into a new column with a different name and apply directives there.

To copy a column, follow these steps:

  1. [Go to Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, go to a column name and click the arrow_drop_down expander arrow.
  3. Select **Copy column** and enter a name for the new column.



Wrangler copies the column and adds the `copy` directive to the recipe.

## Delete a column

For datasets with many columns, you can improve pipeline performance and save resources by deleting unnecessary columns. With fewer columns, the pipeline run completes faster. This is especially true for pipelines that include a Joiner transformation.

To delete a column from a dataset, follow these steps:

  1. [Go to Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, go to a column name and click the arrow_drop_down expander arrow.
  3. Select **Delete column**.



Wrangler deletes the column and adds the `drop` directive to the recipe.

## Keep a column

You can keep a column in a dataset and delete all other columns.

To keep a column, follow these steps:

  1. [Go to Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, go to a column name and click the arrow_drop_down expander arrow.
  3. Select **Keep column**.



Wrangler deletes all columns in the dataset, except the one you chose, and adds the `keep` directive to the recipe.

## What's next

  * Learn more about [Wrangler directives](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#apply_directives).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
