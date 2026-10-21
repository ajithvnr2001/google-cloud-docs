---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/cluster-scoped-objects/
title: Configure clusters and cluster-scoped objects \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:21:17.127797+00:00
---

# Configure clusters and cluster-scoped objects  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/cluster-scoped-objects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Configure clusters and cluster-scoped objects Stay organized with collections  Save and categorize content based on your preferences. 

Config Sync lets you declaratively manage cluster-scoped objects—such as Namespace, ClusterRole, and CustomResourceDefinition resources—across your Kubernetes clusters from a central source of truth. Synchronizing cluster-scoped configurations helps you enforce consistent cluster-wide policies, role-based access controls (RBAC), and custom APIs across your fleet. You can also target specific clusters by using selectors. To manage resources within individual namespaces instead, see [Sync objects to multiple namespaces](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/namespace-scoped-objects).

## Configure clusters and cluster-scoped objects

In [unstructured](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/unstructured-repo) repositories, you can organize configs for clusters and cluster-scoped objects in the way that's most convenient for you. All configs organized this way apply to every cluster enrolled in Config Sync.

## Configure CustomResourceDefinitions

Config Sync lets you sync [CustomResourceDefinitions (CRDs)](https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/) the same way you would sync any other resource. There are a few things to keep in mind when syncing CRDs:

  * Updates to CRDs and their corresponding CustomResources do not occur in any predictable order. If you modify CRDs and the corresponding CustomResources in the same commit, there is no expectation that CRD updates occur before Custom Resource updates. This might cause the `nomos status` to report a transient error for a brief period of time, until both the CustomResource and the CRD are present in the cluster.

  * Config Sync does not allow removal of a CRD if any CustomResource in the repo depends on it. To remove a CRD, you also need to remove its CustomResource. We recommend that you remove them both in the same commit to the repo.

  * You can sync a CustomResource without syncing its CRD, as long as you can guarantee that the CRD already exists in the cluster.




## Limit which clusters a config affects

By default, Config Sync applies a config to every enrolled cluster. However, if you need to apply a config to only a subset of clusters, you can either add a cluster-name-selector annotation or a ClusterSelector config to your repository.

The `cluster-name-selector` annotation provides a simple way to specify a subset of clusters to apply a config to. This option only supports selecting clusters by names.

The `ClusterSelector` object supports selecting clusters by labels, but it requires more complex configurations.

