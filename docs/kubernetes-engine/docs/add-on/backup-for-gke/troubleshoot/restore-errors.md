---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/restore-errors/
title: Troubleshoot restore operation errors in Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:06.702917+00:00
---

# Troubleshoot restore operation errors in Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/restore-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Troubleshoot restore operation errors in Backup for GKE Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This document describes the errors and corresponding codes you might encounter when using Backup for GKE to perform restore operations. Included in each section are things to consider when performing actions to resolve the restore errors, and instructions on how to resolve the restore operation errors.

## Error 200010301: Failure to complete restore operation due to unavailable admission webhook service

Error `200010301` occurs when an attempt to complete a restore operation fails because an admission webhook service, also referred to as an HTTP callback, is unavailable, which results in the following error message. The error message indicates that the GKE API server attempted to contact an admission webhook while trying to restore a resource but the service backing the webhook was either unavailable or not found:
    
    
      resource [/example-group/ClusterSecretStore/example-store] restore failed:
    
      Internal error occurred: failed calling webhook "example-webhook.io":
      failed to call webhook: Post "https://example-webhook.example-namespace.svc:443/validate-example": service "example-webhook" not found.
    

This error occurs when a `ValidatingAdmissionWebhook` or `MutatingAdmissionWebhook` GKE resource is active in the target cluster, but the GKE API server can't reach the endpoint configured in the webhook. Admission webhooks intercept requests to the GKE API server, and their configuration specifies how the GKE API server should query the requests.

The webhook's `clientConfig` specifies the backend that handles the admission requests, which can be an internal cluster service or an external URL. The choice between these two options depends on the specific operational and architectural requirements of your webhook. Depending on the option type, the restore operation might have failed for the following reasons:

  * **In-cluster services** : the GKE service and its backing pods aren't restored or ready when the GKE API server attempted to call the webhook. This occurs during restore operations where cluster-scoped webhook configurations are applied before the namespaced services are fully in a `ready` state.

  * **External URLs** : the external endpoint is temporarily unavailable due to network connectivity issues between the GKE cluster and the external endpoint, or due to DNS resolution issues or firewall rules.




To resolve this error, use the following instructions:

  1. Identify the failing webhook mentioned in the error message. For example, `failed calling webhook "..."`.

  2. Inspect the webhook by running the `kubectl get validatingwebhookconfigurations` command:
         
         kubectl get validatingwebhookconfigurations WEBHOOK_NAME -o yaml
         

Replace `WEBHOOK_NAME` with the name of the webhook that was identified in the error message.

You can also run the `kubectl get mutatingwebhookconfigurations` command to inspect the webhook:
         
         kubectl get mutatingwebhookconfigurations WEBHOOK_NAME -o yaml
         

Replace `WEBHOOK_NAME` with the name of the webhook that was identified in the error message.

**Note:** Webhooks are either validating or mutating. Therefore, depending on the webhook type, only one of these commands succeeds.
  3. Perform the following troubleshooting steps based on your configuration type:

### Service-based `clientConfig`

Define a custom restore order by modifying the `RestorePlan` resource to include a `RestoreOrder` with `GroupKindDependency` entries. This allows the components backing the webhook such as `Deployment`, `StatefulSet`, or `Service` to be restored and ready before the `ValidatingWebhookConfiguration` or `MutatingWebhookConfiguration`.

For instructions on how to define a custom restore order, see [Specify resource restore ordering during restoration](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore-order).

This approach can fail because the service's pods don't enter a fully `ready` state even after the `Service` object is created. Another reason for failure could be because the webhook configuration might be created unexpectedly by another application. Alternatively, you can perform a two-stage restore operation using the following steps:

     1. Create a `Restore` resource using the backup by configuring the restore operation with a fine-grained restore filter which would include the specific resources that are required for the webhook to function, for example, `Namespaces`, `Deployments`, `StatefulSets`, or `Services`.

