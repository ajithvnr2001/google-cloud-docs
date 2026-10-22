---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/understand-apigee-observability/
title: Understand Apigee observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:09.502501+00:00
---

# Understand Apigee observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/understand-apigee-observability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Understand Apigee observability Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Apigee API Monitoring, Apigee API Analytics, and Apigee access logs are three powerful tools you can use to collect, observe, and understand your API usage data. Each of these tools provides different insights and is recommended for different use cases. This document provides a brief overview of the purpose of each tool and its recommended usage, as described in the following sections:

  * API Monitoring
  * Apigee API Analytics
  * Apigee access logs



## API Monitoring

The goal of API Monitoring is to provide real-time insights into API performance, so that you can quickly diagnose and fix issues to keep your APIs working as intended.

API Monitoring provides you with aggregated data from your API proxies on a minute-by-minute basis, enabling you to closely monitor the health and performance of your APIs. You can use API Monitoring to configure near to real-time alerting on specified parameters and take advantage of the aggregated data when troubleshooting.

API Monitoring lets you:

  * Maintain the availability of your APIs.
  * Act on alerts before consumers are affected.
  * Use Apigee fault codes to speed diagnosis of issues.
  * Isolate problem areas quickly to diagnose the source of performance and latency issues.



Apigee customers can also use [Cloud Monitoring](https://cloud.google.com/monitoring/docs) tools to support API Monitoring. If you want to integrate with other monitoring systems, we recommend that you use the Monitoring API to pull metrics.

### Latency data when using API monitoring

As API monitoring is intentionally designed to scale, it does _not_ record every individual latency measurement in each transaction. Instead, [distribution buckets are used to measure latencies](https://cloud.google.com/monitoring/charts/charting-distribution-metrics). Latency buckets use predefined ranges to group observed latency values.

To learn more about using API Monitoring for your APIs, see [API Monitoring overview](https://docs.cloud.google.com/apigee/docs/api-monitoring).

To learn more about using Monitoring along with Apigee to configure alerts, see [Setting up alerts and notification](https://docs.cloud.google.com/apigee/docs/api-monitoring/alerts-notifications).

## Apigee API Analytics

Apigee API Analytics provides historical trend analysis and detailed reporting for API call metadata. The goal of Apigee Analytics is to help you understand the long-term trends of your API traffic, so that you can make sure your APIs are supporting your business requirements, or make changes if necessary.

With Apigee API Analytics, you can choose from approximately 50 available [dimensions](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#dimensions) that specify the data you want to capture for each API call handled by a proxy. You can then create [custom reports](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/create-custom-reports) to determine how specific [API metrics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#metrics) change over time.

The analytics data captured is stored in BigQuery. You can use Apigee API Analytics to [create custom reports in Data Studio](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/data-studio), set up [asynchronous custom report jobs](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/create-custom-reports#real-time-reports-versus-report-jobs), or [export analytics data to your own Google Cloud storage repository](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/export-data), like BigQuery.If you start with Pay-as-you-go pricing, API Analytics is an optional add-on.

Here are a few of the trends that you can identify using Apigee Analytics:

  * How is your API traffic trending over time?
  * What are your top apps?
  * Who are your top developers?
  * When is API response time fastest or slowest?
  * Which geographical regions have the most API traffic?

**Note:** Apigee API Analytics is not recommended as a tool for configuring alerts.

### Latency data when using Apigee API Analytics

Observed latency in Apigee API Analytics uses an [approximate quantile](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/approximate_aggregate_functions#approx_quantiles) aggregation function on individual records stored in BigQuery. This makes the resulting data surrounding latency more precise as compared to the bucketing logic used in API Monitoring. The latency in both API Monitoring and Apigee API Analytics is measured from the Apigee runtime and does not include latency calculations from prior networking hops, including Istio.

To learn more about Apigee API Analytics, see [Apigee API Analytics overview](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview).

## Apigee access logs

[Apigee access logs](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/cloud-logging-ingress-access) can be used to troubleshoot API calls to Apigee and identify which APIs are returning particular HTTP response codes.

Apigee access logs capture logs per transaction at the ingress gateway to Apigee. This lets you filter logs based on specific HTTP codes and readily troubleshoot corner cases, such as a response status code of `0` on Istio.

To learn more about using Apigee access logs to troubleshoot your APIs, see [Apigee access logs](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/cloud-logging-ingress-access).

## Differences between data displayed by API Monitoring data and Analytics

API Monitoring and Apigee API Analytics use different pipelines to access API data. As a result, you may see some discrepancies between the data displayed by Apigee API Analytics dashboards and the data available in API Monitoring.

### Timeliness and accuracy

In general, the data displayed by Apigee API Analytics is more accurate, but may be slightly delayed (by less than an hour) compared to the data displayed by API Monitoring.

### Data retention

Apigee API Analytics retains data for a longer time period than API Monitoring, making it more suitable for analysis of long-term trends.

The data retention periods for Analytics and API Monitoring are as follows:

  * Analytics

    * Standard: 60 days
    * Enterprise: 90 days
    * Enterprise +: 14 months
  * API Monitoring: 1 month


**Note:** The default retention period of one month for API Monitoring can be extended by changing the retention period in Cloud Monitoring. For more information, see [Data retention](https://docs.cloud.google.com/monitoring/quotas#data_retention_policy). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
