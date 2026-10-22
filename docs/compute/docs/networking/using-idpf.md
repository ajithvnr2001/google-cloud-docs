---
url: https://docs.cloud.google.com/compute/docs/networking/using-idpf/
title: Using the IDPF network interface \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:05.041327+00:00
---

# Using the IDPF network interface  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/networking/using-idpf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Using the IDPF network interface Stay organized with collections  Save and categorize content based on your preferences. 

Bare metal instances available with machine series such as C3 and X4 use [Infrastructure Data Plane Function (IDPF)](https://docs.kernel.org/next/networking/device_drivers/ethernet/intel/idpf.html), which is a standardized, multi-vendor PCIe network data plane function device. IDPF is a physical device. The IDPF driver is included in the kernel of Linux operating system (OS) images.

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

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




## Supported features with IDPF

Similar to gVNIC, the following features are supported with IDPF:

  * [Per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)
  * Large MTU support ([Jumbo Frames](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu))
  * [VPC network](https://docs.cloud.google.com/vpc/docs/overview) features: 
    * Cloud Next Generation Firewall
    * Packet mirroring
    * VPC Flow Logs
    * IPv6 support
    * VPC Network Peering
    * Network Connectivity Center 



## Limitations of the IDPF network interface

When using the IDPF network interface, note the following limitations:

  * Only a single NIC is supported for the instance. You can't create a compute instance with multiple NICs.
  * IDPF only supports the default queue allocation with 16 [Receive and transmit queues (RX/TX)](https://docs.cloud.google.com/compute/docs/network-bandwidth#rx-tx) per NIC.
  * If you use [DPDK](https://docs.cloud.google.com/compute/docs/networking/use-dpdk) with a bare metal instance, DPDK replaces the IDPF as the driver for the physical NIC. The DPDK application must forward packets to the kernel, such as through a [TAP interface](https://wikipedia.org/wiki/TUN/TAP).



## Overview of using IDPF with bare metal instances

To create a bare metal instance that uses IDPF, complete the following steps:

  1. Choose a [public OS image](https://docs.cloud.google.com/compute/docs/images#os-compute-support) that supports IDPF, or create a custom OS image that is tagged to use IDPF.
  2. Create a bare metal instance using the public or custom OS image. During instance creation, configure the network interface to use IDPF.
  3. Verify that IDPF is enabled.



## Operating system support

On Compute Engine, IDPF is available with a limited number of supported public OS images.

For information about which operating systems are supported with IDPF, see the **Interfaces** tab for an [operating system](https://docs.cloud.google.com/compute/docs/images/os-details#networking).

## Use on non-supported operating systems

For OS images that don't support IDPF, check with the operating system distributor about including the IDPF driver.

After you get an operating system image that includes IDPF, [import a bootable virtual disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks#bootable) that contains the customized operating system. You can then use the custom OS image to create bare metal instances that use IDPF on that operating system. For more information about creating a custom OS image for use with bare metal instances, see Create a custom OS image that supports IDPF on this page.

## Create a custom OS image that supports IDPF

If you require a different OS image or version for your bare metal instance than those provided by Google Cloud, you can create the OS image using either the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute) or [REST](https://docs.cloud.google.com/compute/docs/reference/rest/v1). For detailed information and best practices for creating custom OS images, see [Create custom OS images](https://docs.cloud.google.com/compute/docs/images/create-custom).

###  gcloud 

When creating the custom image, either from a Google Cloud provided image or an imported OS image, you must tag the OS image with `IDPF`. Use the [`gcloud compute images create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/create) as shown in the following example:
    
    
    gcloud compute images create IMAGE_NAME \
        --source-image=SOURCE_IMAGE \
        --source-image-project=SOURCE_IMAGE_PROJECT \
        --guest-os-features=IDPF
    

Replace the following:

  * `IMAGE_NAME`: a name for the custom image.
  * `SOURCE_IMAGE`: a specific OS image that supports IDPF, for example: `sles-15-sp4-sap-v20240208-x86-64`.

If you want to use the latest OS image in an [image family](https://docs.cloud.google.com/compute/docs/images#image_families), replace the `--source-image` flag with the `--source-image-family` flag and set its value to an image family that supports IDPF, for example: `--source-image-family=sles-15-sp4-sap`.

  * `SOURCE_IMAGE_PROJECT`: the name of the project that contains the source OS image or image family.

**Example**

To create a SUSE Linux Enterprise Server (SLES) OS image using the latest OS image from the Compute Engine `sles-15-sp5-sap` image family, run the following command:
        
        gcloud compute images create my-sles15sp5-metal-os \
          --source-image-family=sles-15-sp5-sap \
          --source-image-project=suse-sap-cloud \
          --guest-os-features=IDPF
        

For more information about when to use image families, see [Image family best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).




###  REST 

  1. Select an OS image or image family that supports IDPF For more information, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#networking).

  2. Using the OS image or image family selected in the previous step, create an OS image and tag this OS image with `IDPF`. To create the OS image, use the [`images.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/insert).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images
         {
          "name":"IMAGE_NAME",
          "sourceImage":"SOURCE_IMAGE_URI",
          "guestOsFeatures":[
           {
              "type":"IDPF"
            }
          ]
         }
         

Replace the following:

     * `IMAGE_NAME`: a name for the custom image that you are creating.
     * `SOURCE_IMAGE_URI`: the URI for the specific OS image or image family that you want to use.

For example:

       * Specific OS image: `"sourceImage": "projects/suse-sap-cloud/global/images/sles-15-sp5-sap-v20240427-x86-64"`
       * Image family: `"sourceImage": "projects/suse-sap-cloud/global/images/family/sles-15-sp5-sap"`.

When you specify an image family, Compute Engine creates a VM from the most recent, non-deprecated OS image in that family. For more information about when to use image families, see [Image family best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).




## Create a bare metal instance with IDPF support

You can create a bare metal instance using one of the [public OS images](https://docs.cloud.google.com/compute/docs/images/os-details#networking) that supports IDPF or using a custom OS image that you created using the steps in Create a custom OS image that supports IDPF.

### Create a bare metal instance using a public OS image

To create a bare metal instance using a public OS image that supports IDPF, follow the instructions at [Create a bare metal instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#baremetal).

### Create a bare metal instance using a custom OS image

If you aren't using a public OS image that supports IDPF, you must first create a custom OS image that supports IDPF. You then use that custom OS image to create a bare metal instance by using the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute) or [REST](https://docs.cloud.google.com/compute/docs/reference/rest/v1).

###  gcloud 

  1. Create the bare metal instance by using the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create). For the boot disk image, specify the custom OS image that you created earlier. For the network interface, set the value of the `nic-type` flag to `IDPF`.
         
         gcloud compute instances create INSTANCE_NAME \
             --zone=ZONE \
             --image=IMAGE_NAME \
             --image-project=YOUR_IMAGE_PROJECT \
             --network-interface=nic-type=IDPF
         

Replace the following:

     * `INSTANCE_NAME`: a name for the new instance.
     * `ZONE`: the zone to create the instance in.
     * `IMAGE_NAME`: the custom OS image that was created previously.
     * `YOUR_IMAGE_PROJECT`: the name of the project that contains the custom OS image.
  2. Optional: Verify that Compute Engine created the instance and that the `nicType` is set to `IDPF`.
         
         gcloud compute instances describe INSTANCE_NAME \
            --zone=ZONE
         

Replace the following:

     * `INSTANCE_NAME`: the name of the instance.
     * `ZONE`: the zone that you created the instance in.

**Example**

To create a bare metal instance in zone `eu-west4-b` using a customized SLES 15 SP5 for SAP OS image named `my-sles15sp5-metal-os` that's in project `my-project-12345`, run the following command:
    
    gcloud compute instances create test-x4-metal-custom-os \
        --zone=eu-west4-b \
        --machine-type=x4-1440-24t-metal \
        --image=my-sles15sp5-metal-os \
        --image-project=my-project-12345 \
        --network-interface=nic-type=IDPF
    

**Things to consider**

The `--network-interface` flag has sub-level flags such as the following:

     * `--address`: Assign an IP address to the instance
     * `--network`: The network the interface is to be a part of
     * `--network-tier`: The network tier of the interface
     * `--subnet`: The subnet that the interface is to be part of. If `--network` is also specified, the subnet must be a part of the specified network.
     * `--private-network-ip`: Specify the RFC 1918 IP to assign to the instance.

For a full list see, the [`--network-interface` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--network-interface).

**Note:** When enabling IDPF, if you need to set any of these sub-level flags, you must specify these as a comma separated list to the `--network-interface` flag. For example, `-network-interface=subnet=SUBNET_NAME,nic-type=IDPF`.



###  REST 

Create the bare metal instance by using the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).

  * For the boot disk image, specify the custom OS image that you created earlier.
  * For the network interface, set the value of the `nicType` field to `IDPF`.


    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
      "name":"INSTANCE_NAME",
      "networkInterfaces":[
        {
          "nicType":"IDPF",
          "network":"NETWORK",
          "subnetwork":"SUBNET_NAME"
        }
      ],
      "disks":[
        {
          "initializeParams":{
            "sourceImage":"projects/YOUR_IMAGE_PROJECT/global/images/IMAGE_NAME"
          },
          "boot":true
        }
      ]
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project to create the instance in.
  * `ZONE`: the zone to create the instance in.
  * `INSTANCE_NAME`: a name for the new instance.
  * `NETWORK`: the URL of the network resource for this instance. If neither the network nor the subnetwork is specified, the default network `global/networks/default` is used.
  * `SUBNET_NAME`: name of the subnet. The network is inferred from the specified subnet. This is an optional field.
  * `YOUR_IMAGE_PROJECT`: the name of your project that contains the OS image.
  * `IMAGE_NAME`: the name of the custom OS image that was created in the previous step.



## Verify that IDPF is enabled

You can use the `lshw` tool to extract detailed information about the hardware configuration of the bare metal instance.

To install the `lshw` tool on your Linux instance, open an SSH connection to the guest OS, and then run the following command:
    
    
    sudo apt-get install lshw -y
    

To determine whether the instance is using the IDPF network interface, run the following command:
    
    
    sudo lshw -class network
    

The following shows an example of the output:
    
    
    *-network
           description: Ethernet interface
           product: Intel Corporation
           vendor: Intel Corporation
           physical id: 0
           bus info: pci@0000:05:00.0
           logical name: enp5s0f0
           version: 11
           serial: 42:01:0a:96:00:02
           width: 64 bits
           clock: 33MHz
           capabilities: pm msi msix pciexpress bus_master cap_list ethernet physical
           configuration: autonegotiation=off broadcast=yes **driver=idpf driverversion=6.5.0-1023-gcp** duplex=full ip=10.150.0.2 latency=0 link=yes multicast=yes
           resources: iomemory:21ff0-21fef iomemory:21ff0-21fef irq:16 memory:21ffe0000000-21ffefffffff memory:21fff2000000-21fff203ffff
    

## What's next

  * Learn more about [IDPF](https://www.oasis-open.org/2023/01/11/creating-a-leading-peripheral-component-interconnect-express-pcie-based-ethernet-host-interface-standard-infrastructure-data-plane-function-idpf/).
  * Learn how to [connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).
  * Learn about [jumbo frames](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu).
  * Learn how to [change the MTU setting of a VPC network](https://docs.cloud.google.com/vpc/docs/change-mtu-vpc-network).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
