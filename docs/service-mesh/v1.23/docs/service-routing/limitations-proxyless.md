---
url: https://docs.cloud.google.com/service-mesh/v1.23/docs/service-routing/limitations-proxyless/
title: Proxyless gRPC limitations \u00a0|\u00a0 Cloud Service Mesh v1.23 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:53:07.042207+00:00
---

# Proxyless gRPC limitations  |  Cloud Service Mesh v1.23  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.23/docs/service-routing/limitations-proxyless/

You are viewing archived v1.23 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ v1.23 ](https://docs.cloud.google.com/service-mesh/v1.23/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.23/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Proxyless gRPC limitations

This document describes limitations that apply to Cloud Service Mesh with proxyless gRPC applications. For information about _limits_ , see [Quotas and limits](https://docs.cloud.google.com/service-mesh/v1.23/quotas).

Limitations on forwarding rules, URL maps, and target proxies apply only to Cloud Service Mesh with the Google Cloud load balancing APIs.

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

## General limitations

The limitations of Cloud Service Mesh with proxyless gRPC applications include the following:

  * You cannot configure backend services and routing rule maps with the gRPC protocol in the Google Cloud console. For these resources, the Google Cloud console is read-only.

  * Proxyless gRPC supports endpoint discovery, routing, load balancing, load reporting, and many advanced traffic management features.

    * For the minimum gRPC version required to support some [advanced traffic management](https://docs.cloud.google.com/service-mesh/v1.23/docs/service-routing/advanced-traffic-management) features, see [Supported gRPC versions and languages](https://docs.cloud.google.com/service-mesh/v1.23/docs/service-routing/prepare-proxyless-grpc#supported_grpc_versions_and_languages).

    * For your gRPC applications that need unsupported advanced traffic management features, use the DNS name resolver instead of the xDS resolver and deploy with sidecar proxies that are supported with Cloud Service Mesh. In your target gRPC proxy, set the `validateForProxyless` field to `FALSE` so that you can configure features that are not yet supported by gRPC but that are available in Cloud Service Mesh with the use of sidecar proxies.

  * Proxyless gRPC supports only round-robin and ring hash load balancing policies. Other [load-balancing policies](https://docs.cloud.google.com/service-mesh/v1.23/docs/service-routing/features#load_balancing) are not supported.

    * Cloud Service Mesh provides a prioritized weighted list of localities—one instance group or one network endpoint group (NEG)—to the gRPC client. Cloud Service Mesh calculates this list based on the closest available zone, its capacity, and the balancing mode of the backend service.
    * For a particular request, the gRPC client picks one or more localities based on the priority and weight and does round-robin or ring hash-based load balancing to the backends within those localities.
  * The failover from one zone (locality) to another starts when the current zone capacity falls under 50%. You can't configure this threshold.

  * In some cases, the configuration commands related to a target gRPC proxy and a forwarding rule that references a target gRPC proxy might take up to a minute.

  * [Hybrid connectivity NEGs (`NON_GCP_PRIVATE_IP_PORT` NEGs)](https://docs.cloud.google.com/service-mesh/v1.23/docs/service-routing/multi-environment-overview) are not supported with proxyless gRPC clients.




## URL map limitations

The following [URL map](https://docs.cloud.google.com/compute/docs/reference/rest/beta/urlMaps) traffic management features are supported with proxyless gRPC services.

Features supported in the `pathMatcher` of `hostRules`:
    
    
    pathMatcher
      name
      description
      defaultService
      defaultRouteAction
         weightedBackendServices
           backendService
           weight
        retryPolicy
           retryConditions
           numRetries
        faultInjectionPolicy
        maxStreamDuration
      pathRules
        service
        routeAction
          weightedBackendServices
             backendService
             weight
          retryPolicy
             retryConditions
             numRetries
          faultInjectionPolicy
          maxStreamDuration
        paths
      routeRules
        priority
        description
        matchRules
            prefixMatch
            fullPathMatch
            headerMatches
            metadataFilters
        service
        routeAction
          weightedBackendServices
             backendService
             weight
          retryPolicy
             retryConditions
             numRetries
          faultInjectionPolicy
          maxStreamDuration
    

The following URL map limitations apply when you use proxyless gRPC services:

  * Wildcard characters in the host rules and default rules of a URL map, including the implicitly created `*` host rule of a URL map, are not supported. Such entries are skipped when host matching is done.

  * The following features are not supported:

    * `queryParameterMatches` in `routeRules`
    * `headerAction`, `urlRewrite`, `requestMirrorPolicy`, `corsPolicy`, and `urlRedirect` route actions
    * `timeout` route action; use `maxStreamDuration` instead of `timeout`
    * `perTryTimeout` in `retryPolicy`
    * `retryConditions` in `retryPolicy` except one or more conditions of `cancelled`, `deadline-exceeded`, `internal`, `resource-exhausted`, and `unavailable`
    * The `defaultService`, `defaultRouteAction`, `defaultUrlRedirect`, and `headerAction` of the URL map are not used by proxyless gRPC services. If a matching host rule is not found when a proxyless gRPC client looks up a service name, Cloud Service Mesh returns a name lookup error instead of using the default service or action of the URL map.
    * `headerAction` in `weightedBackendServices`
  * In URL map header match rules, only non-binary user-specified [custom metadata](https://github.com/grpc/grpc/blob/master/doc/PROTOCOL-HTTP2.md#requests) and the `content-type` header are supported. The following transport-level headers cannot be used in header matching rules: `:authority`, `:method`, `:path`, `:scheme`, `user-agent`, `accept-encoding`, `content-encoding`, `grpc-accept-encoding`, `grpc-encoding`, `grpc-previous-rpc-attempts`, `grpc-tags-bin`, `grpc-timeout`, and `grpc-trace-bin`.

  * When you update a URL map host rule to change from one backend service to another, traffic might be dropped momentarily while the new configuration is pushed to the clients. To avoid this limitation, configure [traffic splitting with weighted backend services](https://docs.cloud.google.com/service-mesh/v1.23/docs/service-routing/advanced-traffic-management#traffic-splitting). After configuring traffic splitting, slowly shift traffic from the old backend service to the new backend service.




## Target gRPC proxy limitations

When a target gRPC proxy references a URL map, you cannot configure the following URL map features. This is true whether you are using a sidecar proxy or a proxyless gRPC service because these HTTP protocol-specific features don't apply to the gRPC protocol:

  * `queryParameterMatches` match rule
  * `urlRewrite` route action
  * `urlRedirect` route action
  * `corsPolicy` action



## Backend service limitations

The following backend service features are not supported with proxyless gRPC services with a sidecar proxy:

  * `localityLbPolicy` except `LEAST_REQUEST` (with Java clients only), `ROUND_ROBIN`, and `RING_HASH`
  * `sessionAffinity` except `HEADER_FIELD` and `NONE`
  * `consistentHash` except the `httpHeaderName` and `minimumRingSize` fields
  * `affinityCookieTtlSec`
  * `timeoutSec`; use `maxStreamDuration` instead
  * `circuitBreakers` except the `maxRequests` field



Note that a gRPC client will NACK the configuration from Cloud Service Mesh when unsupported values are configured. This will cause configuration for all backend services to be rejected by the client because the xDS protocol requires rejecting all resources in a given response, rather than being able to reject only an individual resource from the response. This will cause the client channel to go into a transient error state until the configuration is fixed. Due to this limitation, you must ensure that all clients support the required value before configuring a feature for a service. For example, if you change the `ROUND_ROBIN` policy to `RING_HASH`, you must ensure that all the clients are upgraded to a version that supports `RING_HASH`.

## Advanced traffic management limitations

You can't configure some advanced traffic management features for proxyless gRPC services with Cloud Service Mesh. For supported features, see the following:

  * [Supported gRPC versions and languages](https://docs.cloud.google.com/service-mesh/v1.23/docs/service-routing/prepare-proxyless-grpc#supported_grpc_versions_and_languages)
  * [Cloud Service Mesh features](https://docs.cloud.google.com/service-mesh/v1.23/docs/service-routing/features), including [load balancing](https://docs.cloud.google.com/service-mesh/v1.23/docs/service-routing/features#load_balancing)



## Limitations with Service Directory

  * Service Directory and Cloud Service Mesh don't guarantee network reachability for clients.
  * A backend service can only reference one of the following:

    * Managed instance group or unmanaged instance group
    * Network endpoint group
    * Service bindings
  * Service Directory services can only be used with global backend services with `load-balancing-scheme=INTERNAL_SELF_MANAGED`.

  * A Service Directory service that is referenced by a service binding can be deleted. If the underlying Service Directory service to which the backend service is attached is deleted, applications that use Cloud Service Mesh cannot send traffic to this service, therefore, requests fail. See [Observability and debugging](https://docs.cloud.google.com/service-mesh/docs/service-directory-observability) for best practices.

  * When you bind a Service Directory service to a backend service, you cannot configure a health check on that backend service.




## What's next

  * To learn about limitations that apply to Cloud Service Mesh, including advanced traffic management limitations, see [Cloud Service Mesh limitations](https://docs.cloud.google.com/service-mesh/v1.23/docs/service-routing/limitations).
  * To find uses cases and architecture patterns for proxyless gRPC services, see the [Proxyless gRPC services overview](https://docs.cloud.google.com/service-mesh/v1.23/docs/service-routing/proxyless-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
