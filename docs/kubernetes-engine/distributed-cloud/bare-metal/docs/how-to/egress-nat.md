---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/egress-nat/
title: Configure an egress NAT gateway \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:29.721583+00:00
---

# Configure an egress NAT gateway  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/egress-nat/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Configure an egress NAT gateway Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to set up an egress NAT gateway for Google Distributed Cloud. This gateway provides persistent, deterministic SNAT IP addresses for the egress traffic from your clusters. When you run workloads that have egress user traffic (outside of your clusters), your customers want to identify this traffic by using a few deterministic IP addresses. This allows your customers to establish IP-based security measures, like allowlisting policies.

This page is for Networking specialists who design and architect the network for their organization, and install, configure, and support network equipment. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

The egress NAT gateway is enabled using two custom resources. For a given namespace, the `NetworkGatewayGroup` custom resource specifies floating IP addresses that can be configured on the network interface of a Node that is chosen to act as a gateway. The `EgressNatPolicy` custom resource lets you specify egress routing policies to control the traffic on the egress gateway.

If you don't set up an egress NAT gateway, or if egress traffic doesn't meet traffic selection rules, egress traffic from a given Pod to a destination outside your cluster is masqueraded to the IP address of the node where the Pod is running. In this scenario, there is no guarantee that all egress traffic from a particular Pod will have the same source IP address or will masquerade to the same Node IP address.

Egress NAT gateway is an advanced networking offering built on top of [Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2).

**Note:** If your nodes run Ubuntu 18.04, the Linux kernel must be version 5.4 or higher. For more information, see [Configure Ubuntu](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-os/ubuntu).

## How the egress NAT gateway works

The egress traffic selection logic is based on a namespace selector, a Pod selector, and a set of destination IP address ranges in CIDR block notation. To illustrate how the egress NAT gateway works, consider the flow of a packet from a Pod to an external consumer and the corresponding response. Assume the Node subnet has IP addresses in the 192.168.1.0/24 CIDR block.

The following diagram shows the network architecture for egress traffic through a gateway node.

![Egress NAT gateway diagram for Google Distributed Cloud](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/images/egress-nat-gateway.svg)

The packet flow through the egress NAT gateway might look like this:

  1. Egress traffic is generated from a Pod with IP address `10.10.10.1` in a Node with IP address `192.168.1.1`.

The traffic's destination address is an endpoint outside of the cluster.

  2. If the traffic matches an egress rule, the eBPF program routes the egress traffic to the gateway Node, instead of directly masquerading with the Node IP address.

  3. The gateway Node receives the egress traffic.

  4. The gateway node masquerades the originating traffic's source IP address, `10.10.10.1`, with the source egress IP address, `192.168.1.100` specified in the `EgressNATPolicy` custom resource.

  5. Return traffic comes back to the gateway Node with destination as `192.168.1.100`.

  6. The gateway node matches the conntrack of the return traffic with that of the original egress traffic and rewrites the destination IP address as `10.10.10.1`.

  7. `10.10.10.1` is treated as in-cluster traffic, routed to the original Node, and delivered back to the original Pod.




## Configure floating IP addresses for Node traffic

The Network Gateway Group custom resource is a bundled component of Google Distributed Cloud. The resource manages a list of one or more floating IP addresses to use for egress traffic from Nodes in your cluster. Participating Nodes are determined by the specified namespace. The Network Gateway Group makes a floating IP address available at all times on a best-effort basis. If a Node using a floating IP address goes down, the advanced network operator moves the assigned IP address to the next available Node. All workload egress traffic using that IP address will move as well.

Include the Network Gateway Group details (annotation and spec) in the cluster configuration file when you create a new 1.36.100-gke.144 cluster.

### Create the `NetworkGatewayGroup` custom resource

You enable the Network Gateway Group by setting the `spec.clusterNetwork.advancedNetworking` field to `true` in the cluster configuration file when you create a cluster as shown in the following example:
    
    
    apiVersion: baremetal.cluster.gke.io/v1
    kind: Cluster
    metadata:
      name: cluster1
      namespace: cluster-cluster1
    spec:
      clusterNetwork:
        ...
        advancedNetworking: true
        ...
    

When you create the `NetworkGatewayGroup` custom resource, set its namespace to the cluster namespace and specify a list of floating IP addresses, as shown in the following example:

