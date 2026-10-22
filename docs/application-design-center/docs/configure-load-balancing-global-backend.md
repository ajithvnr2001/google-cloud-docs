---
url: https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-global-backend/
title: Configure a global Cloud Load Balancing backend service \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:58.281714+00:00
---

# Configure a global Cloud Load Balancing backend service  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-global-backend/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a global Cloud Load Balancing backend service Stay organized with collections  Save and categorize content based on your preferences. 

Create a load balancer in your application by configuring and connecting distinct Cloud Load Balancing frontend and backend components. These components let you apply distinct controls for external and internal traffic, and prevent direct access to data.

The global Cloud Load Balancing backend component lets you manage load balancer traffic distribution settings, including the protocol used to connect to backends, session settings, health checks, and timeouts. Configure the following backends:

  * Serverless NEG: A list of serverless Cloud Run or Cloud Run functions applications as backends.

  * Managed Instance Group (MIG): A list of Compute Engine instance groups as backends.




For more information, see [Backend services overview](https://docs.cloud.google.com/load-balancing/docs/backend-service).

This document describes the connections and parameters you configure when using App Design Center to create a global Cloud Load Balancing backend. The configuration parameters are based on the [terraform-google-lb-http](https://github.com/terraform-google-modules/terraform-google-lb-http/tree/main/modules/backend) Terraform module.

## Component connections

To create a complete Cloud Load Balancing component, connect your global Cloud Load Balancing backend to at least one global Cloud Load Balancing frontend. Connected Cloud Load Balancing components are displayed as a group in the design canvas.

The following table lists the components that you connect to a global Cloud Load Balancing backend, and the resulting updates to your application and its generated Terraform code.

Connected component | Application updates | Background information  
---|---|---  
[Cloud Run](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run) | 

  * The load balancer can distribute incoming traffic to the Cloud Run service.
  * The Cloud Run service is added as a backend endpoint in the Cloud Load Balancing serverless NEG backends configuration.

| [Set up a global external Application Load Balancer with Cloud Run](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-serverless)  
[Global Cloud Load Balancing frontend](https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-global-frontend) (required) | 

  * The Cloud Load Balancing frontend, which handles incoming requests, is linked to the Cloud Load Balancing backend, which processes the requests.
  * The backend service information is added to the frontend URL map input.

| [URL maps overview](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts)  
[Compute Engine MIG](https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-mig) | 

  * The load balancer can distribute incoming traffic to the Compute Engine MIG.
  * The Compute Engine MIG is added to the Cloud Load Balancing backend service groups field.

| [Set up a classic Application Load Balancer with a managed instance group backend](https://docs.cloud.google.com/load-balancing/docs/https/ext-https-lb-simple)  
  
## Required configuration parameters

If your template includes a global Cloud Load Balancing backend component, configure the following parameters before you deploy.

Parameter name | Description and constraints | Background information  
---|---|---  
**Name** | Name for the load balancer backend service. | [name](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices)  
**Project ID** | The project where you want to deploy the Cloud Load Balancing backend service. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Parameter name | Description and constraint information | Background information  
---|---|---|---  
**Host Path Mappings** | Host | [Configure URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map#configure_url_maps) | [Use URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map)  
Path | [Configure URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map#configure_url_maps) | [Use URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map)  
| Load Balancing Scheme | [loadBalancingScheme](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.load_balancing_scheme) | [Backend services overview](https://docs.cloud.google.com/load-balancing/docs/backend-service)  
| Protocol | [protocol](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.service_protocol) | [Protocol to the backends](https://docs.cloud.google.com/load-balancing/docs/backend-service#protocol_to_the_backends)  
| Port Name | [portName](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.port_name) | [Named ports](https://docs.cloud.google.com/load-balancing/docs/backend-service#named-ports)  
| Description | A description for the backend service. | [description](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.description)  
| Enable CDN | [enableCDN](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.enable_cdn) | [Cloud CDN overview](https://docs.cloud.google.com/cdn/docs/overview)  
| Compression Mode | [compressionMode](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.compression_mode) | [Compression isn't working](https://docs.cloud.google.com/load-balancing/docs/https/troubleshooting-ext-https-lbs#compression-not-working)  
| Custom Request Headers | [customRequestHeaders[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.custom_request_header) | [Create custom headers in backend services](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers)  
| Custom Response Headers | [customResponseHeaders[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.custom_response_header) | [Create custom headers in backend services](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers)  
| Connection Draining Timeout Sec | [connectionDraining.drainingTimeoutSec](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_20) | [Enable connection draining](https://docs.cloud.google.com/load-balancing/docs/enabling-connection-draining)  
| Session Affinity | [sessionAffinity](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.session_affinity) | [Session affinity](https://docs.cloud.google.com/load-balancing/docs/backend-service#session_affinity)  
| Affinity Cookie TTL Sec | [affinityCookieTtlSec](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.affinity_cookie_ttl_sec) | [Generated cookie affinity](https://docs.cloud.google.com/load-balancing/docs/backend-service#generated_cookie_affinity)  
| Locality LB Policy | [localityLbPolicy](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.locality_lb_policy) | [Load balancing locality policy](https://docs.cloud.google.com/load-balancing/docs/backend-service#lb-locality-policy)  
| Timeout Sec | [timeoutSec](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.timeout_sec) | [Backend service timeout](https://docs.cloud.google.com/load-balancing/docs/backend-service#timeout-setting)  
**Log config** | Enable | [logConfig.enable](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_47) | [Logging](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#logging)  
Sample Rate | [logConfig.sampleRate](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_48) | [Logging](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#logging)  
**Groups** | Group | [backends[].group](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_1) | [Backends](https://docs.cloud.google.com/load-balancing/docs/backend-service#backends)  
Description | A description for the backends group. | [backends[].description](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField)  
Balancing Mode | [backends[].balancingMode](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_2) | [Balancing modes and target capacity settings](https://docs.cloud.google.com/load-balancing/docs/backend-service#target-capacity)  
Capacity Scaler | [backends[].capacityScaler](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_10) | [Capacity scaler](https://docs.cloud.google.com/load-balancing/docs/backend-service#capacity_scaler)  
Max Connections | [backends[].maxConnections](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_7) | [Connection balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#connection_balancing_mode)  
Max Connections Per Instance | [backends[].maxConnectionsPerInstance](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_8) | [Connection balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#connection_balancing_mode)  
Max Connections Per Endpoint | [backends[].maxConnectionsPerEndpoint](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_9) | [Connection balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#connection_balancing_mode)  
Max Rate | [backends[].maxRate](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_4) | [Rate balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#rate_balancing_mode)  
Max Rate Per Instance | [backends[].maxRatePerInstance](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_5) | [Rate balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#rate_balancing_mode)  
Max Rate Per Endpoint | [backends[].maxRatePerEndpoint](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_6) | [Rate balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#rate_balancing_mode)  
Max Utilization | [backends[].maxUtilization](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_3) | [Utilization balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#utilization_balancing_mode)  
**Serverless NEG backends** | Region | [region](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkEndpointGroups#NetworkEndpointGroup.FIELDS.region) | [Serverless network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts)  
Type | The type of serverless backend. Possible values include `cloud-run`, `cloud-function`, or `app-engine`. | [Supported load balancers](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#lb-support)  
Service Name | [appEngine.service](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkEndpointGroups#NetworkEndpointGroup.FIELDS.inlinedField_3) | [Serverless network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts)  
Service Version | [appEngine.version](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkEndpointGroups#NetworkEndpointGroup.FIELDS.inlinedField_4) | [Serverless network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts)  
**IAP Config** | Enable | [iap.enabled](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_21) | [Identity-Aware Proxy overview](https://docs.cloud.google.com/iap/docs/concepts-overview)  
OAuth2 Client ID | [iap.oauth2ClientId](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_22) | [How to share OAuth clients](https://docs.cloud.google.com/iap/docs/sharing-oauth-clients)  
OAuth2 Client Secret | [iap.oauth2ClientSecret](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_23) | [How to share OAuth clients](https://docs.cloud.google.com/iap/docs/sharing-oauth-clients)  
**CDN Policy** | Cache Mode | [cdnPolicy.cacheMode](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_36) | [Caching overview](https://docs.cloud.google.com/cdn/docs/caching)  
Signed URL Cache Max Age Sec | [cdnPolicy.signedUrlCacheMaxAgeSec](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_34) | [Customize the maximum cache time](https://docs.cloud.google.com/cdn/docs/using-signed-urls#customize_the_maximum_cache_time)  
Default TTL | [cdnPolicy.defaultTtl](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_37) | [Change TTL settings and overrides ](https://docs.cloud.google.com/cdn/docs/using-ttl-overrides)  
Max TTL | [cdnPolicy.maxTtl](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_38) | [Change TTL settings and overrides ](https://docs.cloud.google.com/cdn/docs/using-ttl-overrides)  
Client TTL | [cdnPolicy.clientTtl](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_39) | [Change TTL settings and overrides ](https://docs.cloud.google.com/cdn/docs/using-ttl-overrides)  
Negative Caching | [cdnPolicy.negativeCaching](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_40) | [Use negative caching](https://docs.cloud.google.com/cdn/docs/using-negative-caching)  
Serve While Stale | [cdnPolicy.serveWhileStale](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_46) | [Serving stale content](https://docs.cloud.google.com/cdn/docs/serving-stale-content)  
Bypass Cache on Request Headers | [cdnPolicy.bypassCacheOnRequestHeaders[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_44) | [Bypassing cache](https://docs.cloud.google.com/cdn/docs/caching#bypassing-cache)  
**Negative Caching Policy** | Code | [cdnPolicy.negativeCachingPolicy[].code](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_42) | [Use negative caching](https://docs.cloud.google.com/cdn/docs/using-negative-caching)  
TTL | [cdnPolicy.negativeCachingPolicy[].ttl](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_43) | [Use negative caching](https://docs.cloud.google.com/cdn/docs/using-negative-caching)  
**Cache Key Policy** | Include Host | [cdnPolicy.cacheKeyPolicy.includeHost](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_27) | [Cache keys](https://docs.cloud.google.com/cdn/docs/caching#cache-keys)  
Include Protocol | [cdnPolicy.cacheKeyPolicy.includeProtocol](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_26) | [Cache keys](https://docs.cloud.google.com/cdn/docs/caching#cache-keys)  
Include Query String | [cdnPolicy.cacheKeyPolicy.includeQueryString](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_28) | [Query string include list](https://docs.cloud.google.com/cdn/docs/caching#query-string-include)  
Query String Blacklist | [cdnPolicy.cacheKeyPolicy.queryStringBlacklist[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_30) | [Query string exclude list](https://docs.cloud.google.com/cdn/docs/caching#query-string-exclude)  
Query String Whitelist | [cdnPolicy.cacheKeyPolicy.queryStringWhitelist[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_29) | [Query string include list](https://docs.cloud.google.com/cdn/docs/caching#query-string-include)  
Include HTTP Headers | [cdnPolicy.cacheKeyPolicy.includeHttpHeaders[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_31) | [HTTP headers and HTTP cookies cache key settings](https://docs.cloud.google.com/cdn/docs/caching#http-headers-cookies)  
Include Named Cookies | [cdnPolicy.cacheKeyPolicy.includeNamedCookies[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_32) | [Including named cookies](https://docs.cloud.google.com/cdn/docs/caching#including-named-cookies)  
**Outlier Detection** | Base Ejection Time Seconds | [outlierDetection.baseEjectionTime.seconds](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_76) | [Outlier detection for serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#outlier-detection)  
Base Ejection Time Nanos | [outlierDetection.baseEjectionTime.nanos](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_77) | [Outlier detection for serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#outlier-detection)  
Consecutive Errors | [outlierDetection.consecutiveErrors](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_79) | [Outlier detection for serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#outlier-detection)  
Consecutive Gateway Failure | [outlierDetection.consecutiveGatewayFailure](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_84) | [Outlier detection for serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#outlier-detection)  
Enforcing Consecutive Errors | [outlierDetection.enforcingConsecutiveErrors](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_79) | [Outlier detection for serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#outlier-detection)  
Enforcing Consecutive Gateway Failure | [outlierDetection.enforcingConsecutiveGatewayFailure](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_84) | [Outlier detection for serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#outlier-detection)  
Enforcing Success Rate | [outlierDetection.enforcingSuccessRate](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_80) | [Outlier detection for serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#outlier-detection)  
Interval Seconds | [outlierDetection.interval.seconds](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_73) | [Outlier detection for serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#outlier-detection)  
Interval Nanos | [outlierDetection.interval.nanos](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_74) | [Outlier detection for serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#outlier-detection)  
Max Ejection Percent | [outlierDetection.maxEjectionPercent](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_78) | [Outlier detection for serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#outlier-detection)  
Success Rate Minimum Hosts | [outlierDetection.successRateMinimumHosts](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_81) | [Outlier detection for serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#outlier-detection)  
Success Rate Request Volume | [outlierDetection.successRateRequestVolume](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_82) | [Outlier detection for serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#outlier-detection)  
Success Rate Stdev Factor | [outlierDetection.successRateStdevFactor](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.inlinedField_83) | [Outlier detection for serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#outlier-detection)  
**Health Check** | Host | [http2HealthCheck.host](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks#HealthCheck.FIELDS.inlinedField_29) | [Additional flags for HTTP, HTTPS, and HTTP/2 health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#optional-flags-hc-protocol-http)  
Request Path | [http2HealthCheck.requestPath](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks#HealthCheck.FIELDS.inlinedField_30) | [Success criteria for HTTP, HTTPS, and HTTP/2](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-http)  
Request | [sslHealthCheck.request](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks#HealthCheck.FIELDS.inlinedField_9) | [Success criteria for SSL and TCP](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-ssl-tcp)  
Response | [sslHealthCheck.response](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks#HealthCheck.FIELDS.inlinedField_10) | [Additional flags for HTTP, HTTPS, and HTTP/2 health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#optional-flags-hc-protocol-http)  
Port | [http2HealthCheck.port](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks#HealthCheck.FIELDS.inlinedField_26) | [Health check categories, protocols, and ports](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#categories_protocols_ports)  
Port Name | [http2HealthCheck.portName](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks#HealthCheck.FIELDS.inlinedField_27) | [Named ports](https://docs.cloud.google.com/load-balancing/docs/backend-service#named-ports)  
Proxy Header | [http2HealthCheck.proxyHeader](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks#HealthCheck.FIELDS.inlinedField_31) | [Headers](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#headers)  
Port Specification | [http2HealthCheck.portSpecification](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks#HealthCheck.FIELDS.inlinedField_28) | [Port specification flags](https://docs.cloud.google.com/load-balancing/docs/health-checks#hc-port-flags)  
Protocol | [type](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks#HealthCheck.FIELDS.type) | [Health check categories, protocols, and ports](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#categories_protocols_ports)  
Check Interval Sec | [checkIntervalSec](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks#HealthCheck.FIELDS.check_interval_sec) | [Probes](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#probes)  
Timeout Sec | [timeoutSec](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks#HealthCheck.FIELDS.timeout_sec) | [Probes](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#probes)  
Healthy Threshold | [healthyThreshold](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks#HealthCheck.FIELDS.healthy_threshold) | [Health state](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#health_state)  
Unhealthy Threshold | [unhealthyThreshold](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks#HealthCheck.FIELDS.unhealthy_threshold) | [Health state](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#health_state)  
Logging | [logConfig.enable](https://docs.cloud.google.com/compute/docs/reference/rest/v1/healthChecks#HealthCheck.FIELDS.inlinedField_37) | [Health check logging information](https://docs.cloud.google.com/load-balancing/docs/health-check-logging)  
| Edge Security Policy | [edge_security_policy](https://github.com/terraform-google-modules/terraform-google-lb-http/tree/main/modules/backend#inputs) | [Edge security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#edge-policies)  
| Security Policy | [security_policy](https://github.com/terraform-google-modules/terraform-google-lb-http/tree/main/modules/backend#inputs) | [Security policy overview](https://docs.cloud.google.com/armor/docs/security-policy-overview)  
| Firewall Networks | [network](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls#Firewall.FIELDS.network) | [Configure firewall rules](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#configure_firewall_rules)  
| Firewall Projects | Names of the projects to create firewall rules in. | [Configure firewall rules](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#configure_firewall_rules)  
| Target Tags | [targetTags[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls#Firewall.FIELDS.target_tag) | [Restrict which clients can send traffic to the load balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#restrict__clients)  
| Target Service Accounts | [targetServiceAccounts[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls#Firewall.FIELDS.target_service_account) | [Source and target filtering by service account](https://docs.cloud.google.com/firewall/docs/firewalls#serviceaccounts)  
  
## What's next

Connect your backend component to a frontend component. To configure the frontend component, see [Configure a global Cloud Load Balancing frontend in Application Design Center](https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-global-frontend).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
