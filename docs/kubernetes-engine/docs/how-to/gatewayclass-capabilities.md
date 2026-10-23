---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities/
title: GatewayClass capabilities \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:05.802598+00:00
---

# GatewayClass capabilities  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/gatewayclass-capabilities/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  GatewayClass capabilities Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page lists the capabilities of the [GatewayClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#gateway_resources) resources available on Google Kubernetes Engine (GKE) and their supported specifications.

#### Table legend

For the various tables on this page, the legend for the tables is as follows:

  * indicates that the field is supported.
  * `-` indicates that the field is not supported.
  * If GKE supports some values in the field, the table describes what values are supported.



## GatewayClass capabilities

The following table lists the distinguishing features of the GatewayClass resources available on GKE.

### Architecture

Feature | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
GKE Gateway Controller | Google-hosted Gateway controller  
Location | Google Cloud infrastructure  
Platform | GKE  
[Cluster type](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters) | GKE Autopilot or GKE Standard  
Cluster scope | Single cluster | Multi-cluster | Single cluster | Multi-cluster | Single cluster | Multi-cluster | Single cluster | Multi-cluster  
Gateway API versions | **New clusters and cluster upgrades:**  
GKE 1.35.2-gke.1842000 or later: **1.5.0**  
GKE 1.34.1-gke.1822000 or later: **1.4.0**  
GKE 1.33.2-gke.1335000 or later: **1.3.0**  
GKE 1.32.2-gke.1475000 or later: **1.2.0**  
GKE 1.30.2-gke.1783000 or later: **1.1.0**  
API enablement | GKE Autopilot: enabled by default  
[Launch stage](https://cloud.google.com/products#product-launch-stages) | GA  
  
### Multi-cluster Services

Feature | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
Required |  |  |  |  |  |  |  |  |   
API version |  | `net.gke.io/v1` |  | `net.gke.io/v1` | `net.gke.io/v1` |  | `net.gke.io/v1` |  | `net.gke.io/v1`  
Resource type |  | ServiceExport |  | ServiceExport | ServiceExport |  | ServiceExport |  | ServiceExport  
  
### Load balancer

**Feature** | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
Type | [Global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) | [Regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) | [Internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) | [Classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https)  
[Load balancer scope](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview#global_versus_regional_load_balancing) | Global | Regional | Regional | Regional | Global  
Container-native load balancing |  (Default, using `GCE_VM_IP_PORT` [zonal NEGs](https://docs.cloud.google.com/load-balancing/docs/negs#zonal-neg))  
  
### VPC

Feature | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
[Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) support | All clusters and fleet host project in the same Shared VPC host or service project  
Shared Gateway/Ingress for multiple routes |  |  |  |  |  |  |  |  |   
Automated VPC firewall lifecycle management |  |  |  |  |  |  |  |  |   
**Note:** You must deploy firewall rules manually for Gateways in a Shared VPC environment.  
For more information, see required [firewall rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#gateway-fws) for Gateways.  
  
### Gateway IP address

Feature | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
Gateway IP address assignment | Static or dynamic  
[Network Service tier](https://docs.cloud.google.com/network-tiers/docs/overview) IP address | Premium Tier |  Standard Tier or Premium Tier  | Standard Tier or Premium Tier  | Premium Tier | Premium Tier  
Gateway IP address reachability | Internet | Internet | VPC internal | Internet  
Same IP address for multiple ports (HTTP, HTTPS) |   
  
### Routing and traffic management

Feature | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
[Global Access](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_global_access) | Implicit for Global load balancers | Implicit for Global load balancers |  |  |  | Implicit for Global load balancers  
Cross-region backend load balancing |  |  |  |  |  |  |  |  |   
Cross-project load balancing | Backend services and NEGs must be in the same project  
(Managed by the GKE Gateway controller)  
Cross-namespace routing |  |  |  |  |  |  |  |  |   
Host/Path routing | Prefix or exact match | Prefix, exact match or [regular expression](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#regex-matching) | Prefix or exact match  
Header-based routing | Exact match | Exact match or [regular expression](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#regex-matching) | Exact match  
[Path redirects](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#configure_path_redirects) |  |  |  |  |  |  |  |  |   
[URL rewrites](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#configure_url_rewrites) |  |  |  |  |  |  |  |  |   
[CORS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#configure-cors) |  |  |  |  |  |  |  |  |   
[Traffic splitting](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/traffic-management#splitting) |  |  |  |  |  |  |  |  |   
[Traffic mirroring](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways#traffic-mirror) |  |  |  |  |  |  |  |  |   
[Traffic cut over](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways#cut-over) |  |  |  |  |  |  |  |  |   
[Traffic-based autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/horizontal-pod-autoscaling#autoscale-traffic) |  |  |  |  |  |  |  |  |   
[Custom request headers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#configure_custom_request_headers) |  |  |  |  |  |  |  |  |   
[Custom response headers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#configure_custom_response_headers) |  |  |  |  |  |  |  |  |   
[GCPRoutingExtension](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gke-service-extensions#configure-gcproutingextension) | Not supported | Not supported |  |  |  |  |  | Not supported | Not supported  
[GCPTrafficExtension](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gke-service-extensions#configure-the-gateways) |  |  |  |  |  |  |  | Not supported | Not supported  
[GCPWasmPlugin](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gke-service-extensions#gcp-extensions-plugin) | Preview | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported | Not supported  
[GCPAuthzExtension](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gke-service-extensions#configure-gcp-authz-ext) |  | Not supported |  | Not supported | Not supported |  | Not supported | Not supported | Not supported  
  
### Frontend security

Feature | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
[SSL policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_ssl_policies) |  |  |  |  |  |  |  |  |   
[HTTP-to-HTTPS redirect](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#configure_http-to-https_redirects) |  |  |  |  |  |  |  |  |   
Multiple TLS certificates support |  |  |  |  |  |  |  |  |   
Frontend mTLS |  |  |  |  |  |  |  |  |   
**Backend mTLS** |  |  |  |  |  |  |  |  |   
[Kubernetes Secrets-based certificates](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-secret) |  |  |  |  |  |  |  |  |   
[Self-managed Compute Engine SSL certificates](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-secret) |  |  |  |  |  |  |  |  |   
[Google-managed Compute Engine SSL certificates](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-ssl-certificate) |  |  |  |  |  |  |  |  |   
[Self-managed SSL certificates with Certificate Manager](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-certificate-manager) |  |  |  |  |  |  |  |  |   
[Google-managed SSL certificates with Certificate Manager](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#secure-using-certificate-manager) |  |  |   
|   
|   
|   
|   
|  |   
[Authorization policies (GCPAuthzPolicy)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#auth-policy) |  |  |  |  |  |  |  |  |   
  
### Backend service properties

Feature | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
[Connection draining timeout](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_connection_draining) |  |  |  |  |  |  |  |  |   
[Session affinity (GCPTrafficDistributionPolicy)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#expanded-session-affinity) |  |  |  |  |  |  |  |  |   
[Session affinity (GCPBackendPolicy)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#session-affinity-backend-policy) |  |  |  |  |  |  |  |  |   
[Stable Load Balancing (Ring Hash Size)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure-endpoint-routing) |  |  |  |  |  |  |  |  |   
[HTTP access logging configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_http_access_logging) |  |  |  |  |  |  |  |  |   
[Backend service timeout](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_timeout) |  |  |  |  |  |  |  |  |   
[Custom load balancer health check configuration](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_health_check) |  |  |  |  |  |  |  |  |   
[Backend TLS](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#configure-backend-tls) |  |  |  |  |  |  |  |  |   
[Supported backend services protocols](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#load-balancer-tls) | HTTP, HTTPS, HTTP/2  
[Custom default backend](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways#configure_the_gateway_default_backend) |  |  |  |  |  |  |  |  |   
  
### Additional Google Cloud services

Features | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
[Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_iap) |  |  |  |  |  |  |  |  |   
[Google Cloud Armor backend security policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_cloud_armor) |  |  |  |  |  |  |  |  |   
[Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview) |  |  |  |  |  |  |  |  |   
[GCPRoutingExtension Support](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gke-service-extensions#configure-gcproutingextension) |  |  |  |  |  |  |  |  |   
[GCPTrafficExtension Support](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gke-service-extensions#configure-the-gateways) |  |  |  |  |  |  |  |  |   
[GCPWasmPlugin Support](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gke-service-extensions#gcp-extensions-plugin) |  |  |  |  |  |  |  |  |   
[GCPAuthzPolicy Support](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway#auth-policy) |  |  |  |  |  |  |  |  |   
[GCPAuthzExtension Support](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gke-service-extensions#configure-gcp-authz-ext) |  |  |  |  |  |  |  |  |   
  
## Supported Gateway API Fields

The following tables list the fields of the [Gateway API specification](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io%2fv1beta1.Gateway) that are supported by GKE.

### Gateway

#### `spec.addresses`

For more information, see [`spec.addresses`](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1beta1.GatewaySpecAddress) in the Gateway documentation.

Fields | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
`type` | `NamedAddress`  
`value` | Static global external address | Static regional external address | Static regional internal address | Static global external address  
  
#### `spec.listeners`

For more information, see [`spec.listeners`](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1beta1.Listener) in the Gateway documentation.

Fields | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
`protocol` | HTTP, HTTPS  
`port` | 1-65535  
`name` |  |  |  |  |  |  |  |  |   
`hostname` |  |  |  |  |  |  |  |  |   
`tls` |  |  |  |  |  |  |  |  |   
`allowedRoutes` |  |  |  |  |  |  |  |  |   
  
#### `spec.listeners.tls`

For more information, see [`spec.listeners.tls`](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1beta1.ListenerTLSConfig) in the Gateway documentation.

Fields | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
`mode` | `Terminate`  
`certificateRefs` |  |  |  |  |  |  |  |  |   
  
#### `spec.listeners.tls.options`

For more information, see [`spec.listeners.tls.options`](https://gateway-api.sigs.k8s.io/reference/spec/#gateway.networking.k8s.io%2fv1.GatewayTLSConfig) in the Gateway documentation.

Fields | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
`networking.gke.io/pre-shared-certs` | [Global SSL certificate resource reference (self- or Google-managed)](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#ssl_certificate_scope) | [Regional, self-managed SSL certificate resource reference](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#ssl_certificate_scope) |  | [Regional, self-managed SSL certificate resource reference](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#ssl_certificate_scope) | [Global SSL certificate resource reference (self- or Google-managed)](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#ssl_certificate_scope)  
  
### GCPTrafficExtension

The following tables list the values of the `GCPTrafficExtension` API specification that are supported by GKE.

#### `spec.targetRefs`

For more information, see [`spec.targetRefs`](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1beta1.TargetRef) in the Gateway documentation.

Fields | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
`group` | `gateway.networking.k8s.io`  
`kind` | `Gateway`  
`name` |  |  |  |  |  |  |  |  |   
  
#### `spec.extensionChains.extensions.BackendRef`

For more information, see [`spec.extensionChains.extensions.BackendRef`](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1beta1.BackendRef) in the Gateway documentation.

Fields | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
`group` | `(empty)`  
`kind` | `Service, GCPWasmPlugin` | `ServiceImport` | `Service` | `ServiceImport` | `ServiceImport` | `Service` | `ServiceImport` |  |   
`name` |  |  |  |  |  |  |  |  |   
`port` |  |  |  |  |  |  |  |  |   
  
#### `spec.extensionChains.extensions.googleAPIServiceName`

Fields | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
`googleAPIServiceName` |  |  |  |  |  |  |  |  |   
  
### GCPRoutingExtension

The following tables list the values of the `GCPRoutingExtension` API specification that are supported by GKE.

#### `spec.targetRefs`

For more information, see [`spec.targetRefs`](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1beta1.TargetRef) in the Gateway documentation.

Fields | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
`group` | `gateway.networking.k8s.io`  
`kind` | `Gateway`  
`name` |  |  |  |  |  |  |  |  |   
  
#### `spec.extensionChains.extensions.BackendRef`

For more information, see [`spec.extensionChains.extensions.BackendRef`](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1beta1.BackendRef) in the Gateway documentation.

Fields | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
`group` | `(empty)`  
`kind` |  |  | `Service` | `ServiceImport` | `ServiceImport` | `Service` | `ServiceImport` |  |   
`name` |  |  |  |  |  |  |  |  |   
`port` |  |  |  |  |  |  |  |  |   
  
### GCPAuthzPolicy

The following tables list the values of the GCPAuthzPolicy API specification that are supported by GKE.

#### `spec.targetRefs`

Fields | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
`group` | `gateway.networking.k8s.io`  
`kind` | `Gateway`  
`name` |  |  |  |  |  |  |  |  |   
  
#### `spec.action`

Fields | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
`ALLOW` |  |  |  |  |  |  |  |  |   
`DENY` |  |  |  |  |  |  |  |  |   
`CUSTOM` |  |  |  |  |  |  |  |  |   
  
### GCPAuthzExtension

The following tables list the values of the GCPAuthzExtension API specification that are supported by GKE.

#### `spec.backendRef`

Fields | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
`group` | `(empty)`  
`kind` | `Service` |  | `Service` |  |  | `Service` |  |  |   
`name` |  |  |  |  |  |  |  |  |   
  
#### `spec.googleAPIServiceName`

Fields | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
`googleAPIServiceName` |  |  |  |  |  |  |  |  |   
  
### HTTPRoute

The following tables list the values of the [HTTPRoute API specification](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1beta1.HTTPRoute) that are supported by GKE.

#### `spec.parentRefs`

For more information, see [`spec.parentRefs`](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1beta1.ParentReference) in the Gateway documentation.

Fields | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
`parentRefs.group` |  |  |  |  |  |  |  |  |   
`parentRefs.kind` |  |  |  |  |  |  |  |  |   
`parentRefs.namespace` |  |  |  |  |  |  |  |  |   
`parentRefs.name` |  |  |  |  |  |  |  |  |   
`parentRefs.sectionName` |  |  |  |  |  |  |  |  |   
`parentRefs.port` |  |  |  |  |  |  |  |  |   
  
#### `spec.hostnames`

For more information, see [`spec.hostnames`](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1beta1.Hostname) in the Gateway documentation.

Fields | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
`precise, wildcard` |  |  |  |  |  |  |  |  |   
  
#### `spec.rules`

For more information, see [`spec.rules`](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1beta1.HTTPRouteMatch) in the Gateway documentation.

Fields | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
`path.type` | `Exact, PathPrefix` | `Exact, PathPrefix, RegularExpression` | `Exact, PathPrefix`  
`path.value` |  |  |  |  |  |  |  |  |   
`headers.type` | `Exact` | `Exact, RegularExpression` | `Exact`  
`headers.name` |  |  |  |  |  |  |  |  |   
`headers.value` |  |  |  |  |  |  |  |  |   
`queryParams` |  |  |  |  |  |  |  |  |   
`method` |  |  |  |  |  |  |  |  |   
  
#### `spec.rules.backendRefs`

For more information, see [`spec.rules.backendRefs`](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1beta1.HTTPBackendRef) in the Gateway documentation.

Fields | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
`backendRef.group` | `(empty), gateway.networking.k8s.io, net.gke.io`  
`backendRef.kind` | `Service` | `ServiceImport` | `Service` | `ServiceImport` | `Service` | `ServiceImport` | `Service` | `ServiceImport`  
`backendRef.name` |  |  |  |  |  |  |  |  |   
`backendRef.namespace` |  |  |  |  |  |  |  |  |   
`backendRef.port` |  |  |  |  |  |  |  |  |   
`backendRef.weight` |  |  |  |  |  |  |  |  |   
`backendRef.filters` |  |  |  |  |  |  |  |  |   
  
#### `spec.rules.filters`

For more information, see [`spec.rules.filters`](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1beta1.HTTPRouteFilter) in the Gateway documentation.

Fields | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
`type` | `cors, requestHeaderModifier, responseHeaderModifier, requestMirror, requestRedirect, urlRewrite` | `requestHeaderModifier, responseHeaderModifier, requestMirror, requestRedirect, urlRewrite` | `cors, requestHeaderModifier, responseHeaderModifier, requestMirror, requestRedirect, urlRewrite` | `requestHeaderModifier, responseHeaderModifier, requestMirror, requestRedirect, urlRewrite` | `cors, requestHeaderModifier, responseHeaderModifier, requestMirror, requestRedirect, urlRewrite` | `requestHeaderModifier, responseHeaderModifier, requestMirror, requestRedirect, urlRewrite` |  |   
`cors.allowOrigins` |  |  |  |  |  |  |  |  |   
`cors.allowMethods` |  |  |  |  |  |  |  |  |   
`cors.allowHeaders` |  |  |  |  |  |  |  |  |   
`cors.exposeHeaders` |  |  |  |  |  |  |  |  |   
`cors.allowCredentials` |  |  |  |  |  |  |  |  |   
`cors.maxAge` |  |  |  |  |  |  |  |  |   
`requestHeaderModifier.add` |  |  |  |  |  |  |  |  |   
`requestHeaderModifier.remove` |  |  |  |  |  |  |  |  |   
`requestHeaderModifier.set` |  |  |  |  |  |  |  |  |   
`responseHeaderModifier.add` |  |  |  |  |  |  |  |  |   
`responseHeaderModifier.remove` |  |  |  |  |  |  |  |  |   
`responseHeaderModifier.set` |  |  |  |  |  |  |  |  |   
`requestMirror.backendRef` |  |  |  |  |  |  |  |  |   
`requestRedirect.scheme` | `HTTP, HTTPS` |  |   
`requestRedirect.hostname` |  |  |  |  |  |  |  |  |   
`requestRedirect.path` | `replaceFullPath, replacePrefixMatch` |  |   
`requestRedirect.port` |  |  |  |  |  |  |  |  |   
`requestRedirect.statusCode` |  |  |  |  |  |  |  |  |   
`urlRewrite.hostname` |  |  |  |  |  |  |  |  |   
`urlRewrite.path` | `replacePrefixMatch` |  |   
  
### ReferenceGrant

The following tables list the values of the [ReferenceGrant API specification](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1beta1.ReferenceGrant) that are supported by GKE.

#### `spec.from`

For more information, see [`spec.from`](https://gateway-api.sigs.k8s.io/reference/spec/#gateway.networking.k8s.io/v1beta1.ReferenceGrantFrom) in the Gateway documentation.

Fields | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
`group` | `(empty), gateway.networking.k8s.io, net.gke.io`  
`kind` | `Gateway, HTTPRoute`  
`namespace` |  |  |  |  |  |  |  |  |   
  
#### `spec.to`

For more information, see [`spec.to`](https://gateway-api.sigs.k8s.io/reference/spec/#gateway.networking.k8s.io/v1beta1.ReferenceGrantTo) in the Gateway documentation.

Fields | `gke-l7-global-external-managed` | `gke-l7-global-external-managed-mc` | `gke-l7-regional-external-managed` | `gke-l7-regional-external-managed-mc` | `gke-l7-cross-regional-internal-managed-mc` | `gke-l7-rilb` | `gke-l7-rilb-mc` | `gke-l7-gxlb` | `gke-l7-gxlb-mc`  
---|---|---|---|---|---|---|---|---|---  
`group` | `(empty), gateway.networking.k8s.io, net.gke.io`  
`kind` | `Secret, Service, ServiceImport`  
`name` |  |  |  |  |  |  |  |  |   
  
## What's next

  * Learn how to [deploy Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways).
  * Learn more about the [Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).
  * Learn how to [configure Gateway resources using Policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources).
  * Learn how to [secure Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/secure-gateway).
  * Learn more about [traffic management](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/traffic-management).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
