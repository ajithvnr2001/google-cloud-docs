---
url: https://docs.cloud.google.com/ull-solution/participants/create-ull-instances/
title: Create ULL Compute Engine instances \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:21.934124+00:00
---

# Create ULL Compute Engine instances  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/create-ull-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create ULL Compute Engine instances

**GA with allowlist** : ULL Solution is available only to approved exchange operators and their exchange participants. If you are an approved exchange participant, contact [exchanges@google.com](mailto:exchanges@google.com) to request access.

This page describes how to create Ultra Low Latency (ULL) Compute Engine instances by using U4P or U4C machine types from the [U4 machine family](https://docs.cloud.google.com/ull-solution/participants/u4-machines).

For an overview of the ULL infrastructure configuration process, see [Configuration overview for ULL Solution](https://docs.cloud.google.com/ull-solution/participants/configuration-overview).

## Before you begin

Before you create ULL compute instances, see the following sections.

### Create VPC networks

If you haven't already, create VPC networks for each of your instance's network interfaces as described in [Configuration overview for ULL Solution](https://docs.cloud.google.com/ull-solution/participants/configuration-overview).

### Create a placement policy

You can optionally apply a [spread placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview) to your ULL instance for increased resiliency. For more information, see [Create and apply spread placement policies](https://docs.cloud.google.com/compute/docs/instances/use-spread-placement-policies) in the Compute Engine documentation.

### Set your project

Set the gcloud CLI to use your project. Alternatively you can include the `--project=PROJECT_ID` flag for each command in the following procedures.
    
    
    gcloud config set project PROJECT_ID
    

Replace `PROJECT_ID` with the ID of your project.

### Enable APIs

If you haven't already, enable the following APIs.

###  Console 

Enable the Compute Engine API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=compute.googleapis.com)

###  gcloud 

Enable the Compute Engine API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
    
    
    gcloud services enable compute.googleapis.com

### Required roles

To get the permissions that you need to create Compute Engine instances , ask your administrator to grant you the following IAM roles: 

  * To create and manage compute instances: Compute Instance Admin (`compute.instanceAdmin`) on your project 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## ULL instance configuration overview

To create a ULL compute instance and configure the instance to send or receive ULL unicast and multicast traffic, do the following:

Step | Description  
---|---  
Create a ULL instance | Create an instance using a U4P or U4C machine type and connect its network interfaces to a general-purpose VPC network and a ULL VPC network. If you plan to use the instance as a multicast consumer, set the `igmp-query` flag to `IGMP_QUERY_V2`.  
Configure routing for the non-`nic0` interfaces for ULL unicast traffic | Configure source-based policy routing in the guest OS to ensure that egress packets leave through the correct interface and prevent asymmetric routing.  
Configure an instance to be a ULL multicast consumer |  Complete each of the following to receive multicast traffic on ULL network interfaces:  


  * Enable IGMP query
  * Set IGMPv2 in the guest OS
  * Configure reverse path filtering
  * Increase the ring buffer size of the network driver

To further optimize performance, we recommend that you also follow the procedures in [Work with Onload](https://docs.cloud.google.com/ull-solution/participants/use-onload) or [Work with DPDK](https://docs.cloud.google.com/ull-solution/participants/use-dpdk).   
  
Additionally, you can use the example commands on this page for testing multicast connectivity.

## Create a ULL instance

This section describes how to create a new instance to use for ULL unicast and multicast.

For general information about creating compute instances, including additional configuration options, see [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

###  gcloud 

To create a ULL instance, use the [`compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create).

The supported network interface type for ULL instances is `GVNIC`. You must include the `queue-count` field and specify a value of `32` for XDP support.

For the network interfaces that attach to a ULL VPC network, `no-address` must be specified.

Additionally, the following command includes the `igmp-query` flag to enable the instance to be a multicast consumer. This flag isn't required if the instance is a multicast producer only, or if the instance sends and receives unicast only.
    
    
    gcloud compute instances create INSTANCE_NAME \
        --zone=ZONE \
        --machine-type=MACHINE_TYPE \
        --image-project=IMAGE_PROJECT \
        --image-family=IMAGE_FAMILY \
        --maintenance-policy=TERMINATE \
        --network-interface=nic-type=GVNIC,queue-count=32,network=GENERAL_PURPOSE_VPC_NETWORK,subnet=GENERAL_PURPOSE_SUBNET \
        --network-interface=nic-type=GVNIC,queue-count=32,network=ULL_VPC_NETWORK,subnet=ULL_SUBNET_1,no-address,igmp-query=IGMP_QUERY_V2 \
        --network-interface=nic-type=GVNIC,queue-count=32,network=ULL_VPC_NETWORK,subnet=ULL_SUBNET_2,no-address,igmp-query=IGMP_QUERY_V2
    

Replace the following values:

  * `ZONE`: the zone in which to create the instance
  * `INSTANCE_NAME`: a name for the instance
  * `MACHINE_TYPE`: the U4P or U4C machine type of the instance
  * `IMAGE_PROJECT`: the [image project](https://docs.cloud.google.com/compute/docs/images/os-details#general-info), such as `rhel-cloud`. See [Operating system support for U4 machine types](https://docs.cloud.google.com/ull-solution/participants/u4-machines#u4-os-images).
  * `IMAGE_FAMILY`: the [image family](https://docs.cloud.google.com/compute/docs/images/os-details#general-info), such as `rhel-10-2-eus-oot-gve`. See [Operating system support for U4 machine types](https://docs.cloud.google.com/ull-solution/participants/u4-machines#u4-os-images).

Specifying an image family creates the instance from the most recent, non-deprecated version of the OS image in the image family. Alternatively, you can use the `--image` flag instead and specify an image version.

  * `GENERAL_PURPOSE_VPC_NETWORK`, `GENERAL_PURPOSE_SUBNET`: the VPC network and subnet to attach the `nic0` interface of the instance to

  * `ULL_VPC_NETWORK`: the ULL VPC network to attach the non-`nic0` interfaces to

    * `ULL_SUBNET_1`: the subnet in the ULL VPC network to attach the `nic1` interface to

    * `ULL_SUBNET_2`: the subnet in the ULL VPC network to attach the `nic2` interface to




## Configure routing for the non-`nic0` interfaces for ULL unicast traffic

By default, an instance uses the default route associated with its `nic0` interface to send traffic to any destination outside of its directly connected subnet. For more information, see the [multiple network interfaces overview](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts#specifications).

For your instance's `nic1` and `nic2` interfaces to successfully send and receive ULL unicast traffic, you must configure source-based policy routing in the guest OS. This configuration ensures that egress packets leave through the correct interface and prevents asymmetric routing, where traffic enters one interface but attempts to exit through `nic0`.

For an example of how to configure policy routing, see [Configure policy routing](https://docs.cloud.google.com/vpc/docs/configure-routing-additional-interface#configuring_policy_routing) in the _Configure routing for an additional network interface_ tutorial.

## Configure an instance to be a ULL multicast consumer

This section describes how to configure an existing ULL instance to be a multicast consumer.

### Enable IGMP query on an existing ULL instance

If you didn't enable IGMP when creating your instance, you can enable it on your existing instance as described in this section.

###  gcloud 

To enable IGMP query on an existing ULL instance, use the [`compute instances network-interfaces update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/network-interfaces/update).

Repeat the following command for each network interface that you want to receive multicast traffic.
    
    
    gcloud compute instances network-interfaces update INSTANCE_NAME \
        --zone=ZONE \
        --network-interface=NETWORK_INTERFACE_NAME \
        --igmp-query=IGMP_QUERY_V2
    

Replace the following values:

  * `INSTANCE_NAME`: the name of the instance
  * `ZONE`: the zone of the instance
  * `NETWORK_INTERFACE_NAME`: the name of the network interface on which to enable IGMP query. In Google Cloud, the format is `nicNUMBER`, such as `nic0`, `nic1`, or `nic2`.



### Set IGMPv2 in the guest OS

To set IGMPv2 in the guest OS of your instance, do the following:

  1. [Connect to the instance](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms) by using SSH.

  2. Run the following command and identify the device names of the network interfaces that you want to receive multicast traffic.
         
         sudo ifconfig
         

  3. For each applicable network interface, run the following command to force IGMPv2.
         
         sudo -i
         echo "2" > /proc/sys/net/ipv4/conf/NETWORK_INTERFACE_DEVICE_NAME/force_igmp_version
         

Replace `NETWORK_INTERFACE_DEVICE_NAME` with the device name of the network interface, such as `eth0`, `eth1`, or `eth2`.




### Configure reverse path filtering (`rp_filter`)

In some cases, such as with multi-NIC instances, strict source validation by reverse path filtering (`rp-filter`) can cause legitimate multicast packets to be dropped. To prevent this from happening, you can configure reverse path filtering to loosen or disable source validation on non-`nic0` network interfaces that receive multicast traffic. For example, the following commands configure reverse path filtering to disable source validation on `eth1` and `eth2` by setting `rp_filter` to `0`.
    
    
    sudo sysctl -w net.ipv4.conf.all.rp_filter=0
    sudo sysctl -w net.ipv4.conf.eth1.rp_filter=0
    sudo sysctl -w net.ipv4.conf.eth2.rp_filter=0
    

For more information about `rp_filter`, see [IP Sysctl](https://docs.kernel.org/networking/ip-sysctl.html) in the Linux kernel documentation.

### Increase the ring buffer size of the network driver

This section describes how to increase the ring buffer size of the network driver on your instance.

For multicast consumers that receive high levels of traffic, increase the ring buffer size of the network driver to a value of `2048` to help avoid packet loss. Do this for each network interface that receives multicast traffic.

See the following example commands, which configure `nic1` and `nic2`:
    
    
    sudo ethtool -G eth1 rx 2048 tx 2048
    sudo ethtool -G eth2 rx 2048 tx 2048
    

## Example commands for testing ULL multicast connectivity

This section provides example commands for testing multicast traffic without starting an application workload by using the [`iperf` tool](https://wikipedia.org/wiki/Iperf). The steps in this section require that the multicast configuration described in [Configuration overview for ULL Solution](https://docs.cloud.google.com/ull-solution/participants/configuration-overview) is complete.

**Note:** The example commands in this section use the `iperf` tool. If your VM instance doesn't have an external IP address, then you must configure [Cloud NAT](https://docs.cloud.google.com/nat/docs/set-up-manage-network-address-translation) so that you can install the `iperf` package on the instance.

### Send ULL multicast traffic from a multicast producer

  1. [Connect to the instance](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms) by using SSH.

  2. Install `iperf` if you haven't already. `iperf3` doesn't support multicast. The following command uses `iperf`, which installs `iperf2`.
         
         sudo yum install iperf
         

  3. To send multicast traffic to the multicast group IP address, run the following command:
         
         iperf -c MULTICAST_GROUP_ADDRESS%NIC -p 1234 -l 512 -i 1 -u -b 1000pps -t 999999 -B NIC_IP_ADDRESS
         

Replace the following values:

     * `MULTICAST_GROUP_ADDRESS`: the multicast group IP address
     * `NIC` the network interface device name, such as `eth1` or `eth2`
     * `NIC_IP_ADDRESS` the IP address that is assigned to the NIC that you specified



### Join a group and receive ULL multicast traffic from a multicast consumer

  1. [Connect to the instance](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms) by using SSH.

  2. Install `iperf` if you haven't already.
         
         sudo yum install iperf
         

  3. To join a multicast group and log the traffic that you receive, run the following command:
         
         iperf -s -p 1234 -B MULTICAST_GROUP_ADDRESS%NIC -l 512 -u -i 1
         

Replace the following values:

     * `MULTICAST_GROUP_ADDRESS` the multicast group IP address
     * `NIC` the network interface device name, such as `eth1` or `eth2`

For example, the following command joins a group with the IP address `224.1.0.176` to receive packets up to 512 bytes and logs the traffic received:
    
    iperf -s -p 1234 -B 224.1.0.176%eth1 -l 512 -u -i 1
    




## Verify ULL link status and speed

On your instance's ULL network interfaces, `ethtool` displays the actual physical port link status (`up`/`down`) and physical link speeds.

To check the physical link status and speed of a ULL network interface, run the following command:
    
    
    sudo ethtool NIC
    

Replace `NIC` with the name of the network interface assigned by the guest OS, such as `ens8f0` or `ens48f0`.

## What's next

  * For general information about troubleshooting network performance for bare metal instances, see [troubleshooting network performance](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-performance#bare_metal_instances) in the Compute Engine documentation. For example, you can disable CPU sleep states to achieve full network bandwidth performance.
  * To configure Onload or DPDK to optimize performance, see [Work with Onload](https://docs.cloud.google.com/ull-solution/participants/use-onload) and [Work with DPDK](https://docs.cloud.google.com/ull-solution/participants/use-dpdk).
  * To synchronize your instance system clock to the physical NIC clock of its host server, see [Configure accurate time](https://docs.cloud.google.com/ull-solution/participants/configure-time-sync).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
