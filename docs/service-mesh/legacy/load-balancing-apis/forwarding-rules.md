---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/forwarding-rules/
title: Forwarding rules for Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:49:09.884664+00:00
---

# Forwarding rules for Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/forwarding-rules/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Forwarding rules for Cloud Service Mesh

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

This document applies only to Cloud Service Mesh with the load balancing APIs. We strongly recommend that you use the [service routing APIs](https://docs.cloud.google.com/service-mesh/docs/service-routing/service-routing-overview) to deploy Cloud Service Mesh.

Cloud Service Mesh uses the forwarding rule to determine the target proxy to which traffic in the mesh is routed.

Each forwarding rule provides a single global IPv4 address for a service. You can use that address to create internal DNS records for your service (for example, by using a [Cloud DNS managed private zone](https://docs.cloud.google.com/dns/docs/zones#create-private-zone)). Metadata filters in the forwarding rule specify the criteria for which an xDS-compliant sidecar proxy receives the configuration.

**Note:** This page only discusses forwarding rules in the context of Cloud Service Mesh. Forwarding rules are also used to provide forwarding information in the control plane for [protocol forwarding](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding), [Classic VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#classic-vpn), and [Google Cloud load balancers](https://docs.cloud.google.com/load-balancing/docs/using-forwarding-rules). For a more comprehensive overview of forwarding rules, see the [Cloud Load Balancing forwarding rules overview](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts).

For the Cloud Service Mesh control plane, the internal, self-managed, and global forwarding rule routes traffic by IP address, port, and protocol to a target proxy. The target proxy points to a URL map that contains rules that determine the destination of the traffic. The URL map also specifies the default backend service. This backend service specifies a health check and determines the appropriate backend, such as a managed instance group (MIG) that contains virtual machine (VM) instances or a [network endpoint group (NEG)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg) that contains Google Kubernetes Engine (GKE) backend Pods.

The following diagram shows how a forwarding rule fits into the Cloud Service Mesh architecture.

[ ![Cloud Service Mesh forwarding rule highlighted.](https://docs.cloud.google.com/static/service-mesh/docs/images/td-forwarding-rule.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/td-forwarding-rule.svg) Cloud Service Mesh forwarding rule highlighted (click to enlarge)

## Forwarding rule properties

A forwarding rule resource contains the following properties that apply to Cloud Service Mesh. The forwarding rule handles traffic that matches the destination IP address, protocol, and port number.

A `0.0.0.0` IP address in a forwarding rule is one of the options when using Cloud Service Mesh. A `0.0.0.0` IP address means any IP address.

  * With a proxy deployment, a `0.0.0.0` IP address lets a proxy match any incoming traffic if no other specific match is found.

  * With a proxyless deployment, a `0.0.0.0` IP address provides a way to specify that an IP address is not required. More details follow about using `0.0.0.0` IP addresses with a target gRPC proxy.




The following table describes forwarding rule properties in more detail.

Property | Required | Description  
---|---|---  
`name` | ✔ | The name of the forwarding rule. The name must be unique in this project, from 1 to 63 characters, and match the regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?` This means that the first character must be a lowercase letter, and all the following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`IPAddress` | ✔ | One of the following: `0.0.0.0` or `127.0.0.1`, or any RFC 1918 address. IP addresses for Cloud Service Mesh forwarding rules don't need to correspond to IP address ranges of subnets in the Virtual Private Cloud (VPC) network. For a given VPC network, IP address, and port, you can have only one internal, self-managed forwarding rule. For example, in the same VPC network, you cannot create two forwarding rules that use the `0.0.0.0` IP address and port `80`.  
`IPAddress` with a target gRPC proxy |  |  A forwarding rule that references a target gRPC proxy with the `validateForProxyless` field set to `TRUE` and its IP address set to `0.0.0.0`. A gRPC client that uses the `xds` scheme does not perform DNS lookup to resolve the hostname in the channel URI. Instead, such a client resolves the `hostname[:port]` in the target URI by sending a [Listener discovery service (LDS)](https://www.envoyproxy.io/docs/envoy/latest/configuration/listeners/lds) request to Cloud Service Mesh. There is no DNS lookup involved, and a DNS entry for the hostname is not required. As a result, Cloud Service Mesh uses the `0.0.0.0` IP address and the port (default `80`) specified in the URI to look up the forwarding rule. Then, Cloud Service Mesh looks for a matching host rule in the URL map of the target proxy referenced by the forwarding rule.  
`target` | ✔ |  The target proxy that this forwarding rule directs traffic to. Cloud Service Mesh supports `target-http-proxy`, `target-https-proxy`, and `target-grpc-proxy`. When you use the Google Cloud console to configure the forwarding rule, the target proxy is configured automatically. When you use the Google Cloud CLI or the API, the target proxy must exist before you create your forwarding rule. You can use more than one forwarding rule with a given proxy.  
`IPProtocol` | ✔ | The type of protocol that this forwarding rule matches. The only supported value is `TCP`.  
`loadBalancingScheme` | ✔ | Specifies how the forwarding rule is used. The valid value for Cloud Service Mesh is `INTERNAL_SELF_MANAGED`.  
`portRange` | ✔ |  A port or a port range joined by a dash. Packets of the specified protocol sent to these ports are forwarded to the appropriate backend. You can specify a single number of a range—for example, `80` or `80-8080`. For a given VPC network, IP address, and port, you can have only one internal, self-managed forwarding rule. For example, in the same VPC network, you cannot create two forwarding rules that use the `0.0.0.0` IP address and port `80`. With proxyless gRPC services, the port in the forwarding rule is matched with the port specified in the URI that a gRPC application uses to connect to a service. If a port is not specified in the URI, then `80` is the default port.  
`network` | ✔ |  Specifies the VPC network where the Google Cloud VMs running Envoy proxies are located. The Envoy proxies read the Cloud Service Mesh configuration that you define for the same network where the proxies are deployed. You can use the VPC network named `default` or a custom network. Cloud Service Mesh supports load balancing for clients only within the Google Cloud network. You specify the network name in the forwarding rule. VPC Network Peering isn't supported.  
  
## Add a global forwarding rule

To learn how to configure a forwarding rule within the overall Cloud Service Mesh setup with the load balancing APIS, see the following:

  * [Set up Cloud Service Mesh for Compute Engine VMs with automatic Envoy deployment](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gce-vms-auto)
  * [Set up Cloud Service Mesh for Compute Engine VMs with manual Envoy deployment](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gce-vms)
  * [Set up Cloud Service Mesh for GKE Pods with automatic Envoy injection](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gke-pods-auto)
  * [Set up Cloud Service Mesh for GKE Pods with manual Envoy injection](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-gke-pods)
  * [Set up Cloud Service Mesh for Compute Engine VMs and proxyless gRPC services](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-proxyless-gce)
  * [Set up Cloud Service Mesh for GKE Pods and proxyless gRPC services](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/set-up-proxyless-gke)



## What's next

  * To use metadata filters to control which sidecar proxies receive the configuration attached to the forwarding rule, see [Setting up config filtering based on `MetadataFilter` match](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/configure-advanced-traffic-management#config-filtering-metadata).
  * To route traffic, see [Cloud Service Mesh routing rule maps overview](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/routing-rule-maps).
  * To learn more about Cloud Service Mesh, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
