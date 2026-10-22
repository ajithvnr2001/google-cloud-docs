---
url: https://docs.cloud.google.com/compute/docs/networking/using-irdma/
title: Using the IRDMA Cloud RDMA driver \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:40.795681+00:00
---

# Using the IRDMA Cloud RDMA driver  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/networking/using-irdma/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Using the IRDMA Cloud RDMA driver Stay organized with collections  Save and categorize content based on your preferences. 

Cloud RDMA enables low-latency reliable messaging capabilities by using the IRDMA RDMA driver. This driver supports Remote Direct Memory Access (RDMA) between Compute Engine instances. RDMA transfers data between remote machines and local memory through the network interface without using host CPU or intermediate host buffers.

Cloud RDMA capable instances require at least two virtual network interfaces (vNICs):

  * A vNIC for Cloud RDMA communication that uses the IDPF network driver and the IRDMA RDMA driver. This vNIC can't connect to the internet. An instance can have only one vNIC that uses Cloud RDMA.
  * A vNIC for normal network traffic. This vNIC is fully connected to the Google Cloud network and can connect to the internet. This vNIC uses the gVNIC network driver. You can add up to eight additional gVNIC network interfaces, for a total of 10 vNICs per instance.



The IRDMA driver is supported with [H4D instances](https://docs.cloud.google.com/compute/docs/compute-optimized-machines#h4d_series) and [Z4M instances](https://docs.cloud.google.com/compute/docs/storage-optimized-machines#z4m_series).

When configuring a vNIC that uses the IRDMA driver, you must specify a VPC network that was created by using the [Falcon RDMA network profile](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles).

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




## Operating system support

Google recommends using [Advanced Compute Images](https://docs.cloud.google.com/compute/docs/images/workload/aci-images) or the [HPC VM image](https://docs.cloud.google.com/compute/docs/instances/create-hpc-vm), which comes with Cloud RDMA drivers pre-installed.

The IRDMA RDMA driver is supported with the following public OS images that are provided for Google Cloud:

  * Container-Optimized OS 117 LTS or later
  * Rocky Linux 8 optimized for Google Cloud and later optimized for Google Cloud versions



## Overview of using Cloud RDMA with Compute Engine instances

To create a compute instance that uses Cloud RDMA, you must have at least one regular VPC network and one [Falcon VPC network](https://docs.cloud.google.com/vpc/docs/rdma-network-profiles). The Falcon VPC network uses the Falcon RDMA network profile to enable Cloud RDMA traffic between H4D instances. This network is separate from the regular VPC network that carries non-RDMA traffic to other Google Cloud services or the internet.

The tasks to complete to create a compute instance that uses Cloud RDMA are as follows:

  1. Choose a [public OS image](https://docs.cloud.google.com/compute/docs/images#os-compute-support) that supports Cloud RDMA, or create a custom OS image that is tagged to use IRDMA.
  2. Identify or create at least two VPC networks:

     * A regular VPC network for the traffic that goes through the gVNIC network interface
     * A Falcon VPC network for the Cloud RDMA traffic
  3. Create a compute instance by using the public OS image or a custom OS image. During the instance creation, configure at least two network interfaces: one that uses the gVNIC network driver and one that uses the IRDMA RDMA driver.

  4. Verify that Cloud RDMA is enabled.




## Add the IRDMA driver to an OS image

To use an OS image that doesn't have the IRDMA driver installed by default, complete the following steps:

  1. Create a compute instance that uses the OS image that you want to use with Cloud RDMA.

  2. Connect to the compute instance that you created.

  3. If you aren't using an OS image that is optimized for Google Cloud, then add the CIQ repository by using one of the following options:

     * Recommended: Install the CIQ RPM package directly to configure the CIQ repository:
           
           sudo dnf install -y https://depot.ciq.com/public/files/gce-accelerator/irdma-kernel-modules-el8-x86_64/irdma-repos.rpm
           

     * Alternatively, update the YUM repositories directly:
           
           sudo tee /etc/yum.repos.d/irdma-kernel-modules.repo > /dev/null << 'EOF'
           [irdma-kernel-modules]
           name = irdma kernel modules for EL $releasever ($basearch)
           baseurl = https://depot.ciq.com/public/files/gce-accelerator/irdma-kernel-modules-el$releasever-$basearch
           metadata_expire = 5m
           priority = -1
           repo_gpgcheck = false
           gpgcheck = false
           enabled = true
           skip_if_unavailable = true
           
           [irdma-kernel-modules-source]
           name = irdma kernel modules for EL $releasever (source)
           baseurl = https://depot.ciq.com/public/files/gce-accelerator/irdma-kernel-modules-el$releasever-source
           metadata_expire = 5m
           priority = -1
           repo_gpgcheck = false
           gpgcheck = false
           enabled = false
           skip_if_unavailable = true
           
           [irdma-kernel-modules-testing]
           name = irdma kernel modules for EL $releasever ($basearch) - testing
           baseurl = https://depot.ciq.com/public/files/gce-accelerator/irdma-kernel-modules-testing-el$releasever-$basearch
           metadata_expire = 5m
           priority = -1
           repo_gpgcheck = false
           gpgcheck = false
           enabled = false
           skip_if_unavailable = true
           
           [irdma-kernel-modules-testing-source]
           name = irdma kernel modules for EL $releasever (source) - testing
           baseurl = https://depot.ciq.com/public/files/gce-accelerator/irdma-kernel-modules-testing-el$releasever-source
           metadata_expire = 5m
           priority = -1
           repo_gpgcheck = false
           gpgcheck = false
           enabled = false
           skip_if_unavailable = true
           EOF
           

  4. Install the `kmod-idpf-irdma` driver package, which includes the IDPF and IRDMA drivers:
         
         sudo dnf install kmod-idpf-irdma
         

The CIQ package requires specific kernel versions, which can affect the installation in the following ways:

     * If your kernel version is older than the required version, then installing the package automatically upgrades your kernel and other system packages as a dependency.
     * If your kernel version is newer than the version that is supported by the CIQ repository, then the installation might fail. In this case, use an OS image that is optimized for Google Cloud, which uses a supported kernel version.
  5. Verify that the `kmod-idpf-irdma` package is installed:
         
         sudo dnf list --installed
         

The output includes an entry similar to the following:
         
         kmod-idpf-irdma.ARCHITECTURE VERSION@REPO_NAME

  6. Install the user space packages:
         
         sudo dnf install -y \
             libibverbs libibverbs-devel libibverbs-utils \
             librdmacm librdmacm-devel librdmacm-utils \
             infiniband-diags
         

The `librdmacm-utils` and `libibverbs-utils` packages install supplementary utilities to check RDMA functionality, such as [`rping`](https://man7.org/linux/man-pages/man1/rping.1.html) and [`ibv_devinfo`](https://man7.org/linux/man-pages/man1/ibv_devinfo.1.html).

  7. Recommended: After you update the operating system in your compute instance to use IRDMA, create a custom image based on that OS image. You can then use the custom image to create additional compute instances that use IRDMA on that OS.

Follow the instructions in [Create the image](https://docs.cloud.google.com/compute/docs/images/create-custom#create_image) to create a custom image by using the boot disk of the instance that you created in the first step.




## Create a custom OS image from a public OS image that supports Cloud RDMA

You can create the OS image by using either the [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute) or [REST](https://docs.cloud.google.com/compute/docs/reference/rest/v1). For detailed information and best practices for creating custom OS images, see [Create custom OS images](https://docs.cloud.google.com/compute/docs/images/create-custom).

###  gcloud 

  1. Select an OS image or image family that supports the IRDMA driver and interface. For more information, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#networking) and select the **Interfaces** tab.

  2. Using the OS image or image family that you selected in the previous step, create a custom OS image. To create the custom OS image, use the [`gcloud compute images create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/create). For example, the following command creates a custom OS image that supports the IRDMA driver and is based on a specific OS image.
         
         gcloud compute images create IMAGE_NAME \
             --source-image=SOURCE_IMAGE \
             --source-image-project=SOURCE_IMAGE_PROJECT
         

Replace the following:

     * `IMAGE_NAME`: the name of the image that you want to create
     * `SOURCE_IMAGE`: a specific OS image that supports the IRDMA driver—for example: `hpc-rocky-linux-8-v20250721`

If you want to use the latest OS image in an [image family](https://docs.cloud.google.com/compute/docs/images#image_families), then replace the `--source-image` flag with the `--source-image-family` flag and set its value to an image family that supports the IRDMA driver. For example: `--source-image-family=hpc-rocky-linux-8`.

     * `SOURCE_IMAGE_PROJECT`: the name of the project that contains the source OS image or image family

For more information about when to use image families, see [Image family best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).




###  REST 

  1. Select an OS image or image family that supports the IRDMA network interface. For more information, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details#networking).

  2. Using the OS image or image family that you selected in the previous step, create an OS image by using the [`images.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/images/insert).
         
         POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/images
         {
           "name":"IMAGE_NAME",
           "sourceImage":"SOURCE_IMAGE_URI"
         }
         

Replace the following:

     * `PROJECT_ID`: the ID of the project in which to create the new image
     * `IMAGE_NAME`: a name for the custom image
     * `SOURCE_IMAGE_URI`: the URI for the specific OS image or image family that you want to use

For example:

       * Specific OS image: `"sourceImage": "projects/rocky-linux-cloud/global/images/hpc-rocky-linux-8-v20250721"`
       * Image family: `"sourceImage": "projects/rocky-linux-cloud/global/images/family/hpc-rocky-linux-8"`

When you specify an image family, Compute Engine creates a VM from the most recent, non-deprecated OS image in that family. For more information about when to use image families, see [Image family best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).




## Create a VM with IRDMA driver support

You can create a VM by using one of the [supported public OS images](https://docs.cloud.google.com/compute/docs/images/os-details#networking) or by using a custom OS image that you created by using the steps in Create a custom OS image that supports IRDMA.

To use Cloud RDMA with your instance, you must configure multiple network interfaces (NICs) for the instance. One NIC must use the gVNIC driver (specify `nic-type=GVNIC`) and another NIC must use the IRDMA driver (specify `nic-type=IRDMA`).

### Create a VM using a public OS image

To create VMs by using Advanced Compute Images, the HPC VM image, or a public OS image that supports Cloud RDMA, follow the instructions on the following pages:

  * To create an on-demand instance, see [Create an instance that uses Cloud RDMA](https://docs.cloud.google.com/compute/docs/instances/create-vm-with-rdma).
  * To create Cloud RDMA-enabled instances in bulk, see [Bulk create HPC-optimized instances that use Cloud RDMA](https://docs.cloud.google.com/compute/docs/hpc/bulk-create-hpc-vms).
  * To use Slurm to create a cluster of Cloud RDMA-enabled instances, see [Create an Cloud RDMA-enabled HPC Slurm cluster with H4D instances](https://docs.cloud.google.com/cluster-toolkit/docs/quickstarts/create-a-slurm-cluster-h4d).
  * To create a MIG, see [Create a HPC MIG with H4D machine series](https://docs.cloud.google.com/compute/docs/hpc/create-mig-hpc-dense).



### Create a VM using a custom OS image

If you created a custom OS image that supports Cloud RDMA, then you can use that custom OS image to create a VM by using the [Google Cloud console](https://docs.cloud.google.com/compute/docs/console), [Google Cloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute), or [REST](https://docs.cloud.google.com/compute/docs/reference/rest/v1).

For instructions on how to create an instance by using a custom image, see [Create an instance from a custom image](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-custom-image).

## Verify that Cloud RDMA is enabled

After the VM is deployed, run the following performance bandwidth test to ensure that you are running on a healthy Cloud RDMA-enabled VM instance.
    
    
    ib_send_bw -aF & # start the server
    ib_send_bw -aF $(hostname) # start the client (can be done on the same machine)
    

The reported single-connection bandwidth `BW average [MB/s]` should reach at least 11,000 MBps for rows higher than 4096 B. Smaller values are expected for lower message sizes.

## What's next

  * [Connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance)
  * [Change the MTU setting of a VPC network](https://docs.cloud.google.com/vpc/docs/change-mtu-vpc-network)
  * [Overview of HPC cluster creation](https://docs.cloud.google.com/compute/docs/hpc/overview-hpc-clusters)
  * [Set up and scale MPI applications on H4D VMs with Cloud RDMA](https://docs.cloud.google.com/cluster-toolkit/docs/setup/configure-mpi-application)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
