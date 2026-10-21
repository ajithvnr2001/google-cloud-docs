---
url: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/vpc-network/ip-utilization/
title: IP address utilization insights \u00a0|\u00a0 Network Intelligence Center - Network Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:40:56.098948+00:00
---

# IP address utilization insights  |  Network Intelligence Center - Network Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/vpc-network/ip-utilization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Network Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/overview)



Send feedback 

#  IP address utilization insights Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the Network Analyzer insights for IP address utilization. For information about all the insight types, see [Insight groups and types](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insight-groups-types).

IP address utilization insights show the IP address allocation percentage of subnet ranges, which are calculated based on configurations that use IP addresses, such as VMs and load balancers. In the case of Shared VPC, Network Analyzer provides the IP address utilization insights of the host project, and the information from service projects is automatically aggregated to derive the insight information.

## View insights in the Recommender API

To view these insights in the gcloud CLI or the Recommender API, use the following insight type:

  * `google.networkanalyzer.vpcnetwork.ipAddressInsight`



You need the following permissions:

  * `recommender.networkAnalyzerIpAddressInsights.list`
  * `recommender.networkAnalyzerIpAddressInsights.get`



For more information about using the Recommender API for Network Analyzer insights, see [Use the Recommender CLI and API](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/use-cli-recommender-api).

## High IP address utilization of a subnet

This insight indicates that the IP address utilization of a subnet is too high (the allocation ratio is higher than 75 percent). Such an issue can prevent automation from creating new VMs or upgrading a GKE cluster. This insight includes the following information:

  * **Subnetwork:** The name of the subnetwork.
  * **Secondary range name:** If the insight shows the primary range of the subnet, this field is not displayed.
  * **IP address range:** The IP address range of the subnetwork range.
  * **Allocation ratio:** The percentage of IP addresses from the range of the subnet that are allocated.
  * **Resources using this range:** The count of the number of resources of this type that have allocated IP addresses within the IP address range of the subnet. This attribute gives a summary of the number of IP addresses used by resources such as VMs and load balancers.



The allocation ratio of the primary range includes the [four unusable IP addresses](https://docs.cloud.google.com/vpc/docs/subnets#unusable-ip-addresses-in-every-subnet).

### Recommendations

You have two options:

  * [Expand the subnet primary ranges](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#expand-subnet).
  * [Add more secondary ranges](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#edit-secondary).



## IP address utilization summary

This insight gives a summary of the IP address utilization of subnet ranges in the analyzed project. In the case of Shared VPC, Network Analyzer gives a summary of the IP address utilization of all relevant subnet ranges of the host project, and also provides the insights of the service projects. It includes the following information:

  * All subnet ranges that have an allocation ratio more than zero.
  * **Secondary range name:** The secondary range name of a subnet. This field is not displayed for the primary range of a subnet.
  * **Subnet range prefix:** The IP address range of the subnetwork range in CIDR format.
  * **Allocation ratio:** The ratio (between 0 and 1, 1 being 100%) of IP addresses allocated from the range of the subnet compared to the total number of IP addresses in the subnet.



The allocation ratio of the primary range includes the [four unusable IP addresses](https://docs.cloud.google.com/vpc/docs/subnets#unusable-ip-addresses-in-every-subnet).

### Related topics

For more information, see [High IP address utilization insight](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/insights/vpc-network/ip-utilization#ip-allocation-ratio-high).

## Private services access IP address utilization summary

This insight gives a summary of the utilization of IP address ranges used for [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) in the analyzed projects. Private services access IP address ranges are used by Google Cloud managed services such as Cloud SQL.

When you use private services access, you create an [allocated range](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#allocating-range) that is used when you create a [private connection](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#creating-connection) to the service. In Network Analyzer, allocated IP address ranges are referred to as _PSA ranges_.

The managed service producer creates a subnet in a service-managed Virtual Private Cloud (VPC) that is peered to your VPC network. The service producer chooses an available IP address range for the subnet that falls within the allocated IP address range. In Network Analyzer, the service producer subnets are referred to as _PSA subnets_.

This insight includes the following information:

  * **PSA range prefix** : The prefix of the allocated IP address range (PSA range) reserved in your VPC network for managed services.
  * **PSA subnet prefix** : The prefix of the subnet that was created from the PSA range.
  * **PSA subnet region** : The region used by the managed service for this subnet.
  * **PSA subnet service** : The name of the managed service that uses this subnet. For more information about the services that support this field, see Managed services supporting the name field.
  * **Allocation ratio** : 
    * The allocation ratio of the PSA range corresponds to how much of the range is allocated to managed services. Each managed service you use reserves one or multiple ranges of varying size, depending on the service.
    * The allocation ratio of the PSA subnet corresponds to the number of IP addresses that are allocated from the range of the PSA subnet in the service-managed VPC network compared to the total number of IP addresses in the range.



In the case of Shared VPC, Network Analyzer provides this insight in the host project.

### Managed services supporting the name field

The name field is populated for the following services:

  * AlloyDB for PostgreSQL
  * Apigee
  * Cloud Build
  * Cloud SQL
  * Memorystore for Memcached
  * Memorystore for Redis
  * Vertex AI managed notebooks



### Recommendations

Review the allocation ratio for your PSA ranges and consider [adding new allocated IP address ranges](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#modifying-connection) as soon as the allocation ratio is greater than 50%.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
