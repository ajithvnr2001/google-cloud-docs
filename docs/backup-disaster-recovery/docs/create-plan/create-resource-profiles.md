---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-resource-profiles/
title: Manage resource profiles in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:53.550263+00:00
---

# Manage resource profiles in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-resource-profiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Manage resource profiles in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page tells you how to create resource profiles in the appliance management console that store backups in self-managed storage. If you want to learn how to store your backups in a backup vault, see [Overview of backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault).

A resource profile specifies the storage media for backups of application and VM data. The template and the resource profile that make up the backup plan dictate the type of application data policies to perform and where to store the application data backups (which storage pool is used). **Resource Profiles** define which snapshot pool (if needed) is used and which remote appliance data is replicated.

In addition to templates, you also create resource profiles in the backup plans menu. Profiles specify where to store data. Profiles are defined by the following parameters:

  * **Primary appliance** : The backup/recovery appliance that the resource profile is created for. This includes selecting which appliance snapshot pool will be used.

  * **Storage type** : OnVault pools can point to backup vaults or to Cloud Storage. When creating a profile, you must specify which type of storage will be used if an OnVault pool is specified. This selection can't be changed after the profile is created.

    * **(Optional) OnVault pools** : Up to four OnVault storage pools are available. The OnVault pools store compressed and encrypted backups of application data.
  * **(Optional) Remote appliance** : The backup/recovery appliance used for remote replication. This remote appliance must be an appliance that is already paired to the selected local appliance. You can configure the remote appliance field only when one or more remote appliances are configured on the selected local appliance. See [Join appliance in non-sharing mode](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/br-appliance-control-panel#joining_in_non-sharing_mode).




Resource profiles are applied to applications in the **App Manager** and the resource profiles work in tandem with policy templates:

  * A policy template that doesn't include a replication policy can be applied to an application along with a resource profile.
  * A policy template that includes a replication policy must be applied to an application along with a resource profile that stores data either on another appliance or to storage defined by OnVault storage pool.



You define a profile for any backup/recovery appliance that has been added to the appliance management console.

## Create a resource profile

Use these instructions to create a resource profile:

  1. Click **Backup Plans** and select **Profiles** from the list.

The **Profiles** page opens.

  2. Click **Create Profile**.

The **Create Profile** page opens with a new (empty) resource profile.

  3. In the **Profile** field, enter a descriptive profile name.

**Note:** For profile name, enter an alphanumeric text string. Spaces, underscores (_), and dashes (-) are allowed in a name; but don't include special characters.
  4. In the **Description** field, enter a brief description about the resource profile.

  5. Click **Primary Appliance** , and select the backup/recovery appliance that is considered as the primary (local) appliance from the drop-down. This is the backup/recovery appliance that the profile is created for and where data images reside.

  6. Click **Snapshot Pool** , and select the snapshot pool where you want to store snapshot images from the drop-down. The drop-down displays all snapshot pools.

**Note:** To back up Google Cloud console instances, you should only use the pool type _Cloud_. For VMware VM and agent-based backups, always select a pool that has the **Snapshot pool** type as shown in **Manage** > **Storage Pools**.
  7. Optional: From the numbered **OnVault Pool** lists, you can select an OnVault pool to store the data in a Google Cloud storage bucket or in a backup vault. You can select up to four different target pools or you can keep the **None** if you don't want to configure an OnVault pool.

**Note:** Direct to OnVault policies use only one OnVault pool.**Note:** Each OnVault pool that you select as a target must point to a different object storage bucket or backup vault.

You can select OnVault pools only if the backup/recovery appliance has defined the OnVault Storage pools.

  8. (Optional) From the **Remote Appliance** drop-down list, select a remote appliance to which data is used for remote replication. You can select this option only if the appliance is joined with another appliance.

  9. Click **Save Profile**.




## View and filter resource profiles

The Profiles window in the backup plans lists all of the resource profiles created on the appliance management console. From the Profiles window you can see the appliance, profile name, profile description, local appliance, remote appliance, OnVault storage pool, and snapshot pool associated with all resource profiles in the appliance management console. You can modify the display of fields that appear in the Profiles table, and you can also use the filter feature to locate resource profiles by name and description.

To view the resource profiles:

  1. Click **Backup Plans** , and select **Profiles** from the drop-down menu.

The **Profiles** page opens.

  2. In the list, select the resource profile that you want to view.

  3. To modify the display of the properties in this view, you can do the following:

     * **Adjust Fields**. To modify the fields that appear in the table, right-click within the table header row and click the checkboxes for the fields you want displayed (or those fields you don't want to view).
     * **Sort Content**. To sort the content listed in a table column by alphanumeric order, select a column header and then click the **Up** or **Down** arrow to change the order.
     * **Adjust Column Width**. To adjust the width of a table column to show more content in the table, drag the column divider in a column header to the left or right to resize the column width. Column dividers are marked by a pair of thin gray lines.
     * **Filter By**. To filter the list of hosts, click **show filter**. Enter one or more filter criteria as appropriate. To clear a filter, click the **x** to the right of the applied filter.

**Note:** Filters that are of type text, list, and date, persist across different appliance management console sessions for the same user.
  4. To export the resource profiles list click the export icon. You can export them in PDF format.




## Modify a resource profile

Use these instructions to modify a resource profile:

  1. Click the **Backup Plans** tab and select **Profiles** from the drop-down menu.

The **Profiles** page opens.

  2. Select the resource profile you want to modify from the list, then select **Edit** from the drop-down list at the bottom right corner of the window.

**Note:** You can also right-click on the item in the list and select **Edit** from the menu.
  3. Make the necessary changes to the resource profile:

     * In the **Profile** field, enter a descriptive profile name.
     * In the **Description** field, enter a brief description about this resource profile.
  4. From the **Primary** drop-down list, if necessary change select the primary (local) backup/recovery appliance that the profile is created for and where data images will reside.

  5. From **Snapshot Pool** drop-down list, if necessary modify the pool where you want to preserve the snapshots. The pool drop-down displays all Snapshot pools created during and after the backup/recovery appliance installation.

  6. Update any OnVault pools to which data will be sent. You can select this option only if this appliance has defined the OnVault Storage pool.

  7. (Optional) From the **Remote Appliance** drop-down list select:

     * A remote backup/recovery appliance to which data will be used for remote replication. You can select this option only if the appliance is joined with another appliance.
     * None: If data won't be replicated.
  8. Click **Save Profile**.




## Delete a resource profile

**Note:** Before deleting a profile, ensure that none of the managed applications are using the profile. You can delete a resource profile only when the resource profile isn't used to manage an application.

To delete a resource profile:

  1. Click the **Backup Plans** tab and select **Profiles** from the drop-down menu.The Profiles page opens.
  2. Select the resource profile you would like to delete from the list, then select **Delete** from the drop-down list at the bottom right corner of the window.

**Note:** You can also right-click on the item in the list and select **Delete** from the menu.
  3. Click **Confirm** in the confirmation dialog. The resource profile is deleted.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
