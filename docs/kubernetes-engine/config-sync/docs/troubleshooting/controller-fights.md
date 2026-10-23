---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/troubleshooting/controller-fights/
title: Troubleshoot controller fights \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:14.835133+00:00
---

# Troubleshoot controller fights  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/troubleshooting/controller-fights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Troubleshoot controller fights Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with controller fights. Such fights consume a high amount of resources and can degrade your performance. Controller fights are also known as _resource contention_.

Config Sync watches the objects it applies on the cluster and reverts changes made to the values declared in the source of truth. If these changes are made by another controller, the resource might switch back and forth between the states wanted by the competing controllers. One symptom of this behavior is that the `metadata.generation` and `metadata.resourceVersion` fields increase rapidly. Because of this, if a managed object is updated more than five times per minute, Config Sync detects the fight, logs the drift, and reports the error in the `RootSync` or `RepoSync` object status.

Config Sync has special logic to detect fights between multiple `RootSync` and `RepoSync` objects. For `RepoSync` objects, if the reconciler sees that the object is already managed by another reconciler, further updates are skipped. For `RootSync` objects, the reconciler attempts to adopt any object it's configured to manage, unless it's managed by another `RootSync` object. This prevents Config Sync reconcilers from fighting between themselves and reports errors in the status of all `RootSync` and `RepoSync` objects involved.

## Identify controller fights

You can review the fight errors by using the [`nomos status`](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command#status-install) command or by checking the status field in the `RootSync` or `RepoSync` object.

If you don't have the `nomos` command-line tool installed, you can review the logs for the `RootSync` reconciler by running the following command:
    
    
    kubectl logs -n config-management-system \
        --selector "app=reconciler,configsync.gke.io/sync-name=root-sync" \
        --container reconciler
    

To filter for specific `RepoSync` reconcilers, run the following command:
    
    
    kubectl logs -n config-management-system \
        --selector "app=reconciler,configsync.gke.io/sync-namespace=NAMESPACE" \
        --container reconciler
    

Replace `NAMESPACE` with the namespace that you created your namespace-scoped source of truth in.

If you see `KNV2005` in the results, then there is a controller fight.

The following error message is an example of the type of error you might see in your logs:
    
    
    KNV2005: detected excessive object updates, approximately 6 times per
    minute. This may indicate Config Sync is fighting with another controller over
    the object.
    

## Investigate controller fights

To find more information about any controller fight, watch updates to the resource's YAML file by running the following command:
    
    
     kubectl get RESOURCE OBJECT_NAME \
         --namespace NAMESPACE \
         --watch -o yaml
    

Replace the following:

  * `RESOURCE`: the kind of resource that's being fought over.
  * `OBJECT_NAME`: the name of the object that's being fought over.
  * `NAMESPACE`: the namespace that the resource being fought over is in.



The log results specify the resource, object name, and namespace you need to add.

This command returns a stream of the state of the resource after updates are applied to the API server. Use a file comparison tool to compare the output.

## Resolve controller fights

There are multiple ways to resolve controller fights. Choose the option that works best for your Config Sync setup:

  * Update the resource manifest in the source to match the value that the other controller wants.
  * Remove the field in question from the source to let the other controller to manage it.
  * Disable or uninstall the other controller.
  * Remove the resource from the source and manage it manually or with a custom controller that tolerates specific changes or co-management.
  * If you own the controller that is causing resource contention, and the field being changed is not in the source of truth, update your controller to perform patching instead of updating. That way the change will be allowed by Config Sync and not reverted.



There are also some resources that should belong to other controllers (for example, some [operators](https://kubernetes.io/docs/concepts/extend-kubernetes/operator/) install or maintain CRDs). These other controllers automatically remove any metadata specific to Config Sync. If another component in your Kubernetes cluster removes Config Sync metadata, stop managing the resource with Config Sync. For information about how to do this, see [Stop managing a managed object](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/managing-objects#stop-managing).

Alternatively, if you don't want Config Sync to revert changes to managed objects in the cluster, you can add the `client.lifecycle.config.k8s.io/mutation: ignore` annotation to the object that you want Config Sync to ignore mutations in. For information about how to do this, see [Ignore object mutations](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/configs#ignoring).

### Resolving controller fights for implicit namespaces

By default, Config Sync creates an implicit namespace when a RootSync manages a namespaced object but the namespace itself doesn't yet exist. If a different controller then tries to take ownership of the namespace, a controller fight with Config Sync might occur. You can confirm that a namespace was implicitly created if it was never declared in the root repository and the live namespace has the [prevent deletion annotation](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/managing-objects#prevent_deletion_for_kubernetes_objects).

There are multiple ways to resolve fights over an implicit namespace. Choose the option that works best for your Config Sync setup:

  * Use the [explicit namespace strategy on your RootSync object](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/namespace-scoped-objects#implicit_vs_explicit). This strategy resolves the controller fight and prevents Config Sync from creating additional implicit namespaces.
  * Add the Namespace to your root repository with the [management disabled annotation](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/managing-objects#stop-managing). This annotation tells Config Sync to stop managing the Namespace, but still allows Config Sync to create implicit namespaces.



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