**Note:** The cluster operator creates a copy of the `NetworkGatewayGroup` custom resource in the `kube-system` namespace. This copy of the `NetworkGatewayGroup` custom resource in the `kube-system` namespace is responsible for defining the floating IP addresses that are used by the advanced networking operator.
    
    
    kind: NetworkGatewayGroup
    apiVersion: networking.gke.io/v1
    metadata:
      namespace: cluster-cluster1
      name: default
    spec:
      floatingIPs:
      - 192.168.1.100
      - 192.168.1.101
      - 192.168.1.102
    

**Note:** The egress NAT gateway doesn't support a high availability (HA) configuration. If the network gateway node handling the floating IP address goes down or has connectivity issues, egress traffic may be interrupted for short periods of time. The advanced networking operator automatically reassigns the floating IP address to a new node to restore egress traffic.

The advanced networking operator assigns the floating IPs to Nodes based on the following criteria:

  * Node subnet: the floating IP address has to match Node's subnet.
  * Node role (control plane, worker): worker Nodes take precedence over control plane Nodes when assigning floating IP addresses.
  * Whether a Node has a floating IP address: the operator prioritizes assignments to Nodes that don't have a floating IP assigned already.



The address to node mapping can be found in the `status` section when you get the `NetworkGatewayGroup` object. Note that the `NetworkGatewayGroup` object is in the `kube-system` namespace. If a gateway node is down, the advanced network operator assigns the floating IP addresses to the next available Node.

### Verify the gateway configuration

After you have applied your gateway configuration changes, you can use `kubectl` to check the status of the gateway and retrieve the floating IP addresses specified for the gateway.

Use the following command to check the status of the `NetworkGatewayGroup` and see how the floating IP addresses are allocated:
    
    
    kubectl -n kube-system get networkgatewaygroups.networking.gke.io default -o yaml

The response for a cluster with two nodes, `worker1` and `worker2` might look like this:
    
    
    kind: NetworkGatewayGroup
    apiVersion: networking.gke.io/v1
    metadata:
      namespace: kube-system
      name: default
    spec:
      floatingIPs:
      - 192.168.1.100
      - 192.168.1.101
      - 192.168.1.102
    status:
      nodes:
        worker1: Up
        worker2: Up // Or Down
      floatingIPs:
        192.168.1.100: worker1
        192.168.1.101: worker2
        192.168.1.102: worker1
    

## Set traffic selection rules

The `EgressNATPolicy` custom resource specifies traffic selection rules and assigns a deterministic IP address for egress traffic that leaves the cluster. When specifying the custom resource, `egress` (with at least one rule), `destinationCIDRs`, and `egressSourceIP` are all required.

**Note:** It's possible to set traffic selection rules that specify an `egressSourceIP` address that's already in use for another `EgressNATPolicy` object. This may cause egress traffic routing conflicts. Coordinate with your development team to determine which floating IP addresses are available for use before specifying the `egressSourceIP` address in your `EgressNATPolicy` custom resource.

Use `kubectl apply` to create the `EgressNATPolicy` custom resource. The following sections provide details and examples for defining the specification.

### Specify egress routing rules

The `EgressNatPolicy` custom resource lets you specify the following rules for egress traffic:

  * You must specify one or more egress traffic selection rules in the `egress` section.

    * Each rule consists of a `podSelector` and a `namespaceSelector`.
    * Selection is based on a namespace label, `namespaceSelector.matchLabels.**user**`, and a Pod label, `podSelector.matchLabels.**role**`.
    * If a Pod matches any of the rules (matching uses an OR relationship), it is selected for egress traffic.
  * Specify allowed destination addresses in the `destinationCIDRs` section.

    * `destinationCIDRs` takes a list of CIDR blocks.
    * If outgoing traffic from a Pod has a destination IP address that falls within the range of any of the specified CIDR blocks, it is selected for egress traffic.



In the following example, egress traffic from a Pod is permitted when the following criteria are met:

  * Pod is labeled with `role: frontend`.
  * Pod is in a namespace labeled as either `user: alice` or `user: paul`.
  * Pod is communicating to IP addresses in the `8.8.8.0/24` CIDR block.


    
    
    kind: EgressNATPolicy
    apiVersion: networking.gke.io/v1
    metadata:
      name: egress
    spec:
      sources:
      - namespaceSelector:
          matchLabels:
            user: alice
        podSelector:
          matchLabels:
            role: frontend
      - namespaceSelector:
          matchLabels:
            user: paul
        podSelector:
          matchLabels:
            role: frontend
      action: SNAT
      destinations:
        - cidr: 8.8.8.0/24
      gatewayRef:
        name: default
        namespace: kube-system
    

