---
url: https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-from-vm/
title: Create a MIG from an existing VM \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:20.549194+00:00
---

# Create a MIG from an existing VM  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-from-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Create a MIG from an existing VM Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create a regional or zonal managed instance group (MIG) from an existing virtual machine (VM) instance.

By creating a MIG, you can scale the service running on a single VM across multiple VMs and manage them as a single entity. MIGs are useful to make your workloads highly available and scalable. For more information, see the [benefits of using a MIG](https://docs.cloud.google.com/compute/docs/instance-groups#benefits).

## Before you begin

  * If you haven't already, [ create and start a VM](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).



## Limitations

The following limitations apply when you create a MIG from an existing VM:

  * The MIG doesn't add the existing VM to the MIG. The VM continues to exist as a standalone VM.

  * You can't create [stateful MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/stateful-migs) from an existing VM.




## Create a MIG from an existing VM

You can create a MIG from an existing VM that is running, stopped, or suspended. Creating a MIG from an existing VM involves the configuration of the following:

  1. An [instance template](https://docs.cloud.google.com/compute/docs/instance-templates), which Compute Engine uses to define the properties of the VMs in the MIG. By default, the instance template specifies the following:

     * The same properties of the existing VM, except for the existing VM's IP addresses.

     * An option to create a [custom boot disk image](https://docs.cloud.google.com/compute/docs/images#custom_images) from the existing VM's boot disk. Additionally, if the existing VM uses non-boot disks, Compute Engine does the following as applicable:

       * For any [local SSD](https://docs.cloud.google.com/compute/docs/disks/local-ssd) that is attached to the existing VM, Compute Engine creates a blank local SSD disk.

       * For any [persistent disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) in read-write mode that is attached to the existing VM, Compute Engine creates a custom persistent disk image from the existing VM's persistent disk image.

       * For any persistent disk in read-only mode that is attached to the existing VM, the same disk is included in the instance template.

Optionally, you can customize the disks and properties of the instance template.

  2. The MIG, which uses the instance template you configured in the previous step. By default, the MIG is a [zonal MIG](https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig) that specifies the following:

     * [Autoscaling](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-basic-autoscaling) is disabled.

     * One VM in the group.

     * The same zone where the existing VM is located.

Optionally, you can customize the properties of the MIG.


**Caution:** If you create a MIG from a running or suspended VM and you choose to create disk images using that VM's disks, then you must [prepare the VM](https://docs.cloud.google.com/compute/docs/images/create-custom#minimize_writing_data_to_the_persistent_disk). Otherwise, Compute Engine might create corrupted disk images.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * To create an image: `compute.images.create` on the project.
  * To create an instance template: `compute.instanceTemplates.create` on the project.
  * To create a regional MIG: `compute.regionInstanceGroupManagers.create` on the project.
  * To create a zonal MIG: `compute.instanceGroupManagers.create` on the project.



To create a MIG from an existing VM, follow these steps:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Select the VM that you want to use to create the MIG.

  3. Click **Create a group based on this VM**.

The **Scale to instance group** page opens.

  4. In the **Instance template properties** section, do the following:

     1. In the **Name** field, use the default name or enter a name for the instance template.

     2. In the **Disks** section, do the following:

        * **Boot disk** : By default, Compute Engine generates a new custom image of the VM boot disk. If you want to use an existing disk instead, click edit **Edit boot disk**. You can select a public image or an existing custom image to attach to the VMs in the MIG.

        * **Existing disk** : Applicable only if your VM has a read-only disk. Optionally, you can do one of the following:

          * To customize any attachment settings of the read-only disk, click edit **Edit disk**.

          * To remove the disk, click close **Remove disk**.

        * **New disk** : Applicable only if your VM has a read-write disk. By default, Compute Engine creates a new custom disk image. Optionally, you can do one of the following:

          * To use an existing disk or modify the disk settings, click edit **Edit disk**.

          * To remove the disk, click close **Remove disk**.

     3. If the existing VM is running or suspended, and you have specified to attach new boot or non-boot disks that use the VM's disk images as sources, the **On image generation** section appears. Then, you must select one of following options:

        * If you want to maintain the file system's integrity while generating an image from the VM disk, stop the VM by selecting **Stop the VM**. You can restart the VM after the MIG is created. Until then, your service is interrupted.

        * If you do not want interruption to your service and the file system's integrity is not a concern, select **Keep the VM running**.

     4. To further customize the instance template used to define the properties of the VMs in the MIG, click settings **Customize instance template** and modify the fields as needed. For more information, see [Create instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates).

  5. In the **Instance group properties** section, do the following:

     1. In the **Name** field, use the default name or enter a name for the MIG.

     2. In the **Location** section, you can choose to create a regional or zonal MIG by doing one of the following:

        * To create a regional MIG, follow these steps:

          1. Select **Multiple zones**.

          2. In the **Region** list, select a region where to create the VMs in the MIG.

          3. In the **Zones** list, select the zones where to create the VMs in the MIG.

        * To create a zonal MIG, follow these steps:

          1. Select **Single zone** (default).

          2. In the **Region** list, select a region where to create the VMs in the MIG. By default, the region where the original VM exists is selected.

          3. In the **Zone** list, select a zone where to create the VMs for the MIG. By default, the zone where the original VM exists is selected.

     3. To further specify the MIG settings—for example, to specify the number of VMs—click settings **Configure instance group**. For more information, see how to create a [regional](https://docs.cloud.google.com/compute/docs/instance-groups/distributing-instances-with-regional-instance-groups) or [zonal MIG](https://docs.cloud.google.com/compute/docs/instance-groups/create-zonal-mig).

  6. After you've finished customizing the instance template and the MIG, click **Create group**. If your VM is running and you specified to stop the VM in the previous steps, click **Stop VM and create group**.

The **Instance groups** page opens. Creating the instance template and the MIG might take a few minutes to complete.




## What's next

  * Learn how to [update VM configurations in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs).

  * Learn how to [autoscale groups of VMs](https://docs.cloud.google.com/compute/docs/autoscaler).

  * Learn more about [different configuration options available in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances).

  * Learn more about [building scalable and resilient web applications](https://docs.cloud.google.com/solutions/scalable-and-resilient-apps).

  * Learn more about [disaster recovery on Google Cloud](https://docs.cloud.google.com/solutions/disaster-recovery-cookbook).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
