---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/plan-restores/
title: Plan a set of restores \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:23.730538+00:00
---

# Plan a set of restores  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/plan-restores/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Plan a set of restores Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create, edit, and delete a restore plan in Google Distributed Cloud (GDC) air-gapped.

Restore plans are pre-configured restore scenarios for a corresponding line of backups. Restore plans can assign permissions for users with the Backup Creator role to use these configurations.

Backup Creators can quickly and independently restore a backup when an incident occurs. For example, persistent data might be corrupted by a software update in a deployed application, putting the application namespace in an invalid state, which requires a restore.

During restoration, you can optionally apply a set of _substitution_ rules which are used to match a set of resources and substitute the current value of an attribute on those resources for a new value. For example, a substitution rule can change the namespace of the backed up resources during the restore to migrate a workload from one namespace to another.

## Before you begin

### Request IAM roles

To create a restore plan, ask your Organization IAM Admin to grant you the **User Cluster Backup Admin** (`user-cluster-backup-admin`) role. This role creates, gets, lists, watches, updates, patches, and deletes backup resources such as backup plans and restore plans in user clusters.

If you are an Application Operator, ask an administrator with User Cluster Backup Admin privileges to create a restore plan for you.

**Warning:** Due to a known issue when creating restore plans using the GDC console or the API, don't use the **All namespaced resources** option or the `allNamespaces` API field. Instead, use the **Selected namespaced resources** option or the `selectedNamespaces` API field to restore user namespaces.

## Create a restore plan

Create a restore plan using the GDC console or the API.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for Clusters**.
  3. Click **Create Restore Plan**.
  4. In the **Restore plan basics** section, complete the following steps and click **Next** : 
     1. In **Restore plan name** , enter the name of your restore plan.
     2. (Optional) In **Restore plan description** enter a description for the restore plan.
     3. In the **Source cluster** list, choose the source cluster for the restore plan.
     4. In the **Project** list, choose the project for the restore plan.
     5. Select the project which is attached to source cluster.
     6. In the **Backup plan** field, choose a backup plan for an existing cluster that corresponds to the backups that you want to restore.
     7. In the **Target cluster** field, choose the target cluster where you want to restore the backup.
  5. In the **Choose namespaced resources** section, complete the following steps and click **Next** : 
     1. Choose what namespaces to restore: 
        1. Click **Selected namespaced resources** to specify the namespaces in the backup to restore. 
           1. Click **Edit cluster namespaces** and then **Add cluster namespace** to enter a namespace.
        2. Click **Selected protected applications** to add resources by specifying the namespace and application name.
     2. Choose how to handle conflicts: 
        1. Click **Fail on conflict (non-destructive)** to fail the restore if any namespaces targeted for restore from a backup already exist in the target cluster.
        2. Click **Rollback (destructive)** to delete the existing namespaces before restoring the new namespaces if any namespaces targeted for restore from a backup already exist in the target cluster.
     3. Choose how to restore volume data: 
        1. Click **Provision new volumes and restore volume data from backup** to restore volume data from the backup on a new persistent disk.
        2. Click **Don't restore volume data** to provision a new persistent volume. If the target cluster contains an unbound persistent volume that satisfies the `PersistentVolumeClaim` requirements, the cluster is bound to the volume.
        3. Click **Reuse existing volumes containing your data** to not restore volume backup data. Any `PersistentVolumeClaims` are bound to volumes that reference existing persistent disks.
  6. Optional: In the **Choose cluster-scoped resources** section, complete the following steps and click **Next** : 
     1. Click **Don't restore cluster-scoped resources** to leave the existing version of the resource untouched.
     2. Click **Restore cluster-scoped resources** by GroupKind to restore these resources. 
        1. Click **Edit GroupKinds** to add more cluster-scoped resources. Enter the **API group** and **Object kind** to match resources within those types.
     3. Click **Preserve existing resources** to create resources if they don't exist on the target cluster.
     4. Click **Overwrite resources in target cluster** to delete a resource if it already exists in the target cluster, and restore the copy from the backup.
  7. Optional: In the **Add substitution rules** section, complete the following steps and click **Next** : 
     1. Click **Add new rule**.
     2. In the **Cluster namespaces** box, type a list of namespaces to match resources within those namespaces.
     3. To add GroupKinds, click **Add GroupKind** and enter the **API group** and **Object kind** to match resources within those types.
     4. In the **JSON path** field, type the JSON path that identifies the fields within the matched resources for which the substitution applies.
     5. In the **Original value pattern** field, type the original pattern to compare against the new value.
     6. In the **New value** field, type the new value that replaces the current value of the matched attributes.
     7. Click **Save**.
  8. Click **Create**.



### API

