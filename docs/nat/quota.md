---
url: https://docs.cloud.google.com/nat/quota/
title: Quotas and limits \u00a0|\u00a0 Cloud NAT \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:36:36.650618+00:00
---

# Quotas and limits  |  Cloud NAT  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nat/quota/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NAT ](https://docs.cloud.google.com/nat/docs)
  * [ Resources ](https://docs.cloud.google.com/nat/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quotas and limits

This document lists the quotas and system limits that apply to Cloud NAT.

  * _Quotas_ have default values, but you can typically request adjustments.
  * _System limits_ are fixed values that can't be changed.



A given quota or limit is calculated per resource. Quotas and limits may be _per project_ , _per network_ , _per region_ , or per another resource. NAT IP addresses can't be shared between NAT gateways. To change a quota, see requesting additional quota.

Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on Cloud NAT resources. System limits can't be changed. 

## Quotas

For quotas that affect Cloud NAT, see the Cloud Router [quotas](https://docs.cloud.google.com/network-connectivity/docs/router/quotas) page.

## Limits

Item | Limit | Notes  
---|---|---  
NAT gateways | 50 per Cloud Router | Each network supports up to 5 Cloud Router instances per region, so you can have up to 250 Cloud NAT gateways per region per Virtual Private Cloud (VPC) network. For Cloud Router quotas, see the [Cloud Router documentation](https://docs.cloud.google.com/network-connectivity/docs/router/quotas).  
NAT IP addresses per gateway | 300 manual addresses 2,500 auto-allocated addresses | The maximum number of external IP addresses that you can have on a NAT gateway. However, this value depends on the [static IP addresses](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_static_addresses) and [in-use IP addresses](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/regional_in_use_addresses) VPC [per-project](https://docs.cloud.google.com/vpc/docs/quota#per_project) quotas.  
Subnet ranges | 50 per gateway | The maximum number of subnets that you can associate with a gateway when you configure a custom list of subnet ranges. The number of subnet ranges might be more than the limit because each subnet can have a primary IPv4 range and one or more secondary ranges. If you have configured NAT for primary ranges for all subnets or primary and secondary ranges for all subnets, this limit doesn't apply.  
NAT rules | 150 per gateway 2,500 per Cloud Router | If this limit is exceeded, the API returns an error.  
Active IP addresses per NAT rule | 300 |   
Private NAT subnets | 50 per gateway | The maximum number of subnets that you can reserve for use as the source NAT ranges for Private NAT. These subnets have a purpose of `PRIVATE_NAT`.  
Characters in CEL expressions per rule | 2,048 |   
Characters in CEL expressions per Cloud Router instance | 500,000 |   
  
## Considerations

  * Some servers such as legacy DNS servers require UDP port randomization among 64,000 ports for enhanced security. Because Cloud NAT selects a random port from one of 64 or a user-configured number of ports, it is best to assign an external IP address to these servers instead of using Cloud NAT. Because Cloud NAT doesn't allow connections initiated from outside, most of these servers are required to use an external IP address anyway.

  * Cloud NAT isn't available for legacy networks.

  * Cloud NAT doesn't provide application-level gateway (ALG) capabilities—Cloud NAT doesn't update the IP address and port information in the packet data for application layer protocols such as FTP and SIP.

  * Cloud NAT gateways implement NAT connection tracking tables for each VM network interface on which it provides NAT services. Entries in each connection tracking table are 5-tuple hashes for the gateway's supported protocols.

The maximum number of connection tracking table entries for all NAT connections that are associated with a VM depends on its number of vCPUs and the type of NAT translation, as described in the following table. Each maximum covers connections, in aggregate, for all protocols that the gateway supports, across all network interfaces of the VM.

vCPUs | Maximum number of NAT connections per VM  
---|---  
7 or fewer | 65,535  
8 to 15 | 
    * 65,535 or
    * 98,3021  
16 or more | 
    * 65,535 or
    * 131,0701  
  
1 This limit applies only if all NAT connections that are associated with the VM are NAT44. 

Entries in each connection tracking table persist for about as long as the relevant NAT timeout. For more information about NAT timeouts, see [NAT timeouts](https://docs.cloud.google.com/nat/docs/tune-nat-configuration#nat-timeouts).

  * Small idle connection timeouts might not work.

NAT mappings are checked every 30 seconds for expiration and configuration change. Even if a connection timeout value of 5 seconds is used, the connection may not be available for up to 30 seconds in the worst case, and 15 seconds in the average case.




## Manage quotas

Cloud NAT enforces quotas on resource usage for various reasons. For example, quotas protect the community of Google Cloud users by preventing unforeseen spikes in usage. Quotas also help users who are exploring Google Cloud with the [free tier](https://docs.cloud.google.com/free/docs/gcp-free-tier) to stay within their trial. 

All projects start with the same quotas, which you can change by requesting additional quota. Some quotas might increase automatically based on your use of a product.

### Permissions

To view quotas or request quota increases, Identity and Access Management (IAM) principals need one of the following roles. 

Task | Required role  
---|---  
Check quotas for a project | One of the following: 

  * Project [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)
  * Project [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)
  * [Quota Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement) (`roles/servicemanagement.quotaViewer`)

  
Modify quotas, request additional quota | One of the following: 

  * Project [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)
  * Project [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)
  * [Quota Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement) (`roles/servicemanagement.quotaAdmin`)
  * A custom role with the `serviceusage.quotas.update` permission

  
  
### Check your quota

### Console

  1. In the Google Cloud console, go to the **Quotas** page. 

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. To search for the quota that you want to update, use the **Filter table**. If you don't know the name of the quota, use the links on this page instead.



### gcloud

Using the Google Cloud CLI, run the following command to check your quotas. Replace `PROJECT_ID` with your own project ID.
    
    
        gcloud compute project-info describe --project PROJECT_ID

To check your used quota in a region, run the following command:
    
    
        gcloud compute regions describe example-region
        

### Errors when exceeding your quota

If you exceed a quota with a `gcloud` command, `gcloud` outputs a `quota exceeded` error message and returns with the exit code `1`.

If you exceed a quota with an API request, Google Cloud returns the following HTTP status code: `413 Request Entity Too Large`. 

### Request additional quota

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

### Resource availability

Each quota represents a maximum number for a particular type of resource that you can create, if that resource is available. It's important to note that quotas _don't_ guarantee resource availability. Even if you have available quota, you can't create a new resource if it is not available.

For example, you might have sufficient quota to create a new regional, external IP address in a given region. However, that is not possible if there are no available external IP addresses in that region. Zonal resource availability can also affect your ability to create a new resource.

Situations where resources are unavailable in an entire region are rare. However, resources within a zone can be depleted from time to time, typically without impact to the service level agreement (SLA) for the type of resource. For more information, review the relevant SLA for the resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
