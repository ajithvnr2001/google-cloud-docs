---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-find-and-replace-data/
title: Find and replace data \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:29.297079+00:00
---

# Find and replace data  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-find-and-replace-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Find and replace data Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to find and replace when you prepare data in the Wrangler workspace of the Cloud Data Fusion Studio. In Wrangler, you can find and replace values in columns of any data type.

To find and replace values in a column, follow these steps:

  1. [Go to Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, go to a column name and click the arrow_drop_down expander arrow.
  3. Select **Find and replace**.
  4. Optional: choose to replace only exact matches and to ignore letter case.
  5. In the **Find** field, enter the value to replace.
  6. In the **Replace** field, enter the replacement value.
  7. Click **Replace all**.



Wrangler replaces the values in the column and adds the `find-and-replace` directive to the recipe. When you run the data pipeline, Cloud Data Fusion applies the transformation to each value in the column. For example, in a column called `Name`, you replace the string `Doctor` with `Dr.` using the preceding steps. Wrangler adds the directive `find-and-replace Name s/Doctor/Dr./g` to the recipe.

## What's next

  * Learn more about [Wrangler directives](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#apply_directives).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
