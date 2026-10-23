---
url: https://docs.cloud.google.com/network-connectivity/docs/router/quotas/
title: Quotas and limits \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:39:53.102275+00:00
---

# Quotas and limits  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Resources ](https://docs.cloud.google.com/network-connectivity/docs/router/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quotas and limits

This document lists the quotas and system limits that apply to Cloud Router.

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

There are also _system limits_ on Cloud Router resources. System limits can't be changed. 

## Quotas

To change a quota, see Request additional quota.

This table covers important quotas per project. For other quotas, see the [Google Cloud console **Quotas & System Limits** page](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com).

Item | Quota | Notes  
---|---|---  
Cloud Routers per project | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/routers) | Regardless of quota, each network is limited to five Cloud Routers per region. See Limits.  
Unique Cloud Router dynamic route prefixes from own region per region per VPC network The maximum number of assured unique destination prefixes for learned routes to be applied to subnets in a given region by all Cloud Routers in _the same_ region. This is referred to as a region's _from-own-region_ quota. | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/cloud_router_prefixes_from_own_region_per_region_per_vpc_network) |  Both IPv4 and IPv6 prefixes count toward this quota. All learned routes count toward this quota, including [custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes) and BGP-received routes. Routes are grouped by unique destinations. Routes with identical destinations but different next hops only count as a single destination. Routes with identical destinations and identical next hops also only count as a single destination. For networks in _global dynamic routing mode_ , it is possible to reach one of the unique dynamic route prefix quotas without reaching the other. If either of the quotas has been exceeded, you may experience intermittent connectivity issues when routes are dropped. For details, see the learned route example. For more information about these quotas, including metrics that you can use to understand your current usage, see [Troubleshoot BGP routes and route selection](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-routes#check-quotas-and-limits).  
_Only applicable to VPC networks in[global dynamic routing mode](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#dynamic-routing-mode)._ Unique Cloud Router dynamic route prefixes from other regions per region per VPC network The maximum number of assured unique destinations for learned routes that can be applied to subnets in a given region by Cloud Routers from _different_ regions. This is referred to as a region's _from-other-regions_ quota. | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/cloud_router_prefixes_from_other_regions_per_region_per_vpc_network) |  Both IPv4 and IPv6 prefixes count toward this quota. All learned routes count toward this quota, including [custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes) and BGP-received routes. Routes are grouped by unique destinations. Routes with identical destinations but different next hops only count as a single destination. Routes with identical destinations and identical next hops also only count as a single destination. For networks in _global dynamic routing mode_ , it is possible to reach one of the unique dynamic route prefix quotas without reaching the other. If either of the quotas has been reached, you might experience intermittent connectivity issues when routes are dropped. For details, see the learned route example. For more information about these quotas, including metrics that you can use to understand your current usage, see [Troubleshoot BGP routes and route selection](https://docs.cloud.google.com/network-connectivity/docs/router/support/troubleshoot-bgp-routes#check-quotas-and-limits).  
  
## Limits

The following limits for Cloud Router apply to Virtual Private Cloud (VPC) networks. Unless otherwise stated, these limits cannot be increased.

Item | Limit | Notes  
---|---|---  
Maximum number of Cloud Routers per combination of VPC network and region | 5 | If you have sufficient project quota, you can create up to five Cloud Routers in a given VPC network and region.   
Maximum number of BGP peers for each Cloud Router in a given VPC network and region | 128 | The BGP peer can be any of the following: 

  * A [ Cloud VPN tunnel using dynamic routing](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/choosing-networks-routing#dynamic-routing)
  * A VLAN attachment for any of the following: 
    * [ Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview)
    * [ Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview)
    * [ Cross-Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview)
  * A [ Router appliance within Network Connectivity Center](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview)

  
Maximum number of prefixes that Cloud Router accepts from a single BGP peer | 5,000 | If a BGP peer advertises more than 5,000 prefixes, Cloud Router resets the BGP session.  
For a given Cloud Router, the maximum size of all policy resources. | 35kB (35,000 bytes) |   
Maximum number of terms of all applied BGP route policies within a single BGP peer or direction | 1,000 | This limit isn't split across resources, but combined. There isn't a limit on the size of a single match or action expression, number of actions in a term, number of terms in a single policy, or the number of policies.  
For a given Cloud Router, the maximum number of _subnet route_ advertisements per BGP session | No restriction | Cloud Routers don't have a limit for the number of subnet routes they can advertise. The number of subnet routes are determined by the number of subnets ranges, which are controlled by [VPC network quotas and limits](https://docs.cloud.google.com/vpc/docs/quota).  
For a given Cloud Router, the maximum number of _custom advertised routes_ per BGP session | 200 | If the custom advertised routes are identical for all BGP sessions on a Cloud Router, this limit represents the total number of _unique_ IPv4 and IPv6 custom advertised routes for the Cloud Router. In this case, each session receives the same set of custom advertised routes.  
The maximum size for a single match expression literal used in a BGP route policy, combined across `destination` and `community` matches. | 100 match elements | For example, `destination.inAnyRange([prefix(...), prefix(..)]) && communities.matchesEvery(['0:0', '1:1'])` has four match elements and ` destination == ... || destination == ...` has two match elements. There isn't a limit on the number of actions in a term, number of terms in a single BGP route policy, or the number of BGP route policies.  
The maximum number of action elements allowed in an action operation that accepts a list in BGP route policies. | 10 action elements | The following action operations accept lists:

  * `asPath.prependSequence`
  * `communities.add`
  * `communities.remove`
  * `communities.replaceAll`

There isn't a limit on the number of actions in a term, number of terms in a single BGP route policy, or the number of BGP route policies.  
For a given Cloud Router, the maximum number of named sets. | 500 | Named sets contribute to the overall limit on the size of policy related resources on the router.  
The maximum number of elements per named set. | 1000 |   
Maximum queries per minute for `list-bgp-routes` calls on a single Cloud Router | 1500 | This quota is from `compute.googleapis.com/list_requests_per_region`. For more information, see [ Rate quotas](https://docs.cloud.google.com/compute/api-quota#api-rate-limits-global).  
Maximum number of BGP route policies per Cloud Router. | 500 |   
For a given BGP session, the maximum number of custom learned routes | 10 |  For more information about this feature, see [Custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/custom-learned-routes).   
For a given region in a VPC network, the maximum number of unique IP prefixes that can be configured as custom learned routes; this limit allows for the same ranges to be used on multiple peers  | 10 |  For more information about this feature, see [Custom learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/custom-learned-routes).   
  
## Learned route example

The following examples illustrate the route dropping behavior that you can encounter when the from-own-region quota or the from-other-regions quota is exceeded.

Suppose you have Cloud Routers in the `us-east1` region and Cloud Routers in the `us-west1` region in the same VPC network, and global dynamic routing is enabled. Each Cloud Router in each region learns 250 _unique_ destinations. For illustrative purposes of this example, each Cloud Router in each region doesn't learn any of the same destinations.

Regardless of which Cloud Routers learn the routes within each region, each region's from-own-region quota is exhausted because 250 of 250 unique destinations are learned by the Cloud Routers in each region. The from-other-regions quotas for both regions are also exhausted because each Cloud Router imports 250 unique destinations from the other region. If the example VPC network used regional dynamic routing, the from-other-regions quotas in each region doesn't apply because regional dynamic routing mode instructs the VPC network to only create dynamic routes in the region that matches the route's next hop.

### Exceeding a region's from-own-region quota

Suppose your on-premises router that's connected to a Cloud Router in `us-west1` advertises a 251st destination. Cloud Routers in the `us-west1` region pick 250 of the 251 unique destinations following a [deterministic route order](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#deterministic). These routers send those 250 unique destinations to the VPC network, creating 250 dynamic routes in the `us-west1` region.

Because the VPC network uses global dynamic routing mode, it also creates no more than 250 dynamic routes _in every other region_ , subject to each other region's from-other-regions unique destination quota. The next section describes what happens in other regions in more detail.

### Exceeding a region's from-other-regions quota

When 251 unique destinations are learned by Cloud Routers in the `us-west1` region, 250 of the 251 unique destinations from `us-west1` are made available to resources in the `us-east1` region because the `us-east1` region's from-other-regions quota can only accept 250 unique destinations.

Suppose that you create a Cloud Router in a third region, `us-central1`, in the same VPC network. Suppose that the new Cloud Router learns 10 unique destinations from its BGP peer. Although the `us-central1` region's from-own-region quota has not been exceeded, the `us-central1` region's from-other-regions quota has been exceeded because a total of 500 unique destinations are provided by the other two regions (250 from `us-east1` and a different 250 from `us-west1`).

On a region-by-region basis, the [deterministic route order](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#deterministic) selects routes for no more than 250 unique destinations in other regions, as indicated in the following table.

Region |  Unique destinations local to the region   
(usage of region's from-own-region quota)  |  Unique destinations from other regions   
(usage of region's from-other-regions quota)  |  **us-west1** |  251 received. 250 of the 251 are selected, and one of the 251 is dropped by the deterministic route order. 250 dynamic routes with next hops in `us-west1` are created in `us-west1`. The 250 selected prefixes are shared with other regions. |  260 received (250 from `us-east1`, 10 from `us-central1`). 250 of the 260 are selected, and 10 of the 260 are dropped by the deterministic route order. 250 dynamic routes with next hops outside of `us-west1` are created in `us-west1`.  
---|---|---  
**us-east1** |  250 received. All 250 are selected by the deterministic route order. 250 dynamic routes with next hops in `us-east1` are created in `us-east1`. All 250 selected prefixes are shared with other regions. |  260 received (250 from `us-west1`, 10 from `us-central1`). 250 of the 260 are selected, and 10 of the 260 are dropped by the deterministic route order. 250 dynamic routes with next hops outside of `us-east1` are created in `us-east1`.  
**us-central1** |  10 received. All 10 are selected by the deterministic route order. 10 dynamic routes with next hops in `us-central1` are created in `us-central1`. All 10 selected prefixes are shared with other regions. |  500 received (250 from `us-west1`, 250 from `us-east1`). 250 of the 500 are selected, and 250 of the 500 are dropped by the deterministic route order. 250 dynamic routes with next hops outside of `us-central1` are created in `us-central1`.  
  
Although the `us-central1` region's from-other-regions quota is exceeded, its from-own-region quota can accept destinations whose next hops are in the `us-central1` region.

### Deterministic route dropping behavior

Cloud Router implements a deterministic route dropping behavior based on the subnet mask length and lexicographic characteristics of each prefix received. Within each region, the following process applies independently to the region's from-own-region destinations list and the region's from-other-regions unique destinations list:

  * The list is sorted first from shortest to longest subnet mask length, then IPv4 before IPv6, then lexicographically. For example, `10.0.0.0/8` comes before `10.2.1.0/24`, which comes before `10.99.1.0/24`.

  * The first 250 entries in the list are preserved. All others are discarded.




As shown in [exceeding a region's from-other-regions quota](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#exceeding_region_other), the deterministic dropping behavior is applied _independently_ to each region's from-own-region quota and each region's from-other-regions quota.

The deterministic route dropping behavior has the following consequences:

  * If the mask lengths are equal, IPv6 prefixes are discarded before IPv4 prefixes.

  * If the set of prefixes learned in each region remains constant, Google Cloud programs a consistent set of local dynamic routes in every region, subject to the dynamic routing mode of the VPC network. This consistency, including which routes are dropped by Cloud Router, is preserved when Cloud Router tasks restart.




### Avoiding route dropping

During route dropping, you lose connectivity for the prefixes that are dropped. To avoid route dropping, monitor each region's from-own-region and from-other-regions prefix usage by using Cloud Monitoring or Cloud Logging, and make sure not to advertise more unique destinations than each quota.

Consider summarizing routes to reduce the number of unique destinations. For example, if you have the four subnets `10.10.0.0/24`, `10.10.1.0/24`, `10.10.2.0/24`, and `10.10.3.0/24`, then you can summarize them as one prefix, `10.10.0.0/22`.

If summarization isn't possible, contact your Google Cloud Sales team to discuss alternative options.

## Manage quotas

Cloud Router enforces quotas on resource usage for various reasons. For example, quotas protect the community of Google Cloud users by preventing unforeseen spikes in usage. Quotas also help users who are exploring Google Cloud with the [free tier](https://docs.cloud.google.com/free/docs/gcp-free-tier) to stay within their trial. 

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

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
