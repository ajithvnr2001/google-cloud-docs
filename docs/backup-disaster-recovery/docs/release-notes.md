---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/release-notes/
title: Backup and DR release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:05.031695+00:00
---

# Backup and DR release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Resources ](https://docs.cloud.google.com/backup-disaster-recovery/docs/resources)



Send feedback 

#  Backup and DR release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Backup and DR. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/backupdr-release-notes.xml) directly. 

## September 30, 2026

Deprecated

Support for backing up and restoring workloads managed via the legacy appliance management console is deprecated.

Key milestones for this deprecation include the following:

  * **End of Support for New Backups** : After September 30, 2027, you will no longer be able to run new backups using the legacy stack.
  * **End of Standard Restores** : Support for standard restores, exports, and migrations using the legacy appliance management console continues till March 31, 2028.



For more information, see [Deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

## September 26, 2026

Security

**Note:** These fixes and updates are available starting with Backup and DR release 11.0.17.496. These fixes are not rolled out to the 11.0.16 release; we recommend upgrading the backup/recovery appliance to version 11.0.17 to receive these updates.

**Security Bulletin – Appliance:**

  * Addressed multiple input sanitization vulnerabilities, including SQL injection and cross-site scripting (XSS), across appliance platform server utilities.
  * Remediated an authorization and validation vulnerability in user management workflows.



**Security Bulletin – Host Agent:**

  * Strengthened local RPC interface access controls and improved credential isolation between concurrent backup jobs on the Host Agent.
  * Hardened database layer against command injection, path traversal, and unauthorized directory permission modifications.
  * Remediated local privilege escalation vulnerabilities in Oracle and SAP HANA host agent environment and profile handling.
  * Improved temporary file creation and link handling across Windows and Linux Host Agents to mitigate symlink race conditions.
  * Addressed buffer overflow vulnerabilities in Linux Host Agent components.



**Libraries Bugs (Appliance):**

  * Upgraded third-party runtime and application libraries (including Go and Java packages such as Netty and Jackson Databind) on the appliance management server.
  * Updated the Linux kernel and base operating system packages across Backup and DR appliance virtual machine images to mitigate reported vulnerabilities.



Fixed

**Note:** These fixes and updates are available starting with Backup and DR release 11.0.17.496. These fixes are not rolled out to the 11.0.16 release; we recommend upgrading the backup/recovery appliance to version 11.0.17 to receive these updates.

These issues have been resolved for the Host Agent:

  * Resolved an issue where Oracle ASM backups failed with the error "Failed to create ASM staging disk group".
  * Resolved an issue causing Oracle RAC database restores to fail with error 6407 due to invalid node names in the nodelist.
  * Fixed a PostgreSQL backup failure during snapshot preparation where the database user lacked execute permissions on `pg_backup_start`.
  * Corrected an issue where the Oracle mount process was unable to locate the undo catalog configuration file.
  * Improved Oracle backup metadata processing to support databases containing a large volume of datafiles.
  * Resolved an issue where discovery of SAP Sybase instances failed when multiple instances were configured under different user accounts.
  * Fixed an issue causing PostgreSQL database discovery to fail during host agent discovery workflows.
  * Resolved an issue that prevented successful discovery of MySQL database applications.



Change

**Note:** These fixes and updates are available starting with Backup and DR release 11.0.17.496. These fixes are not rolled out to the 11.0.16 release; we recommend upgrading the backup/recovery appliance to version 11.0.17 to receive these updates.

**Non-Breaking Changes (Host Agent):**

  * Modernized host agent database integration scripts for IBM Db2, MySQL, MariaDB, SAP Sybase IQ, and MaxDB to standard Bash execution for improved stability and security hardening.



Feature

**Note:** These fixes and updates are available starting with Backup and DR release 11.0.17.496. These fixes are not rolled out to the 11.0.16 release; we recommend upgrading the backup/recovery appliance to version 11.0.17 to receive these updates.

These features are now available for the Host Agent:

  * Added Linux Changed Block Tracking (CBT) support for Red Hat Enterprise Linux (RHEL) 10 OS family kernels.
  * Expanded Linux Changed Block Tracking (CBT) support across the latest kernel updates for RHEL 8, RHEL 9, and RHEL 10 distributions.



## September 16, 2026

Feature

You can now use auto-protection policies and resource labels to automatically protect Compute Engine instances and Persistent Disks at scale in Backup and DR. This feature allows you to automatically assign a backup plan to qualifying resources across projects based on user-defined labels. This feature is in **Preview**. For more information, see [Automate resource protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/protect/automate-protection).

## September 14, 2026

Feature

You can now monitor restore jobs for Filestore instances directly from the Backup and DR **Jobs** page in the Google Cloud console. When you trigger a restore on a Filestore instance, Backup and DR automatically tracks the job progress and status.

For more information, see [Restore a Filestore instance from a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/filestore/filestore-instance-restore) and [Monitor backup and restore jobs in Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs-console).

## September 01, 2026

Feature

Backup vault support for AlloyDB for PostgreSQL instances encrypted with customer-managed encryption keys (CMEK) is generally available (GA), providing immutable and indelible storage with enforced retention. For more information, see [Encrypt AlloyDB for PostgreSQL cluster backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/alloydb/alloydb-backup#alloydb-encryption-context).

Announcing the general availability (GA) of cross-region backups for AlloyDB for PostgreSQL clusters. You can now protect AlloyDB for PostgreSQL clusters against regional outages by storing backups in a distinct secondary region of your choice. To learn more, see [Backup vaults for immutable and indelible backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/alloydb/alloydb-backup#backup-vaults-for-immutable-and-indel-backups).

## August 24, 2026

Feature

Backup vault support for Filestore instances encrypted with customer-managed encryption keys (CMEK) is now generally available (GA). When you back up Filestore instances to a CMEK-enabled backup vault, the backups are encrypted using the backup vault CMEK key.

For more information, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cmek), [Back up Filestore instances to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/filestore/filestore-instance-backup), and [Restore a Filestore instance from a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/filestore/filestore-instance-restore).

## August 17, 2026

Announcement

Beginning November 1, 2026, Backup and DR will automatically apply a project-level lien to any project containing a backup vault with backups protected by enforced retention. To secure project liens against unauthorized removal and manage lien deletion securely, you can configure multi-party approval using Privileged Access Manager (PAM).

For more information, see [Protect project liens by using Privileged Access Manager](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/project-liens-multi-party-approval) and [Protect projects with liens](https://docs.cloud.google.com/resource-manager/docs/project-liens).

## August 13, 2026

Feature

You can now configure scheduled, application-consistent backups and point-in-time recovery (PITR) workflows for self-managed databases (including IBM Db2, SAP HANA, SAP ASE, SAP IQ, SAP MaxDB, PostgreSQL, MySQL, and MariaDB) running on Compute Engine Linux instances.

This feature uses the bring-your-own-script guest-flush framework to quiesce the database before snapshot creation, ensuring transaction consistency and eliminating data corruption risks. Additionally, you can configure dedicated Persistent Disk backups for database archive logs to enable point-in-time recovery.

For more information, see [Configure application-consistent backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/application-consistent-backups-for-self-managed-databases).

## August 03, 2026

Feature

You can now change the backup plan associated with a Cloud SQL instance. This allows you to switch an instance to a different backup plan, provided the new plan uses the same backup vault and is in the same region as the instance. This feature is available through the Google Cloud console and [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). To learn more, see [Change the associated backup plan for a Cloud SQL instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/sql/csql-backup#change-plan).

## July 31, 2026

Deprecated

Support for backing up SAP ASE, SAP IQ, SAP MaxDB, MariaDB, MySQL, and PostgreSQL databases in the legacy appliance management console is deprecated.

Key milestones for this deprecation include the following:

  * **End of new deployments** : After July 31, 2026, new deployments of the affected databases in the appliance management console are no longer supported.
  * **End of support for new backups** : The ability to create _new_ backups for existing setups of the affected databases in the appliance management console ends on July 31, 2027.
  * **End of migration period** : You must migrate any existing backup data that you want to retain from the appliance management console by December 30, 2027.



To avoid losing your data, we recommend that you migrate your MySQL and PostgreSQL database instances to Google Cloud fully managed database services, such as Cloud SQL or AlloyDB for PostgreSQL. For other database types, use native database backup utilities, third-party backup solutions, or application-consistent backups on Compute Engine.

For more information, see [Migrate from legacy database backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations/migrating-legacy-databases) and [Deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

## July 30, 2026

Feature

You can now configure **selective disk backup** for Compute Engine instances in a backup plan to exclude specific attached non-boot disks from virtual machine (VM) backups. You can configure selective disk backup by backing up only the boot disk (`boot-disk-only`) or by excluding disks that match specified label key-value pairs (`disk-exclusion-labels`). When you restore a VM from a selective disk backup, only the protected disks are restored.

Additionally, you can now perform a **selective disk restore** from a Compute Engine instance backup by selecting the **Individual disk** restore scope. This allows you to selectively restore an individual protected disk from an instance backup to create a new Persistent Disk volume without restoring the entire VM instance.

For more information, see [Selective disk backup for Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup#selective-disk-backup), [Restore limitations for selective disk backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-restore#restore-from-selective-disk-backup), and [Perform a selective disk restore from a Compute Engine instance backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/disk-restore#restore-disk-from-compute-instance-backup).

## July 24, 2026

Feature

You can now use Model Context Protocol (MCP) servers with Backup and DR to connect AI assistants and applications—such as the Gemini CLI, ChatGPT, or Claude—with your backup environment. Using either the local or remote MCP server, you can use natural language prompts to perform and automate Backup and DR tasks, such as creating backup plans, triggering on-demand backups, and managing backup vaults. Comprehensive reference documentation is also available with detailed specifications, input and output schemas, and sample invocation commands for all available MCP tools.

For more information, see the following:

  * [Use the Backup and DR remote MCP server](https://docs.cloud.google.com/backup-disaster-recovery/docs/integrations/remote-mcp)
  * [Backup and DR MCP reference](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/mcp)



## July 10, 2026

Feature

Cloud SQL enhanced backups now supports custom on-demand backups. You can now initiate an on-demand backup with a custom retention period. To cap this retention period, you can specify a maximum retention limit by using the `max-custom-on-demand-retention-days` field when creating a backup plan. Additionally, you can now create a backup plan without scheduled backup rules, provided that the custom on-demand retention period is configured.

For more information, see [On-demand backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/sql/csql-backup#on-demand-backups) and [Create a backup plan with no backup rule](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create#create-backup-plan-with-no-backup-rule).

Feature

  * You can now change the backup plan applied to an existing AlloyDB for PostgreSQL cluster, provided that the new backup plan uses the same backup vault and is in the same region as the AlloyDB for PostgreSQL cluster. For more information, see [Change a backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/alloydb/alloydb-backup#change-plan).

  * You can now take **on-demand backups with custom retention** of your AlloyDB for PostgreSQL cluster at any time, independently of your _scheduled backups_. For more information, see [Create an on-demand backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/alloydb/alloydb-backup#create_an_on-demand_backup).




## July 01, 2026

Feature

Centralized Restore Job Monitoring: You can now monitor restore and point-in-time restore (PITR) jobs for Cloud SQL instances directly from the Backup and DR **Jobs** page in the Google Cloud Console. This provides a unified monitoring experience for all backups and restores managed by Backup and DR.

You can view these job logs in both the backup vault project (for backup administrators) and the target Cloud SQL project (for database administrators).

For more information, see [Monitor jobs in the Google Cloud Console](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs-console).

## June 23, 2026

Feature

Announcing the general availability (GA) of cross-region backups for Backup and DR. Customers can now protect Compute Engine instances, Compute Engine disks, and Filestore instances against regional outages by storing backups in a distinct secondary region of their choice. This functionality enhances disaster recovery capabilities, provides a cost-effective way to ensure regional resilience, and helps maintain strict control over data residency. To learn more, see [Backup vaults for immutable and indelible backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#regions).

Feature

You can now configure application-consistent backups for Compute Engine instances directly through the Google Cloud Console. This enhancement allows you to enable Guest Flush or VSS options within Backup Plans, ensuring data integrity for applications running on Linux or Windows VMs during the backup process. The [Back up Compute Engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup) documentation has been updated with instructions on how to create and modify backup plans to use this feature. 

## June 18, 2026

Feature

Backup vault support for Cloud SQL instances encrypted with customer-managed encryption keys (CMEK) is generally available (GA), providing immutable and indelible storage with enforced retention. For more information, see [Back up Cloud SQL instances to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/sql/csql-backup).

## May 28, 2026

Feature

You can now view the Google Cloud Backup and DR Service protection summary at the organization and folder levels. To learn more about protection summary, see [Find unprotected resources using protection summary](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup-admin/protection-summary).

## May 14, 2026

Feature

These features are now available:

  * Replication Optimization: Introduced a deletion replication optimization for AGM-BA to reduce operational blockages and improve platform performance.

  * Expanded Linux Support: Qualified Linux CBT support has been added for specific kernel versions of RHEL 8 (ranging from 4.18.0-477.128.1 to 4.18.0-553.117.1) and RHEL 9 (ranging from 5.14.0-284.156.1 to 5.14.0-611.47.1), including dedicated support for the SAP OS family, notably RHEL 9.6 for SAP kernels from 5.14.0-570.64.1 to 5.14.0-570.106.1.




SAP HANA Restore Enhancements: Enhanced restore functionality to support alternate host restores and optimized subsequent backups to prevent full backups after an alternate host restore.

Security

Tomcat Vulnerability Mitigation: Upgraded Apache Tomcat to version 9.0.117 to address several high-severity vulnerabilities, including CVE-2026-24734, CVE-2026-34487, and CVE-2026-29146.

Fixed

These issues have been resolved: 

  * vCenter Connectivity: Resolved a critical regression where similarities in IP prefixes caused the Backup Appliance (BA) to incorrectly identify ESX host alternate IPs as potential hostnames for vCenter, leading to server-side certificate validation failures.

  * SAP HANA Backups: Fixed a hang in the dd command during SAP HANA Backint backups by implementing a utility to detect and clean non-printable or binary characters from catalog files.

  * Resource Cleanup: Improved the reliability of the appliance by ensuring loopback devices are properly removed following failed Onvault NFS restore jobs.

  * Restore Stability: Addressed intermittent "Image not found" errors (Error 1263) during restore operations and implemented an early exit in omdtool to prevent gRPC cleanup crashes.

  * Backup Management: Corrected an issue where empty vdiskname entries in the appvdisk table blocked automated cleanup for PDSnap backups and converted the vmtaskcompletiontimeout into a dynamic parameter for better flexibility.

  * Reporting and UI: Enhanced reporting by adding pool names to ZFS listings and removed legacy agent download links from the index-post.html file.




## April 10, 2026

Feature

Expanded OS Support: Qualified Linux Change Block Tracking (CBT) support for multiple new RHEL 8 and 9 kernels, including versions 8.8, 8.10, 9.2, 9.4, and 9.7.

Verbose Process Logging: Added enhanced verbose logging for fingerprint computation and verification to assist in troubleshooting verification failures.

Fixed

  * HANA Backup and Restore Stability: Resolved HANA backup failures by improving the matching logic for alternate IP addresses and addressed restore job failures (error 5728) caused by missing configuration files during the database freeze phase.

  * SAP IQ Log Management: Fixed an issue where SAP IQ log backups would fail due to invisible characters in temporary log file paths.

  * Cleanup and Expiration Improvements: Resolved recurring cleanup job failures (error 1271) by ensuring failed backup images are assigned valid cloud credential IDs.

  * Log Reliability and Diagnostics: Prevented root filesystem exhaustion by rate-limiting excessive UDSAgent logging during custom app activities. Additionally, the UDPINFO logging limit was increased to 10KB to prevent the truncation of large XML messages, facilitating better debugging.




Security

Vulnerability Remediation: Addressed over 38 security vulnerabilities identified in internal and customer scans, including remediations for Kernel, OpenSSL, rsync, glibc, and OpenJDK packages.

## April 08, 2026

Feature

Filestore enhanced backups are now generally available (GA). Enhanced backups are managed and stored by Backup and DR and provide immutable and indelible backups through backup vault, fine grained scheduling, backup protection against source instance deletion and centralized monitoring and reporting.

For more information on protecting Filestore instances using Backup and DR, see [Back up Filestore instances to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/filestore/filestore-instance-backup).

Feature

  * Announcing the general availability (GA) of a 1-hour backup frequency for Compute Engine instances to support mission-critical workloads requiring a lower RPO.

  * Backup and DR now supports Shielded VMs during the restore process, meaning no changes to org policies are required, maintaining a continuous security posture.

  * You can now take application-consistent backups of disk data, enabling the execution of custom pre- and post-scripts. This allows databases and filesystems to be paused or flushed to disk properly before the backup, ensuring a consistent and usable state upon recovery.

**Note:** This capability is available through [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud), Terraform, and API only.
  * Announcing the [Preview](https://cloud.google.com/products#product-launch-stages) launch of cross-region backups. You can now protect resources against regional outages by storing backups in a distinct secondary region, providing a cost-effective way to ensure regional resilience and maintain strict control over data residency. To learn more about cross-region backups, see [Backup vaults for immutable and indelible backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#regions).




## March 17, 2026

Feature

Announcing the general availability (GA) of multi-region backup vaults for Cloud SQL instances.

This release extends our robust data protection capabilities, allowing you to store your Cloud SQL instance backups in backup vaults in multi-region storage locations.

## March 13, 2026

Feature

  * Backup/recovery appliance: Implemented changes to support Google Cloud Hyperdisk extraction.
  * Reporting: Added replication of the `protectiontype` field into the report manager database.



Fixed

  * SAP HANA: Resolved an issue where the `runquery` utility script would fail on RHEL 8.8 due to output redirection.
  * SAP HANA: Fixed a bug causing application discovery to fail when no tenant databases were present.
  * Db2: Addressed failures encountered during Persistent Disk backup image mounts for Db2 instances.



## March 12, 2026

Feature

Announcing the release of the Backup and DR local MCP server. With this you can use natural language prompts to manage Backup and DR jobs.

## March 05, 2026

Feature

AlloyDB enhanced backups are now generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Enhanced backups are managed and stored by Backup and DR and provide immutable and indelible backups through backup vault, fine grained scheduling, backup protection against source project deletion and source cluster deletion, PiTR using logs and centralized monitoring and reporting.

For more information on protecting AlloyDB clusters using Backup and DR, see [Protect and recover an AlloyDB cluster to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/alloydb-quickstart).

## March 03, 2026

Feature

Backup vault support for Compute Engine instances and Persistent Disk encrypted with customer-managed encryption keys (CMEK) is now generally available.

## February 09, 2026

Fixed

  * Compute Engine Instance: Enhanced failure resilience by implementing graceful handling of transient connection failures during Compute Engine API status polling.
  * Oracle: Resolved a race condition that caused duplicate daily backups and corrected initialization parameter mapping for restores to new targets.
  * IBM Db2: Fixed mount operation failures when device lists are missing and enhanced preflight disk validation for complex configurations.
  * SAP HANA: Resolved log backup failures occurring on secured connections and synchronized log retention policies with database backup settings for databases in environments utilizing HANA tenant isolation.

**Note:** For the HANA tenant isolation fix, the backup/recovery appliance and the backup agent must both be on v11.0.17.

Feature

  * Performance: Introduced significant optimizations to increase VMware VM clone/restore throughput.
  * OS Support: Expanded Change Block Tracking (CBT) support to include SLES 15 SP7 and updated kernels for RHEL 8 and 9.



## January 26, 2026

Fixed

Backup/Recovery appliance non-disruptive update:

  * Database Restore & Management: Resolved SAP HANA differential restore failures and Oracle "Mount and Migrate" disk eligibility issues, while enhancing Db2 log purging and HANA /etc/fstab cleanup.
  * System Stability: Improved reliability by addressing gpdmgr memory leaks, preventing udpengine crashes during OnVault jobs, and enabling size-based log rotation.
  * API & Infrastructure: Optimized host discovery and API performance, including support for duplicate VM names, subnet pagination, and the removal of deprecated NFS options.



## January 20, 2026

Feature

Cost reports are now generally available for Backup and DR. Use cost reports to view resource specific Backup & DR Billing costs to gain granular insights into service spend and take actions to optimize resource allocation.

## January 07, 2026

Feature

You can now use cost reports to view resource-specific Backup and DR billing costs to gain granular insights into service spending and to take actions to optimize resource allocation.

Announcement

Protection summary is now generally available for Backup and DR. Use Protection summary to identify and fix data protection gaps across your projects.

## December 22, 2025

Fixed

Backup/Recovery appliance non-disruptive update:

  * Resolved issues with Db2 migration scripts and various SAP HANA backup failures, including differential and log backups.
  * Improved system stability and diagnostics by enhancing logging, adding log rotation, and correcting unit reporting in dashboards.
  * Corrected the data copy reporting for Persistent Disk (PD) based backups, ensuring it accurately reflects zero data copied.



Security

Addressed multiple OpenSSH vulnerabilities, including CVE-2025-26465 and CVE-2025-26466.

Feature

Enhanced performance for restore and clone of VMware VMs.

Expanded Linux CBT support for new kernels on RHEL 8 and 9.

## December 17, 2025

Feature

Backup Vault: CMEK support for Compute Engine (GA) Backup Vault now supports data protection for Compute Engine instances and Persistent Disks encrypted with Customer-Managed Encryption Keys (CMEK). This capability is currently available via Allow-list General Availability; please contact your Google Cloud sales representative to request access.

## December 16, 2025

Feature

Cloud SQL enhanced backups are now generally available (GA). With enhanced backups, backups are managed and stored in a centralized backup management project that leverages [Backup and DR service](https://cloud.google.com/backup-disaster-recovery) to provide enforced retention, granular scheduling, and longer retention. Enhanced backups now also support [point-in-time-recovery (PITR) after instance deletion](https://cloud.google.com/sql/docs/mysql/backup-recovery/restore).

For more information about the available options and their limitations, see [Backup options](https://cloud.google.com/sql/docs/mysql/backup-recovery/backups#backup-options).

For more information about enhanced backups pricing, see [Backup and DR pricing](https://cloud.google.com/backup-disaster-recovery/pricing).

## November 19, 2025

Security

Resolved a decryption failure that occurred when accessing KMS keys.

Fixed

  * Resolved an issue with SAP HANA datafile validation on scale-out clusters.
  * Fixed a bug causing SAP HANA log backups to fail when the log mode is not 'normal'.
  * Addressed failures in Db2 dump full backups in some environments.
  * Corrected an issue where Db2 restore jobs with the roll-forward option were not applying logs completely.



Feature

Added Change Block Tracking (CBT) support for RHEL 8.8 SAP kernels.

## November 07, 2025

Feature

Announcing the public preview launch of Database Center support for resources protected with Backup and DR Service. Database Center is an AI-assisted dashboard that highlights fleet-wide data points.The integration is designed to provide Database Center users with a single, unified, and accurate view of the data protection posture for all databases protected by Backup and DR Service.This capability is available today, at no additional cost, for all Cloud SQL customers who have protected their databases through Backup and DR Service enhanced protection.

## October 30, 2025

Feature

Announcing the **Public Preview** launch of AlloyDB for PostgreSQL enhanced backups with Backup and DR Service. This enables advanced data protection capabilities offered by Backup and DR Service including backup vault support, granular scheduling through backup plans, and centralized management.

Feature

A new backup vault setting, **Prevent deletion for duration specified in backup rule** , is now available. When enabled, this feature locks backups for the exact retention period defined in the associated backup plan, overriding the vault's local minimum retention and preventing manual deletion.

## October 21, 2025

Fixed

  * Resolved a problem with timestamp conversions during recovery range calculations in SAP HANA
  * Fixed a bug that prevented the identification of persistent disk names in some SAP HANA environments
  * Fixed DB2 restore issue wrt pre-flight checks and instances with a large number of archive logs
  * Fixed a logging issue during Postgres upgrades where an incorrect version was displayed after a rollback
  * Resolved a restore failure when using a combination of full and incremental backups for SAP ASE
  * Fixed a connection leak and an issue with executor service shutdown in the VMware hypervisor integration, improving reliability.



Security

The following CVEs have been addressed in this release: CVE-2022-1471, CVE-2025-31651, CVE-2025-31650, CVE-2022-42003, CVE-2025-25193, CVE-2024-6763, CVE-2025-52999, CVE-2025-24970, CVE-2025-49125, CVE-2025-48734, CVE-2024-52317, CVE-2025-48988, CVE-2025-46701

Feature

  * Change Block Tracking (CBT) support has been added for latest kernel versions in RHEL 8.10, 9.2, 9.4 and 9.6.
  * Improved alerting for long-running jobs by adding application type and name to the alerts.



## October 15, 2025

Announcement

Backup and DR Service 11.0.16.253 is now available to update your backup/recovery appliances. Refer to these [instructions](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance) to update your appliance.

  * Guardrails have been defined for each backup/recovery appliance to specify the number of supported job slots, ensuring smooth parallel backup and mount jobs.



Introducing notifications and alerts for the following critical events:

  * Processes not running on a backup/recovery appliance
  * Expired certificates
  * No jobs running on a backup/recovery appliance
  * CPU and memory usage exceeding threshold values
  * Backup/recovery appliance appliance version out of support
  * Backup/recovery appliance updates available



You can subscribe to these events and configure email alerts.

## October 14, 2025

Feature

You can now set up backup vault specific workload quotas for critical resources like data sources, backups, backup plans, and backup plan associations. Until now these quotas were set up only at the project level, not at the workload level.

## September 03, 2025

Fixed

An issue where Backup and DR Service management charges for SAP HANA backup were calculated using the allocated size of the database disk volume, rather than the amount of data in the database. This issue only affected Backup and DR Service deployments where SAP HANA was backed up using either the Volume level (LVM CBT) or Persistent Disk snapshot backup methods.

## August 27, 2025

Announcement

Announcing the 30-Day Introductory Trial for Google Cloud Backup and DR Service

You can now activate a 30-day, full-featured introductory trial of the Backup and DR Service on any project that does not have an active Backup and DR configuration. The trial provides a hands-on experience with all features, from centralized management to our advanced immutable backup vault, without any initial commitment.

## August 12, 2025

Announcement

Announcing the General Availability (GA) of Backup Vault support for independent Persistent Disks and Hyperdisks!

This new capability empowers you to protect application data, databases, and file shares stored on individual disks (where a full VM backup is not required) — all within a secure, immutable, logically air-gapped vault designed to withstand malicious deletion and advanced threats like ransomware.

## July 31, 2025

Announcement

Announcing the **Public Preview launch of Cloud SQL enhanced backups** with Backup and DR. This enables advanced data protection capabilities offered by Backup and DR including backup vault support, granular scheduling through backup plans, and centralized management.

## July 11, 2025

Announcement

We're excited to announce the launch of Editable Backup Plans, a new feature designed to give you more flexibility and control over your data protection strategy. You can now modify your existing backup plans directly, eliminating the need to create new plans and reassign them when your requirements change. This makes it easier than ever to adapt to evolving business needs, optimize for cost, and correct configuration errors on the fly.

What's new:

  * Directly Edit Key Settings: You can now change the description, schedule, backup window, and retention periods of your existing backup plans. You can also add or remove backup rules as needed.

  * Automatic Updates: Once a plan is edited, the changes are automatically applied to all resources protected by that plan for all future backups. There's no need to manually detach and reattach the plan.

  * Backward Compatibility: This new capability is available for all backup plans, including those created before this update.




Important Note: While most settings in a backup plan are now editable, the assigned backup vault cannot be changed. To store backups in a different vault, a new backup plan must be created.

## June 16, 2025

Announcement

Announcing the General Availability (GA) of multi-region backup vaults.

You can now create backup vaults in multi-region storage locations. This new capability allows you to leverage the security benefits of backup vault, while also enhancing your ability to maintain accessibility and recoverability of critical backup data during a regional service disruption (such as natural disasters and power outages).

## May 21, 2025

Announcement

Backup and DR Service 11.0.15.226 is now available to update your backup/recovery appliance. Refer to these [instructions](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance) to update your appliance.

Announcement

There is a new committed use discount (CUD) for customers using Backup and DR Service to protect Oracle databases into a backup vault. This is a way to lower backup costs in consideration of a 1-year or 3-year commitment. You can purchase CUDs from Google Cloud Marketplace via the standard process.

Fixed

These issues have been fixed:

  * An issue in which multiple snapshot/Direct OnVault jobs became stuck in an unresponsive state after attempting to connect to vCenter with an openssl command.
  * An issue in which database persistent disk snapshot backup jobs failed with the unhelpful error message `resource not found` now has a useful error message.
  * An issue in which Log explorer was showing some spurious "read error, check permissions" results on backup/recovery appliances.
  * An issue in which a backup/recovery appliance could come out of synchronization with a management console following a `Trying to release lock` or `Failed to acquire lock` error.
  * A rare issue in which a backup/recovery appliance became unresponsive after a very heavy load exhausted all job threads and /var/log/ was 100% full. Thread management is now more efficient.
  * An issue in which persistent disk database snapshot images were failing to import log backups, and the recovery range was missing on imported backups.
  * An issue in which some backups of PostgreSQL version 15 failed due to a premature timeout.
  * An issue in which some mount jobs failed if the host's lvmconfig has global/system_id_source set to `uname`.
  * An issue in which database names provided in mount screen were not honored correctly when creating child applications on the target host.
  * The `Staging disk is full` error message has been made more useful.



Feature

Backup and DR Service now supports backup and restore of Db2 databases using persistent disk snapshots. This is typically faster and simpler than previous methods and in some cases may also reduce costs.

Feature

This release introduces enhanced logging and alerting capabilities for [backup/recovery appliances](https://docs.cloud.google.com/backup-disaster-recovery/docs/event-codes), enabling proactive monitoring of their health and status. You can now configure email notifications via Cloud Logging to receive timely alerts on appliance status changes or potential issues, and five new events have been added for more granular monitoring:

  * 10237: Jobs running over 6 hours.
  * 11001: Backup/recovery appliance certificate expires in X days.
  * 11004: Backup/recovery appliance system components are down.
  * 11006: Backup/recovery appliance unable to sync with host.
  * 90003: A new backup/recovery appliance update is available.



Security

Vulnerabilities CVE-2024-42301, CVE-2024-42284, and CVE-2024-41092 have been fixed at kernel version 4.18.0-553.33.1.el8_10.

## May 20, 2025

Announcement

Introducing preview of a simplified one-step procedure for changing backup plans assigned to your Compute Engine VMs. Previously, changing the backup plan for a VM required removing the existing plan and then applying the new plan. With this update, you can now change the backup plan for a VM in a single operation. This enhancement streamlines your workflow, making it quicker and more efficient to ensure your VMs are protected by the desired backup strategy.

## March 24, 2025

Announcement

The Backup and DR service has added support for activating the [management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-plan#mc-supported-regions), for creating [backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan#backup_plan_supported_regions), and for storing [backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#regions) data in the following regions: northamerica-northeast1 (Montréal), northamerica-northeast2 (Toronto), and asia-east2 (Hong Kong).

## March 14, 2025

Feature

**Generally available** : The **Create an instance** page in the Google Cloud console has a **Data protection** pane where you can specify how to back up and replicate your data. For more information, see [Configuration options during instance creation](https://docs.cloud.google.com/compute/docs/instances/instance-creation-overview#new-instance-configuration-options) and [Data protection options](https://docs.cloud.google.com/compute/docs/disks/data-protection).

## February 28, 2025

Announcement

Security Command Center adds threat detection support for Backup Vault, Backup Plans, and vaulted backups.

Security Command Center released [new rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules) for Google Cloud Backup and DR Service. Security Command Center can now do the following:

  * Detect Backup Vault deletions
  * Detect Backup Plan deletions
  * Detect deletion of backups stored in a Backup Vault



These detectors are available to all Security Command Center Premium and Enterprise customers. For more information, see [Security Command Center for Backup and DR Service](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/alerts-scc).

Announcement

The Backup and DR service has added support for activating the management console and for storing backup vault data in the following regions: us-west3 (Salt Lake City), europe-west9 (Paris), me-west1 (Israel), europe-north1 (Finland), europe-west6 (Zürich), asia-northeast3 (Seoul), southamerica-west1 (Santiago).

## February 27, 2025

Announcement

Backup and DR now supports the latest RHEL and SLES OS and kernels in backup/recovery appliance 11.0.13 and later:

**RHEL 8.8** : 4.18.0-477.36.1, 4.18.0-477.43.1, 4.18.0-477.51.1, 4.18.0-477.55.1, 4.18.0-477.58.1, 4.18.0-477.64.1, 4.18.0-477.67.1, 4.18.0-477.70.1, 4.18.0-477.75.1, 4.18.0-477.81.1, 4.18.0-477.83.1

**RHEL 8.10** : 4.18.0-553.30.1, 4.18.0-553.32.1, 4.18.0-553.33.1

**RHEL 9.3** : 5.14.0-362.24.1

**RHEL 9.4** : 5.14.0-427.13.1, 5.14.0-427.16.1, 5.14.0-427.18.1, 5.14.0-427.20.1, 5.14.0-427.22.1, 5.14.0-427.24.1, 5.14.0-427.26.1, 5.14.0-427.28.1, 5.14.0-427.31.1, 5.14.0-427.33.1, 5.14.0-427.35.1, 5.14.0-427.37.1, 5.14.0-427.40.1, 5.14.0-427.42.1

**RHEL 9.5** : 5.14.0-503.11.1, 5.14.0-503.14.1, 5.14.0-503.15.1, 5.14.0-503.16.1, 5.14.0-503.19.1

**SLES 15 SP6** : All kernels

## February 26, 2025

Announcement

Backup and DR Service 11.0.14.302 is now available to update your backup/recovery appliance. Refer to these [instructions](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance) to update your appliance.

Backup and DR Service 11.0.14.302 includes the following fixes and improvements:

  * The following CVEs have been addressed in this hotfix: CVE-2024-42301, CVE-2024-42284, CVE-2024-41092
  * In some cases, a database that has data on multiple volumes can be mounted successfully, but a subsequent unmount operation fails. This has been fixed.
  * In rare cases, the management console could lose the connection to the backup appliance for up to an hour, after which it automatically recovered. During the disconnection, the scheduled backups continued to be taken but the jobs monitor could not show progress and new on-demand jobs could not be run. This has been fixed. 
  * A Db2 log backup to a full disk failed without notification. With this hotfix, upon failure the disk is resized and the backup job is retried successfully.
  * A persistent disk backup job for an SAP HANA or an IBM Db2 database fails if the backup/recovery appliance includes another host with the same name in a different project. This has been fixed.
  * Imported persistent disk snapshots of SAP HANA and Db2 databases sometimes failed to mount or to restore if the database host had a custom (non-default) PD disk names. This fix ensures that these imported databases can be successfully mounted and restored.
  * For SAP IQ databases, the INC_BKP.1 file (a config file) is backed up. It can be a large file that consumes much storage, so starting with this hotfix the config file is compressed for backup.
  * Recovery of an IBM Db2 database from a standby image sometimes failed. This has been fixed.
  * Backup and DR now supports "Import without ownership" for SAP HANA and IBM Db2 databases and logs.



## February 20, 2025

Announcement

Protection summary is now available for public preview. Protection summary provides a centralized, single-pane-of-glass view of your backup configurations for resources running within your Google Cloud project. Use protection summary to gain a holistic understanding of your backup state, identify gaps in coverage, and implement centralized backup management strategies. You can read about protection summary at [Use protection summary](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup-admin/protection-summary).

## February 04, 2025

Announcement

The Backup and DR service has added support for activating the management console and for storing backup vault data in the following regions: us-east5, asia-northeast1, and asia-southeast2.

## January 24, 2025

Fixed

Fixes for Oracle databases backed up to OnVault and backup vault

  * Hosts from both source and remote backup appliances are now listed in the restore page. For cases when no host is reachable or the primary backup appliance is down, the UI was improved by showing a spinning wheel to avoid waiting for longer than necessary while attempting to restore from an imported image.

  * A **Replace Original Application Identity** option has been added for Oracle traditional restore functionality.




Feature

For updates to the backup appliance, a default window now exists to schedule non disruptive patch updates. (Disruptive updates do not get the default window.) You will now receive notifications 2 weeks , 1 week and 24 hours before the scheduled update after which the appliance will be automatically updated. An option to reschedule non disruptive patch updates is also available.

Fixed

Fixes for SAP HANA Persistent Disk Snapshots

  * Enhancing imports of log images: Log images can now be imported correctly with the right recovery range. Enabled importing log images without having to take the ownership of the images. Fixed the workflow for importing on the source management server instance and another new management server instance.

  * UI fixes for point-in-time recovery from imported images: Imported images appear in the remote snapshot lane in access view, populating correct recovery range for imported images, populating recovery time in restore operation request, adding archive log mount point location in restore page, disabling **Replace Original Application Identity** for remote images, mount page waiting indefinitely for imported image, adding import PD snapshot option in application page, enabling host selection drop-downs for replication cluster etc.

  * BA fixes: Issues with uploading metadata for replication clusters and with point-in-time recovery from imported images were fixed.




Security

The following CVEs have been addressed in this release: CVE-2024-38286, CVE-2019-9636, CVE-2023-5178, CVE-2020-14343, CVE-2021-29921, CVE-2019-7164, CVE-2020-27619, CVE-2018-20060, CVE-2019-20477, CVE-2019-9948, CVE-2020-1747, CVE-2021-3177, CVE-2022-42919, CVE-2024-0565, CVE-2015-20107, CVE-2023-51042, CVE-2020-10878, CVE-2023-6546, CVE-2022-0391, CVE-2022-45884, CVE-2021-33631, CVE-2020-10543, CVE-2019-20907, CVE-2023-3812, CVE-2019-11324, CVE-2022-45919, CVE-2023-6931, CVE-2024-1086, CVE-2021-43818, CVE-2021-33503, CVE-2020-26116, CVE-2019-20916, CVE-2023-2163, CVE-2021-42771, CVE-2022-45886, CVE-2021-3737, CVE-2023-52425, CVE-2018-18074, CVE-2021-27291, CVE-2021-20270, CVE-2023-24329, CVE-2019-18874, CVE-2019-16056, CVE-2019-7548, CVE-2021-3572, CVE-2019-9740, CVE-2021-23336, CVE-2020-14422, CVE-2021-3426, CVE-2023-1192, CVE-2022-38096, CVE-2023-6135, CVE-2020-8492, CVE-2020-27783, CVE-2020-28493, CVE-2023-46218, CVE-2021-4189, CVE-2020-26137, CVE-2021-3733, CVE-2019-16935, CVE-2021-28957, CVE-2018-20852, CVE-2019-11236, CVE-2019-9947, CVE-2020-28241, CVE-2023-5388, CVE-2023-28322 CVE-2022-48624, CVE-2023-38546, CVE-2021-20095

## December 02, 2024

Feature

Backup and DR service added integration with the Compute Engine VM creation experience, enabling the application of Backup and DR backup policies when VMs are created. This feature is now generally available.

Feature

Backup and DR service added centralized backup management within Google Cloud console, with support for [Compute Engine VM backup to backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup). This feature is now generally available.

Feature

Backup and DR service added support for immutable and indelible backups with the new [backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault) feature. This feature is now generally available.

## November 21, 2024

Fixed

This release fixes an issue with OnVault pool jobs leaving behind inactive cloudbacker mountpoints. It does this by retrying the unmount process a set number of times, including forced unmounts. Due to the increased number of retries and the wait time between them, job durations may be slightly longer.

Deprecated

This release deprecates support for ssh-rsa as the ssh Host Key algorithm.

Security

This release fixes the following Kernel vulnerabilities: 

CRITICAL Kernel issues: CVE-2023-25775 CVE-2019-15505

MEDIUM Kernel issues CVE-2019-13631 CVE-2020-25656 CVE-2020-26555 CVE-2020-36777 CVE-2021-3753 CVE-2021-46909 CVE-2021-46939 CVE-2021-47171 CVE-2022-38096 CVE-2022-48743 CVE-2023-1192 CVE-2023-4133 CVE-2023-5090 CVE-2023-6121 CVE-2023-6176 CVE-2023-6240 CVE-2023-6622 CVE-2023-6915 CVE-2023-24023 CVE-2023-31083 CVE-2023-37453 CVE-2023-38409 CVE-2023-39189 CVE-2023-39192 CVE-2023-39193 CVE-2023-39194 CVE-2023-39198 CVE-2023-42754 CVE-2023-42755 CVE-2023-45863 CVE-2023-52448 CVE-2023-52463 CVE-2023-52471 CVE-2024-0340 CVE-2024-21140 CVE-2024-21145 CVE-2024-25739 CVE-2024-26583 CVE-2024-26584 CVE-2024-26585 CVE-2024-26586 CVE-2024-26602 CVE-2024-26603 CVE-2024-26901 CVE-2024-26908 CVE-2024-27014 CVE-2024-27019 CVE-2024-36270 CVE-2024-36489 CVE-2024-38598 CVE-2024-39472 CVE-2024-39476

HIGH Kernel issues: CVE-2019-25162 CVE-2021-4204 CVE-2021-33631 CVE-2021-47624 CVE-2022-0500 CVE-2022-3565 CVE-2022-23222 CVE-2022-45884 CVE-2022-45886 CVE-2022-45919 CVE-2022-45934 CVE-2023-2163 CVE-2023-3567 CVE-2023-3812 CVE-2023-4244 CVE-2023-5178 CVE-2023-6546 CVE-2023-6931 CVE-2023-6932 CVE-2023-28464 CVE-2023-51042 CVE-2023-51780 CVE-2023-52340 CVE-2023-52434 CVE-2023-52439 CVE-2023-52445 CVE-2023-52451 CVE-2023-52464 CVE-2023-52469 CVE-2024-0565 CVE-2024-0841 CVE-2024-1086 CVE-2024-21147 CVE-2024-23307 CVE-2024-25744 CVE-2024-26593 CVE-2024-26907 CVE-2024-26933 CVE-2024-26934 CVE-2024-27020 CVE-2024-36971 CVE-2024-36978 CVE-2024-36979 CVE-2024-38538 CVE-2024-38555 CVE-2024-38627 CVE-2024-39487

Fixed

This release fixes an issue where SAP HANA database and log backup jobs using Persistent Disk snapshots would complete with a warning status due to metadata upload failures to Google Cloud Storage for disaster recovery.

Change

This release removes the 700 thread hard limit and psrv restarts at 800 threads when the psrv is at high usage.

Fixed

This release fixes the synchronization between database and log backup states. Log backups should not copy the logs to the database staging after the database staging disk is unmounted and the state DBBACKUP_DONE is set.

Security

This release fixes the Tomcat vulnerability CVE-2024-38286.

## October 21, 2024

Feature

Backup and DR service added support to deploy new management console without the need to create private services access. You can also deploy backup/recovery appliances in any VPC available within the management console project.

## October 17, 2024

Feature

Backup and DR Service added support to view [connector version logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/connector-version) in Cloud Logging.

Announcement

Backup and DR Service 11.0.13.278 is now available to update your backup/recovery appliance. Refer to these [instructions](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance) to update your appliance.

Feature

Backup and DR Service added support to view [connector version reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/connector-reports-bigquery) in BigQuery.

## September 30, 2024

Feature

Backup and DR Service added support to view [unprotected resource reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/unprotected-resource-reports) in BigQuery.

Feature

Backup and DR Service added support to view [unprotected resource logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/unprotected-resource-logs) in Cloud Logging.

## September 10, 2024

Feature

Backup and DR service added support for immutable and indelible backups via the new [backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault) feature. This feature is in Preview.

Feature

Backup and DR service added centralized backup management within Google Cloud console, with support for [Compute Engine VM backup to backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup). This feature is in Preview.

Feature

Backup and DR service added integration with the Compute Engine VM creation experience, enabling the application of Backup and DR backup policies when VMs are created. This feature is in Preview.

## September 04, 2024

Feature

Backup and DR Service added support to [automatically protect your Google Cloud VMware Engine VMs using vSphere tags](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/dynamic-protection-gcve). The dynamic protection tags feature is supported for backup/recovery appliances running on version 11.0.12.320 or later. You can check the appliance version from **Manage** > **Appliances** page.

## September 02, 2024

Feature

Backup and DR Service added support to view [mounted image reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/mounted-images-reports-bigquery) in BigQuery.

Feature

Backup and DR Service added support to view [mounted image logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/mounted-images-logs) in Cloud Logging.

## August 20, 2024

Announcement

Backup and DR Service hotfixes `hf-11.0.12.3217`, `hf-11.0.12.3218`, and `hf-11.0.12.3219` automatically update backup/recovery appliances. These hotfixes address the following issues:

  * Oracle DB application backups wait indefinitely for in-progress log backups to complete. These log backups, in turn, cannot obtain a lock mutex to discover the backup staging LUNs, resulting in an indefinite hang. This issue occurs when the size of the application transaction logs exceeds the log backup staging size.
  * Cloud stats are repeatedly logged into the enginemgr log and increase log usage.



## August 07, 2024

Announcement

Management console is now available in the London (`europe-west2`), Mumbai (`asia-south1`), and Los Angeles (`us-west2`) regions.

Announcement

Backup and DR Service 11.0.12.322 is now available to update your backup/recovery appliance. Refer to these [instructions](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance) to update your appliance.

Feature

Backup and DR Service now supports migrating manual protection to dynamic protection using tags through management console. [Learn more](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/dynamic-protection#migrate_manual_protection_to_dynamic_protection).

Feature

Backup and DR service now supports restoring Oracle database to any target. [Learn more](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-oracle#any-target).

## June 11, 2024

Feature

Backup and DR Service added support to view [storage resource utilization reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/utilization-reports-bigquery) in BigQuery.

Feature

Backup and DR Service added support to view [storage resource usage logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/storage-utilization-logs) in Cloud Logging.

## May 21, 2024

Feature

Backup and DR Service supports migrating from manual protection to the new dynamic protection using tags. It is now also supported on all types of backup/recovery appliances. [Learn more](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/dynamic-protection#migrate_manual_protection_to_dynamic_protection).

Announcement

Backup and DR Service 11.0.11.323 is now available to update your backup/recovery appliance. Refer to these [instructions](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance) to update your appliance.

Issue

If the management console and backup/recovery appliance connectivity is not established for more than 6 hours, contact customer support to resolve the issue. This is particularly relevant to the appliance running on version 11.0.11.323 or later. You can check the connection status from the Connectivity column in the **Manage** > **Appliances** page.

Feature

Backup and DR Service now supports auto patch updates. [Learn more](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance).

## May 06, 2024

Announcement

Backup and DR Service 11.0.10.425 is now available to update your backup/recovery appliance. Refer to these [instructions](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance) to update your appliance. This release includes fixes for the following security vulnerabilities:

  * [CVE-2021-35937](https://nvd.nist.gov/vuln/detail/CVE-2021-35937)
  * [CVE-2021-35939](https://nvd.nist.gov/vuln/detail/CVE-2021-35939)
  * [CVE-2022-48560](https://nvd.nist.gov/vuln/detail/CVE-2022-48560)
  * [CVE-2022-48564](https://nvd.nist.gov/vuln/detail/CVE-2022-48564)
  * [CVE-2023-1667](https://nvd.nist.gov/vuln/detail/CVE-2023-1667)
  * [CVE-2023-7104](https://nvd.nist.gov/vuln/detail/CVE-2023-7104)
  * [CVE-2023-27043](https://nvd.nist.gov/vuln/detail/CVE-2023-27043)
  * [CVE-2023-28484](https://nvd.nist.gov/vuln/detail/CVE-2023-28484)
  * [CVE-2023-28486](https://nvd.nist.gov/vuln/detail/CVE-2023-28486)
  * [CVE-2023-28487](https://nvd.nist.gov/vuln/detail/CVE-2023-28487)
  * [CVE-2023-29469](https://nvd.nist.gov/vuln/detail/CVE-2023-29469)
  * [CVE-2023-38408](https://nvd.nist.gov/vuln/detail/CVE-2023-38408)
  * [CVE-2023-39615](https://nvd.nist.gov/vuln/detail/CVE-2023-39615)
  * [CVE-2023-42465](https://nvd.nist.gov/vuln/detail/CVE-2023-42465)
  * [CVE-2023-48795](https://nvd.nist.gov/vuln/detail/CVE-2023-48795)



## April 22, 2024

Feature

Backup and DR Service now support viewing Backup and DR Service pre built reports in Looker Studio. [Learn more](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-lookerstudio).

## April 01, 2024

Feature

Backup and DR Service added support to [automatically protect your compute engine instances](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/dynamic-protection) using Google Cloud tags. The dynamic protection tags feature is supported for backup/recovery appliances running on version 11.0.10.417 or later. You can check the appliance version from **Manage** > **Appliances** page.

## March 29, 2024

Change

For SAP HANA databases, the database and log backups are not run together in parallel.

## March 25, 2024

Feature

Backup and DR Service added support to view [daily scheduled compliance reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/compliance-reports-bigquery) in BigQuery.

Feature

Backup and DR Service added support to view [daily scheduled compliance logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/compliance-logs) in Cloud Logging.

## March 21, 2024

Announcement

Backup and DR Service 11.0.10.417 is now available to update your backup/recovery appliance. Refer to these [instructions](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance) to update your appliance.

Feature

Backup and DR Service added support to access historical reports. [Learn more](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/access-report).

Announcement

Backup and DR Service 11.0.10 includes an operating system upgrade from CentOS 7 to Rocky Linux 8. As CentOS 7 will reach its End of Life (EOL) on June 24, 2024, you must upgrade to 11.0.10 before the EOL date to continue receiving security updates. 

To upgrade to 11.0.10, you should take a snapshot of the appliance's boot disk. If your backup/recovery appliance was originally deployed as version 11.0.5 or below, then you need to upgrade to 11.0.9 before successfully upgrading to 11.0.10. See [11.0.9 release notes](https://docs.cloud.google.com/backup-disaster-recovery/docs/release-notes#February_16_2024) to know how to back up the boot disk.

## February 28, 2024

Feature

Backup and DR Service is now integrated with Cloud Monitoring. You can analyze metrics and set custom email alerts. [Learn more](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/metrics).

Feature

You can now view comprehensive job related reporting data through backup and recovery job logs in Cloud Logging. [Learn more](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/job-logs).

Feature

You can now view prebuilt reports in BigQuery. [Learn more](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery).

Feature

Backup and DR Service has added a new reporting system based on the built-in Google Cloud services: Cloud Monitoring, Cloud Logging, and BigQuery. [Learn more](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/reports-overview).

## February 16, 2024

Feature

Backup and DR Service now supports Google Cloud VMware Engine Storage only nodes. [Learn more](https://cloud.google.com/backup-disaster-recovery/pricing).

Feature

SAP HANA databases running in Compute Engine instances can now be backed up as Persistent Disk snapshots of the Compute Engine instance. For more information, see [protect and recover an SAP HANA database running in a Compute Engine instance](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/sap-hana-on-gce-backup-recovery).

Announcement

Backup and DR Service 11.0.9.429 is now available to update your backup/recovery appliance. Refer to these [instructions](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance) to update your appliance.

Announcement

The upcoming 11.0.10 release includes an important OS change. If your backup appliance was originally installed as version 11.0.5 or older (before July 2023), then the 11.0.9 upgrade includes an additional automated procedure to prepare for the coming upgrade by making some adjustments to the backup appliance's boot disk partitions. This additional procedure takes about 30 minutes.

If the upgrade is disrupted, there is a chance that the backup/recovery appliance might become non-functional. To prepare for this risk, it is highly recommended that you take a snapshot of the backup appliance boot disk before upgrading the appliance to 11.0.9. If the backup appliance is not back online after the upgrade, contact the Backup and DR support team. Here is a brief guide for how to take the snapshot:  


  1. In the Backup and DR management console, click **Manage** > **Appliances** and write down or screen-capture the appliance names.
  2. In the Google Cloud console of your workload project, click **Compute Engine** > **VM instances**.
  3. Identify the backup appliance VM instance with the same name as that shown in the Backup and DR management console.
  4. [Take a snapshot of the backup appliance boot disk](https://cloud.google.com/compute/docs/disks/create-snapshots). If you need assistance taking the snapshot, [contact the Backup and DR support team](https://docs.cloud.google.com/backup-disaster-recovery/docs/support).
  5. [Contact the Backup and DR support team](https://docs.cloud.google.com/backup-disaster-recovery/docs/support) if the appliance becomes non-functional after the upgrade. The support team will determine the best way to mitigate the problem.   
Caution: Do NOT try to restore the bootdisk from the snapshot without assistance from Support. Doing so may damage the appliance and make it unrecoverable.
  6. Delete the snapshot once you confirm that the appliance is online using version 11.0.9.



Feature

Added Change Block Tracking (CBT) support for the following OSes. See [Support matrix](https://docs.cloud.google.com/backup-disaster-recovery/docs/supportmatrix-backupdr). 

* SLES 15 SP5
* SLES for SAP 15 SP5

Feature

Added basic connector support for the following OSes. See [Support matrix](https://docs.cloud.google.com/backup-disaster-recovery/docs/supportmatrix-backupdr). 

  * RHEL 8.9
  * RHEL 9.3
  * Rocky Linux 8.9
  * Rocky Linux 9.3
  * Rocky Linux Optimized for Google Cloud 8.9
  * Rocky Linux Optimized for Google Cloud 9.3



## December 20, 2023

Feature

Added support to create a management console using [Google Cloud CLI](https://docs.cloud.google.com/backup-disaster-recovery/docs/deployment/deployment-guide#gcloud).

## December 01, 2023

Feature

Management console is now highly available within the deployed region, ensuring resilience against zonal outages.

## November 21, 2023

Feature

SAP HANA databases running in Compute Engine instances can now be backed up as Persistent Disk snapshots of the Compute Engine instance. This feature is in Private Preview.

Feature

Added basic connector support for the following OSes. See [Support matrix](https://cloud.google.com/backup-disaster-recovery/docs/supportmatrix-backupdr). 

  * OEL 8.8, 9.1, and 9.2
  * RHEL 8.8 and 9.2
  * RHEL for SAP 8.8, 9.0, and 9.2
  * Rocky Linux 8.8, 9.0, 9.1, and 9.2
  * Rocky Linux Optimised for Google Cloud 8.8 and 9.2
  * SLES 15 SP5
  * SLES for SAP 15 SP5



Announcement

Backup and DR Service 11.0.8.454 is now available to update your backup/recovery appliance. Refer to these [instructions](https://cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance) to update your appliance.

Feature

Added support to view successful job events and set up [alerts](https://cloud.google.com/backup-disaster-recovery/docs/configure-alerts) to notify you when a job has successfully completed.

## October 19, 2023

Feature

Security Command Center Premium adds real-time threat detection for Google Cloud Backup and DR Service. Event Threat Detection, a Security Command Center Premium service, released [new rules](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview#rules) for Google Cloud Backup and DR Service. Security Command Center can now do the following: 

  * Detect Backup and DR actions that result in data destruction.
  * Detect Backup and DR actions that inhibit inhibit system recovery.

These new rules are available now to all Security Command Center Premium customers. For more information, see [Security Command Center Premium for Backup and DR Service](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/alerts-scc).

## October 06, 2023

Announcement

Backup and DR Service 11.0.7.404 is now available to update your backup/recovery appliance. Refer to these [instructions](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance) to update your appliance.

Feature

Added support to restore PostgreSQL database backup images to an alternate location. [Learn more](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-postgresql).

Feature

Backup and DR agent now supports Rocky Linux 8.7 on Oracle 19c database. See [support matrix](https://docs.cloud.google.com/backup-disaster-recovery/docs/supportmatrix-backupdr).

Feature

Backup and DR agent is enhanced to support Rocky Linux 8.7 operating system version. See [support matrix](https://docs.cloud.google.com/backup-disaster-recovery/docs/supportmatrix-backupdr).

Announcement

The new Backup and DR Service update policy requires updating all backup/recovery appliances older than version 11.0.3 to maintain product support and avoid restrictions on enabling backups for new entities. [Learn more](https://docs.cloud.google.com/backup-disaster-recovery/docs/bulletins/backupdr-update-policy).

Feature

Backup and DR agent now supports RHEL 8.4 on Oracle 21c database. See [support matrix](https://docs.cloud.google.com/backup-disaster-recovery/docs/supportmatrix-backupdr).

## August 21, 2023

Feature

Backup and DR Service now supports [backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-snapshot-images-of-cloud-instances#new) and [restore](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-compute-engine) of Compute Engine instances with local SSDs.

Feature

Backup and DR Service now supports in-product notifications for important product updates.

Feature

Backup and DR Service now supports roll back of hotfix updates. For more information, see [Rollback a hotfix update](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance#rollback).

Change

Pricing model for protecting Google Cloud VMware Engine workloads has been updated to a node based flat rate model. For more information, see [pricing change announcement](https://docs.cloud.google.com/backup-disaster-recovery/docs/bulletins/billing).

Feature

Backup and DR Service now supports concurrent database and log backups. For more information, see [Manage image expiration](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/manage-image-expiration).

Announcement

Backup and DR Service 11.0.6.342 is now available to update your appliance. Refer to the [instructions](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance) to update your appliance.

## July 10, 2023

Feature

Backup and DR Service is now integrated with cloud Identity and Access Management (IAM). Refer to [IAM roles and permissions](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-control) to learn more.

Feature

Backup and DR service now manages hotfixes on backup/recovery appliances.

Feature

Backup and DR Service significantly reduced recovery time objective (RTO) for Oracle databases by bringing up production workloads almost instantly, running from backup storage, and then migrating the database to production storage online—while applications are up and running.

Announcement

Backup and DR Service 11.0.5.447 is now available to update your appliance. Refer to the [instructions](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance) to update your appliance.

Feature

Backup and DR Service is now integrated with cloud [audit logging](https://docs.cloud.google.com/backup-disaster-recovery/docs/audit-logging).

## April 28, 2023

Feature

Backup and DR agent is enhanced to support RHEL for SAP 8.6 operating system version. See [Support matrix](https://docs.cloud.google.com/backup-disaster-recovery/docs/supportmatrix-backupdr).

## April 27, 2023

Feature

Simplified experience for [updating backup/recovery appliances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/update-appliance) from the management console.

Feature

Backup and DR agent is enhanced to support Oracle Enterprise Linux 8.7 and 9.0 operating system version. See [Support matrix](https://docs.cloud.google.com/backup-disaster-recovery/docs/supportmatrix-backupdr).

Feature

Backup and DR agent is enhanced to support RHEL 8.6, RHEL 8.7, and RHEL 9.0 operating system version. See [Support matrix](https://docs.cloud.google.com/backup-disaster-recovery/docs/supportmatrix-backupdr).

Feature

Backup and DR Service now supports [archive snapshots](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings) for Compute Engine instance backups.

Announcement

Backup and DR Service release 11.0.4.580 is now available. This release includes the following features:

## April 14, 2023

Issue

If you migrate from Actifio GO to Backup and DR 11.0.2 or later, then you may see error message "Lvmetad service is running, please disable the service. Make sure to disable lvmetad in /etc/lvm/lvm.conf. Refer to KB article number 000045289 for more details". If this occurs, backup jobs may fail. Lvmetad is not required for any Backup and DR services; disable it to prevent this failure. To disable lvmetad, contact [Support](https://cloud.google.com/support/docs/manage-cases).

lvmetad is being deprecated on most supported OS platforms. It has already been deprecated in [RHEL 7.6 and RHEL 8](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/7.6_release_notes/chap-red_hat_enterprise_linux-7.6_release_notes-other_deprecated_functionality#:%7E:text=The%20lvmetad%20daemon%20has%20been%20deprecated&text=In%20a%20future%20major%20release,conf%20configuration%20file.): The use of lvm2-lvmetad is deprecated and not supported and the attribute use_lvmetad no longer exists in /etc/lvm/lvm.conf and the the systemd service lvm2-lvmetad no longer exists.

## March 17, 2023

Issue

If you are in a region where Hyperdisk Extreme is available, then a mount _as a new_ Compute Engine instance may fail unless you change the boot disk disktype away from Hyperdisk Extreme. This is because images cannot be created using Hyperdisk Extreme disks. In addition, the target instance requires 64 CPUs or more and each disk being created must be 64 GB or larger.

Issue

If you are in a region where Hyperdisk Extreme is available, then a mount to an _existing_ Compute Engine instance may fail unless you change the disktype away from Hyperdisk Extreme. This is because the target instance requires 64 CPUs or more and the disk being created needs to be 64 GB or larger.

## March 06, 2023

Feature

Backup and DR Service now supports logging and alerting via [Cloud Logging](https://docs.cloud.google.com/logging) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring). It:

  * Supports centralized logging of backup events. 
  * Enables users to [view backup events](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/appliance-events) in Cloud Logging with custom filters.
  * Enables users to [configure alerts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configure-alerts) for backup events via email, SMS, Slack, PagerDuty, and more – all within Cloud Monitoring.



## February 21, 2023

Announcement

Google Cloud Backup and DR is now available under Google Cloud terms of service.

## January 31, 2023

Announcement

Backup and DR release 11.0.3.534 is now available. This release includes bug fixes and supportability improvements.

Feature

Adds project cleanup guidance where Backup and DR components are deleted or disabled.

Feature

Improves metrics reporting for ongoing management console and backup/recovery appliance supportability.

Fixed

Fixed issue where backup/recovery appliance deployment would fail in some limited circumstances

## January 03, 2023

Announcement

Backup and DR release 11.0.2.9632 is now available. This release:

  * Improves the ease of use for Compute Engine instances by eliminating creation of service account, cloud credentials, cloud storage bucket, and OnVault pool.
  * Addresses security concerns by removing the need to export private keys.
  * Supports restoring Compute Engine instances to its appropriate sole-tenant node.



## September 30, 2022

Announcement

Backup and DR is now generally available.

## September 09, 2022

Announcement

Announcing Google Cloud Backup and DR Service, a managed backup and disaster recovery (DR) service for centralized, application-consistent data protection. Protect workloads running in Google Cloud and on-premises by backing them up to Google Cloud.

Coming late September, 2022.

## June 01, 2022

Announcement

Backup and DR is now in Private Preview. For information about how to use Backup and DR, see the [product documentation](https://docs.cloud.google.com/backup-disaster-recovery/docs/how-to).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
