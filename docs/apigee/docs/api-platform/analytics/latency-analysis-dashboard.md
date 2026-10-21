---
url: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/latency-analysis-dashboard/
title: Latency analysis dashboard \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:58:49.770499+00:00
---

# Latency analysis dashboard  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/analytics/latency-analysis-dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Latency analysis dashboard Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Note:** This feature may not be available in all Apigee plans. To see which pricing plan includes this feature, see [ https://cloud.google.com/apigee/pricing/](https://cloud.google.com/apigee/pricing/).

## What does this dashboard tell me?

The Latency Analysis dashboard can alert you to any latency issues your API proxies may be experiencing. It displays latency measurements down to the window of a minute, highlighting the median, 95th percentile, and 99th percentile values.

The median value tells you the point at which half of your traffic is experiencing latency that is less than this value and half of your traffic is experiencing latency that is greater than this value. For example, if the median response time latency for your selected API proxy is 62 ms, it means that half of the responses from this API proxy take less than 62 ms. It also means that half of the responses from this API proxy take more than 62 ms.

The 95th percentile and 99th percentile values tell you the point at which 95% and 99% of your traffic is experiencing latency that is less than these values. Or rather more importantly, it can point out outlying behavior, telling you that 5% and 1% of your traffic is experiencing latency values that are out-of-range.

**Note:** **Data delay interval**  
After API calls are made to proxies, it may take up to **10 minutes** for the data to appear in dashboards, custom reports, and management API calls.

## The Latency Analysis dashboard

To access the Latency Analysis dashboard: 

In the Google Cloud console, go to the **Apigee > Analytics > API metrics > Latency Analysis** page.

[Go to Latency Analysis](https://console.cloud.google.com/apigee/analytics/latency)

The **Latency Analysis** view is shown:

![A dashboard that shows charts for response time, target response time, request processing
    latency, and response processing latency.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/latencyv2.png)

## What does this dashboard measure?

See also this interesting article on the Apigee Community site: [When can the Average Total Response Time be less than the Average Target Response Time?](https://discuss.google.dev/t/when-can-the-average-total-response-time-be-less-than-the-average-target-response-time/17793)

Metric | Description  
---|---  
Response Time | Total number of milliseconds it took to respond to a call. This time includes the Apigee API proxy overhead and your target server time.  
Target Response Time | Number of milliseconds it took your target server to respond to a call. This number tells you how your own servers are behaving.  
Request Processing Latency |  Number of milliseconds from the time when a call reaches the selected API proxy to the time when Apigee sends the call to your target server. Add the request and response latencies to calculate the final overhead the API proxy added to the call.  
Response Processing Latency |  Number of milliseconds from the time when the API proxy receives your target server’s response to the time when Apigee sends the response to the original caller. Add the request and response latencies to calculate the final overhead the API proxy added to the call. **Note:** It is expected that the internal Istio ingress load balancer used by Apigee will add approximately 5-10ms to the 99th percentile latency.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
