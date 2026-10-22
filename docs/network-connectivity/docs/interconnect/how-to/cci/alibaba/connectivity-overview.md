---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/connectivity-overview/
title: Connect to Alibaba Cloud \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:53.904428+00:00
---

# Connect to Alibaba Cloud  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/connectivity-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Connect to Alibaba Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Cross-Cloud Interconnect lets you establish a dedicated physical connection between Google Cloud and Alibaba Cloud networks.

Google provisions this physical connection on your behalf. However, as part of the setup process, you must complete several tasks. You complete some tasks before Google provisions your connection and some tasks afterward.

These tasks include the following:

  1. [Choose your locations](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/choose-locations)

Identify locations for your primary and redundant Cross-Cloud Interconnect and Alibaba ports. Make a note of the location names. You need these details to complete the ordering and configuration processes.

  2. [Order Cross-Cloud Interconnect connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/order-google-connections)

Place an order for two Cross-Cloud Interconnect connections—a primary connection and a redundant one. In response, Google reserves two ports for you in the facility that you specify. For each port, we send you a confirmation email that contains instructions related to the next step: ordering your Alibaba ports. 

  3. [Order Alibaba ports](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/order-alibaba-ports)

Order your Alibaba ports, and download the corresponding letter of authorization (LOA). This document confirms your right to use the ports. Send the LOA to Google, following the instructions from the confirmation email that Google sent you. After Google receives the LOA, we begin the process of establishing your connections.

  4. [Configure your Google Cloud resources](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/configure-google-resources)

Complete the required configuration in Google Cloud. First, create a redundant set of VLAN attachments in your Virtual Private Cloud (VPC) network. Each VLAN attachment represents a logical connection between a region in your VPC network and your Alibaba resources. Then, for each VLAN attachment, use a Cloud Router to configure a Border Gateway Protocol (BGP) peering session.

  5. [Configure your Alibaba resources](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/configure-alibaba)

Configure your Alibaba Cloud resources. 

  6. [Verify your connections](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/test-connections)

Follow the recommended steps to verify that your networks are connected.




You can also use Cross-Cloud Interconnect to connect to other cloud service providers. For more information, see the [Supported cloud providers](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/cci-overview#supported-cloud-service-providers) section in the Cross-Cloud Interconnect overview. 

[ Next Choose your locations  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/cci/alibaba/choose-locations)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
