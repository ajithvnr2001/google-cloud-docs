---
url: https://docs.cloud.google.com/compute/docs/networking/use-dpdk/
title: Enable faster network packet processing with DPDK \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:24.236697+00:00
---

# Enable faster network packet processing with DPDK  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/networking/use-dpdk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Enable faster network packet processing with DPDK Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to enable the [Data Plane Development Kit (DPDK)](https://www.dpdk.org/) on a virtual machine (VM) instance for faster network packet processing.

DPDK is a framework for performance-intensive applications that require fast packet processing, low latency, and consistent performance. DPDK provides a set of data plane libraries and a network interface controller (NIC) that bypass the kernel network and run directly in the user space. For example, enabling DPDK on your VM is useful when running the following:

  * Network function virtualization (NFV) deployments

  * Software-defined networking (SDN) applications

  * Video streaming or voice over IP applications




You can run DPDK on a VM that uses one of the following virtual NIC (vNIC) types:

  * Recommended: [gVNIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic)

A high-performance, secure, and scalable virtual network interface specifically designed for Compute Engine that succeeds virtIO as the next generation vNIC.

  * [VirtIO-Net](https://ozlabs.org/%7Erusty/virtio-spec/virtio-0.9.5.pdf)

An open source ethernet driver that lets VMs efficiently access physical hardwares, such as block storage and networking adapters.




One issue with running DPDK in a virtual environment, instead of on physical hardware, is that virtual environments lack support for SR-IOV and I/O Memory Management Unit (IOMMU) for high-performing applications. To overcome this limitation, you must run DPDK on guest physical addresses rather than host virtual addresses by using one of the following drivers:

  * [Userspace I/O (UIO)](https://www.kernel.org/doc/html/v4.18/driver-api/uio-howto.html)

  * IOMMU-less [Virtual Function I/O (VFIO)](https://docs.kernel.org/driver-api/vfio.html)




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




## Requirements

When creating a VM to run DPDK on, make sure of the following:

  * To avoid a lack of network connectivity when running your applications, use two Virtual Private Cloud networks:

    * A VPC network for the control plane

    * A VPC network for the data plane

  * The two VPC networks must both specify the following:

    * A subnet with a unique IP address range

    * The same region for their subnets

    * The same type of VNIC—either gVNIC or VirtIO-Net

  * When creating the VM:

    * You must specify the same region as the two VPC networks' subnets.

    * You must specify the vNIC type you plan to use with DPDK.

    * You must specify a [supported machine series](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison) for gVNIC or VirtIO-Net.




## Restrictions

Running DPDK on a VM has the following restrictions:

  * You can only use [single-stack subnets](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types) for the two VPC networks used in the VM.

  * If you're using gVNIC as the vNIC type for the two VPC networks, make sure of the following:

    * You must use DPDK version 22.11 or later.

    * You can only use [supported disk images](https://docs.cloud.google.com/compute/docs/images/os-details#networking).

  * If you want to enable [per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration) for higher network performance when creating the VM, you must specify the following:

    * gVNIC as the vNIC type

    * A [supported machine type](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#limitations) with 30 vCPUs or more




## Overview of DPDK features and versions

Google recommends using the most recent version of the DPDK driver to benefit from latest features and bug fixes. The following list provides an overview of what is available with each version of the DPDK driver:

26.07
    RX timestamping support (DQ only)
26.03
    

  * DPDK Passive Reset Support
  * DPDK Flow steering support (DQ only)


25.11
    Out-of-order completions for DQ format
25.07
    

  * FreeBsd Support
  * Support for non-4K guest page sizes


24.07
    

  * Modify ring size support (for all supported machine types).
  * [Secondary process support](https://doc.dpdk.org/guides/prog_guide/multi_proc_support.html).


24.03
    RSS support (for all supported machine types).
23.11
    

  * RX buffer size support (for all supported machine types).
  * Jumbo frame (9K) support for [third generation and later](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology) machine types.


23.07
    

  * Added support for third generation and later machine types.
  * Jumbo frame (9K) support for first and second generation machine types.


23.03
    

Support for reporting stats:

  * Software stats for all supported machine types.
  * Hardware stats for first and second generation machine types.


22.11
    Initial driver release with support for first and second generation machine types.

## Configure a VM to run DPDK

This section explains how to create a VM to run DPDK on.

### Create the VPC networks

Create two VPC networks, for the data plane and control plane, by using the Google Cloud console, Google Cloud CLI, or Compute Engine API. You can later specify these networks when creating the VM.

### Console

  1. Create a VPC network for the data plane:

     1. In the Google Cloud console, go to **VPC networks**.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

The **VPC networks** page opens.

     2. Click add_box **Create VPC network**.

The **Create a VPC network** page opens.

     3. In the **Name** field, enter a name for your network.

     4. In the **New subnet** section, do the following:

        1. In the **Name** field, enter a name for your subnet.

        2. In the **Region** menu, select a region for your subnet.

        3. Select **IPv4 (single-stack)** (default).

        4. In the **IPv4 range** , enter a [valid IPv4 range](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges) address in CIDR notation.

        5. Click **Done**.

     5. Click **Create**.

The **VPC networks** page opens. It can take up to a minute before the creation of the VPC network completes.

  2. Create a VPC network for the control plane with a firewall rule to allow SSH connections into the VM:

     1. Click add_box **Create VPC network** again.

The **Create a VPC network** page opens.

     2. In the **Name** field, enter a name for your network.

     3. In the **New subnet** section, do the following:

        1. In the **Name** field, enter a name for the subnet.

        2. In the **Region** menu, select the same region you specified for the subnet of the data plane network.

        3. Select **IPv4 (single-stack)** (default).

        4. In the **IPv4 range** , enter a [valid IPv4 range](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges) address in CIDR notation.

**Important:** Specify a different IPv4 range than the one you specified in the subnet for the data plane network. Otherwise, creating the network fails.
        5. Click **Done**.

     4. In the **IPv4 firewall rules** tab, select the **NETWORK_NAME -allow-ssh** checkbox.

Where NETWORK_NAME is the network name you specified in the previous steps.

     5. Click **Create**.

The **VPC networks** page opens. It can take up to a minute before the creation of the VPC network completes.




### gcloud

  1. To create a VPC network for the data plane, follow these steps:

     1. Create a VPC network with a manually-created subnet by using the [`gcloud compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create) with the `--subnet-mode` flag set to `custom`.
            
            gcloud compute networks create DATA_PLANE_NETWORK_NAME \
                --bgp-routing-mode=regional \
                --mtu=MTU \
                --subnet-mode=custom
            

Replace the following:

        * `DATA_PLANE_NETWORK_NAME`: the name for the VPC network for the data plane.

        * `MTU`: the maximum transmission unit (MTU), which is the largest packet size of the network. The value must be between `1300` and `8896`. The default value is `1460`. Before setting the MTU to a value higher than `1460`, see [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).

     2. Create a subnet for the VPC data plane network you've just created by using the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
            
            gcloud compute networks subnets create DATA_PLANE_SUBNET_NAME \
                --network=DATA_PLANE_NETWORK_NAME \
                --range=DATA_PRIMARY_RANGE \
                --region=REGION
            

Replace the following:

        * `DATA_PLANE_SUBNET_NAME`: the name of the subnet for the data plane network.

        * `DATA_PLANE_NETWORK_NAME`: the name of the data plane network you specified in the previous steps.

        * `DATA_PRIMARY_RANGE`: a [valid IPv4 range](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges) for the subnet in CIDR notation.

        * `REGION`: the region where to create the subnet.

  2. To create a VPC network for the control plane with a firewall rule to allow SSH connections into the VM, follow these steps:

     1. Create a VPC network with a manually-created subnet by using the [`gcloud compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create) with the `--subnet-mode` flag set to `custom`.
            
            gcloud compute networks create CONTROL_PLANE_NETWORK_NAME \
                --bgp-routing-mode=regional \
                --mtu=MTU \
                --subnet-mode=custom
            

Replace the following:

        * `CONTROL_PLANE_NETWORK_NAME`: the name for the VPC network for the control plane.

        * `MTU`: the MTU, which is the largest packet size of the network. The value must be between `1300` and `8896`. The default value is `1460`. Before setting the MTU to a value higher than `1460`, see [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).

     2. Create a subnet for the VPC control plane network you've just created by using the [`gcloud compute networks subnets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/create).
            
            gcloud compute networks subnets create CONTROL_PLANE_SUBNET_NAME \
                --network=CONTROL_PLANE_NETWORK_NAME \
                --range=CONTROL_PRIMARY_RANGE \
                --region=REGION
            

Replace the following:

        * `CONTROL_PLANE_SUBNET_NAME`: the name of the subnet for the control plane network.

        * `CONTROL_PLANE_NETWORK_NAME`: the name of the control plane network you specified in the previous steps.

        * `CONTROL_PRIMARY_RANGE`: a [valid IPv4 range](https://docs.cloud.google.com/vpc/docs/subnets#ipv4-ranges) for the subnet in CIDR notation.

**Important:** Specify a different IPv4 range than the one you specified in the data plane network's subnet. Otherwise, creating the subnet fails.
        * `REGION`: the region where to create the subnet, which must match with the region you specified in the data plane network's subnet.

     3. Create a VPC firewall rule that allows SSH connections to the control plane network by using the [`gcloud compute firewall-rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/firewall-rules/create) with the `--allow` flag set to `tcp:22`.
            
            gcloud compute firewall-rules create FIREWALL_RULE_NAME \
                --action=allow \
                --network=CONTROL_PLANE_NETWORK_NAME \
                --rules=tcp:22
            

Replace the following:

        * `FIREWALL_RULE_NAME`: the name of the firewall rule.

        * `CONTROL_PLANE_NETWORK_NAME`: the name of the control plane network you created in the previous steps.




### API

  1. To create a VPC network for the data plane, follow these steps:

     1. Create a VPC network with a manually-created subnet by making a `POST` request to the [`networks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/insert) with the `autoCreateSubnetworks` field set to `false`.
            
            POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks
            
            {
              "autoCreateSubnetworks": false,
              "name": "DATA_PLANE_NETWORK_NAME",
              "mtu": MTU
            }
            

Replace the following:

        * `PROJECT_ID`: the project ID of the current project.

        * `DATA_PLANE_NETWORK_NAME`: the name for the network for the data plane.

        * `MTU`: the maximum transmission unit (MTU), which is the largest packet size of the network. The value must be between `1300` and `8896`. The default value is `1460`. Before setting the MTU to a value higher than `1460`, see [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).

     2. Create a subnet for the VPC data plane network by making a `POST` request to the [`subnetworks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert).
            
            POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks
            
            {
              "ipCidrRange": "DATA_PRIMARY_RANGE",
              "name": "DATA_PLANE_SUBNET_NAME",
              "network": "projects/PROJECT_ID/global/networks/DATA_PLANE_NETWORK_NAME"
            }
            

Replace the following:

        * `PROJECT_ID`: the project ID of the project where the data plane network is located.

        * `REGION`: the region where you want to create the subnet.

        * `DATA_PRIMARY_RANGE`: the primary [IPv4 range](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges) for the new subnet in CIDR notation.

        * `DATA_PLANE_SUBNET_NAME`: the name of the subnet for the data plane network you created in the previous step.

        * `DATA_PLANE_NETWORK_NAME`: the name of the data plane network you created in the previous step.

  2. To create a VPC network for the control plane with a firewall rule to allow SSH connections to the VM, follow these steps:

     1. Create a VPC network with a manually-created subnet by making a `POST` request to the [`networks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/insert) with the `autoCreateSubnetworks` field set to `false`.
            
            POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks
            
            {
              "autoCreateSubnetworks": false,
              "name": "CONTROL_PLANE_NETWORK_NAME",
              "mtu": MTU
            }
            

Replace the following:

        * `PROJECT_ID`: the project ID of the current project.

        * `CONTROL_PLANE_NETWORK_NAME`: the name for the network for the control plane.

        * `MTU`: the MTU, which is the largest packet size of the network. The value must be between `1300` and `8896`. The default value is `1460`. Before setting the MTU to a value higher than `1460`, see [Maximum transmission unit](https://docs.cloud.google.com/vpc/docs/mtu).

     2. Create a subnet for the VPC data control network by making a `POST` request to the [`subnetworks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/subnetworks/insert).
            
            POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/subnetworks
            
            {
              "ipCidrRange": "CONTROL_PRIMARY_RANGE",
              "name": "CONTROL_PLANE_SUBNET_NAME",
              "network": "projects/PROJECT_ID/global/networks/CONTROL_PLANE_NETWORK_NAME"
            }
            

Replace the following:

        * `PROJECT_ID`: the project ID of the project where the control plane network is located.

        * `REGION`: the region where you want to create the subnet.

        * `CONTROL_PRIMARY_RANGE`: the primary [IPv4 range](https://docs.cloud.google.com/vpc/docs/subnets#manually_created_subnet_ip_ranges) for the new subnet in CIDR notation.

**Important:** Specify a different IPv4 range than the one you specified in the data plane network's subnet. Otherwise, creating the subnet fails.
        * `CONTROL_PLANE_SUBNET_NAME`: the name of the subnet for the control plane network you created in the previous step.

        * `CONTROL_PLANE_NETWORK_NAME`: the name of the control plane network you created in the previous step.

     3. Create a VPC firewall rule that allows SSH connections to the control plane network by making a `POST` request to the [`firewalls.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls/insert). In the request, set the `IPProtocol` field to `tcp` and the `ports` field to `22`.
            
            POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/firewalls
            
            {
              "allowed": [
                {
                  "IPProtocol": "tcp",
                  "ports": [ "22" ]
                }
              ],
              "network": "projects/PROJECT_ID/global/networks/CONTROL_PLANE_NETWORK_NAME"
            }
            

Replace the following:

        * `PROJECT_ID`: the project ID of the project where the control plane network is located.

        * `CONTROL_PLANE_NETWORK_NAME`: the name of the control plane network you created in the previous steps.




For more configuration options when creating a VPC network, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

### Create a VM that uses the VPC networks for DPDK

Create a VM that enables gVNIC or virtIO-Net on the two VPC networks that you created previously by using the Google Cloud console, gcloud CLI, and Compute Engine API.

Recommended: Specify [Ubuntu LTS](https://docs.cloud.google.com/compute/docs/images/os-details#ubuntu_lts) or [Ubuntu Pro](https://docs.cloud.google.com/compute/docs/images/os-details#ubuntu_pro) as the operating system image because of their package manager support for the UIO and IOMMU-less VFIO drivers. If you don't want to specify any of these operating systems, specifying [Debian 11 or later](https://docs.cloud.google.com/compute/docs/images/os-details#debian) is recommended for faster packet processing.

### Console

Create a VM that uses the two VPC network subnets you created in the previous steps by doing the following:

  1. In the Google Cloud console, go to **VM instances**.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

The **VM instances** page opens.

  2. Click add_box **Create instance**.

The **Create an instance** page opens.

  3. In the **Name** field, enter a name for your VM.

  4. In the **Region** menu, select the same region where you created your networks in the previous steps.

**Important:** Attempting to create a VM in a different region from where the control and data plane networks exist causes errors.
  5. In the **Zone** menu, select a zone for your VM.

  6. In the **Machine configuration** section, do the following:

     1. Select one of the following options:

        * For common workloads, select the **General purpose** tab (default).

        * For performance-intensive workloads, select the **Compute optimized** tab.

        * For high memory-to-vCPUs ratios workloads, select the **Memory optimized** tab.

        * For workloads that use Graphics processing units (GPUs), select the **GPUs** tab.

     2. Optional. If you specified **GPUs** in the previous step and you want to change the GPU to attach to the VM, do one or more of the following:

        1. In the **GPU type** menu, select a type of GPU.

        2. In the **Number of GPUs** menu, select the number of GPUs.

     3. In the **Series** menu, select a machine series.

**Important:** gVNIC is supported with all machine series, but VirtIO-Net is not supported with the newest machine series (third generation and T2A). If you choose a machine series that doesn't support your vNIC type, creating the VM fails.
     4. In the **Machine type** menu, select a machine type.

     5. Optional: Expand **Advanced configurations** , and follow the prompts to further customize the machine for this VM.

  7. Optional: In the **Boot disk** section, click **Change** , and then follow the prompts to change the disk image.

**Important:** If you specify gVNIC as the vNIC type for this VM, make sure to specify a [supported disk image](https://docs.cloud.google.com/compute/docs/images/os-details#networking). Otherwise, creating the VM fails.
  8. Expand the **Advanced options** section.

  9. Expand the **Networking** section.

  10. In the **Network performance configuration** section, do the following:

     1. In the **Network interface card** menu, select one of the following:

        * To use gVNIC, select **gVNIC**.

        * To use VirtIO-Net, select **VirtIO**.

**Note:** The value **-** in the **Network interface card** menu indicates that the vNIC type can be either gVNIC or VirtIO-Net depending on the machine family type. If both gVNIC and VirtIO-Net are available for a VM, the default is VirtIO-Net.
     2. Optional: For higher network performance and reduced latency, select the **Enable Tier_1 networking** checkbox.

**Important:** You can only enable Tier_1 networking when you use gVNIC and specify a [supported machine type](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#limitations) that has 30 vCPUs or more. Otherwise, creating the VM fails.
  11. In the **Network interfaces** section, do the following:

     1. In the **default** row, click delete **Delete item "default"**.

     2. Click **Add network interface**.

The **New network interface** section appears.

     3. In the **Network** menu, select the control plane network you created in the previous steps.

     4. Click **Done**.

     5. Click **Add network interface** again.

The **New network interface** section appears.

     6. In the **Network** menu, select the data plane network you created in the previous steps.

     7. Click **Done**.

  12. Click **Create**.

The **VM instances** page opens. It can take up to a minute before the creation of the VM completes.




### gcloud

Create a VM that uses the two VPC network subnets you created in the previous steps by using the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create) with the following flags:
    
    
    gcloud compute instances create VM_NAME \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --machine-type=MACHINE_TYPE  \
        --network-interface=network=CONTROL_PLANE_NETWORK_NAME,subnet=CONTROL_PLANE_SUBNET_NAME,nic-type=VNIC_TYPE \
        --network-interface=network=DATA_PLANE_NETWORK_NAME,subnet=DATA_PLANE_SUBNET_NAME,nic-type=VNIC_TYPE \
        --zone=ZONE
    

Replace the following:

  * `VM_NAME`: the name of the VM.

  * `IMAGE_FAMILY`: the image family for the operating system that the boot disk will be initialized with. Alternatively, you can specify the `--image=IMAGE` flag and replace `IMAGE` with a specific version of an image. Learn how to [view a list of images](https://docs.cloud.google.com/compute/docs/images#list_of_public_images_available_on) available in the Compute Engine images project.

  * `IMAGE_PROJECT`: the name of the image project that contains the disk image.

**Important:** If you specify gVNIC as the vNIC type for this VM, make sure to specify a [supported image family and project](https://docs.cloud.google.com/compute/docs/images/os-details). Otherwise, creating the VM fails.
  * `MACHINE_TYPE`: a machine type, [predefined](https://docs.cloud.google.com/compute/docs/machine-resource) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type), for the VM.

**Important:** gVNIC is supported with all machine series, but VirtIO-Net is not supported with the newest machine series (third generation and T2A). If you choose a machine series that doesn't support your vNIC type, creating the VM fails.
  * `VNIC_TYPE`: the vNIC type to use for the control plane and data plane networks. The value must be one of the following:

    * To use gVNIC, specify `GVNIC`.

    * To use VirtIO-Net, specify `VIRTIO_NET`.

  * `CONTROL_PLANE_NETWORK_NAME`: the name of the control plane network you created in the previous steps.

  * `CONTROL_PLANE_SUBNET_NAME`: the name of the subnet for the control plane network you created in the previous steps.

  * `DATA_PLANE_NETWORK_NAME`: the name of the data plane network you created in the previous steps.

  * `DATA_PLANE_SUBNET_NAME`: the name of the subnet for the control plane network you automatically created in the previous steps.

  * `ZONE`: the zone where to create the VM in. Specify a zone within the same region of the subnet you created in the previous steps.




For example, to create a VM named `dpdk-vm` in the `us-central1-a` zone that specifies a 512 GB SSD Persistent Disk volume, a predefined C2 machine type with 60 vCPUs, Tier_1 networking, and a data plane and a control plane network that both use gVNIC, run the following command:
    
    
    gcloud compute instances create dpdk-vm \
        --boot-disk-size=512GB \
        --boot-disk-type=pd-ssd \
        --image-project=ubuntu-os-cloud \
        --image-family=ubuntu-2004-lts \
        --machine-type=c2-standard-60 \
        --network-performance-configs=total-egress-bandwidth-tier=TIER_1 \
        --network-interface=network=control,subnet=control,nic-type=GVNIC \
        --network-interface=network=data,subnet=data,nic-type=GVNIC \
        --zone=us-central1-a
    

### API

Create a VM that uses the two VPC network subnets you created in the previous steps by making a `POST` request to the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert) with the following fields:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    
    {
      "name": "VM_NAME",
      "machineType": "MACHINE_TYPE",
      "disks": [
        {
          "initializeParams": {
            "sourceImage": "projects/IMAGE_PROJECT/global/images/IMAGE_FAMILY"
          }
        }
      ],
      "networkInterfaces": [
        {
          "network": "global/networks/CONTROL_PLANE_NETWORK_NAME",
          "subnetwork": "regions/REGION/subnetworks/CONTROL_PLANE_SUBNET_NAME",
          "nicType": "VNIC_TYPE"
        },
        {
          "network": "global/networks/DATA_PLANE_NETWORK_NAME",
          "subnetwork": "regions/REGION/subnetworks/DATA_PLANE_SUBNET_NAME",
          "nicType": "VNIC_TYPE"
        }
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the project ID of the project where the control plane VPC network and the data plane VPC network are located.

  * `ZONE`: the zone where to create the VM in.

**Important** : Make sure to specify a zone that meets the following requirements: 
    * The zone is within the same region where the subnets of the control and data plane networks are located.
    * The zone of the VM and the zone containing the machine type to use for the VM are matching.
Attempting to create a VM outside of the region where the specified subnets exist or in a zone that doesn't match the zone of the specified machine type causes errors. 
  * `VM_NAME`: the name of the VM.

  * `MACHINE_TYPE`: a machine type, [predefined](https://docs.cloud.google.com/compute/docs/machine-resource) or [custom](https://docs.cloud.google.com/compute/docs/instances/creating-instance-with-custom-machine-type), for the VM.

**Important:** gVNIC is supported with all machine series, but VirtIO-Net is not supported with the newest machine series (third generation and T2A). If you choose a machine series that doesn't support your vNIC type, creating the VM fails.
  * `IMAGE_PROJECT`: the name of the image project that contains the disk image.

  * `IMAGE_FAMILY`: the image family for the operating system that the boot disk will be initialized with. Alternatively, you can specify a specific version of an image. Learn how to [view a list of images](https://docs.cloud.google.com/compute/docs/images#list_of_public_images_available_on) in the Compute Engine images project.

**Important:** If you specify gVNIC as the vNIC type for this VM, make sure to specify a [supported disk image](https://docs.cloud.google.com/compute/docs/images/os-details#networking). Otherwise, creating the VM fails.
  * `CONTROL_PLANE_NETWORK_NAME`: the name of the control plane network you created in the previous steps.

  * `REGION`: the region where the subnets of the control plane and data plane networks exist.

  * `CONTROL_PLANE_SUBNET_NAME`: the name of the subnet for the control plane network you created in the previous steps.

  * `VNIC_TYPE`: the vNIC type to use for the control plane and data plane networks. The value must be one of the following:

    * To use gVNIC, specify `GVNIC`.

    * To use VirtIO-Net, specify `VIRTIO_NET`.

  * `DATA_PLANE_NETWORK_NAME`: the name of the data plane network you created in the previous steps.

  * `DATA_PLANE_SUBNET_NAME`: the name of the subnet for the control plane network you created in the previous steps.




For example, to create a VM named `dpdk-vm` in the `us-central1-a` zone that specifies a 512 GB SSD Persistent Disk volume, a predefined C2 machine type with 60 vCPUs, Tier_1 networking, and a data plane and a control plane network that both use gVNIC, make the following `POST` request:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/example-project/zones/us-central1-a/instances
    
    {
      "name": "dpdk-vm",
      "machineType": "c2-standard-60",
      "disks": [
        {
          "initializeParams": {
            "diskSizeGb": 512,
            "diskType": "pd-ssd",
            "sourceImage": "projects/ubuntu-os-cloud/global/images/family/ubuntu-2404-lts-amd64"
          },
          "boot": true
        }
      ],
      "networkInterfaces": [
        {
          "network": "global/networks/control",
          "subnetwork": "regions/us-central1/subnetworks/control",
          "nicType": "GVNIC"
        },
        {
          "network": "global/networks/data",
          "subnetwork": "regions/us-central1/subnetworks/data",
          "nicType": "GVNIC"
        }
      ],
      "networkPerformanceConfig": {
        "totalEgressBandwidthTier": "TIER_1"
      }
    }
    

For more configuration options when creating a VM, see [Create and start a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).

## Install DPDK on your VM

To install DPDK on your VM, follow these steps:

  1. Connect to the VM you created in the previous section by [using SSH](https://docs.cloud.google.com/compute/docs/connect/standard-ssh).

  2. Configure the dependencies for DPDK installation:
         
         sudo apt-get update && sudo apt-get upgrade -yq
         sudo apt-get install -yq build-essential ninja-build python3-pip \
             linux-headers-$(uname -r) pkg-config libnuma-dev
         sudo pip install pyelftools meson
         

  3. Install DPDK:
         
         wget https://fast.dpdk.org/rel/dpdk-23.07.tar.xz
         tar xvf dpdk-23.07.tar.xz
         cd dpdk-23.07
         

**Important:** If you specified gVNIC as the vNIC type in the previous steps, you must install DPDK version 22.11 or later. Using an earlier version of DPDK causes errors when you try to test or use DPDK on your VM.
  4. To build DPDK with the examples:
         
         meson setup -Dexamples=all build
         sudo ninja -C build install; sudo ldconfig
         




## Install driver

To prepare DPDK to run on a driver, install the driver by selecting one of the following methods:

  * Install a IOMMU-less VFIO.

  * Install UIO.




### Install a IOMMU-less VFIO

To install the IOMMU-less VFIO driver, follow these steps:

  1. Check if VFIO is enabled:
         
         cat /boot/config-$(uname -r) | grep NOIOMMU
         

If VFIO isn't enabled, then follow the steps in Install UIO.

  2. Enable the [No-IOMMU mode](https://lwn.net/Articles/660745/) in VFIO:
         
         sudo bash -c 'echo 1 > /sys/module/vfio/parameters/enable_unsafe_noiommu_mode'
         




### Install UIO

To install the UIO driver on DPDK, select one of the following methods:

  * Install UIO by using git.

  * Install UIO by using Linux packages.




#### Install UIO by using git

To install the UIO driver on DPDK by using `git`, follow these steps:

  1. Clone the [`igb_uio` git repository](https://github.com/ceph/dpdk/blob/master/lib/librte_eal/linuxapp/igb_uio/igb_uio.c) to a disk in your VM:
         
         git clone https://dpdk.org/git/dpdk-kmods
         

  2. From the parent directory of the cloned git repository, build the module and install the UIO driver on DPDK:
         
         pushd dpdk-kmods/linux/igb_uio
         sudo make
         sudo depmod && sudo insmod igb_uio.ko
         popd
         




#### Install UIO by using Linux packages

To install the UIO driver on DPDK by using Linux packages, follow these steps:

  1. Install the [`dpdk-igb-uio-dkms` package](https://packages.ubuntu.com/focal/dpdk-igb-uio-dkms):
         
         sudo apt-get install -y dpdk-igb-uio-dkms
         

  2. Install the UIO driver on DPDK:
         
         sudo modprobe igb_uio
         




## Bind DPDK to a driver and test it

To bind DPDK to the driver you installed in the previous section, follow these steps:

  1. Get the Peripheral Component Interconnect (PCI) slot number for the current network interface:
         
         sudo lspci | grep -e "gVNIC" -e "Virtio network device"
         

For example, if the VM is using `ens4` as the network interface, the PCI slot number is `00:04.0`.

  2. Stop the network interface connected to the network adaptor:
         
         sudo ip link set NETWORK_INTERFACE_NAME down
         

Replace `NETWORK_INTERFACE_NAME` with the name of the network interface specified in the VPC networks. To see which network interface the VM is using, view the configuration of the network interface:
         
         sudo ifconfig
         

  3. Bind DPDK to the driver:
         
         sudo dpdk-devbind.py --bind=DRIVER PCI_SLOT_NUMBER
         

Replace the following:

     * `DRIVER`: the driver to bind DPDK on. Specify one of the following values:

       * UIO driver: `igb_uio`

       * IOMMU-less VFIO driver: `vfio-pci`

     * `PCI_SLOT_NUMBER`: the PCI slot number of the current network interface formatted as `00:0NUMBER.0`.

  4. Create the `/mnt/huge` directory, and then create some hugepages for DPDK to use for buffers:
         
         sudo mkdir /mnt/huge
         sudo mount -t hugetlbfs -o pagesize=1G none /mnt/huge
         sudo bash -c 'echo 4 > /sys/kernel/mm/hugepages/hugepages-1048576kB/nr_hugepages'
         sudo bash -c 'echo 1024 > /sys/kernel/mm/hugepages/hugepages-2048kB/nr_hugepages'
         

  5. Test that DPDK can use the network interface you created in the previous steps by running the `testpmd` example application that is included with the DPDK libraries:
         
         sudo ./build/app/dpdk-testpmd
         

For more information about testing DPDK, see [Testpmd Command-line Options](https://doc.dpdk.org/guides/testpmd_app_ug/run_app.html#testpmd-command-line-options).




## Unbind DPDK

After using DPDK, you can unbind it from the driver you've installed in the previous section. To unbind DPDK, follow these steps:

  1. Unbind DPDK from the driver:
         
         sudo dpdk-devbind.py -u PCI_SLOT_NUMBER
         

Replace `PCI_SLOT_NUMBER` with the PCI slot number you specified in the previous steps. If you want to verify the PCI slot number for the current network interface:
         
         sudo lspci | grep -e "gVNIC" -e "Virtio network device"
         

For example, if the VM is using `ens4` as the network interface, the PCI slot number is `00:04.0`.

  2. Reload the Compute Engine network driver:
         
         sudo bash -c 'echo PCI_SLOT_NUMBER > /sys/bus/pci/drivers/VNIC_DIRECTORY/bind'
         sudo ip link set NETWORK_INTERFACE_NAME up
         

Replace the following:

     * `PCI_SLOT_NUMBER`: the PCI slot number you specified in the previous steps.

     * `VNIC_DIRECTORY`: the directory of the vNIC. Depending on the vNIC type you're using, specify one of the following values:

       * gVNIC: `gvnic`

       * VirtIO-Net: `virtio-pci`

     * `NETWORK_INTERFACE_NAME`: the name of the network interface you specified in the previous section.




## What's next

  * Review the [network bandwidth rates](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration#bandwidth-tiers) for your machine type.

  * Learn more about [creating and managing VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

  * Learn more about [higher MTU settings with jumbo frames](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu).

  * Learn more about [TCP optimization for network performance](https://docs.cloud.google.com/compute/docs/networking/tcp-optimization-for-network-performance-in-gcp-and-hybrid).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
