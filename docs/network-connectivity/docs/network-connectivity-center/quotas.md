---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas/
title: Quotas and limits \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:36:36.524484+00:00
---

# Quotas and limits  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Resources ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and limits that apply to Network Connectivity Center (NCC) and Router appliance.

To change a quota, see Request additional quota.

Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on NCC resources. System limits can't be changed. 

## Quotas

This section lists quotas that apply to NCC and Router appliance.

### NCC quotas

Quotas that apply to network routes for Cloud Router also apply to routes for NCC hubs and spokes. For more information, see Cloud Router [Quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas).

Item | Quota | Notes  
---|---|---  
Number of hubs per project | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/global-per-project-hubs) | Per project, global  
Number of Cloud VPN tunnel spokes per project per region | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/regional-per-project-vpn-tunnel-spokes) | Per project in each region; only HA VPN tunnels are supported  
Number of Cloud Interconnect VLAN attachment spokes per project per region | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/regional-per-project-interconnect-attachment-spokes) | Per project in each region  
Number of Router appliance spokes per project per region | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/regional-per-project-router-appliance-instance-spokes) | Per project in each region  
Number of VPC spokes per project | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/global-per-project-vpc-spokes) | Includes VPC spokes (_edge_ and _center_ spokes combined) even if they are not connected to any hub  
Number of _active_ VPC spokes per hub | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/active_vpc_spokes_per_hub) | Only applicable to VPC spokes that have been accepted into a hub; not applicable to VPC spokes that are pending review or that have been rejected  
Number of subnet routes _per_ hub route table | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/routes_per_route_table) | Only applicable to hubs with VPC spokes  
Number of dynamic routes _per_ hub | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/dynamic_route_prefixes_per_hub_route_table_per_route_region) | Applicable to all VPC spokes  
Number of routing VPC networks _per_ hub | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/routing_vpcs_per_hub) |   
Number of static routes with an internal passthrough Network Load Balancer IP address as the next hop _per_ hub | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/static_routes_per_hub) | Per project, global  
The number of Private Service Connect endpoints for global Google APIs that can be propagated to VPC spokes that attach to the same NCC hub ([Preview](https://cloud.google.com/products#product-launch-stages)). Each endpoint that is propagated counts once towards this quota, regardless of the number of VPC spokes that the endpoint is propagated to. | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/psc_global_gapi_routes_per_route_table) | Per project, per hub, per route table, global  
Number of unique gateway edge dynamic route prefixes per group per region | 1000 | Per group, per region  
Number of gateway spokes per hub per region | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com/gateway_spokes_per_hub_per_region) | Per hub, per region  
Number of gateway advertised routes on a _single_ gateway | 10 | Per gateway  
Number of Private Service Connect forwarding rules _per_ hub | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/psc_ilb_consumer_forwarding_rules_per_hub) | Applicable to all VPC spokes  
  
### Router appliance quotas

Quotas that apply to network routes for Cloud Router also apply to routes for Router appliance spokes attached to NCC hubs.

For more information, see [Cloud Router quotas](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#quotas).

## Limits

This section lists limits that apply to NCC and Router appliance.

### NCC limits

Network Connectivity Center enforces the following usage limits.

Item | Value  
---|---  
Number of VPN tunnels that can be linked to a spoke | 8  
Number of VLAN attachments that can be linked to a spoke | 6  
Number of router appliance instances that can be linked to a spoke | 8  
Number of active VPC spokes per hub | 250  
Maximum number of VPC spokes (active and inactive) per hub | 1,000  
Number of include or exclude export CIDR ranges per spoke | 16  
  
### Router appliance limits

The following limits for Cloud Router also apply to Router appliance:

  * The maximum number of Cloud Routers per combination of VPC network and region
  * The maximum number of BGP peers for each Cloud Router in a given VPC network and region



For more information, see [Cloud Router limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).

## Manage quotas

Network Connectivity Center enforces quotas on resource usage for various reasons. For example, quotas protect the community of Google Cloud users by preventing unforeseen spikes in usage. Quotas also help users who are exploring Google Cloud with the [free tier](https://docs.cloud.google.com/free/docs/gcp-free-tier) to stay within their trial. 

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

## What's next

  * To find quotas and limits information for other Network Connectivity products, see [Network Connectivity quotas and limits](https://docs.cloud.google.com/network-connectivity/quotas).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
