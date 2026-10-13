---
url: https://docs.cloud.google.com/service-mesh/v1.29/docs/service-routing/service-routing-overview/
title: Cloud Service Mesh service routing APIs overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:20.391699+00:00
---

# Cloud Service Mesh service routing APIs overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.29/docs/service-routing/service-routing-overview/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.29/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Service Mesh service routing APIs overview

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview).

This document is intended for mesh or platform administrators and service developers who have an intermediate to advanced level of familiarity with Cloud Service Mesh and service mesh concepts and who are deploying Cloud Service Mesh on Compute Engine with VM instances. This document applies to deployments using Envoy and gRPC clients. For more information on Cloud Service Mesh concepts, see the [general overview](https://docs.cloud.google.com/service-mesh/v1.29/docs/overview).

Cloud Service Mesh provides service networking capabilities to your applications, including advanced traffic management, observability, and security. However, configuring and operating a service mesh is a complex task for mesh administrators and service developers.

This document describes the service routing APIs for configuring Cloud Service Mesh. These APIs are designed to simplify and improve your overall mesh configuration experience.

The service routing model uses API resources called `Mesh`, `Gateway`, and `Route`. These resources provide a contextually-relevant configuration experience when you define your service networking control plane.

This document introduces the following service routing API model and resources.

  * [`Mesh`resource](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.meshes)
    * Service-to-service (east-west) traffic management and security configuration for Envoy sidecar proxies and proxyless gRPC clients.
  * [`Gateway`resource](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.gateways)

    * Traffic management and security configuration for Envoy proxies acting as ingress gateways, allowing external clients to connect to the service mesh (north-south).
  * `Route` resources with the following types:

    * [`HTTPRoute`](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.httpRoutes)
    * [`GRPCRoute`](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes)
    * [`TCPRoute`](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes)
    * [`TLSRoute`](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes)



The Google Cloud console does not provide support for the service routing APIs. You must implement these API resources using the Google Cloud CLI or the REST APIs.

## Use cases and benefits

The service routing APIs let you configure Cloud Service Mesh for both proxyless gRPC and Envoy proxy deployments. The service routing API model enables several key benefits.

In the following diagram, two services in the service mesh are connected by a `Mesh` resource. The two `HTTPRoute` resources configure routing. The mesh or platform administrator manages the `Mesh` resource and the two service owners create the routing configuration for their services.

[ ![East-west service-to-service traffic in a service mesh](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/east-west.svg)](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/east-west.svg) East-west service-to-service traffic in a service mesh (click to enlarge)

### Role-oriented API design enables clear separation of responsibilities

The service routing APIs let you separate mesh configuration responsibilities based on organizational roles:

  * Mesh administrators can define the logical mesh as well as the ingress gateway infrastructure.
  * Service owners (application developers) can independently define access patterns for their services. They can also define and apply traffic management policies for their services.



In the following diagram, Cloud Load Balancing and a `Gateway` resource provide an ingress gateway for traffic entering the mesh from a client that is not in the mesh. The mesh administrator configures and manages the `Gateway` resource, while the service owners configure and manage their own services and traffic routing.

[ ![North-south traffic into the mesh through a gateway](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/north-south.svg)](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/north-south.svg) North-south traffic into the mesh through a gateway (click to enlarge)

### Enhanced reliability with self-serve model

The service routing APIs use per-protocol, per-route resources that can be configured and owned by independent service owners. This approach has several advantages.

  * Service owners have autonomy over how they want to configure policies and traffic management for the services they own.
  * Updating one `Route` resource does not affect other `Route` resources in the mesh. The update process is more reliable because service owners manage small configurations.
  * The service owner who is responsible for the destination service or hostname owns each `Route` resource.
  * Service owners don't have to depend on mesh administrators to update routing.



### Enable a service mesh spanning multiple projects in Shared VPC environments

The service routing API model lets service owners participate in a shared mesh infrastructure using Shared VPC and other means of connectivity while maintaining independent control over their services. For example, service owners can define the `Route` resources in their own projects. Platform administrators can define a `Mesh` in a centrally administered host project, then grant service owners IAM permissions to attach their `Route` resources to a shared `Mesh` or `Gateway`. The following diagram shows an example with Shared VPC.

[ ![Cross-project referencing with Shared VPC](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/cross-project-ref.svg)](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/cross-project-ref.svg) Cross-project referencing with Shared VPC (click to enlarge)

The service routing APIs also let you have service mesh clients connected to different networks using VPC Network Peering.

### Route traffic based on the server name indicator

The `TLSRoute` resource lets you route TLS-encrypted traffic based on the Server Name Indication (SNI) in the TLS handshake. You can configure TLS traffic to be routed to the appropriate backend services by configuring the SNI match in the `TLSRoute` resource. In these deployments, proxies only route traffic and the TLS session is terminated at the destination backend instance.

The `TLSRoute` resource is supported only with Envoy proxies that are deployed as sidecar proxies or gateways.

#### `TLSRoute` resource attached to a `Mesh` resource

The deployment shown in the following diagram routes any service mesh traffic where the SNI extension has the value `service1` to the backend service `service1`. Additionally, any service mesh traffic where the SNI extension has the value `service2` is routed to the backend service `service2`. The SNI extension value and the backend service name are independent of each other.

[ ![TLSRoute resource and Mesh resource](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/tls-route-mesh.svg)](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/tls-route-mesh.svg) `TLSRoute` resource and `Mesh` resource (click to enlarge)

#### `TLSRoute` resource attached to a `Gateway` resource

The deployment shown in the following diagram routes any inbound traffic to the `Gateway` resource where the SNI extension has the value `serviceA` to the backend service `serviceA`. Additionally, any inbound traffic to the `Gateway` where the SNI extension has the value `serviceB` is routed to the backend service `serviceB`. The SNI extension value and the backend service name are independent of each other. The SNI extension value and the header in HTTP requests are also independent.

The `Gateway` resource does not terminate the TLS connection at the `Gateway`'s Envoy proxy. Instead, the TLS connection is terminated at the corresponding backend service. The `Gateway` cannot inspect any information encrypted in the TLS layer, other than seeing the `ClientHello`, which contains a plain text SNI extension. The `Gateway` performs TLS passthrough in this mode. Note that encrypted `ClientHello` is unsupported.

[ ![TLSRoute resource and Gateway resource](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/tls-route-gateway.svg)](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/tls-route-gateway.svg) `TLSRoute` resource and `Gateway` resource (click to enlarge)

### Core gRPC support

You can configure proxyless gRPC clients by using core gRPC attributes such as matching by method.

### Traffic splitting for TCP traffic

You can implement weight-based traffic splitting for TCP traffic across multiple backend services. You can configure patterns such as canary (blue- green) rollouts when you update your service. Traffic splitting also lets you migrate traffic in a controlled manner without downtime.

### Traffic interception

When you use the service routing API `Mesh` and `Gateway` resources, all traffic is automatically intercepted. For more information, see [Options for Compute Engine VM setup with automatic Envoy deployment](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/auto-vms-options).

## Architecture and resources

This section describes the service routing API model and its resources, and helps you to understand how the service routing API resources work together.

### `Mesh` resource

The `Mesh` resource represents an instance of a service mesh. You use it to create a logical service mesh in your project. Each `Mesh` resource must have a unique name in the project. After a `Mesh` resource is created, its name cannot be modified.

[ ![Mesh API resource with Envoy sidecar and proxyless gRPC deployments](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/mesh-resource.svg)](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/mesh-resource.svg) `Mesh`API resource with Envoy sidecar and proxyless gRPC deployments (click to enlarge)

The `Mesh` resource is referenced in the `Route` resource to add routes for services that are part of the mesh.

Envoy proxy and proxyless gRPC clients receive configuration from Cloud Service Mesh by joining the service mesh identified by the `Mesh` resource's name. The `Mesh` resource supports the following data plane deployments:

  * Envoy running alongside the application as sidecar proxies
  * Proxyless gRPC clients
  * Mix of Envoy sidecar and proxyless gRPC clients



### `Route` resource

The `Route` resource is used to set up routing to the services. There are four different types of the `Route` API resource. They define the protocol used to route traffic to a backend service.

  * `HTTPRoute`
  * `GRPCRoute`
  * `TCPRoute`
  * `TLSRoute`



The API doesn't contain a `Route` API verbatim. The only configurable API resources are `HTTPRoute`, `GRPCRoute`, `TCPRoute`, and `TLSRoute`.

The `Route` resource references one or more `Mesh` and `Gateway` resources to add the routes that are part of the corresponding `Mesh` or `Gateway` configuration. A `Route` resource can reference both `Gateway` and `Mesh` resources.

The `Route` resource also references one or more [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) resources. The services are configured using the backend service API. You create a backend service resource that points to one or more MIG or NEG backends.

The following diagram shows the relationships among the `Mesh`, `Gateway`, and `Route` resources and the backend service resource and its backends.

[ ![Route API resources](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/new-route-resources.svg)](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/new-route-resources.svg) `Route` API resources (click to enlarge)

You define other traffic management capabilities, such as routing, header modifications, timeouts, and weight-based traffic splitting in `Route` resources. For example, in the following diagram, an `HTTPRoute` resource defines a 70% / 30% traffic split between two backend services.

[ ![Weight-based traffic splitting](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/traffic-splitting.svg)](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/traffic-splitting.svg) Weight-based traffic splitting (click to enlarge)

To simplify administration of your service mesh, you can list all `Route` resources attached to a `Mesh` or `Gateway` resource.

#### `TLSRoute` resource

Use the `TLSRoute` resource to route TLS traffic to backend services based on SNI hostnames and Application-Layer Protocol Negotiation (ALPN) name. `TLSRoute` configuration implies TLS passthrough, in which the Envoy proxy does not terminate TLS traffic.

The `TLSRoute` resource references one or more `Mesh` and `Gateway` resources to add the routes that are part of the corresponding Mesh or Gateway configuration.

The `TLSRoute` resource also references one or more backend service resources. The services are configured using the backend service API resource.

### `Gateway` resource

The `Gateway` resource is used to represent Envoy proxies acting as ingress gateways, allowing external clients to connect to the service mesh (north-south traffic). This resource has listening ports along with a `scope` parameter. The Envoy proxy that acts as an ingress gateway binds to the ports specified and to `0.0.0.0`, which represents all of the IP addresses on the local VM. The following diagram shows Envoy proxies deployed as an ingress service and configured by the `Gateway` resource. In this particular example, Envoy proxies are configured to listen on port 80 for incoming connections from clients.

The `Gateway` API resource only supports the Envoy proxy data plane. It does not support proxyless gRPC. `gRPCRoutes` are supported in the `Gateway` resource, but the gRPC traffic is routed by the Envoy proxy, acting as a middle-proxy.

[ ![Service mesh ingress through a `Gateway` resource](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/gateway-resource.svg)](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/gateway-resource.svg) Service mesh ingress through a `Gateway` resource (click to enlarge)[ ![Gateway resource](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/gateway-route-resources.svg)](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/gateway-route-resources.svg) `Gateway` resource (click to enlarge)

#### What are a `Gateway` scope and merged `Gateway` configuration?

A `Gateway` resource instance represents the ports and configuration specific to traffic received on those ports. The `Gateway` API resource has a parameter, `scope`, that is used to logically group and merge the configuration of two or more `Gateway` resources.

For example, If you want the `Gateway` proxies to listen on ports 80 and 443 to receive HTTP and HTTPS traffic respectively, you create two `Gateway` resources. Configure one `Gateway` resource with port 80, for HTTP traffic, and the other with 443, for HTTPS traffic. Give the `scope` field in each the same value. Cloud Service Mesh dynamically merges the individual configurations of all Gateways that have the same scope. On the data plane side, the Envoy proxies that run in the ingress gateway mode must also present the same scope parameter to Cloud Service Mesh to receive the `Gateway` configuration. Note that you specify the scope when you create the `Gateway` resource, and you specify the same scope as the bootstrap parameter for the proxies.

[ ![Gateway resource merge behavior](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/gateway-merge.svg)](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/gateway-merge.svg) `Gateway` resource merge behavior (click to enlarge)

The following are key considerations for the `Gateway` resource:

  * The `Gateway` scope parameter is mandatory. Specify the scope in the `Gateway` resource and in the bootstrap configuration of the Envoy proxies even when only one `Gateway` exists.
  * Creating a `Gateway` resource does not deploy a service with an Envoy proxy. Deploying the Envoy proxy is a separate step.
  * The `Gateway` resource has a `type` that represents the type of ingress deployment. This field is reserved for future use. The only currently-supported value is `OPEN_MESH`, which is the default value and which cannot be modified.



### Mesh deployments with mixed protocols and data planes

You can have a mixed data plane deployment, with Envoy proxy and proxyless gRPC in the same mesh. When you create such deployments, consider the following.

  * Envoy sidecar deployments support all Routes (`HTTPRoute`, `GRPCRoute`, `TCPRoute`, and `TLSRoute`).
  * Proxyless gRPC deployments only support `GRPCRoute`.
  * `GRPCRoute` is limited to features supported only by gRPC proxyless deployments.



### Supported topologies in multi-project Shared VPC environments

Cloud Service Mesh supports adding `Route` resources that are defined in other projects to a `Mesh` or `Gateway` resource defined in a centralized administration project. Authorized service owners can directly add their service routing configurations to the `Mesh` or `Gateway`.

[ ![Cross-project referencing between Mesh and Route resources](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/cross-ref-mesh-route.svg)](https://docs.cloud.google.com/static/service-mesh/v1.29/docs/images/cross-ref-mesh-route.svg) Cross-project referencing between `Mesh` and `Route` resources (click to enlarge)

In a typical cross-project scenario, you choose a project (host project or centrally controlled administration project) as the mesh administration project where you create a `Mesh` resource. The mesh administration project owner authorizes `Route` resources from other projects to reference the `Mesh` resource, allowing the routing configuration from other projects to be part of the mesh. A mesh data plane, whether Envoy or gRPC, requests configuration from the administration project and receives a union of all of the routes attached to the `Mesh`. For a `Gateway`, the routes are also merged across all `Gateways` that use the same scope.

The `Mesh` administration project can be any project that you choose, and the configuration works as long as the underlying projects have VPC network connectivity, either through Shared VPC or VPC Network Peering.

### IAM permissions and roles

The following are the IAM permissions that are required to securely get, create, update, delete, list, and use the `Mesh` and `Route` resources.

  * Mesh administrators need to have `networkservices.mesh.*` permissions.
  * Gateway administrators need to have `networkservices.gateways.*` permissions.
  * Service owners need to have `networkservices.grpcRoutes.*`, `networkservices.httpRoutes.*`, or `networkservices.tcpRoutes.*` permissions.



Mesh administrators need to grant the `networkservices.mesh.use` permission to service owners so that the service owners can attach their `Route` resources to the `Mesh` resource. The same model applies to `Gateway` resources.

To see all IAM permissions for `Mesh` resources, go to the [IAM permissions reference page](https://docs.cloud.google.com/iam/docs/permissions-reference) and search for `meshes`.

There are no additional predefined roles required. The existing, predefined role [Compute Network Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkAdmin) (`roles/compute.networkAdmin`) has `networkservices.*` permissions by default. You might need to add the previously described permissions to your custom roles.

## Considerations and limitations

  * The Google Cloud console does not support the service routing APIs.
  * Use the [xDS API version 3](https://www.envoyproxy.io/docs/envoy/latest/api/api_supported_versions) or later. 
    * Minimum Envoy version of 1.20.0 (since the service routing APIs are supported only on xDS version 3)
    * Minimum gRPC bootstrap generator version of v0.14.0
  * The `TLSRoute` resource is supported only with Envoy proxies that are deployed as sidecar proxies or gateways.
  * Only Compute Engine VMs with automatic Envoy deployment and GKE Pods with automatic Envoy injection are supported. You cannot use manual deployment with the service routing APIs.
  * The service routing APIs are not backward compatible with the older APIs.
  * When a `TCPRoute` resource is attached to a `Mesh` resource, the port used to match TCP traffic cannot be used to serve anything except the traffic described by this `TCPRoute`. 
    * For example, your deployments might include a `TCPRoute` resource that matches port "8000" and an HttpRoute resource. When both are attached to the same `Mesh` resource, traffic routed by the `HTTPRoute` resource cannot use port 8000 even when the underlying IP addresses are different. This limitation comes from Envoy proxy implementation, which assigns precedence to the port-matched route first.
  * The `Gateway` resource does not provision a managed load balancer and it does not dynamically create an Envoy service.
  * Automatically deployed Envoys serving as ingress gateways must not have the `serving_ports` argument to the `--service-proxy` flag.
  * Automatically deployed Envoy does not support providing a project number different from the project of the VM.



## What's next

  * For information about listing route resources associated with a `Mesh` or `Gateway` resource, see [List `Route` resources](https://docs.cloud.google.com/service-mesh/v1.29/docs/service-routing/list-route-resources).
  * For information about the service routing APIs, read the documentation for the [network services APIs](https://docs.cloud.google.com/service-mesh/v1.29/docs/reference/network-services/rest).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
