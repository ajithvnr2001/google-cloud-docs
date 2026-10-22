---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/lb-bundled-bgp/
title: Configure bundled load balancers with BGP \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:42.153497+00:00
---

# Configure bundled load balancers with BGP  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/lb-bundled-bgp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Configure bundled load balancers with BGP Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to set up and use bundled load balancers with Border Gateway Protocol (BGP) for Google Distributed Cloud. This load-balancing mode supports the advertisement of `ServiceType` `LoadBalancer` virtual IP addresses (VIPs) through external Border Gateway Protocol (eBGP) for your clusters. In this scenario, your cluster network is an autonomous system, which interconnects with another autonomous system, an external network, through peering.

The bundled load balancers with BGP capability apply to all cluster types, but admin clusters only support the control plane load-balancing part of this capability.

**Note:** Load balancing with BGP is supported in the GKE On-Prem API for user clusters. For details, see [BareMetalLoadBalancerConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalClusters#baremetalloadbalancerconfig) in the GKE On-Prem API documentation. In version 1.34 and later, this feature is supported in the GKE On-Prem API for admin clusters. For details, see [BareMetalAdminLoadBalancerConfig](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/reference/on-prem-api/rest/v1/projects.locations.bareMetalAdminClusters#baremetaladminloadbalancerconfig) in the GKE On-Prem API documentation.

Using the bundled load balancers with BGP feature provides the following benefits:

  * Uses N-way active/active load-balancing capability, providing faster failover and more efficient use of available bandwidth.
  * Supports Layer 3 protocol that operates with third-party top-of-rack (ToR) switches and routers that are compatible with eBGP.
  * Enables data centers that are running an advanced software-defined networking (SDN) stack to push the Layer 3 boundary all the way to the clusters.



## How bundled load balancing with BGP works

The following sections provide a quick summary of how bundled load balancers with BGP work.

**Note:** For bundled load balancing with BGP, Network Gateway for GDC manages BGP functions, such as route advertisement and peering sessions. In bundled load balancing with BGP, we use the bundled MetalLB capability for IP address management (IPAM) only, not for any BGP functions. Specifically, in this load balancing solution, MetalLB assigns VIP addresses to Services from the range of available floating IP addresses.

### BGP peering

The bundled load balancers with BGP feature starts several BGP connections to your infrastructure. BGP has the following technical requirements:

  * Peering sessions are separate for control plane VIP and for service VIPs.
  * Control plane peering sessions are initiated from the IP addresses of the control plane nodes.
  * Service peering sessions are initiated from floating IP addresses that you specify in the `NetworkGatewayGroup` custom resource.
  * Network Gateway for GDC controller manages the floating IP addresses.
  * Bundled BGP-based load balancing supports eBGP peering only.
  * Multi-hop peering is supported by default.
  * MD5 passwords on BGP sessions are not supported.
  * IPv6-based peering sessions are not supported.
  * Routes advertised to any peer are expected to be redistributed throughout the network and reachable from anywhere else in the cluster.
  * Use of BGP `ADD-PATH` capability in receive mode is recommended for peering sessions.
  * Advertising multiple paths from each peer results in active/active load balancing.
  * Equal-cost multipath routing (ECMP) should be enabled for your network so that multiple paths can be used to spread traffic across a set of load balancer nodes.
  * Configure the BGP sessions on the external peers (such as Top-of-Rack switches) in Passive mode. The cluster nodes and floating IP addresses act as the active peers and initiate the BGP peering sessions.



### Control plane load balancing

Each control plane node in your cluster establishes BGP sessions with one or more peers in your infrastructure. We require that each control plane node has at least one peer. In the cluster configuration file, you can configure which control plane nodes connect to which external peers.

The following diagram shows an example of control plane peering. The cluster has two control plane nodes in one subnet and one in another. There is an external peer (TOR) in each subnet and the Google Distributed Cloud control plane nodes peer with their TOR.

**Note:** The diagram illustrates an example only. Peers aren't required to be in the same subnet. We enable multi-hop BGP by default.

![Service load balancing with BGP peering](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/images/cp-peering.svg)

### Service load balancing

In addition to the peering sessions that are initiated from each control plane node for the control plane peering, additional peering sessions are initiated for `LoadBalancer` Services. These peering sessions are not initiated from cluster node IP addresses directly, but use floating IP addresses instead.

**Note:** Service (or data plane) load balancing does not apply to admin clusters. If you include BGP session configuration information for the data plane on your admin cluster, the configuration is ignored.

Services with an `externalTrafficPolicy=Local` network policy are supported. However, the `externalTrafficPolicy=Local` setting is workload dependent and causes routes to update whenever a Pod backing the Service is added or removed completely from a node. This route updating behavior may cause Equal Cost Multi-Path (ECMP) routing to change traffic flows, which can result in drops in traffic.

#### Floating IP addresses

Service load balancing requires you to reserve floating IP addresses in the cluster node subnets to use for BGP peering. At least one floating IP address is required for the cluster, but we recommend you reserve at least two addresses to ensure high availability for BGP sessions. The floating IP addresses are specified in the `NetworkGatewayGroup` custom resource (CR), which can be included in the cluster configuration file.

Floating IP addresses remove the worry about mapping BGP speaker IP addresses to nodes. The Network Gateway for GDC controller takes care of assigning the `NetworkGatewayGroup` to nodes and also manages the floating IP addresses. If a node goes down, the Network Gateway for GDC controller reassigns floating IP addresses to ensure that external peers have a deterministic IP address to peer with.

#### External peers

For data plane load balancing, you can use the same external peers that were specified for control plane peering in the `loadBalancer.controlPlaneBGP` section of the cluster configuration file. Alternatively, you can specify different BGP peers.

If you want to specify different BGP peers for data plane peering, append `BGPLoadBalancer` and `BGPPeer` resource specifications to the cluster configuration file. If you don't specify these custom resources, the control plane peers are used automatically for the data plane.

You specify the external peers used for peering sessions with the floating IP addresses in the `BGPPeer` custom resource, which you add to the cluster configuration file. The `BGPPeer` resource includes a label for identification by the corresponding `BGPLoadBalancer` custom resource. You specify the matching label in the `peerSelector` field in the `BGPLoadBalancer` custom resource to select the `BGPPeer` for use.

The Network Gateway for GDC controller attempts to establish sessions (the number of sessions is configurable) to each external peer from the set of reserved floating IP addresses. We recommend that you specify at least two external peers to ensure high availability for BGP sessions. Each external peer designated for Services load balancing must be configured to peer with every floating IP address specified in the `NetworkGatewayGroup` custom resource.

#### Load balancer nodes

A subset of nodes from the cluster is used for load balancing, which means they are the nodes advertised to be able to accept incoming load-balancing traffic. This set of nodes defaults to the control plane node pool, but you can specify a different node pool in the `loadBalancer` section of the cluster configuration file. If you specify a node pool, it is used for the load balancer nodes, instead of the control plane node pool.

The floating IP addresses, which function as BGP speakers, may or may not run on the load balancer nodes. The floating IP addresses are assigned to a node in the same subnet and peering is initiated from there, regardless of whether it is a load balancer node. However, next hops advertised over BGP are always the load balancer nodes.

#### Example peering topology

The following diagram shows an example of Service load balancing with BGP peering. There are two floating IP addresses assigned to nodes in their respective subnets. There are two external peers defined. Each floating IP peers with both external peers.

![Service load balancing with BGP peering](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/images/ang-peering.svg)

## Set up the BGP load balancer

The following sections describe how to configure your clusters and your external network to use the bundled load balancer with BGP.

### Plan your integration with external infrastructure

In order to use the bundled load balancer with BGP, you must set up the external infrastructure:

  * External infrastructure must be configured to peer with each of the control plane nodes in the cluster to set up the control plane communication. These peering sessions are used to advertise the Kubernetes control plane VIPs.

  * External infrastructure must be configured to peer with a set of reserved floating IP addresses for data plane communication. The floating IP addresses are used for BGP peering for the Service VIPs. We recommend you use two floating IP addresses and two peers to ensure high availability for BGP sessions. The process of reserving floating IP is described as part of configuring your cluster for bundled load balancing with BGP.




When you've configured the infrastructure, add the BGP peering information to the cluster configuration file. The cluster you create can initiate peering sessions with the external infrastructure.

### Configure your cluster for bundled load balancing with BGP

You enable and configure bundled load balancing with BGP in the cluster configuration file when you create a cluster. In the cluster configuration file, you enable advanced networking and update the `loadBalancer` section. You also append specifications for the following three custom resources:

  * `NetworkGatewayGroup`: specifies floating IP addresses that are used for Services BGP peering sessions.

  * `BGPLoadBalancer`: specifies with label selectors which peers are used for BGP load balancing.

  * `BGPPeer`: specifies individual peers, including a label for selection purposes, for BGP peering sessions.




The following instructions describe how to configure your cluster and the three custom resources to set up bundled load balancing with BGP.

  1. Add the `advancedNetworking` field to the cluster configuration file in the `clusterNetwork` section and set it to `true`.

This field enables advanced networking capability, specifically the Network Gateway Group resource.
         
         apiVersion: baremetal.cluster.gke.io/v1
         kind: Cluster
         metadata:
           name: bm
           namespace: CLUSTER_NAMESPACE
         spec:
         ...
           clusterNetwork:
             advancedNetworking: true
         

Replace `CLUSTER_NAMESPACE` with the namespace for the cluster. By default, the cluster namespaces for Google Distributed Cloud are the name of the cluster prefaced with `cluster-`. For example, if you name your cluster `test`, the namespace is `cluster-test`.

  2. In the `loadBalancer` section of the cluster configuration file, set `mode` to `bundled` and add a `type` field with a value of `bgp`.

These field values enable BGP-based bundled load balancing.
         
         ...
           loadBalancer:
             mode: bundled
         
             # type can be 'bgp' or 'layer2'. If no type is specified, we default to layer2.
             type: bgp
             ...
         

  3. To specify the BGP-peering information for the control plane, add the following fields to the `loadBalancer` section:
         
         ...
             # AS number for the cluster
             localASN: CLUSTER_ASN
         
             # List of BGP peers used for the control plane peering sessions.
             bgpPeers:
             - ip: PEER_IP
               asn: PEER_ASN
               # optional; if not specified, all CP nodes connect to all peers.
               controlPlaneNodes:   # optional
               - CP_NODE_IP
         ...
         

Replace the following:

     * `CLUSTER_ASN`: the autonomous system number for the cluster being created.
     * `PEER_IP`: the IP address of the external peer device.
     * `PEER_ASN`: the autonomous system number for the network that contains the external peer device.
     * `CP_NODE_IP`: (optional) the IP address of the control plane node that connects to the external peer. If you don't specify any control plane nodes, all control plane nodes can connect to the external peer. If you specify one or more IP addresses, only the nodes specified participate in peering sessions.

You may specify multiple external peers, `bgpPeers` takes a list of mappings. We recommend you specify at least two external peers for high availability for BGP sessions. For an example with multiple peers, see Example configurations.

  4. Set the `loadBalancer.ports`, `loadBalancer.vips`, and `loadBalancer.addressPools` fields (default values shown).

**Note:** When you use bundled BGP-based load balancing (`mode: bundled` and `type: bgp`), the VIPs you specify must not come from the same subnet as any of the nodes in the cluster.
         
         ...
           loadBalancer:
           ...
             # Other existing load balancer options remain the same
             ports:
               controlPlaneLBPort: 443
             # When type=bgp, the VIPs are advertised over BGP
             vips:
               controlPlaneVIP: 10.0.0.8
               ingressVIP: 10.0.0.1
         
             addressPools:
             - name: pool1
               addresses:
               - 10.0.0.1-10.0.0.4
         ...
         

  5. Specify the cluster node to use for load balancing the data plane.

This step is optional. If you don't uncomment the `nodePoolSpec` section, the control plane nodes are used for data plane load balancing.
         
         ...
           # Node pool used for load balancing data plane (nodes where incoming traffic
           # arrives. If not specified, this defaults to the control plane node pool.
           # nodePoolSpec:
           #   nodes:
           #   - address: <Machine 1 IP>
         ...
         

  6. Reserve floating IP addresses by configuring the `NetworkGatewayGroup` custom resource:

The floating IP addresses are used in peering sessions for data plane load balancing.
         
         ...
         ---
         apiVersion: networking.gke.io/v1
         kind: NetworkGatewayGroup
         metadata:
           name: default
           namespace: CLUSTER_NAMESPACE
         spec:
           floatingIPs:
           - FLOATING_IP
           nodeSelector:    # optional
           - NODE_SELECTOR
         ...
         

Replace the following:

     * `CLUSTER_NAMESPACE`: the namespace for the cluster. By default, the cluster namespaces for Google Distributed Cloud are the name of the cluster prefaced with `cluster-`. For example, if you name your cluster `test`, the namespace is `cluster-test`.
     * `FLOATING_IP`: an IP address from one of the cluster's subnets. You must specify at least one IP address, but we recommend you specify at least two IP addresses.
     * `NODE_SELECTOR`: (Optional) a label selector to identify nodes for instantiating peering sessions with external peers, such as top-of-rack (ToR) switches. If it isn't needed, remove this field.

Ensure the `NetworkGatewayGroup` custom resource is named `default` and uses the cluster namespace. For an example of how the `NetworkGatewayGroup` custom resource specification might look, see Example configurations.

  7. (Optional) Specify the peers to use for data plane load balancing by configuring the `BGPLoadBalancer` custom resource:
         
         ...
         ---
         apiVersion: networking.gke.io/v1
         kind: BGPLoadBalancer
         metadata:
           name: default
           namespace: CLUSTER_NAMESPACE
         spec:
           peerSelector:
             PEER_LABEL: "true"
         ...
         

Replace the following:

     * `CLUSTER_NAMESPACE`: the namespace of the cluster. By default, the cluster namespaces for Google Distributed Cloud are the name of the cluster prefaced with `cluster-`. For example, if you name your cluster `test`, the namespace is `cluster-test`.
     * `PEER_LABEL`: the label used to identify which peers to use for load balancing. Any `BGPPeer` custom resource with a matching label specifies the details of each peer.

Ensure the `BGPLoadBalancer` custom resource is named `default` and uses the cluster namespace. If you don't specify a `BGPLoadBalancer` custom resource, the control plane peers are used automatically for data plane load balancing. For comprehensive examples, see Example configurations.

  8. (Optional) Specify the external peers for the data plane by configuring one or more `BGPPeer` custom resources:
         
         ...
         ---
         apiVersion: networking.gke.io/v1
         kind: BGPPeer
         metadata:
           name: BGP_PEER_NAME
           namespace: CLUSTER_NAMESPACE
           labels:
             PEER_LABEL: "true"
         spec:
           localASN: CLUSTER_ASN
           peerASN: PEER_ASN
           peerIP: PEER_IP
           sessions: SESSION_QTY
           selectors:   # Optional
             gatewayRefs:
             - GATEWAY_REF
           ...
         

Replace the following:

     * `BGP_PEER_NAME`: the name of the peer.
     * `CLUSTER_NAMESPACE`: the namespace for the cluster. By default, the cluster namespaces for Google Distributed Cloud are the name of the cluster prefaced with `cluster-`. For example, if you name your cluster `test`, the namespace is `cluster-test`.
     * `PEER_LABEL`: the label used to identify which peers to use for load balancing. This label should correspond with the label specified in the `BGPLoadBalancer` custom resource.
     * `CLUSTER_ASN`: the autonomous system number for the cluster being created.
     * `PEER_IP`: the IP address of the external peer device. We recommend that you specify at least two external peers, but you must specify at least one.
     * `PEER_ASN`: the autonomous system number for the network that contains the external peer device.
     * `SESSION_QTY`: the number of sessions to establish for this peer. We recommend that you establish at least two sessions to ensure that you maintain a connection to the peer in case one of your nodes goes down.
     * `GATEWAY_REF`: (Optional) the name of a NetworkGatewayGroup resource to use for peering. If left unset, any or all gateway resources may be used. Use this setting in conjunction with the `nodeSelector` field in the NetworkGatewayGroups resource to select which nodes to use for peering with a specific external peer, such as a ToR switch. With one gateway per line, this can take multiple entries to select multiple NetworkGatewayGroups.

You may specify multiple external peers by creating additional `BGPPeer` custom resources. We recommend you specify at least two external peers (two custom resources) for high availability for BGP sessions. If you don't specify a `BGPPeer` custom resource, the control plane peers are used automatically for data plane load balancing.

**Warning:** The `selectors` field (including `gatewayRefs`) in `BGPPeer` is not supported when you use the GKE On-Prem API to configure clusters. If your cluster uses multiple `NetworkGatewayGroup` resources (such as with Egress NAT), this limitation can break external routing. For more information and a workaround, see BGP Selector Limitation with Cloud API/Terraform.
  9. When you run `bmctl cluster create` to create your cluster, preflight checks run. Among other checks, the preflight checks validate the BGP peering configuration for the control plane and report any issues directly to the admin workstation before the cluster can be created.

On success, the added BGP load balancing resources (NetworkGatewayGroup, BGPLoadBalancer, and BGPPeer) go into the admin cluster in the user cluster namespace. Use the admin cluster kubeconfig file when you make subsequent updates to these resources. The admin cluster then reconciles changes to the user cluster. If you edit these resources on the user cluster directly, the admin cluster overwrites your changes in subsequent reconciliations.




### Advertise multiple next-hops per session with BGP `ADD-PATH`

We recommend that you use the BGP `ADD-PATH` capability for peering sessions as specified in [RFC 7911](https://datatracker.ietf.org/doc/html/rfc7911). By default, the BGP protocol allows only a single next hop to be advertised to peers for a single prefix. BGP `ADD-PATH` enables advertising multiple next hops for the same prefix. When `ADD-PATH` is used with BGP-based bundled load balancing, the cluster can advertise multiple cluster nodes as frontend nodes (next hops) for a load balancer service (prefix). Enable ECMP in the network so that traffic can be spread over multiple paths. The ability to fan out traffic by advertising multiple cluster nodes as next hops, provides improved scaling of data plane capacity for load balancing.

If your external peer device, such as a top-of-rack (ToR) switch or router, supports BGP `ADD-PATH`, it is sufficient to turn on the receive extension only. Bundled load balancing with BGP works without the `ADD-PATH` capability, but the restriction of advertising a single load-balancing node per peering session limits load balancer data plane capacity. Without `ADD-PATH`, Google Distributed Cloud picks nodes to advertise from the load balancer node pool and attempts to spread next hops for different VIPs across different nodes.

### Restrict BGP peering to load balancer nodes

Google Distributed Cloud automatically assigns floating IP addresses on any node in the same subnet as the floating IP address. BGP sessions are initiated from these IP addresses even if they don't land on the load balancer nodes. This behavior is by design, because we have decoupled the control plane (BGP) from the data plane (LB node pools).

If you want to restrict the set of nodes which can be used for BGP peering, you can designate one subnet to be used only for load balancer nodes. That is, you can configure all nodes in that subnet to be in the load balancer node pool. Then, when you configure floating IP addresses which are used for BGP peering, ensure they are from this same subnet. Google Distributed Cloud ensures that the floating IP address assignments and BGP peering take place from load balancer nodes only.

### Set up BGP load balancing with dual-stack networking

Starting with Google Distributed Cloud release 1.14.0, the BGP-based bundled load balancer supports IPv6. With the introduction of IPv6 support, you can configure IPv6 and dual-stack LoadBalancer Services on a cluster configured for dual-stack networking. This section describes the changes required to configure dual-stack, bundled load balancing with BGP.

To enable dual-stack LoadBalancer Services, the following configuration changes are required:

  * The underlying cluster must be a configured for dual-stack networking:

    * Specify both IPv4 and IPv6 Service CIDRs in the cluster configuration file under `spec.clusterNetwork.services.cidrBlocks`.

    * Define appropriate ClusterCIDRConfig resources for specifying IPv4 and IPv6 CIDR ranges for Pods.

For more information on configuring a cluster for dual-stack networking, see [IPv4/IPv6 dual-stack networking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/dual-stack-networking).

  * Specify an IPv6 address pool in the cluster configuration file under `spec.loadBalancer.addressPools`. In order for [MetalLB to allocate IP addresses to a Dual Stack Service](https://metallb.universe.tf/usage/#ipv6-and-dual-stack-services), there must be at least one address pool having both IPv4 and IPv6 format addresses.




The following example configuration highlights the changes needed for dual-stack bundled load balancing with BGP:
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: bm
      namespace: cluster-bm
    spec:
    ...
      clusterNetwork:
      services:
          cidrBlocks:**      # Dual-stack Service IP addresses must be provided**
          - 10.96.0.0/16**      - fd00::/112**
    ...
      loadBalancer:
        mode: bundled
    
        # type can be 'bgp' or 'layer2'. If no type is specified we default to layer2.
        type: bgp
    
        # AS number for the cluster
        localASN: 65001
    
        bgpPeers:
        - ip: 10.8.0.10
          asn: 65002
        - ip: 10.8.0.11
          asn: 65002
    
        addressPools:
        - name: pool1
          addresses:
          # Each address must be either in the CIDR form (1.2.3.0/24)
          # or range form (1.2.3.1-1.2.3.5).
          - "203.0.113.1-203.0.113.20"**      - "2001:db8::1-2001:db8::20"  # Note the additional IPv6 range**
    
    ... # Other cluster config info omitted
    ---
    apiVersion: networking.gke.io/v1
    kind: NetworkGatewayGroup
    metadata:
      name: default
      namespace: cluster-bm
    spec:
      floatingIPs:
      - 10.0.1.100
      - 10.0.2.100** ---
    apiVersion: baremetal.cluster.gke.io/v1alpha1
    kind: ClusterCIDRConfig
    metadata:
      name: cluster-wide-1
      namespace: cluster-bm
    spec:
      ipv4:
        cidr: "192.168.0.0/16"
        perNodeMaskSize: 24
      ipv6:
        cidr: "2001:db8:1::/112"
        perNodeMaskSize: 120**
    

#### Limitations for dual-stack, bundled load balancing with BGP

When configuring your cluster to use dual-stack, bundled load balancing with BGP, note the following limitations:

  * IPv6 control plane load balancing isn't supported.

  * IPv6 BGP sessions aren't supported, but IPv6 routes can be advertised over IPv4 sessions using Multiprotocol BGP.




## Example configurations

The following sections demonstrate how to configure BGP-based load balancing for different options or behavior.

### Configure all nodes use the same peers

As shown in the following diagram, this configuration results in a set of external peers (`10.8.0.10` and `10.8.0.11`) that are reachable by all nodes. Control plane nodes (`10.0.1.10`, `10.0.1.11`, and `10.0.2.10`) and floating IP addresses (`10.0.1.100` and `10.0.2.100`) assigned to data plane nodes all reach the peers.

The same external peers are both reachable by either of the floating IP addresses (`10.0.1.100` or `10.0.2.100`) that are reserved for `loadBalancer` Services peering. The floating IP addresses can be assigned to nodes that are in the same subnet.

![BGP load balancing where all nodes use the same peers](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/images/bgp-lb-ex-1.svg)

As shown in the following cluster configuration sample, you configure the peers for the control plane nodes, `bgpPeers`, without specifying `controlPlaneNodes`. When no nodes are specified for peers, then all control plane nodes connect to all peers.

You specify the floating IP addresses to use for Services load-balancing peering sessions in the `NetworkGatewayGroup` custom resource. In this example, since no `BGPLoadBalancer` is specified, the control plane peers are used automatically for the data plane BGP sessions.

**Note:** Cluster configuration sections that don't apply to this bundled BGP-based load-balancing configuration have been removed to make the sample easier to read.
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: bm
      namespace: cluster-bm
    spec:
    ...
      loadBalancer:
        mode: bundled
    
        # type can be 'bgp' or 'layer2'. If no type is specified, we default to layer2.
        type: bgp
    
        # AS number for the cluster
        localASN: 65001
    
        bgpPeers:
        - ip: 10.8.0.10
          asn: 65002
        - ip: 10.8.0.11
          asn: 65002
    
    ... (other cluster config omitted)
    ---
    apiVersion: networking.gke.io/v1
    kind: NetworkGatewayGroup
    metadata:
      name: default
      namespace: cluster-bm
    spec:
      floatingIPs:
      - 10.0.1.100
      - 10.0.2.100
    

### Configure specific control plane nodes to peer with specific external peers

As shown in the following diagram, this configuration results in two control plane nodes (`10.0.1.10` and `10.0.1.11`) peering with one external peer (`10.0.1.254`). The third control plane node (`10.0.2.10`) is peering with another external peer (`10.0.2.254`). This configuration is useful when you don't want all nodes to connect to all peers. For example, you may want control plane nodes to peer with their corresponding top-of-rack (ToR) switches only.

The same external peers are both reachable by either of the floating IP addresses (`10.0.1.100` or `10.0.2.100`) that are reserved for Services load-balancing peering sessions. The floating IP addresses can be assigned to nodes that are in the same subnet.

![BGP load balancing with explicit mapping of control plane nodes to peers](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/images/bgp-lb-ex-2.svg)

As shown in the following cluster configuration sample, you restrict which control plane nodes can connect to a given peer by specifying their IP addresses in the `controlPlaneNodes` field for the peer in the `bgpPeers` section.

You specify the floating IP addresses to use for Services load-balancing peering sessions in the `NetworkGatewayGroup` custom resource. In this example, since no `BGPLoadBalancer` is specified, the control plane peers are used automatically for the data plane BGP sessions.

**Note:** Cluster configuration sections that don't apply to this bundled BGP-based load-balancing configuration have been removed to make the sample easier to read.
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: bm
      namespace: cluster-bm
    spec:
    ...
      loadBalancer:
        mode: bundled
    
        # type can be 'bgp' or 'layer2'. If no type is specified, we default to layer2.
        type: bgp
    
        # AS number for the cluster
        localASN: 65001
    
        bgpPeers:
        - ip: 10.0.1.254
          asn: 65002
          controlPlaneNodes:
            - 10.0.1.10
            - 10.0.1.11
        - ip: 10.0.2.254
          asn: 65002
          controlPlaneNodes:
            - 10.0.2.10
    
    ... (other cluster config omitted)
    ---
    apiVersion: networking.gke.io/v1
    kind: NetworkGatewayGroup
      name: default
      namespace: cluster-bm
    spec:
      floatingIPs:
      - 10.0.1.100
      - 10.0.2.100
    

### Configure control plane and data plane separately

As shown in the following diagram, this configuration results in two control plane nodes (`10.0.1.10` and `10.0.1.11`) peering with one external peer (`10.0.1.254`) and the third control plane node (`10.0.2.11`) peering with another external peer (`10.0.2.254`).

A third external peer (`10.0.3.254`) is reachable by either of the floating IP addresses (`10.0.3.100` or `10.0.3.101`) that are reserved for Services load-balancing peering sessions. The floating IP addresses can be assigned to nodes that are in the same subnet.

![BGP load balancing with separate configuration for control plane and data plane](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/images/bgp-lb-ex-3.svg)

As shown in the following cluster configuration sample, you restrict which control plane nodes can connect to a given peer by specifying their IP addresses in the `controlPlaneNodes` field for the peer in the `bgpPeers` section.

You specify the floating IP addresses to use for Services load-balancing peering sessions in the `NetworkGatewayGroup` custom resource.

To configure the data plane load balancing:

  * Specify the external peer for the data plane in the `BGPPeer` resource and add a label to use for peer selection, such as `cluster.baremetal.gke.io/default-peer: "true"`.

  * Specify the matching label for the `peerSelector` field in the `BGPLoadBalancer` resource.


**Note:** Cluster configuration sections that don't apply to this bundled BGP-based load-balancing configuration have been removed to make the sample easier to read.
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: bm
      namespace: cluster-bm
    spec:
    ...
      loadBalancer:
        mode: bundled
    
        # type can be 'bgp' or 'layer2'. If no type is specified, we default to layer2.
        type: bgp
    
        # AS number for the cluster
        localASN: 65001
    
        bgpPeers:
        - ip: 10.0.1.254
          asn: 65002
          controlPlaneNodes:
            - 10.0.1.10
            - 10.0.1.11
        - ip: 10.0.2.254
          asn: 65002
          controlPlaneNodes:
            - 10.0.2.11
    
    ... (other cluster config omitted)
    ---
    apiVersion: networking.gke.io/v1
    kind: NetworkGatewayGroup
      name: default
      namespace: cluster-bm
    spec:
      floatingIPs:
      - 10.0.3.100
      - 10.0.3.101
    ---
    apiVersion: networking.gke.io/v1
    kind: BGPLoadBalancer
    metadata:
      name: default
      namespace: cluster-bm
    spec:
      peerSelector:
        cluster.baremetal.gke.io/default-peer: "true"
    ---
    apiVersion: networking.gke.io/v1
    kind: BGPPeer
    metadata:
      name: bgppeer1
      namespace: cluster-bm
      labels:
        cluster.baremetal.gke.io/default-peer: "true"
    spec:
      localASN: 65001
      peerASN: 65002
      peerIP: 10.0.3.254
      sessions: 2
    

## Modify your BGP-based load-balancing configuration

After you have created your cluster configured to use bundled load balancing with BGP, some configuration settings can be updated, but some can't be updated after the cluster is created.

Use the admin cluster kubeconfig file when you make subsequent updates to the BGP-related resources (NetworkGatewayGroup, BGPLoadBalancer, and BGPPeer). The admin cluster then reconciles the changes to the user cluster. If you edit these resources on the user cluster directly, the admin cluster overwrites your changes in subsequent reconciliations.

### Control plane

Control plane BGP-peering information can be updated in the `Cluster` resource. You may add or remove peers specified in the control plane load balancing section.

**Warning:** Be careful when updating the control plane BGP peering information, particularly for self-managed clusters (clusters of type admin, hybrid, or standalone). The control plane VIP and Kubernetes control plane become inaccessible from outside the cluster if the cluster isn't able to advertise the control plane VIP to any of the peers. For example, access is lost if the peering configuration doesn't reference a valid peer, or if the cluster isn't able to connect to the peer due to misconfiguration or network issues. For instructions about how to recover access, see Recovering access to the control plane VIP for self-managed clusters.

The following sections outline the best practices for updating your control plane BGP peering information.

#### Check peer status before updating

To minimize the risk of misconfiguring peers, check that control plane BGP peering sessions are in the expected state before making changes. For example, if you expect that all BGP peering sessions are up, then verify that all `bgp-advertiser` Pods report `ready`, indicating that the sessions are up. If the current status doesn't match what you expect, then fix the issue before updating a peer configuration.

For information about retrieving control plane BGP session details, see Control plane BGP sessions.

#### Update peers in a controlled manner

Update one peer at a time, if possible, to help isolate possible problems:

  1. Add or update a single peer.
  2. Wait for the configuration to reconcile.
  3. Verify that the cluster is able to connect to the new or updated peer.
  4. Remove the old or unneeded peers.



### Services

To update address pools and load balancer node settings, edit `nodePoolSpec` in the `Cluster` resource.

**Warning:** Be careful when updating the peering information for data plane services. If the peering information is misconfigured and the cluster can't establish BGP sessions to the peers and advertise the VIPs, then clients can't access services through the LoadBalancer VIPs. We recommend that you update your configuration one peer at a time, as described in the previous section, to minimize the risk of misconfiguration.

To modify the BGP peering configuration after your cluster has been created, edit the `NetworkGatewayGroup` and `BGPLoadBalancer` custom resources. Any modifications to the peering information in these custom resources are reflected in the configuration of the load-balancing solution in the target cluster.

Make updates in the source resources in the cluster namespace in the admin cluster only. Any modifications made to the resources in the target (user) cluster are overwritten.

## Troubleshooting

The following sections describe how to access troubleshooting information for bundled load balancing with BGP.

### Control plane BGP sessions

The control plane BGP-peering configuration is validated with preflight checks during cluster creation. The preflight checks attempt to:

  * Establish a BGP connection with each peer.
  * Advertise the control plane VIP.
  * Verify that the control plane node can be reached, using the VIP.



If your cluster creation fails preflight checks, then review the preflight check logs for errors. Datestamped preflight check log files are located in the `baremetal/bmctl-workspace/CLUSTER_NAME/log` directory.

At runtime, the control plane BGP speakers run as static pods on each control plane node and write event information to logs. These static pods include "bgpadvertiser" in their name, so use the following `kubectl get pods` command to view the status of the BGP speaker Pods:
    
    
    kubectl -n kube-system get pods | grep bgpadvertiser
    

**Note:** The control plane `bgpadvertiser` Pods' Readiness condition is tied to the the status of their BGP sessions. This means that a pod is declared Ready only when all of its BGP sessions are up. If one of the pod's BGP sessions goes down, then the pod's Ready condition will change to False.

When the Pods are operating properly, the response looks something like the following:
    
    
    bgpadvertiser-node-01                            1/1     Running   1          167m
    bgpadvertiser-node-02                            1/1     Running   1          165m
    bgpadvertiser-node-03                            1/1     Running   1          163m
    

Use the following command to view the logs for the `bgpadvertiser-node-01` Pod:
    
    
    kubectl -n kube-system logs bgpadvertiser-node-01
    

### Services BGP sessions

The `BGPSession` resource provides information about current BGP sessions. To get session information, first get the current sessions, then retrieve the `BGPSession` resource for one of the sessions.

Use the following `kubectl get` command to list the current sessions:
    
    
    kubectl -n kube-system get bgpsessions
    

The command returns a list of sessions like the following example:
    
    
    NAME                 LOCAL ASN   PEER ASN   LOCAL IP     PEER IP      STATE            LAST REPORT
    10.0.1.254-node-01   65500       65000      10.0.1.178   10.0.1.254   Established      2s
    10.0.1.254-node-02   65500       65000      10.0.3.212   10.0.1.254   Established      2s
    10.0.3.254-node-01   65500       65000      10.0.1.178   10.0.3.254   Established      2s
    10.0.3.254-node-02   65500       65000      10.0.3.212   10.0.3.254   Established      2s
    

Use the following `kubectl describe` command to get the `BGPSession` resource for the `10.0.1.254-node-01` BGP session:
    
    
    kubectl -n kube-system describe bgpsession 10.0.1.254-node-01
    

The `BGPSession` resource returned should look something like the following example:
    
    
    Name:         10.0.1.254-node-01
    Namespace:    kube-system
    Labels:       <none>
    Annotations:  <none>
    API Version:  networking.gke.io/v1
    Kind:         BGPSession
    Metadata:
     (omitted)
    Spec:
      Floating IP:  10.0.1.178
      Local ASN:    65500
      Local IP:     10.0.1.178
      Node Name:    node-01
      Peer ASN:     65000
      Peer IP:      10.0.1.254
    Status:
      Advertised Routes:
        10.0.4.1/32
      Last Report Time:  2021-06-14T22:09:36Z
      State:             Established
    

Use the `kubectl get` command to get the `BGPAdvertisedRoute` resources:
    
    
    kubectl -n kube-system get bgpadvertisedroutes
    

The response, which should look similar to the following example, shows the routes being advertised:
    
    
    NAME                                    PREFIX           METRIC
    default-default-load-balancer-example   10.1.1.34/32
    default-gke-system-istio-ingress        10.1.1.107/32
    

Use `kubectl describe` to view details about which next hops each route is advertising.

### Recovering access to the control plane VIP for self-managed clusters

To regain access to the control plane VIP on an admin, hybrid, or standalone cluster, you must update the BGP configuration on the cluster. As shown in the following command sample, use SSH to connect to the node, then use `kubectl` to open the cluster resource for editing.
    
    
    ssh -i IDENTITY_FILE root@CLUSTER_NODE_IP
    
    kubectl --kubeconfig /etc/kubernetes/admin.conf edit -n CLUSTER_NAMESPACE cluster CLUSTER_NAME
    

Replace the following:

  * `IDENTITY_FILE`: the name of the SSH identity file that contains the identity key for public key authentication.
  * `CLUSTER_NODE_IP`: the IP address for the cluster node.
  * `CLUSTER_NAMESPACE`: the namespace of the cluster.
  * `CLUSTER_NAME`: the name of the cluster.



Modify the BGP peering configuration in the cluster object. After saving the new cluster configuration, monitor the health of the `bgpadvertiser` pods. If the configuration works, then the pods restart and become healthy once they connect to their peers.

### Manual BGP verification

This section contains instructions for manually verifying your BGP configuration. The procedure sets up a long-running BGP connection so that you can further debug the BGP configuration with your network team. Use this procedure to verify your configuration before you create a cluster or use it if BGP-related preflight checks fail.

Preflight checks automate the following BGP verification tasks:

  * Set up a BGP connection to a peer.
  * Advertise the control plane VIP.
  * Verify that traffic sent from all other cluster nodes to the VIP reaches the current load balancer node.



These tasks are run for each BGP peer on each control plane node. Passing these checks is critical when creating a cluster. The preflight checks, however, don't create long-running connections, so debugging a failure is difficult.

The following sections provide instructions to set up a BGP connection and advertise a route from a single cluster machine to one peer. To test multiple machines and multiple peers, repeat the instructions again, using a different machine and peer combination.

Remember that BGP connections are established from the control plane nodes, so be sure to test this procedure from one of your planned control plane nodes.

#### Obtain the BGP test program binary

Run the steps in this section on your admin workstation. These steps get the `bgpadvertiser` program that is used to test BGP connections and copy it to control plane nodes where you want to test.

  1. Pull the ansible-runner docker image.

###  Without Registry Mirror 

If you don't use a registry mirror, run the following commands to pull the ansible-runner docker image:
         
         gcloud auth login
         gcloud auth configure-docker
         docker pull gcr.io/anthos-baremetal-release/ansible-runner:1.10.0-gke.13
         

###  With Registry Mirror 

If you use a registry mirror, run the following commands to pull the ansible-runner docker image:
         
         docker login REGISTRY_HOST
         docker pull REGISTRY_HOST/anthos-baremetal-release/ansible-runner:1.10.0-gke.13
         

Replace REGISTRY_HOST with the name of your registry mirror server.

  2. To extract the `bgpadvertiser` binary.

###  Without Registry Mirror 

To extract the `bgpadvertiser` binary, run the following command:
         
         docker cp $(docker create gcr.io/anthos-baremetal-release/ansible-runner:1.10.0-gke.13):/bgpadvertiser .
         

###  With Registry Mirror 

To extract the `bgpadvertiser` binary, run the following command:
         
         docker cp $(docker create REGISTRY_HOST/anthos-baremetal-release/ansible-runner:1.10.0-gke.13):/bgpadvertiser .
         

  3. To copy the `bgpadvertiser` binary to the control plane node that you want to test with, run the following command:
         
         scp bgpadvertiser USERNAME>@CP_NODE_IP:/tmp/
         

Replace the following:

     * `USERNAME`: the username that you use to access the control plane node.

     * `CP_NODE_IP`: the IP address of the control plane node.




#### Set up a BGP connection

Run the steps in this section on a control plane node.

  1. Create a configuration file on the node at `/tmp/bgpadvertiser.conf` that looks like the following:
         
         localIP: NODE_IP
         localASN: CLUSTER_ASN
         peers:
         - peerIP: PEER_IP
           peerASN: PEER_ASN
         

Replace the following:

     * `NODE_IP`: IP address of the control plane node that you're on.
     * `CLUSTER_ASN`: the autonomous system number used by the cluster.
     * `PEER_IP`: the IP address of one of the external peers you want to test.
     * `PEER_ASN`: the autonomous system number for the network that contains the external peer device.
  2. Run the `bgpadvertiser` daemon, substituting the control plane VIP in the following command:
         
         /tmp/bgpadvertiser --config /tmp/bgpadvertiser.conf --advertise-ip CONTROL_PLANE_VIP
         

Replace `CONTROL_PLANE_VIP` with the IP address that you're going to use for your control plane VIP. This command causes the BGP advertiser to advertise this address to the peer.

  3. View the program output.

At this point, the `bgpadvertiser` daemon starts up, attempts to connect to the peer, and advertises the VIP. The program periodically prints messages (see the following sample output) that include `BGP_FSM_ESTABLISHED` when the BGP connection is established.
         
         {"level":"info","ts":1646788815.5588224,"logger":"BGPSpeaker","msg":"GoBGP gRPC debug endpoint disabled","localIP":"21.0.101.64"}
         {"level":"info","ts":1646788815.5596201,"logger":"BGPSpeaker","msg":"Started.","localIP":"21.0.101.64"}
         I0309 01:20:15.559667 1320826 main.go:154] BGP advertiser started.
         I0309 01:20:15.561434 1320826 main.go:170] Health status HTTP server started at "127.0.0.1:8080".
         INFO[0000] Add a peer configuration for:21.0.101.80      Topic=Peer
         {"level":"info","ts":1646788815.5623345,"logger":"BGPSpeaker","msg":"Peer added.","localIP":"21.0.101.64","peer":"21.0.101.80/4273481989"}
         DEBU[0000] IdleHoldTimer expired                         Duration=0 Key=21.0.101.80 Topic=Peer
         I0309 01:20:15.563503 1320826 main.go:187] Peer applied: {4273481989 21.0.101.80}
         DEBU[0000] state changed                                 Key=21.0.101.80 Topic=Peer new=BGP_FSM_ACTIVE old=**BGP_FSM_IDLE** reason=idle-hold-timer-expired
         DEBU[0000] create Destination                            Nlri=10.0.0.1/32 Topic=Table
         {"level":"info","ts":1646788815.5670514,"logger":"BGPSpeaker","msg":"Route added.","localIP":"21.0.101.64","route":{"ID":0,"Metric":0,"NextHop":"21.0.101.64","Prefix":"10.0.0.1/32","VRF":""}}
         I0309 01:20:15.568029 1320826 main.go:199] Route added: {0 0 21.0.101.64 10.0.0.1/32 }
         I0309 01:20:15.568073 1320826 main.go:201] BGP advertiser serving...
         DEBU[0005] try to connect                                Key=21.0.101.80 Topic=Peer
         DEBU[0005] state changed                                 Key=21.0.101.80 Topic=Peer new=BGP_FSM_OPENSENT old=BGP_FSM_ACTIVE reason=new-connection
         DEBU[0005] state changed                                 Key=21.0.101.80 Topic=Peer new=BGP_FSM_OPENCONFIRM old=BGP_FSM_OPENSENT reason=open-msg-received
         INFO[0005] Peer Up                                       Key=21.0.101.80 State=BGP_FSM_OPENCONFIRM Topic=Peer
         DEBU[0005] state changed                                 Key=21.0.101.80 Topic=Peer new=**BGP_FSM_ESTABLISHED** old=BGP_FSM_OPENCONFIRM reason=open-msg-negotiated
         DEBU[0005] sent update                                   Key=21.0.101.80 State=**BGP_FSM_ESTABLISHED** Topic=Peer attributes="[{Origin: i} 4273481990 {Nexthop: 21.0.101.64}]" nlri="[10.0.0.1/32]" withdrawals="[]"
         DEBU[0006] received update                               Key=21.0.101.80 Topic=Peer attributes="[{Origin: i} 4273481989 4273481990 {Nexthop: 21.0.101.64}]" nlri="[10.0.0.1/32]" withdrawals="[]"
         DEBU[0006] create Destination                            Nlri=10.0.0.1/32 Topic=Table
         DEBU[0035] sent                                          Key=21.0.101.80 State=**BGP_FSM_ESTABLISHED** Topic=Peer data="&{{[] 19 4} 0x166e528}"
         DEBU[0065] sent                                          Key=21.0.101.80 State=**BGP_FSM_ESTABLISHED** Topic=Peer data="&{{[] 19 4} 0x166e528}"
         




