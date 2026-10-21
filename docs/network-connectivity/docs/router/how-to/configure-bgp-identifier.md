---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-bgp-identifier/
title: Configure the BGP identifier range for a Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:23:18.813289+00:00
---

# Configure the BGP identifier range for a Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-bgp-identifier/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure the BGP identifier range for a Cloud Router

Each Cloud Router has a BGP identifier, also known as a _router ID_. The BGP identifier is unique to each Cloud Router in your Virtual Private Cloud (VPC) network as required by [RFC 6286](https://datatracker.ietf.org/doc/html/rfc6286). A BGP identifier is a 4-octet unsigned integer, represented as a valid IPv4 address.

You can assign an explicit BGP identifier _range_ to your Cloud Router. If you do, your Cloud Router is assigned a stable BGP identifier from the assigned range.

An explicit BGP identifier range is required for IPv6 BGP. If you add an IPv6 interface to a Cloud Router that doesn't already have a BGP identifier range assigned, a random range from the IPv4 link-local address space is assigned to it.

A Cloud Router without an explicit BGP identifier range is assigned a BGP identifier corresponding to the lexicographically-last IPv4 address among its IPv4 interfaces.

## BGP identifier changes and BGP session restarts

Unless you've configured an explicit BGP identifier range, Cloud Router might change the automatically generated router ID in the following circumstances:

  * You add a BGP session
  * You remove a BGP session
  * During periodic maintenance



## Before you begin

###  gcloud 

If you want to use the command-line examples in this guide, do the following:

  1. Install or update to the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute).
  2. Set a [default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



###  API 

If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/compute/docs/api/prereqs).

## Assign a BGP identifier range to Cloud Router

This section describes how to assign an explicit BGP identifier range to a Cloud Router.

###  Console 

  1. In the Google Cloud console, go to the **Create a Cloud Router** page.

[Go to Create a Cloud Router](https://console.cloud.google.com/hybrid/routers/add)

  2. Specify the Cloud Router's details:

     * **Name** : The name of the Cloud Router. This name is displayed in the Google Cloud console and is used by the Google Cloud CLI to reference the Cloud Router—for example, `my-router`. 
     * **Description** : Optional. A description of the Cloud Router. 
     * **Network** : The VPC network that contains the instances that you want to reach—for example, `my-network`. 
     * **Region** : The region where you want to locate the Cloud Router—for example, `asia-east1`. 
     * **Google ASN** : Any [private ASN](https://tools.ietf.org/html/rfc6996) (`64512`-`65534`, `4200000000`-`4294967294`) that you aren't already using in the on-premises network. Cloud Router requires that you use a private ASN, but your on-premises ASN can be public or private. 

**Note:** If you are using Cloud Router with Partner Interconnect, you must specify the Google-owned public ASN `16550` instead. 

     * **BGP peer keepalive interval** : The interval between two successive BGP keepalive messages that are sent to the peer router. This value must be an integer between 20 and 60 that specifies the number of seconds for the interval. The default is 20 seconds. For more information, see [Manage BGP timers](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers). 
     * **BGP identifier** : Optional. The BGP identifier, sometimes called a _router ID_ , that uniquely identifies a Cloud Router in a network. If omitted, Cloud Routers with IPv4 BGP sessions use one of the IPv4 BGP addresses as the BGP identifier, and adding the first IPv6 interface to this Cloud Router populates the field automatically. 

For more information, see [Configure the BGP identifier range for a Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-bgp-identifier). 

  3. Optional: To specify custom advertised routes, go to the **Advertised routes** section. For more information, see [Advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes). 
     1. To specify custom **Routes** , select **Create custom routes**. 
     2. Choose whether to advertise the subnets visible to the Cloud Router. Enabling this option mimics the Cloud Router's default behavior. 
     3. To add an advertised route, select **Add a custom route** , and then configure it. 
  4. To save your settings and create a Cloud Router, click **Create**. Your new Cloud Router appears on the Cloud Router listing page. To view its details and to configure a BGP session, select it. 



###  gcloud 

To assign an explicit BGP identifier range when you create the Cloud Router, use the `--bgp-identifier-range` flag.
    
    
    gcloud compute routers create ROUTER_NAME \
        --bgp-identifier-range=BGP_IDENTIFIER_RANGE
    

Replace `BGP_IDENTIFIER_RANGE` with a link-local IPv4 range from `169.254.0.0/16` with a subnet mask prefix length of at most `/30`. The IPv4 address range must not overlap either of the following:

  * The IPv4 address range used by another BGP session on this Cloud Router.

  * Any custom BGP identifier range used by another Cloud Router in the same VPC network and region.




### API

Use the [`routers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/insert):
    
    
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
        {
          "bgp": {
             "asn": "ASN_NUMBER",
             "keepaliveInterval": KEEPALIVE_INTERVAL,
             "identifierRange": BGP_IDENTIFIER_RANGE
          },
          "name": "ROUTER_NAME",
          "network": "NETWORK"
         }
    

Replace `BGP_IDENTIFIER_RANGE` with a link-local IPv4 range from `169.254.0.0/16` with a subnet mask prefix length of at most `/30`. The range must not overlap with any existing IPv4 Cloud Router interface or a BGP identifier range of a Cloud Router in the same region.

## Modify the BGP identifier range

This section describes how to modify an existing explicit BGP identifier range on a Cloud Router.

**Caution:** Changing the explicit BGP identifier range of Cloud Router causes all existing BGP sessions to restart for all BGP peers on the Cloud Router.

### gcloud

To change the explicit BGP identifier range, run the following command.
    
    
    gcloud compute routers update ROUTER_NAME \
        --bgp-identifier-range=BGP_IDENTIFIER_RANGE
    

Replace `BGP_IDENTIFIER_RANGE` with a link-local IPv4 range from `169.254.0.0/16` with a subnet mask prefix length of at most `/30`.

The IPv4 address range must not overlap either of the following:

  * The IPv4 address range used by another BGP session on this Cloud Router.

  * Any custom BGP identifier range used by another Cloud Router in the same VPC network and region.




### API

Use the [`routers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/patch) to update the `bgp.identifierRange` field:
    
    
        PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers/ROUTER_NAME
        {
          "bgp": {
            "identifierRange": BGP_IDENTIFIER_RANGE
         }
       }
    

Replace `BGP_IDENTIFIER_RANGE` with a link-local IPv4 range from `169.254.0.0/16` with a subnet mask prefix length of at most `/30`. The IPv4 address range must not overlap either of the following:

  * The IPv4 address range used by another BGP session on this Cloud Router.

  * Any custom BGP identifier range used by another Cloud Router in the same VPC network and region.




## What's next

  * [View Cloud Router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
