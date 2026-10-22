---
url: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/container-registry/
title: Transition from Container Registry to Artifact Registry in GKE \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:08.832876+00:00
---

# Transition from Container Registry to Artifact Registry in GKE  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/container-registry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Transition from Container Registry to Artifact Registry in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes how the upcoming shutdown of Container Registry, which begins on March 18, 2025, might impact Google Kubernetes Engine (GKE) workloads. This page provides information about the potential impact on your workloads and recommended migration steps. 

This information is for Admins and architects and Operators who store GKE container images in Container Registry.

## About the Container Registry shutdown

Container Registry was deprecated on May 15, 2023 and will be shut down starting on March 18, 2025. Artifact Registry is the recommended replacement for Container Registry. Artifact Registry provides the same container management features as Container Registry, and includes additional features and benefits.

For details about the shutdown, including the timeline, see [What happens after March 18, 2025](https://docs.cloud.google.com/artifact-registry/docs/transition/prepare-gcr-shutdown#what-happens-after-shutdown) in the Artifact Registry documentation.

## Impact of the shutdown on your workloads

Starting on March 18, 2025, you won't be able to write images to Container Registry repositories. Starting on June 03, 2025, GKE won't be able to read images that you store in Container Registry. This might result in workload disruptions.

Before March 18, 2025, transition your repositories from Container Registry to Artifact Registry. For instructions, see [Transition from Container Registry](https://docs.cloud.google.com/artifact-registry/docs/transition/transition-from-gcr).

## Impact of the shutdown on GKE-managed workloads

All GKE-managed workloads that run in your nodes have already transitioned to Artifact Registry. Artifact Registry supports `gcr.io` repositories as a Generally Available feature. No further action is required.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
