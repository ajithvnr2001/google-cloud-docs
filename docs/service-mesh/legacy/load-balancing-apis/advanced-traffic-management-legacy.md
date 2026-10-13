---
url: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/advanced-traffic-management-legacy/
title: Advanced traffic management overview for load balancing APIs \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:05:02.063687+00:00
---

# Advanced traffic management overview for load balancing APIs  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/advanced-traffic-management-legacy/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Advanced traffic management overview for load balancing APIs

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

This document is intended for mesh or platform administrators and service developers who have an intermediate to advanced level of familiarity with Cloud Service Mesh and service mesh concepts and who determine and configure how traffic is managed in a Cloud Service Mesh deployment. This document applies only to the load balancing APIs, not to the service routing APIs. If your Cloud Service Mesh deployment uses the service routing APIs, see [Advanced traffic management overview](https://docs.cloud.google.com/service-mesh/docs/service-routing/advanced-traffic-management).

Cloud Service Mesh provides advanced traffic management capabilities that give you fine-grained control over how traffic is handled. Cloud Service Mesh supports the following use cases:

  * Fine-grained traffic routing of requests to one or more services
  * Weight-based traffic splitting to distribute traffic across multiple services
  * Traffic mirroring policies that send requests to one debugging service and copies to another
  * Fine-tuned traffic distribution across a service's backends for improved load balancing



These advanced traffic management capabilities let you meet your availability and performance objectives. One of the benefits of using Cloud Service Mesh for these use cases is that you can update how traffic is managed without needing to modify your application code.

  * When you use the target HTTP proxy to configure the Envoy proxies to send HTTP requests, all the capabilities in this document are available.

  * When you use proxyless gRPC services or applications with Cloud Service Mesh, some of the capabilities are not available.

  * When you use the target TCP proxy to configure the Envoy proxies to send TCP requests, none of the capabilities are available because there is no URL map in configurations with a target TCP proxy.




For more details, see the [Features](https://docs.cloud.google.com/service-mesh/docs/service-routing/features) page.

To configure advanced traffic management, you use the same routing rule map and backend services resources that you use when setting up Cloud Service Mesh. Cloud Service Mesh, in turn, configures your Envoy proxies and proxyless gRPC applications to enforce the advanced traffic management policies that you set up.

At a high level, you do the following:

  1. Configure the routing rule map to do the following, based on the characteristics of the outbound request:

     1. Select the backend service to which requests are routed.

     2. Optionally, perform additional actions.

  2. Configure the backend service to control how traffic is distributed to backends and endpoints after a destination service is selected.




## Filtering configuration

One of Cloud Service Mesh's core responsibilities is to generate configuration information from the forwarding rule, target proxy, and URL map, and then send that information to Cloud Service Mesh clients, for example, Envoy proxies and gRPC applications. Cloud Service Mesh controls your service mesh by sending configuration information to its clients that tells them how to behave and how to route traffic—Cloud Service Mesh is the _control plane_.

When you create or update configuration information in Cloud Service Mesh, Cloud Service Mesh translates this configuration into a language that its clients can understand. By default, Cloud Service Mesh shares this configuration with all of its clients. In some cases, you might want to tailor which Cloud Service Mesh clients receive specific configuration information, in other words, filter the configuration to specific clients.

While this is an advanced capability, the following examples illustrate when filtering configuration can help you:

  * Your organization uses the Shared VPC networking model, and multiple teams use Cloud Service Mesh in different service projects. If you want to isolate your configuration from other service projects, you can filter the configuration so that specific Cloud Service Mesh clients receive only a subset of the configuration.
  * You have a very large number of route rules and services configured in Cloud Service Mesh and you want to avoid sending an unusually large amount of configuration to every Cloud Service Mesh client. Keep in mind that a client that needs to evaluate an outbound request by using a large, complex configuration might perform less well than a client that only needs to evaluate a request by using a streamlined configuration.



Configuration filtering is based on the concept of _metadata filters_ :

  1. When a Cloud Service Mesh client connects, it presents information from its bootstrap file to Cloud Service Mesh.
  2. This information contains the contents of metadata fields, in the form of key-value pairs, that you specify in the bootstrap file when you deploy your Envoy proxies and gRPC applications.
  3. You can add metadata filters on the forwarding rule. The entire configuration linked to the forwarding rule is filtered.
  4. You can add metadata filters on the URL map. The metadata filter is applied on a per path routing basis.
  5. Cloud Service Mesh shares the configuration only with clients that present metadata that matches the metadata filter conditions.



For information about how to configure metadata filters for Envoy, see [Set up config filtering based on `MetadataFilter` match](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/configure-advanced-traffic-management#config-filtering-metadata).

## Traffic routing and actions

In Cloud Service Mesh, the [_routing rule map_](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/routing-rule-maps) refers to the combination of the forwarding rule, target proxy, and URL map resources. All advanced traffic management capabilities related to routing and actions are configured by using the URL map.

The following sections describe the advanced traffic management features that you can set up in your routing rule map.

### Request handling

When a client sends a request, the request is handled as described in the following steps:

  1. The request is matched to a specific routing rule map as follows:

     * If you're using Envoy:

       * The request's destination IP address and port are compared to the IP address and port of forwarding rules in all routing rule maps. Only routing rule maps with forwarding rules that have load-balancing scheme `INTERNAL_SELF_MANAGED` are considered.
       * The forwarding rule that matches the request references a target HTTP or gRPC proxy, which references a URL map. This URL map contains information that is used for routing and actions.
     * If you're using proxyless gRPC:

       * A gRPC client that uses the `xds` name resolution scheme does not perform DNS lookup to resolve the hostname in the channel URI. Instead, such a client resolves the `hostname[:port]` in the target URI by sending an [LDS](https://www.envoyproxy.io/docs/envoy/latest/configuration/listeners/lds) request to Cloud Service Mesh.
       * Only the port of a forwarding rule with load-balancing scheme `INTERNAL_SELF_MANAGED` is compared to the port in the target URI (for example, `xds:///example.hostname:8080`). The IP address of the forwarding rule is not used. The default value of the port is `80` if no port is specified in the target URI.
       * The forwarding rule that matches the request references a target gRPC proxy, which references a URL map. This URL map contains information that is used for routing and actions.
       * If more than one forwarding rules match the request, then the URL map that contains the host rule that matches the `hostname[:port]` in the target URI is used for routing and actions.
  2. When the appropriate URL map is determined, the URL map is evaluated to determine the destination backend service and, optionally, apply actions.

  3. After the destination backend service is selected, traffic is distributed among the backends or endpoints for that destination backend service, based on the configuration in the backend service resource.




The second step is described in the following section, Simple routing based on host and path. The third step is discussed in Advanced routing and actions.

### Simple routing based on host and path

Cloud Service Mesh supports a simplified routing scheme and a more advanced scheme. In the simple scheme, you specify a host and, optionally, a path. The request's host and path are evaluated to determine the service to which a request should be routed:

  * The request's host is the domain name portion of a URL—for example, the host portion of the URL `http://example.com/video/` is `example.com`.
  * The request's path is the part of the URL that follows the hostname—for example, the path portion of the URL `http://example.com/video/` is `/video`.



You set up simple routing based on host and path in the routing rule map, which consists of the following:

  * A global forwarding rule
  * A target HTTP proxy, a target HTTPS proxy, or a target gRPC proxy
  * A URL map



Most of the configuration is done in the URL map. After you create the initial routing rule map, you only need to modify the URL map portion of the routing rule map. In the following diagram, path rules have actions similar to the actions in the next diagram.

[ ![Routing based on host and path resources.](https://docs.cloud.google.com/static/service-mesh/docs/images/td-simple-routing.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/td-simple-routing.svg) Routing based on host and path resources (click to enlarge)

The simplest rule is a _default rule_ , in which you only specify a wildcard (`*`) host rule and a path matcher with a default service. After you create the default rule, you can add additional rules that specify different hosts and paths. Outbound requests are evaluated against these rules as follows:

  * If a request's host (such as `example.com`) matches a host rule:

    1. The path matcher is evaluated next.
    2. Each path matcher contains one or more path rules that are evaluated against the request's path.
    3. If a match is found, the request is routed to the service specified in the path rule.
    4. If the host rule matches but no path rules match, requests are routed to a default service that each path matcher contains.
  * If the request does not match any of the host rules that you specified, it is routed to the service specified in the default rule.




For more information about the URL map's resource fields and how they work, see the [`urlMaps` REST API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps) page.

### Advanced routing and actions

If you want to do more than route a request based on the request's host and path, you can set up advanced rules to route requests and perform actions.

[ ![Advanced routing.](https://docs.cloud.google.com/static/service-mesh/docs/images/td-advanced-routing-actions.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/td-advanced-routing-actions.svg) Advanced routing (click to enlarge)

At a high level, advanced routing and actions work as follows:

  1. As with simple routing, the request's host is compared to the host rules that you configure in the URL map. If a request's host matches a host rule, the host rule's path matcher is evaluated.
  2. The path matcher contains one or more route rules that are evaluated against the request. These route rules are evaluated in priority order by matching the request attributes (host, path, header, and query parameters) according to specific match conditions—for example, prefix match.
  3. After a route rule is selected, you can apply actions. The default action is to route the request to a single destination service, but you can configure other actions as well.



#### Advanced routing

Advanced routing is similar to simple routing described previously, except that you can specify rule priority and additional match conditions.

With advanced routing, you must specify a unique priority for each rule. This priority determines the order in which route rules are evaluated, with lower priority values taking precedence over higher priority values. After a request matches a rule, the rule is applied and other rules are ignored.

Advanced routing also supports additional match conditions. For example, you can specify that a rule matches a request's header if the header's name matches exactly or only partially—for example, based on prefix or suffix. A rule can match based on evaluating the header name against a regular expression or on other criteria such as checking for the presence of a header.

For additional match conditions and details for `headerMatches` and `queryParameterMatches`, see the [`urlMaps` REST API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps) page.

By combining host, path, header, and query parameters with priorities and match conditions, you can create highly expressive rules that fit your exact traffic management requirements. For details, see the following table.

| HTTP-based application | gRPC-based application  
---|---|---  
**HTTP hosts versus gRPC hosts** | The host is the domain name portion of the URL that the application calls out to. For example, the host portion of the URL `http://example.com/video/` is `example.com`. | The host is the name that a client uses in the channel URI to connect to a specific service. For example, the host portion of the channel URI `xds:///example.com` is `example.com`.  
**HTTP paths versus gRPC paths** | The path is the part of the URL that follows the hostname. For example, the path portion of the URL `http://example.com/video` is `/video`. | The path is in the `:path` header of the HTTP/2 request and looks like `/SERVICE_NAME/METHOD_NAME`. For example, if you call the `Download` method on the `Example` gRPC service, the contents of the `:path` header looks like `/Example/Download`.  
**Other gRPC headers (metadata)** |  | gRPC supports sending [metadata](https://grpc.io/docs/what-is-grpc/core-concepts/#metadata) between the gRPC client and gRPC server to provide additional information about an RPC call. This metadata is in the form of key-value pairs that are carried as headers in the HTTP/2 request.  
  
#### Actions

Cloud Service Mesh lets you specify actions that your Envoy proxies or proxyless gRPC applications take when handling a request. The following actions can be configured by using Cloud Service Mesh.

**Note:** All the following capabilities are available when you use Envoy with Cloud Service Mesh. Some of the capabilities are not yet available when you use proxyless gRPC applications with Cloud Service Mesh. For more details, see the [Features](https://docs.cloud.google.com/service-mesh/docs/service-routing/features) page and the [Limitations with proxyless gRPC](https://docs.cloud.google.com/service-mesh/docs/service-routing/limitations-proxyless) page.Action | API field name | Description  
---|---|---  
Redirects | `urlRedirect` | Returns a configurable 3xx response code. It also sets the `Location` response header with the appropriate URI, replacing the host and path as specified in the redirect action.   
URL rewrites | `urlRewrite` | Rewrites the hostname portion of the URL, the path portion of the URL, or both, before sending a request to the selected backend service.   
Header transformations | `headerAction` | Adds or removes request headers before sending a request to the backend service. Can also add or remove response headers after receiving a response from the backend service.   
Traffic mirroring | `requestMirrorPolicy` | In addition to forwarding the request to the selected backend service, sends an identical request to the configured mirror backend service on a _[fire and forget](https://www.envoyproxy.io/docs/envoy/latest/api-v3/config/route/v3/route_components.proto.html?highlight=mirror#envoy-v3-api-msg-config-route-v3-routeaction-requestmirrorpolicy)_ basis. The load balancer doesn't wait for a response from the backend to which it sends the mirrored request. Mirroring is useful for testing a new version of a backend service. You can also use it to debug production errors on a debug version of your backend service rather than on the production version.  
Weight-based traffic splitting | `weightedBackendServices` | Allows traffic for a matched rule to be distributed to multiple backend services, proportional to a user-defined weight assigned to the individual backend service. This capability is useful for configuring staged deployments or A/B testing. For example, the route action could be configured such that 99% of the traffic is sent to a service that's running a stable version of an application, while 1% of the traffic is sent to a separate service that's running a newer version of that application.  
Retries | `retryPolicy` | Configures the conditions under which the load balancer retries failed requests, how long the load balancer waits before retrying, and the maximum number of retries permitted.   
Timeout | `timeout` | Specifies the timeout for the selected route. Timeout is computed from the time that the request is fully processed up until the time that the response is fully processed. Timeout includes all retries.   
Fault injection | `faultInjectionPolicy` | Introduces errors when servicing requests to simulate failures, including high latency, service overload, service failures, and network partitioning. This feature is useful for testing the resiliency of a service to simulated faults.   
Security policies | `corsPolicy` | Cross-origin resource sharing (CORS) policies handle settings for enforcing CORS requests.   
  
For more information about actions and how they work, see the [`urlMaps` REST API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps) page.

In each route rule, you can specify one of the following route actions (referred to as **Primary actions** in the Google Cloud console):

  * Route traffic to a single service (`service`)
  * Split traffic between multiple services (`weightedBackendServices`)
  * Redirect URLs (`urlRedirect`)



In addition, you can combine any one of the previously mentioned route actions with one or more of the following route actions (referred to as **Add-on actions** in the Google Cloud console):

  * Manipulate request/response headers (`headerAction`)
  * Mirror traffic (`requestMirrorPolicy`)
  * Rewrite URL host, path, or both (`urlRewrite`)
  * Retry failed requests (`retryPolicy`)
  * Set timeout (`timeout`)
  * Introduce faults to a percentage of the traffic (`faultInjectionPolicy`)
  * Add CORS policy (`corsPolicy`)



Because actions are associated with specific route rules, the Envoy proxy or proxyless gRPC application can apply different actions based on the request that it is handling.

## Distributing traffic among a service's backends

As discussed in Request handling, when a client handles an outbound request, it first selects a destination service. After it selects a destination service, it needs to figure out which backend or endpoint should receive the request.

[ ![Distributing traffic among backends.](https://docs.cloud.google.com/static/service-mesh/docs/images/td-distribute-backends.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/td-distribute-backends.svg) Distributing traffic among backends (click to enlarge)

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
  
For more information about different traffic distribution options and how they work, see the [`backendServices` REST API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices) page.

## Use case examples

Advanced traffic management addresses many use cases. This section provides a few high-level examples.

You can find more examples, including sample code, in the [Configuring advanced traffic management](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/configure-advanced-traffic-management) and [Setting up proxyless gRPC services with advanced traffic management](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management) guides.

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

[ ![Cloud Service Mesh load balancing.](https://docs.cloud.google.com/static/service-mesh/docs/images/atm-least-request.svg)](https://docs.cloud.google.com/static/service-mesh/docs/images/atm-least-request.svg) Cloud Service Mesh load balancing(click to enlarge)

## What's next

  * To read more about URL maps, see [URL maps overview](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts) and [Use URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map).
  * To direct traffic from outside your mesh into your mesh, see [Ingress traffic for your mesh](https://docs.cloud.google.com/service-mesh/docs/service-routing/ingress-traffic).
  * To set up features with sidecar proxy deployments, see [Configure advanced traffic management with Envoy](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/configure-advanced-traffic-management).
  * To set up features with proxyless gRPC deployments, see [Configure advanced traffic management with proxyless gRPC services](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
