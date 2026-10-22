---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview/
title: Dedicated Interconnect provisioning overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:31.055415+00:00
---

# Dedicated Interconnect provisioning overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/provisioning-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Dedicated Interconnect provisioning overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the steps to successfully create and configure a Dedicated Interconnect connection.

**Note:** For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

To create and configure a Cloud Interconnect connection for Dedicated Interconnect, follow these steps:

  1. Decide if you want [MACsec for Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/macsec-overview).

MACsec for Cloud Interconnect can help you secure traffic on Cloud Interconnect connections. If you want MACsec for Cloud Interconnect, you must select it when you order a Dedicated Interconnect connection.

MACsec for Cloud Interconnect is available for 100‑Gbps and 400‑Gbps links, regardless of location. If you want a 10G‑Gpbs link with MACsec support, verify that it is [available in your desired locations](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/macsec-overview#macsec-availability).

  2. [Order a Dedicated Interconnect connection](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/ordering-dedicated-interconnect)

Submit an order, specifying the details of your connection. Google then emails you an order confirmation. After your resources have been allocated, you receive another email with your LOA-CFAs.

  3. [Retrieve LOA-CFAs](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/retrieving-loas)

Send the LOA-CFAs to your vendor. They provision the connections between the Google peering edge and your on-premises network. Google automatically starts testing the light levels on each allocated port after 24 hours.

  4. [Test the connection](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/testing-connections)

If the light level of your physical ports is within the expected threshold, the ports are operational and Google sends you an automated email containing configuration details for connectivity testing. Apply these configurations to your router so that Google can confirm connectivity. This process confirms the IP connectivity of your connection's production configuration.

If you don't apply these configurations (or apply them incorrectly), Google sends an automated email with troubleshooting information.

If the light level of your physical ports is _not_ within the expected threshold, Google sends an automated email to notify you of the failure.

After all tests have passed, your Dedicated Interconnect connection is ready to use.

  5. [Create VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments)

When your connection is ready to use, you need to connect Virtual Private Cloud (VPC) networks to your on-premises network. To do that, first create a VLAN attachment, specifying an existing Cloud Router that's in the VPC network that you want to reach.

If you want to deploy [HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect), you must [create encrypted VLAN attachments](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments#encrypted-attachments).

  6. [Configure on-premises routers](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/configuring-onprem-routers)

After you create a VLAN attachment, to start sending traffic between networks, you need to configure your on-premises router to establish a BGP session with your Cloud Router. To configure your on-premises router, use the VLAN ID, interface IP address, and peering IP address provided by the VLAN attachment.

  7. Optional: [Configure HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/configure-ha-vpn-interconnect)

If you are deploying HA VPN over Cloud Interconnect, you must build the HA VPN tunnels that carry IPsec-encrypted traffic over your VLAN attachment.




If you have any issues during the provisioning steps, refer to the escalation instructions provided in the Letter of Authorization (LOA) and the email that we sent to your technical contact. All correspondence flows exclusively through the customer. For example:

  * If we determine that a fault originates on your side of the connection, you must open a ticket with your vendor.
  * If the vendor requires additional details to resolve the issue, they must request them from you.
  * If you lack such information, like a LOA, you must obtain it from Google and then communicate it to the vendor.



[ Next Order a connection  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/ordering-dedicated-interconnect)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
