---
url: https://docs.cloud.google.com/cloud-ftp/quotas/
title: Quotas and system limits \u00a0|\u00a0 Cloud FTP \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:59.914590+00:00
---

# Quotas and system limits  |  Cloud FTP  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-ftp/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud FTP ](https://docs.cloud.google.com/cloud-ftp)
  * [ Resources ](https://docs.cloud.google.com/cloud-ftp/resources)



Send feedback 

#  Quotas and system limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Cloud FTP.

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

## Quotas

There are no quotas associated with Cloud FTP.

## System limits

The following table lists the system limits that apply to Cloud FTP and the value for each system limit.

System limit | Value  
---|---  
SFTP servers per project | 1024  
Storage directory mappings per user | 10  
Public keys per user | 10  
File size per transfer | 750 GB  
Concurrent sessions per server | 500  
Multiplexed SSH sessions in a single TCP connection | 10  
CIDR blocks for an external server | 500  
Allowed projects for an internal server | 500  
Rejected projects for an internal server | 64  
Connection limit (number of Private Service Connect endpoints that can be created) per project for an internal server | 250  
  
## Cloud Storage quotas and system limits

Cloud FTP manages resources in Cloud Storage, such as objects and folders. This means that the resource naming requirements, quotas, and system limits for Cloud Storage also apply to Cloud FTP. For more information, see the following:

  * [Object naming considerations](https://docs.cloud.google.com/storage/docs/objects#naming)
  * [Folder naming considerations](https://docs.cloud.google.com/storage/docs/folders-overview#considerations)
  * [Cloud Storage quotas and limits](https://docs.cloud.google.com/storage/quotas)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
