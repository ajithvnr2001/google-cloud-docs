---
url: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation/
title: Posture management deprecations \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:59:22.398364+00:00
---

# Posture management deprecations  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Posture management deprecations Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes deprecations and removals for various security posture management and compliance posture management features in Google Kubernetes Engine (GKE) and GKE Enterprise. This information applies to you if you use any of the following features in the Google Cloud console:

  * [GKE security posture dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard)
  * GKE Compliance dashboard (Preview)



## About the posture management dashboards

GKE provides dashboards in the Google Cloud console to monitor the security posture of your GKE clusters and any compliance violations in your fleet. These dashboards support the following capabilities:

  * GKE security posture dashboard: monitor the security posture of GKE clusters and workloads. Supports the following features:

    * Kubernetes security posture - standard tier:

      * Workload configuration auditing
      * Actionable security bulletin surfacing (Preview)
    * Kubernetes security posture - advanced tier:

      * GKE threat detection (Preview) (GKE Enterprise only)
    * Workload vulnerability scanning - standard tier

    * Workload vulnerability scanning - Advanced Vulnerability Insights

    * Supply chain concerns - Binary Authorization (Preview)

  * GKE Compliance dashboard (Preview) (GKE Enterprise only): monitor the compliance status of your workloads against industry standards like the CIS Benchmarks for GKE.




## Deprecated features

Starting on January 28, 2025, specific posture management capabilities are deprecated. The following table lists the deprecated capabilities with deprecation dates, estimated removal dates, and links to learn more.

**Note:** There is no expected disruption to running clusters and workloads because of these deprecations. If you take no actions by the removal dates in the following table, you won't see new or existing findings for that scanning type in the Google Cloud console.Capability | Deprecation date | Removal date | Learn more  
---|---|---|---  
GKE threat detection (Preview) | January 28, 2025 | March 31, 2025 | GKE threat detection  
Supply chain concerns - Binary Authorization (Preview) | January 28, 2025 | March 31, 2025 | Supply chain concerns - Binary Authorization  
GKE Compliance dashboard (Preview) | January 28, 2025 | June 30, 2025 | Compliance dashboard  
Workload vulnerability scanning - standard tier | July 23, 2024 | July 31, 2025 | Workload vulnerability scanning  
Workload vulnerability scanning - Advanced Vulnerability Insights | June 16, 2025 | June 16, 2026 | Workload vulnerability scanning  
  
## What happens when a capability is removed?

After the removal date of a capability, the following changes occur:

  * The Google Cloud console no longer generates new results for the capability. For example, GKE doesn't generate new GKE threat detection results after March 31, 2025.
  * You can't view existing results in the corresponding posture management dashboard. For example, you can't view existing container OS vulnerability scan results for GKE standard edition clusters after July 31, 2025.
  * Security Command Center findings for the capability get the `Inactive` state. Findings are deleted after the [Security Command Center data retention period](https://docs.cloud.google.com/security-command-center/docs/concepts-data-security-overview#data_retention).



The logs for your findings remain in the `_Default` log bucket in Cloud Logging for the [log retention period](https://docs.cloud.google.com/logging/quotas#logs_retention_periods).

## What you should do

This section describes any available alternatives that you can use to get similar monitoring capabilities for your clusters and workloads.

### Workload vulnerability scanning

Both tiers of workload vulnerability scanning are deprecated. For more information, see [Workload vulnerability scanning removal in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/vulnerability-scanning-gkee).

### GKE threat detection

**Preview — GKE threat detection**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

GKE threat detection evaluated your audit logs against a set of rules for cluster and workload threats. Active threats were displayed in the Google Cloud console with information about how to remediate the threat.

GKE threat detection was powered by Security Command Center Event Threat Detection. To continue getting information from Security Command Center about active threats after March 31, 2025, see [Integration with Security Command Center](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard#scc-integration).

### Supply chain concerns - Binary Authorization

**Preview — supply chain concerns - Binary Authorization**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If you enabled the Binary Authorization API in a project, the GKE security posture dashboard displayed results for running container images that met any of the following criteria:

  * Images that used the `latest` tag implicitly or explicitly.
  * Images by digest that were uploaded to Artifact Registry or Container Registry (Deprecated) more than 30 days ago.



To continue monitoring your running containers for these issues after March 31, 2025, do the following:

  1. [Set up Binary Authorization in your cluster](https://docs.cloud.google.com/binary-authorization/docs/setting-up).
  2. [Enable the continuous validation image freshness check](https://docs.cloud.google.com/binary-authorization/docs/cv-freshness-check) (Preview).



Setting up Binary Authorization in a cluster prevents you from deploying Pods that don't specify a container image digest for every container. This helps ensure that workloads don't use the `:latest` tag or omit a tag.

### GKE Compliance dashboard

**Preview — GKE Compliance dashboard**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The GKE Compliance dashboard is a GKE Enterprise feature that lets you scan your clusters against predefined industry standards like the CIS Benchmarks for GKE.

Starting on June 30, 2025, the GKE Compliance dashboard no longer displays results for compliance violations in eligible clusters. You can't enable compliance auditing for new or existing clusters.

To get similar results for compliance violations, do the following:

  1. [Activate either the Premium or the Enterprise tier of Security Command Center](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview)
  2. [Assess and report compliance with security standards](https://docs.cloud.google.com/security-command-center/docs/compliance-management)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
