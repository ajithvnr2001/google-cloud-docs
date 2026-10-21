---
url: https://docs.cloud.google.com/apigee/docs/deprecations/proxyv2-targetv2-metrics/
title: ProxyV2 and TargetV2 metrics deprecation \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:24:03.965889+00:00
---

# ProxyV2 and TargetV2 metrics deprecation  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/deprecations/proxyv2-targetv2-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)



Send feedback 

#  ProxyV2 and TargetV2 metrics deprecation Stay organized with collections  Save and categorize content based on your preferences. 

The `ProxyV2` and `TargetV2` metrics suite is deprecated for Apigee hybrid installations as of April 17, 2024. The Apigee hybrid v1.12 release supports new [proxy and target metrics](https://docs.cloud.google.com/apigee/docs/api-monitoring/alerts-notifications#new-metrics) with improved performance and reliability.

Apigee hybrid users should be aware of the following: 

  * The Apigee hybrid v1.12 release supports the [ new proxy and target metrics](https://docs.cloud.google.com/apigee/docs/api-monitoring/alerts-notifications#new-metrics) by default.
  * Support for the `ProxyV2` and `TargetV2` metrics suite in Apigee hybrid v1.10 and v1.11 will end in April of 2025.



If you are upgrading to v1.12, you should begin using the [new metrics](https://docs.cloud.google.com/apigee/docs/api-monitoring/alerts-notifications#new-metrics) and [reconfigure any existing alerts](https://docs.cloud.google.com/apigee/docs/api-monitoring/alerts-notifications#metric-based-alerts). If you need additional time to transition to new metrics, you can [change the default behavior in 1.12](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/upgrade) to continue using the original metrics.

If you use v1.10 or v1.11, we recommend that you [upgrade to v1.12](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/upgrade) and adjust your alerts and notifications to use the new metrics at your earliest convenience.

## Shutdown schedule

The following table lists the shutdown schedule for the `ProxyV2` and `TargetV2` metrics suite: 

Date | Event  
---|---  
April 17, 2024 | `ProxyV2` and `TargetV2` metrics suite deprecated for Apigee hybrid v1.12.  
April 17, 2024 | Support for the `ProxyV2` and `TargetV2` metrics suite in Apigee hybrid in v1.10 and v1.11 extended for one year.  
April 17, 2025 | Support for the `ProxyV2` and `TargetV2` metrics suite shut down for all Apigee hybrid versions.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
