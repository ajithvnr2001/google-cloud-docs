---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan/
title: Plan a set of restores \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:27.176412+00:00
---

# Plan a set of restores  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Plan a set of restores Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes how to create a Backup for GKE restore plan, which is used for restoring your backups in Google Kubernetes Engine (GKE).

Restore plans are pre-configured restore scenarios for a corresponding line of backups. Restore plans can assign permissions for administrators to use these configurations. Those users can quickly and independently restore a backup when an incident occurs. For example, persistent data might be corrupted by a software update in a deployed application, putting the application namespace in an invalid state, which requires a restore.

Backup for GKE doesn't support restoring a backup from one project to another. You can only restore backups to clusters within the same project that the backup originated from. Restore plans cannot reference backup plans in a different project.

During restoration, you can optionally apply transformation rules, which are used to match a set of resources and substitute the current value of an attribute on those resources for a new value.

**Note:** Restoration is subject to a maximum GKE version difference constraint. Specifically, the target cluster version must be between the backup cluster version and the backup cluster version + 3 minor versions, inclusive. For example, a backup that was produced from a cluster running GKE 1.28 can only be restored to a cluster running 1.28 through 1.31.

## Managed namespaces

Backup for GKE does not restore into managed namespaces. These namespaces are silently skipped during restore. The list of managed namespaces include the following:

  * `cnrm-system`
  * `configconnector-operator-system`
  * `gatekeeper-system`
  * `gke-connect`
  * `gke-gmp-system`
  * `gmp-public`
  * `kube-node-lease`
  * `kube-public`
  * `kube-system`
  * Namespaces with the following label: 
    * Key: `addonmanager.kubernetes.io/mode`
    * Value: `Reconcile` or `EnsureExists`



## Before you begin

[Plan a set of backups](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan).

## Required roles

