---
url: https://docs.cloud.google.com/recommender/docs/insights/insight-types/
title: Insight types \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T05:43:51.677349+00:00
---

# Insight types  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/insights/insight-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Reference ](https://docs.cloud.google.com/recommender/docs/apis)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Insight types

Each insight has a specific _insight type_. Insight types are specific to a single Google Cloud product and resource type. A single product can have multiple insight types, where each provides a different type of insight for a different resource.

Supported insight types:

Name | Insight type ID  
---|---  
[Cloud Asset insights](https://docs.cloud.google.com/asset-inventory/docs/using-asset-insights) | `google.cloudasset.asset.Insight`  
[Dataflow insights](https://docs.cloud.google.com/dataflow/docs/guides/using-dataflow-insights) | `google.dataflow.diagnostics.Insight`  
[ Error Reporting notification insights](https://docs.cloud.google.com/recommender/docs/error-reporting/notification-recommender#view-er-insights) | `google.clouderrorreporting.Insight`  
[Firewall insights](https://docs.cloud.google.com/network-intelligence-center/docs/firewall-insights/how-to/using-firewall-insights) | `google.compute.firewall.Insight`  
[GKE diagnosis insights](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/viewing-deprecation-insights-and-recommendations) | `google.container.DiagnosisInsight`  
[IAM policy insights](https://docs.cloud.google.com/policy-intelligence/docs/policy-insights) | `google.iam.policy.Insight`  
[IAM service account insights science](https://docs.cloud.google.com/policy-intelligence/docs/service-account-insights) | `google.iam.serviceAccount.Insight`  
[Idle Compute Engine resources insights](https://docs.cloud.google.com/compute/docs/viewing-and-applying-idle-resources-recommendations#viewing_insights_for_idle_pd_recommendations) | 

  * `google.compute.disk.IdleResourceInsight`
  * `google.compute.image.IdleResourceInsight`
  * `google.compute.address.IdleResourceInsight`

  
[Lateral movement insights](https://docs.cloud.google.com/policy-intelligence/docs/lateral-movement-insights) | `google.iam.policy.LateralMovementInsight`  
[Managed instance group insights](https://docs.cloud.google.com/compute/docs/instance-groups/view-and-understand-mig-insights) | 

  * `google.compute.instanceGroupManager.CpuUsageInsight`
  * `google.compute.instanceGroupManager.CpuUsagePredictionInsight`
  * `google.compute.instanceGroupManager.CpuUsageTrendInsight`
  * `google.compute.instanceGroupManager.MemoryUsageInsight`
  * `google.compute.instanceGroupManager.MemoryUsagePredictionInsight`

  
[Network Analyzer insights](https://docs.cloud.google.com/network-intelligence-center/docs/network-analyzer/use-cli-recommender-api) | 

  * `google.networkanalyzer.vpcnetwork.ipAddressInsight`
  * `google.networkanalyzer.vpcnetwork.connectivityInsight`
  * `google.networkanalyzer.networkservices.loadBalancerInsight`
  * `google.networkanalyzer.container.ipAddressInsight`
  * `google.networkanalyzer.container.connectivityInsight`
  * `google.networkanalyzer.container.serviceAccountInsight`
  * `google.networkanalyzer.hybridconnectivity.dynamicRouteInsight`

  
[Unattended project insights](https://docs.cloud.google.com/recommender/docs/unattended-project-recommender#projectutilizationinsight) | `google.resourcemanager.projectUtilization.Insight`  
[VM instance insights](https://docs.cloud.google.com/compute/docs/instances/view-and-understand-vm-insights) | 

  * `google.compute.instance.CpuUsageInsight`
  * `google.compute.instance.CpuUsagePredictionInsight`
  * `google.compute.instance.CpuUsageTrendInsight`
  * `google.compute.instance.MemoryUsageInsight`
  * `google.compute.instance.MemoryUsagePredictionInsight`
  * `google.compute.instance.NetworkThroughputInsight`

  
[recent change insights](https://docs.cloud.google.com/recommender/docs/recent-change-recommendations) | `google.cloud.RecentChangeInsight`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
