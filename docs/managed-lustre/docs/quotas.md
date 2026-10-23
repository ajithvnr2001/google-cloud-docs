---
url: https://docs.cloud.google.com/managed-lustre/docs/quotas/
title: Quotas and limits \u00a0|\u00a0 Managed Lustre \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:26.939996+00:00
---

# Quotas and limits  |  Managed Lustre  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-lustre/docs/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Managed Lustre ](https://docs.cloud.google.com/managed-lustre/docs/overview)
  * [ Resources ](https://docs.cloud.google.com/managed-lustre/docs/resources)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This document lists the quotas and system limits that apply to Google Cloud Managed Lustre.

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

There are also _system limits_ on Managed Lustre resources. System limits can't be changed. 

## System limits

Managed Lustre enforces the following system limits:

System limit | Value  
---|---  
Minimum storage capacity per Managed Lustre instance | Defined by [performance tier](https://docs.cloud.google.com/managed-lustre/docs/create-instance#performance-tiers):

  * Dynamic: 472,000 GiB
  * 125 MBps per TiB: 72,000 GiB
  * 250 MBps per TiB: 36,000 GiB
  * 500 MBps per TiB: 18,000 GiB
  * 1000 MBps per TiB: 9,000 GiB

  
Maximum storage capacity per Managed Lustre instance | Defined by [performance tier](https://docs.cloud.google.com/managed-lustre/docs/create-instance#performance-tiers):

  * Dynamic: 84,016,000 GiB (80.1 PiB)
  * 125 MBps per TiB: 20,448,000 GiB (19.5 PiB)
  * 250 MBps per TiB: 40,032,000 GiB (38.2 PiB)
  * 500 MBps per TiB: 20,016,000 GiB (19.1 PiB)
  * 1000 MBps per TiB: 10,008,000 GiB (9.5 PiB)

  
Maximum file size | 0.5 PiB  
Maximum number of instances per project | 20  
Maximum number of client connections per instance. This limit applies to both Compute Engine instances and GKE nodes on which the Managed Lustre instance is mounted.  | 20,000  
  
## Quotas

Throughput and capacity quotas are pooled per region, per VPC network, but are specified at the zonal level.

Although limits are listed per zone, all zones within a region share a single quota pool. Creating an instance in one zone (e.g., `us-central1-a`) draws from the shared regional quota, reducing the capacity available to other zones in the same region (e.g., `us-central1-b` and `us-central1-c`).

The available quota shown per zone in the Google Cloud console does not reflect quota that has been consumed by other zones in the region.

### Numbered tiers

For numbered tiers (e.g., 1000 MBps per TiB) Managed Lustre has quotas for throughput (GBps) and storage capacity (GiB). These quotas are per [Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/vpc/docs/vpc) per zone. When you create an instance, you consume both throughput and capacity from your quotas based on the instance size and performance tier. Throughput and capacity quotas are shared across all numbered tiers, meaning you can use your quota to create instances in any numbered tier without needing to request tier-specific quota.

If you need additional quota, you can request increases for throughput or capacity independently.

### Dynamic tier

The Dynamic tier uses a single quota, **Storage capacity (GiB) for Dynamic tier per zone per VPC**. The individual capacity and throughput quotas don't apply to the Dynamic tier.

### Legacy per-performance-tier quotas

If your project previously used storage capacity quotas specific to individual performance tiers (for example, a quota specific to the 1000 MBps per TiB tier), those quotas have been replaced by the throughput and capacity quotas that are shared across all performance tiers.

As part of this transition, your old tier-specific quotas might be listed as **Unlimited** in the Google Cloud console. Note the following about this status:

  * **Instance creation is limited by shared quotas:** An **Unlimited** status on legacy quotas does not mean you can create unlimited instances. The new shared throughput and capacity quotas take precedence.
  * **Quota increase requests are not available:** You cannot submit a quota increase request for quotas marked as unlimited. To request more quota, submit a request for the new shared throughput and capacity quotas.



## Quota details

Managed Lustre supports the following quotas:

Item | Quota ID | Description  
---|---|---  
[Read limit per minute](https://console.cloud.google.com/iam-admin/quotas?service=lustre.googleapis.com&metric=api-requests) | `RequestsPerMinute` | The maximum number of API requests that an IAM user can make to the Google Cloud Managed Lustre API within a one-minute time period. This quota is only for API calls.   
[Lustre throughput capacity (GBps) per zone per VPC](https://console.cloud.google.com/iam-admin/quotas?service=lustre.googleapis.com&metric=lustre.googleapis.com/throughput) | `Throughput` | Throughput capacity in GBps for Managed Lustre instances.   
[Lustre storage capacity (GiB) per zone per VPC](https://console.cloud.google.com/iam-admin/quotas?service=lustre.googleapis.com&metric=lustre.googleapis.com/capacity) | `Capacity` | Storage capacity in GiB for Managed Lustre instances.   
[Storage capacity (GiB) for Dynamic tier per zone per VPC](https://console.cloud.google.com/iam-admin/quotas?service=lustre.googleapis.com&metric=lustre.googleapis.com/dynamic_tier_capacity) | `DynamicTierCapacity` | Storage capacity in GiB for the Dynamic performance tier.   
  
## Throughput and capacity quota calculators

The following tools can help calculate the maximum numbered tier instance size you can create, as well as how much throughput and capacity quota you need for a specific instance size.

## Request additional quota

Throughput and capacity quotas are scoped to a VPC network and zone.

###  Google Cloud console 

You can request additional quota using the Google Cloud console by visiting the Managed Lustre **Service Details** page:

  1. Visit the **Service Details** page:

[Go to Managed Lustre Service Details](https://console.cloud.google.com/apis/api/lustre.googleapis.com)

  2. Select the **Quotas & System limits** tab.

  3. Select which quota to increase. Throughput and capacity quotas are per zone and network name.

**Important:** If you're requesting a quota increase for a zone and VPC combination in which you haven't created an instance, that combination won't be listed in the table. To request additional quota, use gcloud CLI to create a quota request containing the zone and VPC. See the example in the gcloud CLI tab. Quota requests that don't include the zone and VPC will fail.
  4. Click **Edit**.

  5. Enter a new value, up to the system limit.

  6. Fill out any additional information and click **Submit request**.




###  gcloud CLI 

To request additional quota using Google Cloud CLI, create a Cloud Quotas adjustment request using the [Cloud Quotas API](https://docs.cloud.google.com/sdk/gcloud/reference/beta/quotas/preferences/create).

The Cloud Quotas API requires a case-sensitive `quota-id`. The following values are supported for Managed Lustre quotas:

  * `RequestsPerMinute`
  * `Throughput`
  * `Capacity`
  * `DynamicTierCapacity`



You must create a separate request each for capacity and for throughput.

To create a new quota preference, use the [`gcloud beta quotas preferences create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/quotas/preferences/create) command:
    
    
    gcloud beta quotas preferences create \
      --project=PROJECT_NUMBER \
      --quota-id=QUOTA_ID \
      --preferred-value=PREFERRED_VALUE \
      --service=lustre.googleapis.com \
      --dimensions=zone=ZONE,network_name=projects/VPC_PROJECT_ID/global/networks/NETWORK_NAME \
      --email=EMAIL \
      --justification="JUSTIFICATION"
    

Replace the following:

  * `PROJECT_NUMBER`: Your Google Cloud project number. You can find your project number on the [Welcome](https://console.cloud.google.com/welcome) page of the Google Cloud console or by running the following gcloud CLI command:
        
        PROJECT=$(gcloud info --format='value(config.project)')
        gcloud projects describe ${PROJECT} --format="value(projectNumber)"

  * `QUOTA_ID`: The case-sensitive ID of the quota that you're updating. One of `RequestsPerMinute`, `Throughput`, `Capacity`, or `DynamicTierCapacity`.

  * The PREFERRED_VALUE for the specified quota. Accepts a plain integer (e.g., `18000`). Specify the number according to the following units:

    * `RequestsPerMinute`: requests per user per minute
    * `Throughput`: GBps
    * `Capacity`: GiB
    * `DynamicTierCapacity`: GiB
  * The `ZONE` for this quota increase request. For example, `us-west1-a`.

  * The VPC_PROJECT_ID and NETWORK_NAME. For example, `vpc-project-1234` and `default`.

  * `EMAIL`: An email address that can be used as a contact for this request.

  * `JUSTIFICATION`: The reason for this request.




Cloud Quotas adjustment requests are subject to review. You'll receive an email acknowledging receipt of your request. If you need further assistance, respond to the email. After reviewing your request, you'll receive an email notification indicating whether your request was approved.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
