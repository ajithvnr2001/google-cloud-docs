---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview/
title: Config Sync overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:20:20.030001+00:00
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

## Benefits of Config Sync

Config Sync provides the following key GitOps advantages for managing your Kubernetes clusters:

  * **Consistency across environments** : By using a central source of truth like a Git repository, you can ensure that your cluster configurations and policies remain stable and consistent across all your environments.
  * **Automated reconciliation** : Config Sync continuously monitors your source of truth and automatically reconciles the state of your clusters to match it, preventing configuration drift and saving manual effort.
  * **Version-controlled configuration** : Storing your Kubernetes manifests in Git lets you leverage standard version-control workflows, including peer reviews, audit trails, and easy rollbacks. 



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

  * [Install Config Sync manually using kubectl](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-kubectl)
  * [Review GitOps best practices](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/gitops-best-practices)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
