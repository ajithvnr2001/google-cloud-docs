---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/namespace-scoped-objects/
title: Sync objects to multiple namespaces \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:23.480819+00:00
---

# Sync objects to multiple namespaces  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/namespace-scoped-objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Sync objects to multiple namespaces Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use Config Sync to manage namespaces and choose which objects Config Sync syncs to your namespaces.

Kubernetes resource objects can either be cluster-scoped or namespace-scoped, depending on the resource type. You select the cluster by configuring your client to talk to a specific cluster. You select the namespace by configuring the `metadata.namespace` field in the object manifest. Config Sync adds additional capabilities: cluster selectors and namespace selectors, which let you further refine which objects are synced.

Before reading this page, you should already be familiar with the following Kubernetes concepts:

  * [Namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/)
  * [Labels and selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/)



## About scoping objects with Config Sync

By default, when you install Config Sync on a cluster or as a fleet default, Config Sync syncs _all_ of the Kubernetes objects in your source of truth to clusters with Config Sync installed or all clusters in a fleet. But, by _scoping_ objects to a cluster or namespace, you can control which objects are synced to a cluster or namespace.

Config Sync offers the following methods to scope your objects:

  * [Configure cluster-scoped objects with a cluster selector](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/cluster-scoped-objects)
  * [Configure cluster-scoped objects with fleet package labels](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-packages#use-labels) ([Preview](https://cloud.google.com/products#product-launch-stages))
  * Configure namespace-scoped objects with a namespace selector (this page)



## Use explicit namespaces

We recommend that you use explicit namespace declaration when configuring Config Sync because it lets you manage namespace metadata and delete namespaces later, if needed.

The default setting is `implicit`, but you can change the namespace strategy in your `RootSync` or `RepoSync` object by setting the `namespaceStrategy` field to `explicit`. For more information, see [namespace strategy](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/rootsync-reposync-fields#namespace-strategy).

## About namespace selectors

Namespace selectors are a feature of Config Sync that let you deploy otherwise identical resource objects into multiple namespaces.

Using namespace selectors is similar to using [Kubernetes label selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) to map a Service to a set of Pods, but with an extra layer of indirection. Because you can't add custom fields to existing resource types, you instead define your selector in a `NamespaceSelector` object. Then, you reference that selector by name in an annotation on the objects that you want to use that selector.

To use namespace selectors:

  1. Add or choose an existing label on the namespaces to which you want to deploy.
  2. Define a `NamespaceSelector` resource object in your source of truth. Config Sync does not sync `NamespaceSelector` objects to your cluster.
  3. For each object that you want to sync to one or more namespaces, modify the object's configuration to remove the `metadata.namespace` field and add the `configmanagement.gke.io/namespace-selector` annotation with a value that matches the `metadata.name` of your `NamespaceSelector`.



The examples in the subsequent section provide more details on how to define `NamespaceSelector` objects and annotate other objects to use the `NamespaceSelector`.

## Before you begin

  * [Install Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync).
  * Create, or have access to, a source of truth where you store your configuration files.
  * If you don't already have one or more namespaces, [create the namespaces that you want to scope your resources to](https://kubernetes.io/docs/tasks/administer-cluster/namespaces/#creating-a-new-namespace). You can create the namespace directly in your cluster or in your source of truth.



## Use namespace selectors

Namespace selectors are defined either with equality-based requirements or set-based requirements. You can combine multiple requirements.

### Equality-based label selector example

The following example shows how to use equality-based selectors to select which namespaces a configuration applies to:

  1. Add a label to one or more namespaces:
         
         kubectl label namespace NAMESPACE app=gamestore
         

Replace `NAMESPACE` with the name of your namespace.

Run this command for each namespace that you want to label.

  2. Create a namespace selector called `gamestore-selector`.
         
         kind: NamespaceSelector
         apiVersion: configmanagement.gke.io/v1
         metadata:
           name: gamestore-selector
         spec:
           selector:
             matchLabels:
               app: gamestore
         

If another object's configuration references this namespace selector, that configuration can only be applied to objects in namespaces that have the `app: gamestore` label.

  3. A namespace selector has no effect until you reference it in another configuration. Create an example object quota that references the namespace selector:
         
         kind: ResourceQuota
         apiVersion: v1
         metadata:
           name: quota
           annotations:
             configmanagement.gke.io/namespace-selector: gamestore-selector
         spec:
           hard:
             pods: "1"
             cpu: "200m"
             memory: "200Mi"
         

The resource quota is created only in namespaces that have the `app: gamestore` label.




### Set-based label selector example

The following example shows how to use set-based selectors to exempt namespaces from inheriting objects:

  1. Add a label to one or more namespaces:
         
         kubectl label namespace NAMESPACE quota-exempt=exempt
         

Replace `NAMESPACE` with the name of your namespace.

Run this command for each namespace that you want to label.

  2. Create a namespace selector called `exclude-exempt-namespaces`:
         
         kind: NamespaceSelector
         apiVersion: configmanagement.gke.io/v1
         metadata:
           name: excludes-exempt-namespaces
         spec:
           selector:
             matchExpressions:
               - key: quota-exempt
                 operator: NotIn
                   values:
                     - exempt
         

If another object's configuration references this namespace selector, that configuration is applied to all namespaces _except_ those with the `quota-exempt: exempt` key-value pair.

  3. A namespace selector has no effect until you reference it in another configuration. Create an example object quota that references the namespace selector:
         
         kind: ResourceQuota
         apiVersion: v1
         metadata:
           name: quota
           annotations:
             configmanagement.gke.io/namespace-selector: exclude-exempt-namespaces
         spec:
           hard:
             pods: "1"
             cpu: "200m"
             memory: "200Mi"
         

The resource quota is created in all namespaces except those that have the `quota-exempt: exempt` key-value pair.




## Integration with team scopes and fleet namespaces

Fleet namespaces created in Google Cloud automatically have the `fleet.gke.io/fleet-scope: your-scope` label. All namespaces also have the Kubernetes `kubernetes.io/metadata.name: your-namespace` label. You can use these default labels to set up a namespace selector for selecting fleet namespaces.

The [fleet tenancy tutorial](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-tenancy) explains in more detail how to use namespace selectors with fleets and team scopes to selectively manage objects for different teams.

## Namespace-scoped objects with hierarchical mode

Although unstructured repositories are recommended for most use cases, you can use namespace selectors to scope your objects with a hierarchical repository. The use of namespace selectors is the same, but there are additional limitations and requirements for how you organize your namespace configuration in your source of truth.

### Limitations

When you use a namespace selector configuration with a hierarchical repository, be aware of the following limitations and requirements:

  * You must store all configuration files for namespaces and namespace-scoped objects within the `namespaces/` directory of the [hierarchical repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/hierarchical-repo) and its descendant directories.
  * You must explicitly specify a namespace configuration in the `namespaces/NAMESPACE` subdirectory, where `NAMESPACE` matches the name of the namespace. All other namespace-scoped objects must be stored in the same subdirectory. If a namespace configuration is missing, Config Sync returns a KNV1044 error.
  * Resources that reference a namespace selector are applied to namespaces that inherit a given configuration from an abstract namespace, regardless of the directory structure of the `namespaces/` directory.



#### Namespace selector location

In a hierarchical repository, you can place a namespace selector configuration in any _abstract namespace_ directory, but not in a _namespace_ directory.

The following example repository architecture shows valid and invalid locations for namespace selectors:
    
    
    namespace-inheritance
    ...
    ├── namespaces
    │   ├── eng
    │   │   ├── gamestore
    │   │   │   ├── namespace.yaml
    │   │   │   └── ns_selector.yaml  # invalid
    │   │   └── ns_selector.yaml  # valid
    │   ├── ns_selector.yaml  # valid
    │   ├── rnd
    │   │   ├── incubator-1
    │   │   │   ├── namespace.yaml
    │   │   │   └── ns_selector.yaml  # invalid
    │   │   └── ns_selector.yaml  # valid
    

Because the `namespaces`, `eng`, and `rnd` directories represent abstract namespaces, you can put a selector in them. However, because the `gamestore` and `incubator-1` directories represent actual namespaces, you can't put a namespace selector in them.

### Configure an abstract namespace

With a hierarchical repository, you can optionally use abstract namespaces.

The following example shows how to move your namespace directory into an abstract namespace that contains additional configurations inherited by the namespace:

  1. In your repository, create an abstract namespace directory. The abstract namespace directory doesn't contain any configurations for namespaces, but the descendant namespace directories do contain configurations.

  2. In the abstract namespace directory that you created, create a configuration for a Role that grants `get` and `list` permissions on all objects in any namespace that eventually inherits the Role:
         
         apiVersion: rbac.authorization.k8s.io/v1
         kind: Role
         metadata:
           name: ROLE_NAME
         rules:
         - apiGroups: [""]
           resources: ["*"]
           verbs: ["get", "list"]
         

Replace `ROLE_NAME` with the name of the role.

  3. Create a configuration for a role binding that binds the role to an email group:
         
         kind: RoleBinding
         apiVersion: rbac.authorization.k8s.io/v1
         metadata:
           name: ROLE_NAME
         subjects:
         - kind: Group
           name: group@example.com
           apiGroup: rbac.authorization.k8s.io
         roleRef:
           kind: Role
           name:  ROLEBINDING_NAME
           apiGroup: rbac.authorization.k8s.io
         

Replace `ROLEBINDING_NAME` with the name of the Role.

  4. Move the namespace configuration that you created in the previous section from the `namespaces/` directory to the abstract namespace directory that you created in this section.




### Disable inheritance for objects

You can selectively disable inheritance for any configuration by setting the `hierarchyMode` field to `none`. HierarchyConfigs are stored in the `system/` directory of the repository. This example disables inheritance for role bindings:
    
    
    # system/hierarchy-config.yaml
    kind: HierarchyConfig
    apiVersion: configmanagement.gke.io/v1
    metadata:
      name: rbac
    spec:
      resources:
      # Configure role to only be allowed in leaf namespaces.
      - group: rbac.authorization.k8s.io
        kinds: [ "RoleBinding" ]
        hierarchyMode: none
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
