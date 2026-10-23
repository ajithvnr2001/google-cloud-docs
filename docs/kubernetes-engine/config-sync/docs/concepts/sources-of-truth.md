---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/sources-of-truth/
title: About sources of truth \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:34.975670+00:00
---

# About sources of truth  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/sources-of-truth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  About sources of truth Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the different types of sources of truth that Config Sync can sync from.

A key concept in GitOps workflows is the _source of truth_ , a central repository where your configuration files are stored. A configuration file is typically a YAML or JSON file that defines Kubernetes resources. Normally, you might manually apply Kubernetes objects with the `kubectl` command-line tool, but Config Sync can automatically apply those resources from a single source of truth like a Git repository. Config Sync then monitors your specified source of truth and automatically applies any changes to your clusters.

Config Sync can sync configuration files from three different types of sources: Git repositories, Open Container Initiative (OCI) images, and Helm charts. This document explains each of these source types and how Config Sync interacts with them. Reading this document can help you choose the best source option for your workflow and environment.

## Git repositories

Git is widely adopted technology for version control and collaboration. With Git, you can organize your repository in the way that suits your needs and get the benefits of version control and branching, if needed. Because Git is a mature and widely adopted technology, you get a variety of options for providers and tools.

When you configure Config Sync with a Git repository as the source of truth, Config Sync uses a `git-sync` container within the reconciler Pod to pull configs from the Git repository. You can configure the repository URL, branch, and revision (commit or tag) for greater control over where to pull configs within your Git repository.

### Example `RootSync` configuration

The following example shows a `RootSync` manifest that syncs from a Git repository:
    
    
    apiVersion: configsync.gke.io/v1beta1
    kind: RootSync
    metadata:
      name: root-sync
      namespace: config-management-system
    spec:
      sourceType: git
      sourceFormat: unstructured
      git:
        repo: https://github.com/example/my-configs.git
        revision: main
        dir: cluster-configs
        auth: none # replace with your authentication method such as ssh or token
        period: 60s
    

This configuration sets up Config Sync to sync manifests from a Git repository. Config Sync watches the `cluster-configs` directory in the `main` branch of the `https://github.com/example/my-configs.git` repository, checking for updates every 60 seconds using no authentication.

### Example use case: Centralized management

Imagine that you are a platform administrator who wants to use a Git repository to enforce baseline policies across all clusters in a fleet. In this scenario, you might store standard `NetworkPolicies`, `RoleBindings`, and `ResourceQuotas` in a central Git repository named `standard-configs`. When a new cluster is provisioned, Config Sync is configured to sync from `standard-configs` repository, helping to ensure all clusters meet organizational standards from the start.

## OCI images

OCI images are a standard format for packaging applications and their dependencies. This approach treats your configurations as artifacts, similar to how you would treat container images. This approach offers advantages like immutability and faster performance at scale. With OCI, you can use container image infrastructure and tooling like [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) to manage your images, and Workload Identity Federation for GKE to help simplify authentication.

Using OCI as a configuration source usually requires a separate process to build your configuration files into an OCI image and then push it to a registry platform like Artifact Registry. This approach can be less directly human-readable than configurations stored as files in a Git repository.

When you configure Config Sync with an OCI image as the source of truth, Config Sync uses an `oci-sync` container within the reconciler Pod to pull the OCI image containing the configs from the registry.

### Example `RootSync` configuration

The following example shows a `RootSync` manifest that syncs from an OCI image stored in Artifact Registry:
    
    
    apiVersion: configsync.gke.io/v1beta1
    kind: RootSync
    metadata:
      name: root-sync
      namespace: config-management-system
    spec:
      sourceType: oci
      sourceFormat: unstructured
      oci:
        image: us-central1-docker.pkg.dev/my-project/my-repo/my-config-image:v1.0.0
        dir: .
        auth: k8sserviceaccount
    

This configuration sets up Config Sync to sync from an OCI image. Config Sync pulls the `us-central1-docker.pkg.dev/my-project/my-repo/my-config-image:v1.0.0` image from Artifact Registry using a Kubernetes service account for authentication.

### Example use case: CI/CD pipeline integration

Imagine that you want to integrate OCI image creation into your organization's CI/CD pipeline. When changes to configuration files are merged, you can set up your pipeline to run validation tests (like the `nomos vet` command), build the YAML files into an OCI image, and push the image to Artifact Registry. Config Sync would then automatically detect and apply the new version of the image onto your clusters, ensuring a validated and versioned rollout of all configuration changes.

