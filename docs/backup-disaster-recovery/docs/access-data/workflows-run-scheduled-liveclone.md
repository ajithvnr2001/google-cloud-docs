---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/workflows-run-scheduled-liveclone/
title: Run a scheduled LiveClone Backup and DR Workflow in the appliance management console \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:15.699268+00:00
---

# Run a scheduled LiveClone Backup and DR Workflow in the appliance management console  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/workflows-run-scheduled-liveclone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Run a scheduled LiveClone Backup and DR Workflow in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The options you see when running a scheduled LiveClone Backup and DR Workflow depend on your application type.

  * Oracle and SQL Server applications
  * All other applications

**Note:** Appliance management console users assigned with **Workflow Refresh** rights but not with **Workflow Run** or **Workflow Manage** rights, can only refresh the existing virtual application and cannot run, edit, delete, or disable the Backup and DR Workflow.



## Oracle and SQL Server applications

For Oracle and SQL Server applications, the scheduled **Run Workflow** page shows the following options for selection:

  * **Initiate Scheduled Workflow Now** : Click **Submit** to run the Backup and DR Workflow. Select this option if you don't want to wait for the next scheduled time this Backup and DR Workflow runs. It runs exactly as defined. This does not impact any future scheduled runs of this workflow.

  * **Run with Customizations** : Select this option when you want to create or refresh a mount on a different server than the one predefined in this Backup and DR Workflow. Since only one mount per host can be created by a Backup and DR Workflow, any existing mount created by this Backup and DR Workflow is refreshed if the same server is selected. It has the following options:

    * **Refresh LiveClone** : Select this option if you want to refresh the LiveClone from selected source backup. If no LiveClone exists, it gets created. See Refresh LiveClone for more information.
    * **Perform a Mount or Refresh of a Virtual Application** : Select this option to create or refresh a virtual application or database. It has the following options:

      * **Provision New Virtual Application** : Select this option if you want to create a new virtual application or database on a different server. You can also use this option to update or modify the options that were predefined in the Backup and DR Workflow, for example, change the workflow name.
      * **Refresh an Existing Virtual Application** : Select this option if you previously created a virtual application using this Backup and DR Workflow and now would like to refresh it using a different point-in-time snapshot as the source.



### Refresh LiveClone

If you select **Refresh LiveClone** , complete the following:

  1. From the **Source Image** drop-down, select a backup.
  2. Click **Submit** to run the Backup and DR Workflow.



### Provision new virtual application

