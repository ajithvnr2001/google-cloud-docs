---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/onboarding/unsupported-istio-apis/
title: Unsupported Istio APIs in Managed Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:28:35.947641+00:00
---

# Unsupported Istio APIs in Managed Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/onboarding/unsupported-istio-apis/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Unsupported Istio APIs in Managed Cloud Service Mesh

This page contains a non-exhaustive list of the API fields and their corresponding Istio API that are unsupported in `TRAFFIC_DIRECTOR` or `ISTIOD` control plane implementation.

## Table of contents

  * Annotation
  * DestinationRule
  * Gateway
  * MeshConfig
  * Namespace
  * ProxyConfig
  * RequestAuthentication
  * ServiceEntry
  * Service
  * Sidecar
  * Telemetry
  * VirtualService
  * WasmPlugin
  * WorkloadEntry
  * WorkloadGroup



## Annotation

The following annotations are supported. All other annotations not in this list are unsupported.

Annotation | Resource  
---|---  
`inject.istio.io/templates` | Pod  
`install.operator.istio.io/chart-owner` | Any  
`install.operator.istio.io/owner-generation` | Any  
`install.operator.istio.io/version` | Any  
`istio.io/dry-run` | AuthorizationPolicy  
`istio.io/rev` | Pod  
`kubernetes.io/ingress.class` | Ingress  
`proxy.istio.io/config` | Pod  
`proxy.istio.io/overrides` | Pod  
`sidecar.istio.io/agentLogLevel` | Pod  
`sidecar.istio.io/enableCoreDump` | Pod  
`sidecar.istio.io/inject` | Pod  
`sidecar.istio.io/interceptionMode` | Pod  
`sidecar.istio.io/logLevel` | Pod  
`sidecar.istio.io/proxyCPU` | Pod  
`sidecar.istio.io/proxyCPULimit` | Pod  
`sidecar.istio.io/proxyImageType` | Pod  
`sidecar.istio.io/proxyMemory` | Pod  
`sidecar.istio.io/proxyMemoryLimit` | Pod  
`sidecar.istio.io/status` | Pod  
`status.sidecar.istio.io/port` | Pod  
`traffic.sidecar.istio.io/excludeInboundPorts` | Pod  
`traffic.sidecar.istio.io/excludeInterfaces` | Pod  
`traffic.sidecar.istio.io/excludeOutboundIPRanges` | Pod  
`traffic.sidecar.istio.io/excludeOutboundPorts` | Pod  
`traffic.sidecar.istio.io/includeInboundPorts` | Pod  
`traffic.sidecar.istio.io/includeOutboundIPRanges` | Pod  
`traffic.sidecar.istio.io/includeOutboundPorts` | Pod  
  
## DestinationRule

API | Field | Managed (TD) | Managed (istiod)  
---|---|---|---  
DestinationRule | subsets.trafficPolicy.loadBalancer.localityLbSetting.distribute.from |  |   
DestinationRule | subsets.trafficPolicy.loadBalancer.localityLbSetting.distribute.to |  |   
DestinationRule | subsets.trafficPolicy.loadBalancer.localityLbSetting.distribute.to.key |  |   
DestinationRule | subsets.trafficPolicy.loadBalancer.localityLbSetting.distribute.to.value |  |   
DestinationRule | subsets.trafficPolicy.loadBalancer.localityLbSetting.enabled |  |   
DestinationRule | subsets.trafficPolicy.loadBalancer.localityLbSetting.failover.from |  |   
DestinationRule | subsets.trafficPolicy.loadBalancer.localityLbSetting.failover.to |  |   
DestinationRule | subsets.trafficPolicy.loadBalancer.localityLbSetting.failoverPriority |  |   
DestinationRule | subsets.trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.distribute.from |  |   
DestinationRule | subsets.trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.distribute.to |  |   
DestinationRule | subsets.trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.distribute.to.key |  |   
DestinationRule | subsets.trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.distribute.to.value |  |   
DestinationRule | subsets.trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.enabled |  |   
DestinationRule | subsets.trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.failover.from |  |   
DestinationRule | subsets.trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.failover.to |  |   
DestinationRule | subsets.trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.failoverPriority |  |   
DestinationRule | subsets.trafficPolicy.portLevelSettings.tls.credentialName |  |   
DestinationRule | subsets.trafficPolicy.tls.credentialName |  |   
DestinationRule | subsets.trafficPolicy.tunnel.protocol |  |   
DestinationRule | subsets.trafficPolicy.tunnel.targetHost |  |   
DestinationRule | subsets.trafficPolicy.tunnel.targetPort |  |   
DestinationRule | trafficPolicy.loadBalancer.localityLbSetting.distribute.from |  |   
DestinationRule | trafficPolicy.loadBalancer.localityLbSetting.distribute.to |  |   
DestinationRule | trafficPolicy.loadBalancer.localityLbSetting.failoverPriority |  |   
DestinationRule | trafficPolicy.loadBalancer.warmupDurationSecs |  |   
DestinationRule | trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.distribute.from |  |   
DestinationRule | trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.distribute.to |  |   
DestinationRule | trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.enabled |  |   
DestinationRule | trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.failover.from |  |   
DestinationRule | trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.failover.to |  |   
DestinationRule | trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.failoverPriority |  |   
DestinationRule | trafficPolicy.tls.credentialName |  |   
DestinationRule | trafficPolicy.tunnel.protocol |  |   
DestinationRule | trafficPolicy.tunnel.targetHost |  |   
DestinationRule | trafficPolicy.tunnel.targetPort |  |   
DestinationRule | trafficPolicy.portLevelSettings.tls.credentialName |  |   
  
