---
url: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/api-proxy-performance-dashboard/
title: API Proxy Performance \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:48:03.104328+00:00
---

# API Proxy Performance  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/api-proxy-performance-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  API Proxy Performance Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## What does this dashboard tell me?

The Proxy Performance dashboard helps you see API proxy traffic patterns and processing times. Use is to visualize how much traffic your APIs generate and how long it takes for API calls to be processed, from the time they are received by Apigee until they are returned to the client app.

**Note:** **Data delay interval**  
After API calls are made to proxies, it may take up to **10 minutes** for the data to appear in dashboards, custom reports, and management API calls.

## The API Proxy Performance dashboard

To access the Proxy Performance dashboard:

  1. In the Google Cloud console, go to the **Apigee > Analytics > API metrics > API Proxy Performance** page.

[Go to API Proxy Performance](https://console.cloud.google.com/apigee/analytics/proxy-performance)

  2. Select an **Environment or Hostname** and one or **All** proxies in the **Proxy** list. Selecting **All** shows charts for all proxies including aggregated data for proxies. Selecting a single proxy shows charts with data for that proxy only.
  3. If desired, change the default time range. For example, you can view data for the last day or the last 14 days.



The **API Proxy Performance** view is shown. Aggregate metrics for each chart, such as the average transactions per second (**Average TPS**) and maximum transactions per second (**Peak TPS**) are shown to the right of the chart

![](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/proxy-performance-peaktps.png)

## What does this dashboard measure?

This dashboard includes these charts:

  * Average transactions per second (TPS)
  * Peak transactions per second (TPS)
  * Traffic
  * Average Response Time
  * Traffic by Proxy
  * Average Response Time by Proxy

**Note:** This `client.received.start.timestamp` time value is used to calculate traffic metrics for API proxies in the analytics dashboards. For more information, see the [client](https://docs.cloud.google.com/apigee/docs/api-platform/reference/variables-reference#client) flow variable reference.

### Average transactions per second (TPS)

Metric | Description  
---|---  
**Average TPS** | The average number of API requests and resulting responses per second.  
  
### Peak transactions per second (TPS)

Metric | Description  
---|---  
**Peak TPS** | The maximum number of API requests and resulting responses per second (which is aggregated by minute or hour or day, depending on the time range selected).  
  
### Traffic

Metric | Description  
---|---  
**Total Traffic** | The total number of API requests received by Apigee for an API environment in an organization.  
**Traffic Success** | The total number of requests that resulted in a successful response. Error responses do not count.   
**Traffic Errors** | The total number of all API requests that are unsuccessful, that is, the request does not deliver a response as desired by the end user. The count includes both Proxy and Target errors.  
  
### Average Response Time

See also this interesting article on the Apigee Community site: [When can the Average Total Response Time be less than the Average Target Response Time?](https://discuss.google.dev/t/when-can-the-average-total-response-time-be-less-than-the-average-target-response-time/17793)

Metric | Description  
---|---  
**Average Response Time** |  The average of the Total Response Time measured for all API calls made to an Apigee organization environment. The Total Response Time is the amount of time it takes for an API call to Apigee to return (in milliseconds). Or, put another way, total response time is the time measured from when an entire API call is received on Apigee to the time Apigee begins sending a response back to the client app.  This chart measures the average for all proxies. For individual proxies, see the Average Response Time by Proxy chart below.   
**Average Proxy Response Time** |  This value is calculated as the average of the Total Response Time minus the Target Response Time for all API calls made to an Apigee organization environment.  It's basically a measure of how much time the API calls spend flowing through Apigee itself (in milliseconds).   
**Average Target Response Time** |  The average number of milliseconds that it takes from the point the last byte of a request is sent from Apigee to a backend target to the time Apigee receives the last byte of the response. It's basically measuring how much time the API call spends on the target system.   
  
Average proxy response time is calculated as the difference between the averages of total response time and target response time. The expectation is that total response time is always greater than the target response time. However, there are also calls which are handled by the proxy itself - preflight requests, cached responses, Oauth tokens etc which do not reach the backend system. These "faster" calls by the proxy reduce the average Total Response time without reducing the Target response time. Hence the average total response time may not always be greater than the average target response time which could result in negative values being seen for proxy response time. When you look at larger TPS without zooming in the time scale too much, these exceptions will not hold much weight and hence give you more accurate and actionable data.

You obtain the most meaningful average response data when a large number of requests are collected over a long period of time, rather than from just a few requests collected over a short period of time. If you only observe a small number of requests that come in over a short time period, there's a chance that even one call that does not go to the target will result in a negative average proxy response time. When evaluating average response times, it's best to view longer time frames that have high traffic.

### Traffic by Proxy

Metric | Description  
---|---  
**<_Proxy name_ >** | For the specified API proxy, the number of recorded API requests and responses.  
  
### Average Response Time by Proxy

Metric | Description  
---|---  
**<_Proxy name_ >** |  For the specified API proxy, the average of the Total Response Time measured for all API calls made to an Apigee environment. The Total Response Time is the amount of time it takes for an API call to Apigee to return (in milliseconds). Hover over the graph to see the total amount of time spent on the proxy side and the target side, as well as the average.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