If you don't see these messages, then double-check the BGP configuration parameters in the config file and verify with the network administrator. Now you have a BGP connection set up. You can verify with the network administrator that they see the connection established on their side and that they see the route advertised to them.

#### Traffic test

To test that the network can forward traffic to the VIP, you must add the VIP to your control plane node that's running `bgpadvertiser`. Run the following command in a different terminal so you can leave the `bgpadvertiser` running:

  1. Add the VIP to your control plane node:
         
         ip addr add CONTROL_PLANE_VIP/32 dev INTF_NAME
         

Replace the following:

     * `CONTROL_PLANE_VIP`: the VIP `--advertise-ip` argument of the `bgpadvertiser`.
     * `INTF_NAME`: the Kubernetes interface on the node. That is, the interface that has the IP address that you put in the Google Distributed Cloud configuration for `loadBalancer.bgpPeers.controlPlaneNodes`.
  2. Ping the VIP from a different node:
         
         ping CONTROL_PLANE_VIP
         

If the ping does not succeed, then there may be an issue with the BGP configuration on the network device. Work with your network administrator to verify the configuration and resolve the issue.




#### Clean up

Be sure to follow these steps to reset the node after you've manually verified that BGP is working. If you don't reset the node properly, the manual setup may interfere with the preflight check or subsequent cluster creation.

  1. Remove the VIP from the control plane node if you added it for the traffic test:
         
         ip addr del CONTROL_PLANE_VIP/32 dev INTF_NAME
         

  2. On the control plane node, press `Ctrl`+`C` in the `bgpadvertiser` terminal to stop the bgpadvertiser.

  3. Verify that no `bgpadvertiser` processes are running:
         
         ps -ef | grep bgpadvertiser
         

  4. If you see processes running, then stop them using the `kill` command.




