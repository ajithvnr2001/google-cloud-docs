---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/manual-restore-overview/
title: Manual restore overview \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:36.444028+00:00
---

# Manual restore overview  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/manual-restore-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Manual restore overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the manual restore creation options in Google Distributed Cloud (GDC) air-gapped.

Create a manual restore of a backup to recover your data at any time.

When a backup is restored, the Kubernetes resources are recreated in the target cluster. After the resources are created, actual restoration of workload functionality is subject to the regular cluster reconciliation process. For example, pods are scheduled to nodes and then started on those nodes.

## Restore from an imported backup

You can restore a backup from another backup that was completed in a different cluster. For example, restore a backup from an imported backup if the original cluster is inactive or you want to clone an existing cluster.

First, create a backup repository in the target cluster that points to the storage location used by the source cluster. If the repository is actively being used by the source cluster in `ReadWrite` mode, you must specify the `ImportPolicy` as `ReadOnly`. For more information, see [Backup repository import policies](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/add-backup-repository#backup-repo-import-policies).

After creating the backup repository and successfully importing the backups, the repository backup resources are present in the target cluster. You can then schedule a restore in the target cluster by referencing an imported backup.

## Manual restore overview

To create a manual restore, you must have an existing backup to restore. Create a manual restore in the GDC console or using the API. The API lets you request data restoration from a backup by creating a `ManualRestoreRequest` resource. This resource specifies the name of the restore, the restore plan to use, and the backup to restore from.

The restore plan and backup must exist in the same namespace as the request. The API provides status updates on the restore process and lets you list all restore requests. For more information, see [Create a restore](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/restore-backup#create-a-restore).

If you want more control over the resources that are restored, see Fine-grained restore overview.

## Fine-grained restore overview

The fine-grained restore feature lets you restore a subset of resources from a backup. This feature provides the flexibility to refine the restore scope defined in the restore plan. If the fine-grained restore scope has no overlap with the original scope defined in the restore plan, no resources are restored.

You can enable the fine-grained restore feature for restore plans with these individual resource level conflict handling modes:

  * `MergeSkipOnConflict`: conflicting resources that are encountered during the restore are skipped.
  * `MergeReplaceOnConflict`: conflicting resources that are encountered during the restore process are replaced by the resources in the backup you are restoring.



To use fine-grained restores, create a restore plan or update the `namespacedResourceRestoreMode` field of an existing restore plan to a value of `MergeSkipOnConflict` or `MergeReplaceOnConflict`. The namespace conflict handling modes of `FailOnConflict` or `DeleteAndRestore` are not supported. For more information about the restore modes, see the `namespacedResourceRestoreMode` field in [Create a restore plan](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/plan-restores#create-restore-plan).

### Inclusion and exclusion filters

When you create a fine-grained restore, you define one or more filter conditions under the inclusion and exclusion filters. These filters let you select or exclude a subset of resources from the backup for restoration. You can define inclusion and exclusion filters simultaneously. When both are specified, the following order is followed:

  * If inclusion filters are used, the restore only includes resources matching those filters.
  * If exclusion filters are used, the restore excludes matching resources from the restore process.
  * When both inclusion and exclusion filters are specified, the restore applies inclusion filters first, followed by exclusion filters.
  * If no filters are specified, the restore is performed on the entire scope defined in the parent restore plan.



You can include four optional attributes when constructing a filter condition:

  * `GroupKind`: the Kubernetes API group and kind for the resource.
  * `Namespace`: the namespace for namespace scoped resources.
  * `Name`: the name of the resource.
  * `Labels`: the key-value pairs to select resources based on Kubernetes. For more information on labels, see <https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/>.



You can use a combination of the preceding four attributes to define a filter condition. If more than one attribute is specified, the relationship between attributes is considered as `AND`. A resource is selected if it matches all attributes defined in the filter condition.

You can also provide multiple filter conditions at the same time. The relationship between the different filter conditions is `OR`. A resource is selected if it matches any filter condition. A maximum of 50 filters are allowed, and each filter can have 50 label key-value pairs.

## What's next

  * [Create a restore](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/restore-backup)
  * [Create a fine-grained restore](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/fine-grained-restore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
