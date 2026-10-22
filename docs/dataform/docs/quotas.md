---
url: https://docs.cloud.google.com/dataform/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:20.417103+00:00
---

# Quotas and limits  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Resources ](https://docs.cloud.google.com/dataform/docs/quotas)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Dataform.

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

There are also _system limits_ on Dataform resources. System limits can't be changed. 

## Quota replenishment

Daily quotas are replenished at regular intervals throughout the day, reflecting their intent to guide rate limiting behaviors. Intermittent refresh is also done to avoid long disruptions when quota is exhausted. More quota is typically made available within minutes rather than globally replenished once daily.

## Request a quota increase

To increase or decrease most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota).

## Cap quota usage

To learn how you can limit usage of a particular resource by specifying a smaller quota than the default, see [Cap usage](https://docs.cloud.google.com/docs/quotas/view-manage#capping_usage).

## Required permissions

To view and update your Dataform quotas in the Google Cloud console, you need the same permissions as for any Google Cloud quota. For more information, see [Quota permissions](https://docs.cloud.google.com/docs/quotas/permissions).

## Troubleshooting

For information about troubleshooting errors related to Dataform quotas and limits, see [Troubleshooting](https://docs.cloud.google.com/dataform/docs/troubleshooting).

## Dataform quotas

Dataform has the following API quotas:

Quotas | Limit  
---|---  
Total requests per project, per region | 6000/minute/project/region  
Compilation requests per project, per region | 120/minute/project/region  
File access requests per project, per region | 120/minute/project/region  
Package installation requests per project, per region | 120/minute/project/region  
Move folder requests per project, per region | 6/minute/project/region  
Move file requests per project, per region | 60/minute/project/region  
Delete folder tree requests per project, per region | 20/minute/project/region  
Workflow invocation requests per project, per region | 60/minute/project/region  
Workflow actions per execution | 5000  
  
## Quotas for services used by Dataform

Dataform uses other Google Cloud services. These services have project-level quotas, which apply when you use Dataform.

Dataform uses the following Google Cloud services that have their own quota limits:

  * [BigQuery](https://docs.cloud.google.com/bigquery/quotas)
  * [Identity and Access Management](https://docs.cloud.google.com/iam/quotas)
  * [Cloud Monitoring](https://docs.cloud.google.com/monitoring/quotas)
  * [Secret Manager](https://docs.cloud.google.com/secret-manager/quotas)



## Dataform compilation resource limits

Dataform enforces the following usage limits on compilation resources:

Usage limit | Value  
---|---  
Maximum number of actions per repository compilation | 5000  
Maximum number of dependencies per action in the compiled graph | 50  
Maximum total serialized data size of the compiled graph of actions | 20 MB  
Maximum CPU time of the compilation process | 8 seconds  
Maximum wall time of the compilation process | 30 seconds  
Maximum RSS usage of the compilation process | 200 MB  
Maximum size of NPM dependencies | 200 MB  
Maximum size of a CMEK-encrypted repository | 512 MB  
Maximum size of a workspace in a CMEK-encrypted repository | 512 MB  
  
Additionally, Dataform imposes limits on CPU and memory use during compilation. If these limits are exceeded when you compile your code, the compilation fails and Dataform throws a compilation error.

To estimate the compilation resources usage of your repository, see [Estimate compilation resources usage of your repository](https://docs.cloud.google.com/dataform/docs/best-practices-repositories#estimate-comp-resource-usage-of-repo).

Your repository might exceed the usage limits for the following reasons:

  * An infinite loop bug in the repository code.
  * A memory leak bug in the repository code.
  * Large repository size, approximately more than 1000 workflow nodes.
  * Large number of concurrent queries.

**Tip:** [Update Dataform core](https://docs.cloud.google.com/dataform/docs/manage-repository#manage-dataform-core-package) to the latest version to lower the risk of exceeding compilation limits.

For more information about repository size in Dataform, see [Overview of repository size](https://docs.cloud.google.com/dataform/docs/best-practices-repositories#overview-repo-size). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
