---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/connecting-to-a-cluster/
title: Connecting to a cluster from the Google Cloud console \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:10:59.081182+00:00
---

# Connecting to a cluster from the Google Cloud console  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/connecting-to-a-cluster/

**Version 1.7**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.7 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/overview)



Send feedback 

#  Connecting to a cluster from the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

With Connect, you can use the Google Cloud console to manage your user clusters for Google Distributed Cloud.

## Before you begin

Create a user cluster ([quickstart](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/user-cluster-quickstart) | [full instructions](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/how-to/create-user-cluster)).

## Cluster registration

Each Google Distributed Cloud user cluster that you create automatically runs the Connect agent and is registered with Connect to your project fleet—a unified way to view and manage multiple clusters and their workloads as part of GKE Enterprise. You can find out more about fleets and the functionality that they enable in our [Fleets guide](https://docs.cloud.google.com/anthos/multicluster-management/fleets).

Registered clusters are visible in your [GKE Enterprise Clusters page](https://console.cloud.google.com/anthos/clusters/) in the Google Cloud console and can be used with GKE Enterprise components and features.

If you need to manually register a Google Distributed Cloud cluster with Connect (for example, if you want to move the cluster's membership to a different fleet, or if you unregistered it by mistake), follow the instructions in [Registering a cluster](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster).

## Logging into your cluster

To manage a registered Google Distributed Cloud cluster from the Google Cloud console, you need to log into the cluster from the console. Doing this lets you view, monitor, debug, and manage workloads on your Google Distributed Cloud clusters through the Google Cloud console.

Follow the instructions in [logging into clusters](https://docs.cloud.google.com/anthos/multicluster-management/console/logging-in) to create the necessary roles and accounts and log in to your cluster.

## What's next

  * Learn about multi-cluster management with [Connect](https://docs.cloud.google.com/anthos/multicluster-management/connect/overview).

  * Learn about cluster authentication with [OpenID Connect (OIDC)](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/concepts/authentication).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
