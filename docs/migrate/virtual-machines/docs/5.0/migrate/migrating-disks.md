---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-disks/
title: Migrate VM disks and attach them to a new VM \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:07:08.313522+00:00
---

# Migrate VM disks and attach them to a new VM  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-disks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Migrate VM disks and attach them to a new VM Stay organized with collections  Save and categorize content based on your preferences. 

Migrate to Virtual Machines lets you migrate disks from source virtual machine (VM) instances to Persistent Disk volumes on Google Cloud, with minimal interruptions to the workload. You can also create a new VM instance and attach the migrated Persistent Disk volumes to it.

## Migration process

The following are the steps of the disk migration process:

  1. **Onboard** : Select the VM whose disks you want to migrate.

  2. **Replicate** : Replicate data from the disks of the source VM to Persistent Disk volumes on Google Cloud. Data replication is a continuous process that takes place in the background until the final cut-over or you deleting the migration.

  3. **Set VM target details** : Configure settings for the migrated Persistent Disk volumes. If you choose to create a new VM instance to attach the Persistent Disk volumes to, you must configure the setting for the VM instance as well.

  4. **Clone disks to target** : Create a clone of the source VM's disk based on target details.

  5. **Cut-over disks to target** : Migrate disks from the source VM. This process includes stopping the source VM and performing a final replication of the disks.

  6. **Finalize** : Clean up all resources consumed by the migration following a successful cut-over operation.




The disk migration process follows the same steps as the VM migration process. Therefore, you can choose to switch from VM migration to disk migration and the other way around at any point during the migration process. For more information, see Switch from disk migration to VM migration.

**Note:** You can migrate your VM's boot disk as a data disk using the disk migration process in cases where OS adaptation is not needed. If you want to migrate the boot disk with the OS (to be able to use it as a boot disk), then [VM migration](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms) is more suitable.

## Prerequisites

