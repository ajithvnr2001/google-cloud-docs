---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-strategy/
title: Image import versus machine image import \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:43.235344+00:00
---

# Image import versus machine image import  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-strategy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Image import versus machine image import Stay organized with collections  Save and categorize content based on your preferences. 

Migrating virtual disks or virtual machine (VM) instances to Google Cloud requires choosing the right import strategy based on your needs—whether you need to migrate specific data or operating system components, or replicate entire VM configurations across different projects. Migrate to Virtual Machines offers two primary methods for migrating VM images to Google Cloud: _image import_ and _machine image import_. This document compares these two methods to help you choose the right strategy for your migration.

## Image import and machine image import

Cloud migration often involves more than transferring data: it requires a strategic approach. Before migrating, you must consider the following key aspects:

  * The best method to transfer curated OS images with embedded configurations.
  * How to ensure consistency across scaled environments.
  * The optimal approach for migrating images versus complex, multi-disk virtual machines.



Migrate to Virtual Machines offers two primary methods for migrating VM images to Google Cloud: _image import_ and _machine image import_.

  * **Image import:** This method lets you import individual disks, typically OS or data volumes, into Google Cloud. It is ideal for rebuilding or maintaining golden images, especially when the goal is to replicate a clean, consistent base configuration across multiple instances. For information on importing an image, see [Import images](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/image_import).
  * **Machine image import:** This more comprehensive solution captures the entire VM state, including multiple disks, configuration metadata, networking, and startup scripts. It is particularly suited for migrating complex workloads that require end-to-end replication. For information on importing a machine image, see [Import machine images](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/machine-image-import).



Both options are valuable and their applicability depends on the workload you are migrating. The following table highlights the differences, advantages, and ideal use cases for each method.

Feature | Image Import | Machine Image Import  
---|---|---  
**Focus** | Individual disks (OS or data volumes) | Entire VM configuration (multiple disks and metadata)  
**Use cases** |  The ideal use cases for image import are:   


  * Creating golden images for consistent environments
  * Migrating database data disks
  * Offline migration of specific workloads
  * Replicating consistent environments
  * Migrating applications with specific OS needs
  * Bringing data to Google Cloud with precise data state preservation

|  The ideal use cases for machine image import are: 

  * Deploying a consistent environment such as golden images
  * Migrating complex web applications such as a single VM with a complex disk setup, or a group of VMs
  * Preparing for disaster recovery
  * Migrating complex applications with dependencies and networking
  * Migrating offline with minimal downtime
  * Replicating for testing and disaster recovery

  
**Advantages** |  The advantages of image import are:   


  * **Efficiency** : Fast and reliable for migrating large volumes of data.
  * **Accuracy** : Preserves the exact file system structure of the source system.
  * **Consistency** : Ideal for creating clones of systems for redundancy or scaling.

| The advantages of machine image import are:   


  * **Easy versioning** : Keep your images organized and trackable with seamless image versioning management.
  * **Support for multiple disks** : Can hold multiple disks.
  * **Quick recovery** : As machine images save the entire VM, you don't need to perform manual configuration after import.
  * **Cost-effective** : Saves the time of setting up VMs and benefits from Compute Engine's compressed, affordable storage.
  * **Consistency** : Deploy multiple VMs with the same configuration for standardization across your projects.
  * **Secure and flexible** : Supports encrypted transfers, custom OS support, and hybrid cloud compatibility.
  * **Automation ready** : Integrate image imports into development and operations (DevOps) workflows or infrastructure-as-code (IaaS) tools like Terraform.

  
**Configuration** | Granular (disk-level) | Holistic (entire VM configuration)  
**Complexity** | Recommended for less intricate dependencies | Recommended for intricate dependencies or specific hardware requirements  
**Supported formats** | 

  * VMDK (recommended)
  * VHD/VHDX
  * QCOW/QCOW2
  * QED
  * VDI
  * VPC
  * Raw compressed files (.tar.gz file containing .raw file)

| 

  * OVF (descriptor file + disk files)
  * OVA (single-file package)

  
**Support for the _Generalize_ feature** | Available (removes unique instance data from Windows images) | Available (removes unique instance data from Windows images)  
**Disk support** | Single disk representation | Can hold multiple disks  
**Recovery** | Less comprehensive (focuses on disks) | Quick recovery (entire VM is saved, no manual configuration needed)  
**Versioning** | Can be managed with [image families](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices#public-families) | Can be managed with seamless image versioning management  
**Automation** | Supports integration into DevOps workflows or IaaS | Supports integration into DevOps workflows or IaaS  
  
## Choose the right migration strategy

Cloud migration isn't a one-size-fits-all process. Whether you choose image import or machine image import depends on your specific infrastructure, workload, and migration goals.

### Image import

When you need to migrate individual disks containing either data or operating systems, image import is the preferred option. Consider it as moving specific building blocks of your IT infrastructure. Here are some practical examples:

  * **Create a golden image for development and production environments:** your development team might require a standardized environment with a specific operating system configuration and pre-installed software. You can create a image of a perfectly configured operating system along with auxiliary packages and use it as a template. Each developer can then create a new VM instance using this image, ensuring consistency, security, and saving setup time.
  * **Migrate a database's data disks to the cloud:** if you have a large database on a physical server, you can create a image of the database's data disks an import it into Google Cloud, preserving the data's integrity.
  * **Perform an offline migration of specific workloads:** for physical servers that cannot be migrated directly, you can create a local image of the workload and then import it to Compute Engine.



### Machine image import

Machine image import takes a holistic approach, capturing the entire VM configuration, including multiple disks, metadata, and permissions. This makes it ideal for scenarios where preserving the interdependencies between components is crucial. Here are some practical examples:

  * **Deploy a consistent environment:** replicate entire VM configurations across different projects, commonly referred to as golden images.
  * **Migrate complex web applications:** machine image import lets you migrate an application, whether it is a single virtual machine that has a complex disk setup with the operating system and application installed, or it can be a group of VMs along with other infrastructure services. For example, consider a web application that requires a particular web server setup, a database, and specialized software libraries.
  * **Prepare for disaster recovery:** Machine image import is a valuable tool for low-scale disaster recovery or archiving up to two application configurations. By creating a machine image of your critical servers, you have a readily available backup that can be quickly deployed in case of a system failure. This minimizes downtime and ensures business continuity.



## Key decision factors

When choosing between image import and machine image import, consider the following:

  * **Configuration complexity:** if your workload involves intricate dependencies or specific hardware requirements, machine image import is the recommended approach.
  * **Granularity:** if you only need to migrate specific data or operating system components, image import provides the necessary granularity.



Google Cloud's migration tools are powerful, but they're most effective when you understand their strengths and limitations. Take the time to plan, test, and execute your cloud migrations.

## What's next

  * Review [image import options](https://docs.cloud.google.com/compute/docs/import)
  * Work with boot images 
    * [Create a customized boot disk](https://docs.cloud.google.com/compute/docs/disks/create-root-persistent-disks)
    * [Set up trusted image policies](https://docs.cloud.google.com/compute/docs/images/restricting-image-access)
  * Work with custom images 
    * [Create custom images](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images)
    * [Manage access to custom images](https://docs.cloud.google.com/compute/docs/images/sharing-images-across-projects)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
