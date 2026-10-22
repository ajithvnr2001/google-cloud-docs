---
url: https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview/
title: Private pools overview \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:15.036534+00:00
---

# Private pools overview  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Private pools overview Stay organized with collections  Save and categorize content based on your preferences. 

This page gives an overview of **private pools** and explains its features. If you're new to Cloud Build, read [Cloud Build overview](https://docs.cloud.google.com/build/docs/overview).

## Overview of default pools and private pools

By default, when you run a build on Cloud Build, the build runs in a secure, hosted environment with access to the public internet. Each build runs on its own **worker** and is isolated from other workloads. You can customize your build in multiple ways including increasing the size of the machine type or allocating more disk space. The default pool has limits on how much you can customize the environment, particularly around private network access.

**Private pools** are private, dedicated pools of workers that offer greater customization over the build environment, including the ability to access resources in a private network. Private pools, similar to default pools, are hosted and fully-managed by Cloud Build and scale up and down to zero, with no infrastructure to set up, upgrade, or scale. Because private pools are customer-specific resources, you can configure them in more ways.

The following tables compares the features of the default pool with a private pool:

Feature | Default pool | Private pool  
---|---|---  
Fully managed |  |   
Pay per build minute |  |   
Auto scaling, scales to 0 |  |   
Access to public internet |  | Configurable  
[Peer into a VPC or shared VPC](https://docs.cloud.google.com/build/docs/private-pools/set-up-private-pool-environment) to access private resources |  |   
[VPC Service Controls support](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls) |  |   
Static internal IP ranges |  |   
Ability to disable public IPs |  |   
Maximum concurrent builds | 30 | 100+  
Machine types | [5](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/projects.builds#machinetype) | [64](https://docs.cloud.google.com/build/docs/private-pools/worker-pool-config-file-schema#machinetype)  
[Regions](https://docs.cloud.google.com/build/docs/locations) | global, [supported regions](https://docs.cloud.google.com/build/docs/locations) | [supported regions](https://docs.cloud.google.com/build/docs/locations)  
Region in which the build is run | The build runs in the region specified in `gcloud builds submit` or in the [Google Cloud console triggers page](https://console.cloud.google.com/cloud-build/triggers/add). | The build runs in the region where you create the private pool.  
  
## Network architecture

Private pool is a fully-managed resource created by a user in a Google Cloud project. Private pools can be created, updated, and deleted via API, Google Cloud CLI, Google Cloud console, or managed via infrastructure provisioning tools such as Terraform.

Using Identity and Access Management permissions, builds run on private pools can be submitted cross project; that is builds don't have to originate from the same project as the private pool. Likewise, the service account the build runs as can be configured to allow workers to access resources from other Google Cloud projects during a build.

Private pools are hosted in a Google-owned [service producer network](https://docs.cloud.google.com/vpc/docs/private-services-access) that comes with internal IP addresses. For your builds to access resources in your private network, you can create a private VPC peering connection between your VPC network and the service producer network.

The following diagram shows how builds are routed to the private pool. In this setup, the customer has two projects sending builds to Cloud Build. The customer has configured all the builds from these projects to be routed to their private pool. The service producer network, where the private pool is in, is peered to the customer's VPC network giving the builds access to private resources in the customer's VPC network.

![Builds on a private pool](https://docs.cloud.google.com/build/images/private-pool.png)

## What's next

  * Learn how to [set up your environment to create private pools](https://docs.cloud.google.com/build/docs/private-pools/set-up-private-pool-environment).
  * Learn how to [create and manage private pools](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools).
  * Learn how to [configure commonly used networking use cases](https://docs.cloud.google.com/build/docs/private-pools/use-in-private-network).
  * Learn how to [use VPC Service Controls with private pools](https://docs.cloud.google.com/build/docs/private-pools/using-vpc-service-controls).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
