---
url: https://docs.cloud.google.com/service-mesh/docs/service-routing/advanced-traffic-management/
title: Advanced traffic management overview \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:31:46.256943+00:00
---

# Advanced traffic management overview  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/service-routing/advanced-traffic-management/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Advanced traffic management overview

This document is intended for mesh or platform administrators and service developers who have an intermediate to advanced level of familiarity with Cloud Service Mesh and service mesh concepts and who determine and configure how traffic is managed in a Cloud Service Mesh deployment.

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

Cloud Service Mesh provides advanced traffic management capabilities that give you granular control over how traffic is handled. Cloud Service Mesh supports the following use cases:

  * Fine-grained traffic routing of requests to one or more services.
  * Weight-based traffic splitting to distribute traffic across multiple services.
  * Traffic mirroring policies that send requests to one debugging service and copies to another. Traffic mirroring is not supported with the `TCPRoute` or the `TLSRoute` resource.
  * Fine-tuned traffic distribution across a service's backends for improved load balancing.



These advanced traffic management capabilities let you meet your availability and performance objectives. One of the benefits of using Cloud Service Mesh for these use cases is that you can update how traffic is managed without needing to modify your application code.

Traffic management in a Cloud Service Mesh service mesh relies on the following resources:

  * [`Mesh`](https://docs.cloud.google.com/service-mesh/docs/service-routing/service-routing-overview#mesh-resource) resource, which identifies the service mesh and represents the component that is responsible for forwarding traffic and applying policies. The `Mesh` resource also identifies the traffic interception port.
  * [`Gateway`](https://docs.cloud.google.com/service-mesh/docs/service-routing/service-routing-overview#gateway-resource) resource, which identifies middle proxies and represents the component that listens on a list of IP address:port pairs, forwards traffic, and applies policies.
  * [`Route`](https://docs.cloud.google.com/service-mesh/docs/service-routing/service-routing-overview#route-resource) resource, which can be one of several types, and which contains traffic routing information for the mesh. `Route` resources identify hostnames and ports that clients can use to route traffic to backend services. The following are the types of `Route` resources: 
    * `HTTPRoute`, which is available only in meshes using Envoy proxies. When you use the `HTTPRoute` resource to configure the Envoy proxies to send HTTP requests, all the capabilities in this document are available.
    * `TCPRoute`, which is available only in meshes using Envoy proxies.
    * `TLSRoute`, which is available only in meshes using Envoy proxies.
    * `GRPCRoute`, which is available in meshes using Envoy sidecar proxies and proxyless gRPC. When you use proxyless gRPC services or applications with Cloud Service Mesh, some of the capabilities described in this document are not available.
  * [Backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service), with which `Route` resources are associated.



## Configuration

To configure advanced traffic management, you use the same `Route` and backend services resources that you use when setting up Cloud Service Mesh. Cloud Service Mesh, in turn, configures your Envoy proxies and proxyless gRPC applications to enforce the advanced traffic management policies that you set up.

At a high level, you do the following:

  1. Configure a `Mesh` resource to identify the service mesh.
  2. Configure `Route` resources to do the following, based on the characteristics of the outbound request:

     1. Select the backend service to which requests are routed.

     2. Optionally, perform additional actions.

  3. Configure the backend service to control how traffic is distributed to backends and endpoints after a destination service is selected.




## Traffic routing and actions

In Cloud Service Mesh, traffic is routed based on values in the `Mesh` resource, `Route` resource, and backend service resource. All advanced traffic management capabilities related to routing and actions are configured by using the `Route` objects.

The following sections describe the advanced traffic management features that you can set up in the `Route` objects.

### Request handling

When a client sends a request, the request is handled as described in the following steps:

  1. The request is matched to a specific `Route` resource as follows:

     * If you're using Envoy: 
       * The host header in the HTTP request is matched against the `hostnames` field in each `HTTPRoute` or `GRPCRoute`resource to select the correct `Route` resource for the request. Only the `HTTPRoute` and `GRPCRoute` resources have the `hostnames` field.
       * The IP address is matched for routing TCP traffic using `TCPPRoute`.
       * SNI and ALPN are used for TLS passthrough using `TLSRoute`.
       * The `HTTPRoute` and `GRPCRoute` resources associate with a `Mesh` or a `Gateway` must have unique hostnames. If you try to attach multiple routes that have conflicting hostnames, the configuration is rejected.
       * Similarly, the `IP:Port` field of the `TCPRoute` must be unique or the configuration is rejected.
       * Similarly, SNI and ALPN must be unique for the `TLSRoute`.
       * If there are overlapping hostnames, such as `a.example.com` and `*.example.com`, the request matches the more specific route.
     * If you're using proxyless gRPC: 
       * Proxyless gRPC clients use the `xds` name resolution scheme. They resolve the `hostname[:port]` in the target URI by sending a request to Cloud Service Mesh.
       * Only the port of a `GRPCRoute` resource is compared to the port in the target URI (for example, `xds:///example.hostname:8080`). The target URI must exactly match the string in the `hostnames` field of the `GRPCRoute`.
  2. The `Route` resource can contain further routing information and rules.

  3. After the destination backend service is selected, traffic is distributed among the backends or endpoints for that destination backend service, based on the configuration in the backend service resource.




The second step is described in the following section, Simple routing based on host and path. The third step is discussed in Advanced routing and actions.

### Simple routing based on host and path

Cloud Service Mesh supports a simplified routing scheme and a more advanced scheme. In the simple scheme, you specify a host and, optionally, a path. The request's host and path are evaluated to determine the backend service to which the request is routed.

  * The request's host is the domain name portion of a URL—for example, the host portion of the URL `http://example.com/video/` is `example.com`.
  * The request's path is the part of the URL that follows the hostname—for example, the path portion of the URL `http://example.com/video/` is `/video`.



You set up simple routing based on host and path in the routing rule map, which consists of the following:

  * A global `Mesh`
  * An `HTTPRoute` or a `GRPCRoute`



Most of the configuration is done in the `HTTPRoute`. After you create the initial routing rule map, you only need to modify the `HTTPRoute` resource.

The simplest rule is a _default rule_ , in which you only specify a wildcard (`*`) host rule and a path matcher with a default service. After you create the default rule, you can add additional rules that specify different hosts and paths. Outbound requests are evaluated against these rules as follows:

  * If a request's host (such as `example.com`) matches the hostname of `HTTPRoute`:

    1. The `RouteRule` is evaluated next. The `RouteRule` specifies how to match traffic and how to route traffic when traffic is matched.
    2. Each `RouteRule` contains one or more route matches that are evaluated against the request's path.
    3. If a match is found, the request is routed to the service specified in the `RouteAction`.



For more information about the `HTTPRoute`'s resource fields and how they work, see the [network service API documentation](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest).

### Advanced routing and actions

If you want to do more than route a request based on the request's host and path, you can set up advanced rules to route requests and perform actions.

At a high level, advanced routing and actions work as follows:

  1. As with simple routing, the request's host is compared to the host rules that you configure in the `HTTPRoute` or `GRPCRoute`. If a request's host matches the hostname, the `HTTPRoute` or `GRPCRoute` is evaluated.
  2. After a route is selected, you can apply actions.



#### Advanced routing

Advanced routing is similar to simple routing described previously, except that you can specify additional match conditions. For example, you can specify that a rule matches a request's header if the header's name matches exactly or only partially—for example, based on prefix or suffix. A rule can match based on evaluating the header name against a regular expression or on other criteria such as checking for the presence of a header.

For additional match conditions and details for `headerMatches` and `queryParameterMatches`, see the [`network services` REST API](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest#rest-resource:-v1.projects.locations.httproutes) page.

By combining host, path, header, and query parameters with match conditions, you can create highly expressive rules that fit your exact traffic management requirements. For details, see the following table.

| HTTP-based application | gRPC-based application  
---|---|---  
**HTTP hosts versus gRPC hosts** | The host is the domain name portion of the URL that the application calls out to. For example, the host portion of the URL `http://example.com/video/` is `example.com`. | The host is the name that a client uses in the channel URI to connect to a specific service. For example, the host portion of the channel URI `xds:///example.com` is `example.com`.  
**HTTP paths versus gRPC paths** | The path is the part of the URL that follows the hostname. For example, the path portion of the URL `http://example.com/video` is `/video`. | The path is in the `:path` header of the HTTP/2 request and looks like `/SERVICE_NAME/METHOD_NAME`. For example, if you call the `Download` method on the `Example` gRPC service, the contents of the `:path` header looks like `/Example/Download`.  
**Other gRPC headers (metadata)** |  | gRPC supports sending [metadata](https://grpc.io/docs/what-is-grpc/core-concepts/#metadata) between the gRPC client and gRPC server to provide additional information about an RPC call. This metadata is in the form of key-value pairs that are carried as headers in the HTTP/2 request.  
  
#### Actions

Cloud Service Mesh lets you specify actions that your Envoy proxies or proxyless gRPC applications take when handling a request. The following actions can be configured by using Cloud Service Mesh.

**Note:** All the following capabilities are available when you use Envoy with Cloud Service Mesh. Some of the capabilities are not available when you use proxyless gRPC applications with Cloud Service Mesh. For more details, see the [Features](https://docs.cloud.google.com/service-mesh/docs/service-routing/features) page and the [Limitations with proxyless gRPC](https://docs.cloud.google.com/service-mesh/docs/service-routing/limitations-proxyless) page.Action | API field name | Description  
---|---|---  
Redirects | `redirect [pathredirect?]` | Returns a configurable 3xx response code. It also sets the `Location` response header with the appropriate URI, replacing the host and path as specified in the redirect action.   
URL rewrites | `urlRewrite` | Rewrites the hostname portion of the URL, the path portion of the URL, or both, before sending a request to the selected backend service.   
Header transformations | `requestHeaderModifier/responseHeaderModifier?` | Adds or removes request headers before sending a request to the backend service. Can also add or remove response headers after receiving a response from the backend service.   
Traffic mirroring | `requestMirrorPolicy` | In addition to forwarding the request to the selected backend service, sends an identical request to the configured mirror backend service on a _[fire and forget](https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/route/v3/route_components.proto.html?highlight=mirror#envoy-v3-api-msg-config-route-v3-routeaction-requestmirrorpolicy)_ basis. The load balancer doesn't wait for a response from the backend to which it sends the mirrored request. Mirroring is useful for testing a new version of a backend service. You can also use it to debug production errors on a debug version of your backend service rather than on the production version.  
Weight-based traffic splitting | `weightDestination.serviceName` | Allows traffic for a matched rule to be distributed to multiple backend services, proportional to a user-defined weight assigned to the individual backend service. This capability is useful for configuring staged deployments or A/B testing. For example, the route action could be configured such that 99% of the traffic is sent to a service that's running a stable version of an application, while 1% of the traffic is sent to a separate service that's running a newer version of that application.  
Retries | `retryPolicy` | Configures the conditions under which the load balancer retries failed requests, how long the load balancer waits before retrying, and the maximum number of retries permitted.   
Timeout | `timeout` | Specifies the timeout for the selected route. Timeout is computed from the time that the request is fully processed up until the time that the response is fully processed. Timeout includes all retries.   
Fault injection | `faultInjectionPolicy` | Introduces errors when servicing requests to simulate failures, including high latency, service overload, service failures, and network partitioning. This feature is useful for testing the resiliency of a service to simulated faults.   
Security policies | `corsPolicy` | Cross-origin resource sharing (CORS) policies handle settings for enforcing CORS requests.   
  
For more information about actions and how they work, see the [network services API](https://networkservices.googleapis.com/$discovery/rest?version=v1) page.

In each route rule, you can specify one of the following route actions:

  * Route traffic to a single service (`destination.serviceName`)
  * Split traffic between multiple services (`destination.weight`)
  * Redirect URLs (`redirect`)



In addition, you can combine any one of the previously mentioned route actions with one or more of the following route actions (referred to as **Add-on actions** in the Google Cloud console):

  * Manipulate request or response headers (`requestHeaderModifier/responseHeaderModifier`)
  * Mirror traffic (`requestMirrorPolicy`)
  * Rewrite URL host, path, or both (`urlRewrite`)
  * Retry failed requests (`retryPolicy`)
  * Set timeout (`timeout`)
  * Introduce faults to a percentage of the traffic (`faultInjectionPolicy`)
  * Add CORS policy (`corsPolicy`)



Because actions are associated with specific rules, the Envoy proxy or proxyless gRPC application can apply different actions based on the request that it is handling.

## Distribute traffic among a service's backends

As discussed in Request handling, when a client handles an outbound request, it first selects a destination service. After it selects a destination service, it needs to figure out which backend or endpoint should receive the request.

[ ![Distributing traffic among backends.](https://docs.cloud.google.com/static/service-mesh/docs/images/atm-distribute-traffic.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/atm-distribute-traffic.svg) Distributing traffic among backends (click to enlarge)

In the preceding diagram, the **Rule** has been simplified. The **Rule** is typically a host rule, path matcher, and one or more path or route rules. The destination service is the **(Backend) Service**. **Backend 1** , **…** , and **Backend n** receive and handle the request. These backends might be, for example, Compute Engine virtual machine (VM) instances that host your server-side application code.

By default, the client that handles the request sends requests to the nearest healthy backend that has capacity. To avoid overloading a specific backend, it uses the round robin load-balancing algorithm to load balance subsequent requests across other backends of the destination service. In some cases, however, you might want more fine-grained control over this behavior.

### Load balancing, session affinity, and protecting backends

You can set the following traffic distribution policies on each service.

Policy | API field name | Description  
---|---|---  
Load-balancing mode | `balancingMode` | Controls how a network endpoint group (NEG) or a managed instance group (MIG) is selected after a destination service has been selected. You can configure the balancing mode to distribute load based on concurrent connections and request rate.   
Load-balancing policy | `localityLbPolicy` | Sets the load-balancing algorithm that is used to distribute traffic among backends within a NEG or MIG. To optimize performance, you can choose from various algorithms (such as round robin or least request).   
Session affinity | `sessionAffinity` | Provides a best-effort attempt to send requests from a particular client to the same backend for as long as the backend is healthy and has capacity. Cloud Service Mesh supports four session affinity options: client IP address, HTTP cookie-based, HTTP header-based, and generated cookie affinity (which Cloud Service Mesh generates itself).  
Consistent hash | `consistentHash` | Provides soft session affinity based on HTTP headers, cookies, or other properties.   
Circuit breakers | `circuitBreakers` | Sets upper limits on the volume of connections and requests per connection to a backend service.   
Outlier detection | `outlierDetection` | Specifies the criteria to (1) remove unhealthy backends or endpoints from MIGs or NEGs and (2) add a backend or endpoint back when it is considered healthy enough to receive traffic again. The health check associated with the service determines whether a backend or endpoint is considered healthy.   
  
For more information about different traffic distribution options and how they work, see the following documents:

  * [`backendServices` REST API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices) page
  * [Backend services overview](https://docs.cloud.google.com/load-balancing/docs/backend-service).



## Use case examples

Advanced traffic management addresses many use cases. This section provides a few high-level examples.

You can find more examples, including sample code, in [Configure advanced traffic management with Envoy](https://docs.cloud.google.com/service-mesh/docs/service-routing/advanced-traffic-management) and [Configure advanced traffic management with proxyless gRPC services](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management).

### Fine-grained traffic routing for personalization

You can route traffic to a service based on the request's parameters. For example, you might use this service to provide a more personalized experience for Android users. In the following diagram, Cloud Service Mesh configures your service mesh to send requests with the `user-agent:Android` header to your Android service instead of to your generic service.

[ ![Routing based on the user-agent header set to Android.](https://docs.cloud.google.com/static/service-mesh/docs/images/atm-personalization.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/atm-personalization.svg) Routing based on the `user-agent` header set to `Android` (click to enlarge)

### Weight-based traffic splitting for safer deployments

Deploying a new version of an existing production service can be risky. Even after your tests pass in a test environment, you might not want to route all your users to the new version right away.

Cloud Service Mesh lets you define weight-based traffic splits to distribute traffic across multiple services. For example, you can send 1% of traffic to the new version of your service, monitor that everything works, and then gradually increase the proportion of traffic going to the new service.

[ ![Cloud Service Mesh weight-based traffic splitting.](https://docs.cloud.google.com/static/service-mesh/docs/images/atm-weight-based-split.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/atm-weight-based-split.svg) Cloud Service Mesh weight-based traffic splitting (click to enlarge)

### Traffic mirroring for debugging

When you're debugging an issue, it might be helpful to send copies of production traffic to a debugging service. Cloud Service Mesh lets you set up request mirroring policies so that requests are sent to one service and copies of those requests are sent to another service.

[ ![Cloud Service Mesh traffic mirroring.](https://docs.cloud.google.com/static/service-mesh/docs/images/atm-mirroring.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/atm-mirroring.svg) Cloud Service Mesh traffic mirroring (click to enlarge)

### Fine-tuned load balancing for performance

Depending on your application characteristics, you might find that you can improve performance and availability by fine-tuning how traffic gets distributed across a service's backends. With Cloud Service Mesh, you can apply advanced load-balancing algorithms so that traffic is distributed according to your needs.

The following diagram, in contrast to previous diagrams, shows both a destination backend service (**Production Service**) and the backends for that backend service (**Virtual Machine 1** , **Virtual Machine 2** , **Virtual Machine 3**). With advanced traffic management, you can configure how a destination backend service is selected and how traffic is distributed among the backends for that destination service.

[ ![Cloud Service Mesh load balancing.](https://docs.cloud.google.com/static/service-mesh/docs/images/atm-least-request.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/atm-least-request.svg) Cloud Service Mesh load balancing (click to enlarge)

For more information about load balancing with Cloud Service Mesh, see [Advanced load balancing overview](https://docs.cloud.google.com/service-mesh/docs/service-routing/advanced-load-balancing-overview).

## What's next

  * To direct traffic from outside your mesh into your mesh, see [Ingress traffic for your mesh](https://docs.cloud.google.com/service-mesh/docs/service-routing/ingress-traffic).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
