---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/egress-nat-gateway/
title: Configuring an egress NAT gateway \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:48.059495+00:00
---

# Configuring an egress NAT gateway  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/egress-nat-gateway/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Configuring an egress NAT gateway Stay organized with collections  Save and categorize content based on your preferences. 

With Google Distributed Cloud, you can configure source network address translation (SNAT) so that certain egress traffic from your user cluster is given a predictable source IP address.

This document shows how to configure an egress NAT gateway for a user cluster.

**Caution:** You can't upgrade any version 1.8.x or 1.9.x cluster that has Anthos Network Gateway enabled to any later version. For example, you cannot upgrade a version 1.9.0 cluster that has Anthos Network Gateway enabled to version 1.9.x, nor can you upgrade it to version 1.10. You can only upgrade clusters that have Anthos Network Gateway enabled if they were created in version 1.10 or later. You can delete a version 1.8.x or version 1.9.x cluster, and then recreate it following the instructions in this document.

## Introduction

Sometimes you have Pods running in a user cluster that need to send packets to components running in your organization, but outside of the cluster. You might want to design those external components so that they filter incoming network traffic according to a set of well-known source IP addresses.

Here are some scenarios:

  * You have a firewall in front of a database that allows access only by IP address. And the team that manages the database firewall is different from the team that manages the user cluster.

  * Workloads in your user cluster have to access a third-party API over the internet. For security reasons, the API provider authenticates and authorizes traffic by using IP address as the identity.




With an egress NAT gateway, you can have fine-grained control over the source IP addresses used for network traffic that leaves a cluster.

## How an egress NAT gateway works

Ordinarily, when a Pod sends a packet out of the cluster, the packet is SNAT translated with the IP address of the node where the Pod is running.

When an egress NAT gateway is in place, you can specify that certain outbound packets should be sent first to a dedicated gateway node. The network interface on the gateway node is configured with two IP addresses: the primary IP address and an egress source IP address.

When a packet has been selected to use the egress NAT gateway, the packet leaves the cluster from the gateway node and is SNAT translated with the egress source IP address that is configured on the network interface.

The following diagram illustrates the packet flow:

[ ![Packet flow with an egress NAT gateway in place.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/egress-nat-gateway.svg)](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/egress-nat-gateway.svg)

The preceding diagram, you can see the flow of a packet that is sent from the Pod.

  1. On a node with IP address 192.168.1.1, a Pod with IP address 10.10.10.1 generates an outbound packet.

  2. The packet matches an egress rule, so the packet is forwarded to the gateway node.

  3. The gateway node changes the source IP address to 192.168.1.100 and sends the packet out of the cluster.

  4. Return traffic comes back to the gateway node with destination 192.168.1.100.

  5. The gateway node uses conntrack to modify the destination IP address to 10.10.10.1.

  6. The packet is treated as in-cluster traffic and forwarded to the original node and delivered back to the original Pod.




## Personas

This topic refers to two personas:

  * **Cluster administrator.** This person creates a user cluster and specifies floating IP addresses to be used by Anthos Network Gateway.

  * **Developer.** This person runs workloads on the user cluster and creates egress policies.




## Enable egress NAT gateway

This section is for cluster administrators.

To configure an egress NAT gateway, use the `enableDataplaneV2` and `advancedNetworking` fields in the user cluster configuration file, and create one or more NetworkGatewayGroup objects.

In your cluster configuration file, set these fields to `true`:
    
    
    enableDataplaneV2: true
    ...
    advancedNetworking: true
    

[Create the user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-user-cluster).

## Specify floating IP addresses

This section is for cluster administrators.

Choose a set of IP addresses that you would like to use as egress source addresses. These are called _floating IP addresses_ , because Network Gateway Group assigns them, as needed, to the network interfaces of nodes that it chooses to be egress gateways.

Your floating IP addresses must be in the same subnet as your node IP addresses.

Your set of floating IP addresses must not overlap with the set of IP addresses you have specified for your nodes.

For example, suppose a subnet has the address range 192.168.1.0/24. And suppose you have chosen to use 192.168.1.1 through 192.168.1.99 for nodes. Then you could use 192.168.1.100 through 192.168.1.104 as floating IP addresses.

