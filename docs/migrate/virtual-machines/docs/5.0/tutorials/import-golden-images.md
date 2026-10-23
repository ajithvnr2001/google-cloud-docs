---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/tutorials/import-golden-images/
title: Import a golden image to Google Cloud \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:44.444725+00:00
---

# Import a golden image to Google Cloud  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/tutorials/import-golden-images/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Import a golden image to Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Migrating existing IT infrastructure to the cloud presents challenges, particularly when moving critical assets like golden images. Golden images are standardized, pre-configured operating systems and application stacks essential for consistent environment provisioning across development, testing, and production. Ensuring the replication of these images in Google Cloud, without losing fidelity or operational efficiency, is a top priority for many enterprises.

Migrate to Virtual Machines provides two primary migration paths that address different use cases: _image import_ and _machine image import_.

  * _Image import_ migrates individual disks, such as operating system or data volumes, into Google Cloud. This method supports rebuilding or maintaining golden images, especially when replicating a consistent base configuration across multiple instances.
  * _Machine image import_ captures the entire virtual machine (VM) instance state, including multiple disks, configuration metadata, networking, and startup scripts. This comprehensive solution suits migrating complex workloads that require end-to-end replication.



For more information about the use cases and advantages of image import and machine image import, see [Choose your import strategy](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-strategy).

The best migration approach depends on your workload. Some images are straightforward and well-suited for disk-level or image import, such as OS disks, database disks, or file systems. Others, with tighter interdependencies and configuration requirements, benefit from the holistic nature of machine image import. Understanding the distinctions between these options streamlines your cloud migration.

## Objectives

  * Understand image import capabilities.
  * Understand machine image import capabilities.
  * Choose the appropriate migration approach for simple disk images versus complex, multi-disk VM instances.
  * Migrate golden images to Google Cloud while preserving integrity and flexibility.



## Costs

