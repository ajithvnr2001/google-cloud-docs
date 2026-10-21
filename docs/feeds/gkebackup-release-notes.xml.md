---
url: https://docs.cloud.google.com/feeds/gkebackup-release-notes.xml
title: Backup for GKE - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:12:01.755501+00:00
---

# Backup for GKE - Release notes

> Source: https://docs.cloud.google.com/feeds/gkebackup-release-notes.xml

tag:google.com,2016:gkebackup-release-notesBackup for GKE - Release notesGoogle Cloud Platform2026-10-12T00:00:00-07:00October 12, 2026tag:google.com,2016:gkebackup-release-notes#October_12_20262026-10-12T00:00:00-07:00Change 

Backup for GKE is now available in the following region: `asia-southeast3` (Bangkok, Thailand). For more information, see [Backup for GKE locations](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-locations).

]]> September 16, 2025tag:google.com,2016:gkebackup-release-notes#September_16_20252025-09-16T00:00:00-07:00Feature 

Backup for GKE now supports restoring disks in pre-existing Storage Pools for Hyperdisk Balanced and Hyperdisk Throughput volumes. This feature is available in clusters running the following GKE versions:

  * 1.33: Versions `1.33.4-gke.1245000` and later
  * 1.34 and later: All versions from `1.34.0-gke.1532000` onwards

]]> August 25, 2025tag:google.com,2016:gkebackup-release-notes#August_25_20252025-08-25T00:00:00-07:00Feature 

Backup for GKE cross-project backup and restore is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). You can back up workloads from a GKE cluster in one Google Cloud project, securely store those backups in a second project, and restore them to a cluster in a third project.

For more information, see:

  * [Perform cross-project backups](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/cross-project-backups) \
  * [Perform cross-project restores](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/cross-project-restores)

]]> August 20, 2025tag:google.com,2016:gkebackup-release-notes#August_20_20252025-08-20T00:00:00-07:00Feature 

You can use custom constraints with Organization Policy to provide more granular control over specific fields for some Backup for GKE resources. For more information, see [Manage Backup for GKE resources using custom constraints](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/create-custom-constraints). This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

]]> July 01, 2025tag:google.com,2016:gkebackup-release-notes#July_01_20252025-07-01T00:00:00-07:00Announcement 

Backup for GKE now supports backing up and restoring Hyperdisk ML and Hyperdisk Balanced High Availability volumes. This feature is available for GKE clusters running version 1.33.1-gke.1959000 and later.

]]> May 22, 2025tag:google.com,2016:gkebackup-release-notes#May_22_20252025-05-22T00:00:00-07:00Change 

Backup for GKE is now available in two new regions: europe-north2 and northamerica-south1

]]> November 15, 2024tag:google.com,2016:gkebackup-release-notes#November_15_20242024-11-15T00:00:00-08:00Announcement 

Backup for GKE now supports backing up and restoring Hyperdisk throughput, extreme, and balanced types volumes.

]]> July 29, 2024tag:google.com,2016:gkebackup-release-notes#July_29_20242024-07-29T00:00:00-07:00Feature 

Backup for GKE now offers committed use discounts (CUDs) that provide 20% discount (one year term) and 45% discount (3 year term) on backup management fee in exchange for your commitment. For more information, see [Backup for GKE Committed use discounts](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/cud).

]]> June 27, 2024tag:google.com,2016:gkebackup-release-notes#June_27_20242024-06-27T00:00:00-07:00Feature 

Backup for GKE now supports creating a backup plan when creating a cluster.

]]> June 03, 2024tag:google.com,2016:gkebackup-release-notes#June_03_20242024-06-03T00:00:00-07:00Feature 

Backup for GKE now supports specifying the restore order when you create or update a restore plan. For more information, see [Specify resource restore ordering during restoration](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-order).

### Feature

Backup for GKE now allows configuration of volume data restore policies bound to specific volume types and overridden for specific volumes. This gives you more flexibility when restoring volumes. For more information, see [Define volume data restore behavior](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/volume-data-restore-policy).

### Feature

Starting June 24, 2024, Backup for GKE will gradually roll out the Backup-Side Restore Validation feature to help ensure that backups are restorable. This change applies to backups under backup plans created from June 24, 2024 onwards. For more information, see [Enable permissive mode on a backup plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permissive-mode).

### Feature

Backup for GKE introduces new policies for handling namespaced resources conflict during restoration that are compatible with GitOps tools. For more information, see [Handle resource conflicts during restore](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/resource-conflict).

### Feature

Backup for GKE now provides enhanced granularity in resource selection during the restore creation process. For more information, see [Enable fine-grained restore](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/fine-grained-restore).

]]> April 22, 2024tag:google.com,2016:gkebackup-release-notes#April_22_20242024-04-22T00:00:00-07:00Feature 

Backup index is now available for viewing the resource information in backups. See details on [view backup index](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup#view_backup_index).

### Feature

Backup for GKE now supports Smart Scheduling, an alternative backup creation scheduling approach based on desired RPO instead of a fixed schedule. This approach is in addition to the existing cron scheduling approach. For more information, see [Automatic backup creation and deletion](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-schedule).

]]> March 05, 2024tag:google.com,2016:gkebackup-release-notes#March_05_20242024-03-05T00:00:00-08:00Change 

Backup for GKE is now available in three new regions: africa-south1, europe-west10, and us-west8.

]]> October 31, 2023tag:google.com,2016:gkebackup-release-notes#October_31_20232023-10-31T00:00:00-07:00Feature 

Terraform now supports managing Backup for GKE RestorePlan resources. For more information, see [google_gke_backup_restore_plan](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_backup_restore_plan).

### Feature

Backup for GKE now supports transformation rules that allow for the modification of resources during restore. This is an improvement over the existing substitution rules. For more information, see [Modify resources during restoration](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/transformation-rules).

]]> July 21, 2023tag:google.com,2016:gkebackup-release-notes#July_21_20232023-07-21T00:00:00-07:00Change 

Backup for GKE is now available in five new regions: europe-west12, me-west1, me-central1, us-south1, and us-east5.

]]> July 11, 2023tag:google.com,2016:gkebackup-release-notes#July_11_20232023-07-11T00:00:00-07:00Feature 

Backup for GKE now supports a blocklist for restoring cluster-scoped and namespaced resources. For more information, see [Create a restore plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan#create_a_restore_plan).

### Feature

When you create your first BackupPlan or RestorePlan resource for a cluster, the Backup for GKE agent is automatically installed in that cluster.

]]> November 16, 2022tag:google.com,2016:gkebackup-release-notes#November_16_20222022-11-16T00:00:00-08:00Announcement 

Backup for GKE is now generally available.

]]>
