---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/system-errors/
title: Troubleshoot system errors in Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:13.665978+00:00
---

# Troubleshoot system errors in Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/system-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Troubleshoot system errors in Backup for GKE Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This page describes system-related errors you might experience when you use Backup for GKE, things to consider when you back up resources, and steps for troubleshooting the issue.

## Error 100010108: Failed to backup PersistentVolumeClaim - Missing Backup Plan CMEK for encrypted disk

Error `100010108` occurs when creating regionally scoped volume backups, and the Backup Plan CMEK is mandated because the GKE cluster references an encrypted disk.

### Understanding the Error

When creating regionally scoped volume backups, the Backup Plan CMEK is mandated if the GKE cluster references any encrypted disk. This is a strict requirement for regionally scoped volume backups; if the source disk is encrypted, the snapshot for that disk is only possible if a Backup Plan CMEK is provided. If your Backup Plan lacks this CMEK configuration, the snapshot creation fails, and you will see an error message similar to the following:
    
    
    failed to create snapshot as disk "pvc-1" is encrypted with CMEK "projects/proj1/locations/us-east1/keyRings/keyring1/cryptoKeys/key1/cryptoKeyVersions/1", but no Backup Plan CMEK is provided. Please add CMEK to the Backup Plan.
    

### Troubleshooting Steps

  1. **Identify the missing CMEK configuration** : The error message confirms that the PVC being backed up is encrypted, but the Backup Plan configuration is missing an encryption key.
  2. **Add a CMEK to the Backup Plan** : Update your Backup Plan configuration to include a Customer-Managed Encryption Key (CMEK). This key will be used to encrypt the backup data, including the regionally scoped volume backups.
  3. **Ensure proper permissions** : Verify that the Backup for GKE service agent (`service-PROJECT_NUMBER@gcp-sa-gkebackup.iam.gserviceaccount.com`) has the `roles/cloudkms.cryptoKeyEncrypterDecrypter` role assigned for the newly added CMEK.
  4. **Retest the Backup Operation** : Once the Backup Plan is updated with the CMEK and permissions are granted, retry the backup operation.



## Error 100020102: CustomResourceDefinition - has an invalid schema - Unsupported v1beta1 API version

Error `100020102` occurs when an attempt to back up a `CustomResourceDefinition` that was originally applied as a `apiextensions.k8s.io/v1beta1` version fails because it lacks the structural schema that's required in the `apiextensions.k8s.io/v1` API version. This error results in the following error message: `CustomResourceDefinition - has an invalid schema. The resource was originally applied as v1beta1, which has been removed from Kubernetes 1.22+`.

