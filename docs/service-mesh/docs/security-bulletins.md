---
url: https://docs.cloud.google.com/service-mesh/docs/security-bulletins/
title: Security bulletins \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:48:10.854383+00:00
---

# Security bulletins  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/security-bulletins/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Resources ](https://docs.cloud.google.com/service-mesh/docs/resources)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Security bulletins

[ Use this XML feed to subscribe to Cloud Service Mesh security bulletins. ![Subscribe](https://docs.cloud.google.com/static/docs/images/feed-icon.png)](https://cloud.google.com/feeds/cloud-service-mesh-security-bulletins.xml)

This page lists the security bulletins for Cloud Service Mesh.

## GCP-2026-069

**Published:** 2026-10-19

Description | Severity | Notes  
---|---|---  
Fixes an issue where `AuthorizationPolicy` method rules could be bypassed over HTTP/2 by altering the capitalization of the HTTP method. 

#### What should I do?

**Check if your clusters are impacted** All in-cluster Cloud Service Mesh versions are impacted by this vulnerability.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.31.1-asm.19
  * 1.30.5-asm.11
  * 1.29.8-asm.11
  * 1.28.10-asm.52

If you're using Cloud Service Mesh v1.27 or earlier, your release has reached end of life and is no longer supported. Upgrade to a supported version.  For **managed** Cloud Service Mesh, no customer action is required. Your system is automatically updated.  | High |  [ISTIO-SECURITY-2026-007](https://istio.io/latest/news/security/istio-security-2026-007/)  
[GHSA-w44g-8m76-8gc5](https://github.com/istio/istio/security/advisories/GHSA-w44g-8m76-8gc5)  
  
Description | Severity | Notes  
---|---|---  
Fixes an `istiod` denial of service in ambient mode when a `ServiceEntry` or another service claims the IP address of an IP-addressed waypoint. 

#### What should I do?

**Check if your clusters are impacted** Cloud Service Mesh does not support Istio ambient mode and is not impacted by this vulnerability.  **Mitigation** No customer action is required.  | High |  [ISTIO-SECURITY-2026-007](https://istio.io/latest/news/security/istio-security-2026-007/)  
[GHSA-7p2q-4xvg-vxc6](https://github.com/istio/istio/security/advisories/GHSA-7p2q-4xvg-vxc6)  
  
Description | Severity | Notes  
---|---|---  
Fixes an abnormal process termination (null pointer dereference) in the Envoy OAuth2 HTTP filter when processing path-less HTTP requests, such as `CONNECT` requests missing a `:path` header. 

#### What should I do?

**Check if your clusters are impacted** In-cluster Cloud Service Mesh v1.31, v1.30, and v1.29 are impacted by this vulnerability.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.31.1-asm.19
  * 1.30.5-asm.11
  * 1.29.8-asm.11

If you're using Cloud Service Mesh v1.27 or earlier, your release has reached end of life and is no longer supported. Upgrade to a supported version.  For **managed** Cloud Service Mesh, no customer action is required. Your system is automatically updated.  | High |  [ISTIO-SECURITY-2026-007](https://istio.io/latest/news/security/istio-security-2026-007/)  
[GHSA-8vc2-jrm4-835w](https://github.com/envoyproxy/envoy/security/advisories/GHSA-8vc2-jrm4-835w)  
  
Description | Severity | Notes  
---|---|---  
Fixes an abnormal process termination in the Envoy `api_key_auth` HTTP filter when `hide_credentials` is enabled with a query parameter key source and a request missing a `:path` header is authenticated via an alternative source. 

#### What should I do?

**Check if your clusters are impacted** In-cluster Cloud Service Mesh v1.31, v1.30, and v1.29 are impacted by this vulnerability.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.31.1-asm.19
  * 1.30.5-asm.11
  * 1.29.8-asm.11

If you're using Cloud Service Mesh v1.27 or earlier, your release has reached end of life and is no longer supported. Upgrade to a supported version.  For **managed** Cloud Service Mesh, no customer action is required. Your system is automatically updated.  | Moderate |  [ISTIO-SECURITY-2026-007](https://istio.io/latest/news/security/istio-security-2026-007/)  
[GHSA-47vj-9r25-wv5j](https://github.com/envoyproxy/envoy/security/advisories/GHSA-47vj-9r25-wv5j)  
  
  
## GCP-2026-067

**Published:** 2026-10-12

Description | Severity | Notes  
---|---|---  
Fixes an abnormal process termination in Envoy Proxy when an HTTP filter (such as `ext_proc` configured with `route_cache_action: RETAIN`) mutates the `:path` header after route selection to a string shorter than the matched route prefix on a route configured with `prefix_rewrite`. 

#### What should I do?

**Check if your clusters are impacted** In-cluster Cloud Service Mesh v1.30 and v1.29 are impacted by this vulnerability. In-cluster Cloud Service Mesh v1.28 is not impacted.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.30.5-asm.8
  * 1.29.8-asm.8

If you're using Cloud Service Mesh v1.27 or earlier, your release has reached end of life and is no longer supported. Upgrade to a supported version.  For **managed** Cloud Service Mesh, no customer action is required. Your system is automatically updated.  | High |  [envoyproxy/envoy#47841](https://github.com/envoyproxy/envoy/pull/47841)  
  
  
## GCP-2026-057

**Published:** 2026-08-26

Description | Severity | Notes  
---|---|---  
Fixes an issue where an untrusted upstream sending HTTP/2 response trailers without the END_STREAM flag to an oghttp2 instance could corrupt stream state and cause an abnormal process termination. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.7-asm.2
  * 1.28.10-asm.24
  * 1.27.9-asm.34

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.27 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | High |  [CVE-2026-73513](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-73513)  
  
Description | Severity | Notes  
---|---|---  
Fixes an issue where safe_regex matching treated non-UTF-8 HTTP header bytes as an ordinary non-match, causing RBAC policies using negative matching logic to fail open. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.7-asm.2
  * 1.28.10-asm.24
  * 1.27.9-asm.34

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.27 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | High |  [CVE-2026-73552](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-73552)  
  
Description | Severity | Notes  
---|---|---  
Fixes a use-after-free in the QUIC HTTP datagram handler where a request using the Capsule Protocol could have its stream decoder destroyed while late HTTP/3 datagrams still referenced it. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.7-asm.2
  * 1.28.10-asm.24
  * 1.27.9-asm.34

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.27 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | High |  [CVE-2026-73512](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-73512)  
  
Description | Severity | Notes  
---|---|---  
Fixes an abnormal process termination in the ext_authz filter when processing CONNECT requests without a :path pseudo-header. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.7-asm.2
  * 1.28.10-asm.24
  * 1.27.9-asm.34

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.27 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | High |  [CVE-2026-73547](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-73547)  
  
Description | Severity | Notes  
---|---|---  
Fixes an abnormal process termination during scoped IPv6 address handling in original DST clusters for HTTP/3 requests. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.7-asm.2
  * 1.28.10-asm.24
  * 1.27.9-asm.34

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.27 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | Moderate |  [CVE-2026-73549](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-73549)  
  
Description | Severity | Notes  
---|---|---  
Fixes a use-after-free in the ext_authz raw HTTP client when completing authorization requests with local rejection replies. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.7-asm.2
  * 1.28.10-asm.24
  * 1.27.9-asm.34

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.27 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | Moderate |  [CVE-2026-50572](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-50572)  
  
Description | Severity | Notes  
---|---|---  
Fixes a stored cross-site scripting issue in the HTML stats interface (/stats?format=html). 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.7-asm.2
  * 1.28.10-asm.24
  * 1.27.9-asm.34

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.27 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | Moderate |  [CVE-2026-73546](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-73546)  
  
Description | Severity | Notes  
---|---|---  
Fixes an abnormal process termination during ALPN-based HTTP/3 connection-pool selection caused by dereferencing null transport socket options. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.7-asm.2
  * 1.28.10-asm.24
  * 1.27.9-asm.34

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.27 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | Moderate |  [CVE-2026-48521](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-48521)  
  
Description | Severity | Notes  
---|---|---  
Fixes URL normalization of dot and dot-dot path segments containing parameters that could allow path-based authorization policy bypasses. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.7-asm.2
  * 1.28.10-asm.24
  * 1.27.9-asm.34

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.27 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | Moderate |  [CVE-2026-73551](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-73551)  
  
Description | Severity | Notes  
---|---|---  
Fixes path matching for paths containing per-segment matrix parameters by applying parameter stripping consistently across path segments. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.7-asm.2
  * 1.28.10-asm.24
  * 1.27.9-asm.34

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.27 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | Moderate |  [CVE-2026-73511](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-73511)  
  
Description | Severity | Notes  
---|---|---  
Fixes cross-user response poisoning involving generic, non-WebSocket HTTP upgrades by pausing payloads until the upgrade is accepted. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.7-asm.2
  * 1.28.10-asm.24
  * 1.27.9-asm.34

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.27 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | High |  [CVE-2026-73548](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-73548)  
  
Description | Severity | Notes  
---|---|---  
Fixes an HTTP/2 memory-exhaustion issue where discarded duplicate Host headers were not included in request header limits, preventing potential proxy termination. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.7-asm.2
  * 1.28.10-asm.24
  * 1.27.9-asm.34

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.27 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | High |  [CVE-2026-73550](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-73550)  
  
Description | Severity | Notes  
---|---|---  
Fixes an authorization bypass when ignore_path_parameters_in_path_matching was enabled by ensuring RBAC path matchers apply the same path parameter handling as routing. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.7-asm.2
  * 1.28.10-asm.24
  * 1.27.9-asm.34

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.27 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | High |  [CVE-2026-73553](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-73553)  
  
  
## GCP-2026-045

**Published:** 2026-06-29

Description | Severity | Notes  
---|---|---  
Fixes a vulnerability where blocked QPACK decoding can cause a Denial-of-Service Attack against the HTTP/3 stack. 

#### What should I do?

**Check if your clusters are impacted** All in-cluster Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.5-asm.5
  * 1.28.9-asm.4
  * 1.27.9-asm.9

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.26 or later.  **Managed** Cloud Service Mesh is not affected by this CVE.  | High |  [GHSA-p7c7-7c47-pwch](https://github.com/envoyproxy/envoy/security/advisories/GHSA-p7c7-7c47-pwch)  
  
  
## GCP-2026-040

**Published:** 2026-06-23

Description | Severity | Notes  
---|---|---  
The fix correctly discards TLVs over the size limit. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.5-asm.3
  * 1.28.9-asm.2
  * 1.27.9-asm.8

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.26 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | Moderate |  [CVE-2026-47692](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47692)  
  
Description | Severity | Notes  
---|---|---  
Fixes ext_proc issue with packed responses. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.5-asm.3
  * 1.28.9-asm.2
  * 1.27.9-asm.8

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.26 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | Moderate |  [CVE-2026-47207](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47207)  
  
Description | Severity | Notes  
---|---|---  
Fixes ext_authz per route client uaf crash. 

#### What should I do?

**Check if your clusters are impacted** Only the latest 1.28 and 1.29 Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.28.9-asm.2
  * 1.27.9-asm.8

| Moderate |  [CVE-2026-47205](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47205)  
  
Description | Severity | Notes  
---|---|---  
Fixes a bug where REQUESTED_SERVER_NAME may crash envoy. 

#### What should I do?

**Check if your clusters are impacted** Only the latest 1.29 Cloud Service Mesh version is impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.5-asm.3

| High |  [CVE-2026-47220](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47220)  
  
Description | Severity | Notes  
---|---|---  
Fixed an issue when handling HTTP internal redirects for body-less requests. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.5-asm.3
  * 1.28.9-asm.2
  * 1.27.9-asm.8

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.26 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | Moderate |  [CVE-2026-47221](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47221)  
  
Description | Severity | Notes  
---|---|---  
Enforce MaxInflateRatio inside the decompressor inner loop to prevent OOM from crafted payloads. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.5-asm.3
  * 1.28.9-asm.2
  * 1.27.9-asm.8

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.26 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | High |  [CVE-2026-48044](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-48044)  
  
Description | Severity | Notes  
---|---|---  
Cancel token client on filter destroy to avoid UAF. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.5-asm.3
  * 1.28.9-asm.2
  * 1.27.9-asm.8

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.26 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | Moderate |  [CVE-2026-48090](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-48090)  
  
Description | Severity | Notes  
---|---|---  
Fixes embedded NUL byte SAN validation bypass vulnerability. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.5-asm.3
  * 1.28.9-asm.2
  * 1.27.9-asm.8

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.26 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | Moderate |  [CVE-2026-47778](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47778)  
  
Description | Severity | Notes  
---|---|---  
Fixes direct response grpc status issue. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.5-asm.3
  * 1.28.9-asm.2
  * 1.27.9-asm.8

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.26 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | Moderate |  [CVE-2026-47204](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47204)  
  
Description | Severity | Notes  
---|---|---  
Fix sanity checking of the query name length to avoid abnormal process termination. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.5-asm.3
  * 1.28.9-asm.2
  * 1.27.9-asm.8

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.26 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | Moderate |  [CVE-2026-48497](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-48497)  
  
Description | Severity | Notes  
---|---|---  
Fixes TcpStatsdSync buffer overflow issue with a large status name. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.5-asm.3
  * 1.28.9-asm.2
  * 1.27.9-asm.8

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.26 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | Moderate |  [CVE-2026-48706](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-48706)  
  
Description | Severity | Notes  
---|---|---  
Validates HTTP/3 headers-only request and response content-length. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.5-asm.3
  * 1.28.9-asm.2
  * 1.27.9-asm.8

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.26 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | High |  [CVE-2026-48743](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-48743)  
  
Description | Severity | Notes  
---|---|---  
Fixes the padding oracle in OAuth2 code. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.5-asm.3
  * 1.28.9-asm.2
  * 1.27.9-asm.8

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.26 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | Moderate |  [CVE-2026-47775](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47775)  
  
Description | Severity | Notes  
---|---|---  
Fixes stack overflow in destructor by limiting nesting depth. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.29.5-asm.3
  * 1.28.9-asm.2
  * 1.27.9-asm.8

If you're using Cloud Service Mesh v1.26 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.26 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | High |  [CVE-2026-48042](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-48042)  
  
  
## GCP-2026-035

**Published:** 2026-06-08

Description | Severity | Notes  
---|---|---  
A vulnerability in Envoy's HTTP/2 downstream request processing allows an unauthenticated remote client to trigger excessive memory consumption, potentially resulting in OOM termination of the Envoy process and denial of service. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, [upgrade your cluster](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to one of the following patched versions: 

  * 1.28.7-asm.4
  * 1.27.9-asm.5
  * 1.26.8-asm.11

If you're using Cloud Service Mesh v1.25 or earlier, your release has reached end of life and is no longer supported. This CVE fix has not been backported. Upgrade to v1.26 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | High |  [CVE-2026-47774](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-47774)  
  
  
## GCP-2026-013

**Published:** 2026-03-11

Description | Severity | Notes  
---|---|---  
Fixes multivalue header bypass in RBAC. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, upgrade your cluster to one of the following patched versions: 

  * 1.28.5-asm.9
  * 1.27.8-asm.7
  * 1.26.8-asm.3

If you're using Cloud Service Mesh v1.25 or earlier, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. Upgrade to version 1.26 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | High |  [CVE-2026-26308](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-26308)  
  
Description | Severity | Notes  
---|---|---  
Fixes an off-by-one write that could corrupt the string null terminator. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, upgrade your cluster to one of the following patched versions: 

  * 1.28.5-asm.9
  * 1.27.8-asm.7
  * 1.26.8-asm.3

If you're using Cloud Service Mesh v1.25 or earlier, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. Upgrade to version 1.26 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | Moderate |  [CVE-2026-26309](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-26309)  
  
Description | Severity | Notes  
---|---|---  
Fixes crash in `getAddressWithPort() when called with a scoped IPv6 address. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, upgrade your cluster to one of the following patched versions: 

  * 1.28.5-asm.9
  * 1.27.8-asm.7
  * 1.26.8-asm.3

If you're using Cloud Service Mesh v1.25 or earlier, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. Upgrade to version 1.26 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | Moderate |  [CVE-2026-26310](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-26310)  
  
Description | Severity | Notes  
---|---|---  
Ensures decode* methods are blocked after a downstream reset. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, upgrade your cluster to one of the following patched versions: 

  * 1.28.5-asm.9
  * 1.27.8-asm.7
  * 1.26.8-asm.3

If you're using Cloud Service Mesh v1.25 or earlier, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. Upgrade to version 1.26 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | Moderate |  [CVE-2026-26311](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-26311)  
  
Description | Severity | Notes  
---|---|---  
Fixes a bug where response phase limit may result in crash. 

#### What should I do?

**Check if your clusters are impacted** Only in-cluster Cloud Service Mesh version 1.28.2-asm.4 is impacted by this CVE.  This CVE does not affect Cloud Service Mesh with a managed control plane. **Mitigation** For **in-cluster** Cloud Service Mesh, upgrade your cluster to the following patched version: >1.28.5-asm.9.  For **managed** Cloud Service Mesh, no action is required. This CVE does not affect Cloud Service Mesh with a managed control plane.  | Moderate |  [CVE-2026-26330](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-26330)  
  
Description | Severity | Notes  
---|---|---  
Fixes JSON Web Key Set private key leakage vulnerability. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, upgrade your cluster to one of the following patched versions: 

  * 1.28.5-asm.9
  * 1.27.8-asm.7
  * 1.26.8-asm.3

If you're using Cloud Service Mesh v1.25 or earlier, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. Upgrade to version 1.26 or later.  For **managed** Cloud Service Mesh, follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | High |  [CVE-2026-31837](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-31837)  
  
Description | Severity | Notes  
---|---|---  
Fixes a bug where debug Endpoints Allow Cross-Namespace Proxy Data Access 

#### What should I do?

**Check if your clusters are impacted** Only in-cluster Cloud Service Mesh versions 1.27 and 1.28 are impacted by this CVE.  **Mitigation** For **in-cluster** Cloud Service Mesh, upgrade your cluster to one of the following patched versions: 

  * 1.28.5-asm.9
  * 1.27.8-asm.7

If you're using Cloud Service Mesh v1.25 or earlier, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. Upgrade to version 1.26 or later.  For **managed** Cloud Service Mesh, no action is required. This CVE does not affect Cloud Service Mesh with a managed control plane.  | Medium |  [CVE-2026-31838](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-31838)  
  
  
## GCP-2025-073

**Published:** 2025-12-03

Description | Severity | Notes  
---|---|---  
TLS certificate matcher for `match_typed_subject_alt_names` may incorrectly treat certificates containing an embedded null byte. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if it uses an in-cluster Cloud Service Mesh patch version earlier than: 

  * 1.27.4-asm.1
  * 1.26.7-asm.1
  * 1.25.6-asm.1

This CVE does not affect Cloud Service Mesh with a managed control plane.  **Mitigation** For **in-cluster** Cloud Service Mesh, Upgrade your cluster to one of the following patched versions: 

  * 1.27.4-asm.1
  * 1.26.7-asm.1
  * 1.25.6-asm.1

If you're using Cloud Service Mesh v1.24 or earlier, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. Upgrade to version 1.25 or later.  For **managed** Cloud Service Mesh, no action is required. This CVE does not affect Cloud Service Mesh with a managed control plane.  | Medium |  [CVE-2025-66220](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-CVE-2025-66220)  
  
Description | Severity | Notes  
---|---|---  
Envoy crashes when JWT authentication is configured with the remote JWKS fetching. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if it uses an in-cluster Cloud Service Mesh patch version earlier than: 

  * 1.27.4-asm.1
  * 1.26.7-asm.1
  * 1.25.6-asm.1

Your cluster is impacted if it uses a managed Cloud Service Mesh version earlier than:

  * 1.21.6-asm.7
  * 1.20.8-asm.59
  * 1.19.10-asm.54

**Mitigation** For **in-cluster** Cloud Service Mesh, upgrade your cluster to one of the following patched versions: 

  * 1.27.4-asm.1
  * 1.26.7-asm.1
  * 1.25.6-asm.1

If you're using Cloud Service Mesh v1.24 or earlier, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. Upgrade to version 1.25 or later.  For **managed** Cloud Service Mesh, please follow the instructions in the MSA. All versions remain supported and your system will be automatically updated over the coming weeks.  | Medium |  [CVE-2025-64527](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-64527)  
  
Description | Severity | Notes  
---|---|---  
Potential request smuggling from early data after the `CONNECT` upgrade. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if it uses an in-cluster Cloud Service Mesh patch version earlier than: 

  * 1.27.4-asm.1
  * 1.26.7-asm.1
  * 1.25.6-asm.1

This CVE does not affect Cloud Service Mesh with a managed control plane.  **Mitigation** For **in-cluster** Cloud Service Mesh, upgrade your cluster to one of the following patched versions: 

  * 1.27.4-asm.1
  * 1.26.7-asm.1
  * 1.25.6-asm.1

If you're using Cloud Service Mesh v1.24 or earlier, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. Upgrade to version 1.25 or later.  For **managed** Cloud Service Mesh, no action is required. This CVE does not affect Cloud Service Mesh with a managed control plane.  | Medium |  [CVE-2025-64763](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-CVE-2025-64763)  
  
  
## GCP-2025-064

**Published:** 2025-10-28

Description | Severity | Notes  
---|---|---  
Lua filters may crash Envoy when handling a large response body. 

#### What should I do?

**Check whether your clusters are impacted:** Your cluster is impacted if your patch versions are earlier than:

  * 1.27.2-asm.1
  * 1.26.5-asm.1
  * 1.25.5-asm.9

If you're using Cloud Service Mesh v1.24 or earlier, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. Upgrade to version 1.25 or later.  **Mitigation** For **in-cluster** Cloud Service Mesh, upgrade your cluster to one of the following patched versions: 

  * 1.27.2-asm.1
  * 1.26.5-asm.1
  * 1.25.5-asm.9

For **managed** Cloud Service Mesh, no action is required. All versions remain supported and your system will be automatically updated over the coming weeks.  | Medium |  [CVE-2025-62504](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-62504)  
  
Description | Severity | Notes  
---|---|---  
Large requests or responses may crash the TCP connection pool. 

#### What should I do?

**Check whether your clusters are impacted:** Your cluster is impacted if your patch versions are earlier than:

  * 1.27.2-asm.1
  * 1.26.5-asm.1
  * 1.25.5-asm.9

If you're using Cloud Service Mesh v1.24 or earlier, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. Upgrade to version 1.25 or later.  **Mitigation** For **in-cluster** Cloud Service Mesh, upgrade your cluster to one of the following patched versions: 

  * 1.27.2-asm.1
  * 1.26.5-asm.1
  * 1.25.5-asm.9

For **managed** Cloud Service Mesh, no action is required. All versions remain supported and your system will be automatically updated over the coming weeks.  | Medium |  [CVE-2025-62409](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-62409)  
  
  
## GCP-2025-048

**Published:** 2025-09-02

Description | Severity | Notes  
---|---|---  
Use after free in DNS cache. 

#### What should I do?

**Check if your clusters are impacted** Only clusters running in-cluster Cloud Service Mesh version 1.26 are affected. **If you are running a managed Cloud Service Mesh, you are not affected and do not need to take any action.** **Mitigation** If you are running in-cluster Cloud Service Mesh 1.26, [upgrade any affected clusters](https://docs.cloud.google.com/service-mesh/docs/upgrade/upgrade) to 1.26.4-asm.1.  | High |  [CVE-2025-54588](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-54588)  
  
  
## GCP-2024-065

Description | Severity | Notes  
---|---|---  
Happy Eyeballs: Validate that additional_address are IP addresses instead of crashing when sorting. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if patch versions earlier than:

  * 1.23.4-asm.1
  * 1.22.7-asm.1

**Mitigation** For **in-cluster** Cloud Service Mesh, Upgrade your cluster to one of the following patched versions: 

  * 1.23.4-asm.1
  * 1.22.7-asm.1

If you're using Cloud Service Mesh v1.20 or earlier, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to version 1.21 or later.  For **managed** Cloud Service Mesh, no action is required. All versions remain supported and your system will be automatically updated over the coming weeks.  | Medium |  [CVE-2024-53269](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53269)  
  
Description | Severity | Notes  
---|---|---  
HTTP/1: Sending overload crashes when the request is reset beforehand. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if patch versions earlier than:

  * 1.23.4-asm.1
  * 1.22.7-asm.1
  * 1.21.5-asm.17
  * 1.20.8-asm.14
  * 1.19.10-asm.24

**Mitigation** For **in-cluster** Cloud Service Mesh, Upgrade your cluster to one of the following patched versions: 

  * 1.23.4-asm.1
  * 1.22.7-asm.1
  * 1.21.5-asm.17

If you're using Cloud Service Mesh v1.20 or earlier, your release has reached end of life and is no longer supported. If you're using Cloud Service Mesh v1.20 or earlier, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to version 1.21 or later.  For **managed** Cloud Service Mesh, no action is required. All versions remain supported and your system will be automatically updated over the coming weeks.  | High |  [CVE-2024-53270](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53270)  
  
Description | Severity | Notes  
---|---|---  
HTTP/1.1 Multiple issues with envoy.reloadable_features.http1_balsa_delay_reset. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if patch versions earlier than:

  * 1.23.4-asm.1

**Mitigation** For **in-cluster** Cloud Service Mesh, Upgrade your cluster to one of the following patched versions: 

  * 1.23.4-asm.1

If you're using Cloud Service Mesh v1.20 or earlier, your release has reached end of life and is no longer supported. If you're using Cloud Service Mesh v1.20 or earlier, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to version 1.21 or later.  For **managed** Cloud Service Mesh, no action is required. All versions remain supported and your system will be automatically updated over the coming weeks.  | High |  [CVE-2024-53271](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-53271)  
  
  
## GCP-2024-052

**Published:** 2024-09-19

Description | Severity | Notes  
---|---|---  
oghttp2 crash on OnBeginHeadersForStream 

#### What should I do?

**Check if your clusters are impacted** Only clusters running Cloud Service Mesh v1.23 are affected **Mitigation** Cloud Service Mesh 1.23.2-asm.2 contains the fix for this issue. No action is required.  | High |  [CVE-2024-45807](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45807)  
  
Description | Severity | Notes  
---|---|---  
Malicious log injection via access logs 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE. **Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.20.8-asm.7
  * 1.21.5-asm.7
  * 1.22.5-asm.1
  * 1.23.2-asm.2

| Medium |  [CVE-2024-45808](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45808)  
  
Description | Severity | Notes  
---|---|---  
Potential to manipulate `x-envoy` headers from external sources 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE. **Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.20.8-asm.7
  * 1.21.5-asm.7
  * 1.22.5-asm.1
  * 1.23.2-asm.2

| Medium |  [CVE-2024-45806](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45806)  
  
Description | Severity | Notes  
---|---|---  
JWT filter crash in the clear route cache with remote JWKs 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE. **Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.20.8-asm.7
  * 1.21.5-asm.7
  * 1.22.5-asm.1
  * 1.23.2-asm.2

| Medium |  [CVE-2024-45809](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45809)  
  
Description | Severity | Notes  
---|---|---  
Envoy crashes for LocalReply in http async client 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE. **Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.20.8-asm.7
  * 1.21.5-asm.7
  * 1.22.5-asm.1
  * 1.23.2-asm.2

| Medium |  [CVE-2024-45810](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-45810)  
  
  
## GCP-2024-032

**Published:** 2024-06-24

Description | Severity | Notes  
---|---|---  
Envoy incorrectly accepts HTTP 200 response for entering upgrade mode. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE. **Mitigation** If you are running managed Cloud Service Mesh, your system will be automatically updated over the coming days.  Otherwise, upgrade your cluster to one of the following patched versions: 

  * v1.21.3-asm.3
  * v1.20.7-asm.2
  * v1.19.10-asm.6
  * v1.18.7-asm.26
  * If you're using Cloud Service Mesh v1.17 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.18 or above.

| Medium |  [CVE-2024-23326](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23326)  
  
Description | Severity | Notes  
---|---|---  
Crash in EnvoyQuicServerStream::OnInitialHeadersComplete(). 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE. **Mitigation** If you are running managed Cloud Service Mesh, your system will be automatically updated over the coming days.  Otherwise, upgrade your cluster to one of the following patched versions: 

  * v1.21.3-asm.3
  * v1.20.7-asm.2
  * v1.19.10-asm.6
  * v1.18.7-asm.26
  * If you're using Cloud Service Mesh v1.17 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.18 or above.

| Medium |  [CVE-2024-32974](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-32974)  
  
Description | Severity | Notes  
---|---|---  
Crash in QuicheDataReader::PeekVarInt62Length(). 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE. **Mitigation** If you are running managed Cloud Service Mesh, your system will be automatically updated over the coming days.  Otherwise, upgrade your cluster to one of the following patched versions: 

  * v1.21.3-asm.3
  * v1.20.7-asm.2
  * v1.19.10-asm.6
  * v1.18.7-asm.26
  * If you're using Cloud Service Mesh v1.17 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.18 or above.

| Medium |  [CVE-2024-32975](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-32975)  
  
Description | Severity | Notes  
---|---|---  
Endless loop while decompressing Brotli data with extra input. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE. **Mitigation** If you are running managed Cloud Service Mesh, your system will be automatically updated over the coming days.  Otherwise, upgrade your cluster to one of the following patched versions: 

  * v1.21.3-asm.3
  * v1.20.7-asm.2
  * v1.19.10-asm.6
  * v1.18.7-asm.26
  * If you're using Cloud Service Mesh v1.17 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.18 or above.

| High |  [CVE-2024-32976](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-32976)  
  
Description | Severity | Notes  
---|---|---  
Crash (use-after-free) in EnvoyQuicServerStream. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE. **Mitigation** If you are running managed Cloud Service Mesh, your system will be automatically updated over the coming days.  Otherwise, upgrade your cluster to one of the following patched versions: 

  * v1.21.3-asm.3
  * v1.20.7-asm.2
  * v1.19.10-asm.6
  * v1.18.7-asm.26
  * If you're using Cloud Service Mesh v1.17 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.18 or above.

| Medium |  [CVE-2024-34362](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-34362)  
  
Description | Severity | Notes  
---|---|---  
Crash due to uncaught nlohmann JSON exception. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE. **Mitigation** If you are running managed Cloud Service Mesh, your system will be automatically updated over the coming days.  Otherwise, upgrade your cluster to one of the following patched versions: 

  * v1.21.3-asm.3
  * v1.20.7-asm.2
  * v1.19.10-asm.6
  * v1.18.7-asm.26
  * If you're using Cloud Service Mesh v1.17 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.18 or above.

| High |  [CVE-2024-34363](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-34363)  
  
Description | Severity | Notes  
---|---|---  
Envoy OOM vector from HTTP async client with unbounded response buffer for mirror response. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE. **Mitigation** If you are running managed Cloud Service Mesh, your system will be automatically updated over the coming days.  Otherwise, upgrade your cluster to one of the following patched versions: 

  * v1.21.3-asm.3
  * v1.20.7-asm.2
  * v1.19.10-asm.6
  * v1.18.7-asm.26
  * If you're using Cloud Service Mesh v1.17 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.18 or above.

| Medium |  [CVE-2024-34364](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-34364)  
  
  
## GCP-2024-023

**Published:** 2024-04-24

Description | Severity | Notes  
---|---|---  
HTTP/2: memory exhaustion due to CONTINUATION frame flood. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE. **Mitigation** If you are running managed Cloud Service Mesh, no action is required. Your system will be automatically updated over the coming days.  If you are running in-cluster Cloud Service Mesh, you must upgrade your cluster to one of the following patched versions: 

  * 1.20.6-asm.0
  * 1.19.10-asm.0
  * 1.18.7-asm.21

If you're using Cloud Service Mesh v1.17 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh v1.18 or later.  | High |  [CVE-2024-27919](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-27919)  
  
Description | Severity | Notes  
---|---|---  
HTTP/2: CPU exhaustion due to CONTINUATION frame flood 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE. **Mitigation** If you are running managed Cloud Service Mesh, no action is required. Your system will be automatically updated over the coming days.  If you are running in-cluster Cloud Service Mesh, you must upgrade your cluster to one of the following patched versions: 

  * 1.20.6-asm.0
  * 1.19.10-asm.0
  * 1.18.7-asm.21

If you're using Cloud Service Mesh v1.17 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.18 or later.  | Medium |  [CVE-2024-30255](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-30255)  
  
Description | Severity | Notes  
---|---|---  
Abnormal termination when using `auto_sni` with ':authority' header longer than 255 characters. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE. **Mitigation** If you are running managed Cloud Service Mesh, no action is required. Your system will be automatically updated over the coming days.  If you are running in-cluster Cloud Service Mesh, you must upgrade your cluster to one of the following patched versions: 

  * 1.20.6-asm.0
  * 1.19.10-asm.0
  * 1.18.7-asm.21

If you're using Cloud Service Mesh v1.17 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.18 or above.  | High |  [CVE-2024-32475](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-32475)  
  
Description | Severity | Notes  
---|---|---  
HTTP/2 CONTINUATION frames can be utilized for DoS attacks. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE. **Mitigation** If you are running managed Cloud Service Mesh, no action is required. Your system will be automatically updated over the coming days.  If you are running in-cluster Cloud Service Mesh, you must upgrade your cluster to one of the following patched versions: 

  * 1.20.6-asm.0
  * 1.19.10-asm.0
  * 1.18.7-asm.21

If you're using Cloud Service Mesh v1.17 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to version v1.18 or later.  | Not Provided |  [CVE-2023-45288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45288)  
  
  
## GCP-2024-007

**Published:** 2024-02-08

Description | Severity | Notes  
---|---|---  
Envoy crashes when idle and requests per try timeout occur within the backoff interval. 

#### What should I do?

If you are running managed Cloud Service Mesh, no action is required. Your system will be automatically updated over the coming days.  If you are running in-cluster Cloud Service Mesh, you must upgrade your cluster to one of the following patched versions: 

  * 1.20.3-asm.4
  * 1.19.7-asm.3
  * 1.18.7-asm.4
  * 1.17.8-asm.20

If you're using Anthos Service Mesh v1.17 or earlier, your release has reached end of life and is no longer supported. While these CVE fixes have been backported to 1.17, you should upgrade to 1.18 or later.  | High |  [CVE-2024-23322](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23322)  
  
Description | Severity | Notes  
---|---|---  
Excessive CPU usage when URI template matcher is configured using regex. 

#### What should I do?

If you are running managed Cloud Service Mesh, no action is required. Your system will be automatically updated over the coming days.  If you are running in-cluster Cloud Service Mesh, you must upgrade your cluster to one of the following patched versions: 

  * 1.20.3-asm.4
  * 1.19.7-asm.3
  * 1.18.7-asm.4
  * 1.17.8-asm.20

If you're using Anthos Service Mesh v1.17 or earlier, your release has reached end of life and is no longer supported. While these CVE fixes have been backported to 1.17, you should upgrade to 1.18 or later.  | Medium |  [CVE-2024-23323](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23323)  
  
Description | Severity | Notes  
---|---|---  
External authorization can be bypassed when Proxy protocol filter sets invalid UTF-8 metadata. 

#### What should I do?

If you are running managed Cloud Service Mesh, no action is required. Your system will be automatically updated over the coming days.  If you are running in-cluster Cloud Service Mesh, you must upgrade your cluster to one of the following patched versions: 

  * 1.20.3-asm.4
  * 1.19.7-asm.3
  * 1.18.7-asm.4
  * 1.17.8-asm.20

If you're using Anthos Service Mesh v1.17 or earlier, your release has reached end of life and is no longer supported. While these CVE fixes have been backported to 1.17, you should upgrade to 1.18 or later.  | High |  [CVE-2024-23324](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23324)  
  
Description | Severity | Notes  
---|---|---  
Envoy crashes when using an address type that isn't supported by the OS. 

#### What should I do?

If you are running managed Cloud Service Mesh, no action is required. Your system will be automatically updated over the coming days.  If you are running in-cluster Cloud Service Mesh, you must upgrade your cluster to one of the following patched versions: 

  * 1.20.3-asm.4
  * 1.19.7-asm.3
  * 1.18.7-asm.4
  * 1.17.8-asm.20

If you're using Anthos Service Mesh v1.17 or earlier, your release has reached end of life and is no longer supported. While these CVE fixes have been backported to 1.17, you should upgrade to 1.18 or later.  | High |  [CVE-2024-23325](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23325)  
  
Description | Severity | Notes  
---|---|---  
Crash in proxy protocol when command type is `LOCAL`. 

#### What should I do?

If you are running managed Cloud Service Mesh, no action is required. Your system will be automatically updated over the coming days.  If you are running in-cluster Cloud Service Mesh, you must upgrade your cluster to one of the following patched versions: 

  * 1.20.3-asm.4
  * 1.19.7-asm.3
  * 1.18.7-asm.4
  * 1.17.8-asm.20

If you're using Anthos Service Mesh v1.17 or earlier, your release has reached end of life and is no longer supported. While these CVE fixes have been backported to 1.17, you should upgrade to 1.18 or later.  | High |  [CVE-2024-23327](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-23327)  
  
  
## GCP-2023-031

**Published:** 2023-10-10

Description | Severity | Notes  
---|---|---  
A denial of service attack can affect the data plane when using the HTTP/2 protocol. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if it uses Cloud Service Mesh patch versions earlier than 1.18.4, 1.17.7, or 1.16.7. **Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.18.4-asm.0
  * 1.17.7-asm.0
  * 1.16.7-asm.10

If you are running managed Cloud Service Mesh, your system will be automatically updated within the next few days.  If you're using Cloud Service Mesh v1.15 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to v1.16 or above.  | High |  [CVE-2023-44487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44487)  
  
  
## GCP-2023-021

**Updated:** 2023-07-26

**Published: 2022-07-25** Description | Severity | Notes  
---|---|---  
A malicious client is able to construct credentials with permanent validity in some specific scenarios. For example, the combination of host and expiration time in the HMAC payload can be always valid in OAuth2 filter's HMAC check. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if it uses Cloud Service Mesh patch versions earlier than

  * 1.17.4
  * 1.16.6
  * 1.15.7

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.17.5-asm.0
  * 1.16.7-asm.0
  * 1.15.7-asm.23

**If you are running managed Cloud Service Mesh** , your system will be automatically updated within the next few days.  If you're using Anthos Service Mesh 1.14 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to ASM 1.15 or above.  | High |  [CVE-2023-35941](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35941)  
  
Description | Severity | Notes  
---|---|---  
gRPC access loggers using the listener's global scope can cause a use-after-free crash when the listener is drained. This can be triggered by an LDS update with the same gRPC access log configuration. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if it uses Cloud Service Mesh patch versions earlier than

  * 1.17.4
  * 1.16.6
  * 1.15.7

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.17.5-asm.0
  * 1.16.7-asm.0
  * 1.15.7-asm.23

**If you are running managed Cloud Service Mesh** , your system will be automatically updated within the next few days.  If you're using Anthos Service Mesh 1.14 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to ASM 1.15 or above.  | Medium |  [CVE-2023-35942](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35942)  
  
Description | Severity | Notes  
---|---|---  
If `origin` header is configured to be removed with request_headers_to_remove: origin, CORS filter will segfault and crash Envoy. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if it uses Cloud Service Mesh patch versions earlier than

  * 1.17.4
  * 1.16.6
  * 1.15.7

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.17.5-asm.0
  * 1.16.7-asm.0
  * 1.15.7-asm.23

**If you are running managed Cloud Service Mesh** , your system will be automatically updated within the next few days.  If you're using Anthos Service Mesh 1.14 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to ASM 1.15 or above.  | Medium |  [CVE-2023-35943](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35943)  
  
Description | Severity | Notes  
---|---|---  
Attackers can send mixed scheme requests to bypass some scheme checks in Envoy. For example, if a request with mixed scheme htTp is sent to the OAuth2 filter, it will fail the exact-match checks for http, and inform the remote endpoint the scheme is https, thus potentially bypassing OAuth2 checks specific to HTTP requests. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if it uses Cloud Service Mesh patch versions earlier than

  * 1.17.4
  * 1.16.6
  * 1.15.7

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.17.5-asm.0
  * 1.16.7-asm.0
  * 1.15.7-asm.23

**If you are running managed Cloud Service Mesh** , your system will be automatically updated within the next few days.  If you're using Anthos Service Mesh 1.14 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to ASM 1.15 or above.  | High |  [CVE-2023-35944](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35944)  
  
  
## GCP-2023-019

Description | Severity | Notes  
---|---|---  
A specifically crafted response from an untrusted upstream service can cause a denial of service through memory exhaustion. This is caused by Envoy's HTTP/2 codec which may leak a header map and bookkeeping structures upon receiving RST_STREAM immediately followed by the GOAWAY frames from an upstream server. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if it uses Cloud Service Mesh patch versions earlier than

  * 1.17.4
  * 1.16.6
  * 1.15.7

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.17.4-asm.2
  * 1.16.6-asm.3
  * 1.15.7-asm.21

**If you are running managed Cloud Service Mesh** , your system will be automatically updated within the next few days.  If you're using Anthos Service Mesh 1.14 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to ASM 1.15 or above.  | High |  [CVE-2023-35945](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-35945)  
  
  
## GCP-2023-002

Description | Severity | Notes  
---|---|---  
If Envoy is running with the OAuth filter enabled exposed, a malicious actor could construct a request which would cause denial of service by crashing Envoy. 

#### What should I do?

**Check if your clusters are impacted** Your clusters are impacted if they use Cloud Service Mesh patch versions earlier than:

  * 1.16.4
  * 1.15.7
  * 1.14.6

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.16.4-asm.2
  * 1.15.7-asm.1
  * 1.14.6-asm.11

If you're using Cloud Service Mesh v1.13 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.14 or above.  | Medium |  [CVE-2023-27496](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27496)  
  
Description | Severity | Notes  
---|---|---  
The attacker can use this vulnerability to bypass auth checks when ext_authz is used. 

#### What should I do?

**Check if your clusters are impacted** Your clusters are impacted if they use Cloud Service Mesh patch versions earlier than:

  * 1.16.4
  * 1.15.7
  * 1.14.6

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.16.4-asm.2
  * 1.15.7-asm.1
  * 1.14.6-asm.11

If you're using Cloud Service Mesh v1.13 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh} 1.14 or above.  | Medium |  [CVE-2023-27488](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27488)  
  
Description | Severity | Notes  
---|---|---  
Envoy configuration must also include an option to add request headers that were generated using inputs from the request, i.e. the peer certificate SAN. 

#### What should I do?

**Check if your clusters are impacted** Your clusters are impacted if they use Cloud Service Mesh patch versions earlier than:

  * 1.16.4
  * 1.15.7
  * 1.14.6

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.16.4-asm.2
  * 1.15.7-asm.1
  * 1.14.6-asm.11

If you're using Cloud Service Mesh v1.13 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.14 or above.  | High |  [CVE-2023-27493](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27493)  
  
Description | Severity | Notes  
---|---|---  
Attackers can send large request bodies for routes that have Lua filter enabled and trigger crashes. 

#### What should I do?

**Check if your clusters are impacted** Your clusters are impacted if they use Cloud Service Mesh patch versions earlier than:

  * 1.16.4
  * 1.15.7
  * 1.14.6

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.16.4-asm.2
  * 1.15.7-asm.1
  * 1.14.6-asm.11

If you're using Cloud Service Mesh v1.13 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.14 or above.  | Medium |  [CVE-2023-27492](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27492)  
  
Description | Severity | Notes  
---|---|---  
Attackers can send specifically crafted HTTP/2 or HTTP/3 requests to trigger parsing errors on HTTP/1 upstream service. 

#### What should I do?

**Check if your clusters are impacted** Your clusters are impacted if they use Cloud Service Mesh patch versions earlier than:

  * 1.16.4
  * 1.15.7
  * 1.14.6

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.16.4-asm.2
  * 1.15.7-asm.1
  * 1.14.6-asm.11

If you're using Cloud Service Mesh v1.13 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.14 or above.  | Medium |  [CVE-2023-27491](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27491)  
  
Description | Severity | Notes  
---|---|---  
The header x-envoy-original-path should be an internal header, but Envoy does not remove this header from the request at the beginning of request processing when it is sent from an untrusted client. 

#### What should I do?

**Check if your clusters are impacted** Your clusters are impacted if they use Cloud Service Mesh patch versions earlier than:

  * 1.16.4
  * 1.15.7
  * 1.14.6

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.16.4-asm.2
  * 1.15.7-asm.1
  * 1.14.6-asm.11

If you're using Cloud Service Mesh v1.13 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.14 or above.  | High |  [CVE-2023-27487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-27487)  
  
  
## GCP-2022-020

**Published: 2022-10-05**   
**Updated: 2022-10-12**   
**2022-10-12 Update:** Updated link to CVE description and added information about automatic updates for managed Cloud Service Mesh. Description | Severity | Notes  
---|---|---  
The Istio control plane `istiod` is vulnerable to a request processing error, allowing a malicious attacker that sends a specially crafted message which results in the control plane crashing when the validating webhook for a cluster is exposed publicly. This endpoint is served over TLS port 15017, but does not require any authentication from the attacker. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if it uses Cloud Service Mesh patch versions earlier than 1.14.4, 1.13.8, or 1.12.9. **Mitigation** **If you are running standalone Cloud Service Mesh** , upgrade your cluster to one of the following patched versions: 

  * If you're using Anthos Service Mesh 1.14, upgrade to v1.14.4-asm.2
  * If you're using Anthos Service Mesh 1.13, upgrade to v1.13.8-asm.4
  * If you're using Anthos Service Mesh 1.12, upgrade to v1.12.9-asm.3

**If you are running managed Cloud Service Mesh** , your system will be automatically updated within the next few days.  If you're using Cloud Service Mesh v1.11 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.12 or later.  | High |  [CVE-2022-39278](https://github.com/istio/istio/security/advisories/GHSA-86vr-4wcv-mm9w)  
  
  
## GCP-2022-015

**Published: 2022-06-09**   
**Updated: 2022-06-10**   
**2022-06-10 Update:** Updated patch versions for Cloud Service Mesh. Description | Severity | Notes  
---|---|---  
Istio data plane can potentially access memory unsafely when the Metadata Exchange and Stats extensions are enabled. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if it uses Cloud Service Mesh patch versions earlier than 1.13.4-asm.4, 1.12.7-asm.2, or 1.11.8-asm.4.  **Cloud Service Mesh Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.13.4-asm.4
  * 1.12.7-asm.2
  * 1.11.8-asm.4

If you're using Cloud Service Mesh v1.10 or earlier, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.11 or later. For more information, see [Upgrading from earlier versions (GKE](https://cloud.google.com/service-mesh/docs/upgrade-path-old-versions-gke) or [Upgrading from earlier versions (on-premises)](https://cloud.google.com/service-mesh/docs/upgrade-path-old-versions-on-prem).  | High |  [CVE-2022-31045](https://github.com/istio/istio/security/advisories/GHSA-xwx5-5c9g-x68x)  
  
Description | Severity | Notes  
---|---|---  
Data can exceed intermediate buffer limits if a malicious attacker passes a small highly compressed payload (also known as a zip bomb attack). 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if it uses Cloud Service Mesh patch versions earlier than 1.13.4-asm.4, 1.12.7-asm.2, or 1.11.8-asm.4.  Although Cloud Service Mesh does not support Envoy filters, you could be impacted if you use a decompress filter. **Cloud Service Mesh Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.13.4-asm.4
  * 1.12.7-asm.2
  * 1.11.8-asm.4

If you're using Cloud Service Mesh v1.10 or earlier, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.11 or later. For more information, see [Upgrading from earlier versions (GKE](https://cloud.google.com/service-mesh/docs/upgrade-path-old-versions-gke) or [Upgrading from earlier versions (on-premises)](https://cloud.google.com/service-mesh/docs/upgrade-path-old-versions-on-prem).  **Envoy Mitigation** Envoy users managing their own Envoys should ensure that they are using Envoy release 1.22.1. Envoy users managing their own Envoys build the binaries from a source like GitHub and deploy them. There's no action to be taken by users who run managed Envoys (Google Cloud provides the Envoy binaries), for which cloud products will switch to 1.22.1.  | High |  [CVE-2022-29225](https://github.com/envoyproxy/envoy/security/advisories/GHSA-75hv-2jjj-89hh)  
  
Description | Severity | Notes  
---|---|---  
Potential null pointer dereference in `GrpcHealthCheckerImpl`. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if it uses Cloud Service Mesh patch versions earlier than 1.13.4-asm.4, 1.12.7-asm.2, or 1.11.8-asm.4.  **Cloud Service Mesh Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.13.4-asm.4
  * 1.12.7-asm.2
  * 1.11.8-asm.4

If you're using Cloud Service Mesh v1.10 or earlier, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.11 or later. For more information, see [Upgrading from earlier versions (GKE](https://cloud.google.com/service-mesh/docs/upgrade-path-old-versions-gke) or [Upgrading from earlier versions (on-premises)](https://cloud.google.com/service-mesh/docs/upgrade-path-old-versions-on-prem).  **Envoy Mitigation** Envoy users managing their own Envoys should ensure that they are using Envoy release 1.22.1. Envoy users managing their own Envoys build the binaries from a source like GitHub and deploy them. There's no action to be taken by users who run managed Envoys (Google Cloud provides the Envoy binaries), for which cloud products will switch to 1.22.1.  | Medium |  [CVE-2021-29224](https://github.com/envoyproxy/envoy/security/advisories/GHSA-m4j9-86g3-8f49)  
  
Description | Severity | Notes  
---|---|---  
OAuth filter allows trivial bypass. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if it uses Cloud Service Mesh patch versions earlier than 1.13.4-asm.4, 1.12.7-asm.2, or 1.11.8-asm.4.  Although Cloud Service Mesh does not support Envoy filters, you could be impacted if you use an OAuth filter. **Cloud Service Mesh Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.13.4-asm.4
  * 1.12.7-asm.2
  * 1.11.8-asm.4

If you're using Cloud Service Mesh v1.10 or earlier, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.11 or later. For more information, see [Upgrading from earlier versions (GKE](https://cloud.google.com/service-mesh/docs/upgrade-path-old-versions-gke) or [Upgrading from earlier versions (on-premises)](https://cloud.google.com/service-mesh/docs/upgrade-path-old-versions-on-prem).  **Envoy Mitigation** Envoy users managing their own Envoys also use the OAuth filter should ensure that they are using Envoy release 1.22.1. Envoy users managing their own Envoys build the binaries from a source like GitHub and deploy them. There's no action to be taken by users who run managed Envoys (Google Cloud provides the Envoy binaries), for which cloud products will switch to 1.22.1.  | Critical |  [CVE-2021-29226](https://github.com/envoyproxy/envoy/security/advisories/GHSA-h45c-2f94-prxh)  
  
Description | Severity | Notes  
---|---|---  
OAuth filter can corrupt memory (earlier versions) or trigger an ASSERT() (later versions). 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if it uses Cloud Service Mesh patch versions earlier than 1.13.4-asm.4, 1.12.7-asm.2, or 1.11.8-asm.4.  Although Cloud Service Mesh does not support Envoy filters, you could be impacted if you use an OAuth filter.  **Cloud Service Mesh Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.13.4-asm.4
  * 1.12.7-asm.2
  * 1.11.8-asm.4

If you're using Cloud Service Mesh v1.10 or earlier, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.11 or later.  **Envoy Mitigation** Envoy users managing their own Envoys also use the OAuth filter should ensure that they are using Envoy release 1.22.1. Envoy users managing their own Envoys build the binaries from a source like GitHub and deploy them. There's no action to be taken by users who run managed Envoys (Google Cloud provides the Envoy binaries), for which cloud products will switch to 1.22.1.  | High |  [CVE-2022-29228](https://github.com/envoyproxy/envoy/security/advisories/GHSA-rww6-8h7g-8jf6)  
  
Description | Severity | Notes  
---|---|---  
Internal redirects crash for requests with body or trailers. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if it uses Cloud Service Mesh patch versions earlier than 1.13.4-asm.4, 1.12.7-asm.2, or 1.11.8-asm.4.  **Cloud Service Mesh Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.13.4-asm.4
  * 1.12.7-asm.2
  * 1.11.8-asm.4

If you're using Cloud Service Mesh v1.10 or earlier, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.11 or later. For more information, see [Upgrading from earlier versions (GKE](https://cloud.google.com/service-mesh/docs/upgrade-path-old-versions-gke) or [Upgrading from earlier versions (on-premises)](https://cloud.google.com/service-mesh/docs/upgrade-path-old-versions-on-prem).  **Envoy Mitigation** Envoy users managing their own Envoys should ensure that they are using Envoy release 1.22.1. Envoy users managing their own Envoys build the binaries from a source like GitHub and deploy them. There's no action to be taken by users who run managed Envoys (Google Cloud provides the Envoy binaries), for which cloud products will switch to 1.22.1.  | High |  [CVE-2022-29227](https://github.com/envoyproxy/envoy/security/advisories/GHSA-rm2p-qvf6-pvr6)  
  
  
## GCP-2022-010

**Published: 2022-03-10**   
**Updated: 2022-03-16** Description | Severity | Notes  
---|---|---  
The Istio control plane, istiod, is vulnerable to a request processing error, allowing a malicious attacker that sends a specially crafted message which results in the control plane crashing when the validating webhook for a cluster is exposed publicly. This endpoint is served over TLS port 15017 but does not require any authentication from the attacker. 

#### What should I do?

**Check if your clusters are impacted** All Cloud Service Mesh versions are impacted by this CVE. Note: If you are using Managed Control Plane, this vulnerability has already been fixed and you are not impacted. **Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.12.5-asm.0
  * 1.11.8-asm.0
  * 1.10.6-asm.2

If you're using Cloud Service Mesh v1.9 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.10 or above.  | High |  [CVE-2022-24726](https://github.com/istio/istio/security/advisories/GHSA-8w5h-qr4r-2h6g)  
  
## GCP-2022-007

**Published: 2022-02-22** Description | Severity | Notes  
---|---|---  
Istiod crashes upon receiving requests with a specially crafted `authorization` header. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if both of the following are true:

  * It uses Cloud Service Mesh patch versions earlier than 1.12.4-asm.1, 1.11.7-asm.1, or 1.10.6-asm.1. 

Note: If you are using Managed Control Plane, this vulnerability has already been fixed and you are not impacted. **Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.12.4-asm.1
  * 1.11.7-asm.1
  * 1.10.6-asm.1

If you're using Cloud Service Mesh v1.9 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.10 or above.  | High |  [CVE-2022-23635](https://github.com/istio/istio/security/advisories/GHSA-856q-xv3c-7f2f)  
  
Description | Severity | Notes  
---|---|---  
Potential null pointer dereference when using JWT filter `safe_regex` match. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if both of the following are true:

  * It uses Cloud Service Mesh patch versions earlier than 1.12.4-asm.1, 1.11.7-asm.1, or 1.10.6-asm.1. 
  * Although Cloud Service Mesh do not support Envoy filters, you could be impacted if you use JWT filter regex.

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.12.4-asm.1
  * 1.11.7-asm.1
  * 1.10.6-asm.1

If you're using Cloud Service Mesh v1.9 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.10 or above.  | Medium |  [CVE-2021-43824](https://github.com/envoyproxy/envoy/security/advisories/GHSA-vj5m-rch8-5r2p)  
  
Description | Severity | Notes  
---|---|---  
Use-after-free when response filters increase response data, and increased data exceeds downstream buffer limits. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if both of the following are true:

  * It uses Cloud Service Mesh patch versions earlier than 1.12.4-asm.1, 1.11.7-asm.1, or 1.10.6-asm.1. 
  * Although Cloud Service Mesh do not support Envoy filters, you could be impacted if you use a decompress filter.

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.12.4-asm.1
  * 1.11.7-asm.1
  * 1.10.6-asm.1

If you're using Cloud Service Mesh v1.9 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.10 or above.  | Medium |  [CVE-2021-43825](https://github.com/envoyproxy/envoy/security/advisories/GHSA-h69p-g6xg-mhhh)  
  
Description | Severity | Notes  
---|---|---  
Use-after-free when tunneling TCP over HTTP, if downstream disconnects during upstream connection establishment. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if both of the following are true:

  * It uses Cloud Service Mesh patch versions earlier than 1.12.4-asm.1, 1.11.7-asm.1, or 1.10.6-asm.1. 
  * Although Cloud Service Mesh do not support Envoy filters, you could be impacted if you use a tunneling filter.

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.12.4-asm.1
  * 1.11.7-asm.1
  * 1.10.6-asm.1

If you're using Cloud Service Mesh v1.9 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.10 or above.  | Medium |  [CVE-2021-43826](https://github.com/envoyproxy/envoy/security/advisories/GHSA-cmx3-fvgf-83mf)  
  
Description | Severity | Notes  
---|---|---  
Incorrect configuration handling allows mTLS session re-use without re-validation after validation settings have changed. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if both of the following are true:

  * It uses Cloud Service Mesh patch versions earlier than 1.12.4-asm.1, 1.11.7-asm.1, or 1.10.6-asm.1. 
  * All Cloud Service Mesh services using mTLS are impacted by this CVE.

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.12.4-asm.1
  * 1.11.7-asm.1
  * 1.10.6-asm.1

If you're using Cloud Service Mesh v1.9 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.10 or above.  | High |  [CVE-2022-21654](https://github.com/envoyproxy/envoy/security/advisories/GHSA-5j4x-g36v-m283)  
  
Description | Severity | Notes  
---|---|---  
Incorrect handling of internal redirects to routes with a direct response entry. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if both of the following are true:

  * It uses Cloud Service Mesh patch versions earlier than 1.12.4-asm.1, 1.11.7-asm.1, or 1.10.6-asm.1. 
  * Although Cloud Service Mesh do not support Envoy filters, you could be impacted if you use a direct response filter.

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.12.4-asm.1
  * 1.11.7-asm.1
  * 1.10.6-asm.1

If you're using Cloud Service Mesh v1.9 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.10 or above.  | High |  [CVE-2022-21655](https://github.com/envoyproxy/envoy/security/advisories/GHSA-7r5p-7fmh-jxpg)  
  
Description | Severity | Notes  
---|---|---  
Stack exhaustion when a cluster is deleted via Cluster Discovery Service. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if both of the following are true:

  * It uses Cloud Service Mesh patch versions earlier than 1.12.4-asm.1 or 1.11.7-asm.1. 

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.12.4-asm.1
  * 1.11.7-asm.1

If you're using Cloud Service Mesh v1.9 or below, your release has reached end of life and is no longer supported. These CVE fixes have not been backported. You should upgrade to Cloud Service Mesh 1.10 or above.  | Medium |  [CVE-2022-23606](https://github.com/envoyproxy/envoy/security/advisories/GHSA-9vp2-4cp7-vvxf)  
  
  
## GCP-2021-016

**Published: 2021-08-24** Description | Severity | Notes  
---|---|---  
Istio contains a remotely exploitable vulnerability where an HTTP request with a [fragment](https://en.wikipedia.org/wiki/URI_fragment) (a section in the end of a URI that begins with a `#` character) in the URI path could bypass Istio’s URI path-based authorization policies.  For example, an Istio authorization policy [denies](https://istio.io/latest/docs/reference/config/security/authorization-policy/#AuthorizationPolicy-Action) requests sent to the URI path `/user/profile`. In the vulnerable versions, a request with the URI path `/user/profile#section1` bypasses the deny policy and routes to the backend (with the normalized URI path `/user/profile%23section1`), which leads to a security incident.  This fix depends on a fix in Envoy, which is associated with [CVE-2021-32779](https://github.com/envoyproxy/envoy/security/advisories/GHSA-r222-74fw-jqr9). 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if both of the following are true:

  * It uses Cloud Service Mesh patch versions earlier than 1.7.8-asm.10, 1.8.6-asm.8, 1.9.8-asm.1, and 1.10.4-asm.6.
  * It uses authorization policies with `[DENY actions](https://istio.io/latest/docs/reference/config/security/authorization-policy/#AuthorizationPolicy-Action)` and `[operation.paths](https://istio.io/latest/docs/reference/config/security/authorization-policy/#Operation)`, or `[ALLOW actions](https://istio.io/latest/docs/reference/config/security/authorization-policy/#AuthorizationPolicy-Action)` and `[operation.notPaths](https://istio.io/latest/docs/reference/config/security/authorization-policy/#Operation)`.

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.10.4-asm.6
  * 1.9.8-asm.1
  * 1.8.6-asm.8
  * 1.7.8-asm.10

With the new versions, the fragment part of the request’s URI is removed before the authorization and routing. This prevents a request with a fragment in its URI from bypassing authorization policies which are based on the URI without the fragment part.  **Opt-out** If you opt-out of this new behavior, the fragment section in the URI is kept. To opt-out, you can configure your installation as follows: 
    
    
    apiVersion: install.istio.io/v1alpha1
    kind: IstioOperator
    metadata:
      name: opt-out-fragment-cve-fix
      namespace: istio-system
    spec:
      meshConfig:
        defaultConfig:
          proxyMetadata:
            HTTP_STRIP_FRAGMENT_FROM_PATH_UNSAFE_IF_DISABLED: "false"
    

Note: Opting out of this behavior makes your cluster vulnerable to this CVE.  | High |  [CVE-2021-39156](https://github.com/istio/istio/security/advisories/GHSA-hqxw-mm44-gc4r)  
  
Description | Severity | Notes  
---|---|---  
Istio contains a remotely exploitable vulnerability where an HTTP request could potentially bypass an Istio authorization policy when using rules based on `hosts` or `notHosts`.  In the vulnerable versions, the Istio authorization policy compares the HTTP `Host` or `:authority` headers in a case-sensitive manner, which is inconsistent with [RFC 4343](https://datatracker.ietf.org/doc/html/rfc4343). For example, the user could have an authorization policy that rejects requests with host `secret.com`, but the attacker can bypass this by sending the request at hostname `Secret.com`. The routing flow routes the traffic to the backend for `secret.com`, which causes a security incident. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if both of the following are true:

  * It uses Cloud Service Mesh patch versions earlier than 1.7.8-asm.10, 1.8.6-asm.8, 1.9.8-asm.1, and 1.10.4-asm.6.
  * It uses authorization policies with `[DENY actions](https://istio.io/latest/docs/reference/config/security/authorization-policy/#AuthorizationPolicy-Action)` based on `[operation.hosts](https://istio.io/latest/docs/reference/config/security/authorization-policy/#Operation)` or `[ALLOW actions](https://istio.io/latest/docs/reference/config/security/authorization-policy/#AuthorizationPolicy-Action)` based on `[operation.notHosts](https://istio.io/latest/docs/reference/config/security/authorization-policy/#Operation)`.

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.10.4-asm.6
  * 1.9.8-asm.1
  * 1.8.6-asm.8
  * 1.7.8-asm.10

This mitigation makes sure that the HTTP `Host` or `:authority` headers are evaluated against the `hosts` or `notHosts` specs in the authorization policies in a case-insensitive manner.  | High |  [CVE-2021-39155](https://github.com/istio/istio/security/advisories/GHSA-7774-7vr3-cc8j)  
  
Description | Severity | Notes  
---|---|---  
Envoy contains a remotely exploitable vulnerability that an HTTP request with multiple value headers could do an incomplete authorization policy check when the `ext_authz` extension is used. When a request header contains multiple values, the external authorization server will only see the last value of the given header. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if both of the following are true:

  * It uses Cloud Service Mesh patch versions earlier than 1.7.8-asm.10, 1.8.6-asm.8, 1.9.8-asm.1, and 1.10.4-asm.6.
  * It uses the [External Authorization](https://istio.io/latest/docs/tasks/security/authorization/authz-custom/) feature.

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.10.4-asm.6
  * 1.9.8-asm.1
  * 1.8.6-asm.8
  * 1.7.8-asm.10

| High |  [CVE-2021-32777](https://github.com/envoyproxy/envoy/security/advisories/GHSA-6g4j-5vrw-2m8h)  
  
Description | Severity | Notes  
---|---|---  
Envoy contains a remotely exploitable vulnerability that affects Envoy's `decompressor`, `json-transcoder`, or `grpc-web` extensions or proprietary extensions that modify and increase the size of request or response bodies. Modifying and increasing the size of the body in an Envoy’s extension beyond the internal buffer size could lead to Envoy accessing deallocated memory and terminating abnormally. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if both of the following are true:

  * It uses Cloud Service Mesh patch versions earlier than 1.7.8-asm.10, 1.8.6-asm.8, 1.9.8-asm.1, and 1.10.4-asm.6.
  * It uses [`EnvoyFilters`](https://istio.io/latest/docs/reference/config/networking/envoy-filter/).

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.10.4-asm.6
  * 1.9.8-asm.1
  * 1.8.6-asm.8
  * 1.7.8-asm.10

| High |  [CVE-2021-32781](https://github.com/envoyproxy/envoy/security/advisories/GHSA-5vhv-gp9v-42qv)  
  
Description | Severity | Notes  
---|---|---  
Envoy contains a remotely exploitable vulnerability where an Envoy client opening and then resetting a large number of HTTP/2 requests could lead to excessive CPU consumption. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if it uses Cloud Service Mesh patch versions earlier than 1.7.8-asm.10, 1.8.6-asm.8, 1.9.8-asm.1, and 1.10.4-asm.6. **Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.10.4-asm.6
  * 1.9.8-asm.1

Note: If you are using Cloud Service Mesh 1.8 or earlier, please upgrade to the latest patch versions of Cloud Service Mesh 1.9 and above to mitigate this vulnerability.  | High |  [CVE-2021-32778](https://github.com/envoyproxy/envoy/security/advisories/GHSA-3xh3-33v5-chcc)  
  
Description | Severity | Notes  
---|---|---  
Envoy contains a remotely exploitable vulnerability where an untrusted upstream service could cause Envoy to terminate abnormally by sending the `GOAWAY` frame followed by the `SETTINGS` frame with the `SETTINGS_MAX_CONCURRENT_STREAMS` parameter set to `0`. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if it uses Cloud Service Mesh 1.10 with a patch version earlier than 1.10.4-asm.6. **Mitigation** Upgrade your cluster to the following patch version: 

  * 1.10.4-asm.6

| High |  [CVE-2021-32780](https://github.com/envoyproxy/envoy/security/advisories/GHSA-j374-mjrw-vvp8)  
  
  
## GCP-2021-012

**Published: 2021-06-24** Description | Severity | Notes  
---|---|---  
The [Istio secure `Gateway`](https://istio.io/latest/docs/tasks/traffic-management/ingress/secure-ingress/) or [workloads using the `DestinationRule`](https://istio.io/latest/docs/reference/config/networking/destination-rule/) can load TLS private keys and certificates from Kubernetes secrets via the `credentialName` configuration. From Istio 1.8 and above, the secrets are read from `istiod` and conveyed to gateways and workloads via XDS.  Normally, a gateway or workload deployment is only able to access TLS certificates and private keys stored in the secret within its namespace. However, a bug in `istiod` allows a client authorized to access the Istio XDS API to retrieve any TLS certificate and private keys cached in `istiod`. This security vulnerability only impacts the 1.8 and 1.9 minor releases of Cloud Service Mesh. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted if ALL of the following conditions are true:

  * It is using a 1.9.x version prior to 1.9.6-asm.1 or a 1.8.x prior to 1.8.6-asm.4.
  * It has defined [`Gateways`](https://istio.io/latest/docs/tasks/traffic-management/ingress/secure-ingress/) or [`DestinationRules`](https://istio.io/latest/docs/reference/config/networking/destination-rule/) with the `credentialName` field specified. 
  * It does not specify the `istiod` flag `PILOT_ENABLE_XDS_CACHE=false`.

**Mitigation** Upgrade your cluster to one of the following patched versions: 

  * 1.9.6-asm.1
  * 1.8.6-asm.4

If an upgrade isn't feasible, you can mitigate this vulnerability by disabling `istiod` caching. You can disable caching by setting the `istiod` environment variable to `PILOT_ENABLE_XDS_CACHE=false`. System and `istiod` performance could be impacted because this disables XDS caching.  | High |  [CVE-2021-34824](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-34824)  
  
  
## GCP-2021-008

**Published: 2021-05-17** Description | Severity | Notes  
---|---|---  
Istio contains a remotely exploitable vulnerability where an external client can access unexpected services in the cluster, bypassing authorization checks, when a gateway is configured with AUTO_PASSTHROUGH routing configuration. 

#### What should I do?

**Check if your clusters are impacted** This vulnerability impacts only usage of the AUTO_PASSTHROUGH Gateway type, which is typically only used in multi-network, multi-cluster deployments.  Detect the TLS mode of all Gateways in the cluster with the following command: 
    
    
    kubectl get gateways.networking.istio.io -A -o \
      "custom-columns=NAMESPACE:.metadata.namespace, \
      NAME:.metadata.name,TLS_MODE:.spec.servers[*].tls.mode"
    

If the output shows any AUTO_PASSTHROUGH Gateways, you could be impacted.  **Mitigation** Update your clusters to the latest Cloud Service Mesh versions: 

  * 1.9.5-asm.2
  * 1.8.6-asm.3
  * 1.7.8-asm.8

* Note: The rollout of the Cloud Service Mesh [Managed Control Plane](https://docs.cloud.google.com/service-mesh/docs/managed-control-plane) (available only in 1.9.x versions) will complete in the next few days.  | High |  [CVE-2021-31921](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-31921)  
  
  
## GCP-2021-007

**Published: 2021-05-17** Description | Severity | Notes  
---|---|---  
Istio contains a remotely exploitable vulnerability where an HTTP request path with multiple slashes or escaped slash characters (%2F or %5C) could potentially bypass an Istio authorization policy when path based authorization rules are used.  In a scenario where an Istio cluster administrator defines an authorization DENY policy to reject the request at path `"/admin"`, a request sent to the URL path `"//admin"` will NOT be rejected by the authorization policy.  According to the [RFC 3986](https://tools.ietf.org/html/rfc3986#section-6), the path `"//admin"` with multiple slashes should technically be treated as a different path from the `"/admin"`. However, some backend services choose to normalize the URL paths by merging multiple slashes to a single slash. This can result in a bypass of the authorization policy (`"//admin"` does not match `"/admin"`), and a user can access the resource at path `"/admin"` in the backend. 

#### What should I do?

**Check if your clusters are impacted** Your cluster is impacted by this vulnerability if you have authorization policies using "ALLOW action + notPaths field" or "DENY action + paths field" patterns. These patterns are vulnerable to unexpected policy bypasses and you should upgrade to fix the security issue ASAP.  The following is an example of vulnerable policy that uses "DENY action + paths field" pattern: 
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: deny-path-admin
    spec:
      action: DENY
      rules:
      - to:
        - operation:
            paths: ["/admin"]
    

The following is another example of vulnerable policy that uses "ALLOW action + notPaths field" pattern: 
    
    
    apiVersion: security.istio.io/v1beta1
    kind: AuthorizationPolicy
    metadata:
      name: allow-path-not-admin
    spec:
      action: ALLOW
      rules:
      - to:
        - operation:
            notPaths: ["/admin"]
    

Your cluster is not impacted by this vulnerability if: 

  * You don't have authorization policies.
  * Your authorization policies don't define `paths` or `notPaths` fields.
  * Your authorization policies use "ALLOW action + paths field" or "DENY action + notPaths field" patterns. These patterns could only cause unexpected rejection instead of policy bypasses.
Upgrading is optional for these cases.  
**Mitigation** Update your clusters to the latest supported Cloud Service Mesh versions*. These versions support configuring the Envoy proxies in the system with more normalization options: 

  * 1.9.5-asm.2
  * 1.8.6-asm.3
  * 1.7.8-asm.8

* Note: The rollout of the Cloud Service Mesh [Managed Control Plane](https://docs.cloud.google.com/service-mesh/docs/managed-control-plane) (available only in 1.9.x versions) will complete in the next few days.  Follow the [Istio security best practices guide](https://istio.io/latest/docs/ops/best-practices/security/#authorization-policies) to configure your authorization policies.  | High |  [CVE-2021-31920](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-31920)  
  
  
## GCP-2021-004

**Published: 2021-05-06** Description | Severity | Notes  
---|---|---  
The Envoy and Istio projects recently [announced](https://istio.io/latest/news/security/istio-security-2021-003/) several new security vulnerabilities (CVE-2021-28682, CVE-2021-28683, and CVE-2021-29258), that could allow an attacker to crash Envoy and potentially render parts of the cluster offline and unreachable.  This impacts delivered services such as Cloud Service Mesh. 

#### What should I do?

To fix these vulnerabilities, upgrade your Cloud Service Mesh bundle to one of the following patched versions:

  * 1.9.3-asm.2
  * 1.8.5-asm.2
  * 1.7.8-asm.1
  * 1.6.14-asm.2

For more information, see the [Cloud Service Mesh release notes](https://docs.cloud.google.com/service-mesh/docs/release-notes#April_20_2021). | High |  [CVE-2021-28682](https://github.com/envoyproxy/envoy/security/advisories/GHSA-r22g-5f3x-xjgg)  
[CVE-2021-28683](https://github.com/envoyproxy/envoy/security/advisories/GHSA-xw4q-6pj2-5gfg)  
[CVE-2021-29258](https://github.com/envoyproxy/envoy/security/advisories/GHSA-rqvq-hxw5-776j)  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
