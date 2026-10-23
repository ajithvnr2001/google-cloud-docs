---
url: https://docs.cloud.google.com/kubernetes-engine/ai-ml/install-overview-substrate/
title: Install Agent Substrate on GKE \u00a0|\u00a0 GKE AI/ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:47.777740+00:00
---

# Install Agent Substrate on GKE  |  GKE AI/ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/ai-ml/install-overview-substrate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE AI/ML ](https://docs.cloud.google.com/kubernetes-engine/docs/integrations/ai-infra)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/machine-learning)



Send feedback 

#  Install Agent Substrate on GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Note:** Agent Substrate on GKE is available to all Google Cloud customers for evaluation and non-production use. Production support is offered on an allowlist basis under a private GA program. To request production support for your workloads, submit the [Agent Substrate on GKE Production Support Signup form](https://docs.google.com/forms/d/e/1FAIpQLSeVdndsPwD_D9RCLNvRzVbx0a8gYzIHLOTA6db-N1UFP7w1zw/viewform?usp=preview). Our team will follow up within 48 hours.

[Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/ai-ml/about-agent-substrate) efficiently runs agentic workloads on GKE clusters by suspending idle agents and restoring those agents when they need to act again. Agent Substrate on GKE is open source software that you can install onto a GKE Standard cluster.

This document helps you prepare your Google Cloud project and GKE cluster for Agent Substrate on GKE, explains how to run the installer, and describes the resources that the installation creates.

## Pricing