## BGP Selector Limitation with Cloud API/Terraform

When you manage Google Distributed Cloud clusters using the GKE On-Prem API (Terraform, the Google Cloud console, or `gcloud` CLI), you cannot specify BGP selectors in the cluster configuration. If your cluster uses BGP load balancing and Egress NAT, BGP peering can fail.

### Workaround

To perform manual overrides, you must set the load balancer configuration to "unmanaged" in the admin cluster. This setting prevents the GKE On-Prem API from automatically reconciling changes to the load balancer.

  1. Enforce IP anti-affinity: Split your BGP `NetworkGatewayGroup` into separate `NetworkGatewayGroup` resources (one per floating IP) and use `nodeSelector` in each `NetworkGatewayGroup` to pin the floating IP to a specific physical node. This prevents multiple BGP IPs from landing on the same node.
  2. Unmanage the load balancer: In the admin cluster, remove the `baremetal.cluster.gke.io/managed: "true"` annotation from the `BGPLoadBalancer` resource in the user cluster's namespace. This stops the GDC controllers from reverting your manual changes.
  3. Patch BGPPeer resources: Manually patch the `BGPPeer` resources in the admin cluster to add the `selectors` block referencing the correct `NetworkGatewayGroup` resources and floating IPs. These changes sync to the user cluster and stabilize BGP sessions.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
