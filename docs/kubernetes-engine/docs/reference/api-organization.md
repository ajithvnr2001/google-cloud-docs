---
url: https://docs.cloud.google.com/kubernetes-engine/docs/reference/api-organization/
title: API organization and structure \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:52.092464+00:00
---

# API organization and structure  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/reference/api-organization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/docs/authentication)



Send feedback 

#  API organization and structure Stay organized with collections  Save and categorize content based on your preferences. 

The programmatic interface to your Google Kubernetes Engine cluster has two principal APIs: The [Google Kubernetes Engine API](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest) (and the associated Google Cloud CLI) and the [Kubernetes API](https://kubernetes.io/docs/reference/using-api/api-overview/) (and the associated `kubectl` command-line interface).

**Note:** Before you use some parts of the Google Kubernetes Engine API or Kubernetes API, you may need to grant access to additional resources in Identity and Access Management (IAM). For more information, visit [API permissions](https://docs.cloud.google.com/kubernetes-engine/docs/reference/api-permissions).

## Google Kubernetes Engine API

You use the Google Kubernetes Engine API and Google Cloud CLI primarily for configuring your cluster on Google Cloud. This might include tasks such as:

  * Creating a cluster.
  * Deleting a cluster.
  * Configuring cluster-level networking, such as rotating the cluster control plane IP or enabling network policy enforcement.
  * Updating the version of Kubernetes running on the cluster.
  * Adding, removing, or modifying node pools in your cluster.
  * Setting the machine type or node image used for your cluster's nodes.
  * Configuring the geographic zones or regions in which your cluster runs.



### Google Kubernetes Engine API versioning

The Google Kubernetes Engine API has three groups:

  * `v1` for generally available features.
  * `v1alpha1` for alpha features.
  * `v1beta1` for beta features.



Similarly, Google Kubernetes Engine `gcloud` commands are divided into three groups:

  * [`gcloud container clusters`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters) contain flags for generally available features and use the `v1` group.
  * [`gcloud alpha container clusters`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/container/clusters) contain flags for alpha features and use the `v1alpha1` group.
  * [`gcloud beta container clusters`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/clusters) contain flags for beta features and use the `v1beta1` group.

**Note:** To use Google Kubernetes Engine alpha features and commands, Google must allowlist your project.

To learn how to use Google Kubernetes Engine beta features through the v1beta1 API, refer to Google Kubernetes Engine Beta Features.

### Google Kubernetes Engine beta features

When new features for Google Kubernetes Engine are released to beta, they are made available through the [`v1beta1` API](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest).

To use `gcloud` commands for Google Kubernetes Engine beta features, just run [`gcloud beta container clusters`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/container/clusters) commands.

**Note:** Commands that use the `v1beta1` API to create or modify clusters only affect beta functionality on those clusters. For generally available features, you can still access the cluster using the standard `v1` API.

As features "graduate" from beta to general availability, the commands move from the `v1beta1` API to the `v1` API, and from the `gcloud beta container` track to the `gcloud container` track in the command-line interface). The commands might undergo small changes during this transition. Any breaking changes are only made after a deprecation warning and must maintain a three month period of backward compatibility.

## Kubernetes API

You use the Kubernetes API and `kubectl` command-line interface for managing your cluster's containerized applications and workloads. This might include tasks such as:

  * Deploying an application
  * Scaling an application
  * Configuring intra-cluster networking settings
  * Configuring Pods and Containers
  * Controlling when Pods are evicted or restarted



### Kubernetes API versioning

Kubernetes supports multiple API versions, each at a different API path such as `/api/v1` or `/apis/extensions/v1beta1`. You must specify the API version when writing [object configuration files](https://kubernetes.io/docs/concepts/overview/object-management-kubectl/declarative-config/) or when interacting with the API directly.

The API is versioned separately from Kubernetes itself. For more information on API versioning, refer to the [Kubernetes API versioning documentation](https://kubernetes.io/docs/concepts/overview/kubernetes-api/#api-versioning).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
