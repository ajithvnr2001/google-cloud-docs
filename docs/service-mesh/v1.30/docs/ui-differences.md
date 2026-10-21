---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/ui-differences/
title: GKE Enterprise and Cloud Service Mesh UI differences \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:28:06.756416+00:00
---

# GKE Enterprise and Cloud Service Mesh UI differences  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/ui-differences/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GKE Enterprise and Cloud Service Mesh UI differences

While you can use Cloud Service Mesh without subscribing to GKE Enterprise, certain UI elements and features in Google Cloud console are only available to GKE Enterprise subscribers. This page explains what is available to subscribers and non-subscribers.

## Dashboard

You can use the Dashboard to view an overview of your Cloud Service Mesh resources.

Card | Cloud Service Mesh | GKE Enterprise  
---|---|---  
Service mesh | ✓ | ✓  
Cluster status |  | ✓  
Config status |  | ✓  
Policy status |  | ✓  
GKE Enterprise total project cost |  | ✓  
  
  * The Service mesh card displays the health status and lists the number of Services running in your Service mesh.
  * The Cluster status card displays the health status and lists the number of clusters running in your project.
  * The Config status card displays the health and package status of Config Sync.
  * The Policy status card displays how many clusters have Policy Controller installed.
  * The GKE Enterprise total project cost displays the total cost for every GKE Enterprise feature in your project.



[Go to the Dashboard](https://console.cloud.google.com/anthos)

## Config Sync

If you have a GKE Enterprise subscription, you can use the [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/concepts/config-sync) page to view a list of clusters in your current project that includes each cluster's name, sync status, sync date, sync branch, sync tag, and commit ID. You can also view and update Config Sync settings for your clusters.

[Go to the Config Sync page](https://console.cloud.google.com/anthos/config_management)

## Policy Controller

If you have a GKE Enterprise subscription, you can use the [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller) page to view a list of clusters in your current project that includes an overview of your cluster's compliance with different standards, and your cluster's Policy Controller settings.

[Go to the Policy Controller page](https://console.cloud.google.com/anthos/policy_controller)

## Clusters

The Clusters page lists Anthos-managed clusters in your current project and includes each cluster's name, compute zone, type, and labels.

If you have an GKE Enterprise subscription, you can use this page to view, add, and register Google Cloud or external clusters.

If you don't have an GKE Enterprise subscription, you cannot view, add, or register clusters on the Clusters page. You can only [register clusters running on Google Cloud using gcloud](https://docs.cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster).

[Go to the Clusters page](https://console.cloud.google.com/anthos/clusters)

## Features

You can use the Features page to add and manage GKE Enterprise features available in your [fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets). Because this page is exclusively for GKE Enterprise features, it is only available to GKE Enterprise subscribers.

[Go to the Features page](https://console.cloud.google.com/anthos/features)

## What's next

  * [Explore GKE Enterprise with a sample Deployment](https://docs.cloud.google.com/anthos/docs/tutorials/explore-anthos)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
