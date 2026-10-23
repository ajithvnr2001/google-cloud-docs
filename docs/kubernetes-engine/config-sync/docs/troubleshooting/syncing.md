---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/troubleshooting/syncing/
title: Troubleshoot syncing configs to your cluster \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:38:59.572874+00:00
---

# Troubleshoot syncing configs to your cluster  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/troubleshooting/syncing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Troubleshoot syncing configs to your cluster Stay organized with collections  Save and categorize content based on your preferences. 

Resolving configuration synchronization issues in Config Sync helps ensure that your clusters stay aligned with your central source of truth. When synchronization fails, deployments can stall and cluster configurations can drift from their declared state. You can diagnose and fix common `KNV2009` syncing errors—such as missing role-based access control (RBAC) permissions, `ResourceGroup` objects exceeding `etcd` size limits, and webhook latency—to restore automated reconciliation.

## Troubleshoot KNV 2009 errors

`KNV2009` errors indicate that Config Sync failed to sync some configs to the cluster. The following sections explain some of the most common causes and how to resolve them.

### Operation on certain resources is forbidden

Because you need to grant `RepoSync` objects their RBAC, it might be missing the permissions needed to apply resources.

You can verify that the permissions are missing by getting the `RepoSync` resource status:
    
    
    kubectl get reposync repo-sync -n NAMESPACE -o yaml
    

Replace `NAMESPACE` with the namespace that you created your namespace repository in.

