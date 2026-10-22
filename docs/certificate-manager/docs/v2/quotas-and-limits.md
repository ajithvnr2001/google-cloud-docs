---
url: https://docs.cloud.google.com/certificate-manager/docs/v2/quotas-and-limits/
title: Quotas and limits \u00a0|\u00a0 Certificate Manager (2nd gen) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:18.006509+00:00
---

# Quotas and limits  |  Certificate Manager (2nd gen)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-manager/docs/v2/quotas-and-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Certificate Manager ](https://docs.cloud.google.com/certificate-manager)
  * [ Certificate Manager (2nd gen) ](https://docs.cloud.google.com/certificate-manager/docs/v2/overview)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

****

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document lists the quotas and system limits that apply to Certificate Manager.

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

## System limits

The following table lists the system limits for the Certificate Manager inventory. System limits are fixed values that you can't change.

Item | System limit | Description  
---|---|---  
**List requests** | 100 requests per minute | Requests to change your inventory filters.  
**Read certificate requests** | 600 requests per minute | Requests to view a single observed certificate.  
**Certificate retention** | 30 days past expiration | Certificate Manager retains certificates until 30 days past their expiration, and then deletes them.  
**Certificate ingestion time** | 24 hours | Certificate Manager might take up to 24 hours to add certificates to the certificate inventory.  
  
## What's next

  * [How Certificate Manager (2nd gen) works](https://docs.cloud.google.com/certificate-manager/docs/v2/core-components)
  * [Compare Certificate Manager versions](https://docs.cloud.google.com/certificate-manager/docs/v2/comparison)
  * [Roles and permissions](https://docs.cloud.google.com/certificate-manager/docs/v2/roles)
  * [Monitor resources using Cloud Monitoring](https://docs.cloud.google.com/certificate-manager/docs/v2/cloud-monitoring)
  * [Troubleshoot issues](https://docs.cloud.google.com/certificate-manager/docs/v2/troubleshoot)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
