---
url: https://docs.cloud.google.com/service-mesh/docs/understand-api-resources/
title: Understand Cloud Service Mesh API Resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:30:47.497358+00:00
---

# Understand Cloud Service Mesh API Resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/understand-api-resources/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Understand Cloud Service Mesh API Resources

**Note:** This guide only supports Cloud Service Mesh with Istio APIs and does not support Google Cloud APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

When you use Gateway API and Istio API to configure your service mesh on GKE, the KRM-based API resources you managed on GKE will be automatically translated to a set of Google Cloud API resources:

  * They don't incur any additional billing to you.
  * They are managed exclusively by the managed Cloud Service Mesh infrastructure(based on the API resources you create in your GKE clusters). You won't be able to modify or delete these Google Cloud API resources. Changes to the KRM API would trigger update or removal of the corresponding Google Cloud API resources. And the Google Cloud API resources will be automatically removed when you deprovision your Cloud Service Mesh service mesh.
  * They are functionally equivalent to the API resources you managed on GKE. The Cloud Service Mesh infrastructure programs the dataplane in your GKE clusters based on these Google Cloud API resources.
  * They are subjected to the standard Google Cloud [API quota control](https://docs.cloud.google.com/docs/quotas/view-manage). You can view the current [quota usage](https://console.cloud.google.com/iam-admin/quotas) in your Google Cloud project. Config propagation to the dataplane will be stalled when Google Cloud resource quota is exceeded. Note that Google Cloud enforces resource quota at project level and these Google Cloud API resources share quota with the same type of Google Cloud API resource managed by yourself.



The following is a high-level overview of how API resources on GKE are mapped to Google Cloud API resources. In most cases, understanding the API mapping is not a requirement to use your service mesh on GKE, as you will be managing your service mesh on GKE using Gateway API or Istio API. On the other hand, having a high level understanding of the API mapping helps you plan and manage your Google Cloud API quota more efficiently as your service mesh scales.

## Understand API resources

The API resources you manage on GKE will be mapped to a set of Google Cloud API resources that control different aspects of the behaviors of the traffic in the dataplane. We recommend that you set up [quota alerts](https://docs.cloud.google.com/docs/quotas/set-up-quota-alerts) for these resources.

### Istio API with Managed Cloud Service Mesh

Item | Istio API Resources | Google Cloud API Resources | Scope | Quotas and Limits | Upper Bound  
---|---|---|---|---|---  
Traffic routing | [VirtualService](https://istio.io/latest/docs/reference/config/networking/virtual-service/) |  [HTTPRoute](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.httpRoutes)  
[TCPRoute](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.tcpRoutes)  
[TLSRoute](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.tlsRoutes) | Global |  [HTTPRoute Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&&metric=networkservices.googleapis.com/httproutes)  
[TCPRoute Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&&metric=networkservices.googleapis.com/tcproutes)  
[TLSRoute Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&&metric=networkservices.googleapis.com/tlsroutes) | 1 per service port, and for each of Istio VirtualService HTTPRoute, TCPRoute, and TLSRoute.  
Service representation(for route / policy attachment) |  [Service](https://kubernetes.io/docs/concepts/services-networking/service/)  
[ServiceEntry](https://istio.io/latest/docs/reference/config/networking/service-entry/) |  [BackendService](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services) | Global |  [BackendService Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/global_internal_traffic_director_backend_services) | 1 per service port (include Istio ServiceEntry).  
Workload properties(such as IP:port, locality) |  [Service](https://kubernetes.io/docs/concepts/services-networking/service/)  
[ServiceEntry](https://istio.io/latest/docs/reference/config/networking/service-entry/) |  [NetworkEndpointGroup](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups) | Zonal |  [NetworkEndpointGroup Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/network_endpoint_groups) | 1 per (service port, zone). In a regional GKE cluster, a NetworkEndpointGroup is created in every single zone where the cluster has at least a node in, for a given service port.  
Workload health monitoring |  [Service](https://kubernetes.io/docs/concepts/services-networking/service/) |  [HealthCheck](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks) | Global |  [HealthCheck Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/health_checks) | 1 per GKE cluster.  
Workload policy attachment point |  [PeerAuthentication](https://istio.io/latest/docs/reference/config/security/peer_authentication/)  
[AuthorizationPolicy](https://istio.io/latest/docs/reference/config/security/authorization-policy/)  
[RequestAuthentication](https://istio.io/latest/docs/reference/config/security/request_authentication/) [EnvoyFilter](https://istio.io/latest/docs/reference/config/networking/envoy-filter/) |  [EndpointPolicy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-services/endpoint-policies) | Global |  [EndpointPolicy Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&&metric=networkservices.googleapis.com/endpointpolicies) | 1 per service port and for each of the workload policies.  
Authentication |  [PeerAuthentication](https://istio.io/latest/docs/reference/config/security/peer_authentication/) |  [ClientTlsPolicy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/client-tls-policies)  
[ServerTlsPolicy](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-security/server-tls-policies) | Global |  [ClientTlsPolicy Quota](https://console.cloud.google.com/iam-admin/quotas?service=networksecurity.googleapis.com&&metric=networksecurity.googleapis.com/clienttlspolicies)  
[ServerTlsPolicy Quota](https://console.cloud.google.com/iam-admin/quotas?service=networksecurity.googleapis.com&&metric=networksecurity.googleapis.com/servertlspolicies) | 1 ClientTlsPolicy per service port. 1 ServerTlsPolicy for every TLS Gateway.  
Authorization |  [AuthorizationPolicy](https://istio.io/latest/docs/reference/config/security/authorization-policy/) |  [HttpFilter](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/network-services/http-filters) | Global |  [HttpFilter Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&&metric=networkservices.googleapis.com/httpfilters) | 1 per Istio AuthorizationPolicy  
Gateway |  [Gateway](https://istio.io/latest/docs/reference/config/networking/gateway/) |  [Gateway](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.gateways) | Global |  [Gateway Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&&metric=networkservices.googleapis.com/gateways) | 1 per Istio Gateway server port  
Traffic distribution policy |  [GCPTrafficDistributionPolicy](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/advanced-load-balancing-istio#gcptrafficdistributionpolicy) 1 |  [ServiceLbPolicy](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.serviceLbPolicies) | Global |  [ServiceLbPolicy Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&&metric=networkservices.googleapis.com/servicelbpolicies) | 1 per GCPTrafficDistributionPolicy  
  
If your service mesh spans across multiple clusters in different projects, all Google Cloud resources will be created in the fleet project.

1[GCPTrafficDistributionPolicy](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/advanced-load-balancing-istio#gcptrafficdistributionpolicy) is not an Istio API. It enhances the Istio API to provide advanced traffic management.

### Kubernetes Gateway API with Managed Cloud Service Mesh

Item | Kubernetes Gateway API Resources | Google Cloud API Resources | Scope | Quotas and Limits | Upper Bound  
---|---|---|---|---|---  
Traffic routing |  [HTTPRoute](https://gateway-api.sigs.k8s.io/reference/spec/#gateway.networking.k8s.io/v1.HTTPRoute)  
[GRPCRoute](https://gateway-api.sigs.k8s.io/reference/spec/#gateway.networking.k8s.io/v1.GRPCRoute) |  [HTTPRoute](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.httpRoutes)  
[GRPCRoute](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1/projects.locations.grpcRoutes) | Global |  [HTTPRoute Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&&metric=networkservices.googleapis.com/httproutes)  
[GRPCRoute Quota](https://console.cloud.google.com/iam-admin/quotas?service=networkservices.googleapis.com&&metric=networkservices.googleapis.com/grpcroutes)  
| 1 per service port, and for each of HTTPRoute and GRPCRoute.  
Service representation(for route / policy attachment) |  [Service](https://kubernetes.io/docs/concepts/services-networking/service/) |  [BackendService](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services) | Global |  [BackendService Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/global_internal_traffic_director_backend_services) | 1 per service port attached by HTTPRoute and GRPCRoute.  
Workload properties(such as IP:port, locality) |  [Service](https://kubernetes.io/docs/concepts/services-networking/service/) |  [NetworkEndpointGroup](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-endpoint-groups) | Zonal |  [NetworkEndpointGroup Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/network_endpoint_groups) | 1 per (service port, zone). In a regional GKE cluster, a NetworkEndpointGroup is created in every single zone where the cluster has at least a node in, for a given service port.  
Workload health monitoring |  [Service](https://kubernetes.io/docs/concepts/services-networking/service/) |  [HealthCheck](https://docs.cloud.google.com/sdk/gcloud/reference/compute/health-checks) | Global |  [HealthCheck Quota](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/health_checks) | 1 per service port attached by HTTPRoute and GRPCRoute.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
