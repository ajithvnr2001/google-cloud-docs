---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/limits/
title: Quotas and limits \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:23.110970+00:00
---

# Quotas and limits  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Quotas and limits Stay organized with collections  Save and categorize content based on your preferences. 

This page explains Distributed Cloud software only for bare metal quotas and limits for Google Cloud projects, clusters, and nodes.

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

Google Distributed Cloud supports the configuration of maximum pods per node in the `nodeConfig.PodDensity.MaxPodsPerNode` setting of the [cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config#cluster_configuration_file). The following table shows the minimum and maximum values supported for `MaxPodsPerNode`, which includes pods running add-on services:

Cluster type | Minimum allowed value | Recommended maximum value | Maximum allowed value  
---|---|---|---  
All HA clusters and non-HA user clusters | 32 | 110 | 250  
All other non-HA clusters | 64 | 110 | 250  
  
### Maximum number of endpoints

On Red Hat Enterprise Linux (RHEL), there's a cluster-level limitation of 100,000 endpoints. This number is the sum of all pods that are referenced by a Kubernetes service. If two services reference the same set of pods, this situation counts as two separate sets of endpoints. The underlying `nftable` implementation on RHEL causes this limitation; it's not an intrinsic limitation of Google Distributed Cloud.

**Mitigation**

For RHEL, there are no mitigations. For Ubuntu and Debian systems, we recommend [switching from the default `nftables` to legacy `iptables`](https://wiki.debian.org/nftables#Reverting_to_legacy_xtables) on large-scale clusters.

### Dataplane V2

Google Distributed Cloud uses [Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2), a cluster dataplane implemented with [Cilium](https://cilium.io/) and [eBPF](https://ebpf.io/what-is-ebpf/), which is optimized for Kubernetes networking.

#### Dataplane V2 `NetworkPolicy` limits

Dataplane V2 uses Cilium to manage Kubernetes `NetworkPolicy` resources. The following limits apply to your clusters:

Dimension | Supported limits  
---|---  
Maximum change rate for namespace labels | At most, one change per hour for each namespace. In most cases, this limit isn't necessary. As long as changes aren't frequent, such as every second, or the number of _Cilium identities_ (unique label sets) isn't close to the limit: 16,000 label sets with _allow all_ network policies, or 65,535 label sets per cluster.  
Maximum number of Service endpoints per cluster | 100,000 endpoints is the tested and recommended limit. The hardcoded limit for Service endpoints is 262,000.  
Maximum number of network policies and rules | At most, 40,000 network policies and 80,000 rules. For example, you can specify 40,000 network policies with two rules each, or you can specify 20,000 policies with four rules each.  
Maximum change rate for network policies | At most, 20 changes (creations or deletions) per second.  
Maximum number of unique pod label sets | 65,535 (216-1). This is the [Cilium security identity](https://docs.cilium.io/en/stable/internals/security-identities/) limit.  
Maximum number of unique pod label sets selected by policy selectors | 16,000 (the fixed eBPF map size). A given policy selector map entry consists of the following: security-identity, port, and protocol.  
  
#### Dataplane V2 eBPF limit

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

The port limit for `LoadBalancer` and `NodePort` Services is 2,768. The default port range is `30000`-`32767`. If you exceed the limit, you can't create new `LoadBalancer` or `NodePort` Services and you can't add new node ports for existing services.

By default, Kubernetes allocates node ports to Services of type `LoadBalancer`. These allocations can quickly exhaust available node ports from the 2,768 allotted to your cluster. To save node ports, disable load balancer node port allocation by setting the `allocateLoadBalancerNodePorts` field to `false` in the [LoadBalancer Service spec](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/deploy-app#lb_ports). This setting prevents Kubernetes from allocating node ports to `LoadBalancer` Services. For more information, see [Disabling load balancer NodePort allocation](https://kubernetes.io/docs/concepts/services-networking/service/#load-balancer-nodeport-allocation) in the Kubernetes documentation.

Use the following command to check the number of ports allocated:
    
    
    kubectl get svc -A | grep : | tr -s ' ' | cut -d ' '  -f6 | tr ',' '\n' | wc -l
    

### Bundled load balancer node connection limits

The number of connections allowed for each node used for bundled load balancing (MetalLB) is 28,000. The default ephemeral port range for these connections is 32768-60999. If you exceed the connection limit, requests to the LoadBalancer Service might fail.

If you need to expose a load balancer service that is capable of handling a substantial number of connections (for Ingress, for example), we recommend that you consider an alternate load balancing method to avoid this limitation with MetalLB.

## Cluster quotas

By default, you can register a maximum of 250 clusters with global memberships per fleet. To register more clusters in GKE Hub, you can submit a request to increase your quota in the Google Cloud console:

[Go to Quotas](https://console.cloud.google.com/apis/api/gkehub.googleapis.com/quotas)

For more information about cluster quotas based on membership settings, see [Allocation quotas](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/quotas#allocation_quotas).

**Note:** Each user cluster must have a unique name across _all_ admin clusters that are within a single Google Cloud project.

## Scaling information

The information in this document is relevant for planning how to scale up your clusters. For more information, see [Scale up Google Distributed Cloud clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/scale).

Didn't find what you were looking for? Click **Send feedback** and tell us what's missing.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