For more information about using labels, refer to [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/) in the Kubernetes documentation.

### Get a source IP address for egress traffic

The `EgressNATPolicy` custom resource (policy) uses the `gatewayRef.name` and `gatewayRef.namespace` values to find a `NetworkGatewayGroup` object (gateway). The policy uses one of the gateway's floating IP addresses as the source IP address for egress traffic. If there are multiple floating IP addresses in the matching gateway, the policy uses the first IP address in the `floatingIPs` list and ignores any other IP addresses. For the example gateway, the first address in the `floatingIPs` list is `192.168.1.100`. Having invalid fields or values in the `gatewayRef` section will result in failure to apply the policy object.

### Multiple egress policies and multiple gateway objects

As described in the previous section, each `egressNATPolicy` object (policy) uses the first IP address in the `floatingIPs` list from the gateway object that matches `gatewayRef.name` and `gatewayRef.namespace`. You can create multiple policies and, if you intend to use different IP addresses, you need to create multiple `NetworkGatewayGroup` objects and refer to them respectively.

Each `NetworkGatewayGroup` resource must contain unique floating IP addresses. To configure multiple `EgressNATPolicy` objects to use the same IP address, use the same `gatewayRef.name` and `gatewayRef.namespace` for both. 

**Note:** Network Gateway for GDC doesn't let you create new gateway objects that contain IP addresses in `spec.floatingIPs` that are already used in existing gateway objects. This rule is enforced by a webhook.

To set up multiple egress policies and multiple gateway objects:

  1. Create gateway objects in the `kube-system` namespace to manage each floating IP address. Typically, each egress policy should have a corresponding gateway object to ensure the correct IP address is allocated.

Then verify each gateway object with `kubectl` to get the allocation status of the floating IP addresses:
         
         kind: NetworkGatewayGroup
         apiVersion: networking.gke.io/v1
         metadata:
           namespace: kube-system
           name: gateway1
         spec:
           floatingIPs:
           - 192.168.1.100
         status:
           ...
           floatingIPs:
             192.168.1.100: worker1
         ---
         kind: NetworkGatewayGroup
         apiVersion: networking.gke.io/v1
         metadata:
           namespace: kube-system
           name: gateway2
         spec:
           floatingIPs:
           - 192.168.1.101
         status:
           ...
           floatingIPs:
             192.168.1.101: worker2
         ---
         kind: NetworkGatewayGroup
         apiVersion: networking.gke.io/v1
         metadata:
           namespace: kube-system
           name: gateway3
         spec:
           floatingIPs:
           - 192.168.1.102
         status:
           ...
           floatingIPs:
             192.168.1.102: worker1
         

  2. Create multiple policies that refer to the gateway objects, such as `gateway1` created in the preceding step:
         
         kind: EgressNATPolicy
         apiVersion: networking.gke.io/v1
         metadata:
           name: egress1
         spec:
           ...
           gatewayRef:
             name: gateway1
             namespace: kube-system
         ---
         kind: EgressNATPolicy
         apiVersion: networking.gke.io/v1
         metadata:
           name: egress2
         spec:
           ...
           gatewayRef:
             name: gateway2
             namespace: kube-system
         ---
         kind: EgressNATPolicy
         apiVersion: networking.gke.io/v1
         metadata:
           name: egress3
         spec:
           ...
           gatewayRef:
             name: gateway3
             namespace: kube-system
         




### (Optional) Specify nodes to place floating IP addresses on

`NetworkGatewayGroup` resources support node selectors. To specify a subset of nodes that are considered for hosting a floating IP address, you can add the node selector to the `NetworkGatewayGroup` object as shown in the following sample:
    
    
    kind: NetworkGatewayGroup
    apiVersion: networking.gke.io/v1
    metadata:
      namespace: cluster-cluster1
      name: default
    spec:
      floatingIPs:
      - 192.168.1.100
      - 192.168.1.101
      - 192.168.1.102**  nodeSelector:
        node-type: "egressNat"**
    

