---
url: https://docs.cloud.google.com/kubernetes-engine/docs/learn/learn-gke-net-architecture/
title: Learn GKE networking architecture \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:40:58.359666+00:00
---

# Learn GKE networking architecture  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/learn/learn-gke-net-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Learn GKE networking architecture Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Google Kubernetes Engine (GKE) networking uses and extends the software-defined networking (SDN) infrastructure provided by Virtual Private Cloud (VPC). GKE networking lets your components communicate within a Kubernetes cluster and with external services and networks. The GKE networking model builds on the Kubernetes networking principle—where every Pod gets its own IP address—to provide IP addressing, load balancing, DNS resolution, and network policy enforcement. This document explains how core components like nodes, Pods, and Services interact with the control plane within the context of GKE networking, covering the following:

  * How these components interact within your VPC
  * How IP addresses are allocated and managed
  * How traffic flows into, within, and out of the cluster



## Architecture of a GKE network

A GKE network builds on Google Cloud's Virtual Private Cloud (VPC). This foundation provides robust and scalable connectivity for all your containerized applications.

### The VPC foundation and IP address ranges

Within your VPC, you define subnets, which are regional IP address ranges. GKE strategically uses different IP address ranges within these subnets for various cluster components, often using VPC alias IP address ranges:

  * Node IP address range: this is the primary IP address range of the subnet where your cluster nodes are deployed. All your GKE worker nodes, which are Compute Engine VMs, get their main IP addresses from this range. These IP addresses are used for communication between nodes and for health checks from load balancers. The node IP address is also the source for traffic that originates on the node itself. In VPC-native clusters, traffic from Pods uses the Pod IP address as the source address, unless the Pod IP address is translated by a feature like Cloud NAT.
  * Pod IP address range: a dedicated secondary IP address range, often a larger CIDR block, that's within your subnet. Each node receives a pool of IP addresses from this range. GKE assigns these IP addresses to Pods that run on that node. Every Pod in your cluster gets its unique IP address from this range. These Pod IP addresses are natively routable within your Virtual Private Cloud. By default, each node gets a `/24` range, which provides 256 IP addresses. However, GKE limits the maximum number of Pods per node to 110. This buffer helps ensure IP address availability during rapid Pod creation and deletion, also known as churn. These IP addresses enable direct communication between Pods across different nodes without requiring Network Address Translation (NAT).
  * Service IP address range (ClusterIP): a secondary IP address range for the virtual IP addresses (ClusterIPs) assigned to Kubernetes Services. These stable IP addresses are used only for communication within the cluster.
  * Control plane IP address: each control plane has a public or internal IP address, depending on the cluster type, version, and creation date. This IP address is used by worker nodes and external clients, such as `kubectl`, to communicate securely with the Kubernetes API server. GKE Frontend (GKFE) provides a DNS-based endpoint for each cluster, offering a secure and reliable way to access the control plane without directly managing IP addresses.



## The three pillars of GKE networking

GKE networking consists of three interconnected pillars, each representing a distinct layer of communication. This framework helps you understand how your applications communicate within the cluster and with external networks:

  * **Pod networking** : the foundational layer, defining how individual containers (Pods) communicate with each other within the cluster.
  * **Service networking** : built upon Pod networking, this layer describes how Kubernetes Services provide stable endpoints to expose applications for internal or external clients, including load balancing and service discovery.
  * **Cluster networking** : the outermost layer, covering how your entire GKE cluster connects to the broader network ecosystem, including managing ingress from the internet, egress to external services, and connectivity to Google Cloud services and on-premises systems.



These layers work together to create a comprehensive communication model that supports internal and external connectivity, security, and scalability. The following sections explore each pillar in detail.

### Pod networking

Pod networking is the foundation for all communication within a GKE cluster. It defines how applications running inside Pods can find and interact with each other. In Kubernetes, a _Pod_ is the smallest and most basic deployable unit. A Pod acts as a logical host for your applications. It runs one or more containers that share network resources. When a Pod is scheduled on a node, Kubernetes creates a dedicated network namespace for it in the node's Linux kernel, which isolates its network from other Pods on the same node.

#### How Pod networking works

Pod networking is established through a combination of unique IP addresses, virtual network devices, and specialized plugins that manage connectivity.

