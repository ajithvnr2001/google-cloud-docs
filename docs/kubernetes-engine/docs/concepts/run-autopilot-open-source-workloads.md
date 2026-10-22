---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/run-autopilot-open-source-workloads/
title: Run privileged open source workloads on GKE Autopilot \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:22.601083+00:00
---

# Run privileged open source workloads on GKE Autopilot  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/run-autopilot-open-source-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Run privileged open source workloads on GKE Autopilot Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This page shows you how to run privileged open-source workloads on Google Kubernetes Engine (GKE) Autopilot. This page is for Platform engineers who want to run specific open source applications in Autopilot nodes. 

## About allowlists for privileged Autopilot workloads

By default, GKE Autopilot enforces security constraints that reject workloads that need elevated privileges in the cluster. For example, you can't, by default, run a Pod that enables privileged mode or adds the `NET_RAW` Linux capability.

You can optionally run a specific set of privileged workloads from [Autopilot partners](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners) and from certain open source projects in Autopilot mode. 

To deploy privileged open source workloads in Autopilot mode, you do the following:

  1. Install an _allowlist_ for the workload by deploying an `AllowlistSynchronizer` object. The AllowlistSynchronizer installs the allowlist as a `WorkloadAllowlist` object and manages its lifecycle. For instructions, see [Run privileged workloads from GKE Autopilot partners](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-autopilot-partner-workloads).
  2. Deploy the privileged open source workload in your cluster by following the installation steps in the project's documentation.



## Privileged open source workloads with Autopilot support

The following table describes the privileged open source workloads that you can run on Autopilot. To enable a workload, [create an `AllowlistSynchronizer` resource](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/run-autopilot-partner-workloads#create-allowlistsynchronizer) with the path to the allowlists for that workload in the `allowlistPaths` field.

Privileged open source workloads for Autopilot | Allowlist path  
---|---  
[Grafana Alloy](https://grafana.com/docs/alloy/latest/) |  `Grafana/alloy/*`  
[Grafana Beyla](https://grafana.com/oss/beyla-ebpf/) |  `Grafana/beyla/*`  
  
This table describes only the open-source workloads that need elevated privileges and are supported on Autopilot. Open-source software that requires elevated privileges and is not listed in this table might not work on Autopilot. If an open source application doesn't violate the default security constraints in Autopilot, you can run the application without an allowlist.

## What's next

  * [AllowlistSynchronizer CustomResourceDefinition](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/allowlistsynchronizer)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
