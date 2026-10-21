---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-ip-address-mgmt-strategies/
title: Manage IP address migration in GKE \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:25.649673+00:00
---

# Manage IP address migration in GKE  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-ip-address-mgmt-strategies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Manage IP address migration in GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes how to manage IP address usage on Google Kubernetes Engine (GKE) and how to use alternative network models in GKE when necessary. This document covers the following concepts: 

  * How to reduce the usage of Pod IP addresses in GKE so that GKE fits the IP address needs of most organizations.
  * How alternative networking models can be implemented on GKE when the [cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-compare-network-models#fully-integrated-model) doesn't meet your organization's requirements.



This document is for cloud architects, operations engineers, and network engineers who are planning to migrate Kubernetes clusters from other environments to GKE. Use the guidance in this document when your organization is finding it a challenge to assign enough internal IP addresses for your expected usage of GKE.

This document assumes that you are familiar with [Kubernetes](https://kubernetes.io/docs/home/) and its [networking model](https://kubernetes.io/docs/concepts/cluster-administration/networking/). You should also be familiar with networking concepts such as IP addressing, [network address translation (NAT)](https://wikipedia.org/wiki/Network_address_translation), firewalls, and proxies.

This document doesn't cover management strategies for the [address range that is used for Service IP addresses](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview#ip-allocation). The number of addresses required for Services is much smaller than for Pods and the options to reduce this number are limited. On GKE, the range of Service IP addresses is fixed for the lifetime of the cluster. Thus, the range of Service IP addresses needs to be sized to the largest-expected number of Services. Because Service IP addresses are not reachable outside the cluster, you can reuse those addresses in other networks.

This document also refers to different Kubernetes network models: fully integrated, island-mode, and isolated. These models differ in how Pod IP addresses can be reached throughout the network. These differences have an impact on the IP address management strategies that can be used. For more detailed information about these models and the GKE network model, see [Comparison of network models used by GKE and other Kubernetes implementations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-compare-network-models).

**Note:** When talking about different network models, this document refers to their effects on connected on-premises networks. The same concepts apply to all networks connected to the [Virtual Private Cloud (VPC)](https://docs.cloud.google.com/network-connectivity/docs/vpn) that contains your GKE cluster through [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect), including connections to other cloud providers.

## Reduce internal IP address usage in GKE

GKE uses a [fully integrated network model](https://docs.cloud.google.com/architecture/gke-compare-network-models#fully-integrated-model) where clusters are deployed in a VPC network that can also contain other applications. [The GKE model](https://docs.cloud.google.com/architecture/gke-compare-network-models#gke-networking-model) has many benefits. However, this type of model doesn't allow Pod IP addresses to be reused. This lack of reuse requires you to use Pod IP addresses that are unique throughout the entire VPC network. Therefore, you must carefully consider how many unique IP addresses that you need.

The number of unique addresses that you need influences whether you need to reduce IP address usage, as follows:

  * If you have enough address space for your IP address needs, then you don't necessarily need to take steps to reduce IP address usage. However, knowing how to reduce IP address usage is helpful in identifying the minimum number of IP addresses to use.
  * If you don't have enough address space, then you need to reduce IP address usage in order to create GKE clusters that fit the constraints of your address space.



To help you reduce IP address usage in GKE, consider the following options:

  * **Change the Pods-per-node setting.** By default, GKE [Standard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#modes) clusters reserve a [`/24` subnet](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) range for every node and allow up to 110 Pods per node. If you expect to use only 64 or fewer Pods per node, you can [adjust the maximum number of Pods per node](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/flexible-pod-cidr) and therefore reduce Pod IP address usage by half or more. [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) clusters allow for 32 Pods per node and this setting can't be changed.
  * **Use multiple Pod IP address ranges.** Using [discontiguous multi-Pod classless inter-domain routing (CIDR)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr), you can add secondary Pod IP address ranges to existing clusters. You can select which Pod IP address range that each [node pool](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools) uses. Selecting the IP address range used by each pool lets you be conservative when allocating the initial Pod IP address space while still being able to grow your cluster.
  * **Use non-RFC 1918 IP addresses.** Your enterprise network might not have enough unallocated RFC 1918 IP addresses to use for your Pod IP addresses. If you don't have enough unallocated RFC 1918 IP addresses, you can then use [non-RFC 1918 addresses](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/alias-ips#enable_reserved_ip_ranges), such as addresses in the [RFC 6598](https://tools.ietf.org/html/rfc6598) address space (`100.64.0.0/10`).

If you're already using the RFC 6598 space elsewhere in your enterprise network, you can use the [Class E/RFC 5735](https://tools.ietf.org/html/rfc5735) (`240.0.0.0/4`) address space for Pod IP addresses. However, traffic from these IP addresses gets blocked on Windows hosts and on some on-premises hardware. To avoid blocking RFC 5735 addresses, consider masquerading traffic to these external destinations as described in the section Hide Pod IP addresses from on-premises networks only. However, you lose some telemetry data that is directed toward on-premises applications when you masquerade traffic to external destinations.




If your organization has a large public IP address space, you can also use [privately used public (PUPI) addresses](https://docs.cloud.google.com/kubernetes-engine/docs/archive/configuring-privately-used-public-ips-for-GKE). When using PUPI addresses, you have to [include the PUPI addresses in the `nonMasqueradeCIDRs` list](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#config-ip-masq-agent) to have connectivity outside the cluster without using NAT.

## Choose a network model in GKE

The document on the [GKE networking model](https://docs.cloud.google.com/architecture/gke-compare-network-models#gke-networking-model) discusses how Standard clusters work in GKE, including the Pod IP addresses involved. In this document, the section Reduce internal IP address usage in GKE describes how to reduce the number of internal IP addresses needed in those clusters. Knowing both how the GKE networking model works and how to reduce internal IP addresses is foundational to any network model that you use in GKE.

However, just knowing and applying those concepts might not provide you with a network implementation that meets your needs. The following decision tree can help you decide on how to implement the GKE network model that is best for you:

![Decision tree for IP address migration strategies in GKE.](https://docs.cloud.google.com/static/architecture/images/gke-ip-address-mgmt-strategies-decision-tree.svg)

The decision tree always starts with the creation of GKE Standard clusters that are based on a fully integrated network model. The next step in the tree is to reduce IP address usage by applying all the options described in this document.

If you have reduced IP address usage as much as possible and still don't have enough address space for your GKE clusters, you need an alternative network model. The decision tree helps you decide on which of the following alternative network models to use:

  * Hide Pod IP addresses from on-premises networks only. Use this model when you have the following criteria: 
    * You can't use the RFC 6598 space to reduce internal IP address usage.
    * You can use the Class E/RFC 5735 address space and hide this space from on-premises networks.
  * Hide Pod IP addresses by using Private Service Connect. Use this model when you have the following criteria: 
    * You can't use the Class E/RFC 5735 address space.
    * Your clusters don't need private communication to services on the larger network.
    * You don't need to reach your clusters from any regions that are outside the cluster's region.
  * Hide Pod IP addresses through the internal use of public IP addresses and VPC Network Peering. Though rarely required, use this model when you have the following criteria: 
    * You can't use the Class E/RFC 5735 address space.
    * Your clusters do need private communication to services on the larger network.
    * Your organization has been assigned a public IP address space that is unused and large enough for your largest cluster.
  * Hide Pod IP addresses by using Cloud VPN. Use this model when your clusters don't meet any of the other criteria outlined in the decision tree.



Remember that this decision tree should only be used as guidance. According to your specific use case, you might still prefer another model based on the advantages and disadvantages of each model. Often, multiple models are workable and you can choose which approach fits better to your organization.

There are rare cases where the alternative models presented in the decision tree don't meet your needs. For these rare cases, you might be able to use the model described in Using multi-NIC instances to hide cluster addresses.

## Emulate alternative network models

To take advantage of the benefits of the fully integrated network model, we recommend that you keep your GKE clusters in the same logical network as your other cloud resources. However, you might not be able to follow this recommendation. You might not have enough IP address space, or you might be required to hide Pod IP addresses from your organization's larger network.

This section provides options to using the fully integrated network model by describing different architecture patterns that mimic various alternative network models on GKE. These alternative architecture patterns create an operation mode for GKE that is similar to the island-mode network model or the isolated-mode network model.

Each alternative architecture pattern includes the following information:

  * A description of the architecture pattern.
  * A diagram showing how to implement that pattern.

Each implementation diagram shows the use of an internal load balancer. If a specific load balancer isn't shown in the diagram, we recommend that you use an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal). If you want to use [multiple backend services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#multiple_backend_services), you could use an [internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) instead.

  * A discussion of that pattern's benefits and drawbacks.




### Hide Pod IP addresses from on-premises networks only

The architecture pattern where you hide IP addresses from on-premises networks uses a combination of the following routing objectives:

  * Have the GKE clusters on Google Cloud assign Pod IP addresses that are routed throughout the Google Cloud deployment.
  * Prevent these IP addresses from being routed without NAT to on-premises resources or to other cloud environments through [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn) or [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect).



This architecture pattern is commonly used with the Class E/RFC 5735 IP address space because this space includes many IP addresses. Having so many IP addresses available helps accommodate the need to provide unique IP addresses to each Pod. However, Class E/RFC 5735 IP addresses can't be easily routed to on-premises resources because many network hardware vendors block this traffic.

Instead of using the Class E/RFC 5735 IP address space, you can use RFC 1918 IP addresses or an internal set of non-RFC 1918 IP addresses. If you use one of these other sets of IP addresses, determine whether there is any overlap of IP addresses between those addresses used for the Pods and those addresses used in on-premises networks. If there is overlap, make sure that there is never any communication between clusters that use those addresses and the on-premises applications that use those same addresses.

The following steps outline how to set up this architecture pattern:

  1. Create a secondary IP address range for the Pod subnet. As previously described in this section, you can create this address range from the Class E/RFC 5735 space, the RFC 1918 space, or an internal set of non-RFC 1918 IP addresses. Typically, the Class E/RFC 5735 space is used.
  2. Use [custom advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes) and remove the Pod IP address range from the advertisements on your Cloud Routers. Removing these addresses helps to ensure that Pod IP ranges are not announced through [Border Gateway Protocol (BGP)](https://wikipedia.org/wiki/Border_Gateway_Protocol) to your on-premises routers.
  3. Create your GKE cluster by using the secondary IP address range as the classless inter-domain routing (CIDR) for the Pod. You can use the strategies described in Reduce internal IP address usage in GKE to reduce IP address usage.
  4. Add the following IP addresses to [the `nonMasqueradeCIDRs` list in the masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#config-ip-masq-agent):

     * The IP address range that you used for Pods.
     * The IP address range used for nodes.
     * Other IP addresses that are used only on Google Cloud, such as the primary IP address ranges used on Google Cloud.

Don't include the internal IP address ranges that are used in on-premises environments or in other cloud environments. If you have Windows workloads in Google Cloud, keep them in separate subnets and don't include those ranges either.




When you use the previous steps to set up this pattern, you configure your clusters to have the following behaviors:

  * Act like a fully integrated network model within Google Cloud.
  * Act like an island-mode network model when interacting with on-premises networks.



To have this alternative pattern fully emulate the island-mode network model, you need to change [the `nonMasqueradeCIDRs` list in the masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#config-ip-masq-agent) to a list containing only the cluster's node and Pod IP address ranges. Making such a list results in always masquerading traffic outside the cluster to the node IP address, even within Google Cloud. However, after making this change, you can't collect Pod-level telemetry data within the VPC network.

The following diagram shows an implementation of this architecture pattern:

![Network diagram that shows the implementation of hiding IP address from on-premises networks only.](https://docs.cloud.google.com/static/architecture/images/gke-ip-address-mgmt-strategies-hide-on-prem-only.svg)

The preceding diagram shows how to hide Pod IP addresses from external networks. As shown in this diagram, Pods within Google Cloud can communicate directly with each other, even between clusters. This Pod communication is similar to the [GKE model](https://docs.cloud.google.com/architecture/gke-compare-network-models#gke-networking-model). Notice that the diagram also shows the Pods using addresses in the Class E/RFC 5735 space.

For traffic sent outside of the clusters, the diagram shows how source NAT (SNAT) is applied to that traffic as it exits the node. SNAT is used regardless of whether that traffic gets routed through Cloud VPN to on-premises applications or through [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) to external applications.

This architecture pattern uses Pod IP addresses for communication within Google Cloud. Traffic is only masqueraded when directed toward on-premises applications or other cloud environments. While you can't connect to Pods directly from on-premises applications, you can connect to services exposed through internal load balancing.

Hiding Pod IP addresses from on-premises networks has the following advantages:

  * You can still take advantage of the fully integrated network model within Google Cloud, such as using firewalls and collecting telemetry data based on Pod IP addresses. In addition, you can connect to Pods directly for debugging purposes from within Google Cloud.
  * You can still use multi-cluster service meshes with Pod IP addresses within Google Cloud.



However, hiding Pod IP addresses from external networks has the following disadvantages:

  * You can't reuse Pod or Services IP address ranges for different clusters within Google Cloud.
  * You might have to manage two different sets of firewall rules: one for traffic between on-premises networks and one for traffic fully within Google Cloud.
  * You can't have direct Pod-to-Pod communication in multi-cluster service meshes that span both Google Cloud and your on-premises or other cloud service providers environment. When using Istio for example, all communication has to happen between Istio Gateways.



### Hide Pod IP addresses by using Private Service Connect

This architecture pattern uses [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) to hide Pod IP addresses. Use this architecture pattern when you have the following needs:

  * You only need to expose a limited number of Services from your GKE clusters.
  * Your GKE clusters can work independently and don't require egress communication to many applications in your corporate network.



Private Service Connect provides a way to publish your services that are to be consumed from other networks. You can expose your GKE Services by using an internal passthrough Network Load Balancer and [service attachments](https://docs.cloud.google.com/vpc/docs/private-service-connect#service-attachments), and consume these services by using an [endpoint](https://docs.cloud.google.com/vpc/docs/private-service-connect#endpoints) from other VPC networks.

The following steps outline how to set up this architecture pattern:

  1. In a separate VPC network, create a GKE cluster. The VPC network should contain only that cluster.
  2. For each GKE Service in your cluster that needs to be accessible from other clusters or applications in another VPC network, [create an internal passthrough Network Load Balancer with Private Service Connect](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing-across-vpc-net#ilb_psc).
  3. (Optional) If your GKE cluster needs egress communication to some applications in your corporate network, expose those applications by [publishing services through Private Service Connect](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-producer).

The following diagram shows an implementation of this architecture pattern:




![Network diagram that shows the implementation of hiding IP address by using Private Service Connect.](https://docs.cloud.google.com/static/architecture/images/gke-ip-address-mgmt-strategies-hiding-using-psc.svg)

The preceding diagram shows how communication within and across clusters in the Private Service Connect model is similar to [an isolated network model](https://docs.cloud.google.com/architecture/gke-compare-network-models#isolated-model). However, allowed communication happens through Private Service Connect endpoints instead of through public IP addresses. As shown in this diagram, every cluster gets its own separate VPC network. Additionally, each VPC network can share the same IP address, and each cluster can share the same IP address space. Only Pods within a cluster can communicate directly with each other.

For communication from outside of the cluster, the diagram shows how an external application can reach the cluster through a Private Service Connect endpoint. That endpoint connects to the service attachment provided by the service producer in the cluster VPC network. Communication between clusters also goes through a Private Service Connect endpoint and a service producer's service attachment.

Using Private Service Connect to hide Pod IP addresses has the following advantages:

  * You don't have to plan IP addresses because the IP address space of the GKE cluster is hidden from the rest of the network. This approach exposes only a single IP address per service to the consuming VPC network.
  * Securing your cluster is easier because this model clearly defines which services are exposed, and only those exposed services can be reached from the rest of the VPC network.



However, using Private Service Connect to hide Pod IP addresses has the following disadvantages:

  * Pods inside the cluster can't establish private communication outside the cluster. Pods can only talk to public services (when the Pods have internet connectivity) or Google APIs (by using Private Google Access). If services outside the cluster are exposed through Private Service Connect, Pods can also reach those services. However, not all internal service providers create service attachments. So, the use of Private Service Connect only works when the number of these services are limited to those providers who do provide attachments.
  * Endpoints can only be reached from the same region that the service sits in. Furthermore, these endpoints can be reached only from the connected VPC network itself, not from peered VPC networks or networks connected through Cloud VPN or Cloud Interconnect.



### Hide Pod IP addresses by using Cloud VPN

This architecture pattern uses Cloud VPN to create a separation between the GKE clusters and the main VPC network. When you create this separation, the resulting network functions similarly to the [island-mode network model](https://docs.cloud.google.com/architecture/gke-compare-network-models#island-mode-model). Like the island-mode model, this pattern offers you the advantage of reusing Pod and Service IP address ranges between clusters. Reuse is possible because communication with applications outside of the cluster use SNAT. The nodes use SNAT to map Pod IP addresses to its own node IP address before the traffic exits the node.

The following steps outline how to set up this model:

  1. In a separate VPC network, create a GKE cluster. The VPC network should contain only that cluster.

For the cluster, use the unused portion of your public IP address assignment to define two IP address ranges: one for Pods and one for Services. Size these IP address ranges based on the needs of the largest GKE cluster that you expect to use. Reserve each of these ranges for exclusive use within GKE. You also reuse these ranges for all GKE clusters in your organization.

Sometimes, reserving such a large range of IP addresses isn't possible. Your organization might already use either or both of the Pod and Services IP address ranges for other applications. If the IP address range is in use and can't be reserved, make sure the applications that use those IP addresses don't need to communicate with the GKE cluster.

  2. For the cluster that you just created, configure [the `nonMasqueradeCIDRs` list in the masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#config-ip-masq-agent) to a list containing the cluster's node and Pod IP address ranges. This list results in GKE always masquerading traffic leaving the cluster to the node IP address, even within Google Cloud.

  3. Use Cloud VPN to connect the VPC network that contains the GKE cluster to the existing (main) VPC network.

  4. Use [custom advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes) to stop the cluster's VPC network from advertising the Pod and Services IP address ranges that are directed toward your main VPC network.

  5. Repeat steps 1-4 for the other GKE clusters that you need. For all clusters, use the same IP address ranges for Pods and Services. However, use distinct IP addresses for each node.

  6. If you have connectivity to on-premises networks through Cloud VPN or Cloud Interconnect, use [custom advertised routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes) to manually advertise the node IP ranges.

  7. If you have other networks connected to your main VPC network through VPC Network Peering, [export custom routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#importing-exporting-routes) on these peerings to ensure the GKE cluster nodes can reach the peered networks.




The following diagram shows an implementation of using Cloud VPN to hide Pod IP addresses:

![Network diagram that shows the implementation of hiding IP address by using Cloud VPN.](https://docs.cloud.google.com/static/architecture/images/gke-ip-address-mgmt-strategies-hide-through-vpn.svg)

The preceding diagram shows how to hide Pod IP addresses by using Cloud VPN, which creates an approach that is similar to the island-mode network model. As shown in the diagram, every GKE cluster gets its own separate VPC network. Each network has a node IP address space that is distinct but uses the same Pod IP address space. Cloud VPN tunnels connect these VPC networks to each other and to the corporate network, and the Pod IP address space is not advertised from the VPC networks that contain clusters.

Notice in the diagram that only Pods within a cluster can communicate directly with each other. The node uses SNAT to masquerade the Pod IP address space when communicating outside the cluster to another cluster, to the corporate network, or to a connected on-premises network. Pods can't be reached directly from other clusters or the corporate network. Only cluster Services exposed with an internal load balancer can be reached through the Cloud VPN connections.

Using Cloud VPN to hide Pod IP addresses has the following advantages:

  * As described in the [island-mode network model](https://docs.cloud.google.com/architecture/gke-compare-network-models#island-mode-model), you can reuse Pod and Service IP address ranges between clusters.
  * Firewalls might need less configuration because Pod IP addresses can't be reached directly from the main VPC network and connected networks. Therefore, you don't need to configure explicit firewall rules to block communication with the Pods.



However, using Cloud VPN to hide Pod IP addresses has the following disadvantages:

  * The same disadvantages as mentioned in the [island-mode network model](https://docs.cloud.google.com/architecture/gke-compare-network-models#island-mode-model) apply. For example, you can't set firewall rules at the Pod level. You also can't collect telemetry data at the Pod level in the main VPC network or connected network.
  * Compared to the default GKE networking model, this pattern leads to additional costs that come from [the costs of that are associated with Cloud VPN tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/pricing) and [data transfer charges](https://docs.cloud.google.com/vpc/network-pricing#egress-within-gcp).
  * Cloud VPN has a [bandwidth limit per VPN tunnel](https://docs.cloud.google.com/network-connectivity/docs/vpn/quotas#limits). If you reach this bandwidth limit, you can configure multiple Cloud VPN tunnels and distribute traffic by using [equal-cost multipath (ECMP)](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/order-of-routes#example-ecmp-tunnels). But performing these actions does add to the complexity of setting up and maintaining your GKE implementation.
  * Keeping the route advertisements in sync adds complexity to cluster creation. Whenever you create new GKE clusters, you need to set up Cloud VPN tunnels, and create custom advertised routes on those tunnels and to on-premises applications.



### Hide Pod IP addresses by using internally-used public IP addresses and VPC Network Peering

If your organization owns unused public IP addresses, you can use this architecture pattern that resembles an [island-mode network model](https://docs.cloud.google.com/architecture/gke-compare-network-models#island-mode-model) but through the private use of this Public IP address space. This architecture is similar to the model that uses Cloud VPN but instead uses [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) to create the separation between GKE cluster and the main network.

The following steps outline how to set up this architecture pattern:

  1. In a separate VPC network, create a GKE cluster. The VPC network should contain only that cluster.

For the cluster, use the unused portion of your public IP address assignment to define two IP address ranges: one for Pods and one for Services. Size these IP address ranges based on the needs of the largest GKE cluster that you expect to use. Reserve each of these ranges for exclusive use within GKE. You also reuse these ranges for all GKE clusters in your organization.

Instead of using your public IP address assignment, it is theoretically possible to use the larger, unused public IP address blocks that are owned by third parties. However, we strongly discourage such a setup because such IP addresses might be sold or used publicly at any time. The sale or use of addresses has lead to security and connectivity issues when using public services on the internet.

  2. For the cluster that you just created, configure [the `nonMasqueradeCIDRs` list in the masquerade agent](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent#config-ip-masq-agent) to a list containing the cluster's node and Pod IP address ranges. This list results in GKE always masquerading traffic leaving the cluster to the node IP address, even within Google Cloud.

  3. Use VPC Network Peering to connect the VPC network that contains the GKE cluster to the existing (main) VPC network. Because you don't want PUPI addresses to be exchanged in this model, set the `--no-export-subnet-routes-with-public-ip` flag when configuring the peering.

  4. Repeat steps 1-3 for the other GKE clusters that you need. For all clusters, use the same IP address range for Pod and Services. However, use a distinct IP address for each node.

  5. If you have connectivity to on-premises networks through Cloud VPN or Cloud Interconnect, use [custom route advertisements ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/advertised-routes)to manually advertise the node IP address ranges.




The following diagram shows an implementation of this architecture pattern:

![Network diagram that shows the implementation of hiding IP addresses by using PUPI and VPC Network Peering.](https://docs.cloud.google.com/static/architecture/images/gke-ip-address-mgmt-strategies-hide-through-pupi-vpc-peering.svg)

The preceding diagram shows how to hide IP addresses by using VPC Network Peering. As shown in the diagram, every GKE cluster gets its own separate VPC network. Each node has a distinct node IP address space but uses the same Pod IP address space that was defined from your organization's PUPI address space. The VPC networks connect to each other and to non-Kubernetes applications in Google Cloud through VPC Network Peering. The PUPI address space is not advertised between the peerings. The VPC networks connect to the corporate network through Cloud VPN tunnels.

Only Pods within a cluster can communicate directly with each other. The node uses SNAT to masquerade the Pod IP space when communicating outside the cluster to another cluster, to the corporate network, or to a connected on-premises network. Pods can't be reached directly from other clusters or the corporate network. Only Services exposed with an internal load balancer can be reached through the VPC Network Peering connections.

This architecture pattern is similar to the Cloud VPN approach described previously, but has the following advantages over that pattern:

  * Unlike the Cloud VPN architecture pattern,VPC Network Peering doesn't come with any additional costs for Cloud VPN tunnels or bandwidth between environments.
  * VPC Network Peering doesn't have bandwidth limitations and is fully integrated into Google's software-defined networks. Thus, VPC Network Peering might provide slightly lower latency than Cloud VPN because peering doesn't require the gateways and processing needed by Cloud VPN.



However, the VPC Network Peering model also has the following disadvantages over the Cloud VPN model:

  * Your organization requires a public IP address space that is both unused and is large enough for the Pod IP address space needed by the largest GKE cluster that you expect to have.
  * VPC Network Peering is non-transitive. Thus, GKE clusters connected through VPC Network Peering to the main VPC network can't directly talk to each other or to applications in VPC networks that are peered with the main VPC. You have to directly connect those networks through VPC Network Peering to enable such communication, or use a proxy VM in the main VPC network.



### Use multi-NIC instances to hide cluster addresses

This architecture pattern consists of the following components and technologies to create a model that is similar to an island-mode network model:

  * It uses Compute Engine instances with multiple network interface cards (multi-NIC) to create a separation layer between GKE clusters and the main VPC network.
  * It uses NAT on IP addresses sent between those environments.



You might use this pattern when you need to inspect, transform, or filter specific traffic that enters or exits the GKE clusters. If you need to do this type of inspecting, transforming, or filtering, use the deployed Compute Engine instances to perform these tasks.

Using multi-NIC instances to hide cluster addresses has the following advantages:

  * The IP address space of the GKE cluster is hidden from the rest of the network. Only a single IP address per service is exposed to the consuming VPC network.
  * Services can be reached globally, from connected on-premises networks, and from peered networks.



However, using multi-NIC instances to hide cluster addresses has the following disadvantages:

  * This model is more complex to implement than other approaches because it requires not only implementing the model, but also setting up the monitoring and logging for the multi-NIC instances.
  * The multi-NIC instances have [bandwidth limitations](https://docs.cloud.google.com/compute/docs/network-bandwidth) and are subject to [VM instances pricing](https://cloud.google.com/compute/vm-instance-pricing).
  * You need to manage and upgrade the multi-NIC instances.



## What's next

  * Companion document: [Comparison of network models used by GKE and other Kubernetes implementations](https://docs.cloud.google.com/architecture/gke-compare-network-models#fully-integrated-model)
  * [GKE networking best practices](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices)
  * [Compare AWS and Azure services to Google Cloud](https://docs.cloud.google.com/free/docs/aws-azure-gcp-service-comparison)
  * [Migrating containers to Google Cloud: Migrating Kubernetes to GKE](https://docs.cloud.google.com/architecture/migrating-containers-kubernetes-gke)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
