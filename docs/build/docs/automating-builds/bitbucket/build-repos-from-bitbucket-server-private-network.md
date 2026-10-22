---
url: https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-server-private-network/
title: Build repositories from Bitbucket Server in a private network \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:58.455342+00:00
---

# Build repositories from Bitbucket Server in a private network  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-server-private-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Build repositories from Bitbucket Server in a private network Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Build enables you to create triggers to build from repositories hosted on [Bitbucket Server](https://confluence.atlassian.com/bitbucketserver/bitbucket-data-center-and-server-documentation-776639749.html), allowing you to execute builds in response to events such as commit pushes or pull requests associated with your Bitbucket Server repository.

This page explains how you can enable trigger functionality on a Bitbucket Server instance if your instance is hosted in a private network.

## Before you begin

  * Enable the Cloud Build, Secret Manager, Compute Engine, and Service Networking APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=cloudbuild.googleapis.com,secretmanager.googleapis.com,compute.googleapis.com,servicenetworking.googleapis.com&redirect=https%3A//cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-server-private-network)



  * If you have not created a private pool, follow the instructions in [Create and manage private pools](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools) to create a private pool. You will need a private pool to build in a private network.



## Building repositories from Bitbucket Server in a private network

If your Bitbucket Server instance is hosted in a private network and not reachable over a public internet connection, you must create a private connection between your VPC network and the [service producer network](https://docs.cloud.google.com/vpc/docs/private-services-access#service_producer_network). You also need a [private pool](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview) to build in a private network.

To create a Bitbucket Server trigger to build in a private network:

  1. Create a private connection between the VPC network and your service producer network by completing the following steps:

     1. [Create a new VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network) or [select an existing VPC network](https://console.cloud.google.com/networking/networks/list).

**Note:** You must configure your VPC network to have access to your Bitbucket Server instance in a private network.
     2. [Allocate a named IP range in the VPC network](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#allocating-range) for your peered network.

     3. [Allocate an internal IP range in the VPC](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#allocating-range) that the Cloud Build producer network can use to allocate to VMs maintaining a connection with private repositories.

To use the VPC network with Cloud Build, your prefix length must be `/23` or lower, such as `/22` or `/21`. This is to accommodate, at a minimum, both your triggers and your worker pools, because each service connection tries to claim an IP range with a prefix length of `/24`.

You can specify the range using the Classless Inter-Domain Routing (CIDR) routing notation in the format `STARTING_IP/SUBNET_PREFIX_SIZE`. For example, `192.0.2.0/24` has a prefix length of 24. The first 24 bits of the IP range are used as the subnet mask (`192.0.2.0`) while the possible hosts addresses range from `192.0.2.0` to `192.0.2.255`.

**Note:** The value of your prefix length must not exceed `/29`. If no value is specified for the range, a default value of `/24` is automatically assigned. If no value is specified for the prefix length, IP addresses are automatically assigned within the peered VPC network. 
     4. Establish a VPC network private connection between your VPC network and Google Cloud. To learn more, see [Creating a private connection](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#creating-connection).

     5. If you have DNS configured for your Bitbucket Server instance, you need to manually peer your DNS zone to our service provider. To learn more, see the [Sharing private DNS zones with service producers](https://docs.cloud.google.com/vpc/docs/configure-private-services-access#dns-peering).

     6. [OPTIONAL] If you do not want to create a private connection from your Cloud project, you can set up a [Shared VPC](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc) and have your Cloud project use that network instead if your project is part of an organization. You will still need the Shared VPC to be peered to the network.

  2. Use [private pools](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview) to run your builds. If you have not created a private pool, see [create a new private pool](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools).

  3. [Connect a Bitbucket Server host](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-host-bitbucket-server).

  4. [Connect a Bitbucket Server repository](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/connect-repo-bitbucket-server).

  5. [Create a Bitbucket Server trigger](https://docs.cloud.google.com/build/docs/automating-builds/bitbucket/build-repos-from-bitbucket-server) to build repositories hosted on a Bitbucket Server instance.




Your Bitbucket Server trigger will now automatically invoke builds on your Bitbucket Server instance based on your configuration. To learn how to run builds using a private pool, see [Running builds in a private pool](https://docs.cloud.google.com/build/docs/private-pools/run-builds-in-private-pool).

## What's next

  * Learn how to [create and manage build triggers](https://docs.cloud.google.com/build/docs/automating-builds/create-manage-triggers).
  * Learn how to [perform blue/green deployments on Compute Engine](https://docs.cloud.google.com/build/docs/deploying-builds/deploy-compute-engine).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