Create a `ClusterRestorePlan` custom resource to plan restores from an existing `ClusterBackupPlan`. The `ClusterRestorePlan` assigns the exact set of resources and namespaces that a Backup Creator is permitted to restore. Here's an example of a `ClusterRestorePlan`:
    
    
    apiVersion: backup.gdc.goog/v1
    kind: ClusterRestorePlan
    metadata:
      name: RESTORE_PLAN_NAME
      namespace:  PROJECT_NAME
    spec:
      targetCluster:
        targetClusterType: UserCluster
        targetClusterName:
          kind: "Cluster"
          name: CLUSTER_NAME
      description: RESTORE_PLAN_DESCRIPTION
      clusterBackupPlanName: CLUSTER_BACKUP_PLAN_NAME
      clusterRestoreConfig:
        volumeDataRestorePolicy: RestoreVolumeDataFromBackup
        clusterResourceConflictPolicy: UseBackupVersion
        namespacedResourceRestoreMode: DeleteAndRestore
        namespacedResourceRestoreScope:
          selectedNamespaces:
            namespaces: [NAME_SPACE]
        clusterBackupRepositoryRef: CLUSTER_BACKUP_REPOSITORY
        substitutionRules:
          - newValue: NEW_CONFIG_VALUE
            originValuePattern: VALUE_PATTERN
            target:
              groupKinds:
              jsonPath: '{.metadata.name}'
              namespaces:
              - NAME_SPACE
          - newValue: NEW_CONFIG_VALUE
            originValuePattern: VALUE_PATTERN
            target:
              groupKinds:
              jsonPath: '{.metadata.name}'
              namespaces:
              - NAME_SPACE
    

Replace the following:

  * Replace `RESTORE_PLAN_NAME` with the name of your restore plan.
  * Replace `PROJECT_NAME` with the name of your GDC project.
  * Replace `CLUSTER_NAME` with the name of your cluster.



This example uses the following values:

  
**Value** |   
**Attribute** |   
**Description**  
---|---|---  
`targetClusterName` |  | Name of the source cluster in a project which this plan is associated with.  
`description` |  | A user-provided description for the purpose of the `ClusterRestorePlan`.  
`clusterBackupPlanName` |  | The name of the `ClusterBackupPlan` to restore. The `ClusterBackupPlan` must exist in the same namespace as the `ClusterRestorePlan`.  
`clusterRestoreConfig` |  | Configuration for the restore process.  
| `volumeDataRestorePolicy` | Specify one of: 

  * `NoVolumeDataRestoration`: PV/PVCs are not restored.


  * `RestoreVolumeDataFromBackup`: New PVs and PVCs are created from the backup.


  * `ReuseVolumeHandleFromBackup`: Does create new PVs, but attempts to restore PVCs using their original PVs. Intended for restoring to the same cluster that the backup was taken from.

  
| `clusterResourceConflictPolicy` | Specifies behavior for handling cluster resource conflicts, such as if the resource already exists in the cluster. Specify one of: 

  * `UseExistingVersion`: Does not overwrite existing resources during conflict


  * `UseBackupVersion`: Deletes and recreates existing cluster resources during conflict. Existing cluster-scoped resources in the target cluster will be overwritten by the versions from the backup. This is a dangerous option which can cause unintended data loss if used inappropriately. For example, deleting a custom resource definition causes Kubernetes to delete all custom resources of that type.

  
| `namespacedResourceRestoreMode` | Handles the situation where the sets of namespaced resources being restored already exist in the target cluster. Specify one of: 

  * `DeleteAndRestore`: When conflicting top-level resources such as the `Namespaces` or `ProtectedApplications` are encountered, this first triggers a deletion of the conflicting resource and all of its referenced resources before restoring the resources from the `Backup`. Use this mode only when you intend to revert some portion of a cluster to an earlier state.


  * `FailOnConflict`: If conflicting top-level resources such as the `Namespace` or `ProtectedApplication` resource are encountered at the beginning of the restore process or during the restore process, the `Restore` fails.


  * `MergeSkipOnConflict`: If conflicting resources are encountered during the restore process, this mode skips restoring the conflicting resources from the backup and continues restoring other resources which are not in the cluster.


  * `MergeReplaceOnConflict`: If conflicting resources are encountered during the restore process, this mode replaces the conflicting resources from the backup and continues restoring other resources which are not in the cluster.

  
| `namespacedResourceRestoreScope` | Specifies which `Namespaces` or `ProtectedApplications` are permitted for restoration. 

  * `selectedApplications` associates protected applications with this restore.


  * `selectedNamespaces` contains `NAME_SPACE` which specifies the namespace to restore from backup.

  
| `clusterBackupRepositoryRef` | Specifies the repository to store the `Restore` resources. This repository can be different from the repository that the backup is from. The repository must be a `ReadWrite` repository in the cluster.  
| `substitutionRules` | Rules to substitute values in the backed-up Kubernetes resources during restore. An empty list means no substitution occurs. Substitution rules are applied sequentially in the order defined. This order is important, as changes made by a rule might impact the matching logic of the subsequent rule. Each rule specifies a `target`, an `originValuePattern` to match (`VALUE_PATTERN`), and a `newValue` (`NEW_CONFIG_VALUE`) to replace with. The `target` can include `namespaces` to scope the rule (`NAME_SPACE`).  
  
After a `ClusterRestorePlan` is created, users with the Backup Creator role can manually restore backups.

## View a restore plan

