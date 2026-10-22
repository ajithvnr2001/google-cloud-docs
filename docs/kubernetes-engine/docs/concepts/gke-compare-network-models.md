---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-compare-network-models/
title: Compare network models in GKE \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:57.909694+00:00
---

# Compare network models in GKE  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-compare-network-models/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Compare network models in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes the network model that's used by Google Kubernetes Engine (GKE) and how it can differ from network models in other [Kubernetes](https://kubernetes.io) environments. This document covers the following concepts:

  * The most common network models that are used by various Kubernetes implementations.
  * The IP addressing mechanisms of the most common network models.
  * The advantages and disadvantages that each network model brings.
  * A detailed description of the default network model that GKE uses.



The document is for cloud architects, operations engineers, and network engineers who might be familiar with other Kubernetes implementations and are planning to use GKE. This document assumes that you are familiar with [Kubernetes](https://kubernetes.io/docs/home/) and its basic [networking model](https://kubernetes.io/docs/concepts/cluster-administration/networking/). You should also be familiar with networking concepts such as IP addressing, [network address translation (NAT)](https://wikipedia.org/wiki/Network_address_translation), firewalls, and proxies.

This document doesn't cover how to modify the default GKE networking model to meet various IP address constraints. If you have a shortage of IP addresses when migrating to GKE, see [IP address management strategies when migrating to GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-ip-address-mgmt-strategies).

**Note:** This document describes implementations of the Kubernetes networking model in other cloud environments, such as Amazon Web Services, Microsoft Azure, and Oracle® Cloud Infrastructure. Those implementations might change without notice. For up-to-date implementation information, see the documentation that is provided by those vendors.

## Typical network model implementations

You can implement the Kubernetes networking model in various ways. However, any implementation always needs to fulfill the following requirements:

  * Every Pod needs a unique IP address.
  * Pods can communicate with other Pods on all nodes without using NAT.
  * Agents on a node, such as the `kubelet`, can communicate with all Pods on that node.
  * Pods on the host network of a node can communicate with all Pods on all nodes without using NAT.



There have been [more than 20 different implementations for the Kubernetes network model](https://kubernetes.io/docs/concepts/cluster-administration/networking/#how-to-implement-the-kubernetes-networking-model) developed that meet these requirements.

These implementation can be grouped into three types of network models. These three models differ in the following ways:

  * How Pods can communicate with non-Kubernetes services on the corporate network.
  * How Pods can communicate to other Kubernetes clusters in the same organization.
  * Whether NAT is required for communication outside the cluster.
  * Whether Pod IP addresses can be reused in other clusters or elsewhere in the enterprise network.



Each cloud provider has implemented one or more of these model types.

The following table identifies the three types of models that are commonly used, and in which Kubernetes implementation they are used:

Network model name | Used in these implementations  
---|---  
Fully integrated or flat | 

  * GKE
  * [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/)
  * [Azure Kubernetes Service (AKS)](https://azure.microsoft.com/en-us/services/kubernetes-service/) when using [Azure CNI (advanced) networking](https://docs.microsoft.com/en-us/azure/aks/concepts-network#azure-cni-advanced-networking)

  
Island-mode or bridged | 

  * [Azure Kubernetes Service (AKS)](https://docs.microsoft.com/en-us/azure/aks/) when using [Kubenet (basic) networking](https://docs.microsoft.com/en-us/azure/aks/configure-kubenet) which is the default
  * [Oracle Container Engine for Kubernetes (OKE)](https://www.oracle.com/cloud-native/container-engine-kubernetes/)
  * Many on-premises Kubernetes implementations

  
Isolated or air-gapped | 

  * Not commonly used by Kubernetes implementations but can be used with any implementation when the cluster is deployed in a separate network or virtual private cloud (VPC)

  
  
When this document describes these network models, it refers to their effects on connected on-premises networks. However, you can apply the concepts described for connected on-premises networks to networks that are connected through a virtual private network (VPN) or through a private interconnect, including connections to other cloud providers. For GKE, these connections include all connectivity through [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect).

### Fully integrated network model

The fully integrated network (or flat) model offers ease of communications with applications outside Kubernetes and in other Kubernetes clusters. Major cloud service providers commonly implement this model because those providers can tightly integrate their Kubernetes implementation with their [software-defined network (SDN)](https://wikipedia.org/wiki/Software-defined_networking).

When you use the fully integrated model, the IP addresses that you use for Pods are routed within the network in which the Kubernetes cluster sits. Also, the underlying network knows on which node the Pod IP addresses are located. In many implementations, Pod IP addresses on the same node are from a specific, pre-assigned Pod IP address range. But this pre-assigned address range is not a requirement.

The following diagram shows Pod communication options in the fully integrated networking model:

![Network diagram that shows the communication patterns in the fully integrated network model.](https://docs.cloud.google.com/static/architecture/images/gke-compare-network-models-fully-integrated.svg)

The preceding diagram of a fully integrated network model shows the following communication patterns:

  * Pods within a Kubernetes cluster can communicate directly with each other.
  * Pods can communicate with other Pods in other clusters as long as those clusters are within the same network.
  * Pods don't need NAT to communicate with other applications outside the cluster, regardless of whether those applications are in the same network or interconnected networks.



The diagram also shows that Pod IP address ranges are distinct between different clusters.

#### Availability

The fully integrated network model is available in the following implementations:

  * By default, GKE implements this model. For more information on this implementation, see GKE networking model later in this document.
  * By default, Amazon EKS implements this model. In this implementation, Amazon EKS uses the Amazon VPC Container Networking interface (CNI) Plugin for Kubernetes to [assign Pod IP addresses directly from the VPC address space](https://docs.aws.amazon.com/eks/latest/userguide/pod-networking.html). The CNI plugin assigns IP addresses from either the default subnet in which the nodes are in or from a custom subnet. Pod IP addresses do not come from a dedicated Pod IP address range per node.
  * In Azure, AKS implements this model when using Azure CNI (advanced networking). This implementation is not the default configuration. In this implementation, each Pod gets an IP address from the subnet. You can also configure the maximum number of Pods per node. Thus, the number of IP addresses reserved in advance for Pods on that node is the same as the maximum number of Pods per node.



#### Advantages

Using a fully integrated network model offers the following advantages:

  * **Better telemetry data.** Pod IP addresses are visible throughout the network. This visibility makes telemetry data more useful than in other models because Pods can be identified even from telemetry data that is collected outside the cluster.
  * **Easier firewall configuration.** When setting firewall rules, differentiating node and Pod traffic is easier in the fully integrated network model than in the other models.
  * **Better compatibility.** Pods can communicate using protocols that don't support NAT.
  * **Better debugging.** If allowed by the firewall, resources outside the cluster can reach Pods directly during the debugging process.
  * **Compatibility with service meshes.** Service meshes, such as [Istio](https://istio.io/) or [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview), can easily communicate across clusters because Pods can communicate directly with each other. Some service mesh implementations only support Pod-to-Pod connectivity for multi-cluster service meshes.



#### Disadvantages

Using a fully integrated network model has the following disadvantages:

  * **IP address usage**. You can't reuse Pod IP addresses within the network, and each IP address must be unique. These requirements can lead to a large number of IP addresses that need to be reserved for Pods.
  * **SDN requirements.** A fully integrated network model requires a deep integration with the underlying network because the Kubernetes implementation needs to program the SDN directly. The programming of the SDN is transparent for the user and doesn't produce any user-facing disadvantages. However, such deeply integrated network models can't be easily implemented in self-managed, on-premises environments.



### Island-mode network model

The island-mode network model (or bridged) is commonly used for on-premises Kubernetes implementations where no deep integration with the underlying network is possible. When you use an island-mode network model, Pods in a Kubernetes cluster can communicate to resources outside of the cluster through some kind of gateway or proxy.

The following diagram shows Pod communication options in an island-mode networking model:

![Network diagram that shows the communication patterns in the island-mode network model.](https://docs.cloud.google.com/static/architecture/images/gke-compare-network-models-island-mode-1.svg)

The preceding diagram of an island-mode network model shows how Pods within a Kubernetes cluster can communicate directly with each other. The diagram also shows that Pods in a cluster need to use a gateway or proxy when communicating with either applications outside the cluster or Pods in other clusters. While communication between a cluster and an external application requires a single gateway, cluster-to-cluster communication requires two gateways. Traffic between two clusters passes through a gateway when leaving the first cluster and another gateway when entering the other cluster.

There are different ways to implement the gateways or proxies in an isolated network model. The following implementations are the two most common gateways or proxies:

  * **Using the nodes as gateways.** This implementation is commonly used when nodes in the cluster are part of the existing network and their IP addresses are natively routable within this network. In this case, the nodes themselves are the gateways that provide connectivity from inside the cluster to the larger network. Egress traffic from a Pod to outside of the cluster can be directed toward either other clusters or toward non-Kubernetes applications, for example to call an on-premises API on the corporate network. For this egress traffic, the node that contains the Pod uses [source NAT (SNAT)](https://en.wikipedia.org/wiki/Network_address_translation#SNAT) to map the Pod's IP address to the node IP address. To allow applications that are outside of the cluster to communicate with Services within the cluster, you can use the [NodePort](https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport) service type for most implementations. In some implementations, you can use the [LoadBalancer](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer) service type to expose Services. When using the LoadBalancer service type, you give those Services a virtual IP address that is load balanced between nodes and routed to a pod that is part of the Service.

The following diagram shows the implementation pattern when using nodes as gateways:

![Network diagram that shows the communication patterns in the island-mode network model that uses nodes as gateways.](https://docs.cloud.google.com/static/architecture/images/gke-compare-network-models-island-mode-2.svg)

The preceding diagram shows that the use of nodes as gateways doesn't have an impact on Pod-to-Pod communication within a cluster. Pods in a cluster still communicate with each other directly. However, the diagram also shows the following communication patterns outside of the cluster:

    * How Pods communicate to other clusters or non-Kubernetes applications by using SNAT when leaving the node.
    * How traffic from outside Services in other clusters or non-Kubernetes applications enters the cluster through a NodePort service before being forwarded to the correct Pod in the cluster.
  * **Using proxy virtual machines (VMs) with multiple network interfaces.** This implementation pattern uses proxies to access the network that contains the Kubernetes cluster. The proxies must have access to the Pod and node IP address space. In this pattern, each proxy VM has two network interfaces: one interface in the larger enterprise network and one interface in the network containing the Kubernetes cluster.

The following diagram shows the implementation pattern when using proxy VMs:

![Network diagram that shows the communication patterns in the island-mode network model that uses proxy VMs.](https://docs.cloud.google.com/static/architecture/images/gke-compare-network-models-island-mode-3.svg)

The preceding diagram shows that using proxies in island-mode doesn't have an impact on communication within a cluster. Pods in a cluster can still communicate with each other directly. However, the diagram also shows how communication from Pods to other clusters or non-Kubernetes applications passes through a proxy that has access to both the cluster's network and to the destination network. Furthermore, communication entering the cluster from outside also passes through the same kind of proxy.




#### Availability

The island-mode network model is available in the following implementations:

  * By default, Azure Kubernetes Service (AKS) uses island-mode networking when using [Kubenet (basic) networking](https://docs.microsoft.com/en-us/azure/aks/configure-kubenet). When AKS uses island-mode networking, the virtual network that contains the cluster includes only node IP addresses. Pod IP addresses are not part of the virtual network. Instead, Pods receive IP addresses from a different logical space. The island-mode model used by AKS also routes Pod-to-Pod traffic between nodes by using [user-defined routes](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-networks-udr-overview#user-defined) with [IP forwarding activated on the nodes interface](https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-network-interface#enable-or-disable-ip-forwarding). For Pod communication to resources outside of the cluster, the node uses SNAT to map the Pod IP address to the node IP address before the egress traffic exits the node.
  * In Oracle Container Engine for Kubernetes (OKE), Pod-to-Pod communication uses a [VXLAN overlay network](https://wikipedia.org/wiki/Virtual_Extensible_LAN). Also, the traffic from Pods to applications outside the cluster uses SNAT to map the Pod IP address to the node IP address.



#### Advantages

Using an island-mode network model has the following advantages:

  * **IP address usage.** Pod IP addresses in the cluster can be reused in other clusters. However, GKE's default VPC-native clusters don't support reusing Pod IP address ranges across clusters within the same VPC network. In GKE, Pod IP addresses are directly routable within your VPC network. Therefore, Pod IP addresses must be unique across all clusters and resources within that single VPC. If you require IP address reuse, deploy your GKE clusters into separate VPC networks. Regardless of the network model, Pods that need to communicate with external services in your enterprise network can't use IP addresses that those external services already use. For island-mode networking, the best practice is to reserve a Pod IP address space that is unique within your enterprise network and use this IP address space for all clusters that utilize this island-mode configuration.

  * **Easier security settings.** Because Pods aren't directly exposed to the rest of the enterprise network, you don't need to secure the Pods against ingress traffic from the rest of the enterprise network.




#### Disadvantages

Using an island-mode network model has the following disadvantages:

  * **Imprecise Telemetry.** Telemetry data collected outside of the cluster only contains the node IP address, not the Pod IP address. The lack of Pod IP addresses makes it harder to identify the source and destination of traffic.
  * **Harder to debug.** When debugging, you can't connect directly to Pods from outside of the cluster.
  * **Harder to configure firewalls.** You can only use node IP addresses when you configure your firewall. Thus, the resulting firewall settings either allow all Pods on a node and the node itself to reach outside services, or allow none of them to reach outside services.
  * **Compatibility with service meshes.** With island-mode, direct Pod-to-Pod communication across clusters in service meshes, such as [Istio](https://istio.io/) or [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview), isn't possible.

There are further restrictions with some service mesh implementations. [Cloud Service Mesh multi-cluster support](https://docs.cloud.google.com/service-mesh/docs/supported-features#multi-cluster_support) for GKE clusters on Google Cloud supports only clusters on the same network. For Istio implementations that support a [multi-network model](https://istio.io/latest/docs/ops/deployment/deployment-models/#multiple-networks), communication has to occur through [Istio Gateways](https://istio.io/latest/docs/concepts/traffic-management/#gateways), which makes multi-cluster service mesh deployments more complex.




### Isolated network model

The isolated (or air-gapped) network model is most commonly used for clusters that don't need access to the larger corporate network except through public-facing APIs. When you use an isolated network model, each Kubernetes cluster is isolated and can't use internal IP addresses to communicate with the rest of the network. The cluster sits on its own private network. If any Pod in the cluster needs to communicate with services outside of the cluster, this communication needs to use public IP addresses for both ingress and egress.

The following diagram shows Pod communication options in an isolated network model:

![Network diagram that shows the communication patterns in the isolated network model.](https://docs.cloud.google.com/static/architecture/images/gke-compare-network-models-fully-isolated.svg)

The preceding diagram of an isolated network model shows that Pods within a Kubernetes cluster can communicate directly with each other. The diagram also shows that Pods can't use internal IP addresses to communicate with Pods in other clusters. Furthermore, Pods can communicate with applications outside the cluster only when the following criteria are met:

  * There is an internet gateway that connects the cluster to the outside.
  * The outside application uses an external IP address for communications.



Finally, the diagram shows how the same IP address space for Pods and nodes can be reused between different environments.

#### Availability

The isolated network model is not commonly used by Kubernetes implementations. However, you could achieve an isolated network model in any implementation. You just need to deploy a Kubernetes cluster in a separate network or VPC without any connectivity to other services or the enterprise network. The resulting implementation would have the same advantages and disadvantages as the isolated network model.

#### Advantages

Using an isolated network mode has the following advantages:

  * **IP address usage.** You can reuse all internal IP addresses in the cluster: node IP addresses, Service IP addresses, and Pod IP addresses. Reuse of internal IP addresses is possible because each cluster has its own private network and communication to resources outside the cluster only happens through public IP addresses.
  * **Control.** The cluster administrators have full control over IP addressing in the cluster and don't have to perform any IP address management tasks. For example, administrators can allocate the full `10.0.0.0/8` address space to Pods and Services in the cluster, even if these addresses are already used in the organization.
  * **Security.** Communication outside the cluster is tightly controlled and, when allowed, uses well-defined external interfaces and NAT.



#### Disadvantages

Using an isolated network model has the following disadvantages:

  * **No private communication.** Communication using internal IP addresses isn't allowed to other clusters or other services in the network.



## GKE networking model

GKE uses a fully integrated network model where clusters are deployed in a Virtual Private Cloud (VPC) network that can also contain other applications.

[We recommend using a VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking#vpc-native-clusters) for your GKE environment. You can [create your VPC-native cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips) in either [Standard or Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview#modes). If you choose [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) mode, VPC-native mode is always on and cannot be turned off. The following paragraphs describe the GKE networking model in Standard with notes on how Autopilot differs.

### Understand IP address management in VPC-native clusters

When you use a VPC-native cluster, Pod IP addresses are [secondary IP addresses](https://docs.cloud.google.com/vpc/docs/alias-ip#subnet_primary_and_secondary_cidr_ranges) on each node. Each node is assigned a specific subnet of a Pod IP address range that you select out of your internal IP address space when you create the cluster. By default, a VPC-native cluster assigns [a `/24` subnet](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) to each node for use as Pod IP addresses. A `/24` subnet corresponds to 256 IP addresses. In Autopilot, the cluster uses a `/26` subnet that corresponds to 64 addresses, and you can't change this subnet setting.

GKE networking model doesn't allow IP addresses to be reused across the network. When you migrate to GKE, you must plan your IP address allocation to [Reduce internal IP address usage in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-ip-address-mgmt-strategies#reduce-private-ip-address-usage-in-gke).

Because Pod IP addresses are routable within the VPC network, Pods can receive traffic, by default, from the following resources:

  * From other services in the VPC network.
  * From VPC networks connected through [VPC Network Peering.](https://docs.cloud.google.com/vpc/docs/vpc-peering)
  * From connected on-premises networks through [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect).



### Manage external traffic communication with IP masquerade agent

When you communicate from Pods to services outside the cluster, the [IP masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent) governs how traffic appears to those services. The IP masquerade agent handles private and external IP addresses differently as outlined in the following bullets:

  * By default, the IP masquerade agent doesn't masquerade traffic to internal IP addresses, including [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918) IP addresses, and non-RFC 1918 IP addresses that are commonly used internally. (For more information, [see the list of default non-masquerade destinations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ip-masquerade-agent#default-non-masq-dests)). Because the internal IP addresses aren't masqueraded, the node doesn't use NAT on those addresses.
  * For external IP addresses, the IP masquerade agent does masquerade those addresses to the node IP address. Thus, those masqueraded addresses are translated to an external IP address by [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) or [to the external IP address of the virtual machine (VM) instance](https://docs.cloud.google.com/nat/docs/overview#specifications).



You can also use [privately used public IP (PUPI) addresses](https://docs.cloud.google.com/solutions/configuring-privately-used-public-ips-for-GKE) inside your VPC network or connected networks. If you use PUPI addresses, you can still benefit from the fully integrated network model and see the Pod IP address directly as a source. To achieve both of these goals, you have to [include the PUPI addresses in the `nonMasqueradeCIDRs` list](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#config-ip-masq-agent).

### Understand Pod traffic flow in a GKE network

The following diagram shows how Pods can communicate in the GKE networking model:

![Network diagram that shows the communication patterns in the GKE network model.](https://docs.cloud.google.com/static/architecture/images/gke-compare-network-models-gke-model.svg)

The preceding diagram shows how Pods in GKE environments can use internal IP addresses to communicate directly with the following resources:

  * Other Pods in the same cluster.
  * Pods in other GKE clusters in the same VPC network.
  * Other Google Cloud applications in the same VPC network.
  * On-premises applications connected through Cloud VPN.



The diagram also shows what happens when a Pod needs to use an external IP address to communicate with an application. As the traffic leaves the node, the node in which the Pod resides uses SNAT to map the Pod's IP address to the node's IP address. After the traffic leaves the node, Cloud NAT then translates the node's IP address to an external IP address.

For the benefits described previously in this document, especially for the benefit of having Pod IP addresses visible in all telemetry data, Google has chosen a fully integrated network model. In GKE, Pod IP addresses are exposed in [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs) (including Pod names in metadata), [Packet Mirroring](https://docs.cloud.google.com/vpc/docs/packet-mirroring), [Firewall Rules Logging](https://docs.cloud.google.com/vpc/docs/firewall-rules-logging), and in your own application logs for non-masqueraded destinations.

## What's next

  * Learn about [IP address management strategies when migrating to GKE](https://docs.cloud.google.com/architecture/gke-ip-address-mgmt-strategies)
  * Learn about [GKE networking best practices](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking)
  * [Compare AWS and Azure services to Google Cloud](https://docs.cloud.google.com/free/docs/aws-azure-gcp-service-comparison)
  * Read [Migrating containers to Google Cloud: Migrating Kubernetes to GKE](https://docs.cloud.google.com/architecture/migrating-containers-kubernetes-gke)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
