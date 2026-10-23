---
url: https://docs.cloud.google.com/vpc/docs/network-profiles/
title: Network profiles for specific use cases \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:18:22.365731+00:00
---

# Network profiles for specific use cases  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/network-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Network profiles for specific use cases

This page provides an overview of network profiles in Google Cloud.

## About network profiles

Google Cloud provides network profiles that each define a specific use case for a VPC network. When you create a VPC network, you can associate a network profile with the new network:

  * VPC networks that are created _without_ an associated network profile are called _regular VPC networks_.

  * A VPC network that has an associated network profile operates differently than a regular VPC network. The differences depend on the network profile—each network profile does the following:

    * Enables unique features that aren't available in regular VPC networks, such as support for Remote Direct Memory Access (RDMA) NICs.

    * Limits certain feature combinations that are incompatible with the network profile's use case.




### Specifications

Network profiles have the following specifications:

  * **Network profile properties** : See the following details about the properties of network profiles:

    * Network profiles are predefined by Google Cloud. You can't create a network profile or modify the properties of a network profile.

    * Each network profile resource consists of the following:

      * `name`: the resource name of the network profile. The resource name always starts with a location (region or zone).
      * `description`: a description of the network profile.
      * `location`: the location of the network profile (region or zone).
      * `features`: the set of features that are enabled and disabled by the network profile.
  * **Association with a VPC network** : You can associate a network profile with a VPC network only when you create the VPC network.

    * To create a _regular VPC network_ , don't associate a network profile.
    * You can't change the associated network profile of a VPC network after the network has been created.
  * **Location requirements** : If you associate a network profile with a new VPC network, the resources that use that VPC network must be in the same location as the network profile's location.




## Available network profiles

You can list network profiles and view the details of each network profile as described in [View network profiles](https://docs.cloud.google.com/vpc/docs/view-network-profiles). The following list summarizes network profile options that are available:

  * **No network profile** : Any VPC network that doesn't have an associated network profile is a regular VPC network.

  * **[RDMA network profiles](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles)** : Use an RDMA network profile to configure a VPC network to support RDMA NICs. A VPC network created with an RDMA network profile enables zonal workloads that depend on RDMA connectivity, such as AI workloads in Google Cloud. For more information about running AI workloads in Google Cloud, see the [AI Hypercomputer](https://docs.cloud.google.com/ai-hypercomputer/docs/overview) documentation.




## What's next

  * Learn about [RDMA network profiles](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles).
  * Create a [VPC network for RDMA NICs](https://docs.cloud.google.com/vpc/docs/create-vpc-network-rdma).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