**Container Network Interface (CNI)** : GKE uses CNI plugins to implement and manage Pod networking. For VPC-native clusters, the default is the Google CNI. Other options include `kubenet` (for non-VPC-native clusters), Calico, and GKE Dataplane V2 (which is based on Cilium). These plugins are responsible for connecting Pods to the network and enforcing network policies.

  * **IP address allocation** : each node receives a pool of IP addresses from the Pod IP address range to assign to Pods. GKE reserves a portion of these addresses to create a buffer that helps ensure IP address availability during rapid Pod churn (creation and destruction). This reservation is why the number of allocatable Pod IP addresses per node is always smaller than the size of the range.

  * **Network namespaces and virtual Ethernet (veth) pairs** : to facilitate communication, Kubernetes connects the Pod's isolated network namespace to the node's primary, or root, network namespace. Kubernetes makes this connection by using a virtual Ethernet pair, or _veth pair_ , which acts like a virtual network cable. One end of the pair is placed inside the Pod's namespace and appears as `eth0`. The other end connects to either a network bridge or directly to the node's network stack in the node's root namespace, which then allows packet flow to and from the Pod.

The specific connection method depends on the CNI plugin that your cluster uses:

    * **Google CNI** : this is the default CNI for VPC-native clusters. The Pod's veth pair connects to the node's root network namespace. Because Pod IP addresses are alias IP addresses that are known to the VPC network, standard Linux routing on the node directs traffic to and from the Pod.
    * **GKE Dataplane V2** : this uses eBPF programs to handle Pod networking and often bypasses conventional Linux bridges and veth pairs to directly manage packet flows within the kernel for higher performance.
    * **Kubenet** : this is used in non-VPC-native clusters. The other end of the veth pair connects to a Linux bridge device called `cbr0` in the node's root namespace. This bridge manages traffic between Pods on the same node and uses NAT for traffic that leaves the node.
    * **Calico** : when network policy is enabled with Calico, the other end of the veth pair connects to the node's root namespace, and Calico then programs host routes to direct traffic to the correct Pods.



**Maximum Transmission Unit (MTU)** : this determines the largest packet size that can be sent over a network without being fragmented. In GKE, the MTU for a Pod's interface is a critical setting that depends on the GKE CNI plugin that the cluster uses and the MTU settings of the underlying VPC network. A mismatch in MTU values can cause packet loss or performance degradation. The Pod interface MTU value is either a fixed 1460 bytes or it is inherited from the primary network interface of the node, as shown in the following table.

CNI | MTU | Usage  
---|---|---  
Google CNI | 1460 | Default for VPC-native clusters that use GKE versions before 1.26.1.  
Google CNI | Inherited | Default for VPC-native clusters that use GKE versions 1.26.1 and later.  
Calico | 1460 | Used when network policy is enabled (`--enable-network-policy`).  
GKE Dataplane V2 | Inherited | Used when GKE Dataplane V2 is enabled (`--enable-dataplane-v2`).  
netd | Inherited | Used when features like `Intranode` visibility, Workload Identity Federation for GKE for GKE, or IPv4/IPv6 dual-stack networking are enabled.  
On clusters that run versions before 1.26.1, enabling features such as `Intranode visibility`, Workload Identity Federation for GKE, or IPv4/IPv6 dual-stack networking causes the Pod MTU to be inherited from the node's primary interface. 

#### Pod-to-Pod communication flow

Kubernetes uses a flat networking model, where every Pod has a unique, routable IP address. This model helps ensures seamless connectivity between Pods.

**Communication within the same node**

When a Pod sends traffic to another Pod on the same node, the request flows from the first Pod's network namespace, through its veth pair, and into the node's root network namespace. This traffic remains within the node. Depending on the CNI plugin used, the CNI plugin then forwards the traffic to the second Pod's veth pair. For example, with `kubenet`, a bridge device forwards the traffic. With GKE Dataplane V2, eBPF programs manage the packet flow directly.

**Communication between different nodes**

When a Pod on one node sends traffic to a Pod on another node, the traffic flows to the root network namespace of the first node. The traffic then leaves the first node's primary network interface and enters the VPC network. Because Pod IP addresses are natively routable in a VPC-native GKE cluster, the VPC network routes the traffic directly to the second node. The second node then forwards the traffic to the destination Pod.

**Host network Pods**

