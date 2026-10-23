---
url: https://docs.cloud.google.com/vpc/docs/multicast/configure-consumer-vms/
title: Configure multicast consumer instances \u00a0|\u00a0 Cloud Multicast \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:56:59.026572+00:00
---

# Configure multicast consumer instances  |  Cloud Multicast  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/configure-consumer-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/multicast/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure multicast consumer instances

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This page describes how to configure Compute Engine instances so that they can receive multicast traffic. Instances that receive multicast traffic are called _multicast consumers_.

The procedures on this page describe how to configure multicast consumers as follows:

  * Enable IGMP query on a new or existing instance and set IGMPv2 in the guest OS.

Completing these steps lets applications that run on your instance join and leave multicast groups.

  * For multicast configurations in which the multicast administrator has pre-configured a placement policy, you can optionally apply the placement policy to a new or existing instance.

  * For multicast consumers that receive high levels of traffic, increase the ring buffer size of the network driver to help avoid packet loss.




For more information about how IGMPv2 works after you configure your instance, see [How IGMPv2 works](https://docs.cloud.google.com/vpc/docs/multicast/overview#how-igmp-works).

## Before you begin

Before you create multicast consumer instances, see the following sections.

### Review machine and OS considerations for multicast consumers

To help ensure optimal performance, review the following guidance and create your instance accordingly:

  * **Machine type** : Review the guidance described in [Machine considerations for multicast producers and consumers](https://docs.cloud.google.com/vpc/docs/multicast/overview#machine-requirements).

  * **Operating system (OS) and network driver** : See the following:

    * We recommend that you use a Linux OS. For more information, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).

    * For multicast consumers that receive high levels of traffic, we recommend increasing the ring buffer size of the network driver to a value of `2048` to help avoid packet loss.

If you are using a virtual machine (VM) instance, see the following considerations for the [gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic):

      * Some earlier OS versions might not use a gVNIC driver version that supports increasing the ring buffer size. Examples of OS versions that support this functionality by default are RHEL 10, Rocky Linux 10, and Ubuntu 24.04.

      * If you can't increase the ring buffer size by default, then you must first [manually upgrade the gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup) to version 1.4.5 or later.




### Check for a pre-configured placement policy

If the multicast administrator configured a [domain group](https://docs.cloud.google.com/vpc/docs/multicast/resources-topologies#domains) for redundant multicast domains, then Google Cloud automatically provides an optional [placement policy](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview), unless the multicast administrator disabled the policy when activating the domain. When you apply this placement policy to new or existing instances, Compute Engine tries to place the instances as close as possible to the infrastructure for the multicast domain in the corresponding zone.

To check whether a placement policy is available to you, do the following:

  1. View the details of your multicast consumer association for the zone in which you plan to create your instance. See [View multicast consumer associations](https://docs.cloud.google.com/vpc/docs/multicast/view-resources#view-consumer-associations).

  2. If the output contains a placement policy name in the `placementPolicy` field, then you can apply the placement policy when creating a new instance or configuring an existing instance. Record the value so that you can use it when completing the procedures on this page.




## Create a multicast consumer instance

This section describes how to create a new instance to use as a multicast consumer by enabling IGMP and using an optional placement policy if applicable.

For more information about creating instances, see [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

###  gcloud 

  1. To create a new multicast consumer instance, use the [`compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) and specify the `igmp-query` flag:
         
         gcloud compute instances create INSTANCE_NAME \
            --zone=ZONE \
            --network-interface=network=MULTICAST_CONSUMER_NETWORK,subnet=MULTICAST_CONSUMER_SUBNET,igmp-query=IGMP_QUERY_V2[,no-address] \
            --machine-type=MACHINE_TYPE \
            --image-project=IMAGE_PROJECT \
            --image-family=IMAGE_FAMILY_NAME \
            --network-performance-configs=total-egress-bandwidth-tier=TIER_1  \
            [--maintenance-policy=MAINTENANCE_POLICY] \
            [--resource-policies=PLACEMENT_POLICY_NAME] \
            [--shielded-secure-boot] \
            [--shielded-vtpm] \
            [--shielded-integrity-monitoring]
         

Replace the following values:

     * `INSTANCE_NAME`: a name for the instance
     * `ZONE`: the zone in which to create the instance. Must a zone in which you activated the multicast consumer VPC network that hosts the instance.
     * `MULTICAST_CONSUMER_NETWORK`, `MULTICAST_CONSUMER_SUBNET`: the multicast consumer VPC network and subnet in which to host the instance
     * `MACHINE_TYPE`: the machine type for the instance. If you haven't already, review the guidance described in [Machine considerations for multicast producers and consumers](https://docs.cloud.google.com/vpc/docs/multicast/overview#machine-requirements).
     * `IMAGE_PROJECT`: the [image project](https://docs.cloud.google.com/compute/docs/images/os-details#general-info) that contains the image, such as `ubuntu-os-cloud`.
     * `IMAGE_FAMILY`: the [image family](https://docs.cloud.google.com/compute/docs/images/os-details#general-info), such as `ubuntu-2404-lts-amd64`.

Specifying an image family creates the instance from the most recent, non-deprecated version of the OS image in the image family. Alternatively, you can use the `--image` flag instead and specify an image version.

     * If you are using a machine type with 48 vCPUs or more, keep the `-network-performance-configs` flag and its value, which enables [Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#create-high-bandwidth-vms-containers). If you are using a machine type with 32 vCPUs, remove this flag as Tier_1 networking isn't supported for C4 instances with 32 vCPUs or fewer.

     * If a placement policy is available, you can optionally create the instance with the placement policy by using the following flags. For more information, see [Apply a compact placement policy while creating a instance](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies#create-vm).

       * `MAINTENANCE_POLICY`: the [host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#available_host_maintenance_properties) of the instance. If your chosen machine type doesn't support live migration, then you can only specify `TERMINATE`. Otherwise, you can specify `MIGRATE` or `TERMINATE`. Alternatively, to use the default maintenance policy for your instance type, you can omit this flag.
       * `PLACEMENT_POLICY_NAME`: the name of the placement policy from the output of your multicast consumer association.
     * Optionally, create a Shielded VM without an external IP address by using the `--shielded` and `no-address` parameters. For more information, see [What is Shielded VM?](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm).

  2. Follow the instructions to set IGMPv2 in the guest OS.

  3. Follow the instructions to increase the ring buffer size of the network driver.




## Configure an existing instance to be a multicast consumer

This section describes how to configure an existing instance to be a multicast consumer by enabling IGMP and using an optional placement policy if applicable.

###  gcloud 

  1. To configure an existing instance to be a multicast consumer, use the [`compute instances network-interfaces update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/network-interfaces/update) and specify the `igmp-query` flag.

The following command updates the `nic0` interface. To specify a different interface, use the `--network-interface` flag.
         
         gcloud compute instances network-interfaces update INSTANCE_NAME \
            --zone=ZONE \
            --igmp-query=IGMP_QUERY_V2
         

Replace the following values:

     * `INSTANCE_NAME`: the name of the instance
     * `ZONE`: the zone of the instance
  2. If a placement policy is available and you want to apply it to your instance, see [Apply a compact placement policy to an existing instance](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies#apply-to-vm). For the policy name, use the name of the placement policy from the output of your multicast consumer association.

  3. Follow the instructions to set IGMPv2 in the guest OS.

  4. Follow the instructions to increase the ring buffer size of the network driver.

  5. If the machine type of your instance has 48 vCPUs or more, then enable Tier_1 networking as described in [Update a compute instance to include Tier_1 networking](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#update-vms).




## Set IGMPv2 in the guest OS

To set IGMPv2 in the guest OS of your instance, do the following:

  1. [Connect to the instance](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms) by using SSH.

  2. Run the following command and identify the name of the network interface that is attached to a subnet in the multicast consumer VPC network.
         
         sudo ifconfig
         

  3. Run the following command to force IGMPv2.
         
         sudo -i
         echo "2" > /proc/sys/net/ipv4/conf/NETWORK_INTERFACE_NAME/force_igmp_version
         

Replace `NETWORK_INTERFACE_NAME` with the name of the network interface.




## Increase the ring buffer size of the network driver

This section describes how to increase the ring buffer size of the network driver on your instance.

Depending on the OS version that your instance uses, you might need to [manually upgrade the gVNIC driver](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup) to version 1.4.5 or later to be able to run the following command successfully.

For multicast consumers that receive high levels of traffic, increase the ring buffer size of the network driver to a value of `2048` to help avoid packet loss. See the following example command:
    
    
    sudo ethtool -G eth0 rx 2048 tx 2048
    

For more information, see [Driver features and configuration](https://github.com/GoogleCloudPlatform/compute-virtual-ethernet-linux?tab=readme-ov-file#driver-features-and-configuration).

## What's next

  * To quickly test your multicast configuration without starting an application workload, you can use the `iperf` tool as described in [Example commands for testing multicast traffic](https://docs.cloud.google.com/vpc/docs/multicast/troubleshoot#testing-example).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
