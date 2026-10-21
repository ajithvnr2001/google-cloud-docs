---
url: https://docs.cloud.google.com/sap/docs/checklist-sap-other/
title: Checklist for SAP on Google Cloud with other databases \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:14:31.669623+00:00
---

# Checklist for SAP on Google Cloud with other databases  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/checklist-sap-other/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Checklist for SAP on Google Cloud with other databases Stay organized with collections  Save and categorize content based on your preferences. 

This checklist helps you to improve the design, migration, implementation, and maintenance of your SAP systems on Google Cloud using databases other than SAP HANA.

As you go through the checklist, take into account your own business needs. If you make choices that differ from what we've recommended, then keep track of those differences for later tasks in the checklist.

**Note:** This checklist contains general recommendations and doesn't cover all aspects of your SAP landscape on Google Cloud. 

****

###  Plan your SAP landscape with other databases

  * We recommend that you do not deploy multiple databases on the same Compute Engine VM instance in a production environment. Instead, distribute your databases across multiple VM instances to isolate resource consumption and avoid contention.
  * Avoid running other applications on the same VM instance as the database.

    * By using a single VM instance to run both the database and other software, both applications share the VM resources, which can decrease the performance of the database. Keep in mind the following: 
      * Database operations are resource intensive and require compute resource availability based on the benchmark and sizing guides.
      * SAP applications are very sensitive to paging and swapping, which can deteriorate the performance and possibly cause the system to go down.
  * If you choose to deploy any custom or third-party software on the same VM instance as a database used in an SAP landscape, then:

    * Make sure you deploy this model only in non-production systems (for example, a test system).
    * Use hostname aliases for the SAP installations.
    * For each installation, use a separate static IP address mapped to an alias hostname.



###  Select regions and zones for SAP with other databases

  * To learn which regions and zones support specific Compute Engine VMs, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available). Keep in mind that SAP-certified Compute Engine VMs might not be available in all locations.
  * To protect against zonal failures for SAP landscapes, deploy the databases in multiple zones, especially for VMs that are part of the same high-availability (HA) cluster.
  * To protect against regional failures, add disaster-recovery sites in other regions.



###  Choose a deployment model for SAP with other databases

  * When installing some databases for SAP, you can use Terraform configuration files that Google Cloud provides, which install and configure all the required packages necessary to run the database and SAP on Google Cloud. For more information, see the following database deployment guides: 
    * [SAP ASE guides](https://docs.cloud.google.com/sap/docs/sap-ase-guides)
    * [IBM Db2 guides](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-guides)
    * [SAP MaxDB guides](https://docs.cloud.google.com/sap/docs/sap-maxdb-guides)
    * [Microsoft SQL Server guide](https://docs.cloud.google.com/compute/docs/instances/sql-server/creating-sql-server-instances)
    * [Oracle Database guides](https://docs.cloud.google.com/sap/docs/oracle-all-guides)



###  Pick appropriate machine types and operating systems for SAP with other databases

  * To select a Compute Engine machine type for your database deployment and workloads, see [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432) or [Certified machine types](https://docs.cloud.google.com/sap/docs/certifications-sap-apps#sap-certified-vms) (Google Cloud). 
    * To ensure that the needs of your landscape, such as capacity planning and reservations, can be fulfilled in the region of your choice, work with your Technical Account Manager or designated Customer Engineer.
  * To select an SAP-supported OS that works on Google Cloud, see [ SAP Note 2456432 - SAP Applications on Google Cloud: Supported Products and Google Cloud machine types](https://launchpad.support.sap.com/#/notes/2456432) or the [Quick reference table](https://docs.cloud.google.com/sap/docs/netweaver-os-support#quick_reference_table) (Google Cloud).
  * Confirm that the OS has recent patches and updates.

    * If you use SUSE Linux Enterprise Server (SLES) in your landscape, then follow these guidelines:

      * SAP note [1275776 - Linux: Preparing SLES for SAP environments](https://me.sap.com/notes/1275776)

      * [Tuning systems with saptune](https://documentation.suse.com/sles-sap/15-SP2/html/SLES-SAP-guide/cha-tune.html) (SUSE documentation)

    * If you use Red Hat Enterprise Linux (RHEL) in your landscape, then follow the guidelines described in the following SAP notes:

      * [3562909 - Red Hat Enterprise Linux 10.x: Installation and Configuration](https://me.sap.com/notes/3562909)
      * [3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://me.sap.com/notes/3108316)
      * [2772999 - Red Hat Enterprise Linux 8.x: Installation and Configuration](https://me.sap.com/notes/2772999)
      * [2002167 - Red Hat Enterprise Linux 7.x: Installation and Upgrade](https://me.sap.com/notes/2002167)
    * We recommend that you use the OS images provided by Google Cloud because they meet the certification requirements of SAP, the OS vendor, and Google. However, if your landscape has unique requirements that cannot be met with the standard images, then see [Custom OS Images](https://docs.cloud.google.com/compute/docs/images#custom_images).




###  Choose storage and persistent disks for SAP with other databases

  * When choosing a persistent disk for SAP with other databases:

    * For the highest performance use a Compute Engine Persistent Disk or Hyperdisk that is backed by solid-state drive storage (SSD-based) to store logs and data, including temporary table spaces.
    * If high performance is not a requirement, for example when you use a disk for backups, then use a Compute Engine Standard Persistent Disk (`pd-standard`), which is backed by standard hard disk drives (HDD).
    * For more information about persistent disks for databases other than SAP HANA, see: 
      * [Persistent disks for SAP MaxDB](https://docs.cloud.google.com/sap/docs/sap-maxdb-planning-guide#persistent_disks)
      * [Persistent disks for SAP ASE](https://docs.cloud.google.com/sap/docs/sap-ase-planning-guide#persistent_disks)
      * [Persistent disks for IBM Db2](https://docs.cloud.google.com/sap/docs/sap-ibm-db2-planning-guide#persistent_disks)
      * "Block storage" section in the [Plan Oracle Database implementation for SAP NetWeaver](https://docs.cloud.google.com/sap/docs/oracle-planning#block_storage)
  * Test and compare your results against expectations to ensure that the landscape meets your disk performance requirements for benchmarks such as database startup time, backup, volume test, and load test. After comparing, document these baselines for future reference.

  * When using the [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview), make sure that NetApp Volumes has been certified by your database vendor.




###  Have a backup strategy for SAP with other databases

  * When you use a persistent disk for backups, consider the following: 
    * You can use any disk type as long as it meets your performance requirements. If a Standard Persistent Disk (`pd-standard`) does not provide enough performance for your needs, then use a Balanced (`pd-balanced`) or SSD Persistent Disk (`pd-ssd`).
    * Remember to test your backup and recovery procedures to verify that they meet your performance needs.



###  Include high availability and disaster recovery for SAP with other databases

  * For testing purposes, create a non-production HA system that is equivalent to your production environment.
  * Test your failover and failback procedures extensively as follows: 
    * To simulate a Compute Engine [live migration](https://docs.cloud.google.com/compute/docs/instances/live-migration) and ensure that you've configured adequate cluster failover thresholds, see [Testing your availability policies](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#testingpolicies).
    * To ensure that your landscape fails over properly to a new region in the event of a localized disaster, regularly test your disaster recovery procedures.
    * To enable successful failover and failback, create an operations playbook and update it as needed.



###  Use monitoring and alerting for SAP with other databases

  * Establish a monitoring and alerting procedure. Common items to track include system down events, resource utilization (CPU, memory, and disk), database alerts for tables, buffers, log space, and backups. To learn about a useful monitoring tool available in Google Cloud, see [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