For more information on how to configure the restore with a fine-grained restore filter, see [Enable fine-grained restore](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/fine-grained-restore).

     2. Create another `Restore` resource for the backup operation and configure the rest of the resources you choose.

### URL-based `clientConfig`

     1. Verify the external HTTPS endpoint and make sure it's active, reachable, and functioning correctly.

     2. Confirm that there is network connectivity from your GKE cluster's nodes and control plane to the external URL. You might also need to check firewall rules, for example, if you're using Virtual Private Cloud, on-premises, or a cloud provider hosting the webhook, network policies, and DNS resolution.

  4. Retry the restore operation. If the operation continues to fail, contact Cloud Customer Care for further assistance.




## Error 200010302: Failure to complete restore operation due to denied resource creation request

Error `200010302` occurs when an attempt to complete a restore operation fails because an admission webhook denies a resource creation request, which results in the following error message indicating that a resource from your backup couldn't be created in the target cluster because an active admission webhook intercepted the request and rejected it based on a custom policy:
    
    
      [KubeError]; e.g. resource
    
      [/example-namespace/example-api/ExampleResource/example-name]
    
      restore failed: admission webhook "example-webhook.example.com" denied the request: {reason for denial}
    

This error is caused by the configuration set in the target GKE cluster, which has either a `ValidatingAdmissionWebhook` or `MutatingAdmissionWebhook` that enforces specific rules on resource creation and modification, blocking the resource creation request. For example, a webhook prevents the creation of a resource because a related but conflicting resource already exists in the cluster. For example, a webhook might deny the creation of a deployment if it's already managed by a `HorizontalPodAutoscaler` GKE API resource.

To resolve this error, use the following instructions:

  1. Identify the webhook that is denying the request using the error message that occurs when the restore operation fails. For example, `webhook WEBHOOK_NAME denied the request` The error message contains the following information:

     * **Webhook name** : the name of the webhook denying the request.

     * **Reason for denial** : the specific reason for denying the request.

  2. Inspect the webhook by running the `kubectl get validatingwebhookconfigurations` command:
         
         kubectl get validatingwebhookconfigurations WEBHOOK_NAME -o yaml
         

Replace `WEBHOOK_NAME` with the name of the webhook you identified in the error message.

You can also run the `kubectl get mutatingwebhookconfigurations` command to inspect the webhook:
         
         kubectl get mutatingwebhookconfigurations WEBHOOK_NAME -o yaml
         

Replace `WEBHOOK_NAME` with the name of the webhook you identified from the error message.

**Note:** Webhooks are either validating or mutating. Therefore, depending on the webhook type, only one of these commands succeeds.
  3. Resolve the underlying issue in the target cluster. The correct action depends on the specific error. For the example, if there is an `HorizontalPodAutoscaler` conflict, you need to delete the existing `HorizontalPodAutoscaler` in the target cluster before running the restore to allow the backed-up workloads and its associated resources to be created.

  4. Retry the restore operation. If the restore operation continues to fail, contact Cloud Customer Care for further assistance.




## Error 200060202: Failure to complete restore operation due missing GKE resource during workload validation

Error `200060202` occurs during the workload validation phase of a restore operation when a GKE resource that Backup for GKE expects to validate cannot be found in the target cluster, resulting in the following error message:
    
    
      Workload Validation Error: [KIND] "[NAME]" not found
    

For example, `Example: Workload Validation Error: pods "jenkins-0" not found`

