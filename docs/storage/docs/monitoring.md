---
url: https://docs.cloud.google.com/storage/docs/monitoring/
title: Overview of monitoring in Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:07.624928+00:00
---

# Overview of monitoring in Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Overview of monitoring in Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This page discusses options for monitoring requests to Cloud Storage, including tracking errors and request rates. For instructions on accessing monitoring data in Cloud Storage, see [Access monitoring data](https://docs.cloud.google.com/storage/docs/access-monitoring).

## Monitoring options

Within the Google Cloud console, there are several levels of the resource hierarchy at which you can monitor your Cloud Storage requests:

### Individual buckets

Within each **Bucket details** page, there is an **Observability** tab that reports metrics for that particular bucket. For instructions on accessing monitoring data for individual buckets, see [Monitoring individual buckets](https://docs.cloud.google.com/storage/docs/access-monitoring#monitor-individual-buckets).

### All buckets within a project

Each project has a Cloud Storage **Monitoring** page, accessible in the left pane for Cloud Storage. For instructions on accessing monitoring data across all buckets within a project, see [Monitoring all buckets in a project](https://docs.cloud.google.com/storage/docs/access-monitoring#monitor-all-buckets).

### All Google Cloud resources

For monitoring across all services and resources in your Google Cloud project, folder, or organization, use the [Cloud Monitoring](https://docs.cloud.google.com/monitoring) service in the Google Cloud console. This service is available at <https://console.cloud.google.com/monitoring>.

### Bandwidth usage by region

For information about bandwidth usage metrics and monitoring, see [bandwidth monitoring](https://docs.cloud.google.com/storage/docs/bandwidth-usage#bandwidth-monitoring).

## Default monitoring

By default, the following graphs appear in your individual bucket monitoring and your Cloud Storage Monitoring page:

Graph | Description  
---|---  
**Server Error Rate** | Requests with 5xx error codes. These errors are generally caused by issues internal to Google Cloud and are [retryable](https://docs.cloud.google.com/storage/docs/retry-strategy). 5xx error codes are applicable to the [Cloud Storage SLA](https://cloud.google.com/storage/sla).  
**Client Error Rate** | Requests with 4xx error codes or a 304 status code with a `FAILED_PRECONDITION` error. These errors indicate changes that need to be made by or made for requesters, such as granting requesters sufficient permission to access the relevant Cloud Storage resources or scaling back requests to prevent exhausting quotas.   
**Read Errors** | Object reading errors, specifically for errors with an `INTERNAL`, `UNAVAILABLE`, or `DEADLINE_EXCEEDED` response code. Errors related to requests for bucket metadata, object listings, or object metadata are not included in this graph. 

  * For single-bucket monitoring, errors are aggregated for the entire bucket.
  * For Cloud Storage Monitoring, errors are aggregated for each bucket, and the 5 buckets with the most read errors are displayed by default. The graph can be customized to display additional buckets.

  
**Write Errors** | Object write errors, specifically for errors with an `INTERNAL`, `UNAVAILABLE`, or `DEADLINE_EXCEEDED` response code. Errors related to requests for object rewrites, object compositions, metadata updates, and XML API multipart uploads are not included in this graph. 

  * For single-bucket monitoring, errors are aggregated for the entire bucket.
  * For Cloud Storage Monitoring, errors are aggregated for each bucket, and the 5 buckets with the most write errors are displayed by default. The graph can be customized to display additional buckets.

  
**Total Read/List/Get Request Count** | 

  * For single-bucket monitoring, the total number of get requests made to the bucket.
  * For Cloud Storage Monitoring, the total number of get requests made to all buckets.

Counts are grouped by method type, such as requests for bucket metadata, requests for object metadata, requests for object data, and requests to list objects.  
**Total Write Request Count** | 

  * For single-bucket monitoring, the total number of object write requests made to the bucket.
  * For Cloud Storage Monitoring, the total number of object write requests made to all buckets.

Requests for object rewrites, object compositions, metadata updates, and XML API multipart uploads are not included in this graph.  
**Data Ingress Rate over the Network** | 

  * For single-bucket monitoring, the rate of received bytes by the bucket.
  * For Cloud Storage Monitoring, the rate of received bytes by all buckets.

  
**Data Egress Rate over the Network** | 

  * For single-bucket monitoring, the rate of bytes sent by the bucket.
  * For Cloud Storage Monitoring, the rate of bytes sent by all buckets.

  
  
### Graphs specific to the Observability page

By default, the **Observability** tab available for each bucket also contains the following monitoring graphs:

Graph | Description  
---|---  
**Percent of minutes out of RPO** | Applicable to buckets in dual-regions and multi-regions. The percentage of minutes during which one or more objects took longer than their RPO (Recovery Point Objective) time to be replicated between geographically distinct locations. Metrics are aggregated over the previous 30 days. There is a delay, typically several hours, between when a replication occurs and when monitoring reports the associated metrics.  
For more information, including RPO times for different replication options, see [Performance monitoring](https://docs.cloud.google.com/storage/docs/availability-durability#monitoring).  
**Percent of objects out of target** | Applicable to buckets in dual-regions and multi-regions. The percentage of objects that were not replicated between geographically distinct locations within the RPO (Recovery Point Objective) time. Metrics are aggregated over the previous 30 days. When tracking default replication metrics, this graph also includes a line that measures the percentage of objects that were not replicated between geographically distinct locations within the 1 hour design target. There is a delay, typically several hours, between when the replication occurs and when monitoring reports the associated metrics.  
For more information, including RPO times for different replication options, see [Performance monitoring](https://docs.cloud.google.com/storage/docs/availability-durability#monitoring).  
**Bucket meeting RPO** | Applicable to buckets in dual-regions and multi-regions. A boolean value indicating whether all objects in the bucket are meeting RPO or not.  
For more information, including RPO times for different replication options, see [Performance monitoring](https://docs.cloud.google.com/storage/docs/availability-durability#monitoring).  
**Maximum delay in turbo replication** | Applicable to buckets in dual-regions with turbo replication. The age, in seconds, of the oldest unreplicated object in the bucket.   
  
#### Cross-bucket replication graphs

If you used [cross-bucket replication](https://docs.cloud.google.com/storage/docs/access-monitoring#monitor-individual-buckets) to replicate objects from a source bucket to a destination bucket, the following monitoring graphs also appear in the source bucket's **Observability** tab:

Graph | Description  
---|---  
**Objects replicated cross-bucket** | The rate of objects being replicated to the destination bucket per second.  
  
**Cross-bucket replication latency** | The time taken (50th percentile) for replicated objects to be available in the destination bucket, measured in seconds.   
  
### Graphs specific to the Monitoring page

By default, the Cloud Storage **Monitoring** page also contains the following monitoring graphs:

Graph | Description  
---|---  
**Google Egress Bandwidth Usage** | The amount of data egress from Cloud Storage to other Google Cloud services. For more information, see [Bandwidth usage in Cloud Storage](https://docs.cloud.google.com/storage/docs/bandwidth-usage).   
**Note:** Cloud Storage requests that are not bucket-specific, such as listing buckets and managing HMAC keys, are not tracked in these metrics.

You can create your own dashboard layouts and customize the data you collect by clicking the **Customize dashboard** button, which appears in both individual bucket monitoring tabs and in your Cloud Storage Monitoring page. For more formation, see [Manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards).

## Graphs specific to Rapid Cache

Cloud Storage provides monitoring charts using the Google Cloud console that let you track the performance of caches created with Rapid Cache. To view a list of available charts and how to access charts at the bucket and project-level, see [Monitor cache performance](https://docs.cloud.google.com/storage/docs/rapid/use-rapid-cache#monitor-performance).

## What's next

  * [Access monitoring data](https://docs.cloud.google.com/storage/docs/access-monitoring).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