## Helm charts

Helm is a popular package manager for Kubernetes, which uses a packaging format called charts. Config Sync can fetch, render, and sync resources defined in Helm charts.

Helm offers a consistent way to package and reuse Kubernetes applications. You can use templates or prebuilt Helm charts for consistent and reusable configurations.

If you're not already familiar with Helm, the templating and release process can add extra complexity to your configuration management pipeline.

When you configure Config Sync with a Helm chart as the source of truth, Config Sync uses a `helm-sync` container within the reconciler Pod to pull charts from a Helm repository (like Artifact Registry) or a Git repository, and then renders the chart to produce Kubernetes manifests. Alternatively, you can use Config Sync with Kustomize to render Helm charts. For more information about this approach, see [Use Config Sync with Kustomize and Helm](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/tutorials/config-sync-helm).

### Example `RootSync` configuration

The following example shows a `RootSync` manifest that syncs from a Helm chart stored in Artifact Registry:
    
    
    apiVersion: configsync.gke.io/v1beta1
    kind: RootSync
    metadata:
      name: root-sync
      namespace: config-management-system
    spec:
      sourceType: helm
      helm:
        repo: oci://us-central1-docker.pkg.dev/my-project/my-helm-repo
        chart: my-chart
        version: 1.2.0
        auth: gcpserviceaccount
        gcpServiceAccountEmail: my-service-account@my-project.iam.gserviceaccount.com
        releaseName: my-chart-release
        namespace: my-app-namespace # Namespace where the chart resources will be deployed
    

This configuration sets up Config Sync to sync a Helm chart from an OCI repository. Config Sync fetches version `1.2.0` of `my-chart` chart from the `oci://us-central1-docker.pkg.dev/my-project/my-helm-repo` repository, and it authenticates with the `my-service-account@my-project.iam.gserviceaccount.com` service account. It deploys the chart's resources into the `my-app-namespace` namespace under the release name of `my-chart-release`.

### Example use case: Deploying a third-party application

Imagine that you are part of an application team that wants to deploy Prometheus to a cluster. You can configure Config Sync to pull from a prebuilt Helm chart that deploys Prometheus. Instead of manually running Helm commands, you instead define the chart source, version, and any custom `values` within Config Sync's `RootSync` or `RepoSync` object. Config Sync then keeps the deployment in sync with the specified chart version and configurations.

## Choosing a source type

The best source type depends on your team's existing tools, workflows, and preferences. You can use this table to understand the key characteristics of each source type to help you make an informed decision:

Feature | Git repository | OCI image | Helm chart  
---|---|---|---  
Best for | General purpose configuration management; flexibility; human-readability | Immutable, versioned configurations; leveraging container infrastructure | Packaging and distributing complex applications  
Mutability | Mutable | Immutable | Mutable (chart versions are immutable, but values can change)  
Rollbacks | Revert commits or change branches | Deploy previous image tag | Rollback to a previous chart version  
Tooling | Standard Git clients, CI/CD pipelines | Docker or Podman, container registries | Helm CLI, Helm repositories  
Performance | Can be slower for large repositories | Faster, especially at scale | Fast when fetching from a chart repository  
Authentication | Flexible (SSH, token), can be more complex to set up | Simplified with Workload Identity Federation for GKE (for example, with Artifact Registry) | Simplified with Workload Identity Federation for GKE (for example, with Artifact Registry)  
  
It's also possible to use different source types for different purposes on the same cluster. For example, a cluster might have the following:

  * A `RootSync` syncing from a **Git repository** containing base cluster-wide resources and policies managed by the platform team.
  * A `RepoSync` in a specific namespace syncing from a **Helm chart** to deploy a Redis instance managed by an application team.
  * Another `RepoSync` in a different namespace syncing from an **OCI image** containing a set of application-specific configurations built by a separate CI/CD process.



## What's next

  * Learn about [GitOps best practices](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/gitops-best-practices).
  * [Install Config Sync with default settings](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/install-default).
  * [Configure syncing from Git](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/tutorials/config-sync-multi-repo).
  * [Sync OCI artifacts from Artifact Registry](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/sync-oci-artifacts-from-artifact-registry).
  * [Sync Helm charts from Artifact Registry](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/sync-helm-charts-from-artifact-registry).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
