---
url: https://docs.cloud.google.com/vision-ai/docs/connect-data-destination/
title: Overview: Connect app output to a data destination \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:49.646978+00:00
---

# Overview: Connect app output to a data destination  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/connect-data-destination/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Overview: Connect app output to a data destination Stay organized with collections  Save and categorize content based on your preferences. 

After you [create the data ingestion stream](https://docs.cloud.google.com/vision-ai/docs/create-manage-streams) and [add the processing nodes](https://docs.cloud.google.com/vision-ai/docs/build-app#add-pretrained-model) to your app, you must choose where to send the processed data. This data destination ("data sink") is the end point of your app graph that accepts stream data without producing any stream data. The destination you choose depends on how you use the app output data. ![connector nodes image](https://docs.cloud.google.com/static/vision-ai/docs/images/connector-nodes.png)_In the Google Cloud console, data destinations are available in the**Connectors** section of the app graph page._

You can connect app output data to the following data destinations:

  1. **Vision Warehouse** : Store original or analyzed video data that you can view and query. Using a Vision Warehouse allows you to specify annotations on whole or partial video clips.

For more information about sending app output data to a Vision Warehouse, see [Connect and store data to a warehouse](https://docs.cloud.google.com/vision-ai/docs/connect-warehouse).

![warehouse information card in UI](https://docs.cloud.google.com/static/vision-ai/docs/images/warehouse-card.png)

  2. **BigQuery** : Store data in BigQuery to use its offline analytics capabilities. Using BigQuery allows you to query streaming data, access and share analytical insights, create reports and dashboards, and export BigQuery ML models for online prediction.

For more information about sending app output data to BigQuery, see [Connect and store data to BigQuery](https://docs.cloud.google.com/vision-ai/docs/connect-bigquery).

![BigQuery information card in UI](https://docs.cloud.google.com/static/vision-ai/docs/images/bq-card.png)

  3. **Live stream data** : If you want more granular control to act on real-time analytics, you can receive the live output from your app. For example, you can write code that uses live occupancy count data to programmatically change staffing allocation. 

For more information about directly streaming app output data, see [Enable live stream output](https://docs.cloud.google.com/vision-ai/docs/enable-stream-output).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
