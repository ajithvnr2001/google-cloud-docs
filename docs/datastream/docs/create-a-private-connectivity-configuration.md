---
url: https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration/
title: Create a private connectivity configuration \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:34.602493+00:00
---

# Create a private connectivity configuration  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Create a private connectivity configuration Stay organized with collections  Save and categorize content based on your preferences. 

A private connectivity configuration lets you connect Datastream to data sources over an internal Google Cloud network, VPN, or Cloud Interconnect. You can connect through a Private Service Connect interface attached to a network attachment subnetwork in your Virtual Private Cloud (VPC) network.

Alternatively, you can use VPC peering to route traffic between two VPC networks over an allocated internal IP range. Because Datastream doesn't support DNS resolution in private connections, you must specify private IPv4 addresses for your sources.

Note that Datastream automatically deletes private connectivity configurations that haven't been used for a period of six consecutive months. To retain your private connectivity configurations, make sure they are used in at least one active connection profile.

## Before you begin

Before you create your private connectivity configuration, review the prerequisites:

  * For VPC peering, see [VPC peering prerequisites](https://docs.cloud.google.com/datastream/docs/vpc-peering#vpc-prereqs).
  * For Shared VPC, see [Shared VPC prerequisites](https://docs.cloud.google.com/datastream/docs/vpc-peering#shared-vpc).
  * For Private Service Connect interfaces, see [Private Service Connect prerequisites](https://docs.cloud.google.com/datastream/docs/psc-interfaces#psci-prereqs).



## Create the configuration

To create a private connectivity configuration, perform the following steps:

  1. Go to the **Private connectivity configurations** page in the Google Cloud console.

[Go to the Private connectivity configurations page](https://console.cloud.google.com/datastream/private-connections)

  2. Click **Create configuration**.

  3. Use the following table to populate the fields of the **Configure private connectivity** section of the **Create private connectivity configuration** page:

Field| Description  
---|---  
Configuration name| Enter the display name of the private connectivity configuration.  
Configuration ID| Datastream populates this field automatically based on the configuration name that you enter. You can keep the ID that's auto-generated or change it.  
Region| Select the region where the private connectivity configuration is stored. To use a private connection, any streams and connection profiles that use this configuration must be in the same region.  
  4. In the **Set up connection** section, select an option from the **Private connectivity method** drop-down:

     * **PSC interfaces** : select this option to use Private Service Connect interface as your private connectivity method: Field| Description  
---|---  
Project ID| Select the identifier of the project where the network attachment that you want to use is. By default, this is your current project. To change the value, click **Change** and select a different project. To view the list of network attachments in the selected project, you need the `compute.networkAttachments.get` permission.   
Network attachment| Select the network attachment that you created for your VPC. Ensure that the subnetwork associated with the network attachment doesn't overlap with the internal IP ranges reserved by Datastream (`10.1.0.0/16` and `10.2.2.0/24`).  
Update allowlist| Click this button to allow connections from the Datastream IP addresses. You need to have the `compute.networkAdmin` role assigned to connect to the network attachment.  
     * **VPC peering** : select this option to use VPC peering as your private connectivity method: Field| Description  
---|---  
Authorized VPC network| Select the VPC network that you created.  
Allocate an IP range| Enter an available IP range on the VPC network. Ensure that the IP range doesn't overlap with the internal IP ranges reserved by Datastream (`10.1.0.0/16` and `10.2.2.0/24`).  
  5. Click **CREATE**.

It takes a few minutes for your private connectivity configuration to be created. Background resources need to be created so that the configuration can be created.



After creating a private connectivity configuration, you can [view high-level and detailed information](https://docs.cloud.google.com/datastream/docs/view-a-private-connectivity-configuration) about it.

## What's next

  * Learn how to [view your private connectivity configuration](https://docs.cloud.google.com/datastream/docs/create-a-private-connectivity-configuration).
  * Find out how to [delete a private connectivity configuration](https://docs.cloud.google.com/datastream/docs/delete-a-private-connectivity-configuration).
  * Learn about the [Private Service Connect interfaces](https://docs.cloud.google.com/datastream/docs/psc-interfaces) private connectivity method.
  * Learn about the [VPC peering](https://docs.cloud.google.com/datastream/docs/vpc-peering) private connectivity method.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
