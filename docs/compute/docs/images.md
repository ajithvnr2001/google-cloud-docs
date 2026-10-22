---
url: https://docs.cloud.google.com/compute/docs/images/
title: OS images \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:15.402157+00:00
---

# OS images  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  OS images Stay organized with collections  Save and categorize content based on your preferences. 

Use operating system (OS) images to create boot disks for your Compute Engine virtual machine (VM) or bare metal instances. You can use the following types of OS images when you create compute instances and boot disks:

  * **Public OS images** are provided and maintained by Google, open source communities, and third-party vendors. By default, all Google Cloud projects have access to these OS images and can use them to [create a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-public-image).
  * **Custom OS images** are available only to your Google Cloud project. You can [create a custom OS image](https://docs.cloud.google.com/compute/docs/images/create-custom) from boot disks and other images. Then, use the custom OS image to create a Compute Engine instance.



Some OS images are also capable of running [containers on Compute Engine](https://docs.cloud.google.com/compute/docs/containers).

## Public OS images

Compute Engine offers many preconfigured public OS images that have compatible Linux or Windows operating systems. Use these OS images to [create and start instances](https://docs.cloud.google.com/compute/docs/instances/create-start-instance). Compute Engine uses your selected image to create a persistent boot disk for each compute instance. By default, the boot disk for an instance is the same size as the image that you selected. If your compute instance requires a larger boot disk than the image size, then [resize the boot disk](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk).

### List of public OS images available on Compute Engine

To see a full list of public OS images with each image's name, size, and version number, you can use the Google Cloud console or the Google Cloud CLI. Compute Engine updates public OS images regularly, or when a patch for a critical impact common vulnerability and exposure (CVE) is available.

Compute Engine provides 64-bit versions of these public OS images. For more information about each OS, including how each OS is customized to run on Compute Engine, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).

###  Console 

  1. In the Google Cloud console, go to the **Images** page.

[Go to Images](https://console.cloud.google.com/compute/images)

By default, the Google Cloud console lists all OS images available in the [Compute Engine images](https://docs.cloud.google.com/compute/docs/images/os-details), [Deep Learning VM Images](https://docs.cloud.google.com/deep-learning-vm/docs/images), and [HPC VM image](https://docs.cloud.google.com/compute/docs/images/workload/hpc-vm-images) projects. 




###  gcloud 
    
    
    gcloud compute images list

By default, the gcloud CLI lists all OS images available in the [Compute Engine images](https://docs.cloud.google.com/compute/docs/images/os-details) projects.

**Note:** Use of the operating systems on these images is subject to additional licensing terms. For more information about operating system licensing in Google Cloud, see [Terms of Service](https://cloud.google.com/terms/service-terms) and the documentation provided by the following operating system vendors.

## Custom OS images

A custom OS image is a boot disk image that you own and control access to. Use custom OS images for the following tasks:

  * [Import a virtual disk](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) to Compute Engine from your on-premises environment or from compute instances that are running on your local workstation or on another cloud platform. You can [manually import boot disk images](https://docs.cloud.google.com/compute/docs/import/import-existing-image) to Compute Engine, but only one disk at a time.

**Note:** If you are planning to migrate several VM instances to Compute Engine, consider using the [VM migration service](https://docs.cloud.google.com/compute/docs/import).
  * [Create custom images](https://docs.cloud.google.com/compute/docs/images/create-custom) from the boot disks of your existing Compute Engine instances. Then use that image to [create new boot disks](https://docs.cloud.google.com/compute/docs/disks/create-root-persistent-disks#creatingrootpdalone) for your compute instances. This process lets you create new instances that are preconfigured with the apps that you need without having to configure a public OS image from scratch.

  * Copy one image to another image by using either the [gcloud CLI](https://docs.cloud.google.com/compute/docs/gcloud-compute) or the [API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances). Use the same process that you use to [create an image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images), but specify another image as the image source. You can also create an image from a custom image in a different project.




## Guest operating system features

Some guest operating system features are available only on certain OS images. For example, [multiqueue SCSI](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface) is enabled only on some public OS images.

To enable these features on your custom OS images, specify one or more guest operating system features when you [create a custom OS image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features).

## OS image costs

[Premium OS images](https://docs.cloud.google.com/compute/disks-image-pricing#premiumimages), whether public or custom, incur licensing fees to run on Compute Engine. You have two options:

  * Attach an on-demand/pay-as-you-go (PAYG) license
  * Bring your own license (BYOL)/Bring your own subscription (BYOS)

For more information about licenses, see [License types and pricing](https://docs.cloud.google.com/compute/docs/licenses/about#license_types_and_pricing).




For custom OS images, you also incur an [image storage charge](https://docs.cloud.google.com/compute/disks-image-pricing#imagestorage) while you keep your custom OS image in your project.

## Image families

Image families help you manage images in your project by grouping related images together, so that you can roll forward and roll back between specific image versions. An image family always points to the latest version of an OS image that is not deprecated. Most [public OS images](https://docs.cloud.google.com/compute/docs/images/os-details) are grouped into an image family. For example, the `debian-13` image family in the `debian-cloud` project always points to the most recent Debian 13 image.

### Custom image families

If you regularly update your custom OS images with newer configurations and software, you can group those images into a custom image family. The image family always points to the most recent OS image in that family, so your instance templates and scripts can use that image without having to update references to a specific image version.

Also, because the image family never points to a deprecated image, you can roll the image family back to a previous OS image version by deprecating the most recent image in that family. Note that the rollback is possible only if the previous image version is not deprecated. For more information, see [Setting image versions in an image family](https://docs.cloud.google.com/compute/docs/images/set-version-custom).

For best practices recommendations when working with image families, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

## Partner supported operating systems

These are operating systems that you can run on Google Cloud, but the partner or distributor is responsible for ensuring that these operating systems work with Google Cloud features and that security updates are maintained. For issues specific to the partner supported operating systems, you must use either community resources or get enterprise-level support from the partner.

The following partner supported operating systems can run on Google Cloud.

### Oracle Linux

Oracle Linux is an operating system that is offered by Oracle. Oracle Linux images are available on Google Cloud provided by Oracle. You can also import Oracle Linux images to Google Cloud.

If you require support that is specific to the Oracle Linux operating system, you can either consult community resources, or get enterprise-level support directly from Oracle.

**Import Oracle Linux OS images**

To import an Oracle Linux OS image to Compute Engine, you can use the import tool available from Migrate to Virtual Machines. This tool ensures the imported OS images are set up correctly for working in a Google Cloud environment. For detailed instructions, see [Import virtual disk images](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/image_import). For a list of the Oracle Linux OS versions supported for import, see [Operating systems supported by partners](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/supported-os-versions#operating-systems-supported-by-partners). **Note:** Oracle Linux OS images don't incur licensing charges on Google Cloud.

## Community supported OS images

Community-supported OS images are not directly supported by Google Cloud. It is up to the project community to ensure that these OS images work with Google Cloud features and that security updates are maintained. Community-supported images are provided as-is by the project communities that build and maintain them.

**Note:** Community-supported OS images don't incur licensing charges on Google Cloud.

The following community supported images can run on Google Cloud.

### Fedora Cloud

Fedora Cloud is an operating system maintained by the [Fedora Cloud project](https://fedoraproject.org/cloud/). Fedora Cloud images are available in the `fedora-cloud` project. To list Fedora Cloud OS images, use the following `gcloud` command:
    
    
    gcloud compute images list --project fedora-cloud --no-standard-images

### FreeBSD

FreeBSD is an operating system maintained by the [FreeBSD project](https://www.freebsd.org/). FreeBSD images are available in the `freebsd-org-cloud-dev` project. To list FreeBSD OS images, use the following `gcloud` command:
    
    
    gcloud compute images list --project freebsd-org-cloud-dev --no-standard-images

gVNIC support for FreeBSD ([Preview](https://cloud.google.com/products/#product-launch-stages)) is available with release 14.0 and later. To use gVNIC with other releases, the driver can be [installed manually](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#manual-gvnic-setup).

To create a compute instance that uses gVNIC with a FreeBSD release earlier than 14.0, you must [create a custom OS image that supports gVNIC](https://docs.cloud.google.com/compute/docs/networking/using-gvnic#create-custom-image) and then use that OS image when creating the compute instance.

### openSUSE

[openSUSE](https://www.opensuse.org/) is a Linux-based operating system sponsored by SUSE. openSUSE images are available in the `opensuse-cloud` project. To list openSUSE OS images, use the following `gcloud` command:
    
    
    gcloud compute images list --project opensuse-cloud --no-standard-images

## TPU OS images

The following OS images are available for creating VMs that use TPUs:

TPU version | OS version | Kernel version | Image project | Image family  
---|---|---|---|---  
TPU7x (Ironwood) | `Ubuntu 24.04 LTS` | **6.17** | `ubuntu-os-accelerator-images` | `ubuntu-accel-2404-amd64-tpu-tpu7x`  
v6e (Trillium), v5p | `Ubuntu 22.04 LTS` | **6.8** | `ubuntu-os-accelerator-images` | `ubuntu-accel-2204-amd64-tpu-v5e-v5p-v6e`  
  
For more information, see [GA Ubuntu LTS versions](https://docs.cloud.google.com/compute/docs/images/os-details#ga_ubuntu_lts_versions).

## What's next

  * Learn about [workload-optimized images](https://docs.cloud.google.com/compute/docs/images/workload/overview-workload-images).
  * [View the source image](https://docs.cloud.google.com/compute/docs/instances/view-vm-image) for a compute instance.
  * Read [Image management best practices](https://docs.cloud.google.com/solutions/image-management-best-practices).
  * Learn about [Support and maintenance policy for OS images](https://docs.cloud.google.com/compute/docs/images/support-maintenance-policy).
  * [Create and start an instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).
  * Read about [Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances).
  * [Create a custom image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images).
  * [Build an image from scratch](https://docs.cloud.google.com/compute/docs/tutorials/building-images).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Compute Engine performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Compute Engine free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
