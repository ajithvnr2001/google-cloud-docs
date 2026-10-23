---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms/
title: Migrate individual VMs \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:03.477058+00:00
---

# Migrate individual VMs  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Guides ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle)



Send feedback 

#  Migrate individual VMs Stay organized with collections  Save and categorize content based on your preferences. 

The migration process for an individual source VM occurs in the following phases:

  1. **Onboard** : Select the VMs to migrate.

  2. **Replicate** : Replicate data from the source VM to Google Cloud. Data replication is a continuous process that takes place in the background until the final cut-over or you deleting the migration.

  3. **Set VM target details** : Configure settings for the migrated VM, such as the project, instance type, memory, network, and more.

  4. **(Optional) Test-clone** : Create a clone of the source VM from the replication data and test it on Google Cloud.

  5. **Cut-over** : Migrate the source VM. This process includes stopping the source VM, performing a final replication, and creating the production instance from the source VM.

  6. **Finalize** : Clean up all resources consumed by the migration following a successful cut-over operation.




For a complete description of each of these phases, see [VM migration process](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/lifecycle). The VMs that you create during the migration process are called migrating VMs, and they exist in various states during and after a migration.

You should also see [Migration progress details](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details) for more insight into how to monitor progress during your migration journey.

The VM migration process follows the same steps as that of the disk migration process. Therefore, you can choose to switch from VM migration to disk migration and the other way around at any point during the migration process. For more information, see Switch from VM migration to disk migration.

This document describes the phases of migrating a source VM to Google Cloud.

## Prerequisites

