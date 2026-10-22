---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/ha-vpn-interconnect-deploy-process/
title: Deploy HA VPN over Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:58.990399+00:00
---

# Deploy HA VPN over Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/ha-vpn-interconnect-deploy-process/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Deploy HA VPN over Cloud Interconnect Stay organized with collections  Save and categorize content based on your preferences. 

This page provides the steps required to deploy HA VPN over Cloud Interconnect. Before deploying HA VPN over Cloud Interconnect, see the [HA VPN over Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect).

To create and configure an HA VPN over Cloud Interconnect deployment, follow these steps:

  1. [Determine the level of SLA](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect#sla) that you need for your deployment:

     * **For a 99.9% SLA** , you need two Cloud Interconnect connections that are redundant with each other. The deployment occurs in a single [Google Cloud region](https://docs.cloud.google.com/docs/geography-and-regions) but in two different edge availability domains (zones).

     * **For a 99.99% SLA** , you need four Cloud Interconnect connections that make up two sets of redundant connections. The overall deployment must occur across two regions. Place each connection pair in a different region.

Each pair of redundant connections must be located in the same metropolitan area, but the individual connections must exist in different edge availability domains.

  2. Order the correct number of connections for your SLA.

For information about ordering connections, see [Order a Dedicated Interconnect connection](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/ordering-dedicated-interconnect) or [Request Partner Interconnect connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/requesting-connections).

If you are using Dedicated Interconnect, set up and test your connections.

  3. Optional: [Assign internal IP ranges to HA VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/ha-vpn-interconnect-internal-ips) interfaces.

  4. Create the encrypted VLAN attachments and the Cloud Router for the Cloud Interconnect tier:

     * For Dedicated Interconnect, see [Create encrypted VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments#encrypted-attachments).

     * For Partner Interconnect, see [Create encrypted VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments#encrypted-attachments).

  5. Configure your on-premises routers for Cloud Interconnect:

     * For Dedicated Interconnect, see [Configure on-premises routers](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configuring-onprem-routers).

     * For Partner Interconnect Layer 2 connections, see [Configure on-premises routers](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/configuring-onprem-routers).

You do not need to perform this step for Partner Interconnect Layer 3 connections.

  6. Create HA VPN gateways and tunnels, including the Cloud Router used for HA VPN. When you create the HA VPN gateways and tunnels, calculate the number of tunnels to deploy. Larger capacity VLAN attachments require more VPN tunnels to match throughput.

Because you can create both encrypted and unencrypted attachments on the same Cloud Interconnect connection, derive the number of tunnels that you require based only on the capacity of your encrypted VLAN attachments.

For more information, see [Configure HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/configure-ha-vpn-interconnect).

  7. Configure your on-premises VPN gateways. For more information, see [Configure the peer VPN gateway](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/configuring-peer-gateway).




## What's next?

  * To choose a connection type for Cloud Interconnect, see [Choosing a Network Connectivity product](https://docs.cloud.google.com/network-connectivity/docs/how-to/choose-product#cloud-interconnect).

  * To learn about best practices when planning for and configuring Cloud Interconnect, see [Best practices](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/best-practices).

  * To use Terraform to deploy HA VPN over Cloud Interconnect, see [Terraform examples for HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/ha-vpn-interconnect-terraform).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
