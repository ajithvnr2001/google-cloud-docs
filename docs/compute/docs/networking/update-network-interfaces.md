---
url: https://docs.cloud.google.com/compute/docs/networking/update-network-interfaces/
title: Update the network interfaces for an instance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:55.033212+00:00
---

# Update the network interfaces for an instance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/networking/update-network-interfaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Update the network interfaces for an instance Stay organized with collections  Save and categorize content based on your preferences. 

Every Compute Engine instance has a `nic0` virtual network interface (vNIC) connected to a subnet in a VPC network. Depending on the instance's machine type, you can define additional vNICs only when you create a instance.

With Dynamic Network Interfaces, you can create VLAN-based subinterfaces for each vNIC, which lets you scale the number of network interfaces and VPC network connections.

You can add or remove Dynamic NICs without having to restart or recreate the instance. For more information, see the following pages in the Virtual Private Cloud (VPC) documentation:

  * [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts)
  * [Add Dynamic NICs to an instance](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics)
  * [Delete Dynamic NICs from an instance](https://docs.cloud.google.com/vpc/docs/delete-dynamic-nics)



This page describes how to update the properties of the network interface of an instance.

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Update a network interface of an instance

To update the properties of a network interface, see the procedure that corresponds to the property that you want to update, such as one of the following.

If you are updating a Dynamic NIC by using the gcloud CLI or the API, ensure that you specify the Dynamic NIC according to the [naming format of Dynamic NICs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#dynamic-nic-properties).

  * To update the network or subnetwork that the network interface belongs to, see [Migrating a VM between networks](https://docs.cloud.google.com/compute/docs/instances/migrating-interfaces-between-networks).
  * To update the IP stack type, see [Change the stack type of an instance](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-ipv6-address#update-vm-stacktype).
  * To update IP addresses, see the following: 
    * [Configure static internal IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-internal-ip-address)
    * [Configure static external IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address)
  * To update alias IP ranges, see [Modify alias IP ranges for an existing instance](https://docs.cloud.google.com/vpc/docs/configure-alias-ip-ranges#modifying_alias_ip_ranges_for_an_existing_instance).
  * To update instance netmasks, see [Compute instance netmasks](https://docs.cloud.google.com/vpc/docs/compute-instance-netmasks).
  * To update network edge security policies, see [Configure network edge security policies](https://docs.cloud.google.com/armor/docs/network-edge-policies).



## What's next

  * Learn how to [create and manage routes](https://docs.cloud.google.com/vpc/docs/using-routes) for VPC networks.
  * Learn how to scale your VMs and [optimize application latency with load balancing](https://docs.cloud.google.com/load-balancing/docs/tutorials/optimize-app-latency).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
