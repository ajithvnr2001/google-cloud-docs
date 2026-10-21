---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/quotas/
title: Quotas \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:05.567003+00:00
---

# Quotas  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Resources ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/quotas)



Send feedback 

#  Quotas Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

## Total requests quotas

The following quotas apply to AML AI requests:

Quota | Value  
---|---  
Requests per second per project per region | 100  
Requests per second per organization per region | 100  
Number of parties used in requests to [ `projects.locations.instances.engineConfigs.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs/create) per day per project | 55,000,000  
Number of parties used in requests to [ `projects.locations.instances.engineConfigs.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs/create) per day per organization | 55,000,000  
Number of parties used in requests to [`projects.locations.instances.models.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models/create) per day per project | 55,000,000  
Number of parties used in requests to [`projects.locations.instances.models.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models/create) per day per organization | 55,000,000  
Number of parties used in requests to [ `projects.locations.instances.backtestResults.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults/create) multiplied by the number of backtest periods per day per project | 55,000,000  
Number of parties used in requests to [ `projects.locations.instances.backtestResults.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults/create) multiplied by the number of backtest periods per day per organization | 55,000,000  
Number of registered parties used in requests to [ `projects.locations.instances.predictionResults.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults/create) multiplied by the number of prediction periods per day per project | 55,000,000  
Number of registered parties used in requests to [ `projects.locations.instances.predictionResults.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults/create) multiplied by the number of prediction periods per day per organization | 55,000,000  
Number of copy model requests per day per project.  | 100  
Number of copy model requests per day per organization.  | 100  
  
## Concurrent request quotas

The following quotas apply to concurrent requests:

Quota | Value  
---|---  
[Tuning requests](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs/create) per project per region | 1  
[Training requests](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models/create) per project per region | 5  
Inference requests ([ `projects.locations.instances.backtestResults.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.backtestResults/create) and [ `projects.locations.instances.predictionResults.create`](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.predictionResults/create) combined) per project per region | 5  
  
## Collection size quotas

The following quotas apply to AML AI collections. These quotas don't reset over time and instead are released when you delete a resource.

Quota | Value  
---|---  
[Instances](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances) per project per region | 10  
[Datasets](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.datasets) per project per region | 1000  
[EngineConfigs](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.engineConfigs) per project per region | 2000  
[Models](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances.models) per project per region | 1000  
  
## Registered parties allocation limit

Quota | Value  
---|---  
[Registered parties](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/rest/v1/projects.locations.instances/importRegisteredParties) per project per region | 1,500,000  
  
## Request a quota increase

AML AI does not currently support increasing quotas via the Google Cloud console, to request a quota increase, please reach out to [support](https://docs.cloud.google.com/support).

To decrease most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota).

## Set up quota alerts

You can set up quota alerts to get notifications when quota usage reaches a defined threshold. For more information, see [Set up quota usage alerts in the Quotas page](https://docs.cloud.google.com/docs/quotas/monitor).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