## Create a NetworkGatewayGroup object

This section is for cluster administrators.

Here's an example of a manifest for a NetworkGatewayGroup object:
    
    
    kind: NetworkGatewayGroup
    apiVersion: networking.gke.io/v1
    metadata:
      namespace: kube-system
      name: default
    spec
      floatingIPs:
      - 192.168.1.100
      - 192.168.1.101
      - 192.168.1.102
      - 192.168.1.103
      - 192.168.1.104
    

Replace the `floatingIPs` array with your floating IP addresses, and save the manifest in a file named `my-ngg.yaml`.

Create the NetworkGatewayGroup object:
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG apply -f my-ngg.yaml
    

## Example of an egress NAT policy

This section is for developers.

Here's an example of an EgressNatPolicy custom resource:
    
    
    kind: EgressNATPolicy
    apiVersion: networking.gke.io/v1
    metadata:
      name: alice-paul
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
    

In the preceding manifest, we see:

  * A Pod is a candidate for egress NAT if it satisfies one the following:

    * The Pod has the label `role: frontend`, and the Pod is in a namespace that has the label `user: alice`.

    * The Pod has the label `role: frontend`, and the Pod is in a namespace that has the label `user: paul`.

  * Traffic from a candidate Pod to an address in the 8.8.8.0/24 range is sent to the egress NAT gateway.

  * The `gatewayRef` section determines the egress source IP address. The EgressNATPolicy custom resource uses the `gatewayRef.name` and `gatewayRef.namespace` values to find a NetworkGatewayGroup object. The policy uses one of the NetworkGatewayGroup's floating IP addresses as the source IP address for egress traffic. If there are multiple floating IP addresses in the matching NetworkGatewayGroup, the policy uses the first IP address in the `floatingIPs` list, and ignores any other IP addresses. If there are invalid fields in the `gatewayRef` section, this will result in an a failure to apply the EgressNATPolicy object.




## Create an EgressNATPolicy object

Create your own EgressNATPolicy manifest. Set `metadata.name` to `"my-policy"`. Save your manifest in a file named `my-policy.yaml`.

Create the EgressNatPolicy object:
    
    
    kubectl apply --kubeconfig USER_CLUSTER_KUBECONFIG -f my-policy.yaml
    

## View information about your egress NAT policy
    
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get egressnatpolicy my-policy --output yaml
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG get networkgatewaygroup --namespace kube-system --output yaml
    
    kubectl --kubeconfig USER_CLUSTER_KUBECONFIG describe egressnatpolicy my-policy
    

## Order of operations

Egress NAT policy is compatible with network policy APIs. Network policy is evaluated before egress NAT policy. If a network policy says to drop a packet, the packet is dropped regardless of the egress NAT policy.

## Multiple egress policies

As described previously, each EgressNATPolicy uses the first IP address in the `floatingIPs` list from the NetworkGatewayGroup that matches `gatewayRef.name` and `gatewayRef.namespace`. If you create multiple policies and intend to use different IP addresses, you need to create multiple NetworkGatewayGroup objects, and refer to them respectively. If you create multiple policies, the `gatewayRef` object must be unique for each policy.

Each `NetworkGatewayGroup` resource must contain unique floating IP addresses. To configure multiple `EgressNATPolicy` objects to use the same IP address, use the same `gatewayRef.name` and `gatewayRef.namespace` for both.

**Note:** Anthos Network Gateway doesn't let you create new gateway objects that contain IP addresses in `spec.floatingIPs` that are already used in existing gateway objects. This rule is enforced by a webhook in Google Distributed Cloud version 1.15.0 and higher.

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
           name: egresspolicy1
         spec:
           ...
           gatewayRef:
             name: gateway1
             namespace: kube-system
         ---
         kind: EgressNATPolicy
         apiVersion: networking.gke.io/v1
         metadata:
           name: egresspolicy2
         spec:
           ...
           gatewayRef:
             name: gateway2
             namespace: kube-system
         ---
         kind: EgressNATPolicy
         apiVersion: networking.gke.io/v1
         metadata:
           name: egresspolicy3
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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
