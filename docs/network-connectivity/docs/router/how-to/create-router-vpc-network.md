---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-network/
title: Create a Cloud Router to connect a VPC network to a peer network \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:26:12.980648+00:00
---

# Create a Cloud Router to connect a VPC network to a peer network  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a Cloud Router to connect a VPC network to a peer network

This page outlines the Cloud Router configuration process necessary to exchange routes between a Virtual Private Cloud (VPC) network or NCC Gateway and a peer network. The peer network can be an on-premises network, a network hosted by another cloud provider such as AWS or Azure, or even another VPC network in Google Cloud.

The Cloud Router configuration process consists of these three high-level tasks:

  1. Create a Cloud Router.
  2. Set up a network connectivity product in Google Cloud.
  3. Establish Border Gateway Protocol (BGP) sessions with a router on the peer network.



## Before you begin

###  gcloud 

If you want to use the command-line examples in this guide, do the following:

  1. Install or update to the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute).
  2. Set a [default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



###  API 

If you want to use the API examples in this guide, set up [API access](https://docs.cloud.google.com/compute/docs/api/prereqs).

## Autonomous system number (ASN)

When you create a Cloud Router, you [choose the Google-side ASN](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/create#--asn) for all BGP sessions used by the Cloud Router. Directions for each product and how they use ASN are listed in [Google Cloud products that use Cloud Router](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview#cloud-products-that-use-cloud-router).

**Note:** Cloud NAT doesn't use ASN information. Cloud NAT gateways can be connected to Cloud Routers that have any ASN or that have no ASN specified.

## Create a Cloud Router

To create a Cloud Router, follow these steps.

If you want to create a Cloud Router that's associated with an NCC Gateway spoke, you must use either the Google Cloud CLI or the Cloud Router API instructions in this section. For more information, see [Add hybrid connections to NCC Gateway](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/add-vlan-attachments). 

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

The [`gcloud compute routers create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/routers/create) creates a new Cloud Router. A Cloud Router is associated either with a VPC network or an NCC Gateway spoke. Once created, you can't change the region, the associated VPC network, or the associated NCC Gateway spoke.

The `--set-advertisement-groups=ALL_SUBNETS` flag is valid only when the `--advertisement-mode=CUSTOM` flag is set. When this flag and value are specified, the router-level advertisements include local subnet ranges according to the dynamic routing mode of the VPC network.

For more information, see [Subnet range advertisement](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#am-subnets).

Include the `--encrypted-interconnect-router` flag only if the Cloud Router manages BGP sessions for [HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect). 

  * To create a Cloud Router that's associated with a region of a VPC network, use the following command:
        
        gcloud compute routers create ROUTER_NAME \
            --project=PROJECT_ID \
            --network=NETWORK \
            --region=REGION\
            --asn=ASN_NUMBER \
            [--advertisement-mode=ADVERTISEMENT_MODE] \
            [--set-advertisement-groups=ALL_SUBNETS] \
            [--set-advertisement-ranges=CUSTOM_ADVERTISED_RANGES] \
            [--bgp-identifier-range=ROUTER_IDENTIFIER_RANGE] \
            [--keepalive-interval=KEEPALIVE_TIMER] \
            [--encrypted-interconnect-router]
        

Replace the following:

    * `ROUTER_NAME`: the name of the Cloud Router

    * `PROJECT_ID`: the project ID for the project that contains the Cloud Router

    * `NETWORK`: the VPC network that contains the Cloud Router

    * `REGION`: the region that contains the Cloud Router

    * `ASN_NUMBER`: any [private ASN](https://tools.ietf.org/html/rfc6996) (`64512`-`65534`, `4200000000`-`4294967294`) that you aren't already using in the on-premises network

Cloud Router requires you to use a private ASN, but your on-premises ASN can be public or private. **Note:** If you are using Cloud Router with Partner Interconnect, you must specify ASN `16550`.

    * `ADVERTISEMENT_MODE`: specifies the router-level advertisement mode

Valid values are `CUSTOM` or `DEFAULT`. If you omit the `--advertisement-mode` flag, Google Cloud uses the `DEFAULT` advertisement mode at the router level. For information about the meaning of the router-level advertisement mode and its effect on individual BGP session advertisements, see [Advertisement modes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#overview-am) and [Effective advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#effective-adv-prefixes).

    * `CUSTOM_ADVERTISED_RANGES`: valid only when `--advertisement-mode=CUSTOM`, an optional list of custom IP address ranges in CIDR format or individual IP addresses to be included in the router-level advertisements

Individual IPv4 addresses are interpreted as a CIDR with a `/32` subnet mask, and individual IPv6 addresses are interpreted as a CIDR with a `/128` subnet mask. For information about the maximum number of custom route advertisements, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).

    * `ROUTER_IDENTIFIER_RANGE`: an optional IPv4 address range that serves as a unique identifier for the Cloud Router

For more information, see [Configure the BGP identifier range](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-bgp-identifier).

    * `KEEPALIVE_TIMER`: an optional time, in seconds, that defines the BGP keepalive timer

Valid values are between `20` and `60`, inclusive. If you omit the `--keepalive-interval` flag, Cloud Router uses a 20 second BGP keepalive timer. For more information, see [Keepalive timer](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers#keepalive_timer). 

  * To create a Cloud Router that's associated with an NCC Gateway spoke, use the following command.

Use the `--advertisement-mode=CUSTOM` flag to set the router-level advertisement mode to `CUSTOM` so that you can specify router-level custom route advertisements.

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

    * `--advertisement-mode=CUSTOM`: sets the router-level advertisement mode to `CUSTOM` so that you can specify router-level custom route advertisements.

For information about the effect of the router-level advertisement mode on individual BGP session advertisements, see [Effective advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#effective-adv-prefixes).

    * `CUSTOM_ADVERTISED_RANGES`: the list of custom IP address ranges in CIDR format or individual IP addresses to be included in the router-level advertisements

Individual IPv4 addresses are interpreted as a CIDR with a `/32` subnet mask, and individual IPv6 addresses are interpreted as a CIDR with a `/128` subnet mask. For information about the maximum number of custom route advertisements, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits).

    * `ROUTER_IDENTIFIER_RANGE`: an optional IPv4 address range that serves as a unique identifier for the Cloud Router

For more information, see [Configure the BGP identifier range](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-bgp-identifier).

    * `KEEPALIVE_TIMER`: an optional time, in seconds, that defines the BGP keepalive timer

Valid values are between `20` and `60`, inclusive. If you omit the `--keepalive-interval` flag, Cloud Router uses a 20 second BGP keepalive timer. For more information, see [Keepalive timer](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers#keepalive_timer). 




###  Terraform 

Use the [Google Cloud Terraform module for Cloud Router](https://github.com/terraform-google-modules/terraform-google-cloud-router).
    
    
    module "cloud_router" {
      source = "../.."
    
      name   = "my-router"
      region = "us-central1"
    
      bgp = {
        # The ASN (16550, 64512 - 65534, 4200000000 - 4294967294) can be any private ASN
        # not already used as a peer ASN in the same region and network or 16550 for Partner Interconnect.
        asn = "65001"
      }
    
      project_id = var.project_id
      network    = module.vpc.network_name
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  API 

The [`routers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/insert) creates a new Cloud Router. A Cloud Router is associated either with a VPC network or an NCC Gateway spoke. Once created, you can't change the region, the associated VPC network, or the associated NCC Gateway spoke.

The `"advertisedGroups": [ALL_SUBNETS]` flag is valid only when `bgp.advertiseMode: CUSTOM`, when `bgp.advertisedGroups: [ALL_SUBNETS]`, the router-level advertisements include local subnet ranges according to the dynamic routing mode of the VPC network. For more information, see [Subnet range advertisement](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#am-subnets).

The `encryptedInterconnectRouter` flag is a boolean parameter to indicate whether the Cloud Router manages BGP sessions for [HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect). 

  * To create a Cloud Router that's associated with a region of a VPC network, use the following request:
        
        POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/routers
             {
               "name": "ROUTER_NAME",
               "network": "NETWORK",
               "encryptedInterconnectRouter": True|False,
               "bgp": {
                 "asn": "ASN_NUMBER",
                 "advertiseMode": "ADVERTISEMENT_MODE",
                 "advertisedGroups": [ALL_SUBNETS],
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

    * `ROUTER_NAME`: the name of the Cloud Router

    * `PROJECT_ID`: the project ID for the project that contains the Cloud Router

    * `NETWORK`: the VPC network that contains the Cloud Router

    * `REGION`: the region that contains the Cloud Router

    * `ASN_NUMBER`: any [private ASN](https://tools.ietf.org/html/rfc6996) (`64512`-`65534`, `4200000000`-`4294967294`) that you aren't already using in the on-premises network

Cloud Router requires you to use a private ASN, but your on-premises ASN can be public or private. **Note:** If you are using Cloud Router with Partner Interconnect, you must specify ASN `16550`.

    * `ADVERTISEMENT_MODE`: specifies the router-level advertisement mode

Valid values are `CUSTOM` or `DEFAULT`. If you omit `bgp.advertiseMode`, Google Cloud uses the `DEFAULT` advertisement mode at the router level. For information about the meaning of the router-level advertisement mode and its effect on individual BGP session advertisements, see [Advertisement modes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#overview-am) and [Effective advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#effective-adv-prefixes).

    * `CUSTOM_ADVERTISED_RANGE` and `CUSTOM_ADVERTISED_RANGE_DESCRIPTION`: keys in a dictionary that specify a router-level custom route advertisement

`bgp.advertisedIpRanges` is the list containing each custom route advertisement dictionary. Specifying `bgp.advertisedIpRanges` requires `bgp.advertiseMode: CUSTOM`. Each `CUSTOM_ADVERTISED_RANGE` is an IP address range in CIDR format or an individual IP address. Individual IPv4 addresses are interpreted as a CIDR with a `/32` subnet mask, and individual IPv6 addresses are interpreted as a CIDR with a `/128` subnet mask. For information about the maximum number of custom route advertisements, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits). Each `CUSTOM_ADVERTISED_RANGE_DESCRIPTION` is a string to describe the advertisement.

    * `ROUTER_IDENTIFIER_RANGE`: defines an IPv4 address range that serves as a unique identifier for the Cloud Router

For more information, see [Configure the BGP identifier range](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-bgp-identifier).

    * `KEEPALIVE_TIMER`: an optional time, in seconds, that defines the BGP keepalive timer

Valid values are between `20` and `60`, inclusive. If you omit `bgp.keepaliveInterval`, Cloud Router uses a 20 second BGP keepalive timer. For more information, see [Keepalive timer](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers#keepalive_timer). 

    * `encryptedInterconnectRouter`: a boolean parameter to indicate whether the Cloud Router manages BGP sessions for [HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect)

  * To create a Cloud Router that's associated with an NCC Gateway spoke, use the following request.

The `bgp.advertiseMode: CUSTOM` flag sets the router-level advertisement mode to `CUSTOM` so that you can specify router-level custom route advertisements. For information about the effect of the router-level advertisement mode on individual BGP session advertisements, see [Effective advertisements](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#effective-adv-prefixes).
        
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

    * `ROUTER_NAME`: the name of the Cloud Router

    * `PROJECT_ID`: the project ID for the project that contains the Cloud Router

    * `NCC_GATEWAY_URI`: the full URI of the NCC Gateway associated with the router. The format of the URI follows this pattern: `https://networkconnectivity.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/spokes/GATEWAY_SPOKE_NAME`

    * `REGION`: the region that contains the Cloud Router

    * `ASN_NUMBER`: any [private ASN](https://tools.ietf.org/html/rfc6996) (`64512`-`65534`, `4200000000`-`4294967294`) that you aren't already using in the on-premises network

Cloud Router requires you to use a private ASN, but your on-premises ASN can be public or private. **Note:** If you are using Cloud Router with Partner Interconnect, you must specify ASN `16550`.

    * `CUSTOM_ADVERTISED_RANGE` and `CUSTOM_ADVERTISED_RANGE_DESCRIPTION`: keys in a dictionary that specify a router-level custom route advertisement

`bgp.advertisedIpRanges` is the list containing each custom route advertisement dictionary. Specifying `bgp.advertisedIpRanges` requires `bgp.advertiseMode: CUSTOM`. Each `CUSTOM_ADVERTISED_RANGE` is an IP address range in CIDR format or an individual IP address. Individual IPv4 addresses are interpreted as a CIDR with a `/32` subnet mask, and individual IPv6 addresses are interpreted as a CIDR with a `/128` subnet mask. For information about the maximum number of custom route advertisements, see [Limits](https://docs.cloud.google.com/network-connectivity/docs/router/quotas#limits). Each `CUSTOM_ADVERTISED_RANGE_DESCRIPTION` is a string to describe the advertisement.

    * `ROUTER_IDENTIFIER_RANGE`: defines an IPv4 address range that serves as a unique identifier for the Cloud Router

For more information, see [Configure the BGP identifier range](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configure-bgp-identifier).

    * `KEEPALIVE_TIMER`: an optional time, in seconds, that defines the BGP keepalive timer

Valid values are between `20` and `60`, inclusive. If you omit `bgp.keepaliveInterval`, Cloud Router uses a 20 second BGP keepalive timer. For more information, see [keepalive timer](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-bgp-timers#keepalive_timer). 




## Set up the network connectivity product

A Cloud Router that's associated with a region of a VPC network can manage BGP sessions for the following connectivity products:

  * Cloud Interconnect VLAN attachments for [Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/dedicated-overview) or [Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview). You can optionally associate a VLAN attachment with a NCC hybrid spoke by [creating a VLAN attachment spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vlan-spoke).
  * [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview), specifically HA VPN. You can optionally associate a HA VPN tunnel with a NCC hybrid spoke by [creating a VPN spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vpn-spoke).
  * [Router appliances](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview), which must always be associated a NCC hybrid spoke by [creating a Router appliance spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-ra-spoke).



A Cloud Router that's associated with an NCC Gateway spoke can manage BGP sessions for VLAN attachments associated with the NCC Gateway spoke. 

### Cloud Interconnect

To connect a VPC network to an on-premises network by using Cloud Interconnect and Cloud Router, you must first provision a Cloud Interconnect connection.

  * For Dedicated Interconnect, see [Dedicated Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview).

  * For Partner Interconnect, see [Partner Interconnect provisioning overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/provisioning-overview).




You configure Cloud Router and its BGP sessions when you create the VLAN attachments for your Cloud Interconnect connection. See [Create VLAN attachments for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments) and [Create VLAN attachments for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments).

If you are deploying HA VPN over Cloud Interconnect, you must deploy two Cloud Routers: 

  * A special Cloud Router for Cloud Interconnect that you configure for the VLAN attachments. This Cloud Router makes sure that only traffic encrypted by the HA VPN gateways can be sent to the VLAN attachment.

  * A regular Cloud Router that you configure for HA VPN tunnels. 

### Cloud VPN




To connect a VPC network to an on-premises or multicloud network by using HA VPN and Cloud Router, see [Create an HA VPN gateway to a peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn).

To connect a VPC network to another VPC network by using HA VPN and Cloud Router, see [Create an HA VPN between Google Cloud networks ](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn2).

You configure Cloud Router and its BGP sessions when you create the HA VPN tunnels to the peer network.

**Note:** You can use Cloud Router with Classic VPN, but only to support dynamic routing for tunnels that connect to third-party VPN gateway software running on Google Cloud VM instances. All other dynamic routing functionality for Classic VPN is deprecated. For more information, see [ Classic VPN dynamic routing partial deprecation](https://docs.cloud.google.com/network-connectivity/docs/vpn/deprecations/classic-vpn-deprecation).

### Router appliances

To connect a VPC network to a peer network by using Router appliances in a NCC hybrid spoke, see [Create Router appliance instances](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/creating-router-appliances).

### NCC Gateway spokes

To configure VLAN attachments on an NCC Gateway spoke, see [Add hybrid connections to NCC Gateway](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/ncc-gateway/add-vlan-attachments). 

## Establish BGP sessions

When you set up a network connectivity product with Cloud Router, you establish Border Gateway Protocol (BGP) sessions between the Cloud Router and the router on the peer network.

You can reuse the same Cloud Router with different network connectivity products. However, each BGP session is unique to the network connectivity product (VLAN attachment, Cloud VPN tunnel, or Router appliance instance) that you configure to use with Cloud Router. Different network connectivity products cannot use the same BGP session. Sometimes, you might need to set up multiple BGP sessions for a network connectivity product to achieve sufficient redundancy. For example, you set up multiple BGP sessions when using Cloud Router with HA VPN.

**Note:** Partner Interconnect VLAN attachments have a [specific ASN requirement](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments#create_vlan_attachments) of ASN 16550. In addition, Cloud Router must use the same ASN for all its BGP sessions. Therefore, a Cloud Router that manages BGP sessions for Partner Interconnect VLAN attachments can only manage BGP sessions for other Partner Interconnect VLAN attachments. As an exception, the Cloud Router can also manage BGP sessions for Dedicated Interconnect VLAN attachments where ASN 16550 is acceptable.

To establish BGP sessions between your Cloud Router and the router on your peer network, see [Establish BGP sessions](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/configuring-bgp).

## What's next

  * To view the details of a Cloud Router, see [View Cloud Router details](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-router-details).

  * To modify custom advertised routes on your Cloud Router, see [Custom advertisement](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes#am-custom).

  * To list or delete the Cloud Routers in your project, see [List and delete Cloud Routers](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/managing-routers).

  * To troubleshoot issues when using Cloud Router, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/router/resources/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