For specific use cases, you can configure a Pod with the `hostNetwork: true` setting. This setting bypasses the isolated Pod network and lets the Pod share the node's network namespace directly. With this direct access, the Pod uses the node's IP address and can communicate with all other Pods without needing NAT. In clusters that use the `kubenet` CNI plugin, this behavior is different from regular Pods. Regular Pods require NAT for outbound traffic because their IP addresses are not directly routable on the VPC network. By contrast, GKE's VPC-native networking makes this translation unnecessary for all Pods. However, when configuring Pods with the `hostNetwork: true` setting, be careful to avoid port conflicts with other processes or Pods that run on the same node. In clusters that use the `kubenet` CNI, the `cbr0` virtual network bridge is created only if the node has Pods that have the `hostNetwork: false` setting.

### Service networking

Although Pod networking provides the fundamental connectivity between individual Pods, it isn't sufficient for building robust, scalable applications. Pods are ephemeral; they can be created, destroyed, and rescheduled at any time. This situation causes their IP addresses to change. Service networking solves this problem by providing a stable and reliable way to expose applications and manage how they communicate, both within the cluster and with the outside world.

A Kubernetes Service is an abstraction that defines a logical set of Pods and a policy for accessing them. Services use labels to group multiple related Pods into a single logical unit. When you create a Service, Kubernetes assigns it a stable, virtual IP address, known as a ClusterIP, from a pool of addresses reserved for Services. This ClusterIP, along with an associated DNS name, remains constant for the entire lifecycle of the Service, providing a consistent endpoint that other applications can use to connect to the Pods.

#### How Service networking works

Service networking relies on two key mechanisms to route traffic from a Service's stable endpoint to its dynamic backend Pods: service discovery and load balancing.

**Service discovery** : for applications to find and communicate with each other, GKE provides an internal DNS service (either `kube-dns` or Cloud DNS). When you create a Service, the DNS service automatically creates a corresponding DNS record. This record lets applications connect to the Service by using its DNS name (for example, `my-app-service`) instead of needing to know its ClusterIP. Although `kube-dns` is the default for Standard clusters, Cloud DNS for GKE is the recommended solution for most production environments. It is also the only supported solution for GKE Autopilot clusters. This service is fully managed, scalable, and highly available. It integrates with VPC networking and Cloud Logging, offering improved performance and observability without requiring you to manage the `kube-dns` Pods.

**Load balancing mechanisms** : the implementation of Service load balancing depends on your GKE cluster's networking mode.

  * **GKE Dataplane V2** : clusters that use GKE Dataplane V2 (which is based on Cilium) don't use `kube-proxy` for Service load balancing. Instead, GKE Dataplane V2 uses eBPF programs that run in the Linux kernel. These eBPF programs are highly efficient at intercepting traffic to Service ClusterIPs and directly load-balance traffic to the appropriate backend Pods. This approach results in better performance and is tightly integrated with GKE Dataplane V2's network policy enforcement capabilities.

  * **`kube-proxy` (for clusters without GKE Dataplane V2)**: on every node in a GKE cluster that doesn't use GKE Dataplane V2, a component called `kube-proxy` implements the virtual IP address mechanism for Services. `kube-proxy` watches the Kubernetes API server for changes to Services and Endpoints, and then programs network rules on the node to intercept traffic destined for a Service's ClusterIP.

`kube-proxy` can operate in different modes, including the following:

    * **`iptables` mode**: this is the default mode. `kube-proxy` adds and removes Destination NAT (DNAT) rules in the node's `iptables` subsystem. When traffic arrives for a Service's ClusterIP, these rules perform a NAT translation and change the destination IP address to one of the healthy backend Pods. The load balancing across backend Pods is typically random or round-robin.
    * **`ipvs` mode**: this mode uses the Linux IP Virtual Server (IPVS) for high-performance load balancing. `kube-proxy` configures IPVS rules, which can handle a large number of services and provide more sophisticated load balancing algorithms.



#### Internal communication flow example

The following list describes how a request flows from a client Pod to a server Pod using a Service in a cluster that doesn't use GKE Dataplane V2:

  1. The client application makes a DNS query for `my-server-service`.
  2. The cluster's internal DNS service resolves this name to the Service's stable ClusterIP (for example, `10.0.32.8`).
  3. The client Pod sends a request to the Service's ClusterIP.
  4. The `iptables` rules on the client's node, which are managed by `kube-proxy`, intercept this request.
  5. These `iptables` rules perform DNAT and select one of the healthy backend Pods for `my-server-service` (for example, Pod 2 with IP address `10.4.0.3`). The rules also rewrite the destination IP address of the packet to the Pod's IP address.
  6. The packet is routed through the flat Pod network to Pod 2, which processes the request.



