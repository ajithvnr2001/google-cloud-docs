---
url: https://docs.cloud.google.com/apigee/docs/api-monitoring/compare/
title: Compare API Monitoring with Apigee Analytics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:59.000573+00:00
---

# Compare API Monitoring with Apigee Analytics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-monitoring/compare/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Compare API Monitoring with Apigee Analytics Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This section compares API Monitoring with [Apigee Analytics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview). While both API Monitoring and Analytics let you collect and view API data, they have different objectives, as described in the following sections:

  * API Monitoring
  * Apigee Analytics



## API Monitoring

The goal of API Monitoring is to provide real-time insights into API performance, and help you quickly diagnose and fix issues to you keep your APIs working as intended. API Monitoring displays the latest API traffic data, and sends you alerts when issues arise so you can troubleshoot them quickly.

Here are a few examples of the tasks API Monitoring enables you to perform:

  * Maintain the availability of your APIs.
  * Take appropriate actions based on alerts before consumers are affected.
  * Leverage Apigee fault codes to speed diagnosis of issues.
  * Isolate problem areas quickly to diagnose errors, performance, and latency issues, and their sources.



Apigee customers can also use [Cloud Monitoring](https://cloud.google.com/monitoring/docs) tools to support API Monitoring. If you wish to integrate with other monitoring systems, we recommend that you use the Cloud Monitoring API by default to pull metrics.

## Apigee analytics

The goal of Apigee Analytics is to help you understand the long-term trends of your API traffic, so that you can make sure your APIs are supporting your business requirements, or make changes if necessary. To study these trends, you can create [custom reports](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/create-custom-reports) to determine how specific [API metrics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-reference#metrics) are changing over time.

Here are a few of the trends that you can identify using Apigee Analytics:

  * How is your API traffic is trending over time?
  * What are your top apps?
  * Who are your top developers?
  * When is API response time fastest or slowest?
  * In what geographical regions do you see the most API traffic?



## Differences between data displayed by API Monitoring data and Analytics

API Monitoring and Analytics use different pipelines to access API data. As a result, you may see some discrepancies between data displayed by Analytics dashboards as opposed to API Monitoring. In general, data displayed by Analytics is more accurate, but may be slightly more delayed (by less than an hour), than data displayed by API Monitoring data. However, these minor differences don't affect API Monitoring's ability to keep you informed about your API's performance.

### Data retention

Apigee Analytics has longer data retention than API Monitoring, making it more suitable for analysis of long-term trends. The data retention periods for Analytics and API Monitoring are as follows:

  * API Analytics: 14 months
  * API Monitoring: 6 weeks



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
