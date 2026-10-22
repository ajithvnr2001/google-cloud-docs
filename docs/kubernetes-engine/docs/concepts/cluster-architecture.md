---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture/
title: GKE cluster architecture \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:52.311435+00:00
---

# GKE cluster architecture  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  GKE cluster architecture Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes the architecture of the Google Kubernetes Engine (GKE) clusters that run your containerized workloads. Use this page to learn about the control plane, nodes, and how the various GKE cluster components interact with each other.

This page is for Admins, Architects, and Operators who define IT solutions and system architecture. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page, ensure that you're familiar with the [Kubernetes cluster architecture](https://kubernetes.io/docs/concepts/architecture/).

A GKE cluster consists of a _control plane_ and worker machines called _nodes_. The control plane and nodes make up the Kubernetes cluster orchestration system. GKE Autopilot manages the entire underlying infrastructure of clusters, including the control plane, nodes, and all system components.

If you use GKE Standard mode, GKE manages the control plane and system components, and you manage the nodes.

The following diagram shows the architecture of a GKE cluster:

![](https://docs.cloud.google.com/static/kubernetes-engine/images/gke-architecture.svg)

This diagram shows the following components:

  * Control plane: managed by GKE. Runs the Kubernetes API server, workload controllers, Kubernetes scheduler, and cluster state storage.
  * Nodes: managed by GKE in Autopilot mode, and managed by customers in Standard mode. All of your Pods run in nodes.
  * Other Google Cloud services: available to integrate with GKE.



## About the control plane

The control plane runs processes such as the Kubernetes API server, scheduler, and core resource controllers. GKE manages the control plane lifecycle from cluster creation to deletion. This includes upgrades to the Kubernetes version running on the control plane, which GKE performs automatically, or manually at your request if you prefer to upgrade earlier than the automatic schedule.

### Control plane and the Kubernetes API

The control plane is the unified endpoint for your cluster. You interact with the control plane through Kubernetes API calls. The control plane runs the Kubernetes API server process (`kube-apiserver`) to handle API requests. You can make Kubernetes API calls in the following ways:

  * Direct calls: HTTP/gRPC
  * Indirect calls: Kubernetes command-line clients such as `kubectl`, or the Google Cloud console.



The API server process is the hub for all communication for the cluster. All internal cluster components such as nodes, system processes, and application controllers act as clients of the API server.

Your API requests tell Kubernetes what your _desired state_ is for the objects in your cluster. Kubernetes attempts to constantly maintain that state. Kubernetes lets you configure objects in the API either _imperatively_ or _declaratively_.

To learn more about object management in Kubernetes, refer to the following pages:

  * [Understanding Kubernetes objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/)
  * [Kubernetes object management](https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/)



### Control plane and the cluster state database

The open source Kubernetes project uses [etcd](https://kubernetes.io/docs/tasks/administer-cluster/configure-upgrade-etcd/) as the storage database for all cluster data by default. The cluster state is kept in a key-value store that contains information about the state of every Kubernetes API object in your cluster. For example, the cluster state database stores every Secret, ConfigMap, and Deployment.

GKE clusters store the cluster state in one of the following key-value stores:

  * **etcd** : GKE stores the cluster state in etcd instances that run on every control plane virtual machine (VM).
  * **Spanner** : GKE stores the cluster state in [Spanner](https://docs.cloud.google.com/spanner). The Spanner database doesn't run in the cluster control plane.



Regardless of the type of database, every GKE cluster serves the etcd API in the control plane. The Kubernetes API server uses the etcd API to communicate with the backend cluster state database.

### Control plane and node interaction

The control plane manages what runs on all of the cluster's nodes. The control plane schedules workloads and manages the workloads' lifecycle, scaling, and upgrades. The control plane also manages network and storage resources for those workloads. The control plane and nodes communicate with each other using Kubernetes APIs.

### Control plane interactions with Artifact Registry

When you create or update a cluster, GKE pulls container images for the Kubernetes system software running on the control plane and nodes from Artifact Registry repositories in the `pkg.dev` or the `gcr.io` domain. An outage affecting these registries might cause the following actions to fail:

  * New cluster creation
  * Cluster version upgrades



Disruptions to workloads might occur even without your intervention, depending on the specific nature and duration of the outage.

If the Artifact Registry repository outage is regional, we might redirect requests to a zone or region that isn't affected by the outage.

To check the status of Google Cloud services, go to the [Google Cloud status dashboard](https://status.cloud.google.com/).

**Best practice** : 

Deploy across multiple regions to permit availability of applications during region outages.

## About the nodes

Nodes are the worker machines that run your containerized applications and other workloads. The individual machines are [Compute Engine virtual machines (VMs)](https://docs.cloud.google.com/compute/docs/instances) that GKE creates. The control plane manages and receives updates on each node's self-reported status.

A node runs the services necessary to support the containers that make up your cluster's workloads. These include the runtime and the Kubernetes node agent (`kubelet`), which communicates with the control plane and is responsible for starting and running containers scheduled on the node.

GKE also runs a number of system containers that run as per-node agents, called DaemonSets, that provide functionality such as log collection and intra-cluster network connectivity.

**Best practice** : 

Use `stdout` for containerized applications because `stdout` lets your platform handle the [application logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-logs).

Node management varies based on the cluster [mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode), as follows: 

Node component | Autopilot mode | Standard mode  
---|---|---  
Lifecycle | Fully managed by GKE, including:

  * [Automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot#how_cluster_and_node_pool_upgrades_work)
  * Automatic repairs
  * Health checks
  * [Automatic node scaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#scale_workloads)
  * Node creation and deletion
  * Resizing
  * Labelling for [workload separation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-separation).

| GKE manages the following:

  * [Automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#upgrading_automatically)
  * Automatic repairs
  * Health checks

You can manage the following:

  * [Node automatic scaling configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
  * [Manual version upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#upgrading_manually)
  * Configuration changes (such as [labels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels#create-node-pool-labels) and [resizing](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/resizing-a-cluster))
  * [Node pool creation and deletion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools)

  
Visibility | View nodes using `kubectl`. Underlying Compute Engine virtual machines not visible or accessible in the gcloud CLI or the Google Cloud console. | View nodes using `kubectl`, the gcloud CLI, and the Google Cloud console. View and access underlying Compute Engine VMs.  
Connectivity | No direct connection to the underlying VMs. | Connect to underlying VMs using SSH.  
Node operating system (OS) | Managed by GKE. All nodes use [Container-Optimized OS with containerd (`cos_containerd`)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#cos-variants). | [Choose an operating system for your nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images).  
Machine hardware selection | Request [_compute classes_](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-compute-classes) in Pods based on use case. GKE manages machine configuration, scheduling, quantity, and lifecycle. | Choose and configure Compute Engine machine types when [creating node pools](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create#--machine-type). Configure settings for sizing, scaling, quantity, scheduling, and location based on need.  
  
## Node registration with the Kubernetes API

When a node is created in a GKE cluster, the `kubelet` process on that node establishes a [TLS connection](https://kubernetes.io/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/#initialization-process) with the Kubernetes API server. During node initialization, the kubelet creates a `CertificateSigningRequest` to request a unique client certificate from the API server. The `kubelet` uses the certificate to create a `Node` object in the Kubernetes API.

A GKE feature named [Shielded GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes), which is enabled by default in all new clusters, enhances the security of this node self-registration process by using a virtual Trusted Platform Module (vTPM) on the node to cryptographically verify the node's identity. This verification ensures that the control plane issues credentials only to legitimate nodes.

You can optionally require a trusted GKE control plane component to create these `Node` objects instead of the `kubelet`, which reduces the potential impact if a node is compromised. For more information, see [Control Plane node creation](https://docs.cloud.google.com/kubernetes-engine/security/control-plane-node-creation) ([Preview](https://cloud.google.com/products#product-launch-stages)). 

## What's next

  * Learn more about [GKE Autopilot overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview).
  * Learn more about [regional clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters).
  * Learn more about [GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview).
  * Learn how to [create a zonal cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster).
  * Learn more about [node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