## Gateway

API | Field | Managed (TD) | Managed (istiod)  
---|---|---|---  
Gateway | servers.name |  |   
Gateway | servers.tls.verifyCertificateHash |  |   
Gateway | servers.tls.verifyCertificateSpki |  |   
  
## MeshConfig

API | Field | Managed (TD) | Managed (istiod)  
---|---|---|---  
MeshConfig | ca.address |  |   
MeshConfig | ca.istiodSide |  |   
MeshConfig | ca.requestTimeout |  |   
MeshConfig | ca.tlsSettings.caCertificates |  |   
MeshConfig | ca.tlsSettings.clientCertificate |  |   
MeshConfig | ca.tlsSettings.credentialName |  |   
MeshConfig | ca.tlsSettings.insecureSkipVerify |  |   
MeshConfig | ca.tlsSettings.mode |  |   
MeshConfig | ca.tlsSettings.privateKey |  |   
MeshConfig | ca.tlsSettings.sni |  |   
MeshConfig | ca.tlsSettings.subjectAltNames |  |   
MeshConfig | caCertificates.certSigners |  |   
MeshConfig | caCertificates.spiffeBundleUrl |  |   
MeshConfig | caCertificates.trustDomains |  |   
MeshConfig | certificates.dnsNames |  |   
MeshConfig | certificates.secretName |  |   
MeshConfig | configSources.subscribedResources |  |   
MeshConfig | configSources.tlsSettings.caCertificates |  |   
MeshConfig | configSources.tlsSettings.clientCertificate |  |   
MeshConfig | configSources.tlsSettings.credentialName |  |   
MeshConfig | configSources.tlsSettings.insecureSkipVerify |  |   
MeshConfig | configSources.tlsSettings.mode |  |   
MeshConfig | configSources.tlsSettings.privateKey |  |   
MeshConfig | configSources.tlsSettings.sni |  |   
MeshConfig | configSources.tlsSettings.subjectAltNames |  |   
MeshConfig | connectTimeout |  |   
MeshConfig | defaultHttpRetryPolicy |  |   
MeshConfig | defaultProviders.metrics |  |   
MeshConfig | disableEnvoyListenerLog |  |   
MeshConfig | dnsRefreshRate |  |   
MeshConfig | enableAutoMtls |  |   
MeshConfig | enableEnvoyAccessLogService |  |   
MeshConfig | enablePrometheusMerge |  |   
MeshConfig | enableTracing |  |   
MeshConfig | extensionProviders.datadog.maxTagLength |  |   
MeshConfig | extensionProviders.datadog.port |  |   
MeshConfig | extensionProviders.datadog.service |  |   
MeshConfig | extensionProviders.envoyExtAuthzHttp.includeAdditionalHeadersInCheck.key |  |   
MeshConfig | extensionProviders.envoyExtAuthzHttp.includeAdditionalHeadersInCheck.value |  |   
MeshConfig | extensionProviders.envoyExtAuthzHttp.includeRequestBodyInCheck.allowPartialMessage |  |   
MeshConfig | extensionProviders.envoyExtAuthzHttp.includeRequestBodyInCheck.maxRequestBytes |  |   
MeshConfig | extensionProviders.envoyExtAuthzHttp.includeRequestBodyInCheck.packAsBytes |  |   
MeshConfig | extensionProviders.envoyFileAccessLog.logFormat.labels.fields |  |   
MeshConfig | extensionProviders.envoyFileAccessLog.logFormat.text |  |   
MeshConfig | extensionProviders.envoyFileAccessLog.path |  |   
MeshConfig | extensionProviders.envoyHttpAls.additionalRequestHeadersToLog |  |   
MeshConfig | extensionProviders.envoyHttpAls.additionalResponseHeadersToLog |  |   
MeshConfig | extensionProviders.envoyHttpAls.additionalResponseTrailersToLog |  |   
MeshConfig | extensionProviders.envoyHttpAls.filterStateObjectsToLog |  |   
MeshConfig | extensionProviders.envoyHttpAls.logName |  |   
MeshConfig | extensionProviders.envoyHttpAls.port |  |   
MeshConfig | extensionProviders.envoyHttpAls.service |  |   
MeshConfig | extensionProviders.envoyOtelAls.logFormat.labels.fields |  |   
MeshConfig | extensionProviders.envoyOtelAls.logFormat.text |  |   
MeshConfig | extensionProviders.envoyOtelAls.logName |  |   
MeshConfig | extensionProviders.envoyOtelAls.port |  |   
MeshConfig | extensionProviders.envoyOtelAls.service |  |   
MeshConfig | extensionProviders.envoyTcpAls.filterStateObjectsToLog |  |   
MeshConfig | extensionProviders.envoyTcpAls.logName |  |   
MeshConfig | extensionProviders.envoyTcpAls.port |  |   
MeshConfig | extensionProviders.envoyTcpAls.service |  |   
MeshConfig | extensionProviders.lightstep.accessToken |  |   
MeshConfig | extensionProviders.lightstep.maxTagLength |  |   
MeshConfig | extensionProviders.lightstep.port |  |   
MeshConfig | extensionProviders.lightstep.service |  |   
MeshConfig | extensionProviders.opencensus.context |  |   
MeshConfig | extensionProviders.opencensus.maxTagLength |  |   
MeshConfig | extensionProviders.opencensus.port |  |   
MeshConfig | extensionProviders.opencensus.service |  |   
MeshConfig | extensionProviders.opentelemetry.dynatraceSampler |  |   
MeshConfig | extensionProviders.opentelemetry.http |  |   
MeshConfig | extensionProviders.opentelemetry.maxTagLength |  |   
MeshConfig | extensionProviders.opentelemetry.port |  |   
MeshConfig | extensionProviders.opentelemetry.resourceDetectors |  |   
MeshConfig | extensionProviders.opentelemetry.service |  |   
MeshConfig | extensionProviders.prometheus |  |   
MeshConfig | extensionProviders.skywalking.accessToken |  |   
MeshConfig | extensionProviders.skywalking.port |  |   
MeshConfig | extensionProviders.skywalking.service |  |   
MeshConfig | extensionProviders.stackdriver.debug |  |   
MeshConfig | extensionProviders.stackdriver.logging.labels.key |  |   
MeshConfig | extensionProviders.stackdriver.logging.labels.value |  |   
MeshConfig | extensionProviders.stackdriver.maxNumberOfAnnotations |  |   
MeshConfig | extensionProviders.stackdriver.maxNumberOfAttributes |  |   
MeshConfig | extensionProviders.stackdriver.maxNumberOfMessageEvents |  |   
MeshConfig | extensionProviders.stackdriver.maxTagLength |  |   
MeshConfig | extensionProviders.zipkin.enable64bitTraceId |  |   
MeshConfig | extensionProviders.zipkin.maxTagLength |  |   
MeshConfig | extensionProviders.zipkin.port |  |   
MeshConfig | extensionProviders.zipkin.service |  |   
MeshConfig | h2UpgradePolicy |  |   
MeshConfig | inboundClusterStatName |  |   
MeshConfig | inboundTrafficPolicy.mode |  |   
MeshConfig | ingressClass |  |   
MeshConfig | ingressControllerMode |  |   
MeshConfig | ingressSelector |  |   
MeshConfig | ingressService |  |   
MeshConfig | localityLbSetting |  |   
MeshConfig | localityLbSetting.distribute.from |  |   
MeshConfig | localityLbSetting.distribute.to |  |   
MeshConfig | localityLbSetting.distribute.to.key |  |   
MeshConfig | localityLbSetting.distribute.to.value |  |   
MeshConfig | localityLbSetting.failoverPriority |  |   
MeshConfig | meshMTLS |  |   
MeshConfig | outboundClusterStatName |  |   
MeshConfig | outboundTrafficPolicy |  |   
MeshConfig | pathNormalization.normalization |  |   
MeshConfig | protocolDetectionTimeout |  |   
MeshConfig | proxyHttpPort |  |   
MeshConfig | proxyInboundListenPort |  |   
MeshConfig | proxyListenPort |  |   
MeshConfig | rootNamespace |  |   
MeshConfig | serviceSettings.hosts |  |   
MeshConfig | tcpKeepalive.interval |  |   
MeshConfig | tcpKeepalive.probes |  |   
MeshConfig | tcpKeepalive.time |  |   
MeshConfig | tlsDefaults |  |   
MeshConfig | trustDomain |  |   
MeshConfig | trustDomainAliases |  |   
MeshConfig | verifyCertificateAtClient |  |   
  
