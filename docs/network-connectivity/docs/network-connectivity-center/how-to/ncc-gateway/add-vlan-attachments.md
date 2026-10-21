---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/add-vlan-attachments/
title: Add VLAN attachments to NCC Gateway \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:19:05.574883+00:00
---

# Add VLAN attachments to NCC Gateway  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/add-vlan-attachments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Add VLAN attachments to NCC Gateway Stay organized with collections  Save and categorize content based on your preferences. 

To complete your NCC Gateway configuration in a greenfield environment, your Google Cloud and on-premises or other cloud environments must be connected through [hybrid connectivity](https://cloud.google.com/hybrid-connectivity) by using Cloud Interconnect VLAN attachments with Cloud Router.

This page describes how to create a Cloud Router and a VLAN attachment and connect them to NCC Gateway.

## Create a Cloud Router

Before you create and connect the Cloud Router, keep the following considerations in mind:

  * The Cloud Router must be associated with an NCC Gateway in the same region.
  * At the most, one service, such as a [Secure Access Connect attachment](https://docs.cloud.google.com/secure-access-connect/docs/overview), can be attached to an NCC Gateway at a time.
  * Only the VLAN attachments whose BGP sessions are managed by the Cloud Router that's associated with the NCC Gateway are part of the NCC Gateway spoke.



For detailed information about Cloud Router, see [Cloud Router overview](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview).

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ the following IAM roles.

**Permissions**

  * `compute.routers.create` to configure the Cloud Router
  * `networkconnectivity.spokes.use` on the NCC Gateway resource



To create a Cloud Router, do the following:

###  Console 

To create a Cloud Router and associate it with an NCC Gateway spoke, you must first [Create an NCC Gateway spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-spoke).

  1. In the Google Cloud console, go to the **Network Connectivity Center** page.

[Go to Network Connectivity Center](https://console.cloud.google.com/hybrid/hubs/list)

  2. In the project menu, select a project in which you want to create the spoke.

  3. Click the **Spokes** tab.

  4. Click the spoke that you want to associate with the Cloud Router.

**Note:** When creating the router, by default, the NCC Gateway spoke gets selected if there is only one spoke associated with the hub. If there are multiple spokes, you must select the spoke with which you want to associate the Cloud Router.
  5. On the **Spoke details** page, click **Add Cloud Router**. This step automatically preselects **Associated with** to **NCC Gateway**.

  6. Specify the Cloud Router's details:

     * **Name** : The name of the Cloud Router. This name is displayed in the Google Cloud console and is used by Google Cloud CLI to reference the Cloud Router—for example, `my-router`.

     * **Description** : Optional. A description of the Cloud Router.

     * **Region** : The region where you want to locate the Cloud Router—for example, `asia-east1`.

     * **Google ASN** : Any [private ASN](https://tools.ietf.org/html/rfc6996) (`64512`-`65534`, `4200000000`-`4294967294`) that you aren't already using in the on-premises network.

Cloud Router requires that you use a private ASN, but your on-premises ASN can be public or private.

**Note:** If you are using Cloud Router with Partner Interconnect, you must specify the Google-owned public ASN `16550` instead.
     * **BGP peer keepalive interval** : The interval between two successive BGP keepalive messages that are sent to the peer router. This value must be an integer between 20 and 60 that specifies the number of seconds for the interval. The default is 20 seconds. For more information, see [Manage BGP timers](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers).

     * **BGP identifier** : Optional. The BGP identifier, sometimes called a _router ID_ , that uniquely identifies a Cloud Router in a network. If omitted, Cloud Routers with IPv4 BGP sessions use one of the IPv4 BGP addresses as the BGP identifier, and adding the first IPv6 interface to this Cloud Router populates the field automatically.

For more information, see [Configure the BGP identifier range for a Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-bgp-identifier).

  7. Optional: To specify custom advertised routes, go to the **Advertised routes** section. For more information, see [Advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes).

     1. To specify custom **Routes** , select **Create custom routes**.

     2. Choose whether to advertise the subnets visible to the Cloud Router. Enabling this option mimics the Cloud Router's default behavior.

     3. To add an advertised route, select **Add a custom route** , and then configure it.

  8. To save your settings and create a Cloud Router, click **Create**.

Your new Cloud Router appears on the Cloud Router page under **Routers associated with NCC Gateway**.




###  gcloud 

Use the [`gcloud compute routers create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/create). Cloud Routers in gateway spokes must use the custom advertisement mode. In this example, the router-level advertisement mode is set to `CUSTOM`.

For information about the effect of the router-level advertisement mode on individual BGP session advertisements, see [Effective advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#effective-adv-prefixes).
    
    
    gcloud compute routers create ROUTER_NAME \
        --project=PROJECT_ID \
        --ncc-gateway=NCC_GATEWAY_URI \
        --region=REGION\
        --asn=ASN_NUMBER \
        --advertisement-mode=CUSTOM \
        --set-advertisement-ranges=CUSTOM_ADVERTISED_RANGES \
        [--bgp-identifier-range=ROUTER_IDENTIFIER_RANGE] \
        [--keepalive-interval=KEEPALIVE_TIMER] \
    

Replace the following:

  * `ROUTER_NAME`: the name of the Cloud Router

  * `PROJECT_ID`: the project ID for the project that contains the Cloud Router

  * `NCC_GATEWAY_URI`: the full URI of the NCC Gateway associated with the router. The format of the URI follows this pattern: `https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/spokes/GATEWAY_SPOKE_NAME`

  * `REGION`: the region that contains the Cloud Router

  * `ASN_NUMBER`: any [private ASN](https://tools.ietf.org/html/rfc6996) (`64512`-`65534`, `4200000000`-`4294967294`) that you aren't already using in the on-premises network

Cloud Router requires you to use a private ASN, but your on-premises ASN can be public or private. **Note:** If you are using Cloud Router with Partner Interconnect, you must specify ASN `16550`.

  * `CUSTOM_ADVERTISED_RANGES`: the list of custom IP address ranges in CIDR format or individual IP addresses to be included in the router-level advertisements

Individual IPv4 addresses are interpreted as a CIDR with a `/32` subnet mask, and individual IPv6 addresses are interpreted as a CIDR with a `/128` subnet mask. For information about the maximum number of custom route advertisements, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas#ncc-limits).

  * `ROUTER_IDENTIFIER_RANGE`: an optional IPv4 address range that serves as a unique identifier for the Cloud Router

For more information, see [Configure the BGP identifier range for a Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-bgp-identifier).

  * `KEEPALIVE_TIMER`: an optional time, in seconds, that defines the BGP keepalive timer.

Valid values are between `20` and `60`, inclusive. If you omit the `--keepalive-interval` flag, Cloud Router uses a 20 second BGP keepalive timer. For more information, see [Keepalive timer](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers#keepalive_timer).




###  API 

Use the [`compute.router.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/insert) with NCC Gateway specified in the payload. To specify router-level custom route advertisements, set the `bgp.advertiseMode` flag to `CUSTOM`. For information about the effect of the router-level advertisement mode on individual BGP session advertisements, see [Effective advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#effective-adv-prefixes).
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers
    {
    "name": "ROUTER_NAME",
    "ncc_gateway": "NCC_GATEWAY_URI",
    "bgp": {
      "asn": "ASN_NUMBER",
      "advertiseMode": CUSTOM,
      "advertisedIpRanges": [
        {
            "range": CUSTOM_ADVERTISED_RANGE,
            "description": CUSTOM_ADVERTISED_RANGE_DESCRIPTION
        }, ...
      ],
      "identifierRange": ROUTER_IDENTIFIER_RANGE,
      "keepaliveInterval": KEEPALIVE_TIMER
    }
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID for the project that contains the Cloud Router
  * `REGION`: the region that contains the Cloud Router
  * `ROUTER_NAME`: the name of the Cloud Router
  * `NCC_GATEWAY_URI`: the full URI of the NCC Gateway associated with the router. The format of the URI follows this pattern: `https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/spokes/GATEWAY_SPOKE_NAME`
  * `ASN_NUMBER`: any [private ASN](https://tools.ietf.org/html/rfc6996) (`64512`-`65534`, `4200000000`-`4294967294`) that you aren't already using in the on-premises network

Cloud Router requires you to use a private ASN, but your on-premises ASN can be public or private. **Note:** If you are using Cloud Router with Partner Interconnect, you must specify ASN `16550`.

  * `CUSTOM_ADVERTISED_RANGE` and `CUSTOM_ADVERTISED_RANGE_DESCRIPTION`: keys in a dictionary that specify a router-level custom route advertisement

The `bgp.advertisedIpRanges` list contains each custom route advertisement dictionary. Specifying `bgp.advertisedIpRanges` requires `bgp.advertiseMode: CUSTOM`. Each `CUSTOM_ADVERTISED_RANGE` is an IP address range in CIDR format or an individual IP address. Individual IPv4 addresses are interpreted as a CIDR with a `/32` subnet mask, and individual IPv6 addresses are interpreted as a CIDR with a `/128` subnet mask. For information about the maximum number of custom route advertisements, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas#ncc-limits). Each `CUSTOM_ADVERTISED_RANGE_DESCRIPTION` is a string to describe the advertisement.

  * `ROUTER_IDENTIFIER_RANGE`: defines an IPv4 address range that serves as a unique identifier for the Cloud Router

For more information, see [Configure the BGP identifier range for a Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-bgp-identifier).

  * `KEEPALIVE_TIMER`: an optional time, in seconds, that defines the BGP keepalive timer

Valid values are between `20` and `60`, inclusive. If you omit `bgp.keepaliveInterval`, Cloud Router uses a 20 second BGP keepalive timer. For more information, see [Keepalive timer](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers#keepalive_timer).




## Create VLAN attachments

VLAN attachments for Dedicated Interconnect or Partner Interconnect provide the connectivity path between the NCC Gateway and an on-premises network.

The VLAN attachment traffic goes through the NCC Gateway before it reaches the partner service and the hub.

For detailed information about how to create VLAN attachments and set up interface and BGP peering, see [Create VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/tutorials/dedicated-creating-9999-availability#create_vlan_attachments).

[ Previous arrow_back  Connect the Secure Access Connect attachment  ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/connect-sac)

[ Next Create and manage NCC Gateway advertised routes  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/create-manage-advertised-routes)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
