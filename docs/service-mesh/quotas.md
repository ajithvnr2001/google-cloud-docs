---
url: https://docs.cloud.google.com/service-mesh/quotas/
title: Quotas \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:39:52.349514+00:00
---

# Quotas  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/quotas/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Resources ](https://docs.cloud.google.com/service-mesh/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Quotas

This document contains current content limits and request quotas for Cloud Service Mesh.

Google Cloud uses quotas to help ensure fairness and reduce spikes in resource use and availability. A quota restricts how much of a Google Cloud resource your Google Cloud project can use. Quotas apply to a range of resource types, including hardware, software, and network components. For example, quotas can restrict the number of API calls to a service, the number of load balancers used concurrently by your project, or the number of projects that you can create. Quotas protect the community of Google Cloud users by preventing the overloading of services. Quotas also help you to manage your own Google Cloud resources.

The Cloud Quotas system does the following:

  * Monitors your consumption of Google Cloud products and services
  * Restricts your consumption of those resources
  * Provides a way to [request changes to the quota value](https://docs.cloud.google.com/docs/quotas/help/request_increase) and [automate quota adjustments](https://docs.cloud.google.com/docs/quotas/quota-adjuster)



In most cases, when you attempt to consume more of a resource than its quota allows, the system blocks access to the resource, and the task that you're trying to perform fails.

Quotas generally apply at the Google Cloud project level. Your use of a resource in one project doesn't affect your available quota in another project. Within a Google Cloud project, quotas are shared across all applications and IP addresses. 

For more information, see the [Cloud Quotas overview](https://docs.cloud.google.com/docs/quotas/overview). 

There are also _system limits_ on Cloud Service Mesh resources. System limits can't be changed. 

Note that Istio resources are translated into Traffic Director resources that count against the quotas that follow.

## Limits

Cloud Service Mesh has a limit of 100 queries per second (QPS) per Google Cloud project.

All existing forwarding rule, backend service, and other load-balancing limits and quotas per project apply to Cloud Service Mesh deployments based on Google Cloud load balancing and service routing APIs.

### URL map limits

URL maps for Cloud Service Mesh with the load-balancing APIs are subject to the following per-project limits.

Item | Quotas and limits | Notes | URL maps | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=trafficdirector.googleapis.com&metric=%22URL%20maps%22) | This quota is per project.  
---|---|---  
Paths in path rules | 50 | This limit cannot be increased.  
Match rules in route rules | 50 | This limit cannot be increased.  
Host rules per URL map | 2,500 | This limit cannot be increased.  
Path matchers per URL map | 2,500 | This limit cannot be increased.  
Path rules per path matcher | 500 | This limit cannot be increased.  
Route rules per path matcher | 500 | This limit cannot be increased.  
Header matches per match rule | 50 | This limit cannot be increased.  
Query parameter matches per match rule | 50 | This limit cannot be increased.  
Metadata filters per match rule | 5 | This limit cannot be increased.  
Filter labels per metadata filter | 64 | This limit cannot be increased.  
Hosts per host rule | 100 | This limit cannot be increased.  
Tests per URL map | 100 | This limit cannot be increased.  
Size of URL maps | 524 KB | This limit cannot be increased.  
Weighted backend services per route action | 10 | This limit cannot be increased.  
  
If you exceed one of the limits in the table, you see an error such as the following:
    
    
    Value for field 'resource.hostRules[0].hosts' is too large:
    maximum size 100 element(s);actual size 107.
    

### Service routing API limits

Item | Notes | [**Meshes**](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/meshes) | This quota is per project.  
---|---  
[**Gateways**](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/gateways) | This quota is per project.  
[**GrpcRoutes**](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/grpcroutes) | This quota is per project.  
[**HttpRoutes**](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/httproutes) | This quota is per project.  
[**TcpRoutes**](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/tcproutes) | This quota is per project.  
[**TlsRoutes**](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/tlsroutes) | This quota is per project.  
  
### Network security API limits

Item | Quotas and limits | Notes | [**clientTlsPolicy**](https://console.cloud.google.com/iam-admin/quotas?service=networksecurity.googleapis.com&metric=%20networksecurity.googleapis.com/clienttlspolicies) | 500 | This quota is per project.  
---|---|---  
[**serverTlsPolicy**](https://console.cloud.google.com/iam-admin/quotas?service=networksecurity.googleapis.com&metric=%20networksecurity.googleapis.com/servertlspolicies) | 500 | This quota is per project.  
[**AuthorizationPolicy**](https://console.cloud.google.com/iam-admin/quotas?service=networksecurity.googleapis.com&metric=%20networksecurity.googleapis.com/authorizationpolicies) | 500 | This quota is per project.  
[**EndpointPolicy**](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/endpointpolicies) | 750 | This quota is per project.  
  
### Service load balancing policy

Item | Quotas and limits | Notes  
---|---|---  
ServiceLbPolicies | [Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/servicelbpolicies) | This quota is per project.  
  
To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

## Manage quotas

Cloud Service Mesh enforces quotas on resource usage for various reasons. For example, quotas protect the community of Google Cloud users by preventing unforeseen spikes in usage. Quotas also help users who are exploring Google Cloud with the [free tier](https://docs.cloud.google.com/free/docs/gcp-free-tier) to stay within their trial. 

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
