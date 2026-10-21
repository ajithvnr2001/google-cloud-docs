---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-services/
title: Multi-cluster Services \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:10.361578+00:00
---

# Multi-cluster Services  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Multi-cluster Services Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides you with an overview of how GKE multi-cluster Services (MCS) works. To learn how to use MCS, see [Configuring multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services).

## Overview of MCS

Kubernetes' familiar [Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) object lets you discover and access a Service within the confines of a single Kubernetes cluster. However, sometimes you might want to split applications into multiple clusters, to address state management, privacy, scalability, availability, and data sovereignty requirements. With MCS, you can build Kubernetes applications that span multiple clusters.

MCS is a cross-cluster Service discovery and invocation mechanism for Google Kubernetes Engine (GKE) that leverages the existing Service object. Services enabled with this feature are discoverable and accessible across clusters with a virtual IP, matching the behavior of a [ClusterIP Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#services_of_type_clusterip) accessible in a cluster. Just like your existing Services, MCS is compatible with community-driven and open APIs, ensuring your workloads remain portable.

MCS is a feature of GKE. MCS configures Cloud DNS zones and records for each exported Service in your [fleet clusters](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs). A fleet lets you logically group and normalize your GKE clusters, making administration of infrastructure easier and enabling the use of multi-cluster features such as MCS. You can learn more about the benefits of fleets and how to create them in the [fleet management documentation](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs).

Exported Services regardless of type always have one Cloud DNS record, and exported Headless type services have records for each backend Pod with a hostname, including Pods in StatefulSets. Using Cloud DNS incurs additional charges. You are billed according to [Cloud DNS pricing](https://cloud.google.com/dns/pricing).

To export a Service with MCS, create a ServiceExport custom resource using the same namespace and name as the Service. MCS automatically imports the Service to each cluster in the fleet. When MCS imports a Service, it creates:

  * A ServiceImport custom resource using the same namespace and name as the Service.
  * An Endpoints object using the same namespace as the Service and a random name.



## Benefits of using MCS

Using MCS provides you with the following benefits:

  * **High availability** : Running the same Service across clusters in multiple regions provides you with improved fault tolerance. If a Service in a cluster is unavailable, the request can fail over and be served from other clusters. With MCS, it's possible to manage the communication between Services across clusters, to improve the availability of your containerized applications.
  * **Stateful and stateless Services** : Stateful and stateless Services have different operational dependencies and complexities and present different operational tradeoffs. Typically, the absence of state management makes it easier to scale, upgrade, and migrate a workload with higher availability. MCS lets you separate clusters for stateful and stateless workloads and make them independent, isolated, and easier to manage.
  * **Shared Services** : It's common to create separate Kubernetes clusters to get higher availability, better management of stateful and stateless Services, and easier compliance with data sovereignty requirements. However, many Services such as [monitoring with Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) or [using secrets management with Vault](https://www.cloudskillsboost.google/focuses/1210?parent=catalog) are often shared among all clusters. Instead of each cluster requiring its own local Service replica, MCS makes it easier to set up common shared Services in a separate cluster that all functional clusters use.
  * **Migration** : Modernizing an existing application into a containerized microservice-based architecture often requires you to deploy Services across multiple Kubernetes clusters. MCS provides you with a mechanism to help bridge the communication between those Services, making it easier to migrate your applications. This is especially helpful as you can deploy the same Service to two different clusters and traffic is allowed to shift from one cluster or application to another.



## What's next

  * Learn more about [configuring multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-services).
  * Read an overview of [Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress).
  * Learn how to [choose a multi-cluster load balancing solution](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-mc-lb-api).
  * Learn about [fleet management](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs).
  * Read about [migrating to GKE multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-gke-multi-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
