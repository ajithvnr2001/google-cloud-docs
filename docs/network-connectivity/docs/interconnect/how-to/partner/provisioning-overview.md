---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/provisioning-overview/
title: Partner Interconnect provisioning overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:27:52.902948+00:00
---

# Partner Interconnect provisioning overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/provisioning-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Partner Interconnect provisioning overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the steps to successfully create and provision a Partner Interconnect connection with a service provider.

Before you start the Partner Interconnect provisioning process, you must already have connectivity with a [supported service provider](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/service-providers).

**Note:** For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

To create and provision a Partner Interconnect connection, follow these steps:

  1. [Create a VLAN attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments)

Create a VLAN attachment for a Partner Interconnect connection. This step generates a pairing key that you share with your service provider. The pairing key is a unique key that lets a service provider identify and connect to your Virtual Private Cloud (VPC) network and associated Cloud Router. The service provider requires this key to complete the configuration of your VLAN attachment.

If you want to deploy [HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect), you must [create encrypted VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments#encrypted-attachments).

  2. [Request a connection from your service provider](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/requesting-connections)

Go to your service provider to submit the pairing key and other connection details, such as the connection capacity and location. Wait until your service provider configures your connection because they must check that they can serve your requested capacity. After their configuration is complete, you receive an email notification from Google.

  3. [Activate your connection](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/activating-connections)

After the service provider configures your connection, you must activate it. Activating the connection and checking its activation status enables you to verify that you established connectivity with the expected service provider.

  4. [Configure on-premises routers](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/configuring-onprem-routers)

For Layer 2 connections, you must establish a BGP session between your VPC network's Cloud Router and your on-premises router. Use your service provider's console to find the VLAN ID of the connection. Use that VLAN ID and the BGP peer IP address from the Google Cloud console to configure your on-premises router.

For Layer 3 connections, the service provider establishes a BGP session with your VPC network's Cloud Router. This configuration is automated and doesn't require any action from you.

  5. Optional: [Configure HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/configure-ha-vpn-interconnect)

If you are deploying HA VPN over Cloud Interconnect, you must build the HA VPN tunnels that carry encrypted traffic over your VLAN attachment.




[ Next Create VLAN attachments  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
