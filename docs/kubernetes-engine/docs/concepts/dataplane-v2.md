---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2/
title: GKE Dataplane V2 \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:47.678268+00:00
---

# GKE Dataplane V2  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  GKE Dataplane V2 Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page provides an overview of what GKE Dataplane V2 does and how it works.

This page assumes that you know about [networking inside GKE clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview#inside-cluster).

## Overview of GKE Dataplane V2

GKE Dataplane V2 is a dataplane that is optimized for Kubernetes networking. GKE Dataplane V2 provides the following:

  * A consistent user experience for networking.
  * Real-time visibility of network activity.
  * Simpler architecture that makes it easier to manage and troubleshoot clusters.



GKE Dataplane V2 is enabled by default for all new Autopilot clusters.

## How GKE Dataplane V2 works

GKE Dataplane V2 is implemented using [eBPF](https://ebpf.io/what-is-ebpf/). As packets arrive at a GKE node, eBPF programs installed in the kernel decide how to route and process the packets. Unlike packet processing with [`iptables`](https://en.wikipedia.org/wiki/Iptables), eBPF programs can use Kubernetes-specific metadata in the packet. This lets GKE Dataplane V2 process network packets in the kernel more efficiently and report annotated actions back to user space for logging.

The following diagram shows the path of a packet through a node using GKE Dataplane V2:

![The path of a packet through a node using GKE Dataplane V2.](https://docs.cloud.google.com/static/kubernetes-engine/images/dataplanev2.svg)

GKE deploys the GKE Dataplane V2 controller as a [DaemonSet](https://kubernetes.io/docs/concepts/workloads/controllers/daemonset/) named `anetd` to each node in the cluster. `anetd` interprets Kubernetes objects and programs network topologies in eBPF. The `anetd` Pods run in the `kube-system` namespace.

### GKE Dataplane V2 and NetworkPolicy

GKE Dataplane V2 is implemented using [Cilium](https://cilium.io/). The legacy dataplane for GKE is implemented using [Calico](https://www.tigera.io/project-calico/).

Both of these technologies manage Kubernetes [NetworkPolicy](https://kubernetes.io/docs/concepts/services-networking/network-policies/). Cilium uses eBPF and the Calico Container Network Interface (CNI) uses `iptables` in the Linux kernel.

### Custom eBPF programs

GKE Dataplane V2 uses eBPF programs to manage network traffic, including routing, load balancing, and network policy enforcement. Because these programs are essential for network connectivity, GKE doesn't support installing custom eBPF programs on nodes that use GKE Dataplane V2. Custom eBPF programs can interfere with GKE Dataplane V2 programs and might disrupt cluster networking.

If a custom eBPF program is detected in your cluster, GKE provides a [Recommendation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders) that informs you about the presence of the program.

## Advantages of GKE Dataplane V2

GKE Dataplane V2 offers the following benefits:

### Scalability

GKE Dataplane V2 has different scalability characteristics than legacy data plane.

For GKE versions where the GKE Dataplane V2 [does not use kube-proxy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2#kube-proxy) and does not rely on `iptables` for service routing, GKE removes some `iptables` related bottlenecks, such as the number of Services.

GKE Dataplane V2 relies on eBPF maps that are limited to 260,000 endpoints across all services.

### Security

Kubernetes NetworkPolicy is always on in clusters with GKE Dataplane V2. You don't have to install and manage third-party software add-ons such as Calico to enforce network policy.

### Operations

When you create a cluster with GKE Dataplane V2, network policy logging is built-in. Configure the [logging CRD](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging) on your cluster to see when connections are allowed and denied by your Pods.

### Consistency

GKE Dataplane V2 provides a consistent networking experience.

For more information, see [Availability of GKE Dataplane V2](https://docs.cloud.google.com/anthos/clusters/docs/dataplane-v2).

## GKE Dataplane V2 technical specifications

GKE Dataplane V2 supports clusters with the following specifications:

Specification | GKE | Google Distributed Cloud Edge | Google Distributed Cloud Hosted  
---|---|---|---  
Number of nodes per cluster | 15,000 | 500 | 500  
Number of Pods per cluster | 400,000 | 15,000 | 27,500  
Number of Pods behind one Service | 10,000 | 1,000 | 1,000  
Number of Cluster IP Services | 10,000 | 1,000 | 1,000  
Number of [LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service#services_of_type_loadbalancer) per cluster | 750 | 500 | 1,000  
  
GKE Dataplane V2 maintains a Service map to keep track of which Services refer to which Pods as their backends. The number of Pod backends for each Service summed across all Services must all fit into the Service map, which can contain up to 260,000 entries. If this limit is exceeded your cluster may not work as intended.

### Node limits

The maximum number of nodes per cluster depends on your GKE Dataplane V2 cluster's location:

  * **Regional clusters** : Up to 5,000, 15,000, or 65,000 nodes per cluster. Not all node increases are automatic. Depending on your target node count, there are specific infrastructure requirements, and you might need to contact Cloud Customer Care. Scaling to 65,000 nodes requires the Dataplane V2 scale-optimized mode, which disables network policy enforcement. For detailed information, see [Cluster size limits and requirements](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/planning-large-clusters#clusters-5k-nodes).
  * **Zonal clusters** : Up to 1,000 nodes.



To achieve node scaling limits beyond 5,000 nodes in regional clusters, your environment must meet the following conditions:

  * Your cluster must have Private Service Connect enabled. To check if your cluster uses Private Service Connect, see [Clusters with Private Service Connect](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/private-service-connect#clusters-private-service-connect).
  * Clusters using the [CiliumNetworkPolicy CRD](https://cilium.io/) are restricted to zonal cluster limits of up to 1,000 nodes. Use the CiliumClusterwideNetworkPolicy CRD instead to support scaling up to 5,000 nodes.



### LoadBalancer Services in Google Distributed Cloud

The number of LoadBalancer Services supported in Google Distributed Cloud depends on the [load balancer mode](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/setup-load-balance) being used. Google Distributed Cloud supports 500 LoadBalancer Services when using bundled load balancing mode (Seesaw) and 250 when using integrated load balancing mode with F5. For more information, see [Scalability](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.7/concepts/scalability#load_balancer).

### Maglev support

For GKE clusters running version 1.36.0-gke.2882000 and later, you can configure Services to use the [Maglev consistent hashing algorithm](https://research.google/pubs/pub44824/) for backend selection.

By default, Kubernetes Services use the `random` algorithm to select backends. The `random` algorithm can cause healthy connections to be rerouted and reset when the set of backend Pods changes (for example, during scaling events). Maglev mitigates this by continuing to route traffic to a connection's assigned backend as long as it remains healthy, even when other Pods are added or removed.

#### Benefits of using the Maglev algorithm

Using the Maglev algorithm offers the following benefits:

  * It can improve connection stability by directing traffic for a connection to the same backend.
  * It can mitigate connection issues when backend Pods are added or removed—for example, during Pod restarts.



#### Limitations of using the Maglev algorithm

Using the Maglev algorithm might be resource intensive:

  * It might cause increased memory usage on `anetd` in every cluster. For more information, see the next section, "Maglev memory usage considerations."
  * It might be connected to higher `anetd` CPU usage (up to three times more) during backend changes.



#### Maglev memory usage considerations

To track connections and backends, the Maglev algorithm uses a hash table: it hashes the packet's 5-tuple (source IP address, destination IP address, source port, destination port, and protocol).

The size of the look-up table is configured to 16,381 entries. Because each entry has a size of 4 bytes, a Service configured to use the Maglev algorithm requires 65.5 KB (16,381 × 4 bytes) of each node's allocatable memory.

Number of services with Maglev enabled | Additional memory usage  
---|---  
100 | 6.5 MB  
1,000 | 65 MB  
10,000 | 650 MB  
  
#### Applying the Maglev algorithm

To apply the Maglev algorithm to a Service of type `NodePort` or `LoadBalancer`, add the `gke.networking.io/lb-algorithm: "maglev"` annotation to the Service's metadata during Service creation.

Example:
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: maglev-service
      annotations:
        gke.networking.io/lb-algorithm: "maglev"
    spec:
      type: LoadBalancer
      selector:
        app: application
      ports:
      - protocol: TCP
        port: 80
        targetPort: 8080
    

The `gke.networking.io/lb-algorithm` annotation takes effect during Service creation. To change the algorithm of an existing Service, you must delete and re-create the Service. Changing the annotation value without re-creation causes inconsistent behavior. `anetd` on new nodes attempts to use the newly configured algorithm, while existing Pods continue using the previous algorithm.

### Deploy workloads with SCTP

You can deploy workloads that use the Stream Control Transmission Protocol (SCTP) on clusters that are enabled with GKE Dataplane V2. SCTP is a transport layer protocol that provides reliable, message-oriented transmission. For more information, see [Deploy workloads with SCTP](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-workloads-with-sctp).

## Limitations

GKE Dataplane V2 has the following limitations:

  * GKE Dataplane V2 can only be enabled when creating a new cluster. Existing clusters cannot be upgraded to use GKE Dataplane V2.
  * Manually created internal passthrough Network Load Balancers associated with a Service of type NodePort are not supported.
  * GKE Dataplane V2 uses `cilium` instead of `kube-proxy` to implement Kubernetes Services. `kube-proxy` is maintained and developed by the Kubernetes community, so new features for Services are more likely to be implemented in `kube-proxy` before they are implemented in `cilium` for GKE Dataplane V2.
  * In certain cases, GKE Dataplane V2 agent Pods (`anetd`) can consume a significant amount of CPU resources, up to two or three vCPUs per instance. This occurs when there's a high volume of TCP connections being opened and closed rapidly on the node. To mitigate this problem, we recommend implementing keep-alives for HTTP calls and connection pooling for the relevant workloads.
  * The _reported_ memory usage of GKE Dataplane V2 agent Pods (`anetd`) depends on the total memory available on the node. Nodes that have higher total memory report higher memory usage for the `anetd` Pods. The `anetd` Pods don't actually use more memory; the reported usage increases because this metric includes the memory reservation of the [eBPF map](https://docs.cilium.io/en/stable/network/ebpf/maps/).

In GKE, the memory reservation for the largest eBPF maps is 0.25% of the total node memory. Additional memory might be reserved for other GKE-specific features.

  * GKE Dataplane V2 uses eBPF to manage your cluster's network traffic. If you install a third-party application that also uses eBPF, it might interfere with GKE Dataplane V2. For example, using Retina with GKE Dataplane V2 can prevent your Pods from connecting to Services. This happens because Retina's eBPF programs can disrupt how GKE Dataplane V2 routes traffic. If you see error messages indicating that traffic is being dropped because it's trying to reach the Service's IP address directly, you might be encountering this issue. This is because Pods aren't allowed to directly access the Service's IP address and traffic must go through Dataplane V2's routing mechanisms. For more information, see [Retina incompatibility issues](https://github.com/microsoft/retina/issues/252).

  * Fragmented ICMP packets are not supported and are dropped by GKE Dataplane V2.




## Network policy enforcement without GKE Dataplane V2

See [Using network policy enforcement](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy#enabling_network_policy_enforcement) for instructions to enable network policy enforcement in clusters that don't use GKE Dataplane V2.

## What's next

  * Read [Using GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/dataplane-v2).
  * Learn about [GKE Dataplane V2 observability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-dpv2-observability).
  * Learn how to [Use network policy logging](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy-logging).
  * See which [GKE Enterprise cluster environments GKE Dataplane V2 is available on](https://docs.cloud.google.com/anthos/clusters/docs/dataplane-v2).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
