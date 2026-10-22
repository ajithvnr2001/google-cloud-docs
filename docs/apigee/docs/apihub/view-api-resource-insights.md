---
url: https://docs.cloud.google.com/apigee/docs/apihub/view-api-resource-insights/
title: View API resource insights \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:55:06.419057+00:00
---

# View API resource insights  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/view-api-resource-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  View API resource insights Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

This page describes the API resource insights available for each API resource in API hub. These insights are collected and analyzed using the API insights feature in API hub. For more information about API insights, see [API insights overview](https://docs.cloud.google.com/apigee/docs/apihub/api-insights-overview). 

## Before you begin

Assign the following IAM roles to your principal account: 

  * API hub API Insights Viewer (`roles/apihub.apiInsightsViewer`)
  * API hub Viewer (`roles/apihub.viewer`)



## View insights

The **Insights** tab on the **API details** page provides api-centric insights, enabling you to understand API usage patterns and adoption for a particular API. You can filter the insights based on the deployment name. 

The following insights are available for each API resource: 

  * **Summary scorecards** : the following metric scorecards are displayed to provide a quick overview of the API traffic and performance data: 
    * **Total API traffic** : the total number of API calls in the selected time period.
    * **Avg TPS** : the average number of transactions processed per second in the selected time period.

![Summary scorecards screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/acv1.png)![Summary scorecards screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/acv1.png)

  * **Total API traffic:** displays a time-series graph of the total number of API calls in the selected time period. 

![Total API traffic screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/acv2.png)![Total API traffic screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/acv2.png)

  * **Request processing latency (ms) (p50, p90, p99):** displays percentiles (p50, p90, p99) of the latency specifically during the request processing phase in milliseconds for APIs in the selected time period. 

![Request processing latency \(ms\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/acv3.png)![Request processing latency \(ms\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/acv3.png)

  * **Response processing latency (ms) (p50, p90, p99):** displays percentiles (p50, p90, p99) of the latency specifically during the response processing phase in milliseconds for APIs in the selected time period. 

![Response processing latency \(ms\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/acv4.png)![Response processing latency \(ms\) \(p50, p90, p99\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/acv4.png)

  * **API traffic per gateway** : displays a time-series graph of the total number of API calls for each gateway in the selected time period. 

![API traffic per gateway screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/acv5.png)![API traffic per gateway screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/acv5.png)

  * **API traffic (success vs. error):** displays a time-series graph comparing successful API calls to error calls in the selected time period. 

![API traffic \(success vs. error\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/acv6.png)![API traffic \(success vs. error\) screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/acv6.png)

  * **Top HTTP methods by % API traffic:** shows the HTTP methods used and the percentage of calls for each method. 

![Top HTTP methods by % API traffic screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/acv7.png)![Top HTTP methods by % API traffic screenshot](https://docs.cloud.google.com/static/apigee/docs/apihub/images/insights-metrics/acv7.png)




## Limitations

  * API insights doesn't support data ingestion for [custom plugins](https://docs.cloud.google.com/apigee/docs/apihub/plugins#plugin-types). 
  * API hub doesn't support REST APIs for the API insights feature.
  * API insights doesn't support exporting metric data to other Google Cloud services such as BigQuery, Cloud Storage, or Data Studio. 
  * Time-series charts and tables are limited to displaying the top **50** API resources. 



## Considerations

  * If the data volume is too large for a selected time range, or if you have a high number of resources (such as APIs, deployments, plugin instances, or target IPs), the UI might not be able to display the data. Consider selecting smaller time ranges for better results and keeping your resources below 1000. 



## What's next

  * Learn more about [API insights overview](https://docs.cloud.google.com/apigee/docs/apihub/api-insights-overview).
  * Learn more about [API insights dashboards](https://docs.cloud.google.com/apigee/docs/apihub/api-insights-dashboard).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
