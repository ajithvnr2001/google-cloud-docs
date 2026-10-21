---
url: https://docs.cloud.google.com/app-hub/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 App Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:05:36.142827+00:00
---

# Quotas and limits  |  App Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Resources ](https://docs.cloud.google.com/app-hub/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to App Hub.

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

**Note:** Quotas are the same for host projects and management projects. To learn about the differences between these projects in App Hub, see [Key concepts](https://docs.cloud.google.com/app-hub/docs/key-concepts).

There are also _system limits_ on App Hub resources. System limits can't be changed. 

## Allocation quotas

App Hub enforces the following usage limits:

Resource | Description | Limit | Scope  
---|---|---|---  
Service project | Maximum number of projects that can be attached to a host project. | 25 | Per host project  
Regional applications | Maximum number of regional applications that can be created in a region in the host project or management project. | 100 | In a single region per host project or management project  
Regional registered services | Maximum number of services that can be registered into a regional application in the host project or management project. | 500 | In a single region per application per host project or management project  
Regional registered workloads | Maximum number of workloads that can be registered into a regional application in the host project or management project. | 500 | In a single region per application per host project or management project  
Global applications | Maximum number of global applications that can be created in the host project or management project. | 100 | Per host project or management project  
Global registered services | Maximum number of services that can be registered into a global application in the host project or management project. | 500 | Globally per application per host project or management project  
Global registered workloads | Maximum number of workloads that can be registered into a global application in the host project or management project. | 500 | Globally per application per host project or management project  
  
## Rate quotas

The following quotas apply to App Hub requests:

Quota | Description | Value | Scope  
---|---|---|---  
API requests per minute | Maximum number of requests that can be made from a host project, management project, or service project. This is a project-wide aggregation of global and regional requests per minute. | 12000 | Per host project, service project, or management project  
Regional API requests per minute | Maximum number of regional requests that can be made from a host project, management project, or service project. | 1200 | In a single region per host project or management project  
API requests per minute | Maximum number of global requests that can be made from a host project, management project, or service project. | 1200 | Globally per host project or management project  
  
## Observability quotas

The following quotas apply to Google Cloud Observability features when used with App Hub:

Resource | Description | Quota | Limit | Scope  
---|---|---|---|---  
Projects per metrics scope | The number of projects that can be included in a metrics scope for application monitoring. | 375 | 3500 | Per metrics scope  
**Note:** When you use an app-enabled folder, App Hub attempts to synchronize the projects in the folder with the metrics scope. If the number of projects in your folder exceeds the metrics scope quota, some projects might not be included, and you might not see all of your application's metrics. You can request a quota increase for your metrics scope. For more information, see [Metrics scopes for app-enabled folders](https://docs.cloud.google.com/monitoring/settings/metrics-scope-app-enabled-folders).

## Edit your quota

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
