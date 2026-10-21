---
url: https://docs.cloud.google.com/vpc/docs/create-pdp/
title: Create public delegated prefixes \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:11.019127+00:00
---

# Create public delegated prefixes  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/create-pdp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create public delegated prefixes

You can create [public delegated prefixes](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#pdp) before the public advertised prefix creation is complete.

The public advertised prefix type determines the configuration of the public delegated prefix. For more information, see [Bring your own IP configurations](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#comparison).

We recommend that you use v2 public advertised prefixes to create regional public delegated prefixes. You must use v2 public advertised prefixes to import IPv6 prefixes to Google Cloud.

## Before you begin

  * [Create a public advertised prefix](https://docs.cloud.google.com/vpc/docs/create-pap).
  * If you're creating a global public delegated prefix, the parent public advertised prefix must meet these requirements: 
    * The public advertised prefix is used for global public delegated prefixes only.
    * The public advertised prefix is in a project that has been added to the allowlist for global prefixes. For more information, see [Global public delegated prefixes](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#global-pdp).
  * If you're creating a top-level public delegated prefix for Standard Tier IP addresses ([Preview](https://cloud.google.com/products#product-launch-stages)), and if you followed the [recommended approach of creating a ROA for the parent public advertised prefix](https://docs.cloud.google.com/vpc/docs/create-pap#standard-roa), make sure you have a valid ROA for the public delegated prefix.




### Roles

To get the permissions that you need to complete the tasks in this guide, ask your administrator to grant you the [Compute Public IP Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.publicIpAdmin) (`roles/compute.publicIpAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create public delegated prefixes

A public delegated prefix name can't be changed without deleting and recreating the resource. For this reason, we recommend that you create generic names that won't need to change—for example, `pdp-203-0-113-0-25`, where `pdp` denotes the resource type and `203-0-113-0-25` denotes the specific prefix and prefix length. 

To create a global public delegated prefix, you must use a public advertised prefix that is used for global public delegated prefixes only, and is in a project that has been added to the allowlist for global prefixes. For more information, see [Global public delegated prefixes](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#global-pdp).

The [public delegated prefixes per public advertised prefix limit](https://docs.cloud.google.com/vpc/docs/quota#ip_address_limits) restricts the number of public delegated prefixes that you can create from a single public advertised prefix. To avoid reaching this limit, create a small number of large top-level public delegated prefixes, and then sub-delegate those prefixes into smaller sub-prefixes.

###  Console 

  1. In the Google Cloud console, go to **Bring your own IP**.



[Go to Bring your own IP](https://console.cloud.google.com/networking/byoip)

  1. Click the public advertised prefix that you want to delegate.
  2. Click **Create PDP**.
  3. For **Name** , enter a name for the public delegated prefix.
  4. For **Description** , enter an optional description for the public delegated prefix.
  5. If you're creating a public delegated prefix for an IPv4 address range, do the following: 
     1. Select a prefix length from the **Prefix length** list.
     2. Select a range of IP addresses from the **IP addresses** list.
     3. Select a **Scope** for the public delegated prefix.
     4. If you selected **Regional** for the scope, select a **Region**.
  6. If you're creating a public delegated prefix for an IPv6 address range, do the following: 
     1. Select a prefix length from the **IPv6 prefix length** list.
     2. Enter an IPv6 address range in **IPv6 range**.
     3. Select a region from the **Region** list.
  7. Select a **Project** for the public delegated prefix.
  8. Click **Create**.



###  gcloud 

Use the [`public-delegated-prefixes create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/create).

  * To create an IPv4 PDP, use the following command:
        
        gcloud compute public-delegated-prefixes create PDP_NAME \
            --public-advertised-prefix=PAP_NAME \
            --range=PDP_IP_RANGE \
            --region=PDP_REGION
        

Replace the following:

    * `PDP_NAME`: the name to use for the public delegated prefix that you are creating.

    * `PAP_NAME`: the name of the public advertised prefix to use to create the public delegated prefix.

    * `PDP_IP_RANGE`: the IPv4 or IPv6 address range to use to create the public delegated prefix.

    * `PDP_DESCRIPTION`: an optional description for the public delegated prefix.

    * `PDP_REGION`: the region where you want to use the public delegated prefix addresses. If you want a global public delegated prefix instead, replace `--region=PDP_REGION` with `--global`.

  * To create an IPv6 PDP, use the following commamd:
        
        gcloud compute public-delegated-prefixes create PDP_NAME \
            --public-advertised-prefix=PAP_NAME \
            --range=PDP_IP_RANGE \
            --region=PDP_REGION \
            --mode=DELEGATION
        




## Check the status of a public delegated prefix

You can check the status of a public delegated prefix. The available statuses for both v2 and v1 public delegated prefixes are described in the following table.

Status | Description | v2 | v1  
---|---|---|---  
`INITIALIZING` | The public delegated prefix is being initialized and addresses can't be created yet. |  |   
`READY_TO_ANNOUNCE` | The public delegated prefix is withdrawn, and is ready to be announced. |  [Manage announcement](https://docs.cloud.google.com/vpc/docs/manage-bgp-announcement) |   
`ANNOUNCED` | The public delegated prefix is active and is announced. |  |   
`ANNOUNCED_TO_GOOGLE` | The prefix is announced within Google Cloud's network. |  |   
`ANNOUNCED_TO_INTERNET` | The prefix is announced to the internet and within Google Cloud's network. |  |   
`DELETING` | The public delegated prefix is being deprovisioned. |  |   
  
###  Console 

  1. In the Google Cloud console, go to **Bring your own IP**.

[Go to Bring your own IP](https://console.cloud.google.com/networking/byoip)

  2. The **Status** column displays the status for all public delegated prefixes.




###  gcloud 

To describe the public delegated prefix and get its status, use the [`public-delegated-prefixes describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/public-delegated-prefixes/describe).
    
    
    gcloud compute public-delegated-prefixes describe PDP_NAME \
        --region=PDP_REGION \
        --format='value(status)'
    

Replace the following:

  * `PDP_NAME`: the public delegated prefix or sub-prefix that you want to get information for.

  * `PDP_REGION`: the region of the public delegated prefix or sub-prefix.

  * `PDP_REGION`: the region where you want to use the public delegated prefix addresses. If you want a global public delegated prefix instead, replace `--region=PDP_REGION` with `--global`.




## Check enhanced IP address allocation

To check if an IPv4 public delegated prefix supports [enhanced IP address allocation](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#enhanced-allocation), do the following.

###  Console 

  1. In the Google Cloud console, go to **Bring your own IP**.

[Go to Bring your own IP](https://console.cloud.google.com/networking/byoip)

  2. The **Enhanced IP allocation** column displays whether each IPv4 public delegated prefix uses enhanced IP address allocation.




###  gcloud 

Use the following command.
    
    
    gcloud compute public-delegated prefixes describe PDP_NAME \
        --region=PDP_REGION \
        --format='value(enableEnhancedIpv4Allocation)'
    

Replace the following:

  * `PDP_NAME`: the name of the public delegated prefix to describe.
  * `PDP_REGION`: the region of the public delegated prefix.



## What's next

  * [Create IPv4 sub-prefixes and IP addresses](https://docs.cloud.google.com/vpc/docs/create-sub-prefixes-ip-addresses)
  * [Create IPv6 sub-prefixes](https://docs.cloud.google.com/vpc/docs/create-ipv6-sub-prefixes)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
