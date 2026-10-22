---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/hierarchical-repo/
title: Use a hierarchical repository \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:13.984816+00:00
---

# Use a hierarchical repository  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/hierarchical-repo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Use a hierarchical repository Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how Config Sync reads [configs](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/configs) from a hierarchical source of truth and applies the resulting configuration to your clusters automatically.

We recommend that you [use an unstructured source of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/unstructured-repo) instead of hierarchical because it provides the same core capabilities, but gives you more flexibility in organizing your resources. If you already use a hierarchical source of truth, you can [convert it to an unstructured source of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/unstructured-repo#convert).

To understand how Config Sync uses a hierarchical repository, it's helpful if you're familiar with Git repositories and the `git` command-line interface.

You can [view an example of how to organize and configure a hierarchical source of truth](https://github.com/GoogleCloudPlatform/anthos-config-management-samples/tree/main/hierarchical-format) in the Config Sync samples repository.

## Structure of the directory

For hierarchical sources, Config Sync takes advantage of filesystem-like structures, and uses the directory to determine which clusters or namespaces a config is relevant to.

### `namespaces/`

The `namespaces/` directory contains configs for namespaces and namespace-scoped objects. The structure within `namespaces/` is the mechanism that drives [namespace inheritance](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/namespace-scoped-objects#abstract-namespace-config). You can limit which namespaces can inherit a config, by using a [NamespaceSelector](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/namespace-scoped-objects#namespaceselectors).

### `cluster/`

The `cluster/` directory contains configs that apply to entire clusters, rather than to namespaces. By default, any config in the `cluster/` directory applies to every cluster enrolled in Config Sync. You can limit which clusters a config can affect by using a [ClusterSelector](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/cluster-scoped-objects#configure_a_subset_of_clusters).

**Note:** Namespaces are configured within `namespaces/`, even though they are cluster-scoped.

### `clusterregistry/`

The `clusterregistry/` directory is optional, and contains configs for [ClusterSelectors](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/cluster-scoped-objects#configure_a_subset_of_clusters). ClusterSelectors limit which clusters a config applies to, and are referenced in configs found in the `cluster/` and `namespaces/` directories.

### `system/`

The `system/` directory contains configs for the Operator.

## Example hierarchical source of truth

The following directory structure demonstrates how to use a Config Sync hierarchical source of truth to configure a Kubernetes cluster shared by two different teams, `team-1` and `team-2`.

  * Each team has its own Kubernetes namespace, Kubernetes service account, resource quotas, network policies, rolebindings.
  * The cluster administrator sets up a policy in `namespaces/limit-range.yaml` to constrain resource allocations (to Pods or containers) in both namespaces.
  * The cluster administrator also sets up ClusterRoles and ClusterRoleBindings.



A valid Config Sync hierarchical source must include three subdirectories: `cluster/`, `namespaces/`, and `system/`.

The `cluster/` directory contains configs that apply to entire clusters (such as ClusterRole, ClusterRoleBinding), rather than to namespaces.

The `namespaces/` directory contains configs for the namespace objects and the namespace-scoped objects. Each subdirectory under `namespaces/` includes the configs for a namespace object and all the namespace-scoped objects under the namespace. The name of a subdirectory should be the same as the name of the namespace object. Namespace-scoped objects which need to be created in each namespace, can be put directly under `namespaces/` (for example, `namespaces/limit-range.yaml`).

The `system/` directory contains configs for the ConfigManagement Operator.
    
    
    ├── cluster
    │   ├── clusterrolebinding-namespace-reader.yaml
    │   ├── clusterrole-namespace-reader.yaml
    │   ├── clusterrole-secret-admin.yaml
    │   └── clusterrole-secret-reader.yaml
    ├── namespaces
    │   ├── limit-range.yaml
    │   ├── team-1
    │   │   ├── namespace.yaml
    │   │   ├── network-policy-default-deny-egress.yaml
    │   │   ├── resource-quota-pvc.yaml
    │   │   ├── rolebinding-secret-reader.yaml
    │   │   └── sa.yaml
    │   └── team-2
    │       ├── namespace.yaml
    │       ├── network-policy-default-deny-all.yaml
    │       ├── resource-quota-pvc.yaml
    │       ├── rolebinding-secret-admin.yaml
    │       └── sa.yaml
    ├── README.md
    └── system
        └── repo.yaml
    

## Use namespace inheritance and abstract namespaces

With a hierarchical source of truth, you can use the concept of namespace inheritance to automatically apply configs to groups of namespaces in all the clusters where those namespaces exist (or should exist).

Namespace inheritance applies to the `namespaces/` directory of the hierarchical repository and all its subdirectories. Configs in other directories in the repository, such as `cluster/`, are not subject to inheritance.

In a hierarchical source of truth, the `namespaces/` directory can contain two different types of subdirectories:

  * A _namespace directory_ contains a config for a namespace. The name of the file containing the config is not important, but the config must have `kind: Namespace`. A namespace directory can also contain configs for other kinds of Kubernetes objects. A namespace directory cannot contain subdirectories. A namespace config represents an actual namespace in a cluster.

  * An _abstract namespace directory_ contains namespace directories. It can also contain configs for other Kubernetes objects, but it cannot directly contain a config for a namespace. An abstract namespace directory does not represent an object in a Kubernetes cluster, but its descendant namespace directories do.




To help ensure that your namespace and abstract namespace sources have the correct type of configs and structure, error [KNV1003: IllegalNamespaceSubdirectoryError](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/errors#knv1003) reports when there is a problem.

Configs in a namespace directory only apply to that namespace. However, configs in an abstract namespace directory are applied to all of that abstract namespace's descendant namespace directories (or those descendant namespaces that match a config's [NamespaceSelector](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/namespace-scoped-objects#namespaceselectors), if one is present).

Inheritance of a config in the `namespaces/` directory is based largely on its location within the directory tree in the source of truth. To understand which configs are being applied to a given namespace in a given cluster, you can browse the [namespace inheritance example repository](https://github.com/GoogleCloudPlatform/anthos-config-management-samples/tree/main/namespace-inheritance).

## Restricted namespaces

`config-management-system` is a restricted namespace. You cannot use it as an abstract namespace directory. You can define a `config-management-system` namespace, but the only permitted resource type for the `config-management-system` namespace is `RootSync`.

## Making changes in your source of truth

When you make a change in your source of truth that creates or deletes namespace directories from within the `namespaces/` directory, you might get unexpected results depending on the action:

**Caution:** By default, Git repositories don't provide fine-grained access control. If the set of people with commit rights to your repository is not exactly the same as the set of users allowed to create, modify, or delete Kubernetes objects in your clusters, consider using an access control mechanism such as `OWNERS` or `CODEOWNERS` files in your repository.

  * **Creating a directory** : when a valid `namespaces/` hierarchy is committed to the source of truth, Config Sync creates namespaces, and then creates Kubernetes objects in those namespaces for each config that the namespace directory contains or inherits.
  * **Deleting a directory** : deleting a namespace directory is a destructive operation. The namespace, and its contents, is deleted, on every cluster managed by Config Sync where the namespace exists. If you delete an abstract namespace directory containing descendant namespace directories, all of those namespaces and their contents are deleted from every cluster managed by Config Sync.
  * **Renaming a directory** : Renaming a namespace directory is a deletion, followed by a creation and is considered a destructive operation. Renaming an abstract namespace directory has no externally visible effect.

**Note:** If you rename a namespace directory, remember to also update its name in the config for the namespace.
  * **Moving a directory** : moving a namespace or an abstract namespace directory within `namespaces/` does not delete the namespace or objects within it, except where the namespace starts or stops inheriting a config from an abstract namespace directory, due to a change in its hierarchy.




## What's next

  * Learn how to [manage namespaces and namespace-scoped objects](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/namespace-scoped-objects)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
