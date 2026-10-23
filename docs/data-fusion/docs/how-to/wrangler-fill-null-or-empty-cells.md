---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-fill-null-or-empty-cells/
title: Fill null or empty cells \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:22.361239+00:00
---

# Fill null or empty cells  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-fill-null-or-empty-cells/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Fill null or empty cells Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to add values to null and empty cells when you prepare data in the Wrangler workspace of the Cloud Data Fusion Studio. If you have a column that contains null or empty cells, you can specify a value to add to those cells.

To specify a value to add to null or empty cells in a column, follow these steps:

  1. [Go to Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, go to a column name and click the arrow_drop_down expander arrow.
  3. Select **Fill null or empty cells**.
  4. Enter the value to add to each null or empty cell in the column.
  5. Click **Apply**.



Wrangler fills each null or empty cell with the new value and adds the `fill-null-or-empty` directive to the recipe. When you run the data pipeline, the transformation is applied to all values in the column.

For example, in a column called `Age`, you replace the empty and null values with the string `N/A`using the preceding steps. Wrangler updates the sample dataset and adds the following directive to the recipe: `fill-null-or-empty :Age 'N/A'`.

## What's next

  * Learn more about [Wrangler directives](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#apply_directives).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
