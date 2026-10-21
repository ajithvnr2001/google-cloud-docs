---
url: https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes/
title: Create and use IPv6 sub-prefixes \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:12.134818+00:00
---

# Create and use IPv6 sub-prefixes  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and use IPv6 sub-prefixes

This page describes how to divide your IPv6 public delegated prefix into sub-prefixes that you can assign to resources in specific projects. When you create a sub-prefix, your configuration includes a prefix length and a mode that determines how the IP addresses can be used.

The following modes are supported:

  * **For further delegation** (`--mode=DELEGATION`): Sub-prefixes that you can further divide into smaller sub-prefixes. The associated IP addresses can't be assigned to resources until you create a non-delegation mode sub-prefix.

  * **For forwarding rules** (`--mode=EXTERNAL_IPV6_FORWARDING_RULE_CREATION`): Sub-prefixes that you can use as a source of regional external global unicast address (GUA) ranges for forwarding rules. You choose a prefix length for the IPv6 addresses when you create the sub-prefix. The forwarding rules can only be used for regional external passthrough Network Load Balancers and external protocol forwarding. Sub-prefixes in this mode can't be further delegated.

  * **For external subnet ranges** (`--mode=EXTERNAL_IPV6_SUBNETWORK_CREATION`): Sub-prefixes that you can use as a source of GUAs for [external subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#external-ipv6). BYOIP-provided external subnet ranges can only be used by VM instances. Sub-prefixes in this mode can't be further delegated.

  * **For internal subnet ranges** (`--mode=INTERNAL_IPV6_SUBNETWORK_CREATION`): Sub-prefixes that you can use as a source of GUAs for [internal subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#internal-ipv6). When assigned to an internal subnet range, GUAs are used privately and aren't advertised to the internet. Sub-prefixes in this mode can't be further delegated.




The different modes support different prefix sizes and IPv6 access types. For more information, see the following section.

## Sub-prefix mode configuration

The following table describes the configuration settings and requirements for each sub-prefix mode.

Sub-prefix mode or setting | Prefix length specifications | IPv6 access type  
---|---|---  
**Sub-prefix for delegation**  
`(--mode=DELEGATION)` |  Can be the same size or smaller (have a longer prefix length) than the parent public delegated prefix The difference between the prefix length of a sub-prefix and its parent public delegated prefix can't be greater than 24 Valid lengths: `/32`, `/40`, `/48`, `/56` | 

  * `External`
  * `Internal`

  
**Sub-prefix for external forwarding rules**  
`(--mode=EXTERNAL_IPV6_FORWARDING_RULE_CREATION)` |  Can be the same size or smaller (have a longer prefix length) than the parent public delegated prefix The difference between the prefix length of a sub-prefix and its parent public delegated prefix can't be greater than 24 Valid lengths: `/32`, `/40`, `/48`, `/56`, `/64`, or `/72` | 

  * `External`

  
**Setting: External forwarding rule allocatable prefix length** Determines the prefix length for IPv6 address ranges that are used by external forwarding rules. Specified when creating an IPv6 sub-prefix for external forwarding rules. |  Must be smaller than the associated sub-prefix—the difference between the allocatable prefix length and the sub-prefix length must be at least 8, and can't be greater than 32 Valid lengths: `/48`, `/56`, `/64`, `/72`, `/80`, `/88`, `/96` Default lengths:

  * If the parent sub-prefix's length is `/64` or `/72`, the default allocatable prefix length is `/96`
  * Otherwise, the default allocatable prefix length is `/64`

|   
**Sub-prefix for external subnet ranges**  
`(--mode=EXTERNAL_IPV6_SUBNETWORK_CREATION)` |  Can be the same size or smaller (have a longer prefix length) than the parent public delegated prefix The difference between the prefix length of a sub-prefix and its parent public delegated prefix can't be greater than 24 Valid lengths: `/32`, `/40`, `/48`, `/56` | 

  * `External`

  
**Sub-prefix for internal subnet ranges**  
`(--mode=INTERNAL_IPV6_SUBNETWORK_CREATION)` |  Can be the same size or smaller (have a longer prefix length) than the parent public delegated prefix The difference between the prefix length of a sub-prefix and its parent public delegated prefix can't be greater than 24 Valid lengths: `/32`, `/40`, `/48`, `/56` | 

  * `Internal`

  
  
## Sub-prefix delegation

IPv6 sub-prefixes that are in delegation mode can be sub-delegated into smaller sub-prefixes. This lets you assign the address blocks to different projects or regions. When you sub-delegate a sub-prefix, the following applies:

  * A public delegated prefix can be sub-delegated up to three times from a public advertised prefix.
  * IPv6 sub-prefixes can only be sub-delegated if they are in delegation mode. 
  * Public delegated prefixes and sub-prefixes inherit the [access type](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#access-type) that you specify when you create a parent public advertised prefix.
  * The prefix length of a delegation mode sub-prefix affects the possible modes of its child sub-prefixes. This is because a child sub-prefix must have a prefix length that is valid for its mode, and the prefix length must be the same size as or smaller than its parent.



The following example demonstrates a multi-level delegation. Each step adheres to the prefix length and mode restrictions that are detailed in the sub-prefix mode table. If you have an external access public advertised prefix with IP address range `2001:db8::/32`, you might do the following:

  1. From the parent public advertised prefix, you can create one or more top-level public delegated prefixes. A top-level public delegated prefix can be the same size or smaller than its parent public advertised prefix, and it must be in delegation mode. For this example, the entire IP address range of the parent prefix is delegated (`2001:db8::/32`).

  2. From the top-level public delegated prefix, you can create one or more sub-prefixes. A sub-prefix can be the same size as or smaller than its parent public delegated prefix, and it can be in any mode that's compatible with its access type. For this example, another delegation mode sub-prefix is created with IP address range `2001:db8::/48`.

  3. From the previous sub-prefix, you can create one or more sub-prefixes. To make the IP addresses available for resources, these prefixes must be in a non-delegation mode such as forwarding rule or subnet creation mode. For this example, two sub-prefixes are created: one for external subnet ranges with IP address range `2001:db8:0:0::/56` and one for external forwarding rules with IP address range `2001:db8:1:0::/64`.




At this point, you can't further divide the sub-prefixes that use the `2001:db8:0:0::/56` or `2001:db8:1:0::/64` ranges. A sub-prefix can't be divided if it's in a non-delegation mode or if it already has three levels of delegation from its parent public advertised prefix. In this example, both conditions are true.

## Before you begin

  1. Create an IPv6 [public advertised prefix](https://docs.cloud.google.com/vpc/docs/create-pap).
  2. Create an IPv6 [public delegated prefix](https://docs.cloud.google.com/vpc/docs/create-pdp).



### Roles

To get the permissions that you need to complete the tasks in this guide, ask your administrator to grant you the [Compute Public IP Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.publicIpAdmin) (`roles/compute.publicIpAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create IPv6 sub-prefixes

When you create an IPv6 sub-prefix, all IP addresses in the sub-prefix are made available; there is no reserved network address or broadcast address.

You can't change the mode of a sub-prefix. If needed, you can [delete it](https://docs.cloud.google.com/vpc/docs/deprovision-byoip#delete-pdp) and then recreate it. Before you can delete a sub-prefix, it must not be in use by any resources.

You can't edit a sub-prefix to change its name. As a best practice, choose generic names that don't need to change—for example, `sub-2001-db8-0-0-0-0-0-0-40`, where `sub` denotes the resource type and `2001-db8-0-0-0-0-0-0-40` denotes the specific prefix and prefix length.

###  Console 

  1. In the Google Cloud console, go to **Bring your own IP**.

[Go to Bring your own IP](https://console.cloud.google.com/networking/byoip)

  2. Click the public delegated prefix that you want to subdivide.

  3. Click **Create sub-prefix**.

  4. Enter a name and optional description for the sub-prefix.

  5. In the **Prefix length** list, select a prefix length for the sub-prefix.

  6. Enter an IPv6 address range to assign to the sub-prefix.

  7. In the **How this PDP will be used** section, do the following:

     * To create a sub-prefix for further delegation, select **Subdivide into smaller PDPs**.
     * To create a sub-prefix with addresses that you can assign to resources, select **Allocate IPv6 address ranges for use** , and then specify how you want to use the IP addresses: 
       * For external forwarding rules for regional external passthrough Network Load Balancers and external protocol forwarding, select **External Network Load Balancer forwarding rule** , and then select an **Allocatable prefix length**.
       * For external subnet ranges that can only host VMs, select **External subnet range for VMs**.
       * For internal subnet ranges, select **Internal subnet range**.
  8. In the **Project** menu, select the project that you want to use the sub-prefix in.

  9. Click **Create**.




###  gcloud 

Use the [`gcloud compute public-delegated-prefixes create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/create).
    
    
    gcloud compute public-delegated-prefixes create SUB_PREFIX_NAME \
        --range=SUB_PREFIX_RANGE \
        --mode=MODE \
        --public-delegated-prefix=PDP_NAME \
        --region=PDP_REGION \
        --project=PROJECT_ID \
        [--allocatable-prefix-length=PREFIX_LENGTH]
    

Replace the following:

  * `SUB_PREFIX_NAME`: a name for this sub-prefix

  * `SUB_PREFIX_RANGE`: the IP address range for this sub-prefix, in CIDR notation

  * `MODE`: the mode for this sub-prefix, which must be one of the following:

    * `DELEGATION`
    * `EXTERNAL_IPV6_FORWARDING_RULE_CREATION`
    * `EXTERNAL_IPV6_SUBNETWORK_CREATION`
    * `INTERNAL_IPV6_SUBNETWORK_CREATION`

The mode must be compatible with the [access type](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#access-type) of the parent public delegated prefix.

  * `PDP_NAME`: the parent public delegated prefix of this sub-prefix

  * `PDP_REGION`: the region for this sub-prefix

  * `PROJECT_ID`: the project to delegate the sub-prefix to

If the `--project` flag is omitted, the sub-prefix is created in the same project as the parent public delegated prefix.

  * `PREFIX_LENGTH`: the prefix length for the IPv6 address ranges that are used by forwarding rules

Only use this flag with `EXTERNAL_IPV6_FORWARDING_RULE_CREATION` mode. The default and possible values depend on the prefix length of `SUB_PREFIX_RANGE`. For more information, see Allocatable prefix length for forwarding rules. 




## Assign IPv6 subnet ranges

You can assign external or internal [IPv6 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges) by using sub-prefixes. IPv6 subnet ranges that are created from a sub-prefix use global unicast addresses (GUAs). The way that you can use the assigned range depends on the access type and mode of the sub-prefix:

  * External subnet ranges are assigned from `EXTERNAL_IPV6_SUBNETWORK_CREATION` mode sub-prefixes. BYOIP-provided external subnet ranges can only be used to reserve static external IP addresses with the `VM` endpoint type and assign static or ephemeral external addresses to VM instances.

  * Internal subnet ranges are assigned from `INTERNAL_IPV6_SUBNETWORK_CREATION` mode sub-prefixes. BYOIP-provided internal subnet ranges are configured with privately used GUAs aren't advertised to the internet. The addresses can be used in the same way as a Google-provided ULA internal subnet range.




### Create subnets with IPv6 BYOIP ranges

When creating a new subnet, you can allocate an IPv6 address range from your sub-prefix.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. To view the **VPC network details** page, click the name of a VPC network.

  3. On the **Subnets** tab, click add_box**Add subnet**. In the panel that appears:

     1. Provide a name.
     2. Select a region.
     3. For **IP stack type** , select either **IPv4 and IPv6 (dual-stack)** or **IPv6 (single-stack)**.
     4. If you are creating a dual-stack subnet, enter an IPv4 range.
     5. For **IPv6 access type** , select the access type of the sub-prefix that you want to assign to the subnet.
     6. Select the **From PDP** checkbox.
     7. In the **PDP** list, select the sub-prefix to use for allocating IP addresses to the subnet.
     8. Optional: Enter a specific IPv6 CIDR range to assign to the subnet. To let Google Cloud automatically select an address block, skip this step.
     9. Click **Add**.



###  gcloud 

Use the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
    
    
    gcloud compute networks subnets create SUBNET \
        --network=NETWORK \
        --stack-type=STACK_TYPE \
        --ipv6-access-type=ACCESS_TYPE \
        --region=REGION \
        --ip-collection=PDP_NAME \
        {--external-ipv6-prefix=EXTERNAL_IPV6_RANGE | --internal-ipv6-prefix=INTERNAL_IPV6_RANGE}
        [--range=PRIMARY_IPv4_RANGE]
    

Replace the following:

  * `SUBNET`: a name for the new subnet
  * `NETWORK`: the name of the VPC network that will contain the new subnet
  * `STACK_TYPE`: the subnet's stack type

The stack type can be `IPV4_IPV6` or `IPV6_ONLY`. If you use `IPV4_IPV6`, you must specify a primary IPv4 range by using the `--range` flag.

  * `ACCESS_TYPE`: the access type of the sub-prefix that you're assigning to this subnet. Enter `EXTERNAL` to assign the subnet an external GUA subnet range. Enter `INTERNAL` to assign the subnet a privately used internal GUA subnet range.

  * `REGION`: the Google Cloud region in which the new subnet will be created, which must be the same region as this subnet's sub-prefix

  * `PDP_NAME`: the name of an IPv6 sub-prefix in `EXTERNAL_IPV6_SUBNETWORK_CREATION` or `INTERNAL_IPV6_SUBNETWORK_CREATION` mode to use for assigning IP addresses to this subnet

  * `EXTERNAL_IPV6_RANGE` or `INTERNAL_IPV6_RANGE`: an optional `/64` IPv6 CIDR range to assign to this subnet

The range must be associated with the subnet's sub-prefix. If empty, Google Cloud assigns the subnet a random `/64` range from the CIDR block of the associated sub-prefix.

  * `PRIMARY_IPv4_RANGE`: for dual-stack subnets, the primary IPv4 range for the new subnet, in CIDR notation




### Add an IPv6 BYOIP range to an IPv4-only subnet

You can change an IPv4-only subnet into a dual-stack subnet that uses an IPv6 address range from a sub-prefix.

###  Console 

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. Click the name of the VPC network that contains the subnet to update.

  3. Click **Subnets** , and then click the name of the subnet to update.

  4. Click **Edit**.

  5. In the **IP stack type** section, select **IPv4 and IPv6 (dual-stack)**.

  6. For **IPv6 access type** , select the access type of the sub-prefix that you want to assign to the subnet.

  7. Click the **From PDP** checkbox.

  8. In the **PDP** list, select the sub-prefix to use for allocating IP addresses to the subnet.

  9. Optional: Enter a specific IPv6 address range to assign to the subnet.

  10. Click **Save**.




###  gcloud 

Use the [`gcloud compute networks subnets update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/update).
    
    
    gcloud compute networks subnets update SUBNET \
        --ipv6-access-type=ACCESS_TYPE \
        --stack-type=IPV4_IPV6 \
        --ip-collection=PDP_NAME \
        --region=REGION \
        {--external-ipv6-prefix=EXTERNAL_IPV6_RANGE | --internal-ipv6-prefix=INTERNAL_IPV6_RANGE}
    

Replace the following:

  * `SUBNET`: a name for the new subnet
  * `ACCESS_TYPE`: the access type of the sub-prefix that you're assigning to this subnet. Enter `EXTERNAL` to assign the subnet an external GUA subnet range. Enter `INTERNAL` to assign the subnet a privately used internal GUA subnet range.
  * `PDP_NAME`: the name of an IPv6 sub-prefix in `EXTERNAL_IPV6_SUBNETWORK_CREATION` or `INTERNAL_IPV6_SUBNETWORK_CREATION` mode to use for assigning IP addresses to this subnet
  * `REGION`: the Google Cloud region in which the new subnet will be created, which must be the same region as this subnet's sub-prefix
  * `EXTERNAL_IPV6_RANGE` or `INTERNAL_IPV6_RANGE`: an optional `/64` IPv6 CIDR range to assign to this subnet

The range must be associated with the subnet's sub-prefix. If empty, Google Cloud assigns the subnet a random `/64` range from the CIDR block of the associated sub-prefix.




### Deploy resources in subnets with IPv6 BYOIP ranges

After you create or update a subnet with a BYOIP-provided range, you can deploy resources that use the range's IP addresses.

For general information about assigning static and ephemeral IPv6 addresses to instances, see [Configure IPv6 addresses for instances](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address).

For information about assigning static external IPv6 addresses to VM instances, see the following:

  * [Reserve static external IPv6 addresses](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#reserve_new_static)
  * [Configure static external IPv6 addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address)



For information about assigning internal IPv6 addresses to VM instances or forwarding rules, see the following:

  * [Internal forwarding rules](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts#internal_fr)
  * [Reserve static internal IPv6 addresses](https://docs.cloud.google.com/vpc/docs/reserve-static-internal-ip-address)
  * [Configure static internal IPv6 addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-internal-ip-address)



## Create external forwarding rules

You can use an `EXTERNAL_IPV6_FORWARDING_RULE_CREATION` mode sub-prefix to assign regional external IPv6 address ranges to forwarding rules. External forwarding rules with BYOIP-provided ranges can only be used by [regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer) and [external protocol forwarding](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding).

You assign the ranges by using either [ephemeral or static IP addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses#ephemeral_and_static_ip_addresses). To use static IP addresses, reserve an IP address resource for your range before you create the forwarding rule. To use ephemeral IP addresses, let Google Cloud assign the address range when you create the forwarding rule.

### Reserve an IP address range for external forwarding rules from an IPv6 sub-prefix

When you create a static IPv6 address resource, the single IPv6 address that you specify represents the base address for a reserved range. The size of the range matches the allocatable prefix length of the sub-prefix.

###  Console 

  1. In the Google Cloud console, go to the **IP addresses** page.

[Go to IP addresses](https://console.cloud.google.com/networking/addresses/list)

  2. Click **Reserve external**.

  3. For **Name** , enter a name for the IP address resource.

  4. Optional: In the **Description** box, enter a description.

  5. For **IP version** , select **IPv6**.

  6. For **Type** , select **Regional**.

  7. For **Source** , select **IP collection**.

  8. Click **BYOIP IP collection** , and then select the IPv6 sub-prefix that contains the address range you want to reserve.

  9. Optional: To reserve a specific IP address range, enter an IP address in the **IP address** box. To let Google Cloud select the range automatically, leave the box blank.

  10. Click **Reserve**.




###  gcloud 

Use the [`gcloud compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create).
    
    
    gcloud compute addresses create ADDRESS_NAME \
        --region=REGION \
        --ip-collection=PDP_NAME \
        --addresses=IPV6_ADDRESS \
        --description=DESCRIPTION \
        --endpoint-type=NETLB
    

Replace the following:

  * `ADDRESS_NAME`: a name for the reserved address
  * `REGION`: the region of the address, which must match the region of the public delegated prefix
  * `PDP_NAME`: the name of an `EXTERNAL_IPV6_FORWARDING_RULE_CREATION` mode public delegated prefix that contains the IP address range to reserve
  * `IPV6_ADDRESS`: an optional IPv6 address from the public delegated prefix's CIDR range

Specify the first IPv6 address in the range you want to reserve. Omit to assign the range automatically.

  * `DESCRIPTION`: an optional description




### Assign BYOIP IPv6 ranges to external forwarding rules

To create forwarding rules for external passthrough Network Load Balancers, see the following:

  * [Create a BYOIP forwarding rule for a regional external passthrough Network Load Balancer with a backend service](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service#byoip-ipv6)
  * [Create a BYOIP forwarding rule for a regional external passthrough Network Load Balancer for multiple IP protocols](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-networklb-multiple-protocols#byoip-ipv6)
  * [Create a BYOIP forwarding rule for a regional external passthrough Network Load Balancer with zonal NEGs](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-zonal-neg#byoip-ipv6)



You can also create forwarding rules for external protocol forwarding. When you do this, you specify an address from your sub-prefix by providing either the name of a static external IP address resource or the IP address itself. For more information, see [Set up external protocol forwarding](https://docs.cloud.google.com/load-balancing/docs/set-up-protocol-forwarding#set-up-ext-pf).

### Promote an ephemeral BYOIP IPv6 address

If you created an external forwarding rule that uses an ephemeral IP address range from a BYOIP sub-prefix, you can promote the range to a static external IP address. This prevents the range from being released if the forwarding rule is deleted.

###  Console 

  1. Go to the **IP addresses** page.

[Go to IP addresses](https://console.cloud.google.com/networking/addresses)

  2. Click **External IP addresses**.

  3. Optional: In the **Filter** field, search for the base IP address of the ephemeral range that you want to promote.

  4. In the **More actions** menu (more_vert) of the IP address that you want to promote, select **Promote to static IP address**.

  5. Enter a name for the new static IP address, and then click **Reserve**.




###  gcloud 

Use the [`gcloud compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create).
    
    
    gcloud compute addresses create ADDRESS_NAME \
        --addresses=IPV6_ADDRESS \
        --region=REGION \
        --endpoint-type=NETLB
    

Replace the following:

  * `ADDRESS_NAME`: a name for the reserved address
  * `IPV6_ADDRESS`: the first IP address of the ephemeral range that is assigned to the forwarding rule
  * `REGION`: the region of the public delegated prefix that contains the address range you want to promote



## List prefixes

You can list all public advertised prefixes and public delegated prefixes (including sub-prefixes) in a project.

###  Console 

  1. In the Google Cloud console, go to **Bring your own IP**.

[Go to Bring your own IP](https://console.cloud.google.com/networking/byoip)

  2. All public advertised prefixes, public delegated prefixes, and sub-prefixes are displayed.




###  gcloud 

To list public delegated prefixes, including sub-prefixes, use the [`public-delegated-prefixes list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/list).
    
    
    gcloud compute public-delegated-prefixes list
    

## What's next

  * [Manage BGP announcement (v2)](https://docs.cloud.google.com/vpc/docs/manage-bgp-announcement)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