The node selector matches to nodes that have the specified label and only these nodes are considered for hosting a floating IP address. If you specify multiple selectors, their logic is additive, so a node has to match every label to be considered for hosting a floating IP address. If there aren't many nodes with matching labels, a node selector can reduce the high availability (HA) qualities of floating IP address placement.

### Fast failover for a high availability egress NAT gateway

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For version 1.34 and higher clusters, you can configure the egress NAT gateway with fast failover. When you have multiple floating IP addresses and you configure fast failover, it provides high availability egress. This feature provides better load distribution for egress traffic and faster failover to minimize downtime. Instead of relying on a single gateway node at a time (active-standby), the cluster distributes outbound traffic across multiple gateway nodes and all configured floating IP addresses in a `NetworkGatewayGroup` resource. 

This active-active model has the following main benefits:

  * **Load Distribution** : Outbound traffic from different source endpoints, such as Pods, spreads across all available gateway nodes, which reduces the load on any single node and increases the total available egress bandwidth.

  * **Fast Failover** : If an egress gateway node fails, traffic automatically redirects to the remaining healthy nodes. The goal is to have traffic failover quickly. While existing connections on the failed node drop, new connections immediately establish through other gateways, minimizing downtime.




#### Key differences

Configuring the egress NAT gateway for fast failover changes how the egress NAT gateway operates:

Capability | Active-standby (default) | Active-active (fast failover)  
---|---|---  
Floating IP usage | The `EgressNATPolicy` uses only the first floating IP address in the `NetworkGatewayGroup`. | All floating IP addresses listed in the `NetworkGatewayGroup` actively distribute egress traffic.  
Failover | If the gateway node fails, the same floating IP address moves to a different node, which can cause traffic interruption. | If a gateway node fails, traffic redirects to a different, healthy IP address on another node. New connections immediately route through the healthy gateways, while existing stateful connections on the failed node terminate.  
Traffic | All traffic for a given policy goes through a single gateway node. | Traffic distributes across multiple gateway nodes based on a consistent hashing of the source endpoint, such as a Pod.  
  
#### Configure fast failover

Configuring the feature involves two main steps:

  1. Specify multiple floating IP addresses.

Configure the `NetworkGatewayGroup` with a pool of at least two floating IP addresses to realize the benefits of high availability and load distribution. Using more floating IP addresses improves egress reliability and throughput.

Here is a sample configuration:
         
         apiVersion: networking.gke.io/v1
         kind: NetworkGatewayGroup
         metadata:
           name: egress-gateways
           namespace: cluster-admin
         spec:
           nodeSelector:
             # Selects nodes that are designated as egress gateways
             node-role.kubernetes.io/egress: ""
           floatingIPs:
           - "192.168.1.100"
           - "192.168.1.101"
           - "192.168.1.102"
         

  2. To enable fast failover, add the `networking.gke.io/egressnat-ha: "enable"` annotation to the `EgressNATPolicy` custom resource:
         
         kind: EgressNATPolicy
         apiVersion: networking.gke.io/v1
         metadata:
           name: egress
           annotations:**    networking.gke.io/egressnat-ha: "enable"**
         spec:
           ...
         




### Egress traffic selection rules and network policies

The egress NAT gateway is compatible with network policy APIs. Network policies are assessed first and take precedence over the traffic selection rules of the egress NAT gateway. For example, if the egress traffic triggers a network policy resulting in the packet being dropped, egress gateway rules won't check the packet. Only when the network policy allows the packet to egress will the egress traffic selection rules be evaluated to decide how the traffic is handled, either using the egress NAT gateway or directly masquerading with the IP address of the Node where the Pod is running.

## Limitations

The current limitations for the egress NAT gateway include:

  * The egress NAT gateway is only enabled for IPv4 mode.

  * Egress IP addresses have to be in the same Layer 2 domain with Node IP addresses.

  * If you configure standard BGP load balancing alongside Egress NAT and use the GKE On-Prem API to manage your clusters (with Terraform, the Google Cloud console, or `gcloud` CLI), BGP peer selectors are not supported. This lack of support can cause BGP sessions to randomly use incorrect local IPs to peer, which leads to BGP peering failure. For a workaround, see [Configure bundled load balancers with BGP: BGP Selector Limitation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/lb-bundled-bgp#bgp-selector-limitation).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
