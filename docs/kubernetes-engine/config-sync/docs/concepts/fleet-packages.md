---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/fleet-packages/
title: About fleet packages \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:14.398236+00:00
---

# About fleet packages  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/fleet-packages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  About fleet packages Stay organized with collections  Save and categorize content based on your preferences. 

This page explains fleet packages, the `FleetPackage` API, and how they relate to Config Sync.

A `FleetPackage` is a declarative API that lets you manage packages across a fleet. A **fleet package** is a set of Kubernetes YAML manifests that define cluster configuration. By using fleet packages, you can deploy packages through an all-at-once or progressive rollout to clusters that are registered to your fleet.

You define each `FleetPackage` object once, and then you can update that package with a new revision. When you apply a new revision, the fleet package service picks up those changes and deploys them to your clusters.

## Benefits

Use fleet packages to deploy Kubernetes resources across clusters that are registered to a fleet. After you create and apply a fleet package, the fleet package automatically deploys the Kubernetes configuration files in the Git repository to the new cluster. Fleet packages builds upon Config Sync's benefits like automatic drift correction, and offers the following unique advantages:

  * **Automate resource rollout:** After you set up a fleet package, the Kubernetes resources it points to are automatically deployed by the fleet package service on all clusters.

  * **Configure new clusters automatically** : If you configure a fleet package and then later add new clusters to a fleet, any resources defined by the fleet package are automatically deployed to the new cluster.

  * **Manage Kubernetes configuration at scale:** Instead of managing clusters one-by-one, use fleet packages to deploy resources to an entire fleet of clusters.

  * **Minimize the impact of incorrect changes:** Choose a maximum number of clusters to deploy resources to at once. You can closely monitor the changes to each cluster to ensure that incorrect changes don't impact your entire fleet.

  * **Simplify Config Sync configuration:** Fleet packages uses Cloud Build to authenticate to Git, meaning you authenticate once per project instead of once per `RootSync` or `RepoSync` object.




You might prefer to use Config Sync with `RootSync` or `RepoSync` objects instead of fleet packages if one or more of the following scenarios applies to you:

  * You manage a small number of clusters.

  * You need more control over how resources are deployed to your clusters, beyond what the fleet package API provides with labels and variants.




