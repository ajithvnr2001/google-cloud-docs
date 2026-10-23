---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-to-external-endpoint-connectivity/
title: Configuring GKE pod to external endpoint connectivity \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:13.497829+00:00
---

# Configuring GKE pod to external endpoint connectivity  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/pod-to-external-endpoint-connectivity/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Configuring GKE pod to external endpoint connectivity Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document explains how to configure connectivity from Pods in GKE to external endpoints, including resources in on-premises networks and public internet services. To control the source IP address of GKE Pod traffic, you can use both the [`ip-masq-agent`](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-masquerade-agent) (node-level translation) and the [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) (VPC-level egress).

## Overview

When a Pod in a VPC-native GKE cluster sends a packet to a destination outside the cluster, the source IP address of the packet changes depending on how the node-level IP masquerading agent (`ip-masq-agent`) and Cloud NAT are configured.

  1. **Node-level translation (`ip-masq-agent`):** translates the source IP address of the packet from the _Pod IP address_ (secondary subnet range) to the internal _node IP address_ (primary subnet range) based on a configured `nonMasqueradeCIDRs` list.
  2. **VPC-level Gateway (Cloud NAT):** translates internal VPC IP addresses (Node IP addresses or Pod IP addresses) to static public IP addresses to allow outbound internet access.



Depending on whether a destination is masqueraded by the node, the packet leaves the node with either the node's IP address or the Pod's IP address. This source IP address determines how you configure your [Cloud Routers](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview) or on-premises routers.

* * *

## How IP masquerading and Cloud NAT work together

For internet-facing traffic, packets from a Pod traverse both the node network stack and the Cloud NAT gateway.

### Scenario A: Masquerading to node IP address (recommended for Internet egress)

If the destination IP address does _not_ match any range in the `nonMasqueradeCIDRs` list:

  * The `ip-masq-agent` performs Source NAT (SNAT) on the GKE node. The source IP address is rewritten from the _Pod IP address_ to the _node IP address_.
  * The packet enters the VPC network with the node IP address as the source.
  * The Cloud NAT gateway intercepts the packet.
  * Cloud NAT translates the node IP address to a public IP address and routes it to the internet.



### Scenario B: Preserving the Pod IP address (no masquerading)

If the destination IP address matches a range in the `nonMasqueradeCIDRs` list (or if default SNAT is disabled):

  * The `ip-masq-agent` leaves the packet unmodified. The source IP address remains the _Pod IP address_.
  * The packet enters the VPC network with the Pod IP address as the source.
  * The Cloud NAT gateway intercepts the packet.
  * Cloud NAT translates the Pod IP address to a public IP address _only if_ Cloud NAT is explicitly configured to translate the subnet's secondary IP address range that's used for GKE Pods.



* * *

## IP masquerade checker

Use this checker to verify if a destination IP address will be masqueraded based on your `ip-masq-agent` configuration.

* * *

## Example traffic flow

To understand the translation path, consider the following example configuration:

  * **Pod IP address range:** `10.4.0.0/14` (Pod IP address: `10.4.0.5`)
  * **Node IP address range:** `10.128.0.0/20` (node IP address: `10.128.0.10`)
  * **Destination IP address:** `8.8.8.8` (public DNS server, not in the `nonMasqueradeCIDRs` list)



When the Pod sends a packet, the following occurs:

  1. **Packet starts at Pod:** the packet originates from the Pod's network interface (IP address: `10.4.0.5`) with a destination IP address of `8.8.8.8`.
  2. **Node-level masquerading:** because the `8.8.8.8` destination IP address is not in the `nonMasqueradeCIDRs` list, the `ip-masq-agent` on the host node intercepts the packet as it leaves and performs SNAT. The source IP address is rewritten from the `10.4.0.5` Pod IP address to the host node IP address, which is `10.128.0.10`.
  3. **VPC egress:** the packet reaches the VPC network by using the `10.128.0.10` host node IP address as the source IP address.
  4. **Cloud NAT gateway:** because the destination is the public internet, Cloud NAT processes the packet, translates the source IP address from `10.128.0.10` to a public NAT IP address (for example, `203.0.113.1`), and forwards it to the internet.
  5. **Response handling:** the response returns to the public Cloud NAT IP address, which Cloud NAT reverse-translates back to the `10.128.0.10` host node IP address. The node then reverse-translates the host node IP address back to the Pod IP address, which is `10.4.0.5`, and delivers it to the Pod container.



### Traffic flow with Cloud Cloud Service Mesh (CSM)

