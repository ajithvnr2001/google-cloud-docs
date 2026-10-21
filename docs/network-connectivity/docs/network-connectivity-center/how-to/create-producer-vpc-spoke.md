---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/create-producer-vpc-spoke/
title: Create a producer VPC spoke \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:19:04.248535+00:00
---

# Create a producer VPC spoke  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/create-producer-vpc-spoke/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Create a producer VPC spoke Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a producer Virtual Private Cloud (VPC) spoke on a Network Connectivity Center (NCC) hub. A producer VPC spoke lets you connect your service producer VPC network with other networks in a given project.

For a detailed overview of producer VPC spokes, see [Producer VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-overview).

## Before you begin

Before you create a producer VPC spoke:

  * Review the [Considerations](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-overview#considerations) for producer VPC spokes.
  * Review the [guidelines for creating VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vpc-spoke), which also apply to producer VPC spokes.



## Create a producer VPC spoke

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `networkconnectivity.spokes.use` on the peered consumer VPC spoke
  * `networkconnectivity.groups.use` on the hub that the spoke is being associated with
  * `networkconnectivity.spokes.create` in the project where the peered consumer VPC network lives
  * `networkconnectivity.groups.create` on the hub to create a group
  * `networkconnectivity.groups.use` on the hub to create spokes associated with a group in a different project from the hub



**Roles**

  * Compute Network Admin role (`roles/compute.networkAdmin`) on the peered consumer VPC network
  * Spoke Admin role (`roles/networkconnectivity.spokeAdmin`) in the project where the peered consumer VPC network lives



To connect a service producer VPC network with other networks in a given project, connect the producer VPC network to a producer VPC spoke, and connect the producer VPC spoke to a hub.

If you use the Google Cloud CLI or the API to connect the producer VPC spoke to a hub that is configured for star topology, you must use the same group name as the existing consumer VPC spoke on the hub. If you use the Google Cloud console, the producer VPC spoke is automatically added to the same group.

If you want to assign [exclude export ranges](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#exclude-export-ranges) or [include export ranges](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#include-export-ranges), use the appropriate options during spoke creation.

To create a producer VPC spoke, follow these steps.

###  Console 

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project in which you want to create the spoke.

  3. Click the **Spokes** tab.

  4. Click **Add spokes**.

  5. In the **Select hub** section, select the hub location as follows:

     * To attach the new spoke to a hub in the same project, select **In project` PROJECT_NAME`** and select the hub name from the list.
     * If you want to attach the new spoke to a hub in another project, select **In another project**. Enter the **Project ID** and the **Hub name** to which you want to attach your new spoke.

When you choose a hub in a different project, your spoke becomes active only when the hub administrator reviews and accepts your proposed spoke. For more information about creating spokes attached to a hub in a different project, see [VPC spokes overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview). If you are creating a producer VPC spoke in the same project as the hub, the auto-accept list is still considered. By default, the auto-accept list already includes the same project, so the producer VPC spoke is automatically accepted and activated.

  6. Enter a **Spoke name** and optionally, a **Description**.

  7. Select **Producer VPC network** as the **Spoke type**.

  8. Enter the name of an existing **Consumer VPC spoke** on the hub that consumes services from the producer VPC network through a VPC Network Peering connection. Google Cloud identifies the producer network through the peering connection. You can choose from one of the following options:

     * For [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access), use `servicenetworking-googleapis-com`.
     * For [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview), use `sn-netapp-prod`.
  9. Optionally, you can add a VPC spoke filter to customize how routes are advertised by entering an IP address range to [exclude or include export](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#vpc-connectivity-with-export-filters) from the spoke to hub. You can change this filter after the spoke is created.

  10. Click **Done**.

  11. If you want to add more spokes, click **Add spoke** and begin the process again, starting with entering a spoke name.

  12. When you have finished adding spokes, click **Create**. The NCC page updates to show details about the spokes that you created.




###  gcloud 

To create a producer VPC spoke, use the [`gcloud network-connectivity spokes linked-producer-vpc-network create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-producer-vpc-network/create).
    
    
    gcloud network-connectivity spokes linked-producer-vpc-network create SPOKE_NAME \
        --hub=HUB \
        --description=DESCRIPTION \
        --network=CONSUMER_VPC_URI \
        --peering=PEERING_NAME \
        --include-export-ranges=[INCLUDE_EXPORT_RANGES] \
        --exclude-export-ranges=[EXCLUDE_EXPORT_RANGES] \
        --global \
        --group=GROUP_NAME
    

Replace the following:

  * `SPOKE_NAME`: the name of the spoke that you are creating, such as `producer-vpc-spoke1`
  * `HUB`: the hub for the spoke
  * `DESCRIPTION`: optional text to describe the spoke
  * `CONSUMER_VPC_URI`: the VPC network that consumes services from the producer network through a VPC Network Peering connection

Google Cloud identifies the producer VPC network through the peering connection. The consumer network that you enter must also be a spoke in the hub. You can enter the full or relative URI. The following example shows the relative URI: `projects/PROJECT_ID/global/networks/NETWORK_NAME`.

  * `PEERING_NAME`: the name of the peering between the your VPC network and the producer VPC spoke. The producer VPC spoke must be in the same project as your VPC network and must be in the `ACTIVE` state. Set the `--peering` flag to one of the following:

    * For [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access), use `servicenetworking-googleapis-com`.
    * For [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview), use `sn-netapp-prod`.
  * `INCLUDE_EXPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which subnet IP address ranges can be exported to the hub.

    * The `ALL_PRIVATE_IPV4_RANGES` keyword adds all subnet ranges that use [private IPv4 addresses](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) to the include export range list.

    * The `ALL_IPV4_RANGES` keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR. All [valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) for subnet ranges, including privately used public IPv4 address ranges, are included. You can refine the list by using the `--exclude-export-ranges` flag.

    * The `ALL_IPV6_RANGES` keyword includes all IPv6 addresses, equivalent to the `::/0` CIDR.

    * The include export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include export ranges can match or contain another CIDR.

    * If you omit `--include-export-ranges` for a VPC spoke, the default include export ranges is the same as if you had specified `ALL_PRIVATE_IPV4_RANGES`.

    * Subnet ranges in the VPC spoke, its include export ranges, and its exclude export ranges must follow the [Export filter rules for VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-vpc-spokes).

  * `EXCLUDE_EXPORT_RANGES`: a comma-delimited list of IP address ranges that define which subnet IP address ranges are never exported to the hub.

    * The exclude export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude export ranges can match or contain another CIDR.

    * Every CIDR specified in the exclude export ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the include export ranges (or the default include export ranges, if you don't specify any include export ranges explicitly).

    * Exclude export ranges don't support keywords.

    * If you omit `--exclude-export-ranges`, NCC uses an empty list as the default exclude export ranges.

    * Subnet ranges in the VPC spoke, its include export ranges, and its exclude export ranges must follow the [Export filter rules for VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-vpc-spokes).

  * `GROUP_NAME`: the group this spoke belongs to—for example, `center` or `edge`. This field is required for spoke groups that use star topology. For detailed information about spoke groups, see [Spoke groups](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#spoke-groups).




###  API 

To create a producer VPC spoke, use the [`networkconnectivity.spokes.create` method](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest/v1/projects.locations.spokes/create).
    
    
      POST https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/global/spokes/SPOKE_NAME
      {
        "hub":"HUB_NAME",
        "linkedProducerVpcNetwork": {
           "network": "CONSUMER_VPC_URI",
           "peering_name": "PEERING_NAME",
           "include_export_ranges": "[INCLUDE_EXPORT_RANGES]",
           "exclude_export_ranges": "[EXCLUDE_EXPORT_RANGES]",
           "group": "GROUP_NAME"
        },
      }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the project that contains the new spoke
  * `HUB_NAME`: the name of the hub that you are attaching the spoke to
  * `SPOKE_NAME`: the name of the spoke that you are creating
  * `CONSUMER_VPC_URI`: the VPC network that consumes services from the producer through a VPC Network Peering connection

Google Cloud identifies the producer VPC network through the peering connection. The consumer network that you enter must also be a spoke in the hub. You can enter the full or relative URI. The following example shows the relative URI: `projects/PROJECT_ID/global/networks/NETWORK_NAME`.

  * `PEERING_NAME`: the name of the peering between the your VPC network and the producer VPC spoke. The producer VPC spoke must be in the same project as your VPC network and must be in the `ACTIVE` state. Set the `--peering` flag to one of the following:

    * For [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access), use `servicenetworking-googleapis-com`.
    * For [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview), use `sn-netapp-prod`.
  * `INCLUDE_EXPORT_RANGES`: a comma-delimited list of keywords, IP address ranges, or a combination of keywords and IP address ranges that define which subnet IP address ranges can be exported to the hub.

    * The `ALL_PRIVATE_IPV4_RANGES` keyword adds all subnet ranges that use [private IPv4 addresses](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) to the include export range list.

    * The `ALL_IPV4_RANGES` keyword includes all IPv4 addresses, equivalent to the `0.0.0.0/0` CIDR. All [valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges) for subnet ranges, including privately used public IPv4 address ranges, are included. You can refine the list by using the `--exclude-export-ranges` flag.

    * The `ALL_IPV6_RANGES` keyword includes all IPv6 addresses, equivalent to the `::/0` CIDR.

    * The include export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the include export ranges can match or contain another CIDR.

    * If you omit `--include-export-ranges` for a VPC spoke, the default include export ranges is the same as if you had specified `ALL_PRIVATE_IPV4_RANGES`.

    * Subnet ranges in the VPC spoke, its include export ranges, and its exclude export ranges must follow the [Export filter rules for VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-vpc-spokes).

  * `EXCLUDE_EXPORT_RANGES`: a comma-delimited list of IP address ranges that define which subnet IP address ranges are never exported to the hub.

    * The exclude export ranges support up to 16 unique, nonoverlapping CIDRs. No CIDR in the exclude export ranges can match or contain another CIDR.

    * Every CIDR specified in the exclude export ranges must expand to IP addresses that are fully contained by CIDRs or keywords in the include export ranges (or the default include export ranges, if you don't specify any include export ranges explicitly).

    * Exclude export ranges don't support keywords.

    * If you omit `--exclude-export-ranges`, NCC uses an empty list as the default exclude export ranges.

    * Subnet ranges in the VPC spoke, its include export ranges, and its exclude export ranges must follow the [Export filter rules for VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-vpc-spokes).

  * `GROUP_NAME`: the group this spoke belongs to—for example, `center` or `edge`. This field is required for spoke groups that use star topology. For detailed information about spoke groups, see [Spoke groups](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#spoke-groups).




## What's next

  * [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes)
  * [Get details about API and `gcloud` commands](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
