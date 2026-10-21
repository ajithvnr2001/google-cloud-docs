---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters/
title: Alpha clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:49.806775+00:00
---

# Alpha clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Alpha clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

You can experiment with Kubernetes alpha features, alpha APIs, and with upcoming minor versions by creating a Google Kubernetes Engine (GKE) _alpha cluster_. Alpha clusters are short-lived clusters that include alpha, beta, and GA Kubernetes APIs and feature gates and provide early access to upcoming Kubernetes minor versions. Alpha clusters are intended for advanced users and early adopters to experiment with workloads that take advantage of new features before those features are production-ready.

**Warning:** Don't use alpha clusters or alpha features for production workloads. Alpha clusters expire after 30 days and don't receive security updates. You must migrate your data from alpha clusters before they expire. GKE does not automatically save data stored on alpha clusters. For more information, see Limitations.

You can [create an alpha cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-alpha-cluster) or learn more about [cluster configuration choices](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters).

## How alpha clusters work

An alpha cluster is a GKE cluster that provides you with experimental access to Kubernetes alpha APIs, alpha feature gates, and alpha patch versions of upcoming Kubernetes minor versions. An alpha cluster has the following configuration:

  * Enables all Kubernetes API versions, including alpha APIs. You can't disable alpha APIs in the alpha cluster.
  * Enables all alpha feature gates that are available in the selected Kubernetes minor version. You can optionally disable specific alpha feature gates during cluster creation.
  * Inherits the default settings for any beta feature gates that are available in the selected minor version. If a beta feature gate is enabled by default in the minor version, then that feature gate is enabled by default in the alpha cluster. You can optionally enable or disable specific beta feature gates during cluster creation.



When you create an alpha cluster, you configure various settings like the [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) to enroll the cluster in, the GKE version to install, and the feature gates to enable or disable.

**Best practice** : Enroll alpha clusters in the Rapid release channel, which provides you with the latest Kubernetes versions and features for experimentation.

Alpha clusters that you enroll in the Rapid channel can run [_alpha patch versions_](https://docs.cloud.google.com/kubernetes-engine/versioning#alpha-versions), which are patch versions of the upcoming Kubernetes minor version that GKE makes available up to four months before GKE makes that minor version available to any cluster in the Rapid channel.

### Limitations

Alpha clusters have the following limitations:

  * Not covered by the [GKE SLA](https://cloud.google.com/kubernetes-engine/sla)
  * Can't be upgraded 
    * You must disable node auto-upgrade and auto-repair on alpha clusters
    * Don't receive security updates
  * Are automatically deleted after 30 days
  * Not supported with Windows Server node pools
  * Can't be enrolled in the Extended release channel.
  * Have additional limitations for enabling feature gates with alpha clusters



## Alpha patch versions

Alpha clusters support any available GKE patch version. In the Rapid release channel, alpha clusters have exclusive access to alpha patch versions of the upcoming Kubernetes minor version. GKE makes these alpha patch versions available up to four months before GKE makes that minor version available to any cluster in the Rapid channel.

GKE makes between one and three alpha patch versions available for the upcoming minor version. You can select one of the available alpha patch versions when you create an alpha cluster in the Rapid channel. You can use these versions to test upcoming Kubernetes features and APIs that are available only in the upcoming minor version.

When GKE makes the minor version available to non-alpha clusters in the Rapid channel, GKE removes all of the available alpha versions for that minor version. You can't select a removed alpha version when you create an alpha cluster. Any existing alpha clusters that use a removed version continue to exist until the cluster expires or you delete the cluster.

For more information about alpha patch versions, the lifecycle of those versions, and how to view available versions, see [GKE versioning and support](https://docs.cloud.google.com/kubernetes-engine/versioning).

## Feature gates and alpha clusters

Feature gates are a set of key-value pairs that toggle Kubernetes features. With alpha clusters, GKE enables the following:

  * **Alpha feature gates** : all feature gates at the alpha stages that are available with the Kubernetes version of your cluster
  * **Beta feature gates** : the feature gates at the beta stages that are available with the Kubernetes version of your cluster, and which are enabled by default by open source Kubernetes



For more information about which feature gates are available for a specific Kubernetes version, and which beta features are enabled by default (`true`), see [Feature gates for Alpha or Beta features](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#feature-gates-for-alpha-or-beta-features) in the Kubernetes documentation. However, you can selectively enable or disable specific feature gates, modifying the default values set by GKE.

Feature gates are a distinct mechanism for feature enablement from Kubernetes APIs, and are managed differently by GKE clusters. With alpha clusters, all Kubernetes alpha APIs are enabled. If you enable or disable a feature gate for an alpha cluster, the enablement of Kubernetes APIs isn't affected. However, some Kubernetes APIs and Kubernetes feature gates work together, so disabling feature gates might cause issues with related APIs. Verify the connection between specific feature gates and APIs.

For more information about how GKE works with feature gates, see [Feature gates](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/feature-gates).

To enable a cluster with a specific feature gate configuration, use the `--alpha-cluster-feature-gates` flag during cluster creation with the Google Cloud CLI. When you include this flag, you can modify which alpha and beta feature gates are enabled or disabled. For more information, see [Create an alpha cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-alpha-cluster#create_an_alpha_cluster).

### Limitations for enabling feature gates with alpha clusters

When you enable feature gates with alpha clusters, understand the following additional limitations:

  * You can only create alpha clusters with specific feature gates by using the gcloud CLI. Cluster creation with the Google Cloud console or Terraform isn't supported.
  * Kubernetes alpha features that require additional configuration beyond enabling the feature gate aren't supported.
  * You can selectively enable or disable alpha or beta feature gates, but all Kubernetes alpha APIs are enabled.



## Latest Kubernetes alpha features

Most Kubernetes releases contain new alpha features that you can test in alpha clusters. For a full list of Kubernetes releases and the features they include, see the [Kubernetes changelog](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/README.md).

### About feature stages

New Kubernetes features are introduced in four stages: early development, alpha, beta, and stable.

To provide stability and production quality, GKE clusters other than alpha clusters enable only features that are _beta or higher_. GKE doesn't enable alpha features on other types of GKE clusters because the features aren't production-ready or upgradeable.

Because GKE automatically upgrades the Kubernetes control plane and, by default, the worker nodes, enabling alpha features in production can jeopardize the reliability of the cluster if there are breaking changes in a new version.

To learn more about the stages of Kubernetes features, see [Alpha, Beta, and Stable Versions](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api_changes.md#alpha-beta-and-stable-versions) in the Kubernetes documentation.

To learn more about determining which features are enabled for a given GKE control plane version, see [Feature gates](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/feature-gates).

## What's next

  * Learn more [about cluster configuration choices](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters).
  * [Create an alpha cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-alpha-cluster).
  * [Read the GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
