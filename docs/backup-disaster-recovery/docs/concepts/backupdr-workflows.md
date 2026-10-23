---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-workflows/
title: Backup and DR Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:00.989810+00:00
---

# Backup and DR Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backupdr-workflows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)



Send feedback 

#  Backup and DR Workflows Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

A Backup and DR Workflow automates access to backup data. While backup plan policy templates govern the automated backup of production data, Backup and DR Workflow automate access to that data. Workflows can run according to a schedule or on demand. Workflows are built with backups of production data. Workflows can present the backup data as a LiveClone, a virtual application, or as a file system mount that contains the application data.

**Note:** Backup and DR Workflows cannot be used to create new Compute Engine instances or VMware VMs from backups.

## Backup and DR Workflow benefits

Backup and DR Workflows have the following benefits:

  * Work environments can be updated with production data as soon as new data is available without having to wait days or even weeks for a DBA or system administrator to do the provisioning. This also frees the DBAs and system administrators from constantly provisioning and refreshing work environments.

  * Work environments can be updated on a predefined schedule or on demand.

  * User Acceptance Testing (UAT) is streamlined. Backup and DR can provision virtual applications (virtual copies of production applications) in UAT environments using the same databases and environments that exist in production.

  * Users can quickly and efficiently reproduce and address issues using the latest production data in a secure, isolated environment.

  * Software updates can be applied and tested, using the latest production data before being released in to a production environment.

  * Multiple teams can work in parallel and instantly access their own copy or virtual copy of production data.




Backup and DR Workflows take provisioning one step further by providing the ability to scrub backups of sensitive data. For those applications that contain sensitive data, a Backup and DR Workflow can include a step that creates a LiveClone and then automatically runs a script to mask the sensitive data.

The LiveClone with masked data can then be mounted as a virtual application or the LiveClone's data to provision a work environment. For example, consider the case where backups of production data contains social security numbers. A Backup and DR Workflow could do the following:

  * Prep-mount the backup data as a LiveClone so a script can scrub the social security numbers from the data.
  * Mount the scrubbed LiveClone as a virtual application using an application aware mount.
  * Flag the scrubbed virtual application as non-sensitive.



Once a Backup and DR Workflow completes, users can access the server on which the virtual application has been mounted and use the data as needed. Access to the data is controlled by the server on which the data is mounted. This ability allows users to self-provision their environments with virtual applications of production data while at the same time maintaining data security.

## Backup and DR Workflow data access methods

Backup and DR Workflows present backups of data as application aware mounts, LiveClones, or standard mounts.

### Direct mount

Direct mounts are used when application data does not need to be scrubbed before it is mounted and made available to users. The application data can be mounted with a standard mount as just the data, as a virtual application, or as both the data and as a virtual application. Direct mounts make backup data available almost instantly without actually moving data.

**Note:** OnVault pools pointing to backup vaults don't support mount operations.

### Application aware mount

The Backup and DR application aware mount feature provides instant access to an application as a virtual application without actually moving data. Applications can be mounted on any application server. If the application is a database, and its logs have been backed up, you can use the logs to roll the database forward to a point in time. Application aware mounts are performed from the backup/recovery appliance and don't require manual intervention by application, database, server, or storage administrators.

Once an application aware mount finishes, the virtual application can be backed up like any other application. This capability is particularly useful when a problem is encountered with a virtual application. Users can roll back their copy of the virtual application to a point where the issue does not exist, while other users troubleshoot the problematic version.

**Note:** OnVault pools pointing to backup vaults don't support mount operations.

### LiveClone

A LiveClone is an independent copy of an application that can be refreshed on a schedule or on demand. LiveClones are typically used in workflows when an application contains sensitive data which must be scrubbed before it is mounted and made available to users. This allows teams such as development and test to use production quality data without exposing sensitive data and interfering with the production environment. LiveClones are updated on demand or according to a schedule defined in the workflow.

## Manage workflows

You can create Backup and DR Workflows for database applications and consistency groups.

### Create backup data for Backup and DR Workflows

Backup and DR Workflows are made up of backed up application data. If you are backing up data specifically for Backup and DR Workflow purposes, the backup operation is no different than backing up data for other purposes.

Use these instructions to create backup data for Backup and DR Workflows:

  1. Define policy templates and resource profiles according to your RPOs and RTOs.
  2. Install the Backup and DR agent on source hosts that have access to the application data.
  3. Add these servers as new hosts.
  4. Discover applications on the added hosts.
  5. Apply policy templates and resource profiles to these applications.



## Create workflows

Use these instructions to create a Backup and DR Workflow:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Workflows** from the drop-down menu.

