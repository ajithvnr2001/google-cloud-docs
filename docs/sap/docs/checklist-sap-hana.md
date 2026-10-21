---
url: https://docs.cloud.google.com/sap/docs/checklist-sap-hana/
title: Checklist for SAP HANA on Google Cloud \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:14:32.104714+00:00
---

# Checklist for SAP HANA on Google Cloud  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/checklist-sap-hana/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Checklist for SAP HANA on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

This checklist helps you to improve the design, migration, implementation, and maintenance of your SAP HANA landscapes on Google Cloud.

As you go through the checklist, take into account your own business needs. If you make choices that differ from what we've recommended, keep track of those differences for later tasks in the checklist.

**Note:** This checklist contains general recommendations and doesn't cover all aspects of your SAP on Google Cloud landscape. 

****

###  Plan your SAP HANA landscape

  * To deploy multiple SAP HANA databases in your landscape:

    * Do not run multiple SAP HANA systems on the same host in production systems. Instead, create one VM per each SAP HANA database. For more information, see [SAP Note 1681092 - Multiple SAP HANA systems (SIDs) on the same underlying server(s)](https://launchpad.support.sap.com/#/notes/1681092) and [SAP HANA Technical Deployment Options](https://help.sap.com/viewer/eb3777d5495d46c5b2fa773206bbfb46/2.0.05/en-US/69f63dd3945f4f4c8ef5588ec816de12.html).
    * Create the tenant databases (also known as multitenant database containers [MDC]) that are appropriate for your environment and licensing. For more details, see [SAP Note 2096000 - SAP HANA tenant databases - Additional Information](https://launchpad.support.sap.com/#/notes/2096000).

    * We recommend that you don't run custom or third-party software on the same VM as an SAP HANA database if this will impact the performance and operations of the SAP HANA database.

    * By using a single VM to run both the SAP HANA database and other business software, both applications share VM resources which can decrease the performance of the database. Keep in mind that SAP HANA is resource intensive and requires compute resource availability based on the benchmark and sizing guides.

    * For more information about the SAP HANA landscape design, see [SAP HANA Deployment Types](https://www.google.com/url?q=https://help.sap.com/viewer/2c1988d620e04368aa4103bf26f17727/2.0.03/en-US/6483b71787f2439c907bd99036559e72.html?q%3DMCOS%2520MCOD&sa=D&ust=1602176584032000&usg=AOvVaw0ColLRQaKGQhbjdP-VgkKG).

  * If you choose to deploy multiple non-production SAP HANA databases on the same VM:

    * Use hostname aliases for the different system IDs (SIDs).
    * For each installation, use a separate static IP address mapped to an alias hostname.



###  Select regions and zones for SAP HANA

  * To learn which regions and zones support specific Compute Engine VMs, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available). Keep in mind that SAP HANA-certified Compute Engine VMs might not be available in all locations.
  * To protect against zonal failures, deploy SAP HANA in multiple zones (especially for VMs that are part of the same SAP HANA HA cluster).
  * To protect against regional failures, add disaster recovery sites in other regions.
  * To meet the latency requirements for an SAP HANA scale-out system, deploy all nodes of the scale-out system in the same zone.



###  Choose a deployment model for SAP HANA

To deploy SAP HANA, you can use the Terraform configurations provided by Google Cloud. Terraform is a popular tool for building, changing, and versioning infrastructure safely and efficiently. To use Terraform and find the appropriate configuration files for SAP solutions, see [Automating SAP deployments on Google Cloud with Terraform](https://docs.cloud.google.com/sap/docs/tf-for-sap).

To understand how to implement SAP HANA on Google Cloud, see the [SAP HANA planning guide](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide).

###  Pick appropriate machine types and operating systems for SAP HANA

  * To select a machine type for your SAP HANA deployment and workloads, see the list of [Certified machine types for SAP HANA](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-cert-table-vms). 
    * To confirm that your preferred machine type is available in your preferred region, see [Available regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones#available).
    * To ensure the capacity needs of your landscape can be fulfilled in the region of your choice (such as capacity planning and reservations), work with your Technical Account Manager or designated Customer Engineer.
  * When choosing an operating system (OS): 
    * Select an SAP-supported OS:   
[Certified operating systems for SAP HANA](https://docs.cloud.google.com/sap/docs/certifications-sap-hana#hana-cert-table-oss) (Google Cloud)
    * Make sure the OS is certified for use on Google Cloud:   
Go to [Certified and supported SAP HANA hardware directory](https://www.sap.com/dmc/exp/2014-09-02-hana-hardware/enEN/#/solutions?filters=iaas;ve:29), click on the required machine type, and then see **Operating System**.
    * Confirm that the OS has recent patches and updates:   
[OS support for SAP HANA on Google Cloud](https://docs.cloud.google.com/sap/docs/sap-hana-os-support)   
For example, you don't want to install an outdated 2-year-old image with security issues or other problems.
    * If you use SUSE Linux Enterprise Server (SLES) in your landscape, follow the guidelines given in the following: 
      * SAP note [1275776 - Linux: Preparing SLES for SAP environments](https://me.sap.com/notes/1275776)
      * SAP note [3577842 - SAP HANA DB: Recommended OS settings for SLES 16 / SLES for SAP Applications 16](https://me.sap.com/notes/3577842)
      * SAP note [2684254 - SAP HANA DB: Recommended OS settings for SLES 15 / SLES for SAP Applications 15](https://me.sap.com/notes/2684254)
      * SAP note [2205917 - SAP HANA DB: Recommended OS settings for SLES 12 / SLES for SAP Applications 12](https://me.sap.com/notes/2205917)
      * SUSE document [Tuning systems with saptune](https://documentation.suse.com/sles-sap/15-SP2/html/SLES-SAP-guide/cha-tune.html)
    * If you use Red Hat Enterprise Linux (RHEL) in your landscape, follow the guidelines given in the following SAP notes: 
      * [2009879 - SAP HANA Guidelines for Red Hat Enterprise Linux (RHEL) Operating System](https://launchpad.support.sap.com/#/notes/2009879)
      * [3562919 - SAP HANA DB: Recommended OS Settings for RHEL 10](https://me.sap.com/notes/3562919)
      * [3108302 - SAP HANA DB: Recommended OS Settings for RHEL 9](https://me.sap.com/notes/3108302)
      * [2777782 - SAP HANA DB: Recommended OS Settings for RHEL 8](https://me.sap.com/notes/2777782)
      * [2292690 - SAP HANA DB: Recommended OS settings for RHEL 7](https://me.sap.com/notes/2292690)
      * [3562909 - Red Hat Enterprise Linux 10.x: Installation and Configuration](https://me.sap.com/notes/3562909)
      * [3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://me.sap.com/notes/3108316)
      * [2772999 - Red Hat Enterprise Linux 8.x: Installation and Configuration](https://me.sap.com/notes/2772999)
      * [2002167 - Red Hat Enterprise Linux 7.x: Installation and Upgrade](https://me.sap.com/notes/2002167)
    * We recommend you use the OS images available on Google Cloud because they meet the certification requirements of SAP, the OS vendor, and Google. However, see [Custom OS Images](https://docs.cloud.google.com/compute/docs/images#custom_images) if your landscape has unique requirements that cannot be met with the standard images (such as migrating your existing on-premises images to Google Cloud).
    * If you need to set custom environment variables for an SAP HANA system on Linux, see [SAP Note 3011163 - How to set Environment Variables for SAP HANA System](https://launchpad.support.sap.com/#/notes/3011163).



###  Choose storage and persistent disks for SAP HANA

When choosing disk types for SAP HANA:

  * Use an _SSD-based_ [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks#pdspecs) or [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks). SSD-based Hyperdisk and Persistent Disk types that are certified by SAP for use with SAP HANA include the following: 
    * **Hyperdisk types** : Hyperdisk Extreme (`hyperdisk-extreme`) and Hyperdisk Balanced (`hyperdisk-balanced`)

      * Hyperdisk Extreme provides higher maximum IOPS and throughput options than SSD-based Persistent Disk types.
      * For a list of the machine types that support Hyperdisk Extreme and Hyperdisk Balanced, see [Machine type support](https://docs.cloud.google.com/compute/docs/disks/hyperdisks#machine_type_support).
      * On Compute Engine bare metal instances such as X4, use Hyperdisk Balanced as the recommended disk for hosting the following volumes: 
        * The boot volume.
        * The `/usr/sap` volume.
        * The `/hana/shared` volume, if you're hosting it on its own disk.
        * The `/hanabackup` volume, if you're saving your backups on a disk.
      * For Hyperdisk Extreme, you select the performance you need by provisioning IOPS, which also determines your throughput. For more information, see [Size and performance limits for Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme#size_limits).
      * For Hyperdisk Balanced, you select the performance you need by provisioning IOPS and throughput. For more information, see [Size and performance limits for Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#size_limits).
      * You can use Hyperdisk Extreme for the `/hana/data` and `/hana/log` volumes when you require the highest performance.
      * To enable the best performance from Hyperdisk Extreme for SAP HANA, update your SAP HANA system properties as recommended in [Hyperdisk performance](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hyperdisk_performance).
    * **Persistent Disk types** : Legacy machine types support Persistent Disk types. Google Cloud recommends that you use the latest machine types and Hyperdisk volumes for running performant SAP HANA workloads.

#### Click to expand and view information about supported Persistent Disk types

      * Supported Persistent Disk types include the following: Balanced (`pd-balanced`), Performance or SSD (`pd-ssd`), and Extreme (`pd-extreme`).
      * These disk types provide cost-effective and reliable block storage.
      * Performance (SSD) Persistent Disk (`pd-ssd`) provides higher performance than Balanced Persistent Disk (`pd-balanced`).
      * Use Balanced Persistent Disk as the recommended disk for hosting the following volumes: 
        * Boot volume of the compute instance.
        * The `/usr/sap` volume.
        * The `/hana/shared` volume, if you're hosting it on its own disk.
        * The `/hanabackup` volume, if you save your backups to a disk. If you want to reduce the backup costs, then you can use a Standard HDD Persistent Disk (`pd-standard`). Balanced Persistent Disk provides faster backups than Standard HDD Persistent Disk. While selecting the disk, make sure that your machine type supports the disk type.
      * Balanced and Performance (SSD) Persistent Disk support PD Async Replication. You can use this feature for cross-region active-passive disaster recovery. For more information, see [Disaster recovery using PD Async Replication](https://docs.cloud.google.com/sap/docs/sap-hana-dr-planning-guide#dr_using_pd_async_replication).
      * While Extreme Persistent Disk (`pd-extreme`) is certified for use with SAP HANA, we recommend that you instead use Hyperdisk Extreme (`hyperdisk-extreme`), which provides greater performance. If you want to use Extreme Persistent Disk, then make sure to provision the disks in accordance with the information in Minimum sizes for SSD-based Persistent Disk and Hyperdisk volumes.
      * For information about Persistent Disk performance, see [Persistent Disk performance overview](https://docs.cloud.google.com/compute/docs/disks/performance) and [Optimize Persistent Disk performance](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#performance_factors)

  * Make sure that your SSD-based Persistent Disk and Hyperdisk volumes are large enough to meet SAP HANA performance requirements. For more information, see [Minimum sizes for SSD-based Persistent Disk and Hyperdisk volumes](https://docs.cloud.google.com/sap/docs/sap-hana-planning-guide#hana-minimum-pd-sizes-ssd-balanced).
  * Test and compare your results against expectations to ensure the landscape meets your disk performance requirements (for benchmarks such as HANA startup time, backup, volume test, and load test), then document these baselines for future reference.
  * Use a small swap disk of 2 GB for SAP HANA. See SAP note [1999997 - FAQ: SAP HANA Memory](https://launchpad.support.sap.com/#/notes/1999997).
  * When using [Google Cloud NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview), follow the [Volume requirements for NetApp Volumes with SAP HANA](https://docs.cloud.google.com/sap/docs/filers-for-sap#netapp_cvs_reqs).



###  Implement SAP HANA Fast Restart

For SAP HANA 2.0 SP04 and later, we recommend the SAP HANA Fast Restart option, especially for Compute Engine memory-optimized machine types, such as the M1, M2, or M3 machine types.

To implement the Fast Restart option, see [SAP HANA Fast Restart Option](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/LATEST/en-US/ce158d28135147f099b761f8b1ee43fc.html) in the SAP HANA documentation.

For more information about configuring the Fast Restart option, see the configuration guide for your Linux distribution:

  * [RHEL: Enable SAP HANA Fast Restart](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-rhel#enable_sap_hana_fast_restart)
  * [SLES: Enable SAP HANA Fast Restart](https://docs.cloud.google.com/sap/docs/sap-hana-ha-config-sles#enable_sap_hana_fast_restart)



If you deploy your SAP HANA system on Google Cloud by using one of the Terraform configuration files that we provide, then you need to create and mount the TMPFS filesystem after the host VM and the base SAP HANA system are successfully deployed.

###  Have a backup strategy for SAP HANA

  * When using the [Backint](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery) feature of Google Cloud's Agent for SAP: 
    * Use version 3.15 (latest) of Google Cloud's Agent for SAP. For instructions to update to it, see [Update Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/operations#agent4sap-update).
    * Adjust performance to meet your needs and perform data backups in parallel. See [Multistreaming data backups with Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#multistreaming_data_backups).
    * While creating the Cloud Storage buckets, choose a location that is closest to your SAP HANA location. Also, ensure that your choice of storage buckets meets your redundancy needs. Typically, using the multi-region option is best because it provides recoverability if a particular region becomes unavailable. For more information, see [Storing backups in Cloud Storage buckets](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery#storing_backups_in_storage_bucket).
    * If you enable Private Google Access on your subnet, then don't route traffic through a private VM (for example, using a NAT gateway or proxy server) because doing so can decrease achievable throughput. For more information, see the [Network configuration](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config) section of the **Configuring Private Google Access** guide.
  * When you perform backups to a Persistent Disk or Hyperdisk volume: 
    * You can use any disk type as long as it meets your performance requirements. If Standard Persistent Disk does not provide enough performance for your needs, then try Balanced Persistent Disk instead.
    * Know that the SAP HANA landscape requires you to allocate additional bandwidth to each VM instance. SAP HANA uses the extra bandwidth for the overhead and IOPS needed to read and write backup data to disk. As a result, we recommend using SAP HANA Backint or third-party tools that support either streaming or snapshots of the Persistent Disk or Hyperdisk volumes.
  * Remember to test your backup and recovery procedures regularly to verify that they meet your performance and recoverability needs.



###  Best practices for high-availability configurations for SAP HANA

For a checklist of best practices for high-availability configurations for SAP HANA on Google Cloud, see [High availability for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/checklist-sap-high-availability).

###  Build in disaster recovery for SAP HANA

  * Test your failover and failback procedures extensively: 
    * To ensure that your landscape will fail over properly to a new region in the event of a localized disaster, regularly test your disaster recovery procedures.
    * To enable successful failover and failback, create an operations playbook and update it as needed.
  * To limit the amount of data that should be transferred with each backup, make use of incremental and differential backup strategies by reviewing [Delta Backup Types](https://help.sap.com/viewer/6b94445c94ae495c83a19646e7c3fd56/LATEST/en-US/15b4aa82ae7544f78f809e35add006ce.html). Consider this against your recovery time objectives.



###  Use monitoring and alerting for SAP HANA

  * Establish a monitoring and alerting procedure. Helpful options available in Google Cloud include [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) and the _SAP HANA monitoring metrics collection_ feature of version 2.0 or later of [Google Cloud's Agent for SAP](https://docs.cloud.google.com/sap/docs/agent-for-sap/latest/planning#sap_hana_monitoring_metrics).



###  Automate validation checks for SAP HANA workloads

To automate continuous validation checks for your SAP HANA workloads that run on Google Cloud, use [Workload Manager](https://docs.cloud.google.com/workload-manager/docs/overview). Workload Manager allows you to automatically scan and evaluate your SAP HANA workloads against best practices to improve their quality, performance, and reliability. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
