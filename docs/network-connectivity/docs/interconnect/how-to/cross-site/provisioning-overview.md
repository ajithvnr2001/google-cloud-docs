---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/provisioning-overview/
title: Cross-Site Interconnect provisioning overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:13.129330+00:00
---

# Cross-Site Interconnect provisioning overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/provisioning-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Cross-Site Interconnect provisioning overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the steps to successfully create and configure Cross-Site Interconnect.

**Note:** For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

To create and configure a Cloud Interconnect connection and create a cross-site network, follow these steps:

  1. [Check bandwidth quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/check-bandwidth-quota)

Check your quota to ensure that you have enough bandwidth to support your expected traffic between metros. If you need more quota, you must request an increase before proceeding. Similarly, check the limit for the maximum bandwidth per wire and request an exception if necessary.

  2. [Order Cross-Site Interconnect connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/order-connections)

Submit an order, specifying the details of your connections. Google then emails you an order confirmation. After your resources have been allocated, you receive another email with your LOA-CFAs.

  3. [Retrieve LOA-CFAs](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/retrieve-loas)

Send the LOA-CFAs to your vendor. They provision the connections between the Google peering edge and your on-premises network. Google automatically starts testing the light levels on each allocated port after 24 hours.

  4. [Test the connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/test-connections)

Follow the recommended steps to verify that your networks are connected to Google's network.

  5. [Create a cross-site network](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/create-network)

When your connections are ready to use, you need to connect your networks to each other. To do that, create a cross-site network over your connections, specifying the properties of the wire or wires between your networks, including their bandwidth.

  6. [Configure on-premises routers](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/configure-onprem-routers)

After you create a cross-site network with one or more wire groups, to start sending traffic between your sites, you need to configure your on-premises routers to establish connectivity with each other.




If you have any issues during the provisioning steps, refer to the escalation instructions provided in the LOA and the email that we sent to your technical contact.

[ Next Check bandwidth quotas and limits  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cross-site/check-bandwidth-quota)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
