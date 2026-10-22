---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-consistency-groups/
title: Manage consistency groups in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:16:52.310770+00:00
---

# Manage consistency groups in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-consistency-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Manage consistency groups in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

A consistency group is a collection of discovered applications from the same host. Create a consistency group to back up application data of all member applications together to preserve consistency of data across the member applications. You apply a common policy to the members of a consistency group.

Use these instructions to access consistency groups:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. From the left panel, select **Consistency Group**.

**Note:** Generic applications and VMs are not allowed in consistency groups. Oracle does not support consistency groups of multiple databases. However, a consistency group may include a single Oracle database with other applications.



The backup/recovery appliance provides a consistent application data capture that undergoes backup at the same moment in time for Windows applications on the same host, including SQL Server, and local file systems.

For all other configurations, a consistency group can be defined and a backup of its member applications run as one job on the host but backups of each application are independent and not from the same point in time.

When creating a backup of these applications, the backup/recovery appliance resolves all of the applications into a collection of volumes.

Consistency groups are managed in the same way that applications are managed.

## Create a consistency group

A consistency group is a group of applications on the same host that are quiesced and captured together using a single policy. As the name implies, consistency groups ensure consistent point-in-time capture and recovery across multiple applications. Capturing application data with a consistency group consumes fewer system resources than capturing applications individually. For this reason, it is common to see groups of SQL server databases placed into consistency groups.

Use these instructions to create a **Consistency Group** from the **App Manager** page:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select one or more applications.

  3. Right-click and select **Add to Consistency Group** from the drop-down list. The **Add/Create Consistency Group** dialog opens. By default, the **Add to Consistency Group** option is selected.

  4. Click **Create Consistency Group**.

  5. In **Group Name** , enter a name for the **Consistency Group**.

  6. In **Description** , optionally add a brief description about the group.

  7. Click **Create**.

Once the **Consistency Group** is created, a success message opens.

  8. To protect the Consistency Group, click the **Click here to manage group** option. Otherwise, click **Okay** to close the success message.




## Best practices for protecting consistency groups

All applications in a consistency group must exist on the same application server. You cannot place applications from different servers into the same consistency group.

A consistency group cannot contain multiple Oracle databases. However, a single Oracle database can be included in a consistency group with other applications.

## Add applications to a consistency group

Use these instructions to add applications to an existing consistency group:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select one or more applications you want to add to the consistency group.

  3. Right-click and select **Add to Consistency Group** from the drop-down list.

The **Add/Create Consistency Group** dialog opens. By default, the **Add to Consistency Group** option is selected.

  4. Select the group and click **Add** to add the selected applications to an existing group.

Once the applications are added, a success message opens.

  5. Click **Click here to manage group** to protect the applications added. Otherwise, click **Okay** to close the success message.




## Edit a consistency group

Use these instructions to edit an existing consistency group:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Click **Consistency Groups** in the left panel to access the **Consistency Groups** list.

  3. Select the consistency group you want to edit and then select **Edit** from the drop-down list.

  4. Make the necessary modifications to the consistency group from the **Create Consistency Group** window. These modifications are described in Create a consistency group.




## Remove an application from a consistency group

Use these instructions to remove an application from a consistency group:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select the applications you want to remove.

  3. Right-click and select **Remove from Consistency Group** from the drop-down list.

The applications are removed from the group.




## Delete a consistency group

Use these instructions to delete an existing consistency group:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select **Consistency Groups** in the left panel to see the **Consistency Groups** list.

  3. Select the consistency group you want to delete and then select **Delete** from the drop-down list.

**Note:** You can also right-click on the item in the list and select **Delete** from the menu.
  4. Click **Confirm** in the confirmation dialog. The group appears as an orphan in the **Applications** window if there are any active backups corresponding to that application.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
