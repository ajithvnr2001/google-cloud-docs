---
url: https://docs.cloud.google.com/oracle/database/docs/configure-vpc/
title: Configure VPC networks \u00a0|\u00a0 Oracle Database at Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:05.692794+00:00
---

# Configure VPC networks  |  Oracle Database at Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/database/docs/configure-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Oracle Database at Google Cloud ](https://docs.cloud.google.com/oracle/database/docs)
  * [ Guides ](https://docs.cloud.google.com/oracle/database/docs/overview)



Send feedback 

#  Configure VPC networks Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to set up a Virtual Private Cloud (VPC) network for your Oracle Database@Google Cloud resources.

Oracle Database@Google Cloud uses VPC networking projects to manage connectivity to your Oracle Database@Google Cloud resources. For more information about how VPC networks work at Google Cloud, see [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc).

## Before you begin

To configure a VPC network for your Oracle Database@Google Cloud resources, you need a Google Cloud project with billing enabled. The VPC network must be in the same Google Cloud project as your Oracle Database@Google Cloud resources.

Complete the following steps before setting up your VPC network:

  * [Set up your Google Cloud project](https://docs.cloud.google.com/oracle/database/docs/set-up).

  * Enable the Oracle Database@Google Cloud API for the project.

[Enable the Oracle Database@Google Cloud API](https://console.cloud.google.com/apis/enableflow?apiid=oracledatabase.googleapis.com)

  * Confirm that you have the required roles necessary to configure a networking project: `roles/compute.networkAdmin`.

For more information on how to assign roles, see [Configure IAM roles](https://docs.cloud.google.com/oracle/database/docs/iam-roles).




## Create a VPC network

To connect to your Oracle Database@Google Cloud resources, you need to define a VPC network. You can create a VPC network using the Google Cloud console, Google Cloud CLI, or VPC API. Oracle Database@Google Cloud only supports IPv4 connections.

To create a VPC network, choose one of the following:

  * [Create an auto mode VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-auto-network)
  * [Create a custom mode VPC network with only IPv4 subnets](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network)



## Modify a VPC network

To modify a VPC network that is being used by your Oracle Database@Google Cloud resources, see [Modify networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#modifying_a_vpc_network).

## What's next

  * [Learn more about how access works](https://docs.cloud.google.com/oracle/database/docs/iam-overview).
  * [Generate SSH keys](https://docs.cloud.google.com/oracle/database/docs/generate-ssh-keys) for your resources.
  * [Create a Exadata VM Cluster](https://docs.cloud.google.com/oracle/database/docs/create-clusters).
  * [Learn more about Oracle Database@Google Cloud](https://docs.cloud.google.com/oracle/database/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
