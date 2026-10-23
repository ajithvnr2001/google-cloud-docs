---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-mc-lb-api/
title: Choose your multi-cluster load balancing API for GKE \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:49.891922+00:00
---

# Choose your multi-cluster load balancing API for GKE  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-mc-lb-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Choose your multi-cluster load balancing API for GKE Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page helps you choose the most suitable API for deploying load balancers to distribute traffic across a fleet of Google Kubernetes Engine (GKE) clusters.

You can attach a load balancer to your fleet of GKE clusters in the following ways:

  1. Use the Multi Cluster Ingress APIs such as the [Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress#multiclusteringress_resource) and [MultiClusterService](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress#multiclusterservice_resources) resources.

  2. Use the Gateway APIs ([GatewayClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#gatewayclass), [Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#gateway), [HTTPRoute](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#httproute), [Policy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#policy), [ServiceExport](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways#mcs), and [ServiceImport](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways#mcs) resources).

  3. Set up the [Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer) using Google Cloud console, gcloud CLI, API, Terraform, Config Connector and attach [Standalone NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg) to the user-managed backend services.




The following table lists the different ways in which you can attach a load balancer to your fleet of GKE clusters. Any features listed in the [Load balancer feature comparison](https://docs.cloud.google.com/load-balancing/docs/features) page that aren't listed in the following table should work with a user-managed load balancer with Standalone NEGs, instead of relying on the Kubernetes-native API for load balancing.

**Solution** | **Multi Cluster Ingress** | **Multi-cluster Gateway** | **User-managed load balancer with Standalone NEGs**  
---|---|---|---  
**GKE platform support** |  |  |   
[Product launch stage](https://cloud.google.com/products#section-22) | GA  | GA  | GA   
[Cluster mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters) | Standard / Autopilot  | Standard / Autopilot  | Standard / Autopilot   
GKE Version  | 1.18 and later  | GKE 1.24 and later for Standard and 1.26 and later for Autopilot  | 1.18 and later   
**Architecture and components** |  |  |   
Google-managed Kubernetes controller  |  |  | close  
Controller  | [GKE Multi Cluster Ingress controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress#architecture) | [GKE Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api#gateway_controller) | \-   
Controller location  | Off-cluster  (Google Cloud infrastructure) | Off-cluster  (Google Cloud infrastructure) | \-   
API  | Kubernetes-native API  | Kubernetes-native API  | Google Cloud API (gcloud CLI)   
API resources  | MultiClusterIngress, MultiClusterService  | GatewayClass, Gateway, HTTPRoute, *Policy  | \-   
API launch stage  | GA (v1)  | GA (v1)  | \-   
API enablement on GKE  | Cluster setting on Autopilot / Standard  | Default on Autopilot Cluster setting on Standard | \-   
**Multi-cluster Services support** |  |  |   
Multi-cluster Services (MCS) required  |  |  |  close  
MCS API version  | [networking.gke.io/v1](http://networking.gke.io/v1) | [net.gke.io/v1](http://net.gke.io/v1) | \-   
Resource type  | MultiClusterService  | ServiceExport  | \-   
License  | Proprietary  | Open source  | \-   
**Cloud Networking resources lifecycle management (excluding Shared VPC)**  
Automated frontend IP address management  |  |  |  close  
Automated Cloud Load Balancer management 

  * Forwarding rule
  * Target proxy
  * URL map
  * Backend services
  * Health checks

|  |  |  close  
Automated Network Endpoint Groups (NEGs) management  |  ([Zonal NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts#gce-vm-ip-port) only) |  ([Zonal NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts#gce-vm-ip-port) only) |  ([Zonal NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts#gce-vm-ip-port) only, annotation required on the Kubernetes Service)  
Cloud NGFW management  |  ([VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) only, [Managed rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#ingress-fws)) |  ([VPC firewall rules](https://docs.cloud.google.com/firewall/docs/firewalls) only, [Managed rules](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/firewall-rules#gateway-fws)) |  close  
**Shared VPC support** |  |  |   
Clusters and fleet (Hub) in the host project  |  |  |   
Clusters and fleet (Hub) in the same service project  |  ([with firewall rules permissions in host project](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#shared_vpc)) |  (with firewall rules permissions in host project) |   
Clusters and fleet (Hub) in different projects  |  close |  close |  (with[ cross-project Service referencing](https://docs.cloud.google.com/load-balancing/docs/https#cross-project))  
**Load balancers support** |  |  |   
[Application load balancers](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer) |  |  |   
Classic  |  |  |   
Global external  |  close |  |   
Regional external  |  close |  |   
Regional internal  |  close |  |   
Cross-region internal  |  close |  close |   
[Proxy Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-network-load-balancer) |  |  |   
Classic  |  close |  close |   
Global external  |  close |  close |   
Regional external  |  close |  close |   
Internal (Always regional)  |  close |  close |   
[Passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/passthrough-network-load-balancer) |  |  |   
External (Always regional)  |  close |  close |  close  
Internal (Always regional)  |  close |  close |  close  
**Client-to-Load-balancer protocols support** |  |  |   
HTTP, HTTPS, HTTP/2  |  |  |   
[WebSocket](https://docs.cloud.google.com/load-balancing/docs/https#websocket-support) |  |  |   
HTTP/3 (based on IETF QUIC)  |  close |  close |   
SSL (TLS) or TCP  |  close |  close |   
**Load Balancer backends support** |  |  |   
Pods (Zonal NEGs)  |  |  |   
Virtual Machines (including GKE nodes)  |  ([Not recommended](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress#container-native_load_balancing)) |  close |   
Other backends: 

  * Cloud Storage
  * Public external endpoints (Internet NEGs)
  * Private external endpoints (Hybrid NEGs)
  * Private Service Connect (PSC NEGs)
  * Cloud Run (Serverless NEGs)

|  close |  close |   
**Load balancer-to-backends protocols support** |  |  |   
HTTP, HTTPS, HTTP/2 (One of)  |  |  |   
[WebSocket](https://docs.cloud.google.com/load-balancing/docs/https#websocket_support) |  |  |   
SSL (TLS) or TCP (One of)  |  close |  close |   
**IP addressing and protocols** |  |  |   
Dynamic IP address assignment  |  |  |   
Static IP address assignment  |  |  |   
Same IP address for multiple ports (HTTP, HTTPS)  |  |  |   
IPv6  |  (Load balancer-to-backend traffic remains IPv4) |  (Load balancer-to-backend traffic remains IPv4) |  (Load balancer-to-backend traffic remains IPv4)  
**Routing and traffic management** |  |  |   
Global access  |  close |  |   
Cross-project load balancing  |  close |  close |   
Host/Path routing  |  (Prefix, Exact match) |  (Prefix, Exact match) |   
Header-based routing  |  close |  (Exact match) |   
Path redirects  |  close |  |   
URL rewrites  |  close |  |   
Traffic splitting  |  close |  |   
Traffic mirroring  |  close |  |   
Traffic cut over  |  close |  |   
Traffic-based autoscaling  |  close |  |   
Custom request headers  |  |  |   
Custom response headers  |  close |  |   
Cross-namespace routing  |  close |  |   
**Frontend Security** |  |  |   
SSL policy  |  |  |   
HTTP-to-HTTPS redirect  |  |  |   
Multiple TLS certificates support  |  |  |   
Kubernetes Secrets-based certificates  |  |  |  close  
Self-managed SSL certificates  |  |  |   
Google-managed SSL certificates  |  |  |   
Certificate Manager support  |  close |  |   
**Backend service properties** |  |  |   
Connection draining timeout  |  |  |   
Session affinity  |  |  |   
HTTP access logging configuration  |  |  |   
Backend service timeout  |  |  |   
Custom load balancer health check configuration  |  [(BackendConfig)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ingress-configuration#configuring_ingress_features_through_backendconfig_parameters) |  [(HealthCheckPolicy)](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-gateway-resources#configure_health_check) |  [(gcloud CLI / Google Cloud console / Terraform)](https://docs.cloud.google.com/load-balancing/docs/health-checks)  
TLS to backend services  |  |  |   
Custom default backend  |  close |  |   
[Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview) |  Not all features: signed cookies, dynamic compression, and private origin authentication are not supported |  Not all features: signed URLs and dynamic compression are not supported |  All features  
[Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview) |  |  |   
[Google Cloud Armor security policy](https://docs.cloud.google.com/armor/docs/security-policy-concepts) |  |  |   
  
## What's next

  * [Set up multi-cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress-setup).
  * [Deploying Ingress across clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/multi-cluster-ingress).
  * [Enable multi-cluster Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enabling-multi-cluster-gateways).
  * [Deploy multi-cluster Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-multi-cluster-gateways).
  * [Container-native load balancing through standalone zonal NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
