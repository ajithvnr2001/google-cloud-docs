---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configuration-overview/
title: About cluster configuration choices \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:45.489068+00:00
---

# About cluster configuration choices  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configuration-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About cluster configuration choices Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains the main cluster configuration choices you can make when creating a cluster in Google Kubernetes Engine (GKE), whether you're using the Google Cloud console, the Google Cloud CLI, or Terraform. These options let you customize a wide range of cluster attributes and behavior to meet your needs, from whether the cluster is accessible from public networks to how you want it to receive version upgrades.

Many of the options discussed in this guide **can't be changed after a cluster is created**. These include choices that affect a cluster's availability and network. If you _do_ need to change these options, you must create a new cluster then migrate traffic to it, which might be disruptive.

**Best practice** : 

Because many cluster configuration options can't be changed after cluster creation, plan and design your cluster configuration with your organization's Admins and architects, Cloud architects, Network administrators, or any other team responsible for defining, implementing, and maintaining the GKE and Google Cloud architecture.

This page is for Admins and architects who define IT solutions and system architecture in accordance with company strategy. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

Before reading this page you should be familiar with the following, as well as [basic Kubernetes concepts](https://docs.cloud.google.com/kubernetes-engine/docs/learn/get-started-with-kubernetes):

  * [GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)
  * [GKE modes of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)
  * [GKE editions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-editions)
  * [Cluster lifecycle](https://docs.cloud.google.com/kubernetes-engine/docs/get-started/cluster-lifecycle)



## Level of cluster management

Before discussing cluster options, it's important to understand the level of flexibility, responsibility, and control that you require for your cluster. The level of control that you require determines the mode of operation to use in GKE, and the cluster configuration choices that you need to make.

When you create a cluster in GKE, you do so by using one of the following modes of operation:

  * **Autopilot** (recommended): Provides a fully-provisioned and managed cluster configuration. Autopilot clusters are pre-configured with an optimized cluster configuration that is ready for production workloads.

  * **Standard** : Provides advanced configuration flexibility over the cluster's underlying infrastructure. For clusters created using the Standard mode, you determine the configuration needed for your production workloads.




For more information about these modes, and to learn more about Autopilot, see [GKE modes of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode) and the [ Autopilot overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview).

You can find a detailed side-by-side comparison of the two modes in [Compare GKE Standard and Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-standard-feature-comparison).

## Cluster configuration choices

After you have chosen a mode of operation, you then select the configuration you require for your cluster. Because Autopilot clusters are more fully managed and configured by Google Cloud than Standard clusters, they have fewer available configuration choices.

Configuration options for all clusters fall into the following categories:

  * **Name and other metadata** : Each cluster must have an identifying name that is unique within its project. You can also optionally add a cluster description and labels.
  * **Availability and scalability** : Specify where you want your cluster control plane and nodes to run, and if you want multiple control plane replicas. All Autopilot clusters are _regional_ , which means they have multiple control planes across multiple compute zones in a Google Cloud region.
  * **Fleet membership** : Choose whether you want your cluster to be a member of a fleet.
  * **Networking** : Networking options including the Virtual Private Cloud (VPC) network and subnet the cluster is in, and whether you want your cluster to be accessible from public networks.
  * **Versions and upgrade management** : Use _release channels_ to choose your preferred balance between new features and stability when upgrading this cluster's software, and set maintenance windows and exclusions to choose when upgrades can and can't occur.
  * **Security** : This includes whether the cluster uses Workload Identity Federation for GKE and the service account used by the cluster's nodes to authenticate to Google Cloud.
  * **Cluster features** : Enable and configure additional GKE and Google Cloud features for this cluster, including backups and observability. Standard mode also lets you create short-lived _alpha clusters_ to try out alpha Kubernetes features.



In addition to these, Standard clusters also have options in the following category:

  * **Node pools** : Specify details about your cluster's nodes, including node pools, node operating system, and node sizing.



The following sections look at some of these categories in more detail, particularly those with options where you can't change the setting after you create your cluster. For a complete list of configuration options, see Configuration reference.

The following table compares available options in some key areas for Autopilot and Standard clusters:

Cluster choices | Mode  
---|---  
Autopilot | Standard  
Availability type | Regional | Regional or Zonal  
Release channel | [Rapid](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#channels), [Regular](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#channels), or [Stable](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#channels) | [Any channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#channels)  
Cluster versions | [Default](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#current_versions) or another available version | [Default](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#current_versions) or another available version  
Network routing | VPC-native | VPC-native or Routes-based  
Network isolation | Customizable | Customizable  
Kubernetes features | Production | Production or Alpha  
  
### Cluster availability

With GKE, you can create a cluster tailored to the availability requirements of your workload and your budget. You can choose between regional clusters that have multiple control plane replicas across multiple compute zones in a Google Cloud region, or zonal clusters with a single control plane in a single zone. Autopilot clusters are always regional.

To help you choose which cluster type to create in Standard mode, see [Choosing a regional or zonal control plane](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-scalability#choosing_a_regional_or_zonal_control_plane).

These settings can't be updated after cluster creation: a zonal cluster can't become a regional cluster, and a regional cluster can't become a zonal cluster.

**Best practice** : 

For production workloads, use regional clusters because they generally offer higher availability than zonal clusters. For development environments, use regional clusters with zonal node pools. A cluster with a regional control plane and zonal node pools has the same costs as a zonal cluster. For more information about region-specific considerations, see [Geography and regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). 

#### Regional clusters

A [regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters) has multiple replicas of the control plane, running in multiple zones within your specified Google Cloud [region](https://docs.cloud.google.com/compute/docs/regions-zones). You always need to specify a region when creating an Autopilot or other regional cluster.

For regional Standard clusters only, you can also choose in which zones the cluster's nodes run. Nodes in a regional cluster can run in multiple zones or a single zone depending on the configured node locations. By default, GKE replicates each node pool across three zones of the control plane's region. When you create a regional Standard cluster or when you add a new node pool, you can change the default configuration by specifying the zone(s) in which the cluster's nodes run. All zones must be within the same region as the control plane.

Use regional clusters to run your production workloads, as they offer higher availability than zonal clusters.

  * To create a regional Standard cluster, see [Creating a regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster).
  * To create a regional Autopilot cluster, see [Creating an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).



You can't change a regional cluster's region after cluster creation.

#### Zonal clusters

Zonal clusters have a single control plane in a single [zone](https://docs.cloud.google.com/compute/docs/regions-zones). Workloads still run during a cluster upgrade or an outage of the zone where the control plane runs. However, the cluster, its nodes, and its workloads can't be configured until the control plane is available. Depending on your workload availability requirements, you can choose to distribute your nodes for your zonal cluster in a single zone or in multiple zones.

To create a zonal cluster, see [Creating a zonal cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster).

### Location and distribution of the nodes

Whether you use regional or zonal clusters, you can precisely determine the location and distribution of your nodes across zones. You can configure the default zones for all future node pools, as well as assign or change the specific zones for nodes within existing node pools.

##### Single-zone clusters

A single-zone cluster—which can be a regional or zonal cluster—runs workloads on nodes located in only one [zone](https://docs.cloud.google.com/compute/docs/regions-zones). If that zone experiences an outage, all workloads become unavailable.

Zonal clusters are created by default as single-zone clusters, but you can update this configuration to multi-zonal clusters.

##### Multi-zonal clusters

A multi-zonal cluster—which can be a regional or zonal cluster—enhances workload availability by distributing nodes across multiple [zones](https://docs.cloud.google.com/compute/docs/regions-zones) within a single region. This lets you run workloads across multiple zones in a region. If you run a workload in multiple zones and a zonal outage occurs, the workload is disrupted in that zone but remains available in other zones.

Distributing GKE nodes across multiple zones can incur charges for [cross-zone network egress](https://docs.cloud.google.com/vpc/network-pricing#egress-within-gcp) when nodes need to communicate with peers located in a different zone within the region.

Regional clusters are created by default as multi-zonal clusters, but you can update this configuration to single-zone clusters.

#### AI zones

AI zones are specialized zones used for AI/ML training and inference workloads. These zones provide significant ML accelerator capacity. For more information, see the [AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones) documentation.

In this document and the GKE documentation, "standard zones" or "zones" refer to non-AI zones within a Google Cloud region.

**Important:** Access to AI zones is restricted unless you've enabled them for your Google Cloud project. To use them, [enable AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/manage-ai-zones#enable_ai_zones) ([Preview](https://cloud.google.com/products#product-launch-stages)).

Before you use an AI zone in GKE, consider the following characteristics:

  * AI zones are physically separate from standard zones to provide additional storage space and power. This separation might result in higher latency, which is generally tolerable for AI/ML workloads.
  * AI zones have a suffix with the `ai` notation. For example, an AI zone in the `us-central1` region is named `us-central1-**ai** 1a`.
  * Currently, only TPU VMs are supported.
  * The cluster's control plane runs in one or more standard zones within the same region as the AI zone.
  * You can run VMs without attached TPUs in an AI zone only if you meet the following requirements:

    * You are already running other workloads that use TPU VMs in the same zone.
    * The non-TPU VMs are either Spot VMs, tied to a reservation, or part of a node pool with a specific accelerator-to-general-purpose VM ratio.
**Note:** Even if GKE lets you create the node pool, Compute Engine provisions the VMs only if these conditions are met. For more information, see [AI zones](https://docs.cloud.google.com/compute/docs/regions-zones/ai-zones).
  * AI zones share components, such as networking connections and software rollouts, with standard zones that have the same suffix within the same region. For high-availability workloads, we recommend that you use different zones. For example, avoid using both `us-central1-ai1a` and `us-central1-a` for high availability.




By default, GKE doesn't deploy your workloads in AI zones. To use an AI zone, you must configure one of the following options:

  * **(Recommended) ComputeClasses** : set your highest priority to request on-demand TPUs in an AI zone. ComputeClasses help you define a prioritized list of hardware configurations for your workloads. For an example, see [About ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes#ai-zones).
  * **Node auto-provisioning** : use a `nodeSelector` or `nodeAffinity` in your Pod specification to instruct node auto-provisioning to create a node pool in the AI zone. If your workload doesn't explicitly target an AI zone, node auto-provisioning considers only standard zones or zones from [`--autoprovisioning-locations`](https://cloud.google.com/sdk/gcloud/reference/container/clusters/create#--autoprovisioning-locations) when creating new node pools. This configuration helps ensure that workloads that don't run AI/ML models remain in standard zones unless you explicitly configure otherwise. For an example of a manifest that uses a `nodeSelector`, see [Set the default zones for auto-created nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning#auto-provisioning_locations).
  * **GKE Standard** : if you directly manage your node pools, use an AI zone in the `--node-locations` flag when you create a node pool. For an example, see [Deploy TPU workloads in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus#single-host).



### Fleet membership

If your organization uses multiple clusters, you can simplify multi-cluster management by adding the clusters to a _fleet_ : a logical grouping of Kubernetes clusters. Creating a fleet helps your organization uplevel management from individual clusters to entire groups of clusters, and lets you use fleet-enabled features such as [Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress), [ Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview), and [ Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller).

Although you can add clusters to a fleet at any time, we strongly recommend registering new clusters to a fleet during cluster creation. This is because these "born in the fleet" clusters are created with your chosen fleet-level default settings for a number of enterprise features, and with recommended logs and metrics already enabled. You can learn more about these in the following guides:

  * [Manage fleet-level features](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/manage-features)
  * [Logs enabled by default](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs#default-logs-enterprise)
  * [Metrics enabled by default](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#default-metrics-enterprise)



This setting _can_ be updated after cluster creation to register or unregister the cluster, although we don't recommend moving clusters with live workloads from one fleet to another.

You can learn much more about adding clusters to fleets in [Create fleets to simplify multi-cluster management](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-fleets).

### Networking settings

When creating a GKE cluster, you can specify a number of networking settings, including the network the cluster is in, the network routing mode, and whether you want your cluster nodes to be accessible from public networks.

If you are not a network administrator, you should consult with your organization's Networking specialists before creating a production-ready cluster, as many of these options can't be changed after cluster creation. If you _are_ a network administrator, you can find out much more about GKE networking in [About GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview), with best practices for networking options in [Best practices for GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking). This section describes only a subset of our possible networking options.

#### Network and subnet

The Virtual Private Cloud (VPC) [network](https://docs.cloud.google.com/vpc/docs/vpc) that a cluster is in determines which other Compute Engine resources it is able to communicate with. By default, GKE clusters are created in your project's default network, though you can choose another network if you or your administrator have created one. If available, you can specify that you want your cluster to belong to a specific VPC subnet: again otherwise the default subnet is used. You can also optionally specify that you want to use a particular IP address range within that subnet for your Pods and Services.

These settings can't be updated after cluster creation.

#### Network isolation choices

You can customize network isolation in your cluster by considering the following two aspects:

  * **Access to the control plane** : By default, both the internal endpoint and external endpoint of the control plane are enabled, and the DNS-based endpoint is disabled. You can choose to:

    * Disable both the external and internal endpoint and use only the DNS endpoint.
    * Disable the external endpoint only to prevent access to external clients.
    * Enable authorized networks to control which IP addresses reach the control plane endpoints.
  * **Cluster networking configuration** : You can choose to enable _private nodes_ in your cluster to completely isolate workloads from public networks. You can enable private nodes for entire clusters or at the node pool (for Standard) or workload (for Autopilot) level. Enabling private nodes at the node pool or workload level overrides any node configuration at the cluster level.




These settings can be changed after cluster creation.

For more information on network isolation, see [About customizing network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-isolation) and [Customize your network isolation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation).

**Best practice** : 

Use [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) to provide GKE [Pods](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview#pods) with access to resources with public IP addresses. Cloud NAT improves the overall security posture of the cluster because Pods are not directly exposed to the internet, but are still able to access internet-facing resources.

#### VPC-native and routes-based clusters

In GKE, clusters can be distinguished according to the way they route traffic from one Pod to another Pod. A cluster that uses Alias IP addresses is called a [_VPC-native cluster_](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips). A cluster that uses [ Google Cloud routes](https://docs.cloud.google.com/vpc/docs/routes) is called a [_routes-based cluster_](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/routes-based-cluster).

By default, all new GKE clusters use VPC-native routing, which is our recommended option. You can change this setting at cluster creation to create a routes-based cluster in Standard mode only. This setting can't be updated after cluster creation.

You can learn more about VPC-native clusters and their benefits, including any special requirements they have, in [VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips).

**Best practice** : 

Use the VPC-native network mode for your clusters. This is the default for Autopilot clusters.

### Versions and upgrades

With [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels), GKE picks software versions for a cluster with your chosen balance between feature availability and stability. When you create a cluster, you can choose which release channel you want. New clusters (both Autopilot and Standard) are enrolled in the Regular release channel by default, though you can choose a specific version during cluster creation if required.

Autopilot clusters _always_ use release channels. Standard clusters use release channels by default, however you can choose not to enroll your cluster in a release channel (although we don't recommend this because this setting gives you more limited access to cluster features).

GKE automatically upgrades all clusters over time, regardless of release channel enrollment. GKE automatically upgrades the cluster's control plane and its nodes as new versions become available in that release channel. You can control the timing and scope of upgrades with [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions).

You can change a cluster's release channel at any time.

For information regarding upcoming automatic upgrades, see the [ GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes).

**Best practice** : 

Choose a release channel for GKE to select versions for your cluster with your chosen balance between feature availability and stability. Use maintenance windows and exclusions to control the timing and scope of automatic upgrades.

#### Alpha features (Standard clusters only)

New features in Kubernetes are listed as [Alpha, Beta, or Stable](https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api_changes.md#alpha-beta-and-stable-versions), depending upon their status in development. In most cases, Kubernetes features that are listed as beta or stable are included with GKE clusters.

If you want to experiment with very new features that are not production ready, alpha features are available in special GKE alpha clusters. An [alpha cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters) has all Kubernetes alpha APIs (sometimes called feature gates) enabled. You can use alpha clusters for early testing and validation of Kubernetes features. Alpha clusters are not supported for production workloads, can't be upgraded or added to release channels, and expire within 30 days.

Alpha features are not available for Autopilot clusters.

To create an alpha cluster, see [Creating an alpha cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-alpha-cluster).

### Security settings

GKE has a number of security settings that you can specify at cluster creation. These include encryption settings, security features such as [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs), the service account you want to use for the cluster's nodes (discussed in more detail in the next section), and whether your cluster uses Workload Identity Federation for GKE.

As with other settings, you should consult with expert colleagues — in this case, your organization's Security specialists — before creating a production-ready cluster. You can learn more about GKE security in our [Security overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview) and [Harden your cluster security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster).

#### Service account for nodes

GKE uses IAM service accounts that are attached to your nodes to run system tasks like logging and monitoring. At a minimum, these _node service accounts_ must have the [Kubernetes Engine Default Node Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.defaultNodeServiceAccount) (`roles/container.defaultNodeServiceAccount`) role on your project. By default, GKE uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account), which is automatically created in your project, as the node service account. 

If your organization enforces the [`iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants), the default Compute Engine service account in your project might not automatically get the required permissions for GKE. 

**Note** : If your organization was created on or after May 3, 2024, this constraint is enforced by default. 

If you use the Compute Engine default service account for other functions in your project or organization, the service account might have more permissions than GKE needs, which could expose you to security risks. 

**Best practice:** Instead of using the Compute Engine default service account, create a _custom service account_ for your nodes to use and give it only the permissions that GKE needs to run system tasks. For more information, see [Configure a custom node service account](https://docs.cloud.google.com/kubernetes-engine/security/configure-node-service-accounts#configure-custom-account). 

**You can't change the service account for Autopilot mode clusters or for Standard mode node pools after creation.**

### Node pool settings (Standard clusters only)

As you know from the [Cluster administration overview](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-admin-overview) and [ GKE modes of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode), if you use Autopilot for your clusters you don't need to worry about node configuration because GKE configures your nodes for you. Autopilot cluster nodes are all fully managed by GKE and all use the same [node operating system (OS)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images).

If you choose to create a Standard cluster, you can specify a number of node options when creating a cluster, including:

  * The name, number, size, and location of [node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) you want to use; node pools are groups of nodes within your cluster that share a common configuration.
  * The node OS you want to use for new nodes.
  * Whether you want to use ephemeral [spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms) for nodes.
  * The Compute Engine [machine type](https://docs.cloud.google.com/compute/docs/machine-resource) you want to use for nodes.
  * The service account you want to use for nodes, as described in Security settings.



Some of a cluster's node pool settings can be changed after cluster creation, though all Standard clusters require at least one node pool. If you don't specify a number of nodes and machine type when creating a Standard cluster, its default node pool consists of three nodes in each of the cluster's zones, with the default [node image](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images) `cos_containerd`, and a general-purpose machine type.

You can learn more about node pool configuration in [About node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) and [Add and manage node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools).

## Configuration reference

Find a complete list of possible configuration options in the following reference guides:

  * [`gcloud container clusters create-auto`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto): Google Cloud CLI reference for Autopilot clusters
  * [`gcloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create): Google Cloud CLI reference for Standard clusters
  * [`google_container_cluster`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster#argument-reference): Terraform reference



## What's next

  * Learn more about cluster architecture in [GKE cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture)
  * See a side-by-side comparison of Standard and Autopilot clusters in [Compare GKE Standard and Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-standard-feature-comparison)
  * Start creating clusters: 
    * [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).
    * [Create a Standard zonal cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster).
    * [Create a Standard regional cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
