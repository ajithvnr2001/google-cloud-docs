---
url: https://docs.cloud.google.com/service-mesh/v1.21/docs/supported-features-managed/
title: Supported features using Istio APIs (managed control plane) \u00a0|\u00a0 Cloud Service Mesh v1.21 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:47.249764+00:00
---

# Supported features using Istio APIs (managed control plane)  |  Cloud Service Mesh v1.21  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.21/docs/supported-features-managed/

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

# Supported features using Istio APIs (managed control plane)

This page describes the supported features and limitations for Cloud Service Mesh using `TRAFFIC_DIRECTOR` or `ISTIOD` as the control plane and the differences between each implementation. Note that these are not options you can choose. The `ISTIOD` implementation is only available for existing users. New installations use the `TRAFFIC_DIRECTOR` implementation when possible.

For the list of Cloud Service Mesh supported features for an in-cluster control plane, see [Using Istio APIs (in-cluster `istiod` control plane)](https://docs.cloud.google.com/service-mesh/v1.21/docs/supported-features-in-cluster). If you're not sure which Cloud Service Mesh control plane you're using, you can check your control plane implementation using the instructions in [Identify control plane implementation](https://docs.cloud.google.com/service-mesh/v1.21/docs/check-control-plane-implementation)

## Limitations

**Caution:** All Cloud Service Mesh clusters for one mesh must be registered to the same fleet at all times to use Cloud Service Mesh. Other clusters in the project of a Cloud Service Mesh cluster must not be registered to a different fleet. 

The following limitations apply:

  * GKE clusters must be in one of the supported regions.
  * GKE version must be a supported version.
  * Only the platforms listed in Environments are supported.
  * Changing [release channels](https://docs.cloud.google.com/service-mesh/docs/managed/select-a-release-channel) is not supported.
  * Migrations from [managed Cloud Service Mesh with `asmcli`](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh-asmcli) to [Cloud Service Mesh with fleet API](https://docs.cloud.google.com/service-mesh/docs/managed/provision-managed-anthos-service-mesh) are not supported. Similarly, provisioning managed Cloud Service Mesh with fleet API from `--management manual` to `--management automatic` is not supported.
  * Migrations and upgrades are supported only from in-cluster Cloud Service Mesh versions 1.9+ installed with Mesh CA. Installations with Istio CA (previously known as Citadel) must first [migrate to Mesh CA](https://docs.cloud.google.com/service-mesh/v1.21/docs/unified-install/options/ca-migration).
  * Scale is limited to 1000 services and 5000 workloads per cluster.
  * Only multi-primary deployment option for multi-cluster is supported: primary-remote deployment option for multi-cluster is not.
  * `istioctl ps` is not supported. Instead you can use the `gcloud beta container fleet mesh debug` commands as described in [Troubleshooting](https://docs.cloud.google.com/service-mesh/v1.21/docs/troubleshooting/troubleshoot-intro).
  * Unsupported APIs:

    * `EnvoyFilter` API

    * `WasmPlugin` API

    * `IstioOperator` API

    * `Kubernetes Ingress` API

**Note:** You can still enable optional features without using the IstioOperator API, see [Enable optional features on managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.21/docs/enable-optional-features). You can also use the migration tool included with `asmcli` to automatically convert other `IstioOperator` optional features to be compatible with managed control plane. For more information, see [Migrate from `IstioOperator`](https://docs.cloud.google.com/service-mesh/v1.21/docs/migrate-istio-operator).
  * You can use the managed control plane without a GKE Enterprise subscription, but certain UI elements and features in Google Cloud console are only available to GKE Enterprise subscribers. For information about what is available to subscribers and non-subscribers, see [GKE Enterprise and Cloud Service Mesh UI differences](https://docs.cloud.google.com/service-mesh/v1.21/docs/ui-differences).

  * During the provisioning process for a managed control plane, Istio CRDs corresponding to the selected channel are installed in the specified cluster. If there are existing Istio CRDs in the cluster, they will be overwritten.

  * Managed Cloud Service Mesh only supports the default DNS domain `.cluster.local`.

  * As of November 14th, 2023, new installations of managed Cloud Service Mesh on the **rapid** release channel fetch JWKS only using Envoys. This is equivalent to the `PILOT_JWT_ENABLE_REMOTE_JWKS=envoy` Istio option. Compared to installations on the **regular** and **stable** release channels, or installations on the **rapid** release channel before November 14th, 2023, you might need extra `ServiceEntry` and `DestinationRule` configurations. For an example, see the [`requestauthn-with-se.yaml.tmpl`](https://github.com/istio/istio/blob/master/tests/integration/security/remote_jwks/testdata/requestauthn-with-se.yaml.tmpl).




## Control plane differences

There are differences in supported features between the `ISTIOD` and `TRAFFIC_DIRECTOR` control plane implementations. To check which implementation you are using, see [Identify control plane implementation](https://docs.cloud.google.com/service-mesh/v1.21/docs/check-control-plane-implementation).

  * – indicates the feature is available and enabled by default.
  * † - indicates that feature APIs may have differences between various platforms.
  * * – indicates the feature is supported for the platform and can be enabled, as described in [Enable optional features](https://docs.cloud.google.com/service-mesh/v1.21/docs/enable-optional-features) or the feature guide linked in the feature table.
  * § – indicates that the feature is supported by allowlist. Previous users of managed Anthos Service Mesh are automatically allowlisted at the [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations) level. [Contact Google Cloud Support](https://docs.cloud.google.com/service-mesh/v1.21/docs/getting-support) to request access or to check your allowlist status.
  * – indicates either the feature isn't available or it isn't supported.



The default and optional features are fully supported by Google Cloud Support. Features not explicitly listed in the tables receive best-effort support.

### What determines control plane implementation

When you provision managed Cloud Service Mesh the first time in a fleet, we determine which control plane implementation to use. The same implementation is used for all clusters that provision managed Cloud Service Mesh in that fleet.

New fleets that onboard to managed Cloud Service Mesh receive the `TRAFFIC_DIRECTOR` control plane implementation, with certain exceptions:

  * If you are an existing managed Cloud Service Mesh user, you receive the `ISTIOD` control plane implementation when you onboard a new fleet in the same Google Cloud Organization to managed Cloud Service Mesh, until at least June 30, 2024. If you are one of these users, you can contact Support to fine-tune this behavior. Users whose existing usage is not compatible with the `TRAFFIC_DIRECTOR` implementation without changes will continue to receive the `ISTIOD` implementation until September 8, 2024. (These users received a Service Announcement.)
  * If any cluster in your fleet uses Certificate Authority Service when you provision managed Cloud Service Mesh, you receive the `ISTIOD` control plane implementation.
  * If any cluster in your fleet contains an in-cluster Cloud Service Mesh control plane when you provision managed Cloud Service Mesh, you will receive the `ISTIOD` control plane implementation.
  * If any cluster in your fleet uses [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods), when you provision managed Cloud Service Mesh, you receive the `ISTIOD` control plane implementation.



## Managed control plane supported features

### Install, upgrade, and rollback

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
Installation on GKE clusters using [fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets) feature API |  |   
Upgrades from ASM 1.9 versions that use Mesh CA |  |   
Direct (skip-level) upgrades from Cloud Service Mesh versions prior to 1.9 (see notes for indirect upgrades) |  |   
Direct (skip-level) upgrades from Istio OSS (see notes for indirect upgrades) |  |   
Direct (skip-level) upgrades from Istio-on-GKE add-on (see notes for indirect upgrades) |  |   
Enabling [optional features](https://docs.cloud.google.com/service-mesh/v1.21/docs/managed-service-mesh-optional-features) |  |   
**Note:** Indirect migrations and upgrades are supported, meaning that you can follow the standard Cloud Service Mesh [upgrade paths](https://docs.cloud.google.com/service-mesh/v1.21/docs/upgrade-path-old-versions-gke) through each version until you reach Cloud Service Mesh 1.21 with an in-cluster control plane, then you can migrate to the managed control plane. Direct migrations and upgrades are supported only from Cloud Service Mesh versions 1.9 or later installed with Mesh CA. Installations with Istio CA must first migrate to Mesh CA.

### Environments

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
GKE 1.25-1.27 in one of the supported regions |  |   
GKE 1.25-1.27 clusters with [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) |  |   
Environments outside of Google Cloud (GKE Enterprise on-premises, GKE Enterprise on other public clouds, Amazon EKS, Microsoft AKS, or other Kubernetes clusters) |  |   
  
### Scale

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
1000 services and 5000 workloads per cluster |  |   
50 [Headless Service Ports](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services) per mesh and 36 pods per Headless ServicePort |  |   
**Note:** This is a soft limit on the number of services and workloads supported per cluster. Reach out to Cloud Support when exceeding this limit.

### Platform environment

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
Single network |  |   
Multi-network |  |   
Single-project |  |   
Multi-project with Shared VPC |  |   
  
### Multi-cluster deployment

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
Multi-primary |  |   
Primary-remote |  |   
Multi-cluster endpoint discovery with [declarative API](https://docs.cloud.google.com/service-mesh/v1.21/docs/unified-install/gke-install-multi-cluster#endpoint-discovery-declarative-api) |  |   
Multi-cluster endpoint discovery with [remote secrets](https://docs.cloud.google.com/service-mesh/v1.21/docs/unified-install/gke-install-multi-cluster#configure_endpoint_discovery_between_public_clusters) |  |   
  
**Notes on terminology**

  * A multi-primary configuration means that the configuration must be replicated in all clusters.
  * A primary-remote configuration means that a single cluster contains the configuration and is considered the source of truth.
  * Cloud Service Mesh uses a simplified definition of network based on general connectivity. Workload instances are on the same network if they are able to communicate directly, without a gateway.



### Base Images

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
[Distroless proxy image](https://docs.cloud.google.com/service-mesh/v1.21/docs/enable-optional-features-managed#distroless_proxy_image) | † |   
  
† Cloud Service Mesh with a managed (TD) control plane only supports the distroless image type. You cannot change it.

Note that distroless images have minimal binaries, so you cannot exec the usual commands like bash or curl because they are not present in the distroless image. However, you can use ephemeral containers to attach to a running workload Pod to be able to inspect it and run custom commands. For example, see [Collecting Cloud Service Mesh logs](https://docs.cloud.google.com/service-mesh/v1.21/docs/troubleshooting/troubleshoot-collect-logs#configure_envoy_proxy).

## Security

#### VPC Service Controls

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
[VPC Service Controls](https://docs.cloud.google.com/service-mesh/docs/managed/vpc-sc) preview |  |   
[VPC Service Controls](https://docs.cloud.google.com/service-mesh/docs/managed/vpc-sc) GA |  |   
  
### Certificate distribution and rotation mechanisms

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
Workload certificate management |  |   
External certificate management on [ ingress](https://istio.io/v1.21/docs/tasks/traffic-management/ingress/secure-ingress/) and [egress](https://istio.io/latest/docs/tasks/traffic-management/egress/egress-gateway-tls-origination/) gateways. |  |   
  
### Certificate authority (CA) support

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
Cloud Service Mesh certificate authority |  |   
[Certificate Authority Service](https://docs.cloud.google.com/service-mesh/v1.21/docs/security/certificate-authority-service) |  |   
Istio CA |  |   
Integration with custom CAs |  |   
  
### Security features

In addition to supporting Istio security features, Cloud Service Mesh provides even more capabilities to help you secure your applications.

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
[IAP integration](https://docs.cloud.google.com/service-mesh/v1.21/docs/security/iap-integration) |  |   
[End-user authentication](https://docs.cloud.google.com/service-mesh/v1.21/docs/unified-install/options/end-user-auth) |  |   
[Dry-run mode](https://docs.cloud.google.com/service-mesh/v1.21/docs/security/authorization-advanced-features#dry-run_mode) |  |   
[Denial logging](https://docs.cloud.google.com/service-mesh/v1.21/docs/security/authorization-advanced-features#denial_logging) |  |   
Audit policies (not supported) |  |   
  
### Authorization policy

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
Authorization v1beta1 policy | † |   
CUSTOM Authorization Policy | § |   
  
† The `TRAFFIC_DIRECTOR` control plane implementation does not support the `rules.from.source.RemoteIp` and `rules.from.source.NotRemoteIp` fields.

### Peer authentication

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
Auto-mTLS |  |   
mTLS PERMISSIVE mode |  |   
mTLS STRICT mode |  * |  *  
mTLS DISABLE mode |  |   
  
#### Request authentication

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
JWT authentication(Note 1) |  |   
JWT Claim Based Routing[](https://istio.io/latest/docs/tasks/security/authentication/jwt-route/) |  |   
JWT Copy Claim to Headers[](https://istio.io/latest/docs/tasks/security/authentication/claim-to-header/) |  |   
  
**Notes:**

  1. Third-party JWT is enabled by default. 
  2. Add the full fqdn/hostname in JWKSURI while defining RequestAuthentication API. 
  3. Managed control plane enforces Envoy to fetch JWKS when specifying JWKS URI. 



## Telemetry

### Metrics

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
Cloud Monitoring (HTTP in-proxy metrics) |  |   
Cloud Monitoring (TCP in-proxy metrics) |  |   
Prometheus metrics export to Grafana (Envoy metrics only) |  * |  *  
Prometheus metrics export to Kiali |  |   
Google Cloud Managed Service for Prometheus, not including the Cloud Service Mesh dashboard |  * |  *  
[Istio Telemetry API](https://preliminary.istio.io/latest/docs/tasks/observability/telemetry/) |  † |   
Custom adapters/backends, in or out of process |  |   
Arbitrary telemetry and logging backends |  |   
  
† The `TRAFFIC_DIRECTOR` control plane supports a subset of Istio telemetry API used to configure [access logs](https://docs.cloud.google.com/service-mesh/v1.21/docs/observability/access-logs) and [trace](https://docs.cloud.google.com/service-mesh/v1.21/docs/observability/accessing-traces).

**Note:** You can configure third-party telemetry products (such as Grafana, and Prometheus), but we cannot guarantee future compatibility and Cloud Support cannot provide help managing them.

### Proxy request logging

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
[Traffic logs](https://docs.cloud.google.com/service-mesh/v1.21/docs/observability/accessing-logs#traffic_logs) |  |   
[Access logs](https://docs.cloud.google.com/service-mesh/v1.21/docs/observability/accessing-logs#access_logs) |  * |  *  
  
### Tracing

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
Cloud Trace |  * |  *  
Jaeger tracing (allows use of customer-managed Jaeger) |  | Compatible  
Zipkin tracing (allows use of customer-managed Zipkin) |  | Compatible  
**Note:** You can configure third-party telemetry products (such as Jaeger, Zipkin, and Grafana), but we cannot guarantee future compatibility and Cloud Support cannot provide help managing them.

## Networking

### Traffic interception and redirection mechanisms

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
Traditional use of `iptables` using `init` containers with `CAP_NET_ADMIN` |  |   
Istio Container Network Interface (CNI) |  |   
Whitebox sidecar |  |   
  
### Protocol support

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
IPv4 |  |   
HTTP/1.1 |  |   
HTTP/2 |  |   
TCP byte streams  (Note 1) |  |   
[gRPC](https://grpc.io) |  |   
IPv6 |  |   
  
**Notes:**

  1. Although TCP is a supported protocol for networking and TCP metrics are collected, they are not reported. Metrics are displayed only for HTTP services in the Google Cloud console. 
  2. Services that are configured with Layer 7 capabilities for the following protocols are not supported: WebSocket, MongoDB, Redis, Kafka, Cassandra, RabbitMQ, Cloud SQL. You might be able to make the protocol work by using TCP byte stream support. If TCP byte stream cannot support the protocol (for example, Kafka sends a redirect address in a protocol-specific reply and this redirect is incompatible with Cloud Service Mesh's routing logic), then the protocol isn't supported. 



### Envoy deployments

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
Sidecars |  |   
Ingress gateway |  |   
Egress directly out from sidecars |  |   
Egress using egress gateways |  * |  *  
  
### CRD support

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
Sidecar resource |  |   
Service entry resource |  |   
Percentage, fault injection, path matching, redirects, retries, rewriting, timeout, retry, mirroring, header manipulation, and CORS routing rules |  |   
[`EnvoyFilter` API](https://istio.io/docs/reference/config/networking/v1alpha3/envoy-filter/) | § |   
[`WasmPlugin` API](https://istio.io/latest/docs/reference/config/proxy_extensions/wasm-plugin/) |  |   
Istio Operator |  |   
  
### Load balancer for the Istio ingress gateway

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
Third-party external load balancer |  |   
Google Cloud Internal load balancer |  * |  *  
  
### Service mesh cloud gateway

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
Service mesh cloud gateway |  |   
  
### Kubernetes Gateway API

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
Kubernetes Gateway API |  |   
  
### Load balancing policies

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
Round robin |  |   
Least connections |  |   
Random |  |   
Passthrough |  |   
Consistent hash |  |   
Locality |  |   
  
### Service entry

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
ServiceEntry v1beta1 | † |   
  
† The `TRAFFIC_DIRECTOR` control plane implementation does not support following fields and values in fields:

  * `workloadSelector` field
  * `endpoints[].network` field
  * `endpoints[].locality` field
  * `endpoints[].weight` field
  * `endpoints[].serviceAccount` field
  * `DNS_ROUND_ROBIN` value in `resolution` field
  * `MESH_INTERNAL` value in `location` field
  * Unix domain socket address in `endpoints[].address` field
  * `subjectAltNames` field



### Destination rule

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
DestinationRule v1beta1 | † |   
  
† The `TRAFFIC_DIRECTOR` control plane implementation does not support `trafficPolicy.loadBalancer.localityLbSetting` field and `trafficPolicy.tunnel` field. Additionally, the `TRAFFIC_DIRECTOR` control plane implementation requires that the destination rule defining subsets is in the same namespace and cluster with the Kubernetes service or ServiceEntry.

### Sidecar

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
Sidecar v1beta1 | † |   
  
† The `TRAFFIC_DIRECTOR` control plane implementation does not support following fields and values in fields:

  * `ingress` field
  * `egress.port` field
  * `egress.bind` field
  * `egress.captureMode` field
  * `inboundConnectionPool` field



## MeshConfig

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
LocalityLB | § |   
ExtensionProviders | § |   
CACert |  |   
ImageType - distroless | § |   
OutboundTrafficPolicy | § |   
defaultProviders.accessLogging |  |   
defaultProviders.tracing |  |   
defaultConfig.tracing.stackdriver | § |   
accessLogFile | § |   
  
## ProxyConfig

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
DNS proxy (ISTIO_META_DNS_CAPTURE, ISTIO_META_DNS_AUTO_ALLOCATE) |  |   
HTTP/1.0 support (ISTIO_META_NETWORK) |  |   
Image selection (distroless or base image) | † |   
  
† [Distroless image](https://docs.cloud.google.com/service-mesh/v1.21/docs/enable-optional-features-managed#distroless_proxy_image) is used for the injection.

## Regions

GKE clusters must be in one of the following regions or any zone within the following regions.

Region | Location  
---|---  
`africa-south1` | Johannesburg  
`asia-east1` | Taiwan  
`asia-east2` | Hong Kong  
`asia-northeast1` | Tokyo, Japan  
`asia-northeast2` | Osaka, Japan  
`asia-northeast3` | South Korea  
`asia-south1` | Mumbai, India  
`asia-south2` | Delhi, India  
`asia-southeast1` | Singapore  
`asia-southeast2 ` | Jakarta  
`australia-southeast1` | Sydney, Australia  
`australia-southeast2` | Melbourne, Australia  
`europe-central2` | Poland  
`europe-north1` | Finland  
`europe-north2` | Stockholm  
`europe-southwest1` | Spain  
`europe-west1` | Belgium  
`europe-west2` | England  
`europe-west3` | Frankfurt, Germany  
`europe-west4` | Netherlands  
`europe-west6` | Switzerland  
`europe-west8` | Milan, Italy  
`europe-west9` | France  
`europe-west10` | Berlin, Germany  
`europe-west12` | Turin, Italy  
`me-central1` | Doha  
`me-central2` | Dammam, Saudi Arabia  
`me-west1` | Tel Aviv  
`northamerica-northeast1` | Montreal, Canada  
`northamerica-northeast2` | Toronto, Canada  
`northamerica-south1` | Mexico  
`southamerica-east1` | Brazil  
`southamerica-west1` | Chile  
`us-central1` | Iowa  
`us-east1` | South Carolina  
`us-east4` | Northern Virginia  
`us-east5` | Ohio  
`us-south1` | Dallas  
`us-west1` | Oregon  
`us-west2` | Los Angeles  
`us-west3` | Salt Lake City  
`us-west4` | Las Vegas  
  
## User interface

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
Cloud Service Mesh dashboards in the Google Cloud console |  |   
Cloud Monitoring |  |   
Cloud Logging |  |   
  
## Tooling

Feature | Managed (TD) | Managed (istiod)  
---|---|---  
`gcloud beta container fleet mesh debug ` tool  |  |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
