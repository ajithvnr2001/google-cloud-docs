---
url: https://docs.cloud.google.com/compute/docs/instances/create-instance-multiple-nics/
title: Create VMs with multiple network interfaces \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:17:56.917454+00:00
---

# Create VMs with multiple network interfaces  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/create-instance-multiple-nics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create VMs with multiple network interfaces Stay organized with collections  Save and categorize content based on your preferences. 

By default, every compute instance has at least one network interface (vNIC) that determines the Virtual Private Cloud network that the instance uses. You can create an instance with multiple network interfaces. For an overview of multiple network interfaces in Google Cloud, see [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts).

Each compute instance receives a default route using DHCP Option 121, as defined by [RFC 3442](https://datatracker.ietf.org/doc/html/rfc3442). The default route is associated with `nic0`. Unless manually configured otherwise, any traffic leaving an instance for any destination other than a directly connected subnet leaves the instance using the default route on `nic0`.

On Linux systems, you can configure custom rules and routes within the guest OS using the `/etc/iproute2/rt_tables` file and the `ip rule` and `ip route` commands. For more information, consult the guest OS documentation. For an example, see the tutorial [Configure routing for an additional interface](https://docs.cloud.google.com/vpc/docs/configure-routing-additional-interface).

If you don't require multiple network interfaces, follow the procedure for [creating and starting an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) to create instances with the default network configuration.

## Before you begin

  * Verify that all required networks and subnets are created before you create the compute instance. If you need to create networks or subnets, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks). 
  * Verify that each network has appropriate firewall rules that let data transfer to and from the instance that has multiple interfaces. If you need to create firewall rules, see [Use VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls). 
  * If you are [connecting an instance to multiple networks by using IPv6 addresses](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces#example-dual), then install the `google-guest-agent` version [20220603.00](https://github.com/GoogleCloudPlatform/guest-agent/releases/tag/20220603.00) or later. For more information, see [I can't connect to a secondary interface's IPv6 address](https://docs.cloud.google.com/vpc/docs/troubleshoot-multiple-interfaces#connect-ipv6). 
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




### Required roles

To get the permissions that you need to create an instance with a specific subnet, ask your administrator to grant you the [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to create an instance with a specific subnet. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create an instance with a specific subnet:

  * `compute.instances.create` on the project
  * To specify a subnet for your instance: `compute.subnetworks.use` on the project or on the chosen subnet 
  * To assign an external IP address to the instance when using a VPC network: `compute.subnetworks.useExternalIp` on the project or on the chosen subnet 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Requirements

Before you create an instance with multiple network interfaces, review the following requirements:

  * Each network interface must use a unique subnet. Multiple network interfaces of an instance can use subnets in different VPC networks or in the same VPC network as described in [Network and subnet requirements](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#specifications).
  * For multi-NIC compute instances in standalone projects, each network interface must use a subnet located in the same project as the instance. For instances in Shared VPC host or service projects, see [Shared VPC ](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#multiple-network-interfaces-in-shared-vpc) in the Virtual Private Cloud documentation. [Private Service Connect interfaces](https://docs.cloud.google.com/vpc/docs/about-private-service-connect-interfaces) provide a way for a multi-NIC instance to have network interfaces in subnets in different projects. For more information, see [About network attachments](https://docs.cloud.google.com/vpc/docs/about-network-attachments).



## Create VM instances with multiple network interfaces

Most Compute Engine instances let you configure multiple vNICs when creating the instance.

  * For information about the number of network interfaces you can create for an instance, see [Maximum number of network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#max-interfaces).
  * You can also configure [Dynamic NICs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#nic-types) when creating an instance.



For information about how to create a compute instance with multiple network interfaces, see [Create VM instances with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces#creating_virtual_machine_instances_with_multiple_network_interfaces).

To create a compute instance that uses a standard network interface and a Cloud RDMA network interface, see [Create an instance that uses Cloud RDMA](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-rdma).

## Add network interfaces to an existing instance

You can configure virtual NICs (vNICs) for an instance only when creating the instance. However, you can add or remove [Dynamic NICs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#nic-types) to an existing instance, and you don't have to restart the instance.

Dynamic NICs are subinterfaces of a parent vNIC. When you configure a Dynamic NIC, you specify a VLAN ID that is used to tag network traffic for the Dynamic NIC:

  * The VLAN ID of a Dynamic NIC must be an integer from 2 to 255.
  * The VLAN ID of a Dynamic NIC must be unique within a parent vNIC. However, Dynamic NICs that belong to different parent vNICs can use the same VLAN ID.



Google Cloud uses the following format for the name of a Dynamic NIC: `PARENT_NIC_NUMBER.VLAN_ID`

`PARENT_NIC_NUMBER` is the name of the parent vNIC, for example `nic0`. The `VLAN_ID` is the number you specified when configuring the Dynamic NIC. An example Dynamic NIC name is `nic0.4`.

For information about how to add Dynamic NICs to an instance, see [Add Dynamic NICs to an instance](https://docs.cloud.google.com/vpc/docs/add-dynamic-nics).

## What's next?

  * Learn how to use [SSH connections](https://docs.cloud.google.com/compute/docs/instances/ssh) to connect to your instance.
  * [Access VMs using internal DNS](https://docs.cloud.google.com/compute/docs/networking/using-internal-dns)
  * [Create a PTR record for a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-ptr-record)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
