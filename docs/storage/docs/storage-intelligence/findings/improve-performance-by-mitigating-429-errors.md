---
url: https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/improve-performance-by-mitigating-429-errors/
title: Improve performance by mitigating rate limited request errors \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:30.216106+00:00
---

# Improve performance by mitigating rate limited request errors  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/improve-performance-by-mitigating-429-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Improve performance by mitigating rate limited request errors Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use Storage Intelligence advisor to help improve performance by mitigating rate limited request errors.

To provide service stability, Cloud Storage limits request rates on buckets and objects. Exceeding these limits can cause `429 Too Many Requests` errors, leading to application latency and timeouts.

When rate-limited request errors increase, Storage Intelligence advisor displays a **Spike in 429 errors indicating rate limited requests** finding. A _finding_ is an anomaly detected from your metrics that needs your attention. For a full list of findings, see [Findings reference catalog](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/findings-reference-catalog).

## Thresholds that trigger a finding

Storage Intelligence creates a baseline for your project, folder, or organization based on historical trends. Storage Intelligence advisor generates a finding when `429` errors increase above the baseline.

Findings reflect the previous day's activity. For example, a spike occurring on Tuesday appears in Storage Intelligence advisor on Wednesday.

## Respond to a finding

  1. [View the finding details](https://docs.cloud.google.com/storage/docs/storage-intelligence/view-advisor#view-finding-details).

  2. Use the following table to select the recommended strategy for your scenario:

Scenario | Recommended action | Details  
---|---|---  
Cause of `429` spike is unclear | Use Gemini Cloud Assist to identify the issue | If the cause and scale of the issue are unclear, use Gemini Cloud Assist to analyze logs and identify specific application or user trends causing the overload. For setup details, see [Analyze stored data with Gemini Cloud Assist](https://docs.cloud.google.com/storage/docs/analyze-data-gemini-cloud-assist).  
Client application issues | Optimize client behavior | Review your application code to verify that it implements [exponential backoff](https://docs.cloud.google.com/storage/docs/retry-strategy). Consider distributing workloads across multiple buckets or prefixes to prevent exceeding per-bucket limits.  
Need granular request logs | Investigate access patterns with Storage Insights datasets | Export metadata to BigQuery for a detailed breakdown of object-level access patterns. This information can help you identify specific patterns or objects that are contributing to contention. **Note:** Exporting data to BigQuery incurs costs. For details, see [BigQuery Pricing](https://docs.cloud.google.com/bigquery/pricing).  



## What's next

  * **Explore other findings:**
    * [Optimize usage for Coldline and Archive storage data](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/optimize-coldline-archive-class-costs)
    * [Identify above trend storage consumption](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/identify-storage-consumption)
    * [Manage cross-region egress](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/manage-egress)
    * [Review the findings reference catalog](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/findings-reference-catalog)
  * **Related concepts:**
    * [Storage Intelligence advisor overview](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview)
    * [Quotas and limits](https://docs.cloud.google.com/storage/quotas)
    * [Request rate and scalability](https://docs.cloud.google.com/storage/docs/request-rate)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
