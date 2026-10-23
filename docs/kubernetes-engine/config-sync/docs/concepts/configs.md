---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/configs/
title: Organize configuration files in a source of truth \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:50.586868+00:00
---

# Organize configuration files in a source of truth  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/configs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Organize configuration files in a source of truth Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to organize configurations in a source of truth.

**Key Term:** A **source of truth** is the central repository where your Kubernetes configuration files (manifests) are stored and versioned. Config Sync supports Git repositories, OCI images, and Helm charts as sources of truth. After setup, Config Sync monitors your source of truth and applies any changes to your clusters. For more information about sources, see [Sources of truth](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/sources-of-truth).

As your organization grows, you likely need to manage configurations across a fleet of clusters and support multiple teams working in the same repositories. A key part of a successful GitOps strategy is ensuring that configurations are applied to the correct clusters and that teams can work without interfering with one another.

## About configuration files

Config Sync is designed for cluster operators who manage many clusters. You can ensure that your clusters meet business and compliance standards by letting Config Sync manage namespaces, Roles, RoleBindings, ResourceQuotas, and other important Kubernetes objects, across your fleet.

When Config Sync manages these resources, it keeps your enrolled clusters in sync using _configs_. A config is a YAML or JSON file in a source of truth. Config Sync supports Git repositories, OCI images, and Helm charts as the source of truth. Configs contain the same type of configuration details that you can manually apply to a cluster using the `kubectl apply` command. You can create a config for any Kubernetes object that can exist in a cluster. However, some Kubernetes objects, such as Secrets, contain sensitive information that might be inappropriate to store in a source of truth. Consider carefully whether to manage these types of objects using Config Sync.

## Requirements and limitations

  * Some Kubernetes resources contain immutable fields, like Pod selectors in a Deployment object. You can't change any immutable field in a config by changing the value in the source of truth. Attempting such a change causes a `KNV2009` error. If you need to change an immutable field, delete the object from your source of truth, wait for Config Sync to delete the object from the cluster, and then re-create the object in your source of truth with your updates.

  * If you use [Git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules), you must [grant Config Sync access](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/grant-access-git) to all repositories, including any submodules.

  * You can't use Config Sync to directly manage built-in Kubernetes ClusterRoles. GKE comes with some built-in [user-facing roles](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles), such as `cluster-admin`, `admin`, `edit`, and `view`. You can't directly manage these ClusterRoles with Config Sync, otherwise Config Sync conflicts with GKE. To add permissions to the built-in ClusterRoles, use [role aggregation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles) to modify them indirectly. To modify the roles, create a uniquely named ClusterRole in your source of truth with the appropriate annotations.




## Organize your source of truth

You can configure Config Sync to sync from an entire repository, or from specific folders or branches. Because of this flexibility, organize your configuration files based on your team's or organization's needs.

We recommend that when you configure Config Sync, you set the `sourceFormat` to `unstructured`. The structured (hierarchical) source type requires a very specific folder structure to correctly sync your configs and adds unnecessary complexity in most cases.

Most of Config Sync's documentation, including this page, uses the unstructured format by default, but you can find information about the hierarchical format, if needed, at [Use a hierarchical repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/hierarchical-repo).

When using an unstructured source, you have the flexibility to organize your configs to suit your team's workflow. This section provides a few common patterns for structuring your repository.

### Environment-based layout

A common approach is to organize your repository by environment.
    
    
    ├── cluster-essentials/
    │   ├── crds/
    │   └── namespace.yaml
    ├── environments/
    │   ├── dev/
    │   │   ├── backend/
    │   │   └── frontend/
    │   ├── staging/
    │   │   ├── backend/
    │   │   └── frontend/
    │   └── prod/
    │       ├── backend/
    │       └── frontend/
    └── system/
        └── monitoring/
    

In this example, the source of truth is organized as follows:

  * `cluster-essentials/`: contains configuration that applies to all clusters, regardless of environment. This might include resources like Custom Resource Definitions (CRDs) and essential namespaces.
  * `environments/`: the parent directory for all environment-specific configurations.
  * `system/`: contains configurations for system-level services like monitoring.



This approach is straightforward to understand and navigate and provides a clear promotion path for changes from one environment to another.

