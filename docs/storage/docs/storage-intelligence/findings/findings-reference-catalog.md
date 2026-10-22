---
url: https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/findings-reference-catalog/
title: Findings reference catalog for Storage Intelligence advisor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:26:32.127871+00:00
---

# Findings reference catalog for Storage Intelligence advisor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/findings-reference-catalog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Findings reference catalog for Storage Intelligence advisor Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a catalog of findings that Storage Intelligence advisor displays. A _finding_ is an anomaly in storage patterns that requires your attention, such as a spike in errors or inefficient storage use. Storage Intelligence advisor displays these findings to help you prioritize remediation based on categories such as usage optimization and performance.

For information about Storage Intelligence advisor, see [About Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview).

The following table describes the findings that are available in Storage Intelligence advisor.

Finding | Category | Description  
---|---|---  
Spike in Class A or B operations on Coldline or Archive data | Usage optimization | Indicates frequent operations on data in Coldline storage and Archive storage. For example, you might see this finding if an analytics job accesses monthly reports in Archive storage daily. This daily access results in a high operation rate for data better suited for Standard storage. To resolve this finding, move the data to a storage class suited for frequent access, or configure the analytics job to use cached data. To learn more, see [Optimize usage for Coldline and Archive storage data](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/optimize-coldline-archive-class-costs).  
Spike in 429 errors indicating rate limited requests | Performance | Indicates that Cloud Storage is rate-limiting requests, which causes latency and timeouts. For example, you might see this finding if a batch processing job rapidly reads or writes many objects in the same bucket. This burst of requests exceeds per-bucket limits and triggers `429 Too Many Requests` errors. To resolve this issue, implement exponential backoff in your application or scale up request throughput gradually. To learn more, see [Improve performance by mitigating rate limited request errors](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/improve-performance-by-mitigating-429-errors).  
Spike in cross-region egress | Usage optimization | Indicates an increase in data transfer between Cloud Storage buckets in one region and Compute Engine instances or other Google Cloud services in another region. This cross-region traffic can lead to unexpected egress costs. For example, you might see this finding if a Compute Engine instance in `us-central1` frequently accesses a bucket in `us-east1`. To resolve this finding, colocate your compute and storage resources in the same region by using bucket relocation. To learn more, see [Manage cross-region egress](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/manage-egress).  
Total bytes stored increased above trend over the last 30 days | Usage optimization | Indicates that storage consumption has increased beyond historical trends over the last 30 days. For example, you might see this finding if your bucket retains noncurrent object versions indefinitely after you upload new versions. Indefinite retention can lead to unnecessary storage costs. To resolve this finding, use Object Lifecycle Management to delete noncurrent versions or move them to colder storage, or enable Autoclass to automatically manage storage classes based on access patterns. To learn more, see [Identify above trend storage consumption](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/identify-storage-consumption).  
  
## What's next

  * **Key tasks** : 
    * [View Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/view-advisor)
  * **Related concepts** : 
    * [About Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