In clusters that use GKE Dataplane V2, eBPF programs handle the interception and load balancing of traffic to the Service ClusterIP, bypassing `kube-proxy` and `iptables`.

#### Example Service manifest

The following example shows a Service manifest. The `selector` field specifies which Pods receive traffic based on their labels.
    
    
    apiVersion: v1
    kind: Service
    metadata:
      name: my-server-service
    spec:
      selector:
        app: my-server # This should match the labels on your server Pods
      ports:
      - protocol: TCP
        port: 80 # The port the Service exposes
        targetPort: 8080 # The port the containers in the Pods are listening on
    

#### Features of Service networking

GKE Service networking offers several features to manage traffic flow and expose applications, both internally and externally.

  * **Internal and external load balancing.** for Services that need to be accessed only from within the cluster, `kube-proxy` (or GKE Dataplane V2) handles the load balancing internally. For Services that need to be exposed to the internet, GKE automatically provisions a cloud load balancer to distribute external traffic to the nodes in the cluster.
  * **Application Load Balancers for HTTP(S) routing.** for HTTP(S) traffic, GKE uses a specialized Layer 7 load balancer, the Application Load Balancer. You configure this load balancer by using the Kubernetes Gateway API, which is the recommended approach for all new applications. The GKE Gateway controller is Google's implementation of the Gateway API and is designed to be a more expressive, flexible, and extensible successor to the Ingress resource. Gateway API uses the following resources to configure the load balancer: 
    * **Gateway:** defines listener configurations like ports, protocols, and hostnames. It functions as the entry point for traffic.
    * **HTTPRoute:** specifies how traffic that's received by a Gateway is routed to Services. It supports advanced features like path-based routing, header matching, and traffic splitting.
    * **Policy:** defines how the underlying Google Cloud infrastructure should function by being attached to a Gateway, Route, or Service.
  * **Service mesh integration.** for complex microservices architectures, GKE supports service mesh technologies. A service mesh is an optional infrastructure layer that provides advanced features for traffic management, observability, and security. For a fully managed and supported experience, GKE offers Cloud Service Mesh, which is built on Istio.



### Cluster networking

Cluster networking is the outermost layer of GKE networking. It focuses on how your entire Kubernetes cluster interacts with external resources and networks, including how internet clients reach your applications, how your Pods access external APIs, and how your cluster connects to on-premises data centers. Cluster networking is built upon Google Cloud's VPC infrastructure.

#### Manage inbound traffic

Ingress is traffic that enters your cluster from the outside world. GKE uses several integrated Google Cloud features to manage and secure this traffic.

**External access data flow** : when a client from the internet sends a request to your application (usually exposed through a Service of type `LoadBalancer` or an Ingress or Gateway resource), it first reaches a Google Cloud load balancer. The load balancer routes the request to a healthy node in your cluster. The node forwards the traffic to the appropriate Pod. `kube-proxy` handles this forwarding on clusters that don't use GKE Dataplane V2, or eBPF programs handle it in clusters that use GKE Dataplane V2. The destination Pod might be on the same node or a different node.

**Firewall rules** : GKE clusters use VPC firewall rules to control inbound traffic. Although GKE automatically creates some default firewall rules for essential cluster operations, such as allowing the control plane to reach the nodes, you can define custom rules to meet your specific security requirements. These VPC firewall rules work with Kubernetes Network Policies to provide defense in depth by controlling traffic at both the node and Pod levels.

**Optimizing external traffic flow** : when a load balancer sends traffic to a node, the node might need to forward that traffic to a Pod on a different node, which requires extra network hops. To avoid this situation, set the `externalTrafficPolicy` field to `Local` in your Service manifest. When this policy is active, the load balancer uses a health check to identify which nodes have healthy Pods for the target Service. The load balancer sends traffic only to the healthy Pods, which prevents the additional network hop. The trade-off is that this policy can lead to uneven traffic distribution if your backend Pods aren't evenly distributed across the nodes in your cluster.

#### Manage outbound traffic

Egress is traffic that leaves your cluster. For a GKE cluster to function and for your applications to reach external services, you must manage several connectivity paths.

**Fundamental connectivity requirements** : all GKE clusters require outbound connectivity to the `*.googleapis.com`, `*.gcr.io`, and `*.pkg.dev` domains. Outbound connectivity to the control plane's IP address must also function correctly. **Internet access for Pods by using Cloud NAT** : in private clusters where Pods don't have public IP addresses, use Cloud NAT to enable outbound internet access. Cloud NAT is a managed service that lets Pods connect to the internet for tasks like downloading updates or accessing external APIs without exposing them to incoming connections.

