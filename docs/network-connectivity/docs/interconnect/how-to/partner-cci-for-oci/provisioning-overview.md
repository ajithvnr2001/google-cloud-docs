---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-oci/provisioning-overview/
title: Partner Cross-Cloud Interconnect for OCI provisioning overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:50.350632+00:00
---

# Partner Cross-Cloud Interconnect for OCI provisioning overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-oci/provisioning-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Partner Cross-Cloud Interconnect for OCI provisioning overview Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the steps to successfully create and provision a partner Cross-Cloud Interconnect for Oracle Cloud Infrastructure (OCI) connection.

Before you start the partner Cross-Cloud Interconnect for OCI provisioning process, you must already have an Oracle Cloud Infrastructure account.

**Note:** For definitions of terms used on this page, see [Cloud Interconnect key terms](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/terminology).

To create and provision a partner Cross-Cloud Interconnect for OCI connection, follow these steps:

  1. [Choose a paired location](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-oci/paired-locations)

Google Cloud regions are paired with specific OCI regions. When you choose a specific Google Cloud region to create your resources in, you must choose the corresponding OCI region.

  2. [Create a VLAN attachment](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-oci/creating-vlan-attachments)

Create a VLAN attachment for a partner Cross-Cloud Interconnect for OCI connection. This step generates a pairing key that you share with OCI. The pairing key is a unique key that lets OCI identify and connect to your Virtual Private Cloud (VPC) network and associated Cloud Router. OCI requires this key to complete the configuration of your VLAN attachment.

  3. [Create a FastConnect virtual circuit with OCI](https://docs.oracle.com/en-us/iaas/Content/Network/Concepts/fastconnectprovider.htm)

Submit the pairing key and other connection details, such as the connection capacity and location to OCI. After the OCI configuration is complete, you receive an email notification from Google.

  4. [Activate your connection](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-oci/activating-connections)

After OCI configures your connection, you must activate it. Activating the connection and checking its activation status lets you verify that you established connectivity with OCI.




[ Next Paired locations  arrow_forward  ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner-cci-for-oci/paired-locations)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
