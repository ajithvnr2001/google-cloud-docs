---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-scalability/
title: Best practices for GKE scalability \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:50.384384+00:00
---

# Best practices for GKE scalability  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-scalability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Best practices for GKE scalability Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes general best practices for architecting scalable GKE clusters. You can apply these recommendations on all clusters and workloads to achieve the optimal performance. These recommendations are especially important for clusters that you plan to largely scale. Best practices are intended for administrators responsible for provisioning the infrastructure and for developers who prepare kubernetes components and workloads.

For a consolidated overview of all GKE best practices, see [Best practices for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices). 

## What is scalability?

In a Kubernetes cluster, scalability refers to the ability of the cluster to grow while staying within its [service-level objectives (SLOs)](https://landing.google.com/sre/sre-book/chapters/service-level-objectives/). Kubernetes also has its [own set of SLOs](https://github.com/kubernetes/community/blob/master/sig-scalability/slos/slos.md)

Kubernetes is a complex system, and its ability to scale is determined by multiple factors. Some of these factors include the type and number of nodes in a node pool, the types and numbers of node pools, the number of Pods available, how resources are allocated to Pods, and the number of Services or backends behind a Service.

## Best practices for availability

### Choosing a regional or zonal control plane

Due to architectural differences, regional clusters are better suited for high availability. Regional clusters have multiple control planes across multiple compute zones in a region, while zonal clusters have one control plane in a single compute zone.

If a zonal cluster is upgraded, the control plane VM experiences downtime during which the Kubernetes API is not available until the upgrade is complete.

In regional clusters, the control plane remains available during cluster maintenance like rotating IPs, upgrading control plane VMs, or resizing clusters or node pools. When upgrading a regional cluster, at least one of multiple control plane VMs is always running during the rolling upgrade, so the Kubernetes API is still available. Similarly, a single-zone outage won't cause any downtime in the regional control plane.

However, the more highly available regional clusters come with certain trade-offs:

  * Changes to the cluster's configuration take longer because they must propagate across all control planes in a regional cluster instead of the single control plane in zonal clusters.

  * You might not be able to create or upgrade regional clusters as often as zonal clusters. If VMs cannot be created in one of the zones, whether from a lack of capacity or other transient problem, clusters cannot be created or upgraded.




Due to these trade-offs, zonal and regional clusters have different use cases:

  * Use zonal clusters to create or upgrade clusters rapidly when availability is less of a concern.
  * Use regional clusters when availability is more important than flexibility.



Carefully select the cluster type when you create a cluster because you cannot change it after the cluster is created. Instead, you must create a new cluster then migrate traffic to it. Migrating production traffic between clusters is possible but difficult at scale.

**Important:** Use regional clusters for production workloads clusters as they offer higher availability than zonal clusters.

### Choosing multi-zonal or single-zone node pools

To achieve high availability, the Kubernetes control plane and its nodes need to be spread across different zones. GKE offers two types of node pools: single-zone and multi-zonal.

To deploy a highly available application, [distribute your workload](https://docs.cloud.google.com/compute/docs/tutorials/robustsystems#distribute) across multiple compute zones in a region by using multi-zonal node pools which distribute nodes uniformly across zones.

**Note:** While you can use the cluster autoscaler with multi-zonal node pools, nodes are not guaranteed to be spread equally among zones.

If all your nodes are in the same zone, you won't be able to schedule Pods if that zone becomes unreachable. Using multi-zonal node pools has certain trade-offs:

  * GPUs are available only in specific [zones](https://docs.cloud.google.com/compute/docs/regions-zones). It may not be possible to get them in all zones in the region.

  * Round-trip latency between zones within a single region might be higher than that between resources in a single zone. The difference should be immaterial for most workloads.

  * The price of egress traffic between zones in the same region is available on the [Compute Engine pricing page](https://cloud.google.com/vpc/network-pricing).


**Important:** Default to using multi-zonal node pools because they offer higher availability. Use single-zone node pools if your app is fragile to network partitioning or if it uses GPUs.

### Choose AI zones

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



## Best practices for scale

### Base infrastructure

Kubernetes workloads require networking, compute, and storage. You need to provide enough CPU and memory to run Pods. However, there are more parameters of underlying infrastructure that can influence performance and scalability of a GKE cluster.

### Cluster networking

Using a _VPC-native cluster_ is the networking default and the recommended choice for [setting up](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips) new GKE clusters. VPC-native clusters allow for larger workloads, higher number of nodes, and some other [advantages](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#benefits).

In this mode, the VPC network has a secondary range for all Pod IP addresses. Each node is then assigned a slice of the secondary range for its own Pod IP addresses. This allows the VPC network to natively understand how to route traffic to Pods without relying on custom routes. A single VPC network can have [up to 15,000](https://docs.cloud.google.com/vpc/docs/quota#per_network) VMs.

Another approach, which is deprecated and supports no more than 1,500 nodes, is to use a _routes-based cluster_. A routes-based cluster is not a good fit for large workloads. It consumes VPC routes quota and lacks other benefits of the VPC-native networking. It works by adding a new [custom route](https://docs.cloud.google.com/vpc/docs/routes#custom-routes) to the routing table in the VPC network for each new node.

### Cluster size

GKE Standard clusters support scaling up to 65,000 nodes. Depending on your target node count, there are specific infrastructure requirements, and you might need to contact Cloud Customer Care. For detailed information, see [Cluster size limits and requirements](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters#clusters-5k-nodes).

### Cluster load balancing

GKE Ingress and Cloud Load Balancing configure and deploy load balancers to expose Kubernetes workloads outside the cluster and also to the public internet. The GKE Ingress and Service controllers deploy objects such as forwarding rules, URL maps, backend services, network endpoint groups, and more on behalf of GKE workloads. Each of these resources has inherent [quotas and limits](https://docs.cloud.google.com/load-balancing/docs/quotas) and these limits also apply in GKE. When any particular Cloud Load Balancing resource has reached its quota, it will prevent a given Ingress or Service from deploying correctly and errors will appear in the resource's events.

The following table describes the scaling limits when using GKE Ingress and Services:

Load balancer | Node limit per cluster  
---|---  
Internal passthrough Network Load Balancer | 

  * [ 250 nodes ](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#limits) without backend subsetting 
  * [ 2,000 nodes ](https://docs.cloud.google.com/load-balancing/docs/quotas#backend_services) with backend [ internal passthrough Network Load Balancer subsetting ](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing#subsetting) enabled 

  
Regional external passthrough Network Load Balancer | 1000 nodes per zone  
External Application Load Balancer | 

  * 1000 nodes per zone
  * No node limit when using [ container-native load balancing ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/container-native-load-balancing)

  
Internal Application Load Balancer | No node limit  
  
If you need to scale further, contact your Google Cloud sales team to increase this limit.

### DNS

Service discovery in GKE is provided through [kube-dns](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-discovery) which is a centralized resource to provide DNS resolution to Pods running inside the cluster. This can become a bottleneck on very large clusters or for workloads which have a high request load. GKE automatically autoscales kube-dns based on the size of the cluster to increase its capacity. When this capacity is still not enough, GKE offers distributed, local resolution of DNS queries on each node with [NodeLocal DNSCache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache). This provides a local DNS cache on each GKE node which answers queries locally, distributing the load and providing faster response times.

**Important:** For large-scale clusters or high DNS request load, enable [NodeLocal DNS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache) for more distributed DNS serving.

### Managing IP addresses in VPC-native clusters

A VPC-native cluster uses three IP address ranges:

  * **Primary range for node subnet** : Defaults to /20 (4092 IP addresses).
  * **Secondary range for Pod subnet** : Defaults to /14 (262,144 IP addresses). However, you can configure the Pod subnet.
  * **Secondary range for Service subnet** : Defaults to /20 (4096 addresses). However, you can't change this range after you create this Service subnet.



For more information, see [IP address ranges for VPC-native clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#cluster_sizing).

IP address limitations and recommendations:

  * **Node limit** : Node limit is determined by both the primary and Pod IP addresses per node. There must be enough addresses in both node and Pod IP address ranges to provision a new node. By default, you can create only 1024 nodes due to Pod IP address limitations.
  * **Pod limit per node** : By default, the Pod limit per node is 110 Pods. However, you can [configure smaller Pod CIDRs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr) for efficient use with fewer Pods per node.
  * **Scaling beyond RFC 1918** : If you require more IP addresses than available within the private space defined by RFC 1918, then we recommend using [non-RFC 1918 private addresses](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#enable_reserved_ip_ranges) or [PUPIs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#enable_pupis) for additional flexibility.
  * **Secondary IP address range for Service and Pod** : By default, you can configure 4096 Services. However, you can configure more Services by choosing the Service subnet range. You cannot modify secondary ranges after creation. When you create a cluster, ensure that you choose ranges large enough to accommodate anticipated growth. However, you can add more IP addresses for Pods later by using [discontiguous multi-Pod CIDR](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr).



For more information, see the following:

  * [Not enough free IP address space for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#not_enough_space)
  * [Node limiting ranges](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#node_limiters)
  * [Plan IP addresses when migrating to GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-ip-address-mgmt-strategies#understanding_address_demand)



### Configuring nodes for better performance

GKE nodes are regular Google Cloud virtual machines. Some of their parameters, for example the number of cores or size of disk, can influence how GKE clusters perform.

### Reducing Pod initialization times

You can use [Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming) to stream data from eligible container images as your workloads request them, which leads to faster initialization times. To compare other options across node provisioning, image pulling, and application startup, see [Strategies to reduce startup latency](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/startup-latency-reduction-strategies).

### Egress traffic

In Google Cloud, the machine type and the number of cores allocated to the instance determine its network capacity. Maximum egress bandwidth varies from 1 to 32 Gbps, while the maximum egress bandwidth for default e2-medium-2 machines is 2 Gbps. For details on bandwidth limits, see [Shared-core machine types](https://docs.cloud.google.com/compute/docs/machine-types#sharedcore).

### IOPS and disk throughput

In Google Cloud, the size of persistent disks determines the IOPS and throughput of the disk. GKE typically uses Persistent Disks as boot disks and to back Kubernetes' Persistent Volumes. Increasing disk size increases both IOPS and throughput, up to [certain limits](https://docs.cloud.google.com/compute/docs/disks/performance#size_price_performance).

Each persistent disk write operation contributes to your virtual machine instance's cumulative [network egress cap](https://docs.cloud.google.com/vpc/docs/quota#per_instance). Thus IOPS performance of disks, especially SSDs, also depend on the number of vCPUs in the instance in addition to disk size. Lower core VMs have lower write IOPS limits due to network egress limitations on write throughput.

If your virtual machine instance has insufficient CPUs, your application won't be able to get close to [IOPS limit](https://docs.cloud.google.com/compute/docs/disks/performance#size_price_performance). As a general rule, you should have one available CPU for every 2000-2500 IOPS of expected traffic.

**Important:** Use larger and fewer disks to achieve higher IOPS and throughput.

Workloads that require high capacity or large numbers of disks need to consider the limits of how many PDs can be attached to a single VM. For regular VMs, that [limit](https://docs.cloud.google.com/compute/docs/machine-types#general_purpose) is 128 disks with a total size of 64 TB, while [shared-core VMs have a limit](https://docs.cloud.google.com/compute/docs/machine-types#sharedcore) of 16 PDs with a total size of 3 TB. Google Cloud enforces this limit, not Kubernetes.

### Monitor control plane metrics

Use the available [control plane metrics](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/control-plane-metrics) to configure your monitoring dashboards. You can use control plane metrics to observe the health of the cluster, observe the results of cluster configuration changes (for example, deploying additional workloads or third-party components) or when troubleshooting issues.

One of the most important metrics to monitor is the [latency](https://docs.cloud.google.com/stackdriver/docs/solutions/gke/control-plane-metrics#apiserver_monitor_latency) of the Kubernetes API. Increases in latency indicate that the system is overloaded. Be aware that LIST calls that transfer large amounts of data are expected to have much higher latency than smaller requests.

Increased Kubernetes API latency can also be caused by slow responses from third party [admission webhooks](https://kubernetes.io/docs/reference/access-authn-authz/extensible-admission-controllers). You can use metrics to measure the latency of webhooks to detect such common issues.

The suggested upper bound for a single-resource call such as GET, POST, or PATCH is one second. The suggested upper bound for both namespace-scoped and cluster-scoped LIST calls is 30 seconds. The upper-bound expectations are set by SLOs that are defined by the open source Kubernetes community. For more information, see [API call latency SLIs/SLOs details](https://github.com/kubernetes/community/blob/master/sig-scalability/slos/api_call_latency.md).

## Best practices for Kubernetes developers

### Use list and watch pattern instead of periodic listing

As a Kubernetes developer, you might need to create a component having the following requirements:

  * Your component needs to retrieve the list of some Kubernetes objects periodically.
  * Your component needs to run in multiple instances (in case of DaemonSet, even on each node).



Such a component can generate load spikes on the kube-apiserver, even if the state of periodically retrieved objects is not changing.

The simplest approach is to use periodic LIST calls. However, this is an inefficient and expensive approach for both the caller and the server because all objects must be loaded to the memory, serialized, and transferred each time. The excessive use of LIST requests might overload the control plane or generate heavy throttling of such requests.

You can improve your component by setting [resourceVersion=0 parameter](https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions) on LIST calls. This allows kube-apiserver to use in-memory object cache and reduces how often the Kubernetes API server interacts with the etcd API, which also reduces any related processing.

We highly recommend avoiding repeatable LIST calls and replace them with the list and watch pattern. List the objects once and then use [Watch API](https://kubernetes.io/docs/reference/using-api/api-concepts/#efficient-detection-of-changes) to get incremental changes of the state. This approach reduces processing time and minimizes traffic compared to periodic LIST calls. When objects do not change, no additional load is generated.

If you use Go language, then check [SharedInformer](https://pkg.go.dev/k8s.io/client-go/tools/cache#SharedInformer) and [SharedInformerFactory](https://pkg.go.dev/k8s.io/client-go/informers#NewSharedInformerFactory) for Go packages implementing this pattern.

**Note:** The previous recommendation promotes usage of watches (as a better option than repeatable list). The following sections promote reduction of general API traffic. These recommendations are not contradictory but provide you with next level optimizations.

### Limit unnecessary traffic generated by watches and lists

Kubernetes internally uses [watches](https://kubernetes.io/docs/reference/using-api/api-concepts/#efficient-detection-of-changes) to send notifications about object updates. Even with watches requiring much less resources than periodic LIST calls, processing of watches in large clusters can take a significant portion of cluster resources and affect the cluster performance. The biggest, negative impact is generated by creating watches that observe frequently changing objects from multiple places. For example, by observing data about all Pods from a component running on all nodes. If you install third-party code or extensions on your cluster, they can create such watches under the hood.

We recommend the following best practices:

  * Reduce unnecessary processing and traffic generated by watches and LIST calls.
  * Avoid creating watches that observe frequently changing objects from multiple places (for example DaemonSets).
  * (Highly recommended) Create a central controller that watches and processes required data on a single node.
  * Watch only a subset of the objects, for example, kubelet on each node observes only pods scheduled on the same node.
  * Avoid deploying third party components or extensions that could impact cluster performance by making a high volume of watches or LIST calls.



### Use rolling updates with DaemonSets to prevent sudden traffic increases

When a DaemonSet is created in a cluster, it schedules a new Pod in every node immediately. If all those new Pods connect to the same network endpoint, those requests occur simultaneously, which puts a high load on the target host. To prevent this, [configure your DaemonSets with rolling updates](https://kubernetes.io/docs/tasks/manage-daemon/update-daemon-set/) with limited `maxSurge` Pods.

### Limit Kubernetes object manifest size

If you need fast operations that require high Pod throughput, such as resizing or updating large workloads, make sure to keep Pod manifest sizes to a minimum, ideally smaller than 10 KiB.

Kubernetes stores resource manifests in a database that's a key-value store. The entire manifest is sent every time the resource is retrieved, including when you use the list and watch pattern.

Manifest size has the following limitations:

  * **Maximum size for each object manifest** : Approximately 1.5 MiB.
  * **Total quota for all Kubernetes API objects in the cluster:** The pre-configured quota size is 6 GiB. This includes a change log with all updates to all objects in the most recent 150 seconds of cluster history.
  * **Control plane performance during high traffic periods:** Larger manifest sizes increase the load on the API server.



For single, rarely processed objects, the manifest size is usually not a concern as long as it's smaller than 1.5 MiB. However, manifest sizes larger than 10 KiB for numerous, frequently processed objects - such as pods in very large workloads - can cause increased API call latency and decreased overall performance. Lists and watches in particular can be significantly affected by large manifest sizes. You might also have issues with the quota of the cluster state database, because the quantity of revisions in the last 150 seconds can accumulate quickly during periods of high API server traffic.

To reduce a pod's manifest size, Kubernetes ConfigMaps can be leveraged to store part of the configuration, particularly the part that is shared by multiple pods in the cluster. For example, environment variables are often shared by all pods in a workload.

Note that it's also possible to run into similar issues with ConfigMap objects if they are as numerous, as large, and processed as frequently as the pods. Extracting part of the configuration is most useful when it decreases overall traffic.

### Disable automounting of default service account

If logic running in your Pods does not need to access Kubernetes API, you should [disable the default, automatic mounting of service account](https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/#use-the-default-service-account-to-access-the-api-server) to avoid creation of related Secrets and watches.

When you create a Pod without specifying a service account, Kubernetes automatically does the following actions:

  * Assigns the default service account to the Pod.
  * Mounts the service account credentials as a Secret for the Pod.
  * For every mounted Secret, the kubelet creates a watch to observe changes to that Secret on every node.



In large clusters, these actions represent thousands of unnecessary watches which may put a significant load on the kube-apiserver.

### Use Protocol buffers instead of JSON for API requests

Use [protocol buffers](https://developers.google.com/protocol-buffers) when implementing highly scalable components as described in [Kubernetes API Concepts](https://kubernetes.io/docs/reference/using-api/api-concepts/#alternate-representations-of-resources).

Kubernetes REST API supports JSON and protocol buffers as a serialization format for objects. JSON is used by default but protocol buffers are more efficient for performance at scale because it requires less CPU intensive processing and sends less data over the network. The overhead related to processing of JSON can cause timeouts when listing large-size data.

## What's next?

  * [Plan for large GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters)
  * [Plan for large workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-workloads)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
