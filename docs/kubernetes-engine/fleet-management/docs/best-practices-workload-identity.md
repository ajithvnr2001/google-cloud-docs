---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/best-practices-workload-identity/
title: Reduce identity sameness risks in multi-tenant fleets \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:05.955828+00:00
---

# Reduce identity sameness risks in multi-tenant fleets  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/best-practices-workload-identity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Reduce identity sameness risks in multi-tenant fleets Stay organized with collections  Save and categorize content based on your preferences. 

This page provides best practices for configuring and using fleet Workload Identity Federation, which is a fleet feature that lets you centrally set up authentication from applications to Google Cloud APIs across projects. For best practices around adopting other fleet features, see [Plan fleet features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/fleet-features). 

This page is for Platform admins and operators and for Security engineers who want to minimize the risks associated with identity sameness in fleets.

Before reading this page, ensure that you're familiar with the concepts in [About fleet Workload Identity Federation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/about-fleet-workload-identity-federation).

## Terminology

This page uses the following terminology:

  * **Workload Identity Federation for GKE** : a feature that provides identities to GKE workloads in a single Google Cloud project.
  * **Fleet Workload Identity Federation** : a feature that extends Workload Identity Federation for GKE to workloads across the entire fleet, including outside of Google Cloud and across multiple projects.
  * **Workload identity pool** : an entity that provides identities to workloads in a format that's compatible with Identity and Access Management (IAM). Each cluster is an identity provider in a workload identity pool.



## Identity sameness in fleets

Workload identity pools are entities that provide identities to workloads in a format that IAM can use when authenticating and authorizing requests. With Workload Identity Federation for GKE, every project has a fixed, Google-managed workload identity pool by default that's unique to that project.

With fleet Workload Identity Federation, the Google-managed workload identity pool for the fleet host project is the default workload identity pool for all clusters that you register to the fleet, regardless of whether the clusters are in other projects or other clouds. You can optionally set up a self-managed workload identity pool for specific clusters to use instead of the default pool.

**Preview — self-managed workload identity pools**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

In both fleet Workload Identity Federation and Workload Identity Federation for GKE, you use IAM allow policies to grant roles on specific Google Cloud resources to entities in your clusters, such as Kubernetes ServiceAccounts or Pods. In your allow policies, you refer to these entities by using a _principal identifier_ , which is a naming syntax that IAM can read. The principal identifier includes the name of the workload identity pool that the cluster uses and other information that selects the specific entities in the cluster. For example, the following principal identifier selects a Kubernetes ServiceAccount in a namespace:
    
    
    principal://iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/WORKLOAD_IDENTITY_POOL_NAME/subject/ns/NAMESPACE/sa/SERVICEACCOUNT
    

In this example, the following fields have information about the principal:

  * `PROJECT_NUMBER`: the project number of the fleet host project.
  * `WORKLOAD_IDENTITY_POOL_NAME`: the name of the workload identity pool.
  * `NAMESPACE`: the name of the namespace.
  * `SERVICEACCOUNT`: the name of the Kubernetes ServiceAccount.



Requests to Google Cloud APIs are authenticated by using short-lived OAuth 2.0 access tokens that clusters generate. These access tokens include the principal identifier of the entity that created the request. IAM uses the principal identifier to ensure that an allow policy authorizes the entity to perform the requested operation.

### Identity sameness implications for multi-tenant fleets

The principal identifier results in _identity sameness_ , which means that any entity in the environment that matches a specific principal identifier is considered by IAM to be the same thing. With single-project Workload Identity Federation for GKE, identity sameness applies to all entities that share a principal identifier in that project. However, with fleet Workload Identity Federation, this identity sameness applies to all entities that share a principal identifier _across the entire fleet, regardless of the cluster project_.

For example, with the principal identifier in the preceding section, requests from Pods that use the same ServiceAccount, the same namespace, and the same workload identity pool get the same principal identifier regardless of the cluster or project.

If your fleet only runs clusters in the fleet host project, the identity sameness implications are the same as for Workload Identity Federation for GKE. However, if your fleet has clusters that run in other projects, the identity sameness extends to all of the registered clusters in the fleet.

## Example complexities for fleet identity sameness

The following example scenarios describe potential identity sameness complexities that can occur when you implement fleet Workload Identity Federation. Each scenario provides you with possible mitigations that might help you to navigate these complexities.

### Single project fleet with all clusters registered and the same workload identity pool

Consider the following fleet configuration:

  * All of the fleet's member clusters are in the fleet host project.
  * All of the clusters in the project are members of the fleet.
  * All of the clusters use the same workload identity pool.



