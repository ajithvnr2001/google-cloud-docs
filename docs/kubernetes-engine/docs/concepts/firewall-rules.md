---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules/
title: Automatically created firewall rules \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:31:49.872599+00:00
---

# Automatically created firewall rules  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Automatically created firewall rules Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes the ingress allow [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) that Google Kubernetes Engine (GKE) by default creates automatically in Google Cloud.

## Applicable firewalls and egress firewalls

GKE uses Virtual Private Cloud (VPC) firewall rules to control incoming and outgoing traffic to your Pods and nodes. By default, GKE automatically creates and manages certain firewall rules to allow essential traffic, such as communication between nodes and Pods, and traffic to your Kubernetes control plane. While GKE automatically creates ingress allow VPC firewall rules for LoadBalancer Services by default, you can disable this behavior to manage firewall rules or policies manually or utilize advanced firewall features.

Ingress allow firewall rules created by GKE aren't the only applicable firewall rules that apply to nodes in a cluster. The complete set of applicable firewall rules for ingress and egress is defined from rules in [hierarchical firewall policies](https://docs.cloud.google.com/firewall/docs/firewall-policies), [global network firewall policies](https://docs.cloud.google.com/firewall/docs/network-firewall-policies), [regional network firewall policies](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies), and other VPC firewall rules.

**Best practice** : 

Plan and design the configuration for your cluster, workloads and Services with your organization's Network administrators and Security engineers, and understand the firewall [policy and rule evaluation order](https://docs.cloud.google.com/firewall/docs/firewall-policies-rule-eval-order) so you know which firewall rules take precedence.

