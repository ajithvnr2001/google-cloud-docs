---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/fleet-features/
title: Plan fleet features \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:22.233583+00:00
---

# Plan fleet features  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/fleet-features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Plan fleet features Stay organized with collections  Save and categorize content based on your preferences. 

An important part of planning for fleets is deciding which fleet-enabled features you want to use. In particular if you are working with existing clusters and production workloads, you might want to identify fleet features that can be immediately adopted with minimal friction or risk to your existing applications, while planning for other features that might require more gradual or careful adoption. This guide describes the different types of features enabled by using fleets and their requirements, and gives some practical guidance on feature adoption. 

This guide is for Cloud architects who want to get started with fleets in their organizations. Before reading this guide, ensure that you're familiar with our [Fleet management overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs) and [Plan fleet resources](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/plan-fleets), which discusses organizing new or existing clusters into fleets.

## Best practices for feature adoption

All fleet features (except basic fleet observability) are opt-in, in that you need to specify that you want to use them. Just adding an existing cluster to a fleet does not change its configuration. When you do decide to use fleet features, some features can be enabled immediately with minimal risk, but you might need to approach some features with more care. This section provides some guidance for feature adoption.

Particularly with existing clusters and workloads, you need to be especially careful where features use _sameness_. This is a fleet concept where namespaces, services, or identities _with the same name_ across different clusters are assumed by the feature to _be the same thing_. You can read more about the principle of sameness and which features use it in [How fleets work](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts#sameness).

### Onboarding low risk features

The following "ambient" features don't assume any type of sameness and don't affect clusters in any way. They can all be safely used even with existing workloads and clusters, letting you immediately benefit from enhanced observability and security insights across your fleet, as well as the ability to manage the order of cluster upgrades based on fleet membership.

  * [Fleet-based rollout sequencing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-rollout-sequencing)
  * [Fleet observability](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/enterprise-overview-dashboard)
  * [Security posture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard)



The following features are installed on individual clusters. The features _can_ assume sameness, but only when configuring or specifying resources across multiple clusters. This means you can safely enable these features on your clusters with existing workloads, and only need to consider sameness when creating or using configurations for them that use these optional selectors.

  * [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview). You might need to consider sameness if you want to use optional [namespace](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/namespace-scoped-objects) and [team scope](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-tenancy) selectors.
  * [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview). You might need to consider namespace, identity, or service sameness if you want to use optional [scoped rules](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console#add-specific-rules-asm).
  * [Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview). You might need to consider namespace sameness if you want to [exclude namespaces from enforcement](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/policy-controller-exclude-namespaces#exempt_namespaces_from_enforcement).



### Onboarding advanced multi-cluster features

The following powerful features reduce the operational overhead of managing multiple clusters. However, greater care needs to be taken with these features, as they all require an assumption of one or more types of sameness to work, and enabling or disabling them can affect multiple clusters and their workloads.

  * [Fleet Workload Identity Federation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity)
  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview)
  * [Multi-cluster Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways)
  * [Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress)
  * [Fleet team management](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/team-management)



For example, if you have existing Kubernetes namespaces with the same name in different clusters and applications (including the default namespace), you should check that you want to have them treated as the same namespace before enabling any features that make this assumption. Similarly, if you want to use Cloud Service Mesh, you should understand which service endpoints will be merged across your clusters, and confirm that this is wanted behavior.

#### Audit namespace sameness

If you know your applications well, then you can audit your namespaces just by verifying that no two "different" applications use the same namespace. In particular, look out for ad hoc use of the default namespace. For example, if you have a namespace called `default` in one cluster, and a namespace called `default` in another cluster, but they are used for different purposes, then you should rename one of them.

For a more rigorous approach, try the following. For each set of same-named namespaces across different clusters of a fleet, check that:

  * in every cluster, the same RBAC rules are in the cluster and the namespace of principals is allowed access to the namespace.
  * the set of images used by Pods (minus hash/tag) is the same.
  * the set of Secrets used by the Pods is identical.



If all of these are true, then the namespaces are sufficiently similar to treat as "the same".

If your namespaces are not sufficiently similar, you can migrate apps to new namespaces. Once you are happy to assume namespace sameness, you can turn on features that use it.

#### Audit service sameness

If you would like to adopt Cloud Service Mesh to manage your microservice-based applications, another issue to consider is service sameness. This means that for any combination of namespace and service name, Cloud Service Mesh will treat them as the same logical service in terms of:

  * **Identity** (specifically for Cloud Service Mesh security): if `namespace1/service1` is authorized to do something, workloads with that identity from any cluster are authorized.
  * **Traffic management** : by default, traffic is load balanced across `namespace1/service1` services in any cluster.
  * **Observability** : metrics for `namespace1/service1` in all clusters are aggregated together.



If you are enabling Cloud Service Mesh with new clusters and applications, we recommend reserving unique namespace/service name combinations across your entire mesh. For existing applications, audit your services to ensure that services with the same namespace and name across your clusters are those that you would like to be treated as the same service in terms of identity, traffic management, and observability.

In particular, make sure that logically different services (for example, a payment accounting API and payment transaction API) don't use the same [namespace, name] pair (for example `payments/api`) because they will be treated as the same service once they are in a service mesh. This conceptual joining occurs even across regional boundaries. Moreover, the function of the services might be impacted.

Service namespace/name sameness is also assumed by Multi Cluster Ingress and multi-cluster Gateway when directing traffic to services across multiple clusters, though only for services that are exposed outside the clusters.

#### Consider workload identity

A powerful fleet feature is fleet-wide Workload Identity Federation. This extends the capabilities provided in Workload Identity Federation for GKE, which lets the workloads in your cluster authenticate to Google without requiring you to download, manually rotate, and generally manage Google Cloud service account keys. Instead, workloads authenticate using short-lived tokens generated by the clusters, with each cluster added as an identity provider to a special workload identity pool. Workloads running in a specific namespace can share the same Identity and Access Management identity across clusters.

While regular Workload Identity Federation for GKE uses a _project-wide_ identity pool, fleet-wide Workload Identity Federation uses a workload identity pool _for the entire fleet_ , even if the clusters are in different projects, with implicit sameness for identities across the fleet as well as namespace and service sameness. This makes it simpler to set up authentication for your applications across projects, but can have access control considerations over and above those for regular Workload Identity Federation for GKE if you choose to use it in multi-project fleets, particularly if the fleet host project has a mixture of fleet and non-fleet clusters.

To find out more about fleet Workload Identity Federation and how to use it to access Google Cloud services, see [Use fleet Workload Identity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/use-workload-identity). For guidance on minimizing risk with fleet Workload Identity Federation with some examples, see [Best practices for using fleet Workload Identity](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/best-practices-workload-identity).

## Fleet-level defaults

GKE provides the ability to set fleet-level defaults for certain features, including Cloud Service Mesh, Config Sync, and Policy Controller. This helps you set up clusters to use these features without having to configure each cluster individually. For example, an administrator can enable Policy Controller for their fleet and set default policies at the fleet level. This installs the required agent in new fleet member clusters and applies default policies to them.

However, these defaults only apply automatically to _new clusters_ that you add to the fleet at cluster creation time. Existing clusters and their workloads are not affected, even if you have already added them to the fleet, or if you add the clusters after you set up your feature defaults. This means that you can safely set up fleet-level defaults without risking enabling or configuring features on clusters where you're not ready to do so. You can always choose to apply the default settings to existing clusters later.

## Feature requirements

There are some limitations to consider when implementing fleets based on the fleet features that your organization wants to use. For example, some features don't support working with clusters that aren't in the fleet host project, while others are not supported on clusters outside Google Cloud.

The following table shows each component's current requirements and limitations, with some specific guidelines in the following sections.

Feature  
| Cluster types  
| Project requirements  
| VPC requirements  
---|---|---|---  
Config Sync | All GKE supported clusters | None | None  
Policy Controller | All GKE supported clusters | None | None  
Cloud Service Mesh | See [limitations](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed#limitations) | All clusters used with Cloud Service Mesh that are in the same project must be registered to the same fleet. For more information, see [Cloud Service Mesh fleet requirements](https://docs.cloud.google.com/service-mesh/docs/onboarding/kubernetes-off-gcp/install/cloud-service-mesh-prerequisites#fleet_requirements). | GKE clusters must be in the same VPC network.  
Multi-cluster Services (MCS) | GKE on Google Cloud | None | See [MCS on Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services#shared_vpc_metadata)  
Multi Cluster Ingress and multi-cluster Gateway | GKE on Google Cloud | Ingress/Gateway resources, GKE clusters, and fleet must be in the same project. | Ingress/Gateway resources and GKE clusters must be in the same VPC network.  
Workload identity pools | Optimized for GKE on Google Cloud and Google Distributed Cloud on VMware. Other Kubernetes clusters are supported, but require additional setup work. | None | None  
Binary Authorization | GKE on Google Cloud, Google Distributed Cloud on VMware, Google Distributed Cloud on bare metal | None | None  
Advanced Vulnerability Insights | GKE on Google Cloud | None | None  
Security Posture | GKE on Google Cloud | None | None  
Compliance Posture | GKE on Google Cloud | None | None  
Fleet resource utilization metrics | GKE on Google Cloud | None | None  
Fleet logging | All | None | None  
Connect gateway | All | None | None  
Fleet team management | All | None | None  
Pod FQDN Network Policies | GKE on Google Cloud | None | None  
Inter-node transparent encryption | GKE on Google Cloud | None | None  
Config Controller | Not applicable | None | None  
Rollout Sequencing | GKE on Google Cloud | None | None  
  
### Consider Virtual Private Cloud requirements

If you plan to use a feature such as Cloud Service Mesh that requires clusters to be in a single [Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs/overview) network, as shown in the previous table, you should create a fleet for each VPC. If not planning to use those features, then multiple VPCs can be put into one fleet.

For example, one common pattern is that an organization has several projects, each with its own default VPC. These might possibly have existing peering connections between each other. If you're not using a feature with single-VPC requirements, these can all be put into a single fleet. Another common pattern follows a "hub and spoke" topology, which uses several VPCs. If you're not using a feature with single-VPC requirements, then you can place clusters from all those VPCs into one fleet. Be aware that in some cases following these guidelines might result in you having fleets that have only one cluster! In that case, you might need to forego using features with VPC restrictions and create multi-project fleets, or reconsider your architecture and move workloads around, as appropriate.

### Requirements for multi-cluster networking

If you want to use Multi Cluster Ingress or multi-cluster Gateways for traffic management then be aware that in both cases the gateway controller can't span projects. This means that all the clusters you want to use with these features need to be in the same project as well as the same fleet. If you need to create fleets that include clusters from multiple projects, you can use single cluster Gateways instead, and direct traffic to the right Gateway some other way (for example, by using DNS). Clusters that use these features also need to be in the same VPC network.

## What's next

  * Learn more about managing fleet features in [Manage fleet-level features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/manage-features).
  * Learn more about how fleets work in [How fleets work](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