You can also use the [`nomos status`](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command#status-install) command.

If you see the following messages in the status, it means that the reconciler in `NAMESPACE` lacks the permission needed to apply the resource:
    
    
    KNV2009: deployments.apps "nginx-deployment" is forbidden: User "system:serviceaccount:config-management-system:ns-reconciler-default" cannot get resource "deployments" in API group "apps" in the namespace "default"
    

To fix this issue, you need to declare a RoleBinding configuration that grants the service account for the reconciler permission to manage the failed resource in that namespace. Details on how to add a RoleBinding are included in [Configure syncing from multiple repositories](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories).

This issue can also affect RootSync objects if you've used [`spec.override.roleRefs`](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields#role-refs) to change the roles granted to the `RootSync` object. If you haven't set this field, `RootSync` objects are granted the `cluster-admin` role by default.

### ResourceGroup object exceeds the `etcd` object size limit

If you receive the following error when a reconciler tries to apply configurations to the cluster, the ResourceGroup object exceeds the `etcd` object size limit:
    
    
    KNV2009: too many declared resources causing ResourceGroup.kpt.dev, config-management-system/root-sync failed to be applied: task failed (action: "Inventory", name: "inventory-add-0"): Request entity too large: limit is 3145728. To fix, split the resources into multiple repositories.
    

We recommend that you [split your Git repository into multiple repositories](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/breaking-up-repo). If you're not able to break up the Git repository, because the object is already too big and changes are not being persisted, you can mitigate it by configuring the `RootSync` or `RepoSync` to temporarily disable writing object status to the ResourceGroup. You can do this by setting the `.spec.override.statusMode` field of the `RootSync` or RepoSync object to `disabled`. By doing so, Config Sync stops updating the managed resources status in the ResourceGroup object. This action reduces the size of the ResourceGroup object. However, you cannot view the status for managed resources from `nomos status`.

If you don't see any error from the `RootSync` or `RepoSync` object, then the objects from your source of truth have been synced to the cluster. To check if the ResourceGroup resource exceeds the `etcd` object size limit, check both the ResourceGroup resource status and the log of the ResourceGroup Controller:

  1. Check the ResourceGroup status:

     * To check the `RootSync` object, run the following command:
           
           kubectl get resourcegroup root-sync -n config-management-system
           

     * To check the `RepoSync` object, run the following command:
           
           kubectl get resourcegroup repo-sync -n NAMESPACE
           

Replace `NAMESPACE` with the namespace that you created your namespace repository in.

The output is similar to the following example:
    
    NAME        RECONCILING   STALLED   AGE
    root-sync   True          False     35m
    

If the value in the `RECONCILING` column is `True`, it means that the ResourceGroup resource is still reconciling.

  2. Check the logs for the ResourceGroup Controller:
         
         kubectl logs deployment resource-group-controller-manager -c manager -n resource-group-system
         

If you see an error similar to the following example in the output, the ResourceGroup resource is too large and exceeds the `etcd` object size limit:
         
         "error":"etcdserver: request is too large"
         




To prevent the ResourceGroup from getting too large, reduce the number of resources in your Git repository. You can [split one root repository into multiple root repositories](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/breaking-up-repo).

### Dependency apply reconcile timeout

If you were syncing objects with dependencies, you might receive an error similar to the following example when the reconciler tries to apply objects with the `config.kubernetes.io/depends-on` annotation to the cluster:
    
    
    KNV2009: skipped apply of Pod, bookstore/pod4: dependency apply reconcile timeout: bookstore_pod3__Pod  For more information, see https://g.co/cloud/acm-errors#knv2009
    

This error means the dependency object did not reconcile within the default reconcile timeout of five minutes. Config Sync cannot apply the dependent object because with the `config.kubernetes.io/depends-on` annotation, Config Sync only applies objects in the order you want. You can override the default reconcile timeout to a longer time by setting [`spec.override.reconcileTimeout`](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields#reconcile-timeout).

It's also possible that the dependency might reconcile after the initial sync attempt has completed. In this case, the dependency should be detected as reconciled on the next sync retry attempt, unblocking the apply of any dependents. When this happens, the error may be reported briefly and then removed. Lengthening the reconcile timeout might help avoid the error being reported intermittently.

### Inventory info is nil

If you receive the following error when reconciler tries to apply configurations to the cluster, it's likely that your inventory has no resources or the manifest has an [unmanaged annotation](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/managing-objects):
    
    
    KNV2009: inventory info is nil\n\nFor more information, see https://g.co/cloud/acm-errors#knv2009
    

To resolve this issue, try the following steps:

  1. Avoid setting up syncs where all resources have the `configmanagement.gke.io/managed: disabled` annotation, by ensuring at least one resource is managed by Config Sync.
  2. Add the annotation `configmanagement.gke.io/managed: disabled` only after completing an initial sync of the resource without this annotation.



### Multiple inventory object templates

If you receive the following error when the reconciler tries to apply configurations to the cluster, it is likely that you have an inventory config generated by kpt in the source of truth, for example a Git repository:
    
    
    KNV2009: Package has multiple inventory object templates.  The package should have one and only one inventory object template.   For more information, see https://g.co/cloud/acm-errors#knv2009
    

The issue happens because Config Sync manages its own inventory config. To resolve this issue, delete the inventory config in your source of truth.

### Cannot make changes to immutable fields

You can't change any immutable field in a config by changing the value in the source of truth. Attempting such a change causes an error similar to the following:
    
    
    KNV2009: failed to apply RESOURCE: admission webhook "deny-immutable-field-updates.cnrm.cloud.google.com" denied the request: cannot make changes to immutable field(s):
    

If you need to change an immutable field, delete the object from your source of truth, wait for Config Sync to delete the object from the cluster, and then re-create the object in your source of truth with your updates.

### Polling for status failed

You can authorize Config Sync to manage resources in a namespace using a `RepoSync` object. If this type of `RepoSync` object uses a `RoleBinding` object that references a custom `ClusterRole` or `Role`, you might get the following error message from the Reconciler Deployment:
    
    
    KNV2009: polling for status failed: unknown
    

To resolve this issue, make sure your `ClusterRole` and `Role` objects have at least the following permissions for each resource that the `RepoSync` object manages:

  * `list`
  * `watch`
  * `get`
  * `patch`
  * `delete`
  * `create`



For instructions on adding these permissions, see [Create a RoleBinding](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories#rolebinding).

## API discovery failed

If you see an error message similar to the following, you might be experiencing an API discovery error:
    
    
    KNV2002: API discovery failed: APIServer error: unable to retrieve the complete list of server APIs: external.metrics.k8s.io/v1beta1: received empty response for: external.metrics.k8s.io/v1beta1
    

Config Sync uses [Kubernetes API discovery](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#api-discovery) to look up which resources are supported by the cluster. This lets Config Sync validate the resource types specified in your source and watch those resources for changes in the cluster.

Prior to Kubernetes version 1.28, any time any APIService backend was unhealthy or returned an empty list result, API Discovery would fail, causing Config Sync and multiple other Kubernetes components to error. Many common APIService backends are not highly available, so this can happen relatively frequently, just by updating the backend or having it be rescheduled onto another node.

Examples of APIService backends with a single replica include `metrics-server` and `custom-metrics-stackdriver-adapter`. Some APIService backends always return empty list results, like `custom-metrics-stackdriver-adapter`. Another common cause of API discovery failure is unhealthy webhooks.

After Kubernetes version 1.28, with the Aggregated Discovery feature enabled, an unhealthy APIService backend no longer causes unhandled errors. Instead the resource group handled by that APIService is shown to have no resources. This lets syncing continue, as long as the unhealthy resource isn't specified in your source.

**Note:** Aggregated Discovery was added as a beta feature in Kubernetes version 1.27.0, but had a bug causing it to be disabled in GKE version 1.27.4-gke.1600. It was re-enabled in GKE version 1.28.0 with a fix.

## Delayed self-healing

Self-healing watches managed resources, detects drift from the source of truth, and reverts that drift.

Self-healing is paused while syncing is being attempted. This behavior means that self-healing might be delayed, especially if there are sync errors preventing the reconciler from completing. To re-enable self-healing, fix all reported sync errors.

## High number of Kubernetes API requests

Config Sync uses a multi-instancing strategy to scale and isolate tenants and fault domains. Because of this, each `RootSync` and `RepoSync` gets its own reconciler instance. In addition to syncing every time changes are made to the source, each reconciler instance also syncs periodically as part of its self-healing behavior, to revert any changes missed by the active drift remediation. When you add `RootSync` or `RepoSync` objects, this causes a linear increase in the number of API requests made by the reconcilers syncing resources to Kubernetes. So if you have many `RootSync` and `RepoSync` objects, this can sometimes cause significant traffic load on the Kubernetes API.

To perform syncing, Config Sync uses [Server-Side Apply](https://kubernetes.io/docs/reference/using-api/server-side-apply/). This replaces the normal GET and PATCH request flow with a single PATCH request, reducing the total number of API calls, but increasing the number of PATCH calls. This ensures that the changes made are correct, even when the resource group version in source doesn't match the default resource group version on the cluster. However, you may see PATCH requests in the audit log, even when there hasn't been any change to the source or drift from the state that you want. This is normal, but can be surprising.

When syncing is erroring, it is retried until it succeeds. However, if this requires human interaction, Config Sync might be erroring and retrying for a while, increasing the amount of requests made to the Kubernetes API. The retries back off exponentially, but if many `RootSync` or `RepoSync` objects are failing to sync simultaneously, this can cause significant traffic load on the Kubernetes API.

To mitigate these issues, try one of the following options:

  * Fix configuration errors quickly, so they don't pile up.
  * Combine multiple `RootSync` or `RepoSync` objects, to reduce the number of reconcilers making Kubernetes API requests.



## KubeVirt uninstall blocked by finalizers

KubeVirt is a Kubernetes package that uses multiple finalizers, requiring precise deletion ordering to facilitate cleanup. If the KubeVirt objects are deleted in the wrong order, deletion of other KubeVirt objects might stall or stop responding indefinitely.

If you tried to uninstall KubeVirt and it became blocked, follow the instructions for manually [deleting KubeVirt](https://kubevirt.io/user-guide/operations/updating_and_deletion/#deleting-kubevirt).

To mitigate this issue in the future, [declare dependencies between resource objects](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/declare-resource-dependency) to ensure they are deleted in reverse dependency order.

## Object deletion blocked by finalizers

[Kubernetes finalizers](https://kubernetes.io/docs/concepts/overview/working-with-objects/finalizers/) are metadata entries that tell Kubernetes not to allow an object to be removed until after a specific controller has performed cleanup. This can cause syncing or reconciling to fail, if the conditions for cleanup are not satisfied or the controller that performs the cleanup for that resource is unhealthy or has been deleted.

To mitigate this problem, identify which resource is still finalizing and which controller should be performing the cleanup.

If the controller is unhealthy, fixing the root cause should allow the resource cleanup to complete, unblocking removal of the object.

If the controller is healthy, the controller should have applied a status condition to the object being deleted to explain why cleanup has stalled. If not, check the controller logs for indications of the root cause.

Often, having an object stuck deleting is an indication that objects were deleted in the wrong order. To prevent this kind of problem in the future, [declare dependencies between resource objects](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/declare-resource-dependency), to ensure they are deleted in reverse dependency order.

## ResourceGroup fields keep changing

When syncing is attempted, the inventory is updated to change resource status to pending. When syncing fails, the inventory is updated to change resource status to failed. When syncing is retried after failure, this pattern repeats, causing periodic updates to the inventory. This causes the ResourceGroup `resourceVersion` to increase with each update and the syncing status to flip back and forth. This is normal, but can be surprising.

Sync failure can be caused by a number of issues. One of the most common is insufficient permissions to manage the resources specified in the source. To fix this error, add the appropriate RoleBindings or ClusterRoleBinding to grant the `RepoSync` or `RootSync` reconciler permission to manage the resources that are failing to sync.

## Config Sync doesn't remove or revert fields not specified in the source

Config Sync uses [Server-Side Apply](https://kubernetes.io/docs/reference/using-api/server-side-apply/) to apply manifests from the source to Kubernetes. This is required to allow other controllers to manage `metadata` and `spec` fields. One example of this is the Horizontal Pod Autoscaler, which updates the number of replicas in a Deployment. Because of this, Config Sync only manages fields specified in the source manifest. This has the side effect that when adopting existing resource objects, any fields unspecified in the source aren't changed, which can sometimes cause the merged configuration to be invalid or incorrect.

To avoid this problem when adopting a resource, use the exact same fields in the source when initially adopting and then change the fields in the source after syncing, so that Config Sync correctly removes the fields it previously applied and replaces them with the new fields from the source. Another way to avoid this problem is to delete the resource from the cluster first and allow Config Sync to apply the new version.

## Config Sync doesn't retain fields from `kubectl` client-side apply when adopting objects

Because Config Sync uses Server-Side Apply, when Config Sync adopts an object that was originally created with `kubectl` client-side apply, it unsets any fields which were set with client-side apply but not declared in the source.

If you want those fields to be retained, use the exact same fields in the source when you initially adopt the object, or create the object using [Server-Side Apply](https://kubernetes.io/docs/reference/using-api/server-side-apply/).

## What's next

  * If you're still experiencing issues, check to see if your problem is a [known issue](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/known-issues).



If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/get-support-config-sync) for further help, including advice on the following topics: 

  * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
  * Getting support from the community by [asking questions on Stack Overflow](http://stackoverflow.com/questions). If you use kpt or Kustomize, use the `kpt` or `kustomize` tag to search for similar issues.
  * Opening bugs or feature requests by using the [public issue tracker](https://github.com/GoogleContainerTools/config-sync/issues) on GitHub.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
