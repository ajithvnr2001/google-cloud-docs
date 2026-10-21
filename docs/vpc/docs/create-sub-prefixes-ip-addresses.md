---
url: https://docs.cloud.google.com/vpc/docs/create-sub-prefixes-ip-addresses/
title: Create IPv4 sub-prefixes and IPv4 addresses \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:31.363632+00:00
---

# Create IPv4 sub-prefixes and IPv4 addresses  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/create-sub-prefixes-ip-addresses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create IPv4 sub-prefixes and IPv4 addresses

This page describes how to divide your IPv4 public delegated prefix and create BYOIP addresses to use with Google Cloud resources. You can create IPv4 BYOIP addresses from a public delegated prefix or sub-prefix.

If you want to divide an IPv6 public delegated prefix, see [Create IPv6 sub-prefixes](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes).

## Before you begin

  1. Create an IPv4 [public advertised prefix](https://docs.cloud.google.com/vpc/docs/create-pap).
  2. Create an IPv4 [public delegated prefix](https://docs.cloud.google.com/vpc/docs/create-pdp).



### Roles

To get the permissions that you need to complete the tasks in this guide, ask your administrator to grant you the [Compute Public IP Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.publicIpAdmin) (`roles/compute.publicIpAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create sub-prefixes

You can divide a public delegated prefix into smaller IP address ranges by creating a sub-prefix. A sub-prefix is a public delegated prefix that has a public delegated prefix parent.

BYOIP v2 IPv4 sub-prefixes and IP addresses inherit the [network tier of their parent public delegated prefix](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#service-tiers). 

A sub-prefix name can't be changed without deleting and recreating the resource. For this reason, we recommend that you create generic names that won't need to change—for example, `sub-203-0-113-0-28`, where `sub` denotes the resource type and `203-0-113-0-28` denotes the specific prefix and prefix length.

A public delegated prefix can be sub-delegated up to three times from a public advertised prefix. For example, if you have a public advertised prefix with IP address range `203.0.113.0/24`, you can do the following:

  * Create a public delegated prefix with IP address range `203.0.113.0/25` from the public advertised prefix.
  * Create a sub-prefix with IP address range `203.0.113.0/26` that has the previous public delegated prefix as its parent.
  * Create a sub-prefix with IP address range `203.0.113.0/27` that has the previous sub-prefix as its parent.



At this point, you cannot create further sub-prefixes that have the `203.0.113.0/27` sub-prefix as a parent.

###  Console 

  1. In the Google Cloud console, go to **Bring your own IP**.

[Go to Bring your own IP](https://console.cloud.google.com/networking/byoip)

  2. Click the public delegated prefix that you want to subdivide.

  3. Click **Create sub-prefix**.

  4. Enter a **Name** and optional **Description** for the sub-prefix.

  5. Select a **Prefix length** for the sub-prefix.

  6. Select **IP addresses** for the sub-prefix.

  7. Select a **Project** for the sub-prefix. The IP addresses are made available in this project only.

  8. Click **Create**.




###  gcloud 

To create a sub-prefix from a public delegated prefix, use the [`public-delegated-prefixes delegated-sub-prefixes create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/create)
    
    
    gcloud compute public-delegated-prefixes \
        delegated-sub-prefixes \
        create SUB_PREFIX_NAME \
        --range=SUB_PREFIX_RANGE \
        --public-delegated-prefix=PDP_NAME \
        --public-delegated-prefix-region=PDP_REGION \
        --delegatee-project=PROJECT_ID
    

Replace the following:

  * `SUB_PREFIX_NAME`: a name for the sub-prefix that you are creating.

  * `SUB_PREFIX_RANGE`: the IP address range for the sub-prefix that you are creating.

  * `PDP_NAME`: the parent public delegated prefix or sub-prefix that contains the sub-prefix you are creating.

  * `PDP_REGION`: the region of the public delegated prefix or sub-prefix that contains the sub-prefix you are creating.

  * `PROJECT_ID`: an optional project ID for the sub-prefix. The following describes the behavior for this value:

    * If you specify a value, the IP addresses are available only in the specified project.

    * If you don't use `--delegatee-project`, the IP addresses are available in the same project as the sub-prefix's parent public delegated prefix or sub-prefix.




## List prefixes

You can list all public advertised prefixes and public delegated prefixes (including sub-prefixes) in a project.

###  Console 

  1. In the Google Cloud console, go to **Bring your own IP**.

[Go to Bring your own IP](https://console.cloud.google.com/networking/byoip)

  2. All public advertised prefixes, public delegated prefixes, and sub-prefixes are displayed.




###  gcloud 

To list public delegated prefixes, including sub-prefixes, use the [`public-delegated-prefixes list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/list).
    
    
    gcloud compute public-delegated-prefixes list
    

## Create IP addresses

You must create [static external IP address resources](https://docs.cloud.google.com/vpc/docs/ip-addresses) before you can use the IP addresses in an IPv4 public delegated prefix or sub-prefix. There are two ways to do this:

  * **Create blocks of IP addresses** : You can create blocks of IP addresses from a public delegated prefix's entire range or a subset of it. This is the only supported method for the following:

    * Creating IP addresses from public delegated prefixes that don't use enhanced IP address allocation
    * Creating global IP addresses
  * **Create single IP addresses** : For v2 public delegated prefixes that [use enhanced IP address allocation](https://docs.cloud.google.com/vpc/docs/create-pdp#check-allocation), you can create single IP addresses, choosing a specific address or letting Google Cloud select one automatically.




After you create IP addresses from a public delegated prefix, you can still use the rest of the prefix to create other IP addresses or sub-prefixes.

### Create a block of IP addresses

The IP addresses that you create from a public delegated prefix or sub-prefix can be regional or global. All IP addresses in a public delegated prefix or sub-prefix are available; there is no reserved network address or broadcast address. For example, if you create IP addresses from the entire range of a `/28` public delegated prefix or sub-prefix, 16 IP address resources are created.

You can [list all static external IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/reserve-static-external-ip-address#list_ip). This list includes IP addresses that you have brought to Google Cloud and IP addresses that are provided by Google Cloud.

BYOIP addresses are created with names in a consistent format. For example, `203.0.113.144` is assigned the name `address-203-0-113-144`.

###  Console 

  1. In the Google Cloud console, go to **Bring your own IP**.

[Go to Bring your own IP](https://console.cloud.google.com/networking/byoip)

  2. Click the public delegated prefix or sub-prefix that you want to create IP addresses in.

  3. Click **Create addresses**.

  4. Select the **Prefix length**.

  5. Select the range of **IP addresses** you want to create.

  6. Click **Create addresses**.




###  gcloud 

To create IP addresses from a public delegated prefix or sub-prefix, use the [`public-delegated-prefixes delegated-sub-prefixes create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/delegated-sub-prefixes/create).
    
    
    gcloud compute public-delegated-prefixes \
        delegated-sub-prefixes \
        create ADDRESSES_NAME \
        --create-addresses \
        --range=RANGE \
        --public-delegated-prefix=PDP_NAME \
        --public-delegated-prefix-region=PDP_REGION
    

Replace the following:

  * `ADDRESSES_NAME`: a name for the group of addresses that you are creating.

  * `RANGE`: the CIDR block to create IP addresses from, which must be a subset of the parent prefix's range. Omit this flag to create IP addresses for the whole range of the parent prefix.

  * `PDP_NAME`: the public delegated prefix or sub-prefix that you are creating IP addresses for.

  * `PDP_REGION`: the region of the public delegated prefix or sub-prefix that you are creating IP addresses for.




### Create a single IP address

You can create single static IP addresses from v2 regional IPv4 public delegated prefixes or sub-prefixes that use enhanced IP address allocation. Only prefixes created after December 13, 2025 support this feature. To check if a prefix uses enhanced IP address allocation, [describe the prefix](https://docs.cloud.google.com/vpc/docs/create-pdp#check-allocation).

###  Console 

  1. In the Google Cloud console, go to the **IP addresses** page. 

[Go to IP addresses](https://console.cloud.google.com/networking/addresses/list)

  2. Click **Reserve external**.
  3. In the **Name** field, enter an IP address name.
  4. Select **Premium**.
  5. Select **IPv4**.
  6. Select **Regional**.
  7. For **Source** , select **IP collection**.
  8. Click **IP collection** , and then select the public delegated prefix that contains the IP address you want to create.
  9. For **IP address** , optionally enter a specific IP address to use. To let Google Cloud automatically select an address from the public delegated prefix's CIDR block, omit the IP address.
  10. Click **Reserve**.



###  gcloud 

Use the [`gcloud compute addresses create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/addresses/create).
    
    
    gcloud compute addresses create NAME \
        --network-tier=PREMIUM \
        --ip-collection=PDP_NAME \
        --addresses=IP_ADDRESS \
        --description=DESCRIPTION \
        --region=REGION
    

Replace the following:

  * `NAME`: a name for the group of addresses you are creating.
  * `PDP_NAME`: the public delegated prefix or sub-prefix that contains the IP addresses you are creating. Must be a v2 regional public delegated prefix with `enableEnhancedIpAllocation` set to true.
  * `IP_ADDRESS`: an optional IP address from the parent prefix's range that specifies which address to create. Omit this flag to let Google Cloud automatically select the address to create.
  * `DESCRIPTION`: an optional description.
  * `REGION`: the region of the IP addresses to create, which must match the region of the public delegated prefix.



## What's next

  * [Manage BGP announcement (v2)](https://docs.cloud.google.com/vpc/docs/manage-bgp-announcement)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
