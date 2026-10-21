---
url: https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-regional-backend/
title: Configure a regional Cloud Load Balancing backend service \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:26:09.303560+00:00
---

# Configure a regional Cloud Load Balancing backend service  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-regional-backend/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a regional Cloud Load Balancing backend service Stay organized with collections  Save and categorize content based on your preferences. 

You create a load balancer in your application by configuring and connecting distinct Cloud Load Balancing frontend and backend components. The separate components help you apply distinct controls for external and internal traffic, and prevent direct access to data.

The regional Cloud Load Balancing backend component helps you manage load balancer traffic distribution settings, including the protocol used to connect to backends, session settings, health checks, and timeouts. These settings provide fine-grained control over how your load balancer behaves. You can configure the following backends:

  * Serverless NEG: A list of serverless Cloud Run or Cloud Run functions applications as backends.

  * Managed Instance Group (MIG): A list of Compute Engine instance groups as backends.




For more information, see [Backend services overview](https://docs.cloud.google.com/load-balancing/docs/backend-service).

This document describes the connections and parameters you can configure when using App Design Center to create a regional Cloud Load Balancing backend service. The configuration parameters are based on the [terraform-google-regional-lb-http](https://github.com/GoogleCloudPlatform/terraform-google-regional-lb-http/tree/main/modules/backend) Terraform module.

## Component connections

To create a complete Cloud Load Balancing component, you must connect your regional Cloud Load Balancing backend to at least one regional Cloud Load Balancing frontend. Connected Cloud Load Balancing components are displayed as a group in the design canvas.

The following table includes the components that you can connect to a regional Cloud Load Balancing backend, and the resulting updates to your application and its generated Terraform code.

Connected component | Application updates | Background information  
---|---|---  
[Cloud Run](https://docs.cloud.google.com/application-design-center/docs/configure-cloud-run) | 

  * The load balancer can distribute incoming traffic to the Cloud Run service.
  * The Cloud Run service is added as a backend endpoint in the Cloud Load Balancing serverless NEG backends configuration.

| [Set up a regional external Application Load Balancer with Cloud Run](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-serverless)  
[Regional Cloud Load Balancing frontend](https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-regional-frontend) (required) | 

  * The Cloud Load Balancing frontend, which handles incoming requests, is linked to the Cloud Load Balancing backend, which processes the requests.
  * The backend service information is added to the frontend URL map input.

| [URL maps overview](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts)  
[Compute Engine MIG](https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-mig) | 

  * The load balancer can distribute incoming traffic to the Compute Engine MIG.
  * The Compute Engine MIG is added to the Cloud Load Balancing backend service groups field.

| [Set up a regional external Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb)  
  
## Required configuration parameters

If your template includes a regional Cloud Load Balancing backend component, you must configure the following parameters before you deploy.

Parameter name | Description and constraints | Background information  
---|---|---  
**Project ID** | The project where you want to deploy the Cloud Load Balancing backend service. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
**Region** | The region where the load balancer backend service is created. | [region](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices)  
**Name** | Name for the load balancer backend service. | [name](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.name)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Parameter name | Description and constraint information | Background information  
---|---|---|---  
Host Path Mappings | **Host** | [Configure URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map#configure_url_maps) | [URL maps overview](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts)  
**Path** | [Configure URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map#configure_url_maps) | [URL maps overview](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts)  
| **Load Balancing Scheme** | [loadBalancingScheme](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.load_balancing_scheme) | [Backend services overview](https://docs.cloud.google.com/load-balancing/docs/backend-service)  
Serverless NEG backends | **Region** | [region](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionNetworkEndpointGroups#NetworkEndpointGroup.FIELDS.region) | [Serverless network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts)  
**Type** | [networkEndpointType](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionNetworkEndpointGroups#NetworkEndpointGroup.FIELDS.network_endpoint_type) | [Serverless network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts)  
**Service Name** | [appEngine.service](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionNetworkEndpointGroups#NetworkEndpointGroup.FIELDS.inlinedField_3) | [Serverless network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts)  
**Service Version** | [appEngine.version](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionNetworkEndpointGroups#NetworkEndpointGroup.FIELDS.inlinedField_4) | [Serverless network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts)  
**Capacity Scaler** | [backends[].capacityScaler](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.inlinedField_10) | [Capacity Scaler](https://docs.cloud.google.com/load-balancing/docs/backend-service#capacity_scaler)  
Groups | **Group** | [backends[].group](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.inlinedField_1) | [Backends](https://docs.cloud.google.com/load-balancing/docs/backend-service#backends)  
**Description** | A description for the backends group. | [backends[].description](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.inlinedField)  
**Balancing Mode** | [backends[].balancingMode](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.inlinedField_2) | [Balancing modes and target capacity settings](https://docs.cloud.google.com/load-balancing/docs/backend-service#traffic_distribution)  
**Capacity Scaler** | [backends[].capacityScaler](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.inlinedField_10) | [Capacity scaler](https://docs.cloud.google.com/load-balancing/docs/backend-service#capacity_scaler)  
**Max Connections** | [backends[].maxConnections](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.inlinedField_7) | [Connection balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#connection_balancing_mode)  
**Max Connections Per Instance** | [backends[].maxConnectionsPerInstance](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.inlinedField_8) | [Connection balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#connection_balancing_mode)  
**Max Connections Per Endpoint** | [backends[].maxConnectionsPerEndpoint](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.inlinedField_9) | [Connection balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#connection_balancing_mode)  
**Max Rate** | [backends[].maxRate](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.inlinedField_4) | [Rate balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#rate_balancing_mode)  
**Max Rate Per Instance** | [backends[].maxRatePerInstance](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.inlinedField_5) | [Rate balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#rate_balancing_mode)  
**Max Rate Per Endpoint** | [backends[].maxRatePerEndpoint](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.inlinedField_6) | [Rate balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#rate_balancing_mode)  
**Max Utilization** | [backends[].maxUtilization](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.inlinedField_3) | [Utilization balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#utilization_balancing_mode)  
| **Protocol** | [protocol](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.service_protocol) | [Protocol to the backends](https://docs.cloud.google.com/load-balancing/docs/backend-service#protocol_to_the_backends)  
| **Port Name** | [portName](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.port_name) | [Named ports](https://docs.cloud.google.com/load-balancing/docs/backend-service#named-ports)  
| **Description** | A description for the backend service. | [description](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.description)  
Health Check | **Host** | [http2HealthCheck.host](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.inlinedField_29) | [Additional flags for HTTP, HTTPS, and HTTP/2 health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#optional-flags-hc-protocol-http)  
**Request Path** | [http2HealthCheck.requestPath](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.inlinedField_30) | [Success criteria for HTTP, HTTPS, and HTTP/2](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-http)  
**Request** | [sslHealthCheck.request](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.inlinedField_9) | [Success criteria for SSL and TCP](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-ssl-tcp)  
**Response** | [sslHealthCheck.response](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.inlinedField_10) | [Additional flags for HTTP, HTTPS, and HTTP/2 health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#optional-flags-hc-protocol-http)  
**Port** | [http2HealthCheck.port](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.inlinedField_26) | [Health check categories, protocols, and ports](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#categories_protocols_ports)  
**Port Name** | [http2HealthCheck.portName](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.inlinedField_27) | [Named ports](https://docs.cloud.google.com/load-balancing/docs/backend-service#named-ports)  
**Proxy Header** | [http2HealthCheck.proxyHeader](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.inlinedField_31) | [Headers](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#headers)  
**Port Specification** | [http2HealthCheck.portSpecification](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.inlinedField_28) | [Port specification flags](https://docs.cloud.google.com/load-balancing/docs/health-checks#hc-port-flags)  
**Protocol** | The protocol that Google Cloud uses to probe the backends. For example, `http2`. | [Health check categories, protocols, and ports](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#categories_protocols_ports)  
**Check Interval Sec** | [checkIntervalSec](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.check_interval_sec) | [Probes](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#probes)  
**Timeout Sec** | [timeoutSec](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.timeout_sec) | [Probes](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#probes)  
**Healthy Threshold** | [healthyThreshold](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.healthy_threshold) | [Health state](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#health_state)  
**Unhealthy Threshold** | [unhealthyThreshold](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.unhealthy_threshold) | [Health state](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#health_state)  
**Logging** | [logConfig.enable](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.inlinedField_37) | [Health check logging information](https://docs.cloud.google.com/load-balancing/docs/health-check-logging)  
| **Firewall Networks** | [network](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls#Firewall.FIELDS.network) | [Configure firewall rules](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#configure_firewall_rules)  
| **Firewall Projects** | Names of the projects to create firewall rules in. | [Configure firewall rules](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#configure_firewall_rules)  
| **Target Tags** | [targetTags[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls#Firewall.FIELDS.target_tag) | [Restrict which clients can send traffic to the load balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#restrict__clients)  
| **Target Service Accounts** | [targetServiceAccounts[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls#Firewall.FIELDS.target_service_account) | [Source and target filtering by service account](https://docs.cloud.google.com/firewall/docs/firewalls#serviceaccounts)  
| **Firewall Source Ranges** | [sourceRanges[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/firewalls#Firewall.FIELDS.source_range) | [Configure firewall rules](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#configure_firewall_rules)  
| **Connection Draining Timeout Sec** | [connectionDraining.drainingTimeoutSec](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.inlinedField_20) | [Enable connection draining](https://docs.cloud.google.com/load-balancing/docs/enabling-connection-draining)  
| **Enable CDN** | [enableCDN](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.enable_cdn) | [Cloud CDN overview](https://docs.cloud.google.com/cdn/docs/overview)  
| **Session Affinity** | [sessionAffinity](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.session_affinity) | [Session affinity](https://docs.cloud.google.com/load-balancing/docs/backend-service#session_affinity)  
| **Affinity Cookie TTL Sec** | [affinityCookieTtlSec](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.affinity_cookie_ttl_sec) | [Generated cookie affinity](https://docs.cloud.google.com/load-balancing/docs/backend-service#generated_cookie_affinity)  
| **Locality LB Policy** | [localityLbPolicy](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.locality_lb_policy) | [Load balancing locality policy](https://docs.cloud.google.com/load-balancing/docs/backend-service#lb-locality-policy)  
| **Security Policy** | [securityPolicy](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.security_policy) | [Google Cloud Armor](https://docs.cloud.google.com/load-balancing/docs/backend-service#armor-support)  
| **Timeout Sec** | [timeoutSec](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionBackendServices#BackendService.FIELDS.timeout_sec) | [Backend service timeout](https://docs.cloud.google.com/load-balancing/docs/backend-service#timeout-setting)  
  
## What's next

You must connect your backend component to a frontend component. To configure the frontend component, see [Configure a regional Cloud Load Balancing frontend in Application Design Center](https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-regional-frontend).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
