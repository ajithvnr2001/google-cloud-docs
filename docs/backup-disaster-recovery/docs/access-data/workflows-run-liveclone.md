---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/workflows-run-liveclone/
title: Run a LiveClone Backup and DR Workflow in the appliance management console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:05.378260+00:00
---

# Run a LiveClone Backup and DR Workflow in the appliance management console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/workflows-run-liveclone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Run a LiveClone Backup and DR Workflow in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The options you see when running an on-demand or scheduled LiveClone Backup and DR Workflow depends on your application type.

  * Database applications
  * All other applications

**Note:** Appliance management console users assigned with **Workflow Refresh** rights but not with **Workflow Run** or **Workflow Manage** rights, can only refresh the existing virtual application and cannot run, edit, delete, or disable the Backup and DR Workflow.

## Database applications

For database applications, the **LiveClone On Demand Run Workflow** page provides the following options:

  * **Refresh LiveClone** : Select this option if you want to refresh the LiveClone from selected source backup. If no LiveClone exists, it is created.
  * **Perform a Mount or Refresh of a Virtual Application** : Select this option to create or refresh a virtual application or database. It has the following options:

    * **Provision New Virtual Application** : Select this option if you want to create a new virtual application or database on a different server. You can also use this option to update or modify the options that were predefined in the Backup and DR Workflow, for example change the Backup and DR Workflow name.
    * **Refresh an Existing Virtual Application** : Select this option if you had previously created a virtual application using this Backup and DR Workflow and now would like to refresh it, using a different point-in-time snapshot as the source.



### Refresh LiveClone

If you select **Refresh LiveClone** , follow these steps:

  1. From the **Source Image** drop-down, select a backup.
  2. If the source application is protected by a snapshot policy that has enabled database log backups, and logs are available with the backup, you can use them to roll forward to a specific point in time by changing these options in the **Roll Forward Time** section:

     * The date field contains all possible dates that the database can be rolled forward to—through the application of database transaction logs. Select which date you want the database to roll forward to.
     * The time field contains a slider showing all possible times on the selected date that the database can roll forward to. If you select the latest possible date and then move the slider to the right most position, the job applies to all available logs. If you select the earliest possible date and move the slider to the left most position, the job applies no logs.
     * Specify to roll forward using either **User Time** or **Host Time**. **User Time** is relative to the local time of the current user. **Host Time** is relative to the system that hosts the data to be mounted.
  3. Click **Submit** to run the Backup and DR Workflow.




### Provision new virtual application

If you select **Provision New Virtual Application** , configure the new application:

  1. From the **Host** drop-down, select the server on which to mount the backup.
  2. Optionally, enable the **Map to All Cluster Nodes** option. You can see this option when one or more target hosts are a cluster node or a cluster host.
  3. You can see the following options only when one or more target hosts are VMware VMs:

     1. For **Mount Mode** , select one of the following:

        * **NFS** : By default NFS mode is selected. Backup and DR presents the data as a VMDK in an NFS datastore mounted from the backup/recovery appliance.
        * **vRDM (virtual raw device mapping)** : VMware snapshots treat mounted vRDMs as independent and are not included in snapshots. Because of this, by default, Backup and DR does not include vRDMs when protecting a mounted VM. Backup and DR does provide an option where you can mark vRDMs as dependent. Although rarely used, when this option is enabled, vRDMs are included in VMware snapshots. Backup templates captures vRDMs marked as dependent. Note that this mount mode needs the ESXi host to have an iSCSI initiator, which by default is not enabled in Google Cloud VMware Engine.
        * **pRDM (physical raw device mapping)** : For file-level restore operations, select this mode. Note that this mount mode needs the ESXi host to have an iSCSI initiator, which by default is not enabled in Google Cloud Google Cloud VMware Engine.
     2. From **Map to ESX Hosts** , select one of the following options. You can see the **Map to ESX Hosts** option only when you have selected vRDM or pRDM in the **Mount Mode** field.

        * **One** : Select **One** if you want to map only to the ESX host running the target VM.
        * **Two** : Select **Two** if you want to map to two ESX hosts, but not all ESX hosts in the cluster. On selecting **Two** , you are given the option to choose the second host, or choose **Auto-select**. Auto-select choose the second host based on logical pairs of ESX hosts and can always select the partner ESX host for the one running the target VM.
        * **All** : Select **All** if you want to map to all the ESX hosts present in the cluster. Note that selecting **All** may increase the duration for the job.
  4. Enable the **Create New Virtual Application** option and configure the new database. The options vary based on the database type.

  5. Click **Submit** to run the Backup and DR Workflow.




### Refresh an existing virtual application

If you select **Refresh an Existing Virtual Application** , follow these steps:

  1. From the **Host** drop-down, select the server where the application is mounted.
  2. Select the application to refresh.
  3. Click **Submit** to run the Backup and DR Workflow.



## All other applications

For all other applications, the **LiveClone On Demand Run Workflow** page provides the following options for selection:

  * **Refresh LiveClone** : Select this option if you want to refresh the LiveClone from selected source backup. If no LiveClone exists, it will get created.
  * **Perform a Mount or Refresh of a Virtual Application** : Select this option to create or refresh an existing mount.



### Refresh LiveClone

If you select **Refresh LiveClone** , follow these steps:

  1. From the **Source Image** drop-down, select a backup for use.
  2. Click **Submit** to run the Backup and DR Workflow.



### Perform a mount or refresh of a virtual application

  1. From the **Host** drop-down, select the server on which to mount the backup.
  2. Optionally, enable the **Map to All Cluster Nodes** option. You can see this option when one or more target hosts are a cluster node or a cluster host.
  3. View the following options only when one or more target hosts are VMware VMs:

     1. For **Mount Mode** , select one of the following options:

        * **NFS** : By default NFS mode is selected. Backup and DR presents the data as a VMDK in an NFS datastore mounted from the backup/recovery appliance.
        * **vRDM (virtual raw device mapping)** : VMware snapshots treat mounted vRDMs as independent and are not included in snapshots. Because of this, by default, Backup and DR does not include vRDMs when protecting a mounted VM. Backup and DR does provide an option where you can mark vRDMs as dependent. Although rarely used, when this option is enabled, vRDMs are included in VMware snapshots. Backup templates can capture vRDMs marked as dependent. Note that this mount mode needs the ESXi host to have an iSCSI initiator, which by default is not enabled in Google Cloud Google Cloud VMware Engine.
        * **pRDM (physical raw device mapping)** : For file-level restore operations, select this mode. Note that this mount mode needs the ESXi host to have an iSCSI initiator, which by default is not enabled in Google Cloud Google Cloud VMware Engine.
     2. From **Map to ESX Hosts** , select one of the following options. You can see the **Map to ESX Hosts** option only when you have selected vRDM or pRDM in the **Mount Mode** field.

        * **One** : Select **One** if you want to map only to the ESX host running the target VM.
        * **Two** : Select **Two** if you want to map to two ESX hosts, but not all ESX hosts in the cluster. On selecting **Two** , you are given the option to choose the second host, or choose **Auto-select**. Auto-select choose the second host based on logical pairs of ESX hosts and always selects the partner ESX host for the one running the target VM.
        * **All** : Select **All** if you want to map to all the ESX hosts present in the cluster. Note that selecting **All** may increase the duration for the job.
  4. Click **Submit** to run the Backup and DR Workflow.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
