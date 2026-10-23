---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/feature-gates/
title: Feature gates \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:57.461991+00:00
---

# Feature gates  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/feature-gates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Feature gates Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how Kubernetes [feature gates](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/) function in Google Kubernetes Engine (GKE). Feature gates are a set of key-value pairs that toggle Kubernetes features. You can modify Kubernetes feature gates in GKE only with alpha clusters. For more information, see [Alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters).

The Kubernetes project releases new features in [stages](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#feature-stages) over time. Features can be in the _alpha_ , _beta_ , or _GA_ stage.

To see what features are enabled for your cluster running version 1.26 or later, check the feature gate state.

Alternatively, to verify the stage of a feature corresponding to the version of your cluster's control plane or nodes, check the [Feature gates for Alpha or Beta features](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#feature-gates-for-alpha-or-beta-features) table in the Kubernetes documentation.

### GA Kubernetes features in GKE

GA (also referred to as _stable_) Kubernetes features are _enabled_ on GKE by default and _cannot be disabled_.

### Beta Kubernetes features in GKE

Beta features are usually _enabled_ by default in GKE. GKE might disable a specific beta feature for a particular version to mitigate a known issue with the feature, to ensure backwards compatibility, or because integration and qualification of the feature in GKE is not yet complete.

If you want to use a beta Kubernetes feature in your GKE cluster running version 1.26 or later, check that this feature is enabled by checking the feature gate state. If your cluster is running a version earlier than 1.26, you can check if the feature is enabled by testing the feature.

[Contact Cloud Customer Care](https://docs.cloud.google.com/support) if you can't verify whether the beta feature is enabled for your GKE cluster's control plane or node version.

#### Kubernetes beta APIs with GKE clusters

In addition to beta Kubernetes features, you can also use Kubernetes beta APIs with GKE clusters. For beta APIs that were introduced with version 1.24 or later, you must configure beta APIs per resource per cluster. For more information, see [Use Kubernetes beta APIs with GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/use-beta-apis).

### Alpha Kubernetes features in GKE

Alpha Kubernetes features are disabled by default in all GKE clusters, except for [alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters). GKE might enable a specific alpha feature in a specific control plane version.

With alpha clusters, all alpha feature gates available with the Kubernetes version are enabled, and some beta feature gates, depending on the default value, are enabled. For more information about which feature gates are available with specific versions, and which beta features are enabled by default, see [Feature gates for Alpha or Beta features](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#feature-gates-for-alpha-or-beta-features) in the Kubernetes documentation. You can also selectively modify specific feature gates. For more information, see [Feature gates and alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters#feature-gates).

To enable all alpha Kubernetes features, create an [alpha Standard cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters).

**Warning:** Alpha clusters are intended for experimental purposes and not for production workloads.

## Check feature gate state

With clusters running version 1.26 or later, you can run a `kubectl` command to check what features are enabled.

Check the feature gate state for your GKE cluster:

  1. [Install and configure kubectl access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl)
  2. Run the following command:
         
         kubectl get --raw /metrics | grep kubernetes_feature_enabled
         

The output, like in the following example, shows you the name of the feature gate, the corresponding stage (`""` is GA), and whether the feature gate is enabled. `1` means enabled and `0` means disabled.

See the following example output:
         
         # HELP kubernetes_feature_enabled [BETA] This metric records the data about the stage and enablement of a k8s feature.
         # TYPE kubernetes_feature_enabled gauge
         kubernetes_feature_enabled{name="APIListChunking",stage=""} 1
         kubernetes_feature_enabled{name="APIPriorityAndFairness",stage=""} 1
         kubernetes_feature_enabled{name="APIResponseCompression",stage="BETA"} 1
         kubernetes_feature_enabled{name="APISelfSubjectReview",stage=""} 1
         kubernetes_feature_enabled{name="APIServerIdentity",stage="BETA"} 1
         kubernetes_feature_enabled{name="APIServerTracing",stage="BETA"} 1
         kubernetes_feature_enabled{name="AdmissionWebhookMatchConditions",stage="BETA"} 1
         ...
         

This output indicates that, for example, the `APIResponseCompression` feature is enabled and in the beta stage.




## What's next

  * For a complete list of current Kubernetes features, see [Feature gates](https://kubernetes.io/docs/reference/command-line-tools-reference/feature-gates/#feature-gates-for-alpha-or-beta-features).
  * For a full list of GKE features, refer to the [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
