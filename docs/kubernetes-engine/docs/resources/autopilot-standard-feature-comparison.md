---
url: https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-standard-feature-comparison/
title: Compare features in Autopilot and Standard clusters \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:01:49.493603+00:00
---

# Compare features in Autopilot and Standard clusters  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-standard-feature-comparison/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Compare features in Autopilot and Standard clusters Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page gives you a high-level comparison between Google Kubernetes Engine (GKE) Autopilot clusters and Standard clusters. The comparison includes important GKE features and the functional differences between these cluster modes.

This page is intended for the following people:

  * Platform administrators who want to know the major differences between Autopilot and Standard clusters, so that you can make an informed choice when you create a cluster.
  * New GKE users who are familiar with GKE and want to know which cluster mode offers the most suitable functionality for a specific requirement.

**Tip:** If you are new to GKE, first see the [Start learning about GKE](https://docs.cloud.google.com/kubernetes-engine/docs/learn) page to get an overview of GKE and Kubernetes fundamentals before you select a cluster mode.

The following sections apply only to clusters that you create in Autopilot or Standard mode. After you create a Standard cluster, you can run some workloads in Autopilot mode. These workloads run on nodes that GKE manages for you. For more information about running Autopilot workloads in your Standard clusters, including any settings that might override your cluster-level configuration, see [About Autopilot workloads in GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters).

## Feature comparison of Autopilot and Standard clusters

The following table provides a detailed comparison of the feature configuration in Autopilot and Standard clusters. Either you or GKE define these feature configurations for the entire cluster.

The table doesn't show every feature in GKE. If you want to know whether a feature that isn't in this table is supported in Autopilot or in Standard, check the documentation for that feature.

This table uses the following terminology:

  * **Pre-configured** : always enabled. Google configures these settings. You can't change or disable pre-configured features.
  * **Default** : GKE configures the feature for you if you don't explicitly configure the feature. You can change default feature configurations.
  * **Optional** : available for you to configure and use. Not enabled by default.

Option | Autopilot clusters | Standard clusters  
---|---|---  
  
### Versions and releases

|  **Default** : Regular [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) **Optional** :

  * [Set the release channel](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster#set-version)
  * [Set a specific GKE version in channels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster#set-version)

|  **Default** : Regular [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) **Optional** :

  * [Set the release channel](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster#create-regional-multi-zone-nodepool)
  * [Set a specific GKE version](https://docs.cloud.google.com/kubernetes-engine/versioning#specifying_cluster_version)
  * [Alpha clusters for Kubernetes Alpha APIs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters)

  
  
### Location availability

| **Pre-configured** : [Regional](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#regional_clusters) | **Optional** : Regional or [zonal](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/configuration-overview#zonal)  
  
### Node management

| **Pre-configured** : GKE manages the nodes, including node configuration, autoscaling, and security constraints. | **Optional** :

  * You create and manage nodes in node pools.
  * You let GKE manage some nodes by using an [Autopilot ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters) in your Standard cluster.

  
  
### Node provisioning and scaling

|  **Pre-configured** : Autopilot automatically scales the quantity and size of nodes based on Pods in the cluster. **Optional** :

  * [Horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling).
  * [Vertical Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/vertical-pod-autoscaling): enabled in the cluster, but GKE doesn't configure any Pod autoscaling parameters by default.

|  **Default** :

  * Manually provision new nodes
  * Manually specify node resources

**Optional** :

  * [Node auto-provisioning](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-provisioning)
  * [Cluster autoscaler](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler)
  * Horizontal Pod autoscaling
  * Vertical Pod autoscaling

  
  
### Node operating system

| **Pre-configured** : [Container-Optimized OS with containerd](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#cos) |  **Default** : Container-Optimized OS with containerd **Optional** :

  * [Ubuntu with containerd](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#ubuntu)
  * [Windows Server LTSC](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-images#windows-server)

  
  
### Node compute configuration

|  **Default** : [Container-optimized compute platform](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview#autopilot-compute-platform) (supporting both x86 and Arm architectures) that's recommended for general-purpose workloads. **Optional** :

  * [Built-in ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-compute-classes) for workloads that have specific requirements, such as Spot VMs instances or explicit [Arm architecture](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-arm-workloads) selection.
  * [Custom ComputeClasses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes) for specific node configurations when autoscaling.
  * Hardware accelerators ([GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus) and [TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus-autopilot)).
  * [Local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd)

|  **Default** : [General-purpose Compute Engine machine types](https://docs.cloud.google.com/compute/docs/general-purpose-machines) **Optional** :

  * ComputeClasses: 
    * Autopilot ComputeClasses to [run Autopilot workloads in Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters)
    * Custom ComputeClasses to [set specific node configurations when autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes)
  * Choice of specific [Compute Engine machines and hardware](https://docs.cloud.google.com/compute/docs/machine-resource), such as [Arm architecture](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment), for node pools
  * Hardware accelerators ([GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gpus) and [TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus))
  * [Local SSDs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/local-ssd)

  
  
### Node upgrades and maintenance

|  **Pre-configured** :

  * [Node auto-repair](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair)
  * [Node auto-upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot)
  * [Surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot#surge)

**Optional** :

  * [Manual version upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot#manual-upgrade)
  * [Maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#maintenance-window)
  * [Maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#configuring_a_maintenance_exclusion)

|  **Default** :

  * [Node auto-repair (release channels only)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair)
  * [Node auto-upgrade (release channels only)](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades)

**Optional** :

  * [Manual version upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#upgrading_manually)
  * [Maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#maintenance-window)
  * [Maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#configuring_a_maintenance_exclusion)
  * [Upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pool-upgrade-strategies)

  
  
### Security

|  **Pre-configured** :

  * [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)
  * [Shielded GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes)
  * [Secure boot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes#secure_boot)
  * [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods)

**Optional** :

  * [Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes)
  * [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek)
  * [Application-layer Secrets encryption](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets)
  * [Google Groups for RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#google-groups-for-gke)
  * [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview)

|  **Default** : [Shielded GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes) **Optional** :

  * [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)
  * [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-cmek)
  * [Application-layer Secrets encryption](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/encrypting-secrets)
  * [Google Groups for RBAC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control#google-groups-for-gke)
  * [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview)
  * [Confidential GKE Nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes)
  * [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods)
  * [`PodSecurity` admission controller](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/podsecurityadmission)
  * [Secure boot](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes#secure_boot)

  
  
### Networking

|  **Pre-configured** :

  * [VPC-native](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips)
  * [Maximum 256 Pods in a node](https://docs.cloud.google.com/kubernetes-engine/quotas)
  * [Intranode visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility)
  * DNS: 
    * **[Cloud DNS](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-discovery#cloud_dns):** Version 1.26.4-gke.500 or later
    * **[kube-dns](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-discovery#kube-dns):** Versions earlier than 1.26.4-gke.500

**Default** :

  * Public IPv4 cluster endpoint
  * [Default CIDR ranges for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr#cidr_settings_for_clusters)
  * VPC network name and subnet name
  * [Google-managed IP Range for Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing_secondary_range_svcs)
  * NIC type: 
    * **[Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-gvnic):** For nodes with version 1.30.2-gke.1023000 or later
  * [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2) enabled
  * [Kubernetes network policy using GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy)

**Optional** :

  * [Disable public IPv4 endpoint](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation)
  * [Granting private nodes outbound internet access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation#private-nodes-outbound)
  * [Add control plane authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks)
  * [Increase available IP address range for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr#add_more_pod_ranges_autopilot)

|  **Pre-configured** : [Maximum 512 Pods in each node](https://docs.cloud.google.com/kubernetes-engine/quotas) **Default** :

  * 110 Pods in each node
  * [VPC-native](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips)
  * Public IPv4 cluster endpoint
  * VPC network name and subnet name
  * [kube-dns](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-discovery#kube-dns)

**Optional** :

  * [Intranode visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility)
  * [Increase available IP address range for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr#add_more_pod_ranges_standard)
  * [Disable public IPv4 endpoint](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/latest/network-isolation)
  * [Add control plane authorized networks](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/authorized-networks)
  * [Kubernetes network policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy)
  * [GKE Dataplane V2 enabled](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2)
  * [Cloud DNS](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-discovery#cloud_dns)
  * [Google Virtual NIC (gVNIC)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-gvnic)

  
  
### Logging and monitoring

|  **Pre-configured** :

  * [System-level logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs#available-logs)
  * [Workload-level logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs#available-logs)
  * [System-level monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#system-metrics)
  * [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus)

**Optional** :

  * [Control plane metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/control-plane-metrics)
  * [Control plane logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-logs#control_plane_logs)

|  **Default** :

  * [System-level logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs#available-logs)
  * [Workload-level logs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-logs#available-logs)
  * [System-level monitoring](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-metrics#system-metrics)
  * [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus)

**Optional** :

  * [Control plane metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/control-plane-metrics)
  * [Control plane logs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-logs#control_plane_logs)

  
  
### Add-ons

|  **Pre-configured** :

  * [HTTP load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress)
  * [Compute Engine persistent disk CSI Driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver)
  * [Filestore CSI Driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver)
  * [Cloud Storage FUSE CSI Driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver)
  * [NodeLocal DNSCache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache)
  * [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming)

**Optional** : [Managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview), which also provides Istio mesh capabilities. |  **Default** :

  * [Compute Engine persistent disk CSI Driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/gce-pd-csi-driver)
  * [Filestore CSI Driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/filestore-csi-driver)

**Optional** :

  * [Cilium](https://cilium.io/) [network policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy)
  * [Cloud Storage FUSE CSI Driver](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/cloud-storage-fuse-csi-driver)
  * [NodeLocal DNSCache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache)
  * [HTTP load balancing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress)
  * [Cloud Run](https://docs.cloud.google.com/run/docs)
  * [Cloud TPU](https://docs.cloud.google.com/tpu/docs/tpus)
  * [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview)
  * [Managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview)
  * [Kalm](https://docs.kalm.dev/)
  * [Usage metering](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering)
  * [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming)

  
  
## Functional differences between Autopilot and Standard clusters

The following table shows you important functional differences between GKE Autopilot and Standard clusters. Use this comparison to make a more informed choice of mode.

Functionality | Autopilot clusters | Standard clusters  
---|---|---  
Third-party monitoring tools | Deploy a third-party monitoring tool provided by [Google Cloud partners](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners#allowlisted-partner-workloads), or any third-party tool that doesn't require elevated access on the node.  | Deploy any third-party monitoring tool regardless of the level of node access.  
Expose applications externally | Use a [`LoadBalancer` Service](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer). This provisions an ephemeral external IP address for you. If you already have a static IP address that you want to use, specify it in the `loadBalancerIP` field. Autopilot doesn't support the `externalIps` field, which doesn't use Google Cloud load balancing. | Use a [`LoadBalancer` Service](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer). This provisions an ephemeral external IP address for you. If you already have a static IP address that you want to use, specify it in the `loadBalancerIP` field. You can also use the [`externalIps`](https://kubernetes.io/docs/concepts/services-networking/service/#external-ips) field in the Service manifest, although we don't recommend this approach.  
Pod bursting | Pods can burst into unused burstable capacity if your resource limits are greater than your resource requests, or if you don't set resource limits. The burstable capacity depends on whether the Pod requests specific hardware. For more information, see [Configure Pod bursting in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-bursting-gke#burstable-capacity). | Pods can burst into unused node capacity if your resource limits are greater than your resource requests. In Standard, you pay for node capacity regardless of whether Pods use the resources. Don't rely on Pod bursting. Evaluate and set adequate resource requests and limits for your workloads.  
Google Cloud Marketplace applications | You can't install apps from [Cloud Marketplace](https://docs.cloud.google.com/marketplace). | You can install apps from [Cloud Marketplace](https://docs.cloud.google.com/marketplace).  
Built-in security constraints | In Autopilot mode, GKE enforces the [GKE Autopilot security measures](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security). | GKE does not automatically enforce security constraints for Standard clusters. If some of the nodes in the cluster run Autopilot workloads by using a ComputeClass, the [GKE Autopilot security measures](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-security) apply to those nodes on a best-effort basis.   
Long-running fault-intolerant Pods | You can protect fault-intolerant Pods such as game servers from eviction caused by node auto-upgrades or scale-downs for up to 7 days. For details, see [Extend the run time of Autopilot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/extended-duration-pods). | You can't protect fault-intolerant Pods from eviction caused by node auto-upgrades. You can protect those Pods from scale-down eviction indefinitely, but you continue to pay for the underutilized nodes on which the Pods run.  
  
## What's next

  * Learn more about [cluster configuration choices](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters).
  * Learn how to [choose a mode of operation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode).
  * Learn how to [create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
