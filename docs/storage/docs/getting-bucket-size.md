---
url: https://docs.cloud.google.com/storage/docs/getting-bucket-size/
title: Get bucket size \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:39:40.189804+00:00
---

# Get bucket size  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/getting-bucket-size/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Get bucket size Stay organized with collections  Save and categorize content based on your preferences. 

[Concepts](https://docs.cloud.google.com/storage/docs/bucket-metadata)

This page shows you how to get the size of your Cloud Storage [buckets](https://docs.cloud.google.com/storage/docs/buckets).

## Required roles

In order to get the required permissions for getting the size of a Cloud Storage bucket, ask your administrator to grant you the Storage Object Viewer (`roles/storage.objectViewer`) role on the bucket. If you plan on using the Google Cloud console, ask your administrator to grant you the Monitoring Viewer (`roles/monitoring.viewer`) role on the project that contains the bucket instead.

These roles contain the permissions required to get the size of a bucket. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * `storage.objects.list`
    * This permission is only required for using the Google Cloud CLI to perform the instructions on this page.



To see the permissions associated with `roles/monitoring.viewer`, refer to the [Monitoring Viewer documentation](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor).

You might be able to get the required permission with other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles) or [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles). For instructions on granting roles on buckets, see [Set and manage IAM policies on buckets](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions). For instructions on granting roles on projects, see [Manage access to projects](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Determine a bucket's size

### Console

**Note:** Monitoring measures bucket size once a day and does not report empty buckets. To measure bucket size at a given moment for any bucket, use `gcloud storage` instead.

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `Total bytes (v2)` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **GCS Bucket**.
     2. In the **Active metric categories** menu, select **Storage**.
     3. In the **Active metrics** menu, select **Total bytes (v2)**. 
     4. Click **Apply**.
The fully qualified name for this metric is **storage.googleapis.com/storage/v2/total_bytes**. 
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. To combine time series, use the menus on the [**Aggregation** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#select_display). For example, to display the CPU utilization for your VMs, based on their zone, set the first menu to **Mean** and the second menu to **zone**.

All time series are displayed when the first menu of the **Aggregation** element is set to **Unaggregated**. The default settings for the **Aggregation** element are determined by the metric type you selected.

  6. For quota and other metrics that report one sample per day, do the following: 
     1. In the **Display** pane, set the **Widget type** to **Stacked bar chart**.
     2. Set the time period to at least one week.



You can also use the Metrics Explorer to measure other bucket metrics such as **storage.googleapis.com/storage/object_count** and **storage.googleapis.com/storage/v2/total_byte_seconds** , which measure the daily number of objects and the daily storage consumed, respectively. See the [Google Cloud metrics documentation](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-storage) for a complete list of available metrics and [Metrics, time series, and resources](https://docs.cloud.google.com/monitoring/api/v3/metrics) for more information about using the Metrics Explorer.

### Command line

**Caution:** The `gcloud storage du` command calculates the current space usage by making a series of object listing requests, which can take a long time for large buckets. If the number of objects in your bucket is hundreds of thousands or more, or if you want to monitor your bucket size over time, use Monitoring instead, as described in the Console tab.

Use the [`gcloud storage du`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/du) command with a `--summarize` flag:
    
    
    gcloud storage du gs://BUCKET_NAME --summarize

where `BUCKET_NAME` is the name of the relevant bucket.

The response looks like the following example:
    
    
    134620      gs://my-bucket

In this example, the size of the bucket named `my-bucket` is 134,620 bytes.

## What's next

  * [List the objects in your bucket](https://docs.cloud.google.com/storage/docs/listing-objects).
  * [Get object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata).
  * [Learn more about monitoring your resources in Monitoring](https://docs.cloud.google.com/monitoring/api/v3/metrics).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Cloud Storage performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Cloud Storage free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
