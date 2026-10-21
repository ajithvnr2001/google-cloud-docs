---
url: https://docs.cloud.google.com/storage/docs/access-monitoring/
title: Access monitoring data in Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:52:57.351289+00:00
---

# Access monitoring data in Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/access-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Access monitoring data in Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to access monitoring data from your Cloud Storage buckets, including request rates, bandwidth usage, and storage usage. For information about monitoring in Cloud Storage and what metrics to use to find the data you want, see [Overview of monitoring](https://docs.cloud.google.com/storage/docs/monitoring) or [Overview of bandwidth usage monitoring](https://docs.cloud.google.com/storage/docs/bandwidth-usage).

## Monitor bucket data for individual buckets

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the list of buckets, click the name of the bucket for which you want to see monitoring data.

  3. In the **Bucket details** page, click the **Observability** tab.

Monitoring charts are displayed.




## Monitor bucket data for all buckets within a project

  1. In the Google Cloud console, go to the Cloud Storage **Buckets** page.  


[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. In the **Cloud Storage** navigation pane, click **Monitoring**.

Monitoring charts are displayed.




The **Monitoring** page can also be directly accessed using the following URL:
    
    
    https://console.cloud.google.com/storage/monitoring?project=PROJECT_ID

Where `PROJECT_ID` is the ID of the project whose metrics you want to monitor.

## Monitor bandwidth and storage usage

Use the instructions in this section to monitor bandwidth usage for buckets or storage usage for zonal buckets or Rapid Cache.

For data egress from a Cloud Storage bucket to Google services:

  * If the bucket is located in a region, the usage must be by resources located in the same region.

  * If the bucket is located in a [dual-region](https://docs.cloud.google.com/storage/docs/locations#location-dr), the usage must be by resources located in either of the regions that makes up the dual-region.

  * The usage must be by Google Cloud resources other than Cloud Storage buckets.

  * The usage must be from either a [JSON API `GET Object`](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/get) request or a [XML API `GET Object`](https://docs.cloud.google.com/storage/docs/xml-api/get-object-download) request.




### Before you begin

In order to track bandwidth monitoring, you must have the [Cloud Storage service `storage.googleapis.com`](https://console.cloud.google.com/apis/library/storage.googleapis.com) enabled for your project.

To monitor bandwidth or storage usage:

### Console

You can view egress bandwidth usage for your project's buckets or storage usage for zonal buckets only by using the **Quotas and system limits** page with the appropriate metric. For information about bandwidth monitoring metrics and what data they return, see [Bandwidth monitoring metrics](https://docs.cloud.google.com/storage/docs/bandwidth-usage#bandwidth-monitoring).

[Open Cloud Storage Quotas and systems limits](https://console.cloud.google.com/iam-admin/quotas)

  * **Google Egress Bandwidth per second per region**

  * **Rapid Zonal Egress Bandwidth per second per zone**

  * **Dualregion Google Egress Bandwidth per second per region per dualregion_location**

  * **MultiRegion Google Egress Bandwidth per second per region**

  * **Internet Egress Bandwidth per second per region**

  * **Dualregion Internet Egress Bandwidth per second per region per dualregion_location**

  * **Multiregion Internet Egress Bandwidth per second per region**

  * **Anywhere Cache Egress Bandwidth per second per zone**

  * **Rapid Zonal Bytes per zone**

  * **Anywhere Cache Storage Size per region per bucket per cache**




You can also view the Google egress bandwidth usage of buckets in your project that are located in regions on the [Cloud Storage monitoring page](https://console.cloud.google.com/storage/monitoring).

For more information on viewing and managing quotas, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage). For information about bandwidth monitoring metrics and what data they return, see [Bandwidth monitoring metrics](https://docs.cloud.google.com/storage/docs/bandwidth-usage#bandwidth-monitoring).

### Command line

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  1. Use the following command to return Cloud Storage quota information for a project:
         
         gcloud alpha services quota list --service=storage.googleapis.com --consumer=projects/PROJECT_ID

Where PROJECT_ID is the project ID.

  2. In the YAML response, look for the following:

     * `storage.googleapis.com/google_egress_bandwidth`

     * `storage.googleapis.com/rapid_zonal_egress_bandwidth`

     * `storage.googleapis.com/dualregion_google_egress_bandwidth`

     * `storage.googleapis.com/multiregion_google_egress_bandwidth`

     * `storage.googleapis.com/internet_egress_bandwidth`

     * `storage.googleapis.com/dualregion_internet_egress_bandwidth`

     * `storage.googleapis.com/multiregion_internet_egress_bandwidth`

     * `storage.googleapis.com/anywhere_cache_egress_bandwidth`

     * `storage.googleapis.com/rapid_zonal_bytes`

     * `storage.googleapis.com/anywhere_cache_storage_size`

For information about bandwidth monitoring metrics and what data they represent, see [Bandwidth monitoring metrics](https://docs.cloud.google.com/storage/docs/bandwidth-usage#bandwidth-monitoring).




For more information, see [Manage your quota using the Google Cloud CLI](https://docs.cloud.google.com/docs/quotas/view-manage#managing_your_quota_gcloud).

### JSON API

For information on programmatically retrieving time series information for non dual-region quotas, see the [ListTimeSeries command](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list), using the following values for `filter`:

  * `metric.type="serviceruntime.googleapis.com/quota/rate/net_usage"`

  * `resource.type="consumer_quota"`

  * One of the following:

    * `metric.label.quota_metric="storage.googleapis.com/google_egress_bandwidth"`

    * `metric.label.quota_metric="storage.googleapis.com/rapid_zonal_egress_bandwidth"`

    * `metric.label.quota_metric="storage.googleapis.com/internet_egress_bandwidth"`

    * `metric.label.quota_metric="storage.googleapis.com/multiregion_google_egress_bandwidth"`

    * `metric.label.quota_metric="storage.googleapis.com/multiregion_internet_egress_bandwidth"`




For information on programmatically retrieving time series information for dual-region quotas, see the [ListTimeSeries command](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list), using the following values for `filter`:

  * `resource.type="storage.googleapis.com/Project"`

  * One of the following:

    * `metric.type="storage.googleapis.com/quota/dualregion_google_egress_bandwidth/usage"`

    * `metric.type="storage.googleapis.com/quota/dualregion_internet_egress_bandwidth/usage"`




For information about bandwidth monitoring metrics and what data they represent, see [Bandwidth monitoring metrics](https://docs.cloud.google.com/storage/docs/bandwidth-usage#bandwidth-monitoring).

## What's next

To request an increase of storage quota for zonal buckets or Rapid Cache, see [Storage usage monitoring](https://docs.cloud.google.com/storage/docs/storage-usage).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
