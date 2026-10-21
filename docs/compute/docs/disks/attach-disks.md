---
url: https://docs.cloud.google.com/compute/docs/disks/attach-disks/
title: Attach a non-boot disk to a VM \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:31.337074+00:00
---

# Attach a non-boot disk to a VM  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/attach-disks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Attach a non-boot disk to a VM Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to attach an existing non-boot disk to one or more virtual machine (VM) instances. 

To create or change a VM's boot disk, see [Create a boot disk](https://docs.cloud.google.com/compute/docs/disks/create-root-persistent-disks) and [Detach and reattach a boot disk](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk), respectively.

To create a new disk, see [Create a new Persistent Disk volume](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk) and [Create a new Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk). 

## Required roles and permissions

To get the permissions that you need to attach a disk to a VM, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to a VM instance that can run as a service account: Service Account User (v1) (`roles/iam.serviceAccountUser` role) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to attach a disk to a VM. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to attach a disk to a VM:

  * To attach a disk to a VM: 
    * `compute.instances.attachDisk` on the VM
    * `compute.instances.attachDisk` on the VM
    * `compute.disks.use` on the disk that you want to attach to the VM
  * To format and mount the attached volume: `compute.instances.setMetadata` on the VM 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Disk attachment mode

When you attach a disk to a VM, you indicate how the VM can access the data on the disk by specifying the disk attachment mode. You can choose read-only or read-write mode.

The default mode is read-write.

## Share a disk between VMs

You can share the same disk between VMs so that each VM can simultaneously access the disk by attaching the disk to each VM. You can attach a disk to multiple VMs if the disk's type and the VM's machine type support it.

To attach a disk to multiple VMs, follow the procedure in Attach a non-boot disk to your VM for each VM.

You must use the same disk attachment mode for all VMs that you attach the disk to. For example, you can't attach a disk to one VM in read-write mode and attach it at the same time to another VM in read-only mode.

For information about attaching a disk to multiple VMs, including the supported disk types, see [Share a disk between VMs](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms).

### Attaching a Hyperdisk volume to multiple VMs

