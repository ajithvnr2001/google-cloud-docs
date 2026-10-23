---
url: https://docs.cloud.google.com/workstations/docs/quotas/
title: Quotas and system limits \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:45.482877+00:00
---

# Quotas and system limits  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Resources ](https://docs.cloud.google.com/workstations/docs/resources)



Send feedback 

#  Quotas and system limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Cloud Workstations.

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

There are also _system limits_ on Cloud Workstations resources. System limits can't be changed. 

## Allocation quotas

These allocation quotas are per region per project and are released when you release the resource. These quotas don't reset over time.

The default Cloud Workstations resource limits per region per project are as follows:

Default allocation quotas | Value  
---|---  
Workstation clusters | 3  
Workstation configurations | 100  
Workstations | 9000  
  
## Rate quotas for API requests

The following quotas specify the per project rate quota for Cloud Workstations API read and write requests:

Default rate quotas | Value  
---|---  
Read requests in QPS | 180  
Write requests in QPS | 60  
  
## System limits

Cloud Workstations enforces the following system limits, which can't be changed:

System limits | Value  
---|---  
Concurrently running workstations per workstation cluster | 3000  
  
To restrict the number of workstations per configuration, see [Limit the number of workstations per developer](https://docs.cloud.google.com/workstations/docs/limit-workstations-per-developer).

## Quotas needed for workstation VMs

For the virtual machines (VMs) that workstations run on, you must allocate the following resources:

  * CPU quotas
  * Persistent Disk quotas
  * If the VMs have external IP addresses, you need IP address quotas
  * Sufficient space in your Virtual Private Cloud (VPC) for the internal IP address for the VM

To use a workstation configuration, make sure that there are sufficient IP addresses available in your VPC. To calculate how many IP addresses need to be available, add these values:

    * Start by adding `1` for each concurrently running workstation that you expect to create using this configuration.
    * If you enabled [**Quick start workstations**](https://docs.cloud.google.com/workstations/docs/create-configuration#configure_basics), also add the value that you specified for the **Quick start pool size**.
    * Lastly, add `1` for the IP address used to establish a connection between the Cloud Workstations controller and your VPC.



## Request a quota adjustment

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
