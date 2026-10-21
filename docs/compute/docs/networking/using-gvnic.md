---
url: https://docs.cloud.google.com/compute/docs/networking/using-gvnic/
title: Using Google Virtual NIC \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:14:32.380675+00:00
---

# Using Google Virtual NIC  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/networking/using-gvnic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Using Google Virtual NIC Stay organized with collections  Save and categorize content based on your preferences. 

Google Virtual NIC (gVNIC) is a virtual network interface designed specifically for Compute Engine. gVNIC is an alternative to the [virtIO-based ethernet driver](https://ozlabs.org/%7Erusty/virtio-spec/virtio-0.9.5.pdf).

As the next generation network interface which succeeds VirtIO, gVNIC replaces VirtIO-Net as the only supported network interface in Compute Engine for all new [machine types](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison) (Generation 3 and onwards). Newer machine series and networking features require gVNIC instead of VirtIO. Consuming gVNIC as the modern I/O interface with Compute Engine VMs offers the following advantages:

  * Provides better performance.
  * Improves consistency by reducing noisy neighbor problems.
  * Introduces new network capabilities beyond what VirtIO is capable of.



## Before you begin

  * If you use gVNIC with Windows Server or Windows client images, make sure the gVNIC driver uses GooGet package version `1.0.0@45` or later.
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




## When to use gVNIC

gVNIC is supported and recommended for all machine families and generations. Some generations support only gVNIC. Others require gVNIC use under special conditions. To identify the generation for your machine series, see [Compute Engine terminology](https://docs.cloud.google.com/compute/docs/machine-resource#vm_terminology).

gVNIC use by machine series generation is as follows:

  * Third generation and later machine series, excluding bare metal instances, support only gVNIC for the virtual network interface.
  * First or second generation machine series must use gVNIC for the virtual network interface for instances if they meet any of the following conditions:

    * The instance runs on the [Arm CPU platform](https://docs.cloud.google.com/compute/docs/cpu-platforms#arm_processors).
    * The instance is a [Confidential VM instance](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview).
    * The instance needs to achieve network speeds between 50 and 100 Gbps. This applies to instances that meet the following criteria:

      * Instances that support [per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration)
      * A2, G2, and N1 instances that support these [higher network bandwidths](https://docs.cloud.google.com/compute/docs/gpus/optimize-gpus#create-high-bandwidth-vm)



## Pricing

To see the latest prices for Tier_1 networking, refer to the [VM instances pricing page](https://docs.cloud.google.com/compute/vm-instance-pricing#section-19).

For a list of additional methods that can be used to find pricing information, see [Compute Engine pricing](https://cloud.google.com/compute/all-pricing).

## Operating system support

On Compute Engine, you can choose to use gVNIC on any supported public operating system (OS) images. You can manually install the gVNIC driver in these cases:

  * The OS image doesn't include the gVNIC driver
  * The OS image doesn't have the latest gVNIC driver version



For the supported operating systems, see the **Interfaces** tab for an [operating system](https://docs.cloud.google.com/compute/docs/images/os-details#networking). Also check the **Networking features** tab for networking feature support.

## Use on non-supported operating systems

For OS images that support gVNIC but don't include the latest version of the gVNIC driver, you can download the latest driver version from GitHub.

You can manually configure and install the latest version of the gVNIC driver on either Linux or Windows VMs.

After you update the operating system in your VM to use gVNIC, [create a custom OS image](https://docs.cloud.google.com/compute/docs/images/create-custom) based on that OS image. You can then use the custom OS image to create additional VMs that use gVNIC on that operating system. For more information about creating VMs using a custom OS image, see Create a custom OS image that supports gVNIC on this page.

Use the following procedures to manually configure and install the latest version of the gVNIC driver.

**Caution:** Before conducting a manual installation of the gVNIC driver, consult with your operating system distributor's out-of-tree (oot) support policy and tainted kernel support policy.

  * For Linux VMs, see [Linux kernel driver Compute Engine Virtual Ethernet](https://github.com/GoogleCloudPlatform/compute-virtual-ethernet-linux#manual-configuration).
  * For VMs running on FreeBSD, see [Compute Engine Virtual Ethernet FreeBSD driver](https://github.com/GoogleCloudPlatform/compute-virtual-ethernet-freebsd?tab=readme-ov-file#installation).
  * For Windows VMs, see Install or update the gVNIC driver on Windows.



### Install or update the gVNIC driver on Windows

On Windows VMs, the gVNIC driver is packaged and distributed using [GooGet](https://github.com/google/googet). All Google-provided Windows images are preconfigured with the GooGet package manager.

To install or update the gVNIC driver on a Windows VM, complete the following steps:

  1. Connect to your Windows VM.

  2. Open PowerShell or Command Prompt as an administrator.

  3. Check if the gVNIC driver package is already installed:
         
         googet installed
         

In the output, verify that the `google-compute-engine-driver-gvnic` package is listed.

  4. Based on the output, do one of the following:

     * **If the package isn't listed** , install the driver:
           
           googet install google-compute-engine-driver-gvnic
           

     * **If the package is listed** , update the driver to the latest version:
           
           googet update google-compute-engine-driver-gvnic
           

Alternatively, run `googet update` to update all installed packages on your Windows instance.

  5. Verify that the gVNIC driver is installed and active on your VM. For more information, see Verify that gVNIC is enabled.




For more information about the Windows gVNIC driver, or to build the driver from the source files, see [Windows driver for Compute Engine Virtual Ethernet](https://github.com/GoogleCloudPlatform/compute-virtual-ethernet-windows) on GitHub.

## Overview of using gVNIC with Compute Engine VMs

To create a VM that uses gVNIC, complete the following steps:

  1. Choose a [public OS image](https://docs.cloud.google.com/compute/docs/images#os-compute-support) that supports gVNIC, or create a custom OS image that is tagged to use gVNIC.
  2. Create a VM using the public or custom OS image. During the VM creation, configure the network interface to use gVNIC.
  3. Verify that gVNIC is enabled.



If you encounter any issues, see [Troubleshooting Google Virtual NIC](https://docs.cloud.google.com/compute/docs/troubleshooting/gvnic).

## Create a custom OS image that supports gVNIC

You can create the OS image using either the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute) or [REST](https://docs.cloud.google.com/compute/docs/reference/rest/v1). For detailed information and best practices for creating custom OS images, see [Create custom OS images](https://docs.cloud.google.com/compute/docs/images/create-custom).

###  gcloud 

  1. Select an OS image or image family that supports gVNIC. For more information, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#networking).

  2. Using the OS image or image family selected in the previous step, create a custom OS image and tag this OS image with `GVNIC`. To create the custom OS image, use the [`gcloud compute images create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/create). For example, the following command creates a custom OS image that supports gVNIC and that's based on a specific OS image.
         
         gcloud compute images create IMAGE_NAME \
             --source-image=SOURCE_IMAGE \
             --source-image-project=SOURCE_IMAGE_PROJECT \
             --guest-os-features=GVNIC
         

Replace the following:

     * `IMAGE_NAME`: the name of the image that you want to create
     * `SOURCE_IMAGE`: a specific OS image that supports gVNIC—for example: `rocky-linux-8-optimized-gcp-v20220719`

If you want to use the latest OS image in an [image family](https://docs.cloud.google.com/compute/docs/images#image_families), replace the `--source-image` flag with the `--source-image-family` flag and set its value to an image family that supports gVNIC. For example: `--source-image-family=rocky-linux-8-optimized-gcp`.

     * `SOURCE_IMAGE_PROJECT`: the name of the project that contains the source OS image or image family

**Example**

To create a Rocky Linux 8 Optimized for Google Cloud OS image using the latest OS image from the Compute Engine `rocky-linux-8-optimized-gcp` image family, run the following command:
    
    gcloud compute images create IMAGE_NAME \
        --source-image-family=rocky-linux-8-optimized-gcp \
        --source-image-project=rocky-linux-cloud \
        --guest-os-features=GVNIC
    

For more information about when to use image families, see [Image family best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).




###  REST 

  1. Select an OS image or image family that supports gVNIC For more information, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#networking).

  2. Using the OS image or image family selected in the previous step, create an OS image and tag this OS image with `GVNIC`. To create the OS image, use the [`images.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/insert).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images
         {
           "name":"IMAGE_NAME",
           "sourceImage":"SOURCE_IMAGE_URI",
           "guestOsFeatures":[
             {
               "type":"GVNIC"
             }
           ]
         }
         

Replace the following:

     * `PROJECT_ID`: the ID of the project in which to create the new image
     * `IMAGE_NAME`: a name for the custom image
     * `SOURCE_IMAGE_URI`: the URI for the specific OS image or image family that you want to use

For example:

       * Specific OS image: `"sourceImage": "projects/rocky-linux-cloud/global/images/rocky-linux-8-optimized-gcp-v20220719"`
       * Image family: `"sourceImage": "projects/rocky-linux-cloud/global/images/family/rocky-linux-8-optimized-gcp"`

When you specify an image family, Compute Engine creates a VM from the most recent, non-deprecated OS image in that family. For more information about when to use image families, see [Image family best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).




## Create a VM with gVNIC support

You can create a VM using one of the [supported public OS images](https://docs.cloud.google.com/compute/docs/images/os-details#networking) or using a custom OS image you created using the steps in Create a custom OS image that supports gVNIC.

Optionally, you can [enable DPDK](https://docs.cloud.google.com/compute/docs/networking/use-dpdk) on the VM for faster network packet processing, low latency, and consistent performance.

For VMs that support multiple network interfaces (NICs), you can have NICs of different types attached to the VM because interface support is configured per NIC. While this is supported, we don't recommend this setup. For VMs that support multiple NICs, ensure that you specify `nic-type=GVNIC` for each network interface when creating the VM.

### Create a VM using a public OS image

To create a VM using a public OS image that supports gVNIC, follow the instructions at [Creating VMs and containers with high-bandwidth configuration](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration).

### Create a VM using a custom OS image

If you aren't using a public OS image that supports gVNIC, you must first create a custom OS image that supports gVNIC. You then use that custom OS image to create a VM by using the [Google Cloud console](https://docs.cloud.google.com/compute/docs/console), [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), or [REST](https://docs.cloud.google.com/compute/docs/reference/rest/v1).

###  Console 

  1. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  2. Enter the **Name** of your VM instance.

  3. Select the **Zone** to create your VM in.

  4. In the **Boot disk** section, click **Change**.

  5. In the **Boot disk** panel, on the **Custom images** tab, complete the following:

     1. Choose the **Source project** that contains the OS image that you created previously.
     2. Select the image from the **Image** drop-down.
     3. Click **Select**.
  6. To set gVNIC as the network interface, expand the **Advanced options** section, and then do the following:

     1. Expand the **Networking** section.
     2. For **Network interface card** , select `gVNIC`.
  7. Make additional VM customizations as needed.

  8. Click **Create** to create the VM instance.




###  gcloud 

  1. Create the VM by using the [`gcloud compute instances create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create). For the boot disk, specify the custom OS image that you created earlier. For the network interface, set the value of the `nic-type` flag to `GVNIC`.
         
         gcloud compute instances create VM_NAME \
             --zone=ZONE \
             --machine-type=MACHINE_TYPE \
             --image=IMAGE_NAME \
             --image-project=YOUR_IMAGE_PROJECT \
             --network-interface=nic-type=GVNIC
         

Replace the following:

     * `VM_NAME`: the name of the new VM.
     * `ZONE`: the zone to create the VM in.
     * `MACHINE_TYPE`: the machine type to use when creating the VM instance. If you don't specify a machine type, the default is `n1-standard-1`.
     * `IMAGE_NAME`: the OS image that was created in the previous step.
     * `YOUR_IMAGE_PROJECT`: the name of your project that contains the OS image.
  2. Optional: Verify that Compute Engine created the VM and that the `nicType` is set to `GVNIC`.
         
         gcloud compute instances describe VM_NAME \
            --zone=ZONE
         

Replace the following:

     * `VM_NAME`: the name of the VM.
     * `ZONE`: the zone that you created the VM in.

**Example**

To create a Rocky Linux 8 VM with an `n1-standard-1` machine type in zone `us-west1-b` using an OS image named `my-gvnic-rocky8` that's in project `my-project-12345`, run the following command:
    
    gcloud compute instances create my-rocky-linux-vm \
        --zone=us-west1-b \
        --image=my-gvnic-rocky8 \
        --image-project=my-project-12345 \
        --network-interface=nic-type=GVNIC
    

**Things to consider**

The `--network-interface` flag has sub-level flags such as the following:

     * `--address`: Assign an IP address to the VM
     * `--network`: The network the interface will be a part of
     * `--network-tier`: The network tier of the interface
     * `--subnet`: The subnet that the interface will be part of. If `--network` is also specified, the subnet must be a part of the specified network.
     * `--private-network-ip`: Specify the RFC 1918 IP to assign to the VM.

For a full list see, the [`--network-interface` flag](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/create#--network-interface).

**Note:** When enabling gVNIC, if you need to set any of these sub-level flags, you must specify these as a comma separated list to the `--network-interface` flag. For example, `-network-interface=subnet=SUBNET_NAME,nic-type=GVNIC`.



###  REST 

Create the VM by using the [`instances.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/insert).

  * For the boot disk, specify the custom OS image that you created earlier.
  * For the network interface, set the value of the `nicType` field to `GVNIC`.


    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances
    {
      "name":"VM_NAME",
      "networkInterfaces":[
        {
          "network":"NETWORK",
          "nicType":"GVNIC",
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

  * `PROJECT_ID`: the ID of the project to create the VM in.
  * `ZONE`: the zone to create the VM in.
  * `VM_NAME`: the name of the new VM.
  * `NETWORK`: the URL of the network resource for this VM. If neither the network nor the subnetwork is specified, the default network `global/networks/default` is used.
  * `SUBNET_NAME`: name of the subnet. The network is inferred from the specified subnet. This is an optional field.
  * `YOUR_IMAGE_PROJECT`: the name of your project that contains the OS image.
  * `IMAGE_NAME`: the OS image that was created in the previous step.



## Verify that gVNIC is enabled

###  Linux 

You can use the `lshw` tool to extract detailed information about the hardware configuration of the virtual machine.

To install the `lshw` tool on your Linux VM instance, open a SSH connection to the VM, and then run the following command:
    
    
    sudo apt-get install lshw -y
    

To determine if the VM is using the gVNIC network interface, run the following command:
    
    
    sudo lshw -class network
    

The output resembles the following:
    
    
    *-network
       description: Ethernet interface
       product: Compute Engine Virtual Ethernet [gVNIC]
       vendor: Google, Inc.
       physical id: 3
       bus info: pci@0000:00:03.0
       logical name: ens3
       version: 00
       serial: 42:01:0a:80:00:6f
       width: 32 bits
       clock: 33MHz
       capabilities: msix bus_master cap_list ethernet physical
       configuration: autonegotiation=off broadcast=yes driver=gve driverversion=1.0.0
        duplex=full ip=10.128.0.111 latency=0 link=yes multicast=yes port=twisted pair
       resources: irq:11 memory:c0203000-c0203fff memory:c0200000-c02000ff memory:c0100000-c01fffff
    

###  Windows 

To verify that the gVNIC driver is installed and active on your Windows VM, use PowerShell, Command Prompt, or Device Manager:

  * **PowerShell** : In a PowerShell session as an administrator, run the following command:
        
        Get-WindowsDriver -Online -All | Where-Object {$_.ProviderName -eq 'Google' -and $_.OriginalFileName -like '*gvnic*'}
        

  * **Command Prompt** : In a Command Prompt session as an administrator, run the following command:
        
        dism /online /get-drivers | findstr gvnic
        

  * **Device Manager** :

    1. On your Windows VM instance, open **Device Manager**.
    2. Under **Network adapters** , verify that **Google Ethernet Adapter** is listed.



## Troubleshooting

To troubleshoot gVNIC, see [Troubleshooting Google Virtual NIC](https://docs.cloud.google.com/compute/docs/troubleshooting/gvnic).

## What's next

  * [Connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).
  * [Add persistent disks](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk) to your new instance.
  * [Configure per VM Tier_1 networking performance](https://docs.cloud.google.com/compute/docs/networking/configure-vm-with-high-bandwidth-configuration).
  * [Change the MTU setting of a VPC network](https://docs.cloud.google.com/vpc/docs/change-mtu-vpc-network).
  * Learn about [jumbo frames](https://docs.cloud.google.com/compute/docs/network-bandwidth#jumbo-mtu).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
