---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/use-beta-apis/
title: Use Kubernetes beta APIs with GKE clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:05.327762+00:00
---

# Use Kubernetes beta APIs with GKE clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/use-beta-apis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Use Kubernetes beta APIs with GKE clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Use Kubernetes beta APIs to access new features in your Google Kubernetes Engine (GKE) clusters. To use beta APIs introduced with version 1.24 or later, configure beta APIs. 

## How new features are introduced with the Kubernetes API

GKE clusters [consist of](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture) a control plane and worker nodes. The control plane exposes the API server, which exposes [the Kubernetes API](https://kubernetes.io/docs/concepts/overview/kubernetes-api/) so that end users, along with internal and external components, can communicate. This API evolves over time, with new features being [introduced in Alpha or Beta stages](https://kubernetes.io/docs/reference/using-api/#api-versioning), and then eventually either graduating to General Availability (GA) or being deprecated and removed in newer minor versions.

You can only use alpha APIs with [alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters), but you can use beta APIs with all types of GKE clusters. Starting with Kubernetes version 1.24, new beta APIs are, by default, disabled in new clusters. Existing clusters created running a version earlier than 1.24 keep existing beta APIs enabled, as automatically enabled (introduced earlier than 1.24) or manually enabled beta APIs (introduced 1.24 or later) cannot be disabled on existing clusters. For all clusters, existing beta APIs introduced before version 1.24 remain enabled by default, and new versions of existing beta APIs also remain enabled by default.

For example, if a `v1beta1` API was introduced in Kubernetes version 1.22, then a new version of this beta API, such as `v1beta3`, is introduced in Kubernetes version 1.25, the API is automatically enabled. This happens because it is a new version of an existing beta API, not a completely new beta API. However, a new beta API with the `v1beta1` version introduced in Kubernetes version 1.24 or later is disabled by default.

To use beta APIs introduced with version 1.24 and later, you must configure beta APIs per resource per cluster. You can enable APIs on cluster creation or for an existing cluster. To see what beta APIs are available for your cluster's minor version, refer to the available beta APIs.

After you enable a beta API, it remains enabled until the beta API is deprecated and the cluster is upgraded to the minor version where the API is removed. To see which beta APIs your cluster has enabled, see Check which beta APIs are enabled.

### Kubernetes beta APIs and Kubernetes feature gates

Feature gates are a distinct mechanism for feature enablement from Kubernetes APIs, and are managed differently by GKE clusters. Some Kubernetes APIs and Kubernetes feature gates work together. Ensure that you understand the connection between specific feature gates and APIs. For more information, see [Feature gates](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/feature-gates).

### Available beta APIs

You can enable a subset of Kubernetes beta APIs for your GKE clusters. Other beta APIs are not available for reasons such as the following:

  * The beta API relies on non-GA Kubernetes features.
  * The beta API is not secure.
  * The beta API is not Autopilot compatible.



Refer to the following table for beta APIs and the corresponding minor version where they were introduced:

Kubernetes version | Beta APIs added with this Kubernetes minor version | Available with GKE | Notes  
---|---|---|---  
[1.32](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.32.md) | 

  * resource.k8s.io/v1beta1/deviceclasses
  * resource.k8s.io/v1beta1/resourceclaims
  * resource.k8s.io/v1beta1/resourceclaimtemplates
  * resource.k8s.io/v1beta1/resourceslices

| 

  * resource.k8s.io/v1beta1/deviceclasses
  * resource.k8s.io/v1beta1/resourceclaims
  * resource.k8s.io/v1beta1/resourceclaimtemplates
  * resource.k8s.io/v1beta1/resourceslices

|  You must enable all listed `resource.k8s.io` APIs at the same time, and you must ensure that nodes use the newly-enabled beta APIs. This enables the Dynamic Resource Allocation Kubernetes beta feature in a GKE cluster. To learn more, see [Dynamic Resource Allocation](https://kubernetes.io/docs/concepts/scheduling-eviction/dynamic-resource-allocation).  
[1.31](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.31.md) | 

  * storage.k8s.io/v1beta1/volumeattributesclasses
  * networking.k8s.io/v1beta1/ipaddresses
  * networking.k8s.io/v1beta1/servicecidrs

| 

  * storage.k8s.io/v1beta1/volumeattributesclasses
  * networking.k8s.io/v1beta1/ipaddresses
  * networking.k8s.io/v1beta1/servicecidrs

|  You must enable both `networking.k8s.io` APIs at the same time, and you must ensure that nodes use the newly-enabled beta APIs. This enables the Multiple Service CIDRs Kubernetes beta feature in a GKE cluster running version 1.31.1-gke.1361000 or later. For more details, see the [October 4, 2024 GKE release note](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#October_04_2024).  
[1.29](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.29.md) | 

  * None

| 

  * admissionregistration.k8s.io/v1beta1/validatingadmissionpolicies
  * admissionregistration.k8s.io/v1beta1/validatingadmissionpolicybindings

| You must enable both APIs at the same time. This enables the [Validating Admission Policy](https://kubernetes.io/docs/reference/access-authn-authz/validating-admission-policy/) beta feature.  
[1.28](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.28.md) | 

  * admissionregistration.k8s.io/v1beta1/validatingadmissionpolicies
  * admissionregistration.k8s.io/v1beta1/validatingadmissionpolicybindings

| 

  * None

|   
[1.27](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.27.md) | 

  * authentication.k8s.io/v1beta1/selfsubjectreviews

| 

  * authentication.k8s.io/v1beta1/selfsubjectreviews

|   
  
## Considerations before using beta APIs

Kubernetes beta APIs are subject to the [Kubernetes Deprecation Policy](https://kubernetes.io/docs/reference/using-api/deprecation-policy/). When a beta API is deprecated, you must discontinue usage of it. To learn more, see Beta API deprecations.

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Configure beta APIs

Beta APIs are enabled per resource per cluster. You can enable APIs when you create a cluster or for an existing cluster.

To list a beta API resource for these commands, use the representation `{group}/{version}/{resource}`. The version must be a beta version. An example of this valid representation is `authentication.k8s.io/v1beta1/selfsubjectreviews`.

For the commands in the next section, replace the following variables:

  * `CLUSTER_NAME`: the name of the cluster you want to update.
  * `LIST_OF_APIS`: the list of beta APIs you want to enable, in a comma-separated list.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



### Create new cluster with beta APIs enabled

Create a new cluster with a list of beta APIs enabled:
    
    
    gcloud container clusters create-auto CLUSTER_NAME  \
        --enable-kubernetes-unstable-apis=LIST_OF_APIS \
        --location=CONTROL_PLANE_LOCATION
    

### Enable beta APIs on an existing cluster

Enable a list of beta APIs on an existing cluster:
    
    
    gcloud container clusters update CLUSTER_NAME  \
        --enable-kubernetes-unstable-apis=LIST_OF_APIS \
        --location=CONTROL_PLANE_LOCATION
    

#### Ensure that nodes use the newly-enabled beta APIs

Some beta features require that the feature is also enabled on the kubelet running on the worker nodes.

To use these newly-enabled beta API features with workloads running on the worker nodes, GKE must apply the change to the nodes:

  * For nodes in new Standard node pools and groups of Autopilot nodes, GKE enables the beta APIs.
  * For new and existing nodes in existing Standard node pools, or existing groups of nodes in Autopilot, GKE applies the change when the nodes are recreated during node upgrades or other types of node updates. To apply the change immediately to existing nodes in a Standard cluster node pool, you can [manually upgrade the node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_nodes) to a later GKE version. Performing an in-place upgrade doesn't apply the change.



### Disable beta APIs on an existing cluster

You cannot disable beta APIs that are already enabled on a cluster. Beta APIs remain available until they are deprecated and the cluster is upgraded to the minor version where the API is removed. To learn more, see Beta API deprecations.

## Check which beta APIs are enabled

Check which beta APIs are enabled for your GKE cluster:
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --format="value(enableK8sBetaApis.enabledApis)"
    

## Beta API deprecations

Once a beta API is enabled, it remains enabled until the beta API is deprecated and the cluster is upgraded to the minor version where the API is removed.

Beta APIs are typically available for three minor versions before they are deprecated in favor of a new beta version, a stable version, or with no replacement. Beta APIs versions are removed three minor versions after deprecation. If you are using a beta API that has been deprecated and is removed in an upcoming Kubernetes minor version, you need to migrate to supported APIs so that your cluster can be upgraded to the minor version where the beta API is removed. To learn more, see [How Kubernetes deprecations work with GKE](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#how_kubernetes_deprecations_work_with).

GKE makes this process easier by attempting to detect the usage of deprecated Kubernetes APIs. If GKE detects the usage of a deprecated API, it [pauses automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#auto-upgrade-pause) to the minor version where that API is removed. GKE also shares [deprecation insights and recommendation](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#what-deprecation-insights-recs) to notify you of your cluster's usage of a deprecated API so that you can take action to let upgrades continue. To learn more, see [Assess and mitigate exposure to upcoming Kubernetes deprecations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#assess_and_mitigate_exposure_to_upcoming_kubernetes_deprecations).

See the [Kubernetes API deprecations table](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#kubernetes_api_deprecations) for a complete list of deprecated APIs and whether GKE detects usage.

## What's next

  * [Feature and API deprecations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
