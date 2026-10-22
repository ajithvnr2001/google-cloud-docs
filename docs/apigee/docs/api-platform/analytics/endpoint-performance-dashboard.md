---
url: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/endpoint-performance-dashboard/
title: Target performance \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:49:00.733582+00:00
---

# Target performance  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/endpoint-performance-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Target performance Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## What does this dashboard tell me?

The **Target Performance** dashboard helps you visualize traffic patterns and performance metrics for API proxy backend targets.

**Note:** **Data delay interval**  
After API calls are made to proxies, it may take up to **10 minutes** for the data to appear in dashboards, custom reports, and management API calls.

## The Target Performance dashboard

To access the Target Performance dashboard: 

In the Google Cloud console, go to the **Apigee > Analytics > API metrics > Target Performance** page.

[Go to Target Performance](https://console.cloud.google.com/apigee/analytics/target-performance)

In the Google Cloud console, go to the **Apigee > Analytics > API metrics > Target Performance** page.

[Go to Target Performance](https://console.cloud.google.com/apigee/analytics/target-performance)

Select an **Environment or Hostname** and one or **All** target IP addresses in the **Target IP address** list. Selecting **All** shows charts for all target endpoints, including aggregated data for endpoints. Selecting a single proxy shows charts with data for that proxy only.

If desired, change the default time range. For example, you can view data for the last day or the last 14 days.

The **Target Performance** dashboard shows aggregate metrics for each chart, such as the total traffic per target IP address and the average response time across endpoints, on the right of the chart.

![The Target Performance dashboard includes charts for metrics such as traffic by
    target and traffic composition.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/target-perf-3.png)

## What does this dashboard measure?

  * Traffic by Target
  * Traffic
  * Response Time
  * Target Errors
  * Payload Size



### Traffic by Target

Metric | Description  
---|---  
**All Targets Traffic** | Measures the total amount of traffic that passes from Apigee to all backend targets.  
**<_Target name_ >** |  Measures the total amount of traffic that passes from Apigee to the specified backend target.  
  
### Traffic

Metric | Description  
---|---  
**Total Traffic** | Measures the total amount of traffic that passes from Apigee to all backend targets. Same as All Targets Traffic.  
**Errors** | The total number of requests to backend targets that resulted in an unsuccessful response. Error responses do not count.   
**Success** | The total number of all requests to backend targets that are successful (that do not return an error).  
  
### Response Time

See also this interesting article on the Apigee Community site: [When can the Average Total Response Time be less than the Average Target Response Time?](https://discuss.google.dev/t/when-can-the-average-total-response-time-be-less-than-the-average-target-response-time/17793.html)

Metric | Description  
---|---  
**Average Time** |  The average of the Total Response Time measured for all API calls made to an Apigee organization environment. The Total Response Time is the amount of time it takes for an API call to Apigee to return (in milliseconds). Or, put another way, total response time is the time measured from when an entire API call is received on Apigee to the time Apigee begins sending a response back to the client app.   
**Average Target Time** |  The average number of milliseconds that it takes from the point the last byte of a request is sent from Apigee to a backend target to the time Apigee receives the last byte of the response. It's basically measuring how much time the API call spends on the target system.   
**Average Proxy Time** |  This value is calculated as the Total Response Time minus the Target Response Time. It's basically a measure of how much time the API call spends flowing through Apigee itself (in milliseconds).   
  
### Target Errors

Metric | Description  
---|---  
**Total Errors** | Measures the total number of errors sent from backend targets to Apigee.  
**3XX Errors** | Measures the total number of HTTP 3XX sent from backend targets to Apigee.  
**4XX Errors** | Measures the total number of HTTP 4XX errors sent from backend targets to Apigee.  
**5XX Errors** | Measures the total number of HTTP 5XX sent from backend targets to Apigee.  
  
### Payload Size

Metric | Description  
---|---  
**Total Payload Size** | The total payload size for all requests and responses between Apigee and backend targets.  
**Request Payload Size** | The total payload size for all requests sent from Apigee to backend targets.  
**Response Payload Size** | The total payload size for all responses sent from backend targets to Apigee.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
