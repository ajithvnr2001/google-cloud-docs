---
url: https://docs.cloud.google.com/cluster-director/docs/quotas/
title: Cluster Director quotas and system limits \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:25:03.601094+00:00
---

# Cluster Director quotas and system limits  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Resources ](https://docs.cloud.google.com/cluster-director/docs/resources)



Send feedback 

#  Cluster Director quotas and system limits Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

## Quotas for required services

To successfully create clusters in Cluster Director, you must first obtain sufficient quota for both of the following resource categories:

  * Quota for sending requests to the Cluster Director API.

  * Quota for the required compute, storage, and networking services that your clusters use.




Otherwise, you encounter errors. To view quota values for one or more resources, see [View and manage quotas](https://docs.cloud.google.com/docs/quotas/view-manage).

The following sections describe the necessary service quotas that you must have to create, view, update, or delete clusters in Cluster Director.

### Quotas for the Cluster Director API

The Cluster Director API uses quotas to control how often you can send requests to the API, as well as the number of active clusters that you can have in your project.

The available quotas for the Cluster Director API are as follows:

Quota name | Description  
---|---  
Cluster Director clusters per region | Restricts the total number of active clusters that can be in your project and per region.  
Create requests per minute per region | Restricts how often you can send requests to the [ `clusters.create` method](https://docs.cloud.google.com/cluster-director/docs/reference/rest/v1/projects.locations.clusters/create) per minute and per region.   
Delete requests per minute per region | Restricts how often you can send requests to the [ `clusters.delete` method](https://docs.cloud.google.com/cluster-director/docs/reference/rest/v1/projects.locations.clusters/delete) per minute and per region.   
Get requests per minute per region | Restricts how often you can send requests to the [ `clusters.get` method](https://docs.cloud.google.com/cluster-director/docs/reference/rest/v1/projects.locations.clusters/get) per minute and per region.   
List requests per minute per region | Restricts how often you can send requests to the [ `clusters.list` method](https://docs.cloud.google.com/cluster-director/docs/reference/rest/v1/projects.locations.clusters/list) per minute and per region.   
Update requests per minute per region | Restricts how often you can send requests to the [ `clusters.patch` method](https://docs.cloud.google.com/cluster-director/docs/reference/rest/v1/projects.locations.clusters/patch) per minute and per region.   
  
### Quotas for compute, storage, and networking services

Cluster Director relies on the following underlying services to deploy cluster components. You must have sufficient quota for all of the following:

  * **Compute Engine** : you must have sufficient Compute Engine quota for creating Compute Engine instances and any resources that are attached to your compute instances, such as GPUs or Local SSD disks. This quota includes regional quota, which controls the number of compute instances that you can create in a region.

**Note:** If you use future reservations for capacity blocks or future reservations in calendar mode to obtain compute resources, then you don't need to request quota. For more information, see [Capacity overview](https://docs.cloud.google.com/cluster-director/docs/obtain-capacity).

For more information, see the [quotas and system limits for Compute Engine](https://docs.cloud.google.com/compute/quotas-limits).

  * **Filestore** : you must have sufficient Filestore quota to create Filestore instances in your cluster. Filestore instances are mandatory for creating Slurm clusters in Cluster Director.

For more information, see the [quotas and system limits for Filestore](https://docs.cloud.google.com/filestore/docs/limits).

  * **Networking** : you must have sufficient networking quota to create Virtual Private Cloud (VPC) networks, subnets, external IP addresses, and configure firewall rules that are necessary for cluster communication and access.

For more information, see the [quotas and system limits for VPC](https://docs.cloud.google.com/vpc/docs/quota).




## Quotas for optional storage services

If you plan to use optional storage services in your cluster besides a mandatory Filestore instance, then you must verify that you have sufficient quota for any of the following services:

  * **Cloud Storage** : you must have sufficient Cloud Storage quota to use Cloud Storage buckets as a storage service.

For more information, see the [quotas and system limits for Cloud Storage](https://docs.cloud.google.com/storage/quotas).

  * **Google Cloud Managed Lustre** : you must have sufficient Managed Lustre quota to use Managed Lustre instances as a storage service. If you use the [Dynamic tier](https://docs.cloud.google.com/managed-lustre/docs/performance-tiers#dynamic_tier), then you must allocate the `dynamic_tier_capacity` quota for an existing VPC network.

For more information, see the [quotas and system limits for Managed Lustre](https://docs.cloud.google.com/managed-lustre/docs/quotas).

  * **Hyperdisk pools** : you must have sufficient Compute Engine storage pool quota for the boot disks in your compute and login nodesets.

For more information, see the [quotas and system limits for Compute Engine storage pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools#hdsp-limits).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
