---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/enabling-multiple-networks-access-same-attachment/
title: Options for connecting to multiple VPC networks \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:55:00.392440+00:00
---

# Options for connecting to multiple VPC networks  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/enabling-multiple-networks-access-same-attachment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Options for connecting to multiple VPC networks Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how Virtual Private Cloud (VPC) networks can access VLAN attachments for Dedicated Interconnect or Partner Interconnect that are located in a different VPC network. Both Shared VPC and VPC Network Peering support this functionality.

For VPC networks that don't use Shared VPC or VPC Network Peering, you must create additional VLAN attachments:

  * [Create VLAN attachments for Dedicated Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/creating-vlan-attachments)
  * [Create VLAN attachments for Partner Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/partner/creating-vlan-attachments)
  * [Use Dedicated Interconnect connections in other projects](https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/dedicated/using-interconnects-other-projects)

**Note:** If you don't use a Shared VPC network, you can create multiple VLAN attachments and Cloud Routers for other projects and networks. However, this method is less cost efficient than using a Shared VPC network.

## Use Cloud Interconnect with Shared VPC

To share your VLAN attachment in a project with other VPC networks, you can use Shared VPC. Using Shared VPC is preferable if you need to create many projects and would like to prevent individual project owners from managing their connectivity back to your on-premises network.

In this scenario, the host project contains a common Shared VPC network that VMs in service projects can use. Because VMs in service projects use this network, [Service Project Admins](https://docs.cloud.google.com/vpc/docs/shared-vpc#svc_proj_admins) don't need to create other VLAN attachments or Cloud Routers in the service projects.

You must create VLAN attachments and Cloud Routers for a Cloud Interconnect connection _only_ in the Shared VPC host project. The combination of a VLAN attachment and its associated Cloud Router are unique to a given Shared VPC network.

Service Project Admins can create VMs in subnets that exist in a host project's Shared VPC network based on the permissions that they have to the host project. VMs that use the Shared VPC network can use the custom dynamic routes for VLAN attachments available to that network.

For more information about setting up a Shared VPC network, see the [Shared VPC overview](https://docs.cloud.google.com/vpc/docs/shared-vpc) and [Provisioning Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc).

## Use Cloud Interconnect with VPC Network Peering

If you have only a few projects (two to three) or if you need to connect VPC networks between different organizations, you can use VPC Network Peering. With VPC Network Peering, you land VLAN attachments in one VPC network and then peer that network with one or more other VPC networks that you want to have access to your on-premises network.

We recommend using Shared VPC over using VPC Network Peering because Shared VPC is easier to configure and scale.

For information about VPC Network Peering, see the [VPC Network Peering overview](https://docs.cloud.google.com/vpc/docs/vpc-peering).

## What's next

  * To learn more about Cloud Interconnect options, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