This tutorial uses the following billable components of Google Cloud:

  * [Compute Engine](https://cloud.google.com/compute/all-pricing) for virtual machine instances and persistent disks
  * [Cloud Storage](https://cloud.google.com/storage/pricing) for storing image files



Review the pricing pages for each service to understand the costs associated with running this tutorial. Delete resources after completing the tutorial to avoid continued charges.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. Enable the [VM Migration API](https://console.cloud.google.com/apis/library/vmmigration.googleapis.com) on your project.
  7. Ensure that the operating system on the disk is supported by Migrate to VMs. For more information, see [Supported operating systems](https://docs.cloud.google.com/migrate/virtual-machines/docs/supported-operating-systems).
  8. Ensure that the virtual disk image files you want to import are supported.
  9. Create a Cloud Storage bucket to upload your image files.
  10. Ensure that the following Identity and Access Management roles are granted. For more information, see [Grant the required permissions](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/machine-image-import#permissions). 
     1. [VM Migration Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/vmmigration#vmmigration.admin)
     2. [VM Migration Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/vmmigration#vmmigration.serviceAgent)



## Image import—your precision migration tool

Image import offers a granular approach, focusing on bringing individual virtual disk images into Google Cloud. This migrates the building blocks of your VM instances. These images, usually containing operating systems, then instantiate new VM instances or create persistent disks within Google Cloud.

For more information about image import features, see [Image import and machine image import](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-strategy#image_import_and_machine_image_import).

### Understand disk images

Disk images are versatile tools. You can use them to set up VM instances quickly, back up entire systems for safekeeping, or clone environments to streamline deployment. They are also ideal for testing software or performing system recovery without altering the original setup. For backups, development, or troubleshooting, disk images make managing IT tasks efficient and reliable.

VM disk images are low-level representations of storage volumes. They exist in several formats.

  * **Raw disk images:** raw disk images are uncompressed, direct block-level copies of entire disk volumes. They offer the highest fidelity but result in the largest file sizes. Common formats include: 
    * VMDK (Virtual Machine Disk) - Recommended for faster import
    * QCOW
    * QCOW2
    * QED
    * VPC
    * VDI
    * VHDX
    * VHD
  * **Sparse disk images:** sparse disk images optimize storage by only storing used disk blocks. This significantly reduces storage overhead and dynamically expands as data writes. In Google Cloud, operating system and data disks are stored and used as images.



### Import a golden image using image import

You can import a virtual disk image to Google Cloud using the Google Cloud console, Google Cloud CLI, or REST API commands. For information about importing images using Google Cloud CLI and REST API commands, see [Import a virtual disk image to Google Cloud](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/image_import#gcloud).

To import a virtual disk image to Google Cloud using the Google Cloud console, use the following steps.

  1. [Upload your virtual disk image file](https://docs.cloud.google.com/storage/docs/uploading-objects) to a Cloud Storage bucket. For better performance, we recommend that you upload the virtual disk image file to a bucket in the same cloud region in which you want to create the image.

  2. Open the **Image imports** tab in Migrate to VMs page in the Google Cloud console.

[Go to Image imports](https://console.cloud.google.com/compute/mfce/images)

  3. Click **Create Image**.

  4. Click **Browse** to view the list of buckets in your current project. Select the file from which you want to import the image.

  5. Define the rest of characteristics of the image. For more information on the parameters, see [Import a virtual disk image](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/image_import#console).

     1. Consider using the _Generalize_ feature for Windows images. When a VM instance is created from an image in Windows, unique information adds to that instance. The _Generalize_ process removes this unique data, enabling you to create multiple instances from the same image.
     2. Use [public image families](https://docs.cloud.google.com/compute/docs/images/image-families-best-practices#public-families) to manage the lifecycle of your images. Ensure that you create new instances from the most up-to-date version of every image family. Add the **Family** field to a new image to indicate that this is the latest version of the images belonging to that family.
  6. After filling in all the parameter details and options, click **Create** to initiate the image import process.

  7. After the import job is created, track its status in the [Migrate to VMs dashboard](https://console.cloud.google.com/compute/mfce/dashboard).




Once the import job is complete, you'll have a disk-based image.

## Machine image import—the holistic migration approach

Machine images offer a comprehensive approach, providing a broader solution compared to focusing solely on individual disks. A machine image captures the configuration of an entire VM instance, including instance settings, network configurations, operating system details, metadata and labels, security configurations, as well as startup and shutdown scripts.

By importing a machine image, you bring a complete and unified blueprint of your VM instance into Google Cloud. This holistic method simplifies the migration of complex workloads, ensuring consistency and reducing the likelihood of errors during deployment.

For more information about machine image import features, see [Image import and machine image import](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-strategy#image_import_and_machine_image_import).

### Import a golden image using machine image import

You can import a machine image to Google Cloud using the Google Cloud console, gcloud CLI, or REST API commands. For information about importing machine images using gcloud CLI and REST API commands, see [Import a machine image to Google Cloud](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/machine-image-import#gcloud).

To import a machine image to Google Cloud using Google Cloud console, use the following steps:

  1. [Upload your OVA or OVF file](https://docs.cloud.google.com/storage/docs/uploading-objects) to a Cloud Storage bucket. For better performance, we recommend that you upload the virtual disk image file to a bucket in the same cloud region in which you want to create the image.

  2. Open the **Machine image imports** tab in Migrate to VMs page in the Google Cloud console.

[Go to Machine image imports](https://console.cloud.google.com/compute/mfce/machineImages)

  3. Click **Create Machine Image**.

  4. Click **Browse** to view the list of buckets in your current project. Select the file from which you want to import the image.

  5. Define the rest of characteristics of the image. For more information on the parameters, see [Import a machine image](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/machine-image-import#console).

Consider using the _Generalize_ feature for Windows images. When a VM instance is created from an image in Windows, unique information adds to that instance. The _Generalize_ process removes this unique data, enabling you to create multiple instances from the same image.

  6. After filling in all the parameter details and options, click **Create** to initiate the image import process.

  7. After the import job is created, track its status in the [Migrate to VMs dashboard](https://console.cloud.google.com/compute/mfce/dashboard).




Once the import job is complete, you'll have a machine image.

## Clean up

After you finish the tutorial, clean up the resources you created to stop incurring charges. The following sections describe how to delete or turn off these resources.

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete individual resources

If you don't want to delete the entire project, delete the individual resources created during this tutorial.

  1. Delete the bucket: 
         
         gcloud storage buckets delete BUCKET_NAME

**Important:** Your bucket must be empty before you can delete it.
  2. Delete any imported images or machine images. 
         
         gcloud compute images delete IMAGE_NAME
         
         gcloud compute machine-images delete MACHINE_IMAGE_NAME

  3. Delete any virtual machine instances created from the imported images. 
  4. Delete the instance: 
         
         gcloud compute instances delete INSTANCE_NAME




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
