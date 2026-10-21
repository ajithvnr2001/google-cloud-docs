---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ambient-overview/
title: Ambient networking overview \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:41:03.018180+00:00
---

# Ambient networking overview  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ambient-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Ambient networking overview Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note** : Before using GKE ambient networking, you must be added to an allowlist. Request access by filling out the [sign-up form](https://forms.gle/HhretawUX6GFFxq87). Allow 2 to 3 business days for your request to be processed. 

GKE ambient networking provides a simplified, sidecarless deployment model for a service mesh with Layer 4 capabilities. By moving proxy functionality to node-level components integrated into [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2) (DPv2), ambient networking reduces resource overhead, eliminates workload restarts for proxy updates, and simplifies mesh lifecycle management.

## Capabilities

The preview of GKE ambient networking supports single-cluster Layer 4 mesh functionality:

  * **Mutual TLS (mTLS):** enforces encrypted transit and identity authentication.
  * **Service discovery:** discovers services and routes connections automatically across workloads.
  * **Layer 4 Traffic Management:** load balances and routes TCP traffic.
  * **Layer 4 Telemetry:** emits network traffic, connection, and error metrics to Cloud Observability. For details on visualizing and analyzing these metrics, see the [Network Services Monitoring overview](https://docs.cloud.google.com/network-intelligence-center/docs/network-services-monitoring/overview).

**Note:** This feature requires using the [Gateway API](https://docs.cloud.google.com/service-mesh/docs/gateway/overview). Istio APIs are not supported for ambient networking.

## Benefits of ambient networking

Compared to sidecar-based service mesh architectures, ambient networking offers several key operational and resource advantages:

  * **Simplified lifecycle management:** eliminates the shared-fate model between sidecar proxies and application containers. You can apply proxy updates, security patches, and upgrades at the node level without restarting workload Pods or causing application downtime.

  * **Reduced resource consumption:** consolidates proxying into shared node-level instances, reducing CPU and memory overhead by up to 90% compared to sidecar models.

  * **Elimination of sidecar risks:** solves common sidecar issues such as container proxy-bypass vulnerabilities, sticky connection disruption, and unreliable connection termination propagation.

  * **Native Google Cloud platform integration:** integrates natively with [GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2) (DPv2), [Managed Workload Identity](https://docs.cloud.google.com/iam/docs/create-managed-workload-identities-gke), Certificate Authority Service (CAS), and Google Cloud Observability.




### Interoperability and scope

During this preview of ambient networking, note the following scope and interoperability constraints:

  * **Gateway API requirement:** ambient networking requires the [Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api). Istio APIs are not supported.
  * **Workload interoperability:** workloads enrolled in ambient networking cannot interoperate with sidecar-injected workloads (on GKE, Compute Engine, or Cloud Run) or proxyless gRPC workloads. 



## Architecture and components

Ambient networking integrates directly into GKE Dataplane V2 (DPv2) on each node rather than injecting Envoy sidecars into workload Pods.

### Existing control plane components

Ambient networking relies on control plane components to distribute policy, translate configuration, and issue certificates:

  * **Traffic Director:** provides the xDS control plane for policy distribution and routing configuration.
  * **GKE Gateway Controller:** translates Kubernetes custom resources into Traffic Director configuration.
  * **Certificate Authority Service (CAS):** issues X.509 identity certificates for workloads by using Managed Workload Identity.
  * **GKE Cluster Control Plane:** approves Certificate Signing Requests (CSRs) and routes them to CAS.



### Node components

Ambient networking installs the following per-node components to intercept and proxy workload traffic directly on each cluster node:

  * **GKE ambient NRI plugin:** [node Resource Interface](https://github.com/containerd/nri) (NRI) plugin that configures low-level networking to intercept and redirect Pod traffic to the proxy.

  * **GKE ambient proxy:** node-level proxy that manages listening sockets, receives xDS rules from Traffic Director, fetches X.509 identity certificates on-demand from the GKE Control Plane, and proxies Layer 4 traffic.




Node-level ambient dataplane components run as DaemonSets in the `gke-managed-ambient` namespace and are automatically versioned, patched, and upgraded alongside the GKE control plane.

## Target scale and limits

During preview, ambient networking has the following scope and interoperability limits:

Resource metric | GKE DPv2 (with ambient) | Standard GKE DPv2 (without ambient)  
---|---|---  
**Nodes per cluster** | **500** | 7,500  
**Services per cluster** | **300** | 10,000  
**Pods per cluster** | **5,000** | 200,000  
**Max Pods per node** | **256** | 256  
  
For general GKE cluster quotas, see the [cluster limits](https://docs.cloud.google.com/kubernetes-engine/quotas#limits_per_cluster) and the [GKE GKE Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2) specifications.

## Pricing

Review the following details regarding pricing and operational resource charges for ambient networking:

  * All Pods in any namespace with the ambient label `networking.gke.io/dataplane-mode=ambient` will be billed at $0.004 per hour ($0.00006667 per minute or roughly $2.90 per month). Billing won't be enforced during preview.
  * Standard usage charges for Cloud Observability (Cloud Monitoring / Cloud Logging) and Certificate Authority Service apply.



## Understand Gateway API resources

When you use ambient networking, the Kubernetes Gateway API custom resources you manage on your cluster are automatically translated into a set of managed Google Cloud API resources.

Functionality | Managed Google Cloud API resource | Scope | Cardinality  
---|---|---|---  
**Mesh** | `Mesh` | Regional | 1 per cluster  
**Service routing** | `TCPRoute` | Regional | 1 per cluster, plus 1 per Service targeted by a `GCPClientTLSPolicy`  
**Service representation** | `BackendService` | Regional | 1 per cluster  
**Client authentication** | `ClientTlsPolicy` | Regional | 1 per cluster  
**Server authentication** | `ServerTlsPolicy` | Regional | 3 per cluster  
**Server authentication** | `EndpointPolicy` | Regional | 1 per `GCPServerTLSPolicy`, plus 1 per distinct mTLS mode in its `portOverrides`  
**Authorization** | `AuthzPolicy` | Regional | 1 per Pod `targetRef` in each `GCPAuthzPolicy` with `enforcementLevel: L4`  
**Egress routing** | `EgressRouting` | Regional | 1 per namespace that has a `GCPEgressPolicy`  
  
## What's next

  * [Prepare GKE ambient networking](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-ambient-networking)
  * [About Gateway API](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api)
  * [Network Services Monitoring overview](https://docs.cloud.google.com/network-intelligence-center/docs/network-services-monitoring/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
