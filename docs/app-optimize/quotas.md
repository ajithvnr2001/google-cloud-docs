---
url: https://docs.cloud.google.com/app-optimize/quotas/
title: Quotas and system limits \u00a0|\u00a0 App Optimize \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:36.400412+00:00
---

# Quotas and system limits  |  App Optimize  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-optimize/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ App Optimize ](https://docs.cloud.google.com/app-optimize)
  * [ Resources ](https://docs.cloud.google.com/app-optimize/quotas)



Send feedback 

#  Quotas and system limits Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document lists the quotas and system limits that apply to App Optimize API.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on App Optimize API resources. System limits can't be changed. 

## System limits

The following system limits apply to App Optimize API resources and operations:

System limit | Description | Value  
---|---|---  
Report expiry | The duration after which a report resource and its associated data are automatically deleted. | 24 hours  
Default report time range | The default time range for report data if no `start_time` and `end_time` are specified in the filter. | Most recent 7 days  
Maximum rows per page | The maximum number of rows that a `ReadReport` request can return in a single page. | 1,000 rows  
Maximum response size per page | The maximum size of the response body for a single page returned by a `ReadReport` request. | 10 MB  
[Maximum concurrent requests for report data](https://docs.cloud.google.com/app-optimize/create-report#limits) | The maximum numer of concurrent requests for cost or utilization data per target project. | 10 per target project  
  
These system limits are fixed and cannot be increased.

For more information about quota policies, viewing your quotas, and managing your quotas, see the [Cloud Quotas documentation](https://docs.cloud.google.com/docs/quotas/overview).

Go to the [API dashboard](https://console.cloud.google.com/apis/dashboard) for your current API activity.

## What's next

  * Review the [App Optimize API overview](https://docs.cloud.google.com/app-optimize/overview).
  * Learn about [Google Cloud quotas](https://docs.cloud.google.com/docs/quotas).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
