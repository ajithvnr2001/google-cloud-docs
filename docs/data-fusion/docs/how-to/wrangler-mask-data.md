---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-mask-data/
title: Mask data \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:58:30.365105+00:00
---

# Mask data  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-mask-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Mask data Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to mask sensitive data when you prepare data in the Wrangler workspace of the Cloud Data Fusion Studio. You can mask data in columns of any data type, except boolean and bytes types.

  1. [Go to Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, go to a column name and click the arrow_drop_down expander arrow.
  3. Select **Mask** , and select an option—for example, **Custom selection**. The options are explained in the following sections.



The transformation is applied to the Preview data shown on Data tab of the Wrangler workspace. Wrangler adds a masking directive to the recipe. When you run the data pipeline, the transformation is applied to all values in the column.

## Show the last four characters only

The **Show the last 4 characters only** masking option adds the `mask-number` directive as a transformation step to the recipe.

## Show the last two characters only

The **show the last 2 characters only** masking option adds the `mask-number` directive as a transformation step to the recipe.

## Custom selection

The **Custom selection** masking option lets you select the position of the characters to mask in a cell and masks similarly positioned characters in each row of the column. For example, in a cell that contains a 10-character string, selecting the first 8 characters of the string causes the first 8 characters to be masked in each row of the column.

To select specific characters to mask:

  1. [Go to Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, go to a column name and click the arrow_drop_down expander arrow.
  3. Select **Mask > Custom selection**. The column values that you can mask appear with a blue background.
  4. In any cell of the column, select the characters to mask.
  5. Click **Apply**.



That portion of the value is masked for all fields in the column.

Custom selection adds the `mask-number` directive to the recipe. When you run the data pipeline, the transformation is applied to all values in the column.

## By shuffling

The **By shuffling** masking option applies a random masking pattern to each field in the column. Wrangler adds the `mask-shuffle` directive as a transformation step to the recipe.

## What's next

  * Learn more about [Wrangler directives](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#apply_directives).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
