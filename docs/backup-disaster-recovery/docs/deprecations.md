---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations/
title: Feature deprecations \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:30.419910+00:00
---

# Feature deprecations  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Resources ](https://docs.cloud.google.com/backup-disaster-recovery/docs/resources)



Send feedback 

#  Feature deprecations Stay organized with collections  Save and categorize content based on your preferences. 

The [Google Cloud Platform Terms of Service (section "Discontinuation of Services")](https://docs.cloud.google.com/terms) defines the deprecation policy that applies to Backup and DR Service. The [deprecation policy](https://docs.cloud.google.com/terms/deprecation) only applies to the services, features, or products listed therein. 

After a service, feature, or product is officially deprecated, it continues to be available for at least the period of time defined in the Terms of Service. After this period of time, the service is scheduled for shutdown. 

Feature (status) | Deprecated date | Shutdown date | Details  
---|---|---|---  
Management Console and associated workloads | **September 30, 2026** | **September 30, 2027** (End of backup support)  
**March 31, 2028** (End of restore support) | Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated.  
  
**Affected workloads:**

  * Compute Engine (managed using the legacy appliance management console)
  * Db2 Instance
  * Oracle Database
  * SAP HANA
  * Microsoft SQL Server
  * Google Cloud VMware Engine (GCVE)
  * Generic App
  * Consistency Group
  * All other user-managed apps (File System, System State, NFS, CIFS)

**Note:** Support for Google first-party managed services including Compute Engine VMs, Disks, Cloud SQL, AlloyDB for PostgreSQL, and Filestore is completely unaffected.  
  
**Key Milestones & Policies:**

  * **End of new deployments:** After July 31, 2026, new deployments of the affected databases in the appliance management console are no longer supported.
  * **End of Support for New Backups:** After September 30, 2027, you will no longer be able to run new backups using the legacy stack.
  * **End of Standard Restores:** Support for standard restores, exports, and migrations using the legacy appliance management console ends on March 31, 2028.

**Migration Alternatives:**

  * _Compute Engine:_ Migrate to native, appliance-free backups using [Backup and DR for Compute Engine](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup).
  * _User-Managed Databases (Oracle, Db2, etc.):_ Use Compute Engine VM/Persistent Disk backups with the [guest-flush framework](https://cloud.google.com/compute/docs/disks/creating-linux-application-consistent-pd-snapshots) and [custom scripts](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/application-consistent-backups-for-self-managed-databases).
  * _SAP HANA:_ Deploy the [GCP SAP Backint Agent](https://cloud.google.com/sap/docs/agent-for-sap/latest/backint-backup-recovery) or [Disk Snapshots](https://cloud.google.com/sap/docs/agent-for-sap/latest/disk-snapshot-backup-recovery).
  * _General VMs / Other:_ Utilize [Native Google Disk Snapshots](https://cloud.google.com/compute/docs/disks/create-snapshots) or third-party solutions on [Google Cloud Marketplace](https://console.cloud.google.com/marketplace).

  
Backup for SAP ASE, SAP IQ, SAP MaxDB, MariaDB, MySQL, PostgreSQL databases | **July 31, 2026** | **July 31, 2027** | Support for backing up the affected databases in the legacy appliance management console is deprecated.   
  
**End of new deployments** : after July 31, 2026, new deployments of the affected databases in the appliance management console are no longer supported.  
  
**End of support for new backups** : the ability to create _new_ backups for existing setups of the affected databases in the appliance management console ends on July 31, 2027.   
  
**End of migration period** : you must migrate any existing backup data that you want to retain from the appliance management console by December 30, 2027.  
  
To avoid losing your data, we recommend that you migrate your MySQL and PostgreSQL database instances to Google Cloud fully managed database services, such as Cloud SQL or AlloyDB for PostgreSQL. For other database types, use native database backup utilities or third-party backup solutions. For details, see the [database backup migration guide](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations/migrating-legacy-databases).  
Report manager | **February 28, 2024** | **April 30, 2024** | The report manager in the appliance management console is replaced with the Backup and DR reporting system. For details, see the [ Backup and DR reporting system overview](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/reports-overview).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
