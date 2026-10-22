---
url: https://docs.cloud.google.com/compute/docs/import/
title: Choose a migration path \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:09.519149+00:00
---

# Choose a migration path  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Choose a migration path Stay organized with collections  Save and categorize content based on your preferences. 

You can move VM instances, custom images, or disks that are available in an existing environment, such as on-premises or on other cloud providers, to Compute Engine.

A variety of migration paths are available that support different formats. Choosing a migration path depends on whether you are moving a VM instance, disk, or image.

The following table summarizes the migration paths available on Compute Engine.

**What you want to migrate** | **Tool or procedure** | **Best used for**  
---|---|---  
VM instances | [Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/compute-engine/docs/latest) | 

  * Importing multiple VM instances and their data.
  * Migrating VM instances from other cloud providers such as VMware and AWS.
  * Testing your apps in the cloud before you migrate. If your apps do not function properly, you can easily roll back.

With Migrate to Virtual Machines, you have a suite of features that help you automate, simplify, and accelerate the migration process.  Migrate to VMs is free to use for customers migrating to Google Cloud. Standard billing rates apply for all other Google Cloud products (such as [Compute Engine](https://cloud.google.com/compute/all-pricing) or [Storage](https://docs.cloud.google.com/storage/pricing)) used or consumed during or after the migration. For example, if you use Compute Engine VMs to deploy Migrate to VMs, you'll need to pay for those instance hours. For more detailed pricing information, see [Migrate to VMs pricing](https://docs.cloud.google.com/migrate/compute-engine/pricing).  **Pro Tip:** This method is ideal for moving a large number of workloads.  
VM instances (in OVA or OVF format) | [Importing virtual appliances](https://docs.cloud.google.com/compute/docs/import/import-ovf-files) | Importing virtual appliances. A virtual appliance is a prepackaged virtual machine. **Pro Tip:** This method is best suited for importing a small number of virtual machines.  
Virtual disks or images | [Import virtual disks](https://docs.cloud.google.com/compute/docs/import/importing-virtual-disks) | Importing virtual disks or template disks from an on-premises or other cloud environment.  
  
These methods use the [images import](https://docs.cloud.google.com/sdk/gcloud/reference/compute/images/import) command.  
  
If you need to make advanced customizations or have source disks in a format that is not supported by the import command, you can [manually import and configure disks](https://docs.cloud.google.com/compute/docs/import/import-existing-image).   
The image import feature on Compute Engine is being moved to Migrate to Virtual Machines. We recommend that you use the new [image import feature on Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/image_import) to import your virtual disks to Google Cloud.   
Machine images | [Importing a machine image from a virtual appliance](https://docs.cloud.google.com/compute/docs/machine-images/import-machine-from-virtual-appliance) | Importing machine images. A machine image is Compute Engine resource that stores all the configuration, metadata, permissions, and data from one or more disks required to create a VM instance.  
  
This method is best suited for creating machine images from virtual appliances.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
