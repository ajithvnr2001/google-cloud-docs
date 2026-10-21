---
url: https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-network-configuration-errors/
title: Troubleshoot network configuration errors \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:24.909709+00:00
---

# Troubleshoot network configuration errors  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/troubleshoot/troubleshoot-network-configuration-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Troubleshoot network configuration errors Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve common network configuration issues in AlloyDB for PostgreSQL.

## NETWORK_NOT_PEERED

This error occurs when you haven't created a Virtual Private Cloud (VPC) peering with Service Networking.

To resolve this error, set up peering between Service Networking and the specified Virtual Private Cloud. For more information, see [Enable private services access](https://docs.cloud.google.com/alloydb/docs/configure-connectivity).

## NETWORK_PEERING_DELETED

This error occurs when the Virtual Private Cloud peering that was present earlier is now deleted.

To resolve this issue, set up peering between Service Networking and the specified Virtual Private Cloud. For more information, see [Increase private services access address space](https://docs.cloud.google.com/alloydb/docs/private-ip-space-increase).

## NETWORK_NOT_FOUND

This error occurs when the network with the name that was specified during cluster creation isn't found.

To resolve this issue, verify that the specified Virtual Private Cloud network is correct.

## RANGES_EXHAUSTED

This error occurs when Virtual Private Cloud peering doesn't have enough IP range space available in the IP reservation that is assigned to the Virtual Private Cloud peering.

To resolve this issue, increase the private services access address space. For more information, see [Increase private services access address space](https://docs.cloud.google.com/alloydb/docs/private-ip-space-increase).

To provide sufficient address space for AlloyDB, we recommend that you use a prefix length of 16 or less, with a minimum size of /24.

## SERVICE_NETWORKING_NOT_ENABLED

This error occurs when the Service Networking API isn't enabled in your Google Cloud project.

To resolve this issue, [enable the required APIs](https://docs.cloud.google.com/alloydb/docs/quickstart/create-and-connect#before-you-begin).

## NETWORK_NOT_IN_CONSUMERS_PROJECT

This error occurs when the network specified during cluster creation is not in your Google Cloud project.

To resolve this issue, verify that the specified Virtual Private Cloud network is correct.

## NETWORK_NOT_IN_CONSUMERS_HOST_PROJECT

This error occurs when the Shared VPC network specified during cluster creation isn't in your host project.

To resolve this issue, verify that the specified Virtual Private Cloud network is correct. For more information, see [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc).

## HOST_PROJECT_NOT_FOUND

This error occurs when the Shared VPC host project is not found.

To resolve this issue, verify that the specified Virtual Private Cloud network is correct. For more information, see [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc).

## CONSUMER_PROJECT_NOT_SERVICE_PROJECT

This error occurs when the specified Shared VPC isn't attached to the AlloyDB project.

To resolve this issue, verify that the specified Virtual Private Cloud network is correct. For more information, see [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