If your workloads use [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview), traffic routing behaves as follows:

  * **Sidecar proxy or sidecarless CNI redirection:** outbound packets from the application container are intercepted by the mesh (by using a sidecar proxy like Envoy, or through ebpf-based or CNI redirection) before reaching the node's network namespace.
  * **Policy application:** the mesh determines whether the connection is permitted based on its authorization and egress policies.
  * **Egress routing:**
    * If traffic is directed using a Cloud Service Mesh egress gateway, the source IP address of the packet leaving the node corresponds to the IP address of the egress gateway's node or Pod, rather than the originating Pod.
    * If traffic is routed directly to the external endpoint, the packet exits the proxy and is routed through the standard host node network stack. In this case, the `ip-masq-agent` policies and Cloud NAT configurations described previously in this document still apply to the egress traffic.
  * For more information about configuring routing, gateways, and managing external traffic in Cloud Service Mesh, see the [Cloud Service Mesh documentation](https://docs.cloud.google.com/service-mesh/docs).



### Troubleshooting and isolating connectivity issues

If a Pod cannot connect to an external endpoint and you are using a service mesh, you must isolate whether the issue is in the service mesh configuration or the underlying GKE routing. To isolate the issue, use the following method:

  1. **Bypass the service mesh:** deploy a temporary client Pod in a namespace where sidecar injection is disabled, or use the `sidecar.istio.io/inject: "false"` annotation in the Pod spec to prevent injection for the test workload.
  2. **Test connectivity:** attempt to connect to the external destination (for example, by using `curl`, `ping`, or `nc`) from the non-mesh Pod.
  3. **Analyze the results:**
     * **If the connection succeeds:** the underlying GKE network routing, `ip-masq-agent` rules, and Cloud NAT gateway are configured correctly. The connectivity block is caused by Cloud Service Mesh policies, missing egress rules, or mTLS rules. For more information about troubleshooting, see [Troubleshooting deployments that use Envoy](https://docs.cloud.google.com/service-mesh/docs/service-routing/troubleshooting) in the Cloud Service Mesh documentation.
     * **If the connection fails:** the issue belongs to the underlying network infrastructure (such as IP masquerading, Cloud Router, Cloud NAT, VPC firewall rules, or on-premises firewalls). Use the steps in this page to verify your routing configuration.



## Determine the source IP address range using the checker

Before you configure routers or firewalls, use the IP masquerade checker in this document, and do the following:

  1. Paste the YAML contents of your `ip-masq-agent` ConfigMap into the configuration field.
  2. Enter the destination IP address of your target endpoint (such as your on-premises database or an external internet service).
  3. Click **Check Masquerading**.
  4. Note the output: 
     * **Masqueraded** : the packet uses the _node IP address range_ as the source.
     * **Not masqueraded** : the packet uses the _Pod IP address range_ as the source.



## Configure connectivity to endpoints

Based on the IP masquerade checker results, configure your networking paths and gateways according to the destination type.

### On-premises endpoints (VPN or Interconnect)

Cloud NAT is not used for on-premises connectivity, but you must configure your routers and firewalls based on the source IP address range that you determined with the IP masquerade checker.

#### If the traffic is masqueraded (source is node IP address):

  1. **Cloud Router:** ensure that the Cloud Router advertisements include the _primary IP address range_ of the GKE cluster subnet.
  2. **On-premises router or firewall:** configure your on-premises routers and firewalls to allow and handle incoming traffic from the GKE _node IP address range_.



#### If the traffic is not masqueraded (source is Pod IP address):

  1. **Cloud Router:** configure custom route advertisements on your Cloud Router to advertise the GKE _Pod secondary IP address range_ to your on-premises network.
  2. **On-premises router or firewall:** configure on-premises routing tables and firewalls to allow traffic originating from the GKE _Pod IP address range_ and ensure that return routes are advertised back to the VPC.



### Internet endpoints (Cloud NAT)

When routing traffic to public internet endpoints, you must configure a Cloud NAT gateway inside the VPC.

  1. In the Google Cloud console, go to the **Cloud NAT** page.
  2. Select or create your Cloud NAT gateway.
  3. Under **Cloud NAT source** , choose how the gateway handles GKE subnet ranges: 
     * **If the traffic is masqueraded (source is the node IP address):** select **Primary IP address ranges** of the subnet. Commercial GKE deployments typically default to this.
     * **If the traffic is not masqueraded (source is the Pod IP address):** must select **Primary and secondary IP address ranges** (or specify the GKE Pod secondary range explicitly). If you select only primary ranges, GKE Pod internet traffic will be blocked.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
