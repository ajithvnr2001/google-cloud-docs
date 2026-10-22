---
url: https://docs.cloud.google.com/firewall/docs/create-manage-roce-vpcs/
title: Create and manage firewall rules for RoCE VPC networks \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:52:08.394552+00:00
---

# Create and manage firewall rules for RoCE VPC networks  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/create-manage-roce-vpcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Create and manage firewall rules for RoCE VPC networks Stay organized with collections  Save and categorize content based on your preferences. 

A Virtual Private Cloud (VPC) network that uses the Remote Direct Memory Access (RDMA) over Converged Ethernet (RoCE) network profile is called an _RoCE VPC network_. This page shows you how to create an RoCE VPC network and configure firewall rules that apply to the network. Before you begin, review the following information:

  * [RDMA RoCE network profile](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles)
  * [Cloud NGFW for RoCE VPC networks](https://docs.cloud.google.com/firewall/docs/firewall-for-roce)



Because the rules in a regional network firewall policy used by an RoCE VPC network rely heavily on target secure tags and source secure tags, ensure that you're familiar with how to [create and manage secure tags](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls) and [bind secure tags](https://docs.cloud.google.com/firewall/docs/use-tags-for-firewalls#bind-tags) to the VM instances.

This section describes how to perform the following tasks:

  * Create an RoCE VPC network
  * Create a regional network firewall policy that works with the RoCE VPC network
  * Create rules in the regional network firewall policy
  * Associate the regional network firewall policy with the RoCE VPC network



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



## Create a regional network firewall policy

RoCE VPC networks only support regional network firewall policies that have a policy type of `RDMA_ROCE_POLICY`.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your project within your organization.

  3. Click **Create firewall policy**.

  4. In the **Name** field, enter a policy name.

  5. For **Policy type** , select **RDMA RoCE policy**.

  6. Click **Create**.




###  gcloud 

To create a regional network firewall policy for a RoCE VPC network, use the [`gcloud compute network-firewall-policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/create):
    
    
      gcloud compute network-firewall-policies create FIREWALL_POLICY \
          --region REGION \
          --policy-type=RDMA_ROCE_POLICY
    

Replace the following:

  * `FIREWALL_POLICY`: a name for the network firewall policy
  * `REGION`: a region you want to apply to the policy. The region must contain the zone of the RoCE network profile used by the RoCE VPC network.



## Create rules in the regional network firewall policy

Regional network firewall policies that have a policy type of `RDMA_ROCE_POLICY` only support ingress rules, and have constraints on valid source, action, and Layer 4 configuration flags. For more information, see [Specifications](https://docs.cloud.google.com/firewall/docs/firewall-for-roce#specifications).

###  Console 

To create an ingress rule that uses the source IP range `0.0.0.0/0` and applies to all network interfaces in the RoCE VPC network, do the following:

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector list, select your project or the folder that contains your policy.

  3. Click the name of your policy and then click **Create firewall rule**.

  4. Enter the priority of the rule.

  5. For **Target** , select **Apply to all**.

  6. For **Source** , select **All IP addresses (0.0.0.0/0)**.

  7. For **Action on match** , specify whether connections that match the rule are allowed (**Allow**) or denied (**Deny**).

  8. For **Logs** , choose **On** or **Off**.

  9. Click **Create**.




To create an ingress rule that uses a source secure tag and applies to specific network interfaces of VMs with an associated secure tag value, do the following:

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector list, select your project or the folder that contains your policy.

  3. Click the name of your policy and then click **Create firewall rule**.

  4. Enter the priority of the rule.

  5. For **Target** , select **Apply to all**.

  6. For **Source** , select **Secure tags** and do the following:

     1. Click **Select scope for tags**.
     2. On the **Select a resource** page, select the organization or project in which you want to create secure tags.
     3. Select the key-value pairs to which the rule is to apply.
     4. To add more key-value pairs, click **Add tag**.
  7. For **Logs** , choose **On** or **Off**.

  8. Click **Create**.




###  gcloud 

To create an ingress rule that uses the `--src-ip-ranges=0.0.0.0/0` flag and applies to all network interfaces in the RoCE VPC network, use the [`gcloud compute network-firewall-policies rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules/create):
    
    
      gcloud compute network-firewall-policies rules create PRIORITY \
          --direction=ingress \
          --layer4-configs=all \
          --enable-logging \
          --action ACTION \
          --firewall-policy FIREWALL_POLICY_NAME\
          --firewall-policy-region FIREWALL_POLICY_REGION \
          --src-ip-ranges=0.0.0.0/0
    

To create an ingress rule that uses a source secure tag and applies to specific network interfaces of VMs with an associated secure tag value, use the [`gcloud compute network-firewall-policies rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules/create):
    
    
      gcloud compute network-firewall-policies rules create PRIORITY \
          --direction=ingress \
          --layer4-configs=all \
          --enable-logging \
          --action ALLOW \
          --firewall-policy FIREWALL_POLICY_NAME\
          --firewall-policy-region FIREWALL_POLICY_REGION \
          --src-secure-tag SRC_SECURE_TAG[,SRC_SECURE_TAG,...] \
          --target-secure-tag TARGET_SECURE_TAG[,TARGET_SECURE_TAG,...]
    

Replace the following:

  * `PRIORITY`: the [priority](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#priority) of the rule
  * `ACTION`: the [action on match](https://docs.cloud.google.com/firewall/docs/firewalls#action_of_the_rule) of the rule 
    * If you use `--src-ip-ranges=0.0.0.0/0`, you can use either `ALLOW` or `DENY`.
    * If you use `--src-secure-tag`, you can only use `ALLOW`.
  * `FIREWALL_POLICY_NAME`: a name of the regional network firewall policy in which the rule is created.
  * `FIREWALL_POLICY_REGION`: the region used by the regional network firewall policy in which the rule is created.
  * `SRC_SECURE_TAG`: defines the [source parameter of the ingress rule](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#hfp-nfp-ingress-src) using a comma-separated list of secure tag values. For more information, see [Secure tags for firewalls](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview).
  * `TARGET_SECURE_TAG`: defines the [target parameter of the rule](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-details#targets) using a comma-separated list of secure tag values. For more information, see [Secure tags for firewalls](https://docs.cloud.google.com/firewall/docs/tags-firewalls-overview).



## Associate the regional network firewall policy with an RoCE VPC network

Associate the regional network firewall policy with your RoCE VPC network. This ensures that the policy's rules apply to the `MRDMA` network interfaces within that network.

###  Console 

  1. In the Google Cloud console, go to the **Firewall policies** page.

[Go to Firewall policies](https://console.cloud.google.com/net-security/firewall-manager/firewall-policies/list)

  2. In the project selector menu, select your project that contains the policy with your RoCE VPC network.

  3. Click your policy.

  4. Click the **Associations** tab.

  5. Click **Add Associations**.

  6. Select the RDMA RoCE networks within the project.

  7. Click **Associate**.




###  gcloud 

To associate a regional network firewall policy with an RoCE VPC network, use the [`gcloud compute network-firewall-policies associations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations/create):
    
    
      gcloud compute network-firewall-policies associations create \
          --firewall-policy FIREWALL_POLICY \
          --network NETWORK \
          --firewall-policy-region FIREWALL_POLICY_REGION
      

Replace the following:

  * `FIREWALL_POLICY`: a name of the regional network firewall policy

The regional network firewall policy must have a policy type of `RDMA_ROCE_POLICY`.

  * `NETWORK`: a name of the RoCE VPC network

  * `FIREWALL_POLICY_REGION`: the region of the firewall policy

The region must contain the zone of the RoCE network profile used by the RoCE VPC network.




## What's next

  * [Network profiles overview](https://docs.cloud.google.com/firewall/docs/network-profiles)
  * [Cloud NGFW for RoCE VPC networks](https://docs.cloud.google.com/firewall/docs/firewall-for-roce)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
