---
url: https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions/
title: Supported regions \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:24.035681+00:00
---

# Supported regions  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/warehouse-supported-regions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/vision-ai/docs/cloud-environment)



Send feedback 

#  Supported regions Stay organized with collections  Save and categorize content based on your preferences. 

## Choosing a region for a Vision Warehouse

When you create a warehouse in Vision Warehouse, you must choose a region. The region determines where your warehouse's underlying elements, such as assets, data schemas, and annotations, are stored.

## Supported regions

The following regions are currently supported:

  * `europe-west4`
  * `us-central1`



Batch video and image warehouses are supported only in `us-central1`.

**Limitation** : Your data for a regionalized resource may not be physically located in the region that you specified when you created the resource. If you have regulatory or compliance requirements mandating your data is stored in a specific region, do not use Gemini Enterprise Agent Platform Vision. 

While Google [Data Residency](https://cloud.google.com/blog/products/identity-security/meet-data-residency-requirements-with-google-cloud) requirements do not apply to all Gemini Enterprise Agent Platform Vision regionalized resources, we deploy those resources in regions that provide high availability and fault tolerance. They may even be replicated to other regions for redundancy and disaster recovery. 

### Regionalized endpoints

Requests must be directed at the regionalized endpoint that matches with the corresponding `location_id` shown below: 

  * `us-central1`: `https://warehouse-visionai.googleapis.com/v1`
  * `europe-west4`: `https://europe-west4-warehouse-visionai.googleapis.com/v1`

**Caution** : Requests sent with mismatching `location-id` and regionalized endpoint return an error. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