This error occurs when Backup for GKE successfully creates or updates the GKE resource as part of the restore operation's process but when the validation stage begins, one or more of the GKE resources is no longer present in the target cluster because the resource was deleted after the resource was created or updated initially by the restore process but before workload validation for the GKE resource could complete. An error like this can occur for the following reasons:

  * **Manual deletion** : a user or administrator manually deleted the resource using `kubectl` or other Google Cloud tools.

  * **External automation** : [GitOps](https://www.gitops.tech/) controllers such as Config Sync, [ArgoCD](https://argo-cd.readthedocs.io/en/stable/), [Flux](https://fluxcd.io/), custom scripts, or other cluster management tools reverted or deleted the resource to match a desired state in a repository.

  * **GKE controllers** : a GKE controller deleted a resource because it conflicts with other resources or policies, or an `OwnerReference` chain leads to [_garbage collection_](https://kubernetes.io/docs/concepts/architecture/garbage-collection/), or the automated cleanup process by GKE that deletes dependent resources when their `owner` resource is deleted.




To resolve this error, use the following instructions:

  1. Identify the missing resource using the error message that appears when the restore operation fails to complete.

  2. Locate the namespace the resource belongs to using one of the following methods:

     * **GKE audit logs** : examine the GKE audit logs that were generated when you attempted the restore operation. You can filter logs for delete operations on the resource `Kind` and `Name`. The audit log entry contains the original namespace.

     * **Backup details** : review the scope of your restore operation and the contents of the backup. The backup index shows the original namespace of the resource. You can also verify if the `RestorePlan` contains a `TransformationRule` which specify rules to restore the resource in the namespace you choose.

     * **Search across namespaces** : run the `kubectl get` command to search for the resource across all namespaces:
           
           kubectl get KIND --all-namespaces | grep NAME
           

Replace `KIND` and `NAME` with the values from the error message. If the resource still exists, this command will show its namespace.

  3. Verify deletion by running the `kubectl get` command:
         
         kubectl get KIND NAME -n [NAMESPACE]
         

Replace `KIND` and `NAME` with the values from the error message. You should receive a `not found` error message.

  4. Investigate the cause of deletion using one of the following methods:

     * **GKE audit logs** : identify which entity issued the deletion request. For example, the user, service account, or controller.

     * **Review configured automations** : If you use GitOps or other automation tools, check their logs and status to see if they interfered with the restored resources.

     * **Examine related events** : check GKE events in the determined namespace by running the `kubectl get events` command:
           
           kubectl get events -n NAMESPACE_NAME --sort-by='.lastTimestamp'
           

Replace `NAMESPACE_NAME` with the name of the namespace.

  5. Address the cause of the resource deletion based on the results of the previous step. For example, pause conflicting automations, correct misconfigurations, or adjust user permissions.

  6. Recover the missing resource using one of the following methods:

     * **Re-apply manifests files** : if you have the manifest for the missing resource, you can re-apply it to the correct namespace.

     * **Perform a fine-grained restore** : perform a fine-grained restore operation to selectively restore just the missing resource from the same backup, which ensures you specify the correct namespace. For more information about how to perform a fine-grained restore operation, see [Enable fine-grained restore](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/fine-grained-restore).

**Note:** The error only points to a single resource which can't be found but there might be more than one resource which actually doesn't exist in the target cluster.
  7. Retry the restore operation. If the restore operation continues to fail, contact Cloud Customer Care for further assistance.




## Error 200060201: Failure to complete restore operation due to workload validation timeout

Error `200060201` occurs when one or more restored workloads fail to become fully `ready` during a restore operation within the expected time limit after the resources have been created in the cluster, resulting in the following error message:

`Workload Validation Error: Timedout waiting for workloads to be ready - [namespace/workload_name, ...]`

This error occurs because Backup for GKE performs a validation step after restoring GKE resource configurations to ensure that critical workloads are functioning correctly. Backup for GKE waits for certain workloads to reach a `ready` state, but at least one workload didn't meet the the following readiness criterion within the allocated timeout period:

  * For **`Pods`** : `status.Phase` is `Running`

  * For **`Deployments`** : `status.ReadyReplicas` equals `spec.Replicas`

  * For **`StatefulSets`** : `status.ReadyReplicas` equals `spec.Replicas`

  * For **`DaemonSets`** : `status.NumberReady` equals `status.DesiredNumberScheduled`




To resolve this error, use the following instructions:

  1. Identify the workloads that aren't in a `ready` state in the error message that lists the workloads and their namespaces that failed to enter a `ready` state.

  2. Inspect workload status and get details and events for the failed workloads by running the `kubectl describe` command:
         
         kubectl describe WORKLOAD_TYPE WORKLOAD_NAME -n NAMESPACE_NAME
         kubectl get pods -n NAMESPACE_NAME -l SELECTOR_FOR_WORKLOAD
         

Replace the following:

     * `WORKLOAD_TYPE`: the type of workload, for example, `Deployment`, `StatefulSet`, or `DaemonSet`.

     * `WORKLOAD_NAME`: the name of the specific workload instance.

     * `NAMESPACE_NAME`: the namespace where the workload is located.

     * `SELECTOR_FOR_WORKLOAD`: the label selector to find `Pods` associated with the workload. For example, `app=my-app`.

For pods within `Deployments` or `StatefulSets` workload types, check the status of individual Pods by running the `kubectl describe pod` command:
    
    kubectl describe pod POD_NAME -n NAMESPACE_NAME
    

Replace the following:

     * `POD_NAME`: the name of the specific pod.

     * `NAMESPACE_NAME`: the namespace where the pod is located.

  3. In the `Events` section, analyze events and logs in the `describe` output and locate the following information:

     * `ImagePullBackOff / ErrImagePull`: indicates that there are issues fetching container images.

     * `CrashLoopBackOff`: indicates that containers are starting and crashing.

  4. In the `Containers` section, analyze container logs in the `describe` output to find the container name by running the `kubectl logs` command:
         
         kubectl logs POD_NAME -n NAMESPACE_NAME -c CONTAINER_NAME
         

Replace the following:

     * `POD_NAME`: the name of the specific pod.

     * `NAMESPACE_NAME`: the namespace where the pod is located.

     * `CONTAINER_NAME`: the name of the container within the Pod.

According to the `describe` output, there are several reasons the pod might not appear in the resource output, including the following:

     * **Readiness probe failures** : the container's readiness probes aren't succeeding.

     * **Resource issues** : there is insufficient CPU, memory, or other resources in the cluster or quota limits being reached.

     * **Init container issues** : failures in init containers blocking main containers from starting.

     * **Config errors** : errors in `ConfigMaps`, `Secrets`, or environment variables.

     * **Network issues** : `Pods` are unable to communicate with required services.

  5. Check the GKE cluster resources to ensure the GKE cluster has sufficient node capacity, CPU, and memory to run the restored workloads. In Autopilot clusters, node auto-provisioning might take additional time, therefore, we recommend checking for any node scaling limitations or errors. Address underlying issues based on your findings, and resolve the issues preventing the workloads from entering a `ready` state. This appraoch can involve correcting manifests, adjusting resource requests or limits, fixing network policies, or ensuring dependencies are met.

  6. After underlying issues are resolved, wait for the workloads to enter a `ready` state. You don't need to run the restore operation again.




If the issue persists, contact Cloud Customer Care for further assistance.

## Error 200060102: Failure to complete restore operation due to volume validation error

Error `200060102` occurs because one or more `VolumeRestore` resources, which manage the process of restoring data from `VolumeBackup` to a `PersistentVolume`, have entered a `failed` or `deleting` state during the volume validation phase of a restore operation. The failed volume restore results in the following error message in the restore resource's stateReason field:
    
    
    Volume Validation Error: Some of the volume restores failed - [projects/PROJECT_ID/locations/LOCATION/restorePlans/RESTORE_PLAN_ID/restores/RESTORE_ID/volumeRestores/VOLUME_RESTORE_ID (PVC: NAMESPACE/PVC_NAME), ...]
    

The error message lists the full resource names of the failed `VolumeRestore`, including the target `PersistentVolumeClaim` name and namespace. The error message indicates that the data restoration process for the affected `PersistentVolumeClaim` didn't complete successfully when Backup for GKE initiated `VolumeRestore` resources to provision `PersistentVolumes` from `VolumeBackups`, and the underlying Persistent Disk creation from the snapshot failed. `VolumeRestore` failures can occur for the following reasons:

  * **Insufficient quota** : there isn't enough allocated Persistent Disk quota in the project or region, for example, `SSD_TOTAL_GB`.

  * **Permission issues** : the service account used by Backup for GKE lacks the necessary permissions to create disks or access snapshots.

  * **Network issues** : there are transient or persistent network issues interrupting the disk creation process.

  * **Invalid snapshot** : the source `VolumeBackup` or the underlying Persistent Disk snapshot is corrupted or inaccessible.

  * **Resource constraints** : other cluster resource constraints are hindering volume provisioning.

  * **Internal errors** : there are internal issues within the Persistent Disk service.




To resolve this error, use the following instructions:

  1. Identify the failed `PersistentVolumeClaims` listed in the error message, which lists the full resource names of the `VolumeRestore` objects that failed.

  2. Get details of each failed `VolumeRestore` resource by running the `gcloud beta container backup-restore volume-restores describe` command:
         
         gcloud beta container backup-restore volume-restores describe VOLUME_RESTORE_ID \
         --project=PROJECT_ID \
         --location=LOCATION \
         --restore-plan=RESTORE_PLAN_ID \
         --restore=RESTORE_ID
         

Replace the following:

     * `VOLUME_RESTORE_ID`: the ID of the failed `VolumeRestore` resource.

     * `PROJECT_ID`: the ID of your Google Cloud project.

     * `LOCATION`: the Google Cloud location of the restore.

     * `RESTORE_PLAN_ID`: the ID of the restore plan.

     * `RESTORE_ID`: the ID of the restore operation.

  3. Examine the `state` and `stateMessage` fields in the output for details regarding the failure.

**Note:** In some cases, the `PersistentVolumeClaim` name and namespace aren't in the restore operation error message. Use the `stateMessage` field from the `gcloud describe` command above to find the target `PersistentVolumeClaim` details.
  4. Examine the state of the target `PersistentVolumeClaim` by running the `kubectl get pvc` command:
         
         kubectl get pvc PVC_NAME -n NAMESPACE_NAME -o yaml
         

Replace the following:

     * `PVC_NAME`: the name of the `PersistentVolumeClaim` resource.

     * `NAMESPACE_NAME`: the namespace where the `PersistentVolumeClaim` is located.

  5. Confirm that the `status.phase` section of the output indicates a `Pending` phase. This phase means that the `PersistentVolumeClaim` isn't yet bound to a `PersistentVolume`, which is expected if the `VolumeRestore` fails.

  6. Inspect the `Events` section in the YAML output for messages related to provisioning failures, such as `ProvisioningFailed`, for example:
         
         Cloud KMS error when using key projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/CRYPTO_KEY:  Permission 'cloudkms.cryptoKeyVersions.useToEncrypt' denied  on resource 'projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/CRYPTO_KEY' (or it may not exist).
         

The output indicates that there is a permission issue while accessing the encryption key during disk creation. To provide `compute service agent` relevant permission to access the key, use the instructions described in the Backup for GKE documentation about [enabling CMEK encryption](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-cmek#enable_cmek_encryption).

  7. Review the GKE events in the `PersistentVolumeClaim` namespace, which provide detailed error messages from the `PersistentVolume` controller or CSI driver, by running the `kubectl get events` command:
         
         kubectl get events -n NAMESPACE_NAME --sort-by='.lastTimestamp'
         

Replace `NAMESPACE_NAME` with the namespace of the `PersistentVolumeClaim`,

  8. Identify events related to the `PersistentVolumeClaim` name, which contains keywords such as `FailedProvisioning` or `ExternalProvisioning`. The events can also contain errors from the storage provisioner, such as `pd.csi.storage.gke.io`.

  9. Examine Persistent Disk logs by checking Cloud Audit Logs and Persistent Disk logs in Cloud Logging for any errors related to disk creation operations around the time of the failure.

  10. Based on the generated error messages, address the following underlying issues:

     * Increase Persistent Disk quotas if indicated, such as `(QUOTA_EXCEEDED}: Quota SSD_TOTAL_GB exceeded`.

     * Verify and correct IAM permissions.

     * Investigate and resolve network issues.

     * Contact Cloud Customer Care to resolve issues with the snapshot or the Persistent Disk service.

     * The `PersistentVolumeClaim` remains in a `Pending` state.

     * The restore operation process doesn't automatically retry the `VolumeRestore`. To resolve this, you should trigger a restore operation for the `Deployment` or `StatefulSet` workload that uses the affected `PersistentVolumeClaim`.

     * Use a fine-grained restore to selectively restore the `Deployment` or `StatefulSet` workload associated with the failed `PersistentVolumeClaim`. This approach lets the standard GKE mechanisms handle the `PersistentVolumeClaim` creation and binding process again if the underlying issue is fixed. For more information about fine-grained restore, see [Enable fine-grained restore](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/fine-grained-restore).




If the issue persists or the cause of the `VolumeRestore` failure is unclear, contact Cloud Customer Care for further assistance.

## Error 200060101: Failure to complete restore operation due to volume validation timeout

Error `200060101` occurs during the volume validation phase of a restore operation when Backup for GKE stops waiting because at least one `VolumeRestore` resource, which manages restoring data from a `VolumeBackup`, didn't reach a `succeeded` state within the allocated timeout period. Other `VolumeRestore` resources might also be incomplete.

The error message in the `Restore` resource's `stateReason` field shows the list of `VolumeRestore` resources encountered that weren't yet in a `succeeded` state when the timeout was checked. It includes the target `PersistentVolumeClaim` name and namespace for those `VolumeRestore` resources, for example:
    
    
    Volume Validation Error: Timed out waiting for volume restore [projects/PROJECT_ID/locations/LOCATION/restorePlans/RESTORE_PLAN_NAME/restores/RESTORE_NAME/volumeRestores/VOLUME_RESTORE_ID (PVC: PVC_NAMESPACE/PVC_NAME), ...]
    

Additionally, if any volume restores failed, the error message includes those failures, for example:
    
    
    Volume Validation Error: Timed out waiting for volume restore [projects/PROJECT_ID/locations/LOCATION/restorePlans/RESTORE_PLAN_NAME/restores/RESTORE_NAME/volumeRestores/VOLUME_RESTORE_ID (PVC: PVC_NAMESPACE/PVC_NAME), ...] and some of the volume restores failed - [projects/PROJECT_ID/locations/LOCATION/restorePlans/RESTORE_PLAN_ID/restores/RESTORE_ID/volumeRestores/VOLUME_RESTORE_ID (PVC: NAMESPACE/PVC_NAME), ...]
    

Backup for GKE initiates `VolumeRestore` resources to provision `PersistentVolumes` from `VolumeBackups`. The error indicates that the underlying Persistent Disk creation from the snapshot and the subsequent binding of the `PersistentVolumeClaim` to the `PersistentVolume` took longer than the calculated timeout for the cited `VolumeRestores`. Other `VolumeRestores` for the same restore operation might also be in a non-completed state.

Even though the timeout was reached from a Backup for GKE perspective, the underlying disk creation process for the mentioned `VolumeRestore` resource, and potentially `VolumeRestore` resources, might still be ongoing or have failed.

To resolve this issue, use the following instructions:

  1. Identify the timed-out `PersistentVolumeClaim` name and namespace in the error message, for example, `(PVC: PVC_NAMESPACE/PVC_NAME)`.

  2. List all the `VolumeRestores` associated with the restore operation to see their current states by running the `gcloud beta container backup-restore volume-restores list` command:
         
         gcloud beta container backup-restore volume-restores list \
         --project=PROJECT_ID \
         --location=LOCATION \
         --restore-plan=RESTORE_PLAN_NAME \
         --restore=RESTORE_NAME
         

Replace the following:

     * `PROJECT_ID`: the ID of the Google Cloud project.

     * `LOCATION`: the Google Cloud location of the restore.

     * `RESTORE_PLAN_NAME`: the name of the restore plan.

     * `RESTORE_NAME`: the name of the restore operation.

  3. Locate `VolumeRestores` that aren't in a `succeeded` state.

  4. If there are any volumes in a `failed` state, you need to perform troubleshooting steps to resolve the volume validation error. For more information, see Error 200060102: Failure to complete restore operation due to volume validation error. If any volumes have failed, they are listed in the second part of the error message.

  5. Get details about the `VolumeRestore` mentioned in the error and any other `VolumeRestores` that aren't in a `succeeded` state by running the `gcloud beta container backup-restore volume-restores describe` command:
         
         gcloud beta container backup-restore volume-restores describe VOLUME_RESTORE_ID \
         --project=PROJECT_ID \
         --location=LOCATION \
         --restore-plan=RESTORE_PLAN_NAME \
         --restore=RESTORE_NAME
         

Replace the following:

     * `VOLUME_RESTORE_ID`: the ID of the `VolumeRestore` resource.

     * `PROJECT_ID`: the ID of your Google Cloud project.

     * `LOCATION`: the Google Cloud location of the restore.

     * `RESTORE_PLAN_NAME`: the name of the restore plan.

     * `RESTORE_NAME`: the name of the restore operation.

  6. Check the `state` and `stateMessage` fields. The value of the `state` field is likely `creating` or `restoring`. The `stateMessage` field might provide more context and contain the target `PersistentVolumeClaim` details.

  7. Examine the state of the identified target `PersistentVolumeClaims` by running the `kubectl get pvc` command:
         
         kubectl get pvc PVC_NAME -n PVC_NAMESPACE -o yaml
         

Replace the following:

     * `PVC_NAME`: the name of the `PersistentVolumeClaim`.

     * `PVC_NAMESPACE`: the namespace of the `PersistentVolumeClaim`.

The value of the `PersistentVolumeClaim's` `status.phase` is likely to be `Pending`. Check the `Events` section for the following errors:

     * **`Waiting for first consumer to be created before binding`** : indicates that the `StorageClass` has `volumeBindingMode: WaitForFirstConsumer`.

Provisioning of the `PersistentVolume` is delayed until a `Pod` that uses the `PersistentVolumeClaim` is created and scheduled. The issue might be with the `Pod` scheduling, not the volume provisioning itself. Therefore, we recommend confirming why the `Pods` consuming the `PersistentVolumeClaim` aren't being scheduled or aren't starting.

     * **`FailedProvisioning` or errors from the storage provisioner**: For example, `pd.csi.storage.gke.io`.

  8. Review GKE events in the relevant namespaces by running the `kubectl get events` command:
         
         kubectl get events -n PVC_NAMESPACE --sort-by='.lastTimestamp'
         

Replace `PVC_NAMESPACE` with the namespace of the `PersistentVolumeClaim`.

Look for events related to the `PersistentVolumeClaim` names, such as provisioning messages or errors.

  9. Check Cloud Audit Logs and Persistent Disk logs in Cloud Logging.

  10. Monitor the status of all `VolumeRestores` in `creating` and `restoring` states.

After the issue, is fixed, the status of the `VolumeRestores` can transition to either `succeeded` or `failed` states. If the `VolumeRestores` reach a `succeeded` state, the `PersistentVolumeClaims` should become `Bound` and workloads should be functional. If any `VolumeRestore` enters a `failed` state, you need to perform troubleshooting steps to resolve the volume validation error. For more information, see [Error 200060102: Failure to complete restore operation due to volume validation error](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/restore-errors#volume-validation-error)




If `VolumeRestores` remain in `creating` or `restoring` states for an excessive period of time, contact Cloud Customer Care for further assistance.

## What's next

  * [Read the Backup for GKE error codes overview page for failed backup operations](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/backup-error-codes).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
