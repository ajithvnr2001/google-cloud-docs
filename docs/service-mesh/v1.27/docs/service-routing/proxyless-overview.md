---
url: https://docs.cloud.google.com/service-mesh/v1.27/docs/service-routing/proxyless-overview/
title: Cloud Service Mesh with proxyless gRPC services overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:31:44.518311+00:00
---

# Cloud Service Mesh with proxyless gRPC services overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.27/docs/service-routing/proxyless-overview/

You are viewing v1.27 Service Mesh documentation.

Available versions

[Cloud Service Mesh latest](https://docs.cloud.google.com/service-mesh/docs)  
[Cloud Service Mesh 1.28 archive](https://docs.cloud.google.com/service-mesh/v1.28/docs)  
[Cloud Service Mesh 1.27 archive](https://docs.cloud.google.com/service-mesh/v1.27/docs)  
[Cloud Service Mesh 1.26 archive](https://docs.cloud.google.com/service-mesh/v1.26/docs)  
[Cloud Service Mesh 1.25 archive](https://docs.cloud.google.com/service-mesh/v1.25/docs)  
[Cloud Service Mesh 1.24 archive](https://docs.cloud.google.com/service-mesh/v1.24/docs)  
[Cloud Service Mesh 1.23 archive](https://docs.cloud.google.com/service-mesh/v1.23/docs)  
[Cloud Service Mesh 1.22 archive](https://docs.cloud.google.com/service-mesh/v1.22/docs)  
[Cloud Service Mesh 1.21 archive](https://docs.cloud.google.com/service-mesh/v1.21/docs)  
[Cloud Service Mesh 1.20 archive](https://docs.cloud.google.com/service-mesh/v1.20/docs)  
[Anthos Service Mesh 1.19 archive](https://docs.cloud.google.com/service-mesh/v1.19/docs)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.27/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Service Mesh with proxyless gRPC services overview

This guide provides you with an overview of the architecture of Cloud Service Mesh with proxyless gRPC services, including use cases and architecture patterns.

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview).

Cloud Service Mesh's managed control plane enables global routing, load balancing, and regional failover for service mesh and load-balancing use cases. This includes deployments that incorporate sidecar proxies and gateway proxies. Cloud Service Mesh support for proxyless gRPC applications offers an additional deployment model in which gRPC applications can participate in a service mesh without needing a sidecar proxy.

In a typical example, a gRPC client establishes a connection with a gRPC server that hosts your backend logic. Cloud Service Mesh gives your gRPC clients information about which servers to contact, how to load balance requests to multiple instances of a server, and what to do with requests if a server is not running.

For a complete overview of how Cloud Service Mesh works, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview).

## How Cloud Service Mesh works with gRPC applications

Cloud Service Mesh configures gRPC clients with a [supported gRPC version](https://docs.cloud.google.com/service-mesh/v1.27/docs/onboarding/prepare-service-routing-envoy-proxyless#supported-grpc-versions-languages), similarly to how sidecar proxies such as Envoy are configured. However, proxyless gRPC applications connected directly to Cloud Service Mesh don't need sidecar proxies. Instead, Cloud Service Mesh uses open source xDS APIs to configure gRPC applications directly. These gRPC applications act as xDS clients, connecting to Cloud Service Mesh's global control plane. After they're connected, gRPC applications receive dynamic configuration from the control plane, enabling endpoint discovery, load balancing, regional failover, and health checks. This approach enables additional Cloud Service Mesh deployment patterns.

In the first illustration, a service mesh is enabled by using a sidecar proxy.

[ ![A service mesh enabled by using a sidecar proxy.](https://docs.cloud.google.com/static/service-mesh/v1.27/docs/images/csm-proxy-enabled.svg)](https://docs.cloud.google.com/static/service-mesh/v1.27/docs/images/csm-proxy-enabled.svg) A service mesh enabled by using a sidecar proxy (click to enlarge)

To configure a sidecar proxy, Cloud Service Mesh uses xDS APIs. Clients communicate with the server through the sidecar proxy.

In the second illustration, a service mesh is enabled without a sidecar proxy by using a proxyless gRPC client.

[ ![A service mesh enabled using proxyless gRPC.](https://docs.cloud.google.com/static/service-mesh/v1.27/docs/images/csm-proxyless-enabled.svg)](https://docs.cloud.google.com/static/service-mesh/v1.27/docs/images/csm-proxyless-enabled.svg) A service mesh enabled using proxyless gRPC (click to enlarge)

If you are deploying only gRPC services that Cloud Service Mesh configures, you can create a service mesh without deploying any proxies at all. This makes it easier to bring service mesh capabilities to your gRPC applications.

## Name resolution

Name resolution works for proxyless deployments in the following ways:

  1. You set `xds` as the name resolution scheme in the gRPC client channel when connecting to a service. The target URI is formatted as `xds:///hostname:port`. When the port is not specified, the default value is 80—for example, in the target URI `xds:///example.hostname`.
  2. The gRPC client resolves the `hostname:port` in the target URI by sending a [listener discovery service (LDS)](https://www.envoyproxy.io/docs/envoy/latest/configuration/listeners/lds) request to Cloud Service Mesh.
  3. Cloud Service Mesh looks up the configured forwarding rules that have a matching port. It then looks up the corresponding URL map for a host rule that matches `hostname:port`. It returns the associated routing configuration to the gRPC client.



The host rules that you configure in Cloud Service Mesh must be unique across all URL maps. For example, `example.hostname`, `example.hostname:80`, and `example.hostname:8080` are all different rules.

## Name resolution with different deployment types

The name resolution scheme is different for proxyless deployments and deployments that use Envoy proxies.

The gRPC client uses the `xds` name resolution scheme to connect to a service, allowing the client to receive the service configuration from Cloud Service Mesh. The gRPC client then communicates directly with the gRPC server.

You can combine sidecar proxy and proxyless deployment patterns for increased flexibility. Combining patterns is especially helpful when your organization and network support multiple teams with different feature requirements, operational needs, and gRPC versions.

In the following illustration, both proxyless gRPC clients and gRPC clients with a sidecar proxy communicate with a gRPC server. The gRPC clients with sidecar proxies use the `dns` name resolution scheme.

[ ![A service mesh consisting of proxyless gRPC clients and gRPC clients with sidecar proxies.](https://docs.cloud.google.com/static/service-mesh/v1.27/docs/images/csm-proxy-proxyless-grpc.svg)](https://docs.cloud.google.com/static/service-mesh/v1.27/docs/images/csm-proxy-proxyless-grpc.svg) A service mesh consisting of proxyless gRPC clients and gRPC clients with sidecar proxies (click to enlarge)

## Use cases

The following use cases help you understand when you might want to use Cloud Service Mesh with proxyless gRPC applications. Your deployment can include proxyless gRPC applications, gRPC applications with sidecar proxies, or a mix of both.

### Resource efficiency in a large-scale service mesh

If your service mesh includes hundreds or thousands of clients and backends, you might find that the total resource consumption from running sidecar proxies starts to add up. When you use proxyless gRPC applications, you don't need to introduce sidecar proxies to your deployment. A proxyless approach can result in efficiency gains.

### High-performance gRPC applications

For some use cases, every millisecond of request and response latency matters. In such a case, you might find reduced latency when you use a proxyless gRPC application, instead of passing every request through a client-side sidecar proxy and, potentially, a server-side sidecar proxy.

### Service mesh for environments where you can't deploy sidecar proxies

In some environments, you might not be able to run a sidecar proxy as an additional process alongside your client or server application. Or, you might not be able to configure a machine's network stack for request interception and redirection—for example, by using [`iptables`](https://wikipedia.org/wiki/Iptables). In this case, you can use Cloud Service Mesh with proxyless gRPC applications to introduce service mesh capabilities to your gRPC applications.

### Heterogeneous service mesh

Because both proxyless gRPC applications and Envoy communicate with Cloud Service Mesh, your service mesh can include both deployment models. Including both models lets you satisfy the particular operational, performance, and feature needs of different applications and different development teams.

### Migrate from a service mesh with proxies to a mesh without proxies

If you already have a gRPC application with a sidecar proxy that Cloud Service Mesh configured, you can transition to a proxyless gRPC application.

When a gRPC client is deployed with a sidecar proxy, it uses DNS to resolve the hostname that it is connecting to. The sidecar proxy intercepts traffic to provide service mesh capabilities.

You can define whether a gRPC client uses the proxyless route or the sidecar proxy route to communicate with a gRPC server by modifying the name resolution scheme that it uses. Proxyless clients use the `xds` name resolution scheme, while sidecar proxies use the `dns` name resolution scheme. Some gRPC clients might even use the proxyless route when talking to one gRPC server, but use the sidecar proxy route when talking to another gRPC server. This lets you gradually migrate to a proxyless deployment.

To migrate from a service mesh with proxies to a mesh without proxies, you create a new Cloud Service Mesh service that your proxyless gRPC client uses. You can use the same APIs to configure Cloud Service Mesh for the existing and new versions.

[ ![Service mesh with a gRPC client that communicates with different services using proxyless and proxy-based mechanisms.](https://docs.cloud.google.com/static/service-mesh/v1.27/docs/images/csm-proxy-proxyless-2.svg)](https://docs.cloud.google.com/static/service-mesh/v1.27/docs/images/csm-proxy-proxyless-2.svg) Service mesh with a gRPC client that communicates with different services using proxyless and proxy-based mechanisms (click to enlarge)

## Architecture and resources

The configuration data model for proxyless gRPC services extends the Cloud Service Mesh configuration model, with some additions and limitations that are described in this guide. Some of these limitations are temporary because proxyless gRPC does not support all of Envoy's features, and others are inherent to using RPCs. For example, HTTP redirects that use gRPC are not supported. To help you understand the configuration model in this guide, we recommend that you familiarize yourself with Cloud Service Mesh [concepts](https://docs.cloud.google.com/service-mesh/v1.27/docs/overview) and [configuration](https://docs.cloud.google.com/service-mesh/v1.27/docs/prepare-for-envoy-setup).

The following diagram shows the resources that you must configure for proxyless gRPC applications.

[ ![Resources supported in proxyless gRPC for load balancing.](https://docs.cloud.google.com/static/service-mesh/v1.27/docs/images/csm-gce-resources-for-proxyless.svg)](https://docs.cloud.google.com/static/service-mesh/v1.27/docs/images/csm-gce-resources-for-proxyless.svg) Resources supported in proxyless gRPC for load balancing (click to enlarge)**Note:** Some Cloud Service Mesh capabilities are not supported with proxyless gRPC applications. For details, see the [Features](https://docs.cloud.google.com/service-mesh/v1.27/docs/features) page. If you require an unsupported feature, you can use Envoy with your gRPC applications. Configuring Cloud Service Mesh for gRPC applications that use Envoy generally follows the same configuration data model described in the following sections.

### Health checks

A gRPC health check can check the status of a gRPC service that is running on a backend virtual machine (VM) instance or a network endpoint group (NEG).

If a gRPC health check cannot be used because your gRPC server does not implement the [gRPC health checking protocol](https://github.com/grpc/grpc/blob/master/doc/health-checking.md), use a TCP health check instead. don't use an HTTP, HTTPS, or HTTP/2 health check.

For more information, see [gRPC health check](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-grpc) and [Additional flag for gRPC health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#optional-flags-hc-protocol-grpc).

### Backend service

The backend service defines how a gRPC client communicates with a gRPC server. When you create a backend service for gRPC, set the protocol field to `GRPC`.

  * A backend service configured with a protocol set to `GRPC` can also be accessed by gRPC applications through a sidecar proxy. In that situation, the gRPC client must not use the `xds` name resolution scheme.

  * In all Cloud Service Mesh deployments, the load-balancing scheme for the backend service must be `INTERNAL_SELF_MANAGED`.




### Backends

Backends host your gRPC server instances. You can use [managed or unmanaged instance groups](https://docs.cloud.google.com/compute/docs/instance-groups) in Compute Engine and [zonal NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg) in Google Kubernetes Engine as backends to host your gRPC server instances.

## What's next

  * To learn about the service routing APIs and how they work, see the [overview](https://docs.cloud.google.com/service-mesh/v1.27/docs/service-routing/service-routing-overview).
  * To prepare to configure Cloud Service Mesh with proxyless gRPC applications, see [Prepare to set up with Envoy and proxyless workloads](https://docs.cloud.google.com/service-mesh/v1.27/docs/onboarding/prepare-service-routing-envoy-proxyless).
  * To learn about limitations that apply to proxyless gRPC deployments, see [Limits and limitations with proxyless gRPC](https://docs.cloud.google.com/service-mesh/v1.27/docs/service-routing/limitations-proxyless).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
