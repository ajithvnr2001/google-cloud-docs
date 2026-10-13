---
url: https://docs.cloud.google.com/sap/docs/migrate-hana-to-bare-metal-instance/
title: Migrate SAP HANA to a Compute Engine bare metal instance \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:18.553808+00:00
---

# Migrate SAP HANA to a Compute Engine bare metal instance  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/migrate-hana-to-bare-metal-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Migrate SAP HANA to a Compute Engine bare metal instance Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the high-level steps for migrating SAP HANA workloads to Compute Engine bare metal machine types, available with X4 and C3. It also describes the migration methods that are recommended by Google Cloud.

This document is intended for SAP Basis and SAP system administrators who are familiar with running SAP HANA and want to migrate their SAP HANA workloads to bare metal instances on Google Cloud.

Bare metal instances on Compute Engine are consumed and managed in the same way as VM instances. For information about bare metal machines types that are certified by SAP to run SAP HANA on Google Cloud, see [Bare metal machine types for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#bare-metal-machines-for-hana).

## High-level migration steps

You can migrate SAP HANA workloads that are running on premises, on other cloud providers, on Compute Engine memory-optimized VMs, or Bare Metal Solution servers.

To migrate an SAP HANA workload to a C3 or X4 based bare metal instance, which is similar to migrating to any VM instance, you complete the following high-level steps:

  1. **Assess the readiness of your SAP HANA workload for migration.** This includes evaluating factors such as OS version, SAP HANA version, system configuration, compatibility of third-party products or services used by your workload, high availability (HA) and disaster recovery (DR) configurations.

  2. **Select your migration method.** Based on the requirements of your SAP HANA workload and the infrastructure that it's using, you need to select the most appropriate migration method. For more information, see Select your migration method.

  3. **Test and validate migration in a non-production environment.** To ensure that migrating an SAP HANA workload doesn't negatively affect the workload performance or data integrity, you must thoroughly test and validate the selected migration method in a non-production environment.

  4. **Prepare your workload for migration.** This involves tasks such as creating database backups, planning downtime, ensuring that all necessary licenses and tools are in place, and updating your license key in the target system.

  5. **Migrate your workload.** Using the selected migration method, migrate your SAP HANA workload to the required type of bare metal instances. This step can involve performing system replication, data transfer, or cutover activities.

  6. **Test and validate your workload.** Once your SAP HANA workload is successfully migrated to bare metal instances, test and validate your workload to make sure it is running as expected.




## Select your migration method

The migration method that you select for your SAP HANA workload depends on factors such as your workload's requirements, whether the workload is running on Google Cloud or not, the infrastructure in use, the system configuration (scale-up or scale-out).

The following flowchart guides you through a series of questions that you can consider to find out the most suitable migration method for your SAP HANA workload:

![Flowchart showing how you can select the method for migrating SAP HANA to Compute Engine bare metal machine types](https://docs.cloud.google.com/static/sap/docs/images/flowchart-migrate-hana-to-bm.svg)

#### How you can select your migration method

  * If you meet any of the following criteria, then we strongly recommend that you contact a Google Cloud representative for help with designing your migration method: 
    * You're new to Google Cloud.
    * Your SAP HANA workload uses a scale-out configuration.
    * Your SAP HANA workload has complex requirements, for example: 
      * You have very narrow migration and cutover windows.
      * You have advanced networking requirements, particularly for connecting from your source environment with suitable effective bandwidth for the migration.
      * You are changing the load profile of your workload. For example, you're rolling out new functionality or adding new users.
      * You are changing multiple infrastructure aspects such as deploying extra application servers, or changing interfaces.
      * You are migrating multiple systems at the same time.
  * **Migrate by changing machine type**. If your SAP HANA environment meets all of the following criteria, then you can migrate the workload by using Google tools: 
    * The workload is running on Compute Engine VM instances.
    * The VMs are running an OS version that is compatible with the required bare metal machine type. For information about the compatibility of machine types with OS versions, see [ Certified operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-cert-table-oss).
    * The VMs are compatible with the required type of Hyperdisk. This also applies to the VM boot volume. For information about the compatibility of machine types with disk types, see the "Hyperdisk Extreme" and "Hyperdisk Balanced" tabs in [ Minimum sizes for SSD-based Persistent Disk and Hyperdisk volumes](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-minimum-pd-sizes-ssd-balanced).

If your source system's machine type is not compatible with the OS version or the Hyperdisk type, then you can migrate your workload by using SAP HANA system replication or backup/recovery.

  * **Migrate by using SAP tools.** If your SAP HANA workload is running on Bare Metal Solution servers, then you can migrate the workload by using SAP tools such as SAP HANA System Replication or database backup and recovery. If your application servers are running in the same region, then you can continue using them. For more information, see Review the migration methods.
  * **Full migration.** If your SAP HANA workload is running on your own on-premises servers or in another cloud, then it's a case of full migration that can involve moving SAP HANA, application servers, and potentially the interfacing systems.



## Review the migration methods

The following table provides information about the migration methods that use functionalities provided by SAP or Google Cloud. In the table, any comparative information is in the context of the given migration methods.

Method | Description  
---|---  
SAP HANA system replication | 

  * **Benefits** : 
    * Shortest cutover window
    * Provides parallel environment for rollback and load testing
  * **Considerations** : 
    * Requires more integration testing due to changing host names and IP addresses
    * Overlapping hardware footprint makes it costly
  * **Recommended for** : 
    * Hybrid, on-premises, or Bare Metal Solution systems that require a shorter outage window
    * Systems that can't be migrated by changing the machine type

  
SAP HANA backup and recovery | 

  * **Benefits** : 
    * Implicit data consistency checks
    * Requires no direct connection between source and target systems
    * It's an operation that is easier to perform by using Google Cloud's Agent for SAP and other standard SAP tools
  * **Considerations** : 
    * Longest migration and cutover time
  * **Recommended for** : 
    * Hybrid, on-premises, or Bare Metal Solution systems that can afford a generous outage window

  
Machine type change | 

  * **Benefits** : 
    * Simplest process, provided requirements are met
    * Doesn't require any additional infrastructure
    * Can utilize high-availability (HA) configuration to enable a phased cutover
  * **Considerations** : 
    * It's usable when prerequisites related to OS and disk compatibility are met
    * Rollback during migration can be more complicated compared to when you use parallel environments
    * Some amount of load and integration testing is still required to confirm functionality and performance, which is applicable to any migration method
  * **Recommended for** : 
    * Systems running on Compute Engine VMs that meet OS and disk type compatibility requirements

  
  
## Method-specific high-level migration steps

For information about the high-level migration steps for the migration method you choose, see the following:

  * Migrate by using SAP HANA system replication
  * Migrate by using database backup and recovery
  * Migrate by changing the machine type



If these migration methods don't fit your scenario, then either it's a case of full migration or you need to design a migration for your scenario, for which you can engage experts such as Google Cloud Professional Services Organization (PSO). For more information about this engagement, see Engage PSO.

### Migrate by using SAP HANA system replication

SAP HANA System Replication (HSR) is a foundational element in high availability and disaster recovery for SAP HANA. HSR decouples the database migration from operating system and other infrastructure dependencies. By leveraging SAP HANA multi-target replication, you can extend HSR to new Compute Engine bare metal instances while retaining existing HA and DR configurations in place until the cutover of your production system.

To migrate an SAP HANA workload to a Compute Engine bare metal instance by using SAP HANA HSR, you complete the following high-level steps:

  1. As with any change in your SAP environment, make sure that a valid backup of your SAP HANA database is available.

  2. Deploy the required type of bare metal instances, and install SAP HANA on them with the required HA and DR configurations. 

You can automate this deployment by using the Terraform configurations provided by Google Cloud. For more information, see the deployment guide for your SAP HANA scenario. 

For information about the bare metal machine types that you can use to run SAP HANA on Google Cloud, the OS versions that you can use, and information about their recommended block storage configuration, see [ Bare metal machine types for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#bare-metal-machines-for-hana). 

  3. Install version 3.15 (latest) of Google Cloud's Agent for SAP on your bare metal instances. 

For information about how to install the agent, see [Install and configure Google Cloud's Agent for SAP on a compute instance](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm). If you deployed your bare metal instances by using any of the Terraform configurations provided by Google Cloud, then the agent is automatically installed. 

  4. Configure the guest OS on your bare metal instance for optimal running of SAP workloads, by using Google Cloud's Agent for SAP. 

For information about how to configure the guest OS, see [ Configure guest OS on bare metal instances](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-bare-metal-instances). 

  5. Configure the required network connection between the source system and your bare metal instance. To accommodate the expected transaction log volume, configure the connection with sufficient network bandwidth.

  6. To provide a baseline for the replication, load initial data from your backup onto the SAP HANA database running on your bare metal instances, or initiate a full synchronization as part of the next step.

  7. Configure multi-target replication from the source system to the SAP HANA system deployed on your bare metal instances.

  8. To estimate cutover, perform at least one dry-run to the new system, including a performance or load test.

  9. Make sure that data is fully synchronized in the new system, then plan and initiate cutover.

     * If your source system is running on Compute Engine VM instances, then modify the internal load balancers to redirect their backends to your bare metal instances. This can also be used to switch back to your source system if anything goes wrong.
     * If your source system is running elsewhere, then you can consider using routes or DNS updates to redirect the external IP addresses that were used by the source system to connect to your bare metal instances.



By using this method, the SAP HANA system on your target bare metal instances can be in sync with your source system before the cutover starts. With proper planning and execution, this migration method can significantly reduce downtime and avoid risks. It can also significantly simplify a rollback if something unforeseen occurs during the migration. However, running two SAP HANA systems in parallel comes with an increased cost.

### Migrate by using database backup and recovery

This migration method involves taking a backup of the source system and restoring it on your bare metal instances.

To minimize the cutover downtime of this method, we recommend that you first deploy SAP HANA on bare metal instances with the required HA and DR configurations, and then perform the recovery operations. This migration method is commonly used for non-production environments, and is suitable when downtime is not a significant concern.

To migrate an SAP HANA workload to a Compute Engine bare metal instance by using database backup and recovery, you complete the following high-level steps:

  1. Deploy the required type of bare metal instances, and install SAP HANA on them with the required HA and DR configurations. 

You can automate this deployment by using the Terraform configurations provided by Google Cloud. For more information, see the deployment guide for your SAP HANA scenario. 

For information about the bare metal machine types that you can use to run SAP HANA on Google Cloud, the OS versions that you can use, and information about their recommended block storage configuration, see [ Bare metal machine types for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#bare-metal-machines-for-hana). 

  2. Install version 3.15 (latest) of Google Cloud's Agent for SAP on your bare metal instances. 

For information about how to install the agent, see [Install and configure Google Cloud's Agent for SAP on a compute instance](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/install-config-on-vm). If you deployed your bare metal instances by using any of the Terraform configurations provided by Google Cloud, then the agent is automatically installed. 

  3. Configure the guest OS on your bare metal instance for optimal running of SAP workloads, by using Google Cloud's Agent for SAP. 

For information about how to configure the guest OS, see [ Configure guest OS on bare metal instances](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-bare-metal-instances). 

  4. To estimate cutover, perform at least one dry-run to the new system, including a performance or load test.

  5. Create an initial full backup with your preferred backup tooling and then transfer the backup to the target environment in preparation for the cutover.

  6. Stop the SAP application and database connections to the source SAP HANA database.

  7. Create a delta backup of your source SAP HANA database by using your preferred tool or file system dump. Alternatively, a full backup can be used if your outage window accommodates this, in which case step 5 can be skipped.

  8. Restore the backups to the SAP HANA database that you installed on your bare metal instances to bring the data in sync with the source.

  9. If applicable, enable replication and configure the HA cluster on your bare metal instances.

  10. Make sure that data is fully recovered, then plan and initiate your pre-go-live activities.

     * If your source system is running on Compute Engine VM instances, then modify the internal load balancers to redirect their backends to your bare metal instances.
     * If your source system is running elsewhere, then you can consider using routes or DNS updates to redirect the external IP addresses that were used by the source system to connect to your bare metal instances.



Migrating multi-terabyte SAP HANA databases by using backup and recovery might require extended downtime during the process because the system needs to remain offline during backup and recovery. Once the target system has the last changes transferred from the source, make sure that you prevent any further changes on the source system.

### Migrate by changing the machine type

This migration method is applicable to SAP HANA workloads running on Compute Engine VM instances. It involves changing the machine type of the underlying VM instances to the required Compute Engine bare metal machine type. This method is ideal for situations where:

  * The source SAP HANA system runs on VM instances where the OS and disk type being used are compatible with the type of bare metal instance that you want to use.
  * You want to retain the instance name, IP address, and other metadata instead of deploying SAP HANA on new compute instances.
  * Your risk tolerance accommodates making changes to your existing systems and configuration. In case something goes wrong during the migration, then such changes would have to be reverted to return your system to the last known working state prior the migration. This approach works best in environments where you operate with a high availability configuration.



To migrate SAP HANA from a Compute Engine VM to a Compute Engine bare metal instance by changing the machine type, complete the following high-level steps:

  1. Ensure that the following prerequisites are met:

     * Your VM instances are using an OS version that is compatible with the bare metal machine type to which you want to migrate. If not, then upgrade to a compatible version. For information about the compatibility of machine types with OS versions, see [Certified operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-cert-table-oss).
     * Ensure that the correct [OS feature](https://docs.cloud.google.com/compute/docs/images/create-custom#guest-os-features) flags are set. For example, the required **`UEFI_COMPATIBLE`** feature must be active on the boot disk to use the disk on a bare metal machine type.
     * Test the compatibility of your OS image with the target machine type prior to attempting to change the machine type. For example, as an initial test, use a snapshot of the boot disk of the source instance to create a test VM, then validate that the new instance can start correctly on the target machine type.
     * Your VM instances are compatible with the required type of Hyperdisk. This applies to all attached block storage devices, including the boot volume. For information about the compatibility of machine types with disk types, see the "Hyperdisk Extreme" and "Hyperdisk Balanced" tabs in [Minimum sizes for SSD-based Persistent Disk and Hyperdisk volumes](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-minimum-pd-sizes-ssd-balanced).
  2. If your VM is part of a high-availability (HA) cluster, then ensure the following:

     1. The primary serving database instance is active on the other nodes in the cluster.
     2. To prevent automated failover, the cluster is put in maintenance mode.
  3. If you're running SAP HANA and using the SAP HANA Fast Restart option, then in the `/etc/fstab` file, specify the `nofail` option for the `tmpfs` mount. 

This helps ensure that the compute instance to which you're going to move your SAP HANA workload can continue through the boot process even if the instance has fewer NUMA nodes.

  4. Stop your SAP HANA instance.

  5. Stop your VM instance.

  6. To safeguard your system and enable rollback in case of migration failures, do the following:

     * Ensure you have a valid, up-to-date full backup of your SAP HANA database.
     * Create snapshots of the disks that you're modifying, including the boot disk.
  7. For each Persistent Disk volume used by your VM, create the required type of Hyperdisk volume by using the disk snapshots you created in the preceding step.

For information about how to do this, see [Change the disk type](https://docs.cloud.google.com/compute/docs/disks/migrate-to-hyperdisk). For information about how to detach and attach boot disks, see [Detaching and attaching boot disks](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk). For information about the storage configuration recommended by Google Cloud for bare metal machine types, see [Supported block storage](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#supported_block_storage).

  8. Detach the Persistent Disk volumes from your VM.

  9. Attach the Hyperdisk volumes that you created to your VM.

  10. Edit your VM's machine type to the required Compute Engine bare metal machine type.

For information about how to edit your instance's machine type, see [Edit the machine type of a compute instance](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance). For information about the Compute Engine bare metal machine types that are certified by SAP for use with SAP HANA, see [Bare metal machine types for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#bare-metal-machines-for-hana).

  11. Start your bare metal instance.

  12. Configure the guest OS on your bare metal instance for optimal running of SAP workloads, by using Google Cloud's Agent for SAP.

For information about how to configure the guest OS, see [Configure guest OS on bare metal instances](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/configure-bare-metal-instances).

  13. If you are using the SAP HANA Fast Restart option and the new compute instance doesn't have the same number of NUMA nodes as the source compute instance, then you need to update the Fast Restart configuration to map the `tmpfs` file system with the NUMA nodes available on the new compute instance. 

If your SAP HANA deployment is based on a Terraform configuration provided by Google Cloud, then you can reconfigure the SAP HANA Fast Restart option by running the `sap_lib_hdbfr.sh` script. For more information, see [Automated steps](https://docs.cloud.google.com/sap/docs/sap-hana-operations-guide#automation-fast-restart).

  14. Start your SAP HANA database.

  15. Verify that SAP HANA is running as expected on your bare metal instance.

  16. If your bare metal instance is part of a HA cluster, then do the following:

     1. Repeat steps 3-13 for the other node in your HA cluster.
     2. Remove the cluster from maintenance mode.
  17. Make sure that data is up to date, then plan and initiate your pre-go-live activities.




This approach is suitable if you want to perform in-place updates by changing the machine type without requiring parallel environments. If the OS version and disk type are not compatible with the required bare metal machine type, then the downtime window and rollback time can significantly increase in case you need to recover the affected instance. You can reduce the downtime by utilizing a phased change approach, which includes using an HA cluster and migrating your VM to Hyperdisk volumes prior to the planned transition to the bare metal machine type.

### Full migration

If your SAP HANA workload is running on your own on-premises servers or in another cloud, then it's a case of full migration that can involve moving SAP HANA, application servers, and potentially the interfacing systems.

You can engage Google Cloud professionals or partners to help with the migration. For more information, see Engage PSO.

### Engage PSO

Engaging Google Cloud Professional Services Organization (PSO) or a Systems Integrator (SI) can be beneficial for migrating complex SAP HANA systems to X4 or C3 bare metal instances. Their expertise in SAP HANA and Google Cloud, along with proven methodologies and best practices, can help ensure a smooth and successful migration, minimizing disruption and optimizing system performance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
