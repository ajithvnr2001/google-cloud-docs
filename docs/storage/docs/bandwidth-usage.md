---
url: https://docs.cloud.google.com/storage/docs/bandwidth-usage/
title: Bandwidth usage monitoring in Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:26:08.148464+00:00
---

# Bandwidth usage monitoring in Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/bandwidth-usage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Bandwidth usage monitoring in Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This page discusses metrics used to monitor data usage for your Cloud Storage buckets, as well as how to request additional egress bandwidth for different quotas if you need more than the [default quota](https://docs.cloud.google.com/storage/quotas#bandwidth). For information about storage usage, see [Storage usage monitoring](https://docs.cloud.google.com/storage/docs/storage-usage).

For instructions on accessing monitoring data in Cloud Storage, see [Access monitoring data](https://docs.cloud.google.com/storage/docs/access-monitoring).

## Introduction to bandwidth monitoring

Cloud Storage provides bandwidth monitoring for you to track bandwidth usage from your project's buckets to other Google Cloud services. Bandwidth monitoring is aggregated by region and tracks usage for the last 6 weeks.

Before monitoring bandwidth usage, review the following terms:

  * _Egress bandwidth_ refers to the rate at which data is retrieved from your buckets in the course of completing requests made to Cloud Storage.

    * _Google egress bandwidth_ refers to data retrieved from your buckets that is destined for other Google services, such as Compute Engine.

    * _Internet egress bandwidth_ refers to data retrieved from your buckets that is served to the Internet, such as data downloaded directly to your local computer or data retrieved by Cloud CDN for serving to the Internet.

  * _Network egress_ refers to the rate at which data is sent over the network from your buckets to requesters.




In normal operation, egress bandwidth and network egress are typically about the same; however, in some cases egress bandwidth can be meaningfully greater than network egress. Broken connections, cancelled requests, and partial requests are cases where the data retrieved can be greater than the data that's ultimately sent.

### Bandwidth monitoring metrics

**Note:** Cloud Storage aggregates and samples bandwidth monitoring metrics every 60 seconds, but enforces egress bandwidth quota every second. Because enforcement is per-second, traffic spikes can cause HTTP `429 Too Many Requests` (or gRPC `RESOURCE_EXHAUSTED`) errors if your usage briefly exceeds the limit within any second. This can occur even if your average usage over 60 seconds is less than your limit, especially during traffic spikes. To address these errors, implement retries with exponential backoff, smooth out traffic spikes, or request a quota increase. For more information, see the [Troubleshooting guide](https://docs.cloud.google.com/storage/docs/troubleshooting#rate-limit).

The following bandwidth usage data is available for monitoring:

  * Google egress bandwidth per second per region: monitors Google egress bandwidth usage for buckets in your project that are located in regions.

  * Zonal Google egress bandwidth per second per zone: monitors Google egress bandwidth usage for buckets in your project that are located in zones.

  * Dual-region Google egress bandwidth per second per region per dual-region location: monitors Google egress bandwidth usage for buckets in your project that are located in dual-regions.

  * Multi-region Google egress bandwidth per second per region: monitors Google egress bandwidth usage for buckets in your project that are located in multi-regions.

  * Internet egress bandwidth per second per region: monitors Internet egress bandwidth usage for buckets in your project that are located in regions.

  * Dual-region internet egress bandwidth per second per region per dual-region location: monitors Internet egress bandwidth usage for buckets in your project that are located in dual-regions.

  * Multi-region internet egress bandwidth per second per region: monitors Internet egress bandwidth usage for buckets in your project that are located in multi-regions.




### Monitoring alerts

You can use Monitoring alerting policies to inform you when metrics such as `storage.googleapis.com/google_egress_bandwidth`, `storage.googleapis.com/dualregion_google_egress_bandwidth`, and `storage.googleapis.com/multiregion_google_egress_bandwidth` approach a quota limit.

  * For an overview of Monitoring alerts, see [Introduction to alerting](https://docs.cloud.google.com/monitoring/alerts).

  * To get started with Monitoring alerts using the Google Cloud console, see [Create metric-based alert policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui).

  * For examples of Monitoring alerts, see [Chart and monitor quota metrics](https://docs.cloud.google.com/monitoring/alerts/using-quota-metrics).




### Network monitoring

In addition to Cloud Storage bandwidth monitoring, you can use the [`network/sent_bytes_count`](https://docs.cloud.google.com/monitoring/api/metrics_gcp_p_z#gcp-storage) metric to measure Cloud Storage network egress. This is useful for approximating bandwidth usage for specific buckets, because bandwidth monitoring tracks bandwidth usage by location and project.

When using this networking metric, keep in mind the following:

  * `network/sent_bytes_count` uses bytes in its measurements, whereas typical networking metrics often use bits. For example, a 1 GiBps measurement for `network/sent_bytes_count` is equivalent to 8 Gibps.

  * `network/sent_bytes_count` tracks all the traffic sent over the network, not only egress to co-located Google Cloud services. As such, `network/sent_bytes_count` is typically greater than bandwidth usage.

    * In some cases, `network/sent_bytes_count` can be less than bandwidth usage due to events such as broken connections, cancelled requests, and partial requests.
  * `network/sent_bytes_count` metrics are sampled every 60 seconds. If the traffic is spiky, it's possible that requests are throttled for a short period of time even though the average egress over 60 seconds is below the limit.




## Request more bandwidth

The following instructions apply when requesting egress bandwidth for Cloud Storage buckets:

  1. Make sure you have enabled the [Cloud Storage service `storage.googleapis.com`](https://console.cloud.google.com/apis/library/storage.googleapis.com).

  2. In the Google Cloud console, go to the IAM **Quotas & System Limits** page.

[Go to Browser](https://console.cloud.google.com/iam-admin/quotas)

  3. In the **Filter** search bar, select the **Metric** property, then search for the metric for which you are requesting an increase:

     * Use `storage.googleapis.com/google_egress_bandwidth` to increase Google egress for your buckets located in regions.

     * Use `storage.googleapis.com/dualregion_google_egress_bandwidth` to increase Google egress for your buckets located in dual-regions.

     * Use `storage.googleapis.com/multiregion_google_egress_bandwidth` to increase Google egress for your buckets located in multi-regions.

     * Use `storage.googleapis.com/rapid_zonal_egress_bandwidth` to increase Google egress for your buckets located in zones.

       * This metric is only available for zonal buckets. For more information about zonal buckets, see [Rapid Bucket](https://docs.cloud.google.com/storage/docs/rapid/rapid-bucket).
     * Use `storage.googleapis.com/internet_egress_bandwidth` to increase Internet egress for your buckets located in regions.

     * Use `storage.googleapis.com/dualregion_internet_egress_bandwidth` to increase Internet egress for your buckets located in dual-regions.

     * Use `storage.googleapis.com/multiregion_internet_egress_bandwidth` to increase Internet egress for your buckets located in multi-regions.

  4. In the list of results, toggle the checkbox for the locations where you want to increase egress bandwidth. For the `storage.googleapis.com/dualregion_google_egress_bandwidth` and `storage.googleapis.com/dualregion_internet_egress_bandwidth` metrics, there must be non-zero historical usage of the metric before you can request an increase.

  5. Click **Edit Quotas**.

  6. Enter your requested quota and business justification.

  7. Click **Submit Request**.




If the previous instructions don't work for you, or if you need bandwidth greater than 5 Tbps for egress from buckets in zones, regions, or dual-regions, contact your [Technical Account Manager](https://docs.cloud.google.com/tam) or Google representative. Increase requests greater than 1 Tbps for egress from buckets in multi-regions are not supported.

For more information, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).

## What's next

  * [Access bandwidth monitoring data](https://docs.cloud.google.com/storage/docs/access-monitoring).
  * [Monitor who accesses your Cloud Storage resources](https://docs.cloud.google.com/storage/docs/audit-logging).
  * [Create notifications](https://docs.cloud.google.com/storage/docs/reporting-changes) when an object is created, updated, or deleted.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