## Requirements and limitations

  * Only Git repositories are supported as the source of truth when configuring a fleet package.

  * The Kubernetes resources stored in Git must represent the end state of the resource. Additional overlays to transform the resource stored in Git are not supported. For more information about the differences in these resources, see [Best practice: Create _WET_ repositories](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/gitops-best-practices#create-wet-repo).

  * The `FleetPackage` API is available only in the `us-central1` region. You can still deploy to clusters in different regions, but you must set up Cloud Build and configure the gcloud CLI in `us-central1`.

  * The maximum number of fleet packages is 300 per project per region.




## Architecture

You can use the `FleetPackage` API to deploy Kubernetes manifests to a fleet of clusters. The `FleetPackage` API uses Cloud Build to sync and fetch Kubernetes resources from your Git repository. The fleet package service then deploys those resources to your clusters.

![Diagram that shows the flow of Kubernetes resources in Git syncing to a fleet of clusters](https://docs.cloud.google.com/static/kubernetes-engine/config-sync/docs/img/fp_workflow.svg)

## How variants are generated

Fleet packages use a system of variants to deploy different Kubernetes resource configurations to different clusters or groups of clusters within your fleet, but from the same Git repository.

There are two fields in the `FleetPackage` spec that control the behavior of variants:

  1. **`resourceBundleSelector.cloudBuildRepository.variantsPattern`** : A glob pattern used to find files and directories in your Git repository (under the specified `path`, or the repository root if `path` is omitted). This pattern determines which files or directories become variants and what content they include.
  2. **`variantSelector.variantNameTemplate`** : An expression that maps each cluster in your fleet to one of the variant names generated by `variantsPattern`. This selection is based on the cluster's fleet membership metadata.



### `variantsPattern` matching

The `variantsPattern` field is _required_ to specify how to generate variants from the configurations stored in your repository. The matching uses the following logic:

  * **File match:** If the pattern matches a YAML file, a variant is created.

    * **Variant name:** The filename without the extension (for example, `prod-config.yaml` becomes variant `prod-config`).
    * **Variant content:** The content of this single file.
  * **Directory match:** If the pattern matches a directory, a variant is created.

    * **Variant name:** The directory name (for example, directory `dev` becomes variant `dev`).
    * **Variant content:** The combination of all YAML files found within this directory and all its subdirectories, recursively.



File matching patterns have the following limitations:

  * No recursive (double) wildcards. The `**` pattern isn't supported.
  * If a pattern includes a dot (`.`) character, it must be followed by an alphanumeric character.
  * Patterns can't include single quotes (`'`).
  * Variant names must be unique. If your pattern matches multiple files with the same name (for example, `app1/deploy.yaml` and `app2/deploy.yaml`), both try to create a variant named `deploy`, causing a name collision.



As an example, consider a repository with the following structure:
    
    
    repo-root/
    └── FleetPackages/
        └── clusters/
            ├── common-ingress.yaml
            ├── us-central1-a/
            │   ├── gke-1/
            │   │   ├── deployment.yaml
            │   │   └── service.yaml
            │   └── gke-2/
            │       ├── deployment.yaml
            │       └── service.yaml
            └── us-central1-b/
                ├── gke-1.yaml
                └── blue-green.yaml
    

You can match, and therefore sync to your clusters, different files, depending on the type of file or directory matching that you define in the fleet package specification, for example:

  * `variantsPattern: "*"`: Matches `common-ingress.yaml`, `us-central1-a`, and `us-central1-b`. Generates variants:

    * `common-ingress` (from file)
    * `us-central1-a` (combining all YAML files within that folder)
    * `us-central1-b` (combining all YAMLs within that folder)
  * `variantsPattern: "*.yaml"`: Matches `common-ingress.yaml`. Generates variant:

    * `common-ingress`
  * `variantsPattern: "us-*"`: Matches `us-central1-a` and `us-central1-b`. Generates variants:

    * `us-central1-a`
    * `us-central1-b`
  * `variantsPattern: "us-central1-b/*.yaml"`: Matches `us-central1-b/gke-1.yaml` and `us-central1-b/blue-green.yaml`. Generates variants:

    * `gke-1`
    * `blue-green`



### `variantNameTemplate` matching

After variants are defined, the `variantNameTemplate` field in the `variantSelector` section determines which variant is applied to each cluster. The template can use variables to access the following fleet membership metadata:

  * `${membership.name}`: The cluster's fleet membership name.
  * `${membership.location}`: The fleet membership location.
  * `${membership.project}`: The fleet membership project.
  * `${membership.labels['KEY']}`: The value of the label `KEY` on the fleet membership.



For example, consider the following scenarios that use labels to match variants:

  * `variantNameTemplate: "${membership.labels['env']}"`: A cluster with the label `env: prod` syncs to a variant named `prod`.
  * `variantNameTemplate: "${membership.location}"`: Clusters sync to variants matching their location (for example, `us-central1-a`).
  * `variantNameTemplate: "default"`: Clusters sync to a variant named `default`. This is the default behavior if `variantSelector` is omitted. If your repository doesn't contain a file named `default.yaml` or a directory named default, nothing is synced.



### Combining `variantsPattern` and `variantNameTemplate`

For a successful deployment, you must ensure that the variant names generated by your `variantsPattern` are names that your clusters can sync to by matching the `variantNameTemplate`.

For example, to deploy to clusters based on an environment label, you might structure your Git repository with directories like `dev`, `staging`, and `prod`. You would then use the following fleet package specification:
    
    
    resourceBundleSelector:
      cloudBuildRepository:
        # ... other fields
        path: "manifests"
        variantsPattern: "*" # Matches dev, staging, prod directories
    variantSelector:
      variantNameTemplate: "${membership.labels['env']}"
    

With this configuration, a cluster labeled `env: staging` receives the contents of the `manifests/staging/` directory.

## Deployment strategies

You can use fleet packages to deploy resources from a Git repository to your entire fleet of clusters. You can also configure your fleet package to control how, where, and what type of resources are deployed.

The following section shows examples of different `FleetPackage` configurations. For more detailed information about applying fleet packages, see [Deploy fleet packages](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-packages).

### Deployment to all clusters in a fleet

The following `FleetPackage` uses a rolling strategy to deploy Kubernetes resources to three clusters at a time and targets all clusters in a fleet:
    
    
    resourceBundleSelector:
      cloudBuildRepository:
        name: projects/my-project/locations/us-central1/connections/my-connection/repositories/my-repo
        tag: v1.0.0
        variantsPattern: "*.yaml"
        serviceAccount: projects/my-project/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    target:
      fleet:
        project: projects/my-project
    rolloutStrategy:
      rolling:
        maxConcurrent: 3
    variantSelector:
      variantNameTemplate: deployment # matches a file named deployment.yaml
    

### Deployment to a subset of clusters

The following `FleetPackage` uses a label selector to deploy Kubernetes resources only to clusters with the membership label `country` that matches `"us"` in the fleet:
    
    
    resourceBundleSelector:
      cloudBuildRepository:
        name: projects/my-project/locations/us-central1/connections/my-connection/repositories/my-repo
        tag: v1.0.0
        variantsPattern: "*.yaml"
        serviceAccount: projects/my-project/serviceAccounts/my-service-account@my-project.iam.gserviceaccount.com
    target:
      fleet:
        project: projects/my-project
        selector:
          matchLabels:
            country: "us"
    rolloutStrategy:
      rolling:
        maxConcurrent: 3
    

## What's next

[Deploy fleet packages](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-packages)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
