---
url: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/cache-performance-dashboard/
title: Cache performance dashboard \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:22.404406+00:00
---

# Cache performance dashboard  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/cache-performance-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Cache performance dashboard Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## What does this dashboard tell me?

The Cache Performance dashboard collects data from the [ResponseCache policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/response-cache-policy). This dashboard does not collect data from the [LookupCache](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/lookup-cache-policy) or [PopulateCache](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/populate-cache-policy) policies. 

The Cache Performance dashboard lets you see at a glance the value of the response cache. The dashboard helps you visualize the benefit of the response cache in terms of lower latency and reduced load backend servers. 

**Note:** **Data delay interval**  
After API calls are made to proxies, it may take up to **10 minutes** for the data to appear in dashboards, custom reports, and management API calls.

## The Cache Performance dashboard

To access the Cache Performance dashboard: 

In the Google Cloud console, go to the **Apigee > Analytics > API metrics > Cache Performance** page.

[Go to Cache Performance](https://console.cloud.google.com/apigee/analytics/cache-performance)

Select an **Environment or Hostname** and one or **All** proxies in the **Proxy** list. Selecting **All** shows charts for all proxies, including aggregated data for proxies. Selecting a single proxy shows charts with data for that proxy only.

If desired, change the default time range. For example, you can view data for the last day or the last 14 days.

The **Cache Performance** dashboard shows aggregate metrics for each chart, such as the average cache hit rate, on the right of the chart.

![The Cache Performance dashboard includes charts for metrics such as cache hits and
    cache hit rate.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/cache-performance.png)

## What does this dashboard measure?

Metric | Description  
---|---  
Average cache hit rate | The rate of calls hitting the cache measured against total API traffic.   
Cache hits by API proxy | Sum of calls hitting the cache, broken down by API proxy.   
| Average time with cache | The average amount of time for an API call when it hits the cache.   
Average time without cache | The average amount of time for an API call when it does not hit the cache.   
**Note:** The performance ratios may appear incorrect for the first few minutes for new data. This is because with a small number of data points, there can be a difference in the number of data points being compared to create the ratios. This inconsistency will resolve itself within a few minutes as it collects more data points. If the performance ratios still appear incorrect, refresh the page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
