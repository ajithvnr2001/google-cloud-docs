---
url: https://docs.cloud.google.com/vision-ai/docs/app-supported-regions/
title: Choose a region for app creation \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:27:09.197985+00:00
---

# Choose a region for app creation  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/app-supported-regions/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Choose a region for app creation Stay organized with collections  Save and categorize content based on your preferences. 

When you create an app in the App Studio, you must choose a region. The region determines where your app's underlying elements, such as inputs, models, and warehouses, are stored.

## All resources in the same region

After you choose a region, resources you select and those you create in the App Studio remain there. This includes inputs, models, warehouses, and any other resources that your app uses.

The region you select is always highlighted in our guides. This ensures that you're aware of the region your resources are stored in, and you can make an informed decision about where to create your app.

## Supported regions

The following regions are currently supported:

  * `us-central1`
  * `europe-west4`

**Limitation** : Your data for a regionalized resource may not be physically located in the region that you specified when you created the resource. If you have regulatory or compliance requirements mandating your data is stored in a specific region, do not use Gemini Enterprise Agent Platform Vision. 

While Google [Data Residency](https://cloud.google.com/blog/products/identity-security/meet-data-residency-requirements-with-google-cloud) requirements do not apply to all Gemini Enterprise Agent Platform Vision regionalized resources, we deploy those resources in regions that provide high availability and fault tolerance. They may even be replicated to other regions for redundancy and disaster recovery. 

## How to choose a region

To choose a region during app creation, follow these steps:

### Console

  1. Open the **Applications** tab of the Gemini Enterprise Agent Platform Vision dashboard.

[Go to the Applications tab](https://console.cloud.google.com/ai/vision-ai/applications)

  2. In the **Region** drop-down, select the region where you want to create your app.

  3. Click **Create**.




## What's next

  * Read instructions about how to begin data ingestion from an app's input stream in [Create and manage streams](https://docs.cloud.google.com/vision-ai/docs/create-manage-streams#ingest-videos).
  * Learn how to list apps and view a deployed app's instances in [Managing applications](https://docs.cloud.google.com/vision-ai/docs/manage-app).
  * Learn how to read app input data from an ingestion stream or analyzed model output data in [Read stream data](https://docs.cloud.google.com/vision-ai/docs/read-stream).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
