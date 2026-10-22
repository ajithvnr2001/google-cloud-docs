---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/workflows-create-direct-mount/
title: Create direct mount Backup and DR Workflows in the appliance management console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:09.254180+00:00
---

# Create direct mount Backup and DR Workflows in the appliance management console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/workflows-create-direct-mount/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Create direct mount Backup and DR Workflows in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Direct mount Backup and DR Workflows are used when the application backup involved does not contain sensitive data. This allows the Backup and DR Workflow to mount an application's data as a virtual application, or as just application data without first having to define a LiveClone and then scrub the LiveClone. Direct mounts make application data and virtual applications available almost instantly.

A direct mount Backup and DR Workflow does the following:

  * Generates new—or updates—virtual applications from a single selected production backup.
  * Defines a schedule for updating the virtual application with the latest production data. Scheduled Backup and DR Workflows can also be run on demand.
  * Mounts the data as a virtual application. A virtual application can be used and protected like any other application.
  * Backs up the mounted virtual application as a new application.

**Note:** Appliance management console users, when assigned with **Workflow Refresh** rights but not with Backup and DR Workflow run or Backup and DR Workflow manage rights, can only refresh the existing virtual application and cannot run or edit, delete, or disable the Backup and DR Workflow.



Use these instructions to create a direct mount Backup and DR Workflow:

  1. From the Backup and DR appliance management console, click **App Manager** and then select a managed application or consistency group.
  2. Right-click and select **Manage Workflows** to open the **Workflows Application Dashboard**. Click **Add Workflow** and add basic configuration details like **Name** and **Appliance** where you want the Backup and DR Workflow to run.
  3. Select **Direct Mount** for the **Workflow Type**.
  4. Select either **Scheduled** or **On Demand** for the **Schedule Type**. If you select **Scheduled** , define a schedule to run the Backup and DR Workflow. The time selector uses a 24-hour clock. The scheduled time—next run time—reflects the time zone of the local appliance that runs the Backup and DR Workflow—which by default is set to UTC.
  5. Scheduled Backup and DR Workflows can also be run on demand.
  6. Configure the **Direct Mount Settings** section.
  7. Select the latest snapshot from the policy that produces the backup to scrub for **Source Image**. If you selected **On Demand** , the user running the Backup and DR Workflow can select the source snapshot at run time. You can also select the latest backup from a specific snapshot policy, the latest StreamSnap backup.
  8. Enter an identifiable name in the **Mount Label** field.
  9. Select one or more servers to mount the backup from in the **Host** drop-down.
  10. Optionally, enable the **Map to All Cluster Nodes** option. You can see this option when one or more target hosts are a cluster node, or a cluster host.
  11. You can see the following options only when one or more target hosts are VMware VMs:

     1. For **Mount Mode** , select one of the following:

        * **NFS** : By default NFS mode is selected. Backup and DR presents the data as a VMDK in an NFS datastore mounted from the backup/recovery appliance.
        * **vRDM (virtual raw device mapping)** : VMware snapshots treat mounted vRDMs as independent and are not included in snapshots. Because of this, by default, Backup and DR does not include vRDMs when protecting a mounted VM. Backup and DR does provide an option where you can mark vRDMs as dependent. Although rarely used, when this option is enabled, vRDMs are included in VMware snapshots. Backup templates can backup vRDMs marked as dependent. Note that this mount mode needs the ESXi host to have an iSCSI initiator, which by default is not enabled in Google Cloud VMware Engine.
        * **pRDM (physical raw device mapping)** : For file-level restore operations, select this mode. Note that this mount mode needs the ESXi host to have an iSCSI initiator, which by default is not enabled in Google Cloud VMware Engine.
     2. From **Map to ESX Hosts** , select one of the following options. You can see the **Map to ESX Hosts** option only if you have selected vRDM or pRDM in the **Mount Mode** field.

        * **One** : Select **One** if you want to map only to the ESX host running the target VM.
        * **Two** : Select **Two** if you want to map to two ESX hosts, but not all ESX hosts in the cluster. On selecting **Two** , you are given the option to choose the second host, or choose **Auto-select**. Auto-select chooses the second host based on logical pairs of ESX hosts, and always selects the partner ESX host for the one running the target VM.
        * **All** : Select **All** if you want to map to all the ESX hosts present in the cluster. Note that selecting **All** might increase the job duration. 
     3. Enable **Mark Dependent** to mark mounted volumes as dependent to include them in VMware snapshots. This is rarely used when mounting to an existing VM.

  12. In **Mapping Options** section, enter the location for the mounted drives for the **Mount Location** —for example, `M:, D:\testdb1`.

  13. In the **Scripts Options** section, specify one pre- or post-processing script to run on the mountedbackup and the corresponding timeout in seconds. For detailed information on pre-script, post-script, and timeout in seconds, see [Script options](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/custom-scripts).

  14. Click the **Create New Virtual Application** option to perform an application aware mount. This option is available only for IBM Db2, Oracle, PostgreSQL, SAP ASE, SAP HANA, SAP MaxDB, and SQL Server database applications. The displayed settings vary according to database type. If you don't select the **Create New** option you instead get a file system mount to your target hosts.

  15. Optionally, enable **Remove Mounted Image After Done** if you employ one or more scripts to process the mounted data as a one-time task, such as extraction of data into a data warehouse. Once the script finishes its task, this option unmounts and deletes the virtual application.

You cannot use this option if you have selected the **Manage New Application** option.

  16. Click **Add** to create the Backup and DR Workflow.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
