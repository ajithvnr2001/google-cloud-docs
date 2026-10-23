---
url: https://docs.cloud.google.com/service-mesh/v1.21/docs/service-routing/features/
title: Cloud Service Mesh with Google Cloud APIs supported features \u00a0|\u00a0 Cloud Service Mesh v1.21 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:30:43.681541+00:00
---

# Cloud Service Mesh with Google Cloud APIs supported features  |  Cloud Service Mesh v1.21  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.21/docs/service-routing/features/

You are viewing archived v1.21 Service Mesh documentation.

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
  * [ v1.21 ](https://docs.cloud.google.com/service-mesh/v1.21/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.21/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud Service Mesh with Google Cloud APIs supported features

This document summarizes the features available in Cloud Service Mesh.

**Note:** This guide only supports Cloud Service Mesh with Google Cloud APIs and does not support Istio APIs. For more information see, [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview).

A Cloud Service Mesh consists of your applications, an xDS-compatible data plane (the [open source Envoy proxy](https://www.envoyproxy.io/) or gRPC proxyless data plane), and Cloud Service Mesh as your control plane.

In the following tables, the value _N/A (not applicable)_ means that a feature cannot be supported because it is not compatible with the particular Cloud Service Mesh configuration. A blank space, without either a check mark or N/A, means that the feature is not supported.

Some of these features are available only with the load balancing APIs. We strongly recommend that you use the [service routing APIs](https://docs.cloud.google.com/service-mesh/v1.21/docs/service-routing/service-routing-overview) and that you don't create new deployments using the load balancing APIs.

## Supported xDS version

Cloud Service Mesh uses open source xDS control plane APIs to configure Envoy and proxyless gRPC clients. These clients act on behalf of your application code to deliver Cloud Service Mesh's application networking capabilities.

Only xDS v3 is supported. Migrate to xDS v3 if you are using xDS v2. For information about how to migrate, see [Migrate from xDS v2 to xDS v3](https://docs.cloud.google.com/service-mesh/v1.21/docs/service-routing/xds-control-plane-apis#migrate_from_xds_v2_to_xds_v3).

## Platforms to run mesh services

You can run applications on the following platforms and adopt them into a global service mesh that Cloud Service Mesh configures.

Feature | Supported  
---|---  
Compute Engine virtual machine (VM) instances | ✔  
Google Kubernetes Engine (GKE) container instances | ✔  
Kubernetes on Compute Engine container instances | ✔  
  
## Services management

Services in a mesh that Cloud Service Mesh configures benefit from the following:

  * **Service discovery.** When an application in your mesh wants to reach another application, it can call on that service by name.

  * **Backend autoscaling.** Instances that run your application code scale up or down dynamically based on your needs.

  * **Automatic endpoint registration.** As new instances are created or removed, they are automatically associated with your service.


Feature | Supported  
---|---  
Automated deployment of sidecar proxies for Compute Engine VMs | ✔  
Automated injection of sidecar proxies for GKE Pods | ✔  
Service discovery based on hostname | ✔  
Instance autoscaling based on CPU utilization | ✔  
Instance autoscaling based on traffic load/serving capacity  
(Compute Engine VMs in managed instance groups, or MIGs, only) | ✔  
Instance autohealing based on configurable health checks | ✔  
Automatic endpoint registration for Compute Engine VMs | ✔  
Automatic endpoint registration for GKE container instances/Pods | ✔  
API to programmatically add or remove endpoints | ✔  
  
## Endpoints for your data plane traffic

Microservices use the data plane to reach services in your mesh and outside of your mesh. Cloud Service Mesh lets you separate application logic from networking logic so that your application only needs to send requests to the data plane (for example, the sidecar proxy running alongside the application). The data plane then sends requests to the correct endpoint.

In the following table, applications described as being in the mesh are those applications that use the Cloud Service Mesh-managed data plane to communicate with other services. Those applications can send traffic to in-mesh services and services outside of the mesh.

Feature | Supported  
---|---  
VM-based applications in the mesh | ✔  
Container-based applications in the mesh | ✔  
VM-based applications outside of the mesh | ✔  
Container-based applications outside of the mesh | ✔  
Applications running in on-premises data centers | ✔  
Applications in multicloud environments | ✔  
  
## Data plane topologies

In the service mesh model, your applications use a data plane to communicate. This data plane often consists of sidecar proxies deployed alongside your applications. Cloud Service Mesh is highly flexible and supports data plane topologies that fit your service networking needs.

Feature | Supported  
---|---  
Sidecar proxies running alongside applications | ✔  
Proxyless gRPC applications | ✔  
Middle proxies between two applications in a mesh | ✔  
Edge proxies at the boundary of your mesh | ✔  
Mesh spanning multiple GKE clusters and/or Compute Engine VMs in multiple regions | ✔  
  
## Programmatic, API-driven configuration

All configuration is exposed through our REST API and dashboard out-of-the-box, letting you automate changes across large teams and manage changes programmatically. Some features cannot be configured by using the Google Cloud console.

Feature | Supported  
---|---  
REST APIs | ✔  
Google Cloud console | ✔  
Google Cloud CLI | ✔  
Cloud Deployment Manager | ✔  
Terraform support | ✔  
  
## Language support with proxyless gRPC applications

You can create proxyless gRPC applications that work with Cloud Service Mesh using the following programming languages. The service mesh features supported in various implementations and versions of gRPC are listed on [GitHub](https://github.com/grpc/grpc/blob/master/doc/grpc_xds_features.md).

Language | Supported  
---|---  
[Java](https://github.com/grpc/grpc-java) | ✔  
[Go](https://github.com/grpc/grpc-go) | ✔  
[C++](https://github.com/grpc/grpc) | ✔  
[Python](https://github.com/grpc/grpc) | ✔  
[Ruby](https://github.com/grpc/grpc) | ✔  
[PHP](https://github.com/grpc/grpc) | ✔  
[Node](https://github.com/grpc/grpc-node) | ✔  
  
## Request protocols

Applications can use the following request protocols when they use the Cloud Service Mesh-configured data plane to communicate.

Feature | Supported  
---|---  
HTTP | ✔  
HTTPS | ✔  
HTTP/2 | ✔  
TCP | ✔  
gRPC | ✔  
  
## Service security

Cloud Service Mesh supports service security with the following configurations.

Feature | Envoy | gRPC  
---|---|---  
TLS with GKE Pods | ✔ | ✔  
mTLS with GKE Pods | ✔ | ✔  
Access control and authorization | ✔ | ✔  
  
## Routing and traffic management

Cloud Service Mesh supports advanced traffic management policies that you can use to steer, split, and shape traffic as it passes through your data plane.

Some advanced traffic management features are not available with proxyless gRPC services, and none of the advanced traffic management features are available with the target TCP proxy resource.

The following features are not supported when Cloud Service Mesh handles TCP (non-HTTP(S)) traffic.

Feature | Supported with Envoy proxy configured to handle HTTP(S) or gRPC traffic | Supported with proxyless gRPC  
---|---|---  
HTTP/Layer 7 request routing based on suffix/prefix/full/regex match on: |  |   
• Hostname | ✔ | ✔  
• Path | ✔ | ✔  
• Headers | ✔ | ✔  
• Method | ✔ | N/A  
• Cookies | ✔ | ✔  
• Request parameters | ✔ | N/A  
Fault injection | ✔ | ✔  
Configurable timeouts | ✔ | N/A  
See _Max stream duration_.  
Retries | ✔ | ✔  
Except _per retry timeout_  
Redirects | ✔ |   
URI rewrites | ✔ |   
Request/response header transformations | ✔ |   
Traffic splitting | ✔ | ✔  
Traffic mirroring | ✔ |   
Outlier detection | ✔ | ✔  
Circuit breaking | ✔ | ✔  
Only _maxRequests_  
Max stream duration | ✔ | ✔  
  
## Load balancing

You can configure advanced load-balancing methods and algorithms to load balance at the service, backend group (instance groups or network endpoint groups), and individual backend or endpoint levels. For more information, see the [Backend services overview](https://docs.cloud.google.com/load-balancing/docs/backend-service) and [Advanced load balancing overview](https://docs.cloud.google.com/service-mesh/v1.21/docs/service-routing/advanced-load-balancing-overview).

Feature | Supported with Envoy proxy configured to handle HTTP(s), TCP, or gRPC traffic | Supported with proxyless gRPC  
---|---|---  
Backend (instance group or network endpoint group) selection based on region (prefer nearest region with healthy backend capacity) | ✔ | ✔  
Backend selection using rate-based (requests per second) balancing mode. | ✔  
Not supported with TCP (non-HTTP(S)) traffic. | ✔  
Backend selection based on utilization-based balancing mode (VMs in Compute Engine instance groups only) | ✔ | ✔  
Configurable maximum capacity per backend (Compute Engine and GKE only) | ✔ | ✔  
Backend selection based on configurable load-balancing policies. For information about each built-in policy, see [`localityLbPolicy`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices).  | 

  * Use a [single built-in policy](https://docs.cloud.google.com/service-mesh/v1.21/docs/service-routing/advanced-traffic-management#locality-load-balancing); choose from the following options:
    * Round robin
    * Least request
    * Ring hash
    * Random
    * Original destination
    * Maglev

| 

  * Use a [single built-in policy](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management#localityLbPolicy); choose from the following options:
    * Round robin
    * Least request
    * Ring hash
  * Use a [custom policy](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management#custom-lb-config)
  * Define a [list of preferred policies](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management#policy-list)

  
  
## Service resiliency

Cloud Service Mesh supports capabilities that help you improve the resiliency of your services. For example, you can use Cloud Service Mesh to implement a blue-green deployment pattern, canary testing, or circuit breaking ([Envoy](https://docs.cloud.google.com/service-mesh/v1.21/docs/service-routing/advanced-traffic-management#circuit-breaking), [gRPC](https://docs.cloud.google.com/service-mesh/legacy/load-balancing-apis/proxyless-configure-advanced-traffic-management#circuit-breaking)).

Feature | Supported with Envoy proxy configured to handle HTTP(s), TCP, or gRPC traffic | Supported with proxyless gRPC  
---|---|---  
Service selection based on weight-based traffic splits | ✔ | ✔  
Circuit breaking | ✔ | ✔  
Only _maxRequests_  
  
## Service and backend capacity management

Cloud Service Mesh takes service and backend capacity into account to ensure optimal distribution of traffic across your services' backends. Cloud Service Mesh is integrated with the Google Cloud infrastructure so that it automatically collects capacity data. You can also set and configure capacity manually.

Feature | Supported  
---|---  
Automatically tracks backend capacity and utilization, based on CPU, for VM instances in a managed instance group (MIG). | ✔  
Manual capacity and overrides for VM and container instances in MIGs and network endpoint groups (NEGs) based on request rate. | ✔  
Manual capacity draining. | ✔  
  
## Failover

Enterprise workloads generally rely on high-availability deployments to ensure service uptime. Cloud Service Mesh supports these types of deployments by enabling multi-zone/multi-region redundancy.

Feature | Supported  
---|---  
Automatic failover to another zone within the same region that has healthy backend capacity. | ✔  
Automatic failover to nearest region with healthy backend capacity. | ✔  
  
## Health checks

Cloud Service Mesh supports centralized health checking to determine backend health.

For reference information, see the [Health checks overview](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts).

Feature | Supported  
---|---  
gRPC health checks | ✔  
HTTP health checks | ✔  
HTTPS health checks | ✔  
HTTP/2 health checks | ✔  
TCP health checks | ✔  
Configurable health checks:

  * Port
  * Check intervals
  * Timeouts
  * Healthy and unhealthy thresholds

| ✔  
Configurable request path (HTTP, HTTPS, HTTP/2) | ✔  
Configurable request string or path (TCP or SSL) | ✔  
Configurable expected response string | ✔  
  
## Observability

Observability tools provide monitoring, debugging, and performance information to help you understand your service mesh. The following capabilities are either provided by default or configured in your data plane. Your application code doesn't need to do anything special to generate this observability data.

The service health dashboard is available with proxyless gRPC services, but you cannot configure data plane logging and tracing. Cloud Service Mesh cannot configure a gRPC application's logging and tracing. You can enable logging and tracing by following the instructions in the troubleshooting sections or gRPC guides available on open source sites. For example, to enable metrics collection and tracing in your proxyless gRPC services, you can use [Opencensus](https://opencensus.io/).

Feature | Supported with proxies | Supported with proxyless gRPC services  
---|---|---  
Service health dashboard | ✔ | ✔  
Data plane logging | ✔ | ✔  
Data plane tracing | ✔ | ✔  
  
## Session affinity

Client-server communications often involve multiple successive requests. In such a case, it's helpful to route successive client requests to the same backend or server. Cloud Service Mesh provides configurable options to send requests from a particular client, on a best effort basis, to the same backend as long as the backend is healthy and has capacity. For more information, see the [Backend services overview](https://docs.cloud.google.com/load-balancing/docs/backend-service).

Feature | Supported with HTTP(S) proxies | Supported with TCP proxies | Supported with proxyless gRPC services  
---|---|---|---  
Client IP address | ✔ | ✔ |   
HTTP cookie | ✔ | N/A |   
HTTP header | ✔ | N/A | ✔  
Generated cookie (sets client cookie on first request) | ✔ | N/A |   
  
## Network topologies

Cloud Service Mesh supports common Google Cloud network topologies.

Feature | Supported  
---|---  
Single network in a Google Cloud project | ✔  
Multiple meshes in a Google Cloud project | ✔  
Multiple gateways in a Google Cloud project | ✔  
Shared VPC (single network shared across multiple Google Cloud projects) | ✔  
  
For a detailed explanation of how Shared VPC is supported with Cloud Service Mesh, see [Limitations](https://docs.cloud.google.com/service-mesh/v1.21/docs/service-routing/limitations).

## Compliance

Cloud Service Mesh is compliant with the following standards.

Compliance certification | Supported  
---|---  
HIPAA | ✔  
ISO 27001, ISO 27017, ISO 27018 | ✔  
SOC1, SOC2, SOC3 | ✔  
PCI DSS | ✔  
  
## What's next

  * To learn more about Cloud Service Mesh, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.21/docs/overview).
  * To find uses cases and architecture patterns for proxyless gRPC services, see the [Proxyless gRPC services overview](https://docs.cloud.google.com/service-mesh/v1.21/docs/service-routing/proxyless-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
