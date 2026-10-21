---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/limits/
title: Quotas and limits \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:47:02.128075+00:00
---

# Quotas and limits  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/limits/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/limits)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/limits)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



This page explains Google Distributed Cloud release 1.16 quotas and limits for Google Cloud projects, clusters, and nodes.

## Limits

The following sections outline some basic limits for your clusters. Take these limits into account when designing your applications to run on Google Distributed Cloud.

### Maximum user clusters per admin cluster

Admin clusters manage the lifecycle for user clusters and their associated nodes. Admin clusters control critical user cluster operations, such as cluster creation, cluster or node resets, cluster upgrades, and cluster updates. The total number of user cluster nodes is one of the primary factors limiting performance and reliability.

Based on ongoing testing, an admin cluster can reliably support a maximum of 100 user clusters having 10 nodes each for a total of 1,000 nodes.

### Maximum number of pods per user cluster

We recommend that you limit the number of pods per user cluster to 15,000 or fewer. For example, if your cluster has 200 nodes, you should restrict the number of pods per node to 75 or fewer. Likewise, if you want to run 110 pods per node, you should restrict the number of nodes in your cluster to 136 or fewer. The following table provides examples of configurations that are and aren't recommended.

Pods per node | Nodes per cluster | Pods per Cluster | Result  
---|---|---|---  
110 | 200 | 22,000 | Too many pods, not recommended  
110 | 136 | 14,960 | Within limit  
100 | 150 | 15,000 | Within limit  
75 | 200 | 15,000 | Within limit  
  
The maximum number of pods per user cluster recommendation takes precedence over the recommendations for pods per node and nodes per user cluster in the following sections.

### Maximum number of nodes per user cluster

We test Google Distributed Cloud to run workloads with up to 500 nodes. However, to ensure optimal performance and reliability, we recommend that you don't exceed 200 nodes per cluster when running workloads in production.

Cluster type | Minimum nodes | Recommended maximum nodes | Absolute maximum nodes  
---|---|---|---  
User, Standalone, or Hybrid | 1 | 200 | 500  
  
For single-node clusters, you must remove the `node-role.kubernetes.io/master:NoSchedule` taint to run workloads on the node. For details, see [Kubernetes taints and tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).

### Maximum number of pods per node

