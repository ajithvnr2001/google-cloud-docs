---
url: https://docs.cloud.google.com/kubernetes-engine/security/control-plane-node-creation/
title: Prevent node self-registration in GKE clusters \u00a0|\u00a0 GKE security \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:40.501514+00:00
---

# Prevent node self-registration in GKE clusters  |  GKE security  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/security/control-plane-node-creation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE security ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview)



Send feedback 

#  Prevent node self-registration in GKE clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

By default, Google Kubernetes Engine (GKE) nodes use the `kubelet` process on each node to register Node objects with the Kubernetes API server. This document shows you how to prevent this [self-registration](https://kubernetes.io/docs/concepts/architecture/nodes/#self-registration-of-nodes) for Shielded GKE Nodes, and instead require a trusted GKE control plane component to perform registration operations. Security engineers and platform administrators can use control plane node creation to limit the privileges of nodes.

You should already be familiar with the following concepts:

  * [Kubernetes nodes](https://kubernetes.io/docs/concepts/architecture/nodes/)
  * [Shielded GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes)
  * [TLS bootstrapping](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/)
  * [Node registration with the Kubernetes API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#node-registration)



## Node creation modes in GKE

Shielded GKE Nodes, which is enabled in all GKE clusters, enforce cryptographic verification of node identities during the node registration process. This verification helps to ensure that only legitimate nodes can register with the Kubernetes API server and run workloads.

The default registration workflow for GKE clusters, in which the `kubelet` on each node creates and modifies its `Node` object in the API server, creates a risk if a node is compromised. For example, in [CVE-2025-5187](https://nvd.nist.gov/vuln/detail/CVE-2025-5187), a vulnerability allowed node users to delete the corresponding `Node` objects and register compromised nodes.

### Control plane node creation

In GKE version 1.35.3-gke.1189000 and later, you can optionally require a trusted GKE control plane component named the `gcp-controller-manager` to create `Node` objects instead of allowing the `kubelet` to self-register the nodes. After the `kubelet` sets up a TLS connection with the API server by using the cryptographically verified node identity, the `gcp-controller-manager` component creates the `Node` object. An admission controller rejects any requests from the `kubelet` to create the `Node` object. By using the control plane component to create `Node` objects, you can reduce the risk of a potentially compromised node creating arbitrary `Node` objects or manipulating its `Node` specification.

To change the default node creation and registration behavior, you do one of the following when you create a Standard or Autopilot cluster:

  * Google Cloud CLI: specify a value of `CONTROL_PLANE` in the `--node-creation-mode` flag.
  * Kubernetes Engine API: specify a value of `VIA_CONTROL_PLANE` in the `node-creation-mode` field in the `NodeCreationConfig` method.



## Limitations

There's a brief delay between when the `gcp-controller-manager` creates a `Node` object in the Kubernetes API and when the `kubelet` updates that `Node` object with the full set of node labels and annotations. Any workloads or controllers that depend on a full set of labels or annotations immediately upon node creation, might show unexpected behavior. Certain labels and annotations may be reconciled at a different time than `kubelet` registration. Verify that your workloads and DaemonSets use label and annotation presence checks before acting.

  * Avoid deploying DaemonSets and workloads that have tolerations for all node taints, which might cause Pods to run on nodes that aren't ready.
  * Use an `initContainer` to check for node labels before letting main containers run.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Enable control plane node creation

You can enable node creation by using the `gcp-controller-manager` component when you create a cluster or update an existing cluster. For existing clusters, the update affects only new nodes in the cluster. Existing nodes aren't affected by the change.

The following command enables the control plane node creation mode for an existing cluster:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --node-creation-mode=CONTROL_PLANE \
        --location=CONTROL_PLANE_LOCATION \
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the region or zone of your cluster control plane.



You can also specify the `--node-creation-mode` flag in the [clusters create command](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--node-creation-mode) and in the [clusters create-auto command](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto#--node-creation-mode).

## Disable control plane node creation

You can revert to the default GKE behavior in which the `kubelet` creates nodes at any time by specifying a value of `KUBELET` in the `--node-creation-mode` Google Cloud CLI flag or `VIA_KUBELET` in the `NodeCreationConfig` GKE API method. For existing clusters, this change affects only new nodes in that cluster.

The following command updates a cluster to disable control plane node creation:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --node-creation-mode=KUBELET \
        --location=CONTROL_PLANE_LOCATION \
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the region or zone of your cluster control plane.



## What's next

  * Learn more about [Shielded GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes).
  * Read the [GKE security overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview).
  * Learn how to [harden your cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
