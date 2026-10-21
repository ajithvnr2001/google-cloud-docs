---
url: https://docs.cloud.google.com/vision-ai/docs/connect-warehouse/
title: Connect and store data to a warehouse \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:00.270528+00:00
---

# Connect and store data to a warehouse  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/connect-warehouse/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Connect and store data to a warehouse Stay organized with collections  Save and categorize content based on your preferences. 

One of the data destination components you can add to your app is a Vision Warehouse to store streamed and processed data.

**Caution** : Gemini Enterprise Agent Platform Vision doesn't support a stream's usage in multiple apps connected to a warehouse ; one stream can be associated with only one warehouse export destination. 

### Console

  1. Open the **Applications** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)

  2. Select **View app** next to the name of your application from the list.

  3. From the side list of components, choose **Vision AI Warehouse** from the list of **Connectors**. The warehouse node is added to the app graph and a side Vision AI Warehouse menu opens.

  4. Select **Connect warehouse**.

  5. If you choose to radio_button_checked**Create a new warehouse** , enter a warehouse name and select a [time to live (TTL)][ttl-link]{: .external}. Then click **Create**.

![create a warehouse image](https://docs.cloud.google.com/static/vision-ai/docs/images/create-warehouse.png)

If you choose to radio_button_checked**Select from existing warehouses** , select the button next to your warehouse and click **Connect**.

![select a warehouse image](https://docs.cloud.google.com/static/vision-ai/docs/images/select-warehouse.png)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