Perform the following steps to configure the migration environment on your [migration source](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/architecture#migration_sources_and_targets) and [migration target](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/architecture#migration_targets).

  * [Enable Migrate to Virtual Machines services](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/enable-services).
  * (Only for VMware VM migration) [Install the Migrate Connector](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrate-connector).



## Step 1: Onboard a VM

Disk migration is performed at the VM level, and so the first phase of migration is to onboard the source VM. For example, a vSphere data center might contain many VMs. Onboard only the VMs whose disks you want to migrate.

You can have up to 200 migrations in progress at a time (excluding migrations in the Finalize phase), per host project and region. The limitation is for migrating disks from VMs of all source types. For example, you can migrate disks attached to 100 VMs from a VMware source and 100 additional VMs from AWS at the same time.

To onboard a source VM, follow these steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Sources** tab.

  3. From the drop-down list, select the migration source from which you want to migrate disks.

Below the drop-down you see the **Source status** of the migration source as follows:

     * **Active** : The source is active and connected to Migrate to Virtual Machines.
     * **Offline** : The source is unavailable.
     * **Pending** : The source is in the process of being connected and verified.

If you don't see any entries in the drop-down list, it indicates that you have not configured the migration source properly. Review the steps for your setting your migration source and try again.

  4. A table appears showing the source VMs in the migration source available for migration. Select one or more source VMs.

The **VM Power Status** column shows the status as **Suspended** , **On** , or **Off**. You can migrate a VM with any of these statuses.

  5. Click **Add Migrations** > **Disk Migration**.

  6. Confirm that you want to create the migration.

After you create a migration, the **Replication status** column for a VM displays one of the following:

     * **Pending** : VM is in the process of being onboarded.
     * **Ready** : VM is onboarded but has not started replicating yet.



You can now start replication of the VM as described in the next step.

## Step 2: Start replication of the source VM

After onboarding a source VM, start replicating the disk data from the source VM to Google Cloud. This process takes place in the background with no disruption to the workload.

Data replication is comprised of two steps, follow these steps:

  1. **First replication step** : Migrate to Virtual Machines creates the initial snapshot of the source VM data disks and replicates the snapshot data to Google Cloud. Depending on the amount of disk data on the source VM, the first replication can take minutes or hours to complete.

The **Replication status** column of a VM on the first replication step displays the **First sync** status followed by the appropriate sub-step.

  2. **Incremental replication step** : Following a successful first replication step, incremental replication steps occur at set time intervals (every two hours by default). In each step, a new snapshot is created for each data disk. Only data updates that occurred after the previous step are replicated to Google Cloud using the Change Block Tracking (CBT) mechanism.

The **Replication status** column of a VM on an incremental replication step displays the **Active** status followed by the appropriate sub-step.




### Initiate replication of a source VM

To initiate replication of a source VM, follow these steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **VM Disk Migrations** tab.

A table appears showing the source VMs along with the disks attached to each VM. You can start replication of the disks on any VM with the replication status **Ready**.

**Note:** Replications are performed at the VM-level. When you replicate a VM, all the disks on the VM are replicated. You cannot select individual disks on a VM to replicate. However, you can select individual disks to create in a test-clone or cut-over phases.
  3. Select one or more source VMs.

  4. Click **Migration > Start Replication**. The **Replication status** column shows replication status along with one of the sub-steps detailed in the [replication cycle sub-steps table](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#replication_cycle_details).

To view the replication history of a VM, click the VM to open the details page. Click **Replication History** to view the replication history of the VM along with the [sub-steps of the replication](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#replication_cycle_details).

Migrate to Virtual Machines saves and displays up to 100 cycles of replication history for a VM.

  5. You can now configure a migration target for the test-clone and cut-over phases.




You can create a test-clone of a disk at any time after the first replication step completes. Replication continues until you explicitly end it during the cut-over phase.

### Pause replication

At any time, you can pause replication for a VM. When you pause replication for a VM, its **Replication status** changes to **Paused**.

To pause replication, follow these steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **VM Disk Migrations** tab.

A table of available source VMs appears.

  3. Select one or more VMs.

  4. Select **Pause**.

To later resume replication, select one or more VMs and then select **Resume**.




### Set the replication interval

To set the replication interval, follow these steps:

By default, Migrate to Virtual Machines performs a replication of the source VM every 2 hours. To set the replication interval, perform the following steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **VM Disk Migrations** tab.

A table of available source VMs appears.

  3. For the VM, select the **Edit Target Details** button. A panel opens to let you configure the target.

  4. Select the **Target Details** tab.

  5. In the **Replication policy** area, set the replication frequency, in seconds.

  6. Select **Save**.




To set the frequency for multiple VMs, select the VMs and then select the **Edit Target Details** button. A panel opens to let you configure the replication frequency of the selected VMs.

### Switch from disk migration to VM migration

You can switch between disk migration and VM migration at any time during the migration process. To switch from disk migration to VM migration, follow these steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **VM Disk Migrations** tab.

  3. Select one or more VMs.

  4. Click **Migration > Convert to VM migration**.




Switching from disk migration to VM migration clears out the target details. This is because the target details for disk migration and VM migration are different. However, the replication progress isn't lost during the switch.

You must update the target details before you clone or cut-over operations on your VM in order for the migration to succeed. For more information, see Configuring the target.

## Step 3: Configure the target for a migrated VM disk

Migrate to Virtual Machines lets you migrate the disks of a source VM to Persistent Disk volumes on Google Cloud with the following options:

  * Migrate the disks to Persistent Disk volumes

  * Migrate the disks to Persistent Disk volumes and attach them to a new VM instance




You must configure the target details such as project, zone, disk type, and more based on the option you choose. The target project is the project that contains the Persistent Disk volumes migrated from the source VM, or the newly created VM instance to which you want to attach the migrated Persistent Disk volumes. You can modify the target details at any time. When you create a test-clone or cut-over, Migrate to Virtual Machines uses the target details settings at the time of the operation.

The [host project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/enable-services#identifying_your_host_project) is automatically added as a target project so there is no need to explicitly add it. If you want to add an additional project as a target project, see [Adding a target project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project).

To configure the Persistent Disk target, follow these steps:

  1. If you have not done so already, add the target project as shown in [Adding a target](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project).

  2. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  3. Select the **VM Disk Migrations** tab.

A table of migrations appears.

  4. Select a source VM (you can select multiple VMs to edit) and click **Edit target details**. On the panel that appears, configure the target details for all of your selected VMs.

  5. Set the **Target details** that define the characteristics of the Persistent Disk volumes to which you want to migrate your data. The following table lists those settings in detail.

Section title | Field name | Description  
---|---|---  
**General** | Project | The name of the project hosting the Persistent Disk volumes. It must be a project you have already added earlier in this section.  
| Zone | Zone for the Persistent Disk volumes. See [ Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).  
  
**Disk Configuration** | Name | Enter a name for the disk.   
| Disk Type | Select the type of Persistent Disk. See [ Persistent Disk types](https://docs.cloud.google.com/compute/docs/disks#disk-types).   
| Customer managed encryption key | The key you want to use to protect your data in Google Cloud. By default, Google Cloud automatically [ encrypts data when it is at rest](https://docs.cloud.google.com/security/encryption-at-rest/default-encryption) using encryption keys managed by Google. If you have specific compliance or regulatory requirements related to the keys that protect your data, you can use [ customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek) to encrypt and decrypt your data at rest. These encryption keys are created, managed, and owned by you.   
When you add a CMEK, you must also assign the [ Cloud KMS CryptoKey Encrypter/Decrypter role](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined) permissions to the Compute Engine Service Agent account you are using. For more information, see [ Protect resources by using Cloud KMS keys](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#before_you_begin).   
  
**Note:** If you've set an encryption key for your source, the same encryption key will be used here. If you've not set a key for the source, then you can't select any encryption type.   
| Labels | To organize your project, add labels as key/value pairs to your resources. See [ Labeling resources](https://docs.cloud.google.com/compute/docs/labeling-resources).  
**Attach to a VM** | Attach disks to VM | Select **Don't attach to a VM** if you don't want to attach the Persistent Disk volumes to a VM instance.  
Select **Create a VM from a disk image** if you want to create a VM instance and attach the Persistent Disk volumes to it. If you choose this option, you must set the target details that define the attributes of the new VM instance to which you want to attach the migrated Persistent Disk volumes. For more information on these settings, see [Configure the target for a VM](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms#configure-target).   
**Replication Policy** | Replication idle duration between cycles | By default, Migrate to Virtual Machines performs a replication of the source VM every 2 hours. Set the replication frequency (in seconds).  
**Note:** The replication cycle idle time counter starts after the previous replication cycle ends.  
  6. Click **Save**.




## (Optional) Step 4: Test a clone of a migrating disk

In the test-clone phase, you can check if the Persistent Disk volumes created during the replication phase are functioning as expected. For example, you can attach the migrated Persistent Disk volumes to a Compute Engine instance in your target environment to check if the disks are working as expected.

If you have created a new VM instance and attached the migrated Persistent Disk volumes to it, Migrate to Virtual Machines deploys a clone of the VM instance to a Compute Engine instance in your target environment to test it. While the testing phase is optional, it is best practice to perform testing before you perform a cut-over to the migrated disk.

Each time you create a test-clone instance, it is cloned from the most recently completed replication cycle data using the current target details. In other words, a test-clone instance represents a _snapshot_ of the source VM at the time of the last completed replication cycle.

**Caution:** New replication data and modifications to the target details are only applied to _new_ test-clones, not to existing test-clones.

### Initiate your first test-clone

You can create your first test-clone after the initial replication cycle completes, and then create additional test-clones throughout your migration process.

In order for you to initiate a test-clone, you must have already configured a target environment for the Persistent Disk volumes or the new VM instance to which you want to attach the migrated Persistent Disk volumes. For more information, see Configuring the target.

You can only test a VM in the **Paused** state if it has completed at least one replication.

For more information on potential issues during the test-clone phase, see the [Troubleshooting](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/support/troubleshooting) section.

### Create a test-clone of the disks of a VM

To create a test-clone of the disks of a VM using Migrate to Virtual Machines, use the following steps:

  1. Verify that you have configured a testing target environment as described in Configuring VM target.

**Note:** You can only test-clone a disk with a valid target environment.
  2. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  3. Select the **VM Disk Migrations** tab.

A table of available source VMs appears. You can test any VM that is in the **Active (Current cycle: XX%)** or **Active (Idle)** state. The **Active** state means the first replication sync of the VM succeeded and VM data is being incrementally replicated.

  4. Select a VM.

  5. Select **Cut-Over and Test-Clone > Test-Clone**. The **Test-Clone/Cut-Over status** column shows the status of the operation along with one of the sub-steps detailed in the [test-clone sub-steps table](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#test-clone_details).

  6. Wait for the **Test-Clone/Cut-Over status** column to show **Succeeded**. This indicates that the clone was created successfully.

You can view the test-clone history of a VM in one of the following ways:

     * Click the **Info panel** icon, ![Info panel file icon](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/images/info-panel-icon.png) for the VM. On the panel that opens from the right, the **Monitoring** tab displays the history, including the name of each test-clone instance.

     * Click the VM to open the details page. Click **Test-Clone/Cut-Over History** to view the test-clone history of the VM along with the [sub-steps of the test-clone](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#test-clone_details).

You can cancel an active test-clone operation by clicking **Cut-Over and Test-Clone** > **Cancel Test-Clone**.

  7. You can now create any VM and attach the test-clone disks to it to check if the migrated disks are working as expected.

  8. After you have completed testing, delete the VM instance to free up resources so that you are no longer charged for the instance.




### Manage multiple test-clones

Over the duration of your migration journey, you might create multiple test-clones. For example, you create the first test-clone after the initial replication cycle. Then, as you refine your migration, you create new test-clones because of the following:

  * Modifications you make to your source VM to support migration
  * Modifications you make to the target details
  * New replication data from the source VM
  * Any other changes you make over the duration of your testing cycle



Remember that a test-clone is a **snapshot** of the source VM created from the current replication data and target details. New replication data and modifications to the target details are only applied to **new** test-clones, not to existing test-clones.

If you have an existing test-clone instance running, then before you create a new test-clone you can either:

  * Delete the existing test-clone instance and create a new one with the same instance name. You cannot create a new instance with the same name as an existing instance.

  * Edit the target details to set new unique names for the disks.




To monitor all test-clone instances, follow these steps:

  1. View the test-clone history of a VM in one of the following ways:

     * Click the **Info panel** icon, ![Info panel file icon](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/images/info-panel-icon.png) for the VM. On the panel that opens from the right, the **Monitoring** tab displays the history, including the name of each test-clone instance.

     * Click the VM to open the details page. Click **Test-Clone/Cut-Over History** to view the test-clone history of the VM along with the [sub-steps of the test-clone](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#test-clone_details).

After you create a test-clone, it is up to you to manage it. If you want to modify or delete a running test-clone disk or the VM instance you created to test the disk, you must use the respective product's tools. You cannot manage these resources using Migrate to Virtual Machines tools.




## Step 5: Create a cut-over

In the cut-over phase, you transfer control to your migrated disk, or the new VM you created with the migrated Persistent Disk volumes attached to it, in your target environment on Google Cloud.

The cut-over process, follow these steps:

  1. If data replication is active, that is, the **Replication status** of the VM is **Active (Current cycle: XX%)** , waits for it to complete.

**Note:** To perform cut-over, replication cannot be paused.
  2. Shuts down the source VM.

  3. Performs the final data replication. Because replication occurs throughout all migration phases, the amount of data to replicate shouldn't be very large.

  4. Stops replication.

  5. Creates the Persistent Disk volumes from the final replicated data.

**Note:** You must have already configured the Persistent Disk target details before you can initiate a cut-over. For more information, see Configuring the target.



The cut-over phase includes a short VM downtime and should take place during a scheduled maintenance window. You must determine the maintenance window during which you can stop the source VM and redirect traffic to the migrated disk.

### Create a cut-over

To create a cut-over, perform the following steps:

  1. Verify that you have configured the target details as described in Configuring VM target. If the target details were previously configured for test-clone operation, you might want to edit the target details to point to a new target.

**Note:** You can only cut-over a VM with a valid target environment.
  2. Open the Migrate to Virtual Machines page in the Google Cloud console.

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  3. Select the **VM Disk Migrations** tab.

A table of available source VMs appears. You can cut-over any VM that is in the **Active (Current cycle: XX%)** or **Active (Idle)** state. The **Active** state means the first replication sync of the VM succeeded and VM data is being incrementally replicated.

     * The **Estimated cut-over time** column shows an estimate of the time it takes to complete a cut-over job for a VM after you initiate a cut-over. This field is populated only for an active VM that has completed a few replication cycles.

     * The **Test-Clone/Cut-Over status** column shows the status of the operation along with one of the sub-steps detailed in the [cut-over sub-steps table](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#cut-over_details).

  4. Select a source VM.

  5. Select **Cut-Over and Test-Clone > Cut-Over**. Initiating a cut-over on a VM starts the following sequence of actions performed by Migrate to Virtual Machines:

     1. Shuts down the source VM.

     2. Performs the final data replication. Because continuous replication occurs throughout all migration phases, the amount of data to replicate shouldn't be very large.

     3. Creates the Persistent Disk volumes hosting the migrated VM from the final replicated data.

     4. Stops data replication.

  6. Wait for the **Test-Clone/Cut-Over status** column to show **Cut-over** job completed. This indicates that the cut-over succeeded.

You can view the cut-over history of a VM in one of the following ways:

     * Click the **Info panel** icon, ![Info panel file icon](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/images/info-panel-icon.png), for the VM. On the panel that opens from the right, the **Monitoring** tab displays the history, including the name of each cut-over instance.

     * Click the VM to open the details page. Click **Test-Clone/Cut-Over History** to view the cut-over history of the VM along with the [sub-steps of the cut-over](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#cut-over_details).

You can cancel an active cut-over operation by clicking **Cut-Over and Test-Clone > Cancel Cut-Over**. However, if you want to resume use of the source VM, you must manually restart the VM.

  7. Perform validation test on the migrated disks.




### Retry cut-over

If for any reason you want to retry cut-over, follow these steps:

  1. Select a VM in the **Cut-Over** state.

  2. Select **Migration > Resume Replication**.

  3. Retry cut-over.




### Roll back from the cut-over

To rollback from cut-over, follow these steps:

  1. Cut-over stops the original source VM in your migration source, so you must start it and redirect traffic back to the source VM.

  2. If necessary, copy new data created on the Persistent Disk volumes so that you can write it to the source VM.

  3. (Optional) Delete Persistent Disk volumes.

  4. Resume replication on the source VM. Replication resumes from the last snapshot taken.

  5. Retry cut-over.




## Step 6: Finalize a migration

The replication data used to create Persistent Disk volumes is retained after cut-over to allow you to resume replication from the last replication snapshot. However, you are charged for the storage used by the replication data until you delete it in the finalize phase. Finalizing deletes all replication data and storage resources.

The Finalize phase does not delete Persistent Disk volumes. If you created Persistent Disk volumes during the testing phase, you must manually delete them. You are charged for those test-clone Persistent Disk volumes until they are deleted.

To finalize a migration, follow these steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **VM Disk Migrations** tab.

A table of available source VMs appears. Finalize can be performed only on VMs in the **Cut-Over** state.

  3. Select a source VM.

  4. Click **Finalize** and then confirm the finalize.

After finalize phase completes, the state of the VM is set to **Finalized**. The only allowed operations on a migration in the **Finalized** state are:

     * Delete the migration
     * Add to or remove from a group



## Delete a migration

Deleting a migration removes the following:

  * The replication data for the VM stored on Google Cloud
  * The Persistent Disk configuration information
  * The monitoring history
  * All other data associated with migrating a disk
  * The VM from the list of onboarded VMs on the **VM Disk Migrations** tab
  * The VM from its group, if the VM is a member of a group



However, deleting a migration does not remove the source VM from the list of available VMs for the migration source displayed on the **Sources** tab. That is, only the migration data for the VM is deleted. The original source VM itself is not affected when you delete a migration.That means you can later onboard the source VM again to migrate it.

To delete a migration, follow these steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **VM Disk Migrations** tab.

  3. Select a source VM.

  4. Click **Delete** and then confirm the deletion.

The VM is removed from the Migration table.

  5. Select the **Sources** tab.

  6. From the drop-down list, select the migration source that you want to delete.

  7. A table appears showing the source VMs in the migration source available for migration. Notice that the source VM corresponding to the deleted migration is still listed.




If necessary, you can restart a disk migration on the VM.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
