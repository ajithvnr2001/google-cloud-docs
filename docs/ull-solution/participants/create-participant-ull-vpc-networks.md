---
url: https://docs.cloud.google.com/ull-solution/participants/create-participant-ull-vpc-networks/
title: Create VPC networks for exchange participant workloads \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:36.136396+00:00
---

# Create VPC networks for exchange participant workloads  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/create-participant-ull-vpc-networks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create VPC networks for exchange participant workloads

**GA with allowlist** : ULL Solution is available only to approved exchange operators and their exchange participants. If you are an approved exchange participant, contact [exchanges@google.com](mailto:exchanges@google.com) to request access.

This page describes how to do the following:

  * Create Virtual Private Cloud (VPC) networks for exchange participant workloads, including Ultra Low Latency (ULL) VPC networks and general-purpose VPC networks.
  * Add your ULL VPC network as a spoke to the Network Connectivity Center (NCC) hub created by the exchange operator. This establishes ULL unicast connectivity and lets you complete multicast configurations to establish ULL multicast connectivity.



For an overview of the ULL infrastructure configuration process, see [Configuration overview for ULL Solution](https://docs.cloud.google.com/ull-solution/participants/configuration-overview).

## Before you begin

Before you create VPC networks for ULL Solution, see the following sections.

### Review VPC network requirements for ULL Solution

To complete the configuration process for ULL Solution, you need each of the following VPC networks.

Required VPC network | Supported instances and NICs | Description and network profile used  
---|---|---  
General-purpose VPC network | 

  * U4C (`nic0`)
  * U4S

|  A network for general-purpose traffic, including management and service access. You can use either of the following:  


  * A regular VPC network (no network profile)
  * A VPC network that is created with a regional network profile (regional VPC network), such as `us-south1-vpc-regional`. 

We recommend that you use a regional VPC network when configuring ULL Solution.  
ULL VPC network | 

  * U4C (`nic1`, `nic2`)

|  A network for ULL unicast and multicast traffic.  
  
To create this network, you use a zonal [participant ULL network profile](https://docs.cloud.google.com/ull-solution/participants/participant-ull-network-profile), such as `us-south1-d-vpc-ull-participant`.   
  
### Review supported and unsupported features in ULL VPC networks

Make sure that you review the [supported and unsupported features](https://docs.cloud.google.com/ull-solution/participants/participant-ull-network-profile) in participant ULL VPC networks. If you attempt to configure unsupported features during network creation, Google Cloud returns an error.

### Set your project

Set the gcloud CLI to use your project. Alternatively you can include the `--project=PROJECT_ID` flag for each command in the following procedures.
    
    
    gcloud config set project PROJECT_ID
    

Replace `PROJECT_ID` with the ID of your project.

### Enable APIs

If you haven't already, enable the following APIs.

###  Console 

Enable the Compute Engine and NCC APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com,networkconnectivity.googleapis.com)

###  gcloud 

Enable the Compute Engine and NCC APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    
    
    gcloud services enable compute.googleapis.com networkconnectivity.googleapis.com

### Required roles

To get the permissions that you need to create participant ULL VPC networks, ask your administrator to grant you the following IAM roles: 

  * To create and manage network resources: Compute Network Admin (`compute.networkAdmin`) on your project 
  * To create NCC spokes: Spoke Admin (`networkconnectivity.spokeAdmin`) on your project 
  * To propose NCC spokes to the hub associated with a multicast domain: Group User (`networkconnectivity.groupUser`) on the multicast administrator project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a general-purpose VPC network

This section describes how to create a VPC network for general-purpose traffic. You use this network for the `nic0` interfaces of ULL Compute Engine instances, and for creating non-ULL instances.

For more information about creating VPC networks, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network).

###  gcloud 

  1. Create a VPC network by using the [`compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create).
         
         gcloud compute networks create GENERAL_PURPOSE_NETWORK \
             --subnet-mode=custom \
             --network-profile=REGION-vpc-regional
         

Replace the following values:

     * `GENERAL_PURPOSE_NETWORK`: a name for the general-purpose VPC network.
     * `REGION`: to create a regional VPC network by using a regional network profile, specify the region in which you are configuring ULL Solution, such as `us-south1`. You can alternatively remove the `--network-profile` flag to create a regular VPC network.
  2. Add one or more subnets by using the [`compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
         
         gcloud compute networks subnets create GENERAL_PURPOSE_SUBNET \
             --network=GENERAL_PURPOSE_NETWORK \
             --range=PRIMARY_RANGE \
             --region=REGION
         

Replace the following values:

     * `GENERAL_PURPOSE_SUBNET`: a name for the subnet.
     * `GENERAL_PURPOSE_NETWORK`: the name of the general-purpose VPC network that you created previously.
     * `PRIMARY_RANGE`: the primary IPv4 range for the subnet, in CIDR notation. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).
     * `REGION`: the region in which you are configuring ULL Solution, such as `us-south1`.
  3. To connect to ULL compute instances by using SSH, the firewall rule configuration of the network for the `nic0` interface must allow SSH.

To configure firewall rules for the general-purpose VPC network that you created, see the [Cloud Next Generation Firewall documentation](https://docs.cloud.google.com/firewall/docs/about-firewalls). For regional VPC networks, we recommend that you use [regional network firewall policies](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies).




## Create a participant ULL VPC network

This section describes how to create a VPC network with the participant ULL network profile for ULL unicast and multicast traffic.

###  gcloud 

  1. Create a participant ULL VPC network by using the [`compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create) and specifying the appropriate zonal participant ULL network profile.
         
         gcloud compute networks create PARTICIPANT_ULL_NETWORK \
             --subnet-mode=custom \
             --network-profile=ZONE-vpc-ull-participant
         

Replace the following values:

     * `PARTICIPANT_ULL_NETWORK`: a name for the participant ULL VPC network.
     * `ZONE`: the zone in which to create the network. The zone must be from the [list of supported locations](https://docs.cloud.google.com/ull-solution/participants/configuration-overview#locations) for ULL Solution, such as `us-south1-d`.
  2. Add at least two subnets to the network for attachments from ULL Compute Engine instances. For a given ULL instance, `nic1` attaches to one subnet in the network, while `nic2` attaches to another subnet in the same network. To add a subnet, use the [`compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
         
         gcloud compute networks subnets create ULL_SUBNET \
             --network=PARTICIPANT_ULL_NETWORK \
             --range=PRIMARY_RANGE \
             --region=REGION
         

Replace the following values:

     * `ULL_SUBNET`: a name for the subnet.
     * `PARTICIPANT_ULL_NETWORK`: the name of the participant ULL VPC network that you created previously.
     * `PRIMARY_RANGE`: the primary IPv4 range for the subnet, in CIDR notation. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges).
     * `REGION`: the Google Cloud region in which the new subnet is created. Must be the region that contains the zone in which you created the network, such as `us-south1`.



## Add the ULL VPC network to a NCC hub

This section describes how to add your ULL VPC network to the NCC hub that was created by the exchange operator. To add your network, you create a VPC spoke in the _edge_ group.

Before proceeding, review the following:

  * This step lets you establish ULL unicast connectivity with the exchange operator, and provides access to the ULL Multicast domains that are associated with a hub so that you can complete multicast consumer configurations to enable ULL multicast connectivity.
  * You attach your ULL VPC networks to separate hubs created by the exchange operator for each zone. For example, one hub for ULL VPC networks in `us-south1-d` and one hub for ULL VPC networks in `us-south1-e`.
  * You don't add your general-purpose VPC network to the same hub as your ULL VPC networks. However, you can add your general-purpose VPC network to a separate hub created by the exchange operator when you [configure Cloud Multicast](https://docs.cloud.google.com/vpc/docs/multicast/configuration-overview).



For more information, see [Star topology](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#star-topology) and [Create a VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vpc-spoke) in the NCC documentation. If you use VPC Service Controls, see [Cross-project VPC spoke proposals across service perimeters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-use-vpcsc#cross-project-spoke-proposals) for the required ingress and egress rules.

###  gcloud 

  1. To add your network as an edge spoke to a hub, use the [`network-connectivity spokes linked-vpc-network create` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-connectivity/spokes/linked-vpc-network/create).
         
         gcloud network-connectivity spokes linked-vpc-network create SPOKE_NAME \
             --hub=projects/MULTICAST_ADMIN_PROJECT/locations/global/hubs/HUB_NAME \
             --vpc-network=PARTICIPANT_ULL_NETWORK \
             --group="edge" \
             --global \
             --include-export-ranges=INCLUDE_RANGES
         

Replace the following values:

     * `SPOKE_NAME`: a name for the edge spoke
     * `MULTICAST_ADMIN_PROJECT`: the ID of the exchange operator project that is used to administer multicast
     * `HUB_NAME`: the name of the NCC hub that was created by the exchange operator. Your multicast consumer network must attach to the same hub as the exchange operator's _multicast administrator network_ and _multicast producer network_. If necessary, contact the exchange operator for the name of the hub.

     * `PARTICIPANT_ULL_NETWORK`: the name of the participant ULL VPC network that you created previously

You can alternatively provide the URI of the participant ULL VPC network by using the following format: `projects/PROJECT_ID/global/networks/PARTICIPANT_ULL_NETWORK`.

     * `INCLUDE_RANGES`: a comma-separated list of IP address ranges to export to the hub.

By default, the spoke exports all subnet ranges. To avoid overlap with other spokes on the hub, you can specify which subnet ranges to export. If you specify subnet ranges, ensure that you include the ranges that host multicast consumers and any other ranges needed for communication with the spokes in the center group, such as for unicast traffic.

Google Cloud prohibits subnet overlaps across VPC spokes as described in [Subnet route uniqueness](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spoke-admin#subnet-uniqueness). For more information about using export filters to avoid overlap, see [VPC connectivity with export filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview#vpc-connectivity-with-export-filters).

  2. Contact the exchange operator to notify them that you proposed a VPC spoke to the hub.

If the hub is in a different project, then the exchange operator must explicitly approve your spoke before it becomes active, unless the exchange operator added your project as an auto-accept project.

To check the status of a spoke after you create it, see [Check the status of a VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-check-spoke-status).




## What's next

  * [Create firewall policies for ULL VPC networks](https://docs.cloud.google.com/ull-solution/participants/firewall/create-firewall-rules)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
