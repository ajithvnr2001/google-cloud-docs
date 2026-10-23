---
url: https://docs.cloud.google.com/storage/docs/storage-usage/
title: Storage usage monitoring in Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:39.475339+00:00
---

# Storage usage monitoring in Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/storage-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Storage usage monitoring in Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This page discusses metrics used to monitor storage usage for zonal buckets and cache storage usage for Rapid Cache. It also describes how to request additional storage capacity for zonal buckets and caches beyond the default [quotas](https://docs.cloud.google.com/storage/quotas#rapid-cache).

For instructions on accessing monitoring data in Cloud Storage, see [Access monitoring data](https://docs.cloud.google.com/storage/docs/access-monitoring).

## Storage usage monitoring

Cloud Storage provides storage usage and quota monitoring for zonal buckets that are created with [Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket) and caches that are created with [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache).

The following storage data is available for monitoring:

  * Rapid storage bytes: monitors storage quota and usage in zonal buckets. Quota and usage are measured in bytes per project, per zone.

Metric name: `storage.googleapis.com/rapid_zonal_bytes`

  * Rapid Cache storage size: monitors storage quota and usage for caches created with Rapid Cache. Quota and usage are measured in bytes per project, per zone.

Metric name: `storage.googleapis.com/anywhere_cache_storage_size`




## Request more storage for zonal buckets

The following instructions describe how to request an increase of storage capacity for zonal buckets beyond the default quota of 1 TB.

  1. Enable the Cloud Storage API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=storage.googleapis.com)

  2. In the Google Cloud console, go to the IAM **Quotas & System Limits** page.

[Go to **Quotas & System Limits**](https://console.cloud.google.com/iam-admin/quotas)

  3. In the **Filter** search bar, select the **Metric** property, then search for the metric `storage.googleapis.com/rapid_zonal_bytes`.

  4. Identify the row for the zone in which you want to increase storage quota. In that row, click **More actions** more_vert, then click **Edit quota**.

  5. In the **Quota changes** pane that appears, enter a new quota value.

  6. Click **Submit request**.




## Request more storage for Rapid Cache

To request an increase of storage capacity for Rapid Cache beyond 1 PiB, contact your Technical Account Manager or Google representative.

## What's next

  * [View bandwidth monitoring data](https://docs.cloud.google.com/storage/docs/access-monitoring).
  * [Monitor who accesses your Cloud Storage resources](https://docs.cloud.google.com/storage/docs/audit-logging).
  * [Create notifications](https://docs.cloud.google.com/storage/docs/reporting-changes) when an object is created, updated, or deleted.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