## Namespace

API | Field | Managed (TD) | Managed (istiod)  
---|---|---|---  
Namespace | topology.istio.io/controlPlaneClusters |  |   
  
## ProxyConfig

API | Field | Managed (TD) | Managed (istiod)  
---|---|---|---  
ProxyConfig | adminPort |  |   
ProxyConfig | availabilityZone |  |   
ProxyConfig | binaryPath |  |   
ProxyConfig | caCertificatesPem |  |   
ProxyConfig | configPath |  |   
ProxyConfig | controlPlaneAuthPolicy |  |   
ProxyConfig | customConfigFile |  |   
ProxyConfig | discoveryAddress |  |   
ProxyConfig | discoveryRefreshDelay |  |   
ProxyConfig | envoyAccessLogService.address |  |   
ProxyConfig | envoyAccessLogService.tcpKeepalive.interval.nanos |  |   
ProxyConfig | envoyAccessLogService.tcpKeepalive.interval.seconds |  |   
ProxyConfig | envoyAccessLogService.tcpKeepalive.probes |  |   
ProxyConfig | envoyAccessLogService.tcpKeepalive.time.nanos |  |   
ProxyConfig | envoyAccessLogService.tcpKeepalive.time.seconds |  |   
ProxyConfig | envoyAccessLogService.tlsSettings.caCertificates |  |   
ProxyConfig | envoyAccessLogService.tlsSettings.clientCertificate |  |   
ProxyConfig | envoyAccessLogService.tlsSettings.credentialName |  |   
ProxyConfig | envoyAccessLogService.tlsSettings.insecureSkipVerify |  |   
ProxyConfig | envoyAccessLogService.tlsSettings.mode |  |   
ProxyConfig | envoyAccessLogService.tlsSettings.privateKey |  |   
ProxyConfig | envoyAccessLogService.tlsSettings.sni |  |   
ProxyConfig | envoyAccessLogService.tlsSettings.subjectAltNames |  |   
ProxyConfig | envoyMetricsService.address |  |   
ProxyConfig | envoyMetricsService.tcpKeepalive.interval.nanos |  |   
ProxyConfig | envoyMetricsService.tcpKeepalive.interval.seconds |  |   
ProxyConfig | envoyMetricsService.tcpKeepalive.probes |  |   
ProxyConfig | envoyMetricsService.tcpKeepalive.time.nanos |  |   
ProxyConfig | envoyMetricsService.tcpKeepalive.time.seconds |  |   
ProxyConfig | envoyMetricsService.tlsSettings.caCertificates |  |   
ProxyConfig | envoyMetricsService.tlsSettings.clientCertificate |  |   
ProxyConfig | envoyMetricsService.tlsSettings.credentialName |  |   
ProxyConfig | envoyMetricsService.tlsSettings.insecureSkipVerify |  |   
ProxyConfig | envoyMetricsService.tlsSettings.mode |  |   
ProxyConfig | envoyMetricsService.tlsSettings.privateKey |  |   
ProxyConfig | envoyMetricsService.tlsSettings.sni |  |   
ProxyConfig | envoyMetricsService.tlsSettings.subjectAltNames |  |   
ProxyConfig | envoyMetricsServiceAddress |  |   
ProxyConfig | extraStatTags |  |   
ProxyConfig | gatewayTopology.proxyProtocol |  |   
ProxyConfig | image.imageType |  |   
ProxyConfig | interceptionMode |  |   
ProxyConfig | meshId |  |   
ProxyConfig | privateKeyProvider.cryptomb.pollDelay.nanos |  |   
ProxyConfig | privateKeyProvider.cryptomb.pollDelay.seconds |  |   
ProxyConfig | privateKeyProvider.qat.pollDelay.nanos |  |   
ProxyConfig | privateKeyProvider.qat.pollDelay.seconds |  |   
ProxyConfig | proxyBootstrapTemplatePath |  |   
ProxyConfig | proxyHeaders.attemptCount.disabled |  |   
ProxyConfig | proxyHeaders.forwardedClientCert |  |   
ProxyConfig | proxyHeaders.metadataExchangeHeaders.mode |  |   
ProxyConfig | proxyHeaders.requestId.disabled |  |   
ProxyConfig | proxyHeaders.server.disabled |  |   
ProxyConfig | proxyHeaders.server.value |  |   
ProxyConfig | proxyMetadata.CA_ROOT_CA |  |   
ProxyConfig | proxyMetadata.ENABLE_NATIVE_SIDECARS |  |   
ProxyConfig | proxyMetadata.GCE_METADATA_HOST |  |   
ProxyConfig | proxyMetadata.HTTPS_PROXY |  |   
ProxyConfig | proxyMetadata.HTTP_PROXY |  |   
ProxyConfig | proxyMetadata.ISTIO_LOG_LEVEL |  |   
ProxyConfig | proxyMetadata.ISTIO_META_DNS_AUTO_ALLOCATE |  |   
ProxyConfig | proxyMetadata.ISTIO_META_DNS_CAPTURE |  |   
ProxyConfig | proxyMetadata.ISTIO_META_ENABLE_NATIVE_SIDECARS |  |   
ProxyConfig | proxyMetadata.ISTIO_META_HTTP10 |  |   
ProxyConfig | proxyMetadata.ISTIO_META_PROXY_XDS_VIA_AGENT |  |   
ProxyConfig | proxyMetadata.OUTPUT_CERTS |  |   
ProxyConfig | proxyMetadata.PILOT_ENABLE_CONFIG_DISTRIBUTION_TRACKING |  |   
ProxyConfig | proxyMetadata.PILOT_ENABLE_K8S_SELECT_WORKLOAD_ENTRIES |  |   
ProxyConfig | proxyMetadata.PILOT_JWT_ENABLE_REMOTE_JWKS |  |   
ProxyConfig | proxyMetadata.PLUGINS |  |   
ProxyConfig | proxyMetadata.PROXY_CONFIG_XDS_AGENT |  |   
ProxyConfig | proxyMetadata.TRUST_DOMAIN |  |   
ProxyConfig | proxyMetadata.XDS_AUTH_PROVIDER |  |   
ProxyConfig | proxyMetadata.XDS_HEADER_Cloud-Run-Enable-H2 |  |   
ProxyConfig | proxyMetadata.XDS_ROOT_CA |  |   
ProxyConfig | readinessProbe.exec.command |  |   
ProxyConfig | readinessProbe.failureThreshold |  |   
ProxyConfig | readinessProbe.httpGet.host |  |   
ProxyConfig | readinessProbe.httpGet.httpHeaders.name |  |   
ProxyConfig | readinessProbe.httpGet.httpHeaders.value |  |   
ProxyConfig | readinessProbe.httpGet.path |  |   
ProxyConfig | readinessProbe.httpGet.port |  |   
ProxyConfig | readinessProbe.httpGet.scheme |  |   
ProxyConfig | readinessProbe.initialDelaySeconds |  |   
ProxyConfig | readinessProbe.periodSeconds |  |   
ProxyConfig | readinessProbe.successThreshold |  |   
ProxyConfig | readinessProbe.tcpSocket.host |  |   
ProxyConfig | readinessProbe.tcpSocket.port |  |   
ProxyConfig | readinessProbe.timeoutSeconds |  |   
ProxyConfig | sds.enabled |  |   
ProxyConfig | sds.k8sSaJwtPath |  |   
ProxyConfig | serviceCluster |  |   
ProxyConfig | statNameLength |  |   
ProxyConfig | statsdUdpAddress |  |   
ProxyConfig | statusPort |  |   
ProxyConfig | tracing.customTags |  |   
ProxyConfig | tracing.datadog.address |  |   
ProxyConfig | tracing.lightstep.accessToken |  |   
ProxyConfig | tracing.lightstep.address |  |   
ProxyConfig | tracing.maxPathTagLength |  |   
ProxyConfig | tracing.openCensusAgent.address |  |   
ProxyConfig | tracing.openCensusAgent.context |  |   
ProxyConfig | tracing.sampling |  |   
ProxyConfig | tracing.stackdriver.debug |  |   
ProxyConfig | tracing.stackdriver.maxNumberOfAnnotations |  |   
ProxyConfig | tracing.stackdriver.maxNumberOfAttributes |  |   
ProxyConfig | tracing.stackdriver.maxNumberOfMessageEvents |  |   
ProxyConfig | tracing.tlsSettings.caCertificates |  |   
ProxyConfig | tracing.tlsSettings.clientCertificate |  |   
ProxyConfig | tracing.tlsSettings.credentialName |  |   
ProxyConfig | tracing.tlsSettings.insecureSkipVerify |  |   
ProxyConfig | tracing.tlsSettings.mode |  |   
ProxyConfig | tracing.tlsSettings.privateKey |  |   
ProxyConfig | tracing.tlsSettings.sni |  |   
ProxyConfig | tracing.tlsSettings.subjectAltNames |  |   
ProxyConfig | tracing.zipkin.address |  |   
ProxyConfig | tracingServiceName |  |   
ProxyConfig | zipkinAddress |  |   
  
