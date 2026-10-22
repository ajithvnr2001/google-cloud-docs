---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/scale/
title: Scale up Google Distributed Cloud clusters \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:20.003099+00:00
---

# Scale up Google Distributed Cloud clusters  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/scale/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Scale up Google Distributed Cloud clusters Stay organized with collections  Save and categorize content based on your preferences. 

Like any Kubernetes cluster, Google Distributed Cloud cluster scalability has many interrelated dimensions. This document is intended to help you understand the key dimensions that you can adjust to scale up your clusters without disrupting your workloads.

## Understanding the limits

Google Distributed Cloud is a complex system with a large integration surface. There are many dimensions that affect cluster scalability. For example, the number of nodes is only one of many dimensions on which Google Distributed Cloud can scale. Other dimensions include the total number of Pods and Services. Many of these dimensions, such as the number of pods per node and the number of nodes per cluster, are interrelated. For more information about the dimensions that have an effect on scalability, see [Kubernetes Scalability thresholds](https://github.com/kubernetes/community/blob/master/sig-scalability/configs-and-limits/thresholds.md) in the Scalability Special Interest Group (SIG) section of the Kubernetes Community repository on GitHub.

Scalability limits are also sensitive to the hardware and node configuration on which your cluster is running. The limits described in this document are verified in an environment that's likely different from yours. Therefore, you might not reproduce the same numbers when the underlying environment is the limiting factor.

For more information about the limits that apply to your Google Distributed Cloud clusters, see [Quotas and limits](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/limits).

## Prepare to scale

As you prepare to scale your Google Distributed Cloud clusters, consider the requirements and limitations described in the following sections.

### Control plane node CPU and memory requirements

The following table outlines the recommended CPU and memory configuration for control plane nodes for clusters running production workloads:

Number of cluster nodes | Recommended control plane CPUs | Recommended control plane memory  
---|---|---  
1-50 | 8 cores | 32 GiB  
51-100 | 16 cores | 64 GiB  
  
### Number of Pods and Services

The number of Pods and Services you can have in your clusters is controlled by the following settings:

  * [`clusterNetwork.pods.cidrBlocks`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#clusternetwork-pods-cidrblocks) specifies the number of Pods allowed in your cluster.

  * [`nodeConfig.podDensity.maxPodsPerNode`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#nodeconfig-poddensity-maxpodspernode) specifies the maximum number of Pods that can run on a single node.

  * [`clusterNetwork.services.cidrBlocks`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#clusternetwork-services-cidrblocks) specifies the number of Services allowed in your cluster.




#### Pod CIDR and maximum node number

The total number of IP addresses reserved for Pods in your cluster is one of the limiting factors for scaling up your cluster. This setting, coupled with the setting for maximum pods per node, determines the maximum number of nodes you can have in your cluster before you risk exhausting IP addresses for your pods.

Consider the following:

  * The total number of IP addresses reserved for Pods in your cluster is specified with [`clusterNetwork.pods.cidrBlocks`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#clusternetwork-pods-cidrblocks), which takes a range of IP addresses specified in [CIDR notation](https://datatracker.ietf.org/doc/html/rfc1519). For example, the pre-populated value `192.168.0.0/16` specifies a range of 65,536 IP addresses from `192.168.0.0` to `192.168.255.255`.

  * The maximum number of Pods that can run on a single node is specified with [`nodeConfig.podDensity.maxPodsPerNode`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#nodeconfig-poddensity-maxpodspernode).

  * Based on the maximum pods per node setting, Google Distributed Cloud provisions approximately twice as many IP addresses to the node. The extra IP addresses help prevent inadvertent reuse of the Pod IPs in a short span of time.

  * Dividing the total number of Pod IP addresses by the number of Pod IP addresses provisioned on each node gives you the total number of nodes you can have in your cluster.




For example, if your Pod CIDR is `192.168.0.0/17`, you have a total of 32,768 IP addresses (2(32-17) = 215 = 32,768). If you set the maximum number of Pods per node to 250, Google Distributed Cloud provisions a range of approximately 500 IP addresses, which is roughly equivalent to a `/23` CIDR block (2(32-23) = 29 = 512). So the maximum number of nodes in this case is 64 (215 addresses/cluster divided by 29 addresses/node = 2(15-9) nodes/cluster = 26 = 64 nodes/cluster).

Both `clusterNetwork.pods.cidrBlocks` and `nodeConfig.podDensity.maxPodsPerNode` are **immutable so plan carefully** for the future growth of your cluster to avoid running out of node capacity. For the recommended maximums for Pods per cluster, Pods per node, and nodes per cluster based on testing, see [Limits](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/limits#limits).

#### Service CIDR

Your Service CIDR can be updated to _add_ more Services as you scale up your cluster. You can't, however, reduce the Service CIDR range. For more information, see [Increase Service network range](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters#increase_service_network_range).

### Resources reserved for system daemons

By default, Google Distributed Cloud automatically reserves resources on a node for system daemons, such as `sshd` or `udev`. CPU and memory resources are reserved on a node for system daemons so that these daemons have the resources they require. Without this feature, Pods can potentially consume most of the resources on a node, making it impossible for system daemons to complete their tasks.

Specifically, Google Distributed Cloud reserves 80 millicores of CPU (80 mCPU) and 280 Mebibytes (280 MiB) of memory on each node for system daemons. Note that the CPU unit _mCPU_ stands for thousandth of a core, and so 80/1000 or 8% of a core on each node is reserved for system daemons. The amount of reserved resources is small and doesn't have a significant impact on Pod performance. However, the kubelet on a node may evict Pods if their use of CPU or memory exceeds the amounts that have been allocated to them.

### Networking with MetalLB

You might want to increase the number MetalLB speakers to address the following aspects:

  * Bandwidth: the entire cluster bandwidth for load balancing services depends on the number of speakers and the bandwidth of each speaker node. Increased network traffic requires more speakers.

  * Fault tolerance: more speakers reduces the overall impact of a single speaker failure.




MetalLB requires Layer 2 connectivities between the load balancing nodes. In this case, you might be bounded by the number of nodes with Layer 2 connectivity where you can put MetalLB speakers on.

Plan carefully about how many MetalLB speakers you want to have in your cluster and determine how many Layer 2 nodes you need. For more information, see MetalLB scalability issues.

Separately, when using the bundled load balancing mode, the control plane nodes also need to be under the same Layer 2 network. Manual load balancing doesn't have this restriction. For more information, see [Manual load balancer mode](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/load-balance#manual_load_balancer_mode).

## Running many nodes, Pods, and Services

Adding nodes, Pods, and Services is a way to scale up your cluster. The following sections cover some additional settings and configurations you should consider when you increase the number of nodes, Pods, and Services in your cluster. For information about the limits for these dimensions and how they relate to each other, see [Limits](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/limits#limits).

### Create a cluster without `kube-proxy`

To create a high-performance cluster that can scale up to use a large number of Services and endpoints, we recommend that you create the cluster without `kube-proxy`. Without `kube-proxy`, the cluster uses GKE Dataplane V2 in _kube-proxy-replacement_ mode. This mode avoids resource consumption required for maintaining a large set of iptables rules.

You can't disable the use of `kube-proxy` for an existing cluster. This configuration must be set up when the cluster is created. For instructions and more information, see [Create a cluster without kube-proxy](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/no-kube-proxy).

### CoreDNS configuration

This section describes aspects of CoreDNS that affect scalability for your clusters.

#### Pod DNS

By default, Google Distributed Cloud clusters inject Pods with a `resolv.conf` that looks like the following:
    
    
    nameserver KUBEDNS_CLUSTER_IP
    search <NAMESPACE>.svc.cluster.local svc.cluster.local cluster.local c.PROJECT_ID.internal google.internal
    options ndots:5
    

The option `ndots:5` means that hostnames that have fewer than 5 dots aren't considered a fully qualified domain name (FQDN). The DNS Server appends all the specified search domains before it looks up the originally requested hostname, which orders lookups like the following when resolving `google.com`:

  1. `google.com.NAMESPACE.svc.cluster.local`
  2. `google.com.svc.cluster.local`
  3. `google.com.cluster.local`
  4. `google.com.c.PROJECT_ID.internal`
  5. `google.com.google.internal`
  6. `google.com`



Each of the lookups is performed for IPv4 (A record) and IPv6 (AAAA record), resulting in 12 DNS requests for each non-FQDN query, which significantly amplifies DNS traffic. To mitigate this issue, we recommend that you declare the hostname to lookup as an FQDN by adding a trailing dot (`google.com.`). This declaration needs to be done at the application workload level. For more information, see the [`resolv.conf` man page](https://linux.die.net/man/5/resolv.conf).

#### IPv6

If the cluster isn't using IPv6, it's possible to reduce the DNS requests by half by eliminating the `AAAA` record lookup to the upstream DNS server. If you need help disabling `AAAA` lookups, reach out to [Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support).

#### Dedicated node pool

Due to the critical nature of DNS queries in application lifecycles, we recommend that you use dedicated nodes for the `coredns` Deployment. This Deployment falls under a different failure domain than normal applications. If you need help setting up dedicated nodes for the `coredns` Deployment, reach out to [Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support).

### MetalLB scalability issues

MetalLB runs in active-passive mode, meaning that at any point of time, there's only a single MetalLB speaker serving a particular `LoadBalancer` VIP.

#### Failover

Before Google Distributed Cloud release 1.28.0, under large scale, the failover of MetalLB could take a long time and can present a reliability risk to the cluster.

#### Connection limits

If there's a particular `LoadBalancer` VIP, such as an Ingress Service, that expects close to or more than 30k concurrent connections, then it's likely that the speaker node handling the VIP might [exhaust available ports](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/limits#lb_conn_limit). Due to an architecture limitation, there's no mitigation for this problem from MetalLB. Consider switching to [bundled load balancing with BGP](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/lb-bundled-bgp) before cluster creation or use a different ingress class. For more information, see Ingress configuration.

#### Load balancer speakers

By default, Google Distributed Cloud uses the same load balancer node pool for both the control plane and the data plane. If you don't specify a load balancer node pool ([`loadBalancer.nodePoolSpec`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/bundled-lb#loadbalancernodepoolspec)), the control plane node pool (`controlPlane.nodePoolSpec`) is used.

To grow the number of speakers when you use the control plane node pool for load balancing, you must increase the number of control plane machines. For production deployments, we recommend that you use three control plane nodes for high availability. Increasing the number of control plane nodes beyond three to accommodate additional speakers might not be a good use of your resources.

### Ingress configuration

If you expect close to 30k concurrent connections coming into one single `LoadBalancer` Service VIP, MetalLB might not be able to support it.

You can consider exposing the VIP through other mechanisms, such as F5 BIG-IP. Alternatively, you can create a new cluster using [bundled load balancing with BGP](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/lb-bundled-bgp). which doesn't have the same limitation.

### Fine tune Cloud Logging and Cloud Monitoring components

In large clusters, depending on the application profiles and traffic pattern, the default resource configurations for the Cloud Logging and Cloud Monitoring components might not be sufficient. For instructions to tune the resource requests and limits for the observability components, refer to [Configuring Stackdriver component resources](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/log-monitoring#configuring_stackdriver_component_resources).

In particular, kube-state-metrics in clusters with a large number of services and endpoints might cause excessive memory usage on both the `kube-state-metrics` itself and the `gke-metrics-agent` on the same node. The resource usage of metrics-server can also scale in terms of nodes, Pods, and Services. If you experience resource issues on these components, reach out to [ Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support).

### Use sysctl to configure your operating system

We recommend that you fine tune the operating system configuration for you nodes to best fit your workload use case. The `fs.inotify.max_user_watches` and `fs.inotify.max_user_instances` parameters that control the number of inotify resources often need tuning. For example, if you see error messages like the following, then you might want to try to see if these parameters need to be tuned:
    
    
    The configured user limit (128) on the number of inotify instances has been reached
    
    
    
    ENOSPC: System limit for number of file watchers reached...
    

Tuning usually varies by workload types and hardware configuration. You can consult about the specific OS best practices with your OS vendor.

## Best practices

This section describes best practices for scaling up your cluster.

### Scale one dimension at a time

To minimize problems and make it easier to roll back changes, don't adjust more than one dimension at the time. Scaling up multiple dimensions simultaneously can cause problems even in smaller clusters. For example, trying to increase the number of Pods scheduled per node to 110 while increasing the number of nodes in the cluster to 250 likely won't succeed because the number of Pods, the number of Pods per node, and the number of nodes are stretched too far.

### Scale clusters in stages

Scaling up a cluster can be resource-intensive. To reduce the risk of cluster operations failing or cluster workloads being disrupted, we recommend against attempting to create large clusters with many nodes in a single operation.

#### Create hybrid or standalone clusters without worker nodes

If you are creating a large hybrid or standalone cluster with more than 50 worker nodes, it's better to create a high-availability (HA) cluster with control plane nodes first and then gradually scale up. The cluster creation operation uses a bootstrap cluster, which isn't HA and therefore is less reliable. Once the HA hybrid or standalone cluster has been created, you can use it to scale up to more nodes.

#### Increase the number of worker nodes in batches

If you are expanding a cluster to more worker nodes, it's better to expand in stages. We recommend that you add no more than 20 nodes at a time. This is especially true for clusters that are running critical workloads.

### Enable parallel image pulls

By default, kubelet pulls images serially, one after the other. If you have a bad upstream connection to your image registry server, a bad image pull can stall the entire queue for a given node pool.

To mitigate this, we recommend that you set `serializeImagePulls` to `false` in custom kubelet configuration. For instructions and more information, see [Configure kubelet image pull settings](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/update-clusters#kubelet-config). Enabling parallel image pulls can introduce spikes in the consumption of network bandwidth or disk I/O.

### Fine tune application resource requests and limits

In densely packed environments, application workloads might get evicted. Kubernetes uses the referenced mechanism to rank pods in case of eviction.

A good practice for setting your container resources is to use the same amount of memory for requests and limits, and a larger or unbounded CPU limit. For more information, see [Prepare cloud-based Kubernetes applications](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke#prepare_cloud-based_kubernetes_applications) in the Cloud Architecture Center.

### Use a storage partner

We recommend that you use one of the [GDC Ready storage partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage) for large scale deployments. It's important to confirm the following information with the particular storage partner:

  * The storage deployments follow best practices for storage aspects, such as high availability, priority setting, node affinities, and resource requests and limits.
  * The storage version is qualified with the particular Google Distributed Cloud version.
  * The storage vendor can support the high scale that you want to deploy.



### Configure clusters for high availability

It's important to audit your high-scale deployment and make sure the critical components are configured for HA wherever possible. Google Distributed Cloud supports HA deployment options for all cluster types. For more information, see [Choose a deployment model](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-prep). For example cluster configuration files of HA deployments, see [Cluster configuration samples](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/config-samples).

It's also important to audit other components including:

  * Storage vendor
  * Cluster webhooks



### Monitoring resource use

This section provides some basic monitoring recommendations for large scale clusters.

#### Monitor utilization metrics closely

It's critical to monitor the utilization of both nodes and individual system components and make sure they have a comfortably safe margin. To see what standard monitoring capabilities are available by default, see [Use predefined dashboards](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/predefined-dashboards).

#### Monitor bandwidth consumption

Monitor bandwidth consumption closely to ensure the network isn't being saturated, which results in performance degradation for your cluster.

### Improve etcd performance

Disk speed is critical to etcd performance and stability. A slow disk increases etcd request latency, which can lead to cluster stability problems. To improve cluster performance, Google Distributed Cloud stores Event objects in a separate, dedicated etcd instance. The standard etcd instance uses `/var/lib/etcd` as its data directory and port 2379 for client requests. The etcd-events instance uses `/var/lib/etcd-events` as its data directory and port 2382 for client requests.

We recommend that you use a solid-state disk (SSD) for your etcd stores. For optimal performance, mount separate disks to `/var/lib/etcd` and `/var/lib/etcd-events`. Using dedicated disks ensures that the two etcd instances don't share disk I/O.

**Note:** When you upgrade a cluster from a version that doesn't have a separate etcd instance for Events, all Event objects are lost. However, since Event objects have a time to live (TTL) of one hour and upgrades often take longer than an hour, the loss shouldn't be noticeable. Also, the loss of Event objects has no impact on cluster operation. Events should be treated as informative, best-effort, supplemental data only.

The etcd documentation provides additional [hardware recommendations](https://etcd.io/docs/v3.4/op-guide/hardware/) for ensuring the best etcd performance when running your clusters in production.

To check your etcd and disk performance, use the following etcd I/O latency metrics in the Metrics Explorer:

  * `etcd_disk_backend_commit_duration_seconds`: the duration should be less than 25 milliseconds for the 99th percentile (p99).
  * `etcd_disk_wal_fsync_duration_seconds`: the duration should be less than 10 milliseconds for the 99th percentile (p99).



For more information about etcd performance, see [What does the etcd warning "apply entries took too long" mean?](https://etcd.io/docs/v3.3/faq/#what-does-the-etcd-warning-apply-entries-took-too-long-mean) and [What does the etcd warning "failed to send out heartbeat on time" mean?](https://etcd.io/docs/v3.3/faq/#what-does-the-etcd-warning-failed-to-send-out-heartbeat-on-time-mean).

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



## What's next?

  * [Installation prerequisites overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-prereq)

  * [Choose a deployment model](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-prep)

  * [Quotas and limits](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/limits)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
