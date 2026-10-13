---
url: https://docs.cloud.google.com/service-mesh/v1.28/docs/supported-features-in-cluster/
title: In-cluster control plane supported features \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:30:55.583426+00:00
---

# In-cluster control plane supported features  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.28/docs/supported-features-in-cluster/

You are viewing v1.28 Service Mesh documentation.

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
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.28/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.28/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# In-cluster control plane supported features

**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/v1.28/docs/supported-platforms#off-gcp). 

This page describes features that are supported in Cloud Service Mesh 1.28.10 with an in-cluster control plane. To see the supported features for Cloud Service Mesh 1.28.10 with a managed control plane instead, see [Managed control plane](https://docs.cloud.google.com/service-mesh/v1.28/docs/supported-features-managed).

## Supported versions

Support for Cloud Service Mesh follows the [GKE Enterprise Version Support Policy](https://docs.cloud.google.com/anthos/docs/support/getting-support#version_support_policy).

For **managed Cloud Service Mesh with a`TRAFFIC_DIRECTOR` control plane implementation**, Google always supports this control plane.

For **managed Cloud Service Mesh with an`ISTIOD` control plane implementation** ([deprecated](https://docs.cloud.google.com/service-mesh/deprecations)), Google supports the current Cloud Service Mesh versions available in each [release channel](https://docs.cloud.google.com/service-mesh/v1.28/legacy/anthos-service-mesh/v1.28/managed-anthos-service-mesh/v1.28/select-a-release-channel#anthos_service_mesh_versions_per_channel).

For **self-installed in-cluster Cloud Service Mesh** , Google supports the current and previous two (n-2) minor versions of Cloud Service Mesh.

**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/v1.28/docs/supported-platforms#off-gcp). 

The following table shows the supported versions of **self-installed in-cluster Cloud Service Mesh** and the earliest end-of-life (EOL) date for a version.

Release version | Release date | Earliest end of life date  
---|---|---  
1.28 | [January 19, 2026](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#January_19_2026) | October 19, 2026  
1.27 | [September 23, 2025](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#September_23_2025) | June 23, 2026  
1.26 | [July 16, 2025](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#July_16_2025) | April 16, 2026  
  
If you are on an unsupported version of Cloud Service Mesh, then you must upgrade to Cloud Service Mesh 1.26 or later. For information on how to upgrade, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade).

The following table shows the unsupported versions of Cloud Service Mesh and their end-of-life (EOL) date.

Release version | Release date | End-of-life date  
---|---|---  
1.25 | [April 4, 2025](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#April_04_2025) | Unsupported (January 14, 2026)  
1.24 | [January 16, 2025](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#January_16_2025) | Unsupported (October 15, 2025)  
1.23 | [September 19, 2024](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#September_19_2024) | Unsupported (July 16, 2025)  
1.22 | [July 25, 2024](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#July_25_2024) | Unsupported (May 21, 2025)  
1.21 | [June 4, 2024](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#June_04_2024) | Unsupported (April 16, 2025)  
1.20 | [February 8, 2024](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#February_08_2024) | Unsupported (November 12, 2024)  
1.19 | [October 31, 2023](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#October_31_2023) | Unsupported (July 31, 2024)  
1.18 | [August 3, 2023](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#August_03_2023) | Unsupported (June 4, 2024)  
1.17 | [April 4, 2023](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#April_04_2023) | Unsupported (February 8, 2024)  
1.16 | [February 21, 2023](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#February_21_2023) | Unsupported (December 11, 2023)  
1.15 | [October 25, 2022](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#October_25_2022) | Unsupported (August 4, 2023)  
1.14 | [July 20, 2022](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#July_20_2022) | Unsupported (April 20, 2023)  
1.13 | [March 30, 2022](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#March_30_2022) | Unsupported (February 8, 2023)  
1.12 | [December 9, 2021](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#December_09_2021) | Unsupported (October 25, 2022)  
1.11 | [October 6, 2021](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#October_06_2021) | Unsupported (July 20, 2022)  
1.10 | [June 24, 2021](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#June_24_2021) | Unsupported (March 30, 2022)  
1.9 | [March 4, 2021](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#March_04_2021) | Unsupported (December 14, 2021)  
1.8 | [December 15, 2020](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#December_15_2020) | Unsupported (December 14, 2021)  
1.7 | [November 3, 2020](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#November_03_2020) | Unsupported (December 14, 2021)  
1.6 | [June 30, 2020](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#June_30_2020) | Unsupported (March 30, 2021)  
1.5 | [May 20, 2020](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#May_20_2020) | Unsupported (February 17, 2021)  
1.4 | [December 20, 2019](https://docs.cloud.google.com/service-mesh/v1.28/docs/release-notes#December_20_2019) | Unsupported (September 18, 2020)  
  
For more information about our support policies, refer to [Getting support](https://docs.cloud.google.com/service-mesh/v1.28/docs/getting-support#version_support_policy).

## Platform differences

There are differences in supported features between [supported platforms](https://docs.cloud.google.com/service-mesh/v1.28/docs/supported-platforms).

The **Other GKE Enterprise clusters** columns refer to clusters that are outside of Google Cloud, for example:

  * Google Distributed Cloud:

    * Google Distributed Cloud (software only) for VMware
    * Google Distributed Cloud (software only) for bare metal

This page uses Google Distributed Cloud where the same support is available on both Google Distributed Cloud (software only) for VMware and Google Distributed Cloud (software only) for bare metal, and the specific platform where there are differences between the platforms.

  * GKE Enterprise on other public clouds:

    * [GKE on AWS](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/aws)
    * [GKE on Azure](https://docs.cloud.google.com/anthos/clusters/docs/multi-cloud/azure)
  * GKE attached clusters - Third-party Kubernetes clusters that have been registered to a fleet. Cloud Service Mesh is supported on the following cluster types:

    * Amazon EKS clusters
    * Microsoft AKS clusters 



In the following tables:

  * – indicates the feature is enabled by default.
  * * – indicates the feature is supported for the platform and can be enabled, as described in [Enabling optional features](https://docs.cloud.google.com/service-mesh/v1.28/docs/enable-optional-features-in-cluster) or the feature guide linked in the feature table.
  * **Compatible** – indicates the feature or third-party tool will integrate or work with Cloud Service Mesh, but is not fully supported by Google Cloud Support and a feature guide is not available.
  * – indicates either the feature isn't available or it isn't supported in Cloud Service Mesh 1.28.10.



The default and optional features are fully supported by Google Cloud Support. Features not explicitly listed in the tables receive best-effort support.

## Base Images

Feature | GKE clusters on Google Cloud (deprecated) | Google Distributed Cloud (software only) for VMware  
---|---|---  
[Distroless proxy image](https://docs.cloud.google.com/service-mesh/v1.28/docs/enable-optional-features-in-cluster#distroless_proxy_image) |  |   
  
## Security

### Certificate distribution/rotation mechanisms

Feature | GKE clusters on Google Cloud (deprecated) | Google Distributed Cloud (software only) for VMware  
---|---|---  
Workload certificate management |  |   
External certificate management on [ ingress](https://istio.io/v1.28/docs/tasks/traffic-management/ingress/secure-ingress/) and [egress](https://istio.io/latest/docs/tasks/traffic-management/egress/egress-gateway-tls-origination/) gateways. |  |   
  
### Certificate authority (CA) support

Feature | GKE clusters on Google Cloud (deprecated) | GKE Enterprise clusters on-premises | Google Distributed Cloud (software only) for VMware  
---|---|---|---  
[Cloud Service Mesh certificate authority](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/kubernetes-off-gcp/install/install-in-cluster-cloud-service-mesh#install_mesh_ca) |  |  |   
[Certificate Authority Service](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/kubernetes-off-gcp/install/install-in-cluster-cloud-service-mesh#install_ca_service) |  * |  * |   
[Istio CA (previously known as Citadel)](https://docs.cloud.google.com/service-mesh/v1.28/docs/onboarding/kubernetes-off-gcp/install/install-in-cluster-cloud-service-mesh#install_istio_ca) |  * |  * |   
Plug in your own CA certificates | Supported by CA service and Istio CA | Supported by CA service and Istio CA | Supported by Istio CA  
  
### Cloud Service Mesh security features

In addition to supporting Istio security features, Cloud Service Mesh provides even more capabilities to help you secure your applications.

Feature | GKE clusters on Google Cloud (deprecated) | Distributed Cloud | GKE Multi-Cloud | Google Distributed Cloud (software only) for VMware  
---|---|---|---|---  
[IAP integration](https://docs.cloud.google.com/service-mesh/v1.28/docs/security/iap-integration) |  |  |  |   
[End-user authentication](https://docs.cloud.google.com/service-mesh/v1.28/docs/security/end-user-auth) |  |  |  |   
[Audit policies (preview)](https://docs.cloud.google.com/service-mesh/v1.28/docs/tutorials/audit-authz) |  |  |  * |   
[Dry-run mode](https://docs.cloud.google.com/service-mesh/v1.28/docs/security/authorization-advanced-features#dry-run_mode) |  |  |  |   
[Denial logging](https://docs.cloud.google.com/service-mesh/v1.28/docs/security/authorization-advanced-features#denial_logging) |  |  |  |   
  
### Authorization policy

Feature | GKE clusters on Google Cloud (deprecated) | Google Distributed Cloud (software only) for VMware  
---|---|---  
Authorization v1beta1 policy |  |   
[Path templating](https://istio.io/latest/news/releases/1.22.x/announcing-1.22/change-notes/#:~:text=Added%20support%20for%20path%20templating) |  |   
  
### Authentication policy

#### Peer authentication

Feature | GKE clusters on Google Cloud (deprecated) | Google Distributed Cloud (software only) for VMware  
---|---|---  
Auto-mTLS |  |   
mTLS PERMISSIVE mode |  |   
  
For information on enabling mTLS STRICT mode, see [Configuring transport security](https://docs.cloud.google.com/service-mesh/v1.28/docs/security/configuring-mtls).

#### Request authentication

Feature | GKE clusters on Google Cloud (deprecated) | Google Distributed Cloud (software only) for VMware  
---|---|---  
JWT authentication (Note 1) |  |   
  
**Notes:**

  1. Third-party JWT is enabled by default. 



## Telemetry

### Metrics

Feature | GKE clusters on Google Cloud (deprecated) | GKE Enterprise clusters on-premises | Google Distributed Cloud (software only) for VMware  
---|---|---|---  
Cloud Monitoring (HTTP in-proxy metrics) |  |  |   
Cloud Monitoring (TCP in-proxy metrics) |  |  |   
[Istio Telemetry API](https://preliminary.istio.io/latest/docs/tasks/observability/telemetry/) |  |  |   
Custom adapters/backends, in or out of process |  |  |   
Arbitrary telemetry and logging backends |  |  |   
[Prometheus metrics export](https://docs.cloud.google.com/service-mesh/v1.28/docs/third-party-integrations#enabling_metrics_export_to_prometheus) to customer-installed Prometheus, Grafana, and Kiali dashboards | Compatible | Compatible | Compatible  
Google Cloud Managed Service for Prometheus, not including the Cloud Service Mesh dashboard |  |  |   
The topology graph in the Google Cloud console no longer uses the Mesh telemetry service as its data source. Although the data source for the topology graph has changed, the UI remains the same.   
  
### Proxy request logging

Feature | GKE clusters on Google Cloud (deprecated) | GKE Enterprise clusters on-premises | Google Distributed Cloud (software only) for VMware  
---|---|---|---  
[Traffic logs](https://docs.cloud.google.com/service-mesh/v1.28/docs/observability/access-logs#traffic-logs_2) |  |  |   
[Access logs](https://docs.cloud.google.com/service-mesh/v1.28/docs/observability/access-logs#envoy-access-logs_2) |  * |  * |  *  
  
### Tracing

Feature | GKE clusters on Google Cloud (deprecated) | GKE Enterprise clusters on-premises | Google Distributed Cloud (software only) for VMware  
---|---|---|---  
Cloud Trace |  * |  * |   
Jaeger tracing (allows use of customer-managed Jaeger) | Compatible | Compatible | Compatible  
Zipkin tracing (allows use of customer-managed Zipkin) | Compatible | Compatible | Compatible  
**Note:** You can configure third-party telemetry products (such as Jaeger, Zipkin, and Grafana), but we cannot guarantee future compatibility and Cloud Support cannot provide help managing them.

## Networking

### Destination rule

Feature | GKE clusters on Google Cloud (deprecated) | Google Distributed Cloud (software only) for VMware  
---|---|---  
[credentialName](https://istio.io/latest/docs/reference/config/networking/destination-rule/#ClientTLSSettings:~:text=No-,credentialName,-string) |  |   
  
### Traffic interception/redirection mechanism

Feature | GKE clusters on Google Cloud (deprecated) | Google Distributed Cloud (software only) for VMware  
---|---|---  
Traditional use of `iptables` using `init` containers with `CAP_NET_ADMIN` |  |   
Container Network Interface (CNI) |  * |  *  
  
### Protocol support

Services that are configured with Layer 7 capabilities for the following protocols are not supported: WebSocket, MongoDB, Redis, Kafka, Cassandra, RabbitMQ, Cloud SQL. You might be able to make the protocol work by using TCP byte stream support. If TCP byte stream cannot support the protocol (for example, Kafka sends a redirect address in a protocol-specific reply and this redirect is incompatible with Cloud Service Mesh's routing logic), then the protocol isn't supported.

Feature | GKE clusters on Google Cloud (deprecated) | Google Distributed Cloud (software only) for VMware  
---|---|---  
IPv4 |  |   
HTTP/1.1 |  |   
HTTP/2 |  |   
TCP byte streams (Note 1) |  |   
[gRPC](https://grpc.io) |  |   
IPv6 |  |   
Istio DualStack |  |   
  
**Notes:**

  1. Although TCP is a supported protocol for networking, TCP metrics aren't collected or reported. Metrics are displayed only for HTTP services in the Google Cloud console. 



### Envoy deployments

Feature | GKE clusters on Google Cloud (deprecated) | Google Distributed Cloud (software only) for VMware  
---|---|---  
Sidecars |  |   
Ingress gateway |  |   
Egress directly out from sidecars |  |   
Egress using egress gateways |  * |  *  
  
The `sidecar.istio.io/bootstrapOverride` annotation for custom Envoy configurations is not supported.

### CRD support

Feature | GKE clusters on Google Cloud (deprecated) | Google Distributed Cloud (software only) for VMware  
---|---|---  
Istio API support (exceptions below) |  |   
[custom Envoy filters](https://istio.io/docs/reference/config/networking/v1alpha3/envoy-filter/) |  |   
  
### Load balancer for the Istio ingress gateway

Feature | GKE clusters on Google Cloud (deprecated) | Google Distributed Cloud (software only) for VMware  
---|---|---  
Third-party external load balancer |  |   
Google Cloud Internal load balancer |  * | Not supported. See the links below.  
  
For information on configuring load balancers, see the following:

  * [Setting up your load balancer for Google Distributed Cloud (software only) for VMware](https://docs.cloud.google.com/anthos/gke/docs/on-prem/how-to/setup-load-balance)
  * GKE on AWS: [Creating a load balancer](https://cloud.google.com/anthos/gke/docs/aws/how-to/loadbalancer)
  * [Expose an ingress gateway using an external load balancer](https://docs.cloud.google.com/service-mesh/v1.28/docs/operate-and-maintain/external-lb-gateway)



### Kubernetes Gateway API (preview)

In Cloud Service Mesh v1.20 the Kubernetes Gateway API is available as a public preview.

Feature | GKE clusters on Google Cloud (deprecated) | Google Distributed Cloud (software only) for VMware  
---|---|---  
Ingress |  |   
Gateway with `class: istio` |  |   
HttpRoute using `parentRef` |  |   
Mesh traffic |  |   
Configuring Istio CRDs using the `targetRef` field  
including AuthorizationPolicy, RequestAuthentication, Telemetry and WasmPlugin  |  |   
**Warning:** Microsoft AKS attached and GKE on Azure clusters require an additional step to use the Kubernetes Gateway API.

If you are using Microsoft AKS attached clusters or GKE on Azure clusters, you must set the following annotation for the gateway resource to configure health checks over TCP:
    
    
      service.beta.kubernetes.io/port_80_health-probe_protocol: tcp
    

Otherwise, HTTP traffic won't be accepted.

#### Kubernetes Gateway API preview requirements

The Kubernetes Gateway API preview has the following requirements:

  * Use the default automated deployments behavior for Gateways.

  * Use the `HttpRoute` CRD for routing configurations. The `HttpRoute` must have a `parentRef` pointing to a Gateway.

  * Don't use [Istio Gateway](https://istio.io/latest/docs/reference/config/networking/gateway/#Gateway) CRs and [Kubernetes Gateway API](https://gateway-api.sigs.k8s.io/reference/spec/#gateway.networking.k8s.io/v1.Gateway) CRs on the same cluster.




### Load balancing policies

Feature | GKE clusters on Google Cloud (deprecated) | Google Distributed Cloud (software only) for VMware  
---|---|---  
Round robin |  |   
Least connections |  |   
Random |  |   
Passthrough |  |   
Consistent hash |  |   
Locality |  |   
  
For more information on load balancing policies, see [Destination Rules](https://istio.io/latest/docs/concepts/traffic-management/#destination-rules).

### Data plane

Feature | GKE clusters on Google Cloud (deprecated) | Google Distributed Cloud (software only) for VMware  
---|---|---  
Sidecar |  |   
Ambient |  |   
  
## Multi-cluster support

For multi-primary deployments of GKE clusters in different projects, all the clusters must be in a [shared Virtual Private Cloud](https://docs.cloud.google.com/vpc/docs/shared-vpc) (VPC).

### Network

Feature | GKE clusters on Google Cloud (deprecated) | GKE Enterprise clusters on-premises | GKE on AWS | GKE on Azure | Attached clusters  
---|---|---|---|---|---  
Single network |  |  |  |  |   
Multi-network |  |  |  |  |   
  
**Notes:**

  * For attached clusters, only multi-cluster meshes spanning a single platform (Microsoft AKS, Amazon EKS) are supported at this time. 



### Deployment model

Feature | GKE clusters on Google Cloud (deprecated) | GKE Enterprise clusters on-premises | GKE Enterprise on other public clouds | Attached clusters  
---|---|---|---|---  
Multi-primary |  |  |  |   
Primary-remote |  |  |  |   
  
**Notes on terminology:**

  * A primary cluster is a cluster with a control plane. A single mesh can have more than one primary cluster for high availability or to reduce latency. In the Istio 1.7 documentation, a multi-primary deployment is referred to as a replicated control plane.

  * A remote cluster is a cluster that connects to a control plane residing outside of the cluster. A remote cluster can connect to a control plane running in a primary cluster or to an external control plane.

  * Cloud Service Mesh uses a simplified definition of network based on general connectivity. Workload instances are on the same network if they are able to communicate directly, without a gateway.




## User interface

Feature | GKE clusters on Google Cloud (deprecated) | Google Distributed Cloud | Google Distributed Cloud (software only) for VMware  
---|---|---|---  
Cloud Service Mesh dashboards in the Google Cloud console |  | * |  *  
Cloud Monitoring |  |  |  *  
Cloud Logging |  |  |  *  
Cloud Trace |  |  |  *  
  
**Note:** On-premises clusters require GKE Enterprise version 1.11 or later. For more information on upgrading see [Upgrading Google Distributed Cloud (software only) for VMware](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/upgrading) or [Upgrading Google Distributed Cloud (software only) for bare metal](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/how-to/upgrade).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
