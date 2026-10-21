---
url: https://docs.cloud.google.com/service-mesh/docs/onboarding/api-support/
title: API Support in Managed Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:47:34.970319+00:00
---

# API Support in Managed Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/onboarding/api-support/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# API Support in Managed Cloud Service Mesh

## Overview

This reference lists the Istio and Google Cloud APIs supported by the managed Cloud Service Mesh with `TRAFFIC_DIRECTOR`. Use this guide to verify your configuration before enabling features.

  * **Release Channels** : Refers to GKE release channels, with **Stable** as the highest and **Rapid** as the lowest.
  * **Unsupported** : Not supported by the managed control plane. Unsupported fields are rejected or ignored during configuration translation and result in unsupported and undefined behavior.
  * **Limitations** : Specific behavior to be aware of for the API field due to the implementation that may differ from the API definition.



## DestinationRule (networking.istio.io/v1beta1)

The following sections describe the supported fields for `DestinationRule` resources.

### Root & Top-Level Fields

The following table lists the supported root and top-level fields.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`exportTo` | Stable | **Array of strings** | When `workloadSelector` is set, `exportTo` cannot be exported beyond the local namespace (`.` or current namespace only).  
`host` | Stable | String | Must be a valid DNS name, FQDN, or wildcard domain prefix. Empty domain names are not allowed.  
`workloadSelector.matchLabels` | Stable | Key-value map | Wildcards (`*`) are not allowed in label keys or values. Limits applicability to client workloads in the local namespace.  
  
### Load Balancer Settings (trafficPolicy.loadBalancer)

The following table lists the field-level support for `trafficPolicy.loadBalancer`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`consistentHash.httpCookie.name` | Stable | String | Required when `httpCookie` is configured.  
`consistentHash.httpCookie.path` | Stable | String |   
`consistentHash.httpCookie.ttl` | Stable | Duration |   
`consistentHash.httpHeaderName` | Stable | String | Only one `consistentHash` key strategy can be specified.  
`consistentHash.httpQueryParameterName` | Stable | String | Only one `consistentHash` key strategy can be specified.  
`consistentHash.maglev.tableSize` | Stable | Integer |   
`consistentHash.minimumRingSize` | Stable | Integer | Deprecated. Use `ringHash.minimumRingSize` instead. Cannot be combined with `ringHash` or `maglev`.  
`consistentHash.ringHash.minimumRingSize` | Stable | Integer |   
`consistentHash.useSourceIp` | Stable | Boolean | Only one `consistentHash` key strategy can be specified.  
`localityLbSetting.distribute.from` | **Unsupported** | String |   
`localityLbSetting.distribute.to` | **Unsupported** | Key-value map |   
`localityLbSetting.enabled` | Stable | Boolean |   
`localityLbSetting.failover.from` | Stable | String | Requires `outlierDetection` to be configured on the traffic policy and it is only allowed syntactically to trigger `WATERFALL_BY_ZONE`. Specific routing paths are ignored.  
`localityLbSetting.failover.to` | Stable | String | Requires `outlierDetection` to be configured on the traffic policy and it is only allowed syntactically to trigger `WATERFALL_BY_ZONE`. Specific routing paths are ignored.  
`localityLbSetting.failoverPriority` | **Unsupported** | **Array of strings** |   
`simple` | Stable | String (`ROUND_ROBIN`, `LEAST_CONN`, `RANDOM`, `PASSTHROUGH`, `LEAST_REQUEST`) | `LEAST_CONN` is not supported.  
`warmupDurationSecs` | **Unsupported** | String |   
  
### Connection Pool Settings (trafficPolicy.connectionPool)

The following table lists the field-level support for `trafficPolicy.connectionPool`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`http.h2UpgradePolicy` | Stable | String (`DEFAULT`, `DO_NOT_UPGRADE`, `UPGRADE`) | Cannot be set to `UPGRADE` when `useClientProtocol` is `true`.  
`http.http1MaxPendingRequests` | Stable | Integer | Must be a non-negative integer (>= 0).  
`http.http2MaxRequests` | Stable | Integer | Must be a non-negative integer (>= 0).  
`http.idleTimeout` | Stable | Duration |   
`http.maxRequestsPerConnection` | Stable | Integer | Must be a non-negative integer (>= 0).  
`http.maxRetries` | Stable | Integer | Must be a non-negative integer (>= 0).  
`http.useClientProtocol` | Stable | Boolean | Cannot be `true` when `h2UpgradePolicy` is `UPGRADE`.  
`tcp.connectTimeout` | Stable | Duration |   
`tcp.maxConnectionDuration` | Stable | Duration | Only applied to HTTP/HTTP2/gRPC services; ignored for TCP byte-stream services.  
`tcp.maxConnections` | Stable | Integer | Must be a non-negative integer (>= 0).  
`tcp.tcpKeepalive.interval` | Stable | Duration |   
`tcp.tcpKeepalive.probes` | Stable | Integer |   
`tcp.tcpKeepalive.time` | Stable | Duration |   
  
### Outlier Detection (trafficPolicy.outlierDetection)

The following table lists the field-level support for `trafficPolicy.outlierDetection`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`baseEjectionTime` | Stable | Duration |   
`consecutive5xxErrors` | Stable | Integer |   
`consecutiveErrors` | **Unsupported** | Integer |   
`consecutiveGatewayErrors` | Stable | Integer |   
`consecutiveLocalOriginFailures` | Stable | Integer |   
`interval` | Stable | Duration |   
`maxEjectionPercent` | Stable | Integer |   
`minHealthPercent` | Stable | Integer |   
`splitExternalLocalOriginErrors` | Stable | Boolean |   
  
### TLS Settings (trafficPolicy.tls)

The following table lists the field-level support for `trafficPolicy.tls`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`caCertificates` | Stable | String |   
`clientCertificate` | Stable | String | Required when mode is `MUTUAL`.  
`credentialName` | **Unsupported** | String |   
`insecureSkipVerify` | Stable | Boolean | When `true`, `caCertificates` and `subjectAltNames` must be empty.  
`mode` | Stable | String (`DISABLE`, `SIMPLE`, `MUTUAL`, `ISTIO_MUTUAL`) | `MUTUAL` mode requires `clientCertificate` and `privateKey`.  
`privateKey` | Stable | String | Required when mode is `MUTUAL`.  
`sni` | Stable | String |   
`subjectAltNames` | Stable | **Array of strings** |   
  
### Tunnel Settings (trafficPolicy.tunnel)

The following table lists the field-level support for `trafficPolicy.tunnel`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`tunnel.protocol` | **Unsupported** | String (`CONNECT`, `POST`) |   
`tunnel.targetHost` | **Unsupported** | String |   
`tunnel.targetPort` | **Unsupported** | Integer |   
  
### Port & Load Balancer Settings (trafficPolicy.portLevelSettings.loadBalancer)

The following table lists the field-level support for `trafficPolicy.portLevelSettings.loadBalancer`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`loadBalancer.consistentHash.httpCookie.name` | Stable | String | Required when `httpCookie` is configured.  
`loadBalancer.consistentHash.httpCookie.path` | Stable | String |   
`loadBalancer.consistentHash.httpCookie.ttl` | Stable | Duration |   
`loadBalancer.consistentHash.httpHeaderName` | Stable | String | Only one `consistentHash` key strategy can be specified.  
`loadBalancer.consistentHash.httpQueryParameterName` | Stable | String | Only one `consistentHash` key strategy can be specified.  
`loadBalancer.consistentHash.maglev.tableSize` | Stable | Integer |   
`loadBalancer.consistentHash.minimumRingSize` | Stable | Integer | Deprecated. Use `ringHash.minimumRingSize` instead. Cannot be combined with `ringHash` or `maglev`.  
`loadBalancer.consistentHash.ringHash.minimumRingSize` | Stable | Integer |   
`loadBalancer.consistentHash.useSourceIp` | Stable | Boolean | Only one `consistentHash` key strategy can be specified.  
`loadBalancer.localityLbSetting.distribute.from` | **Unsupported** | String |   
`loadBalancer.localityLbSetting.distribute.to` | **Unsupported** | Key-value map |   
`loadBalancer.localityLbSetting.enabled` | **Unsupported** | Boolean |   
`loadBalancer.localityLbSetting.failover.from` | **Unsupported** | String |   
`loadBalancer.localityLbSetting.failover.to` | **Unsupported** | String |   
`loadBalancer.localityLbSetting.failoverPriority` | **Unsupported** | **Array of strings** |   
`loadBalancer.simple` | Stable | String (`ROUND_ROBIN`, `LEAST_CONN`, `RANDOM`, `PASSTHROUGH`, `LEAST_REQUEST`) | `LEAST_CONN` is not supported.  
`loadBalancer.warmupDurationSecs` | **Unsupported** | String |   
`port.number` | Stable | Integer | Required. Specifies the port number to which these traffic policies apply.  
  
### Connection Pool Settings (trafficPolicy.portLevelSettings.connectionPool)

The following table lists the field-level support for `trafficPolicy.portLevelSettings.connectionPool`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`http.h2UpgradePolicy` | Stable | String (`DEFAULT`, `DO_NOT_UPGRADE`, `UPGRADE`) | Cannot be set to `UPGRADE` when `useClientProtocol` is `true`.  
`http.http1MaxPendingRequests` | Stable | Integer | Must be a non-negative integer (>= 0).  
`http.http2MaxRequests` | Stable | Integer | Must be a non-negative integer (>= 0).  
`http.idleTimeout` | Stable | Duration |   
`http.maxRequestsPerConnection` | Stable | Integer | Must be a non-negative integer (>= 0).  
`http.maxRetries` | Stable | Integer | Must be a non-negative integer (>= 0).  
`http.useClientProtocol` | Stable | Boolean | Cannot be `true` when `h2UpgradePolicy` is `UPGRADE`.  
`tcp.connectTimeout` | Stable | Duration |   
`tcp.maxConnectionDuration` | Stable | Duration | Only applied to HTTP/HTTP2/gRPC services; ignored for TCP byte-stream services.  
`tcp.maxConnections` | Stable | Integer | Must be a non-negative integer (>= 0).  
`tcp.tcpKeepalive.interval` | Stable | Duration |   
`tcp.tcpKeepalive.probes` | Stable | Integer |   
`tcp.tcpKeepalive.time` | Stable | Duration |   
  
### Outlier Detection Settings (trafficPolicy.portLevelSettings.outlierDetection)

The following table lists the field-level support for `trafficPolicy.portLevelSettings.outlierDetection`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`baseEjectionTime` | **Unsupported** | Duration |   
`consecutive5xxErrors` | **Unsupported** | Integer |   
`consecutiveErrors` | **Unsupported** | Integer |   
`consecutiveGatewayErrors` | **Unsupported** | Integer |   
`consecutiveLocalOriginFailures` | **Unsupported** | Integer |   
`interval` | **Unsupported** | Duration |   
`maxEjectionPercent` | **Unsupported** | Integer |   
`minHealthPercent` | **Unsupported** | Integer |   
`splitExternalLocalOriginErrors` | **Unsupported** | Boolean |   
  
### TLS Settings (trafficPolicy.portLevelSettings.tls)

The following table lists the field-level support for `trafficPolicy.portLevelSettings.tls`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`tls.caCertificates` | Stable | String |   
`tls.clientCertificate` | Stable | String | Required when mode is `MUTUAL`.  
`tls.credentialName` | **Unsupported** | String |   
`tls.insecureSkipVerify` | Stable | Boolean | When `true`, `caCertificates` and `subjectAltNames` must be empty.  
`tls.mode` | Stable | String (`DISABLE`, `SIMPLE`, `MUTUAL`, `ISTIO_MUTUAL`) | `MUTUAL` mode requires `clientCertificate` and `privateKey`.  
`tls.privateKey` | Stable | String | Required when mode is `MUTUAL`.  
`tls.sni` | Stable | String |   
`tls.subjectAltNames` | Stable | **Array of strings** |   
  
### Subset Root & Label Settings (subsets)

