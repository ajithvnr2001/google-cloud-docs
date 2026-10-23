---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/troubleshooting/webhook/
title: Troubleshoot the admission webhook \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:39:19.688308+00:00
---

# Troubleshoot the admission webhook  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/troubleshooting/webhook/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Troubleshoot the admission webhook Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with the Config Sync admission webhook. To learn more about the webhook, see [Prevent config drift](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/prevent-config-drift).

## Troubleshoot KNV 2009 errors

The following sections help you resolve `KNV2009` errors.

### Admission webhook connection refused

If you have drift protection enabled, you might receive the following error when reconciler tries to apply a config to the cluster:
    
    
    KNV2009: Internal error occurred: failed calling webhook "v1.admission-webhook.configsync.gke.io": Post "https://admission-webhook.config-management-system.svc:8676/admission-webhook?timeout=3s": dial tcp 10.92.2.14:8676: connect: connection refused
    

This error means that the admission webhook isn't ready yet or has become unhealthy. It's usually a transient error that you might see when bootstrapping Config Sync.

If the issue persists, describe the admission webhook Deployment to see if its Pods can be scheduled and are healthy:
    
    
    kubectl describe deploy admission-webhook -n config-management-system
    
    kubectl get pods -n config-management-system -l app=admission-webhook
    

A Deployment with healthy Pods has output similar to the following:
    
    
    Replicas:               2 desired | 2 updated | 2 total | 2 available | 0 unavailable
    ...
    Conditions:
      Type           Status  Reason
      ----           ------  ------
      Available      True    MinimumReplicasAvailable
      Progressing    True    NewReplicaSetAvailable
    ...
    

### Admission webhook request I/O timeout

If you receive an error similar to the following when the reconciler tries to apply a config to the cluster, the admission webhook port `8676` might be blocked by the firewall to the control plane network:
    
    
    KNV2009: Internal error occurred: failed calling webhook "v1.admission-webhook.configsync.gke.io": Post https://admission-webhook.config-management-system.svc:8676/admission-webhook?timeout=3s: dial tcp 10.1.1.186:8676: i/o timeout
    

To resolve this issue, [add a firewall rule](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#step_3_add_a_firewall_rule) to allow port `8676`, which the Config Sync admission webhook uses for drift prevention. Port `8676` needs to be open from the control plane to the nodes because the control plane needs to be able to reach the webhook backend on the cluster nodes.

## Admission webhook denied a request

If you receive the following error when you try to apply a change to a field that Config Sync manages, then you might have made a conflicting change:
    
    
    error: OBJECT could not be patched: admission webhook "v1.admission-webhook.configsync.gke.io"
    denied the request: fields managed by Config Sync can not be modified
    

If you have drift protection enabled, when you declare a field in a config and your repository is synced to a cluster, Config Sync manages that field. Any change you attempt to make to that field is a conflicting change.

For example, if you have a Deployment config in your repository with a label of `environment:prod` and you try to change that label to `environment:dev` in your cluster, there would be a conflicting change and you would receive the preceding error message. However, if you add a new label (for example, `tier:frontend`) to the Deployment, there wouldn't be a conflict.

If you want Config Sync to ignore any changes to an object, you can add the annotation described in [Ignoring object mutations](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/configs#ignoring).

## Failed to delete all resource types

A namespace stuck in the `Terminating` phase has the following condition:
    
    
        message: 'Failed to delete all resource types, 1 remaining: admission webhook
          "v1.admission-webhook.configsync.gke.io" denied the request: system:serviceaccount:kube-system:namespace-controller
          is not authorized to delete managed resource "_configmap_bookstore_cm1"'
        reason: ContentDeletionFailed
        status: "True"
        type: NamespaceDeletionContentFailure
    

This error happens when you are trying to delete a `Namespace` object from a root repository, but some objects under the namespace are still actively managed by a namespace reconciler. When a namespace is deleted, the [namespace controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/#namespacelifecycle), whose service account is `system:serviceaccount:kube-system:namespace-controller`, would try to delete all the objects in that namespace. However, the [Config Sync admission webhook](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/prevent-config-drift) only allows the root or namespace reconciler to delete these objects, and denies the namespace controller to delete these objects.

To work around this issue, delete the Config Sync admission webhook:
    
    
    kubectl delete deployment.apps/admission-webhook -n config-management-system
    

The ConfigManagement Operator recreates the Config Sync admission webhook.

If this work around does not work, you might need to reinstall Config Sync.

To avoid running into the error again, [remove the namespace repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/multiple-repositories#remove) before removing the namespace.

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
