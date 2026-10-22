---
url: https://docs.cloud.google.com/compute/docs/images/image-management-best-practices/
title: Image management best practices \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:35.889237+00:00
---

# Image management best practices  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/images/image-management-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Image management best practices Stay organized with collections  Save and categorize content based on your preferences. 

This solution provides in-depth guidance on how to manage Compute Engine images. Images provide the base operating environment for applications that run in Compute Engine, and they are critical to ensuring your application deploys and scales quickly and reliably. You can also use images to archive application versions for disaster recovery or rollback scenarios.

## Understanding images

An [image](https://docs.cloud.google.com/compute/docs/images) in Compute Engine is a cloud resource that provides a reference to an immutable disk. That disk representation is then encapsulated using a few data formats.

![Understanding images.](https://docs.cloud.google.com/static/solutions/images/understanding-images.svg)

An image is a bundle of the raw bytes used to create a prepopulated hard disk. Written on any formatted disk is a partition table that points to one or more partitions that contain data. For an image to be bootable, it must contain the following:

  * A partition table: either a [master boot record](https://wikipedia.org/wiki/Master_boot_record) or [GUID partition table](https://wikipedia.org/wiki/GUID_Partition_Table)
  * A bootable partition



For a disk to be imported as a Compute Engine image, the disk's bytes must be written to a file named `disk.raw`.

After the complete sequence of bytes from the disk are written to the file, the file is archived using the [tar format](http://www.gnu.org/software/tar/manual/html_node/Standard.html) and then compressed using the GZIP format. You can then upload the resulting `*.tar.gz` file to Cloud Storage and register it as an image in Compute Engine, as shown in the preceding diagram. After you register an image, you can use it to create exact replicas of the original disk in any region of Google Cloud. The newly registered images are often used as boot volumes for Compute Engine instances.

For a more basic introduction to these Compute Engine terms, see [Virtual machine instances](https://docs.cloud.google.com/compute/docs/instances) and [Images](https://docs.cloud.google.com/compute/docs/images) in the documentation.

## Choosing a boot image

The first step in using Compute Engine is to choose the image you want as the operating system for your virtual machine (VM) instance. You can use [public images supplied by Google Cloud](https://docs.cloud.google.com/compute/docs/images#os-compute-support), which are updated on a regular basis. Google Cloud provides a variety of operating systems, including Debian, Ubuntu, and CentOS, for your use at no extra cost. Some operating systems, such as Red Hat Enterprise Linux and Microsoft Windows, are premium images, which incur additional fees for every hour that the instances run.

For more information on a particular image, such as automatic update policies, security patching, and support channels, see the [Operating system details](https://docs.cloud.google.com/compute/docs/images#os-details) section of the product documentation.

For added security, you can also use the [Trusted image feature](https://docs.cloud.google.com/compute/docs/images/restricting-image-access) to define an organization policy that restricts images in specific public image projects from being used in the creation of boot images.

![Boot image.](https://docs.cloud.google.com/static/solutions/images/choosing-boot-image.svg)

You can use the Google Cloud public images to boot a Compute Engine instance, after which you can customize the instance to run your application.

One approach to configuring your instance is to use the [startup script](https://docs.cloud.google.com/compute/docs/startupscript) to run the commands that deploy your application as it boots. Keep in mind that this script runs every time the instance boots, so you must make the script idempotent to avoid ending up in an inconsistent or partially configured state. If your instances are part of a managed instance group, you can use the Instance Group Updater to restart or rebuild your instances, which reruns your startup script. A common practice is to use the startup script to run a configuration management tool such as Chef or Ansible.

## Creating customized images

While configuring an instance's startup script is a viable way to provision your infrastructure, a more efficient method is to create a new custom image with your configuration incorporated into the public image. You can customize images in several ways:

  * Manual
  * Automated
  * Import



The process of creating a custom image is called _baking_.

Baking your images has the following benefits:

  * Shorter time from boot to application readiness.
  * Enhanced reliability for application deployments.
  * Easier rollback to previous versions.
  * Fewer dependencies on external services during application bootstrap.
  * Scaling up creates instances that contain identical software versions.



### Manual baking

You can create a simple custom image by creating a new VM instance from a [public image](https://docs.cloud.google.com/compute/docs/images#os-compute-support), configuring the instance with the applications and settings that you want, and then creating a custom image from that instance. Use this method if you can configure your images from scratch manually rather than using automated baking or importing existing images.

You can create a simple custom image using the following steps:

  1. [Create an instance from a public image](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#publicimage).
  2. [Connect to the instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance).
  3. Customize the instance for your needs.
  4. [Stop the instance](https://docs.cloud.google.com/compute/docs/instances/stopping-or-deleting-an-instance#stop_an_instance).
  5. [Create a custom image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#creating_a_custom_image) from the boot disk of that instance. This process requires you to delete the instance but keep the boot disk.



### Automated baking

Manual baking is an easy way to start if you have a small number of images, but large numbers of images become difficult to audit and manage. [Packer](https://packer.io) is an open source tool for making image creation more reproducible, auditable, configurable, and reliable. You can also use Packer as part of a Spinnaker pipeline to produce images that are deployed to clusters of instances.

### Importing existing images

You can import boot disk images from their existing infrastructure to Compute Engine by using the [virtual disk import tool](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks), which automates the image import process. For Linux machines, here's an [in-depth guide for manually migrating RAW disk images, Amazon Machine Images (AMI) and VirtualBox images](https://docs.cloud.google.com/compute/docs/images/import-existing-image).

Another option for importing your existing images is to use [Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/virtual-machines).

Migrate to Virtual Machines is a tool chain and service that facilitates the migration of machines from one platform to another with minimal downtime using continuous block-level replication. You can migrate your machines to Compute Engine and then use manual baking to create images.

### Encrypting images

All disks in Compute Engine are encrypted by default using Google's encryption keys. Images built from disks are also encrypted. Alternatively, you can provide [your own encryption keys when your disks are created](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption#encrypt_a_new_persistent_disk_with_your_own_keys). After you create the disk, you can create an encrypted image by providing your encryption keys to the image create command. For more information about encryption at rest and customer-supplied encryption keys, see [Encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) in the Google Cloud documentation.

## Image lifecycle

After you set up an image-build pipeline, you can use images to reliably launch instances of an application. While the pipeline can handle creating images, you must also ensure that your deployment mechanisms use the latest versions of the images. Finally, you need a process to curate images, so that old and obsolete images aren't used inadvertently.

### Image families

Image families help you manage images in your project by grouping related images together, so that you can roll forward and roll back between specific image versions. For more information, see [Image families best practices](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices).

### Deprecating an image

As an administrator, you can also [roll back the image](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#setting_families) that the image family points to by deprecating the image using the following command:
    
    
    gcloud compute images deprecate my-application-v3-20161011 --state DEPRECATED
    

You can choose from various states of deprecation:

State | Description  
---|---  
DEPRECATED | Images that are no longer the latest, but can still be launched by users. Users will see a warning at launch that they are no longer using the most recent image.  
OBSOLETE | Images that should not be launched by users or automation. An attempt to create an instance from these images will fail. You can use this image state to archive images so their data is still available when mounted as a non-boot disk.  
DELETED | Images that have already been deleted or are marked for deletion in the future. These cannot be launched, and you should delete them as soon as possible.  
  
### Enforcing lifecycle policies

You can mark images for deletion or obsolescence by using the `gcloud compute images deprecate` command. You can attach metadata to images to mark them for future deletion by providing one of the `--delete-in` or `--delete-on` flags. To attach metadata to mark images for future obsolescence, provide the `--obsolete-in` or `--obsolete-on` flags. You can incorporate this command into an image-build process to enforce an image-lifecycle policy that restricts the proliferation of stale and expired images in your project. For example, at the end of your image-build pipeline, you could include an additional check for images that need to be deprecated or deleted and then perform those actions explicitly.

While deprecated and deleted images are no longer shown through the API and UI by default, you can still see them by providing the `--show-deprecated` flag. To completely delete the image and its data, you must send an explicit [delete command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/delete) for that image.

## Sharing images between projects

Organizations often create multiple Google Cloud projects to partition their resources, environments, and user access. Isolating resources into projects allows for granular billing, security enforcement, and segregated networking. Although most cloud resources do not need to span multiple projects, images are good candidates for sharing across projects. By using a shared set of images, you can follow a common process to deliver images with best practices for security, authorization, package management, and operations pre-configured for the rest of the organization.

![Sharing images.](https://docs.cloud.google.com/static/solutions/images/sharing-images.svg)

You share images by assigning [IAM roles](https://docs.cloud.google.com/compute/docs/access/iam) to an organization's projects. The project that contains the images you want to share with other projects, referred to in the preceding diagram as the "Image Creation Project," must have the following IAM roles and policies applied:

  1. Allow users of the "Image User Group" to create instances from these images by granting them the `compute.imageUser` role.
  2. Allow the "Image Creation User" to create instances in this project by granting them the `compute.instanceAdmin` role.
  3. Allow the "Image Creation User" to create images and disks in this project by granting them the `compute.storageAdmin` role.



Projects that you want to be able to use the shared images must allow users with the `compute.imageUser` role to create instances by assigning them the `compute.instanceAdmin` role.

For more detailed instructions on sharing images between projects, see [Sharing images across projects in the Compute Engine documentation.](https://docs.cloud.google.com/compute/docs/images/sharing-images-across-projects)

## What's next

  * Review [OS upgrade best practices](https://docs.cloud.google.com/compute/docs/images/os-upgrade-best-practices)
  * Review image [import options](https://docs.cloud.google.com/compute/docs/import)
  * Work with boot images 
    * [Create a customized boot disk](https://docs.cloud.google.com/compute/docs/disks/create-root-persistent-disks)
    * [Set up trusted image policies](https://docs.cloud.google.com/compute/docs/images/restricting-image-access)
  * Work with custom images 
    * [Create custom images](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images)
    * [Manage access to custom images](https://docs.cloud.google.com/compute/docs/images/sharing-images-across-projects)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