GKE only creates _ingress_ [VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) because GKE relies on the [implied allowed egress lowest-priority firewall rule](https://docs.cloud.google.com/firewall/docs/firewalls#default_firewall_rules).

If you've configured egress deny firewall rules in your cluster's VPC network, you might have to create egress allow rules to permit communication between nodes, Pods, and the cluster's control plane. For example, if you've created an egress deny firewall rule for all protocols and ports and all destination IP addresses, you must create egress allow firewall rules in addition to the ingress rules that GKE creates automatically. Connectivity to control plane endpoints always uses TCP destination port `443`, but connectivity among nodes and Pods of the cluster can use any protocol and destination port.

The following tools are useful to determine which firewall rules allow or deny traffic:

  * [Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests)
  * [Firewall policy rules logging](https://docs.cloud.google.com/firewall/docs/firewall-policy-rules-logging-overview)

**Note:** GKE-managed firewall rules only apply to resources where GKE manages firewall creation. If these rules are not present in your environment, your cluster networking is not affected by GKE's default firewall management behavior.

## Firewall rules

GKE by default creates firewall rules automatically when creating the following resources:

  * GKE clusters
  * GKE Services
  * GKE Gateways and HTTPRoutes
  * GKE Ingresses



Unless otherwise specified, the priority for all automatically created firewall rules is 1000, which is the [default value for firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#priority_order_for_firewall_rules). If you would like more control over firewall behavior, you can create firewall rules with a higher [priority](https://docs.cloud.google.com/vpc/docs/firewalls#priority_order_for_firewall_rules). Firewall rules with a higher priority are applied before automatically created firewall rules.

**Warning:** Don't modify or delete firewall rules created by GKE. Any manual changes to these rules might be reverted, which could lead to unexpected behavior in your clusters.**Note:** Evaluate all firewall rules applicable to the VM instances within a VPC, both ingress and egress. If you decide to block egress connections for clusters, you must ensure that appropriate firewall rules exist to allow nodes to communicate with the control plane on TCP port 443\. If you are using `Konnectivity` proxy and blocking all egress traffic, ensure there is a rule with higher priority that allows traffic on port 8132.

### GKE cluster firewall rules

GKE creates the following ingress firewall rules when creating a cluster:

Name | Purpose | Source | Target (defines the destination) | Protocol and ports | Priority  
---|---|---|---|---|---  
`gke-[cluster-name]-[cluster-hash]-master` |  For Autopilot and Standard clusters that rely on [ VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) for control plane private endpoint connectivity. Permits the control plane to access the kubelet and metrics-server on cluster nodes.  | Control plane IP address range (/28) | Node tag | TCP: 443 (metrics-server) and TCP: 10250 (kubelet) | 1000  
`gke-[cluster-name]-[cluster-hash]-vms` |  Used for intra-cluster communication required by the [Kubernetes networking model](https://kubernetes.io/docs/concepts/cluster-administration/networking/#the-kubernetes-network-model). Allows software running on nodes to send packets, with sources matching node IP addresses, to destination Pod IP and node IP addresses in the cluster. For example, traffic allowed by this rule includes:

  * Packets sent from system daemons, such as kubelet, to node and Pod IP address destinations of the cluster. 
  * Packets sent from software running in Pods with `hostNetwork:true` to node and Pod IP address destinations of the cluster. 

|  The node IP address range or a superset of this node IP address range: 

  * For [ auto mode VPC networks](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges), GKE uses the `10.128.0.0/9` CIDR because that range includes all current and future subnet primary IPv4 address ranges for the automatically created subnetworks. 
  * For [ custom mode VPC networks](https://docs.cloud.google.com/vpc/docs/vpc#subnet-ranges), GKE uses the primary IPv4 address range of the cluster's subnet. 

GKE does **not** update the source IPv4 range of this firewall rule if you [ expand the primary IPv4 range of the cluster's subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#expand-subnet). You must create the necessary ingress firewall rule manually if you expand the primary IPv4 range of the cluster's subnet.  | Node tag | TCP: 1-65535, UDP: 1-65535, ICMP | 1000  
`gke-[cluster-name]-[cluster-hash]-all` |  Permits traffic between all Pods on a cluster, as required by the [Kubernetes networking model](https://kubernetes.io/docs/concepts/cluster-administration/networking/#the-kubernetes-network-model).  |  Pod CIDR  For clusters with [ discontiguous multi-Pod CIDR](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-pod-cidr) enabled, all Pod CIDR blocks used by the cluster.  | Node tag | TCP, UDP, SCTP, ICMP, ESP, AH | 1000  
`gke-[cluster-hash]-ipv6-all` |  For [dual-stack network clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#dual_stack_network) only. Permits traffic between nodes and Pods on a cluster.  |  Same IP address range allocated in `subnetIpv6CidrBlock`.  | Node tag | TCP, UDP, SCTP, ICMP for IPv6, ESP, AH | 1000  
`gke-[cluster-name]-[cluster-hash]-inkubelet` |  Allow access to port 10255 (Kubelet read-only port) from internal Pod CIDRs and Node CIDRs in new GKE clusters running version 1.23.6 or later. Clusters running versions later than 1.26.4-gke.500 use the Kubelet authenticated port (10250) instead. Don't add firewall rules blocking 10250 within the cluster.  |  Internal Pod CIDRs and Node CIDRs.  | Node tag | TCP: 10255 | 999  
`gke-[cluster-name]-[cluster-hash]-exkubelet` |  Deny public access to port 10255 in new GKE clusters running version 1.23.6 or later.  |  0.0.0.0/0  | Node tag | TCP: 10255 | 1000  
  
### GKE Service firewall rules

GKE creates the following ingress firewall rules when creating a [Service](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service). You can prevent some of these firewall rules from being created by managing VPC firewall rules creation.

Name | Purpose | Source | Target (defines the destination) | Protocol and ports  
---|---|---|---|---  
`k8s-fw-[loadbalancer-hash]` | 
* Permits ingress traffic to reach a Service.
* For GKE versions earlier than 1.35.1-gke.1473000, this rule has a priority of 1000.
* For GKE version 1.35.1-gke.1473000 and later, this rule has a priority of 999.
| Source comes from `spec.loadBalancerSourceRanges`. Defaults to `0.0.0.0/0` if `spec.loadBalancerSourceRanges` is omitted. For more details, see [Firewall rules and source IP address allowlist](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters#fw_ip_address). | LoadBalancer virtual IP address | TCP and UDP on the ports specified in the Service manifest.  
`k8s-fw-[loadbalancer-hash]-deny` | 
* Denies all traffic that is not explicitly allowed by the `k8s-fw-[loadbalancer-hash]` rule.
* For GKE versions 1.35.1-gke.1473000 and later, this rule has a priority of 1000.
* This rule does not exist for GKE versions earlier than 1.35.1-gke.1473000.
| 0.0.0.0/0 | LoadBalancer virtual IP address | All  
`k8s-[cluster-id]-node-http-hc` |  Permits [health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) of a regional external passthrough Network Load Balancer Service when `externalTrafficPolicy` is set to `Cluster`. 
* For GKE versions earlier than 1.35.1-gke.1473000, this rule has a priority of 1000.
* For GKE version 1.35.1-gke.1473000 and later, this rule has a priority of 999.
| 

  * `35.191.0.0/16`
  * `130.211.0.0/22`
  * `209.85.152.0/22`
  * `209.85.204.0/22`

| LoadBalancer virtual IP address | TCP: 10256  
`k8s-[loadbalancer-hash]-http-hc` |  Permits [health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) of a regional external passthrough Network Load Balancer Service when `externalTrafficPolicy` is set to `Local`. 
* For GKE versions earlier than 1.35.1-gke.1473000, this rule has a priority of 1000.
* For GKE version 1.35.1-gke.1473000 and later, this rule has a priority of 999.
| 

  * `35.191.0.0/16`
  * `130.211.0.0/22`
  * `209.85.152.0/22`
  * `209.85.204.0/22`

| Node tag | TCP port defined by `spec.healthCheckNodePort`. If unspecified, the Kubernetes control plane assigns a health check port from the node port range. For more details, see [Health check port](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters#spd-hc-port).  
`k8s-[cluster-id]-node-hc` |  Permits [health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) of an internal passthrough Network Load Balancer Service when `externalTrafficPolicy` is set to `Cluster`.  | 

  * `35.191.0.0/16`
  * `130.211.0.0/22`
  * `209.85.152.0/22`
  * `209.85.204.0/22`

| Node tag | TCP: 10256  
`[loadbalancer-hash]-hc` |  Permits [health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) of an internal passthrough Network Load Balancer Service when `externalTrafficPolicy` is set to `Local`.  | 

  * `35.191.0.0/16`
  * `130.211.0.0/22`
  * `209.85.152.0/22`
  * `209.85.204.0/22`

| Node tag | TCP port defined by `spec.healthCheckNodePort`. If unspecified, the Kubernetes control plane assigns a health check port from the node port range. For more details, see [Health check port](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters#spd-hc-port).  
`k8s2-[cluster-id]-[namespace]-[service-name]-[suffixhash]` |  Permits IPv4 ingress traffic to reach a Service when one of the following is enabled: 
* [ GKE subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#subsetting).
* [ Backend service-based regional external passthrough Network Load Balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/backend-service-based-external-load-balancer).
* You can disable the automatic creation of these VPC firewall rules. For more information, see [Manage automatic firewall rule creation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#manage-firewall-rule-creation).
* For GKE versions earlier than 1.35.1-gke.1031000, this rule has a priority of 1000.
* For GKE version 1.35.1-gke.1031000 and later, this rule has a priority of 999.
| Source comes from `spec.loadBalancerSourceRanges`. Defaults to `0.0.0.0/0` if `spec.loadBalancerSourceRanges` is omitted. For more details, see [Firewall rules and source IP address allowlist](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters#fw_ip_address). | LoadBalancer virtual IP address | TCP and UDP on the ports specified in the Service manifest.  
`k8s2-[cluster-id]-[namespace]-[service-name]-[suffixhash]-ipv6` |  Permits IPv6 ingress traffic to reach a Service when one of the following is enabled: 
* [ GKE subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#subsetting).
* [ Backend service-based regional external passthrough Network Load Balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/backend-service-based-external-load-balancer).
* You can disable the automatic creation of these VPC firewall rules. For more information, see [Manage automatic firewall rule creation](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#manage-firewall-rule-creation).
* For GKE versions earlier than 1.35.1-gke.1031000, this rule has a priority of 1000.
* For GKE versions 1.35.1-gke.1031000 and later, this rule has a priority of 999.
| Source comes from `spec.loadBalancerSourceRanges`. Defaults to `::/0` if `spec.loadBalancerSourceRanges` is omitted. For more details, see [Firewall rules and source IP address allowlist](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters#fw_ip_address). | LoadBalancer virtual IP address | TCP and UDP on the ports specified in the Service manifest.  
`k8s2-[cluster-id]-[namespace]-[service-name]-[suffixhash]-deny` |  Denies all IPv4 traffic that is not explicitly allowed by the `k8s2-[cluster-id]-[namespace]-[service-name]-[suffixhash]` rule. 
* For GKE versions 1.35.1-gke.1031000 and later, this rule has a priority of 1000.
* This rule does not exist for GKE versions earlier than 1.35.1-gke.1031000.
| 0.0.0.0/0 | LoadBalancer virtual IP address | All  
`k8s2-[cluster-id]-[namespace]-[service-name]-[suffixhash]-deny-ipv6` |  Denies all IPv6 traffic that is not explicitly allowed by the `k8s2-[cluster-id]-[namespace]-[service-name]-[suffixhash]-ipv6` rule. 
* For GKE versions 1.35.1-gke.1031000 and later, this rule has a priority of 1000.
* This rule does not exist for GKE versions earlier than 1.35.1-gke.1031000.
| ::/0 | LoadBalancer virtual IP address/96 range | All  
`k8s2-[cluster-id]-[namespace]-[service-name]-[suffixhash]-fw` |  Permits [health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) of the Service when `externalTrafficPolicy` is set to `Local` and any of the following are enabled: 
* [ GKE subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#subsetting).
* [ Backend service-based regional external passthrough Network Load Balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/backend-service-based-external-load-balancer).
* For GKE versions earlier than 1.35.1-gke.1031000, this rule has a priority of 1000.
* For GKE versions 1.35.1-gke.1031000 and later, this rule has a priority of 999.
| 

  * `35.191.0.0/16`
  * `130.211.0.0/22`
  * `209.85.152.0/22`
  * `209.85.204.0/22`

| LoadBalancer virtual IP address | TCP port defined by `spec.healthCheckNodePort`. If unspecified, the Kubernetes control plane assigns a health check port from the node port range. For more details, see [Health check port](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer-parameters#spd-hc-port).  
`k8s2-[cluster-id]-l4-shared-hc-fw` |  Permits [health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) of the Service when `externalTrafficPolicy` is set to `Cluster` and any of the following are enabled: 
* [ GKE subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service-load-balancer#subsetting).
* [ Backend service-based regional external passthrough Network Load Balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/backend-service-based-external-load-balancer).
* For GKE versions earlier than 1.35.1-gke.1031000, this rule has a priority of 1000.
* For GKE versions 1.35.1-gke.1031000 and later, this rule has a priority of 999.
| 

  * `35.191.0.0/16`
  * `130.211.0.0/22`
  * `209.85.152.0/22`
  * `209.85.204.0/22`

| Node tag | TCP: 10256  
`gke-[cluster-name]-[cluster-hash]-mcsd` |  Permits the control plane to access the kubelet and metrics-server on cluster nodes for [ Multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-services). This rule has a priority of 900.  |  [ Health check IP addresses ](https://docs.cloud.google.com/load-balancing/docs/health-checks#fw-rule) | Node tag | TCP, UDP, SCTP, ICMP, ESP, AH  
  
### GKE Gateway firewall rules

GKE creates the following Gateway firewall rules when creating a [Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#gateway) and [HTTPRoute](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#httproute) resources:

Name | Purpose | Source | Target (defines the destination) | Protocol and ports  
---|---|---|---|---  
  
  * `gkegw1-l7-[network]-[region/global]`
  * `gkemcg1-l7-[network]-[region/global]`

|  Permits [health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) of a [network endpoint group (NEG)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/container-native-load-balancing).  The Gateway controller creates this rule when the first Gateway resource is created. The Gateway controller can update this rule if more Gateway resources are created.  | 

  * `35.191.0.0/16`
  * `130.211.0.0/22`
  * [ User defined proxy-only subnet ranges](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#configure-test-environment) (for internal Application Load Balancers)

| 0.0.0.0/0 | TCP: 1-65535   
  
### GKE Ingress firewall rules

GKE creates the following Ingress firewall rules when creating an [Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress) resource:

Name | Purpose | Source | Target (defines the destination) | Protocol and ports  
---|---|---|---|---  
`k8s-fw-l7-[random-hash]` |  Permits [health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) of a `NodePort` Service or [network endpoint group (NEG)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/container-native-load-balancing).  The Ingress controller creates this rule when the first Ingress resource is created. The Ingress controller can update this rule if more Ingress resources are created.  | 

  * `35.191.0.0/16`
  * `130.211.0.0/22`
  * `209.85.152.0/22`
  * `209.85.204.0/22`
  * [ User defined proxy-only subnet ranges](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#configure-test-environment) (for internal Application Load Balancers)

For GKE v1.17.13-gke.2600 or later: 
  * `35.191.0.0/16`
  * `130.211.0.0/22`
  * User-defined proxy-only subnet ranges (for internal Application Load Balancers)

| Node tag | TCP: 30000-32767, TCP:80 (for internal Application Load Balancers), TCP: all container target ports (for NEGs)   
  
## Manage VPC firewall rules creation

By default, GKE automatically creates ingress allow VPC firewall rules for all LoadBalancer Services. If you want to manage firewall rules for LoadBalancer Services yourself, you must disable the automatic creation of VPC firewall rules.

Disabling the automatic creation of VPC firewall rules for LoadBalancer Services only applies to the following:

  * [Internal LoadBalancer Services using GKE subsetting](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing)
  * [Backend service-based external LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/backend-service-based-external-load-balancer)



For information on how to disable firewall rules, see [User-managed firewall rules for GKE LoadBalancer Services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/user-managed-firewall-rules).

## Shared VPC

If you're using Ingress or LoadBalancer Services, and you have a cluster that is located in a Shared VPC using a Shared VPC network, the GKE service account in the service project can't create and update ingress allow firewall rules in the host project. You can grant the GKE service account in a service project permissions to create and manage the firewall resources. For more information, see [Shared VPC](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#shared_vpc).

**Note:** In case of GKE Gateway, the firewall rules are not automatically deployed. You need to manually create the firewall rules in order for health checks to succeed.

## Required firewall rule for expanded subnet

If you [expand the primary IPv4 range of the cluster's subnet](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks#expand-subnet), GKE does not automatically update the source range of the `gke-[cluster-name]-[cluster-hash]-vms` firewall rule. Because nodes in the cluster can receive IPv4 addresses from the expanded portion of the subnet's primary IPv4 range, you must manually create a firewall rule to allow communication between nodes of the cluster.

The ingress firewall rule you must create must allow TCP and ICMP packets _from the expanded primary subnet IPv4 source range_ , and it must at least apply to all nodes in the cluster.

To create an ingress firewall rule that only applies to the cluster's nodes, set the firewall rule's target to the same target tag used by your cluster's automatically-created `gke-[cluster-name]-[cluster-hash]-vms` firewall rule.

## What's next

  * Read an overview of [networking in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview).
  * Learn about [Configuring network policies for applications](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/network-policy).
  * Learn about other [Pre-populated firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#more_rules_default_vpc) in Google Cloud.
  * Learn more about [Creating firewall rules](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-shared-vpc#create_firewall_rules) in projects that use Shared VPC.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
