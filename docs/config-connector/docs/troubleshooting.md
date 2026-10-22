---
url: https://docs.cloud.google.com/config-connector/docs/troubleshooting/
title: Troubleshoot Config Connector \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:50.405426+00:00
---

# Troubleshoot Config Connector  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/config-connector/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Config Connector ](https://docs.cloud.google.com/config-connector/docs)
  * [ Guides ](https://docs.cloud.google.com/config-connector/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot Config Connector

This page describes troubleshooting techniques that you can use to troubleshoot Config Connector and common issues that you might encounter when using the product.

## Check Config Connector status and conditions

### Check the version of Config Connector

Run the following command to get the installed Config Connector version, and cross-reference [the release notes](https://docs.cloud.google.com/config-connector/docs/release-notes) to verify that the running version supports the features and resources that you want to use:
    
    
    kubectl get ns cnrm-system -o jsonpath='{.metadata.annotations.cnrm\.cloud\.google\.com/version}'
    

### Check the resource's status and events

Usually, you can determine the issue with your Config Connector resources by [inspecting the state of your resources in Kubernetes](https://docs.cloud.google.com/config-connector/docs/how-to/monitoring-your-resources). Checking a resource's status and events is particularly helpful for determining if Config Connector failed to reconcile the resource and why the reconciliation failed.

### Check that Config Connector is running

To check that Config Connector is running, verify that all of its Pods are `READY`:
    
    
    kubectl get pod -n cnrm-system
    

Example output:
    
    
    NAME                                            READY   STATUS    RESTARTS   AGE
    cnrm-controller-manager-0                       1/1     Running   0          1h
    cnrm-deletiondefender-0                         1/1     Running   0          1h
    cnrm-resource-stats-recorder-77dc8cc4b6-mgpgp   1/1     Running   0          1h
    cnrm-webhook-manager-58496b66f9-pqwhz           1/1     Running   0          1h
    cnrm-webhook-manager-58496b66f9-wdcn4           1/1     Running   0          1h
    

If you have Config Connector installed in [namespaced-mode](https://docs.cloud.google.com/config-connector/docs/how-to/install-namespaced), then you will have one controller (`cnrm-controller-manager`) Pod for each namespace that is responsible for managing the Config Connector resources in that namespace.

You can check the status of the controller Pod responsible for a specific namespace by running:
    
    
    kubectl get pod -n cnrm-system \
        -l cnrm.cloud.google.com/scoped-namespace=NAMESPACE \
        -l cnrm.cloud.google.com/component=cnrm-controller-manager
    

Replace `NAMESPACE` with the name of the namespace.

### Check the controller logs

The controller Pod logs information and errors related to the reconciliation of Config Connector resources.

You can check the controller Pod's logs by running:
    
    
    kubectl logs -n cnrm-system \
        -l cnrm.cloud.google.com/component=cnrm-controller-manager \
        -c manager
    

If you have Config Connector installed in [namespaced-mode](https://docs.cloud.google.com/config-connector/docs/how-to/install-namespaced), then the previous command shows the logs of all controller Pods combined. You can check the logs of the controller Pod for a specific namespace by running:
    
    
    kubectl logs -n cnrm-system \
        -l cnrm.cloud.google.com/scoped-namespace=NAMESPACE \
        -l cnrm.cloud.google.com/component=cnrm-controller-manager \
        -c manager
    

Replace `NAMESPACE` with the name of the namespace.

Read more about how to inspect and query Config Connector's logs.

### Abandon and acquire the resource

In some cases, you might need to update an immutable field in a resource. Since you can't edit immutable fields, you must abandon and then acquire the resource:

  1. Update the YAML configuration of the Config Connector resource and set the `cnrm.cloud.google.com/deletion-policy` annotation to [`abandon`](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources#keeping_resources_after_deletion).
  2. Apply the updated YAML configuration to update the Config Connector resource's deletion policy.
  3. [Abandon the Config Connector resource](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources#delete-bigquery-dataset).
  4. Update the immutable fields that need to be changed in the YAML configuration.
  5. Apply the updated YAML configuration to [acquire the abandoned resource](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources#acquiring_a_resource).



## Troubleshoot by issue type

Use the following table to help troubleshoot your issue based on the type of symptom.

**Type of issue** | **Common issues**  
---|---  
**Reconciliation** | 

  * Resource keeps updating every 5-15 mins
  * Reconciliation fails or loops due to automatic field updates
  * Resource has no status
  * KNV2005: syncer excessively updating resource
  * Resource deleted by Config Connector
  * Controller Pod OOMKilled

  
**Deletion** | 

  * Deletions of namespaces stuck at `Terminating`
  * Deletions of resources stuck at `DeleteFailed` after project was deleted

  
**Permissions** | 

  * Compute Engine Metadata not defined
  * Error 403: Request had insufficient authentication scopes
  * 403 Forbidden: The caller does not have permission
  * Error 403: Caller is missing IAM permission
  * Update error with IAMPolicy, IAMPartialPolicy and IAMPolicyMember

  
**Installation and upgrades** | 

  * Version not supported in Config Connector add-on installations
  * `failed calling webhook`
  * `PodSecurityPolicy` prevents upgrades

  
**Configuration** | 

  * Cannot make changes to immutable fields
  * No matches for kind "RESOURCE_KIND"
  * Labels are not propagated to the Google Cloud resource
  * Error due to special characters in resource name
  * Unable to remove fields from resource spec
  * Invalid value "merge" for `state-into-spec` annotation

  
  
## Reconciliation

The following section lists common issues related to reconciliation of resources by Config Connector.

### Resource keeps updating every 5-15 mins

#### Symptom

Your Config Connector resource keeps switching from an `UpToDate` status to an `Updating` status every 5-10 minutes.

#### Cause

It is likely that Config Connector is detecting unintentional diffs between the resource's desired state and actual state, thereby causing Config Connector to constantly update the resource.

#### Resolution

First, confirm that you do not have any external systems that are constantly modifying either the Config Connector or Google Cloud resource (for example, CI/CD pipelines, custom controllers, cron jobs, etc.).

If the behavior is not due to an external system, see if Google Cloud is changing any of the values specified in your Config Connector resource. For example, in some cases, Google Cloud changes the formatting (for example, capitalization) of field values which leads to a diff between your resource's desired state and actual state.

Get the state of the Google Cloud resource using the REST API (for example, [for ContainerCluster](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/get)) or the Google Cloud CLI. Then, compare that state against your Config Connector resource. Look for any fields whose values do not match, then update your Config Connector resource to match. In particular, look for any values that were reformatted by Google Cloud. For example, see GitHub issues [#578](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/578) and [#294](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/294#issuecomment-960094147).

Note that this is not a perfect method since the Config Connector and Google Cloud resource models _are_ different, but it should let you catch most cases of unintended diffs.

If you are unable to resolve your issue, see Additional help.

### Reconciliation fails or loops due to automatic field updates

This issue occurs when Google Cloud automatically updates a field on a resource that uses the `cnrm.cloud.google.com/state-into-spec: merge` annotation.

#### Symptom

Your Config Connector resource enters an `UpdateFailed` status or repeatedly switches to the `Updating` status after Google Cloud automatically updates a field that you didn't specify in your YAML manifest.

For example, after Cloud SQL performs an automatic maintenance update on a SQLInstance resource, reconciliation might fail with an error similar to the following:
    
    
    Update call failed: error updating: patching SQLInstance ... maintenanceVersion failed: googleapi: Error 400: Invalid request: The requested maintenance version is not an available maintenance version to upgrade. Please refer to the availableMaintenanceVersions on the instance resource to see the available maintenance versions.., invalid
    

#### Cause

The resource has the `cnrm.cloud.google.com/state-into-spec: merge` annotation. This annotation was the default for resources created before Config Connector version 1.123.1 for CustomResourceDefinitions (CRDs) added in version 1.113.0 and earlier. Your resource might also have this annotation if the `spec.stateIntoSpec` field is set to `Merge` in your ConfigConnector or ConfigConnectorContext custom resource (CR).

When the `cnrm.cloud.google.com/state-into-spec` annotation is set to `merge`, Config Connector populates unspecified fields, such as the `spec.maintenanceVersion` field, into the Kubernetes resource `spec` field during initial reconciliation. When Google Cloud later automatically updates that field on the underlying resource, Config Connector treats the older value stored in the `spec` field as the target state and attempts to revert the change. If the Google Cloud API rejects downgrades (as Cloud SQL does for the `spec.maintenanceVersion` field), reconciliation fails.

#### Resolution

To resolve this issue, migrate the resource from the `Merge` behavior to the `Absent` behavior so that Config Connector stops populating unspecified fields into the `spec` field:

  1. In your resource YAML manifest, omit the automatically updated field (such as the `spec.maintenanceVersion` field) and set the `cnrm.cloud.google.com/state-into-spec` annotation to `absent`.
  2. Follow the steps in [Migrate resources from `Merge` to `Absent`](https://docs.cloud.google.com/config-connector/docs/concepts/ignore-unspecified-fields#migrate-from-merge-to-absent) to abandon the Kubernetes resource and re-acquire it with the updated YAML manifest.



### Resource has no status

#### Symptom

Your resources don't have a `status` field.

#### Cause

It is likely that Config Connector is not running properly.

#### Resolution

Check that Config Connector is running.

### KNV2005: syncer excessively updating resource

#### Symptom

You use [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview) and are seeing [KNV2005 errors](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/errors#knv2005) for Config Connector resources, similar to the following:
    
    
    KNV2005: detected excessive object updates, approximately 6 times per
    minute. This may indicate Config Sync is fighting with another controller over
    the object.
    

#### Cause

It is likely that Config Sync and Config Connector are fighting over the resource.

Config Sync and Config Connector are said to be "fighting" over a resource if they keep updating the same field(s) to different values. One's update triggers the other to act and update the resource, which causes the other to act and update the resource, and this repeats without ending.

Fighting is not a problem for most fields. Fields that are specified in Config Sync are not changed by Config Connector. Similarly, fields that are not specified in Config Sync and defaulted by Config Connector are ignored by Config Sync. Therefore, for most fields, Config Sync and Config Connector shouldn't need to update the same field.

One exception is list fields. Similar to how Config Connector may default subfields in object fields, Config Connector may also default subfields in objects inside lists. However, since list fields in Config Connector resources are atomic, the defaulting of subfields is considered as changing the value of the list entirely.

Therefore, Config Sync and Config Connector will "fight" over a resource if Config Sync sets a list field and Config Connector defaults any subfields within that list.

#### Resolution

To work around this issue, you have the following options:

  1. Update the resource manifest in the Config Sync repository to match what Config Connector is trying to set the resource to.

One way to do this is to temporarily [stop syncing configs](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/stopping-resuming-syncing), wait for Config Connector to finish reconciling the resource, and then update your resource manifest to match the resource on the Kubernetes API Server.

  2. Stop Config Sync from reacting to updates to the resource on the Kubernetes API Server by setting the annotation `client.lifecycle.config.k8s.io/mutation` to `ignore`. Read more about [how to have Config Sync ignore object mutations](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/configs#ignoring).

  3. Stop Config Connector from updating the resource's spec entirely by setting the annotation `cnrm.cloud.google.com/state-into-spec` to `absent` on the resource. This annotation is not supported for all resources. To see if your resource supports the annotation, check the corresponding [resource reference page](https://docs.cloud.google.com/config-connector/docs/reference/resources). [Read more about the annotation](https://docs.cloud.google.com/config-connector/docs/concepts/managing-fields-externally#behavior_for_list_fields_in_resource_spec).




### Resource deleted by Config Connector

#### Symptom

A resource was deleted from your cluster, and you suspect Config Connector deleted it.

#### Cause

Config Connector never deletes your resources without an external cause. For example, running `kubectl delete`, using config management tools like Argo CD, or using a customized API client can cause resource deletion.

A common misconception is that Config Connector has initiated and deleted some of the resources in your cluster. For example, if you are using Config Connector, you may notice delete requests from Config Connector controller manager against certain resources from either container log messages or Kubernetes cluster audit logs. These delete requests are a result of external triggers and Config Connector is trying to reconcile the delete requests.

#### Resolution

To determine why a resource was deleted, you need to look into the first delete request that was sent to the corresponding resource. The best way to look into this is by examining the Kubernetes cluster audit logs.

As an example, if you are using GKE, you can [use Cloud Logging to query](https://docs.cloud.google.com/logging/docs/view/building-queries) for GKE cluster audit logs. For example, if you want to look for the initial delete requests for a BigQueryDataset resource named `my-dataset` in the `my-namespace` namespace, run a query like the following:
    
    
    resource.type="k8s_cluster"
    resource.labels.project_id="my-project-id"
    resource.labels.cluster_name="my-cluster-name"
    protoPayload.methodName="com.google.cloud.cnrm.bigquery.v1beta1.bigquerydatasets.delete"
    protoPayload.resourceName="bigquery.cnrm.cloud.google.com/v1beta1/namespaces/my-namespace/bigquerydatasets/my-dataset"
    

Using this query, you would look for the first delete request and then check `authenticationInfo.principalEmail` of that delete log message to determine the cause of the deletion.

### Controller Pod OOMKilled

#### Symptom

You see an OOMKilled error on a Config Connector controller Pod. The Pod's status may appear as `OOMKilled` or `Terminating`.

#### Cause

A container or the entire Pod was terminated because they used more memory than allowed. This can be verified by running the [kubectl describe](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe) command:
    
    
    kubectl describe pod POD_NAME -n cnrm-system
    

Replace `POD_NAME` with the Pod you are troubleshooting.

Additionally, scrutinizing the Pod's event logs can reveal any occurrences of OOM-related events.

#### Resolution

To address this issue, you can [use the ControllerResource](https://docs.cloud.google.com/config-connector/docs/how-to/customizing-container-resources) custom resource to increase the memory request and the memory limit for the Pod.

## Deletion

The following section lists common issues related to user-initiated delete operations that can cause conflicts with Config Connector.

### Namespace deletion stuck at "Terminating"

#### Symptom

Deleting a namespace is stuck at the `Terminating` stage.

#### Cause

This issue can happen if you have Config Connector installed in [namespaced-mode](https://docs.cloud.google.com/config-connector/docs/how-to/install-namespaced) and if the namespace's `ConfigConnectorContext` was deleted before all Config Connector resources in that namespace are deleted. When a namespace's `ConfigConnectorContext` is deleted, Config Connector is disabled for that namespace, which prevents any remaining Config Connector resources in that namespace from getting deleted.

#### Resolution

To fix this issue, you must do a forced cleanup and then manually delete the underlying Google Cloud resources afterwards.

To mitigate this issue in the future, only delete the `ConfigConnectorContext` after all Config Connector resources in its namespace have been deleted from Kubernetes. Avoid deleting entire namespaces before all Config Connector resources in that namespace have been deleted since the `ConfigConnectorContext` might get deleted first.

### Resource deletion stuck at "DeleteFailed" after project was deleted

#### Symptom

Deleting a Config Connector resource fails with the `DeleteFailed` status.

#### Cause

This issue can happen if a Google Cloud project is deleted before the resource.

#### Resolution

To fix this issue, [restore the project on Google Cloud](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#restoring_a_project) to allow Config Connector to delete the remaining child resources from Kubernetes. Alternatively, you can do a forced cleanup.

To mitigate this issue in the future, only delete Google Cloud projects after all their child Config Connector resources have been deleted from Kubernetes. Avoid deleting entire namespaces that might contain both a `Project` resource and its child Config Connector resources since the `Project` resource might get deleted first.

## Permissions and authentication

The following section lists common issues related to permissions and authentication.

### Compute Engine metadata not defined

#### Symptom

Your Config Connector resource has an `UpdateFailed` status with a message stating that the Compute Engine metadata is not defined, similar to the following error:
    
    
    Update call failed: error fetching live state: error reading underlying
    resource: summary: Error when reading or editing SpannerInstance
    "my-project/my-spanner- instance": Get
    "https://spanner.googleapis.com/v1/projects/my-project/instances/my-spanner-instance?alt=json":
    metadata: Compute Engine metadata "instance/service-accounts/default/token?
    scopes=https%!A(MISSING)%!F(MISSING)%!F(MISSING)www.googleapis.com%!F(MISSING)auth%!F(MISSING)compute%!C(MISSING)https%!A(MISSING)%!F(MISSING)%!F(MISSING)www.googleapis.com%!F(MISSIN
    G)auth%!F(MISSING)cloud-platform%!C(MISSING)https%!A(MISSING)%!F(MISSING)%!F(MISSING)www.googleapis.com%!F(MISSING)auth%!F(MISSING)cloud-identity%!C(MISSING)https%!A(MISSING)%!F(MISS
    ING)%!F(MISSING)www.googleapis.com%!F(MISSING)auth%!F(MISSING)ndev.clouddns.readwrite%!C(MISSING)https%!A(MISSING)%!F(MISSING)%!F(MISSING)www.googleapis.com%!F(MISSING)auth%!F(MISSIN
    G)devstorage.full_control%!C(MISSING)https%!A(MISSING)%!F(MISSING)%!F(MISSING)www.googleapis.com%!F(MISSING)auth%!F(MISSING)userinfo.email%!C(MISSING)https%!A(MISSING)%!F(MISSING)%!F
    (MISSING)www.googleapis.com%!F(MISSING)auth%!F(MISSING)drive.readonly" not
    defined, detail:
    

#### Cause

It is likely that the IAM service account used by Config Connector does not exist.

#### Resolution

To fix the issue, ensure that the IAM service account used by Config Connector exists.

To mitigate this issue in the future, ensure that you follow the [Config Connector installation instructions](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall).

### Error 403: Request had insufficient authentication scopes

#### Symptom

Your Config Connector resource has an `UpdateFailed` status with a message indicating a 403 error due to insufficient authentication scopes, similar to the following error:
    
    
    Update call failed: error fetching live state: error reading underlying
    resource: summary: Error when reading or editing SpannerInstance
    "my-project/my-spanner-instance": googleapi: Error 403: Request had
    insufficient authentication scopes.
    

#### Cause

[Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) is likely not enabled on your GKE cluster.

To confirm that Workload Identity Federation for GKE is not enabled, complete the following steps:

  1. Save the following Pod configuration as `wi-test.yaml`:
         
         apiVersion: v1
         kind: Pod
         metadata:
           name: workload-identity-test
           namespace: cnrm-system
         spec:
           containers:
           - image: google/cloud-sdk:slim
             name: workload-identity-test
             command: ["sleep","infinity"]
           serviceAccountName: cnrm-controller-manager
         

If you installed Config Connector using [namespaced mode](https://docs.cloud.google.com/config-connector/docs/how-to/install-namespaced), `serviceAccountName` should be `cnrm-controller-manager-NAMESPACE`. Replace `NAMESPACE` with namespace you used during the installation.

  2. Create the Pod in your GKE cluster:
         
         kubectl apply -f wi-test.yaml
         

  3. Open an interactive session in the Pod:
         
         kubectl exec -it workload-identity-test \
             --namespace cnrm-system \
             -- /bin/bash
         

  4. List your identity:
         
         gcloud auth list
         

  5. Verify that the identity listed matches the Google service account bound to your resources.

If you see the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) instead, then that means that Workload Identity Federation for GKE is not enabled on your GKE cluster and/or node pool.

  6. Exit the interactive session, then delete the Pod from your GKE cluster:
         
         kubectl delete pod workload-identity-test \
             --namespace cnrm-system
         




#### Resolution

To fix this issue, ensure that Workload Identity Federation for GKE is enabled on your cluster.

If you're still seeing the same error, ensure that you have also [enabled Workload Identity Federation for GKE on the cluster's node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#migrate_applications_to).

### 403 Forbidden: The caller does not have permission

#### Symptom

Your Config Connector resource has an `UpdateFailed` status with a message indicating a 403 error due to Workload Identity Federation for GKE, similar to the following error:
    
    
    Update call failed: error fetching live state: error reading underlying
    resource: summary: Error when reading or editing SpannerInstance
    "my-project/my-spanner- instance": Get
    "https://spanner.googleapis.com/v1/projects/my-project/instances/my-spanner-instance?alt=json":
    compute: Received 403 `Unable to generate access token; IAM returned 403
    Forbidden: The caller does not have permission
    This error could be caused by a missing IAM policy binding on the target IAM
    service account.
    For more information, refer to the Workload Identity documentation:
      https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#creating_a_relationship_between_ksas_and_gsas
    

#### Cause

Config Connector's Kubernetes service account is missing the appropriate IAM permissions to impersonate your IAM service account as a Workload Identity Federation for GKE user.

#### Resolution

To fix and mitigate the issue in the future, refer to the [Config Connector installation instructions](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall).

### Error 403: Caller is missing IAM permission

#### Symptom

Your Config Connector resource has an `UpdateFailed` status with a message stating that the caller is missing an IAM permission, similar to the following error:
    
    
    Update call failed: error fetching live state: error reading underlying
    resource: summary: Error when reading or editing SpannerInstance
    "my-project/my-spanner- instance": googleapi: Error 403: Caller is missing IAM
    permission spanner.instances.get on resource
    projects/my-project/instances/my-spanner-instance., detail:
    

#### Cause

The IAM service account used by Config Connector is missing the IAM permission stated in the message that is needed to manage the Google Cloud resource.

#### Resolution

If you're still seeing the same error after granting your IAM service account the appropriate IAM permissions, then check that your resource is being created in the correct project. Check the Config Connector resource's `spec.projectRef` field (or its `cnrm.cloud.google.com/project-id` annotation if the resource doesn't support a `spec.projectRef` field) and verify that the resource is referencing the correct project. Note that Config Connector uses the namespace's name as the project ID if neither the resource nor namespace specifies a target project. Read more about [how to configure the target project for project-scoped resources](https://docs.cloud.google.com/config-connector/docs/how-to/organizing-resources/project-scoped-resources).

If you're still seeing the same error, then check if Workload Identity Federation for GKE is enabled on your GKE cluster.

To mitigate this issue in the future, ensure that you follow the [Config Connector installation instructions](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall).

### Update error with IAMPolicy, IAMPartialPolicy and IAMPolicyMember

#### Symptom

You see an `UpdateFailed` status with an error message indicating a 400 error because the service account does not exist:
    
    
    Update call failed: error setting policy member: error applying changes: summary: Request `Create IAM Members roles/[MYROLE] serviceAccount:[NAME]@[PROJECT_ID].iam.gserviceaccount.com for project \"projects/[PROJECT_ID]\"` returned error: Error applying IAM policy for project \"projects/[PROJECT_ID]\": Error setting IAM policy for project \"projects/[PROJECT_ID]\": googleapi: Error 400: Service account [NAME]@[PROJECT_ID].iam.gserviceaccount.com does not exist., badRequest
    

#### Cause

If you delete an `IAMServiceAccount` Config Connector resource before cleaning up `IAMPolicy`,`IAMPartialPolicy`, and `IAMPolicyMember` resources that depend on that service account, Config Connector cannot locate the service account referenced in those IAM resources during reconciliation.

#### Resolution

To resolve this issue, check your service accounts and see if the required service account for those IAM resources is deleted. If the service account is deleted, clean up the related IAM Config Connector resources, too. For `IAMPolicyMember`, delete the whole resource. For `IAMPolicy` and `IAMParitialPolicy`, only remove the bindings that involve the deleted service account. However, such cleanup doesn't remove Google Cloud role bindings immediately. The Google Cloud role bindings are retained for 60 days because of the retention on the deleted service account. For more information, see the Google Cloud IAM documentation about [Delete a service account](https://docs.cloud.google.com/iam/docs/service-accounts-delete-undelete#deleting).

**Note:** If you encounter any problems during deletion, you might need to do a forced cleanup. If you want to delete the Google Cloud IAM bindings right away, you need to manually delete the underlying Google Cloud resources using `gcloud`.

To avoid this issue, you should always clean up `IAMPolicy`, `IAMPartialPolicy`, `IAMPolicyMember` Config Connector resources _before_ deleting the referenced `IAMServiceAccount`.

### `ServiceIdentity` resource fails with `Invalid service producer`

#### Symptom

Your `ServiceIdentity` resource has an `UpdateFailed` status, with an error message similar to the following:
    
    
    Update call failed: error applying desired state: summary: Error creating Service Identity: Invalid service producer: ...
    

#### Cause

This error means that the specified resource does not support on-demand service identity creation.

#### Resolution

The `ServiceIdentity` resource can generate service identities only for supported services. To verify if a service supports on-demand service identity creation before applying your configuration, run the following command:
    
    
    gcloud beta services identity create --service SERVICE_NAME.googleapis.com
    

Replace `SERVICE_NAME` with the name of the service, for example `spanner`.

If the command succeeds, Config Connector can create an identity for that service. If the command fails, it means Config Connector can't create an identity for that service.

## Installation and upgrades

The following section lists common issues related to installation or upgrading the version of Config Connector.

### Version not supported in Config Connector add-on installations

#### Symptom

If you can't enable the Config Connector add-on successfully, the following error message appears: `Node version 1.15.x-gke.x s unsupported`.

The error message also appears if [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) or [GKE Monitoring](https://docs.cloud.google.com/monitoring/kubernetes-engine/installing) are disabled.

#### Cause

The version of the GKE cluster doesn't meet the requirements or required features are disabled.

#### Resolution

To solve this error, verify that the version of the GKE cluster meets the version and feature requirements. Ensure that Workload Identity Federation for GKE and GKE Monitoring are enabled.

To get all valid versions for your clusters, run the following command:
    
    
    gcloud container get-server-config --format "yaml(validMasterVersions)" \
        --zone ZONE
    

Replace ZONE with the Compute Engine zone.

Pick a version from the list that meets the [requirements](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall#addon-requirements).

### `failed calling webhook`

#### Symptom

You cannot uninstall Config Connector and receive an error similar to the following:
    
    
    error during reconciliation: error building deployment objects: error finalizing the deletion of Config Connector system components deployed by ConfigConnector controller: error waiting for CRDs to be deleted: error deleting CRD accesscontextmanageraccesslevels.accesscontextmanager.cnrm.cloud.google.com: Internal error occurred: failed calling webhook "abandon-on-uninstall.cnrm.cloud.google.com": failed to call webhook: Post "https://abandon-on-uninstall.cnrm-system.svc:443/abandon-on-uninstall?timeout=3s": service "abandon-on-uninstall" not found
    

#### Cause

This issue can occur when using the Config Connector add-on and disabling Config Connector _before_ [removing the Config Connector CRDs](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall#uninstalling).

#### Resolution

To resolve this error, you must first manually delete the webhooks:
    
    
    kubectl delete validatingwebhookconfiguration abandon-on-uninstall.cnrm.cloud.google.com --ignore-not-found --wait=true
    kubectl delete validatingwebhookconfiguration validating-webhook.cnrm.cloud.google.com --ignore-not-found --wait=true
    kubectl delete mutatingwebhookconfiguration mutating-webhook.cnrm.cloud.google.com --ignore-not-found --wait=true
    

You can then proceed to uninstall Config Connector.

### `PodSecurityPolicy` prevents upgrades

#### Symptom

After [switching from the Config Connector add-on to a manual install](https://docs.cloud.google.com/config-connector/docs/how-to/install-manually#switch-add-on) and upgrading Config Connector to a new version, `cnrm` Pods fail to update.

#### Cause

The use of PodSecurityPolicies can prevent `cnrm` Pods from updating.

To confirm that the PodSecurityPolicies are preventing your upgrade, [check the `config-connector-operator`'s events](https://docs.cloud.google.com/config-connector/docs/troubleshooting#check_the_resources_status_and_events) and look for an error similar to the following:
    
    
    create Pod configconnector-operator-0 in StatefulSet configconnector-operator failed error: pods "configconnector-operator-0" is forbidden: PodSecurityPolicy: unable to admit pod: [pod.metadata.annotations[seccomp.security.alpha.kubernetes.io/pod]: Forbidden: seccomp may not be set pod.metadata.annotations[container.seccomp.security.alpha.kubernetes.io/manager]: Forbidden: seccomp may not be set]
    

#### Resolution

To resolve this issue, you must [specify the annotation on the PodSecurityPolicy](https://kubernetes.io/docs/reference/access-authn-authz/psp-to-pod-security-standards/#podsecuritypolicy-annotations) that corresponds to the annotation mentioned in the error. In the previous example, the annotation is `seccomp.security.alpha.kubernetes.io`.

## Configuration

The following section lists common issues relating to configuring resources.

### Cannot make changes to immutable fields

Config Connector rejects updates to immutable fields [at admission](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers/).

For example, updating an immutable field with `kubectl apply` causes the command to fail immediately.

This means that tools which continuously re-apply resources (for example, GitOps) might find themselves getting stuck while updating a resource if they don't handle admission errors.

Since Config Connector does not allow updates to immutable fields, the only way to perform such an update is to delete and re-create the resource.

#### Error updating the immutable fields when there is no update

You might see the following errors in the status of the Config Connector resource shortly after you create or acquire a Google Cloud resource using Config Connector:

  * `Update call failed: error applying desired state: infeasible update: ({true \<nil\>}) would require recreation` ([example](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/661))

  * `Update call failed: cannot make changes to immutable field(s)` ([example](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues/194))




This might not mean that you've actually updated the resource, but the reason might be that the Google Cloud API has made a change to an immutable field that was managed by you in the Config Connector resource. This caused the mismatch between the desired state and the live state of the immutable fields.

You can resolve the issue by updating the values of those immutable fields in the Config Connector resource to match the live state. To achieve it, you should complete the following steps:

  1. Update the YAML configuration of the Config Connector resource and set the `cnrm.cloud.google.com/deletion-policy` annotation to `abandon`.
  2. Apply the updated YAML configuration to update the Config Connector resource's deletion policy.
  3. [Abandon the Config Connector resource](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources#deleting_the_dataset).
  4. Print out the live state of the corresponding Google Cloud resource using gcloud CLI.
  5. Find the mismatch in between the gcloud CLI output and the YAML configuration of the Config Connector resource, and update those fields in the YAML configuration.
  6. Apply the updated YAML configuration to [acquire the abandoned resource](https://docs.cloud.google.com/config-connector/docs/how-to/managing-deleting-resources#acquiring_an_existing_resource).



### No matches for kind "RESOURCE_KIND"

#### Symptom

You see the error `No matches for kind "RESOURCE_KIND"`.

#### Cause

Your Kubernetes cluster doesn't have the CRD for the RESOURCE_KIND resource kind installed.

#### Resolution

Verify that the kind is a [resource kind supported by Config Connector](https://docs.cloud.google.com/config-connector/docs/reference/overview).

If the kind is supported, then that means your Config Connector installation is either out-of-date or invalid.

If you installed Config Connector using the GKE add-on, then your installation should be upgraded automatically. If you manually installed Config Connector, then you must [perform a manual upgrade](https://docs.cloud.google.com/config-connector/docs/how-to/install-manually#upgrading-config-connector).

Check the GitHub repository to determine which resource kinds are supported by which Config Connector versions (for example, [here are the kinds supported by Config Connector v1.44.0](https://github.com/GoogleCloudPlatform/k8s-config-connector/tree/v1.44.0/crds)).

### Labels are not propagated to the Google Cloud resource

#### Symptom

Labels in your YAML are not showing up on the Google Cloud resource.

#### Cause

Not all Google Cloud resources support labels.

#### Resolution

Config Connector propagates labels found in `metadata.labels` to the underlying Google Cloud resource. Check the resource's REST API documentation (for example, here is the [API documentation for PubSubTopic](https://docs.cloud.google.com/pubsub/docs/reference/rest/v1/projects.topics)) to see if they support labels.

### Error due to special characters in resource name

#### Symptom

You see an error related to invalid characters in `metadata.name`:
    
    
    a lowercase RFC 1123 subdomain must consist of lower case alphanumeric characters, '-' or '.', and must start and end with an alphanumeric character (e.g. 'example.com', regex used for validation is '[a-z0-9]([-a-z0-9]*[a-z0-9])?(\.[a-z0-9]([-a-z0-9]*[a-z0-9])?)*')
    

#### Cause

Special characters are not valid in the Kubernetes `metadata.name` field.

#### Resolution

If you'd like to give your resource a name that is not a valid Kubernetes name, but is a valid Google Cloud resource name, you can use the [resourceID](https://docs.cloud.google.com/config-connector/docs/how-to/managing-resources-with-resource-ids), field as shown in the following example:
    
    
    apiVersion: sql.cnrm.cloud.google.com/v1beta1
    kind: SQLUser
    metadata:
      name: 'test'
    spec:
      instanceRef:
        name: sqlinstance-sample-postgresql
      host: "%"
      type: CLOUD_IAM_USER
      resourceID: test.example@example-project.iam
    
    

This configuration causes Config Connector to use `resourceID` instead of `metadata.name` as the name of the resource.

### Unable to remove fields from resource spec

#### Symptom

Removing a field from a Config Connector resource's spec does not remove it from the resource.

#### Cause

Removing a field from the spec for a resource managed by Config Connector does not make that field empty or revert to a default value. Instead, it causes that field to become [externally-managed](https://docs.cloud.google.com/config-connector/docs/concepts/managing-fields-externally).

**Note:** There is one exception: fields inside lists. Lists are atomic, which means Config Connector will try to set the list in the underlying Google Cloud to be equivalent to the one specified in the spec.

#### Resolution

If you want to change value of a field to empty or default in the underlying Google Cloud resource, you must zero-out the field in the Config Connector resource spec:

  * For list type field, set the field to an empty list by using `[]`.

The following example shows the `targetServiceAccounts` field that we want to remove:
        
        spec:
          targetServiceAccounts:
            - external: "example-sa-1@example-project.iam.gserviceaccount.com"
            - external: "example-sa-2@example-project.iam.gserviceaccount.com"
        

To remove this field, set the value to empty:
        
        spec:
          targetServiceAccounts: []
        

  * For primitive type field, set the field to empty by using one of the following:

Type | Empty value  
---|---  
string | ""  
bool | "false"  
integer | 0  
  
The following example shows the `identityNamespace` field that we want to remove:
        
        spec:
          workloadIdentityConfig:
            identityNamespace: "example-project.svc.id.goog"
        

To remove this field, set the value to empty:
        
        spec:
          workloadIdentityConfig:
            identityNamespace: ""
        

  * For object type fields, you can try to set the subfields of the object type as empty or default following the guidance in the previous section and verify if it works. However, this is not guaranteed to work.




### Invalid value "merge" for `state-into-spec` annotation

This issue occurs when a resource uses the `cnrm.cloud.google.com/state-into-spec: merge` annotation, but the resource kind or Config Connector version rejects the `merge` value.

#### Symptom

Your Config Connector resource fails to reconcile with an error message similar to the following:
    
    
    Update call failed: error applying desired state: invalid value "merge" for "cnrm.cloud.google.com/state-into-spec" annotation
    

#### Cause

This error occurs for one of the following reasons:

  * The resource kind doesn't support the `Merge` behavior, but the resource has the `cnrm.cloud.google.com/state-into-spec: merge` annotation. This annotation might be set directly on the resource or inherited from the `spec.stateIntoSpec: Merge` setting in your ConfigConnector or ConfigConnectorContext CR. CRDs added in Config Connector version 1.114.0 and later support only the `Absent` behavior.
  * You upgraded to Config Connector version 1.134.0 or 1.134.1 and have an existing SQLInstance resource that had the `cnrm.cloud.google.com/state-into-spec: merge` annotation by default from an earlier version. Versions 1.134.0 and 1.134.1 had a [known issue that rejected the `merge` value on SQLInstance resources](https://docs.cloud.google.com/config-connector/docs/known-issues#sqlinstance-merge-error).



#### Resolution

To resolve this issue, complete the steps that apply to your scenario:

  * **Your resource kind doesn't support the`Merge` behavior**: set the `cnrm.cloud.google.com/state-into-spec: absent` annotation in your resource YAML manifest and set the `spec.stateIntoSpec` field to `Absent` in your ConfigConnector or ConfigConnectorContext CR. To verify whether your resource kind supports the `Merge` behavior, see [Kinds with `Merge` support](https://docs.cloud.google.com/config-connector/docs/concepts/ignore-unspecified-fields#crds_with_merge_support). If the annotation is already present on an existing resource in the cluster, follow the steps in [Migrate resources from `Merge` to `Absent`](https://docs.cloud.google.com/config-connector/docs/concepts/ignore-unspecified-fields#migrate-from-merge-to-absent).
  * **You use an existing SQLInstance resource in Config Connector version 1.134.0 or 1.134.1** : upgrade Config Connector to version 1.134.2 or later. Alternatively, migrate the SQLInstance resource to the `cnrm.cloud.google.com/state-into-spec: absent` annotation by following the steps in [Migrate resources from `Merge` to `Absent`](https://docs.cloud.google.com/config-connector/docs/concepts/ignore-unspecified-fields#migrate-from-merge-to-absent).



### Config Connector fails to start on Arm-based nodes

If your cluster contains node pools using the Arm architecture (such as the C4A, N4A, or Tau T2A machine series), Config Connector components might fail to run. This is a known limitation because Config Connector does not support Arm-based systems.

#### Symptoms

If your Config Connector instance is affected by this issue, you might experience the following symptoms:

  * Pods in the `cnrm-system` namespace remain in the `Pending` state.
  * Pods may show a `CrashLoopBackOff` with an error message in the logs similar to: `exec user process caused "exec format error"`.
  * Describing the Pod reveals scheduling failures or architecture mismatches.



#### Resolution

To resolve this issue, ensure that Config Connector components are scheduled on nodes with x86 architecture:

  * **Add an x86 node pool** : If your cluster only contains Arm nodes, add at least one node pool using an x86 machine type (such as `e2-standard-2`) to host the Config Connector controller Pods.
  * **Verify node taints** : GKE Arm nodes are typically tainted with `kubernetes.io/arch=arm64:NoSchedule` to prevent x86-only workloads from being scheduled on them. Ensure that you haven't added tolerations to the Config Connector deployments that would allow them to run on these nodes.



## Forced cleanup

If your Config Connector resources are stuck on deletion and you simply want to get rid of them from your Kubernetes cluster, you can force their deletion by deleting their [finalizers](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definitions/#finalizers).

**Warning:** This operation should be done as a last resort since deletions of finalizers is outside the bounds of normal usage for Config Connector and could have unintended consequences. In particular, there are no guarantees as to what happens to the underlying Google Cloud resources.

You can delete a resource's finalizers by editing the resource using `kubectl edit`, deleting the `metadata.finalizers` field, and then saving the file to preserve your changes to the Kubernetes API Server.

Since deleting a resource's finalizers allows the resource to be immediately deleted from the Kubernetes cluster, Config Connector _might_ (but not necessarily) not get a chance to complete the deletion of the underlying Google Cloud resource. This means that you might want to manually delete your Google Cloud resources afterwards.

## Monitoring

Monitoring Config Connector and exploring its logs can help you determine the soruce of issues and better understand unexpected behavior.

### Metrics

[You can use Prometheus to collect and show metrics from Config Connector](https://docs.cloud.google.com/config-connector/docs/how-to/monitoring-prometheus).

### Logging

All Config Connector Pods output structured logs in JSON format.

The logs of the controller Pods are particularly useful for debugging issues with the reconciliation of resources.

You can query for logs for specific resources by filtering for the following fields in the log messages:

  * `logger`: contains the resource's kind **in lower-case**. For example, `PubSubTopic` resources have a `logger` of `pubsubtopic-controller`.
  * `resource.namespace`: contains the resource's namespace.
  * `resource.name`: contains the resource's name.



#### Using Logging for advanced log querying

If you are using GKE, you can [use Cloud Logging to query for logs](https://docs.cloud.google.com/logging/docs/view/building-queries) for a specific resource with the following query:

**Note:** The querying syntax doesn't support comments. The following query uses a commenting convention, # comment, to provide explanatory text, but these comments cannot be included in queries.
    
    
    # Filter to include only logs coming from the controller Pods
    resource.type="k8s_container"
    resource.labels.container_name="manager"
    resource.labels.namespace_name="cnrm-system"
    labels.k8s-pod/cnrm_cloud_google_com/component="cnrm-controller-manager"
    
    # Filter to include only logs coming from a particular GKE cluster
    resource.labels.cluster_name="GKE_CLUSTER_NAME"
    resource.labels.location="GKE_CLUSTER_LOCATION"
    
    # Filter to include only logs for a particular Config Connector resource
    jsonPayload.logger="RESOURCE_KIND-controller"
    jsonPayload.resource.namespace="RESOURCE_NAMESPACE"
    jsonPayload.resource.name="RESOURCE_NAME"
    

Replace the following:

  * `GKE_CLUSTER_NAME` with the name of the GKE cluster running Config Connector
  * `GKE_CLUSTER_LOCATION` with the location of the GKE cluster running Config Connector. For example, `us-central1`.
  * `RESOURCE_KIND` with the resource's kind **in lower-case**. For example, `pubsubtopic`.
  * `RESOURCE_NAMESPACE` with the resource's namespace.
  * `RESOURCE_NAME` with the resource's name.



## Additional help

To get additional help, you can [file an issue on GitHub](https://github.com/GoogleCloudPlatform/k8s-config-connector/issues) or contact [Google Cloud Support](https://cloud.google.com/support-hub).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
