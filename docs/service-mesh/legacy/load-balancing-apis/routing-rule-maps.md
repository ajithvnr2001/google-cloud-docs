---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/routing-rule-maps/
title: Routing rule maps overview \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:29.350184+00:00
---

# Routing rule maps overview  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/routing-rule-maps/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Routing rule maps overview

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

This document applies only to Cloud Service Mesh with the load balancing APIs. We strongly recommend that you use the [service routing APIs](https://docs.cloud.google.com/service-mesh/docs/service-routing/service-routing-overview).

A routing rule map consists of the following:

  * A [forwarding rule](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/forwarding-rules) that references a target proxy
  * A [target proxy](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/target-proxies) that references a URL map
  * A [URL map](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts) that contains various routing rules



When you create and configure these resources for Cloud Service Mesh, Cloud Service Mesh uses the values to create the configuration that it sends to your data plane, which includes xDS clients such as Envoy proxies and proxyless gRPC applications. The data plane then handles traffic according to this configuration.

A forwarding rule references a target proxy, and has an IP address and a port. For Cloud Service Mesh deployments, the forwarding rule's load-balancing scheme must be set to `INTERNAL_SELF_MANAGED`. The target proxy, in turn, references a URL map. These three resources combine to form a routing rule map.

A forwarding rule that references a target gRPC proxy with the `validateForProxyless` field set to `TRUE` must have its IP address set to `0.0.0.0`. When `validateForProxyless` is set to `TRUE`, configurations that specify an IP address other than `0.0.0.0` are rejected.

The routing rule map defines how traffic passes from clients to servers inside a service mesh.

## Supported target proxy types

Cloud Service Mesh supports the following target proxy types:

  * **Target HTTP proxy** , which you configure when your clients and servers send or receive HTTP or HTTP/2 traffic.
  * **Target HTTPS proxy** , which you configure when your clients and servers send or receive HTTPS traffic. This is required when you set up service security with Envoy proxies.
  * **Target TCP proxy** , which you configure when your clients and servers send or receive TCP traffic.
  * **Target gRPC proxy** , which you configure when your clients and servers send or receive gRPC traffic. Target gRPC proxies contain the field `validateForProxyless`, which is set to `TRUE` when you deploy proxyless gRPC services.



## Traffic routing with Envoy sidecar proxies

When you use Cloud Service Mesh with Envoy sidecar proxies, client requests are routed as follows:

  * The network stack intercepts the request and redirects it to your Envoy sidecar proxy.
  * The Envoy sidecar proxy looks at the request's IP address and port.
  * The IP address and port pair are checked against the IP address and port specified in any forwarding rules that have the load-balancing scheme set to `INTERNAL_SELF_MANAGED`.
  * If a forwarding rule with a matching IP address and port is found, Envoy looks at the target HTTP proxy or the target gRPC proxy that the forwarding rule references.
  * Envoy checks the URL map that the target proxy references.
  * Envoy routes the request according to the rules specified in the URL map.



For information about how traffic is routed with a target TCP proxy, see [Routing TCP traffic with Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/configure-tcp).

## Traffic routing with proxyless gRPC applications

This behavior is different for proxyless gRPC applications. When you configure a gRPC client, you specify the target URI for the service that the client needs to contact. This URI uses the `xds` name resolver scheme and the `hostname:port` format—for example `xds:///example.hostname:8080`.

When the proxyless gRPC client connects to Cloud Service Mesh, Cloud Service Mesh sends it information corresponding to the service as follows:

  * Cloud Service Mesh looks for forwarding rules with the load-balancing scheme set to `INTERNAL_SELF_MANAGED` to find forwarding rules whose port matches the port specified in the target URI.
  * Cloud Service Mesh finds the target gRPC proxy or the target HTTP proxy for each of these forwarding rules.
  * Cloud Service Mesh finds the URL maps referenced by these target gRPC proxies or target HTTP proxies.
  * Cloud Service Mesh checks the host rules in the URL map, which also have the `hostname[:port]` format, and looks for a match.
  * When a match is found, Cloud Service Mesh returns routing rules and service information to the gRPC client.



If more than one match is found, the behavior is undefined and can lead to unpredictable behavior. This generally happens when both of the following conditions are met:

  * The same hostname is used across multiple URL maps.
  * Multiple forwarding rules with the load-balancing scheme `INTERNAL_SELF_MANAGED` specify the same port.



For this reason, we recommend that you don't re-use the same hostname across multiple URL maps that are referenced by forwarding rules that specify the same port.

## What's next

  * To get fine-grained control over how traffic is handled, see the [Advanced traffic management overview](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/advanced-traffic-management-legacy).

  * To learn more about Cloud Service Mesh, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/overview).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