Agent Substrate on GKE is offered at no extra charge. [GKE pricing](https://cloud.google.com/kubernetes-engine/pricing) applies to the resources that you create.

## Limitations

Agent Substrate on GKE has the following installation limitations:

  * **Cloud Shell** : you can't install Agent Substrate on GKE in Cloud Shell because Cloud Shell provides 5 GB of persistent disk storage, which is insufficient for the installation. You must run the installer on your local machine.
  * **Cluster mode** : you can install Agent Substrate on GKE only in GKE Standard clusters. Autopilot clusters aren't supported.
  * **Existing clusters and beta APIs** : if you enable the required beta APIs (`podcertificaterequests` and `clustertrustbundles`) on an existing cluster that runs version 1.36, you must replace the existing nodes before installing Agent Substrate on GKE. Nodes created before the update don't have Pod certificate projection enabled (`MountVolume.SetUp failed: unimplemented`). On clusters that run version 1.37 or later, existing nodes don't need to be replaced.
  * **Machine types** : you can't use machine series that run on mixed CPU architectures (such as E2 machine types).



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * [Install the following components in the gcloud CLI](https://docs.cloud.google.com/sdk/docs/components#installing_components): 
    * `kubectl`
    * `gke-gcloud-auth-plugin`
  * Ensure that the following tools are installed on your local machine: 
    * [Git](https://git-scm.com/downloads) to clone the Agent Substrate repository.
    * [Go](https://go.dev/doc/install) to run the installer's programs, which are distributed as source code.
    * `make` to start the installer.
  * Because the installer acts on your behalf to enable APIs and provision resources, set up Application Default Credentials (ADC) by running the following command:
        
        gcloud auth application-default login
        

For more information about authenticating with ADC, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).




### Required roles

To get the permissions that you need to install Agent Substrate on GKE, ask your administrator to grant you the following IAM roles on your project: 

  * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)
  * [Kubernetes Engine Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.admin) (`roles/container.admin`)
  * [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`)
  * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * [Monitoring Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Cluster requirements

If you let the installer create a cluster for you, it automatically configures a cluster that meets all requirements for Agent Substrate on GKE.

If you choose instead to install Agent Substrate on GKE in an existing cluster, that cluster must meet the following requirements:

  * Runs on GKE Standard (Agent Substrate on GKE is supported on Standard clusters only).
  * Runs GKE version 1.36 (with beta flags enabled) or version 1.37 or later.
  * Uses `c3-standard-4` or larger machine types for nodes.
  * Has the `PodCertificateRequest` and `ClusterTrustBundle` Kubernetes APIs enabled (`certificates.k8s.io/v1beta1/podcertificaterequests` and `certificates.k8s.io/v1beta1/clustertrustbundles`). To enable these APIs on an existing cluster, run the following command:
        
        gcloud container clusters update CLUSTER_NAME \
            --location=CONTROL_PLANE_LOCATION \
            --enable-kubernetes-unstable-apis=certificates.k8s.io/v1beta1/podcertificaterequests,certificates.k8s.io/v1beta1/clustertrustbundles
        

    * **Version 1.36** : after enabling the APIs, you must [replace the existing nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/use-beta-apis#ensure-nodes-use-beta-apis)—for example, by upgrading the node pool or re-creating its nodes. Pod certificate projection isn't enabled on nodes that existed before the update (`MountVolume.SetUp failed: unimplemented`).
    * **Version 1.37 or later** : Pod certificate projection is already enabled on existing nodes, so you don't need to replace nodes after enabling the APIs.



## Install Agent Substrate on GKE

To install Agent Substrate on GKE, run the following command in your local terminal:
    
    
    curl -sSL https://raw.githubusercontent.com/ai-on-gke/substrate-gke/main/install.sh | bash
    

The interactive installer prompts you for your project, cluster, and storage settings. It suggests recommended defaults where possible, which you can accept or customize:

  * **Project ID (required)** : specify the Google Cloud project where resources will be provisioned. If you configured a default project for the gcloud CLI, then the installer uses that project ID.
  * **Cluster (required)** : choose whether to let the installer create a new GKE cluster with recommended defaults or to install Agent Substrate on GKE in an existing cluster. If you choose to install on an existing cluster, verify that it meets the requirements in the Cluster requirements section.
  * **Snapshot bucket (optional)** : specify a custom Cloud Storage bucket name, or leave it blank to let the installer create a default bucket named `ate-snapshots-<project>-<zone>`.



When prompted to select a container image source, you can choose from the following options:

  * **Prebuilt images** : pulls published images from a container registry. Because nothing is built or pushed, your Google Cloud project doesn't need a container registry of its own.
  * **Build from source** : builds the images from the upstream [Agent Substrate repository](https://github.com/agent-substrate/substrate) (or a custom branch) and pushes them to your project's Artifact Registry registry.



### What the installer does

The installer executes the following programs on your behalf:

  * `setup-gcp`: creates or verifies the required Google Cloud resources, enables APIs, creates the GKE cluster (if you chose not to use an existing cluster) and Cloud Storage bucket, and configures IAM policies.
  * `ate-setup`: deploys the prebuilt Agent Substrate on GKE container images and controllers onto your GKE cluster.



First, the installer makes the following changes to your Google Cloud project:

  1. Enables the Google Cloud APIs that Agent Substrate on GKE needs.
  2. Creates a GKE Standard cluster (if not using an existing cluster) that has the following settings: 
     * **Workload Identity Federation for GKE** : allows Agent Substrate on GKE to access Cloud Storage without storing keys on the nodes.
     * **GKE Dataplane V2** : handles the networking required to route incoming requests to your agents.
     * **Certificate APIs (`PodCertificateRequest` and `ClusterTrustBundle`)**: enables these [Kubernetes beta APIs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/use-beta-apis) to issue certificates for TLS communication between Agent Substrate on GKE components.
     * **Managed OpenTelemetry** : collects metrics and traces from your cluster.
  3. Creates the Cloud Storage bucket that Agent Substrate on GKE writes your snapshots to.
  4. Grants Agent Substrate on GKE access to Cloud Storage for storing snapshots. If you choose to build from source, also grants access to Artifact Registry for container images.
  5. Creates Cloud Monitoring dashboards that chart Agent Substrate on GKE routing latency, snapshot size, and gRPC traffic.



Next, the installer makes the following changes to your cluster:

  1. Adds the Agent Substrate on GKE API group and resources to your cluster. These are Kubernetes custom resources, such as `ActorTemplate` (which defines the container images and resources your agents use) and `WorkerPool` (which defines how many idle sandboxes are kept ready).
  2. Sets up the certificate authorities that issue the certificates identifying Agent Substrate on GKE components and your Actors. Components present these certificates to authenticate to each other using mTLS.
  3. Deploys Agent Substrate on GKE components to your cluster, along with a PostgreSQL database that tracks the state of your Actors and Workers. The installer waits for the database and all control plane Pods to become ready.



Agent Substrate on GKE deploys its components as ordinary workloads within the `ate-system` and `podcertificate-controller-system` namespaces. The installation doesn't modify the GKE control plane.

The components that get deployed include the gVisor-based runtime that Agent Substrate on GKE uses by default to isolate each of your agents from the node it runs on. The installer doesn't configure microVM runtimes. To use microVM runtimes, you must manually deploy them onto a node pool that has [nested virtualization](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nested-virtualization) enabled. For details, see the [microVM runtime instructions](https://github.com/agent-substrate/substrate/blob/main/docs/dev/microvm-local.md) in the upstream Agent Substrate repository.

If the installation fails at any point (for example, due to a transient network error or token expiration), rerun the command. The installer preserves existing resources and resumes from where it left off.

To upgrade Agent Substrate on GKE in an existing cluster, run the installer and select **Upgrade an installed cluster**. For details, see [Upgrading an installed cluster](https://github.com/ai-on-gke/substrate-gke#upgrading-an-installed-cluster) in the `substrate-gke` README.

### Optional steps

After deploying the core components, the installer offers the following optional steps:

  * **Filestore CSI driver** : installs the [Filestore CSI driver](https://docs.cloud.google.com/filestore/docs/filestore-for-gke) configured for Agent Substrate on GKE. Choose this option if your agents need shared file storage across Pods, such as shared workspaces or repositories. If your cluster has the managed GKE Filestore add-on enabled, the installer disables it before deploying the driver.
  * **Node-pool autoscaling** : enables GKE [cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) on your node pool. You specify the minimum and maximum number of nodes for the pool. Choose this option if you want GKE to automatically add nodes during demand surges and remove nodes when agents are suspended. Skip this option if you prefer a fixed node count with predictable compute costs.
  * **Counter demo** : deploys an example workload that demonstrates agent suspension and restoration. Choose this option if you want to test the cluster after installation. For details, see Try the Counter demo.



## Verify the installation

To verify that the installation succeeded and the core components are running, run the following commands and ensure that all Pods have a status of `Running`:
    
    
    kubectl get pods -n ate-system
    kubectl get pods -n podcertificate-controller-system
    

### Node labeling and versions

The installer applies the `ate.dev/substrate-version` label to every node in your cluster. This label specifies which version of Agent Substrate on GKE is installed on your cluster, and Agent Substrate on GKE runs Workers only on nodes that have this version label.

To check which version of Agent Substrate on GKE is installed on your cluster, run the following command:
    
    
    kubectl get ds -n ate-system -l app=atelet -L ate.dev/substrate-version
    

Consider the following node labeling details:

  * **Worker pools** : when you create a `WorkerPool`, configure it to target this version tag. For examples, see [Pin pools to the installed substrate version](https://github.com/agent-substrate/substrate/blob/main/docs/api-guide.md#pin-pools-to-the-installed-substrate-version-templatenodeselector) in the Substrate API guide.
  * **New nodes** : the installer labels individual nodes rather than the node pool. Because of this, any new nodes added after installation—even in a node pool created by the installer—start without the version label. You should label your [GKE node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels) so that new nodes automatically receive the label.



## Try the Counter demo

If you chose to deploy the Counter demo when prompted by the installer, you can observe the suspension and restoration capabilities of Agent Substrate on GKE. The demo runs a small web server that keeps a count in memory.

After deploying the demo's `WorkerPool` and `ActorTemplate`, the installer prints the commands you need to create an `Actor` from the `ActorTemplate` and to send a request to that `Actor`. The [Counter demo README](https://github.com/agent-substrate/substrate/blob/main/demos/counter/README.md) in the upstream Agent Substrate repository explains the next steps to take.

## Uninstall Agent Substrate on GKE

When the installation completes and exits, the installer prints customized cleanup commands for your environment.

To remove resources created during installation, choose one of the following options:

  * **Remove Agent Substrate on GKE from an existing cluster** : if you installed on an existing cluster and want to retain the cluster and its other workloads, delete only the Agent Substrate on GKE components by running the `ate-setup delete ate-system` command that the installer prints. The installer pre-populates this command with the project, cluster, and location values configured during installation.

  * **Delete all resources (including the cluster)** : to delete the GKE cluster, snapshot bucket, IAM bindings, and dashboards, run the `cleanup-gcp` command that the installer prints. The installer pre-populates this command with the project, cluster, location, and bucket values configured during installation. For details, see the "Tearing down" section of the [substrate-gke README](https://github.com/ai-on-gke/substrate-gke#tearing-down).




## What's next

  * To learn more about Agent Substrate on GKE, see [About Agent Substrate on GKE](https://docs.cloud.google.com/kubernetes-engine/ai-ml/about-agent-substrate).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
