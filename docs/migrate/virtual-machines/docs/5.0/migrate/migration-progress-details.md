---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details/
title: Migration progress details \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:07:09.239346+00:00
---

# Migration progress details  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Migration progress details Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an exhaustive list of the steps and sub-steps for replication cycles, test-clone and cut-over, as well as the reference information for adaptation reports generated during your migrations.

## Replication cycle details

During the replication cycle, one of the following sub-steps is displayed along with the replication status:

_**Replication status sub-step**_ | _**Actions performed**_  
---|---  
**Initializing replication** | Initiating migration cycle, creating a snapshot of the source VM, and scanning for changes in the source VM disk data.  
**Replicating** | Live progress of the source VM data upload.  
**Post processing** | Creating a snapshot of the target disks, running OS adaptations, and deleting the source VM snapshot.  
**Idle** | There is no active cycle.  
  
### Snapshots created when migrating a workload

While using Migrate to Virtual Machines with a workload, every replication cycle starts with creating a snapshot of the migrating VM's disks. Older snapshots are deleted at the end of each cycle.

**Caution:** At least one snapshot per volume is maintained between cycles. Make sure you don't delete these snapshots or you will need to restart your replication process.

The snapshot also includes the tags provided in the **User tags** section of the source creation together with tags unique to Migrate to Virtual Machines that help the service identify VMs for cleanup.

**Note:** Migrate to Virtual Machines cleans deprecated snapshots on a best effort basis.

## Test-clone details

While creating a test-clone of a migrated VM, you'll see one of the following sub-steps displayed:

**Test-clone status sub-steps** | **Actions performed** | **Comments**  
---|---|---  
**OS Adaptation** | Running OS adaptation | (Optional) Visible if the target license has changed since the last successful adaptation run.  
**Preparing VM Disks** | Preparing VM disks for migration, creating an image of the source VM. |   
**Instantiating Migrated VM** | Creating the target VM with the migrated workload. |   
  
## Cut-over details

While creating a cut-over of your workload, you'll see one of the following sub-steps displayed:

**Cut-over status sub-steps** | **Actions performed** | **Comments**  
---|---|---  
**Previous Replication Cycle** | Identical to any replication cycle (including the same sub-steps). | (Optional) Visible if a prior replication cycle was active when the cut-over job was created.  
**Shutting down VM** | Shut down the source VM. | Initiates source VM down-time.  
**Final sync** | Final replication cycle (including the same sub-steps). |   
**Preparing VM disks** | Preparing VM disks for migration, creating an image of the source VM. | An identical action is performed during the test-clone phase.  
**Instantiating Migrated VM** | Creating the target VM with the migrated workload. | An identical action is performed during the test-clone phase.  
  
## Adaptation report

Migrate to Virtual Machines generates adaptation reports during replication cycles, test-clone, and cut-over. You can use this information for troubleshooting, problem solving, and deeper insight into your migration process.

For a migrating VM instance, the adaptation report is available after at least one replication cycle. To view the adaptation report for a migrating VM instance, follow these steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to Migrate to Virtual Machines](https://console.cloud.google.com/compute/mfce)

  2. Click the migrating VM instance name. Note that this VM instance must have completed at least one replication cycle.

  3. Click the **Replication History** tab.

  4. Click a completed replication cycle to open it.

  5. Click the Cloud Logging icon. The adaption report opens in Cloud Logging.




Here is an example of an adaptation report:
    
    
    "Adaptation report: root:{type:{value:\"linux\"} osinfo:{value:\"ubuntu14.04\"} distro:{value:\"ubuntu\"} product_name:{value:\"Ubuntu 14.04.5 LTS\"} major_version:{value:14} minor_version:{value:4}} boot_type:BIOS guest_os_features:\"VIRTIO_SCSI_MULTIQUEUE\" applied_license:{type:NONE default:true}"
    
    

The fields for the Migrate to Virtual Machines adaptation report:

Field | Description  
---|---  
**status** | The status of this adaptation report. Possible values: 

  * `SUCCESS`
  * `FAILURE`

  
**errors** | List of errors in this adaptation report. |   
**warnings** | List of warnings in this adaptation report. |   
**root** | The root file system of the OS.  
**boot_type** | The boot type of the VM. Possible values: 

  * `UNKNOWN`
  * `BIOS`
  * `UEFI`

  
**guest_os_features** | [Guest OS Features](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features) to attach on the boot disk.  
**licenses** | [Licenses](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#guest-os-features) to attach on the boot disk.  
**applied_license** | License information to support user license type setting. `applied_license.default` indicates whether Migrate to Virtual Machines should apply the [default license](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/supported-os-versions) for your migration. `applied.license.type` specifies the applied license for your migration if `applied_license.default` is set to `FALSE`.  
Possible values `applied_license.type`: 

  * `UNSPECIFIED`
  * `NONE`
  * `BYOL`
  * `PAYG`

Possible values `applied_license.default:`

  * `TRUE` (default)
  * `FALSE`

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
