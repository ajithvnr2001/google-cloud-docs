---
url: https://docs.cloud.google.com/vpc/docs/create-vpc-network-rdma/
title: Create a VPC network for RDMA NICs \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:27.503684+00:00
---

# Create a VPC network for RDMA NICs  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/create-vpc-network-rdma/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a VPC network for RDMA NICs

This page describes how to create a VPC network with an RDMA network profile provided by Google Cloud.

You only need to configure a network profile if you want to run workloads that require RDMA NICs as described in [RDMA network profiles](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles). Otherwise, [create a regular VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) without a network profile.

## Before you begin

Make sure that you review the [supported and unsupported features](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles#supported-features) in VPC networks with an RDMA network profile. If you attempt to configure unsupported features, Google Cloud returns an error.

## Create a network with an RDMA network profile

To create a VPC network with an RDMA network profile, do the following.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click **Create VPC network**.

  3. In the **Name** field, enter a name for the network.

  4. Keep the **Set MTU automatically** checkbox selected. When this checkbox is selected, Google Cloud automatically sets the MTU to the default value for the type of VPC network that you are creating. For VPC networks with an RDMA network profile, the default MTU value is `8896`.

  5. Select **Configure network profile** and do the following:

     1. In the **Zone** field, select the zone of the network profile that you want to use. The VPC network that you create is constrained to this zone, which means that you can only create resources in the network in this zone.
     2. Select the RDMA network profile for the zone that you selected previously, such as `us-central1-b-vpc-falcon`, `us-central1-b-vpc-roce`, or `us-central1-b-vpc-roce-metal`.
     3. To view the set of supported features for the network profile that you selected, click **Preview network profile features**.
  6. In the **New subnet** section, specify the following configuration parameters for a subnet:

     1. In the **Name** field, enter a name for the subnet.
     2. In the **Region** field, select the region in which to create the subnet. This region must correspond to the zone of the network profile that you configured. For example, if you configured a network profile in the `us-central1-b` zone (such as `us-central1-b-vpc-roce`), then you must create the subnet in the `us-central1` region.
     3. Enter an **IPv4 range**. This range is the [primary IPv4 range](https://docs.cloud.google.com/vpc/docs/vpc#vpc_networks_and_subnets) for the subnet.

If you select a range that is not an RFC 1918 address, confirm that the range doesn't conflict with an existing configuration. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges).

     4. Click **Done**.

  7. To add more subnets, click **Add subnet** and repeat the previous steps. You can also [add more subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnets) to the network after you have created the network.

  8. Click **Create**.




###  gcloud 

  1. To create the network, use the [`gcloud compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create) and specify the `--network-profile` flag.
         
         gcloud compute networks create NETWORK \
               --subnet-mode=custom \
               --network-profile=NETWORK_PROFILE
         

Replace the following:

     * `NETWORK`: a name for the VPC network
     * `NETWORK_PROFILE`: the zone-specific name of the network profile, such as `us-central1-b-vpc-falcon`, `us-central1-b-vpc-roce`, or `us-central1-b-vpc-roce-metal`.

RDMA network profiles aren't available in all zones. To view the zone-specific instances of a network profile that are available, follow the instructions to [list network profiles](https://docs.cloud.google.com/vpc/docs/view-network-profiles#list_network_profiles).

  2. To add subnets, use the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
         
         gcloud compute networks subnets create SUBNET \
               --network=NETWORK \
               --range=PRIMARY_RANGE \
               --region=REGION
         

Replace the following:

     * `SUBNET`: a name for the new subnet
     * `NETWORK`: the name of the VPC network that contains the new subnet
     * `PRIMARY_RANGE`: the primary IPv4 range for the new subnet, in CIDR notation. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges).
     * `REGION`: the Google Cloud region in which the new subnet is created. This must correspond to the zone of the network profile that you configured. For example, if you configured a network profile in the `us-central1-b` zone (such as `us-central1-b-vpc-roce`), then you must create the subnet in the `us-central1` region.



###  API 

  1. To create the network, make a `POST` request to the [`networks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/insert) and specify the `networkProfile` property.
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks
         {
         "autoCreateSubnetworks": false,
         "name": "NETWORK",
         "networkProfile": "NETWORK_PROFILE"
         }
         

Replace the following:

     * `PROJECT_ID`: the ID of the project where the VPC network is created
     * `NETWORK`: a name for the VPC network
     * `NETWORK_PROFILE`: the zone-specific name of the network profile, such as `us-central1-b-vpc-falcon`, `us-central1-b-vpc-roce`, or `us-central1-b-vpc-roce-metal`.

RDMA network profiles aren't available in all zones. To view the zone-specific instances of a network profile that are available, follow the instructions to [list network profiles](https://docs.cloud.google.com/vpc/docs/view-network-profiles#list_network_profiles).

  2. To add subnets, make a `POST` request to the [`subnetworks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks
         {
         "ipCidrRange": "IP_RANGE",
         "network": "NETWORK_URL",
         "name": "SUBNET"
         }
         

Replace the following:

     * `PROJECT_ID`: the ID of the project that contains the VPC network to modify
     * `REGION`: the name of the Google Cloud region where the subnet is added. This region must correspond to the zone of the network profile that you configured. For example, if you configured a network profile in the `us-central1-b` zone (such as `us-central1-b-vpc-roce`), then you must create the subnet in the `us-central1` region.
     * `IP_RANGE`: the primary IPv4 address range for the subnet. For more information, see [IPv4 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges).
     * `NETWORK_URL`: the URL of the VPC network where you're adding the subnet
     * `SUBNET`: a name for the subnet



## What's next

  * To create instances in your network, see the procedure that corresponds to your instance type and deployment method: 
    * For GPU instances, see [Deployment options overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview).
    * For H4D instances, see [Create a VM with IRDMA driver support](https://docs.cloud.google.com/compute/docs/networking/using-irdma#create_a_vm_with_irdma_driver_support).
  * To get a general overview of network profiles, see [Network profiles for specific use cases](https://docs.cloud.google.com/vpc/docs/network-profiles).
  * To learn about RDMA network profiles, see [RDMA network profiles](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
