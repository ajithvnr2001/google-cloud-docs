---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-pricing/
title: Backup for GKE pricing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:12:01.628845+00:00
---

# Backup for GKE pricing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-pricing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-pricing)



Send feedback 

#  Backup for GKE pricing Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

**Note:** Starting March 2nd, 2026, Backup for GKE will transition to a namespace-based pricing model for simpler, more predictable billing. [Learn more about this transition](https://cloud.google.com/products/backup-for-gke/pricing-changes).

This document describes the pricing model and cost dimensions for Backup for GKE.

Backup for GKE helps you protect your GKE clusters and their workloads. By understanding how Backup for GKE calculates costs, you can effectively manage and optimize your backup expenses.

Your costs for Backup for GKE are determined by three dimensions:

  * Backup management: calculated at the `BackupPlan` level. It's based on the number of non-system namespaces protected by your `BackupPlan`'s most recent backup.
  * Backup storage: calculated based on the number of bytes stored for each backup over time.
  * Network egress: calculated based on bytes transferred across regions during backup operations. These charges apply only when your source cluster and `BackupPlan` are in different regions.



You can find full pricing details on the [GKE pricing page](https://docs.cloud.google.com/kubernetes-engine/pricing#backup-for-gke).

## Pricing for cross-project backups and restores

For any cross-project backup and restore scenarios, three projects are potentially involved:

  * **`cluster_project`** : the project that contains the cluster that you want to back up.

  * **`backup_project`** : the project where you want your backups to be stored.

  * **`restore_project`** : the project that contains the restore's target cluster.




All three dimensions are billed in the `backup_project` under the Backup for GKE line item.

### Network data transfer charges

Similar to single-project backup and restore operations, network data transfer charges apply for cross-region backup and restore operations. Additionally, there are network data transfer changes for `Config backup` during backup operations, between backup regions, and between restore regions when restoring a volume. These charges are listed under Compute Engine.

## Adjust future billing

To stop any future billing for Backup for GKE, delete any existing `Backup` resources and then delete or disable any `BackupPlans`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