When you set up Config Sync in this scenario, you create multiple `RootSync` objects on each cluster. For example, a development cluster has `RootSync` objects syncing from `cluster-essentials/`, `system/`, and `environments/dev/`.

### Cluster-based layout

If your focus is on managing a fleet of individual clusters with distinct configurations, a cluster-based layout might be more suitable.
    
    
    ├── clusters/
    │   ├── cluster-a/
    │   │   ├── apps/
    │   │   └── networking/
    │   ├── cluster-b/
    │   │   ├── apps/
    │   │   └── networking/
    │   └── cluster-c/
    │       ├── apps/
    │       └── networking/
    └── shared/
        ├── roles/
        └── policies/
    

In this example, the source of truth is organized as follows:

  * `clusters/`: contains a directory for each cluster you are managing.
  * `shared/`: holds configurations that are common across all clusters, like RBAC roles and security policies.



This approach is effective for managing many clusters if those clusters all have unique configurations, as it provides clear ownership and isolation of configurations. This approach can be more complex to manage if you have many shared cluster configurations.

When you set up Config Sync in this scenario, you can use a `RepoSync` to configure each cluster to sync both from `shared` and the cluster-specific directory.

### Team-based layout

For organizations where different teams manage different applications or services, a team-based layout can be effective. This approach aligns the source of truth structure with your organizational structure.
    
    
    ├── teams/
    │   ├── team-alpha/
    │   │   ├── app-one/
    │   │   └── app-two/
    │   ├── team-beta/
    │   │   ├── service-a/
    │   │   └── service-b/
    │   └── team-gamma/
    │       ├── data-pipeline/
    │       └── dashboard/
    └── platform/
        ├── cluster-roles/
        └── storage-classes/
    

In this example, the source of truth is organized in the following way:

  * `teams/`: organizes configuration by team, with each team managing their own application and service configurations.
  * `platform/`: contains cluster-wide configurations that a central platform team manages and that all teams use.



This approach lets teams manage their own configuration and release cycles and reduces the chance that one team's changes accidentally impact another team. However, this approach requires careful management of dependencies between app teams and platform teams.

When you set up Config Sync, for this scenario, each team uses a `RootSync` object to sync configurations, for example `team-alpha` syncs from `teams/team-alpha/`.

## Validating configuration files

After you create, organize, and add configuration files to a source of truth, use the [`nomos vet --source-format=unstructured` command](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command#vet) to check the syntax and validity of your configs. This helps you avoid errors during or after a sync.

## Ignore object mutations

If you don't want Config Sync to maintain the state of the object in the cluster after it exists, add the `client.lifecycle.config.k8s.io/mutation: ignore` annotation to the object that you want Config Sync to ignore mutations in.

The following example shows you how to add the annotation to an object:
    
    
    metadata:
      annotations:
        **client.lifecycle.config.k8s.io/mutation : ignore **
    

You cannot manually modify this annotation on managed objects in the cluster.

## Convert a hierarchical repository to an unstructured repository

If you use a [hierarchical repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/hierarchical-repo) and want to convert it to an [unstructured repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/unstructured-repo), run the following command:
    
    
    nomos hydrate PATH
    

Replace `PATH` with the path to your directory.

This command creates a `compiled/` directory in the current working directory. Within that directory, a subdirectory is created for each enrolled cluster. These subdirectories contain the fully resolved configs and can be used in an unstructured repository.

For more details, see [`nomos` commands](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command#hydrate).

If you prefer converting your repository manually, complete the following instructions:

  1. Remove `Repo` configs in the `system/` directory from your Git repository. The `Repo` resource is not needed for an unstructured repository.

  2. The [abstract namespace directory](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/hierarchical-repo#namespace-inheritance) isn't supported in an unstructured repository. Therefore, declare the namespace of all resources originally included in the `namespaces/` directory and its subdirectories.

  3. [Namespace inheritance](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/hierarchical-repo#namespace-inheritance) isn't supported in the unstructured repository. Therefore, declare all resources that are originally inherited in descendant namespaces (the ones originally under the `namespaces/` directory).




## What's next

  * [Learn more about sources of truth](https://docs.cloud.google.com/kubernetes-engine/enterprise/config-sync/docs/concepts/sources-of-truth)
  * [Learn GitOps best practices](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/gitops-best-practices)
  * [Set up Config Sync with default settings](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/install-default)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
