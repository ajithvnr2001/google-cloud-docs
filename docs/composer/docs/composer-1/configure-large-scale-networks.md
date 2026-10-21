---
url: https://docs.cloud.google.com/composer/docs/composer-1/configure-large-scale-networks/
title: Configure large-scale networks for Managed Airflow environments \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:40.490242+00:00
---

# Configure large-scale networks for Managed Airflow environments  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/composer-1/configure-large-scale-networks/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Gen 1 Guides ](https://docs.cloud.google.com/composer/docs/composer-1/composer-overview)



Send feedback 

#  Configure large-scale networks for Managed Airflow environments Stay organized with collections  Save and categorize content based on your preferences. 

Managed Airflow (Gen 3) | [Managed Airflow (Gen 2)](https://docs.cloud.google.com/composer/docs/composer-2/configure-large-scale-networks "View this page for Managed Airflow \(Gen 2\)") | **Managed Airflow (Legacy Gen 1)**

This section explains how to organize large-scale networks for Managed Airflow environments.

## Quotas for VPC, subnet and forwarding rules

Managed Airflow and GKE services use VPC peerings to establish connections between the [components of Managed Airflow environments](https://docs.cloud.google.com/composer/docs/composer-1/environment-architecture) (Customer Project and Tenant Project) and between a GKE cluster and a GKE Control Plane.

If your project has a large-scale network configuration, such as one with hundreds of networks and many VPC peerings configured, then when you try to create new Managed Airflow environments, the operations might fail because of VPC, subnet or forwarding rules quota errors.

The errors that you might encounter are:

  * The maximum number of VPC peerings per single VPC network is reached.

The default quota for a number of VPC peerings within a single VPC is 25 (unless you request an increase of this quota).

  * The maximum number of primary and secondary subnet IP ranges is reached.

The quota for this parameter is 400.

  * The maximum number of forwarding rules in the peering group for Internal TCP/ UDP Load Balancing is reached.

The quota for this parameter is 175.




For more information about default quotas for VPCs in Google Cloud, see [Quotas and limits](https://docs.cloud.google.com/vpc/docs/quota#vpc-peering).

## About large-scale networks for Managed Airflow environments

To overcome challenges related to these limits, you can organize your Managed Airflow environments into several VPC networks connected to your main/backbone VPC as it is described in the following sections.

This solution is applicable to Shared VPC and non-Shared VPC scenarios.

## Large-scale network setup in a non-Shared VPC scenario

![Large-scale network setup in a non-Shared VPC scenario](https://docs.cloud.google.com/static/composer/docs/images/large-scale-composer-network-regular.png)

To create a large-scale network setup for Managed Airflow:

  1. [Create a backbone VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network). This network acts as a hub for individual VPC networks that host Managed Airflow environments.

  2. [Create dedicated VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network) for Managed Airflow environments. You can combine several Managed Airflow environments into one VPC network. For example, you can name these networks `composer-vpc-1`, `composer-vpc-2`, and so on.

  3. Establish connectivity between Managed Airflow environment VPC networks and the backbone VPC by [creating HA VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to).


**Note:** The recommended way of configuring VPC network is to use custom mode when creating subnets.

## Large-scale network setup in a Shared VPC scenario

To solve the network peering limits issue in a Shared VPC networks, organize your Managed Airflow environments into several projects and VPC networks connected to one backbone VPC.

![Large-scale network setup in a Shared VPC scenario](https://docs.cloud.google.com/static/composer/docs/images/large-scale-composer-network-shared-vpc.png)

To create a large-scale Shared VPC network setup for Managed Airflow:

  1. In the host project, [create a backbone VPC network](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network). This network connects individual VPC networks for service projects running Managed Airflow environments.

  2. In the host project, [create VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#create-custom-network) for Managed Airflow environments. For example, you can name these networks `composer-shared-vpc-1`, `composer-shared-vpc-2`, and so on.

  3. Establish connectivity between these VPC networks and the backbone VPC network by manually [creating HA VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to).

  4. Configure Managed Airflow environments [in the Shared VPC setup](https://docs.cloud.google.com/composer/docs/composer-1/configure-shared-vpc).


**Note:** The recommended way of configuring VPC network is to use custom mode when creating subnets.

## What's next

  * [Configure Shared VPC](https://docs.cloud.google.com/composer/docs/composer-1/configure-shared-vpc)
  * [Create an environment](https://docs.cloud.google.com/composer/docs/composer-1/create-environments)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
