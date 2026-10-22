---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-send-records-to-error/
title: Send records to error \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:38.162831+00:00
---

# Send records to error  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-send-records-to-error/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Send records to error Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to remove common errors from a dataset when you prepare data in the Wrangler workspace of the Cloud Data Fusion Studio.

The following types of errors occur in datasets:

  * Systemic errors, such as service or instance failures
  * Logical errors, such as pipeline run failures
  * Data errors, such as invalid credit card numbers, invalid date formats, or invalid zip codes



Wrangler provides a set of over 50 directives to help you remove common errors from a dataset.

To send records to error, follow these steps:

  1. [Go to the Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, go to a column name and click the arrow_drop_down expander arrow.
  3. Select **Send to error** , and then select the condition that sends bad records to error.



Wrangler removes values that match the specified condition from the sample and adds the `send to error` directive to the recipe. When you run the data pipeline, the transformation is applied to all values in the column.

## Add an error collector plugin to a data pipeline

When you add a Wrangler transformation with a recipe that includes the `send to error` directive to a data pipeline, you can choose to connect it to the Error Collector plugin. The Error Collector plugin is usually connected to a downstream sink plugin, such as a BigQuery sink.

When you run the pipeline, the records flagged by the `send to error` directive go from the Wrangler transformation step in your pipeline, to the Error Collector step, to the sink step. When the run finishes, you can examine those flagged records written to the sink.

If your recipe includes the `send to error` transformation, but the pipeline doesn't include the Error Collector plugin, the records flagged by the `send to error` directive are dropped during the pipeline run.

## What's next

  * Learn more about [Wrangler directives](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#apply_directives).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