The following table lists the field-level support for `subsets`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`labels` | Stable | Key-value map | Must conform to Kubernetes label syntax rules to select target endpoints.  
`name` | Stable | String | Required. Must be a valid DNS 1123 label.  
  
### Subset Load Balancer Settings (subsets.trafficPolicy.loadBalancer)

The following table lists the field-level support for `subsets.trafficPolicy.loadBalancer`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`consistentHash.httpCookie.name` | Stable | String | Required when `httpCookie` is configured.  
`consistentHash.httpCookie.path` | Stable | String |   
`consistentHash.httpCookie.ttl` | Stable | Duration |   
`consistentHash.httpHeaderName` | Stable | String | Only one `consistentHash` key strategy can be specified.  
`consistentHash.httpQueryParameterName` | Stable | String | Only one `consistentHash` key strategy can be specified.  
`consistentHash.maglev.tableSize` | Stable | Integer |   
`consistentHash.minimumRingSize` | Stable | Integer | Deprecated. Use `ringHash.minimumRingSize` instead. Cannot be combined with `ringHash` or `maglev`.  
`consistentHash.ringHash.minimumRingSize` | Stable | Integer |   
`consistentHash.useSourceIp` | Stable | Boolean | Only one `consistentHash` key strategy can be specified.  
`localityLbSetting.distribute.from` | **Unsupported** | String |   
`localityLbSetting.distribute.to` | **Unsupported** | Key-value map |   
`localityLbSetting.enabled` | **Unsupported** | Boolean |   
`localityLbSetting.failover.from` | **Unsupported** | String |   
`localityLbSetting.failover.to` | **Unsupported** | String |   
`localityLbSetting.failoverPriority` | **Unsupported** | **Array of strings** |   
`simple` | Stable | String (`ROUND_ROBIN`, `LEAST_CONN`, `RANDOM`, `PASSTHROUGH`, `LEAST_REQUEST`) | `LEAST_CONN` is not supported.  
`warmupDurationSecs` | **Unsupported** | String |   
  
### Subset Connection Pool Settings (subsets.trafficPolicy.connectionPool)

The following table lists the field-level support for `subsets.trafficPolicy.connectionPool`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`http.h2UpgradePolicy` | Stable | String (`DEFAULT`, `DO_NOT_UPGRADE`, `UPGRADE`) | Cannot be set to `UPGRADE` when `useClientProtocol` is `true`.  
`http.http1MaxPendingRequests` | Stable | Integer | Must be a non-negative integer (>= 0).  
`http.http2MaxRequests` | Stable | Integer | Must be a non-negative integer (>= 0).  
`http.idleTimeout` | Stable | Duration |   
`http.maxRequestsPerConnection` | Stable | Integer | Must be a non-negative integer (>= 0).  
`http.maxRetries` | Stable | Integer | Must be a non-negative integer (>= 0).  
`http.useClientProtocol` | Stable | Boolean | Cannot be `true` when `h2UpgradePolicy` is `UPGRADE`.  
`tcp.connectTimeout` | Stable | Duration |   
`tcp.maxConnectionDuration` | Stable | Duration | Only applied to HTTP/HTTP2/gRPC services; ignored for TCP byte-stream services.  
`tcp.maxConnections` | Stable | Integer | Must be a non-negative integer (>= 0).  
`tcp.tcpKeepalive.interval` | Stable | Duration |   
`tcp.tcpKeepalive.probes` | Stable | Integer |   
`tcp.tcpKeepalive.time` | Stable | Duration |   
  
### Subset Outlier Detection Settings (subsets.trafficPolicy.outlierDetection)

The following table lists the field-level support for `subsets.trafficPolicy.outlierDetection`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`baseEjectionTime` | **Unsupported** | Duration |   
`consecutive5xxErrors` | **Unsupported** | Integer |   
`consecutiveErrors` | **Unsupported** | Integer |   
`consecutiveGatewayErrors` | **Unsupported** | Integer |   
`consecutiveLocalOriginFailures` | **Unsupported** | Integer |   
`interval` | **Unsupported** | Duration |   
`maxEjectionPercent` | **Unsupported** | Integer |   
`minHealthPercent` | **Unsupported** | Integer |   
`splitExternalLocalOriginErrors` | **Unsupported** | Boolean |   
  
### Subset TLS & Tunnel Settings (subsets.trafficPolicy.tls, tunnel)

The following table lists the field-level support for `subsets.trafficPolicy.tls` and `tunnel`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`tls.caCertificates` | Stable | String |   
`tls.clientCertificate` | Stable | String | Required when mode is `MUTUAL`.  
`tls.credentialName` | **Unsupported** | String |   
`tls.insecureSkipVerify` | Stable | Boolean | When `true`, `caCertificates` and `subjectAltNames` must be empty.  
`tls.mode` | Stable | String (`DISABLE`, `SIMPLE`, `MUTUAL`, `ISTIO_MUTUAL`) | `MUTUAL` mode requires `clientCertificate` and `privateKey`.  
`tls.privateKey` | Stable | String | Required when mode is `MUTUAL`.  
`tls.sni` | Stable | String |   
`tls.subjectAltNames` | Stable | **Array of strings** |   
`tunnel.protocol` | **Unsupported** | String (`CONNECT`, `POST`) |   
`tunnel.targetHost` | **Unsupported** | String |   
`tunnel.targetPort` | **Unsupported** | Integer |   
  
### Subset Port & Load Balancer Settings (subsets.trafficPolicy.portLevelSettings.loadBalancer)

The following table lists the field-level support for `subsets.trafficPolicy.portLevelSettings.loadBalancer`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`loadBalancer.consistentHash.httpCookie.name` | Stable | String | Required when `httpCookie` is configured.  
`loadBalancer.consistentHash.httpCookie.path` | Stable | String |   
`loadBalancer.consistentHash.httpCookie.ttl` | Stable | Duration |   
`loadBalancer.consistentHash.httpHeaderName` | Stable | String | Only one `consistentHash` key strategy can be specified.  
`loadBalancer.consistentHash.httpQueryParameterName` | Stable | String | Only one `consistentHash` key strategy can be specified.  
`loadBalancer.consistentHash.maglev.tableSize` | Stable | Integer |   
`loadBalancer.consistentHash.minimumRingSize` | Stable | Integer | Deprecated. Use `ringHash.minimumRingSize` instead. Cannot be combined with `ringHash` or `maglev`.  
`loadBalancer.consistentHash.ringHash.minimumRingSize` | Stable | Integer |   
`loadBalancer.consistentHash.useSourceIp` | Stable | Boolean | Only one `consistentHash` key strategy can be specified.  
`loadBalancer.localityLbSetting.distribute.from` | **Unsupported** | String |   
`loadBalancer.localityLbSetting.distribute.to` | **Unsupported** | Key-value map |   
`loadBalancer.localityLbSetting.enabled` | **Unsupported** | Boolean |   
`loadBalancer.localityLbSetting.failover.from` | **Unsupported** | String |   
`loadBalancer.localityLbSetting.failover.to` | **Unsupported** | String |   
`loadBalancer.localityLbSetting.failoverPriority` | **Unsupported** | **Array of strings** |   
`loadBalancer.simple` | Stable | String (`ROUND_ROBIN`, `LEAST_CONN`, `RANDOM`, `PASSTHROUGH`, `LEAST_REQUEST`) | `LEAST_CONN` is not supported.  
`loadBalancer.warmupDurationSecs` | **Unsupported** | String |   
`port.number` | Stable | Integer | Required. Specifies the port number to which these traffic policies apply.  
  
### Subset Connection Pool Settings (subsets.trafficPolicy.portLevelSettings.connectionPool)

The following table lists the field-level support for `subsets.trafficPolicy.portLevelSettings.connectionPool`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`http.h2UpgradePolicy` | Stable | String (`DEFAULT`, `DO_NOT_UPGRADE`, `UPGRADE`) | Cannot be set to `UPGRADE` when `useClientProtocol` is `true`.  
`http.http1MaxPendingRequests` | Stable | Integer | Must be a non-negative integer (>= 0).  
`http.http2MaxRequests` | Stable | Integer | Must be a non-negative integer (>= 0).  
`http.idleTimeout` | Stable | Duration |   
`http.maxRequestsPerConnection` | Stable | Integer | Must be a non-negative integer (>= 0).  
`http.maxRetries` | Stable | Integer | Must be a non-negative integer (>= 0).  
`http.useClientProtocol` | Stable | Boolean | Cannot be `true` when `h2UpgradePolicy` is `UPGRADE`.  
`tcp.connectTimeout` | Stable | Duration |   
`tcp.maxConnectionDuration` | Stable | Duration | Only applied to HTTP/HTTP2/gRPC services; ignored for TCP byte-stream services.  
`tcp.maxConnections` | Stable | Integer | Must be a non-negative integer (>= 0).  
`tcp.tcpKeepalive.interval` | Stable | Duration |   
`tcp.tcpKeepalive.probes` | Stable | Integer |   
`tcp.tcpKeepalive.time` | Stable | Duration |   
  
### Subset Outlier Detection Settings (subsets.trafficPolicy.portLevelSettings.outlierDetection)

The following table lists the field-level support for `subsets.trafficPolicy.portLevelSettings.outlierDetection`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`baseEjectionTime` | **Unsupported** | Duration |   
`consecutive5xxErrors` | **Unsupported** | Integer |   
`consecutiveErrors` | **Unsupported** | Integer |   
`consecutiveGatewayErrors` | **Unsupported** | Integer |   
`consecutiveLocalOriginFailures` | **Unsupported** | Integer |   
`interval` | **Unsupported** | Duration |   
`maxEjectionPercent` | **Unsupported** | Integer |   
`minHealthPercent` | **Unsupported** | Integer |   
`splitExternalLocalOriginErrors` | **Unsupported** | Boolean |   
  
### Subset TLS Settings (subsets.trafficPolicy.portLevelSettings.tls)

The following table lists the field-level support for `subsets.trafficPolicy.portLevelSettings.tls`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`tls.caCertificates` | Stable | String |   
`tls.clientCertificate` | Stable | String | Required when mode is `MUTUAL`.  
`tls.credentialName` | **Unsupported** | String |   
`tls.insecureSkipVerify` | Stable | Boolean | When `true`, `caCertificates` and `subjectAltNames` must be empty.  
`tls.mode` | Stable | String (`DISABLE`, `SIMPLE`, `MUTUAL`, `ISTIO_MUTUAL`) | `MUTUAL` mode requires `clientCertificate` and `privateKey`.  
`tls.privateKey` | Stable | String | Required when mode is `MUTUAL`.  
`tls.sni` | Stable | String |   
`tls.subjectAltNames` | Stable | **Array of strings** |   
  
## EnvoyFilter (networking.istio.io/v1alpha3)

The following sections describe the supported fields for `EnvoyFilter` resources.

### Root & Spec Fields

The following table lists the field-level support.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`configPatches` | Stable | **Array of objects** |   
`priority` | Stable | Integer |   
`workloadSelector` | Stable | Key-value map |   
`workloadSelector.labels` | Stable | Key-value map |   
  
### Config Patches (configPatches)

