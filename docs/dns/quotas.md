---
url: https://docs.cloud.google.com/dns/quotas/
title: Quotas and limits \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:29.868947+00:00
---

# Quotas and limits  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Resources ](https://docs.cloud.google.com/dns/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Cloud DNS.

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

There are also _system limits_ on Cloud DNS resources. System limits can't be changed. 

## Quotas

To change a quota, see requesting additional quota.

This table highlights important global quotas for Cloud DNS resources in each project. For other quotas, see the [**Quotas** page](https://console.cloud.google.com/iam-admin/quotas) in the Google Cloud console.

Item | Description  
---|---  
[Read limit for a minute for a region](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/reads_per_region) | The maximum number of API requests that an IAM user can make to the Cloud DNS API within a one-minute time period. This quota is only for API calls. There are no quotas for DNS query processing.   
[DNSSEC keys per managed zone](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/dns_keys_per_managed_zone) | The maximum number of DNSSEC keys per managed zone.  
[Managed zones per project](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/managed_zones) | The maximum allowed number of managed zones in the project.  
[Managed zones per VPC network](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/managed_zones_per_network) | The maximum allowed number of managed zones which can be attached to a VPC network.  
[Policy resources per project](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/policies) | The maximum number of DNS server policies per project.  
[Networks per response policy](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/networks_per_response_policy) | The maximum allowed number of VPC networks per response policy.  
[Internet health checked routing policies per project](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/internet_health_checked_routing_policies_per_project) | The maximum allowed internet health checked DNS routing policies per project.  
[Items per routing policy](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/items_per_routing_policy) | The maximum allowed number of items per routing policy.  
[GKE clusters per managed zone](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/gke_clusters_per_managed_zone) | The maximum allowed number of Google Kubernetes Engine (GKE) clusters to which a privately scoped zone can be attached.  
[GKE clusters per policy](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/gke_clusters_per_policy) | The maximum allowed number of GKE clusters per policy.  
[Managed zones per GKE cluster](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/managed_zones_per_gke_cluster) | The maximum allowed number of managed zones which can be attached to a GKE cluster.  
[Resource record additions per change](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/rrset_additions_per_change) | The maximum allowed number of `ResourceRecordSets` you can add per `ChangesCreateRequest`.  
[Resource record deletions per change](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/rrset_deletions_per_change) | The maximum allowed number of `ResourceRecordSets` you can delete per `ChangesCreateRequest`.  
[Resource record sets per managed zone](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/rrsets_per_managed_zone) | The maximum allowed number of `ResourceRecordSets` per zone in the project.  
[Resource records per resource record set](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/resource_records_per_rrset) | The maximum allowed number of `ResourceRecords` per `ResourceRecordSet`. Each delegation (resource record sets of type `NS`) can have up to eight name servers.  
[Response policies per project](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/response_policies) | The maximum allowed number of response policies per project.  
[Response policy rule write limit for a minute for a region](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/response_policy_rule_writes_per_region) | The maximum number of response policy rules that can be written per minute for a region.  
[Response policy rules per batch action](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/response_policy_per_batch_action) | The maximum number of response policy management actions per batch per minute.  
[Response policy rules per policy](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/response_policy_rules_per_policy) | The maximum number of response policy rules that that you can create for a policy.  
[Target name servers per forwarding policy](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/target_nameservers_per_policy) | The maximum allowed number of target name servers per forwarding policy.  
[Target name servers per managed zone](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/target_nameservers_per_managed_zone) | The maximum allowed number of target name servers per managed forwarding zone.  
[Total size of resource record set data (in bytes) per change](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/total_rrdata_size_per_change) | The maximum allowed size for total `rrdata` in one `ChangesCreateRequest` in bytes.  
[VPC networks per managed zone](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/networks_per_managed_zone) | The maximum allowed number of VPC networks to which a privately scoped zone can be attached.  
[VPC networks per policy](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/networks_per_policy) | The maximum allowed number of VPC networks per Cloud DNS server policy.  
[Write limit for a minute for a region](https://console.cloud.google.com/iam-admin/quotas?service=dns.googleapis.com&metric=dns.googleapis.com/quota/writes_per_region) | The maximum number of DNS writes per region per minute. This quota is used for any write operation that creates, modifies, or deletes a DNS record.  
  
## Limits

Unlike quotas, where you can request additional quota, _limits_ cannot generally be increased unless specifically noted.

### API usage

The number of API requests (queries) per day is governed at the project level. All API requests count against this limit, including those made from the Google Cloud CLI and through the Google Cloud console.

### Resource limits

Item | Limit  
---|---  
**To request an update to these limits, contact[Cloud Customer Care](https://docs.cloud.google.com/support).**  
Number of peering zones per network | 1,000  
Name servers per delegation | 8  
Additions per change | 1,000  
Deletions per change | 1,000  
Resource record data size per change | 100,000 bytes  
Number of label combinations | 1,000  
Number of rules per response policy | 10,000  
Number of items per routing policy | 100  
Number of managed zones bound to a VPC network | 10,000  
Largest size of a DNS response (UDP) | 1,440 bytes  
Largest size of a DNS response (TCP) | 65,533 bytes  
**These limits cannot be increased.**  
Maximum query rate per VPC network per zone | 100,000 queries in a ten-second (10s) period in a Google Cloud zone, for example `us-central1-a`  
Number of response policies per VPC network | 1  
Number of labels per managed zone | 64 labels and 128 bytes per key or value  
Number of forwarding targets in a forwarding zone | 50  
Number of forwarding targets in an alternative name server | 50  
  
### Name server limits

Cloud DNS assigns every public managed zone to one of five name server shards. Shards are the letter before the number in an authoritative name server name, so `ns-cloud-e1` through `ns-cloud-e4` are the _E_ shard.

A new managed zone of a domain, for example `domain.example.tld`, cannot be assigned to a shard if any of the following already exists on the same shard:

  * A managed zone with the same DNS name, such as `domain.example.tld`
  * A subdomain of the DNS name, such as `sub.domain.example.tld`
  * A parent domain of the DNS name, such as `example.tld`



Because of these restrictions, the following limitations apply to public managed zones:

  * You can create a maximum of five zones with the exact same DNS name.
  * For any parent domain, you can create a maximum of five levels of subdomains.



These limitations apply to all projects and users in Google Cloud. Non-delegated subdomains and delegations hosted on other DNS services don't count against this limit. Before Cloud DNS creates a zone that occupies the last available name server shard, you must verify the zone domain ownership with a `TXT` record.

Multiple subdomains of the same parent domain, for example `domain.example.tld` and `otherdomain.example.tld`, can be assigned to the same shard. However, Cloud DNS might pick any available shard after considering the limitations. If you create such subdomains in each shard, you cannot create a zone for the parent domain `example.tld`.

You can avoid these limitations by always creating managed zones for the parent domains _before_ creating zones for their subdomains.

If the child domains are already blocking all shards, follow these steps to free a shard for the parent domain:

  1. Check the name servers for every subdomain zone to determine its shard.
  2. Find the shard (_X_) with the fewest (or least important) managed zones.
  3. Export zones in shard _X_ (and change their delegations) to another DNS service.
  4. _After TTLs expire_ for the original delegations, delete the managed zones for shard _X_ subdomains.
  5. Create the managed zone for the parent domain; it is assigned to shard _X_.
  6. Restore the deleted managed zones for the subdomains, _restoring subdomains before any of their own sub-subdomains_. They are in new shards, so they all need updated delegations.

**Note:** Google Domains creates its own zones on shards for all domains registered through it. Shard restrictions and limits apply across these products, so a Google Domains registration uses one of the shards available for domain and subdomain zones in Cloud DNS. Conversely, if some domain has Cloud DNS zones with identical or subdomain DNS names on all the name server shards, you cannot register that domain with Google Domains until you free up a shard by using the previous steps.

## Check limits

You can run the following command to look up the limits for your project. The following example shows the total limits for the various types of objects in the `my-project` project. The `totalRrdataSizePerChange` quota is measured in bytes and the combined total of both the additions and deletions for a change.
    
    
    gcloud dns project-info describe my-project
    

Even though these are limits, Google Cloud tracks them internally as quotas, so they are labeled as quotas in the output.
    
    
    id: my-project,
    kind: "dns#project",
    number: "123456789012",
    quota:
        kind: dns#quota,
        managedZones: 10000,
        resourceRecordsPerRrset: 10000,
        rrsetAdditionsPerChange: 3000,
        rrsetDeletionsPerChange: 3000,
        rrsetsPerManagedZone: 10000,
        totalRrdataSizePerChange: 100000,
        labelSets: 1000
    

You can find the name of your default project and additional projects at the top of the **Home** page in the [Google Cloud console](https://console.cloud.google.com/).

## Manage quotas

Cloud DNS enforces quotas on resource usage for various reasons. For example, quotas protect the community of Google Cloud users by preventing unforeseen spikes in usage. Quotas also help users who are exploring Google Cloud with the [free tier](https://docs.cloud.google.com/free/docs/gcp-free-tier) to stay within their trial. 

All projects start with the same quotas, which you can change by requesting additional quota. Some quotas might increase automatically based on your use of a product.

### Permissions

To view quotas or request quota increases, Identity and Access Management (IAM) principals need one of the following roles. 

Task | Required role  
---|---  
Check quotas for a project | One of the following: 

  * Project [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)
  * Project [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)
  * [Quota Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.quotaViewer) (`roles/servicemanagement.quotaViewer`)

  
Modify quotas, request additional quota | One of the following: 

  * Project [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)
  * Project [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)
  * [Quota Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/servicemanagement#servicemanagement.quotaAdmin) (`roles/servicemanagement.quotaAdmin`)
  * A custom role with the `serviceusage.quotas.update` permission

  
  
### Check your quota

### Console

  1. In the Google Cloud console, go to the **Quotas** page. 

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. To search for the quota that you want to update, use the **Filter table**. If you don't know the name of the quota, use the links on this page instead.



### gcloud

Using the Google Cloud CLI, run the following command to check your quotas.

Replace `PROJECT_ID` with your own project ID. 
    
    
        gcloud dns project-info describe PROJECT_ID
        

### Errors when exceeding your quota

If you exceed a quota with a `gcloud` command, `gcloud` outputs a `quota exceeded` error message and returns with the exit code `1`.

If you exceed a quota with an API request, Google Cloud returns the following HTTP status code: `413 Request Entity Too Large`. 

### Request additional quota

To adjust most quotas, use the Google Cloud console. For more information, see [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase). 

### Console

  1. In the Google Cloud console, go to the **Quotas** page. 

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. On the **Quotas** page, select the quotas that you want to change.
  3. At the top of the page, click edit**Edit quotas**.
  4. For **Name** , enter your name.
  5. Optional: For **Phone** , enter a valid phone number.
  6. Submit your request. Quota requests take 24 to 48 hours to process.



### Resource availability

Each quota represents a maximum number for a particular type of resource that you can create, if that resource is available. It's important to note that quotas do _not_ guarantee resource availability. Even if you have available quota, you can't create a new resource if it is not available.

For example, you might have sufficient quota to create a new regional, external IP address in the `us-central1` region. However, that is not possible if there are no available external IP addresses in that region. Zonal resource availability can also affect your ability to create a new resource.

Situations where resources are unavailable in an entire region are rare. However, resources within a zone can be depleted from time to time, typically without impact to the service level agreement (SLA) for the type of resource. For more information, review the relevant SLA for the resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