If you select **Provision New Virtual Application** , configure the new application:

  1. In the **Roll Forward Time** section, configure the log roll forward time. Select from host time (default) or user time. This option is available only for Oracle and SQL applications and only when the source backup has available logs.
  2. From the **Host** drop-down, select the server on which to mount the backup.
  3. Optionally, enable the **Map to All Cluster Nodes** option. You can see this option when one or more target hosts are a cluster node or a cluster host.
  4. You can see the following options only when one or more target hosts are VMware VMs:

     1. For **Mount Mode** , select one of the following:

        * **NFS** : By default NFS mode is selected. Backup and DR presents the data as a VMDK in an NFS datastore mounted from the backup/recovery appliance.
        * **vRDM (virtual raw device mapping)** : VMware snapshots treat mounted vRDMs as independent and are not included in snapshots. Because of this, by default, Backup and DR does not include vRDMs when protecting a mounted VM. Backup and DR does provide an option where you can mark vRDMs as dependent. Although rarely used, when this option is enabled, vRDMs is included in VMware snapshots. Backup templates captures vRDMs marked as dependent. Note that this mount mode needs the ESXi host to have an iSCSI initiator, which by default is not enabled in Google Cloud VMware Engine.
        * **pRDM (physical raw device mapping)** : For file-level restore operations, select this mode. Note that this mount mode needs the ESXi host to have an iSCSI initiator, which by default is not enabled in Google Cloud VMware Engine.
     2. From **Map to ESX Hosts** , select one of the following options. You can see the **Map to ESX Hosts** option only when you have selected vRDM or pRDM in the **Mount Mode** field.

        * **One** : Select **One** if you want to map only to the ESX host running the target VM.
        * **Two** : Select **Two** if you want to map to two ESX hosts, but not all ESX hosts in the cluster. On selecting **Two** , you are given the option to choose the second host, or choose **Auto-select**. Auto-select chooses the second host based on logical pairs of ESX hosts and always selects the partner ESX host for the one running the target VM.
        * **All** : Select **All** if you want to map to all the ESX hosts present in the cluster. Note that selecting **All** may increase the duration for the job.
  5. Enable the **Create New Virtual Application** option and configure the new database using information from:

     * [Configure application settings for Microsoft SQL server databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/sql-protect#sql-appsettings)
     * [Configure application details and settings for Oracle databases](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/oracle-advanced-settings)
  6. Click **Submit** to run the Backup and DR Workflow.




### Refresh an existing virtual application

If you select **Refresh an Existing Virtual Application** , complete the following:

  1. In the **Roll Forward Time** section, configure the log roll forward time. Select from host time—default—or user time. This option is available only for Oracle and SQL applications and only when the source backup has available logs.
  2. From the **Host** drop-down, select the server where the application is mounted.
  3. Select the application to refresh.
  4. Click **Submit** to run the Backup and DR Workflow.



## All other applications

For all other applications, the scheduled **Run Workflow** page shows the following options for selection:

  * **Initiate Scheduled Workflow Now** : Click **Submit** to run the Backup and DR Workflow. Select this option if you don't want to wait for the next scheduled time this Backup and DR Workflow runs. It runs exactly as defined. This does not impact any future scheduled runs of this Backup and DR Workflow.

  * **Run with Customizations** : Select this option when you want to create or refresh a mount on a different server than the one predefined in this Backup and DR Workflow. Since only one mount per host can be created by a Backup and DR Workflow, any existing mount created by this Backup and DR Workflow is refreshed if the same server is selected. It has the following options:

    * **Refresh LiveClone** : Select this option if you want to refresh the LiveClone from selected source backup. If no LiveClone exists, it gets created. See Refresh LiveClone for more information.
    * **Perform a Mount or Refresh of a Virtual Application** : Select this option to create or refresh a virtual application or database.



### Perform a mount or refresh of a virtual application

  1. From the **Host** drop-down, select the server on which to mount the backup.
  2. Optionally, enable the **Map to All Cluster Nodes** option. This option appears when one or more target hosts are a cluster node or a cluster host.
  3. The following options appear only when one or more target hosts are VMware VMs:

     1. For **Mount Mode** , select one of the following:

        * **NFS** : By default NFS mode is selected. Backup and DR presents the data as a VMDK in an NFS datastore mounted from the backup/recovery appliance.
        * **vRDM (virtual raw device mapping)** : VMware snapshots treat mounted vRDMs as independent and are not included in snapshots. Because of this, by default, Backup and DR does not include vRDMs when protecting a mounted VM. Backup and DR does provide an option where you can mark vRDMs as dependent. Although rarely used, when this option is enabled, vRDMs are included in VMware snapshots. Backup templates capture vRDMs marked as dependent. Note that this mount mode needs the ESXi host to have an iSCSI initiator, which by default is not enabled in Google Cloud VMware Engine.
        * **pRDM (physical raw device mapping)** : For file-level restore operations, select this mode. Note that this mount mode needs the ESXi host to have an iSCSI initiator, which by default is not enabled in Google Cloud VMware Engine.
     2. From **Map to ESX Hosts** , select one of the following options. You can see the **Map to ESX Hosts** option only when you have selected vRDM or pRDM in the **Mount Mode** field.

        * **One** : Select **One** if you want to map only to the ESX host running the target VM.
        * **Two** : Select **Two** if you want to map to two ESX hosts, but not all ESX hosts in the cluster. On selecting **Two** , you are given the option to choose the second host, or choose **Auto-select**. Auto-select choose the second host based on logical pairs of ESX hosts and can always select the partner ESX host for the one running the target VM.
        * **All** : Select **All** if you want to map to all the ESX hosts present in the cluster. Note that selecting **All** may increase the duration for the job.
  4. Click **Submit** to run the Backup and DR Workflow.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