**Connectivity to Google Cloud Services** : if you need to allow your cluster to communicate securely with other Google Cloud services, such as Cloud Storage or Cloud SQL, without traversing the public internet, use Private Google Access. This is an important egress mechanism for private clusters that interact with Google APIs.

#### Hybrid and multi-cluster connectivity

To connect your GKE clusters to on-premises infrastructure, use Cloud VPN for encrypted tunnels or Cloud Interconnect for dedicated, high-bandwidth connections. To enable communication between multiple GKE clusters, use Multi-cluster Services, which facilitate service discovery and traffic flow across different clusters, regions, or projects.

#### Network security controls

To protect your cluster and the applications running in it, GKE provides multiple layers of security controls for both internal (east-west) and external (north-south) traffic.

#### Securing internal traffic (east-west) with network policies

By default, all Pods in a GKE cluster can communicate freely with each other. To secure internal traffic and enforce the principle of least privilege, you can use `NetworkPolicy`. A `NetworkPolicy` is a Kubernetes resource that acts as a firewall for your Pods by controlling the network traffic between them. `NetworkPolicy` resources let you define rules to restrict the ingress and egress traffic for a selected group of Pods based on a combination of labels, IP address ranges, and port numbers. When you create the first `NetworkPolicy` in a namespace, all traffic that isn't explicitly allowed by that policy is denied. The enforcement of these policies is built directly into GKE Dataplane V2, or is handled by the cluster's CNI plugin, such as Calico.

#### Example `NetworkPolicy` manifest

The following example shows a `NetworkPolicy` manifest. This policy applies to Pods with the `app: backend` label and allows ingress traffic only from Pods that have the `app: frontend` label on TCP port 6379.
    
    
    apiVersion: networking.k8s.io/v1
    kind: NetworkPolicy
    metadata:
      name: backend-policy
    spec:
      podSelector:
        matchLabels:
          app: backend
      policyTypes:
      - Ingress
      ingress:
      - from:
        - podSelector:
            matchLabels:
              app: frontend
        ports:
        - protocol: TCP
          port: 6379
    

#### Secure external access to the cluster

Controlling traffic that enters and leaves your cluster is critical to protecting your applications from external threats.

**VPC firewall rules**

GKE clusters reside within a Google Cloud VPC network and are protected by VPC firewall rules that control traffic to and from the cluster nodes. VPC firewall rules and network policies work together to provide defense-in-depth. VPC firewalls operate at the node (Layer 3 or Layer 4) level, and they control traffic to the VMs themselves. Network policies operate at the Pod (Layer 3 or Layer 4) level, and they provide more granular control over traffic between applications inside the cluster.

Creating ingress or egress firewall rules that target nodes in your cluster might have adverse effects. For example, applying egress-deny rules to nodes in your cluster could break features such as NodePort and `kubectl exec`. 

**Limit access to load balancers**

When you expose applications by using a Kubernetes Service or Ingress, you can apply additional security controls at the load balancer level. For external load balancers, consider these options:

  * If you expose a Service by using the `type: LoadBalancer` field, you can specify the `loadBalancerSourceRanges` field in your Service manifest. This field restricts access to the Service to only the IP address ranges that you define.
  * For application load balancers (Ingress), you can use more advanced security services when exposing HTTP(S) applications:

    * Google Cloud Armor: this service is a web-application firewall (WAF) that helps protect your applications from DDoS attacks and other web-based threats.
    * Identity-Aware Proxy (IAP): for fine-grained access control, you can enable IAP on your endpoints. IAP verifies a user's identity and uses it to determine whether the user should be allowed to access the application.



## Custom CNI

GKE offers natively supported CNI options, including the default Google CNI, Calico, and GKE Dataplane V2. Although other third-party custom CNIs might function in your cluster, GKE doesn't officially support them. Using a custom CNI requires you to manage its configuration and troubleshoot any potential issues.

If a custom CNI is detected in your cluster, GKE provides a [Recommendation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders) advising you to remove it to help ensure a supported configuration. For service mesh use cases, custom Istio installations are also considered unsupported; we recommend using Cloud Service Mesh instead.

## What's next

  * Learn how to [create a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips).
  * Read more about [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2).
  * [Implement network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) to secure Pod-to-Pod communication.
  * Explore different ways to [expose applications using Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service) and [configure Ingress with the Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
