---
url: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/
title: Feature and API deprecations \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:39.286595+00:00
---

# Feature and API deprecations  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Feature and API deprecations Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how feature and API deprecations that are caused by Kubernetes and other dependencies work with Google Kubernetes Engine (GKE). This page also includes tables with information about specific upstream deprecations. To learn how to view your exposure to upcoming deprecations, see [Viewing deprecation insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/viewing-deprecation-insights-and-recommendations).

## What are Kubernetes deprecations?

GKE clusters are powered by the [Kubernetes](https://kubernetes.io/) open source cluster management system. The feature set of Kubernetes evolves over time, and just as new features are introduced over time, sometimes a feature might need to be removed. Or, a feature may [graduate](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#feature-stages) from the Beta phase to the GA phase. [Kubernetes deprecation policy](https://kubernetes.io/docs/reference/using-api/deprecation-policy/) a deprecated feature or API before it is removed.

After its deprecation period, when a feature or API is removed, you can no longer use it starting with the corresponding GKE minor version. If a cluster was dependent on a feature or API that was deprecated, functionality could be impaired.

### Deprecations caused by other upstream dependencies

Apart from Kubernetes features and APIs, GKE also provides features that are powered by other providers, such as Windows node images backed by Microsoft, and Ubuntu node images backed by Canonical. When these upstream providers deprecate or end support for a feature, GKE might have to remove the corresponding feature. The tables on this page also provide information about upcoming deprecations and removals that are caused by upstream dependencies apart from Kubernetes.

### How Kubernetes deprecations work with GKE

Running applications on GKE involves [shared responsibility](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility) between you and GKE.

As a user, you must assess and mitigate any exposure to deprecated features and APIs that are removed in upcoming Kubernetes minor versions. In the next sections, learn about how GKE makes this process easier by detecting usage of deprecated Kubernetes features and APIs, sharing insights about this usage, and providing recommendations about how to migrate to features and APIs compatible with upcoming minor versions.

If GKE detects that a cluster is using a feature that is removed in an upcoming minor version of Kubernetes, automatic cluster upgrades to the next minor version are paused, and GKE shares a deprecation insight and recommendation.

**Warning:** GKE cannot guarantee the detection of all usage of deprecated features or APIs, and cannot guarantee that upgrades will be paused. As part of the [shared responsibility](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility) model, you must review upcoming deprecations, assess your clusters for exposure, and mitigate any exposure to deprecations. To ensure that a cluster is not upgraded, use [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions).

#### What happens when GKE pauses automatic upgrades?

If GKE detects usage of a deprecated feature or API, GKE pauses [automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot#how_cluster_and_node_pool_upgrades_work) to prevent your cluster from being upgraded into a broken state. Upgrades to the next [Kubernetes minor version](https://docs.cloud.google.com/kubernetes-engine/versioning#versioning_scheme) are paused, but GKE continues to deliver [patch upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning#versioning_scheme) to the cluster on the current minor version. For example, if a cluster is on version 1.21.11-gke.1100 and has calls to deprecated APIs that are removed from version 1.22, GKE pauses the automatic upgrade to version 1.22. However, GKE does not pause the automatic upgrade to a new patch version, 1.21.11-gke.1900.

As GKE cannot guarantee that all usage is detected, GKE cannot guarantee that upgrades are always paused when a deprecated feature or API is used. To ensure that a cluster is not upgraded, you must use [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions).

#### When does GKE resume automatic upgrades?

Once GKE hasn't detected usage of the deprecated feature or calls to deprecated APIs for 30 days, the cluster is automatically upgraded if the next minor version is the auto-upgrade target for your cluster in the cluster's [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels), and your cluster doesn't have other factors preventing upgrades such as an active maintenance exclusion. To see when the minor version becomes an auto-upgrade target in your cluster's release channel, see the [release schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule_for_release_channels) for an estimated date, and the [release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) for the specific announcement. To get auto-upgrade targets for a specific cluster, see [Get information about a cluster's upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist#get-info).

If GKE continues to detect usage of the deprecated feature on the cluster, then GKE keeps the cluster on its current minor version until the version's [end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#lifecycle) date.

The dates for the end of support of minor versions are available in the [Release Schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule). As the end of support date for a minor version depends on release channel enrollment, ensure that you refer to the correct date that is reflective of your cluster's release channel:

  * **Release channels other than Extended** : If your cluster is enrolled in the Rapid, Regular, Stable channels or the cluster isn't enrolled in a release channel, this date is the minor version's [end of standard support](https://docs.cloud.google.com/kubernetes-engine/versioning#end-of-standard-support).
  * **Extended channel** : If your cluster is enrolled in the [Extended channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#extended), GKE won't automatically upgrade your cluster from the minor version until the [end of extended support](https://docs.cloud.google.com/kubernetes-engine/versioning#end-of-extended-support).



Once this date is reached, the cluster is automatically upgraded to the next minor version and the cluster environment might be impaired as the removed feature is still being used. To learn more, read about [Automatic upgrades at the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support).

**Important:** After June 30, 2024—when [1.26 reaches end of standard support](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels)— GKE begins to automatically upgrade clusters still using version 1.26 and deprecated APIs (removed in version 1.27) to version 1.27. GKE will stop [pausing automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#how_kubernetes_deprecations_work_with) after June 30, 2024 for clusters still using [deprecated APIs removed in version 1.27](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-27). We recommend that you upgrade your clusters to version 1.27 as soon as possible as GKE minor versions that have reached end of support will no longer receive security patches and bug fixes. To learn more about the GKE minor version lifecycle, see [GKE versioning and support](https://docs.cloud.google.com/kubernetes-engine/versioning).

#### What are deprecation insights and recommendations?

If GKE detects that a cluster is using a feature that is removed in an upcoming minor version of Kubernetes, GKE shares a deprecation _insight_ and _recommendation_ , notifying you of your cluster's usage of a deprecated feature. This insight provides information about last detected usage, and further details depending on the type of deprecation. To learn about viewing this information, see [Viewing deprecation insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/viewing-deprecation-insights-and-recommendations).

### Assess and mitigate exposure to upcoming Kubernetes deprecations

GKE provides migration guides that instruct you how to migrate from deprecated features and APIs to those compatible with the upcoming minor version. For a list of upcoming deprecations and their migration guides, see Kubernetes deprecations information.

While GKE shares insights about clusters it has detected are exposed to a deprecation, detection of all exposures to upcoming deprecations is not guaranteed. For example, if a deprecated feature has not been used in the last 30 days, GKE does not detect any usage, and an insight and recommendation is not generated.

You must independently assess your cluster environment's exposure to any upcoming deprecations before you upgrade your cluster to the next minor version. You can exercise control over the upgrade process by choosing a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels), using [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions), or [manually upgrading your clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) if you have determined that they are not exposed to deprecations on the next minor version.

### Resolving exposure to Kubernetes deprecations

You can take action by reviewing upcoming deprecations. [View deprecation insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/viewing-deprecation-insights-and-recommendations), to assess if your cluster is exposed, and use migration guides to mitigate the exposure before the last available minor version supporting the feature reaches its [end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#lifecycle).

After you make changes to stop usage of deprecated APIs or features in your cluster, GKE waits until it has no longer observed use of deprecated APIs or features for 30 days, and then unblocks automatic upgrades. Automatic upgrades proceed according to the [release schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule).

You can also [upgrade your cluster manually](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) if you've confirmed that the upgrade does not cause disruption to your cluster environment. You can do this by first creating a test cluster and checking whether the upgrade causes any disruption. If it does not, you can manually upgrade your cluster.

When you dismiss a recommendation, you only hide it for all users. Automatic upgrades remain paused until you migrate out of the deprecated features and GKE does not detect usage of the deprecated features for 30 consecutive days.

## Kubernetes deprecations information

The following sections provide information about ongoing deprecations, including guides explaining how to migrate to features or APIs compatible with available Kubernetes minor versions. You can check these tables to see if GKE detects and reports usage with insights and recommendations.

These tables only provide information about ongoing deprecations, and omit previously included information for features or APIs that were deprecated with versions that are significantly past their end of support date.

### Kubernetes feature deprecations

The following table outlines ongoing GKE feature deprecations, as well as the version in which those features are no longer supported:

Name | Deprecated | Removed | More information | Does GKE detect and report usage?  
---|---|---|---|---  
Identity Service for GKE | July 1, 2026 | Version 1.37 and later | [Identity Service for GKE deprecation](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/identity-service) | No  
Container Registry | May 15, 2023 | March 18, 2025 | [Transition from Container Registry to Artifact Registry in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/container-registry) | No  
GKE Compliance dashboard (Preview) | January 28, 2025 | June 30, 2025 | [Posture management feature deprecations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation) | No  
Workload vulnerability scanning _GKE security posture dashboard_ | 

  * Standard tier: July 23, 2024
  * Advanced Vulnerability Insights: June 16, 2025

| 

  * Standard tier: July 31, 2025
  * Advanced Vulnerability Insights: June 16, 2026

| [Vulnerability scanning removal from GKE Standard edition](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/vulnerability-scanning-gkee) | Yes  
Supply chain concerns - Binary Authorization (Preview) _GKE security posture dashboard_ | January 28, 2025 | March 31, 2025 | [Posture management feature deprecations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation) | No  
Kubernetes security posture - advanced tier (Preview) _GKE security posture dashboard_ | January 28, 2025 | March 31, 2025 | [Posture management feature deprecations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/posture-management-deprecation) | Yes  
containerd 1.7 features | GKE version 1.32 | GKE version 1.33 | [Migrate nodes to containerd 2](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/migrate-containerd-2) | Yes  
Linux cgroupv1 mode | GKE version 1.31 | TBD | [Migrate nodes to Linux cgroupv2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/migrate-cgroupv2) | No  
Vulnerability scanning removal from GKE standard edition | July 23, 2024 | July 31, 2025 | [Vulnerability scanning removal from GKE Standard edition](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/vulnerability-scanning-gkee) | No  
TLS certificates signed with SHA-1 algorithm | GKE version 1.24 | GKE version 1.29 | [SHA-1 TLS certificates support removal](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/sha1-1-29) | Yes  
Built-in authentication plugin for Kubernetes clients | GKE version 1.22 | GKE version 1.25 | [Deprecated authentication plugin for Kubernetes clients](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/auth-plugin) | No  
PodSecurityPolicy | GKE version 1.21 | GKE version 1.25 | [PodSecurityPolicy deprecation](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/podsecuritypolicy) | Yes  
Docker-based node images | GKE version 1.20 | GKE version 1.24 | [Docker node image deprecation](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/docker-containerd) | Yes  
X.509 Common Name field in webhook certificates | GKE version 1.19 | GKE version 1.23 | [Webhook certificates CN field deprecation](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/webhookcompatibility) | Yes  
  
### Kubernetes API deprecations

The following table provides an overview of Kubernetes APIs that are deprecated and no longer served, sorted by Kubernetes version:

Kubernetes version | More information | Does GKE detect and report usage?  
---|---|---  
1.32 | [Kubernetes 1.32 deprecated APIs](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-32) | Yes  
1.29 | [Kubernetes 1.29 deprecated APIs](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-29) | Yes  
1.27 | [Kubernetes 1.27 deprecated APIs](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-27) | Yes  
1.26 | [Kubernetes 1.26 deprecated APIs](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-26) | Yes  
1.25 | [Kubernetes 1.25 deprecated APIs](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-25) | Yes  
1.22 | [Kubernetes 1.22 deprecated APIs](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-22),   
[Kubernetes Ingress Beta APIs removed in GKE 1.23](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-23) | Yes  
  
### Other feature deprecations

The following table provides information on deprecations and removals that are caused by other upstream providers that are not part of the Kubernetes open source project.

Name | Deprecated | Removed | More information | Does GKE detect and report usage?  
---|---|---|---|---  
Windows Server Semi-Annual Channel (SAC) node images | N/A | August 9, 2022 | [Windows Server SAC end of servicing](https://docs.cloud.google.com/kubernetes-engine/docs/archive/windows-server-sac) | No  
Saxml for multi-host serving on TPUs and GKE | N/A | April 24, 2025 | [Release note](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#April_24_2025) | No  
  
## What's next

  * [Viewing deprecation insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/viewing-deprecation-insights-and-recommendations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
