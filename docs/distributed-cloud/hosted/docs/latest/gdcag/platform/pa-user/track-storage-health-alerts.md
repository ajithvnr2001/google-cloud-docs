---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/track-storage-health-alerts/
title: Track storage health alerts \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:22.776197+00:00
---

# Track storage health alerts  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/track-storage-health-alerts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Track storage health alerts Stay organized with collections  Save and categorize content based on your preferences. 

Platform Administrators (PA) and Application Operators (AO) access metrics in the monitoring instance to monitor usage and capacity in the system. These metrics have associated labels to differentiate measured characteristics, such as the stock-keeping unit (SKU) name, tenant type, and bucket.

According to your role, you have access to the following metrics from the monitoring dashboard:

**Monitoring metrics**  
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
`obj_proxy_servehttp_request_total_platform` | A counter that tracks the total number of S3 requests to object storage. | 

  * operation_type
  * result

| PA  
`obj_proxy_servehttp_first_byte_latency_milliseconds_platform_bucket`, `obj_proxy_servehttp_first_byte_latency_milliseconds_platform_count`, `obj_proxy_servehttp_first_byte_latency_milliseconds_platform_sum` | Histogram of the time it takes for a single operation or request to complete. | 

  * operation_type
  * result

| PA  
  
The following table contains some examples of how to use the previous monitoring metrics:

**Query examples**  
---  
**Query** | **Description** | **Roles**  
`(sum by (tenant_type, sku_id) (obj_tenant_used_capacity_bytes_count) / sum by (tenant_type, sku_id) (obj_tenant_quota_bytes))` | Percentage of used capacity per tenant. | PA  
`obj_tenant_used_capacity_bytes_count` | Bytes used in each bucket. | PA and AO  
`obj_tenant_objects_count` | Objects used in each bucket. | PA and AO  
`obj_tenant_used_capacity_bytes_count{bucket=FULLY_QUALIFIED_BUCKET_NAME}` | Bytes used in a particular bucket. | PA and AO  
`histogram_quantile(0.95, sum(rate(obj_proxy_servehttp_first_byte_latency_milliseconds_platform_bucket{operation_type="read_object", result="success"}[5m])) by (le))` | Calculate 95th percentile s3_get_object_latency_milliseconds. | PA  
`sum by (operation_type) (increase(obj_proxy_servehttp_request_total_platform{operation_type="(^list_bucket$)", result=(^success$)|(^user_error$)}[5m]))` | Calculate total successful `list_buckets` successful requests over 5 minutes. | PA  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
