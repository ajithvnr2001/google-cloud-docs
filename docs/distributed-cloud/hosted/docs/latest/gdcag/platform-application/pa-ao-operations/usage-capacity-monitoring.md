---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/usage-capacity-monitoring/
title: Usage and capacity monitoring \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:28.941620+00:00
---

# Usage and capacity monitoring  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/usage-capacity-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Usage and capacity monitoring Stay organized with collections  Save and categorize content based on your preferences. 

Platform Administrators (PA) and Application Operators (AO) access metrics in Grafana to monitor usage and capacity in the system. These metrics have associated labels to differentiate measured characteristics, such as the stock-keeping unit (SKU) name, tenant type, and bucket.

According to your role, you have access to the following metrics from the Grafana dashboard:

**Grafana metrics**  
---  
**Name** | **Description** | **Labels** | **Roles**  
`obj_tenant_used_capacity_bytes_count` | Number of bytes consumed in object storage. | 

  * Bucket
  * SKU ID
  * SKU name
  * Tenant type

| PA and AO  
`obj_tenant_objects_count` | Number of objects in object storage. | 

  * Bucket
  * SKU ID
  * SKU name
  * Tenant type

| PA and AO  
`obj_tenant_quota_bytes` | Quota of a tenant in object storage. | 

  * SKU ID
  * SKU name
  * Tenant type

| PA  
  
The following table contains some examples of how to use the previous Grafana metrics:

**Query examples**  
---  
**Query** | **Description** | **Roles**  
`(sum by (tenant_type, sku_id) (obj_tenant_used_capacity_bytes_count) / sum by (tenant_type, sku_id) (obj_tenant_quota_bytes))` | Percentage of used capacity per tenant. | PA  
`obj_tenant_used_capacity_bytes_count` | Bytes used in each bucket. | PA and AO  
`obj_tenant_objects_count` | Objects used in each bucket. | PA and AO  
`obj_tenant_used_capacity_bytes_count{bucket=BUCKET_NAME}` | Bytes used in a particular bucket. | PA and AO  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