## RequestAuthentication

API | Field | Managed (TD) | Managed (istiod)  
---|---|---|---  
RequestAuthentication | jwtRules.outputClaimToHeader.claim |  |   
RequestAuthentication | jwtRules.outputClaimToHeader.header |  |   
  
## Service

API | Field | Managed (TD) | Managed (istiod)  
---|---|---|---  
Service | networking.istio.io/traffic-distribution |  |   
Service | traffic.istio.io/nodeSelector |  |   
  
## ServiceEntry

API | Field | Managed (TD) | Managed (istiod)  
---|---|---|---  
ServiceEntry | endpoints.locality |  |   
ServiceEntry | endpoints.network |  |   
ServiceEntry | endpoints.serviceAccount |  |   
ServiceEntry | endpoints.weight |  |   
ServiceEntry | subjectAltNames |  |   
ServiceEntry | workloadSelector |  |   
  
## Sidecar

API | Field | Managed (TD) | Managed (istiod)  
---|---|---|---  
Sidecar | egress.bind |  |   
Sidecar | egress.captureMode |  |   
Sidecar | egress.port.name |  |   
Sidecar | egress.port.number |  |   
Sidecar | egress.port.protocol |  |   
Sidecar | egress.port.targetPort |  |   
Sidecar | inboundConnectionPool.http.h2UpgradePolicy |  |   
Sidecar | inboundConnectionPool.http.http1MaxPendingRequests |  |   
Sidecar | inboundConnectionPool.http.http2MaxRequests |  |   
Sidecar | inboundConnectionPool.http.idleTimeout |  |   
Sidecar | inboundConnectionPool.http.maxRequestsPerConnection |  |   
Sidecar | inboundConnectionPool.http.maxRetries |  |   
Sidecar | inboundConnectionPool.http.useClientProtocol |  |   
Sidecar | inboundConnectionPool.tcp.connectTimeout |  |   
Sidecar | inboundConnectionPool.tcp.maxConnectionDuration |  |   
Sidecar | inboundConnectionPool.tcp.maxConnections |  |   
Sidecar | inboundConnectionPool.tcp.tcpKeepalive.interval |  |   
Sidecar | inboundConnectionPool.tcp.tcpKeepalive.probes |  |   
Sidecar | inboundConnectionPool.tcp.tcpKeepalive.time |  |   
Sidecar | ingress.bind |  |   
Sidecar | ingress.captureMode |  |   
Sidecar | ingress.connectionPool.http.h2UpgradePolicy |  |   
Sidecar | ingress.connectionPool.http.http1MaxPendingRequests |  |   
Sidecar | ingress.connectionPool.http.http2MaxRequests |  |   
Sidecar | ingress.connectionPool.http.idleTimeout |  |   
Sidecar | ingress.connectionPool.http.maxRequestsPerConnection |  |   
Sidecar | ingress.connectionPool.http.maxRetries |  |   
Sidecar | ingress.connectionPool.http.useClientProtocol |  |   
Sidecar | ingress.connectionPool.tcp.connectTimeout |  |   
Sidecar | ingress.connectionPool.tcp.maxConnectionDuration |  |   
Sidecar | ingress.connectionPool.tcp.maxConnections |  |   
Sidecar | ingress.connectionPool.tcp.tcpKeepalive.interval |  |   
Sidecar | ingress.connectionPool.tcp.tcpKeepalive.probes |  |   
Sidecar | ingress.connectionPool.tcp.tcpKeepalive.time |  |   
Sidecar | ingress.defaultEndpoint |  |   
Sidecar | ingress.port.name |  |   
Sidecar | ingress.port.number |  |   
Sidecar | ingress.port.protocol |  |   
Sidecar | ingress.port.targetPort |  |   
Sidecar | ingress.tls.caCertificates |  |   
Sidecar | ingress.tls.cipherSuites |  |   
Sidecar | ingress.tls.credentialName |  |   
Sidecar | ingress.tls.httpsRedirect |  |   
Sidecar | ingress.tls.maxProtocolVersion |  |   
Sidecar | ingress.tls.minProtocolVersion |  |   
Sidecar | ingress.tls.mode |  |   
Sidecar | ingress.tls.privateKey |  |   
Sidecar | ingress.tls.serverCertificate |  |   
Sidecar | ingress.tls.subjectAltNames |  |   
Sidecar | ingress.tls.verifyCertificateHash |  |   
Sidecar | ingress.tls.verifyCertificateSpki |  |   
Sidecar | outboundTrafficPolicy.egressProxy.host |  |   
Sidecar | outboundTrafficPolicy.egressProxy.port.number |  |   
Sidecar | outboundTrafficPolicy.egressProxy.subset |  |   
  