The following table lists the field-level support for `configPatches`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`applyTo` | Stable | String (`HTTP_FILTER`) | Only `HTTP_FILTER` is supported.  
`match.cluster.name` | **Unsupported** | String |   
`match.cluster.portNumber` | **Unsupported** | Integer |   
`match.cluster.service` | **Unsupported** | String |   
`match.cluster.subset` | **Unsupported** | String |   
`match.context` | Stable | String (`ANY`, `SIDECAR_INBOUND`, `SIDECAR_OUTBOUND`, `GATEWAY`) |   
`match.listener.filterChain.applicationProtocols` | **Unsupported** | String |   
`match.listener.filterChain.destinationPort` | **Unsupported** | Integer |   
`match.listener.filterChain.filter.name` | Stable | String | Must be `envoy.filters.network.http_connection_manager` when used with `INSERT_BEFORE`.  
`match.listener.filterChain.filter.subFilter.name` | Stable | String | Must be `envoy.filters.http.router` when used with `INSERT_BEFORE`.  
`match.listener.filterChain.name` | **Unsupported** | String |   
`match.listener.filterChain.sni` | **Unsupported** | String |   
`match.listener.filterChain.transportProtocol` | **Unsupported** | String |   
`match.listener.listenerFilter` | **Unsupported** | String |   
`match.listener.name` | **Unsupported** | String |   
`match.listener.portName` | **Unsupported** | String |   
`match.listener.portNumber` | **Unsupported** | Integer |   
`match.proxy.metadata` | **Unsupported** | String |   
`match.proxy.proxyVersion` | **Unsupported** | String |   
`match.routeConfiguration.gateway` | **Unsupported** | String |   
`match.routeConfiguration.name` | **Unsupported** | String |   
`match.routeConfiguration.portName` | **Unsupported** | String |   
`match.routeConfiguration.portNumber` | **Unsupported** | Integer |   
`match.routeConfiguration.vhost.name` | **Unsupported** | String |   
`match.routeConfiguration.vhost.route.action` | **Unsupported** | String (`ANY`, `ROUTE`, `REDIRECT`, `DIRECT_RESPONSE`) |   
`match.routeConfiguration.vhost.route.name` | **Unsupported** | String |   
`patch.filterClass` | **Unsupported** | String (`UNSPECIFIED`, `AUTHN`, `AUTHZ`, `STATS`) |   
`patch.operation` | Stable | String (`INSERT_FIRST`, `INSERT_BEFORE`) | Only `INSERT_FIRST` and `INSERT_BEFORE` are supported.  
`patch.value` | Stable | String |   
  
## Gateway (networking.istio.io/v1beta1)

The following sections describe the supported fields for `Gateway` resources.

### Root Fields

The following table lists the supported root fields.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`selector` | Stable | Key-value map |   
`servers` | Stable | **Array of objects** |   
  
### Server Settings (servers)

The following table lists the field-level support for `servers`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`bind` | Stable | String | IP address is supported. Unix Domain Sockets (UDS) are not supported.  
`defaultEndpoint` | **Unsupported** | String |   
`hosts` | Stable | **Array of strings** | At least one host is required. Supports `<namespace>/<hostname>` format.  
`name` | **Unsupported** | String |   
`port.name` | Stable | String | Required. Port names must be unique across all servers in the Gateway.  
`port.number` | Stable | Integer | Required. Must be a valid port number between 1 and 65535.  
`port.protocol` | Stable | String (`HTTP`, `HTTPS`, `GRPC`, `GRPC-WEB`, `HTTP2`, `MONGO`, `MYSQL`, `REDIS`, `TCP`, `TLS`) | `MONGO`, `MYSQL`, and `REDIS` protocols are treated as plain `TCP` traffic; protocol-specific Envoy filters (such as `mongo_proxy`) are not supported.  
`port.targetPort` | **Unsupported** | Integer |   
  
### Server TLS Settings (servers.tls)

The following table lists the field-level support for `servers.tls`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`caCertificates` | Stable | String | Required for `MUTUAL` mode unless `credentialName` is set.  
`cipherSuites` | Stable | **Array of strings** | Must be specified when `minProtocolVersion` is `TLSV1_0` or `TLSV1_1`.  
`credentialName` | Stable | String | Only supported when `mode` is `SIMPLE` or `MUTUAL` (the `builtin://` prefix is only supported when `mode` is `MUTUAL`).  
`httpsRedirect` | Stable | Boolean | Only supported when `port.protocol` is `HTTP`, `HTTP2`, or `GRPC`.  
`maxProtocolVersion` | Stable | String (`TLS_AUTO`, `TLSV1_0`, `TLSV1_1`, `TLSV1_2`, `TLSV1_3`) |   
`minProtocolVersion` | Stable | String (`TLS_AUTO`, `TLSV1_0`, `TLSV1_1`, `TLSV1_2`, `TLSV1_3`) |   
`mode` | Stable | String (`PASSTHROUGH`, `SIMPLE`, `MUTUAL`, `ISTIO_MUTUAL`) | `AUTO_PASSTHROUGH` and `OPTIONAL_MUTUAL` are not supported. `ISTIO_MUTUAL` manages certificates automatically.  
`privateKey` | Stable | String | Required for `SIMPLE` and `MUTUAL` modes unless `credentialName` is set.  
`serverCertificate` | Stable | String | Required for `SIMPLE` and `MUTUAL` modes unless `credentialName` is set.  
`subjectAltNames` | Stable | **Array of strings** | Maximum of 8 SAN entries per server (entries beyond 8 are truncated). Only supported when `mode` is `MUTUAL` or `ISTIO_MUTUAL`; only exact and prefix (`*`) matching are supported.  
`verifyCertificateHash` | **Unsupported** | **Array of strings** |   
`verifyCertificateSpki` | **Unsupported** | **Array of strings** |   
  
## ProxyConfig (networking.istio.io/v1beta1)

The `ProxyConfig` custom resource (CR) is not supported.

## ServiceEntry (networking.istio.io/v1beta1)

The following sections describe the supported fields for `ServiceEntry` resources.

### Root & General Configuration

The following table lists the supported root and general configuration fields.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`addresses` | Stable | **Array of strings** | CIDR subnets are only supported with `STATIC` or `NONE` resolution. Required for `TCP` ports.  
`exportTo` | Stable | **Array of strings** |   
`hosts` | Stable | **Array of strings** | At least one host required. `*` alone not allowed. Multiple hosts require `HTTP`/`HTTPS`/`TLS` ports.  
`location` | Stable | String (`MESH_EXTERNAL`, `MESH_INTERNAL`) | `MESH_INTERNAL` is not supported.  
`resolution` | Stable | String (`NONE`, `STATIC`, `DNS`, `DNS_ROUND_ROBIN`) | `DNS_ROUND_ROBIN` is not supported. `NONE` requires empty endpoints; `STATIC` requires endpoints.  
`subjectAltNames` | **Unsupported** | **Array of strings** |   
`workloadSelector.labels` | **Unsupported** | Key-value map |   
  
### Port Settings (ports)

The following table lists the field-level support for `ports`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`name` | Stable | String | Required. Port names must be unique across the ServiceEntry.  
`number` | Stable | Integer | Required (1-65535). Port numbers must be unique across the ServiceEntry.  
`protocol` | Stable | String (`HTTP`, `HTTPS`, `GRPC`, `HTTP2`, `MONGO`, `TCP`, `TLS`) |   
`targetPort` | Stable | Integer | Must be a valid port number (1-65535) if specified.  
  
### Endpoint Settings (endpoints)

The following table lists the field-level support for `endpoints`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`address` | Stable | String | Required. Must be a valid IP address for `STATIC` resolution or FQDN or IP address for `DNS` resolution.  
`labels` | Stable | Key-value map | Must conform to Kubernetes label syntax rules.  
`locality` | **Unsupported** | String |   
`network` | **Unsupported** | String |   
`ports` | Stable | Key-value map | Port names in map must match port names defined in `spec.ports`.  
`serviceAccount` | **Unsupported** | String |   
`weight` | **Unsupported** | Integer |   
  
## Sidecar (networking.istio.io/v1beta1)

The following sections describe the supported fields for `Sidecar` resources.

### Root & General Configuration

