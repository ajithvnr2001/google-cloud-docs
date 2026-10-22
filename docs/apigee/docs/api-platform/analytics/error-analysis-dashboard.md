---
url: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/error-analysis-dashboard/
title: Error Code Analysis Dashboard \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:49:00.367388+00:00
---

# Error Code Analysis Dashboard  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/error-analysis-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Error Code Analysis Dashboard Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## What does this dashboard tell me?

The Error Code Analysis dashboard tells you about error rates for API proxies and targets. The Error Code Analysis dashboard uses:

  * The response code to calculate proxy errors

  * The target response code to calculate target errors




Errors reported on the Error Code Analysis dashboard might be different from errors reported on the [API Proxy Performance dashboard](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/api-proxy-performance-dashboard) because that dashboard calculates error rates based on the `is_error` flow variable. That variable can be explicitly set by the API proxy, so it is not related to the error codes in the proxy response or target response.

When calculating error rates:

  * A proxy can handle a target error and still return a success response. In this case, the error is counted as a target error but not as a proxy error.

  * When the target response is either success or does not exist, but the proxy responded with an error, the error is counted against the proxy. 

  * If both the proxy and target respond with an error, the error is counted on the target.




**Note:** **Data delay interval**  
After API calls are made to proxies, it may take up to **10 minutes** for the data to appear in dashboards, custom reports, and management API calls.

## The Error Code Analysis dashboard

To access the Error Code Analysis dashboard:

In the Google Cloud console, go to the **Apigee > Analytics > API metrics > Error Code Analysis** page.

[Go to Error Code Analysis](https://console.cloud.google.com/apigee/analytics/error-analysis)

Select an **Environment or Hostname** and one or **All** proxies in the **Proxy** list. Selecting **All** shows charts for all proxies, including aggregated data for proxies. Selecting a single proxy shows charts with data for that proxy only.

If desired, change the default time range. For example, you can view data for the last day or the last 14 days.

The **Error Code Analysis** dashboard shows aggregate metrics for each chart, such as the total proxy errors and total target errors, on the right of the chart.

![The dashboard contains charts for error composition, proxy errors, and target
    errors.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/error-code-analysis2.png)

## What does this dashboard measure?

  * Error Composition
  * Proxy Errors
  * Target Errors
  * Errors by Proxy
  * Errors by Target
  * Proxy Errors by Response Code
  * Target Errors by Response Code



### Error Composition

Metric | Description  
---|---  
**Total Errors** | The **total number of proxy errors + target errors** that resulted from all requests and responses seen in an Apigee organization over the specified time period. See What does this dashboard tell me? for more on how **Total Errors** , **Proxy Errors** , and **Target Errors** are calculated.  
**Proxy Errors** | The total number of proxy errors seen in an Apigee organization in the specified time period as determined by the response code. Proxy errors are measured between the time an entire request is received by Apigee from a client and the time the request is sent to the backend target.  
**Target Errors** | The total number of target errors seen in an Apigee organization in the specified time period as determined by the target response code. Target errors are measured between the time an entire request is sent by Apigee to a backend target and the time the response is returned the client app.  
  
### Proxy Errors

Metric | Description  
---|---  
**Total Proxy Errors** | The **total number of proxy errors** seen in an Apigee organization in the specified time period. Proxy errors are measured between the time an entire request is received by Apigee from a client and the time the request is sent to the backend target.  
**4XX** | Shows the number of proxy errors that resulted in HTTP 4xx errors. For a complete list of HTTP status codes, see "[Status Code Definitions](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)" in the HTTP specification.   
**5XX** | Shows the number API requests that resulted in HTTP 5xx errors. For a complete list of HTTP status codes, see "[Status Code Definitions](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)" in the HTTP specification.  
  
### Target Errors

Metric | Description  
---|---  
**Total Target Errors** | The **total number of target errors** seen in an Apigee organization in the specified time period. Target errors are measured between the time an entire request is sent by Apigee to a backend target and the time the response is returned the client app.  
**4XX** | The number of target errors that resulted in HTTP 4xx errors. For a complete list of HTTP status codes, see "[Status Code Definitions](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)" in the HTTP specification.  
**5XX** | The number of target errors that resulted in HTTP 5xx errors. For a complete list of HTTP status codes, see "[Status Code Definitions](https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html)" in the HTTP specification.  
  
### Errors by Proxy

Metric | Description  
---|---  
**<_Proxy name_ >** |  The total number of proxy errors seen in an Apigee organization in the specified time period **for each individual proxy**. Hover over the bars to see the number of errors that came from the each proxy request flow and from the target request flow, respectively.  Proxy errors are measured between the time an entire request is received by Apigee from a client and the time the request is sent to the backend target.  
  
### Errors by Target

Metric | Description  
---|---  
**<_Target name_ >** |  The total number of target errors seen in an Apigee organization in the specified time **for each individual target**. The number of calls that did not reach any target are listed in the **Target Not Contacted** column. Hover over the bars to see the number of errors that came from the each proxy response flow and from the target response flow, respectively.  Target errors are measured between the time an entire request is sent by Apigee to a backend target and the time the response is returned to the client app. The chart shows the number of errors that came from the proxy response flow and from the target response flow, respectively.   
  
### Proxy Errors by Response Code

Metric | Description  
---|---  
**<_Response Code_ >** |  The total number of proxy errors seen in an Apigee organization in the specified time **that returned each response code**. Hover over the bars to see the number of errors that returned each response code.  
  
### Target Errors by Response Code

Metric | Description  
---|---  
**<_Response Code_ >** |  The total number of target errors seen in an Apigee organization in the specified time **that returned each response code**. Hover over the bars to see the number of errors that returned each response code.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