The **Workflows** page opens.

  2. Click the drop-down menu option on the lower right corner of the page and select **Run Workflows**. Alternatively, right-click the application and select **Run Workflows**.

The **Run Workflow** page opens. If the application has any existing workflows, they are listed here.

  3. Click **Add Workflow** and add basic configuration details.

  4. In **Workflow Name** , enter a unique name for the workflow. Note: Backup and DR Workflow names cannot include special characters.

  5. From the **Appliance** drop-down, select the appliance where you want this Backup and DR Workflow to run.

**Note:** If the application is replicated, and is managing both the source and replication target appliance, both the source and the replication target appliances will be listed. The source appliance is selected by default.
     1. Configure the type, schedule and other Backup and DR Workflow details following the instructions in [Create direct mount workflows](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/create-direct-mount-workflows) and in [Create LiveClone workflows](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/create-liveclone-workflows).



## Edit a Backup and DR Workflow

When editing a Backup and DR Workflow, you cannot update the following Backup and DR Workflow properties:

  * Backup and DR Workflow name
  * Backup and DR Workflow type
  * Appliance
  * Schedule type



You can make changes to other Backup and DR Workflow properties following these instructions.

**Note:** Appliance management console users, when assigned with **Workflow Refresh** rights but not with **Workflow Run** or **Workflow Manage** rights, can only refresh the existing virtual application and cannot run or edit or delete or disable the workflow.

Use these instructions to edit a Backup and DR Workflow:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Workflows** from the drop-down menu.

The **Workflows** page opens.

  2. Select a managed application or **Consistency Group** with the Backup and DR Workflow you want to edit.

  3. Right-click the application and from the drop-down menu, select **Edit**.

The **Edit Workflow** page opens.

Alternately, select the application and then choose **Edit** from the drop-down list at the bottom of the **Applications Workflows** window.

  4. Make the required changes using instructions in creating workflows topics.

     * To edit a Backup and DR Workflow of type direct mount, see [Create direct mount workflows](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/create-direct-mount-workflows)
     * To edit a Backup and DR Workflow of type LiveClone mount, see [Create LiveClone workflows](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/create-liveclone-workflows)



## Disable a Backup and DR Workflow

**Note:** Appliance management console users, who are assigned with **Workflow Refresh** rights but not with **Workflow Run** or **Workflow Manage** rights, can only refresh the existing virtual application and cannot run or edit or delete or disable the workflow.

Use these instructions to disable a Backup and DR Workflow:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Workflows** from the drop-down menu.

The **Workflows** page opens.

  2. Select the Backup and DR Workflow you want to delete.

  3. Right-click and select **Disable**. Alternately, select the workflow and then choose **Disable** from the drop-down list at the bottom of the **Workflow Application Dashboard** page.

You are prompted to confirm your action.

  4. Click **Confirm** to disable the workflow. The **Workflow Application Dashboard** page refreshes and the Backup and DR Workflow is listed with the **Current Status** of **Disabled**.




You can enable a disabled Backup and DR Workflow as necessary.

## Enable a disabled Backup and DR Workflow

You can enable a disabled Backup and DR Workflow using these instructions.

**Note:** Appliance management console users who are assigned with **Workflow Refresh** rights but not with **Workflow Run** or **Workflow Manage** rights, can only refresh the existing virtual application and cannot run or edit or delete or disable the workflow.

Use these instructions to enable a disabled Backup and DR Workflow:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Workflows** from the drop-down menu.

The **Workflows** page opens.

  2. Select the application that you want to enable.

  3. Right-click the application and select **Enable** from the drop-down menu. You are prompted to confirm your action.

  4. Alternately, select the application and then choose **Enable** from the drop-down list at the bottom of the workflows window.

  5. Click **Confirm** to enable the workflow.




## Delete a Backup and DR Workflow

**Note:** Appliance management console users who are assigned with **Workflow Refresh** rights but not with **Workflow Run** or **Workflow Manage** rights, can only refresh the existing virtual application and cannot run or edit or delete or disable the workflow.

Use these instructions to delete a Backup and DR Workflow:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Application** page opens.

  2. From the left panel, select **Managed** and select the application that you want to delete.

  3. Right-click the application and from the drop-down menu, select **Manage Workflows**.

The **Workflow Application Dashboard** page opens.

  4. Alternately, select the application and then choose **Manage Workflows** from the drop-down list at the bottom of the **Applications** window.

  5. Select the Backup and DR Workflow you want to delete.

  6. Right-click and select **Delete**. Alternately, select the workflow and then choose **Delete** from the drop-down list at the bottom of the **Workflow Application Dashboard** page.

  7. Click **Confirm** to delete the workflow. The **Workflow Application Dashboard** page refreshes and the Backup and DR Workflow is no longer listed.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
