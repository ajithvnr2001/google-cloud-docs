---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/resource-conflict/
title: Handle resource conflicts during restore \u00a0|\u00a0 Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:26.852766+00:00
---

# Handle resource conflicts during restore  |  Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/resource-conflict/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Handle resource conflicts during restore Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes how to configure conflict handling strategies for namespaced and cluster-scoped resources in a restore plan.

When restoring to a cluster, you might encounter resource conflicts in the following scenarios:

  * Restoring to an existing cluster that already has resources provisioned.
  * When a Kubernetes resource is managed by tools, such as GitOps or an [operator](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/).



Backup for GKE provides various options to define conflict handling for cluster-scoped and namespaced resources that you can specify in a [restore plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-plan#create_a_restore_plan).

## Restore conflict handling for cluster-scoped resources

You can configure the following options in the restore plan to handle conflicts for a cluster-scoped resources:

  * **Keep resources in target cluster (non-destructive)** : if a resource with the same name exists in the target cluster, leave it as it is.
  * **Replace resources in target cluster (destructive)** : if a resource already exists in the target cluster, delete it and restore the copy from the backup.

**Warning:** This option could cause unintentional data loss if used inappropriately. For example, deleting a `CustomResourceDefinition` will cause Kubernetes to delete all custom `CustomResource` of that type.



### gcloud

Update an existing restore plan to handle conflict for a cluster-scoped resource:
    
    
    gcloud beta container backup-restore restore-plans update RESTORE_PLAN \
        --project=PROJECT_ID \
        --location=LOCATION \
        --cluster-resource-conflict-policy=CLUSTER_RESOURCE_CONFLICT_POLICY
    

Replace the following:

  * `RESTORE_PLAN`: the name of the restore plan that you want to update.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the resource, for example `us-central1`.
  * `CLUSTER_RESOURCE_CONFLICT_POLICY`: defines how to handle restore-time conflicts for selected cluster resources. Use one of the following options:

    * `use-existing-version`: if the resources that are being restored already exist in the target cluster, Backup for GKE keeps the existing resources.
    * `use-backup-version`: if the resources that are being restored already exist in the target cluster, Backup for GKE replaces the existing resources with the new resources from the backup.



### Console

Use the following instructions to update cluster-scoped resources conflict policy in the Google Cloud console:

  1. In the Google Cloud console, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Restore plans** tab.

  4. Click the restore plan name.

  5. Click the **Details** tab.

  6. In the **Restore configurations** section, go to the **Cluster-scoped resources** section and click **Edit**.

  7. In the **Define conflict handling** section, select a conflict handling option.

  8. Click **Save changes**.




## Restore conflict handling for namespaced resources

In the restore plan, you can configure the following options to manage conflict for a namespaced resource. You can specify conflict handling for namespaced resources at the following levels:

  * Individual resource
  * Namespace and ProtectedApplication

**Note:** If the restore plan includes destructive policies, such as merge replace volume, merge replace, and rollback, the PV and volume continue to exist but become orphaned and unused if the reclaim policy is [Retain](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#retain). If the reclaim policy is [Delete](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#delete), the PV and volume are deleted.

The following are the available options to handle conflicts for the individual resources:

  * **Merge skip (non-destructive)** : if a specific resource already exists, skip restoring the resource from the backup.
  * **Merge replace volume (destructive)** : if a specific resource already exists, skip restoring that resource but replace the underlying persistent volume using the volume data restore policy. The merge replace volume achieves the data-only restore.
  * **Merge replace (destructive)** : if a specific resource already exists, replace that resource with the one from backup and the associated volume data by following the volume data restore policy. To replace an existing resource, the first attempt tries to update the resource to match the one from the backup; if the update fails, the second attempt tries to delete the resource and restore it from the backup. Note that this mode could cause data loss because it replaces the existing resources in the target cluster, and the original PV can be retained or deleted depending on its reclaim policy.



The following are the available options to handle conflicts of all resources belonging to a **Namespace** and **ProtectedApplication** :

  * **Fail on conflict (non-destructive)** : if namespace or [ProtectedApplication](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/protected-application) targeted for restore from a backup that already exists in the target cluster, the restore fails.
  * **Rollback (destructive)** : when the target cluster contains the namespace or [ProtectedApplication](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/protected-application) that are targeted for restore to the cluster, the existing group of resources is deleted before the new resources are restored.




### gcloud

Update an existing restore plan to handle conflict for a namespaced resource:
    
    
    gcloud beta container backup-restore restore-plans update RESTORE_PLAN \
        --project=PROJECT_ID \
        --location=LOCATION \
        --namespaced-resource-restore-mode=NAMESPACED_RESOURCE_RESTORE_MODE
    

Replace the following:

  * `RESTORE_PLAN`: the name of the restore plan that you want to update.
  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the [compute region](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the resource, for example `us-central1`.
  * `NAMESPACED_RESOURCE_RESTORE_MODE`: defines how to handle restore-time conflicts for namespaced resources. Use one of the following options:

    * `merge-skip-on-conflict`: skip the individual conflicting resources.
    * `merge-replace-volume-on-conflict`: skip the individual conflicting resources but replace the underlying persistent volume data.
    * `merge-replace-on-conflict`: replace the individual conflicting resources and underlying persistent volume data.
    * `fail-on-conflict`: to fail on conflicting namespace or [ProtectedApplication](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/protected-application).
    * `delete-and-restore`: roll back conflicting namespace or [ProtectedApplication](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/protected-application).



### Console

Use the following instructions to update namespaced resources conflict policy in the Google Cloud console:

  1. In the Google Cloud console, go to the **Google Kubernetes Engine** page.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the navigation menu, click **Backup for GKE**.

  3. Click the **Restore Plans** tab.

  4. Click the restore plan name.

  5. Click the **Details** tab.

  6. In the **Restore configurations** section, go to the **Namespaced resources** section and click **Edit**.

  7. In the **Define conflict handling** section, select a conflict handling option.

  8. Click **Save changes**.




## Recommended conflict handlings for common scenarios

The following table lists the recommended conflict handling strategies for certain common scenarios:

**Scenarios** | **Use the recommended conflict handling for a namespaced resource** | **Use the recommended conflict handling for a cluster-scoped resource**  
---|---|---  
Restore to a brand new cluster | Fail on conflict | Keep resources in target cluster  
Roll back the entire namespace or [ProtectedApplication](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/protected-application) | Delete and restore | Not applicable  
Restore to a GitOps managed cluster without volumes | Merge skip | Keep resources in target cluster  
Data-only restore for a GitOps managed cluster | Merge replace volume | Keep resources in target cluster  
Roll back selected workload and volume data | Merge replace | Replace resources in target cluster  
  
## What's next

  * Learn more about [restoring a backup](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
