---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-disk-groups/
title: Migrate disks in groups \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:07:10.342352+00:00
---

# Migrate disks in groups  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-disk-groups/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Migrate disks in groups Stay organized with collections  Save and categorize content based on your preferences. 

Use groups to perform bulk disk migration tasks on multiple VMs simultaneously. Groups streamline the process of planning and migrating disks of multiple VMs so that you can perform migration in batches. You can also create new VM instances and attach the migrated Persistent Disk volumes to them.

The migration process for groups uses the same phases as for an individual VM:

  * **Onboard**
  * **Replicate**
  * **Set VM target details**
  * **Test-clone (optional)**
  * **Cut-over**
  * **Finalize**



With groups, before you start replication you first add one or more source VMs to a group. You then perform the migration on the entire group, or on a subset of VMs in the group.

The disk migration process follows the same steps as the VM migration process. Therefore, you can choose to switch from VM migration to disk migration and the other way around at any point during the migration process. For more information, see Switch from disk migration to VM migration.

**Note:** You can migrate your VM's boot disk as a data disk using the disk migration process in cases where OS adaptation is not needed. In case you want to migrate the boot disk with the OS (to be able to use it as a boot disk), then [VM migration](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms) is more suitable.

## Prerequisites

Perform the following steps to configure the migration environment on the your [migration source](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/architecture#migration_sources_and_targets) and [migration target](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/architecture#migration_targets).

  * [Enable Migrate to Virtual Machines services](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/enable-services).
  * (Only for VMware VM migration) [Install the Migrate Connector](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrate-connector).



## Options for configuring groups

While you typically perform operations on an entire group (such as starting replication) you can also perform any operation on a specific VM or subset of VMs in the group. For example, when configuring the target details, some or all of the VMs in the group might have specific requirements (such as project or disk type) that don't apply to other VMs.

When configuring the target for a migration, you can:

  * **Select the entire group** to configure the target for all VMs. You can later modify the target configuration for a subset of VMs or for an individual VM.

  * **Select a subset of VMs** in the group and configure the target for those VMs. You can later modify the target configuration for an individual VM.

  * **Select an individual VM** in the group and configure the target just for that VM.




## Step 1: Onboard VMs in a group

A group is a logical collection of one or more VMs. Groups have the following characteristics:

  * All source VMs in the group must be from the same source.

  * A source VM can belong to one group or to no groups. That is, a VM cannot be a member of multiple groups.

  * You can perform operations on all source VMs in a group, or on a subset of VMs in the group.

  * You can configure the target's characteristics for the entire group, and then override them for individual source VMs in the group.

  * A group name can contain only lowercase letters (a-z), numbers, and hyphens. The name must start with a lowercase letter, and end with a lowercase letter or a number.




You can have up to 200 migrations in progress at a time (excluding migrations in the Finalize phase).

To onboard VMs in a group, follow these steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Sources** tab.

  3. From the drop-down list, select the migration source from which you want to migrate a VM.

Below the drop-down you see the status of the migration source as:

     * **Active** : The source is active and connected to Migrate to Virtual Machines.
     * **Offline** : The source is unavailable.
     * **Pending** : The source is in the process of being connected and verified.

If you don't see any entries in the drop-down list, it indicates that you have not configured the migration source properly. Review the steps for your setting your migration source and try again.

  4. A table appears showing the source VMs in the migration source available for migration. Select the source VMs you want to add to a group.

The **VM Power Status** column shows the status as **Suspended** , **On** , or **Off**. You can add a VM with any of these statuses to a group.

  5. Select **Add to group**.

  6. In the dialog, either specify the name of a new group or select the name of an existing group.

  7. Select **Add to Group**. The group name for each VM appears under the **Migration group** column.

The **Migration** **status** column for each VM displays one of the following:

     * **Pending** : VM is in the process of being onboarded.
     * **Ready** : VM is onboarded but not yet replicating.



You can now start replication of the VMs as described in the next section.

## Step 2: Start replication for a group

The first phase of migration is to start replicating the disk data from the source VMs to Google Cloud. This is a continuous process that takes place in the background.

Data replication is comprised of two steps:

  1. **First replication step** : Migrate to Virtual Machines creates the initial snapshot of the source VM data disks and replicates the snapshot data to Google Cloud. Depending on the amount of disk data on the source VM, the first replication can take minutes or hours to complete.

The **Replication status** column of a VM on the first replication step displays the **First sync** status followed by the appropriate sub-step.

  2. **Incremental replication step** : Following a successful first replication step, incremental replication steps occur at set time intervals (every two hours by default). In each step, a new snapshot is created for each data disk. Only data updates that occurred after the previous step are replicated to Google Cloud using the Change Block Tracking (CBT) mechanism.

The **Replication status** column of a VM on an incremental replication step displays the **Active** status followed by the appropriate sub-step.




### Initiate replication for a group

To initiate replication for a group, follow these steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Groups** tab. You should see a list of all VM groups.

If you don't see any entries in the table, it means you have not yet created any groups. See Onboard VMs in a group for the procedure on creating a group.

  3. Select the group name from the list. A table appears showing the source VMs in the group.

  4. Start replication:

     1. **To replicate all VMs in the group** , from the **Migration** drop-down, select **Start Replication** under **All migrations in group**.

     2. **To replicate a subset of VMs** , select the required VMs and then from the **Migration** drop-down, select **Start Replication** under **Selected migrations**.

Starting the migration initiates the replication phase of migration. The **Replication** **status** column for a VM displays one of the following:

        * **First sync** : VM is performing the first replication step.
        * **Active (Current cycle: XX%)** : VM has performed **XX%** percent of the current replication step.
        * **Active (Idle)** : VM is idle between replication steps.

To view the replication history of a VM, click the VM to open the details page. Click **Replication History** to view the replication history of the VM along with the [sub-steps of the replication](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#replication_cycle_details).

**Note:** Migrate to Virtual Machines saves and displays up to 100 cycles of replication history for a VM.



You can now configure group targets for the test-clone and cut-over phases.

You can also set the migration interval. For more information, see [Set the replication interval](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-disks#set_the_replication_interval).

### Switch from disk migration to VM migration

You can switch between disk migration and VM migration at any time during the migration process. Note that you cannot switch the migration type of a VM that belongs to a group. You must remove the VM from the group and then convert the migration from disk migration to VM migration.

To switch from disk migration to VM migration, follow these steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Groups** tab. You should see a list of all VM groups.

  3. Remove VMs for which you want to change the migration type from the group:

     1. **To remove all VMs from the group** , from the **Group Assignment** drop-down, select **Move to group** or **Remove from group** under **All migrations in group**.

     2. **To remove a subset of VMs** , select the required VMs and then from the **Group Assignment** drop-down select **Move to group** or **Remove from group** under **Selected migrations**.

The VMs that you have removed from the group should appear in the **Disk Migrations** tab.

  4. Select the **Disk Migrations** tab.

  5. Select one or more VMs.

  6. Click **Migration > Convert to VM migration**.




Switching from disk migration to VM migration clears out the target details. This is because the target details for disk migration and VM migration are different. However, the replication progress isn't lost during the switch.

You must update the target details before you clone or cut-over operations on your VM in order for the migration to succeed. For more information, see Configure group targets.

## Step 3: Configure group targets

Migrate to Virtual Machines lets you migrate the disks of a source VM to Persistent Disk volumes on Google Cloud with the following options:

  * Migrate the disks to Persistent Disk volumes

  * Migrate the disks to Persistent Disk volumes and attach them to a new VM instance




You must configure the target details such as project, zone, disk type, and more based on the option you choose. The target project is the project that contains the Persistent Disk volumes migrated from the source VM, or the newly created VM instances to which you want to attach the migrated Persistent Disk volumes. You can modify the target details at any time. When you create a test-clone or cut-over, Migrate to Virtual Machines uses the target details settings at the time of the operation.

The [host project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/enable-services#identifying_your_host_project) is automatically added as a target project so there is no need to explicitly add it. If you want to add an additional project as a target project, see [Adding a target project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project).

To configure the Persistent Disk target, follow these steps:

  1. If you have not done so already, add the target project as shown in [Adding a target](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project).

  2. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  3. Select the **Groups** tab.

A table of available groups appears.

  4. Select a group.

  5. Select the VMs in the group to configure:

     1. Select the checkbox for an individual VM.

     2. Select the checkbox for multiple VMs.

     3. Select the checkbox in the top row of the table to select all the visible rows in the table.

**Note:** This action does not select the rows that are not visible. When you select the checkbox in the top row of a table when some rows are not visible, a prompt appears in the top row asking if you want to select all rows in the table.
  6. Click **Edit Target Details**. A panel opens to let you configure the **Target Details** for the selected VMs.

On the panel, setting most options applies that option to all selected VMs. However, some settings are specific to the VMs and you can set them individually. If you are configuring multiple VMs, you set these options individually for each VM:

     1. **(Required)** : The Persistent Disk volume **Name**.

     2. **(Optional)** : The **External IP** and **Internal IP** addresses of the Persistent Disk volume.

  7. Set the **Target details** that define the characteristics of the Persistent Disk volumes to which you want to migrate your data. The following table lists those settings in detail.

You can select the checkbox next to each disk indicating whether or not it should be created in the target project when the VM is cloned or cut over.

Section title | Field name | Description  
---|---|---  
**General** | Project | The name of the project hosting the Persistent Disk volumes. It must be a project you have already added earlier in this section.  
| Zone | Zone for the Persistent Disk volumes. See [ Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).  
  
**Disk Configuration** | Name | Enter a name for the disk.   
| Disk Type | Select the type of Persistent Disk. See [ Persistent Disk types](https://docs.cloud.google.com/compute/docs/disks#disk-types).   
| Labels | To organize your project, add labels as key/value pairs to your resources. See [ Labeling resources](https://docs.cloud.google.com/compute/docs/labeling-resources).  
**Attach to a VM** | Attach disks to VM | Select **Don't attach to a VM** if you don't want to attach the Persistent Disk volumes to a VM instance.  
Select **Create a VM from a disk image** if you want to create a VM instance and attach the Persistent Disk volumes to it. If you choose this option, you must set the target details that define the attributes of the new VM instance to which you want to attach the migrated Persistent Disk volumes. For more information on these settings, see [Configure the target for a VM](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms#configure-target).   
**Replication Policy** | Replication idle duration between cycles | By default, Migrate to Virtual Machines performs a replication of the source VM every 2 hours. Set the replication frequency (in seconds).  
**Note:** The replication cycle idle time counter starts after the previous replication cycle ends.  
  8. Click **Save**.




## (Optional) Step 4: Test a clone of disks in a group

In the test-clone phase, you can check if the Persistent Disk volumes created during the replication phase are functioning as expected. For example, you can attach the migrated Persistent Disk volumes to a Compute Engine instance in your target environment to check if the disks are working as expected.

If you have created a new VM instance and attached the migrated Persistent Disk volumes to it, Migrate to Virtual Machines deploys a clone of the VM instance to a Compute Engine instance in your target environment to test it. While the testing phase is optional, it is best practice to perform testing before you perform a cut-over to the migrated disk.

Each time you create a test-clone instance, it is cloned from the most recently completed replication cycle data using the current target details. In other words, a test-clone instance represents a _snapshot_ of the source VM at the time of the last completed replication cycle.

**Caution:** New replication data and modifications to the target details are only applied to _new_ test-clones, not to existing test-clones.

You can test a VM in the **Paused** state if it has completed at least one replication.

### Test a group

To test a group, follow these steps:

  1. Ensure that you have configured a target environment as shown in Configure group targets.

**Note:** You can only test-clone VMs with a valid target environment.
  2. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  3. Select the **Groups** tab.

A table of available VM groups appears.

  4. Select a group.

A table of available source VMs appears. You can test any VM that is in the **Active (Current cycle: XX%)** or **Active (Idle)** state. The **Active** state means the first replication sync of the VM succeeded.

  5. Select the VMs in the group to test:

     1. For all VMs in the group, from the **Cut-Over and Test-Clone** drop-down, select **Test-clone** under **All migrations in group**. Any VMs without a valid target environment, and any VMs not in the **Active (Current cycle: XX%)** or **Active (Idle)** state, are ignored.

     2. For one or more selected VMs, from the **Cut-Over and Test-Clone** drop-down, select **Test-clone** under **Selected migrations**. All selected VMs must have a valid target environment and be in the **Active (Current cycle: XX%)** or **Active (Idle)** state.

The **Test-Clone/Cut-Over status** column shows the status of the operation along with one of the sub-steps detailed in the [test-clone sub-steps table](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#test-clone_details).

  6. Wait for the **Test-Clone/Cut-Over status** column to show **Succeeded**. This indicates that the clone was created successfully.

You can view the test-clone history of a VM in one of the following ways:

     * Click the **Info panel** icon, ![Info panel file icon](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/images/info-panel-icon.png), for the VM. On the panel that opens from the right, the **Monitoring** tab displays the history, including the name of each test-clone instance.
     * Click the VM to open the details page. Click **Test-Clone/Cut-Over History** to view the test-clone history of the VM along with the [sub-steps of the test-clone](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#test-clone_details).

You can cancel an active test-clone operation by selecting a VM and then clicking **Cancel Test-Clone** from the **Cut-Over and Test-Clone** drop-down.

  7. You can now create VM instance(s) and attach the test-clone disks to it to check if the migrated disks are working as expected.

  8. After you have completed testing, delete the VM instance(s) to free up resources so that you are no longer charged for the instance.




### Manage multiple test-clones

Over the duration of your migration journey, you might create multiple test-clones. For example, you create the first test-clone after the initial replication cycle. Then, as you refine your migration, you create new test-clones. For information on managing multiple test clones, see [Manage multiple test clones](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-disks#manage_multiple_test-clones).

## Step 5: Cut-over a group

In the cut-over phase, you transfer control to your migrated disk, or the new VM you created with the migrated Persistent Disk volumes attached to it, in your target environment on Google Cloud.

The cut-over process does the following:

  1. If data replication is active, that is, the **Replication status** of a VM is **Active (Current cycle: XX%)** , waits for it to complete.

  2. Shuts down the source VMs.

  3. Performs the final data replication. Because replication occurs throughout all migration phases, the amount of data to replicate shouldn't be very large.

**Note:** To perform cut-over, replication cannot be paused on a VM.
  4. Stops replication.

  5. Creates the Persistent Disk volumes from the final replicated data.

**Note:** You must have already configured the Persistent Disk target details before you can initiate a cut-over. For more information, see Configure group targets.



The cut-over phase includes a short VM downtime and should take place during a scheduled maintenance window. You must determine the maintenance window during which you can stop the source VM and redirect traffic to the migrated disk.

### Create a cut-over

To create a cut-over, follow these steps:

  1. Ensure that you have configured a production VM target environment as shown in Configure group targets. If the target details were previously configured for test-clone operation, you might want to edit the target details to point to a new target.

**Note:** You can only cut-over VMs with a valid target environment.
  2. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  3. Select the **Groups** tab.

A table of available groups appears.

  4. Select a group.

A table of available source VMs appears. You can cut-over any VM that is in the **Active (Current cycle: XX%)** or **Active (Idle)** state. The **Active** state means the first replication sync of the VM succeeded.

You can also cut-over a VM that has already been cut-over and is in the **Cut-over** state. Select the individual VM or multiple VMs in the table to perform the cut-over. However, selecting **Cut-Over** for the entire group only performs a cut-over on **Active** or **Active (Idle)** VMs.

  5. Select the VMs in the group to cut-over:

     1. For all VMs in the group, from the **Cut-Over and Test-Clone** drop-down, select **Cut-Over** under **All migrations in group**. Any VMs without a valid target environment, and any VMs not in the **Active (Current cycle: XX%)** or **Active (Idle)** state, are ignored.

     2. For one or more selected VMs, from the **Cut-Over and Test-Clone** drop-down, select **Cut-Over** under **Selected migrations**. All selected VMs must have a valid target environment and be in the **Active (Current cycle: XX%)** or **Active (Idle)** state.

The **Test-Clone/Cut-Over status** column shows the status of the operation along with one of the sub-steps detailed in the [cut-over sub-steps table](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#cut-over_details).

Migrate to Virtual Machines performs the following actions when you initiate a cut-over:

     1. If data replication is active, waits for it to complete.

     2. Shuts down the source VM.

     3. Performs the final data replication cycle. Because continuous replication occurs throughout all migration phases, the amount of data to replicate shouldn't be very large.

     4. Creates the Persistent Disk volumes hosting the migrated VM from the final replicated data.

     5. Stops data replication.

  6. Wait for the **Test-Clone/Cut-Over status** column to show **Succeeded**. This indicates that the cut-over was created successfully.

You can view the cut-over history of a VM in one of the following ways:

     * Click the **Info panel** icon, ![Info panel file icon](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/images/info-panel-icon.png), for the VM. On the panel that opens from the right, the **Monitoring** tab displays the history, including the name of each cut-over instance.
     * Click the VM to open the details page. Click **Test-Clone/Cut-Over History** to view the cut-over history of the VM along with the [sub-steps of the cut-over](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#cut-over_details).

You can cancel an active cut-over operation by selecting a VM and clicking **Cancel Cut-Over** from the **Cut-Over and Test-Clone** drop-down.

  7. Perform validation test on the VM.




### Retry cut-over

If for any reason you want to retry cut-over, follow these steps:

  1. Select a VM in the **Cut-Over** state.

  2. Select **Migration > Resume Replication**.

  3. Retry cut-over.




### Roll back from the cut-over

To rollback from cut-over, perform the following steps:

  1. Cut-over stops the original source VM in your migration source, so you must start it and redirect traffic back to the source VM.

  2. If necessary, copy new data created on the Persistent Disk volumes so that you can write it to the source VM.

  3. (Optional) Delete Persistent Disk volumes.

  4. Resume replication on the source VM. Replication resumes from the last snapshot taken.

  5. Retry cut-over.




## Step 6: Finalize a migration

The replication data used to create Persistent Disk volumes is retained after cut-over to allow you to resume replication from the last replication snapshot.

However, you are charged for the storage used by the replication data until you delete it in the finalize phase. Finalizing deletes all replication data and storage resources.

The Finalize phase does not delete Persistent Disk volumes. If you created Persistent Disk volumes during the testing phase, you must manually delete them. You are charged for those test-clone Persistent Disk volumes until they are deleted.

To finalize a migration, follow these steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Groups** tab.

A table of available groups appears.

  3. Select a group.

A table of available source VMs appears.

  4. Select the VMs in the group to finalize:

     1. Select an individual VM. If the VM is in the **Cut-Over** state then the **Finalize** button is enabled.

     2. Select multiple VMs in the group. If all selected VMs are in the **Cut-Over** state then the **Finalize** button is enabled.

     3. To finalize all VMs in the group, from the **Group Operations** drop-down, select **Finalize**. Any VMs not in the **Cut-Over** state are ignored.

  5. Click **Finalize** and then confirm the finalize.

After finalize phase completes, the state of the VM is set to **Finalized**. The only allowed operations on a migration in the **Finalized** state are:

     * Delete the migration
     * Add to or remove from a group



## Remove a VM from a group

When you remove a VM from a group, you can either move it to another group or remove it from all groups.

After removing a VM from a group, you can still manage its migration from the **Disk Migrations** tab.

To remove a VM from a group, follow these steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Groups** tab.

  3. Select a group.

  4. Remove VMs:

     1. **To remove all VMs from the group** , from the **Group Assignment** drop-down, select **Move to group** or **Remove from group** under **All migrations in group**.

     2. **To remove a subset of VMs** , select the required VMs and then from the **Group Assignment** drop-down select **Move to group** or **Remove from group** under **Selected migrations**.




## Delete a group migration or a group

You can delete a group or a migration associated with a VM in a group.

Deleting a group has no effect on the individual VMs in the group. When you delete the group, all migration information for the individual VMs is retained and you can continue with migrating the individual VMs.

Deleting a migrating VM removes:

  * The replication data for the VM stored on Google Cloud
  * The Persistent Disk configuration information
  * The monitoring history
  * All other data associated with migrating the VM
  * The VM from the list of onboarded VMs on the **Groups** and **Migrations** tabs
  * The VM from its group



However, deleting a migration does not remove the source VM from the list of available VMs for the migration source displayed on the **Sources** tab. That is, only the migration data for the VM is deleted. The original source VM itself is not affected when you delete a migration. That means you can later onboard the source VM again to migrate it.

To delete a group, follow these steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Groups** tab.

A table of available groups appears.

  3. Select the checkbox in the table for the group.

  4. Click **Delete** and then confirm the deletion.




To delete the migration associated with one or more group VMs:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Groups** tab.

  3. Select a group.

  4. Select the checkbox for one or more VMs in the group.

  5. Click **Delete** and then confirm the deletion.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