## Telemetry

API | Field | Managed (TD) | Managed (istiod)  
---|---|---|---  
Telemetry | accessLogging.filter.expression |  |   
Telemetry | accessLogging.match |  |   
Telemetry | metrics.overrides.disabled |  |   
Telemetry | metrics.overrides.match.customMetric |  |   
Telemetry | metrics.overrides.match.metric |  |   
Telemetry | metrics.overrides.match.mode |  |   
Telemetry | metrics.overrides.tagOverrides |  |   
Telemetry | metrics.providers.name |  |   
Telemetry | metrics.reportingInterval |  |   
Telemetry | tracing.customTags |  |   
Telemetry | tracing.match.mode |  |   
  
## VirtualService

API | Field | Managed (TD) | Managed (istiod)  
---|---|---|---  
VirtualService | http.corsPolicy.maxAge.nanos |  |   
VirtualService | http.fault.abort.grpcStatus |  |   
VirtualService | http.fault.abort.http2Error |  |   
VirtualService | http.fault.delay.exponentialDelay |  |   
VirtualService | http.match.statPrefix |  |   
VirtualService | http.mirrorPercent.value |  |   
VirtualService | http.mirrors.percentage.value |  |   
VirtualService | http.timeout.nanos |  |   
VirtualService | tcp.match.sourceLabels |  |   
VirtualService | tls.match.sourceLabels |  |   
  
## WasmPlugin

API | Field  
---|---  
WasmPlugin | ALL_UNSUPPORTED  
  
## WorkloadEntry

API | Field  
---|---  
WorkloadEntry | ALL_UNSUPPORTED  
  
## WorkloadGroup

API | Field  
---|---  
WorkloadGroup | ALL_UNSUPPORTED  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
