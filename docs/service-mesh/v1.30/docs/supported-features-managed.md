---
url: https://docs.cloud.google.com/service-mesh/v1.30/docs/supported-features-managed/
title: Supported features using Istio APIs (managed control plane) \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:27:52.545989+00:00
---

# Supported features using Istio APIs (managed control plane)  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/v1.30/docs/supported-features-managed/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/v1.30/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/v1.30/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Supported features using Istio APIs (managed control plane)

**Caution:** Managed Cloud Service Mesh using the `ISTIOD` control plane implementation is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). You must [modernize](https://docs.cloud.google.com/service-mesh/v1.30/docs/modernization) all managed `ISTIOD` fleets to the `TRAFFIC_DIRECTOR` control plane implementation. 

This page describes the supported features and limitations for Cloud Service Mesh using `TRAFFIC_DIRECTOR` or `ISTIOD` as the control plane and the differences between each implementation. Note that these are not options you can choose. The `ISTIOD` implementation is only available for existing users. New installations use the `TRAFFIC_DIRECTOR` implementation when possible.

For a list of Istio and Google Cloud APIs supported by managed Cloud Service Mesh with `TRAFFIC_DIRECTOR`, see [API Support in Managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.30/docs/onboarding/api-support).

For the list of Cloud Service Mesh supported features for an in-cluster control plane, see [Using Istio APIs (in-cluster `istiod` control plane)](https://docs.cloud.google.com/service-mesh/v1.30/docs/supported-features-in-cluster).

If you're not sure which Cloud Service Mesh control plane you're using, you can check your control plane implementation using the instructions in [Identify control plane implementation](https://docs.cloud.google.com/service-mesh/v1.30/docs/check-control-plane-implementation).

## Limitations

**Caution:** All Cloud Service Mesh clusters for one mesh must be registered to the same fleet at all times to use Cloud Service Mesh. Other clusters in the project of a Cloud Service Mesh cluster must not be registered to a different fleet. 

The following limitations apply:

  * GKE clusters must be in one of the supported regions.
  * GKE version must be a supported version.
  * Only the platforms listed in Environments are supported.
  * Pods running with [`hostNetwork: true`](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.26/#podspec-v1-core) are not supported.
  * Managed Cloud Service Mesh must not be deployed in a cluster that also has an in-cluster deployment of OSS Istio or an in-cluster Cloud Service Mesh control plane.
  * Changing [release channels](https://docs.cloud.google.com/service-mesh/v1.30/docs/managed/select-a-release-channel) is not supported.
  * Migrations from [managed Cloud Service Mesh with `asmcli`](https://docs.cloud.google.com/service-mesh/v1.30/docs/managed/provision-managed-anthos-service-mesh-asmcli) to [Cloud Service Mesh with fleet API](https://docs.cloud.google.com/service-mesh/v1.30/docs/managed/provision-managed-anthos-service-mesh) are not supported. Similarly, provisioning managed Cloud Service Mesh with fleet API from `--management manual` to `--management automatic` is not supported.
  * Migrations from in-cluster Cloud Service Mesh are only supported using the [Canary cluster migration](https://docs.cloud.google.com/service-mesh/v1.30/docs/migrate-istio-to-anthos-service-mesh) strategy.
  * Migrations and upgrades are supported only from in-cluster Cloud Service Mesh versions that are in the [Supported versions](https://docs.cloud.google.com/service-mesh/v1.30/docs/supported-features-in-cluster#supported_versions) table and using Mesh CA or Certificate Authority Service. Installations with Istio CA (previously known as Citadel) must first [migrate to Mesh CA](https://docs.cloud.google.com/service-mesh/v1.30/docs/unified-install/options/ca-migration).
  * The limits on scale are outlined in this [guide](https://docs.cloud.google.com/service-mesh/v1.30/docs/operate-and-maintain/scalability-limits)
  * Only multi-primary deployment option for multi-cluster is supported: primary-remote deployment option for multi-cluster is not.
  * `istioctl ps` is not supported. Instead you can use the `gcloud beta container fleet mesh debug` commands as described in [Troubleshooting](https://docs.cloud.google.com/service-mesh/v1.30/docs/troubleshooting/troubleshoot-intro).
  * Unsupported APIs:

    * `WasmPlugin` API

    * `IstioOperator` API

    * `Kubernetes Ingress` API

**Note:** You can still enable optional features without using the IstioOperator API, see [Enable optional features on managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.30/docs/enable-optional-features-managed).
  * For detailed field-level support and limitations across all Istio APIs, see [Cloud Service Mesh API support](https://docs.cloud.google.com/service-mesh/v1.30/docs/onboarding/api-support).

  * You can use the managed control plane without a GKE Enterprise subscription, but certain UI elements and features in Google Cloud console are only available to GKE Enterprise subscribers. For information about what is available to subscribers and non-subscribers, see [GKE Enterprise and Cloud Service Mesh UI differences](https://docs.cloud.google.com/service-mesh/v1.30/docs/ui-differences).

  * During the provisioning process for a managed control plane, Istio CRDs corresponding to the selected channel are installed in the specified cluster. If there are existing Istio CRDs in the cluster, they will be overwritten.

  * Managed Cloud Service Mesh only supports the default DNS domain `.cluster.local`.

  * New installations of managed Cloud Service Mesh fetch JWKS only using Envoys, unless the fleet contains other clusters for which that behavior is not enabled. This is equivalent to the `PILOT_JWT_ENABLE_REMOTE_JWKS=envoy` Istio option. Compared to installations that don't have VPCSC_GA_SUPPORTED condition (see below), you might need extra configuration for `ServiceEntry` and `DestinationRule` configurations. For an example, see [`requestauthn-with-se.yaml.tmpl`](https://github.com/istio/istio/blob/master/tests/integration/security/remote_jwks/testdata/requestauthn-with-se.yaml.tmpl). You can determine whether the current mode of operation is equivalent to `PILOT_JWT_ENABLE_REMOTE_JWKS=envoy` by determining whether [VPC Service Controls](https://docs.cloud.google.com/service-mesh/v1.30/docs/managed/vpc-sc) are supported for the control plane (ie. the VPCSC_GA_SUPPORTED condition is displayed).

  * Managed data plane is only supported for workloads without additional sidecars (other than the Cloud Service Mesh sidecar).




## Control plane differences

There are differences in supported features between the `ISTIOD` and `TRAFFIC_DIRECTOR` control plane implementations. To check which implementation you are using, see [Identify control plane implementation](https://docs.cloud.google.com/service-mesh/v1.30/docs/check-control-plane-implementation).

  * – indicates the feature is available and enabled by default.
  * † - indicates that feature APIs may have differences between various platforms.
  * * – indicates the feature is supported for the platform and can be enabled, as described in [Enable optional features](https://docs.cloud.google.com/service-mesh/v1.30/docs/enable-optional-features) or the feature guide linked in the feature table.
  * – indicates either the feature isn't available or it isn't supported.



The default and optional features are fully supported by Google Cloud Support. Features not explicitly listed in the tables receive best-effort support.

### What determines control plane implementation

When you provision managed Cloud Service Mesh the first time in a fleet, we determine which control plane implementation to use. The same implementation is used for all clusters that provision managed Cloud Service Mesh in that fleet.

New fleets that onboard to managed Cloud Service Mesh receive the `TRAFFIC_DIRECTOR` control plane implementation, with certain exceptions:

  * If you are an existing managed Cloud Service Mesh user, you receive the `ISTIOD` control plane implementation when you onboard a new fleet in the same Google Cloud Organization to managed Cloud Service Mesh, until at least June 30, 2024. If you are one of these users, you can contact Support to fine-tune this behavior. Users whose existing usage is not compatible with the `TRAFFIC_DIRECTOR` implementation without changes will continue to receive the `ISTIOD` implementation until September 8, 2024. (These users received a Service Announcement.)
  * If any GKE on Google Cloud cluster in your fleet contains an in-cluster Cloud Service Mesh control plane when you provision managed Cloud Service Mesh, you will receive the `ISTIOD` control plane implementation.
  * If any cluster in your fleet uses [GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/sandbox-pods), when you provision managed Cloud Service Mesh, you receive the `ISTIOD` control plane implementation.



## Managed control plane supported features

### Install, upgrade, and rollback

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
Installation on GKE clusters using [fleet](https://docs.cloud.google.com/anthos/multicluster-management/fleets) feature API |  |   
Upgrades from ASM 1.9 versions that use Mesh CA |  |   
Direct (skip-level) upgrades from Cloud Service Mesh versions prior to 1.9 (see notes for indirect upgrades) |  |   
Direct (skip-level) upgrades from Istio OSS (see notes for indirect upgrades) |  |   
Direct (skip-level) upgrades from Istio-on-GKE add-on (see notes for indirect upgrades) |  |   
Enabling [optional features](https://docs.cloud.google.com/service-mesh/v1.30/docs/managed-service-mesh-optional-features) |  |   
**Note:** Indirect migrations and upgrades are supported, meaning that you can follow the standard Cloud Service Mesh [upgrade paths](https://docs.cloud.google.com/service-mesh/v1.30/docs/upgrade-path-old-versions-gke) through each version until you reach Cloud Service Mesh 1.30 with an in-cluster control plane, then you can migrate to the managed control plane. Direct migrations and upgrades are supported only from Cloud Service Mesh versions 1.9 or later installed with Mesh CA. Installations with Istio CA must first migrate to Mesh CA.

### Environments

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
GKE versions [currently available in release channels](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#current_versions), in one of the supported regions |  |   
GKE versions [currently available in release channels](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#current_versions), in one of the supported regions, GKE [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) clusters  |  |   
Environments outside of Google Cloud (GKE Enterprise on-premises, GKE Enterprise on other public clouds, Amazon EKS, Microsoft AKS, or other Kubernetes clusters) |  |   
  
### Scale

Refer to the [Scalability Limits page](https://docs.cloud.google.com/service-mesh/v1.30/docs/operate-and-maintain/scalability-limits)

### Platform environment

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
Single network |  |   
Multi-network |  |   
Single-project |  |   
Multi-project with Shared VPC |  |   
  
### Multi-cluster deployment

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
Multi-primary |  |   
Primary-remote |  |   
Multi-cluster endpoint discovery with [declarative API](https://docs.cloud.google.com/service-mesh/v1.30/docs/unified-install/gke-install-multi-cluster#endpoint-discovery-declarative-api) |  |   
Multi-cluster endpoint discovery with [remote secrets](https://docs.cloud.google.com/service-mesh/v1.30/docs/unified-install/gke-install-multi-cluster#configure_endpoint_discovery_between_public_clusters) |  |   
Multi-cluster endpoint discovery with [declarative API](https://docs.cloud.google.com/service-mesh/v1.30/docs/unified-install/gke-install-multi-cluster#endpoint-discovery-declarative-api) and a simple topology |  |   
  
**Notes on terminology**

  * A multi-primary configuration means that the configuration must be replicated in all clusters.
  * A primary-remote configuration means that a single cluster contains the configuration and is considered the source of truth.
  * Cloud Service Mesh uses a simplified definition of network based on general connectivity. Workload instances are on the same network if they are able to communicate directly, without a gateway.
  * Simple topology for multi-cluster endpoint discovery means that every cluster in the fleet either participates or does not participate in endpoints discovery. Complex topologies that are unsupported include (a) one-way endpoint discover (e.g. cluster A can discover endpoints in cluster B but not vice versa) and (b) disjointed endpoint discovery networks (e.g. clusters A and B can discover each other's endpoints, clusters C and D can discover each other's endpoints, but A/B and C/D cannot discover each other's endpoints).



### Base Images

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
[Distroless proxy image](https://docs.cloud.google.com/service-mesh/v1.30/docs/enable-optional-features-managed#distroless_proxy_image) | † |   
  
† Istio publishes `default`, `debug`, and `distroless` proxy images. For Cloud Service Mesh with a managed (`TRAFFIC_DIRECTOR`) control plane: directly onboarded clusters use `distroless` by default and cannot be changed. Migrated clusters use `default` images by default and can opt-in to `distroless` using `MeshConfig` or pod annotation. Overrides to other image types (`debug`) are unsupported.

Note that distroless images have minimal binaries, so you cannot exec the usual commands like bash or curl because they are not present in the distroless image. However, you can use ephemeral containers to attach to a running workload Pod to be able to inspect it and run custom commands. For example, see [Collecting Cloud Service Mesh logs](https://docs.cloud.google.com/service-mesh/v1.30/docs/troubleshooting/troubleshoot-collect-logs#configure_envoy_proxy).

## Security

#### VPC Service Controls

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
[VPC Service Controls](https://docs.cloud.google.com/service-mesh/v1.30/docs/managed/vpc-sc) |  |   
  
### Certificate distribution and rotation mechanisms

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
Workload certificate management |  |   
External certificate management on [ ingress](https://istio.io/v1.30/docs/tasks/traffic-management/ingress/secure-ingress/) and [egress](https://istio.io/latest/docs/tasks/traffic-management/egress/egress-gateway-tls-origination/) gateways. |  |   
  
### Certificate authority (CA) support

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
Cloud Service Mesh certificate authority |  |   
[Certificate Authority Service](https://docs.cloud.google.com/service-mesh/v1.30/docs/security/certificate-authority-service) |  |   
Istio CA |  |   
Integration with custom CAs |  |   
  
### Security features

In addition to supporting Istio security features, Cloud Service Mesh provides even more capabilities to help you secure your applications.

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
[IAP integration](https://docs.cloud.google.com/service-mesh/v1.30/docs/security/iap-integration) |  |   
[End-user authentication](https://docs.cloud.google.com/service-mesh/v1.30/docs/unified-install/options/end-user-auth) |  |   
[Dry-run mode](https://docs.cloud.google.com/service-mesh/v1.30/docs/security/authorization-advanced-features#dry-run_mode) |  |   
[Denial logging](https://docs.cloud.google.com/service-mesh/v1.30/docs/security/authorization-advanced-features#denial_logging) |  |   
Audit policies (not supported) |  |   
  
### Authorization policy

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
Authorization v1beta1 policy |  |   
CUSTOM Authorization Policy |  |   
  
### Peer authentication

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
Auto-mTLS |  |   
mTLS PERMISSIVE mode |  |   
mTLS STRICT mode |  * |  *  
mTLS DISABLE mode |  |   
  
**Note:** While the `PeerAuthentication` API does not support `DISABLE` mode for the `TRAFFIC_DIRECTOR` control plane implementation, you can disable mTLS for specific workloads by using the `DestinationRule` API as a workaround. For more information, see [Disabling mTLS for Managed CSM](https://docs.cloud.google.com/service-mesh/v1.30/docs/security/configuring-mtls#disable-mtls).

#### Request authentication

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
JWT authentication(Note 1) |  |   
JWT Claim Based Routing[](https://istio.io/latest/docs/tasks/security/authentication/jwt-route/) |  |   
JWT Copy Claim to Headers[](https://istio.io/latest/docs/tasks/security/authentication/claim-to-header/) |  |   
  
**Notes:**

  1. Third-party JWT is enabled by default. 
  2. Add the full fqdn/hostname in JWKSURI while defining RequestAuthentication API. 
  3. Managed control plane enforces Envoy to fetch JWKS when specifying JWKS URI. 
  4. AES CBC algorithms A128CBC-HS256, A192CBC-HS384, and A256CBC-HS512 are not allowed in inlined JWKS when using `TRAFFIC_DIRECTOR` control plane implementation. 



## Telemetry

### Metrics

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
Cloud Monitoring (HTTP in-proxy metrics) |  |   
Cloud Monitoring (TCP in-proxy metrics) |  |   
Prometheus metrics export to Grafana (Envoy metrics only) |  * |  *  
Prometheus metrics export to Kiali |  |   
Google Cloud Managed Service for Prometheus, not including the Cloud Service Mesh dashboard |  * |  *  
[Istio Telemetry API](https://preliminary.istio.io/latest/docs/tasks/observability/telemetry/) |  † |   
Custom adapters/backends, in or out of process |  |   
Arbitrary telemetry and logging backends |  |   
  
† The `TRAFFIC_DIRECTOR` control plane supports a subset of Istio telemetry API used to configure [access logs](https://docs.cloud.google.com/service-mesh/v1.30/docs/observability/access-logs) and [trace](https://docs.cloud.google.com/service-mesh/v1.30/docs/observability/accessing-traces).

**Note:** You can configure third-party telemetry products (such as Grafana, and Prometheus), but we cannot guarantee future compatibility and Cloud Support cannot provide help managing them.

### Proxy request logging

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
[Traffic logs](https://docs.cloud.google.com/service-mesh/v1.30/docs/observability/accessing-logs#traffic_logs) |  |   
[Access logs](https://docs.cloud.google.com/service-mesh/v1.30/docs/observability/accessing-logs#access_logs) |  * |  *  
  
### Tracing

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
Cloud Trace |  * |  *  
Jaeger tracing (allows use of customer-managed Jaeger) |  | Compatible  
Zipkin tracing (allows use of customer-managed Zipkin) |  | Compatible  
**Note:** You can configure third-party telemetry products (such as Jaeger, Zipkin, and Grafana), but we cannot guarantee future compatibility and Cloud Support cannot provide help managing them.

## Networking

### Traffic interception and redirection mechanisms

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
Use of `iptables` using `init` containers with `CAP_NET_ADMIN` |  | †  
Istio Container Network Interface (CNI) |  |   
Whitebox sidecar |  |   
  
† We strongly recommend using Container Network Interface (CNI) instead of `init` containers.

### Protocol support

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
IPv4 |  |   
HTTP/1.1 |  |   
HTTP/2 |  |   
TCP byte streams  (Note 1) |  |   
[gRPC](https://grpc.io) |  |   
IPv6 | † |   
  
**Notes:**

  1. Although TCP is a supported protocol for networking and TCP metrics are collected, they are not reported. Metrics are displayed only for HTTP services in the Google Cloud console. 
  2. Services that are configured with Layer 7 capabilities for the following protocols are not supported: WebSocket, MongoDB, Redis, MySQL, Kafka, Cassandra, RabbitMQ, Cloud SQL. You might be able to make the protocol work by using TCP byte stream support. If TCP byte stream cannot support the protocol (for example, Kafka sends a redirect address in a protocol-specific reply and this redirect is incompatible with Cloud Service Mesh's routing logic), then the protocol isn't supported. Although gateway ports can be created with Mongo, MySQL and Redis protocol, the mesh treats the resulting traffic as standard TCP, lacking protocol-specific handling. 
  3. † In proxyless gRPC, IPv6 dual-stack features are supported only in gRPC 1.66.1 or newer in [C++](https://github.com/grpc/grpc/releases/tag/v1.66.1) and [Python](https://pypi.org/project/grpcio/1.66.1), [gRPC Go v1.71](https://github.com/grpc/grpc-go/releases/tag/v1.71.0), and or [gRPC Node.js v1.12](https://github.com/grpc/grpc-node/releases/tag/%40grpc%2Fgrpc-js-xds%401.12.0). If you try to configure dual-stack features with a version of gRPC that doesn't support dual-stack, the clients will use only the first address sent by Traffic Director. 



### Envoy deployments

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
Sidecars |  |   
Ingress gateway |  |   
Egress directly out from sidecars |  |   
Egress using egress gateways |  * |  *  
  
### CRD support

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
Sidecar resource |  |   
Service entry resource |  |   
Percentage, fault injection, path matching, redirects, retries, rewriting, timeout, retry, mirroring, header manipulation, and CORS routing rules |  |   
[`WasmPlugin` API](https://istio.io/latest/docs/reference/config/proxy_extensions/wasm-plugin/) |  |   
Istio Operator |  |   
  
### Load balancer for the Istio ingress gateway

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
Third-party external load balancer |  |   
Google Cloud Internal load balancer |  * |  *  
  
### Service mesh cloud gateway

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
Service mesh cloud gateway |  |   
  
### Kubernetes Gateway API

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
Kubernetes Gateway API |  |   
  
### Load balancing policies

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
Round robin |  |   
Least connections |  |   
Random |  |   
Passthrough |  |   
Consistent hash |  |   
Locality |  |   
GCPTrafficDistributionPolicy |  |   
GCPBackendPolicy |  |   
  
### Load balancing modes

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
RATE |  |   
UTILIZATION |  |   
CUSTOM_METRICS |  |   
IN-FLIGHT |  |   
  
For more information about balancing modes, see the [Backend services overview](https://docs.cloud.google.com/load-balancing/docs/backend-service#balancing-mode).

### Service entry

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
ServiceEntry v1beta1 | † |   
  
† The `TRAFFIC_DIRECTOR` control plane implementation supports a subset of `ServiceEntry` fields. For the complete list of supported fields, unsupported fields, and configuration limitations, see [API support: ServiceEntry](https://docs.cloud.google.com/service-mesh/v1.30/docs/onboarding/api-support#serviceentryv1beta1).

### Destination rule

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
DestinationRule v1beta1 | † |   
  
† The `TRAFFIC_DIRECTOR` control plane implementation requires that the destination rule defining subsets is in the same namespace and cluster as the Kubernetes service or ServiceEntry. For the complete list of supported fields, unsupported fields, and configuration limitations, see [API support: DestinationRule](https://docs.cloud.google.com/service-mesh/v1.30/docs/onboarding/api-support#destinationrulev1beta1).

### Sidecar

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
Sidecar v1beta1 | † |   
  
† The `TRAFFIC_DIRECTOR` control plane implementation supports a subset of `Sidecar` fields. For the complete list of supported fields, unsupported fields, and configuration limitations, see [API support: Sidecar](https://docs.cloud.google.com/service-mesh/v1.30/docs/onboarding/api-support#sidecarv1beta1).

### DNS proxy

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
Name resolution of `Service` across clusters | † |   
Name resolution of `ServiceEntry` in a cluster | † |   
Name resolution of [Headless `Service`](https://kubernetes.io/docs/concepts/services-networking/service/#headless-services) |  |   
[Address auto allocation](https://docs.cloud.google.com/service-mesh/v1.30/docs/operate-and-maintain/dns-proxy#ip_auto-allocation_for_serviceentry) | † |   
  
† `1.21.5-asm.39` or later version of the sidecar is required.

### EnvoyFilter

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
EnvoyFilter v1alpha3 | † |   
  
† Refer to [Dataplane Extensibility page](https://docs.cloud.google.com/service-mesh/v1.30/docs/data-plane-extensibility) for supported fields and configurable extensions

## MeshConfig

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
DiscoverySelectors |  |   
clusterLocal |  |   
LocalityLB | † |   
ExtensionProviders |  |   
CACert |  |   
ImageType - distroless | † |   
OutboundTrafficPolicy |  |   
defaultProviders.accessLogging |  |   
defaultProviders.tracing |  |   
defaultConfig.tracing.stackdriver |  |   
accessLogFile | † |   
accessLogFormat | † |   
accessLogEncoding | † |   
  
† See [Distroless proxy image](https://docs.cloud.google.com/service-mesh/v1.30/docs/enable-optional-features-managed#distroless_proxy_image) for detailed configuration behavior.  
† See [Configuring Locality Load Balancing](https://docs.cloud.google.com/service-mesh/v1.30/docs/operate-and-maintain/multi-cluster#configuring-locality-load-balancing) for detailed configuration behavior and limitations.   
† See [Customizing Envoy access log format and encoding](https://docs.cloud.google.com/service-mesh/v1.30/docs/observability/access-logs#customizing_envoy_access_log_format_and_encoding) for detailed configuration behavior and limitations.   


## ProxyConfig

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
HTTP/1.0 support (ISTIO_META_NETWORK) |  |   
Image selection (distroless or base image) |  |   
[Kubernetes native sidecar](https://kubernetes.io/blog/2023/08/25/native-sidecar-containers) (ENABLE_NATIVE_SIDECARS) |  |   
  
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

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
Cloud Service Mesh dashboards in the Google Cloud console |  |   
Cloud Monitoring |  |   
Cloud Logging |  |   
  
## Tooling

Feature | Managed (TD) | Managed (istiod) deprecated  
---|---|---  
`gcloud beta container fleet mesh debug ` tool  |  |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