Google Distributed Cloud supports the configuration of maximum pods per node in the `nodeConfig.PodDensity.MaxPodsPerNode` setting of the [cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/reference/cluster-config#cluster_configuration_file). The following table shows the minimum and maximum values supported for `MaxPodsPerNode`, which includes pods running add-on services:

Cluster type | Minimum allowed value | Recommended maximum value | Maximum allowed value  
---|---|---|---  
All HA clusters and non-HA user clusters | 32 | 110 | 250  
All other non-HA clusters | 64 | 110 | 250  
  
### Maximum number of endpoints

On RHEL and CentOS, there's a cluster-level limitation of 100,000 endpoints. This number is the sum of all pods that are referenced by a Kubernetes service. If two services reference the same set of pods, this situation counts as two separate sets of endpoints. The underlying `nftable` implementation on RHEL and CentOS causes this limitation; it's not an intrinsic limitation of Google Distributed Cloud.

**Mitigation**

For RHEL and CentOS, there are no mitigations. For Ubuntu and Debian systems, we recommend [switching from the default `nftables` to legacy `iptables`](https://wiki.debian.org/nftables#Reverting_to_legacy_xtables) on large-scale clusters.

### Dataplane V2 eBPF limit

The maximum number of entries in the BPF lbmap for Dataplane V2 is 65,536. Increases in the following areas can cause the total number of entries to grow:

  * Number of services
  * Number of ports per service
  * Number of backends per service



We recommend that you monitor the actual number of entries used by your cluster to ensure that you don't exceed the limit. Use the following command to get the current entries:
    
    
    kubectl get po -n kube-system -l k8s-app=cilium | cut -d " " -f1 | grep anetd | head -n1 | \
        xargs -I % kubectl -n kube-system exec % -- cilium bpf lb list | wc -l
    

We also recommend that you use your own monitoring pipeline to collect metrics from the `anetd` DaemonSet. Monitor for the following conditions to identify when the number of entries are causing problems:
    
    
    cilium_bpf_map_ops_total{map_name="lb4_services_v2",operation="update",outcome="fail" } > 0
    
    
    
    cilium_bpf_map_ops_total{map_name="lb4_backends_v2",operation="update",outcome="fail" } > 0
    

### LoadBalancer and NodePort Services port limit

The port limit for `LoadBalancer` and `NodePort` Services is 2,768. The default port range is 30000-32767. If you exceed the limit, you can't create new `LoadBalancer` or `NodePort` Services and you can't add new node ports for existing services.

By default, Kubernetes allocates node ports to Services of type `LoadBalancer`. These allocations can quickly exhaust available node ports from the 2,768 allotted to your cluster. To save node ports, disable load balancer node port allocation by setting the `allocateLoadBalancerNodePorts` field to `false` in the [LoadBalancer Service spec](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/how-to/deploy-app#lb_ports). This setting prevents Kubernetes from allocating node ports to `LoadBalancer` Services. For more information, see [Disabling load balancer NodePort allocation](https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-nodeport-allocation) in the Kubernetes documentation.

Use the following command to check the number of ports allocated:
    
    
    kubectl get svc -A | grep : | tr -s ' ' | cut -d ' '  -f6 | tr ',' '\n' | wc -l
    

### Bundled load balancer node connection limits

The number of connections allowed for each node used for bundled load balancing (MetalLB) is 28,000. The default ephemeral port range for these connections is 32768-60999. If you exceed the connection limit, requests to the LoadBalancer Service might fail.

If you need to expose a load balancer service that is capable of handling a substantial number of connections (for Ingress, for example), we recommend that you consider an alternate load balancing method to avoid this limitation with MetalLB.

## Cluster quotas

You can register a maximum of 15 clusters by default. To register more clusters in GKE Hub, you can submit a request to increase your quota in the Google Cloud console:

[Go to Quotas](https://console.cloud.google.com/apis/api/gkehub.googleapis.com/quotas)

**Note:** Each user cluster must have a unique name across _all_ admin clusters that are within a single Google Cloud project.

## Scaling issues

This section describes some issues to keep in mind when scaling your clusters.

### Resources reserved for system daemons

Starting from version 1.14, Google Distributed Cloud automatically reserves resources on a node for system daemons such as `sshd` or `udev`. CPU and memory resources are reserved on a node for system daemons so that these daemons have the resources they require. Without this feature, which is enabled by default, Pods can potentially consume most of the resources on a node, making it impossible for system daemons to complete their tasks.

Specifically, Google Distributed Cloud reserves 50 millicores of CPU (50 mCPU) and 280 Mebibytes (280 MiB) of memory on each node for system daemons. Note that the CPU unit 'mCPU' stands for "thousandth of a core", and so 50/1000 or 5% of a core on each node is reserved for system daemons. The amount of reserved resources is small and doesn't have a significant impact on Pod performance. However, the kubelet on a node may evict Pods if their use of CPU or memory exceeds the amounts that have been allocated to them.

### etcd performance

Disk speed is critical to etcd performance and stability. A slow disk increases etcd request latency, which can lead to cluster stability problems. To improve cluster performance, Google Distributed Cloud stores Event objects in a separate, dedicated etcd instance. The standard etcd instance uses `/var/lib/etcd` as its data directory and port 2379 for client requests. The etcd-events instance uses `/var/lib/etcd-events` as its data directory and port 2382 for client requests.

We recommend that you use a solid-state disk (SSD) for your etcd stores. For optimal performance, mount separate disks to `/var/lib/etcd` and `/var/lib/etcd-events`. Using dedicated disks ensures that the two etcd instances don't share disk IO.

**Note:** When you upgrade a cluster from a version that doesn't have a separate etcd instance for Events, all Event objects are lost. However, since Event objects have a time to live (TTL) of one hour and upgrades often take longer than an hour, the loss shouldn't be noticeable. Also, the loss of Event objects has no impact on cluster operation. Events should be treated as informative, best-effort, supplemental data only.

The etcd documentation provides additional [hardware recommendations](https://etcd.io/docs/v3.4/op-guide/hardware/) for ensuring the best etcd performance when running your clusters in production.

To check your etcd and disk performance, use the following etcd I/O latency metrics in the Metrics Explorer:

  * `etcd_disk_backend_commit_duration_seconds`: the duration should be less than 25 milliseconds for the 99th percentile (p99).
  * `etcd_disk_wal_fsync_duration_seconds`: the duration should be less than 10 milliseconds for the 99th percentile (p99).



For more information about etcd performance, see [What does the etcd warning "apply entries took too long" mean?](https://etcd.io/docs/v3.3/faq/#what-does-the-etcd-warning-apply-entries-took-too-long-mean) and [What does the etcd warning "failed to send out heartbeat on time" mean?](https://etcd.io/docs/v3.3/faq/#what-does-the-etcd-warning-failed-to-send-out-heartbeat-on-time-mean).

Didn't find what you were looking for? Click **Send feedback** and tell us what's missing.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
