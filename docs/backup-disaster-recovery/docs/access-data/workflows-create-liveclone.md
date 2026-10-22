---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/workflows-create-liveclone/
title: Create LiveClone Backup and DR Workflows in the appliance management console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:35.994457+00:00
---

# Create LiveClone Backup and DR Workflows in the appliance management console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/workflows-create-liveclone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Create LiveClone Backup and DR Workflows in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

LiveClone Backup and DR Workflows are used when the production data contains sensitive information. It lets you define a LiveClone from production data and then scrub the LiveClone's data before mounting it.

A LiveClone Backup and DR Workflow can do the following:

  * Generate a new, or updates an existing, LiveClone from a selected production backup that is marked as sensitive.
  * Define a schedule for updating the LiveClone with the latest production data. Scheduled Backup and DR Workflows can also be run on demand.
  * Employ scripts to scrub the LiveClone of sensitive data.
  * Mark the scrubbed virtual application as non-sensitive.
  * Either mount the scrubbed data—standard mount—to a specific host, or mount the scrubbed backup as a virtual application—application aware mount—to a specific host.

**Note:** Appliance management console users, when assigned with **Workflow Refresh** rights but not with Backup and DR Workflow run or Backup and DR Workflow manage rights, can only refresh the existing virtual application and cannot run, edit, delete, or disable the Backup and DR Workflow.



Use these instructions to create a LiveClone Backup and DR Workflow:

  1. From the Backup and DR appliance management console, click **App Manager** , then select a managed application or consistency group.
  2. Right-click and select **Manage Workflows** to open the Backup and DR Workflows **Application Dashboard**. Click **Add Workflow** and add basic configuration details like **Name** and **Appliance** of where you want the Backup and DR Workflow to run.
  3. Select **LiveClone** for the **Workflow Type**.
  4. Select **Scheduled** or **On Demand** for the **Schedule Type**. For scheduled Backup and DR Workflows, define a schedule to run the Backup and DR Workflow. The time selector uses a 24-hour clock. Scheduled Backup and DR Workflows can also be run on demand.
  5. Complete the **LiveClone Settings** section.

     * Select the latest snapshot from the policy that produces the backup to scrub for the **Source Image**. If you selected **On Demand** , the user running the Backup and DR Workflow selects the source snapshot at run time.
