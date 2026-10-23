---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/docs/release-notes/
title: Backup for GKE release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:06.895821+00:00
---

# Backup for GKE release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-pricing)



Send feedback 

#  Backup for GKE release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Backup for GKE. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/gkebackup-release-notes.xml) directly. 

## October 12, 2026

Change

Backup for GKE is now available in the following region: `asia-southeast3` (Bangkok, Thailand). For more information, see [Backup for GKE locations](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-locations).

## September 16, 2025

Feature

Backup for GKE now supports restoring disks in pre-existing Storage Pools for Hyperdisk Balanced and Hyperdisk Throughput volumes. This feature is available in clusters running the following GKE versions:

  * 1.33: Versions `1.33.4-gke.1245000` and later
  * 1.34 and later: All versions from `1.34.0-gke.1532000` onwards



## August 25, 2025

Feature

Backup for GKE cross-project backup and restore is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). You can back up workloads from a GKE cluster in one Google Cloud project, securely store those backups in a second project, and restore them to a cluster in a third project.

For more information, see:

  * [Perform cross-project backups](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/cross-project-backups) \
  * [Perform cross-project restores](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/cross-project-restores)



## August 20, 2025

Feature

You can use custom constraints with Organization Policy to provide more granular control over specific fields for some Backup for GKE resources. For more information, see [Manage Backup for GKE resources using custom constraints](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/create-custom-constraints). This feature is generally available ([GA](https://cloud.google.com/products#product-launch-stages)).

## July 01, 2025

Announcement

Backup for GKE now supports backing up and restoring Hyperdisk ML and Hyperdisk Balanced High Availability volumes. This feature is available for GKE clusters running version 1.33.1-gke.1959000 and later.

## May 22, 2025

Change

Backup for GKE is now available in two new regions: europe-north2 and northamerica-south1

## November 15, 2024

Announcement

Backup for GKE now supports backing up and restoring Hyperdisk throughput, extreme, and balanced types volumes.

## July 29, 2024

Feature

Backup for GKE now offers committed use discounts (CUDs) that provide 20% discount (one year term) and 45% discount (3 year term) on backup management fee in exchange for your commitment. For more information, see [Backup for GKE Committed use discounts](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/cud).

## June 27, 2024

Feature

Backup for GKE now supports creating a backup plan when creating a cluster.

## June 03, 2024

Feature

Backup for GKE now supports specifying the restore order when you create or update a restore plan. For more information, see [Specify resource restore ordering during restoration](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-order).

Feature

Backup for GKE now allows configuration of volume data restore policies bound to specific volume types and overridden for specific volumes. This gives you more flexibility when restoring volumes. For more information, see [Define volume data restore behavior](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/volume-data-restore-policy).

Feature

Starting June 24, 2024, Backup for GKE will gradually roll out the Backup-Side Restore Validation feature to help ensure that backups are restorable. This change applies to backups under backup plans created from June 24, 2024 onwards. For more information, see [Enable permissive mode on a backup plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permissive-mode).

Feature

Backup for GKE introduces new policies for handling namespaced resources conflict during restoration that are compatible with GitOps tools. For more information, see [Handle resource conflicts during restore](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/resource-conflict).

Feature

Backup for GKE now provides enhanced granularity in resource selection during the restore creation process. For more information, see [Enable fine-grained restore](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/fine-grained-restore).

## April 22, 2024

Feature

Backup index is now available for viewing the resource information in backups. See details on [view backup index](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup#view_backup_index).

Feature

Backup for GKE now supports Smart Scheduling, an alternative backup creation scheduling approach based on desired RPO instead of a fixed schedule. This approach is in addition to the existing cron scheduling approach. For more information, see [Automatic backup creation and deletion](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-schedule).

## March 05, 2024

Change

Backup for GKE is now available in three new regions: africa-south1, europe-west10, and us-west8.

## October 31, 2023

Feature

Terraform now supports managing Backup for GKE RestorePlan resources. For more information, see [google_gke_backup_restore_plan](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_backup_restore_plan).

Feature

Backup for GKE now supports transformation rules that allow for the modification of resources during restore. This is an improvement over the existing substitution rules. For more information, see [Modify resources during restoration](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/transformation-rules).

## July 21, 2023

Change

Backup for GKE is now available in five new regions: europe-west12, me-west1, me-central1, us-south1, and us-east5.

## July 11, 2023

Feature

Backup for GKE now supports a blocklist for restoring cluster-scoped and namespaced resources. For more information, see [Create a restore plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan#create_a_restore_plan).

Feature

When you create your first BackupPlan or RestorePlan resource for a cluster, the Backup for GKE agent is automatically installed in that cluster.

## November 16, 2022

Announcement

Backup for GKE is now generally available.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