Perform the following steps to configure the migration environment on your [migration source](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/architecture#migration_sources_and_targets) and [migration target](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/architecture#migration_targets).

  * [Enabling Migrate to Virtual Machines services](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/enable-services).
  * (Only for VMware VM migration) [Installing the Migrate Connector](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrate-connector).
  * Some Compute Engine features require agents and services running on the VM. These agents and services are installed automatically during the migration. However, certain security features such as SELinux, anti-viruses, and firewalls, may interfere with these services and prevent certain features from functioning. In order to make sure that the guest environment functions properly, follow the steps in [Loaded services for the guest environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment#wgei_services) and if needed, the [Troubleshooting steps for Compute Engine](https://docs.cloud.google.com/compute/docs/troubleshooting).

**Note:** You need at least 128 MB of free space in the boot partition of a VM that you want to migrate to Google Cloud.

## Licensing

Compute Engine supports premium pay as you go (PAYG) licenses and bring your own (BYOL) licenses, based on the operating system of the source VM. PAYG licenses are billed based on the resources that you use.

See [Supported operating systems](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/supported-os-versions) for details on licensing for all supported operating system.

## Step 1: Onboard a VM

The first phase of migration is to onboard the source VM. For example, a vSphere data center might contain tens, hundreds, or even thousands of VMs. Onboard only the VMs that you want to migrate.

You can have up to 200 migrations in progress at a time (excluding migrations in the Finalize phase), per host project and region. This limitation is for migrating VMs of all source types. For example, you can migrate 100 VMs from a VMware source and 100 additional VMs from AWS at the same time.

**Note:** When migrating VM instances with 16 or more disks to regions that don't support N2 machines, we recommend that you migrate fewer than 200 VMs concurrently to avoid any issues. You can also contact Migrate to Virtual Machines support for help.

To onboard a source VM, follow these steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Sources** tab.

  3. From the drop-down list, select the migration source from which you want to migrate a VM.

Below the drop-down you see the **Source status** of the migration source as:

     * **Active** : The source is active and connected to Migrate to Virtual Machines.
     * **Offline** : The source is unavailable.
     * **Pending** : The source is in the process of being connected and verified.

If you don't see any entries in the drop-down list, it indicates that you have not configured the migration source properly. Review the steps for your setting your migration source and try again.

  4. A table appears showing the source VMs in the migration source available for migration. Select one or more source VMs.

The **VM Power Status** column shows the status as **Suspended** , **On** , or **Off**. You can migrate a VM with any of these statuses.

  5. Click **Add Migrations** > **VM Migration**.

  6. Confirm that you want to create the migration.

After you create a migration, the **Replication status** column for a VM displays one of the following:

     * **Pending** : VM is in the process of being onboarded.
     * **Ready** : VM is onboarded but has not started replicating yet.
  7. You can now start replication of the VMs as described in the next step.




## Step 2: Start replication of the source VM

After onboarding a source VM, start replicating the disk data from the source VM to Google Cloud. This process takes place in the background with no disruption to the workload.

Data replication is comprised of two steps:

  1. **First replication step** : Migrate to Virtual Machines creates the initial snapshot of the source VM data disks and replicates the snapshot data to Google Cloud. Depending on the amount of disk data on the source VM, the first replication can take minutes or hours to complete.

The **Replication status** column of a VM on the first replication step displays the **First sync** status followed by the appropriate sub-step.

  2. **Incremental replication step** : Following a successful first replication step, incremental replication steps occur at set time intervals (every two hours by default). In each step, a new snapshot is created for each data disk. Only data updates that occurred after the previous step are replicated to Google Cloud using the Change Block Tracking (CBT) mechanism.

The **Replication status** column of a VM on an incremental replication step displays the **Active** status followed by the appropriate sub-step.




### Initiate replication of a source VM

To initiate replication of a source VM, follow these steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Migrations** tab.

A table appears showing the source VMs in the migration source that you have onboarded. You can start replication on any VM with the replication status **Ready**.

  3. Select one or more source VMs.

  4. Click **Migration > Start Replication**. The **Replication status** column shows replication status along with one of the sub-steps detailed in the [replication cycle sub-steps table](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#replication_cycle_details).

To view the replication history of a VM, click the VM to open the details page. Click **Replication History** to view the replication history of the VM along with the [sub-steps of the replication](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#replication_cycle_details).

**Note:** Migrate to Virtual Machines saves and displays up to 100 cycles of replication history for a VM.
  5. You can now configure a migration target for the test-clone and cut-over phases.




Migrate to Virtual Machines generates an adaptation report after your replication cycle is complete. For more information about adaptation reports, see the [adaptation report](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#adaptation_report) documentation.

You can create a test-clone at any time after the first replication step completes. Replication continues until you explicitly end it during the cut-over phase.

### Pause replication

To pause replication, follow these steps:

At any time, you can pause replication for a VM. When you pause a VM, its **Replication status** changes to **Paused**.

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Migrations** tab.

A table of available source VMs appears.

  3. Select one or more VMs.

  4. Select **Pause**.

To later resume replication, select one or more VMs and then select **Resume**.




### Set the replication interval

To set the replication interval, follow these steps:

By default, Migrate to Virtual Machines performs a replication of the source VM every 2 hours. To change the replication frequency:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Migrations** tab.

A table of available source VMs appears.

  3. For the VM, select the **Edit Target Details** button. A panel opens to let you configure the target.

To set the frequency for multiple VMs, select the VMs and then select the **Edit Target Details** button. A panel opens to let you configure the replication frequency of the selected VMs.

  4. Select the **Target Details** tab.

  5. In the **Replication policy** area, set the replication frequency, in seconds.

  6. Select **Save**.




### Switch from VM migration to disk migration

You can switch between VM migration and disk migration at any time during the migration process.

To switch from VM migration to disk migration, follow these steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Migrations** tab.

  3. Select one or more VMs.

  4. Click **Migration > Convert to disk migration**.




Switching from VM migration to disk migration clears out the target details. This is because the target details for VM migration and disk migration are different. However, the replication progress won't be lost during the switch.

You must update the target details before you clone or cut-over operations on your VM in order for the migration to succeed. For more information, see Configuring the target.

## Step 3: Configure the target for a migrated VM

To configure a target, perform two main steps:

  1. Add a target project. The target project is the project that contains the [Compute Engine](https://docs.cloud.google.com/compute/docs/how-to) instance used to host the migrated VM.

The [host project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/enable-services#identifying_your_host_project) is automatically added as a target project so there is no need to explicitly add it. If you want to add an additional project as a target project, see [Adding a target project](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project).

  2. Configure the [Compute Engine](https://docs.cloud.google.com/compute/docs/how-to) instance used to host the migrated VM. For both a test and a production environment, configure the target Compute Engine instance to specify settings including:

     * Google project
     * Number of CPUs
     * Amount of memory



This section describes how to set the initial configuration of the [Compute Engine](https://docs.cloud.google.com/compute/docs/how-to) instance used to host the migrated VM. However, there are many additional settings that you can apply to a Compute Engine instance. See the [Compute Engine documentation](https://docs.cloud.google.com/compute/docs/how-to) for detailed descriptions of all settings.

You can modify the target details at any time. When instantiating a Compute Engine instance for either the test-clone or cut-over phase, Migrate to Virtual Machines uses the target details settings at the time of the operation.

To configure the Compute Engine target, follow these steps:

  1. If you have not done so already, add the target project as shown in [Adding a target](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-project).

  2. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  3. Select the **Migrations** tab.

A table of migrations appears.

  4. Select a VM (you can select multiple to edit) and then select the **Edit target details** button. On the panel that appears, configure the target details for all of your selected VMs.

  5. Set the **Target details** that define the characteristics of the Compute Engine instance used to host the migrated VM. The following table lists those settings and provides links to the [Compute Engine documentation](https://docs.cloud.google.com/compute/docs/how-to) for detailed descriptions.

Migrate to Virtual Machines does not support all Compute Engine settings. You can only set those described in the following table. After the Compute Engine instance is created, you can modify all of its settings:

Section title | Field name | Description  
---|---|---  
**General** | 

###### Instance name

| The name of the Compute Engine instance. See [ Resource naming convention](https://docs.cloud.google.com/compute/docs/naming-resources#resource-name-format) for the naming rules.  
| 

###### Project

| The name of the project hosting the Compute Engine instance. It must be a project you have already added earlier in this section.  
| 

###### Zone

| Zone for the Compute Engine instance. See [ Regions and Zones](https://docs.cloud.google.com/compute/docs/regions-zones).  
The region of the deployed instance is the one you specified when you registered the Migration Connector. See [ Installing the Migration Connector](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrate-connector) for more.   
**Note:** When migrating VM instances with 16 or more disks to regions that don't support N2 machines, we recommend that you migrate fewer than 200 VMs concurrently to avoid any issues. You can also contact Migrate to Virtual Machines support for help.   
| 

###### Labels

| To organize your project, add labels as key/value pairs to your resources. See [ Labeling resources](https://docs.cloud.google.com/compute/docs/labeling-resources).  
**Machine configuration** | 

###### Machine type series

| Compute Engine offers [ predefined machine type series](https://docs.cloud.google.com/compute/docs/machine-types#predefined_machine_types) that you can use when you create an instance. Each option has a different cost. Select the machine type series that is most appropriate for your workload.  
See [Pricing](https://cloud.google.com/compute/all-pricing) for more information.  
Migrate to Virtual Machines determines the OS type of the Compute Engine instance automatically based on the source VM and applies PAYG licensing to the instance. See [ Licensing](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms#licensing).  
| 

###### Machine type

| Compute Engine offers predefined machine types that you can use when you create an instance. The available machine types depend on the machine series you select in the _Machine type series_ field.  
See [ predefined machine types](https://docs.cloud.google.com/compute/docs/machine-types#predefined_machine_types) documentation for more information.  
| 

###### On host maintenance

| When Compute Engine performs periodic infrastructure maintenance, it can migrate your VM instances to other hardware without downtime. Set this option to Migrate VM Instance (Recommended), the default, to migrate the VM. Set it to Terminate to terminate the instance.  
| 

###### Automatic restart

| When set to **On** (Recommended), the default, Compute Engine automatically restarts instances when they are terminated for non-user-initiated reasons, such as a maintenance event, hardware failure, or software failure. Set it to **Off** to disable restart.  
| 

###### Metadata

| Specify VM metadata key/value pairs that will be stored for your migrated VM.  
For more information about Compute Engine VM metadata, see the [VM metadata](https://docs.cloud.google.com/compute/docs/metadata/setting-custom-metadata) documentation.  
Migrate to Virtual Machines enforces a limitation of **64K** characters for all metadata key/value pairs in each migrated VM.  
**Networking** | 

###### Network name

| Specify the [VPC](https://docs.cloud.google.com/vpc/docs/vpc) network that the instances will be part of.  
| 

###### Subnetwork name

| Specify the subnet associated with a region. This must be a subnetwork of the specified Network.  
| 

###### External IP address

| Set to None (default) to disable external access, and to Ephemeral to allow gcloud CLI to assign an IP address. See [Configure static external IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-external-ip-address).  
| 

###### Internal IP address

| Set to Ephemeral (Automatic) (default) to allow gcloud CLI to assign an IP address, Ephemeral (Custom) to set your own IP address, or reserved-internal-ip (IP) to use a predefined IP address. See [Configure static internal IP addresses](https://docs.cloud.google.com/compute/docs/ip-addresses/configure-static-internal-ip-address).  
| 

###### Hostname

|  You can create a VM with a custom hostname by specifying any fully qualified DNS name. Custom hostnames must conform to [RFC 1035](https://datatracker.ietf.org/doc/html/rfc1035) requirements for valid hostnames.  For more information about formatting custom hostnames, see the [Custom hostname](https://docs.cloud.google.com/compute/docs/instances/custom-hostname-vm) documentation.  You can change the hostname for Windows VMs using the [TargetDetails API](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeEngineTargetDetails). After changing a Windows VM hostname locally, make sure that you update the hostname in the Active Directory (AD) so that AD trust doesn't break.   
| 

###### Add Network Interface

| Migrate to Virtual Machines lets you optionally create a Compute Engine instance with multiple network interfaces (NICs). Each interface is attached to a unique subnet in a VPC network, giving that instance access to one or more VPC networks in gcloud CLI. If you don't choose a network interface, the machine image is attached to the default network and subnet of the project in a region.   
Before you add additional network interfaces, be aware of the following considerations:  

     * Attaching multiple network interfaces to the same VPC network is supported only if the additional network interfaces are attached to the same VPC network as the `nic0` interface. While other configurations may save, the instantiation of the VM will fail.
     * After a Compute Engine instance is instantiated, by using `test-clone` or `cut-over`, you cannot add or remove a network interface on the created instance. You can repeat `test-clone` or `cut-over` with different target details to recreate the instance.  
To add or remove a network interface: 
       * Select **Add network interface** to add an additional network interface to the Compute Engine instance. You can set all of the same options as you do with the initial network interface.  

For more information, see [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts) and [Creating instances with multiple network interfaces](https://docs.cloud.google.com/vpc/docs/create-use-multiple-interfaces).   
| 

###### Network tags

| Tags enable you to make [firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) and [routes](https://docs.cloud.google.com/vpc/docs/routes) applicable to specific instances. See [Configuring network tags](https://docs.cloud.google.com/vpc/docs/add-remove-network-tags).  
**Additional configuration** | 

###### Service account

| Specify the service account on the target project used to run the Compute Engine instance. By default, no service account is assigned to the Compute Engine instance.  
If you plan to run an application on the Compute Engine instance that needs access to other gcloud CLI services and APIs, [create a service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#createanewserviceaccount) in the target project with the necessary permissions to access those services and APIs before creating the Compute Engine instance. Then, specify that service account here. For more information, see [set up a VM to run as a service account](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#using).  
To attach the service account to the Compute Engine instance, your user account on the Migrate to Virtual Machines host project requires the necessary permissions. See [Configuring permissions on target project service account](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/get-started/target-sa-compute-engine) for more.  
| 

###### Disk type

| Specify the storage type for the instance. See [Storage options](https://docs.cloud.google.com/compute/docs/disks). **Note:** Regional `pd-standard` disks smaller than 200 GB will be increased to 200 GB.  
| 

###### Storage pools

|  **Note:** This option is only enabled if your [disk type](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-vms#disk-type) is a [Hyperdisk Balanced disk](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced). To use Hyperdisk Balanced disks, your target VM must be on a [supported machine series](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#machine-series). Select **Enable storage pool** if you need large-scale storage for your data and want to use a Hyperdisk Storage Pool. A Hyperdisk Storage Pool is a pre-purchased collection of capacity, throughput, and input/output operations per second (IOPS) that you can then provision to your applications as needed. You can use Hyperdisk Storage Pools to create and manage disks in pools and use the disks across multiple workloads. By managing disks in aggregate, you can save costs while achieving expected capacity and performance growth. For more information on Hyperdisk Storage Pools, see [About Hyperdisk Storage Pools](https://docs.cloud.google.com/compute/docs/disks/storage-pools).   
**Note:** When you create the storage pool, make sure that it is in the same target zone and project as the target VM. Otherwise, you won't be able to associate your storage pool with the target VM.  
| 

###### Customer managed encryption key

| The key you want to use to protect your data in Google Cloud. By default, Google Cloud automatically [ encrypts data when it is at rest](https://cloud.google.com/docs/security/encryption/default-encryption) using encryption keys managed by Google. If you have specific compliance or regulatory requirements related to the keys that protect your data, you can use [ customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek) to encrypt and decrypt your data at rest. These encryption keys are created, managed, and owned by you.   
When you add a CMEK, you must also assign the [ Cloud Key Management Service CryptoKey Encrypter/Decrypter role](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#predefined) permissions to the Compute Engine Service Agent account you are using. For more information, see [ Protect resources by using Cloud KMS keys](https://docs.cloud.google.com/compute/docs/disks/customer-managed-encryption#before_you_begin).   
| 

###### Convert BIOS to UEFI

| Enable this option to convert the OS boot type of a VM instance from Basic Input/Output System (BIOS) to Unified Extensible Firmware Interface (UEFI). This option is useful when you want to securely boot your VM instance, as secure boot is only supported by UEFI. However, you can also just convert the boot type from BIOS to UEFI, without using secure boot.   
**Note:** Not all operating systems support BIOS to UEFI conversion. To see the list of operating systems that support the conversion, see the **BIOS to UEFI conversion supported** column in [Supported operating systems](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/supported-os-versions).  
| 

###### Secure boot

| All selected VMs must have an EFI boot option to enable secure boot. Compute Engine enforces up-to-date policies that may prevent your VM from loading when secure boot is enabled. For more information, see [Secure Boot](https://docs.cloud.google.com/compute/shielded-vm/docs/shielded-vm#secure-boot) in the Compute Engine documentation.  
| 

###### License type

| Compute Engine supports pay as you go (PAYG) licenses and bring your own licenses (BYOL) for your deployed VMs. The default license type for a migrated VM is assigned by Migrate to Virtual Machines based on the migrated operating system, as described in [Supported operating systems](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/supported-os-versions).  
If your operating system supports multiple license types, you can override the default license type to explicitly specify a license type of PAYG or BYOL.  
**Note:** Some operating system types, such as CentOS and Debian, don't support a license. Other operating systems only support one type of license. Attempting to set an unsupported license type causes an error when you attempt to deploy a test-clone VM or to cut-over to a production VM.  
| 

###### Additional licenses

| Migrate to Virtual Machines supports up to 10 additional licenses (using valid URL format) that you can add in the **Additional configuration** section of the **Target details** dialog.   
For example, you can add additional licenses using this URL format:   

    
    https://www.googleapis.com/compute/beta/projects/windows-sql-cloud/global/licenses/sql-server-2012-enterprise  
  
**Sole tenancy** | 

###### Node affinity labels

| Compute Engine supports the deployment of migrated workloads to [sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes). A sole-tenant node is a Compute Engine server that is dedicated to hosting only your project's VMs.  
Before you can configure your migrated workloads to run on sole-tenant nodes, you must have already created a sole-tenant node template and sole-tenant node group in the target project and zone. See [Provisioning VMs on sole-tenant nodes](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms).  
_Affinity labels_ let you logically group nodes and node groups. When provisioning your Compute Engine instances, use affinity labels to schedule your instances to run on a specific set of nodes or node groups.  
You can add affinity labels to your migrating VMs by entering them manually in the Info panel by key-value pair, or by using the Browse Node dialog to select a node or node group. You can then edit the VM affinity labels to customize the sole-tenant deployment:  

     * Select Browse Node to add an affinity label from the list of available sole-tenant nodes and node groups. A key-value pair will automatically be created for you upon selecting the node or node group.
     * Select Add New to manually enter the affinity label.  
| 

###### Minimum vCPUs allocated

| Set the Minimum vCPUs allocated for the Compute Engine instance.  
See [Node affinity and anti-affinity](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes#node_affinity_and_anti-affinity) and [Configure node affinity labels](https://docs.cloud.google.com/compute/docs/nodes/provisioning-sole-tenant-vms#configure_node_affinity_labels) for more information.  
**Replication Policy** | 

###### Replication idle duration between cycles

| By default, Migrate to Virtual Machines performs a replication of the source VM every 2 hours. Set the replication frequency (in seconds).  
**Note:** The replication cycle idle time counter starts after the previous replication cycle ends.  
  6. Select **Save**.




You can later edit the target details. When instantiating a Compute Engine instance for either the `test-clone` or `cut-over` phase, Migrate to Virtual Machines uses the target details settings at the time of the operation.

## (Optional) Step 4: Test a clone of a migrating VM

In the test-clone phase, Migrate to Virtual Machines deploys a clone of your migrated VM to a Compute Engine instance in your _testing_ environment. While the testing phase is optional, it is best practice to perform testing before deploying a migrated VM to production.

Each time you create a test-clone instance, it is cloned from the most recently completed replication cycle data using the current target details. In other words, a test-clone instance represents a _snapshot_ of the source VM at the time of the last completed replication cycle.

For Azure source VMs that have more than one disk, the Migrate to Virtual Machines replication cycles take snapshots of each disk independently of each other. As these snapshots are not taken simultaneously, the data captured might sometimes have minor discrepancies. Therefore, it is recommended that you don't use test-clones as a production replacement when you cut-over.

**Caution:** New replication data and modifications to the target details are only applied to new test-clones, not to existing test-clones.

### Initiate your first test-clone

You can create your first test-clone after the initial replication cycle completes, and then create additional test-clones throughout your migration process.

In order for you to initiate a test-clone, you must have already configured a target environment for the Compute Engine instance before you can initiate a test-clone. See Configuring the target documentation for more information.

You can only test a VM in the **Paused** state if it has completed at least one replication.

For more information on potential issues during the test-clone phase, see the [Troubleshooting](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/support/troubleshooting) section.

### Create a test-clone of a VM

To create a test-clone of a VM using Migrate to Virtual Machines, follow these steps:

  1. Verify that you have configured a testing VM target environment as shown in Configuring VM target.

**Note:** You can only test-clone a VM with a valid target environment.
  2. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  3. Select the **Migrations** tab.

A table of available source VMs appears. You can test any VM that is in the **Active (Current cycle: XX%)** or **Active (Idle)** state. The **Active** state means the first replication sync of the VM succeeded and VM data is being incrementally replicated.

  4. Select a VM.

  5. Select **Cut-Over and Test-Clone > Test-Clone**. The **Test-Clone/Cut-Over status** column shows the status of the operation along with one of the sub-steps detailed in the [test-clone sub-steps table](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#test-clone_details).

  6. Wait for the **Test-Clone/Cut-Over status** column to show **Succeeded**. This indicates that the clone was created successfully.

You can view the test-clone history of a VM in one of the following ways:

     * Click the **Info panel** icon, ![Info panel file icon](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/images/info-panel-icon.png) for the VM. On the panel that opens from the right, the **Monitoring** tab displays the history, including the name of each test-clone instance.

     * Click the VM to open the details page. Click **Test-Clone/Cut-Over History** to view the test-clone history of the VM along with the [sub-steps of the test-clone](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#test-clone_details).

You can cancel an active test-clone operation by clicking **Cut-Over and Test-Clone > Cancel Test-Clone**.

  7. For the test-clone VM, click **Show details** to view the VM instance name.

  8. To manage the running Compute Engine instance, go to the **VM instances** page in the Google Cloud console for your project:

[Go to VM instances page](https://console.cloud.google.com/compute/instances)

From the Google Cloud console manage the Compute Engine instance to:

     1. Start, stop, and delete the instance.
     2. Determine the internal and external IP address of the instance.
     3. View and modify characteristics of the instance.
     4. Perform all other management tasks.
  9. Perform any validation testing or other testing on the migrated VM.

  10. After you have completed testing, delete the Compute Engine instance to free up resources so that you will no longer be charged for the instance.




### Manage multiple test-clones

Over the duration of your migration journey, you might create multiple test-clones. For example, you create the first test-clone after the initial replication cycle. Then, as you refine your migration, you create new test-clones because of:

  * Modifications you make to your source VM to support migration
  * Modifications you make to the target details of the migrated VM
  * New replication data from the source VM
  * Any other changes you make over the duration of your testing cycle



Remember that a test-clone is a **snapshot** of the source VM created from the current replication data and target details. New replication data and modifications to the target details are only applied to **new** test-clones, not to existing test-clones.

If you have an existing test-clone instance running, then before you create a new test-clone you can either:

  * Delete the existing test-clone instance and then create a new one with the same instance name. You cannot create a new instance with the same name as an existing instance.

  * Edit the target details to set a new instance name. In addition, if you specified a reserved or custom IP address for an existing test-clone instance, make sure to use different values for any additional instances.




To monitor all test-clone instances, follow these steps:

  1. View the test-clone history of a VM in one of the following ways:

     * Click the **Info panel** icon, ![Info panel file icon](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/images/info-panel-icon.png) for the VM. On the panel that opens from the right, the **Monitoring** tab displays the history, including the name of each test-clone instance.

     * Click the VM to open the details page. Click **Test-Clone/Cut-Over History** to view the test-clone history of the VM along with the [sub-steps of the test-clone](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#test-clone_details).

  2. To manage a running Compute Engine instance, select the arrow icon arrow_right_alt to open the VM instance in the Google Cloud console.

Or, go directly to the **VM instances** page in the Google Cloud console:

[Go to VM instances page](https://console.cloud.google.com/compute/instances)

After you create a test-clone, it is up to you to manage it. If you want to modify or delete a running test-clone VM, you use the Compute Engine tools, not Migrate to Virtual Machines.




## Step 5: Create a Cut-over

In the cut-over phase, you transfer control to your migrated VM running in a Compute Engine instance in your production environment on Google Cloud.

Migrate to Virtual Machines generates an adaptation report when your cut-over cycle is complete. For more information about adaptation reports, see the [adaptation report](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#adaptation_report) documentation.

**Caution:** For Azure source VMs that have more than one disk, the Migrate to Virtual Machines replication cycles take snapshots of each disk independently of each other. As these snapshots are not taken simultaneously, the data captured might sometimes have minor discrepancies. Therefore, it is recommended that you don't use test-clones as a production replacement when you cut-over.

The cut-over process, follow these steps:

  1. If data replication is active, that is, the **Replication status** of the VM is **Active (Current cycle: XX%)** , waits for it to complete.

**Note:** To perform cut-over, replication cannot be paused.
  2. Shuts down the source VM.

  3. Performs the final data replication. Because replication occurs throughout all migration phases, the amount of data to replicate shouldn't be very large.

  4. Stops replication.

  5. Creates the Compute Engine instance from the final replicated data.

**Note:** You must have already configured the Compute Engine target details before you can initiate a cut-over. See Configuring the target for more.



The cut-over phase includes a short VM downtime and should take place during a scheduled maintenance window. You must determine the maintenance window during which you can stop the source VM and redirect traffic to the migrated VM running on Compute Engine.

To create a cut-over, follow these steps:

  1. Verify that you have configured the VM target details as shown in Configuring VM target. If the target details were previously configured for test-clone operation, you might want to edit the target details to point to a new target.

**Note:** You can only cut-over a VM with a valid target environment.
  2. Open the Migrate to Virtual Machines page in the Google Cloud console.

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  3. Select the **Migrations** tab.

A table of available source VMs appears. You can cut-over any VM that is in the **Active (Current cycle: XX%)** or **Active (Idle)** state. The **Active** state means the first replication sync of the VM succeeded and VM data is being incrementally replicated.

     * The **Estimated cut-over time** column shows an estimate of the time it takes to complete a cut-over job for a VM after you initiate a cut-over. This field is populated only for an active VM that has completed a few replication cycles.

     * The **Test-Clone/Cut-Over status** column shows the status of the operation along with one of the sub-steps detailed in the [cut-over sub-steps table](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#cut-over_details).

  4. Select a source VM.

  5. Select **Cut-Over and Test-Clone > Cut-Over**. Initiating a cut-over on a migrating VM starts the following sequence of actions performed by Migrate to Virtual Machines:

     1. Shuts down the source VM.

     2. Performs the final data replication. Because continuous replication occurs throughout all migration phases, the amount of data to replicate should not be very large.

     3. Creates the Compute Engine instance hosting the migrated VM from the final replicated data.

     4. Stops data replication.

  6. Wait for the **Test-Clone/Cut-Over status** column to show **Cut-over** job completed. This indicates that the cut-over succeeded.

You can view the cut-over history of a VM in one of the following ways:

     * Click the **Info panel** icon, ![Info panel file icon](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/images/info-panel-icon.png), for the VM. On the panel that opens from the right, the **Monitoring** tab displays the history, including the name of each cut-over instance.

     * Click the VM to open the details page. Click **Test-Clone/Cut-Over History** to view the cut-over history of the VM along with the [sub-steps of the cut-over](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migration-progress-details#cut-over_details).

You can cancel an active cut-over operation by clicking **Cut-Over and Test-Clone > Cancel Cut-Over**. However, if you want to resume use of the source VM, you must manually restart the VM.

  7. To manage a running Compute Engine instance, select the arrow icon arrow_right_alt to open the VM instance in the Google Cloud console.

Or, go directly to the **VM instances** page in the Google Cloud console:

[Go to VM instances page](https://console.cloud.google.com/compute/instances)

From the Google Cloud console manage the Compute Engine instance to:

     1. Start, stop, and delete the instance.
     2. Determine the internal and external IP address of the instance.
     3. View and modify characteristics of the instance.
     4. Perform all other management tasks.
  8. Perform validation test on the migrated workload.




If for any reason you want to retry cut-over or roll back from the cut-over:

### Retry cut-over

To retry cut-over, follow these steps:

  1. Select a VM in the **Cut-Over** state.

  2. Select **Migration > Resume Replication**.

  3. Retry cut-over.




### Rollback from cut-over

To rollback from cut-over, follow these steps:

  1. Cut-over stops the original source VM in your migration source, so you must start it and redirect traffic back to the source VM.

  2. If necessary, copy new data created on the Compute Engine instance so that you can write it to the source VM.

  3. (Optional) delete or shutdown the Compute Engine instance running the migrated VM.

  4. Resume replication on the source VM. Replication resumes from the last snapshot taken.

  5. Retry cut-over.




## Step 6: Finalize a migration

The replication data used to create a Compute Engine VM is retained after cut-over to allow you to resume replication from the last replication snapshot.

However, you are charged for the storage used by the replication data until you delete it in the finalize phase. Finalizing deletes all replication data and all other storage resources associated with a migrated VM.

The Finalize phase does not delete Compute Engine instances running a migrated VM. If you created Compute Engine instances during the testing phase, you must manually delete them. You will be charged for those test-clone instances until they are deleted.

To finalize a migration, follow these steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Migrations** tab.

A table of available source VMs appears. Finalize can be performed only on VMs in the **Cut-Over** state.

  3. Select a source VM.

  4. Select **Finalize** and then confirm the finalize.

After finalize completes, the state of the VM is set to **Finalized**. The only allowed operations on a migration in the **Finalized** state are:

     * Delete the migration
     * Add to or remove from a group



## Delete a migration

Deleting a migration removes:

  * The replication data for the VM stored on Google Cloud
  * The Compute Engine configuration information
  * The monitoring history
  * All other data associated with migrating a VM
  * The VM from the list of onboarded VMs on the **Migrations** tab
  * The VM from its group, if the VM is a member of a group



However, deleting a migration does not remove the source VM from the list of available VMs for the migration source displayed on the **Sources** tab. That is, only the migration data for the VM is deleted. The original source VM itself is not affected when you delete a migration.That means you can later onboard the source VM again to migrate it.

To delete a migration, follow these steps:

  1. Open the Migrate to Virtual Machines page in the Google Cloud console:

[Go to the Migrate to Virtual Machines page](https://console.cloud.google.com/compute/mfce)

  2. Select the **Migrations** tab.

  3. Select a source VM.

  4. Select **Delete** and then confirm the deletion.

The VM is removed from the Migration table.

  5. Select the **Sources** tab.

  6. From the drop-down list, select the migration source that you want to delete.

  7. A table appears showing the source VMs in the migration source available for migration. Notice that the source VM corresponding to the deleted migration is still listed.




If necessary, you can restart a migration on the VM.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
