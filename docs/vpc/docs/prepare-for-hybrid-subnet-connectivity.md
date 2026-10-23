---
url: https://docs.cloud.google.com/vpc/docs/prepare-for-hybrid-subnet-connectivity/
title: Prepare for Hybrid Subnets connectivity \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:18:21.883685+00:00
---

# Prepare for Hybrid Subnets connectivity  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/prepare-for-hybrid-subnet-connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Prepare for Hybrid Subnets connectivity

This page describes the steps to prepare an on-premises network and a VPC network for Hybrid Subnets connectivity.

## Before you begin

  * Read [About migrating to Google Cloud with Hybrid Subnets](https://docs.cloud.google.com/vpc/docs/hybrid-subnets).
  * Identify or [create](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#creating_networks) a VPC network.
  * Identify the region for your migration. The subnet that uses hybrid subnet routing, your Cloud Router, and the Cloud VPN tunnels or Cloud Interconnect VLAN attachments that provide hybrid connectivity must all be in this region.
  * In the VPC network, identify or [create](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#add-subnets) a subnet whose primary internal IPv4 address range matches the CIDR block in your on-premises network that hosts the workloads you plan to migrate. This matched range is the shared CIDR block. Hybrid subnet routing supports both primary and secondary IPv4 address ranges, but this guide focuses on using the subnet's primary IPv4 range for the shared CIDR block.
  * To use the command-line examples in this guide, install or update to the latest version of the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).
  * [Enable the Compute Engine API](https://console.cloud.google.com/apis/library/compute.googleapis.com) in your Google Cloud project. For more information, see the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/rest/v1).
  * [Enable the Network Connectivity API](https://console.cloud.google.com/apis/library/networkconnectivity.googleapis.com) in your Google Cloud project. For more information, see the [Network Connectivity API](https://docs.cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest).



### Required roles

To get the permissions that you need to configure hybrid subnet routing, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Connect a VPC network to an on-premises network

Hybrid subnet routing requires connectivity between a VPC network and an on-premises network. The connection must be one of the following types:

  * A pair of HA VPN tunnels
  * VLAN attachments for Dedicated Interconnect
  * VLAN attachments for Partner Interconnect



The HA VPN tunnels or VLAN attachments must be in the same region as the subnet where you plan to enable hybrid subnet routing.

For help choosing a connection type, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product).

To configure hybrid connectivity, see the following:

  * [Create an HA VPN gateway to a peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/creating-ha-vpn)
  * [Create Dedicated Interconnect VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments)
  * [Create Partner Interconnect VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments)



## Configure custom route advertisement

When you configure hybrid connectivity, you create a Cloud Router. Configure the Cloud Router's BGP session to [only advertise custom routes](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/advertising-subnets#bgp-session). Don't add any routes now; in a later step, you add custom routes for each migrated VM.

## Configure firewall rules

To ensure that Google Cloud instances can communicate with all workloads that use the shared CIDR block, do the following:

  * In Google Cloud, create ingress allow firewall rules or rules in firewall policies to allow all packets from the shared CIDR block.

You can scope firewall rules to specific instances by using the target parameter of the rule. For more information, see:

    * [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls)
    * [Firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies-overview)
  * Configure firewalls in your on-premises network in a similar way.




## Configure routing for on-premises network

Configure on-premises routing by completing the steps in the following sections.

### Enable proxy ARP for the on-premises network

Enable [proxy ARP](https://en.wikipedia.org/wiki/Proxy_ARP) for your on-premises network. For more information, see [Proxy ARP and Hybrid Subnets](https://docs.cloud.google.com/vpc/docs/hybrid-subnets#proxy-arp).

For information about enabling proxy ARP, see the documentation of your proxy ARP solution.

### Advertise your shared CIDR block

Configure your on-premises network to advertise the the shared CIDR block. This IP address range must match the primary internal IPv4 address range of the subnet that uses hybrid subnet routing.

For information about configuring route advertisement, see the documentation of your router.

## What's next

  * To configure hybrid subnet routing and migrate workloads to Google Cloud, see [Migrate workloads to Google Cloud with Hybrid Subnets](https://docs.cloud.google.com/vpc/docs/migrate-with-hybrid-subnets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