To get the permissions that you need to create and manage a restore plan, ask your administrator to grant you the Backup for GKE Restore Admin (`roles/gkebackup.restoreAdmin`), which is a subset of Backup for GKE Admin (`roles/gkebackup.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a restore plan

You can create a restore plan for your backups by using the Google Cloud CLI or the Google Cloud console.

**Note:** This will automatically install the Backup for GKE [agent](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke#architecture) in the specified cluster.

### gcloud

To create a restore plan, run the following command:
    
    
    gcloud beta container backup-restore restore-plans create RESTORE_PLAN \
        --project=PROJECT_ID \
        --location=RESTORE_LOCATION \
        --backup-plan=projects/PROJECT_ID/locations/BACKUP_LOCATION/backupPlans/BACKUP_PLAN_NAME \
        --cluster=CLUSTER \
        --namespaced-resource-restore-mode=NAMESPACED_RESOURCE_RESTORE_MODE \
        --all-namespaces \
        --cluster-resource-conflict-policy=CLUSTER_RESOURCE_CONFLICT_POLICY \
        --cluster-resource-scope-selected-group-kinds=CLUSTER_RESOURCE_SCOPE \
        --volume-data-restore-policy=VOLUME_DATA_RESTORE_POLICY
    

Replace the following:

  * `RESTORE_PLAN`: the name of the restore plan that you want to create.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `RESTORE_LOCATION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the resource, for example `us-central1`. See [About resource locations](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-locations). The location must be the same region where the target cluster is located.
  * `BACKUP_PLAN`: the source of backups that can be restored with this restore plan: 
    * `projects/PROJECT_ID/locations/BACKUP_LOCATION/backupPlans/BACKUP_PLAN_NAME` Ensure that the backup plan is in the same project as the new restore plan.
  * `CLUSTER`: the name of the target cluster to which you want to restore the backup:

    * Regional clusters: `projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_NAME`
    * Zonal clusters: `projects/PROJECT_ID/locations/ZONE/clusters/CLUSTER_NAME`
  * `NAMESPACED_RESOURCE_RESTORE_MODE`: defines how to handle restore-time conflicts for namespaced resources. Namespaced resources are always restored in groups, either by namespace or by [ProtectedApplication](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/protected-application). Use one of these options:

    * `merge-skip-on-conflict`: skip the individual conflicting resources.
    * `merge-replace-volume-on-conflict`: skip the individual conflicting resources but replace the underlying persistent volume data.
    * `merge-replace-on-conflict`: replace the individual conflicting resources and underlying persistent volume data.
    * `delete-and-restore`: When the target cluster contains the same group of resources that are targeted for restore to the cluster, the existing group of resources is deleted before the new resources are restored.
    * `fail-on-conflict`: If any groups of resources targeted for restore from a backup already exist in the target cluster, the restore will fail.
  * `--all-namespaces`: restores all namespaced resources in the backup. Alternatively, specify:

    * `--excluded-namespaces` with a list of namespaces as `NAMESPACE1,NAMESPACE2,...` to restore all namespaces except the ones in the list.
    * `--selected-applications` with a list of [ProtectedApplications](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/protected-application) as `NAMESPACE1/APP1,NAMESPACE2/APP2,...` to restore.
    * `--selected-namespaces` with a list of namespaces as `NAMESPACE1,NAMESPACE2,...` to restore.
    * `--no-namespaces` restores no namespaced resources in the backup. This option cannot be specified together with `--cluster-resource-scope-no-group-kinds`.

You must specify one of these options when creating a restore plan.


**Caution:** Backup for GKE does not restore resources into managed namespaces. These namespaces are silently skipped during a restore process. Listing them explicitly results in an error.

  * `CLUSTER_RESOURCE_CONFLICT_POLICY`: defines how to handle restore-time conflicts for selected cluster resources. Use one of these options:

    * `use-existing-version`: If the resources that are being restored already exist in the target cluster, Backup for GKE keeps the existing resources.

    * `use-backup-version`: If the resources that are being restored already exist in the target cluster, Backup for GKE replaces the existing resources with the new resources from the backup.

**Warning:** this is a dangerous option which could cause unintentional data loss if used inappropriately. For example, deleting a CRD will cause Kubernetes to delete all CRs of that type.
  * `--cluster-resource-scope-selected-group-kinds`: (Optional) restores cluster resources with selected group kinds in the format `Group/Kind`. `CLUSTER_RESOURCE_SCOPE` defines GroupKinds of cluster resources to be restored. For example, `apiextension.k8s.io/CustomResourceDefinition,storage.k8s.io/StorageClass`.

Alternatively, specify:

    * `cluster-resource-scope-all-group-kinds` to select all cluster resource group kinds to restore.
    * `cluster-resource-scope-excluded-group-kinds` with a list of cluster resource group kinds to restore all cluster resource group kinds except those in the list.
    * `cluster-resource-scope-no-group-kinds`. This option cannot be specified together with `--no-namespaces`.

Not specifying any of these options won't restore any cluster resources.


**Caution:** Backup for GKE is not allowed to select cluster-scoped resources that are managed by GKE clusters or driven by restore configuration elsewhere. Such GroupKinds include `Namespace`, `Node`, `PersistentVolume`, `gkebackup.gke.io/BackupJob`, `gkebackup.gke.io/RestoreJob`, `metrics.k8s.io/NodeMetrics`, `migration.k8s.io/StorageState`, `migration.k8s.io/StorageVersionMigration`, `snapshot.storage.k8s.io/VolumeSnapshotContent`, `storage.k8s.io/CSINode`. Selecting `cluster-resource-scope-all-group-kinds` automatically skips these cluster-scoped resources. Listing them explicitly results in an error.

  * `VOLUME_DATA_RESTORE_POLICY`: defines how data is populated for restored volumes. Use one of these options:

    * `restore-volume-data-from-backup`: New PVs will be restored using the corresponding volume backup data in the Backup.

    * `reuse-volume-handle-from-backup`: PVs will be pre-provisioned using the volume handle of the original PV in the Backup.

    * `no-volume-data-restoration`: PVs won't be restored. The restoration only restores selected PVCs and expects the corresponding storage driver to either dynamically provision blank PVs or bind them to pre-provisioned PVs created out-of-band.




For the full list of options, refer to the [`gcloud beta container backup-restore restore-plans create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/restore-plans/create) documentation.

**Create a restore plan for all namespaces**

The following command creates a restore plan to restore all namespaces and cluster resources:
    
    
    gcloud beta container backup-restore restore-plans create RESTORE_PLAN \
        --location=LOCATION \
        --backup-plan=projects/PROJECT_ID/locations/BACKUP_LOCATION/backupPlans/BACKUP_PLAN_NAME \
        --cluster=CLUSTER \
        --namespaced-resource-restore-mode=fail-on-conflict \
        --all-namespaces \
        --cluster-resource-conflict-policy=use-existing-version \
        --cluster-resource-scope-all-group-kinds \
        --volume-data-restore-policy=restore-volume-data-from-backup
    

**Create a restore plan to roll back a namespace**

The following command creates a restore plan to roll back the namespace `my-ns` from backup:
    
    
    gcloud beta container backup-restore restore-plans create RESTORE_PLAN \
        --location=LOCATION \
        --backup-plan=projects/PROJECT_ID/locations/BACKUP_LOCATION/backupPlans/BACKUP_PLAN_NAME \
        --cluster=CLUSTER \
        --namespaced-resource-restore-mode=delete-and-restore \
        --selected-namespaces=my-ns \
        --cluster-resource-conflict-policy=use-existing-version \
        --cluster-resource-scope-selected-group-kinds=apiextension.k8s.io/CustomResourceDefinition,storage.k8s.io/StorageClass \
        --volume-data-restore-policy=restore-volume-data-from-backup
    

**Create a restore plan to roll back a`ProtectedApplication` to reconnect original volumes**

The following command creates a restore plan to roll back the protected application `my-ns/my-app` to reconnect original volumes:
    
    
    gcloud beta container backup-restore restore-plans create RESTORE_PLAN \
        --location=LOCATION \
        --backup-plan=projects/PROJECT_ID/locations/BACKUP_LOCATION/backupPlans/BACKUP_PLAN_NAME \
        --cluster=CLUSTER \
        --namespaced-resource-restore-mode=delete-and-restore \
        --selected-applications=my-ns/my-app \
        --cluster-resource-conflict-policy=use-existing-version \
        --cluster-resource-scope-no-group-kinds \
        --volume-data-restore-policy=reuse-volume-handle-from-backup
    

**Create a restore plan to restore cluster resources only**

The following command creates a restore plan to restore all cluster resources:
    
    
    gcloud beta container backup-restore restore-plans create RESTORE_PLAN \
        --location=LOCATION \
        --backup-plan=projects/PROJECT_ID/locations/BACKUP_LOCATION/backupPlans/BACKUP_PLAN_NAME \
        --cluster=CLUSTER \
        --namespaced-resource-restore-mode=fail-on-conflict \
        --no-namespaces \
        --cluster-resource-conflict-policy=use-existing-version \
        --cluster-resource-scope-all-group-kinds
    

### Console

Use the following instructions to create a restore plan in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click **Create a restore plan**.

  4. In the **Name your plan and choose a cluster** section, complete the following and click **Next** :

     1. Enter the restore plan name and optional description.
     2. Choose a backup plan for an existing cluster that corresponds to the backups that you want to restore.
     3. Choose the target cluster where you want to restore the backup.
  5. In the **Choose namespaced resources** section, complete the following and click **Next** :

     1. Choose what namespaces to restore:

        * Click **All namespaced resources** to restore all namespaced resources in the backup. 
          1. Click **Add namespaces** under the Exceptions section to exclude any namespace in the backup.
        * Click **Selected namespaced resources** to specify the namespaces in the backup to restore.
        * Click **Selected protected applications** to add resources by specifying the namespace and application name.
        * Click **No namespaced resources** to not restore any namespaced resources.
**Caution:** Backup for GKE does not restore resources into managed namespaces such as `kube-system`, `kube-public`, or `kube-node-lease`. These namespaces are silently skipped during a restore process. Listing them explicitly will result in an error.
     2. Choose how to handle conflicts if any namespaced resources are selected:

        * Click **Merge skip (non-destructive)** if a specific resource already exists, skip restoring the resource from the backup.
        * Click **Merge replace volume (destructive)** if a specific resource already exists, skip restoring that resource but replace the underlying persistent volume using the volume data restore policy. The merge replace volume achieves the data-only restore.
        * Click **Merge replace (destructive)** if a specific resource already exists, replace that resource with the one from backup and the associated volume data by following the volume data restore policy.
        * Click **Fail on conflict (non-destructive)** to fail the restore if any namespaces targeted for restore from a backup already exist in the target cluster.
        * Click **Rollback (destructive)** to delete the existing namespaces before restoring the new namespaces if any namespaces targeted for restore from a backup already exist in the target cluster.
     3. Choose how to restore volume data and click **Next** :

        * Click **Provision new volumes and restore volume data from backup** to restore volume data from the backup on a new persistent disk.
        * Click **Don't restore volume data** to provision a new persistent volume. If the target cluster contains an unbound persistent volume that satisfies the `PersistentVolumeClaim` requirements, the cluster is bound to the volume.
        * Click **Reuse existing volumes containing your data** to not restore volume backup data. Any `PersistentVolumeClaims` are bound to volumes that reference existing persistent disks.
  6. (Optional) In the **Choose cluster-scoped resources** section, complete the following and click **Next** :

     1. Choose what group kinds to restore:

        * Click **All cluster-scoped resources** to restore all cluster-scoped resources in the backup. 
          1. Click **Add groupkinds** under the Exceptions section to exclude any cluster-scoped resource in the backup.
        * Click **Selected cluster-scoped resources** to specify the cluster-scoped resources in the backup to restore. `apiextensions.k8s.io/CustomResourceDefinition` and `storage.k8s.io/StorageClass` are selected by default. Click **Add groupkind** to add more cluster-scoped resources.
        * Click **No cluster-scoped resources** to choose to not restore any cluster resource.
**Caution:** Backup for GKE is not allowed to select cluster-scoped resources that are managed by GKE clusters or driven by restore configuration elsewhere. Such GroupKinds include `Namespace`, `Node`, `PersistentVolume`, `gkebackup.gke.io/BackupJob`, `gkebackup.gke.io/RestoreJob`, `metrics.k8s.io/NodeMetrics`, `migration.k8s.io/StorageState`, `migration.k8s.io/StorageVersionMigration`, `snapshot.storage.k8s.io/VolumeSnapshotContent`, `storage.k8s.io/CSINode`. Selecting **All cluster-scoped resources** automatically skips these cluster-scoped resources. Listing them explicitly results in an error.
     2. Choose how to handle conflicts if any cluster-scoped resources are selected:

        * Click **Keep resources in target cluster** to skip a resource if it already exists in the target cluster.
        * Click **Replace resources in target cluster** to delete a resource if it already exists in the target cluster, and restore the copy from the backup.

**Warning:** this is a dangerous option which could cause unintentional data loss if used inappropriately. For example, deleting a CRD will cause Kubernetes to delete all CRs of that type.
  7. (Optional) In the **Add transformation rules** section, complete the following and click **Next** :

     1. Click **Add rule** and enter an optional description.
     2. If you want to restrict the transformation rules to resources that match specific conditions, do the following in the **Specify resource conditions and actions** section: 
        1. Click **Namespaces condition** and type a list of namespaces to match resources within those namespaces.
        2. Click **Groupkind condition** and type API group kind and then type the object kind. This matches an API group to resources within those types.
        3. Click **JSON path condition** and type the JSON path that identifies the fields within the matched resources for which the transformation applies.
        4. Type the new value that replaces the current value of the matched attributes, or select the **Replace specific values (using a regular expression)** checkbox. Then type the pattern to compare against the current value of those resources.
     3. Click **Save changes**.
  8. Review the restore plan details and click **Create plan**.




## View a restore plan

You can view a restore plan and its details by using the gcloud CLI or the Google Cloud console.

### gcloud

To list all the restore plans within the project and location, run the following command:
    
    
    gcloud beta container backup-restore restore-plans list \
        --project=PROJECT_ID \
        --location=LOCATION
    

For **`list`** commands only, you can provide `-` as the value for any parameters except `PROJECT_ID`. The `-` value acts as a wildcard. The `-` value is the default for any parameter if you don't specify a command-line option or set a property.

For the full list of options, refer to the [`gcloud beta container backup-restore restore-plans list`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/restore-plans/list) documentation.

To see the details of a restore plan, run the following command:
    
    
    gcloud beta container backup-restore restore-plans describe RESTORE_PLAN \
         --project=PROJECT_ID \
         --location=LOCATION
    

### Console

Use the following instructions to view a restore plan and its details in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Restore Plans** tab.

  4. Expand the backup plan and click the restore plan name.

  5. Click the **Details** tab to view its details.




## Update a restore plan

Update a restore plan and its details by using the gcloud CLI.

### gcloud

To update a restore plan, for example by adding a new description, run the following command:
    
    
    gcloud beta container backup-restore restore-plans update RESTORE_PLAN \
        --project=PROJECT_ID \
        --location=LOCATION \
        --description=DESCRIPTION
    

For the full list of options, refer to the [`gcloud beta container backup-restore restore-plans update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/restore-plans/update) documentation.

### Console

Use the following instructions to update a restore plan in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Restore Plans** tab.

  4. Click the restore plan name.

  5. Click the **Details** tab.

  6. Click _edit_ **Edit** to edit a plan section and click **Save changes**.




## Delete a restore plan

You can delete a restore plan by using the gcloud CLI or the Google Cloud console. Deleting a restore plan also deletes any child restore plans.

### gcloud

To delete a restore plan, run the following command:
    
    
    gcloud beta container backup-restore restore-plans delete RESTORE_PLAN \
        --project=PROJECT_ID \
        --location=LOCATION
    

For the full list of options, refer to the [`gcloud beta container backup-restore restore-plans delete`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/backup-restore/restore-plans/delete) documentation.

### Console

Use the following instructions to delete a restore plan in the Google Cloud console:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Restore Plans** tab.

  4. Expand the cluster and click the plan name.

  5. Click _delete_ **Delete plan**.

  6. Type the restore plan name and then click **Delete restore plan** in the confirmation dialog.




## What's next

  * Learn more about [restoring a backup](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