**Note:** You can also select the latest StreamSnap backup from a specific snapshot policy.
     * Enter an identifiable name in the **LiveClone Label** field.
     * Select the diskpool to hold the LiveClone—as well as the differences from subsequent mounts of the LiveClone—for **Diskpool**. Be sure enough storage space is allocated to accommodate the LiveClone.
  6. Optionally, enable the **Mount for Pre-Processing** option. This makes sure that the LiveClone is mounted to a host and one or more scripts run on the mounted backup to scrub or mask sensitive data.

     1. Enable the **Mark data as non-sensitive** option if your selected application contains sensitive data and you want it be scrubbed and made non-sensitive. This allows non-sensitive data users to access the Backup and DR Workflow and provision their work environments.
     2. Select the host on which to mount the LiveClone from the **Host** drop-down.
     3. Optionally, enable the **Map to All Cluster Nodes** option. You can see this option when one or more target hosts are a cluster node or a cluster host.

     4. You can see the following options only when one or more target hosts are VMware VMs:

        1. For **Mount Mode** , select one of the following:

           * **NFS** : By default NFS mode is selected. Backup and DR presents the data as a VMDK in an NFS datastore mounted from the backup/recovery appliance.
           * **vRDM (virtual raw device mapping)** : VMware snapshots treat mounted vRDMs as independent and are not included in snapshots. Because of this, by default, Backup and DR does not include vRDMs when protecting a mounted VM. Backup and DR does provide an option where you can mark vRDMs as dependent. Although rarely used, when this option is enabled, vRDMs are included in VMware snapshots. Backup templates capture vRDMs marked as dependent. Note that this mount mode needs the ESXi host to have an iSCSI initiator, which by default is not enabled in Google Cloud VMware Engine.
           * **pRDM (physical raw device mapping)** : For file-level restore operations, select this mode. Note that this mount mode needs the ESXi host to have an iSCSI initiator, which by default is not enabled in Google Cloud VMware Engine.
        2. From **Map to ESX Hosts** , select one of the following options. You can see the **Map to ESX Hosts** option only when you have selected vRDM or pRDM in the **Mount Mode** field.

           * **One** : Select **One** if you want to map only to the ESX host running the target VM.
           * **Two** : Select **Two** if you want to map to two ESX hosts, but not all ESX hosts in the cluster. When selecting **Two** , you can choose the second host or choose **Auto-select**. Auto-select chooses the second host based on logical pairs of ESX hosts and always selects the partner ESX host for the one running the target VM.
           * **All** : Select **All** if you want to map to all the ESX hosts present in the cluster. Note that selecting **All** may increase the duration for the job.
     5. Enter the location for the mounted drives in the **Mount Location** field. For example, `M:, D:\testdb1`.

     6. Select an option to mask sensitive data in the **Scripts Options** section.

        * Select the **Optim Privacy Data Masking** option if you are using Optim Data Privacy software for data masking. The **Masking Set** drop-down is populated automatically, so you can specify the corresponding timeout in minutes in **Masking Set**.
        * Select the **Custom Scripts** option if you are using Backup and DR custom scripts. Specify at least one pre- or post-processing script and the corresponding timeout in seconds. For more information, see [Custom scripts](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/custom-scripts).
     7. Click the **Create New Virtual Application** option to perform an application aware mount. This option is available only for IBM Db2, Oracle, PostgreSQL, SAP ASE, and SQL Server applications.

**Note:** You may need to create a new database (perform an AppAware mount) if the scripts to scrub sensitive data can only be run when the database is powered up and running.
  7. Click **Next**.

  8. Specify the mount details for the LiveClone backup.

     * For **Mount Label** , provide a name to make it identifiable.
     * In the Hosts section, select one host on which you will perform the AppAware mount. You cannot perform an AppAware mount on multiple hosts.
     * In Mapping Options section, for **Mount Location** , enter the location for the mounted drives—for example, `M:`, `D:\testdb1`, or `/oracledata/db1data`.
     * In the **Scripts Options** section, add any pre- and post-scripts that are needed to use.

     * (Databases only) Enable **Create New Virtual Application** if you want to perform an application aware mount (a virtual database). This option is available only for IBM Db2, Oracle, PostgreSQL, SAP ASE, and SQL Server applications. The displayed settings vary according to database type. If you don't select the **Create New Virtual Application** option, you can instead get a file system mount to your target hosts.

     * Optionally, enable **Remove Mounted Image After Done** if you employ one or more scripts to process the mounted data as a one-time task after which the mounted data is no longer needed, such as extraction of data into a data warehouse. Once the script finishes its task this option unmounts and deletes the virtual application.

  9. Click **Add** to create the Backup and DR Workflow.




## The VMware administrator's guide

This page is one in a series of pages specific to protecting and recovering VMware VMs with Backup and DR. You can find additional information at:

  * [Backup and DR for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/vmware-intro)
  * [Configure Google Cloud VMware Engine for Backup and DR protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-vmware)
  * [Add vCenter and ESX server hosts to the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-vcenter-host)
  * [Discover and protect VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-vms)
  * [Apply a backup template to protect a VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-template-to-manage-a-VM)
  * [Configure Application settings for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-application-settings-for-vmware-vm)
  * [Restore a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-vm)
  * [Mount a VMware backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-vmware-image)
  * [Clone an image of a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-image-of-a-vm)
  * [Create LiveClone workflows](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/create-liveclone-workflows)
  * [Move VM management between two backup/recovery appliances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/supported-vmware)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
