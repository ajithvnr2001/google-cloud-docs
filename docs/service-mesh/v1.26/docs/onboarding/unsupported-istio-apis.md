---
url: https://docs.cloud.google.com/service-mesh/v1.26/docs/onboarding/unsupported-istio-apis/
title: Unsupported Istio APIs in Managed Cloud Service Mesh \u00a0|\u00a0 Cloud Service Mesh v1.26 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:11:39.805067+00:00
---

# Unsupported Istio APIs in Managed Cloud Service Mesh  |  Cloud Service Mesh v1.26  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.26/docs/onboarding/unsupported-istio-apis/

You are viewing archived v1.26 Service Mesh documentation.

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
  * [ v1.26 ](https://docs.cloud.google.com/service-mesh/v1.26/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.26/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Unsupported Istio APIs in Managed Cloud Service Mesh

This page contains a non-exhaustive list of the API fields and their corresponding Istio API that have are unsupported in `TRAFFIC_DIRECTOR` control plane implementation.

## Table of contents

  * DestinationRule
  * MeshConfig
  * Gateway
  * ProxyConfig
  * ServiceEntry
  * Sidecar
  * Telemetry
  * VirtualService
  * WasmPlugin
  * WorkloadEntry
  * WorkloadGroup



## DestinationRule

API | Field  
---|---  
DestinationRule | subsets.trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.failoverPriority  
DestinationRule | trafficPolicy.loadBalancer.localityLbSetting.failoverPriority  
DestinationRule | trafficPolicy.loadBalancer.localityLbSetting.distribute.from  
DestinationRule | trafficPolicy.loadBalancer.localityLbSetting.distribute.to  
DestinationRule | subsets.trafficPolicy.loadBalancer.localityLbSetting.distribute.to  
DestinationRule | subsets.trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.failover.from  
DestinationRule | subsets.trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.failover.to  
DestinationRule | subsets.trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.distribute.to  
DestinationRule | subsets.trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.enabled  
DestinationRule | trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.distribute.to  
DestinationRule | trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.enabled  
DestinationRule | trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.failover.from  
DestinationRule | trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.failover.to  
DestinationRule | trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.failoverPriority  
DestinationRule | trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.distribute.from  
DestinationRule | subsets.trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.distribute.to.key  
DestinationRule | subsets.trafficPolicy.loadBalancer.localityLbSetting.distribute.from  
DestinationRule | subsets.trafficPolicy.loadBalancer.localityLbSetting.distribute.to.value  
DestinationRule | subsets.trafficPolicy.loadBalancer.localityLbSetting.enabled  
DestinationRule | subsets.trafficPolicy.loadBalancer.localityLbSetting.failover.from  
DestinationRule | subsets.trafficPolicy.loadBalancer.localityLbSetting.failover.to  
DestinationRule | subsets.trafficPolicy.loadBalancer.localityLbSetting.failoverPriority  
DestinationRule | subsets.trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.distribute.to.value  
DestinationRule | subsets.trafficPolicy.portLevelSettings.loadBalancer.localityLbSetting.distribute.from  
DestinationRule | trafficPolicy.tunnel.protocol  
DestinationRule | subsets.trafficPolicy.loadBalancer.localityLbSetting.distribute.to.key  
  
## Gateway

API | Field  
---|---  
Gateway | servers.tls.verifyCertificateHash  
Gateway | servers.tls.verifyCertificateSpki  
  
## MeshConfig

API | Field  
---|---  
MeshConfig | ca.tlsSettings.caCertificates  
MeshConfig | localityLbSetting.failoverPriority  
MeshConfig | localityLbSetting.distribute.from  
MeshConfig | localityLbSetting.distribute.to  
MeshConfig | ca.tlsSettings.privateKey  
MeshConfig | configSources.tlsSettings.credentialName  
MeshConfig | extensionProviders.envoyTcpAls.logName  
MeshConfig | extensionProviders.envoyTcpAls.service  
MeshConfig | certificates.dnsNames  
MeshConfig | extensionProviders.lightstep.maxTagLength  
MeshConfig | extensionProviders.lightstep.port  
MeshConfig | configSources.tlsSettings.caCertificates  
MeshConfig | extensionProviders.stackdriver.debug  
MeshConfig | extensionProviders.stackdriver.maxTagLength  
MeshConfig | localityLbSetting.distribute.to.value  
MeshConfig | configSources.tlsSettings.insecureSkipVerify  
MeshConfig | extensionProviders.envoyHttpAls.additionalResponseHeadersToLog  
MeshConfig | extensionProviders.envoyHttpAls.additionalResponseTrailersToLog  
MeshConfig | extensionProviders.envoyOtelAls.logFormat.text  
MeshConfig | extensionProviders.skywalking.accessToken  
MeshConfig | proxyListenPort  
MeshConfig | ca.tlsSettings.subjectAltNames  
MeshConfig | ingressService  
MeshConfig | configSources.subscribedResources  
MeshConfig | extensionProviders.envoyHttpAls.filterStateObjectsToLog  
MeshConfig | extensionProviders.envoyHttpAls.service  
MeshConfig | extensionProviders.envoyTcpAls.filterStateObjectsToLog  
MeshConfig | extensionProviders.stackdriver.logging.labels.key  
MeshConfig | extensionProviders.envoyHttpAls.logName  
MeshConfig | extensionProviders.stackdriver.logging.labels.value  
MeshConfig | proxyInboundListenPort  
MeshConfig | ca.tlsSettings.insecureSkipVerify  
MeshConfig | configSources.tlsSettings.privateKey  
MeshConfig | extensionProviders.envoyHttpAls.port  
MeshConfig | extensionProviders.envoyTcpAls.port  
MeshConfig | extensionProviders.stackdriver.maxNumberOfAttributes  
MeshConfig | extensionProviders.stackdriver.maxNumberOfMessageEvents  
MeshConfig | ingressControllerMode  
MeshConfig | ca.tlsSettings.sni  
MeshConfig | certificates.secretName  
MeshConfig | extensionProviders.datadog.maxTagLength  
MeshConfig | extensionProviders.envoyOtelAls.logName  
MeshConfig | extensionProviders.lightstep.accessToken  
MeshConfig | extensionProviders.opencensus.maxTagLength  
MeshConfig | ingressClass  
MeshConfig | ca.tlsSettings.clientCertificate  
MeshConfig | caCertificates.trustDomains  
MeshConfig | extensionProviders.envoyOtelAls.logFormat.labels.fields  
MeshConfig | extensionProviders.stackdriver.maxNumberOfAnnotations  
MeshConfig | ingressSelector  
MeshConfig | caCertificates.certSigners  
MeshConfig | caCertificates.spiffeBundleUrl  
MeshConfig | configSources.tlsSettings.mode  
MeshConfig | configSources.tlsSettings.sni  
MeshConfig | configSources.tlsSettings.subjectAltNames  
MeshConfig | extensionProviders.lightstep.service  
MeshConfig | proxyHttpPort  
MeshConfig | ca.istiodSide  
MeshConfig | ca.tlsSettings.credentialName  
MeshConfig | extensionProviders.skywalking.port  
MeshConfig | extensionProviders.skywalking.service  
MeshConfig | extensionProviders.zipkin.enable64bitTraceId  
MeshConfig | localityLbSetting.distribute.to.key  
MeshConfig | ca.tlsSettings.mode  
MeshConfig | configSources.tlsSettings.clientCertificate  
MeshConfig | extensionProviders.zipkin.maxTagLength  
MeshConfig | extensionProviders.envoyHttpAls.additionalRequestHeadersToLog  
MeshConfig | extensionProviders.opentelemetry.maxTagLength  
MeshConfig | extensionProviders.envoyExtAuthzHttp.includeAdditionalHeadersInCheck.key  
MeshConfig | extensionProviders.envoyExtAuthzHttp.includeAdditionalHeadersInCheck.value  
MeshConfig | extensionProviders.envoyExtAuthzHttp.includeRequestBodyInCheck.allowPartialMessage  
MeshConfig | extensionProviders.envoyExtAuthzHttp.includeRequestBodyInCheck.maxRequestBytes  
MeshConfig | extensionProviders.envoyExtAuthzHttp.includeRequestBodyInCheck.packAsBytes  
  
## ProxyConfig

API | Field  
---|---  
ProxyConfig | envoyAccessLogService.tlsSettings.subjectAltNames  
ProxyConfig | envoyMetricsService.tlsSettings.caCertificates  
ProxyConfig | envoyMetricsService.tlsSettings.privateKey  
ProxyConfig | readinessProbe.httpGet.httpHeaders.value  
ProxyConfig | discoveryAddress  
ProxyConfig | envoyMetricsService.tcpKeepalive.time.nanos  
ProxyConfig | proxyMetadata.TRUST_DOMAIN  
ProxyConfig | envoyAccessLogService.tcpKeepalive.time.nanos  
ProxyConfig | envoyMetricsService.address  
ProxyConfig | proxyMetadata.XDS_ROOT_CA  
ProxyConfig | readinessProbe.tcpSocket.port  
ProxyConfig | statsdUdpAddress  
ProxyConfig | statusPort  
ProxyConfig | envoyAccessLogService.tcpKeepalive.interval.nanos  
ProxyConfig | envoyMetricsService.tlsSettings.sni  
ProxyConfig | readinessProbe.timeoutSeconds  
ProxyConfig | tracing.openCensusAgent.context  
ProxyConfig | tracing.tlsSettings.mode  
ProxyConfig | tracing.tlsSettings.subjectAltNames  
ProxyConfig | envoyAccessLogService.tcpKeepalive.probes  
ProxyConfig | envoyAccessLogService.tlsSettings.clientCertificate  
ProxyConfig | envoyMetricsService.tlsSettings.mode  
ProxyConfig | readinessProbe.httpGet.scheme  
ProxyConfig | tracing.tlsSettings.caCertificates  
ProxyConfig | envoyAccessLogService.tlsSettings.sni  
ProxyConfig | envoyMetricsService.tlsSettings.credentialName  
ProxyConfig | proxyMetadata.HTTP_PROXY  
ProxyConfig | readinessProbe.failureThreshold  
ProxyConfig | readinessProbe.httpGet.path  
ProxyConfig | tracing.tlsSettings.insecureSkipVerify  
ProxyConfig | customConfigFile  
ProxyConfig | envoyAccessLogService.tlsSettings.credentialName  
ProxyConfig | proxyMetadata.ISTIO_META_PROXY_XDS_VIA_AGENT  
ProxyConfig | proxyMetadata.XDS_HEADER_Cloud-Run-Enable-H2  
ProxyConfig | readinessProbe.exec.command  
ProxyConfig | readinessProbe.httpGet.httpHeaders.name  
ProxyConfig | readinessProbe.initialDelaySeconds  
ProxyConfig | tracing.lightstep.accessToken  
ProxyConfig | tracing.tlsSettings.privateKey  
ProxyConfig | configPath  
ProxyConfig | envoyAccessLogService.address  
ProxyConfig | envoyAccessLogService.tlsSettings.mode  
ProxyConfig | envoyAccessLogService.tlsSettings.privateKey  
ProxyConfig | envoyMetricsService.tcpKeepalive.interval.seconds  
ProxyConfig | proxyMetadata.PILOT_JWT_ENABLE_REMOTE_JWKS  
ProxyConfig | readinessProbe.successThreshold  
ProxyConfig | envoyAccessLogService.tlsSettings.caCertificates  
ProxyConfig | envoyMetricsService.tcpKeepalive.probes  
ProxyConfig | envoyMetricsService.tlsSettings.insecureSkipVerify  
ProxyConfig | privateKeyProvider.qat.pollDelay.nanos  
ProxyConfig | proxyMetadata.CA_ROOT_CA  
ProxyConfig | proxyMetadata.PROXY_CONFIG_XDS_AGENT  
ProxyConfig | readinessProbe.tcpSocket.host  
ProxyConfig | statNameLength  
ProxyConfig | tracing.tlsSettings.credentialName  
ProxyConfig | tracing.tlsSettings.sni  
ProxyConfig | envoyAccessLogService.tlsSettings.insecureSkipVerify  
ProxyConfig | envoyMetricsService.tlsSettings.clientCertificate  
ProxyConfig | envoyMetricsService.tlsSettings.subjectAltNames  
ProxyConfig | meshId  
ProxyConfig | proxyHeaders.server.value  
ProxyConfig | binaryPath  
ProxyConfig | envoyMetricsService.tcpKeepalive.interval.nanos  
ProxyConfig | privateKeyProvider.cryptomb.pollDelay.nanos  
ProxyConfig | proxyBootstrapTemplatePath  
ProxyConfig | tracing.lightstep.address  
ProxyConfig | tracing.tlsSettings.clientCertificate  
ProxyConfig | controlPlaneAuthPolicy  
ProxyConfig | envoyAccessLogService.tcpKeepalive.interval.seconds  
ProxyConfig | envoyMetricsService.tcpKeepalive.time.seconds  
ProxyConfig | readinessProbe.periodSeconds  
ProxyConfig | serviceCluster  
ProxyConfig | envoyAccessLogService.tcpKeepalive.time.seconds  
ProxyConfig | privateKeyProvider.qat.pollDelay.seconds  
ProxyConfig | proxyMetadata.HTTPS_PROXY  
ProxyConfig | proxyMetadata.ISTO_META_ENABLE_NATIVE_SIDECARS  
ProxyConfig | readinessProbe.httpGet.host  
ProxyConfig | privateKeyProvider.cryptomb.pollDelay.seconds  
ProxyConfig | proxyMetadata.XDS_AUTH_PROVIDER  
ProxyConfig | readinessProbe.httpGet.port  
ProxyConfig | gatewayTopology.proxyProtocol  
ProxyConfig | tracing.stackdriver.debug  
ProxyConfig | tracing.stackdriver.maxNumberOfAnnotations  
ProxyConfig | tracing.stackdriver.maxNumberOfAttributes  
ProxyConfig | tracing.stackdriver.maxNumberOfMessageEvents  
  
## ServiceEntry

API | Field  
---|---  
ServiceEntry | endpoints.network  
ServiceEntry | endpoints.serviceAccount  
ServiceEntry | endpoints.weight  
  
## Sidecar

API | Field  
---|---  
Sidecar | inboundConnectionPool.tcp.maxConnections  
Sidecar | ingress.connectionPool.http.maxRetries  
Sidecar | ingress.tls.cipherSuites  
Sidecar | inboundConnectionPool.http.http2MaxRequests  
Sidecar | ingress.connectionPool.tcp.maxConnectionDuration  
Sidecar | ingress.tls.credentialName  
Sidecar | outboundTrafficPolicy.egressProxy.host  
Sidecar | inboundConnectionPool.tcp.tcpKeepalive.interval  
Sidecar | inboundConnectionPool.tcp.tcpKeepalive.time  
Sidecar | ingress.connectionPool.http.h2UpgradePolicy  
Sidecar | ingress.connectionPool.tcp.maxConnections  
Sidecar | ingress.tls.subjectAltNames  
Sidecar | ingress.tls.verifyCertificateHash  
Sidecar | outboundTrafficPolicy.egressProxy.subset  
Sidecar | ingress.connectionPool.tcp.tcpKeepalive.probes  
Sidecar | ingress.tls.maxProtocolVersion  
Sidecar | ingress.tls.privateKey  
Sidecar | egress.port.targetPort  
Sidecar | ingress.connectionPool.http.http1MaxPendingRequests  
Sidecar | ingress.connectionPool.http.useClientProtocol  
Sidecar | ingress.tls.serverCertificate  
Sidecar | inboundConnectionPool.http.maxRetries  
Sidecar | inboundConnectionPool.tcp.maxConnectionDuration  
Sidecar | ingress.connectionPool.tcp.tcpKeepalive.interval  
Sidecar | inboundConnectionPool.http.http1MaxPendingRequests  
Sidecar | ingress.tls.mode  
Sidecar | outboundTrafficPolicy.egressProxy.port.number  
Sidecar | inboundConnectionPool.tcp.connectTimeout  
Sidecar | ingress.connectionPool.http.idleTimeout  
Sidecar | ingress.connectionPool.http.maxRequestsPerConnection  
Sidecar | inboundConnectionPool.http.idleTimeout  
Sidecar | ingress.connectionPool.tcp.tcpKeepalive.time  
Sidecar | ingress.tls.minProtocolVersion  
Sidecar | inboundConnectionPool.http.h2UpgradePolicy  
Sidecar | inboundConnectionPool.http.useClientProtocol  
Sidecar | ingress.connectionPool.http.http2MaxRequests  
Sidecar | ingress.tls.httpsRedirect  
Sidecar | ingress.tls.verifyCertificateSpki  
Sidecar | inboundConnectionPool.http.maxRequestsPerConnection  
Sidecar | inboundConnectionPool.tcp.tcpKeepalive.probes  
Sidecar | ingress.port.targetPort  
Sidecar | ingress.connectionPool.tcp.connectTimeout  
Sidecar | ingress.tls.caCertificates  
  
## Telemetry

API | Field  
---|---  
Telemetry | metrics.reportingInterval  
Telemetry | metrics.overrides.match.customMetric  
Telemetry | accessLogging.match  
  
## VirtualService

API | Field  
---|---  
VirtualService | http.mirrors.percentage.value  
VirtualService | http.match.statPrefix  
VirtualService | http.corsPolicy.maxAge.nanos  
VirtualService | http.fault.abort.http2Error  
VirtualService | http.fault.delay.exponentialDelay  
  
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

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
