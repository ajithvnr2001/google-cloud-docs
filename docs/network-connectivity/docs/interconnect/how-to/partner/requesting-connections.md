---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/requesting-connections/
title: Request connections \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:27.481802+00:00
---

# Request connections  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/requesting-connections/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Request connections Stay organized with collections  Save and categorize content based on your preferences. 

After you create VLAN attachments for a Partner Interconnect connection, you can request connections from a [supported service provider](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/service-providers) with whom you already have connectivity. The service provider must configure your VLAN attachments before the attachments can start passing traffic. To request a Partner Interconnect connection, contact your service provider or visit their portal.

For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

To help you solve common issues that you might encounter when using Partner Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting#partner).

When you request a connection, your service provider requires the following information:

  * **Your VLAN attachment's[pairing key](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology#pairingkey).** This pairing key is generated when you create the VLAN attachment.

  * **The VLAN attachment's[region](https://docs.cloud.google.com/compute/docs/regions-zones).** The region that you select must be supported by a [Partner Interconnect location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#provisioning), which is a city where the service provider's network meets Google Cloud's network. Traffic between your Virtual Private Cloud (VPC) network and the service provider's network passes through this location. Typically, you would choose a location that's close to your data center to reduce the latency to your Google Cloud workloads.

Each service provider location supports only some regions. Check with your service provider to determine which regions each location supports.

  * **Your VLAN attachment's connection capacity.** This capacity can range from 50 Mbps to 50 Gbps. The capacity depends on your bandwidth requirements and what's offered by your service provider. Also, [pricing](https://docs.cloud.google.com/network-connectivity/docs/interconnect/pricing#partner-pricing) for each VLAN attachment is based on its capacity.




After you request a connection, wait until the service provider completes the VLAN attachment configuration. After their configuration is complete, you receive an email notification from Google. The state of your attachment changes from `PENDING_PARTNER` to `PENDING_CUSTOMER`. If you [pre-activated](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/partner-overview#pre-activate) your attachment, it changes to `ACTIVE`.

**Note** : If your encrypted VLAN attachment remains in the `PENDING_PARTNER` or `Waiting for service provider` state for an extended period of time, contact your service provider for assistance.

If you pre-activated your VLAN attachment and are using a Layer 3 connection, the attachment can immediately start passing traffic. If not, you must activate the attachment before it can pass traffic.

When your service provider completes the VLAN attachment configuration, Google automatically configures an interface and a BGP peering session on the associated Cloud Router. Do not modify these Google-defined configurations because doing so shuts down the BGP session. However, if you delete your attachment, you can delete these configurations.

For Layer 3 connections, the service provider supplies their ASN, which is automatically added to your Cloud Router's BGP session and allows BGP to establish a session.

[ Previous arrow_back  Create VLAN attachments  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments)

[ Next Activate connections  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/activating-connections)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