The following table lists the supported root and general configuration fields.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`workloadSelector` | Stable | Object | Subject to [Istio Sidecar resources scalability limits](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/scalability-limits#istio_sidecar_resources): maximum 150 total `Sidecar` resources per cluster and 20 with `workloadSelector` per cluster (`Sidecar` resources with `workloadSelector` count toward both limits).  
`workloadSelector.labels` | Stable | Key-value map | Subject to [Istio Sidecar resources scalability limits](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/scalability-limits#istio_sidecar_resources) (maximum 20 `Sidecar` resources with `workloadSelector` per cluster, which also count toward the 150 total limit).  
  
### Egress Listeners (egress)

The following table lists the field-level support for `egress`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`bind` | **Unsupported** | String |   
`captureMode` | **Unsupported** | String (`DEFAULT`, `IPTABLES`, `NONE`) |   
`hosts` | Stable | **Array of strings** | Only the first matching `egress` listener entry without a port specification is processed. If multiple `egress` listeners are declared in a single Sidecar resource, all listeners after the first are silently ignored. The `~` namespace qualifier (representing no namespace in Istio) is not supported. To match no hosts, explicitly set `hosts: []` (empty list) within an `egress` listener entry.  
`port.name` | **Unsupported** | String |   
`port.number` | **Unsupported** | Integer |   
`port.protocol` | **Unsupported** | String (`HTTP`, `HTTPS`, `GRPC`, `HTTP2`, `MONGO`, `TCP`, `TLS`) |   
`port.targetPort` | **Unsupported** | Integer |   
  
### Ingress Listeners: Port & Binding (ingress)

The following table lists the field-level support for `ingress`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`bind` | **Unsupported** | String |   
`captureMode` | **Unsupported** | String (`DEFAULT`, `IPTABLES`, `NONE`) |   
`defaultEndpoint` | **Unsupported** | String |   
`port.name` | **Unsupported** | String |   
`port.number` | **Unsupported** | Integer |   
`port.protocol` | **Unsupported** | String (`HTTP`, `HTTPS`, `GRPC`, `HTTP2`, `MONGO`, `TCP`, `TLS`) |   
`port.targetPort` | **Unsupported** | Integer |   
  
### Ingress Listeners: TLS Settings (ingress.tls)

The following table lists the field-level support for `ingress.tls`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`caCertificates` | **Unsupported** | String |   
`cipherSuites` | **Unsupported** | **Array of strings** |   
`credentialName` | **Unsupported** | String |   
`httpsRedirect` | **Unsupported** | Boolean |   
`maxProtocolVersion` | **Unsupported** | String (`TLS_AUTO`, `TLSV1_0`, `TLSV1_1`, `TLSV1_2`, `TLSV1_3`) |   
`minProtocolVersion` | **Unsupported** | String (`TLS_AUTO`, `TLSV1_0`, `TLSV1_1`, `TLSV1_2`, `TLSV1_3`) |   
`mode` | **Unsupported** | String (`PASSTHROUGH`, `SIMPLE`, `MUTUAL`, `AUTO_PASSTHROUGH`, `ISTIO_MUTUAL`, `OPTIONAL_MUTUAL`) |   
`privateKey` | **Unsupported** | String |   
`serverCertificate` | **Unsupported** | String |   
`subjectAltNames` | **Unsupported** | **Array of strings** |   
`verifyCertificateHash` | **Unsupported** | **Array of strings** |   
`verifyCertificateSpki` | **Unsupported** | **Array of strings** |   
  
### Outbound Traffic Policy (outboundTrafficPolicy)

The following table lists the field-level support for `outboundTrafficPolicy`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`egressProxy.host` | **Unsupported** | String |   
`egressProxy.port.number` | **Unsupported** | Integer |   
`egressProxy.subset` | **Unsupported** | String |   
`mode` | Stable | String (`REGISTRY_ONLY`, `ALLOW_ANY`) | When omitted on a workload or namespace `Sidecar`, `MeshConfig.outboundTrafficPolicy` takes precedence over the root (`istio-system`) `Sidecar`.  
  
## VirtualService (networking.istio.io/v1beta1)

The following sections describe the supported fields for `VirtualService` resources.

### Root & General Configuration

The following table lists the supported root and general configuration fields.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`exportTo` | Stable | **Array of strings** |   
`gateways` | Stable | **Array of strings** | Defaults to `mesh` if omitted. Must match a Gateway name or `mesh`. Cannot bind to both `mesh` and other gateways simultaneously.  
`hosts` | Stable | **Array of strings** | At least one host required unless configured as delegate. Wildcard `*` not allowed when bound to mesh.  
  
### HTTP Route Settings (http)

The following table lists the field-level support for `http`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`delegate.name` | Stable | String | Required for delegate route. Must be a valid DNS label.  
`delegate.namespace` | Stable | String |   
`name` | Stable | String |   
`timeout` | Stable | Duration |   
  
### HTTP Match Conditions (http.match)

The following table lists the field-level support for `http.match`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`authority.exact` | Stable | String |   
`authority.prefix` | Stable | String |   
`authority.regex` | Stable | String | Must be valid RE2 regular expression (< 1024 characters).  
`gateways` | Stable | **Array of strings** | Defaults to `mesh` if omitted. Must match a Gateway name or `mesh`. Cannot bind to both `mesh` and other gateways simultaneously.  
`headers.exact` | Stable | Key-value map |   
`headers.prefix` | Stable | Key-value map |   
`headers.regex` | Stable | Key-value map | Must be valid RE2 regular expression (< 1024 characters).  
`ignoreUriCase` | Stable | Boolean |   
`method.exact` | Stable | String |   
`method.prefix` | Stable | String |   
`method.regex` | Stable | String | Must be valid RE2 regular expression (< 1024 characters).  
`name` | Stable | String |   
`port` | Stable | Integer | Must be a valid port number (1-65535).  
`queryParams.exact` | Stable | Key-value map |   
`queryParams.prefix` | Stable | Key-value map |   
`queryParams.regex` | Stable | Key-value map | Must be valid RE2 regular expression (< 1024 characters).  
`scheme.exact` | Stable | String |   
`scheme.prefix` | Stable | String |   
`scheme.regex` | Stable | String | Must be valid RE2 regular expression (< 1024 characters).  
`sourceLabels` | Stable | Key-value map | Must conform to Kubernetes label syntax rules.  
`sourceNamespace` | Stable | String | Must be a valid DNS label.  
`statPrefix` | **Unsupported** | String |   
`uri.exact` | Stable | String |   
`uri.prefix` | Stable | String |   
`uri.regex` | Stable | String | Must be valid RE2 regular expression (< 1024 characters).  
`withoutHeaders.exact` | Stable | Key-value map |   
`withoutHeaders.prefix` | Stable | Key-value map |   
`withoutHeaders.regex` | Stable | Key-value map | Must be valid RE2 regular expression (< 1024 characters).  
  
### HTTP Route Destinations (http.route)

The following table lists the field-level support for `http.route`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`destination.host` | Stable | String | Required. Must be a valid service host.  
`destination.port.number` | Stable | Integer | Must be a valid port number (1-65535).  
`destination.subset` | Stable | String |   
`headers.request.add` | Stable | Key-value map | Internal pseudo-headers starting with `:` (except `:authority`) cannot be modified.  
`headers.request.remove` | Stable | **Array of strings** | `Host` and internal pseudo-headers starting with `:` cannot be modified.  
`headers.request.set` | Stable | Key-value map | Internal pseudo-headers starting with `:` (except `:authority`) cannot be modified.  
`headers.response.add` | Stable | Key-value map | `Host` and internal pseudo-headers starting with `:` cannot be modified.  
`headers.response.remove` | Stable | **Array of strings** | `Host` and internal pseudo-headers starting with `:` cannot be modified.  
`headers.response.set` | Stable | Key-value map | `Host` and internal pseudo-headers starting with `:` cannot be modified.  
`weight` | Stable | Integer | Non-negative integer. Total weight must be > 0 when multiple destinations are specified.  
  
### HTTP Redirect & Direct Response (http.redirect, directResponse)

The following table lists the field-level support for `http.redirect` and `directResponse`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`http.directResponse.body.bytes` | Stable | String | Maximum response body size is 1 MB.  
`http.directResponse.body.string` | Stable | String | Maximum response body size is 1 MB.  
`http.directResponse.status` | Stable | Integer | Status code must be between 200 and 600.  
`http.redirect.authority` | Stable | String |   
`http.redirect.derivePort` | Stable | String (`FROM_PROTOCOL_DEFAULT`, `FROM_REQUEST_PORT`) |   
`http.redirect.port` | Stable | Integer | Must be a valid port number (1-65535).  
`http.redirect.redirectCode` | Stable | Integer | Redirect code must be 3xx (300-399).  
`http.redirect.scheme` | Stable | String | Must be `http` or `https`.  
`http.redirect.uri` | Stable | String |   
  
### HTTP Rewrite & CORS Policy (http.rewrite, corsPolicy)

The following table lists the field-level support for `http.rewrite` and `corsPolicy`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`http.corsPolicy.allowCredentials` | Stable | Boolean |   
`http.corsPolicy.allowHeaders` | Stable | **Array of strings** |   
`http.corsPolicy.allowMethods` | Stable | **Array of strings** | Supported methods: `GET`, `HEAD`, `POST`, `PUT`, `PATCH`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`.  
`http.corsPolicy.allowOrigin` | **Unsupported** | **Array of strings** |   
`http.corsPolicy.allowOrigins.exact` | Stable | String |   
`http.corsPolicy.allowOrigins.prefix` | Stable | String |   
`http.corsPolicy.allowOrigins.regex` | Stable | String | Must be valid RE2 regular expression (< 1024 characters).  
`http.corsPolicy.exposeHeaders` | Stable | **Array of strings** |   
`http.corsPolicy.maxAge` | Stable | Duration |   
`http.rewrite.authority` | Stable | String |   
`http.rewrite.uri` | Stable | String | Cannot be set simultaneously with `uriRegexRewrite`.  
`http.rewrite.uriRegexRewrite.match` | Stable | String | Cannot be set simultaneously with `uri` rewrite.  
`http.rewrite.uriRegexRewrite.rewrite` | Stable | String | Cannot be set simultaneously with `uri` rewrite.  
  
### HTTP Retries & Header Operations (http.retries, headers)

The following table lists the field-level support for `http.retries` and `headers`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`http.headers.request.add` | Stable | Key-value map | Internal pseudo-headers starting with `:` (except `:authority`) cannot be modified.  
`http.headers.request.remove` | Stable | **Array of strings** | `Host` and internal pseudo-headers starting with `:` cannot be modified.  
`http.headers.request.set` | Stable | Key-value map | Internal pseudo-headers starting with `:` (except `:authority`) cannot be modified.  
`http.headers.response.add` | Stable | Key-value map | `Host` and internal pseudo-headers starting with `:` cannot be modified.  
`http.headers.response.remove` | Stable | **Array of strings** | `Host` and internal pseudo-headers starting with `:` cannot be modified.  
`http.headers.response.set` | Stable | Key-value map | `Host` and internal pseudo-headers starting with `:` cannot be modified.  
`http.retries.attempts` | Stable | Integer | Non-negative integer. Must be > 0 if `retryOn` or `perTryTimeout` is configured.  
`http.retries.perTryTimeout` | Stable | Duration |   
`http.retries.retryOn` | Stable | String |   
`http.retries.retryRemoteLocalities` | Stable | Boolean |   
  
### HTTP Fault Injection (http.fault)

The following table lists the field-level support for `http.fault`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`abort.grpcStatus` | **Unsupported** | String |   
`abort.http2Error` | **Unsupported** | String |   
`abort.httpStatus` | Stable | Integer | Abort HTTP status code must be between 200 and 599.  
`abort.percentage.value` | Stable | Double | Percentage must be in range 0-100.  
`delay.exponentialDelay` | **Unsupported** | Duration |   
`delay.fixedDelay` | Stable | Duration | Fixed delay duration is supported. Exponential delay is not supported.  
`delay.percent` | **Unsupported** | Integer | Integer percent value is deprecated. Use the double percentage field instead.  
`delay.percentage.value` | Stable | Double | Percentage must be in range 0-100.  
  
### HTTP Traffic Mirroring (http.mirror, mirrors)

The following table lists the field-level support for `http.mirror` and `mirrors`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`http.mirror.host` | Stable | String | Single mirror destination. Cannot be combined with `mirrors`.  
`http.mirror.port.number` | Stable | Integer |   
`http.mirror.subset` | Stable | String |   
`http.mirrorPercent` | **Unsupported** | Integer |   
`http.mirrorPercentage.value` | Stable | Double | Percentage must be in range 0-100.  
`http.mirrors.destination.host` | **Unsupported** | String | Only the singular `http.mirror` field is supported; multiple mirrors configured using `http.mirrors` are ignored.  
`http.mirrors.destination.port.number` | **Unsupported** | Integer | Only the singular `http.mirror` field is supported; multiple mirrors configured using `http.mirrors` are ignored.  
`http.mirrors.destination.subset` | **Unsupported** | String | Only the singular `http.mirror` field is supported; multiple mirrors configured using `http.mirrors` are ignored.  
`http.mirrors.percentage.value` | **Unsupported** | Double | Only the singular `http.mirror` field is supported; multiple mirrors configured using `http.mirrors` are ignored.  
  
### TLS Routing (tls)

The following table lists the field-level support for `tls`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`match.destinationSubnets` | Stable | **Array of strings** | Must be a valid CIDR IP subnet string.  
`match.gateways` | Stable | **Array of strings** |   
`match.port` | Stable | Integer | Must be a valid port number (1-65535).  
`match.sniHosts` | Stable | **Array of strings** | At least one SNI host is required. Full wildcard (`*`) and partial wildcards (for example, `*example.com`) are not supported; only subdomain wildcards (for example, `*.example.com`) are allowed.  
`match.sourceLabels` | **Unsupported** | Key-value map |   
`match.sourceNamespace` | **Unsupported** | String |   
`route.destination.host` | Stable | String | Required. Must be a valid service host.  
`route.destination.port.number` | Stable | Integer | Must be a valid port number (1-65535).  
`route.destination.subset` | Stable | String |   
`route.weight` | Stable | Integer | Non-negative integer. Total weight must be > 0 when multiple destinations are specified.  
  
### TCP Routing (tcp)

The following table lists the field-level support for `tcp`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`match.destinationSubnets` | Stable | **Array of strings** | Must be a valid CIDR IP subnet string.  
`match.gateways` | Stable | **Array of strings** |   
`match.port` | Stable | Integer | Must be a valid port number (1-65535).  
`match.sourceLabels` | **Unsupported** | Key-value map |   
`match.sourceNamespace` | **Unsupported** | String |   
`match.sourceSubnet` | **Unsupported** | String |   
`route.destination.host` | Stable | String | Required. Must be a valid service host.  
`route.destination.port.number` | Stable | Integer | Must be a valid port number (1-65535).  
`route.destination.subset` | Stable | String |   
`route.weight` | Stable | Integer | Non-negative integer. Total weight must be > 0 when multiple destinations are specified.  
  
## WorkloadEntry (networking.istio.io/v1beta1)

The `WorkloadEntry` custom resource (CR) is not supported.

## WorkloadGroup (networking.istio.io/v1beta1)

The `WorkloadGroup` custom resource (CR) is not supported.

## AuthorizationPolicy (security.istio.io/v1beta1)

The following sections describe the supported fields for `AuthorizationPolicy` resources.

### Root & Spec Fields

The following table lists the field-level support.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`action` | Stable | String (`ALLOW`, `DENY`, `AUDIT`, `CUSTOM`) |   
`provider.name` | Stable | String | Only supported when `action: CUSTOM`.  
`selector.matchLabels` | Stable | Key-value map | If omitted, applies to all workloads in the namespace.  
  
### From Sources (rules.from.source)

The following table lists the field-level support for `rules.from.source`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`ipBlocks` | Stable | **Array of strings** |   
`notIpBlocks` | Stable | **Array of strings** |   
`namespaces` | Stable | **Array of strings** |   
`notNamespaces` | Stable | **Array of strings** |   
`principals` | Stable | **Array of strings** |   
`notPrincipals` | Stable | **Array of strings** |   
`remoteIpBlocks` | Stable | **Array of strings** |   
`notRemoteIpBlocks` | Stable | **Array of strings** |   
`requestPrincipals` | Stable | **Array of strings** |   
`notRequestPrincipals` | Stable | **Array of strings** |   
  
### To Operations (rules.to.operation)

The following table lists the field-level support for `rules.to.operation`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`hosts` | Stable | **Array of strings** |   
`methods` | Stable | **Array of strings** |   
`notHosts` | Stable | **Array of strings** |   
`notMethods` | Stable | **Array of strings** |   
`notPaths` | Stable | **Array of strings** | Only prefix and suffix wildcard matching is supported.  
`notPorts` | Stable | **Array of objects** | Must be valid port numbers (1-65535).  
`paths` | Stable | **Array of strings** | Only prefix and suffix wildcard matching is supported.  
`ports` | Stable | **Array of objects** | Must be valid port numbers (1-65535).  
  
### When Conditions (rules.when)

The following table lists the field-level support for `rules.when`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`key` | Stable | String | Supported keys: `request.headers`, `request.auth.claims`, IPs, ports, principals. When `action` is `CUSTOM`, `source.namespace`, `source.principal`, and `request.auth.*` keys are not supported. `destination.namespace/labels` unsupported.  
`notValues` | Stable | **Array of strings** | At least one of `values` or `notValues` must be specified.  
`values` | Stable | **Array of strings** | At least one of `values` or `notValues` must be specified.  
  
## PeerAuthentication (security.istio.io/v1beta1)

The following sections describe the supported fields for `PeerAuthentication` resources.

### Root & Spec Fields

The following table lists the field-level support.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`mtls.mode` | Stable | String (`UNSET`, `DISABLE`, `PERMISSIVE`, `STRICT`) | `DISABLE` mode is not supported.  
`portLevelMtls.mode` | Stable | String (`UNSET`, `DISABLE`, `PERMISSIVE`, `STRICT`) | `DISABLE` mode is not supported.  
`selector.matchLabels` | Stable | Key-value map | Policy in root namespace is not allowed to have label selector.  
  
## RequestAuthentication (security.istio.io/v1beta1)

The following sections describe the supported fields for `RequestAuthentication` resources.

### Root Fields

The following table lists the supported root fields.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`selector.matchLabels` | Stable | Key-value map | If omitted, applies to all workloads in the namespace. Wildcards (`*`) not allowed.  
  
### JWT Rules (jwtRules)

The following table lists the field-level support for `jwtRules`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`audiences` | Stable | **Array of strings** |   
`forwardOriginalToken` | Stable | Boolean |   
`fromHeaders.name` | Stable | String |   
`fromHeaders.prefix` | Stable | String |   
`fromParams` | Stable | **Array of strings** |   
`issuer` | Stable | String |   
`jwks` | Stable | String | Only one of `jwksUri` and `jwks` should be used.  
`jwksUri` | Stable | String | Only one of `jwksUri` and `jwks` should be used.  
`outputClaimToHeaders.claim` | **Unsupported** | String |   
`outputClaimToHeaders.header` | **Unsupported** | String |   
`outputPayloadToHeader` | Stable | String |   
  
## Telemetry (telemetry.istio.io/v1alpha1)

The following sections describe the supported fields for `Telemetry` resources.

### Root & General Configuration

The following table lists the supported root and general configuration fields.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`selector.matchLabels` | Regular | Key-value map | In the Stable channel, only mesh-wide telemetry in root namespace is supported.  
  
### Access Logging (accessLogging)

The following table lists the field-level support for `accessLogging`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`disabled` | Stable | Boolean | Disables access logging for the provider.  
`filter.expression` | **Unsupported** | String |   
`match.mode` | **Unsupported** | String (`CLIENT_AND_SERVER`, `CLIENT`, `SERVER`) |   
`providers.name` | Stable | String | Only Envoy or Stackdriver.  
  
### Tracing (tracing)

The following table lists the field-level support for `tracing`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`customTags.environment.defaultValue` | **Unsupported** | String |   
`customTags.environment.name` | **Unsupported** | String |   
`customTags.header.defaultValue` | **Unsupported** | String |   
`customTags.header.name` | **Unsupported** | String |   
`customTags.literal.value` | **Unsupported** | String |   
`disableSpanReporting` | Stable | Boolean | Disables span reporting to Cloud Trace.  
`match.mode` | **Unsupported** | String (`CLIENT_AND_SERVER`, `CLIENT`, `SERVER`) |   
`providers.name` | Stable | String | Only Stackdriver.  
`randomSamplingPercentage` | Regular | Double | Defaults to 0.0. Supported value range: 0.0 to 100.0.  
`useRequestIdForTraceSampling` | **Unsupported** | Boolean |   
  
### Metrics (metrics)

The following table lists the field-level support for `metrics`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`overrides.disabled` | **Unsupported** | Boolean |   
`overrides.match.customMatch` | **Unsupported** | **Array of objects** |   
`overrides.match.customMetric` | **Unsupported** | String |   
`overrides.match.metric` | **Unsupported** | String (`ALL_METRICS`, `REQUEST_COUNT`, `REQUEST_DURATION`, `REQUEST_SIZE`, `RESPONSE_SIZE`, `TCP_OPENED_CONNECTIONS`, `TCP_CLOSED_CONNECTIONS`, `TCP_SENT_BYTES`, `TCP_RECEIVED_BYTES`, `GRPC_REQUEST_MESSAGES`, `GRPC_RESPONSE_MESSAGES`) |   
`overrides.match.mode` | **Unsupported** | String (`CLIENT_AND_SERVER`, `CLIENT`, `SERVER`) |   
`overrides.tagOverrides.operation` | **Unsupported** | String (`UPSERT`, `REMOVE`) |   
`overrides.tagOverrides.value` | **Unsupported** | String |   
`providers.name` | **Unsupported** | String |   
`reportingInterval` | **Unsupported** | Duration |   
  
## WasmPlugin (extensions.istio.io/v1alpha1)

The `WasmPlugin` custom resource (CR) is not supported.

## MeshConfig (mesh.istio.io/v1alpha1)

The following sections describe the supported fields for `MeshConfig` resources.

### Root & General Configuration

The following table lists the supported root and general configuration fields.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`accessLogEncoding` | Rapid | String (`TEXT`, `JSON`) | Supported encoding formats: `TEXT` or `JSON`.  
`accessLogFile` | Stable | String | Destination path for Envoy access logging (for example, `/dev/stdout`).  
`accessLogFormat` | Rapid | String |   
`connectTimeout` | **Unsupported** | Duration |   
`defaultDestinationRuleExportTo` | Stable | **Array of strings** | Default export scope for DestinationRules (defaults to `*`).  
`defaultHttpRetryPolicy.attempts` | **Unsupported** | Integer |   
`defaultHttpRetryPolicy.perTryTimeout` | **Unsupported** | Duration |   
`defaultHttpRetryPolicy.retryOn` | **Unsupported** | String |   
`defaultHttpRetryPolicy.retryRemoteLocalities` | **Unsupported** | String |   
`defaultServiceExportTo` | Stable | **Array of strings** | Default export scope for Services (defaults to `*`).  
`defaultVirtualServiceExportTo` | Stable | **Array of strings** | Default export scope for VirtualServices (defaults to `*`).  
`disableEnvoyListenerLog` | **Unsupported** | String |   
`dnsRefreshRate` | **Unsupported** | String |   
`enableAutoMtls` | **Unsupported** | Boolean |   
`enableEnvoyAccessLogService` | **Unsupported** | String |   
`enablePrometheusMerge` | **Unsupported** | String |   
`enableTracing` | **Unsupported** | String |   
`h2UpgradePolicy` | **Unsupported** | String (`DO_NOT_UPGRADE`, `UPGRADE`) |   
`inboundClusterStatName` | **Unsupported** | String |   
`inboundTrafficPolicy.mode` | **Unsupported** | String (`PASSTHROUGH`, `LOCALHOST`) |   
`ingressClass` | **Unsupported** | String |   
`ingressControllerMode` | **Unsupported** | String (`UNSPECIFIED`, `OFF`, `DEFAULT`, `STRICT`) |   
`ingressSelector` | **Unsupported** | Key-value map |   
`ingressService` | **Unsupported** | String |   
`outboundClusterStatName` | **Unsupported** | String |   
`pathNormalization.normalization` | **Unsupported** | String |   
`pathNormalization.normalizationType` | **Unsupported** | String (`DEFAULT`, `NONE`, `BASE`, `MERGE_SLASHES`, `DECODE_AND_MERGE_SLASHES`) |   
`protocolDetectionTimeout` | **Unsupported** | Duration |   
`proxyHttpPort` | **Unsupported** | Integer |   
`proxyInboundListenPort` | **Unsupported** | Integer |   
`proxyListenPort` | **Unsupported** | Integer |   
`rootNamespace` | **Unsupported** | String |   
`trustDomain` | **Unsupported** | String |   
`trustDomainAliases` | **Unsupported** | **Array of strings** |   
`verifyCertificateAtClient` | **Unsupported** | String |   
  
### CA & Certificate Settings (ca, caCertificates, certificates)

The following table lists the field-level support for `ca`, `caCertificates`, and `certificates`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`ca.address` | **Unsupported** | String |   
`ca.istiodSide` | **Unsupported** | Boolean |   
`ca.requestTimeout` | **Unsupported** | Duration |   
`ca.tlsSettings.caCertificates` | **Unsupported** | String |   
`ca.tlsSettings.clientCertificate` | **Unsupported** | String |   
`ca.tlsSettings.clientCertificates` | **Unsupported** | String |   
`ca.tlsSettings.credentialName` | **Unsupported** | String |   
`ca.tlsSettings.insecureSkipVerify` | **Unsupported** | Boolean |   
`ca.tlsSettings.mode` | **Unsupported** | String (`DISABLE`, `SIMPLE`, `MUTUAL`, `ISTIO_MUTUAL`) |   
`ca.tlsSettings.privateKey` | **Unsupported** | String |   
`ca.tlsSettings.sni` | **Unsupported** | String |   
`ca.tlsSettings.subjectAltNames` | **Unsupported** | **Array of strings** |   
`caCertificates.certSigners` | **Unsupported** | String |   
`caCertificates.pem` | **Unsupported** | String |   
`caCertificates.spiffeBundleUrl` | **Unsupported** | String |   
`caCertificates.trustDomains` | **Unsupported** | String |   
`certificates.dnsNames` | **Unsupported** | **Array of strings** |   
`certificates.secretName` | **Unsupported** | String |   
  
### Config Sources (configSources)

The following table lists the field-level support for `configSources`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`address` | **Unsupported** | String |   
`subscribedResources` | **Unsupported** | **Array of strings** (`SERVICE_REGISTRY`) |   
`tlsSettings.caCertificates` | **Unsupported** | String |   
`tlsSettings.clientCertificate` | **Unsupported** | String |   
`tlsSettings.credentialName` | **Unsupported** | String |   
`tlsSettings.insecureSkipVerify` | **Unsupported** | Boolean |   
`tlsSettings.mode` | **Unsupported** | String (`DISABLE`, `SIMPLE`, `MUTUAL`, `ISTIO_MUTUAL`) |   
`tlsSettings.privateKey` | **Unsupported** | String |   
`tlsSettings.sni` | **Unsupported** | String |   
`tlsSettings.subjectAltNames` | **Unsupported** | **Array of strings** |   
  
### Default Providers (defaultProviders)

The following table lists the field-level support for `defaultProviders`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`accessLogging` | Stable | **Array of strings** (`envoy`) |   
`metrics` | **Unsupported** | **Array of strings** |   
`tracing` | Stable | **Array of strings** (`stackdriver`) |   
  
### Discovery Selectors (discoverySelectors)

The following table lists the field-level support for `discoverySelectors`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`matchExpressions.key` | Stable | String |   
`matchExpressions.operator` | Stable | String |   
`matchExpressions.values` | Stable | **Array of strings** |   
`matchLabels` | Stable | Key-value map |   
  
### External Authorization HTTP (extensionProviders.envoyExtAuthzHttp)

The following table lists the field-level support for `extensionProviders.envoyExtAuthzHttp`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`failOpen` | Stable | Boolean |   
`headersToDownstreamOnAllow` | Stable | String | Wildcard `*` alone not supported.  
`headersToDownstreamOnDeny` | Stable | String | Wildcard `*` alone not supported.  
`headersToUpstreamOnAllow` | Stable | String | Wildcard `*` alone not supported.  
`includeAdditionalHeadersInCheck` | **Unsupported** | Key-value map |   
`includeHeadersInCheck` | **Unsupported** | String |   
`includeRequestBodyInCheck.allowPartialMessage` | **Unsupported** | Boolean |   
`includeRequestBodyInCheck.maxRequestBytes` | **Unsupported** | Integer |   
`includeRequestBodyInCheck.packAsBytes` | **Unsupported** | Boolean |   
`includeRequestHeadersInCheck` | Stable | String | Wildcard `*` alone not supported.  
`pathPrefix` | Stable | String | Must begin with `/` (for example, `/check`).  
`port` | Stable | Integer | Required port number (1-65535).  
`service` | Stable | String | Required. Must be a valid FQDN or `<namespace>/<hostname>`.  
`statusOnError` | Stable | String | Must be a valid Envoy status code if configured.  
`timeout` | Stable | Duration |   
  
### External Authorization gRPC (extensionProviders.envoyExtAuthzGrpc)

The following table lists the field-level support for `extensionProviders.envoyExtAuthzGrpc`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`failOpen` | Stable | Boolean |   
`includeRequestBodyInCheck.allowPartialMessage` | Stable | Boolean |   
`includeRequestBodyInCheck.maxRequestBytes` | Stable | Integer |   
`includeRequestBodyInCheck.packAsBytes` | Stable | Boolean |   
`port` | Stable | Integer | Required port number (1-65535).  
`service` | Stable | String | Required. Must be a valid FQDN or `<namespace>/<hostname>`.  
`statusOnError` | Stable | String | Must be a valid Envoy status code if configured.  
`timeout` | Stable | Duration |   
  
### OpenTelemetry (extensionProviders.opentelemetry)

The following table lists the field-level support for `extensionProviders.opentelemetry`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`dynatraceSampler.clusterId` | **Unsupported** | Integer |   
`dynatraceSampler.httpService.http.headers.name` | **Unsupported** | String |   
`dynatraceSampler.httpService.http.headers.value` | **Unsupported** | String |   
`dynatraceSampler.httpService.http.path` | **Unsupported** | String |   
`dynatraceSampler.httpService.http.timeout` | **Unsupported** | Duration |   
`dynatraceSampler.httpService.port` | **Unsupported** | Integer |   
`dynatraceSampler.httpService.service` | **Unsupported** | String |   
`dynatraceSampler.rootSpansPerMinute` | **Unsupported** | Integer |   
`dynatraceSampler.tenant` | **Unsupported** | String |   
`http.headers.name` | **Unsupported** | String |   
`http.headers.value` | **Unsupported** | String |   
`http.path` | **Unsupported** | String |   
`http.timeout` | **Unsupported** | Duration |   
`maxTagLength` | **Unsupported** | String |   
`port` | **Unsupported** | Integer |   
`resourceDetectors.dynatrace` | **Unsupported** | String |   
`resourceDetectors.environment` | **Unsupported** | String |   
`service` | **Unsupported** | String |   
  
### Zipkin & Lightstep (extensionProviders.zipkin, lightstep)

The following table lists the field-level support for `extensionProviders.zipkin` and `lightstep`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`lightstep.accessToken` | **Unsupported** | String |   
`lightstep.maxTagLength` | **Unsupported** | String |   
`lightstep.port` | **Unsupported** | Integer |   
`lightstep.service` | **Unsupported** | String |   
`zipkin.enable64bitTraceId` | **Unsupported** | Boolean |   
`zipkin.maxTagLength` | **Unsupported** | String |   
`zipkin.port` | **Unsupported** | Integer |   
`zipkin.service` | **Unsupported** | String |   
  
### Datadog, Stackdriver, SkyWalking & OpenCensus (extensionProviders.datadog, stackdriver, skywalking, opencensus)

The following table lists the field-level support for `extensionProviders.datadog`, `stackdriver`, `skywalking`, and `opencensus`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`datadog.maxTagLength` | **Unsupported** | String |   
`datadog.port` | **Unsupported** | Integer |   
`datadog.service` | **Unsupported** | String |   
`opencensus.context` | **Unsupported** | **Array of strings** (`UNSPECIFIED`, `W3C_TRACE_CONTEXT`, `GRPC_BIN`, `CLOUD_TRACE_CONTEXT`, `B3`) |   
`opencensus.maxTagLength` | **Unsupported** | String |   
`opencensus.port` | **Unsupported** | Integer |   
`opencensus.service` | **Unsupported** | String |   
`skywalking.accessToken` | **Unsupported** | String |   
`skywalking.port` | **Unsupported** | Integer |   
`skywalking.service` | **Unsupported** | String |   
`stackdriver.debug` | **Unsupported** | String |   
`stackdriver.logging` | **Unsupported** | Boolean |   
`stackdriver.logging.labels` | **Unsupported** | Key-value map |   
`stackdriver.maxNumberOfAnnotations` | **Unsupported** | Key-value map |   
`stackdriver.maxNumberOfAttributes` | **Unsupported** | String |   
`stackdriver.maxNumberOfMessageEvents` | **Unsupported** | String |   
`stackdriver.maxTagLength` | **Unsupported** | String |   
  
### Access Logging Settings (extensionProviders.envoyFileAccessLog, envoyHttpAls, envoyTcpAls, envoyOtelAls, prometheus)

The following table lists the field-level support for `extensionProviders.envoyFileAccessLog`, `envoyHttpAls`, `envoyTcpAls`, `envoyOtelAls`, and `prometheus`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`envoyFileAccessLog.logFormat.labels` | **Unsupported** | Key-value map |   
`envoyFileAccessLog.logFormat.text` | **Unsupported** | String |   
`envoyFileAccessLog.path` | **Unsupported** | String |   
`envoyHttpAls.additionalRequestHeadersToLog` | **Unsupported** | String |   
`envoyHttpAls.additionalResponseHeadersToLog` | **Unsupported** | String |   
`envoyHttpAls.additionalResponseTrailersToLog` | **Unsupported** | String |   
`envoyHttpAls.filterStateObjectsToLog` | **Unsupported** | String |   
`envoyHttpAls.logName` | **Unsupported** | String |   
`envoyHttpAls.port` | **Unsupported** | Integer |   
`envoyHttpAls.service` | **Unsupported** | String |   
`envoyOtelAls.logFormat.labels` | **Unsupported** | Key-value map |   
`envoyOtelAls.logFormat.text` | **Unsupported** | String |   
`envoyOtelAls.logName` | **Unsupported** | String |   
`envoyOtelAls.port` | **Unsupported** | Integer |   
`envoyOtelAls.service` | **Unsupported** | String |   
`envoyTcpAls.filterStateObjectsToLog` | **Unsupported** | String |   
`envoyTcpAls.logName` | **Unsupported** | String |   
`envoyTcpAls.port` | **Unsupported** | Integer |   
`envoyTcpAls.service` | **Unsupported** | String |   
`prometheus` | **Unsupported** | Object |   
  
### Provider Name (extensionProviders.name)

The following table lists the field-level support for `extensionProviders.name`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`name` | Stable | String | Required. Must be unique across all extension providers.  
  
### Locality Load Balancing (localityLbSetting)

The following table lists the field-level support for `localityLbSetting`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`distribute.from` | **Unsupported** | String |   
`distribute.to` | **Unsupported** | Key-value map |   
`enabled` | Stable | Boolean |   
`failover.from` | Stable | String | Requires `outlierDetection` to be configured on the traffic policy and it is only allowed syntactically to trigger `WATERFALL_BY_ZONE`. Specific routing paths are ignored.  
`failover.to` | Stable | String | Requires `outlierDetection` to be configured on the traffic policy and it is only allowed syntactically to trigger `WATERFALL_BY_ZONE`. Specific routing paths are ignored.  
`failoverPriority` | **Unsupported** | **Array of strings** |   
  
### Mesh & TLS Defaults (meshMTLS, tlsDefaults)

The following table lists the field-level support for `meshMTLS` and `tlsDefaults`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`meshMTLS.cipherSuites` | **Unsupported** | **Array of strings** |   
`meshMTLS.ecdhCurves` | **Unsupported** | **Array of strings** |   
`meshMTLS.minProtocolVersion` | **Unsupported** | String (`TLS_AUTO`, `TLSV1_2`, `TLSV1_3`) |   
`tlsDefaults.cipherSuites` | **Unsupported** | **Array of strings** |   
`tlsDefaults.ecdhCurves` | **Unsupported** | **Array of strings** |   
`tlsDefaults.minProtocolVersion` | **Unsupported** | String (`TLS_AUTO`, `TLSV1_2`, `TLSV1_3`) |   
  
### Mesh Networks (networks)

The following table lists the field-level support for `networks`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`endpoints.fromCidr` | Stable | String |   
`endpoints.fromRegistry` | Stable | String |   
`gateways.address` | Stable | String |   
`gateways.locality` | Stable | String |   
`gateways.port` | Stable | Integer |   
`gateways.registryServiceName` | Stable | String |   
  
### Outbound Traffic Policy & Service Settings (outboundTrafficPolicy, serviceSettings)

The following table lists the field-level support for `outboundTrafficPolicy` and `serviceSettings`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`outboundTrafficPolicy.mode` | Stable | String (`REGISTRY_ONLY`, `ALLOW_ANY`) | Configures mesh-wide outbound traffic handling for unknown destinations.  
`serviceSettings.hosts` | Stable | **Array of strings** |   
`serviceSettings.settings.clusterLocal` | Stable | Boolean |   
  
### TCP Keepalive (tcpKeepalive)

The following table lists the field-level support for `tcpKeepalive`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`interval` | **Unsupported** | Duration |   
`probes` | **Unsupported** | Integer |   
`time` | **Unsupported** | Duration |   
  
### Proxy General Settings (defaultConfig)

The following table lists the field-level support for `defaultConfig`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`availabilityZone` | **Unsupported** | String |   
`binaryPath` | **Unsupported** | String |   
`caCertificatesPem` | **Unsupported** | **Array of strings** |   
`concurrency` | Stable | Integer |   
`configPath` | **Unsupported** | String |   
`controlPlaneAuthPolicy` | **Unsupported** | String (`NONE`, `MUTUAL_TLS`, `INHERIT`) |   
`customConfigFile` | **Unsupported** | String |   
`discoveryAddress` | **Unsupported** | String |   
`discoveryRefreshDelay` | **Unsupported** | String |   
`drainDuration` | Stable | Duration | Must have precision of seconds. Maximum 1 hour (3600s).  
`envoyMetricsServiceAddress` | **Unsupported** | String |   
`extraStatTags` | **Unsupported** | **Array of strings** |   
`holdApplicationUntilProxyStarts` | Stable | Boolean | Delays application pod startup until Envoy proxy is ready.  
`interceptionMode` | Stable | String (`REDIRECT`, `TPROXY`, `NONE`) | Traffic interception mode for proxy sidecars.  
`meshId` | **Unsupported** | String |   
`proxyAdminPort` | **Unsupported** | Integer |   
`proxyBootstrapTemplatePath` | **Unsupported** | String |   
`proxyMetadata` | Stable | Key-value map | Supported metadata key-value pairs for proxy configuration.  
`serviceCluster` | **Unsupported** | String |   
`statNameLength` | **Unsupported** | Integer |   
`statsdUdpAddress` | **Unsupported** | String |   
`statusPort` | **Unsupported** | Integer |   
`terminationDrainDuration` | Stable | Duration | Maximum grace period for connection drain during proxy shutdown.  
`tracingServiceName` | **Unsupported** | String (`APP_LABEL_AND_NAMESPACE`, `CANONICAL_NAME_ONLY`, `CANONICAL_NAME_AND_NAMESPACE`) |   
`zipkinAddress` | **Unsupported** | String |   
  
### Tracing Settings (defaultConfig.tracing)

The following table lists the field-level support for `defaultConfig.tracing`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`customTags` | **Unsupported** | Key-value map |   
`datadog.address` | **Unsupported** | String |   
`lightstep.accessToken` | **Unsupported** | String |   
`lightstep.address` | **Unsupported** | String |   
`maxPathTagLength` | **Unsupported** | Integer |   
`openCensusAgent.address` | **Unsupported** | String |   
`openCensusAgent.context` | **Unsupported** | **Array of strings** (`UNSPECIFIED`, `W3C_TRACE_CONTEXT`, `GRPC_BIN`, `CLOUD_TRACE_CONTEXT`, `B3`) |   
`sampling` | **Unsupported** | String |   
`stackdriver.debug` | **Unsupported** | String |   
`stackdriver.maxNumberOfAnnotations` | **Unsupported** | Key-value map |   
`stackdriver.maxNumberOfAttributes` | **Unsupported** | String |   
`stackdriver.maxNumberOfMessageEvents` | **Unsupported** | String |   
`tlsSettings.caCertificates` | **Unsupported** | String |   
`tlsSettings.clientCertificate` | **Unsupported** | String |   
`tlsSettings.credentialName` | **Unsupported** | String |   
`tlsSettings.insecureSkipVerify` | **Unsupported** | Boolean |   
`tlsSettings.mode` | **Unsupported** | String (`DISABLE`, `SIMPLE`, `MUTUAL`, `ISTIO_MUTUAL`) |   
`tlsSettings.privateKey` | **Unsupported** | String |   
`tlsSettings.sni` | **Unsupported** | String |   
`tlsSettings.subjectAltNames` | **Unsupported** | **Array of strings** |   
`zipkin.address` | **Unsupported** | String |   
  
### Envoy Access Log & Metrics Service (defaultConfig.envoyAccessLogService, envoyMetricsService)

The following table lists the field-level support for `defaultConfig.envoyAccessLogService` and `envoyMetricsService`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`envoyAccessLogService.address` | **Unsupported** | String |   
`envoyAccessLogService.tcpKeepalive.interval` | **Unsupported** | Duration |   
`envoyAccessLogService.tcpKeepalive.probes` | **Unsupported** | Integer |   
`envoyAccessLogService.tcpKeepalive.time` | **Unsupported** | Duration |   
`envoyAccessLogService.tlsSettings.caCertificates` | **Unsupported** | String |   
`envoyAccessLogService.tlsSettings.clientCertificate` | **Unsupported** | String |   
`envoyAccessLogService.tlsSettings.credentialName` | **Unsupported** | String |   
`envoyAccessLogService.tlsSettings.insecureSkipVerify` | **Unsupported** | Boolean |   
`envoyAccessLogService.tlsSettings.mode` | **Unsupported** | String (`DISABLE`, `SIMPLE`, `MUTUAL`, `ISTIO_MUTUAL`) |   
`envoyAccessLogService.tlsSettings.privateKey` | **Unsupported** | String |   
`envoyAccessLogService.tlsSettings.sni` | **Unsupported** | String |   
`envoyAccessLogService.tlsSettings.subjectAltNames` | **Unsupported** | **Array of strings** |   
`envoyMetricsService.address` | **Unsupported** | String |   
`envoyMetricsService.tcpKeepalive.interval` | **Unsupported** | Duration |   
`envoyMetricsService.tcpKeepalive.probes` | **Unsupported** | Integer |   
`envoyMetricsService.tcpKeepalive.time` | **Unsupported** | Duration |   
`envoyMetricsService.tlsSettings.caCertificates` | **Unsupported** | String |   
`envoyMetricsService.tlsSettings.clientCertificate` | **Unsupported** | String |   
`envoyMetricsService.tlsSettings.credentialName` | **Unsupported** | String |   
`envoyMetricsService.tlsSettings.insecureSkipVerify` | **Unsupported** | Boolean |   
`envoyMetricsService.tlsSettings.mode` | **Unsupported** | String (`DISABLE`, `SIMPLE`, `MUTUAL`, `ISTIO_MUTUAL`) |   
`envoyMetricsService.tlsSettings.privateKey` | **Unsupported** | String |   
`envoyMetricsService.tlsSettings.sni` | **Unsupported** | String |   
`envoyMetricsService.tlsSettings.subjectAltNames` | **Unsupported** | **Array of strings** |   
  
### Readiness Probe Settings (defaultConfig.readinessProbe)

The following table lists the field-level support for `defaultConfig.readinessProbe`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`exec.command` | **Unsupported** | String |   
`failureThreshold` | **Unsupported** | Integer |   
`httpGet.host` | **Unsupported** | String |   
`httpGet.httpHeaders.name` | **Unsupported** | String |   
`httpGet.httpHeaders.value` | **Unsupported** | String |   
`httpGet.path` | **Unsupported** | String |   
`httpGet.port` | **Unsupported** | Integer |   
`httpGet.scheme` | **Unsupported** | String |   
`initialDelaySeconds` | **Unsupported** | Integer |   
`periodSeconds` | **Unsupported** | Integer |   
`successThreshold` | **Unsupported** | Integer |   
`tcpSocket.host` | **Unsupported** | String |   
`tcpSocket.port` | **Unsupported** | Integer |   
`timeoutSeconds` | **Unsupported** | Integer |   
  
### Proxy Headers & Topology (defaultConfig.proxyHeaders, gatewayTopology)

The following table lists the field-level support for `defaultConfig.proxyHeaders` and `gatewayTopology`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`gatewayTopology.forwardClientCertDetails` | Stable | String (`UNDEFINED`, `SANITIZE`, `FORWARD_ONLY`, `APPEND_FORWARD`, `SANITIZE_SET`, `ALWAYS_FORWARD_ONLY`) |   
`gatewayTopology.numTrustedProxies` | Stable | Integer |   
`gatewayTopology.proxyProtocol` | **Unsupported** | Object |   
`proxyHeaders.attemptCount.disabled` | **Unsupported** | Boolean |   
`proxyHeaders.envoyDebugHeaders.disabled` | **Unsupported** | Boolean |   
`proxyHeaders.forwardedClientCert` | **Unsupported** | String (`UNDEFINED`, `SANITIZE`, `FORWARD_ONLY`, `APPEND_FORWARD`, `SANITIZE_SET`, `ALWAYS_FORWARD_ONLY`) |   
`proxyHeaders.metadataExchangeHeaders.mode` | **Unsupported** | String (`UNDEFINED`, `IN_MESH`) |   
`proxyHeaders.requestId.disabled` | **Unsupported** | Boolean |   
`proxyHeaders.server.disabled` | **Unsupported** | Boolean |   
`proxyHeaders.server.value` | **Unsupported** | String |   
  
### Proxy Metadata & Runtime Values (defaultConfig.proxyMetadata, runtimeValues)

The following table lists the field-level support for `defaultConfig.proxyMetadata` and `runtimeValues`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`CA_PROVIDER` | Stable | String |   
`CA_ROOT_CA` | **Unsupported** | String |   
`ENABLE_NATIVE_SIDECARS` | **Unsupported** | String |   
`EXIT_ON_ZERO_ACTIVE_CONNECTIONS` | Stable | String |   
`GCE_METADATA_HOST` | **Unsupported** | String |   
`GCP_METADATA` | Stable | String |   
`GKE_CLUSTER_URL` | Stable | String |   
`GODEBUG` | Stable | String |   
`GRPC_VERBOSITY` | Stable | String |   
`HTTPS_PROXY` | **Unsupported** | String |   
`HTTP_PROXY` | **Unsupported** | String |   
`ISTIO_LOG_LEVEL` | **Unsupported** | String |   
`ISTIO_META_CLOUDRUN_ADDR` | Stable | String |   
`ISTIO_META_DNS_AUTO_ALLOCATE` | **Unsupported** | String |   
`ISTIO_META_DNS_CAPTURE` | **Unsupported** | String |   
`ISTIO_META_ENABLE_GSM_TD_LRS` | Stable | String |   
`ISTIO_META_ENABLE_MCP_LRS` | Stable | String |   
`ISTIO_META_GSM_TD_XDS_CAPABILITIES` | Stable | String |   
`ISTIO_META_HTTP10` | **Unsupported** | String |   
`ISTIO_META_PROXY_XDS_VIA_AGENT` | **Unsupported** | String |   
`ISTIO_META_ENABLE_NATIVE_SIDECARS` | **Unsupported** | String |   
`MINIMUM_DRAIN_DURATION` | Stable | String |   
`OUTPUT_CERTS` | **Unsupported** | String |   
`PILOT_ENABLE_CONFIG_DISTRIBUTION_TRACKING` | **Unsupported** | String |   
`PILOT_ENABLE_K8S_SELECT_WORKLOAD_ENTRIES` | **Unsupported** | String |   
`PILOT_JWT_ENABLE_REMOTE_JWKS` | **Unsupported** | String |   
`PLUGINS` | **Unsupported** | String |   
`PROXY_CONFIG_XDS_AGENT` | **Unsupported** | String |   
`SECRET_GRACE_PERIOD_RATIO` | Stable | String |   
`SECRET_TTL` | Stable | String |   
`TERMINATION_DRAIN_DURATION_SECONDS` | Stable | String |   
`TRUST_DOMAIN` | **Unsupported** | String |   
`USE_TOKEN_FOR_CSR` | Stable | String |   
`XDS_AUTH_PROVIDER` | **Unsupported** | String |   
`XDS_HEADER_Cloud-Run-Enable-H2` | **Unsupported** | String |   
`XDS_ROOT_CA` | **Unsupported** | String |   
`runtimeValues` | Stable | Key-value map |   
  
### Security & Other Settings (defaultConfig.sds, privateKeyProvider, proxyStatsMatcher, image)

The following table lists the field-level support for `defaultConfig.sds`, `privateKeyProvider`, `proxyStatsMatcher`, and `image`.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`image.imageType` | Stable | String (`distroless`) | Only `distroless` is supported.  
`privateKeyProvider.cryptomb.pollDelay` | **Unsupported** | Duration |   
`privateKeyProvider.qat.pollDelay` | **Unsupported** | Duration |   
`proxyStatsMatcher.inclusionPrefixes` | Stable | **Array of strings** |   
`proxyStatsMatcher.inclusionRegexps` | Stable | **Array of strings** |   
`proxyStatsMatcher.inclusionSuffixes` | Stable | **Array of strings** |   
`sds.enabled` | **Unsupported** | Boolean |   
`sds.k8sSaJwtPath` | **Unsupported** | String |   
  
## GCPBackend (networking.gke.io/v1)

The following sections describe the supported fields for `GCPBackend` resources.

### Spec Fields

The following table lists the supported spec fields.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`spec.hostname` | Stable | String (RFC 1123 hostname) |   
`spec.port` | Stable | Integer |   
`spec.type` | Stable | String (`CloudRun`, `BackendService`, or unset for `spec.serviceUris`) |   
`spec.cloudrun.service` | Stable | String |   
`spec.cloudrun.regions` | Stable | **Array of strings** (Region) |   
`spec.cloudrun.project` | Stable | String | Must be the project ID of the cluster. Cross-project Cloud Run backends aren't supported.  
`spec.backendservice.name` | Stable | String |   
`spec.backendservice.location` | Stable | String (`global`) | Must be `global`. Regional backend services aren't supported.  
`spec.backendservice.project` | Stable | String (Project ID) | Must be the project ID of the cluster. Cross-project backend services aren't supported.  
`spec.serviceUris` | Stable | **Array of strings** (URI) | All URIs must be of the same type, must be regional, and at most one URI per region is allowed.  
  
## GCPBackendPolicy (networking.gke.io/v1)

The following sections describe the supported fields for `GCPBackendPolicy` resources.

### Root & Default Policy Fields

The following table lists the supported root and default policy fields.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`targetRef` | Stable | Object (`group`, `kind`, `name`, `namespace`) | Must target a `Service`. Cross-namespace references are not supported.  
`default.maxRatePerEndpoint` | Stable | Integer |   
`default.backendPreference` | Stable | String (`DEFAULT`, `PREFERRED`) |   
`default.logging` | **Unsupported** | Object |   
`default.sessionAffinity` | **Unsupported** | Object |   
`default.connectionDraining` | **Unsupported** | Object |   
`default.timeoutSec` | **Unsupported** | Integer |   
`default.securityPolicy` | **Unsupported** | String |   
`default.iap` | **Unsupported** | Object |   
`default.balancingMode` | **Unsupported** | String |   
`default.capacityScalerPercent` | **Unsupported** | Integer |   
`default.customMetrics` | **Unsupported** | **Array of objects** |   
`default.scopes` | **Unsupported** | **Array of objects** |   
`default.trafficDuration` | **Unsupported** | String |   
`default.maxInFlightRequestsPerEndpoint` | **Unsupported** | Integer |   
  
## GCPTrafficDistributionPolicy (networking.gke.io/v1)

The following sections describe the supported fields for `GCPTrafficDistributionPolicy` resources.

### Root & Default Policy Fields

The following table lists the supported root and default policy fields.

Field | Highest Channel Support | Supported Data Types (Values) | Limitations  
---|---|---|---  
`targetRefs` | Stable | **Array of objects** (`group`, `kind`, `name`) | Must reference `Service` resources.  
`default.serviceLbAlgorithm` | Stable | String (`SPRAY_TO_REGION`, `WATERFALL_BY_ZONE`, `WATERFALL_BY_REGION`) | Defaults to `WATERFALL_BY_REGION` if omitted.  
`default.autoCapacityDrain.enableAutoCapacityDrain` | Stable | Boolean |   
`default.failoverConfig.failoverHealthThreshold` | Stable | Integer |   
`default.localityLbAlgorithm` | **Unsupported** | String |   
`default.minimumHashRingSize` | **Unsupported** | Integer |   
`default.customMetrics` | **Unsupported** | **Array of objects** |   
`default.sessionAffinity` | **Unsupported** | Object |   
`default.subsetting` | **Unsupported** | String |   
`default.sharding` | **Unsupported** | Object |   
  
## Annotations

The following table lists the supported annotations.

Annotation | Highest Channel Support | Resource | Description | Limitations  
---|---|---|---|---  
`alpha.istio.io/canonical-serviceaccounts` | **Unsupported** | Service | Specifies the non-Kubernetes service accounts that are allowed to run this service. | Deprecated.  
`alpha.istio.io/identity` | **Unsupported** | Pod | Identity for the workload. | Deprecated.  
`alpha.istio.io/kubernetes-serviceaccounts` | **Unsupported** | Service | Specifies the Kubernetes service accounts that are allowed to run this service on the VMs. | Deprecated.  
`galley.istio.io/analyze-suppress` | **Unsupported** | Any | A comma-separated list of configuration analysis message codes to suppress when Istio analyzers are run (for example, `galley.istio.io/analyze-suppress=IST0108,IST0103` or `*` for all). |   
`gateway.istio.io/controller-version` | **Unsupported** | Any | A version added to the Gateway by the controller specifying the controller version. |   
`inject.istio.io/templates` | Stable | Pod | The names of the inject templates to use, as a comma-separated list. See [custom templates](https://istio.io/latest/docs/setup/additional-setup/sidecar-injection/#custom-templates-experimental). |   
`install.operator.istio.io/chart-owner` | Stable | Any | Represents the name of the chart used to create this resource. |   
`install.operator.istio.io/owner-generation` | Stable | Any | Represents the generation to which the resource was last reconciled. |   
`install.operator.istio.io/version` | Stable | Any | Represents the Istio version associated with the resource. |   
`istio.io/autoRegistrationGroup` | **Unsupported** | WorkloadEntry | On a WorkloadEntry, stores the associated WorkloadGroup. |   
`istio.io/connectedAt` | **Unsupported** | WorkloadEntry | On a WorkloadEntry, stores the time in nanoseconds when the associated workload connected to a Pilot instance. |   
`istio.io/disconnectedAt` | **Unsupported** | WorkloadEntry | On a WorkloadEntry, stores the time in nanoseconds when the associated workload disconnected from a Pilot instance. |   
`istio.io/dry-run` | Stable | AuthorizationPolicy | Specifies whether the given resource is in dry-run mode. See [dry-run mode](https://istio.io/latest/docs/tasks/security/authorization/authz-dry-run/). |   
`istio.io/rev` | Stable | Pod | Specifies a control plane revision to which a given proxy is connected. | Added automatically by the control plane; not set by a user. Represents the actual revision, not the requested revision.  
`istio.io/workloadController` | **Unsupported** | WorkloadEntry | On a WorkloadEntry, stores the current or last pilot instance connected to the workload for XDS. |   
`kubernetes.io/ingress.class` | Stable | Ingress | Annotation on an Ingress resource denoting the class of controllers responsible for it. |   
`networking.istio.io/exportTo` | **Unsupported** | Service | Specifies the namespaces to which this service should be exported. A value of `*` indicates it is reachable within the mesh, `.` indicates it is reachable within its namespace. |   
`prometheus.istio.io/merge-metrics` | **Unsupported** | Pod | Specifies whether application Prometheus metrics are merged with Envoy metrics for this workload. |   
`proxy.istio.io/config` | Stable | Pod | Overrides for the proxy configuration for this specific proxy. Available options can be found in the [ProxyConfig reference](https://istio.io/docs/reference/config/istio.mesh.v1alpha1/#ProxyConfig). |   
`proxy.istio.io/overrides` | Stable | Pod | Used internally to indicate user-specified overrides in the proxy container of the pod during injection. |   
`readiness.status.sidecar.istio.io/applicationPorts` | **Unsupported** | Pod | Specifies the list of ports exposed by the application container. Used by the Envoy sidecar readiness probe to determine that Envoy is configured and ready to receive traffic. |   
`readiness.status.sidecar.istio.io/failureThreshold` | **Unsupported** | Pod | Specifies the failure threshold for the Envoy sidecar readiness probe. |   
`readiness.status.sidecar.istio.io/initialDelaySeconds` | **Unsupported** | Pod | Specifies the initial delay (in seconds) for the Envoy sidecar readiness probe. |   
`readiness.status.sidecar.istio.io/periodSeconds` | **Unsupported** | Pod | Specifies the period (in seconds) for the Envoy sidecar readiness probe. |   
`sidecar.istio.io/agentLogLevel` | Stable | Pod | Specifies the log output level for `pilot-agent`. |   
`sidecar.istio.io/bootstrapOverride` | **Unsupported** | Pod | Specifies an alternative Envoy bootstrap configuration file. |   
`sidecar.istio.io/componentLogLevel` | **Unsupported** | Pod | Specifies the component log level for Envoy. |   
`sidecar.istio.io/controlPlaneAuthPolicy` | **Unsupported** | Pod | Specifies the authentication policy used by the Istio control plane. If `NONE`, traffic won't be encrypted. If `MUTUAL_TLS`, traffic between Envoy sidecars is wrapped into mutual TLS connections. | Deprecated.  
`sidecar.istio.io/discoveryAddress` | **Unsupported** | Pod | Specifies the XDS address to use for this specific workload. | Deprecated.  
`sidecar.istio.io/enableCoreDump` | Stable | Pod | Specifies whether an Envoy sidecar should enable core dump. |   
`sidecar.istio.io/extraStatTags` | **Unsupported** | Pod | An additional list of tags to extract from the in-proxy Istio Wasm telemetry. | Deprecated.  
`sidecar.istio.io/inject` | Stable | Pod | Specifies whether an Envoy sidecar should be automatically injected into the workload. | Deprecated in favor of the `sidecar.istio.io/inject` label.  
`sidecar.istio.io/interceptionMode` | Stable | Pod | Specifies the mode used to redirect inbound connections to Envoy (`REDIRECT` or `TPROXY`). |   
`sidecar.istio.io/logLevel` | Stable | Pod | Specifies the log level for Envoy. |   
`sidecar.istio.io/proxyCPU` | Stable | Pod | Specifies the requested CPU setting for the Envoy sidecar. |   
`sidecar.istio.io/proxyCPULimit` | Stable | Pod | Specifies the CPU limit for the Envoy sidecar. |   
`sidecar.istio.io/proxyImage` | **Unsupported** | Pod | Specifies the Docker image to be used by the Envoy sidecar. |   
`sidecar.istio.io/proxyImageType` | Stable | Pod | Specifies the Docker image type to be used by the Envoy sidecar. | Only `distroless` is supported.  
`sidecar.istio.io/proxyMemory` | Stable | Pod | Specifies the requested memory setting for the Envoy sidecar. |   
`sidecar.istio.io/proxyMemoryLimit` | Stable | Pod | Specifies the memory limit for the Envoy sidecar. |   
`sidecar.istio.io/rewriteAppHTTPProbers` | **Unsupported** | Pod | Rewrite HTTP readiness and liveness probes to be redirected to the Envoy sidecar. |   
`sidecar.istio.io/statsHistogramBuckets` | **Unsupported** | Pod | Specifies the custom histogram buckets with a prefix matcher to separate the Istio mesh metrics from the Envoy stats, such as `{"istiocustom":[1,5,10,50,100,500,1000,5000,10000],"cluster.xds-grpc":[1,5,10,25,50,100,250,500,1000,2500,5000,10000]}`. Default buckets are `[0.5,1,5,10,25,50,100,250,500,1000,2500,5000,10000,30000,60000,300000,600000,1800000,3600000]`. |   
`sidecar.istio.io/statsInclusionPrefixes` | **Unsupported** | Pod | Specifies the comma-separated list of prefixes of the stats to be emitted by Envoy. | Deprecated.  
`sidecar.istio.io/statsInclusionRegexps` | **Unsupported** | Pod | Specifies the comma-separated list of regular expressions the stats should match to be emitted by Envoy. | Deprecated.  
`sidecar.istio.io/statsInclusionSuffixes` | **Unsupported** | Pod | Specifies the comma-separated list of suffixes of the stats to be emitted by Envoy. | Deprecated.  
`sidecar.istio.io/status` | Stable | Pod | Generated by Envoy sidecar injection that indicates the status of the operation. Includes a version hash of the executed template and the names of injected resources. |   
`sidecar.istio.io/userVolume` | **Unsupported** | Pod | Specifies one or more user volumes (as a JSON array) to be added to the Envoy sidecar. |   
`sidecar.istio.io/userVolumeMount` | **Unsupported** | Pod | Specifies one or more user volume mounts (as a JSON array) to be added to the Envoy sidecar. |   
`status.sidecar.istio.io/port` | Stable | Pod | Specifies the HTTP status port for the Envoy sidecar. | If zero, the sidecar won't provide status.  
`topology.istio.io/controlPlaneClusters` | **Unsupported** | Namespace | A comma-separated list of clusters (or `*` for any) running `istiod` that should attempt leader election for a remote cluster whose system namespace includes this annotation. |   
`traffic.istio.io/nodeSelector` | **Unsupported** | Service | A set of node labels (`key1=value,key2=value`) used for cross-network communication. |   
`traffic.sidecar.istio.io/excludeInboundPorts` | Stable | Pod | A comma-separated list of inbound ports to be excluded from redirection to Envoy. | Only applies when all inbound traffic (that is, `*`) is being redirected.  
`traffic.sidecar.istio.io/excludeInterfaces` | Stable | Pod | A comma-separated list of interfaces to be excluded from Istio traffic capture. |   
`traffic.sidecar.istio.io/excludeOutboundIPRanges` | Stable | Pod | A comma-separated list of IP ranges in CIDR form to be excluded from redirection. | Only applies when all outbound traffic (that is, `*`) is being redirected.  
`traffic.sidecar.istio.io/excludeOutboundPorts` | Stable | Pod | A comma-separated list of outbound ports to be excluded from redirection to Envoy. |   
`traffic.sidecar.istio.io/includeInboundPorts` | Stable | Pod | A comma-separated list of inbound ports for which traffic is to be redirected to Envoy. The wildcard character `*` can be used to configure redirection for all ports. An empty list disables all inbound redirection. |   
`traffic.sidecar.istio.io/includeOutboundIPRanges` | Stable | Pod | A comma-separated list of IP ranges in CIDR form to redirect to Envoy (optional). The wildcard character `*` can be used to redirect all outbound traffic. An empty list disables all outbound redirection. |   
`traffic.sidecar.istio.io/includeOutboundPorts` | Stable | Pod | A comma-separated list of outbound ports for which traffic is to be redirected to Envoy, regardless of the destination IP. |   
`traffic.sidecar.istio.io/kubevirtInterfaces` | **Unsupported** | Pod | A comma-separated list of virtual interfaces whose inbound traffic (from VM) is treated as outbound. |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