Both options require `clusterName` to be specified in Config Sync on the cluster. Depending on how you installed Config Sync, you can provide the cluster name in the following ways:

  * **If you installed Config Sync by using Google Cloud CLI or Google Cloud console** : `clusterName` is automatically set to the fleet membership name.

  * **If you installed Config Sync manually by using`kubectl`**, you must set the `CLUSTER_NAME` environment variable on the `reconciler-manager` deployment. For more information, see [Provide a cluster name for cluster selectors](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-kubectl#configure-cluster-name).




## Configure using the `cluster-name-selector` annotation

You can apply a config to a subset of clusters with the `configsync.gke.io/cluster-name-selector` annotation. You can use this annotation to apply a config to a set of clusters, denoted by cluster names. The value of the annotation is a comma-separated list of target cluster names. You can apply the annotation on cluster-scoped objects and namespace-scoped objects. Namespace objects are selected when the annotation matches the cluster name and when the namespace that the clusters belong to is also selected.

### Select a single cluster

The following config creates a Role called `namespace-reader` that defines a set of permissions for reading namespaces. This Role is only applied on the cluster that has the name `cluster-1`.
    
    
    kind: Role
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      namespace: my-namespace
      name: namespace-reader
      **annotations :
        configsync.gke.io/cluster-name-selector: cluster-1**
    rules:
    - apiGroups: [""]
      resources: ["namespaces"]
      verbs: ["get", "watch", "list"]
    

### Select a list of clusters

The following config creates the same Role as the previous example, but this Role is only applied on the clusters that have the name `cluster-1`, `cluster-2`, or `cluster-3`.
    
    
    kind: Role
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      namespace: my-namespace
      name: namespace-reader
      **annotations :
        configsync.gke.io/cluster-name-selector: cluster-1,cluster-2,cluster-3**
    rules:
    - apiGroups: [""]
      resources: ["namespaces"]
      verbs: ["get", "watch", "list"]
    

## Configure using the `ClusterSelector` object

A ClusterSelector is a special type of config that uses Kubernetes [labelSelectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/). You can use a ClusterSelector to limit which clusters a particular config applies to, based on the cluster's labels. You can also use ClusterSelectors to limit which clusters instantiate a namespace-scoped object.

Like other labelSelectors, ClusterSelectors operate using AND logic. Since ClusterSelectors use AND logic, objects are only selected when they match all of the labels that you define.

A ClusterSelector config does not persist in a cluster. Instead, you reference it in another config using an annotation, and that config only applies to clusters that match the ClusterSelector.

Before you can use ClusterSelectors, each cluster must have a unique name and a set of labels that can be selected. The cluster metadata is specified in a Cluster config in your source of truth.

Next, you add labels to a cluster, create the ClusterSelector, then reference it in another config.

**Note:** The Cluster and ClusterSelector configs are only used to filter the cluster-specific configurations and will not be applied to the cluster.

### Add labels to a cluster

To use ClusterSelectors, each cluster must have a set of labels that can be selected. In unstructured repositories, Cluster configs can be stored arbitrarily in the config directory or its descendant directories.

To apply configs to a cluster, the `metadata.name` field of the Cluster config must match the [`clusterName` field](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/configmanagement-fields#configuration_for_behavior_of_the_configmanagement_object) of your ConfigManagement object.

The following example Cluster config declares that `cluster-2` has the `environment: prod` and `location: central` labels.
    
    
    kind: Cluster
    apiVersion: clusterregistry.k8s.io/v1alpha1
    metadata:
      name: cluster-2
      **labels :
        environment: prod
        location: central**
    

You can also apply annotations using a Cluster config.

**Note:** The labels defined in the `Cluster` config are different from [GKE cluster labels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels#what-are-labels).

### Create a ClusterSelector

A ClusterSelector selects only clusters with a given label or combination of labels. In unstructured repositories, ClusterSelectors can be stored arbitrarily in the sync directory or its descendant directories.

The following ClusterSelector selects only clusters with the `environment: prod` label.
    
    
    kind: ClusterSelector
    apiVersion: configmanagement.gke.io/v1
    metadata:
      name: selector-env-prod
    spec:
      selector:
        **matchLabels :
          environment: prod**
    

The following ClusterSelector selects any clusters with the `location: central` or `location: west` labels.
    
    
    kind: ClusterSelector
    apiVersion: configmanagement.gke.io/v1
    metadata:
      name: selector-central-or-west
    spec:
      selector:
        **matchExpressions :
          - key: location
            operator: In
            values:
            - central
            - west **
    

A ClusterSelector has no effect until you reference it in another config.

### Reference a ClusterSelector

To reference a ClusterSelector in another config, set the annotation `configmanagement.gke.io/cluster-selector: CLUSTERSELECTOR-NAME`.

The following config creates a ClusterRole called `namespace-reader` that defines a set of permissions for reading namespaces. This ClusterRole is only instantiated on clusters that match the `selector-env-prod` ClusterSelector.
    
    
    kind: ClusterRole
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: namespace-reader
      **annotations :
        configmanagement.gke.io/cluster-selector: selector-env-prod**
    rules:
    - apiGroups: [""]
      resources: ["namespaces"]
      verbs: ["get", "watch", "list"]
    

### Limit the clusters a namespace-scoped config affects

By default, Config Sync applies configs inherited by a namespace to that namespace in each cluster where it exists. You can use a ClusterSelector to apply the config to only a subset of those clusters.

**Note:** ClusterSelectors are similar to but not identical to [NamespaceSelectors](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/namespace-scoped-objects#namespaceselectors). A NamespaceSelector narrows the pool of namespaces that can inherit a given config from an abstract namespace, regardless of the directory structure of the `namespaces/` directory.   
  
A ClusterSelector narrows the pool of clusters a config applies to, whether the config is focused on a cluster-scoped or namespace-scoped object.

For example, you can configure clusters differently based on their geographic location or the geographic location of their clients. This configuration can be useful for localization or for legal compliance. The examples in this section apply locale-specific configs to only clusters with the label `location: france`.

The following Cluster config adds an `location: france` label to a cluster called `cluster-1`:
    
    
    kind: Cluster
    apiVersion: clusterregistry.k8s.io/v1alpha1
    metadata:
      name: cluster-1
      **labels :
        location: france**
    

Create a ClusterSelector config that references the labels you want to select. The following ClusterConfig selects the `location: france` label:
    
    
    kind: ClusterSelector
    apiVersion: configmanagement.gke.io/v1
    metadata:
      name: selector-location-france
    spec:
      **selector :
        matchLabels:
          location: france**
    

A ClusterSelector has no effect until you reference it in another config. The following RoleBinding config selects only clusters that match the `selector-location-france` ClusterSelector. This configuration might be useful, for instance, if a compliance guideline only allowed a particular service account to view information on clusters in their designated geographic region.
    
    
    kind: RoleBinding
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: viewers
      **annotations :
        configmanagement.gke.io/cluster-selector: selector-location-france**
    subjects:
    - kind: Group
      name: system:serviceaccounts:foo
      apiGroup: rbac.authorization.k8s.io
    roleRef:
      kind: ClusterRole
      name: view
      apiGroup: rbac.authorization.k8s.io
    

If you place this config in an abstract namespace or a namespace directory, such as `namespaces/eng`, it is applied to the namespaces that inherit it, but only on clusters with the `location: france` label.

## What's next

  * Learn more about [configuring namespaces and namespace-scoped objects](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/namespace-scoped-objects)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
