---
url: https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-considerations/
title: Learning Path: Scale applications - Production considerations \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:49.221816+00:00
---

# Learning Path: Scale applications - Production considerations  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-considerations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Learning Path: Scale applications - Production considerations Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

In this set of tutorials, some of the planning considerations are simplified so that you can focus on learning key Google Kubernetes Engine (GKE) features and services. Before you start to create your own Google Kubernetes Engine environment similar to the one described in this set of tutorials, there are some additional planning considerations to keep in mind. These considerations include the cluster management level, networking, and availability types.

## Networking

GKE clusters require careful IP address planning. The networking options that you choose impact the architecture of your GKE clusters. Some of these options can't be changed after they're configured without recreating the cluster.

In this set of tutorials, you use Autopilot mode clusters that always use VPC-native mode networking. VPC-native clusters use alias IP address ranges on GKE nodes, and are required for creating clusters on Shared VPCs. VPC-native clusters scale more easily than routes-based clusters without consuming Google Cloud routes and so are less susceptible to hitting routing limits.

Before you create your own GKE environment and deploy workloads, review the following networking guidance:

  * [GKE network overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview)
  * [Best practices for GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking)
  * [Plan IP addresses for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-ip-address-mgmt-strategies)



## Cluster modes

In this set of tutorials you create a regional GKE cluster that uses Autopilot mode. Autopilot clusters are pre-configured with an optimized cluster configuration that is ready for production workloads. You can alternatively use Standard mode clusters for more advanced configuration flexibility over the underlying infrastructure.

For a more comprehensive overview, review the planning documents that start with the [cluster configuration choices](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters).

## Namespaces

Namespaces let you organize your applications and isolate components from each other. Each namespace has its own set of resources, such as Pods, Services, and Deployments. For example, you can create a namespace for all your frontend services and a namespace for your backend services. This grouping makes it easier to manage your services and to control access to them.

In this set of tutorials, you deploy the Pods and Services for the Cymbal Bank sample application into a single namespace. This approach reduces deployment complexity, but doesn't let you use namespaces to assign resources to different teams and users, as you might do in a production environment. For a more secure and production-ready example of the Cymbal Bank sample application that uses multiple namespaces, see [Cymbal Bank application architecture](https://docs.cloud.google.com/architecture/enterprise-application-blueprint/cymbal-bank).

## Pod disruption budgets

Pod Disruption Budget (PDB) policies help ensure app performance by preventing Pods going down at the same time when you make a change to the system and limit the number of simultaneously unavailable Pods in a replicated application.

In this set of tutorials, you don't configure and use PDBs. When you complete the tutorial to simulate failure, your Services and nodes should all respond as expected. When you deploy your own workloads, PDBs on nodes might block node draining.

If you use PDBs, review your configuration before you try to cordon and drain nodes. If the nodes can't successfully drain, you might have problems with scheduled maintenance events.

## What's next

Get started by completing the [first tutorial to a deploy a single GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-basic-deployment) that runs a microservices-based application.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