To attach a Hyperdisk volume to multiple VMs, make sure the disk's access mode is set to an appropriate value for your use case. For instructions on setting the access mode, see [set the disk's access mode](https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks#change_access_mode).

When you attach a Hyperdisk volume to a VM, you must choose a disk attachment mode that doesn't conflict with the disk's access mode. For example, you can't use read-only attachment mode with a disk that's in single-writer or multi-writer mode.

## Limitations

When attaching a disk to a VM, be aware of the following limitations:

  * A disk must be in the same zone as the VM that you want to attach it to. For regional disks, the VM must be in the same zone as one of the disk's replicas.

  * You can attach up to 127 secondary, non-boot, zonal disks to a VM.

  * You can't attach a disk to a VM if doing so will exceed the [Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance).

  * The following disk types don't support read-only mode:

    * Hyperdisk Balanced
    * Hyperdisk Balanced High Availability
    * Hyperdisk Throughput
    * Hyperdisk Extreme
  * When you attach a disk to multiple VMs, you must use the same disk attachment mode for all the VMs.

  * When you attach a disk to multiple VMs, additional restrictions apply. See the restrictions for sharing a disk between VMs in [read-only mode](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms#ro-limitations) and [multi-writer mode](https://docs.cloud.google.com/compute/docs/disks/sharing-disks-between-vms#mw-limitations).

  * Disks attached to multiple VMs don't support auto-delete, that is, they can't be automatically deleted when the VM is deleted.




## Attach a non-boot disk to a VM

You can attach a non-boot zonal disk to a VM by using the Google Cloud console, the Google Cloud CLI, or REST.

When attaching a disk to a VM, keep the following points in mind:

  * **Use a custom device name** : Google recommends that you specify a custom device name when attaching a disk to a VM. The name you specify is used to generate a [symlink](https://docs.cloud.google.com/compute/docs/disks/disk-symlinks) for the disk in the guest OS, which makes it easier to identify and manage disks on the VM.

**Caution:** If you add a custom device name to a disk after you attach the disk to a VM, Compute Engine temporarily detaches the disk from the VM, which might disrupt your workloads.
  * **Attaching a disk to multiple VMs** : To attach a disk to multiple VMs, repeat the procedure in this section for each VM. You must use the same disk attachment mode for all VMs that you attach the disk to.




To attach a [Regional Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk) or [Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha) volume to your VM, see instead [Attach a regional disk to your VM](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk#repd_add_disk).

###  Console 

  1. Go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click the name of the VM where you want to add a disk.

  3. On the details page, click **Edit**.

  4. In the **Storage** section, under **Additional disks** , click **\+ Attach existing disk**.

  5. In the **Disk** list, select the disk you want to attach. If the disk isn't listed, make sure it's in the same location as the VM. This means the same zone for a zonal disk and the same region for a regional disk.

  6. For **Disk attachment mode** , select **Read-only** to only allow the VM to read from the disk. To allow the VM read-write access, select **Read/write**.

  7. Under **Deletion rule** , specify whether to delete the disk when the VM is deleted. To keep the disk when the VM is deleted, select **Keep disk**. To delete the disk when the VM is deleted, select **Delete disk**. If you're attaching the disk to multiple VMs, you must select **Keep disk**.

  8. Optional: To make identifying the disk easier from within the guest OS, specify a custom device name. Under the heading **Device name** , select **Use a custom device name**. In the **Device name** field, enter a string to use as a symlink for the disk.

  9. To apply the changes to the disk, click **Done**.

  10. Click **Save** to apply your changes and attach the disk to the VM.




###  gcloud 

To attach a disk to a VM, use the [`gcloud compute instances attach-disk` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk). Use the `mode` flag to specify the disk attachment mode.
    
    
    gcloud compute instances attach-disk VM_NAME \
        --disk DISK_NAME --device-name=DEVICE_NAME \
        --mode DISK_ATTACHMENT_MODE
    

Replace the following:

  * `VM_NAME`: the name of the VM where you are adding the new zonal persistent disk
  * `DISK_NAME`: the name of the new disk that you are attaching to the VM.
  * `DEVICE_NAME`: Optional: a name that the guest OS uses to identify the disk.
  * `DISK_ATTACHMENT_MODE`: Optional: how to attach the disk to the VM. For read-only mode, set to `ro`. For read-write mode, set to `rw`, or omit this flag because `rw` is the default.



###  Terraform 

To attach the disk to a VM, use the [`google_compute_instance` resource](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance).
    
    
    resource "google_compute_instance" "test_node" {
      name         = "test-node"
      machine_type = "f1-micro"
      zone         = "us-west1-a"
    
      boot_disk {
        initialize_params {
          image = "debian-cloud/debian-13"
        }
      }
      attached_disk {
        source      = google_compute_disk.default.id
        device_name = google_compute_disk.default.name
      }
    
      network_interface {
        network = "default"
        access_config {
          # Ephemeral IP
        }
      }
    
      # Ignore changes for persistent disk attachments
      lifecycle {
        ignore_changes = [attached_disk]
      }
    
    
    }

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

###  REST 

To attach a disk to a VM, construct a `POST` request to the [`compute.instances.attachDisk` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/attachDisk), and include the URL to the disk that you want to attach.

To specify the disk attachment mode, use the `mode` parameter.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/VM_NAME/attachDisk
    
    {
       "source": "/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME",
       "deviceName": DEVICE_NAME,
       "mode" : "DISK_ATTACHMENT_MODE"
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID
  * `ZONE`: the zone where the VM and disk are located
  * `VM_NAME`: the name of the VM that you want to attach the disk to
  * `DISK_NAME`: the name of the disk to attach
  * `DEVICE_NAME`: Optional: a name that the guest OS uses to create a symlink, which helps identify the disk.
  * `DISK_ATTACHMENT_MODE`: Optional: how the disk should be attached to the VM. For read-only mode, use `READ_ONLY`. For read-write mode, set to `READ_WRITE`, or omit because `READ_WRITE` is the default.



After you attach a disk to a VM, connect to the VM and enable the VM's operating system (OS) to use the disk:

  * If you attached a blank disk, format and mount the disk
  * If you attached a non-empty disk, mount the disk



Learn how to format and mount your new disks on [Linux](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux) or [Windows](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-windows) VMs.

## What's next

  * Prevent data loss by regularly [backing up your disks with snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshots)
  * Use [regional persistent disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk) for synchronous replication between two zones.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
