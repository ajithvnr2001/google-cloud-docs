---
url: https://docs.cloud.google.com/feeds/servicemesh-release-notes.xml
title: Cloud Service Mesh - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:22:15.712658+00:00
---

# Cloud Service Mesh - Release notes

> Source: https://docs.cloud.google.com/feeds/servicemesh-release-notes.xml

tag:google.com,2016:servicemesh-release-notesCloud Service Mesh - Release notesGoogle Cloud Platform2026-10-12T00:00:00-07:00October 12, 2026tag:google.com,2016:servicemesh-release-notes#October_12_20262026-10-12T00:00:00-07:001.27.x 

### Announcement

**1.31.1-asm.16 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.31.1-asm.16 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.31.1](https://istio.io/latest/news/releases/1.31.x/announcing-1.31/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster).

The following are not supported:

  * `PILOT_NODE_UNTAINT_CONTROLLERS_TAINT_NAME`
  * `prefix_rewrite` field in `HTTPRedirect`
  * `ALLOW_ANY_DYNAMIC_DNS` in `outboundTrafficPolicy`
  * `connectionSettings` in `ProxyConfig`
  * `defaultTrafficPolicy` in `MeshConfig`
  * `zoneAwareLbSetting` in `DestinationRule` and `MeshConfig`
  * `trustDomains` and `notTrustDomains` fields in `source` field of `AuthorizationPolicy`
  * `fips-140-3` for the `COMPLIANCE_POLICY`
  * `PILOT_ENABLE_REMOTE_CREDENTIALS_CONTROLLER`
  * External SDS provider for gateways
  * `PILOT_AGENT_MERGE_ENVOY_STATS`
  * `prometheus.istio.io/scrape-targets`
  * `ENVOY_SECURE_METRICS_PORT` and `ENVOY_SECURE_MERGED_METRICS_PORT`
  * `istioctl manifest generate` with `-o/--output`



For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh version 1.31.1-asm.16 uses Envoy v1.39.3.

### Announcement

**1.30.5-asm.8 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh 1.30.5-asm.8 uses Envoy v1.38.7-dev.

This release resolves the security vulnerability listed in Security Bulletin [GCP-2026-067](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-067).

### Fixed

Patch 1.30.5-asm.8 contains the fix for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-18924](https://nvd.nist.gov/vuln/detail/CVE-2026-18924) | Yes | Yes | No | Yes | Medium (9.1)  
[CVE-2026-82474](https://nvd.nist.gov/vuln/detail/CVE-2026-82474) | Yes | Yes | No | Yes | Medium (8.5)  
[CVE-2026-82209](https://nvd.nist.gov/vuln/detail/CVE-2026-82209) | Yes | Yes | No | Yes | Medium (8.2)  
[CVE-2026-84782](https://nvd.nist.gov/vuln/detail/CVE-2026-84782) | Yes | Yes | No | Yes | High (8.2)  
[CVE-2026-96512](https://nvd.nist.gov/vuln/detail/CVE-2026-96512) | Yes | Yes | No | Yes | Medium (7.8)  
[CVE-2026-80230](https://nvd.nist.gov/vuln/detail/CVE-2026-80230) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-13608](https://nvd.nist.gov/vuln/detail/CVE-2026-13608) | Yes | Yes | No | Yes | Medium (7.4)  
[CVE-2026-15534](https://nvd.nist.gov/vuln/detail/CVE-2026-15534) | Yes | Yes | No | Yes | Medium (5.7)  
[CVE-2026-19487](https://nvd.nist.gov/vuln/detail/CVE-2026-19487) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-35189](https://nvd.nist.gov/vuln/detail/CVE-2026-35189) | Yes | Yes | No | Yes | Low (5.3)  
[CVE-2026-75805](https://nvd.nist.gov/vuln/detail/CVE-2026-75805) | Yes | Yes | No | Yes | Low (5.3)  
[CVE-2026-75806](https://nvd.nist.gov/vuln/detail/CVE-2026-75806) | Yes | Yes | No | Yes | Low (5.3)  
[CVE-2026-54872](https://nvd.nist.gov/vuln/detail/CVE-2026-54872) | Yes | Yes | No | Yes | Low (3.7)  
[CVE-2026-77696](https://nvd.nist.gov/vuln/detail/CVE-2026-77696) | Yes | Yes | No | Yes | Low (3.7)  
[CVE-2026-0799](https://nvd.nist.gov/vuln/detail/CVE-2026-0799) | Yes | Yes | No | Yes | Medium (0.0)  
  
### Announcement

**1.29.8-asm.8 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade). Cloud Service Mesh 1.29.8-asm.8 uses Envoy v1.37.9-dev.

This release resolves the security vulnerability listed in Security Bulletin [GCP-2026-067](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-067).

### Fixed

Patch 1.29.8-asm.8 contains the fix for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-18924](https://nvd.nist.gov/vuln/detail/CVE-2026-18924) | Yes | Yes | No | Yes | Medium (9.1)  
[CVE-2026-82474](https://nvd.nist.gov/vuln/detail/CVE-2026-82474) | Yes | Yes | No | Yes | Medium (8.5)  
[CVE-2026-82209](https://nvd.nist.gov/vuln/detail/CVE-2026-82209) | Yes | Yes | No | Yes | Medium (8.2)  
[CVE-2026-84782](https://nvd.nist.gov/vuln/detail/CVE-2026-84782) | Yes | Yes | No | Yes | High (8.2)  
[CVE-2026-96512](https://nvd.nist.gov/vuln/detail/CVE-2026-96512) | Yes | Yes | No | Yes | Medium (7.8)  
[CVE-2026-80230](https://nvd.nist.gov/vuln/detail/CVE-2026-80230) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-13608](https://nvd.nist.gov/vuln/detail/CVE-2026-13608) | Yes | Yes | No | Yes | Medium (7.4)  
[CVE-2026-15534](https://nvd.nist.gov/vuln/detail/CVE-2026-15534) | Yes | Yes | No | Yes | Medium (5.7)  
[CVE-2026-19487](https://nvd.nist.gov/vuln/detail/CVE-2026-19487) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-35189](https://nvd.nist.gov/vuln/detail/CVE-2026-35189) | Yes | Yes | No | Yes | Low (5.3)  
[CVE-2026-75805](https://nvd.nist.gov/vuln/detail/CVE-2026-75805) | Yes | Yes | No | Yes | Low (5.3)  
[CVE-2026-75806](https://nvd.nist.gov/vuln/detail/CVE-2026-75806) | Yes | Yes | No | Yes | Low (5.3)  
[CVE-2026-54872](https://nvd.nist.gov/vuln/detail/CVE-2026-54872) | Yes | Yes | No | Yes | Low (3.7)  
[CVE-2026-77696](https://nvd.nist.gov/vuln/detail/CVE-2026-77696) | Yes | Yes | No | Yes | Low (3.7)  
[CVE-2026-0799](https://nvd.nist.gov/vuln/detail/CVE-2026-0799) | Yes | Yes | No | Yes | Medium (0.0)  
  
### Announcement

**1.28.10-asm.49 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade). Cloud Service Mesh 1.28.10-asm.49 uses Envoy v1.36.10-dev.

### Fixed

Patch 1.28.10-asm.49 contains the fix for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-18924](https://nvd.nist.gov/vuln/detail/CVE-2026-18924) | Yes | Yes | No | Yes | Medium (9.1)  
[CVE-2026-82474](https://nvd.nist.gov/vuln/detail/CVE-2026-82474) | Yes | Yes | No | Yes | Medium (8.5)  
[CVE-2026-82209](https://nvd.nist.gov/vuln/detail/CVE-2026-82209) | Yes | Yes | No | Yes | Medium (8.2)  
[CVE-2026-84782](https://nvd.nist.gov/vuln/detail/CVE-2026-84782) | Yes | Yes | No | Yes | High (8.2)  
[CVE-2026-96512](https://nvd.nist.gov/vuln/detail/CVE-2026-96512) | Yes | Yes | No | Yes | Medium (7.8)  
[CVE-2026-80230](https://nvd.nist.gov/vuln/detail/CVE-2026-80230) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-13608](https://nvd.nist.gov/vuln/detail/CVE-2026-13608) | Yes | Yes | No | Yes | Medium (7.4)  
[CVE-2026-15534](https://nvd.nist.gov/vuln/detail/CVE-2026-15534) | Yes | Yes | No | Yes | Medium (5.7)  
[CVE-2026-19487](https://nvd.nist.gov/vuln/detail/CVE-2026-19487) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-35189](https://nvd.nist.gov/vuln/detail/CVE-2026-35189) | Yes | Yes | No | Yes | Low (5.3)  
[CVE-2026-75805](https://nvd.nist.gov/vuln/detail/CVE-2026-75805) | Yes | Yes | No | Yes | Low (5.3)  
[CVE-2026-75806](https://nvd.nist.gov/vuln/detail/CVE-2026-75806) | Yes | Yes | No | Yes | Low (5.3)  
[CVE-2026-54872](https://nvd.nist.gov/vuln/detail/CVE-2026-54872) | Yes | Yes | No | Yes | Low (3.7)  
[CVE-2026-77696](https://nvd.nist.gov/vuln/detail/CVE-2026-77696) | Yes | Yes | No | Yes | Low (3.7)  
[CVE-2026-81870](https://nvd.nist.gov/vuln/detail/CVE-2026-81870) | Yes | Yes | Yes | Yes | Low (2.0)  
[CVE-2026-0799](https://nvd.nist.gov/vuln/detail/CVE-2026-0799) | Yes | Yes | No | Yes | Medium (0.0)  
]]> September 28, 2026tag:google.com,2016:servicemesh-release-notes#September_28_20262026-09-28T00:00:00-07:001.27.x 

### Deprecated

Cloud Service Mesh support for the in-cluster `ISTIOD` control plane on Google Kubernetes Engine (GKE) on Google Cloud is deprecated as of September 28, 2026, and support will end on **March 1, 2028**. After March 1, 2028, in-cluster control plane components on GKE will not receive updates, security patches, or support from Google Cloud.

Cloud Service Mesh with the in-cluster `ISTIOD` control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms#off-gcp).

You must migrate your clusters to managed Cloud Service Mesh by March 1, 2028. review the [Supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed) to confirm feature compatibility, and follow the [migration guide](https://docs.cloud.google.com/service-mesh/docs/tutorials/migrate-in-cluster-to-managed-on-new-cluster) to transition to managed Cloud Service Mesh with the `TRAFFIC_DIRECTOR` control plane.

For more details on the deprecation schedule, see [Deprecations](https://docs.cloud.google.com/service-mesh/deprecations/).

**Managed Cloud Service Mesh**

### Deprecated

Cloud Service Mesh support for the managed `ISTIOD` control plane on Google Kubernetes Engine (GKE) on Google Cloud is deprecated as of September 28, 2026, and support will end on **March 1, 2028**. After March 1, 2028, managed `ISTIOD` control plane components on GKE on Google Cloud will not receive updates, security patches, or support from Google Cloud, and workload sidecars on unmodernized clusters will fail and be unable to receive or send requests.

Google Cloud is transitioning managed Cloud Service Mesh with Istio APIs to the `TRAFFIC_DIRECTOR` control plane implementation using Istio APIs. As part of this transition, support will also end for any features that are incompatible with the `TRAFFIC_DIRECTOR` control plane.

To continue using managed Cloud Service Mesh on GKE, you must modernize your clusters by March 1, 2028:

  1. Confirm that you affected.
  2. Check your compatibility. Review the [Supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed) to confirm feature compatibility with the `TRAFFIC_DIRECTOR` control plane and [evaluate a fleet's compatibility for control plane modernization](https://docs.cloud.google.com/service-mesh/docs/migrate/eligibility).
  3. Plan your modernization following the [modernization guide](https://docs.cloud.google.com/service-mesh/docs/modernization).



For more details on the transition, see [Managed control plane](https://docs.cloud.google.com/service-mesh/docs/managed-control-plane-overview) documentation and monitor the [release notes](https://docs.cloud.google.com/service-mesh/docs/release-notes) for ongoing updates.

]]> September 23, 2026tag:google.com,2016:servicemesh-release-notes#September_23_20262026-09-23T00:00:00-07:001.27.x 

### Announcement

**1.30.4-asm.14 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh 1.30.4-asm.14 uses Envoy v1.38.5-dev.

### Fixed

Patch 1.30.4-asm.14 contains the fix for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2022-31045](https://nvd.nist.gov/vuln/detail/CVE-2022-31045) | Yes | Yes | Yes | Yes | Medium (9.8)  
[CVE-2026-5450](https://nvd.nist.gov/vuln/detail/CVE-2026-5450) | No | No | Yes | No | Low (9.8)  
[CVE-2026-84304](https://nvd.nist.gov/vuln/detail/CVE-2026-84304) | Yes | Yes | Yes | Yes | High (8.7)  
[CVE-2026-84445](https://nvd.nist.gov/vuln/detail/CVE-2026-84445) | Yes | Yes | Yes | Yes | High (8.7)  
[CVE-2026-54371](https://nvd.nist.gov/vuln/detail/CVE-2026-54371) | Yes | Yes | No | Yes | Medium (8.4)  
[CVE-2019-14993](https://nvd.nist.gov/vuln/detail/CVE-2019-14993) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2021-39155](https://nvd.nist.gov/vuln/detail/CVE-2021-39155) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2021-39156](https://nvd.nist.gov/vuln/detail/CVE-2021-39156) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2022-23635](https://nvd.nist.gov/vuln/detail/CVE-2022-23635) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-5928](https://nvd.nist.gov/vuln/detail/CVE-2026-5928) | No | No | Yes | No | Low (7.5)  
[CVE-2026-59847](https://nvd.nist.gov/vuln/detail/CVE-2026-59847) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-59850](https://nvd.nist.gov/vuln/detail/CVE-2026-59850) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-59843](https://nvd.nist.gov/vuln/detail/CVE-2026-59843) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-84303](https://nvd.nist.gov/vuln/detail/CVE-2026-84303) | Yes | Yes | Yes | Yes | Medium (6.3)  
[CVE-2026-13757](https://nvd.nist.gov/vuln/detail/CVE-2026-13757) | Yes | Yes | No | Yes | Medium (6.2)  
[CVE-2026-18938](https://nvd.nist.gov/vuln/detail/CVE-2026-18938) | Yes | Yes | No | Yes | Medium (6.2)  
[CVE-2024-2236](https://nvd.nist.gov/vuln/detail/CVE-2024-2236) | Yes | Yes | No | Yes | Low (5.9)  
[CVE-2026-59845](https://nvd.nist.gov/vuln/detail/CVE-2026-59845) | Yes | Yes | No | Yes | Medium (5.9)  
[CVE-2026-27171](https://nvd.nist.gov/vuln/detail/CVE-2026-27171) | Yes | Yes | No | Yes | Low (5.5)  
[CVE-2026-13595](https://nvd.nist.gov/vuln/detail/CVE-2026-13595) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-59848](https://nvd.nist.gov/vuln/detail/CVE-2026-59848) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2025-6141](https://nvd.nist.gov/vuln/detail/CVE-2025-6141) | Yes | Yes | No | Yes | Low (4.8)  
[CVE-2026-27456](https://nvd.nist.gov/vuln/detail/CVE-2026-27456) | Yes | Yes | No | Yes | Medium (4.7)  
[CVE-2025-5278](https://nvd.nist.gov/vuln/detail/CVE-2025-5278) | Yes | Yes | No | Yes | Low (4.4)  
[CVE-2026-59846](https://nvd.nist.gov/vuln/detail/CVE-2026-59846) | Yes | Yes | No | Yes | Medium (3.9)  
[CVE-2026-19499](https://nvd.nist.gov/vuln/detail/CVE-2026-19499) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-19542](https://nvd.nist.gov/vuln/detail/CVE-2026-19542) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-41990](https://nvd.nist.gov/vuln/detail/CVE-2026-41990) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-42250](https://nvd.nist.gov/vuln/detail/CVE-2026-42250) | Yes | Yes | No | Yes | Low (0.0)  
[CVE-2026-53612](https://nvd.nist.gov/vuln/detail/CVE-2026-53612) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-53613](https://nvd.nist.gov/vuln/detail/CVE-2026-53613) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-53614](https://nvd.nist.gov/vuln/detail/CVE-2026-53614) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-53615](https://nvd.nist.gov/vuln/detail/CVE-2026-53615) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-53910](https://nvd.nist.gov/vuln/detail/CVE-2026-53910) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-57062](https://nvd.nist.gov/vuln/detail/CVE-2026-57062) | Yes | Yes | No | Yes | Low (0.0)  
[CVE-2026-6368](https://nvd.nist.gov/vuln/detail/CVE-2026-6368) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-6791](https://nvd.nist.gov/vuln/detail/CVE-2026-6791) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-77117](https://nvd.nist.gov/vuln/detail/CVE-2026-77117) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-80489](https://nvd.nist.gov/vuln/detail/CVE-2026-80489) | Yes | Yes | No | Yes | Medium (0.0)  
  
### Announcement

**1.29.7-asm.18 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh 1.29.7-asm.18 uses Envoy v1.37.6.

### Fixed

Patch 1.29.7-asm.18 contains the fix for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2022-31045](https://nvd.nist.gov/vuln/detail/CVE-2022-31045) | No | Yes | Yes | Yes | Medium (9.8)  
[CVE-2026-11856](https://nvd.nist.gov/vuln/detail/CVE-2026-11856) | No | Yes | No | Yes | Medium (9.8)  
[CVE-2026-5450](https://nvd.nist.gov/vuln/detail/CVE-2026-5450) | No | No | Yes | No | Low (9.8)  
[CVE-2026-57433](https://nvd.nist.gov/vuln/detail/CVE-2026-57433) | No | Yes | No | Yes | Medium (9.8)  
[CVE-2026-12087](https://nvd.nist.gov/vuln/detail/CVE-2026-12087) | No | Yes | No | Yes | Medium (9.1)  
[CVE-2026-13221](https://nvd.nist.gov/vuln/detail/CVE-2026-13221) | No | Yes | No | Yes | Medium (9.1)  
[CVE-2026-75803](https://nvd.nist.gov/vuln/detail/CVE-2026-75803) | No | Yes | No | Yes | Low (9.1)  
[CVE-2026-84304](https://nvd.nist.gov/vuln/detail/CVE-2026-84304) | No | Yes | Yes | Yes | High (8.7)  
[CVE-2026-84445](https://nvd.nist.gov/vuln/detail/CVE-2026-84445) | No | Yes | Yes | Yes | High (8.7)  
[CVE-2026-54371](https://nvd.nist.gov/vuln/detail/CVE-2026-54371) | No | Yes | No | Yes | Medium (8.4)  
[CVE-2026-57432](https://nvd.nist.gov/vuln/detail/CVE-2026-57432) | No | Yes | No | Yes | Medium (8.4)  
[CVE-2019-14993](https://nvd.nist.gov/vuln/detail/CVE-2019-14993) | No | Yes | Yes | Yes | High (7.5)  
[CVE-2021-39155](https://nvd.nist.gov/vuln/detail/CVE-2021-39155) | No | Yes | Yes | Yes | High (7.5)  
[CVE-2021-39156](https://nvd.nist.gov/vuln/detail/CVE-2021-39156) | No | Yes | Yes | Yes | High (7.5)  
[CVE-2022-23635](https://nvd.nist.gov/vuln/detail/CVE-2022-23635) | No | Yes | Yes | Yes | High (7.5)  
[CVE-2026-42151](https://nvd.nist.gov/vuln/detail/CVE-2026-42151) | No | Yes | No | No | High (7.5)  
[CVE-2026-42154](https://nvd.nist.gov/vuln/detail/CVE-2026-42154) | No | Yes | No | No | High (7.5)  
[CVE-2026-48959](https://nvd.nist.gov/vuln/detail/CVE-2026-48959) | No | Yes | No | Yes | Medium (7.5)  
[CVE-2026-54874](https://nvd.nist.gov/vuln/detail/CVE-2026-54874) | No | Yes | No | Yes | Low (7.5)  
[CVE-2026-5928](https://nvd.nist.gov/vuln/detail/CVE-2026-5928) | No | No | Yes | No | Low (7.5)  
[CVE-2026-59847](https://nvd.nist.gov/vuln/detail/CVE-2026-59847) | No | Yes | No | Yes | Medium (7.5)  
[CVE-2026-59850](https://nvd.nist.gov/vuln/detail/CVE-2026-59850) | No | Yes | No | Yes | Medium (7.5)  
[CVE-2026-63072](https://nvd.nist.gov/vuln/detail/CVE-2026-63072) | No | Yes | No | Yes | Medium (7.5)  
[CVE-2026-63076](https://nvd.nist.gov/vuln/detail/CVE-2026-63076) | No | Yes | No | Yes | Medium (7.5)  
[CVE-2026-8932](https://nvd.nist.gov/vuln/detail/CVE-2026-8932) | No | Yes | No | Yes | Low (7.5)  
[CVE-2026-9538](https://nvd.nist.gov/vuln/detail/CVE-2026-9538) | No | Yes | No | Yes | Medium (7.5)  
[CVE-2026-48962](https://nvd.nist.gov/vuln/detail/CVE-2026-48962) | No | Yes | No | Yes | Medium (7.3)  
[CVE-2026-7017](https://nvd.nist.gov/vuln/detail/CVE-2026-7017) | No | Yes | No | Yes | Medium (7.1)  
[CVE-2026-59843](https://nvd.nist.gov/vuln/detail/CVE-2026-59843) | No | Yes | No | Yes | Medium (6.5)  
[CVE-2026-84303](https://nvd.nist.gov/vuln/detail/CVE-2026-84303) | No | Yes | Yes | Yes | Medium (6.3)  
[CVE-2026-13757](https://nvd.nist.gov/vuln/detail/CVE-2026-13757) | No | Yes | No | Yes | Medium (6.2)  
[CVE-2026-18938](https://nvd.nist.gov/vuln/detail/CVE-2026-18938) | No | Yes | No | Yes | Medium (6.2)  
[CVE-2026-40179](https://nvd.nist.gov/vuln/detail/CVE-2026-40179) | No | Yes | No | No | Medium (6.1)  
[CVE-2026-44903](https://nvd.nist.gov/vuln/detail/CVE-2026-44903) | No | Yes | No | No | Medium (6.1)  
[CVE-2024-2236](https://nvd.nist.gov/vuln/detail/CVE-2024-2236) | No | Yes | No | Yes | Low (5.9)  
[CVE-2026-59845](https://nvd.nist.gov/vuln/detail/CVE-2026-59845) | No | Yes | No | Yes | Medium (5.9)  
[CVE-2026-63074](https://nvd.nist.gov/vuln/detail/CVE-2026-63074) | No | Yes | No | Yes | Low (5.9)  
[CVE-2025-15649](https://nvd.nist.gov/vuln/detail/CVE-2025-15649) | No | Yes | No | Yes | Medium (5.5)  
[CVE-2026-27171](https://nvd.nist.gov/vuln/detail/CVE-2026-27171) | No | Yes | No | Yes | Low (5.5)  
[CVE-2026-13595](https://nvd.nist.gov/vuln/detail/CVE-2026-13595) | No | Yes | No | Yes | Medium (5.3)  
[CVE-2026-59848](https://nvd.nist.gov/vuln/detail/CVE-2026-59848) | No | Yes | No | Yes | Medium (5.3)  
[CVE-2025-6141](https://nvd.nist.gov/vuln/detail/CVE-2025-6141) | No | Yes | No | Yes | Low (4.8)  
[CVE-2026-27456](https://nvd.nist.gov/vuln/detail/CVE-2026-27456) | No | Yes | No | Yes | Medium (4.7)  
[CVE-2025-5278](https://nvd.nist.gov/vuln/detail/CVE-2025-5278) | No | Yes | No | Yes | Low (4.4)  
[CVE-2026-59846](https://nvd.nist.gov/vuln/detail/CVE-2026-59846) | No | Yes | No | Yes | Medium (3.9)  
[CVE-2026-19499](https://nvd.nist.gov/vuln/detail/CVE-2026-19499) | No | Yes | No | Yes | Medium (0.0)  
[CVE-2026-19542](https://nvd.nist.gov/vuln/detail/CVE-2026-19542) | No | Yes | No | Yes | Medium (0.0)  
[CVE-2026-41990](https://nvd.nist.gov/vuln/detail/CVE-2026-41990) | No | Yes | No | Yes | Medium (0.0)  
[CVE-2026-42250](https://nvd.nist.gov/vuln/detail/CVE-2026-42250) | No | Yes | No | Yes | Low (0.0)  
[CVE-2026-53612](https://nvd.nist.gov/vuln/detail/CVE-2026-53612) | No | Yes | No | Yes | Medium (0.0)  
[CVE-2026-53613](https://nvd.nist.gov/vuln/detail/CVE-2026-53613) | No | Yes | No | Yes | Medium (0.0)  
[CVE-2026-53614](https://nvd.nist.gov/vuln/detail/CVE-2026-53614) | No | Yes | No | Yes | Medium (0.0)  
[CVE-2026-53615](https://nvd.nist.gov/vuln/detail/CVE-2026-53615) | No | Yes | No | Yes | Medium (0.0)  
[CVE-2026-53910](https://nvd.nist.gov/vuln/detail/CVE-2026-53910) | No | Yes | No | Yes | Medium (0.0)  
[CVE-2026-57062](https://nvd.nist.gov/vuln/detail/CVE-2026-57062) | No | Yes | No | Yes | Low (0.0)  
[CVE-2026-6368](https://nvd.nist.gov/vuln/detail/CVE-2026-6368) | No | Yes | No | Yes | Medium (0.0)  
[CVE-2026-6791](https://nvd.nist.gov/vuln/detail/CVE-2026-6791) | No | Yes | No | Yes | Medium (0.0)  
[CVE-2026-77117](https://nvd.nist.gov/vuln/detail/CVE-2026-77117) | No | Yes | No | Yes | Medium (0.0)  
[CVE-2026-80489](https://nvd.nist.gov/vuln/detail/CVE-2026-80489) | No | Yes | No | Yes | Medium (0.0)  
  
### Announcement

**1.28.10-asm.40 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade). Cloud Service Mesh 1.28.10-asm.40 uses Envoy v1.36.10-dev.

### Fixed

Patch 1.28.10-asm.40 contains the fix for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2022-31045](https://nvd.nist.gov/vuln/detail/CVE-2022-31045) | Yes | Yes | Yes | Yes | Medium (9.8)  
[CVE-2026-11856](https://nvd.nist.gov/vuln/detail/CVE-2026-11856) | Yes | Yes | No | Yes | Medium (9.8)  
[CVE-2026-5450](https://nvd.nist.gov/vuln/detail/CVE-2026-5450) | No | No | Yes | No | Low (9.8)  
[CVE-2026-57433](https://nvd.nist.gov/vuln/detail/CVE-2026-57433) | Yes | Yes | No | Yes | Medium (9.8)  
[CVE-2026-12087](https://nvd.nist.gov/vuln/detail/CVE-2026-12087) | Yes | Yes | No | Yes | Medium (9.1)  
[CVE-2026-13221](https://nvd.nist.gov/vuln/detail/CVE-2026-13221) | Yes | Yes | No | Yes | Medium (9.1)  
[CVE-2026-75803](https://nvd.nist.gov/vuln/detail/CVE-2026-75803) | Yes | Yes | No | Yes | Low (9.1)  
[CVE-2026-84304](https://nvd.nist.gov/vuln/detail/CVE-2026-84304) | Yes | Yes | Yes | Yes | High (8.7)  
[CVE-2026-84445](https://nvd.nist.gov/vuln/detail/CVE-2026-84445) | Yes | Yes | Yes | Yes | High (8.7)  
[CVE-2026-54371](https://nvd.nist.gov/vuln/detail/CVE-2026-54371) | Yes | Yes | No | Yes | Medium (8.4)  
[CVE-2026-57432](https://nvd.nist.gov/vuln/detail/CVE-2026-57432) | Yes | Yes | No | Yes | Medium (8.4)  
[CVE-2019-14993](https://nvd.nist.gov/vuln/detail/CVE-2019-14993) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2021-39155](https://nvd.nist.gov/vuln/detail/CVE-2021-39155) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2021-39156](https://nvd.nist.gov/vuln/detail/CVE-2021-39156) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2022-23635](https://nvd.nist.gov/vuln/detail/CVE-2022-23635) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-42151](https://nvd.nist.gov/vuln/detail/CVE-2026-42151) | No | Yes | No | No | High (7.5)  
[CVE-2026-42154](https://nvd.nist.gov/vuln/detail/CVE-2026-42154) | No | Yes | No | No | High (7.5)  
[CVE-2026-48959](https://nvd.nist.gov/vuln/detail/CVE-2026-48959) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-54874](https://nvd.nist.gov/vuln/detail/CVE-2026-54874) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-5928](https://nvd.nist.gov/vuln/detail/CVE-2026-5928) | No | No | Yes | No | Low (7.5)  
[CVE-2026-59847](https://nvd.nist.gov/vuln/detail/CVE-2026-59847) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-59850](https://nvd.nist.gov/vuln/detail/CVE-2026-59850) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-63072](https://nvd.nist.gov/vuln/detail/CVE-2026-63072) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-63076](https://nvd.nist.gov/vuln/detail/CVE-2026-63076) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-8932](https://nvd.nist.gov/vuln/detail/CVE-2026-8932) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-9538](https://nvd.nist.gov/vuln/detail/CVE-2026-9538) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-48962](https://nvd.nist.gov/vuln/detail/CVE-2026-48962) | Yes | Yes | No | Yes | Medium (7.3)  
[CVE-2026-7017](https://nvd.nist.gov/vuln/detail/CVE-2026-7017) | Yes | Yes | No | Yes | Medium (7.1)  
[CVE-2026-59843](https://nvd.nist.gov/vuln/detail/CVE-2026-59843) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-84303](https://nvd.nist.gov/vuln/detail/CVE-2026-84303) | Yes | Yes | Yes | Yes | Medium (6.3)  
[CVE-2026-13757](https://nvd.nist.gov/vuln/detail/CVE-2026-13757) | Yes | Yes | No | Yes | Medium (6.2)  
[CVE-2026-18938](https://nvd.nist.gov/vuln/detail/CVE-2026-18938) | Yes | Yes | No | Yes | Medium (6.2)  
[CVE-2026-40179](https://nvd.nist.gov/vuln/detail/CVE-2026-40179) | No | Yes | No | No | Medium (6.1)  
[CVE-2026-44903](https://nvd.nist.gov/vuln/detail/CVE-2026-44903) | No | Yes | No | No | Medium (6.1)  
[CVE-2024-2236](https://nvd.nist.gov/vuln/detail/CVE-2024-2236) | Yes | Yes | No | Yes | Low (5.9)  
[CVE-2026-59845](https://nvd.nist.gov/vuln/detail/CVE-2026-59845) | Yes | Yes | No | Yes | Medium (5.9)  
[CVE-2026-63074](https://nvd.nist.gov/vuln/detail/CVE-2026-63074) | Yes | Yes | No | Yes | Low (5.9)  
[CVE-2025-15649](https://nvd.nist.gov/vuln/detail/CVE-2025-15649) | Yes | Yes | No | Yes | Medium (5.5)  
[CVE-2026-27171](https://nvd.nist.gov/vuln/detail/CVE-2026-27171) | Yes | Yes | No | Yes | Low (5.5)  
[CVE-2026-13595](https://nvd.nist.gov/vuln/detail/CVE-2026-13595) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-59848](https://nvd.nist.gov/vuln/detail/CVE-2026-59848) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2025-6141](https://nvd.nist.gov/vuln/detail/CVE-2025-6141) | Yes | Yes | No | Yes | Low (4.8)  
[CVE-2026-27456](https://nvd.nist.gov/vuln/detail/CVE-2026-27456) | Yes | Yes | No | Yes | Medium (4.7)  
[CVE-2025-5278](https://nvd.nist.gov/vuln/detail/CVE-2025-5278) | Yes | Yes | No | Yes | Low (4.4)  
[CVE-2026-59846](https://nvd.nist.gov/vuln/detail/CVE-2026-59846) | Yes | Yes | No | Yes | Medium (3.9)  
[CVE-2026-19499](https://nvd.nist.gov/vuln/detail/CVE-2026-19499) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-19542](https://nvd.nist.gov/vuln/detail/CVE-2026-19542) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-41990](https://nvd.nist.gov/vuln/detail/CVE-2026-41990) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-42250](https://nvd.nist.gov/vuln/detail/CVE-2026-42250) | Yes | Yes | No | Yes | Low (0.0)  
[CVE-2026-53612](https://nvd.nist.gov/vuln/detail/CVE-2026-53612) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-53613](https://nvd.nist.gov/vuln/detail/CVE-2026-53613) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-53614](https://nvd.nist.gov/vuln/detail/CVE-2026-53614) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-53615](https://nvd.nist.gov/vuln/detail/CVE-2026-53615) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-53910](https://nvd.nist.gov/vuln/detail/CVE-2026-53910) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-57062](https://nvd.nist.gov/vuln/detail/CVE-2026-57062) | Yes | Yes | No | Yes | Low (0.0)  
[CVE-2026-6368](https://nvd.nist.gov/vuln/detail/CVE-2026-6368) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-6791](https://nvd.nist.gov/vuln/detail/CVE-2026-6791) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-77117](https://nvd.nist.gov/vuln/detail/CVE-2026-77117) | Yes | Yes | No | Yes | Medium (0.0)  
[CVE-2026-80489](https://nvd.nist.gov/vuln/detail/CVE-2026-80489) | Yes | Yes | No | Yes | Medium (0.0)  
[GHSA-gcjh-h69q-9w9g](https://github.com/advisories/GHSA-gcjh-h69q-9w9g) | No | Yes | No | No | Medium (0.0)  
]]> September 01, 2026tag:google.com,2016:servicemesh-release-notes#September_01_20262026-09-01T00:00:00-07:00Managed Cloud Service Mesh 

### Security

Managed Cloud Service Mesh will start using proxy version csm_mesh_proxy.20260819_RC00 for Gateway API on GKE clusters. This proxy version maps closest to Envoy version 1.37. This change is rolling out to all release channels and contains the fix for the managed Cloud Service Mesh security vulnerabilities listed in [GCP-2026-057](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-057).

]]> August 31, 2026tag:google.com,2016:servicemesh-release-notes#August_31_20262026-08-31T00:00:00-07:001.27.x 

### Announcement

**1.30.4-asm.1 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.30.4-asm.1 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.30.4](https://istio.io/latest/news/releases/1.30.x/announcing-1.30/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster).

Fixed an issue that caused incomplete telemetry in multicluster deployments for routes configured with TLS or PROXY traffic policies. Refer Istio 1.30 Telemetry Release Notes ([last bullet](https://istio.io/latest/news/releases/1.30.x/announcing-1.30/#telemetry)) for more details on the issue.

The following are not supported:

  * Failover Priority support for DNS clusters
  * `ENABLE_WILDCARD_HOST_SERVICE_ENTRIES_FOR_TLS`
  * Multiple `CUSTOM` external authorization providers per workload
  * The `DEBUG_ENDPOINT_AUTH_ALLOWED_NAMESPACES` flag



For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh version 1.30.4-asm.1 uses Envoy v1.38.4-dev.

### Announcement

In-cluster Cloud Service Mesh 1.27 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions).

]]> August 27, 2026tag:google.com,2016:servicemesh-release-notes#August_27_20262026-08-27T00:00:00-07:00Managed Cloud Service Mesh 

### Security

The following images are now rolling out for managed Cloud Service Mesh:

  * 1.21.6-asm.71 is rolling out to the rapid release channel.
  * 1.20.8-asm.119 is rolling out to the regular release channel.
  * 1.19.10-asm.109 is rolling out to the stable release channel.



These versions resolve the security vulnerabilities listed in Security Bulletin [GCP-2026-057](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-057).

]]> August 26, 2026tag:google.com,2016:servicemesh-release-notes#August_26_20262026-08-26T00:00:00-07:001.27.x 

### Announcement

**1.29.7-asm.2 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh 1.29.7-asm.2 uses Envoy v1.35.14.

This release resolves the security vulnerabilities listed in Security Bulletin [GCP-2026-057](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-057).

### Fixed

Patch 1.29.7-asm.2 contains the fix for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-5704](https://ubuntu.com/security/CVE-2026-5704) | Yes | Yes | No | Yes | Medium (5.5)  
  
### Announcement

**1.28.10-asm.24 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade). Cloud Service Mesh 1.28.10-asm.24 uses Envoy v1.36.10.

This release resolves the security vulnerabilities listed in Security Bulletin [GCP-2026-057](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-057).

### Fixed

Patch 1.28.10-asm.24 contains the fix for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-5704](https://ubuntu.com/security/CVE-2026-5704) | Yes | Yes | No | Yes | Medium (5.5)  
  
### Announcement

**1.27.9-asm.34 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh 1.27.9-asm.34 uses Envoy v1.35.14.

This release resolves the security vulnerabilities listed in Security Bulletin [GCP-2026-057](https://cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-057).

### Fixed

Patch 1.27.9-asm.34 contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-10536](https://ubuntu.com/security/CVE-2026-10536) | Yes | Yes | No | Yes | Low (9.8)  
[CVE-2026-42151](https://ubuntu.com/security/CVE-2026-42151) | No | No | No | Yes | High (7.5)  
[CVE-2026-42154](https://ubuntu.com/security/CVE-2026-42154) | No | No | No | Yes | High (7.5)  
[CVE-2026-40179](https://ubuntu.com/security/CVE-2026-40179) | No | No | No | Yes | Medium (6.1)  
[CVE-2026-44903](https://ubuntu.com/security/CVE-2026-44903) | No | No | No | Yes | Medium (6.1)  
[CVE-2026-5704](https://ubuntu.com/security/CVE-2026-5704) | Yes | Yes | No | Yes | Medium (5.5)  
**Managed Cloud Service Mesh**

### Feature

For clusters using the `TRAFFIC_DIRECTOR` implementation, configuring the trace sampling rate with `randomSamplingPercentage` with the `Telemetry` API is now supported in the Rapid release channel. For more information, see [Accessing Cloud Trace](https://docs.cloud.google.com/service-mesh/docs/observability/accessing-traces).

]]> August 20, 2026tag:google.com,2016:servicemesh-release-notes#August_20_20262026-08-20T00:00:00-07:00Managed Cloud Service Mesh 

### Feature

The guidance for using proxy image types (`default` and `distroless`) with Managed Cloud Service Mesh has been updated:

  * **Directly onboarded clusters** using the `TRAFFIC_DIRECTOR` implementation use `distroless` proxy images by default, and other image types are not supported.
  * **Migrated clusters** (migrated from `ISTIOD` to `TRAFFIC_DIRECTOR`) default to `default` images, but can opt in to `distroless` images via `MeshConfig` or the `sidecar.istio.io/proxyImageType: distroless` Pod annotation.



For more information, see [Distroless proxy images](https://docs.cloud.google.com/service-mesh/v1.29/docs/enable-optional-features-managed#distroless_proxy_image) and [Identify the proxy image type used in the cluster](https://docs.cloud.google.com/service-mesh/v1.29/docs/troubleshooting/troubleshoot-proxy#identify_proxy_image_type).

### Feature

The guidance for using proxy image types (`default` and `distroless`) with Managed Cloud Service Mesh has been updated:

  * **Directly onboarded clusters** using the `TRAFFIC_DIRECTOR` implementation use `distroless` proxy images by default, and other image types are not supported.
  * **Migrated clusters** (migrated from `ISTIOD` to `TRAFFIC_DIRECTOR`) default to `default` images, but can opt in to `distroless` images via `MeshConfig` or the `sidecar.istio.io/proxyImageType: distroless` Pod annotation.



For more information, see [Distroless proxy images](https://docs.cloud.google.com/service-mesh/docs/enable-optional-features-managed#distroless_proxy_image) and [Identify the proxy image type used in the cluster](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-proxy#identify_proxy_image_type).

]]> July 29, 2026tag:google.com,2016:servicemesh-release-notes#July_29_20262026-07-29T00:00:00-07:00Managed Cloud Service Mesh 

### Feature

For the clusters using `TRAFFIC_DIRECTOR` implementation, [IP auto-allocation](https://docs.cloud.google.com/service-mesh/v1.29/docs/operate-and-maintain/dns-proxy#ip_auto-allocation_for_serviceentry) with DNS Proxy is now supported in Rapid release channel.

### Feature

For the clusters using `TRAFFIC_DIRECTOR` implementation, [IP auto-allocation](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/dns-proxy#ip_auto-allocation_for_serviceentry) with DNS Proxy is now supported in Rapid release channel.

]]> July 24, 2026tag:google.com,2016:servicemesh-release-notes#July_24_20262026-07-24T00:00:00-07:00Managed Cloud Service Mesh 

### Feature

The [Envoy Compressor Filter](https://docs.cloud.google.com/service-mesh/v1.29/docs/data-plane-extensibility#typegoogleapiscomenvoyextensionsfiltershttpcompressorv3compressor) is now GA in the stable release channel.

### Feature

The [Envoy Compressor Filter](https://docs.cloud.google.com/service-mesh/docs/data-plane-extensibility#typegoogleapiscomenvoyextensionsfiltershttpcompressorv3compressor) is now GA in the stable release channel.

]]> July 21, 2026tag:google.com,2016:servicemesh-release-notes#July_21_20262026-07-21T00:00:00-07:00Managed Cloud Service Mesh 

### Feature

The [Envoy Lua Filter](https://docs.cloud.google.com/service-mesh/v1.29/docs/data-plane-extensibility#typegoogleapiscomenvoyextensionsfiltershttpluav3lua) is now available as a preview feature in the stable release channel.

### Feature

The [Envoy Lua Filter](https://docs.cloud.google.com/service-mesh/docs/data-plane-extensibility#typegoogleapiscomenvoyextensionsfiltershttpluav3lua) is now available as a preview feature in the stable release channel.

]]> July 15, 2026tag:google.com,2016:servicemesh-release-notes#July_15_20262026-07-15T00:00:00-07:001.27.x 

### Announcement

**1.29.5-asm.12 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade). Cloud Service Mesh 1.29.5-asm.12 uses Envoy v1.35.13.

### Announcement

**1.29.5-asm.12 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh 1.29.5-asm.12 uses Envoy v1.35.13.

### Fixed

Patch 1.29.5-asm.12 contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-46595](https://ubuntu.com/security/CVE-2026-46595) | Yes | Yes | Yes | Yes | Critical (10.0)  
[CVE-2026-8376](https://ubuntu.com/security/CVE-2026-8376) | Yes | Yes | No | Yes | Medium (9.8)  
[CVE-2026-8925](https://ubuntu.com/security/CVE-2026-8925) | Yes | Yes | No | Yes | Medium (9.8)  
[CVE-2026-39830](https://ubuntu.com/security/CVE-2026-39830) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-39831](https://ubuntu.com/security/CVE-2026-39831) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-39832](https://ubuntu.com/security/CVE-2026-39832) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-39833](https://ubuntu.com/security/CVE-2026-39833) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-39834](https://ubuntu.com/security/CVE-2026-39834) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-42496](https://ubuntu.com/security/CVE-2026-42496) | Yes | Yes | No | Yes | Medium (9.1)  
[CVE-2026-42508](https://ubuntu.com/security/CVE-2026-42508) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-8924](https://ubuntu.com/security/CVE-2026-8924) | Yes | Yes | No | Yes | Low (9.1)  
[CVE-2026-8927](https://ubuntu.com/security/CVE-2026-8927) | Yes | Yes | No | Yes | Medium (9.1)  
[CVE-2026-8286](https://ubuntu.com/security/CVE-2026-8286) | Yes | Yes | No | Yes | Low (8.1)  
[CVE-2025-69720](https://ubuntu.com/security/CVE-2025-69720) | Yes | Yes | No | Yes | Low (7.8)  
[CVE-2026-39822](https://ubuntu.com/security/CVE-2026-39822) | Yes | Yes | Yes | Yes | High (7.8)  
[CVE-2026-39829](https://ubuntu.com/security/CVE-2026-39829) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-41992](https://ubuntu.com/security/CVE-2026-41992) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-46597](https://ubuntu.com/security/CVE-2026-46597) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-9547](https://ubuntu.com/security/CVE-2026-9547) | Yes | Yes | No | Yes | Low (7.4)  
[CVE-2026-25680](https://ubuntu.com/security/CVE-2026-25680) | Yes | Yes | Yes | Yes | Medium (6.5)  
[CVE-2026-39827](https://ubuntu.com/security/CVE-2026-39827) | Yes | Yes | Yes | Yes | Medium (6.5)  
[CVE-2026-8458](https://ubuntu.com/security/CVE-2026-8458) | Yes | Yes | No | Yes | Low (6.5)  
[CVE-2026-39828](https://ubuntu.com/security/CVE-2026-39828) | Yes | Yes | Yes | Yes | Medium (6.3)  
[CVE-2026-5704](https://ubuntu.com/security/CVE-2026-5704) | Yes | Yes | No | Yes | Medium (5.5)  
[CVE-2026-58055](https://ubuntu.com/security/CVE-2026-58055) | Yes | Yes | No | Yes | Medium (5.4)  
[CVE-2026-39835](https://ubuntu.com/security/CVE-2026-39835) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-42505](https://ubuntu.com/security/CVE-2026-42505) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-46598](https://ubuntu.com/security/CVE-2026-46598) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-41991](https://ubuntu.com/security/CVE-2026-41991) | Yes | Yes | No | Yes | Medium (4.7)  
[CVE-2025-45582](https://ubuntu.com/security/CVE-2025-45582) | Yes | Yes | No | Yes | Medium (0.0)  
  
### Fixed

Patch 1.29.5-asm.12 contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-46595](https://ubuntu.com/security/CVE-2026-46595) | Yes | Yes | Yes | Yes | Critical (10.0)  
[CVE-2026-8376](https://ubuntu.com/security/CVE-2026-8376) | Yes | Yes | No | Yes | Medium (9.8)  
[CVE-2026-8925](https://ubuntu.com/security/CVE-2026-8925) | Yes | Yes | No | Yes | Medium (9.8)  
[CVE-2026-39830](https://ubuntu.com/security/CVE-2026-39830) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-39831](https://ubuntu.com/security/CVE-2026-39831) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-39832](https://ubuntu.com/security/CVE-2026-39832) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-39833](https://ubuntu.com/security/CVE-2026-39833) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-39834](https://ubuntu.com/security/CVE-2026-39834) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-42496](https://ubuntu.com/security/CVE-2026-42496) | Yes | Yes | No | Yes | Medium (9.1)  
[CVE-2026-42508](https://ubuntu.com/security/CVE-2026-42508) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-8924](https://ubuntu.com/security/CVE-2026-8924) | Yes | Yes | No | Yes | Low (9.1)  
[CVE-2026-8927](https://ubuntu.com/security/CVE-2026-8927) | Yes | Yes | No | Yes | Medium (9.1)  
[CVE-2026-8286](https://ubuntu.com/security/CVE-2026-8286) | Yes | Yes | No | Yes | Low (8.1)  
[CVE-2025-69720](https://ubuntu.com/security/CVE-2025-69720) | Yes | Yes | No | Yes | Low (7.8)  
[CVE-2026-39822](https://ubuntu.com/security/CVE-2026-39822) | Yes | Yes | Yes | Yes | High (7.8)  
[CVE-2026-39829](https://ubuntu.com/security/CVE-2026-39829) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-41992](https://ubuntu.com/security/CVE-2026-41992) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-46597](https://ubuntu.com/security/CVE-2026-46597) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-9547](https://ubuntu.com/security/CVE-2026-9547) | Yes | Yes | No | Yes | Low (7.4)  
[CVE-2026-25680](https://ubuntu.com/security/CVE-2026-25680) | Yes | Yes | Yes | Yes | Medium (6.5)  
[CVE-2026-39827](https://ubuntu.com/security/CVE-2026-39827) | Yes | Yes | Yes | Yes | Medium (6.5)  
[CVE-2026-8458](https://ubuntu.com/security/CVE-2026-8458) | Yes | Yes | No | Yes | Low (6.5)  
[CVE-2026-39828](https://ubuntu.com/security/CVE-2026-39828) | Yes | Yes | Yes | Yes | Medium (6.3)  
[CVE-2026-5704](https://ubuntu.com/security/CVE-2026-5704) | Yes | Yes | No | Yes | Medium (5.5)  
[CVE-2026-58055](https://ubuntu.com/security/CVE-2026-58055) | Yes | Yes | No | Yes | Medium (5.4)  
[CVE-2026-39835](https://ubuntu.com/security/CVE-2026-39835) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-42505](https://ubuntu.com/security/CVE-2026-42505) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-46598](https://ubuntu.com/security/CVE-2026-46598) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-41991](https://ubuntu.com/security/CVE-2026-41991) | Yes | Yes | No | Yes | Medium (4.7)  
[CVE-2025-45582](https://ubuntu.com/security/CVE-2025-45582) | Yes | Yes | No | Yes | Medium (0.0)  
  
### Announcement

**1.28.10-asm.4 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade). Cloud Service Mesh 1.28.10-asm.4 uses Envoy v1.36.9.

### Announcement

**1.28.10-asm.4 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade). Cloud Service Mesh 1.28.10-asm.4 uses Envoy v1.36.9.

### Fixed

Patch 1.28.10-asm.4 contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-8376](https://ubuntu.com/security/CVE-2026-8376) | Yes | Yes | No | Yes | Medium (9.8)  
[CVE-2026-8925](https://ubuntu.com/security/CVE-2026-8925) | Yes | Yes | No | Yes | Medium (9.8)  
[CVE-2026-42496](https://ubuntu.com/security/CVE-2026-42496) | Yes | Yes | No | Yes | Medium (9.1)  
[CVE-2026-8924](https://ubuntu.com/security/CVE-2026-8924) | Yes | Yes | No | Yes | Low (9.1)  
[CVE-2026-8927](https://ubuntu.com/security/CVE-2026-8927) | Yes | Yes | No | Yes | Medium (9.1)  
[CVE-2026-8286](https://ubuntu.com/security/CVE-2026-8286) | Yes | Yes | No | Yes | Low (8.1)  
[CVE-2025-69720](https://ubuntu.com/security/CVE-2025-69720) | Yes | Yes | No | Yes | Low (7.8)  
[CVE-2026-39822](https://ubuntu.com/security/CVE-2026-39822) | Yes | Yes | Yes | Yes | High (7.8)  
[CVE-2026-41992](https://ubuntu.com/security/CVE-2026-41992) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-42151](https://ubuntu.com/security/CVE-2026-42151) | No | No | No | Yes | High (7.5)  
[CVE-2026-42154](https://ubuntu.com/security/CVE-2026-42154) | No | No | No | Yes | High (7.5)  
[CVE-2026-9547](https://ubuntu.com/security/CVE-2026-9547) | Yes | Yes | No | Yes | Low (7.4)  
[CVE-2026-8458](https://ubuntu.com/security/CVE-2026-8458) | Yes | Yes | No | Yes | Low (6.5)  
[CVE-2026-40179](https://ubuntu.com/security/CVE-2026-40179) | No | No | No | Yes | Medium (6.1)  
[CVE-2026-44903](https://ubuntu.com/security/CVE-2026-44903) | No | No | No | Yes | Medium (6.1)  
[CVE-2026-5704](https://ubuntu.com/security/CVE-2026-5704) | Yes | Yes | No | Yes | Medium (5.5)  
[CVE-2026-58055](https://ubuntu.com/security/CVE-2026-58055) | Yes | Yes | No | Yes | Medium (5.4)  
[CVE-2026-42505](https://ubuntu.com/security/CVE-2026-42505) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-41991](https://ubuntu.com/security/CVE-2026-41991) | Yes | Yes | No | Yes | Medium (4.7)  
[CVE-2025-45582](https://ubuntu.com/security/CVE-2025-45582) | Yes | Yes | No | Yes | Medium (0.0)  
  
### Fixed

Patch 1.28.10-asm.4 contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-8376](https://ubuntu.com/security/CVE-2026-8376) | Yes | Yes | No | Yes | Medium (9.8)  
[CVE-2026-8925](https://ubuntu.com/security/CVE-2026-8925) | Yes | Yes | No | Yes | Medium (9.8)  
[CVE-2026-42496](https://ubuntu.com/security/CVE-2026-42496) | Yes | Yes | No | Yes | Medium (9.1)  
[CVE-2026-8924](https://ubuntu.com/security/CVE-2026-8924) | Yes | Yes | No | Yes | Low (9.1)  
[CVE-2026-8927](https://ubuntu.com/security/CVE-2026-8927) | Yes | Yes | No | Yes | Medium (9.1)  
[CVE-2026-8286](https://ubuntu.com/security/CVE-2026-8286) | Yes | Yes | No | Yes | Low (8.1)  
[CVE-2025-69720](https://ubuntu.com/security/CVE-2025-69720) | Yes | Yes | No | Yes | Low (7.8)  
[CVE-2026-39822](https://ubuntu.com/security/CVE-2026-39822) | Yes | Yes | Yes | Yes | High (7.8)  
[CVE-2026-41992](https://ubuntu.com/security/CVE-2026-41992) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-42151](https://ubuntu.com/security/CVE-2026-42151) | No | No | No | Yes | High (7.5)  
[CVE-2026-42154](https://ubuntu.com/security/CVE-2026-42154) | No | No | No | Yes | High (7.5)  
[CVE-2026-9547](https://ubuntu.com/security/CVE-2026-9547) | Yes | Yes | No | Yes | Low (7.4)  
[CVE-2026-8458](https://ubuntu.com/security/CVE-2026-8458) | Yes | Yes | No | Yes | Low (6.5)  
[CVE-2026-40179](https://ubuntu.com/security/CVE-2026-40179) | No | No | No | Yes | Medium (6.1)  
[CVE-2026-44903](https://ubuntu.com/security/CVE-2026-44903) | No | No | No | Yes | Medium (6.1)  
[CVE-2026-5704](https://ubuntu.com/security/CVE-2026-5704) | Yes | Yes | No | Yes | Medium (5.5)  
[CVE-2026-58055](https://ubuntu.com/security/CVE-2026-58055) | Yes | Yes | No | Yes | Medium (5.4)  
[CVE-2026-42505](https://ubuntu.com/security/CVE-2026-42505) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-41991](https://ubuntu.com/security/CVE-2026-41991) | Yes | Yes | No | Yes | Medium (4.7)  
[CVE-2025-45582](https://ubuntu.com/security/CVE-2025-45582) | Yes | Yes | No | Yes | Medium (0.0)  
  
### Announcement

**1.27.9-asm.15 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade). Cloud Service Mesh 1.27.9-asm.15 uses Envoy v1.35.13v.

### Announcement

**1.27.9-asm.15 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh 1.27.9-asm.15 uses Envoy v1.35.13v.

### Fixed

Patch 1.27.9-asm.15 contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-8376](https://ubuntu.com/security/CVE-2026-8376) | Yes | Yes | No | Yes | Medium (9.8)  
[CVE-2026-8925](https://ubuntu.com/security/CVE-2026-8925) | Yes | Yes | No | Yes | Medium (9.8)  
[CVE-2026-42496](https://ubuntu.com/security/CVE-2026-42496) | Yes | Yes | No | Yes | Medium (9.1)  
[CVE-2026-8924](https://ubuntu.com/security/CVE-2026-8924) | Yes | Yes | No | Yes | Low (9.1)  
[CVE-2026-8927](https://ubuntu.com/security/CVE-2026-8927) | Yes | Yes | No | Yes | Medium (9.1)  
[CVE-2026-8286](https://ubuntu.com/security/CVE-2026-8286) | Yes | Yes | No | Yes | Low (8.1)  
[CVE-2025-69720](https://ubuntu.com/security/CVE-2025-69720) | Yes | Yes | No | Yes | Low (7.8)  
[CVE-2026-39822](https://ubuntu.com/security/CVE-2026-39822) | Yes | Yes | Yes | Yes | High (7.8)  
[CVE-2026-41992](https://ubuntu.com/security/CVE-2026-41992) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-9547](https://ubuntu.com/security/CVE-2026-9547) | Yes | Yes | No | Yes | Low (7.4)  
[CVE-2026-8458](https://ubuntu.com/security/CVE-2026-8458) | Yes | Yes | No | Yes | Low (6.5)  
[CVE-2026-5704](https://ubuntu.com/security/CVE-2026-5704) | Yes | Yes | No | Yes | Medium (5.5)  
[CVE-2026-58055](https://ubuntu.com/security/CVE-2026-58055) | Yes | Yes | No | Yes | Medium (5.4)  
[CVE-2026-42505](https://ubuntu.com/security/CVE-2026-42505) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-41991](https://ubuntu.com/security/CVE-2026-41991) | Yes | Yes | No | Yes | Medium (4.7)  
[CVE-2025-45582](https://ubuntu.com/security/CVE-2025-45582) | Yes | Yes | No | Yes | Medium (0.0)  
  
### Fixed

Patch 1.27.9-asm.15 contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-8376](https://ubuntu.com/security/CVE-2026-8376) | Yes | Yes | No | Yes | Medium (9.8)  
[CVE-2026-8925](https://ubuntu.com/security/CVE-2026-8925) | Yes | Yes | No | Yes | Medium (9.8)  
[CVE-2026-42496](https://ubuntu.com/security/CVE-2026-42496) | Yes | Yes | No | Yes | Medium (9.1)  
[CVE-2026-8924](https://ubuntu.com/security/CVE-2026-8924) | Yes | Yes | No | Yes | Low (9.1)  
[CVE-2026-8927](https://ubuntu.com/security/CVE-2026-8927) | Yes | Yes | No | Yes | Medium (9.1)  
[CVE-2026-8286](https://ubuntu.com/security/CVE-2026-8286) | Yes | Yes | No | Yes | Low (8.1)  
[CVE-2025-69720](https://ubuntu.com/security/CVE-2025-69720) | Yes | Yes | No | Yes | Low (7.8)  
[CVE-2026-39822](https://ubuntu.com/security/CVE-2026-39822) | Yes | Yes | Yes | Yes | High (7.8)  
[CVE-2026-41992](https://ubuntu.com/security/CVE-2026-41992) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-9547](https://ubuntu.com/security/CVE-2026-9547) | Yes | Yes | No | Yes | Low (7.4)  
[CVE-2026-8458](https://ubuntu.com/security/CVE-2026-8458) | Yes | Yes | No | Yes | Low (6.5)  
[CVE-2026-5704](https://ubuntu.com/security/CVE-2026-5704) | Yes | Yes | No | Yes | Medium (5.5)  
[CVE-2026-58055](https://ubuntu.com/security/CVE-2026-58055) | Yes | Yes | No | Yes | Medium (5.4)  
[CVE-2026-42505](https://ubuntu.com/security/CVE-2026-42505) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-41991](https://ubuntu.com/security/CVE-2026-41991) | Yes | Yes | No | Yes | Medium (4.7)  
[CVE-2025-45582](https://ubuntu.com/security/CVE-2025-45582) | Yes | Yes | No | Yes | Medium (0.0)  
]]> July 06, 2026tag:google.com,2016:servicemesh-release-notes#July_06_20262026-07-06T00:00:00-07:00Managed Cloud Service Mesh 

### Feature

The [Envoy Compressor Filter](https://docs.cloud.google.com/service-mesh/v1.29/docs/data-plane-extensibility#typegoogleapiscomenvoyextensionsfiltershttpcompressorv3compressor) is now GA in the regular release channel.

### Feature

The [Envoy Compressor Filter](https://docs.cloud.google.com/service-mesh/docs/data-plane-extensibility#typegoogleapiscomenvoyextensionsfiltershttpcompressorv3compressor) is now GA in the regular release channel.

### Feature

The [Envoy Lua Filter](https://docs.cloud.google.com/service-mesh/v1.29/docs/data-plane-extensibility#typegoogleapiscomenvoyextensionsfiltershttpluav3lua) is now available as a preview feature in the regular release channel.

### Feature

The [Envoy Lua Filter](https://docs.cloud.google.com/service-mesh/docs/data-plane-extensibility#typegoogleapiscomenvoyextensionsfiltershttpluav3lua) is now available as a preview feature in the regular release channel.

]]> June 29, 2026tag:google.com,2016:servicemesh-release-notes#June_29_20262026-06-29T00:00:00-07:001.27.x 

### Security

**1.29.5-asm.5 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2026-045](https://docs.cloud.google.com/service-mesh/v1.29/docs/security-bulletins#gcp-2026-045).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade). Cloud Service Mesh 1.29.5-asm.5 uses Envoy v1.37.5.

### Security

**1.29.5-asm.5 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2026-045](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-045).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh 1.29.5-asm.5 uses Envoy v1.37.5.

### Security

**1.28.9-asm.4 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2026-045](https://docs.cloud.google.com/service-mesh/v1.29/docs/security-bulletins#gcp-2026-045).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade). Cloud Service Mesh 1.28.9-asm.4 uses Envoy v1.36.9.

### Security

**1.28.9-asm.4 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2026-045](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-045).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade). Cloud Service Mesh 1.28.9-asm.4 uses Envoy v1.36.9.

### Security

**1.27.9-asm.9 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2026-045](https://docs.cloud.google.com/service-mesh/v1.29/docs/security-bulletins#gcp-2026-045).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade). Cloud Service Mesh 1.27.9-asm.9 uses Envoy v1.35.13.

### Security

**1.27.9-asm.9 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2026-045](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-045).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade). Cloud Service Mesh 1.27.9-asm.9 uses Envoy v1.35.13.

**Managed Cloud Service Mesh**

### Security

Proxy version csm_mesh_proxy.csm_mesh_proxy.20260624e_RC01 for Gateway API on GKE clusters is rolling out to all Managed Cloud Service Mesh release channels over the next week.

This patch release contains the fixes for the security vulnerabilities listed in [GCP-2026-040](https://docs.cloud.google.com/service-mesh/v1.29/docs/security-bulletins#gcp-2026-040).

### Security

Proxy version csm_mesh_proxy.csm_mesh_proxy.20260624e_RC01 for Gateway API on GKE clusters is rolling out to all Managed Cloud Service Mesh release channels over the next week.

This patch release contains the fixes for the security vulnerabilities listed in [GCP-2026-040](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-040).

]]> June 23, 2026tag:google.com,2016:servicemesh-release-notes#June_23_20262026-06-23T00:00:00-07:001.27.x 

### Security

**1.29.5-asm.3 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2026-040](https://docs.cloud.google.com/service-mesh/v1.29/docs/security-bulletins#gcp-2026-040).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade). Cloud Service Mesh 1.29.5-asm.3 uses Envoy v1.37.5-dev.

### Security

**1.29.5-asm.3 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2026-040](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-040).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh 1.29.5-asm.3 uses Envoy v1.37.5-dev.

### Fixed

This patch release also contain the fixes for the following CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
CVE-2026-34182 | Yes | Yes | No | Yes | Medium (9.1)  
CVE-2026-45447 | Yes | Yes | No | Yes | High (8.8)  
CVE-2026-7383 | Yes | Yes | No | Yes | Low (8.1)  
CVE-2026-34180 | Yes | Yes | No | Yes | Low (7.5)  
CVE-2026-45445 | Yes | Yes | No | Yes | Medium (7.5)  
CVE-2026-9076 | Yes | Yes | No | Yes | Low (7.5)  
CVE-2026-42766 | Yes | Yes | No | Yes | Low (5.9)  
CVE-2026-42767 | Yes | Yes | No | Yes | Low (5.9)  
CVE-2026-34743 | Yes | Yes | No | Yes | Low (5.3)  
CVE-2026-45446 | Yes | Yes | No | Yes | Low (4.8)  
CVE-2026-42770 | Yes | Yes | No | Yes | Low (3.7)  
CVE-2026-40226 | Yes | Yes | No | Yes | Medium (0.0)  
  
### Fixed

This patch release also contain the fixes for the following CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
CVE-2026-34182 | Yes | Yes | No | Yes | Medium (9.1)  
CVE-2026-45447 | Yes | Yes | No | Yes | High (8.8)  
CVE-2026-7383 | Yes | Yes | No | Yes | Low (8.1)  
CVE-2026-34180 | Yes | Yes | No | Yes | Low (7.5)  
CVE-2026-45445 | Yes | Yes | No | Yes | Medium (7.5)  
CVE-2026-9076 | Yes | Yes | No | Yes | Low (7.5)  
CVE-2026-42766 | Yes | Yes | No | Yes | Low (5.9)  
CVE-2026-42767 | Yes | Yes | No | Yes | Low (5.9)  
CVE-2026-34743 | Yes | Yes | No | Yes | Low (5.3)  
CVE-2026-45446 | Yes | Yes | No | Yes | Low (4.8)  
CVE-2026-42770 | Yes | Yes | No | Yes | Low (3.7)  
CVE-2026-40226 | Yes | Yes | No | Yes | Medium (0.0)  
  
### Security

**1.28.9-asm.2 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2026-040](https://docs.cloud.google.com/service-mesh/v1.29/docs/security-bulletins#gcp-2026-040).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade). Cloud Service Mesh 1.28.9-asm.2 uses Envoy v1.36.9-dev.

### Security

**1.28.9-asm.2 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2026-040](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-040).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade). Cloud Service Mesh 1.28.9-asm.2 uses Envoy v1.36.9-dev.

### Fixed

This patch release also contain the fixes for the following CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
CVE-2026-34182 | Yes | Yes | No | Yes | Medium (9.1)  
CVE-2026-45447 | Yes | Yes | No | Yes | High (8.8)  
CVE-2026-7383 | Yes | Yes | No | Yes | Low (8.1)  
CVE-2026-34180 | Yes | Yes | No | Yes | Low (7.5)  
CVE-2026-45445 | Yes | Yes | No | Yes | Medium (7.5)  
CVE-2026-9076 | Yes | Yes | No | Yes | Low (7.5)  
CVE-2026-42766 | Yes | Yes | No | Yes | Low (5.9)  
CVE-2026-42767 | Yes | Yes | No | Yes | Low (5.9)  
CVE-2026-34743 | Yes | Yes | No | Yes | Low (5.3)  
CVE-2026-45446 | Yes | Yes | No | Yes | Low (4.8)  
CVE-2026-42770 | Yes | Yes | No | Yes | Low (3.7)  
CVE-2026-40226 | Yes | Yes | No | Yes | Medium (0.0)  
  
### Fixed

This patch release also contain the fixes for the following CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
CVE-2026-34182 | Yes | Yes | No | Yes | Medium (9.1)  
CVE-2026-45447 | Yes | Yes | No | Yes | High (8.8)  
CVE-2026-7383 | Yes | Yes | No | Yes | Low (8.1)  
CVE-2026-34180 | Yes | Yes | No | Yes | Low (7.5)  
CVE-2026-45445 | Yes | Yes | No | Yes | Medium (7.5)  
CVE-2026-9076 | Yes | Yes | No | Yes | Low (7.5)  
CVE-2026-42766 | Yes | Yes | No | Yes | Low (5.9)  
CVE-2026-42767 | Yes | Yes | No | Yes | Low (5.9)  
CVE-2026-34743 | Yes | Yes | No | Yes | Low (5.3)  
CVE-2026-45446 | Yes | Yes | No | Yes | Low (4.8)  
CVE-2026-42770 | Yes | Yes | No | Yes | Low (3.7)  
CVE-2026-40226 | Yes | Yes | No | Yes | Medium (0.0)  
  
### Security

**1.27.9-asm.8 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2026-040](https://docs.cloud.google.com/service-mesh/v1.29/docs/security-bulletins#gcp-2026-040).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade). Cloud Service Mesh 1.27.9-asm.8 uses Envoy v1.35.13-dev.

### Security

**1.27.9-asm.8 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2026-040](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-040).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade). Cloud Service Mesh 1.27.9-asm.8 uses Envoy v1.35.13-dev.

### Fixed

This patch release also contain the fixes for the following CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
CVE-2026-34182 | Yes | Yes | No | Yes | Medium (9.1)  
CVE-2026-45447 | Yes | Yes | No | Yes | High (8.8)  
CVE-2026-7383 | Yes | Yes | No | Yes | Low (8.1)  
CVE-2026-34180 | Yes | Yes | No | Yes | Low (7.5)  
CVE-2026-45445 | Yes | Yes | No | Yes | Medium (7.5)  
CVE-2026-9076 | Yes | Yes | No | Yes | Low (7.5)  
CVE-2026-42766 | Yes | Yes | No | Yes | Low (5.9)  
CVE-2026-42767 | Yes | Yes | No | Yes | Low (5.9)  
CVE-2026-34743 | Yes | Yes | No | Yes | Low (5.3)  
CVE-2026-45446 | Yes | Yes | No | Yes | Low (4.8)  
CVE-2026-42770 | Yes | Yes | No | Yes | Low (3.7)  
CVE-2026-40226 | Yes | Yes | No | Yes | Medium (0.0)  
  
### Fixed

This patch release also contain the fixes for the following CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
CVE-2026-34182 | Yes | Yes | No | Yes | Medium (9.1)  
CVE-2026-45447 | Yes | Yes | No | Yes | High (8.8)  
CVE-2026-7383 | Yes | Yes | No | Yes | Low (8.1)  
CVE-2026-34180 | Yes | Yes | No | Yes | Low (7.5)  
CVE-2026-45445 | Yes | Yes | No | Yes | Medium (7.5)  
CVE-2026-9076 | Yes | Yes | No | Yes | Low (7.5)  
CVE-2026-42766 | Yes | Yes | No | Yes | Low (5.9)  
CVE-2026-42767 | Yes | Yes | No | Yes | Low (5.9)  
CVE-2026-34743 | Yes | Yes | No | Yes | Low (5.3)  
CVE-2026-45446 | Yes | Yes | No | Yes | Low (4.8)  
CVE-2026-42770 | Yes | Yes | No | Yes | Low (3.7)  
CVE-2026-40226 | Yes | Yes | No | Yes | Medium (0.0)  
**Managed Cloud Service Mesh**

### Security

The following images are now rolling out for managed Cloud Service Mesh:

  * Sidecar version 1.21.6-asm.38, is rolling out to the rapid release channel.
  * Sidecar version 1.20.8-asm.88 is rolling out to the regular release channel.
  * Sidecar version 1.19.10-asm.78 is rolling out to the stable release channel.



These patch releases contain the fix for the vulnerability listed in [GCP-2026-040](https://docs.cloud.google.com/service-mesh/v1.29/docs/security-bulletins#gcp-2026-040).

These rollouts will preempt those previously announced on June 12, 2026.

### Security

The following images are now rolling out for managed Cloud Service Mesh:

  * Sidecar version 1.21.6-asm.38, is rolling out to the rapid release channel.
  * Sidecar version 1.20.8-asm.88 is rolling out to the regular release channel.
  * Sidecar version 1.19.10-asm.78 is rolling out to the stable release channel.



These patch releases contain the fix for the vulnerability listed in [GCP-2026-040](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-040).

These rollouts will preempt those previously announced on June 12, 2026.

]]> June 22, 2026tag:google.com,2016:servicemesh-release-notes#June_22_20262026-06-22T00:00:00-07:00Managed Cloud Service Mesh 

### Feature

The [Envoy Lua Filter](https://docs.cloud.google.com/service-mesh/v1.29/docs/data-plane-extensibility#typegoogleapiscomenvoyextensionsfiltershttpluav3lua) is now available as a preview feature in the rapid release channel.

### Feature

The [Envoy Lua Filter](https://docs.cloud.google.com/service-mesh/docs/data-plane-extensibility#typegoogleapiscomenvoyextensionsfiltershttpluav3lua) is now available as a preview feature in the rapid release channel.

]]> June 15, 2026tag:google.com,2016:servicemesh-release-notes#June_15_20262026-06-15T00:00:00-07:00Managed Cloud Service Mesh 

### Feature

The [Envoy Compressor Filter](https://docs.cloud.google.com/service-mesh/v1.29/docs/data-plane-extensibility#typegoogleapiscomenvoyextensionsfiltershttpcompressorv3compressor) is now GA in the rapid release channel.

To ensure your `EnvoyFilter` compressor configuration is fully supported, see [Modernize EnvoyFilter compressor configurations](https://docs.cloud.google.com/service-mesh/v1.29/docs/migrate/modernize-envoyfilter-compressor).

### Feature

The [Envoy Compressor Filter](https://docs.cloud.google.com/service-mesh/docs/data-plane-extensibility#typegoogleapiscomenvoyextensionsfiltershttpcompressorv3compressor) is now GA in the rapid release channel.

To ensure your `EnvoyFilter` compressor configuration is fully supported, see [Modernize EnvoyFilter compressor configurations](https://docs.cloud.google.com/service-mesh/docs/migrate/modernize-envoyfilter-compressor).

]]> June 12, 2026tag:google.com,2016:servicemesh-release-notes#June_12_20262026-06-12T00:00:00-07:00Managed Cloud Service Mesh 

### Security

The following images are now rolling out for managed Cloud Service Mesh:

  * Sidecar version 1.21.6-asm.36, is rolling out to the rapid release channel.
  * Sidecar version 1.20.8-asm.86 is rolling out to the regular release channel.
  * Sidecar version 1.19.10-asm.76 is rolling out to the stable release channel.



These rollouts will preempt those previously announced on June 3, 2026.

These patch releases contain the fix for the vulnerability listed in [GCP-2026-035](https://docs.cloud.google.com/service-mesh/v1.29/docs/security-bulletins#gcp-2026-035)

### Security

The following images are now rolling out for managed Cloud Service Mesh:

  * Sidecar version 1.21.6-asm.36, is rolling out to the rapid release channel.
  * Sidecar version 1.20.8-asm.86 is rolling out to the regular release channel.
  * Sidecar version 1.19.10-asm.76 is rolling out to the stable release channel.



These rollouts will preempt those previously announced on June 3, 2026.

These patch releases contain the fix for the vulnerability listed in [GCP-2026-035](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-035)

### Security

Proxy version csm_mesh_proxy.20260423_RC03 for Gateway API on GKE clusters is rolling out to all Managed Cloud Service Mesh release channels over the next week.

### Security

Proxy version csm_mesh_proxy.20260423_RC03 for Gateway API on GKE clusters is rolling out to all Managed Cloud Service Mesh release channels over the next week.

]]> June 09, 2026tag:google.com,2016:servicemesh-release-notes#June_09_20262026-06-09T00:00:00-07:001.27.x 

### Announcement

**1.29.4-asm.0 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.29.4-asm.0 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.29.4](https://istio.io/latest/news/releases/1.29.x/announcing-1.29/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.29/docs/supported-features-in-cluster).

The following environment variables, labels, and annotations are not supported:

  * `PILOT_IGNORE_RESOURCES` and `PILOT_INCLUDE_RESOURCES`
  * `RetryIgnorePreviousHosts`
  * `omit_empty_values`
  * `PILOT_SPAWN_UPSTREAM_SPAN_FOR_GATEWAY`
  * `MAX_CONNECTIONS_PER_SOCKET_EVENT_LOOP` with the value 1
  * `PILOT_DNS_JITTER_DURATION`
  * `PILOT_DNS_JITTER_DURATION`
  * `ENABLE_NATIVE_SIDECARS` with the value true
  * `PILOT_IP_AUTOALLOCATE_IPV4_PREFIX` and `PILOT_IP_AUTOALLOCATE_IPV6_PREFIX`
  * `PILOT_DNS_CARES_UDP_MAX_QUERIES`
  * `ENABLE_WILDCARD_HOST_SERVICE_ENTRIES_FOR_TLS`
  * 'BLOCKED_CIDRS_IN_JWKS_URIS`
  * `ENABLE_DEBUG_ENDPOINT_AUTH`
  * `DISABLE_TRACK_REMAINING_CB_METRICS`
  * `gateway.istio.io/tls-cipher-suites`
  * `fileFlushMinSizeKB` and `fileFlushInterval` settings in ProxyConfig
  * `topology.istio.io/locality`
  * `statsCompression` ProxyConfig option
  * `proxy.istio.io/config` annotation for metric compression overrides



Istio's experimental feature to enable lazy subset creation of envoy statistics is not supported.

The formatter option within the `spec.tracing[].customTags` field of the Telemetry custom resource (telemetry.istio.io) is unsupported.

The `istiod_remote_cluster_sync_status` Prometheus gauge metric, exposed on the **Istiod control plane metrics endpoint** (port 15014 `/metrics`), is not supported.

The following are unsupported for proxyless gRPC clients:

  * Configuring the `LEAST_REQUEST` load balancing policy within the `spec.trafficPolicy.loadBalancer.simple` field of a **DestinationRule** custom resource (`networking.istio.io`)

  * Configuring the `http2MaxRequests` circuit breaker within the `spec.trafficPolicy.connectionPool.http.http2MaxRequests` field of a **DestinationRule** custom resource (`networking.istio.io`)




The `ENABLE_AUTO_SNI` flag is still supported to keep aligned with the legacy behavior.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade). Cloud Service Mesh version 1.29.4-asm.0 uses Envoy v1.37.4-dev.

### Announcement

**1.29.4-asm.0 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.29.4-asm.0 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.29.4](https://istio.io/latest/news/releases/1.29.x/announcing-1.29/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster).

The following environment variables, labels, and annotations are not supported:

  * `PILOT_IGNORE_RESOURCES` and `PILOT_INCLUDE_RESOURCES`
  * `RetryIgnorePreviousHosts`
  * `omit_empty_values`
  * `PILOT_SPAWN_UPSTREAM_SPAN_FOR_GATEWAY`
  * `MAX_CONNECTIONS_PER_SOCKET_EVENT_LOOP` with the value 1
  * `PILOT_DNS_JITTER_DURATION`
  * `PILOT_DNS_JITTER_DURATION`
  * `ENABLE_NATIVE_SIDECARS` with the value true
  * `PILOT_IP_AUTOALLOCATE_IPV4_PREFIX` and `PILOT_IP_AUTOALLOCATE_IPV6_PREFIX`
  * `PILOT_DNS_CARES_UDP_MAX_QUERIES`
  * `ENABLE_WILDCARD_HOST_SERVICE_ENTRIES_FOR_TLS`
  * 'BLOCKED_CIDRS_IN_JWKS_URIS`
  * `ENABLE_DEBUG_ENDPOINT_AUTH`
  * `DISABLE_TRACK_REMAINING_CB_METRICS`
  * `gateway.istio.io/tls-cipher-suites`
  * `fileFlushMinSizeKB` and `fileFlushInterval` settings in ProxyConfig
  * `topology.istio.io/locality`
  * `statsCompression` ProxyConfig option
  * `proxy.istio.io/config` annotation for metric compression overrides



Istio's experimental feature to enable lazy subset creation of envoy statistics is not supported.

The formatter option within the `spec.tracing[].customTags` field of the Telemetry custom resource (telemetry.istio.io) is unsupported.

The `istiod_remote_cluster_sync_status` Prometheus gauge metric, exposed on the **Istiod control plane metrics endpoint** (port 15014 `/metrics`), is not supported.

The following are unsupported for proxyless gRPC clients:

  * Configuring the `LEAST_REQUEST` load balancing policy within the `spec.trafficPolicy.loadBalancer.simple` field of a **DestinationRule** custom resource (`networking.istio.io`)

  * Configuring the `http2MaxRequests` circuit breaker within the `spec.trafficPolicy.connectionPool.http.http2MaxRequests` field of a **DestinationRule** custom resource (`networking.istio.io`)




The `ENABLE_AUTO_SNI` flag is still supported to keep aligned with the legacy behavior.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh version 1.29.4-asm.0 uses Envoy v1.37.4-dev.

**1.26.x**

### Announcement

In-cluster Cloud Service Mesh 1.26 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see [Supported versions](https://docs.cloud.google.com/service-mesh/v1.29/docs/supported-features-in-cluster#supported_versions).

### Announcement

In-cluster Cloud Service Mesh 1.26 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions).

]]> June 08, 2026tag:google.com,2016:servicemesh-release-notes#June_08_20262026-06-08T00:00:00-07:001.27.x 

### Security

**1.28.7-asm.4 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2026-035](https://docs.cloud.google.com/service-mesh/v1.29/docs/security-bulletins#gcp-2026-035).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade). Cloud Service Mesh 1.28.7-asm.4 uses Envoy v1.36.8-dev.

### Security

**1.28.7-asm.4 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2026-035](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-035).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh 1.28.7-asm.4 uses Envoy v1.36.8-dev.

### Security

**1.27.9-asm.5 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2026-035](https://docs.cloud.google.com/service-mesh/v1.29/docs/security-bulletins#gcp-2026-035).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade). Cloud Service Mesh 1.27.9-asm.5 uses Envoy v1.35.12-dev.

### Security

**1.27.9-asm.5 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2026-035](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-035).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade). Cloud Service Mesh 1.27.9-asm.5 uses Envoy v1.35.12-dev.

**1.26.x**

### Security

**1.26.8-asm.11 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2026-035](https://docs.cloud.google.com/service-mesh/v1.29/docs/security-bulletins#gcp-2026-035).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/upgrade/upgrade). Cloud Service Mesh 1.26.8-asm.11 uses Envoy v1.34.14.

### Security

**1.26.8-asm.11 is now available for in-cluster Cloud Service Mesh.**

This patch release contains the fix for the security vulnerability listed in [GCP-2026-035](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-035).

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/upgrade/upgrade). Cloud Service Mesh 1.26.8-asm.11 uses Envoy v1.34.14.

**Managed Cloud Service Mesh**

### Announcement

The rollouts previously announced on June 3, 2026 have been stopped. The following release will supersede them and include those patches and the fix for the vulnerability listed in [GCP-2026-035](https://docs.cloud.google.com/service-mesh/v1.29/docs/security-bulletins#gcp-2026-035).

### Announcement

The rollouts previously announced on June 3, 2026 have been stopped. The following release will supersede them and include those patches and the fix for the vulnerability listed in [GCP-2026-035](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-035).

]]> June 03, 2026tag:google.com,2016:servicemesh-release-notes#June_03_20262026-06-03T00:00:00-07:001.27.x 

### Announcement

**1.28.7-asm.3 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade). Cloud Service Mesh 1.28.7-asm.3 uses Envoy v1.36.7-dev.

### Announcement

**1.28.7-asm.3 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh 1.28.7-asm.3 uses Envoy v1.36.7-dev.

### Fixed

Patch 1.28.7-asm.3 contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-27143](https://ubuntu.com/security/CVE-2026-27143) | Yes | Yes | Yes | Yes | Critical (9.8)  
[CVE-2026-31789](https://ubuntu.com/security/CVE-2026-31789) | Yes | Yes | No | Yes | Low (9.8)  
[CVE-2026-27140](https://ubuntu.com/security/CVE-2026-27140) | Yes | Yes | Yes | Yes | High (8.8)  
[CVE-2026-28387](https://ubuntu.com/security/CVE-2026-28387) | Yes | Yes | No | Yes | Low (8.1)  
[CVE-2026-41413](https://ubuntu.com/security/CVE-2026-41413) | Yes | Yes | Yes | Yes | Medium (7.7)  
[CVE-2026-2219](https://ubuntu.com/security/CVE-2026-2219) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-27135](https://ubuntu.com/security/CVE-2026-27135) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-28388](https://ubuntu.com/security/CVE-2026-28388) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-28389](https://ubuntu.com/security/CVE-2026-28389) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-28390](https://ubuntu.com/security/CVE-2026-28390) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-29181](https://ubuntu.com/security/CVE-2026-29181) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-31790](https://ubuntu.com/security/CVE-2026-31790) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-32280](https://ubuntu.com/security/CVE-2026-32280) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-32281](https://ubuntu.com/security/CVE-2026-32281) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-32283](https://ubuntu.com/security/CVE-2026-32283) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-33811](https://ubuntu.com/security/CVE-2026-33811) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-33814](https://ubuntu.com/security/CVE-2026-33814) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-34986](https://ubuntu.com/security/CVE-2026-34986) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-39820](https://ubuntu.com/security/CVE-2026-39820) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-39836](https://ubuntu.com/security/CVE-2026-39836) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-4046](https://ubuntu.com/security/CVE-2026-4046) | No | No | Yes | No | High (7.5)  
[CVE-2026-42499](https://ubuntu.com/security/CVE-2026-42499) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-42501](https://ubuntu.com/security/CVE-2026-42501) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-4437](https://ubuntu.com/security/CVE-2026-4437) | No | No | Yes | No | High (7.5)  
[CVE-2026-5773](https://ubuntu.com/security/CVE-2026-5773) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-6276](https://ubuntu.com/security/CVE-2026-6276) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-27144](https://ubuntu.com/security/CVE-2026-27144) | Yes | Yes | Yes | Yes | High (7.1)  
[CVE-2026-39883](https://ubuntu.com/security/CVE-2026-39883) | Yes | Yes | Yes | Yes | High (7.0)  
[CVE-2026-4878](https://ubuntu.com/security/CVE-2026-4878) | Yes | Yes | No | Yes | Medium (7.0)  
[CVE-2026-5545](https://ubuntu.com/security/CVE-2026-5545) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-32282](https://ubuntu.com/security/CVE-2026-32282) | Yes | Yes | Yes | Yes | Medium (6.4)  
[CVE-2026-32289](https://ubuntu.com/security/CVE-2026-32289) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39823](https://ubuntu.com/security/CVE-2026-39823) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39826](https://ubuntu.com/security/CVE-2026-39826) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39817](https://ubuntu.com/security/CVE-2026-39817) | Yes | Yes | Yes | Yes | Medium (5.9)  
[CVE-2026-4873](https://ubuntu.com/security/CVE-2026-4873) | Yes | Yes | No | Yes | Low (5.9)  
[CVE-2026-6253](https://ubuntu.com/security/CVE-2026-6253) | Yes | Yes | No | Yes | Medium (5.9)  
[CVE-2026-32288](https://ubuntu.com/security/CVE-2026-32288) | Yes | Yes | Yes | Yes | Medium (5.5)  
[CVE-2026-39350](https://ubuntu.com/security/CVE-2026-39350) | Yes | Yes | Yes | Yes | Medium (5.4)  
[CVE-2026-4438](https://ubuntu.com/security/CVE-2026-4438) | No | No | Yes | No | Medium (5.4)  
[CVE-2026-39819](https://ubuntu.com/security/CVE-2026-39819) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-39825](https://ubuntu.com/security/CVE-2026-39825) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-6429](https://ubuntu.com/security/CVE-2026-6429) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-7168](https://ubuntu.com/security/CVE-2026-7168) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-35469](https://ubuntu.com/security/CVE-2026-35469) | No | Yes | No | Yes | High (0.0)  
[CVE-2026-5958](https://ubuntu.com/security/CVE-2026-5958) | Yes | Yes | No | Yes | Medium (0.0)  
  
### Fixed

Patch 1.28.7-asm.3 contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-27143](https://ubuntu.com/security/CVE-2026-27143) | Yes | Yes | Yes | Yes | Critical (9.8)  
[CVE-2026-31789](https://ubuntu.com/security/CVE-2026-31789) | Yes | Yes | No | Yes | Low (9.8)  
[CVE-2026-27140](https://ubuntu.com/security/CVE-2026-27140) | Yes | Yes | Yes | Yes | High (8.8)  
[CVE-2026-28387](https://ubuntu.com/security/CVE-2026-28387) | Yes | Yes | No | Yes | Low (8.1)  
[CVE-2026-41413](https://ubuntu.com/security/CVE-2026-41413) | Yes | Yes | Yes | Yes | Medium (7.7)  
[CVE-2026-2219](https://ubuntu.com/security/CVE-2026-2219) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-27135](https://ubuntu.com/security/CVE-2026-27135) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-28388](https://ubuntu.com/security/CVE-2026-28388) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-28389](https://ubuntu.com/security/CVE-2026-28389) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-28390](https://ubuntu.com/security/CVE-2026-28390) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-29181](https://ubuntu.com/security/CVE-2026-29181) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-31790](https://ubuntu.com/security/CVE-2026-31790) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-32280](https://ubuntu.com/security/CVE-2026-32280) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-32281](https://ubuntu.com/security/CVE-2026-32281) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-32283](https://ubuntu.com/security/CVE-2026-32283) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-33811](https://ubuntu.com/security/CVE-2026-33811) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-33814](https://ubuntu.com/security/CVE-2026-33814) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-34986](https://ubuntu.com/security/CVE-2026-34986) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-39820](https://ubuntu.com/security/CVE-2026-39820) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-39836](https://ubuntu.com/security/CVE-2026-39836) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-4046](https://ubuntu.com/security/CVE-2026-4046) | No | No | Yes | No | High (7.5)  
[CVE-2026-42499](https://ubuntu.com/security/CVE-2026-42499) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-42501](https://ubuntu.com/security/CVE-2026-42501) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-4437](https://ubuntu.com/security/CVE-2026-4437) | No | No | Yes | No | High (7.5)  
[CVE-2026-5773](https://ubuntu.com/security/CVE-2026-5773) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-6276](https://ubuntu.com/security/CVE-2026-6276) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-27144](https://ubuntu.com/security/CVE-2026-27144) | Yes | Yes | Yes | Yes | High (7.1)  
[CVE-2026-39883](https://ubuntu.com/security/CVE-2026-39883) | Yes | Yes | Yes | Yes | High (7.0)  
[CVE-2026-4878](https://ubuntu.com/security/CVE-2026-4878) | Yes | Yes | No | Yes | Medium (7.0)  
[CVE-2026-5545](https://ubuntu.com/security/CVE-2026-5545) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-32282](https://ubuntu.com/security/CVE-2026-32282) | Yes | Yes | Yes | Yes | Medium (6.4)  
[CVE-2026-32289](https://ubuntu.com/security/CVE-2026-32289) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39823](https://ubuntu.com/security/CVE-2026-39823) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39826](https://ubuntu.com/security/CVE-2026-39826) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39817](https://ubuntu.com/security/CVE-2026-39817) | Yes | Yes | Yes | Yes | Medium (5.9)  
[CVE-2026-4873](https://ubuntu.com/security/CVE-2026-4873) | Yes | Yes | No | Yes | Low (5.9)  
[CVE-2026-6253](https://ubuntu.com/security/CVE-2026-6253) | Yes | Yes | No | Yes | Medium (5.9)  
[CVE-2026-32288](https://ubuntu.com/security/CVE-2026-32288) | Yes | Yes | Yes | Yes | Medium (5.5)  
[CVE-2026-39350](https://ubuntu.com/security/CVE-2026-39350) | Yes | Yes | Yes | Yes | Medium (5.4)  
[CVE-2026-4438](https://ubuntu.com/security/CVE-2026-4438) | No | No | Yes | No | Medium (5.4)  
[CVE-2026-39819](https://ubuntu.com/security/CVE-2026-39819) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-39825](https://ubuntu.com/security/CVE-2026-39825) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-6429](https://ubuntu.com/security/CVE-2026-6429) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-7168](https://ubuntu.com/security/CVE-2026-7168) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-35469](https://ubuntu.com/security/CVE-2026-35469) | No | Yes | No | Yes | High (0.0)  
[CVE-2026-5958](https://ubuntu.com/security/CVE-2026-5958) | Yes | Yes | No | Yes | Medium (0.0)  
  
### Announcement

**1.27.9-asm.4 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade). Cloud Service Mesh 1.27.9-asm.4 uses Envoy v1.35.10-dev.

### Announcement

**1.27.9-asm.4 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh 1.27.9-asm.4 uses Envoy v1.35.10-dev.

### Fixed

Patch 1.27.9-asm.4 contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2022-31045](https://ubuntu.com/security/CVE-2022-31045) | Yes | Yes | Yes | Yes | Medium (9.8)  
[CVE-2026-27143](https://ubuntu.com/security/CVE-2026-27143) | Yes | Yes | Yes | Yes | Critical (9.8)  
[CVE-2026-31789](https://ubuntu.com/security/CVE-2026-31789) | Yes | Yes | No | Yes | Low (9.8)  
[CVE-2026-27140](https://ubuntu.com/security/CVE-2026-27140) | Yes | Yes | Yes | Yes | High (8.8)  
[CVE-2026-28387](https://ubuntu.com/security/CVE-2026-28387) | Yes | Yes | No | Yes | Low (8.1)  
[CVE-2026-41413](https://ubuntu.com/security/CVE-2026-41413) | Yes | Yes | Yes | Yes | Medium (7.7)  
[CVE-2019-14993](https://ubuntu.com/security/CVE-2019-14993) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2021-39155](https://ubuntu.com/security/CVE-2021-39155) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2021-39156](https://ubuntu.com/security/CVE-2021-39156) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2022-23635](https://ubuntu.com/security/CVE-2022-23635) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-2219](https://ubuntu.com/security/CVE-2026-2219) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-27135](https://ubuntu.com/security/CVE-2026-27135) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-28388](https://ubuntu.com/security/CVE-2026-28388) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-28389](https://ubuntu.com/security/CVE-2026-28389) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-28390](https://ubuntu.com/security/CVE-2026-28390) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-29181](https://ubuntu.com/security/CVE-2026-29181) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-31790](https://ubuntu.com/security/CVE-2026-31790) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-32280](https://ubuntu.com/security/CVE-2026-32280) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-32281](https://ubuntu.com/security/CVE-2026-32281) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-32283](https://ubuntu.com/security/CVE-2026-32283) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-33811](https://ubuntu.com/security/CVE-2026-33811) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-33814](https://ubuntu.com/security/CVE-2026-33814) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-34986](https://ubuntu.com/security/CVE-2026-34986) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-39820](https://ubuntu.com/security/CVE-2026-39820) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-39836](https://ubuntu.com/security/CVE-2026-39836) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-4046](https://ubuntu.com/security/CVE-2026-4046) | No | No | Yes | No | High (7.5)  
[CVE-2026-42499](https://ubuntu.com/security/CVE-2026-42499) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-42501](https://ubuntu.com/security/CVE-2026-42501) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-4437](https://ubuntu.com/security/CVE-2026-4437) | No | No | Yes | No | High (7.5)  
[CVE-2026-5773](https://ubuntu.com/security/CVE-2026-5773) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-6276](https://ubuntu.com/security/CVE-2026-6276) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-27144](https://ubuntu.com/security/CVE-2026-27144) | Yes | Yes | Yes | Yes | High (7.1)  
[CVE-2026-39883](https://ubuntu.com/security/CVE-2026-39883) | Yes | Yes | Yes | Yes | High (7.0)  
[CVE-2026-4878](https://ubuntu.com/security/CVE-2026-4878) | Yes | Yes | No | Yes | Medium (7.0)  
[CVE-2026-5545](https://ubuntu.com/security/CVE-2026-5545) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-32282](https://ubuntu.com/security/CVE-2026-32282) | Yes | Yes | Yes | Yes | Medium (6.4)  
[CVE-2026-32289](https://ubuntu.com/security/CVE-2026-32289) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39823](https://ubuntu.com/security/CVE-2026-39823) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39826](https://ubuntu.com/security/CVE-2026-39826) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39817](https://ubuntu.com/security/CVE-2026-39817) | Yes | Yes | Yes | Yes | Medium (5.9)  
[CVE-2026-4873](https://ubuntu.com/security/CVE-2026-4873) | Yes | Yes | No | Yes | Low (5.9)  
[CVE-2026-6253](https://ubuntu.com/security/CVE-2026-6253) | Yes | Yes | No | Yes | Medium (5.9)  
[CVE-2026-32288](https://ubuntu.com/security/CVE-2026-32288) | Yes | Yes | Yes | Yes | Medium (5.5)  
[CVE-2026-39350](https://ubuntu.com/security/CVE-2026-39350) | Yes | Yes | Yes | Yes | Medium (5.4)  
[CVE-2026-4438](https://ubuntu.com/security/CVE-2026-4438) | No | No | Yes | No | Medium (5.4)  
[CVE-2026-39819](https://ubuntu.com/security/CVE-2026-39819) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-39825](https://ubuntu.com/security/CVE-2026-39825) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-6429](https://ubuntu.com/security/CVE-2026-6429) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-7168](https://ubuntu.com/security/CVE-2026-7168) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-35469](https://ubuntu.com/security/CVE-2026-35469) | No | Yes | No | Yes | High (0.0)  
[CVE-2026-5958](https://ubuntu.com/security/CVE-2026-5958) | Yes | Yes | No | Yes | Medium (0.0)  
  
### Fixed

Patch 1.27.9-asm.4 contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2022-31045](https://ubuntu.com/security/CVE-2022-31045) | Yes | Yes | Yes | Yes | Medium (9.8)  
[CVE-2026-27143](https://ubuntu.com/security/CVE-2026-27143) | Yes | Yes | Yes | Yes | Critical (9.8)  
[CVE-2026-31789](https://ubuntu.com/security/CVE-2026-31789) | Yes | Yes | No | Yes | Low (9.8)  
[CVE-2026-27140](https://ubuntu.com/security/CVE-2026-27140) | Yes | Yes | Yes | Yes | High (8.8)  
[CVE-2026-28387](https://ubuntu.com/security/CVE-2026-28387) | Yes | Yes | No | Yes | Low (8.1)  
[CVE-2026-41413](https://ubuntu.com/security/CVE-2026-41413) | Yes | Yes | Yes | Yes | Medium (7.7)  
[CVE-2019-14993](https://ubuntu.com/security/CVE-2019-14993) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2021-39155](https://ubuntu.com/security/CVE-2021-39155) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2021-39156](https://ubuntu.com/security/CVE-2021-39156) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2022-23635](https://ubuntu.com/security/CVE-2022-23635) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-2219](https://ubuntu.com/security/CVE-2026-2219) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-27135](https://ubuntu.com/security/CVE-2026-27135) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-28388](https://ubuntu.com/security/CVE-2026-28388) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-28389](https://ubuntu.com/security/CVE-2026-28389) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-28390](https://ubuntu.com/security/CVE-2026-28390) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-29181](https://ubuntu.com/security/CVE-2026-29181) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-31790](https://ubuntu.com/security/CVE-2026-31790) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-32280](https://ubuntu.com/security/CVE-2026-32280) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-32281](https://ubuntu.com/security/CVE-2026-32281) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-32283](https://ubuntu.com/security/CVE-2026-32283) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-33811](https://ubuntu.com/security/CVE-2026-33811) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-33814](https://ubuntu.com/security/CVE-2026-33814) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-34986](https://ubuntu.com/security/CVE-2026-34986) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-39820](https://ubuntu.com/security/CVE-2026-39820) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-39836](https://ubuntu.com/security/CVE-2026-39836) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-4046](https://ubuntu.com/security/CVE-2026-4046) | No | No | Yes | No | High (7.5)  
[CVE-2026-42499](https://ubuntu.com/security/CVE-2026-42499) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-42501](https://ubuntu.com/security/CVE-2026-42501) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-4437](https://ubuntu.com/security/CVE-2026-4437) | No | No | Yes | No | High (7.5)  
[CVE-2026-5773](https://ubuntu.com/security/CVE-2026-5773) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-6276](https://ubuntu.com/security/CVE-2026-6276) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-27144](https://ubuntu.com/security/CVE-2026-27144) | Yes | Yes | Yes | Yes | High (7.1)  
[CVE-2026-39883](https://ubuntu.com/security/CVE-2026-39883) | Yes | Yes | Yes | Yes | High (7.0)  
[CVE-2026-4878](https://ubuntu.com/security/CVE-2026-4878) | Yes | Yes | No | Yes | Medium (7.0)  
[CVE-2026-5545](https://ubuntu.com/security/CVE-2026-5545) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-32282](https://ubuntu.com/security/CVE-2026-32282) | Yes | Yes | Yes | Yes | Medium (6.4)  
[CVE-2026-32289](https://ubuntu.com/security/CVE-2026-32289) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39823](https://ubuntu.com/security/CVE-2026-39823) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39826](https://ubuntu.com/security/CVE-2026-39826) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39817](https://ubuntu.com/security/CVE-2026-39817) | Yes | Yes | Yes | Yes | Medium (5.9)  
[CVE-2026-4873](https://ubuntu.com/security/CVE-2026-4873) | Yes | Yes | No | Yes | Low (5.9)  
[CVE-2026-6253](https://ubuntu.com/security/CVE-2026-6253) | Yes | Yes | No | Yes | Medium (5.9)  
[CVE-2026-32288](https://ubuntu.com/security/CVE-2026-32288) | Yes | Yes | Yes | Yes | Medium (5.5)  
[CVE-2026-39350](https://ubuntu.com/security/CVE-2026-39350) | Yes | Yes | Yes | Yes | Medium (5.4)  
[CVE-2026-4438](https://ubuntu.com/security/CVE-2026-4438) | No | No | Yes | No | Medium (5.4)  
[CVE-2026-39819](https://ubuntu.com/security/CVE-2026-39819) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-39825](https://ubuntu.com/security/CVE-2026-39825) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-6429](https://ubuntu.com/security/CVE-2026-6429) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-7168](https://ubuntu.com/security/CVE-2026-7168) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-35469](https://ubuntu.com/security/CVE-2026-35469) | No | Yes | No | Yes | High (0.0)  
[CVE-2026-5958](https://ubuntu.com/security/CVE-2026-5958) | Yes | Yes | No | Yes | Medium (0.0)  
**1.26.x**

### Announcement

**1.26.8-asm.10 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade). Cloud Service Mesh 1.26.8-asm.10 uses Envoy v1.34.14.

### Announcement

**1.26.8-asm.10 is now available for in-cluster Cloud Service Mesh.**

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh 1.26.8-asm.10 uses Envoy v1.34.14.

### Fixed

Patch 1.26.8-asm.10 contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2022-31045](https://ubuntu.com/security/CVE-2022-31045) | Yes | Yes | Yes | Yes | Medium (9.8)  
[CVE-2026-27143](https://ubuntu.com/security/CVE-2026-27143) | Yes | Yes | Yes | Yes | Critical (9.8)  
[CVE-2026-31789](https://ubuntu.com/security/CVE-2026-31789) | Yes | Yes | No | Yes | Low (9.8)  
[CVE-2026-27140](https://ubuntu.com/security/CVE-2026-27140) | Yes | Yes | Yes | Yes | High (8.8)  
[CVE-2026-28387](https://ubuntu.com/security/CVE-2026-28387) | Yes | Yes | No | Yes | Low (8.1)  
[CVE-2026-41413](https://ubuntu.com/security/CVE-2026-41413) | Yes | Yes | Yes | Yes | Medium (7.7)  
[CVE-2019-14993](https://ubuntu.com/security/CVE-2019-14993) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2021-39155](https://ubuntu.com/security/CVE-2021-39155) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2021-39156](https://ubuntu.com/security/CVE-2021-39156) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2022-23635](https://ubuntu.com/security/CVE-2022-23635) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-2219](https://ubuntu.com/security/CVE-2026-2219) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-27135](https://ubuntu.com/security/CVE-2026-27135) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-28388](https://ubuntu.com/security/CVE-2026-28388) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-28389](https://ubuntu.com/security/CVE-2026-28389) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-28390](https://ubuntu.com/security/CVE-2026-28390) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-29181](https://ubuntu.com/security/CVE-2026-29181) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-31790](https://ubuntu.com/security/CVE-2026-31790) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-32280](https://ubuntu.com/security/CVE-2026-32280) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-32281](https://ubuntu.com/security/CVE-2026-32281) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-32283](https://ubuntu.com/security/CVE-2026-32283) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-33811](https://ubuntu.com/security/CVE-2026-33811) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-33814](https://ubuntu.com/security/CVE-2026-33814) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-34986](https://ubuntu.com/security/CVE-2026-34986) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-39820](https://ubuntu.com/security/CVE-2026-39820) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-39836](https://ubuntu.com/security/CVE-2026-39836) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-4046](https://ubuntu.com/security/CVE-2026-4046) | No | No | Yes | No | High (7.5)  
[CVE-2026-42499](https://ubuntu.com/security/CVE-2026-42499) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-42501](https://ubuntu.com/security/CVE-2026-42501) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-4437](https://ubuntu.com/security/CVE-2026-4437) | No | No | Yes | No | High (7.5)  
[CVE-2026-5773](https://ubuntu.com/security/CVE-2026-5773) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-6276](https://ubuntu.com/security/CVE-2026-6276) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-27144](https://ubuntu.com/security/CVE-2026-27144) | Yes | Yes | Yes | Yes | High (7.1)  
[CVE-2026-39883](https://ubuntu.com/security/CVE-2026-39883) | Yes | Yes | Yes | Yes | High (7.0)  
[CVE-2026-4878](https://ubuntu.com/security/CVE-2026-4878) | Yes | Yes | No | Yes | Medium (7.0)  
[CVE-2026-5545](https://ubuntu.com/security/CVE-2026-5545) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-32282](https://ubuntu.com/security/CVE-2026-32282) | Yes | Yes | Yes | Yes | Medium (6.4)  
[CVE-2026-32289](https://ubuntu.com/security/CVE-2026-32289) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39823](https://ubuntu.com/security/CVE-2026-39823) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39826](https://ubuntu.com/security/CVE-2026-39826) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39817](https://ubuntu.com/security/CVE-2026-39817) | Yes | Yes | Yes | Yes | Medium (5.9)  
[CVE-2026-4873](https://ubuntu.com/security/CVE-2026-4873) | Yes | Yes | No | Yes | Low (5.9)  
[CVE-2026-6253](https://ubuntu.com/security/CVE-2026-6253) | Yes | Yes | No | Yes | Medium (5.9)  
[CVE-2026-32288](https://ubuntu.com/security/CVE-2026-32288) | Yes | Yes | Yes | Yes | Medium (5.5)  
[CVE-2026-39350](https://ubuntu.com/security/CVE-2026-39350) | Yes | Yes | Yes | Yes | Medium (5.4)  
[CVE-2026-4438](https://ubuntu.com/security/CVE-2026-4438) | No | No | Yes | No | Medium (5.4)  
[CVE-2026-39819](https://ubuntu.com/security/CVE-2026-39819) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-39825](https://ubuntu.com/security/CVE-2026-39825) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-6429](https://ubuntu.com/security/CVE-2026-6429) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-7168](https://ubuntu.com/security/CVE-2026-7168) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-35469](https://ubuntu.com/security/CVE-2026-35469) | No | Yes | No | Yes | High (0.0)  
[CVE-2026-5958](https://ubuntu.com/security/CVE-2026-5958) | Yes | Yes | No | Yes | Medium (0.0)  
  
### Fixed

Patch 1.26.8-asm.10 contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2022-31045](https://ubuntu.com/security/CVE-2022-31045) | Yes | Yes | Yes | Yes | Medium (9.8)  
[CVE-2026-27143](https://ubuntu.com/security/CVE-2026-27143) | Yes | Yes | Yes | Yes | Critical (9.8)  
[CVE-2026-31789](https://ubuntu.com/security/CVE-2026-31789) | Yes | Yes | No | Yes | Low (9.8)  
[CVE-2026-27140](https://ubuntu.com/security/CVE-2026-27140) | Yes | Yes | Yes | Yes | High (8.8)  
[CVE-2026-28387](https://ubuntu.com/security/CVE-2026-28387) | Yes | Yes | No | Yes | Low (8.1)  
[CVE-2026-41413](https://ubuntu.com/security/CVE-2026-41413) | Yes | Yes | Yes | Yes | Medium (7.7)  
[CVE-2019-14993](https://ubuntu.com/security/CVE-2019-14993) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2021-39155](https://ubuntu.com/security/CVE-2021-39155) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2021-39156](https://ubuntu.com/security/CVE-2021-39156) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2022-23635](https://ubuntu.com/security/CVE-2022-23635) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-2219](https://ubuntu.com/security/CVE-2026-2219) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-27135](https://ubuntu.com/security/CVE-2026-27135) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-28388](https://ubuntu.com/security/CVE-2026-28388) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-28389](https://ubuntu.com/security/CVE-2026-28389) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-28390](https://ubuntu.com/security/CVE-2026-28390) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-29181](https://ubuntu.com/security/CVE-2026-29181) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-31790](https://ubuntu.com/security/CVE-2026-31790) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-32280](https://ubuntu.com/security/CVE-2026-32280) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-32281](https://ubuntu.com/security/CVE-2026-32281) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-32283](https://ubuntu.com/security/CVE-2026-32283) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-33811](https://ubuntu.com/security/CVE-2026-33811) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-33814](https://ubuntu.com/security/CVE-2026-33814) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-34986](https://ubuntu.com/security/CVE-2026-34986) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-39820](https://ubuntu.com/security/CVE-2026-39820) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-39836](https://ubuntu.com/security/CVE-2026-39836) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-4046](https://ubuntu.com/security/CVE-2026-4046) | No | No | Yes | No | High (7.5)  
[CVE-2026-42499](https://ubuntu.com/security/CVE-2026-42499) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-42501](https://ubuntu.com/security/CVE-2026-42501) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-4437](https://ubuntu.com/security/CVE-2026-4437) | No | No | Yes | No | High (7.5)  
[CVE-2026-5773](https://ubuntu.com/security/CVE-2026-5773) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-6276](https://ubuntu.com/security/CVE-2026-6276) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-27144](https://ubuntu.com/security/CVE-2026-27144) | Yes | Yes | Yes | Yes | High (7.1)  
[CVE-2026-39883](https://ubuntu.com/security/CVE-2026-39883) | Yes | Yes | Yes | Yes | High (7.0)  
[CVE-2026-4878](https://ubuntu.com/security/CVE-2026-4878) | Yes | Yes | No | Yes | Medium (7.0)  
[CVE-2026-5545](https://ubuntu.com/security/CVE-2026-5545) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-32282](https://ubuntu.com/security/CVE-2026-32282) | Yes | Yes | Yes | Yes | Medium (6.4)  
[CVE-2026-32289](https://ubuntu.com/security/CVE-2026-32289) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39823](https://ubuntu.com/security/CVE-2026-39823) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39826](https://ubuntu.com/security/CVE-2026-39826) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39817](https://ubuntu.com/security/CVE-2026-39817) | Yes | Yes | Yes | Yes | Medium (5.9)  
[CVE-2026-4873](https://ubuntu.com/security/CVE-2026-4873) | Yes | Yes | No | Yes | Low (5.9)  
[CVE-2026-6253](https://ubuntu.com/security/CVE-2026-6253) | Yes | Yes | No | Yes | Medium (5.9)  
[CVE-2026-32288](https://ubuntu.com/security/CVE-2026-32288) | Yes | Yes | Yes | Yes | Medium (5.5)  
[CVE-2026-39350](https://ubuntu.com/security/CVE-2026-39350) | Yes | Yes | Yes | Yes | Medium (5.4)  
[CVE-2026-4438](https://ubuntu.com/security/CVE-2026-4438) | No | No | Yes | No | Medium (5.4)  
[CVE-2026-39819](https://ubuntu.com/security/CVE-2026-39819) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-39825](https://ubuntu.com/security/CVE-2026-39825) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-6429](https://ubuntu.com/security/CVE-2026-6429) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-7168](https://ubuntu.com/security/CVE-2026-7168) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-35469](https://ubuntu.com/security/CVE-2026-35469) | No | Yes | No | Yes | High (0.0)  
[CVE-2026-5958](https://ubuntu.com/security/CVE-2026-5958) | Yes | Yes | No | Yes | Medium (0.0)  
**Managed Cloud Service Mesh**

### Announcement

The following images are now rolling out for managed Cloud Service Mesh:

  * 1.21.6-asm.32 is rolling out to the rapid release channel.
  * The regular release channel is being upgraded from 1.20 to 1.21.6-asm.32.
  * The stable release channel is being upgraded from 1.19 to 1.20.8-asm.80.



### Announcement

The following images are now rolling out for managed Cloud Service Mesh:

  * 1.21.6-asm.32 is rolling out to the rapid release channel.
  * The regular release channel is being upgraded from 1.20 to 1.21.6-asm.32.
  * The stable release channel is being upgraded from 1.19 to 1.20.8-asm.80.



### Fixed

These patch releases contain the fixes for the following CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-27143](https://ubuntu.com/security/CVE-2026-27143) | Yes | Yes | Yes | Yes | Critical (9.8)  
[CVE-2026-31789](https://ubuntu.com/security/CVE-2026-31789) | Yes | Yes | No | Yes | Low (9.8)  
[CVE-2026-27140](https://ubuntu.com/security/CVE-2026-27140) | Yes | Yes | Yes | Yes | High (8.8)  
[CVE-2026-28387](https://ubuntu.com/security/CVE-2026-28387) | Yes | Yes | No | Yes | Low (8.1)  
[CVE-2026-41413](https://ubuntu.com/security/CVE-2026-41413) | Yes | Yes | Yes | Yes | Medium (7.7)  
[CVE-2026-2219](https://ubuntu.com/security/CVE-2026-2219) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-27135](https://ubuntu.com/security/CVE-2026-27135) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-28388](https://ubuntu.com/security/CVE-2026-28388) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-28389](https://ubuntu.com/security/CVE-2026-28389) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-28390](https://ubuntu.com/security/CVE-2026-28390) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-29181](https://ubuntu.com/security/CVE-2026-29181) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-31790](https://ubuntu.com/security/CVE-2026-31790) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-32280](https://ubuntu.com/security/CVE-2026-32280) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-32281](https://ubuntu.com/security/CVE-2026-32281) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-32283](https://ubuntu.com/security/CVE-2026-32283) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-33811](https://ubuntu.com/security/CVE-2026-33811) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-33814](https://ubuntu.com/security/CVE-2026-33814) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-34986](https://ubuntu.com/security/CVE-2026-34986) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-39820](https://ubuntu.com/security/CVE-2026-39820) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-39836](https://ubuntu.com/security/CVE-2026-39836) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-4046](https://ubuntu.com/security/CVE-2026-4046) | No | No | Yes | No | High (7.5)  
[CVE-2026-42499](https://ubuntu.com/security/CVE-2026-42499) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-42501](https://ubuntu.com/security/CVE-2026-42501) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-4437](https://ubuntu.com/security/CVE-2026-4437) | No | No | Yes | No | High (7.5)  
[CVE-2026-5773](https://ubuntu.com/security/CVE-2026-5773) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-6276](https://ubuntu.com/security/CVE-2026-6276) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-27144](https://ubuntu.com/security/CVE-2026-27144) | Yes | Yes | Yes | Yes | High (7.1)  
[CVE-2026-39883](https://ubuntu.com/security/CVE-2026-39883) | Yes | Yes | Yes | Yes | High (7.0)  
[CVE-2026-4878](https://ubuntu.com/security/CVE-2026-4878) | Yes | Yes | No | Yes | Medium (7.0)  
[CVE-2026-5545](https://ubuntu.com/security/CVE-2026-5545) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-32282](https://ubuntu.com/security/CVE-2026-32282) | Yes | Yes | Yes | Yes | Medium (6.4)  
[CVE-2026-32289](https://ubuntu.com/security/CVE-2026-32289) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39823](https://ubuntu.com/security/CVE-2026-39823) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39826](https://ubuntu.com/security/CVE-2026-39826) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39817](https://ubuntu.com/security/CVE-2026-39817) | Yes | Yes | Yes | Yes | Medium (5.9)  
[CVE-2026-4873](https://ubuntu.com/security/CVE-2026-4873) | Yes | Yes | No | Yes | Low (5.9)  
[CVE-2026-6253](https://ubuntu.com/security/CVE-2026-6253) | Yes | Yes | No | Yes | Medium (5.9)  
[CVE-2026-32288](https://ubuntu.com/security/CVE-2026-32288) | Yes | Yes | Yes | Yes | Medium (5.5)  
[CVE-2026-39350](https://ubuntu.com/security/CVE-2026-39350) | Yes | Yes | Yes | Yes | Medium (5.4)  
[CVE-2026-4438](https://ubuntu.com/security/CVE-2026-4438) | No | No | Yes | No | Medium (5.4)  
[CVE-2026-39819](https://ubuntu.com/security/CVE-2026-39819) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-39825](https://ubuntu.com/security/CVE-2026-39825) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-6429](https://ubuntu.com/security/CVE-2026-6429) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-7168](https://ubuntu.com/security/CVE-2026-7168) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-35469](https://ubuntu.com/security/CVE-2026-35469) | No | Yes | No | Yes | High (0.0)  
[CVE-2026-5958](https://ubuntu.com/security/CVE-2026-5958) | Yes | Yes | No | Yes | Medium (0.0)  
  
### Fixed

These patch releases contain the fixes for the following CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-27143](https://ubuntu.com/security/CVE-2026-27143) | Yes | Yes | Yes | Yes | Critical (9.8)  
[CVE-2026-31789](https://ubuntu.com/security/CVE-2026-31789) | Yes | Yes | No | Yes | Low (9.8)  
[CVE-2026-27140](https://ubuntu.com/security/CVE-2026-27140) | Yes | Yes | Yes | Yes | High (8.8)  
[CVE-2026-28387](https://ubuntu.com/security/CVE-2026-28387) | Yes | Yes | No | Yes | Low (8.1)  
[CVE-2026-41413](https://ubuntu.com/security/CVE-2026-41413) | Yes | Yes | Yes | Yes | Medium (7.7)  
[CVE-2026-2219](https://ubuntu.com/security/CVE-2026-2219) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-27135](https://ubuntu.com/security/CVE-2026-27135) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-28388](https://ubuntu.com/security/CVE-2026-28388) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-28389](https://ubuntu.com/security/CVE-2026-28389) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-28390](https://ubuntu.com/security/CVE-2026-28390) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-29181](https://ubuntu.com/security/CVE-2026-29181) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-31790](https://ubuntu.com/security/CVE-2026-31790) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-32280](https://ubuntu.com/security/CVE-2026-32280) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-32281](https://ubuntu.com/security/CVE-2026-32281) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-32283](https://ubuntu.com/security/CVE-2026-32283) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-33811](https://ubuntu.com/security/CVE-2026-33811) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-33814](https://ubuntu.com/security/CVE-2026-33814) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-34986](https://ubuntu.com/security/CVE-2026-34986) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-39820](https://ubuntu.com/security/CVE-2026-39820) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-39836](https://ubuntu.com/security/CVE-2026-39836) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-4046](https://ubuntu.com/security/CVE-2026-4046) | No | No | Yes | No | High (7.5)  
[CVE-2026-42499](https://ubuntu.com/security/CVE-2026-42499) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-42501](https://ubuntu.com/security/CVE-2026-42501) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2026-4437](https://ubuntu.com/security/CVE-2026-4437) | No | No | Yes | No | High (7.5)  
[CVE-2026-5773](https://ubuntu.com/security/CVE-2026-5773) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-6276](https://ubuntu.com/security/CVE-2026-6276) | Yes | Yes | No | Yes | Low (7.5)  
[CVE-2026-27144](https://ubuntu.com/security/CVE-2026-27144) | Yes | Yes | Yes | Yes | High (7.1)  
[CVE-2026-39883](https://ubuntu.com/security/CVE-2026-39883) | Yes | Yes | Yes | Yes | High (7.0)  
[CVE-2026-4878](https://ubuntu.com/security/CVE-2026-4878) | Yes | Yes | No | Yes | Medium (7.0)  
[CVE-2026-5545](https://ubuntu.com/security/CVE-2026-5545) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-32282](https://ubuntu.com/security/CVE-2026-32282) | Yes | Yes | Yes | Yes | Medium (6.4)  
[CVE-2026-32289](https://ubuntu.com/security/CVE-2026-32289) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39823](https://ubuntu.com/security/CVE-2026-39823) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39826](https://ubuntu.com/security/CVE-2026-39826) | Yes | Yes | Yes | Yes | Medium (6.1)  
[CVE-2026-39817](https://ubuntu.com/security/CVE-2026-39817) | Yes | Yes | Yes | Yes | Medium (5.9)  
[CVE-2026-4873](https://ubuntu.com/security/CVE-2026-4873) | Yes | Yes | No | Yes | Low (5.9)  
[CVE-2026-6253](https://ubuntu.com/security/CVE-2026-6253) | Yes | Yes | No | Yes | Medium (5.9)  
[CVE-2026-32288](https://ubuntu.com/security/CVE-2026-32288) | Yes | Yes | Yes | Yes | Medium (5.5)  
[CVE-2026-39350](https://ubuntu.com/security/CVE-2026-39350) | Yes | Yes | Yes | Yes | Medium (5.4)  
[CVE-2026-4438](https://ubuntu.com/security/CVE-2026-4438) | No | No | Yes | No | Medium (5.4)  
[CVE-2026-39819](https://ubuntu.com/security/CVE-2026-39819) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-39825](https://ubuntu.com/security/CVE-2026-39825) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2026-6429](https://ubuntu.com/security/CVE-2026-6429) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-7168](https://ubuntu.com/security/CVE-2026-7168) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2026-35469](https://ubuntu.com/security/CVE-2026-35469) | No | Yes | No | Yes | High (0.0)  
[CVE-2026-5958](https://ubuntu.com/security/CVE-2026-5958) | Yes | Yes | No | Yes | Medium (0.0)  
]]> May 20, 2026tag:google.com,2016:servicemesh-release-notes#May_20_20262026-05-20T00:00:00-07:00Managed Cloud Service Mesh 

### Announcement

Managed Cloud Service Mesh using the `TRAFFIC_DIRECTOR` implementation in the stable channel now supports a limited implementation of the `EnvoyFilter` API. To learn about the supported fields, extensions, and how to use `EnvoyFilter` for features like local rate limiting see [Data plane extensibility with `EnvoyFilter`](https://docs.cloud.google.com/service-mesh/v1.29/docs/data-plane-extensibility).

To troubleshoot any issue while configuring, see [Resolving data plane extensibility issues](https://docs.cloud.google.com/service-mesh/v1.29/docs/troubleshooting/troubleshoot-data-plane-extensibility).

### Announcement

Managed Cloud Service Mesh using the `TRAFFIC_DIRECTOR` implementation in the stable channel now supports a limited implementation of the `EnvoyFilter` API. To learn about the supported fields, extensions, and how to use `EnvoyFilter` for features like local rate limiting see [Data plane extensibility with `EnvoyFilter`](https://docs.cloud.google.com/service-mesh/docs/data-plane-extensibility).

To troubleshoot any issue while configuring, see [Resolving data plane extensibility issues](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-data-plane-extensibility).

### Announcement

Cloud Service Mesh can now report a status code to indicate whether an Istio API is accepted or rejected. You can view the status code on the resource and mesh state. For more information see [MembershipState Error Codes](https://docs.cloud.google.com/service-mesh/v1.29/docs/troubleshooting/troubleshoot-configuration#membershipstate_error_codes).

### Announcement

Cloud Service Mesh can now report a status code to indicate whether an Istio API is accepted or rejected. You can view the status code on the resource and mesh state. For more information see [MembershipState Error Codes](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-configuration#membershipstate_error_codes).

]]> May 13, 2026tag:google.com,2016:servicemesh-release-notes#May_13_20262026-05-13T00:00:00-07:00Managed Cloud Service Mesh 

### Security

Proxy version csm_mesh_proxy.20260423_RC03 is rolling out to all Managed Cloud Service Mesh release channels over the next week.

### Security

Proxy version csm_mesh_proxy.20260423_RC03 is rolling out to all Managed Cloud Service Mesh release channels over the next week.

]]> April 27, 2026tag:google.com,2016:servicemesh-release-notes#April_27_20262026-04-27T00:00:00-07:00Managed Cloud Service Mesh 

### Announcement

Managed Cloud Service Mesh using the `TRAFFIC_DIRECTOR` implementation in the regular channel now supports a limited implementation of the `EnvoyFilter` API. To learn about the supported fields, extensions, and how to use `EnvoyFilter` for features like local rate limiting see [Data plane extensibility with `EnvoyFilter`](https://docs.cloud.google.com/service-mesh/v1.29/docs/data-plane-extensibility).

To troubleshoot any issue while configuring, see [Resolving data plane extensibility issues](https://docs.cloud.google.com/service-mesh/v1.29/docs/troubleshooting/troubleshoot-data-plane-extensibility).

### Announcement

Managed Cloud Service Mesh using the `TRAFFIC_DIRECTOR` implementation in the regular channel now supports a limited implementation of the `EnvoyFilter` API. To learn about the supported fields, extensions, and how to use `EnvoyFilter` for features like local rate limiting see [Data plane extensibility with `EnvoyFilter`](https://docs.cloud.google.com/service-mesh/v1.28/docs/data-plane-extensibility).

To troubleshoot any issue while configuring, see [Resolving data plane extensibility issues](https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-data-plane-extensibility).

### Announcement

Managed Cloud Service Mesh using the `TRAFFIC_DIRECTOR` implementation in the regular channel now supports a limited implementation of the `EnvoyFilter` API. To learn about the supported fields, extensions, and how to use `EnvoyFilter` for features like local rate limiting see [Data plane extensibility with `EnvoyFilter`](https://docs.cloud.google.com/service-mesh/docs/data-plane-extensibility).

To troubleshoot any issue while configuring, see [Resolving data plane extensibility issues](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-data-plane-extensibility).

]]> April 13, 2026tag:google.com,2016:servicemesh-release-notes#April_13_20262026-04-13T00:00:00-07:001.27.x 

### Announcement

**1.28.5-asm.12 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-33186](https://security-tracker.debian.org/tracker/CVE-2026-33186) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-3731](https://security-tracker.debian.org/tracker/CVE-2026-3731) | Yes | Yes | No | Yes | High (7.5)  
[CVE-2026-3784](https://security-tracker.debian.org/tracker/CVE-2026-3784) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-1965](https://security-tracker.debian.org/tracker/CVE-2026-1965) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-29111](https://security-tracker.debian.org/tracker/CVE-2026-29111) | Yes | Yes | No | Yes | Medium (5.5)  
[CVE-2026-3783](https://security-tracker.debian.org/tracker/CVE-2026-3783) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2025-0167](https://security-tracker.debian.org/tracker/CVE-2025-0167) | Yes | Yes | No | Yes | Low (3.4)  
  
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade). Cloud Service Mesh 1.28.5-asm.12 uses Envoy 1.36.5-dev.

### Announcement

**1.28.5-asm.12 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-33186](https://security-tracker.debian.org/tracker/CVE-2026-33186) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-3731](https://security-tracker.debian.org/tracker/CVE-2026-3731) | Yes | Yes | No | Yes | High (7.5)  
[CVE-2026-3784](https://security-tracker.debian.org/tracker/CVE-2026-3784) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-1965](https://security-tracker.debian.org/tracker/CVE-2026-1965) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-29111](https://security-tracker.debian.org/tracker/CVE-2026-29111) | Yes | Yes | No | Yes | Medium (5.5)  
[CVE-2026-3783](https://security-tracker.debian.org/tracker/CVE-2026-3783) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2025-0167](https://security-tracker.debian.org/tracker/CVE-2025-0167) | Yes | Yes | No | Yes | Low (3.4)  
  
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade). Cloud Service Mesh 1.28.5-asm.12 uses Envoy 1.36.5-dev.

### Announcement

**1.28.5-asm.12 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-33186](https://security-tracker.debian.org/tracker/CVE-2026-33186) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-3731](https://security-tracker.debian.org/tracker/CVE-2026-3731) | Yes | Yes | No | Yes | High (7.5)  
[CVE-2026-3784](https://security-tracker.debian.org/tracker/CVE-2026-3784) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-1965](https://security-tracker.debian.org/tracker/CVE-2026-1965) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-29111](https://security-tracker.debian.org/tracker/CVE-2026-29111) | Yes | Yes | No | Yes | Medium (5.5)  
[CVE-2026-3783](https://security-tracker.debian.org/tracker/CVE-2026-3783) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2025-0167](https://security-tracker.debian.org/tracker/CVE-2025-0167) | Yes | Yes | No | Yes | Low (3.4)  
  
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh 1.28.5-asm.12 uses Envoy 1.36.5-dev.

### Announcement

**1.27.8-asm.9 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-33186](https://security-tracker.debian.org/tracker/CVE-2026-33186) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-3731](https://security-tracker.debian.org/tracker/CVE-2026-3731) | Yes | Yes | No | Yes | High (7.5)  
[CVE-2026-3784](https://security-tracker.debian.org/tracker/CVE-2026-3784) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-1965](https://security-tracker.debian.org/tracker/CVE-2026-1965) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-29111](https://security-tracker.debian.org/tracker/CVE-2026-29111) | Yes | Yes | No | Yes | Medium (5.5)  
[CVE-2026-3783](https://security-tracker.debian.org/tracker/CVE-2026-3783) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2025-0167](https://security-tracker.debian.org/tracker/CVE-2025-0167) | Yes | Yes | No | Yes | Low (3.4)  
  
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade). Cloud Service Mesh 1.27.8-asm.9 uses Envoy 1.35.10-dev.

### Announcement

**1.27.8-asm.9 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-33186](https://security-tracker.debian.org/tracker/CVE-2026-33186) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-3731](https://security-tracker.debian.org/tracker/CVE-2026-3731) | Yes | Yes | No | Yes | High (7.5)  
[CVE-2026-3784](https://security-tracker.debian.org/tracker/CVE-2026-3784) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-1965](https://security-tracker.debian.org/tracker/CVE-2026-1965) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-29111](https://security-tracker.debian.org/tracker/CVE-2026-29111) | Yes | Yes | No | Yes | Medium (5.5)  
[CVE-2026-3783](https://security-tracker.debian.org/tracker/CVE-2026-3783) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2025-0167](https://security-tracker.debian.org/tracker/CVE-2025-0167) | Yes | Yes | No | Yes | Low (3.4)  
  
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade). Cloud Service Mesh 1.27.8-asm.9 uses Envoy 1.35.10-dev.

### Announcement

**1.27.8-asm.9 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-33186](https://security-tracker.debian.org/tracker/CVE-2026-33186) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-3731](https://security-tracker.debian.org/tracker/CVE-2026-3731) | Yes | Yes | No | Yes | High (7.5)  
[CVE-2026-3784](https://security-tracker.debian.org/tracker/CVE-2026-3784) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-1965](https://security-tracker.debian.org/tracker/CVE-2026-1965) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-29111](https://security-tracker.debian.org/tracker/CVE-2026-29111) | Yes | Yes | No | Yes | Medium (5.5)  
[CVE-2026-3783](https://security-tracker.debian.org/tracker/CVE-2026-3783) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2025-0167](https://security-tracker.debian.org/tracker/CVE-2025-0167) | Yes | Yes | No | Yes | Low (3.4)  
  
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade). Cloud Service Mesh 1.27.8-asm.9 uses Envoy 1.35.10-dev.

**Managed Cloud Service Mesh**

### Announcement

The following images are now rolling out for managed Cloud Service Mesh:

  * 1.21.6-asm.19 is rolling out to the rapid release channel.
  * 1.20.8-asm.73 is rolling out to the regular release channel.
  * 1.19.10-asm.66 is rolling out to the stable release channel.



These patch releases contain the fixes for the following CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | MDPC | Severity  
---|---|---|---|---|---|---  
[CVE-2022-27943](https://security-tracker.debian.org/tracker/CVE-2022-27943) | Yes | Yes | Yes | No | No | Medium (5.5)  
[CVE-2023-4039](https://security-tracker.debian.org/tracker/CVE-2023-4039) | Yes | Yes | Yes | No | No | Medium (4.8)  
[CVE-2023-4527](https://security-tracker.debian.org/tracker/CVE-2023-4527) | Yes | Yes | Yes | No | No | Medium (6.5)  
[CVE-2023-4806](https://security-tracker.debian.org/tracker/CVE-2023-4806) | Yes | Yes | Yes | No | No | Medium (5.9)  
[CVE-2023-4911](https://security-tracker.debian.org/tracker/CVE-2023-4911) | Yes | Yes | Yes | No | No | High (7.8)  
[CVE-2023-5156](https://security-tracker.debian.org/tracker/CVE-2023-5156) | Yes | Yes | Yes | No | No | High (7.5)  
[CVE-2023-6246](https://security-tracker.debian.org/tracker/CVE-2023-6246) | Yes | Yes | Yes | No | No | High (7.8)  
[CVE-2024-2961](https://security-tracker.debian.org/tracker/CVE-2024-2961) | Yes | Yes | Yes | No | No | High (7.3)  
[CVE-2024-33599](https://security-tracker.debian.org/tracker/CVE-2024-33599) | Yes | Yes | Yes | No | No | High (8.1)  
[CVE-2024-33600](https://security-tracker.debian.org/tracker/CVE-2024-33600) | Yes | Yes | Yes | No | No | Medium (5.9)  
[CVE-2024-33601](https://security-tracker.debian.org/tracker/CVE-2024-33601) | Yes | Yes | Yes | No | No | High (7.3)  
[CVE-2024-33602](https://security-tracker.debian.org/tracker/CVE-2024-33602) | Yes | Yes | Yes | No | No | High (7.4)  
[CVE-2025-0167](https://security-tracker.debian.org/tracker/CVE-2025-0167) | Yes | Yes | No | No | No | Low (3.4)  
[CVE-2025-0395](https://security-tracker.debian.org/tracker/CVE-2025-0395) | Yes | Yes | Yes | Yes | No | Medium (6.2)  
[CVE-2025-15281](https://security-tracker.debian.org/tracker/CVE-2025-15281) | Yes | Yes | Yes | No | No | High (7.5)  
[CVE-2025-4802](https://security-tracker.debian.org/tracker/CVE-2025-4802) | Yes | Yes | Yes | Yes | No | High (7.8)  
[CVE-2025-68972](https://security-tracker.debian.org/tracker/CVE-2025-68972) | Yes | Yes | No | No | No | Medium (4.7)  
[CVE-2025-8058](https://security-tracker.debian.org/tracker/CVE-2025-8058) | Yes | Yes | Yes | No | No | Low (0.0)  
[CVE-2025-8941](https://security-tracker.debian.org/tracker/CVE-2025-8941) | Yes | Yes | No | No | No | Low (0.0)  
[CVE-2026-0861](https://security-tracker.debian.org/tracker/CVE-2026-0861) | Yes | Yes | Yes | No | No | High (8.4)  
[CVE-2026-0915](https://security-tracker.debian.org/tracker/CVE-2026-0915) | Yes | Yes | Yes | No | No | High (7.5)  
[CVE-2026-1965](https://security-tracker.debian.org/tracker/CVE-2026-1965) | Yes | Yes | No | Yes | Yes | Medium (6.5)  
[CVE-2026-29111](https://security-tracker.debian.org/tracker/CVE-2026-29111) | Yes | Yes | No | Yes | Yes | Medium (5.5)  
[CVE-2026-33186](https://security-tracker.debian.org/tracker/CVE-2026-33186) | Yes | Yes | Yes | No | No | Critical (9.1)  
[CVE-2026-3731](https://security-tracker.debian.org/tracker/CVE-2026-3731) | Yes | Yes | No | Yes | Yes | High (7.5)  
[CVE-2026-3783](https://security-tracker.debian.org/tracker/CVE-2026-3783) | Yes | Yes | No | Yes | Yes | Medium (5.3)  
[CVE-2026-3784](https://security-tracker.debian.org/tracker/CVE-2026-3784) | Yes | Yes | No | No | No | Medium (6.5)  
  
### Announcement

The following images are now rolling out for managed Cloud Service Mesh:

  * 1.21.6-asm.19 is rolling out to the rapid release channel.
  * 1.20.8-asm.73 is rolling out to the regular release channel.
  * 1.19.10-asm.66 is rolling out to the stable release channel.



These patch releases contain the fixes for the following CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | MDPC | Severity  
---|---|---|---|---|---|---  
[CVE-2022-27943](https://security-tracker.debian.org/tracker/CVE-2022-27943) | Yes | Yes | Yes | No | No | Medium (5.5)  
[CVE-2023-4039](https://security-tracker.debian.org/tracker/CVE-2023-4039) | Yes | Yes | Yes | No | No | Medium (4.8)  
[CVE-2023-4527](https://security-tracker.debian.org/tracker/CVE-2023-4527) | Yes | Yes | Yes | No | No | Medium (6.5)  
[CVE-2023-4806](https://security-tracker.debian.org/tracker/CVE-2023-4806) | Yes | Yes | Yes | No | No | Medium (5.9)  
[CVE-2023-4911](https://security-tracker.debian.org/tracker/CVE-2023-4911) | Yes | Yes | Yes | No | No | High (7.8)  
[CVE-2023-5156](https://security-tracker.debian.org/tracker/CVE-2023-5156) | Yes | Yes | Yes | No | No | High (7.5)  
[CVE-2023-6246](https://security-tracker.debian.org/tracker/CVE-2023-6246) | Yes | Yes | Yes | No | No | High (7.8)  
[CVE-2024-2961](https://security-tracker.debian.org/tracker/CVE-2024-2961) | Yes | Yes | Yes | No | No | High (7.3)  
[CVE-2024-33599](https://security-tracker.debian.org/tracker/CVE-2024-33599) | Yes | Yes | Yes | No | No | High (8.1)  
[CVE-2024-33600](https://security-tracker.debian.org/tracker/CVE-2024-33600) | Yes | Yes | Yes | No | No | Medium (5.9)  
[CVE-2024-33601](https://security-tracker.debian.org/tracker/CVE-2024-33601) | Yes | Yes | Yes | No | No | High (7.3)  
[CVE-2024-33602](https://security-tracker.debian.org/tracker/CVE-2024-33602) | Yes | Yes | Yes | No | No | High (7.4)  
[CVE-2025-0167](https://security-tracker.debian.org/tracker/CVE-2025-0167) | Yes | Yes | No | No | No | Low (3.4)  
[CVE-2025-0395](https://security-tracker.debian.org/tracker/CVE-2025-0395) | Yes | Yes | Yes | Yes | No | Medium (6.2)  
[CVE-2025-15281](https://security-tracker.debian.org/tracker/CVE-2025-15281) | Yes | Yes | Yes | No | No | High (7.5)  
[CVE-2025-4802](https://security-tracker.debian.org/tracker/CVE-2025-4802) | Yes | Yes | Yes | Yes | No | High (7.8)  
[CVE-2025-68972](https://security-tracker.debian.org/tracker/CVE-2025-68972) | Yes | Yes | No | No | No | Medium (4.7)  
[CVE-2025-8058](https://security-tracker.debian.org/tracker/CVE-2025-8058) | Yes | Yes | Yes | No | No | Low (0.0)  
[CVE-2025-8941](https://security-tracker.debian.org/tracker/CVE-2025-8941) | Yes | Yes | No | No | No | Low (0.0)  
[CVE-2026-0861](https://security-tracker.debian.org/tracker/CVE-2026-0861) | Yes | Yes | Yes | No | No | High (8.4)  
[CVE-2026-0915](https://security-tracker.debian.org/tracker/CVE-2026-0915) | Yes | Yes | Yes | No | No | High (7.5)  
[CVE-2026-1965](https://security-tracker.debian.org/tracker/CVE-2026-1965) | Yes | Yes | No | Yes | Yes | Medium (6.5)  
[CVE-2026-29111](https://security-tracker.debian.org/tracker/CVE-2026-29111) | Yes | Yes | No | Yes | Yes | Medium (5.5)  
[CVE-2026-33186](https://security-tracker.debian.org/tracker/CVE-2026-33186) | Yes | Yes | Yes | No | No | Critical (9.1)  
[CVE-2026-3731](https://security-tracker.debian.org/tracker/CVE-2026-3731) | Yes | Yes | No | Yes | Yes | High (7.5)  
[CVE-2026-3783](https://security-tracker.debian.org/tracker/CVE-2026-3783) | Yes | Yes | No | Yes | Yes | Medium (5.3)  
[CVE-2026-3784](https://security-tracker.debian.org/tracker/CVE-2026-3784) | Yes | Yes | No | No | No | Medium (6.5)  
  
### Announcement

The following images are now rolling out for managed Cloud Service Mesh:

  * 1.21.6-asm.19 is rolling out to the rapid release channel.
  * 1.20.8-asm.73 is rolling out to the regular release channel.
  * 1.19.10-asm.66 is rolling out to the stable release channel.



These patch releases contain the fixes for the following CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | MDPC | Severity  
---|---|---|---|---|---|---  
[CVE-2022-27943](https://security-tracker.debian.org/tracker/CVE-2022-27943) | Yes | Yes | Yes | No | No | Medium (5.5)  
[CVE-2023-4039](https://security-tracker.debian.org/tracker/CVE-2023-4039) | Yes | Yes | Yes | No | No | Medium (4.8)  
[CVE-2023-4527](https://security-tracker.debian.org/tracker/CVE-2023-4527) | Yes | Yes | Yes | No | No | Medium (6.5)  
[CVE-2023-4806](https://security-tracker.debian.org/tracker/CVE-2023-4806) | Yes | Yes | Yes | No | No | Medium (5.9)  
[CVE-2023-4911](https://security-tracker.debian.org/tracker/CVE-2023-4911) | Yes | Yes | Yes | No | No | High (7.8)  
[CVE-2023-5156](https://security-tracker.debian.org/tracker/CVE-2023-5156) | Yes | Yes | Yes | No | No | High (7.5)  
[CVE-2023-6246](https://security-tracker.debian.org/tracker/CVE-2023-6246) | Yes | Yes | Yes | No | No | High (7.8)  
[CVE-2024-2961](https://security-tracker.debian.org/tracker/CVE-2024-2961) | Yes | Yes | Yes | No | No | High (7.3)  
[CVE-2024-33599](https://security-tracker.debian.org/tracker/CVE-2024-33599) | Yes | Yes | Yes | No | No | High (8.1)  
[CVE-2024-33600](https://security-tracker.debian.org/tracker/CVE-2024-33600) | Yes | Yes | Yes | No | No | Medium (5.9)  
[CVE-2024-33601](https://security-tracker.debian.org/tracker/CVE-2024-33601) | Yes | Yes | Yes | No | No | High (7.3)  
[CVE-2024-33602](https://security-tracker.debian.org/tracker/CVE-2024-33602) | Yes | Yes | Yes | No | No | High (7.4)  
[CVE-2025-0167](https://security-tracker.debian.org/tracker/CVE-2025-0167) | Yes | Yes | No | No | No | Low (3.4)  
[CVE-2025-0395](https://security-tracker.debian.org/tracker/CVE-2025-0395) | Yes | Yes | Yes | Yes | No | Medium (6.2)  
[CVE-2025-15281](https://security-tracker.debian.org/tracker/CVE-2025-15281) | Yes | Yes | Yes | No | No | High (7.5)  
[CVE-2025-4802](https://security-tracker.debian.org/tracker/CVE-2025-4802) | Yes | Yes | Yes | Yes | No | High (7.8)  
[CVE-2025-68972](https://security-tracker.debian.org/tracker/CVE-2025-68972) | Yes | Yes | No | No | No | Medium (4.7)  
[CVE-2025-8058](https://security-tracker.debian.org/tracker/CVE-2025-8058) | Yes | Yes | Yes | No | No | Low (0.0)  
[CVE-2025-8941](https://security-tracker.debian.org/tracker/CVE-2025-8941) | Yes | Yes | No | No | No | Low (0.0)  
[CVE-2026-0861](https://security-tracker.debian.org/tracker/CVE-2026-0861) | Yes | Yes | Yes | No | No | High (8.4)  
[CVE-2026-0915](https://security-tracker.debian.org/tracker/CVE-2026-0915) | Yes | Yes | Yes | No | No | High (7.5)  
[CVE-2026-1965](https://security-tracker.debian.org/tracker/CVE-2026-1965) | Yes | Yes | No | Yes | Yes | Medium (6.5)  
[CVE-2026-29111](https://security-tracker.debian.org/tracker/CVE-2026-29111) | Yes | Yes | No | Yes | Yes | Medium (5.5)  
[CVE-2026-33186](https://security-tracker.debian.org/tracker/CVE-2026-33186) | Yes | Yes | Yes | No | No | Critical (9.1)  
[CVE-2026-3731](https://security-tracker.debian.org/tracker/CVE-2026-3731) | Yes | Yes | No | Yes | Yes | High (7.5)  
[CVE-2026-3783](https://security-tracker.debian.org/tracker/CVE-2026-3783) | Yes | Yes | No | Yes | Yes | Medium (5.3)  
[CVE-2026-3784](https://security-tracker.debian.org/tracker/CVE-2026-3784) | Yes | Yes | No | No | No | Medium (6.5)  
**1.26.x**

### Announcement

**1.26.8-asm.5 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-33186](https://security-tracker.debian.org/tracker/CVE-2026-33186) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-3731](https://security-tracker.debian.org/tracker/CVE-2026-3731) | Yes | Yes | No | Yes | High (7.5)  
[CVE-2026-3784](https://security-tracker.debian.org/tracker/CVE-2026-3784) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-1965](https://security-tracker.debian.org/tracker/CVE-2026-1965) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-29111](https://security-tracker.debian.org/tracker/CVE-2026-29111) | Yes | Yes | No | Yes | Medium (5.5)  
[CVE-2026-3783](https://security-tracker.debian.org/tracker/CVE-2026-3783) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2025-68972](https://security-tracker.debian.org/tracker/CVE-2025-68972) | Yes | No | No | Yes | Medium (4.7)  
[CVE-2025-0167](https://security-tracker.debian.org/tracker/CVE-2025-0167) | Yes | Yes | No | Yes | Low (3.4)  
[CVE-2025-8941](https://security-tracker.debian.org/tracker/CVE-2025-8941) | Yes | No | No | Yes | Low (0.0)  
  
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/upgrade/upgrade). Cloud Service Mesh 1.26.8-asm.5 uses Envoy 1.34.14-dev.

### Announcement

**1.26.8-asm.5 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-33186](https://security-tracker.debian.org/tracker/CVE-2026-33186) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-3731](https://security-tracker.debian.org/tracker/CVE-2026-3731) | Yes | Yes | No | Yes | High (7.5)  
[CVE-2026-3784](https://security-tracker.debian.org/tracker/CVE-2026-3784) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-1965](https://security-tracker.debian.org/tracker/CVE-2026-1965) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-29111](https://security-tracker.debian.org/tracker/CVE-2026-29111) | Yes | Yes | No | Yes | Medium (5.5)  
[CVE-2026-3783](https://security-tracker.debian.org/tracker/CVE-2026-3783) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2025-68972](https://security-tracker.debian.org/tracker/CVE-2025-68972) | Yes | No | No | Yes | Medium (4.7)  
[CVE-2025-0167](https://security-tracker.debian.org/tracker/CVE-2025-0167) | Yes | Yes | No | Yes | Low (3.4)  
[CVE-2025-8941](https://security-tracker.debian.org/tracker/CVE-2025-8941) | Yes | No | No | Yes | Low (0.0)  
  
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/upgrade/upgrade). Cloud Service Mesh 1.26.8-asm.5 uses Envoy 1.34.14-dev.

### Announcement

**1.26.8-asm.5 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2026-33186](https://security-tracker.debian.org/tracker/CVE-2026-33186) | Yes | Yes | Yes | Yes | Critical (9.1)  
[CVE-2026-3731](https://security-tracker.debian.org/tracker/CVE-2026-3731) | Yes | Yes | No | Yes | High (7.5)  
[CVE-2026-3784](https://security-tracker.debian.org/tracker/CVE-2026-3784) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-1965](https://security-tracker.debian.org/tracker/CVE-2026-1965) | Yes | Yes | No | Yes | Medium (6.5)  
[CVE-2026-29111](https://security-tracker.debian.org/tracker/CVE-2026-29111) | Yes | Yes | No | Yes | Medium (5.5)  
[CVE-2026-3783](https://security-tracker.debian.org/tracker/CVE-2026-3783) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2025-68972](https://security-tracker.debian.org/tracker/CVE-2025-68972) | Yes | No | No | Yes | Medium (4.7)  
[CVE-2025-0167](https://security-tracker.debian.org/tracker/CVE-2025-0167) | Yes | Yes | No | Yes | Low (3.4)  
[CVE-2025-8941](https://security-tracker.debian.org/tracker/CVE-2025-8941) | Yes | No | No | Yes | Low (0.0)  
  
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/upgrade/upgrade). Cloud Service Mesh 1.26.8-asm.5 uses Envoy 1.34.14-dev.

]]> April 02, 2026tag:google.com,2016:servicemesh-release-notes#April_02_20262026-04-02T00:00:00-07:00Managed Cloud Service Mesh 

### Announcement

Managed Cloud Service Mesh using the `TRAFFIC_DIRECTOR` implementation now supports a limited implementation of the `EnvoyFilter` API. To learn about the supported fields, extensions, and how to use `EnvoyFilter` for features like local rate limiting see [Data plane extensibility with `EnvoyFilter`](https://docs.cloud.google.com/service-mesh/v1.29/docs/data-plane-extensibility).

To troubleshoot any issue while configuring, see [Resolving data plane extensibility issues](https://docs.cloud.google.com/service-mesh/v1.29/docs/troubleshooting/troubleshoot-data-plane-extensibility).

### Announcement

Managed Cloud Service Mesh using the `TRAFFIC_DIRECTOR` implementation now supports a limited implementation of the `EnvoyFilter` API. To learn about the supported fields, extensions, and how to use `EnvoyFilter` for features like local rate limiting see [Data plane extensibility with `EnvoyFilter`](https://docs.cloud.google.com/service-mesh/v1.28/docs/data-plane-extensibility).

To troubleshoot any issue while configuring, see [Resolving data plane extensibility issues](https://docs.cloud.google.com/service-mesh/v1.28/docs/troubleshooting/troubleshoot-data-plane-extensibility).

### Announcement

Managed Cloud Service Mesh using the `TRAFFIC_DIRECTOR` implementation now supports a limited implementation of the `EnvoyFilter` API. To learn about the supported fields, extensions, and how to use `EnvoyFilter` for features like local rate limiting see [Data plane extensibility with `EnvoyFilter`](https://docs.cloud.google.com/service-mesh/docs/data-plane-extensibility).

To troubleshoot any issue while configuring, see [Resolving data plane extensibility issues](https://docs.cloud.google.com/service-mesh/docs/troubleshooting/troubleshoot-data-plane-extensibility).

]]> March 11, 2026tag:google.com,2016:servicemesh-release-notes#March_11_20262026-03-11T00:00:00-07:001.27.x 

### Security

**1.28.5-asm.9 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2026-013](https://docs.cloud.google.com/service-mesh/v1.29/docs/security-bulletins#gcp-2026-013) as well as fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2025-13151](https://ubuntu.com/security/CVE-2025-13151) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2025-14831](https://ubuntu.com/security/CVE-2025-14831) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2025-15281](https://ubuntu.com/security/CVE-2025-15281) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2025-15467](https://ubuntu.com/security/CVE-2025-15467) | Yes | Yes | No | Yes | Medium (9.8)  
[CVE-2025-15558](https://ubuntu.com/security/CVE-2025-15558) | Yes | Yes | Yes | - | High (8.0)  
[CVE-2025-61726](https://ubuntu.com/security/CVE-2025-61726) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2025-61728](https://ubuntu.com/security/CVE-2025-61728) | Yes | Yes | Yes | Yes | Medium (6.5)  
[CVE-2025-61730](https://ubuntu.com/security/CVE-2025-61730) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2025-61731](https://ubuntu.com/security/CVE-2025-61731) | Yes | Yes | Yes | Yes | High (7.8)  
[CVE-2025-61732](https://ubuntu.com/security/CVE-2025-61732) | Yes | Yes | Yes | Yes | High (8.6)  
[CVE-2025-68121](https://ubuntu.com/security/CVE-2025-68121) | Yes | Yes | Yes | Yes | Critical (10)  
[CVE-2025-68160](https://ubuntu.com/security/CVE-2025-68160) | Yes | Yes | No | Yes | Low (4.7)  
[CVE-2025-69418](https://ubuntu.com/security/CVE-2025-69418) | Yes | Yes | No | Yes | Low (4.0)  
[CVE-2025-69419](https://ubuntu.com/security/CVE-2025-69419) | Yes | Yes | No | Yes | Low (7.4)  
[CVE-2025-69420](https://ubuntu.com/security/CVE-2025-69420) | Yes | Yes | Yes | Yes | Low (7.5)  
[CVE-2025-69421](https://ubuntu.com/security/CVE-2025-69421) | Yes | Yes | Yes | Yes | Low (7.5)  
[CVE-2025-8277](https://ubuntu.com/security/CVE-2025-8277) | Yes | Yes | No | Yes | Low (0)  
[CVE-2025-9820](https://ubuntu.com/security/CVE-2025-9820) | Yes | Yes | No | Yes | Low (4)  
[CVE-2026-0861](https://ubuntu.com/security/CVE-2026-0861) | Yes | Yes | No | Yes | Medium (8.4)  
[CVE-2026-0915](https://ubuntu.com/security/CVE-2026-0915) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-0964](https://ubuntu.com/security/CVE-2026-0964) | Yes | Yes | No | Yes | Medium  
[CVE-2026-0965](https://ubuntu.com/security/CVE-2026-0965) | Yes | Yes | No | Yes | Low  
[CVE-2026-0966](https://ubuntu.com/security/CVE-2026-0966) | Yes | Yes | No | Yes | Low  
[CVE-2026-0967](https://ubuntu.com/security/CVE-2026-0967) | Yes | Yes | No | Yes | Medium  
[CVE-2026-0968](https://ubuntu.com/security/CVE-2026-0968) | Yes | Yes | No | Yes | Medium  
[CVE-2026-22795](https://ubuntu.com/security/CVE-2026-22795) | Yes | Yes | No | Yes | Low (5.5)  
[CVE-2026-22796](https://ubuntu.com/security/CVE-2026-22796) | Yes | Yes | No | Yes | Low (5.3)  
[CVE-2026-24051](https://ubuntu.com/security/CVE-2026-24051) | Yes | Yes | Yes | Yes | High (7.0)  
[CVE-2026-25679](https://ubuntu.com/security/CVE-2026-25679) | Yes | Yes | Yes | Yes | High (7.5)  
  
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade). Cloud Service Mesh 1.28.5-asm.9 uses Envoy 1.36.5.

### Security

**1.28.5-asm.9 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2026-013](https://docs.cloud.google.com/service-mesh/v1.28/docs/security-bulletins#gcp-2026-013) as well as fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2025-13151](https://ubuntu.com/security/CVE-2025-13151) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2025-14831](https://ubuntu.com/security/CVE-2025-14831) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2025-15281](https://ubuntu.com/security/CVE-2025-15281) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2025-15467](https://ubuntu.com/security/CVE-2025-15467) | Yes | Yes | No | Yes | Medium (9.8)  
[CVE-2025-15558](https://ubuntu.com/security/CVE-2025-15558) | Yes | Yes | Yes | - | High (8.0)  
[CVE-2025-61726](https://ubuntu.com/security/CVE-2025-61726) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2025-61728](https://ubuntu.com/security/CVE-2025-61728) | Yes | Yes | Yes | Yes | Medium (6.5)  
[CVE-2025-61730](https://ubuntu.com/security/CVE-2025-61730) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2025-61731](https://ubuntu.com/security/CVE-2025-61731) | Yes | Yes | Yes | Yes | High (7.8)  
[CVE-2025-61732](https://ubuntu.com/security/CVE-2025-61732) | Yes | Yes | Yes | Yes | High (8.6)  
[CVE-2025-68121](https://ubuntu.com/security/CVE-2025-68121) | Yes | Yes | Yes | Yes | Critical (10)  
[CVE-2025-68160](https://ubuntu.com/security/CVE-2025-68160) | Yes | Yes | No | Yes | Low (4.7)  
[CVE-2025-69418](https://ubuntu.com/security/CVE-2025-69418) | Yes | Yes | No | Yes | Low (4.0)  
[CVE-2025-69419](https://ubuntu.com/security/CVE-2025-69419) | Yes | Yes | No | Yes | Low (7.4)  
[CVE-2025-69420](https://ubuntu.com/security/CVE-2025-69420) | Yes | Yes | Yes | Yes | Low (7.5)  
[CVE-2025-69421](https://ubuntu.com/security/CVE-2025-69421) | Yes | Yes | Yes | Yes | Low (7.5)  
[CVE-2025-8277](https://ubuntu.com/security/CVE-2025-8277) | Yes | Yes | No | Yes | Low (0)  
[CVE-2025-9820](https://ubuntu.com/security/CVE-2025-9820) | Yes | Yes | No | Yes | Low (4)  
[CVE-2026-0861](https://ubuntu.com/security/CVE-2026-0861) | Yes | Yes | No | Yes | Medium (8.4)  
[CVE-2026-0915](https://ubuntu.com/security/CVE-2026-0915) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-0964](https://ubuntu.com/security/CVE-2026-0964) | Yes | Yes | No | Yes | Medium  
[CVE-2026-0965](https://ubuntu.com/security/CVE-2026-0965) | Yes | Yes | No | Yes | Low  
[CVE-2026-0966](https://ubuntu.com/security/CVE-2026-0966) | Yes | Yes | No | Yes | Low  
[CVE-2026-0967](https://ubuntu.com/security/CVE-2026-0967) | Yes | Yes | No | Yes | Medium  
[CVE-2026-0968](https://ubuntu.com/security/CVE-2026-0968) | Yes | Yes | No | Yes | Medium  
[CVE-2026-22795](https://ubuntu.com/security/CVE-2026-22795) | Yes | Yes | No | Yes | Low (5.5)  
[CVE-2026-22796](https://ubuntu.com/security/CVE-2026-22796) | Yes | Yes | No | Yes | Low (5.3)  
[CVE-2026-24051](https://ubuntu.com/security/CVE-2026-24051) | Yes | Yes | Yes | Yes | High (7.0)  
[CVE-2026-25679](https://ubuntu.com/security/CVE-2026-25679) | Yes | Yes | Yes | Yes | High (7.5)  
  
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade). Cloud Service Mesh 1.28.5-asm.9 uses Envoy 1.36.5.

### Security

**1.28.5-asm.9 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2026-013](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-013) as well as fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2025-13151](https://ubuntu.com/security/CVE-2025-13151) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2025-14831](https://ubuntu.com/security/CVE-2025-14831) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2025-15281](https://ubuntu.com/security/CVE-2025-15281) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2025-15467](https://ubuntu.com/security/CVE-2025-15467) | Yes | Yes | No | Yes | Medium (9.8)  
[CVE-2025-15558](https://ubuntu.com/security/CVE-2025-15558) | Yes | Yes | Yes | - | High (8.0)  
[CVE-2025-61726](https://ubuntu.com/security/CVE-2025-61726) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2025-61728](https://ubuntu.com/security/CVE-2025-61728) | Yes | Yes | Yes | Yes | Medium (6.5)  
[CVE-2025-61730](https://ubuntu.com/security/CVE-2025-61730) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2025-61731](https://ubuntu.com/security/CVE-2025-61731) | Yes | Yes | Yes | Yes | High (7.8)  
[CVE-2025-61732](https://ubuntu.com/security/CVE-2025-61732) | Yes | Yes | Yes | Yes | High (8.6)  
[CVE-2025-68121](https://ubuntu.com/security/CVE-2025-68121) | Yes | Yes | Yes | Yes | Critical (10)  
[CVE-2025-68160](https://ubuntu.com/security/CVE-2025-68160) | Yes | Yes | No | Yes | Low (4.7)  
[CVE-2025-69418](https://ubuntu.com/security/CVE-2025-69418) | Yes | Yes | No | Yes | Low (4.0)  
[CVE-2025-69419](https://ubuntu.com/security/CVE-2025-69419) | Yes | Yes | No | Yes | Low (7.4)  
[CVE-2025-69420](https://ubuntu.com/security/CVE-2025-69420) | Yes | Yes | Yes | Yes | Low (7.5)  
[CVE-2025-69421](https://ubuntu.com/security/CVE-2025-69421) | Yes | Yes | Yes | Yes | Low (7.5)  
[CVE-2025-8277](https://ubuntu.com/security/CVE-2025-8277) | Yes | Yes | No | Yes | Low (0)  
[CVE-2025-9820](https://ubuntu.com/security/CVE-2025-9820) | Yes | Yes | No | Yes | Low (4)  
[CVE-2026-0861](https://ubuntu.com/security/CVE-2026-0861) | Yes | Yes | No | Yes | Medium (8.4)  
[CVE-2026-0915](https://ubuntu.com/security/CVE-2026-0915) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-0964](https://ubuntu.com/security/CVE-2026-0964) | Yes | Yes | No | Yes | Medium  
[CVE-2026-0965](https://ubuntu.com/security/CVE-2026-0965) | Yes | Yes | No | Yes | Low  
[CVE-2026-0966](https://ubuntu.com/security/CVE-2026-0966) | Yes | Yes | No | Yes | Low  
[CVE-2026-0967](https://ubuntu.com/security/CVE-2026-0967) | Yes | Yes | No | Yes | Medium  
[CVE-2026-0968](https://ubuntu.com/security/CVE-2026-0968) | Yes | Yes | No | Yes | Medium  
[CVE-2026-22795](https://ubuntu.com/security/CVE-2026-22795) | Yes | Yes | No | Yes | Low (5.5)  
[CVE-2026-22796](https://ubuntu.com/security/CVE-2026-22796) | Yes | Yes | No | Yes | Low (5.3)  
[CVE-2026-24051](https://ubuntu.com/security/CVE-2026-24051) | Yes | Yes | Yes | Yes | High (7.0)  
[CVE-2026-25679](https://ubuntu.com/security/CVE-2026-25679) | Yes | Yes | Yes | Yes | High (7.5)  
  
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh 1.28.5-asm.9 uses Envoy 1.36.5.

### Security

**1.27.8-asm.7 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2026-013](https://docs.cloud.google.com/service-mesh/v1.29/docs/security-bulletins#gcp-2026-013) as well as fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2025-13151](https://ubuntu.com/security/CVE-2025-13151) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2025-14831](https://ubuntu.com/security/CVE-2025-14831) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2025-15281](https://ubuntu.com/security/CVE-2025-15281) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2025-15467](https://ubuntu.com/security/CVE-2025-15467) | Yes | Yes | Yes | Yes | Medium (9.8)  
[CVE-2025-15558](https://ubuntu.com/security/CVE-2025-15558) | Yes | Yes | Yes | - | High (8.0)  
[CVE-2025-61726](https://ubuntu.com/security/CVE-2025-61726) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2025-61728](https://ubuntu.com/security/CVE-2025-61728) | Yes | Yes | Yes | Yes | Medium (6.5)  
[CVE-2025-61730](https://ubuntu.com/security/CVE-2025-61730) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2025-61731](https://ubuntu.com/security/CVE-2025-61731) | Yes | Yes | Yes | Yes | High (7.8)  
[CVE-2025-61732](https://ubuntu.com/security/CVE-2025-61732) | Yes | Yes | Yes | Yes | High (8.6)  
[CVE-2025-68121](https://ubuntu.com/security/CVE-2025-68121) | Yes | Yes | Yes | Yes | Critical (10)  
[CVE-2025-68160](https://ubuntu.com/security/CVE-2025-68160) | Yes | Yes | No | Yes | Low (4.7)  
[CVE-2025-69418](https://ubuntu.com/security/CVE-2025-69418) | Yes | Yes | No | Yes | Low (4.0)  
[CVE-2025-69419](https://ubuntu.com/security/CVE-2025-69419) | Yes | Yes | No | Yes | Low (7.4)  
[CVE-2025-69420](https://ubuntu.com/security/CVE-2025-69420) | Yes | Yes | Yes | Yes | Low (7.5)  
[CVE-2025-69421](https://ubuntu.com/security/CVE-2025-69421) | Yes | Yes | Yes | Yes | Low (7.5)  
[CVE-2025-8277](https://ubuntu.com/security/CVE-2025-8277) | Yes | Yes | No | Yes | Low (0)  
[CVE-2025-9820](https://ubuntu.com/security/CVE-2025-9820) | Yes | Yes | No | Yes | Low (4)  
[CVE-2026-0861](https://ubuntu.com/security/CVE-2026-0861) | Yes | Yes | No | Yes | Medium (8.4)  
[CVE-2026-0915](https://ubuntu.com/security/CVE-2026-0915) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-0964](https://ubuntu.com/security/CVE-2026-0964) | Yes | Yes | No | Yes | Medium  
[CVE-2026-0965](https://ubuntu.com/security/CVE-2026-0965) | Yes | Yes | No | Yes | Low  
[CVE-2026-0966](https://ubuntu.com/security/CVE-2026-0966) | Yes | Yes | No | Yes | Low  
[CVE-2026-0967](https://ubuntu.com/security/CVE-2026-0967) | Yes | Yes | No | Yes | Medium  
[CVE-2026-0968](https://ubuntu.com/security/CVE-2026-0968) | Yes | Yes | No | Yes | Medium  
[CVE-2026-22795](https://ubuntu.com/security/CVE-2026-22795) | Yes | Yes | No | Yes | Low (5.5)  
[CVE-2026-22796](https://ubuntu.com/security/CVE-2026-22796) | Yes | Yes | No | Yes | Low (5.3)  
[CVE-2026-24051](https://ubuntu.com/security/CVE-2026-24051) | Yes | Yes | Yes | Yes | High (7.0)  
[CVE-2026-25679](https://ubuntu.com/security/CVE-2026-25679) | Yes | Yes | Yes | Yes | High (7.5)  
  
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade). Cloud Service Mesh 1.27.8-asm.7 uses Envoy 1.35.9.

### Security

**1.27.8-asm.7 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2026-013](https://docs.cloud.google.com/service-mesh/v1.28/docs/security-bulletins#gcp-2026-013) as well as fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2025-13151](https://ubuntu.com/security/CVE-2025-13151) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2025-14831](https://ubuntu.com/security/CVE-2025-14831) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2025-15281](https://ubuntu.com/security/CVE-2025-15281) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2025-15467](https://ubuntu.com/security/CVE-2025-15467) | Yes | Yes | Yes | Yes | Medium (9.8)  
[CVE-2025-15558](https://ubuntu.com/security/CVE-2025-15558) | Yes | Yes | Yes | - | High (8.0)  
[CVE-2025-61726](https://ubuntu.com/security/CVE-2025-61726) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2025-61728](https://ubuntu.com/security/CVE-2025-61728) | Yes | Yes | Yes | Yes | Medium (6.5)  
[CVE-2025-61730](https://ubuntu.com/security/CVE-2025-61730) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2025-61731](https://ubuntu.com/security/CVE-2025-61731) | Yes | Yes | Yes | Yes | High (7.8)  
[CVE-2025-61732](https://ubuntu.com/security/CVE-2025-61732) | Yes | Yes | Yes | Yes | High (8.6)  
[CVE-2025-68121](https://ubuntu.com/security/CVE-2025-68121) | Yes | Yes | Yes | Yes | Critical (10)  
[CVE-2025-68160](https://ubuntu.com/security/CVE-2025-68160) | Yes | Yes | No | Yes | Low (4.7)  
[CVE-2025-69418](https://ubuntu.com/security/CVE-2025-69418) | Yes | Yes | No | Yes | Low (4.0)  
[CVE-2025-69419](https://ubuntu.com/security/CVE-2025-69419) | Yes | Yes | No | Yes | Low (7.4)  
[CVE-2025-69420](https://ubuntu.com/security/CVE-2025-69420) | Yes | Yes | Yes | Yes | Low (7.5)  
[CVE-2025-69421](https://ubuntu.com/security/CVE-2025-69421) | Yes | Yes | Yes | Yes | Low (7.5)  
[CVE-2025-8277](https://ubuntu.com/security/CVE-2025-8277) | Yes | Yes | No | Yes | Low (0)  
[CVE-2025-9820](https://ubuntu.com/security/CVE-2025-9820) | Yes | Yes | No | Yes | Low (4)  
[CVE-2026-0861](https://ubuntu.com/security/CVE-2026-0861) | Yes | Yes | No | Yes | Medium (8.4)  
[CVE-2026-0915](https://ubuntu.com/security/CVE-2026-0915) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-0964](https://ubuntu.com/security/CVE-2026-0964) | Yes | Yes | No | Yes | Medium  
[CVE-2026-0965](https://ubuntu.com/security/CVE-2026-0965) | Yes | Yes | No | Yes | Low  
[CVE-2026-0966](https://ubuntu.com/security/CVE-2026-0966) | Yes | Yes | No | Yes | Low  
[CVE-2026-0967](https://ubuntu.com/security/CVE-2026-0967) | Yes | Yes | No | Yes | Medium  
[CVE-2026-0968](https://ubuntu.com/security/CVE-2026-0968) | Yes | Yes | No | Yes | Medium  
[CVE-2026-22795](https://ubuntu.com/security/CVE-2026-22795) | Yes | Yes | No | Yes | Low (5.5)  
[CVE-2026-22796](https://ubuntu.com/security/CVE-2026-22796) | Yes | Yes | No | Yes | Low (5.3)  
[CVE-2026-24051](https://ubuntu.com/security/CVE-2026-24051) | Yes | Yes | Yes | Yes | High (7.0)  
[CVE-2026-25679](https://ubuntu.com/security/CVE-2026-25679) | Yes | Yes | Yes | Yes | High (7.5)  
  
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade). Cloud Service Mesh 1.27.8-asm.7 uses Envoy 1.35.9.

### Security

**1.27.8-asm.7 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2026-013](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-013) as well as fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2025-13151](https://ubuntu.com/security/CVE-2025-13151) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2025-14831](https://ubuntu.com/security/CVE-2025-14831) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2025-15281](https://ubuntu.com/security/CVE-2025-15281) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2025-15467](https://ubuntu.com/security/CVE-2025-15467) | Yes | Yes | Yes | Yes | Medium (9.8)  
[CVE-2025-15558](https://ubuntu.com/security/CVE-2025-15558) | Yes | Yes | Yes | - | High (8.0)  
[CVE-2025-61726](https://ubuntu.com/security/CVE-2025-61726) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2025-61728](https://ubuntu.com/security/CVE-2025-61728) | Yes | Yes | Yes | Yes | Medium (6.5)  
[CVE-2025-61730](https://ubuntu.com/security/CVE-2025-61730) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2025-61731](https://ubuntu.com/security/CVE-2025-61731) | Yes | Yes | Yes | Yes | High (7.8)  
[CVE-2025-61732](https://ubuntu.com/security/CVE-2025-61732) | Yes | Yes | Yes | Yes | High (8.6)  
[CVE-2025-68121](https://ubuntu.com/security/CVE-2025-68121) | Yes | Yes | Yes | Yes | Critical (10)  
[CVE-2025-68160](https://ubuntu.com/security/CVE-2025-68160) | Yes | Yes | No | Yes | Low (4.7)  
[CVE-2025-69418](https://ubuntu.com/security/CVE-2025-69418) | Yes | Yes | No | Yes | Low (4.0)  
[CVE-2025-69419](https://ubuntu.com/security/CVE-2025-69419) | Yes | Yes | No | Yes | Low (7.4)  
[CVE-2025-69420](https://ubuntu.com/security/CVE-2025-69420) | Yes | Yes | Yes | Yes | Low (7.5)  
[CVE-2025-69421](https://ubuntu.com/security/CVE-2025-69421) | Yes | Yes | Yes | Yes | Low (7.5)  
[CVE-2025-8277](https://ubuntu.com/security/CVE-2025-8277) | Yes | Yes | No | Yes | Low (0)  
[CVE-2025-9820](https://ubuntu.com/security/CVE-2025-9820) | Yes | Yes | No | Yes | Low (4)  
[CVE-2026-0861](https://ubuntu.com/security/CVE-2026-0861) | Yes | Yes | No | Yes | Medium (8.4)  
[CVE-2026-0915](https://ubuntu.com/security/CVE-2026-0915) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-0964](https://ubuntu.com/security/CVE-2026-0964) | Yes | Yes | No | Yes | Medium  
[CVE-2026-0965](https://ubuntu.com/security/CVE-2026-0965) | Yes | Yes | No | Yes | Low  
[CVE-2026-0966](https://ubuntu.com/security/CVE-2026-0966) | Yes | Yes | No | Yes | Low  
[CVE-2026-0967](https://ubuntu.com/security/CVE-2026-0967) | Yes | Yes | No | Yes | Medium  
[CVE-2026-0968](https://ubuntu.com/security/CVE-2026-0968) | Yes | Yes | No | Yes | Medium  
[CVE-2026-22795](https://ubuntu.com/security/CVE-2026-22795) | Yes | Yes | No | Yes | Low (5.5)  
[CVE-2026-22796](https://ubuntu.com/security/CVE-2026-22796) | Yes | Yes | No | Yes | Low (5.3)  
[CVE-2026-24051](https://ubuntu.com/security/CVE-2026-24051) | Yes | Yes | Yes | Yes | High (7.0)  
[CVE-2026-25679](https://ubuntu.com/security/CVE-2026-25679) | Yes | Yes | Yes | Yes | High (7.5)  
  
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade). Cloud Service Mesh 1.27.8-asm.7 uses Envoy 1.35.9.

**Managed Cloud Service Mesh**

### Security

The following images are now rolling out for managed Cloud Service Mesh:

  * Sidecar version 1.21.6-asm.16 is rolling out to the rapid release channel.
  * Sidecar version 1.20.8-asm.68 is rolling out to the regular release channel.
  * Sidecar version 1.19.10-asm.61 is rolling out to the stable release channel.
  * CNI and managed data plane controller version 1.23.6-asm.31 is rolling out to all release channels.



These rollouts will preempt those previously announced on February 9, 2026.

Managed Cloud Service Mesh will start using proxy version csm_mesh_proxy.20260304_RC00 for Gateway API on GKE clusters for all channels. This proxy version maps closest to Envoy version 1.37.

These patch releases contain the fixes for the vulnerabilities listed in [GCP-2026-013](https://docs.cloud.google.com/service-mesh/v1.29/docs/security-bulletins#gcp-2026-013) as well as fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | MDPC | Severity  
---|---|---|---|---|---|---  
[CVE-2025-61726](https://ubuntu.com/security/CVE-2025-61726) | Yes | Yes | Yes | - | - | High (7.5)  
[CVE-2025-61728](https://ubuntu.com/security/CVE-2025-61728) | Yes | Yes | Yes | - | - | Medium (6.5)  
[CVE-2025-61730](https://ubuntu.com/security/CVE-2025-61730) | Yes | Yes | Yes | - | - | Medium (5.3)  
[CVE-2025-61731](https://ubuntu.com/security/CVE-2025-61731) | Yes | Yes | Yes | - | - | High (7.8)  
[CVE-2025-61732](https://ubuntu.com/security/CVE-2025-61732) | Yes | Yes | Yes | - | - | High (8.6)  
[CVE-2025-68121](https://ubuntu.com/security/CVE-2025-68121) | Yes | Yes | Yes | - | - | Critical (10)  
[CVE-2025-68160](https://ubuntu.com/security/CVE-2025-68160) | Yes | Yes | No | - | - | Low (4.7)  
[CVE-2025-69418](https://ubuntu.com/security/CVE-2025-69418) | Yes | Yes | No | - | - | Low (4.0)  
[CVE-2025-69419](https://ubuntu.com/security/CVE-2025-69419) | Yes | Yes | No | - | - | Low (7.4)  
[CVE-2025-69420](https://ubuntu.com/security/CVE-2025-69420) | Yes | Yes | No | - | - | Low (7.5)  
[CVE-2025-69421](https://ubuntu.com/security/CVE-2025-69421) | Yes | Yes | No | - | - | Low (7.5)  
[CVE-2025-8277](https://ubuntu.com/security/CVE-2025-8277) | - | - | - | Yes | Yes | Low (0)  
[CVE-2025-9820](https://ubuntu.com/security/CVE-2025-9820) | - | - | - | Yes | Yes | Low (4.0)  
[CVE-2025-14831](https://ubuntu.com/security/CVE-2025-14831) | - | - | - | Yes | Yes | Medium (5.3)  
[CVE-2025-15281](https://ubuntu.com/security/CVE-2025-15281) | Yes | Yes | Yes | - | - | Medium (7.5)  
[CVE-2025-15467](https://ubuntu.com/security/CVE-2025-15467) | Yes | Yes | No | - | - | Medium (9.8)  
[CVE-2026-0861](https://ubuntu.com/security/CVE-2026-0861) | Yes | Yes | No | - | - | Medium (8.4)  
[CVE-2026-0915](https://ubuntu.com/security/CVE-2026-0915) | Yes | Yes | No | - | - | Medium (7.5)  
[CVE-2026-0964](https://ubuntu.com/security/CVE-2026-0964) | - | - | - | Yes | Yes | Medium  
[CVE-2026-0965](https://ubuntu.com/security/CVE-2026-0965) | - | - | - | Yes | Yes | Low  
[CVE-2026-0966](https://ubuntu.com/security/CVE-2026-0966) | - | - | - | Yes | Yes | Low  
[CVE-2026-0967](https://ubuntu.com/security/CVE-2026-0967) | - | - | - | Yes | Yes | Medium  
[CVE-2026-0968](https://ubuntu.com/security/CVE-2026-0968) | - | - | - | Yes | Yes | Medium  
[CVE-2026-22795](https://ubuntu.com/security/CVE-2026-22795) | Yes | Yes | No | - | - | Low (5.5)  
[CVE-2026-22796](https://ubuntu.com/security/CVE-2026-22796) | Yes | Yes | No | - | - | Low (5.3)  
[CVE-2026-24051](https://ubuntu.com/security/CVE-2026-24051) | - | - | - | Yes | Yes | High (7.0)  
[CVE-2026-25679](https://ubuntu.com/security/CVE-2026-25679) | Yes | Yes | - | - | - | High (7.5)  
  
### Security

The following images are now rolling out for managed Cloud Service Mesh:

  * Sidecar version 1.21.6-asm.16 is rolling out to the rapid release channel.
  * Sidecar version 1.20.8-asm.68 is rolling out to the regular release channel.
  * Sidecar version 1.19.10-asm.61 is rolling out to the stable release channel.
  * CNI and managed data plane controller version 1.23.6-asm.31 is rolling out to all release channels.



These rollouts will preempt those previously announced on February 9, 2026.

Managed Cloud Service Mesh will start using proxy version csm_mesh_proxy.20260304_RC00 for Gateway API on GKE clusters for all channels. This proxy version maps closest to Envoy version 1.37.

These patch releases contain the fixes for the vulnerabilities listed in [GCP-2026-013](https://docs.cloud.google.com/service-mesh/v1.28/docs/security-bulletins#gcp-2026-013) as well as fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | MDPC | Severity  
---|---|---|---|---|---|---  
[CVE-2025-61726](https://ubuntu.com/security/CVE-2025-61726) | Yes | Yes | Yes | - | - | High (7.5)  
[CVE-2025-61728](https://ubuntu.com/security/CVE-2025-61728) | Yes | Yes | Yes | - | - | Medium (6.5)  
[CVE-2025-61730](https://ubuntu.com/security/CVE-2025-61730) | Yes | Yes | Yes | - | - | Medium (5.3)  
[CVE-2025-61731](https://ubuntu.com/security/CVE-2025-61731) | Yes | Yes | Yes | - | - | High (7.8)  
[CVE-2025-61732](https://ubuntu.com/security/CVE-2025-61732) | Yes | Yes | Yes | - | - | High (8.6)  
[CVE-2025-68121](https://ubuntu.com/security/CVE-2025-68121) | Yes | Yes | Yes | - | - | Critical (10)  
[CVE-2025-68160](https://ubuntu.com/security/CVE-2025-68160) | Yes | Yes | No | - | - | Low (4.7)  
[CVE-2025-69418](https://ubuntu.com/security/CVE-2025-69418) | Yes | Yes | No | - | - | Low (4.0)  
[CVE-2025-69419](https://ubuntu.com/security/CVE-2025-69419) | Yes | Yes | No | - | - | Low (7.4)  
[CVE-2025-69420](https://ubuntu.com/security/CVE-2025-69420) | Yes | Yes | No | - | - | Low (7.5)  
[CVE-2025-69421](https://ubuntu.com/security/CVE-2025-69421) | Yes | Yes | No | - | - | Low (7.5)  
[CVE-2025-8277](https://ubuntu.com/security/CVE-2025-8277) | - | - | - | Yes | Yes | Low (0)  
[CVE-2025-9820](https://ubuntu.com/security/CVE-2025-9820) | - | - | - | Yes | Yes | Low (4.0)  
[CVE-2025-14831](https://ubuntu.com/security/CVE-2025-14831) | - | - | - | Yes | Yes | Medium (5.3)  
[CVE-2025-15281](https://ubuntu.com/security/CVE-2025-15281) | Yes | Yes | Yes | - | - | Medium (7.5)  
[CVE-2025-15467](https://ubuntu.com/security/CVE-2025-15467) | Yes | Yes | No | - | - | Medium (9.8)  
[CVE-2026-0861](https://ubuntu.com/security/CVE-2026-0861) | Yes | Yes | No | - | - | Medium (8.4)  
[CVE-2026-0915](https://ubuntu.com/security/CVE-2026-0915) | Yes | Yes | No | - | - | Medium (7.5)  
[CVE-2026-0964](https://ubuntu.com/security/CVE-2026-0964) | - | - | - | Yes | Yes | Medium  
[CVE-2026-0965](https://ubuntu.com/security/CVE-2026-0965) | - | - | - | Yes | Yes | Low  
[CVE-2026-0966](https://ubuntu.com/security/CVE-2026-0966) | - | - | - | Yes | Yes | Low  
[CVE-2026-0967](https://ubuntu.com/security/CVE-2026-0967) | - | - | - | Yes | Yes | Medium  
[CVE-2026-0968](https://ubuntu.com/security/CVE-2026-0968) | - | - | - | Yes | Yes | Medium  
[CVE-2026-22795](https://ubuntu.com/security/CVE-2026-22795) | Yes | Yes | No | - | - | Low (5.5)  
[CVE-2026-22796](https://ubuntu.com/security/CVE-2026-22796) | Yes | Yes | No | - | - | Low (5.3)  
[CVE-2026-24051](https://ubuntu.com/security/CVE-2026-24051) | - | - | - | Yes | Yes | High (7.0)  
[CVE-2026-25679](https://ubuntu.com/security/CVE-2026-25679) | Yes | Yes | - | - | - | High (7.5)  
  
### Security

The following images are now rolling out for managed Cloud Service Mesh:

  * Sidecar version 1.21.6-asm.16 is rolling out to the rapid release channel.
  * Sidecar version 1.20.8-asm.68 is rolling out to the regular release channel.
  * Sidecar version 1.19.10-asm.61 is rolling out to the stable release channel.
  * CNI and managed data plane controller version 1.23.6-asm.31 is rolling out to all release channels.



These rollouts will preempt those previously announced on February 9, 2026.

Managed Cloud Service Mesh will start using proxy version csm_mesh_proxy.20260304_RC00 for Gateway API on GKE clusters for all channels. This proxy version maps closest to Envoy version 1.37.

These patch releases contain the fixes for the vulnerabilities listed in [GCP-2026-013](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-013) as well as fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | MDPC | Severity  
---|---|---|---|---|---|---  
[CVE-2025-61726](https://ubuntu.com/security/CVE-2025-61726) | Yes | Yes | Yes | - | - | High (7.5)  
[CVE-2025-61728](https://ubuntu.com/security/CVE-2025-61728) | Yes | Yes | Yes | - | - | Medium (6.5)  
[CVE-2025-61730](https://ubuntu.com/security/CVE-2025-61730) | Yes | Yes | Yes | - | - | Medium (5.3)  
[CVE-2025-61731](https://ubuntu.com/security/CVE-2025-61731) | Yes | Yes | Yes | - | - | High (7.8)  
[CVE-2025-61732](https://ubuntu.com/security/CVE-2025-61732) | Yes | Yes | Yes | - | - | High (8.6)  
[CVE-2025-68121](https://ubuntu.com/security/CVE-2025-68121) | Yes | Yes | Yes | - | - | Critical (10)  
[CVE-2025-68160](https://ubuntu.com/security/CVE-2025-68160) | Yes | Yes | No | - | - | Low (4.7)  
[CVE-2025-69418](https://ubuntu.com/security/CVE-2025-69418) | Yes | Yes | No | - | - | Low (4.0)  
[CVE-2025-69419](https://ubuntu.com/security/CVE-2025-69419) | Yes | Yes | No | - | - | Low (7.4)  
[CVE-2025-69420](https://ubuntu.com/security/CVE-2025-69420) | Yes | Yes | No | - | - | Low (7.5)  
[CVE-2025-69421](https://ubuntu.com/security/CVE-2025-69421) | Yes | Yes | No | - | - | Low (7.5)  
[CVE-2025-8277](https://ubuntu.com/security/CVE-2025-8277) | - | - | - | Yes | Yes | Low (0)  
[CVE-2025-9820](https://ubuntu.com/security/CVE-2025-9820) | - | - | - | Yes | Yes | Low (4.0)  
[CVE-2025-14831](https://ubuntu.com/security/CVE-2025-14831) | - | - | - | Yes | Yes | Medium (5.3)  
[CVE-2025-15281](https://ubuntu.com/security/CVE-2025-15281) | Yes | Yes | Yes | - | - | Medium (7.5)  
[CVE-2025-15467](https://ubuntu.com/security/CVE-2025-15467) | Yes | Yes | No | - | - | Medium (9.8)  
[CVE-2026-0861](https://ubuntu.com/security/CVE-2026-0861) | Yes | Yes | No | - | - | Medium (8.4)  
[CVE-2026-0915](https://ubuntu.com/security/CVE-2026-0915) | Yes | Yes | No | - | - | Medium (7.5)  
[CVE-2026-0964](https://ubuntu.com/security/CVE-2026-0964) | - | - | - | Yes | Yes | Medium  
[CVE-2026-0965](https://ubuntu.com/security/CVE-2026-0965) | - | - | - | Yes | Yes | Low  
[CVE-2026-0966](https://ubuntu.com/security/CVE-2026-0966) | - | - | - | Yes | Yes | Low  
[CVE-2026-0967](https://ubuntu.com/security/CVE-2026-0967) | - | - | - | Yes | Yes | Medium  
[CVE-2026-0968](https://ubuntu.com/security/CVE-2026-0968) | - | - | - | Yes | Yes | Medium  
[CVE-2026-22795](https://ubuntu.com/security/CVE-2026-22795) | Yes | Yes | No | - | - | Low (5.5)  
[CVE-2026-22796](https://ubuntu.com/security/CVE-2026-22796) | Yes | Yes | No | - | - | Low (5.3)  
[CVE-2026-24051](https://ubuntu.com/security/CVE-2026-24051) | - | - | - | Yes | Yes | High (7.0)  
[CVE-2026-25679](https://ubuntu.com/security/CVE-2026-25679) | Yes | Yes | - | - | - | High (7.5)  
**1.26.x**

### Security

**1.26.8-asm.3 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2026-013](https://docs.cloud.google.com/service-mesh/v1.29/docs/security-bulletins#gcp-2026-013) as well as fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2025-13151](https://ubuntu.com/security/CVE-2025-13151) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2025-14831](https://ubuntu.com/security/CVE-2025-14831) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2025-15281](https://ubuntu.com/security/CVE-2025-15281) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2025-15467](https://ubuntu.com/security/CVE-2025-15467) | Yes | Yes | Yes | Yes | Medium (9.8)  
[CVE-2025-15558](https://ubuntu.com/security/CVE-2025-15558) | Yes | Yes | Yes | - | High (8.0)  
[CVE-2025-61726](https://ubuntu.com/security/CVE-2025-61726) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2025-61728](https://ubuntu.com/security/CVE-2025-61728) | Yes | Yes | Yes | Yes | Medium (6.5)  
[CVE-2025-61730](https://ubuntu.com/security/CVE-2025-61730) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2025-61731](https://ubuntu.com/security/CVE-2025-61731) | Yes | Yes | Yes | Yes | High (7.8)  
[CVE-2025-61732](https://ubuntu.com/security/CVE-2025-61732) | Yes | Yes | Yes | Yes | High (8.6)  
[CVE-2025-68121](https://ubuntu.com/security/CVE-2025-68121) | Yes | Yes | Yes | Yes | Critical (10)  
[CVE-2025-68160](https://ubuntu.com/security/CVE-2025-68160) | Yes | Yes | No | Yes | Low (4.7)  
[CVE-2025-68973](https://ubuntu.com/security/CVE-2025-68973) | Yes | Yes | Yes | Yes | High (7.8)  
[CVE-2025-69418](https://ubuntu.com/security/CVE-2025-69418) | Yes | Yes | No | Yes | Low (4.0)  
[CVE-2025-69419](https://ubuntu.com/security/CVE-2025-69419) | Yes | Yes | No | Yes | Low (7.4)  
[CVE-2025-69420](https://ubuntu.com/security/CVE-2025-69420) | Yes | Yes | Yes | Yes | Low (7.5)  
[CVE-2025-69421](https://ubuntu.com/security/CVE-2025-69421) | Yes | Yes | Yes | Yes | Low (7.5)  
[CVE-2025-8277](https://ubuntu.com/security/CVE-2025-8277) | Yes | Yes | No | Yes | Low (0)  
[CVE-2025-9820](https://ubuntu.com/security/CVE-2025-9820) | Yes | Yes | No | Yes | Low (4)  
[CVE-2026-0861](https://ubuntu.com/security/CVE-2026-0861) | Yes | Yes | No | Yes | Medium (8.4)  
[CVE-2026-0915](https://ubuntu.com/security/CVE-2026-0915) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-0964](https://ubuntu.com/security/CVE-2026-0964) | Yes | Yes | No | Yes | Medium  
[CVE-2026-0965](https://ubuntu.com/security/CVE-2026-0965) | Yes | Yes | No | Yes | Low  
[CVE-2026-0966](https://ubuntu.com/security/CVE-2026-0966) | Yes | Yes | No | Yes | Low  
[CVE-2026-0967](https://ubuntu.com/security/CVE-2026-0967) | Yes | Yes | No | Yes | Medium  
[CVE-2026-0968](https://ubuntu.com/security/CVE-2026-0968) | Yes | Yes | No | Yes | Medium  
[CVE-2026-22795](https://ubuntu.com/security/CVE-2026-22795) | Yes | Yes | No | Yes | Low (5.5)  
[CVE-2026-22796](https://ubuntu.com/security/CVE-2026-22796) | Yes | Yes | No | Yes | Low (5.3)  
[CVE-2026-24051](https://ubuntu.com/security/CVE-2026-24051) | Yes | Yes | Yes | Yes | High (7.0)  
[CVE-2026-25679](https://ubuntu.com/security/CVE-2026-25679) | Yes | Yes | Yes | Yes | High (7.5)  
  
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/upgrade/upgrade). Cloud Service Mesh 1.26.8-asm.3 uses Envoy 1.34.13.

### Security

**1.26.8-asm.3 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2026-013](https://docs.cloud.google.com/service-mesh/v1.28/docs/security-bulletins#gcp-2026-013) as well as fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2025-13151](https://ubuntu.com/security/CVE-2025-13151) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2025-14831](https://ubuntu.com/security/CVE-2025-14831) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2025-15281](https://ubuntu.com/security/CVE-2025-15281) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2025-15467](https://ubuntu.com/security/CVE-2025-15467) | Yes | Yes | Yes | Yes | Medium (9.8)  
[CVE-2025-15558](https://ubuntu.com/security/CVE-2025-15558) | Yes | Yes | Yes | - | High (8.0)  
[CVE-2025-61726](https://ubuntu.com/security/CVE-2025-61726) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2025-61728](https://ubuntu.com/security/CVE-2025-61728) | Yes | Yes | Yes | Yes | Medium (6.5)  
[CVE-2025-61730](https://ubuntu.com/security/CVE-2025-61730) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2025-61731](https://ubuntu.com/security/CVE-2025-61731) | Yes | Yes | Yes | Yes | High (7.8)  
[CVE-2025-61732](https://ubuntu.com/security/CVE-2025-61732) | Yes | Yes | Yes | Yes | High (8.6)  
[CVE-2025-68121](https://ubuntu.com/security/CVE-2025-68121) | Yes | Yes | Yes | Yes | Critical (10)  
[CVE-2025-68160](https://ubuntu.com/security/CVE-2025-68160) | Yes | Yes | No | Yes | Low (4.7)  
[CVE-2025-68973](https://ubuntu.com/security/CVE-2025-68973) | Yes | Yes | Yes | Yes | High (7.8)  
[CVE-2025-69418](https://ubuntu.com/security/CVE-2025-69418) | Yes | Yes | No | Yes | Low (4.0)  
[CVE-2025-69419](https://ubuntu.com/security/CVE-2025-69419) | Yes | Yes | No | Yes | Low (7.4)  
[CVE-2025-69420](https://ubuntu.com/security/CVE-2025-69420) | Yes | Yes | Yes | Yes | Low (7.5)  
[CVE-2025-69421](https://ubuntu.com/security/CVE-2025-69421) | Yes | Yes | Yes | Yes | Low (7.5)  
[CVE-2025-8277](https://ubuntu.com/security/CVE-2025-8277) | Yes | Yes | No | Yes | Low (0)  
[CVE-2025-9820](https://ubuntu.com/security/CVE-2025-9820) | Yes | Yes | No | Yes | Low (4)  
[CVE-2026-0861](https://ubuntu.com/security/CVE-2026-0861) | Yes | Yes | No | Yes | Medium (8.4)  
[CVE-2026-0915](https://ubuntu.com/security/CVE-2026-0915) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-0964](https://ubuntu.com/security/CVE-2026-0964) | Yes | Yes | No | Yes | Medium  
[CVE-2026-0965](https://ubuntu.com/security/CVE-2026-0965) | Yes | Yes | No | Yes | Low  
[CVE-2026-0966](https://ubuntu.com/security/CVE-2026-0966) | Yes | Yes | No | Yes | Low  
[CVE-2026-0967](https://ubuntu.com/security/CVE-2026-0967) | Yes | Yes | No | Yes | Medium  
[CVE-2026-0968](https://ubuntu.com/security/CVE-2026-0968) | Yes | Yes | No | Yes | Medium  
[CVE-2026-22795](https://ubuntu.com/security/CVE-2026-22795) | Yes | Yes | No | Yes | Low (5.5)  
[CVE-2026-22796](https://ubuntu.com/security/CVE-2026-22796) | Yes | Yes | No | Yes | Low (5.3)  
[CVE-2026-24051](https://ubuntu.com/security/CVE-2026-24051) | Yes | Yes | Yes | Yes | High (7.0)  
[CVE-2026-25679](https://ubuntu.com/security/CVE-2026-25679) | Yes | Yes | Yes | Yes | High (7.5)  
  
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/upgrade/upgrade). Cloud Service Mesh 1.26.8-asm.3 uses Envoy 1.34.13.

### Security

**1.26.8-asm.3 is now available for in-cluster Cloud Service Mesh.**

This patch release contains fixes for the security vulnerabilities listed in [GCP-2026-013](https://docs.cloud.google.com/service-mesh/docs/security-bulletins#gcp-2026-013) as well as fixes for the following platform CVEs:

CVE | Proxy | Control Plane | Distroless | CNI | Severity  
---|---|---|---|---|---  
[CVE-2025-13151](https://ubuntu.com/security/CVE-2025-13151) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2025-14831](https://ubuntu.com/security/CVE-2025-14831) | Yes | Yes | No | Yes | Medium (5.3)  
[CVE-2025-15281](https://ubuntu.com/security/CVE-2025-15281) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2025-15467](https://ubuntu.com/security/CVE-2025-15467) | Yes | Yes | Yes | Yes | Medium (9.8)  
[CVE-2025-15558](https://ubuntu.com/security/CVE-2025-15558) | Yes | Yes | Yes | - | High (8.0)  
[CVE-2025-61726](https://ubuntu.com/security/CVE-2025-61726) | Yes | Yes | Yes | Yes | High (7.5)  
[CVE-2025-61728](https://ubuntu.com/security/CVE-2025-61728) | Yes | Yes | Yes | Yes | Medium (6.5)  
[CVE-2025-61730](https://ubuntu.com/security/CVE-2025-61730) | Yes | Yes | Yes | Yes | Medium (5.3)  
[CVE-2025-61731](https://ubuntu.com/security/CVE-2025-61731) | Yes | Yes | Yes | Yes | High (7.8)  
[CVE-2025-61732](https://ubuntu.com/security/CVE-2025-61732) | Yes | Yes | Yes | Yes | High (8.6)  
[CVE-2025-68121](https://ubuntu.com/security/CVE-2025-68121) | Yes | Yes | Yes | Yes | Critical (10)  
[CVE-2025-68160](https://ubuntu.com/security/CVE-2025-68160) | Yes | Yes | No | Yes | Low (4.7)  
[CVE-2025-68973](https://ubuntu.com/security/CVE-2025-68973) | Yes | Yes | Yes | Yes | High (7.8)  
[CVE-2025-69418](https://ubuntu.com/security/CVE-2025-69418) | Yes | Yes | No | Yes | Low (4.0)  
[CVE-2025-69419](https://ubuntu.com/security/CVE-2025-69419) | Yes | Yes | No | Yes | Low (7.4)  
[CVE-2025-69420](https://ubuntu.com/security/CVE-2025-69420) | Yes | Yes | Yes | Yes | Low (7.5)  
[CVE-2025-69421](https://ubuntu.com/security/CVE-2025-69421) | Yes | Yes | Yes | Yes | Low (7.5)  
[CVE-2025-8277](https://ubuntu.com/security/CVE-2025-8277) | Yes | Yes | No | Yes | Low (0)  
[CVE-2025-9820](https://ubuntu.com/security/CVE-2025-9820) | Yes | Yes | No | Yes | Low (4)  
[CVE-2026-0861](https://ubuntu.com/security/CVE-2026-0861) | Yes | Yes | No | Yes | Medium (8.4)  
[CVE-2026-0915](https://ubuntu.com/security/CVE-2026-0915) | Yes | Yes | No | Yes | Medium (7.5)  
[CVE-2026-0964](https://ubuntu.com/security/CVE-2026-0964) | Yes | Yes | No | Yes | Medium  
[CVE-2026-0965](https://ubuntu.com/security/CVE-2026-0965) | Yes | Yes | No | Yes | Low  
[CVE-2026-0966](https://ubuntu.com/security/CVE-2026-0966) | Yes | Yes | No | Yes | Low  
[CVE-2026-0967](https://ubuntu.com/security/CVE-2026-0967) | Yes | Yes | No | Yes | Medium  
[CVE-2026-0968](https://ubuntu.com/security/CVE-2026-0968) | Yes | Yes | No | Yes | Medium  
[CVE-2026-22795](https://ubuntu.com/security/CVE-2026-22795) | Yes | Yes | No | Yes | Low (5.5)  
[CVE-2026-22796](https://ubuntu.com/security/CVE-2026-22796) | Yes | Yes | No | Yes | Low (5.3)  
[CVE-2026-24051](https://ubuntu.com/security/CVE-2026-24051) | Yes | Yes | Yes | Yes | High (7.0)  
[CVE-2026-25679](https://ubuntu.com/security/CVE-2026-25679) | Yes | Yes | Yes | Yes | High (7.5)  
  
For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/upgrade/upgrade). Cloud Service Mesh 1.26.8-asm.3 uses Envoy 1.34.13.

]]> February 18, 2026tag:google.com,2016:servicemesh-release-notes#February_18_20262026-02-18T00:00:00-08:00Managed Cloud Service Mesh 

### Announcement

CNI and managed data plane controller version 1.23.6-asm.28 is rolling out to all release channels.

While the managed data plane automatically updates Envoy Proxies by restarting workloads, you must manually restart any StatefulSets and Jobs.

This patch includes the fix for the following CVEs:

Name | CNI | MDPC | Severity  
---|---|---|---  
[CVE-2017-11164](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2017-11164) | Yes | Yes | High (7.5)  
[CVE-2022-27943](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2022-27943) | Yes | Yes | Medium (5.5)  
[CVE-2022-41409](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2022-41409) | Yes | Yes | High (7.5)  
[CVE-2022-4899](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2022-4899) | Yes | Yes | High (7.5)  
[CVE-2023-29383](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2023-29383) | Yes | Yes | Low (3.3)  
[CVE-2023-34969](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2023-34969) | Yes | Yes | Medium (6.5)  
[CVE-2023-50495](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2023-50495) | Yes | Yes | Medium (6.5)  
[CVE-2023-7008](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2023-7008) | Yes | Yes | Medium (5.9)  
[CVE-2024-41996](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-41996) | Yes | Yes | High (7.5)  
[CVE-2025-8114](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-8114) | Yes | Yes | Medium (4.7)  
[CVE-2025-9086](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-9086) | Yes | Yes | High (7.5)  
  
### Announcement

CNI and managed data plane controller version 1.23.6-asm.28 is rolling out to all release channels.

While the managed data plane automatically updates Envoy Proxies by restarting workloads, you must manually restart any StatefulSets and Jobs.

This patch includes the fix for the following CVEs:

Name | CNI | MDPC | Severity  
---|---|---|---  
[CVE-2017-11164](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2017-11164) | Yes | Yes | High (7.5)  
[CVE-2022-27943](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2022-27943) | Yes | Yes | Medium (5.5)  
[CVE-2022-41409](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2022-41409) | Yes | Yes | High (7.5)  
[CVE-2022-4899](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2022-4899) | Yes | Yes | High (7.5)  
[CVE-2023-29383](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2023-29383) | Yes | Yes | Low (3.3)  
[CVE-2023-34969](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2023-34969) | Yes | Yes | Medium (6.5)  
[CVE-2023-50495](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2023-50495) | Yes | Yes | Medium (6.5)  
[CVE-2023-7008](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2023-7008) | Yes | Yes | Medium (5.9)  
[CVE-2024-41996](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-41996) | Yes | Yes | High (7.5)  
[CVE-2025-8114](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-8114) | Yes | Yes | Medium (4.7)  
[CVE-2025-9086](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-9086) | Yes | Yes | High (7.5)  
  
### Announcement

CNI and managed data plane controller version 1.23.6-asm.28 is rolling out to all release channels.

While the managed data plane automatically updates Envoy Proxies by restarting workloads, you must manually restart any StatefulSets and Jobs.

This patch includes the fix for the following CVEs:

Name | CNI | MDPC | Severity  
---|---|---|---  
[CVE-2017-11164](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2017-11164) | Yes | Yes | High (7.5)  
[CVE-2022-27943](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2022-27943) | Yes | Yes | Medium (5.5)  
[CVE-2022-41409](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2022-41409) | Yes | Yes | High (7.5)  
[CVE-2022-4899](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2022-4899) | Yes | Yes | High (7.5)  
[CVE-2023-29383](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2023-29383) | Yes | Yes | Low (3.3)  
[CVE-2023-34969](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2023-34969) | Yes | Yes | Medium (6.5)  
[CVE-2023-50495](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2023-50495) | Yes | Yes | Medium (6.5)  
[CVE-2023-7008](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2023-7008) | Yes | Yes | Medium (5.9)  
[CVE-2024-41996](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-41996) | Yes | Yes | High (7.5)  
[CVE-2025-8114](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-8114) | Yes | Yes | Medium (4.7)  
[CVE-2025-9086](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-9086) | Yes | Yes | High (7.5)  
]]> February 09, 2026tag:google.com,2016:servicemesh-release-notes#February_09_20262026-02-09T00:00:00-08:00Managed Cloud Service Mesh 

### Announcement

The following images are now rolling out for managed Cloud Service Mesh:

  * 1.21.6-asm.10 is rolling out to the rapid release channel.
  * 1.20.8-asm.63 is rolling out to the regular release channel.
  * 1.19.10-asm.57 is rolling out to the stable release channel.



These patch releases contain the fixes for the following managed Cloud Service Mesh CVEs:

CVE | Proxy | Control Plane | CNI | Distroless | Severity  
---|---|---|---|---|---  
[CVE-2025-61729](https://nvd.nist.gov/vuln/detail/CVE-2025-61729) | Yes | Yes | - | Yes | High (7.5)  
[CVE-2025-61727](https://pkg.go.dev/vuln/GO-2025-4175) | Yes | Yes | - | Yes | Medium (6.5)  
[CVE-2024-41996](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-41996) | Yes | Yes | - | Yes | High (7.5)  
[CVE-2025-9086](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-9086) | Yes | Yes | - | Yes | High (7.5)  
[CVE-2021-46848](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2021-46848) | Yes | Yes | - | Yes | Critical (9.1)  
[CVE-2025-13151](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-13151) | Yes | Yes | - | Yes | High (7.5)  
[CVE-2025-68973](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-68973) | Yes | Yes | - | Yes | High (7.8)  
  
### Announcement

The following images are now rolling out for managed Cloud Service Mesh:

  * 1.21.6-asm.10 is rolling out to the rapid release channel.
  * 1.20.8-asm.63 is rolling out to the regular release channel.
  * 1.19.10-asm.57 is rolling out to the stable release channel.



These patch releases contain the fixes for the following managed Cloud Service Mesh CVEs:

CVE | Proxy | Control Plane | CNI | Distroless | Severity  
---|---|---|---|---|---  
[CVE-2025-61729](https://nvd.nist.gov/vuln/detail/CVE-2025-61729) | Yes | Yes | - | Yes | High (7.5)  
[CVE-2025-61727](https://pkg.go.dev/vuln/GO-2025-4175) | Yes | Yes | - | Yes | Medium (6.5)  
[CVE-2024-41996](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-41996) | Yes | Yes | - | Yes | High (7.5)  
[CVE-2025-9086](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-9086) | Yes | Yes | - | Yes | High (7.5)  
[CVE-2021-46848](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2021-46848) | Yes | Yes | - | Yes | Critical (9.1)  
[CVE-2025-13151](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-13151) | Yes | Yes | - | Yes | High (7.5)  
[CVE-2025-68973](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-68973) | Yes | Yes | - | Yes | High (7.8)  
  
### Announcement

The following images are now rolling out for managed Cloud Service Mesh:

  * 1.21.6-asm.10 is rolling out to the rapid release channel.
  * 1.20.8-asm.63 is rolling out to the regular release channel.
  * 1.19.10-asm.57 is rolling out to the stable release channel.



These patch releases contain the fixes for the following managed Cloud Service Mesh CVEs:

CVE | Proxy | Control Plane | CNI | Distroless | Severity  
---|---|---|---|---|---  
[CVE-2025-61729](https://nvd.nist.gov/vuln/detail/CVE-2025-61729) | Yes | Yes | - | Yes | High (7.5)  
[CVE-2025-61727](https://pkg.go.dev/vuln/GO-2025-4175) | Yes | Yes | - | Yes | Medium (6.5)  
[CVE-2024-41996](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2024-41996) | Yes | Yes | - | Yes | High (7.5)  
[CVE-2025-9086](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-9086) | Yes | Yes | - | Yes | High (7.5)  
[CVE-2021-46848](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2021-46848) | Yes | Yes | - | Yes | Critical (9.1)  
[CVE-2025-13151](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-13151) | Yes | Yes | - | Yes | High (7.5)  
[CVE-2025-68973](http://people.ubuntu.com/%7Eubuntu-security/cve/CVE-2025-68973) | Yes | Yes | - | Yes | High (7.8)  
]]> January 20, 2026tag:google.com,2016:servicemesh-release-notes#January_20_20262026-01-20T00:00:00-08:001.27.x 

### Announcement

**1.28.2-asm.4 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.28.2-asm.4 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.28.0](https://istio.io/latest/news/releases/1.28.x/announcing-1.28/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.29/docs/supported-features-in-cluster).

The following environment variables, fields, and annotations are not supported:

  * `PILOT_SPAWN_UPSTREAM_SPAN_FOR_GATEWAY`
  * Additional attributes for `HTTPCookie` in the DestinationRule API
  * `caCertCredentialName` field in ServerTLSSettings API
  * Optional `NetworkPolicy` for Istiod deployment
  * Disable shadow host suffix
  * `MAX_CONNECTIONS_PER_SOCKET_EVENT_LOOP`



Istio dual stack is not supported

Istio's experimental feature to enable lazy subset creation of envoy statistics is not supported.

The `ENABLE_AUTO_SNI` flag is still supported to stay aligned with legacy behavior.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.29/docs/upgrade/upgrade). Cloud Service Mesh version 1.28.2-asm.4 uses Envoy v1.36.5-dev.

### Announcement

**1.28.2-asm.4 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.28.2-asm.4 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.28.0](https://istio.io/latest/news/releases/1.28.x/announcing-1.28/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.28/docs/supported-features-in-cluster).

The following environment variables, fields, and annotations are not supported:

  * `PILOT_SPAWN_UPSTREAM_SPAN_FOR_GATEWAY`
  * Additional attributes for `HTTPCookie` in the DestinationRule API
  * `caCertCredentialName` field in ServerTLSSettings API
  * Optional `NetworkPolicy` for Istiod deployment
  * Disable shadow host suffix
  * `MAX_CONNECTIONS_PER_SOCKET_EVENT_LOOP`



Istio dual stack is not supported

Istio's experimental feature to enable lazy subset creation of envoy statistics is not supported.

The `ENABLE_AUTO_SNI` flag is still supported to stay aligned with legacy behavior.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.28/docs/upgrade/upgrade). Cloud Service Mesh version 1.28.2-asm.4 uses Envoy v1.36.5-dev.

### Announcement

**1.28.2-asm.4 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.28.2-asm.4 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.28.0](https://istio.io/latest/news/releases/1.28.x/announcing-1.28/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster).

The following environment variables, fields, and annotations are not supported:

  * `PILOT_SPAWN_UPSTREAM_SPAN_FOR_GATEWAY`
  * Additional attributes for `HTTPCookie` in the DestinationRule API
  * `caCertCredentialName` field in ServerTLSSettings API
  * Optional `NetworkPolicy` for Istiod deployment
  * Disable shadow host suffix
  * `MAX_CONNECTIONS_PER_SOCKET_EVENT_LOOP`



Istio dual stack is not supported

Istio's experimental feature to enable lazy subset creation of envoy statistics is not supported.

The `ENABLE_AUTO_SNI` flag is still supported to stay aligned with legacy behavior.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade). Cloud Service Mesh version 1.28.2-asm.4 uses Envoy v1.36.5-dev.

### Announcement

**1.27.5-asm.0 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.27.5-asm.0 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.27.5](https://istio.io/latest/news/releases/1.27.x/announcing-1.27.5/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.27/docs/supported-features-in-cluster). Cloud Service Mesh version 1.27.5-asm.0 uses envoy v1.35.9-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade).

### Announcement

**1.27.5-asm.0 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.27.5-asm.0 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.27.5](https://istio.io/latest/news/releases/1.27.x/announcing-1.27.5/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.27/docs/supported-features-in-cluster). Cloud Service Mesh version 1.27.5-asm.0 uses envoy v1.35.9-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade).

### Announcement

**1.27.5-asm.0 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.27.5-asm.0 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.27.5](https://istio.io/latest/news/releases/1.27.x/announcing-1.27.5/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.27/docs/supported-features-in-cluster). Cloud Service Mesh version 1.27.5-asm.0 uses envoy v1.35.9-dev.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.27/docs/upgrade/upgrade).

**1.26.x**

### Announcement

**1.26.8-asm.1 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.26.8-asm.1 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.26.8](https://istio.io/latest/news/releases/1.26.x/announcing-1.26.8/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.26/docs/supported-features-in-cluster). Cloud Service Mesh version 1.26.8-asm.1 uses envoy v1.34.11.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/upgrade/upgrade).

### Announcement

**1.26.8-asm.1 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.26.8-asm.1 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.26.8](https://istio.io/latest/news/releases/1.26.x/announcing-1.26.8/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.26/docs/supported-features-in-cluster). Cloud Service Mesh version 1.26.8-asm.1 uses envoy v1.34.11.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/upgrade/upgrade).

### Announcement

**1.26.8-asm.1 is now available for in-cluster Cloud Service Mesh.**

You can now download 1.26.8-asm.1 for in-cluster Cloud Service Mesh. It includes the features of [Istio 1.26.8](https://istio.io/latest/news/releases/1.26.x/announcing-1.26.8/) subject to the list of [supported features](https://docs.cloud.google.com/service-mesh/v1.26/docs/supported-features-in-cluster). Cloud Service Mesh version 1.26.8-asm.1 uses envoy v1.34.11.

For details on upgrading Cloud Service Mesh, see [Upgrade Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/v1.26/docs/upgrade/upgrade).

**1.25.x**

### Announcement

In-cluster Cloud Service Mesh 1.25 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see [Supported versions](https://docs.cloud.google.com/service-mesh/v1.29/docs/supported-features-in-cluster#supported_versions).

### Announcement

In-cluster Cloud Service Mesh 1.25 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see [Supported versions](https://docs.cloud.google.com/service-mesh/v1.28/docs/supported-features-in-cluster#supported_versions).

### Announcement

In-cluster Cloud Service Mesh 1.25 is no longer supported. For more information and to view the earliest end-of-life dates for other versions, see [Supported versions](https://docs.cloud.google.com/service-mesh/docs/supported-features-in-cluster#supported_versions).

]]>
