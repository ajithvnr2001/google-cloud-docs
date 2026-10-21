---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview/
title: Config Sync overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:47.693186+00:00
---

# Config Sync overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Config Sync overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of Config Sync, the GitOps service included with Google Kubernetes Engine.

Adopting [GitOps](https://opengitops.dev/) as a universal best practice helps organizations manage Kubernetes configuration at scale. By using a central source of truth like a Git repository, you can improve stability, consistency, and security.

**Key Term:** **GitOps** is an approach to managing infrastructure and application configuration by using a version control system like Git as the single source of truth.

Config Sync helps you implement GitOps by automating the synchronization of your configuration and policies across any number of clusters. Automatic syncing lets you manage fleets of clusters centrally, prevent configuration drift, and empower both platform and application teams.

This page is for Operators who want to implement [GitOps](https://opengitops.dev/) tools to centralize configuration management for their teams. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Pricing

For information about pricing, see [GKE pricing](https://cloud.google.com/kubernetes-engine/pricing). 

## Why choose Config Sync for GitOps on GKE?

Although all GitOps tools provide benefits like improved stability and consistency, Config Sync provides a set of unique advantages:

  * **Integration with GKE and other Google Cloud products** : Config Sync is compatible with the Google Cloud console, Terraform, or Google Cloud CLI. Config Sync extends the functionality of GKE and works well with services like Policy Controller, Workload Identity Federation for GKE, and Cloud Monitoring. The built-in integration helps you set up GitOps and eases the maintenance burden required for open-source alternatives.

  * **Built-in observability** : Config Sync includes a dashboard in the Google Cloud console that requires no extra setup. You can view the sync status of all your clusters and configs from a central location, or use the Google Cloud CLI to check for reconciliation issues.

  * **Scalable multi-cluster and multi-team management** : Config Sync is designed for both centralized platform administration and delegated application management. Its architecture is tested to be horizontally and vertically scalable, letting you manage clusters at scale and empower your application teams to safely manage their own environments. 




## How Config Sync works

Config Sync continuously monitors a central source of truth and automatically reconciles the state of your clusters to match it. You can use a Git repository, OCI image, or Helm chart as your source of truth.

The following diagram shows an overview of how a platform administrator can manage central policies while three application operators manage their own namespace configurations. The namespaces all have the same admin configuration, but each namespace has a different application configuration.

![A central administrator controlling multiple configs and app operators controlling their own namespace configs.](https://docs.cloud.google.com/static/kubernetes-engine/config-sync/docs/img/multi-repo.png)

### Configuring clusters

Config Sync lets you create a common set of configuration and policies, such as [Policy Controller constraints](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview#constraints), and consistently apply them across registered and connected clusters from a single source of truth.

Instead of repeatedly running the `kubectl apply` command manually, you can orchestrate configuration changes across fleets of clusters.

### Configuring namespaces

You can use Config Sync to provision and manage Kubernetes namespaces with namespace-scoped policies, such as [RBAC roles](https://kubernetes.io/docs/reference/access-authn-authz/rbac/). These policies can help you implement and manage [multi-tenancy](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy) within your clusters, letting application teams to manage their own configurations safely.

## What's next

  * [Quickstart: Sync from a Git repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/tutorials/config-sync-multi-repo)
  * [Install Config Sync with default settings](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/install-default)
  * [Review GitOps best practices](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/gitops-best-practices)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
