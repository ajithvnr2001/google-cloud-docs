---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/declare-resource-dependency/
title: Declare dependencies between resource objects \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:20:23.320752+00:00
---

# Declare dependencies between resource objects  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/declare-resource-dependency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Declare dependencies between resource objects Stay organized with collections  Save and categorize content based on your preferences. 

This guide teaches you how dependencies work in Config Sync and how to specify your own dependencies.

Config Sync automatically detects implicit dependencies between specific objects when syncing them to the cluster. For example, the Namespace objects are always applied before any objects in those Namespaces, and a CustomResourceDefinition (CRD) object is always applied before any custom resource of this type is applied. Likewise, deletion ordering is reverse for these implicit dependencies: Namespaces are deleted after objects in that namespace, and CRDs are deleted after Custom Resources of that type.

You can also set explicit dependencies by using the `depends-on` annotation. For example, you might want your MySQL StatefulSet to start up before your Wordpress Deployment, so that your database is applied and ready before Wordpress starts.

## Requirements

  * RootSync and RepoSync APIs need to be enabled. If you installed Config Sync manually using kubectl, and don't have RootSync and RepoSync APIs enabled, you need to [migrate your ConfigManagement object](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/migrate-multi-repo).

  * **Limitation:** Dependencies must be in the same source of truth as their dependent. Dependencies must be managed by the same RootSync or RepoSync object as their dependents, which ensures all resources are in the same ResourceGroup.




## Apply group

When syncing resources to the cluster, Config Sync divides resources that have direct or indirect dependencies into different apply groups. One apply group only consists of resources without direct or indirect dependencies on each others. The apply group in which resources do not have any dependencies will be applied first.

## Actuation and reconciliation

When an object is actuated (either applied or pruned), it can take a while for the object to be reconciled by its controller. For example, when a Deployment is applied, the underlying Pods might not be ready immediately. After the underlying Pods are ready, the Deployment is reconciled. For different types of objects, Config Sync checks different types of conditions to verify if an object is reconciled. More details can be found in [sigs.k8s.io/cli-utils](https://github.com/kubernetes-sigs/cli-utils/tree/master/pkg/kstatus)

With the `depends-on` annotation, Config Sync not only applies objects in the order that you want, it also verifies that the dependency object is reconciled before applying the dependent object.

If the dependecy object does not reconcile within the default reconcile timeout of 5 minutes, Config Sync will not apply the dependent object until next sync period. You can override the default reconcile timeout by setting [`spec.override.reconcileTimeout`](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields#reconcile-timeout).

## Add the `depends-on` annotation to an object

To specify a dependency, add the `config.kubernetes.io/depends-on` annotation on the dependent object with a value that references the dependency objects.

For the Wordpress example, the annotation in Wordpress Deployment resembles the following:
    
    
    # deployment.yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: wordpress
      namespace: default
      labels:
        app: wordpress
      annotations:
        config.kubernetes.io/depends-on: apps/namespaces/default/StatefulSet/wordpress-mysql
    

When Config Sync applies the objects, it first applies the dependency, the object `wordpress-mysql` StatefulSet. When the dependency has been reconciled, Config Sync applies the dependent, the `wordpress` Deployment.

## Object references

Object references use the following syntax:

  * For namespaced objects:
        
        GROUP/namespaces/NAMESPACE/KIND/NAME
        

  * For cluster-scoped objects:
        
        GROUP/KIND/NAME
        

Replace the following:

    * `GROUP`: The group of the dependency object.
    * `NAMESPACE`: The namespace of the namespace-scoped dependency object.
    * `KIND`: The kind of the dependency object. This field is case sensitive. For example, use "Pod" instead of "pod".
    * `NAME`: The name of the dependency object.



For objects in the core group, the empty string is used instead, for example `/namespaces/test/Pod/pod-a`.

Use `,` to separate multiple object references, for example `/namespaces/test/Pod/pod-a,/namespaces/test/Pod/pod-b`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
