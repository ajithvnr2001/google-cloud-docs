---
url: https://docs.cloud.google.com/vpc/docs/multicast/quotas/
title: Cloud Multicast quotas and limits \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:01.800552+00:00
---

# Cloud Multicast quotas and limits  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/quotas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Resources ](https://docs.cloud.google.com/vpc/docs/multicast/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Multicast quotas and limits

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This document lists the quotas and system limits that apply to Cloud Multicast resources.

For more information about quotas and system limits, including how to manage quotas, see the [Quotas and limits page](https://docs.cloud.google.com/vpc/docs/quota) for VPC networks.

For an overview of Cloud Multicast, see the [Cloud Multicast overview](https://docs.cloud.google.com/vpc/docs/multicast/overview).

## Quotas and system limits for Cloud Multicast

This section describes the quotas and system limits for Cloud Multicast resources that are enforced by the [Cloud Quotas system](https://docs.cloud.google.com/docs/quotas/overview).

The following table lists each quota and system limit and provides a link to view its corresponding value on the **Quotas and System Limits** page of the Google Cloud console.

To view all multicast quotas and system limits in a single list, you can use a filter such as in the following example: [**All multicast quotas and system limits**](https://console.cloud.google.com/iam-admin/quotas?pageState=\(%22allQuotasTable%22:\(%22f%22:%22%255B%257B_22k_22_3A_22Name_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22multicast_5C_22_22_2C_22i_22_3A_22displayName_22%257D_2C%257B_22k_22_3A_22Dimensions%2520%2528e.g.%2520location%2529_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22_5C_5C_5C_22_5C_5C_5C_22_5C_22_22_2C_22i_22_3A_22displayDimensions_22%257D_2C%257B_22k_22_3A_22Service%2520ID_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22compute.googleapis.com_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22serviceName_22%257D_2C%257B_22k_22_3A_22_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22OR_5C_22_22_2C_22o_22_3Atrue_2C_22s_22_3Atrue%257D_2C%257B_22k_22_3A_22Service%2520ID_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22networkservices.googleapis.com_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22serviceName_22%257D_2C%257B_22k_22_3A_22_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22multicast_5C_22_22%257D_2C%257B_22k_22_3A_22Dimensions%2520%2528e.g.%2520location%2529_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22_5C_5C_5C_22_5C_5C_5C_22_5C_22_22_2C_22i_22_3A_22displayDimensions_22%257D%255D%22\)\)). For more information about viewing and filtering quotas, see [View quotas in the Google Cloud console](https://docs.cloud.google.com/docs/quotas/view-manage#viewing_your_quota_console).

Quota | Description  
---|---  
**Multicast domains**  
[**Multicast domain groups per project**](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/multicast_domain_groups) | The number of [multicast domain groups](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#domains) that you can create in your project.  
[**Multicast domains per project**](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/multicast_domains) | The number of [multicast domains](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#domains) that you can create in your project.  
[**Multicast domain activations per zone**](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/multicast_domain_activations) | The number of [multicast domain activations](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#domains) that you can create in a zone.  
**Multicast group ranges**  
[**Multicast group ranges per project**](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/multicast_group_ranges) | The number of [multicast group ranges](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#group-ranges) that you can create in a project.  
[**Multicast group range activations per project per zone**](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/multicast_group_range_activations) | The number of [multicast group range activations](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#group-ranges) that you can create for a given group range in a zone.  
[**Multicast groups per domain**](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/multicast_groups_per_domain) | The maximum number of IP addresses across all multicast group ranges associated with a domain.  
**Multicast producer configurations**  
[**Multicast producer associations per project per zone**](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/multicast_producer_associations) | The number of [multicast producer associations](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#producer-resources) that you can create between a single multicast producer VPC network and a domain in a zone.  
[**Multicast group producer activations per project per zone**](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/multicast_group_producer_activations) | The number of [multicast group producer activations](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#producer-resources) that you can create for a single multicast producer VPC network and a group range in a zone.  
**Multicast consumer configurations**  
[**Multicast consumer associations per project per zone**](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/multicast_consumer_associations) | The number of [multicast consumer associations](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#consumer-resources) that you can create between a single multicast consumer VPC network and a domain in a zone.  
[**Multicast group consumer activations per project per zone**](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/multicast_group_consumer_activations) | The number of [multicast group consumer activations](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#consumer-resources) that you can create for a single multicast consumer VPC network and a group range in a zone.  
[**Multicast consumers per zone per VPC network**](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/multicast_consumers_per_zone_per_vpc_network) | The maximum number of network interfaces of Compute Engine instances for which you can [enable IGMP query](https://docs.cloud.google.com/vpc/docs/multicast/configure-consumer-vms) in a given VPC network and zone. For a single instance with multiple network interfaces, each network interface counts toward this limit.  
**Multicast routes**  
[**Multicast routes per zone per VPC network**](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&metric=networkservices.googleapis.com/multicast_routes_per_vpc) |  The maximum number of routes that can exist in a VPC network and zone for multicast traffic.  Multicast routes are created automatically by Google Cloud for each multicast group producer activation and multicast group consumer activation. Consequently, this quota corresponds to the total number of multicast group producer activations and multicast group consumer activations in a single VPC network and zone.   
  
## Other system limits for Cloud Multicast

Google Cloud enforces the following additional system limits for Cloud Multicast resources independently of the Cloud Quotas system.

Item | Limit | Notes  
---|---|---  
**Multicast group ranges**  
Multicast group ranges per domain | 500 | The maximum number of multicast group ranges that you can create in a domain.  
**Multicast producer configurations**  
Multicast producer VPC networks per multicast group range per zone | 20 | The maximum number of multicast producer VPC networks that can be activated for a group range in a zone. This corresponds to the number of multicast group producer activations that can be created by using the same multicast group range activation.  
Traffic flows per multicast producer | 512 | The maximum number of traffic flows for a single multicast producer instance. This limit corresponds to the number of multicast groups for which the instance can send traffic. For multicast, a traffic flow is defined as a five-tuple that consists of a protocol (UDP), source IPv4 address, source port, destination IPv4 address, and destination port. This limit applies across all domains and group ranges for which the multicast producer sends traffic.  
**Multicast consumer configurations**  
Multicast consumer VPC networks per multicast group range per zone | 1000 | The maximum number of multicast consumer VPC networks that can be activated for a group range in a zone. This corresponds to the number of multicast group consumer activations that can be created by using the same multicast group range activation.  
Traffic flows per multicast consumer | Depends on the vCPUs of the machine type | The maximum number of traffic flows for a single multicast consumer instance. This limit corresponds to the number of multicast groups for which the instance can receive traffic. For multicast, a traffic flow is defined as a five-tuple that consists of a protocol (UDP), source IPv4 address, source port, destination IPv4 address, and destination port. This limit applies across all domains and group ranges for which the multicast consumer receives traffic. For the limit for each machine type, see [Machine considerations for multicast consumers](https://docs.cloud.google.com/vpc/docs/multicast/overview#machine-requirements).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