View a restore plan using the GDC console:

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for Clusters**.
  3. Click **Select project** to select an organization or project depending on your role: 
     1. User Cluster Backup Admin: Select an organization to see all restore plans in an organization or select a project to see all restore plans in a project.
     2. Backup Creator: Select a project to see all restore plans in a project.
  4. Click the **Restore Plans** tab.
  5. Click a restore plan in the list to view its details.



## Edit a restore plan

If the backup repository associated with the restore plan you want to edit has a value in the **Linked Cluster(read-only)** field when the restore plan is created, it is created twice. The restore plan is propagated to both the read-write and read-only clusters.

When you edit the restore plan owned by a backup repository that has both read-write and read-only clusters set, you must edit the restore plan that has the `TARGET CLUSTER` set to the read-write cluster.

**Warning:** If you edit a restore plan with the `TARGET CLUSTER` set to read-only cluster, it results in an error.

Edit a restore plan using the GDC console:

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for Clusters**.
  3. Click **Select project** to select an organization or project depending on your role: 
     1. User Cluster Backup Admin: Select an organization to see all restore plans in an organization or select a project to see all restore plans in a project.
     2. Backup Creator: Select a project to see all restore plans in a project.
  4. Click the **Restore Plans** tab.
  5. Click the name of the restore plan you want to edit.
  6. Click the **Plan Configuration** tab to view the fields that can be modified.
  7. Click the _edit_ Edit icon next to **Namespaced resources** to edit that resource:

     1. In the **Choose namespaced resources** section, select which namespaced resources in the backup that you want to restore:

        1. Select **Selected namespaced resources** to restore resources from the selected namespaces in the backup:

           1. Select **Edit Cluster Namespaces** to select the cluster namespace.
           2. In the **Cluster namespace 1** field, enter the name for the namespace.
           3. Click the **Save** button.
        2. Select **Selected protected applications** to restore resources from the selected protected applications in the backup:

           1. Select **Edit Protected Applications** to select the namespace and protected application.
           2. In the **Namespace 1** field, enter the name for the namespace.
           3. In the **Protected application 1** field, enter the name of the protected application.
           4. Click the **Save** button.
  8. Click the _edit_ Edit icon next to **Cluster-scoped resources** to edit that resource:

     1. Optional: In the **Choose cluster-scoped resources** section, select the cluster-scoped resources to restore by specifying the API groups and `GroupKinds`, and decide how the conflicts must be resolved:

        1. Select **Don't restore cluster-scoped resources** to remove cluster-scoped resources from the restore process.
        2. Select **Restore cluster-scoped resources by GroupKind** to restore the resources by the specified `GroupKind`:

        3. To specify a `GroupKind`, click the **Edit GroupKind** button.

        4. Click the **Add GroupKind** button.

        5. Enter the name of the `GroupKind`.

        6. Click the **Save** button.

     2. In the **Conflict handling** section, determine what action to take if the resource already exists in the target cluster:

        1. Select **Preserve existing resources** to create resources if they don't already exist on the cluster.
        2. Select **Overwrite existing resources** to delete any existing resources found, and replace this resource with the restored resource.
     3. Click the **Save** button to confirm your changes.

  9. In the **Substitution rules** section, click the **Add New Rule** button to add a new substitution rule:

     1. In the **Cluster namespaces** field, enter the name of the cluster namespace for which to apply this substitution rule.
     2. Click the **Add GroupKind** button to apply this rule to a certain `GroupKind` object.
     3. In the **JSON path** field, enter the path to the resource attribute that you want to substitute, in JSON format.
     4. In the **Original value pattern** field, enter a regular expression that matches the original value of the attribute.
     5. In the **New value** field, enter the value that is substituted for the target field. If this field is blank, the target field is removed from the resource.
     6. Click the **Save button** to complete the creation of the new substitution rule.
  10. In the **Substitution rules** section, click the _edit_ Edit icon to edit an existing substitution rule.

  11. In the **Substitution rules** section, click the _delete_ Delete icon to delete an existing substitution rule.




## Delete a restore plan

`RestorePlans` can be deleted through GDC console or by deleting the resource directly from the Kubernetes API server. This cleans up any associated `RestorePlan` artifacts from the object storage.

### Console

  1. Sign in to the GDC console.
  2. In the navigation menu, click **Backup for Clusters**.
  3. Click **Select project** to select an organization or project depending on your role: 
     1. User Cluster Backup Admin: Select an organization to see all of the restore plans in an organization, or select a project to see all of the restore plans in a project.
     2. Backup Creator: Select a project to see all of the restore plans in a project.
  4. Click the **Restore Plans** tab.
  5. Click the name of the restore plan that you want to delete.
  6. Click the _delete_ **Delete** button.
  7. Enter the name of the restore plan into the field.
  8. Click the **Delete** button to confirm the deletion of this restore plan.



### API

Delete the restore plan resource:
    
    
    kubectl delete clusterRestoreplan RESTORE_PLAN_NAME -n NAMESPACE
    

Replace the following:

  * `RESTORE_PLAN_NAME`: the name of the restore plan.
  * `NAMESPACE`: the namespace that contains the restore plan.



## What's next

  * [Manual restore overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/manual-restore-overview)
  * [View and delete a restore](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/cluster-backup/view-and-delete-restore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
