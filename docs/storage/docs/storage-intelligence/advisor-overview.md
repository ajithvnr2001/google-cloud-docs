---
url: https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview/
title: About Storage Intelligence advisor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:26:11.021320+00:00
---

# About Storage Intelligence advisor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storage-intelligence/advisor-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  About Storage Intelligence advisor Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how Storage Intelligence advisor lets you monitor and manage your Cloud Storage environment at scale across organizations, folders, and projects.

Storage Intelligence advisor displays trends and anomalies in your storage patterns, and provides built-in recommendations to optimize usage and resolve performance bottlenecks.

To view Storage Intelligence advisor, see [View Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/view-advisor).

## Storage Intelligence advisor structure and sections

To help you manage your storage environment, Storage Intelligence advisor displays insights through a structured hierarchy of metrics, findings, and next steps:

  * **Metrics** : data points collected from your Cloud Storage environment, such as storage volume, object counts, and operation rates.
  * **Findings** : anomalies detected from your metrics that require attention, such as a spike in errors or inefficient storage use.
  * **Next steps** : recommendations provided with each finding to help you resolve the identified issue.



To help you analyze your storage data, Storage Intelligence advisor includes the following sections.

### At a glance

The **At a glance** section provides a daily snapshot of your storage environment. The section label adapts to your selected resource: **Project at a glance** , **Folder at a glance** , or **Organization at a glance**. It displays key metrics such as total storage size, bucket and object counts, and average object size. The following table describes how to use these metrics to analyze your storage utilization:

Metric | Description  
---|---  
**Total storage size** | The total size of your storage across multi-regional and regional storage classes.  
**Total buckets with objects** | The number of buckets that contain at least one object.  
**Total objects** | The total number of objects in your selected resource scope.  
**Average object size** | The mean size of objects in your project, folder, or organization, which indicates storage efficiency.  
  
### Top findings

The **Top findings** section alerts you to changes in storage behavior that require attention. Depending on the selected resource scope, findings provide aggregated or granular insights:

  * **Organization and folder scopes** : each finding card aggregates anomalies across contained projects and displays the number of affected projects. To view a panel listing all affected projects, click **View details**. You can then open finding details for any project in a new tab.
  * **Project scope** : finding cards let you drill down into bucket-level and object-level details for that project.



Each finding is associated with one of the following categories to indicate its impact:

  * **Usage optimization** : findings that affect storage usage and cost efficiency.

  * **Performance** : findings that affect speed, latency, and operational health.




The following table describes the findings that are available in Storage Intelligence advisor:

Finding | Category | Description  
---|---|---  
Spike in Class A or B operations on Coldline or Archive data | Usage optimization | Indicates frequent operations on data in Coldline storage and Archive storage. For example, you might see this finding if monthly reports stored in Archive storage are accessed daily by an analytics job, creating a high rate of operations for data that is better suited for Standard storage. To resolve this finding, move the data to a storage class suited for frequent access, or adjust the analytics job to use cached data. To learn more, see [Optimize usage for Coldline and Archive storage data](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/optimize-coldline-archive-class-costs).  
Spike in 429 errors indicating rate limited requests | Performance | Indicates that Cloud Storage is rate-limiting your requests, which causes latency and timeouts. For example, you might see this finding if a batch processing job rapidly reads or writes many objects in the same bucket, exceeding request limits and causing `429 Too Many Requests` errors. To help resolve this finding, implement exponential backoff in your application or scale up request throughput gradually. To learn more, see [Improve performance by mitigating rate limited request errors](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/improve-performance-by-mitigating-429-errors).  
Spike in cross-region egress | Usage optimization | Indicates an increase in data transfer between Cloud Storage buckets in one region and other Google Cloud services in another region. This activity can lead to unexpected egress costs. For example, you might see this finding if a Compute Engine instance in `us-central1` frequently accesses a bucket in `us-east1`. To resolve this finding, colocate your Google Cloud and storage resources in the same region using bucket relocation. To learn more, see [Manage cross-region egress](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/manage-egress).  
Total bytes stored increased above trend over the last 30 days | Usage optimization | Indicates that storage consumption has increased beyond historical trends over the last 30 days. For example, you might see this finding if your bucket retains noncurrent object versions indefinitely after you upload new versions. Indefinite retention can lead to unnecessary storage costs. To resolve this finding, use Object Lifecycle Management to delete noncurrent versions or move them to colder storage, or enable Autoclass to automatically manage storage classes based on access patterns. To learn more, see [Identify above trend storage consumption](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/identify-storage-consumption).  
  
### Key charts

The **Key charts** section contains time-series charts that help you visualize the following storage trends:

  * **Cumulative object count** : tracks the total number of objects in your selected project, folder, or organization across locations and storage classes.
  * **Storage volume over time** : tracks storage size across locations and storage classes.



## Use cases

Storage Intelligence advisor supports the following use cases.

### Minimize custom reporting

Track metrics across your Cloud Storage environment without maintaining custom data processing pipelines, BigQuery scripts, or external visualization tools.

### Centralize oversight

Assess the health of your entire Cloud Storage environment from a single interface across projects, folders, or organizations, without running manual queries across various logs or resources.

To get started, see [View Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/view-advisor).

### Optimize storage usage

Identify opportunities to optimize storage usage by aligning data with the appropriate storage class. For example, a `Spike in Class A or B operations on Coldline or Archive data` finding indicates that data in Coldline storage or Archive storage is being accessed frequently. This data might be better suited for a storage class intended for frequent access, such as Standard storage or Nearline storage.

To learn more, see [Optimize usage for Coldline and Archive storage data](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/optimize-coldline-archive-class-costs).

### Resolve performance bottlenecks

Identify performance issues, such as request throttling or unexpected operation spikes. Findings such as `Spike in 429 errors` help you optimize I/O patterns to improve application reliability.

To learn more, see [Improve performance by mitigating rate limited request errors](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/improve-performance-by-mitigating-429-errors).

## VPC Service Controls support

Storage Intelligence advisor supports [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) for project-level resources inside a service perimeter. For details about VPC Service Controls support and resource-level limitations, see [VPC Service Controls supported products: Cloud Storage](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_storage).

## What's next

  * **Key tasks** : 
    * [View Storage Intelligence advisor](https://docs.cloud.google.com/storage/docs/storage-intelligence/view-advisor)
  * **Explore findings** : 
    * [Review the findings reference catalog](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/findings-reference-catalog)
    * [Optimize usage for Coldline and Archive storage data](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/optimize-coldline-archive-class-costs)
    * [Improve performance by mitigating rate limited request errors](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/improve-performance-by-mitigating-429-errors)
    * [Identify above trend storage consumption](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/identify-storage-consumption)
    * [Manage cross-region egress](https://docs.cloud.google.com/storage/docs/storage-intelligence/findings/manage-egress)
  * **Related concepts** : 
    * [Storage classes](https://docs.cloud.google.com/storage/docs/storage-classes)
    * [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle)
    * [Quotas and limits](https://docs.cloud.google.com/storage/quotas)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
