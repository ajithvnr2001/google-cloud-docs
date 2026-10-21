---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/update-networks/
title: Select VPC networks \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:38:21.704272+00:00
---

# Select VPC networks  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/update-networks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Select VPC networks Stay organized with collections  Save and categorize content based on your preferences. 

This page explains the considerations for adding or updating the Virtual Private Cloud (VPC) networks used by your Managed Service for Microsoft Active Directory domain.

When you add or update the VPC networks used by your Managed Microsoft AD domain, you should consider the following factors:

  * You can only add a VPC network from the project in which you create the domain.

  * You can only add up to a total of five VPC networks to your Managed Microsoft AD domain as authorized networks.

  * CIDR range considerations apply across all VPC networks in a Managed Microsoft AD domain. For more information, see [Select IP address ranges](https://docs.cloud.google.com/managed-microsoft-ad/docs/selecting-ip-address-ranges).

  * Adding authorized networks to your Managed Microsoft AD domain does not provide transitive connectivity. This means that a VM on one of the authorized networks is not automatically able to reach a VM on another authorized network. If you need connectivity between authorized networks, you must manually create VPC peering between them. For more information, see [VPC peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering).

  * Standard [VPC quotas and limits](https://docs.cloud.google.com/vpc/docs/quota) apply to these networks.




## What's next

  * [Create a domain](https://docs.cloud.google.com/managed-microsoft-ad/docs/create-domain)
  * [Manage authorized networks](https://docs.cloud.google.com/managed-microsoft-ad/docs/managing-authorized-networks)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