In this scenario, all the fleet's member clusters are in the fleet host project, and all of the clusters in that project are members of the fleet.

![Diagram showing a project with all clusters in the same fleet](https://docs.cloud.google.com/static/kubernetes-engine/fleet-management/images/simple_fleet.svg)

As described in the Identity sameness implications for fleets section, using fleet Workload Identity Federation in this scenario is the same as using Workload Identity Federation for GKE, and there is no additional risk.

### Single project fleet with some clusters registered and the same workload identity pool

Consider the following fleet configuration:

  * The fleet contains two clusters, both of which run in the fleet host project.
  * The fleet host project contains a third cluster that is not a fleet member.
  * The cluster that isn't a fleet member also has Workload Identity Federation for GKE enabled.
  * All of the clusters in the project use the same workload identity pool



![Diagram showing a project with some clusters in the same fleet.](https://docs.cloud.google.com/static/kubernetes-engine/fleet-management/images/complicated_fleet.svg)

With this configuration, any roles that you grant to an entity in one cluster in the project apply to other entities in the project that match the principal identifier. This might result in unintentionally giving permissions to entities that aren't a part of the fleet. For example, granting a role to a principal identifier that selects a specific service account in a namespace has the following implications:

  * Workloads that run in the specified namespace and use the specified service account in the fleet member clusters share the access.
  * Workloads that run in the third non-member cluster that use the same namespace and service account name _also_ get the same access.



The following suggestions might help to solve this complexity:

  * Configure the fleet member clusters to use a self-managed workload identity pool. This ensures that entities in the fleet member clusters have different principal identifiers from the non-member cluster. For details, see [Authenticate to Google Cloud APIs from mixed-trust fleet workloads](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/authenticate-mixed-trust-workloads).
  * Create a dedicated fleet host project and use organization policies to prevent the dedicated fleet host project from running clusters. This separates the fleet-wide workload identity pool trust domain from the GKE project-level trust domains. Only registered clusters share the fleet-wide workload identity pool.

These suggestions work for clusters on Google Cloud and attached clusters.




### Multi-project fleet with some clusters registered and the same workload identity pool

Consider the following fleet configuration:

  * The fleet contains member clusters that run in two Google Cloud projects: `project-1` and `project-2`.
  * `project-1` is the fleet host project. All of the clusters in `project-1` are fleet members.
  * `project-2` contains one fleet member cluster and one unregistered cluster.
  * All of the clusters in `project-1` use the Google-managed workload identity pool of the project, which is also the default fleet-wide workload identity pool.
  * The fleet member cluster in `project-2` uses the fleet-wide workload identity pool.



![Diagram showing a fleet with clusters from two projects.](https://docs.cloud.google.com/static/kubernetes-engine/fleet-management/images/two_project_fleet.svg)

In this scenario, any permissions that you give to entities in the fleet host project also apply to entities in the member cluster from `project-2`, because they all share the same workload identity pool.

To try and solve this complexity, create a dedicated Google Cloud project to use as the fleet host project. The fleet member clusters in `project-1` and in `project-2` then share the dedicated project's workload identity pool by default. You can then grant project-scoped access to clusters in `project-1` by using the workload identity pool for `project-1` in the principal identifier.

## Prevent creation of similar identities

Identity sameness in fleets requires that you carefully implement access control to prevent intentional or unintentional creation of similar identities. For example, consider a scenario in which you grant access to all Pods that use a specific ServiceAccount in a namespace. If someone creates that namespace and ServiceAccount in a different fleet member cluster, Pods in that cluster get the same access.

To reduce the chances of this issue, use an authorization mechanism to only allow a trusted set of users to create, update, or delete namespaces and Kubernetes service accounts.

  * For IAM, the following permissions provide this access:

    * `container.namespaces.*`
    * `container.serviceAccounts.*`
  * For Kubernetes role-based access control (RBAC), the following example ClusterRoles configure special access to interact with these Kubernetes resources:
        
        apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRole
        metadata:
          name: namespace-admin
        rules:
        - apiGroups: [""]
          resources: ["namespaces"]
          verbs: ["create","delete","update","patch"]
        ---
        apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRole
        metadata:
          name: serviceaccount-admin
        rules:
        - apiGroups: [""]
          resources: ["serviceaccounts"]
          verbs: ["create","delete","update","patch","impersonate"]
        




## What's next

  * [Manage fleet-level features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/manage-features)
  * [Secure your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/secure)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