This error occurs because the `apiextensions.k8s.io/v1beta1` API version was removed in Google Kubernetes Engine version 1.22. For more information about the API removal for GKE version 1.22, see [API removals for GKE v1.22](https://kubernetes.io/blog/2021/07/14/upcoming-changes-in-kubernetes-1-22/#api-changes).

### Backup operation behavior in non-permissive mode

In non-permissive mode, or in a strict backup plan, the backup operation fails if it encounters a resource that can't be backed up, such as a `CustomResourceDefinition` that was created with the `v1beta1` API. This error occurs because the resource lacks the structural schema that's required by the `v1` API. The presence of this `CustomResourceDefinition` is considered a critical error because it might not restore correctly to a newer cluster.

To resolve this error, use the following instructions:

  1. Identify the problematic `CustomResourceDefinition` by running the `kubectl get crd` command:
         
         kubectl get crd CRD_NAME
         

Replace `CRD_NAME` with the name of the `CustomResourceDefinition` from your error message.

  2. In the YAML output, confirm whether the `CustomResourceDefinition` was properly converted from the `vbeta1` API to the `v1` API by locating the following conditions:

     1. **`spec.versions`** : locate the `spec.versions` condition by looking through each version that's listed under the `spec.versions` field. If any of the `spec.versions` are missing the `schema.openAIV3Schema` field, the `CustomResourceDefinition` doesn't have a structural schema defined for that version.

     2. **`status.conditions`** : locate the `status.conditions` condition by finding the `type:NonStructuralSchema` condition. If the `status.conditions`'s `status` is `true`, it explicitly confirms that the schema is not structural.

  3. Upgrade the `CustomResourceDefinition` to `v1` API version by using the following steps:

     1. Edit the existing `CustomResourceDefinition` to make it compatible with the `v1` standard by adding a structural schema that defines every field and its type within the custom resource. For more information about how to add a structural schema, see [Specifying a structural schema](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#specifying-a-structural-schema).

     2. Apply the compatible `v1` manifest to your cluster.

**Note:** In some cases, you might need to delete the previously created `CustomResourceDefinition` that lacks a structural schema and re-apply the `v1` version so that the API server correctly handles the resource convention.
  4. If the upgrade succeeds, re-attempt the backup operation. Otherwise, use one of the following methods to resolve the issue:

     * Delete the `CustomResourceDefinition` by running the `kubectl delete crd` command if the `CustomResourceDefinition` isn't being used in the cluster.

**Note:** You shouldn't attempt to delete a `CustomResourceDefinition` if it's actively serving an existing custom resource in the cluster. You either need to attempt to upgrade the `CustomResourceDefinition` to `v1` API version again or enable permissive mode.
           
           kubectl delete crd CRD_NAME
           

Replace `CRD_NAME` with the name of the `CustomResourceDefinition`you want to delete.

     * Enable permissive mode on the backup plan, which allows Backup for GKE to skip the resource—including `CustomResourceDefinitions` in the `v1beta1` API version—and continue with the rest of the backup operation. For more information about how to enable permissive mode, see [Enable permissive mode on a backup plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permissive-mode).

**Warning:** The problematic `CustomResourceDefinition` and its associated custom resources won't be backed up and won't be included when you restore. To successfully restore such a backup, you need to exclude the resources served by the `CustomResourceDefinition` from the restore, or create the `CustomResourceDefinition` in the target cluster before you start the restore.
  5. Re-attempt the backup operation. If the operation continues to fail, contact Cloud Customer Care for further assistance.




## Error 100020103: Failed to query API resources

Error `100020103` occurs when Backup for GKE fails to discover custom or aggregated Kubernetes API services before taking a backup, resulting in an error message stating `Failed to query API resources. Please check if any API service is unavailable by using 'kubectl get apiservice'`. This happens if an aggregated API service is misconfigured or if its backing services and pods are unhealthy or unreachable. In non-permissive mode, or in a strict backup plan, Backup for GKE stops the backup operation if it encounters an unavailable `APIService` to avoid capturing an incomplete or inconsistent cluster state.

To resolve this error, use the following instructions:

  1. Identify unavailable API services by running the following command:
         
         kubectl get apiservice
         

In the output, look for API services where the `AVAILABLE` column is `False`.

  2. Inspect details of the failing `APIService` by running the following command:
         
         kubectl describe apiservice APISERVICE_NAME
         

Replace `APISERVICE_NAME` with the name of the failing API service, for example, `v1beta1.custom.metrics.k8s.io`.

In the output, review the `Service` field under `spec.service` and the `Conditions` section to identify the backing Service, its namespace, and the cause of the failure (such as missing endpoints or an unreachable target port).

  3. Use one of the following methods to resolve the error:

     * **Restore the backing service** : verify that the backing Service has ready endpoints by running the following command:
           
           kubectl get endpoints -n NAMESPACE SERVICE_NAME
           

Replace the following:

       * `NAMESPACE`: the namespace of the backing service.
       * `SERVICE_NAME`: the name of the backing service.

Verify that the Pods backing the service exist and are in the `Running` state. Resolve any crashing Pods, image pull failures, or network policy misconfigurations that prevent traffic from reaching the backing service.

     * **Delete an orphaned`APIService`**: if the `APIService` belongs to an application, operator, or monitoring tool that was removed or is no longer in use, delete the stale `APIService`:
           
           kubectl delete apiservice APISERVICE_NAME
           

Replace `APISERVICE_NAME` with the name of the orphaned API service.

**Warning:** Don't delete an active `APIService` that workloads or controllers in your cluster depend on, as this can break cluster management and custom resource querying.
     * **Enable permissive mode** : if you can't immediately fix or remove the unavailable API service, enable permissive mode on the backup plan. When permissive mode is enabled, Backup for GKE continues the backup operation. However, resources belonging to the unavailable API group won't be backed up. For more information about how to enable permissive mode, see [Enable permissive mode on a backup plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/permissive-mode).

  4. Re-attempt the backup operation. If the operation continues to fail, contact Cloud Customer Care for further assistance.




## Error 100040102: Namespace not found

Error `100040102` occurs when an attempt to perform a backup operation fails because a namespace specified in the backup scope can't be found within the cluster. The Backup for GKE agent wasn't able to locate one or more namespaces that were explicitly listed in the `selectedNamespaces` field of the `BackupPlan` configuration. Backup for GKE requires all specified namespaces to be present in the cluster at the time the backup operation is initiated. Failure to find the namespace results in the following error message:
    
    
    Namespace [NAMESPACE_NAME] is not found.
    

To resolve this issue, use the following instructions:

  1. Verify that the namespace has been entered correctly by checking the `selectedNamespaces` list in your `BackupPlan` configuration.

  2. Confirm that the namespace reported in the error message exists by running the `kubectl get namespace` command:
         
         kubectl get namespace NAMESPACE_NAME
         

Replace `NAMESPACE_NAME` with the name of the namespace reported in the error message.

If the namespace doesn't exist, a message appears stating that the namespace wasn't found, for example, `Error from server (NotFound): namespaces "[NAMESPACE_NAME]" not found`.

  3. Correct the `BackupPlan`. If the namespace was misspelled, update the `BackupPlan` with the correct namespace name. If the namespace truly no longer exists and does not need to be backed up, remove it from the `selectedNamespaces` list in the `BackupPlan` configuration.

  4. Re-attempt the backup operation after making the necessary corrections to the `BackupPlan` and initiate a new backup.




If the operation continues to fail, contact Cloud Customer Care for further assistance.

## What's next

  * [Read the Backup for GKE error codes overview page](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/backup-error-codes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
