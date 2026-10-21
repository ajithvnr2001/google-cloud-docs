---
url: https://docs.cloud.google.com/feeds/cloudloadbalancing-release-notes.xml
title: Cloud Load Balancing - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:44:55.462418+00:00
---

# Cloud Load Balancing - Release notes

> Source: https://docs.cloud.google.com/feeds/cloudloadbalancing-release-notes.xml

tag:google.com,2016:cloudloadbalancing-release-notesCloud Load Balancing - Release notesGoogle Cloud Platform2026-10-14T00:00:00-07:00October 14, 2026tag:google.com,2016:cloudloadbalancing-release-notes#October_14_20262026-10-14T00:00:00-07:00Change 

Google-managed public SSL certificates signed by [Public Certificate Authority](https://docs.cloud.google.com/certificate-manager/docs/public-ca) (`pki.goog`) are gradually transitioning from a 90-day validity period to a 45-day validity period to improve security.

To align with modern industry-wide security standards and promote shorter certificate lifespans, Google-managed public certificates signed by Public Certificate Authority now rotate more frequently.

This proactive rotation enhances the overall security posture of load balancers. Transition requires no manual intervention or configuration changes as Google Cloud automatically manages issuance and renewal for both Certificate Manager and Compute Engine SSL certificates.

For more information, see [Renew a Google-managed SSL certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#renewal).

]]> October 12, 2026tag:google.com,2016:cloudloadbalancing-release-notes#October_12_20262026-10-12T00:00:00-07:00Feature 

Regular expression matchers in host and route rules in URL maps are now **generally available** (GA).

You can now use regular expressions (regex) matchers to configure more flexible and precise traffic routing rules within URL maps for Application Load Balancers. This feature allows you to leverage the power of RE2 syntax for matching on:

  * **URL Paths:** Using the `regexMatch` field within `routeRules`.
  * **HTTP Headers:** Using the `regexMatch` field within `headerMatches` in `routeRules`.
  * **HTTP Query Parameters:** Using the `regexMatch` field within `queryParameterMatches` in `routeRules`.



This feature is available in:

  * Global external Application Load Balancers
  * Regional internal Application Load Balancers
  * Cross-region internal Application Load Balancers
  * Regional external Application Load Balancers



For more information, see [URL map concepts: Regular expressions matchers in host and route rules](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#regex-support).

]]> October 05, 2026tag:google.com,2016:cloudloadbalancing-release-notes#October_05_20262026-10-05T00:00:00-07:00Feature 

External IPv6 addresses are now supported for [Standard Tier](https://docs.cloud.google.com/network-tiers/docs/overview#standard_tier). For more information, see [IPv6 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges).

This feature is in **Preview**.

]]> September 30, 2026tag:google.com,2016:cloudloadbalancing-release-notes#September_30_20262026-09-30T00:00:00-07:00Feature 

A new quota system governing the configuration size of Application Load Balancers is now **generally available**. This update increases the individual URL map size limit from 64 KB and 128 KB to 1 MB. For more information, see [URL map size and quota units](https://docs.cloud.google.com/load-balancing/docs/url-map-size-quota).

Key aspects of this feature include:

  * Complexity-based quota: _Quota units_ reflect URL map complexity (number of rules, hostnames, and path matchers).
  * Scoped measurement: Quota is measured and enforced on a per-project, per-region, or per-VPC depending on Application Load Balancer type.
  * Active consumption: Only URL maps currently referenced by forwarding rules contribute to quota usage.
  * New URL map size limit: The new quota has a new URL map size limit increased to 1 MB for global and regional external and internal Application Load Balancers. Classic Application Load Balancers remain restricted to 64 KB.



For more information on increasing your limit, please contact [Google Cloud Support](https://cloud.google.com/support).

]]> September 28, 2026tag:google.com,2016:cloudloadbalancing-release-notes#September_28_20262026-09-28T00:00:00-07:00Feature 

Zonal network endpoint groups (NEGs) with `GCE_VM_IP` and `GCE_VM_IP_PORT` endpoints support IPv6-only endpoints that reference IPv6-only or dual-stack Compute Engine VM network interfaces.

This feature is available in **Preview**.

For more information, see [Zonal network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts).

]]> September 18, 2026tag:google.com,2016:cloudloadbalancing-release-notes#September_18_20262026-09-18T00:00:00-07:00Feature 

Managed workload identity for backend mTLS is **generally available** for the following Application Load Balancers:

  * Global external Application Load Balancers
  * Regional external Application Load Balancers
  * Cross-region internal Application Load Balancers
  * Regional internal Application Load Balancers



The key benefits are as follows:

  * **Streamline certificate management** : Automated certificate and trust management for backend mTLS through seamless integration with Certificate Authority Service and Certificate Manager.

  * **Eliminate operational toil** : Certificates are automatically rotated based on the workload identity pool's configuration, removing the complexity and manual bottleneck of private key provisioning and maintenance.

  * **Improve visibility and governance** : Gain visibility into communication between distributed services and proactively apply governance to workloads across environments.




For more information, see [Backend mTLS with managed workload identity overview](https://docs.cloud.google.com/load-balancing/docs/managed-workload-identities-load-balancers-overview)

]]> August 27, 2026tag:google.com,2016:cloudloadbalancing-release-notes#August_27_20262026-08-27T00:00:00-07:00Feature 

For regional external passthrough Network Load Balancers, reserving specific or automatically allocated bring your own IP (BYOIP) IPv6 addresses before creating a load balancer, and promoting an ephemeral BYOIP IPv6 address in use by a load balancer to a reserved static IP address, is generally available (GA).

For more information, see the following documentation:

  * [Set up a regional external passthrough Network Load Balancer with a backend service](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service#byoip-ipv6).
  * [Set up a regional external passthrough Network Load Balancer for multiple IP protocols](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-networklb-multiple-protocols#byoip-ipv6)
  * [Set up a regional external passthrough Network Load Balancer with zonal NEGs](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-zonal-neg#byoip-ipv6)

]]> August 26, 2026tag:google.com,2016:cloudloadbalancing-release-notes#August_26_20262026-08-26T00:00:00-07:00Feature 

SSL policy cross-project referencing is now available for Application Load Balancers and proxy Network Load Balancers in **Preview**. You can use cross-project referencing to define and maintain a central SSL policy in an administrative project and reference it from target HTTPS proxies or target SSL proxies in different projects.

Cross-project referencing is supported for global and regional SSL policies. You can use cross-project referencing with the following load balancers:

  * Global external Application Load Balancer
  * Regional external Application Load Balancer
  * Cross-region internal Application Load Balancer
  * Regional internal Application Load Balancer
  * Global external proxy Network Load Balancer



For more information, see [Cross-project SSL policy referencing](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#cross-project-referencing).

]]> August 19, 2026tag:google.com,2016:cloudloadbalancing-release-notes#August_19_20262026-08-19T00:00:00-07:00Feature 

Global Front End combines global external Application Load Balancers, Google Cloud Armor, Cloud CDN, and Service Extensions into one solution to help deliver, scale, and secure your internet-facing applications.

For more information, see [Global Front End](https://docs.cloud.google.com/load-balancing/docs/https#global-front-end).

This feature is available in **Preview**.

]]> August 04, 2026tag:google.com,2016:cloudloadbalancing-release-notes#August_04_20262026-08-04T00:00:00-07:00Feature 

Regular expression URL rewrites (`regexRewrite`) for route rules in URL maps are now available for Application Load Balancers. You can use regular expression pattern rewrite actions to rewrite URL paths by substituting or removing URL path components before forwarding requests to your backends.

For more information, see [Regular expression URL rewrites for route rules](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#regex-url-rewrite).

This feature is in **Preview**.

]]> July 31, 2026tag:google.com,2016:cloudloadbalancing-release-notes#July_31_20262026-07-31T00:00:00-07:00Feature 

Cloud Load Balancing introduces a new version of the Network Load Balancer—the global external passthrough Network Load Balancer, which is the global variant of the regional external passthrough Network Load Balancer. The load balancer is available in **Preview**.

This load balancer variant solves use cases for Security Service Edge (SSE), DNS hosting, Adtech (real-time bidding), real-time communications (RTC), live streaming, and online gaming, among others.

Global external passthrough Network Load Balancers are Layer 4 passthrough load balancers that distribute external traffic among backends (instance groups or network endpoint groups) that can reside in multiple Google Cloud regions. By using Google's global anycast IP routing, the global external passthrough Network Load Balancer steers user traffic to the closest region with healthy backends and available capacity, delivering ultra-low latency and dynamic cross-region failover to ensure resilience to regional outages.

The load balancer provides you with two external IP addresses, each served by a disjoint and isolated global load balancing control and data plane server infrastructure (also known as an _availability group_) to provide high availability.

The load balancer supports TCP, UDP, ESP, GRE, ICMP, and ICMPv6 traffic and can handle both IPv4 and IPv6 traffic. You can deploy your backends in any of the following Google Cloud regions:

  * North America: `us-west1`, `us-west4`, `us-east4`, `us-east5`
  * Europe: `europe-west2`, `europe-west3`
  * Asia: `asia-southeast1`, `asia-south1`, `asia-northeast1`
  * South America: `southamerica-east1`
  * Africa: `africa-south1`
  * Australia: `australia-southeast1`



Note that this release doesn't support GKE backends for the global external passthrough Network Load Balancer.

For details on the new load balancer, see [Global external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture).

]]> July 27, 2026tag:google.com,2016:cloudloadbalancing-release-notes#July_27_20262026-07-27T00:00:00-07:00Feature 

Service load balancing policies (`serviceLbPolicy`) are now supported for regional external Application Load Balancers and regional internal Application Load Balancers. This feature enables advanced load balancing optimizations such as custom load balancing algorithms, auto-capacity draining, failover thresholds, and the ability to designate preferred backends for these load balancers.

For more information, see [Advanced load balancing optimizations](https://docs.cloud.google.com/load-balancing/docs/service-lb-policy).

This feature is in **Preview**.

]]> July 20, 2026tag:google.com,2016:cloudloadbalancing-release-notes#July_20_20262026-07-20T00:00:00-07:00Feature 

For regional external passthrough Network Load Balancers, you can reserve specific or automatically allocated bring your own IP (BYOIP) IPv6 addresses before creating a load balancer, so that the IPv6 address persists independently of the load balancer's lifecycle. You can also promote an ephemeral BYOIP IPv6 address that is in use by a load balancer to a reserved static IP address.

For more information, see the following documentation:

  * [Set up a regional external passthrough Network Load Balancer with a backend service](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service#byoip-ipv6).
  * [Set up a regional external passthrough Network Load Balancer for multiple IP protocols](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-networklb-multiple-protocols#byoip-ipv6)
  * [Set up a regional external passthrough Network Load Balancer with zonal NEGs](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-zonal-neg#byoip-ipv6)



This feature is in **Preview**.

]]> June 30, 2026tag:google.com,2016:cloudloadbalancing-release-notes#June_30_20262026-06-30T00:00:00-07:00Feature 

**Regular expressions matchers in host and route rules in URL maps**

You can now use regular expressions to configure more flexible and precise traffic routing rules within URL maps for _Global external Application Load Balancers_.

**Note:** Regular expression support for regional and cross-region Application Load Balancers was added in a [previous release](https://docs.cloud.google.com/load-balancing/docs/release-notes#December_03_2025).

This feature lets you leverage the power of RE2 syntax for matching on:

  * **Route rules** : Within `pathMatchers`, the `matchRules` array now supports a `regexMatch` field to validate the URL path against a specified regex pattern.
  * **Header matches** : Within `matchRules`, the `headerMatches` array now supports a `regexMatch` field for pattern matching against HTTP header values.
  * **Query parameter matches** : Within `matchRules`, the `queryParameterMatches` array now supports a `regexMatch` field for pattern matching against HTTP query parameters values.



For more details on usage and syntax, see [URL map concepts: Regular expressions matchers in host and route rules](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#regex-support).

This feature is in **Preview.**

]]> June 02, 2026tag:google.com,2016:cloudloadbalancing-release-notes#June_02_20262026-06-02T00:00:00-07:00Feature 

TLS post-quantum key exchange support is now available for Application Load Balancers and external proxy Network Load Balancers. Post-quantum key exchange is essential for protecting today's traffic from future quantum computing decryption risks (_harvest now, decrypt later_ attacks). With post-quantum key exchange enabled, the load balancer uses post-quantum key exchange with clients that support TLS 1.3 and `X25519MLKEM768` key exchange.

This feature is rolling out in three phases:

  * Phase 1 (Until October 2026): Post-quantum key exchange is not enabled by default. Customers can elect to opt in and enable it using their SSL policy.

  * Phase 2 (October 2026 through October 2027): The feature is enabled by default. Customers can elect to defer (opt out) if required.

  * Phase 3 (After October 2027): The feature is enabled by default, and options to defer are no longer effective.




We strongly encourage you to enable post-quantum key exchange now, even before it is turned on by default. The opportunity to test this today will help you verify that clients and any intermediate network devices can properly negotiate post-quantum key exchange.

For more information, see [Post-quantum key exchange](https://docs.cloud.google.com/load-balancing/docs/post-quantum-tls#post-quantum-key-exchange).

]]> June 01, 2026tag:google.com,2016:cloudloadbalancing-release-notes#June_01_20262026-06-01T00:00:00-07:00Feature 

A modernized, component-centric interface for Cloud Load Balancing is available in **Preview**. This inaugural release provides an expanded perspective of load balancing infrastructure, offering enhanced transparency into individual component configurations.

[Go to Cloud Console](https://console.cloud.google.com/net-services/loadbalancing/advanced)

The key features of this release include the following:

  * **Comprehensive resource inventory** : A centralized, searchable, and sortable management layer for granular resources—including forwarding rules, target proxies, and TLSRoutes—facilitating detailed monitoring of resource status and interdependencies.

  * **Interactive resource topology** : A contextual visualization tool that maps traffic flow from forwarding rules through proxies to backends, enabling technical teams to efficiently analyze dependencies and accelerate issue resolution.

  * **Integrated audit logging** : Embedded audit logs within the console that offer a unified module for monitoring and tracking historical configuration changes.


]]> May 26, 2026tag:google.com,2016:cloudloadbalancing-release-notes#May_26_20262026-05-26T00:00:00-07:00Feature 

For global external Application Load Balancers, you can configure Cloud CDN cache policies at various levels of a URL map. This provides granular control over caching policies based on criteria like hostname, URL path, HTTP headers, and query parameters. This feature is in **General availability**.

For more information, see [Configure a Cloud CDN cache policy](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt#cdn-cache-policy).

### Feature

Frontend configuration for load balancing incoming IPv6 traffic is now supported for the following load balancers:

  * Regional external Application Load Balancer
  * Regional external proxy Network Load Balancer
  * Regional internal Application Load Balancer
  * Regional internal proxy Network Load Balancer
  * Cross-region internal Application Load Balancer
  * Cross-region internal proxy Network Load Balancer



This feature is in **Preview**.

For more information, see the following documentation:

  * [Forwarding rules overview](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts)
  * [IPv6 for Application Load Balancers and proxy Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/ipv6)
  * [Convert Application Load Balancer to IPv6](https://docs.cloud.google.com/load-balancing/docs/https/convert-applb-dualstack)
  * [Convert Proxy Network Load Balancer to IPv6](https://docs.cloud.google.com/load-balancing/docs/tcp/convert-proxynetlb-dualstack)
  * [Proxy-only subnets for Envoy-based load balancers](https://docs.cloud.google.com/load-balancing/docs/proxy-only-subnets#proxy_only_subnet_create)

]]> May 22, 2026tag:google.com,2016:cloudloadbalancing-release-notes#May_22_20262026-05-22T00:00:00-07:00Feature 

Application Load Balancers now support the configuration of a [traffic duration](https://docs.cloud.google.com/load-balancing/docs/backend-service#applb-csm-traffic-duration) setting when you add backends to backend services. You can configure this setting as `SHORT` or `LONG` based on the response time needed by backends to complete HTTP requests.

Application Load Balancers also support the use of the [_in-flight_ balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#bmtc-inflight) that lets you configure the load balancer's traffic distribution to supported backends when requests take more than a second to complete.

This feature is in **General availability**.

]]> May 21, 2026tag:google.com,2016:cloudloadbalancing-release-notes#May_21_20262026-05-21T00:00:00-07:00Feature 

Zonal affinity, which was previously available in Preview, is generally available (GA).

For more information, see [Zonal affinity for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/zonal-affinity).

]]> May 19, 2026tag:google.com,2016:cloudloadbalancing-release-notes#May_19_20262026-05-19T00:00:00-07:00Feature 

Google tag gateway for advertisers lets website owners host and deploy Google tags through Google Cloud. You can use a global external Application Load Balancer to route measurement traffic on your website through your domain for improved measurement data accuracy. This provides more reliable data for advertising campaign optimization.

For more information, see [Google tag gateway for advertisers](https://docs.cloud.google.com/load-balancing/docs/https#tag-gateway).

]]> May 14, 2026tag:google.com,2016:cloudloadbalancing-release-notes#May_14_20262026-05-14T00:00:00-07:00Feature 

You can use three new variables in custom request and response headers for Application Load Balancers:

  * `asn`: The Autonomous System Number (ASN) associated with the client's IP address.

  * `cloud_trace_id`: The trace ID extracted (or generated) from the HTTP request header.

  * `hostname`: The original hostname specified by the client in the `Host` HTTP request header. This allows preservation of the original host header (equivalent to `X-Forwarded-Host`).




These variables are available for both global external Application Load Balancers and classic Application Load Balancers.

For more information, see [Create custom headers in backend services](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers-global).

]]> April 30, 2026tag:google.com,2016:cloudloadbalancing-release-notes#April_30_20262026-04-30T00:00:00-07:00Feature 

Backend Cloud Storage buckets are available for regional external Application Load Balancers and regional internal Application Load Balancers.

For more information, see:

  * [Set up a regional external Application Load Balancer with Cloud Storage buckets](https://docs.cloud.google.com/load-balancing/docs/https/setup-reg-ext-app-lb-backend-buckets)
  * [Set up a regional internal Application Load Balancer with Cloud Storage buckets](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-regional-internal-buckets)
  * [Set up a regional external Application Load Balancer with Cloud Storage buckets in a Shared VPC environment](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-shared-vpc-backend-buckets)
  * [Set up a regional internal Application Load Balancer with Cloud Storage buckets in a Shared VPC environment](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-regional-internal-shared-vpc-buckets)



This feature is in **General availability**.

]]> April 27, 2026tag:google.com,2016:cloudloadbalancing-release-notes#April_27_20262026-04-27T00:00:00-07:00Feature 

A new quota system governing the configuration size of Application Load Balancer is now available in **Preview**. This update increases the individual URL map size limit from 64 KB and 128 KB to 1 MB. For more information, see [URL map size and quota units](https://docs.cloud.google.com/load-balancing/docs/url-map-size-quota).

Key aspects of this feature include:

  * Complexity-based quota: _Quota units_ reflect URL map complexity (number of rules, hostnames, and path matchers).
  * Scoped measurement: Quota is measured and enforced on a per-project, per-region, or per-VPC depending on Application Load Balancer type.
  * Active consumption: Only URL maps currently referenced by forwarding rules contribute to quota usage.
  * New URL map size limit: Projects enabled for the new quota have a new URL map size limit increased to 1 MB for global and regional external and internal Application Load Balancers. Classic Application Load Balancer remain restricted to 64 KB.



For more information on increasing your limit or to participate in the preview, please contact [Google Cloud Support](https://cloud.google.com/support).

]]> April 22, 2026tag:google.com,2016:cloudloadbalancing-release-notes#April_22_20262026-04-22T00:00:00-07:00Feature 

Policy profiles in authorization policies let you define the type of authorization being performed at the load balancer. This feature is available in **Preview**.

You can choose from the following profile types:

  * Request authorization profile (`REQUEST_AUTHZ`): Evaluates access based on HTTP request headers. Authorization decisions can be made directly or delegated to custom services. This is the default profile.

  * Content authorization profile (`CONTENT_AUTHZ`): Enables deep inspection of application payloads (headers, body, and trailers). This is used for content-based security, such as blocking prompt injection attacks and preventing sensitive data leaks. Authorization decisions are always delegated.




Policy profiles are supported for the following Google Cloud services:

  * Regional external Application Load Balancers
  * Regional internal Application Load Balancers
  * Agent Gateway ([Preview](https://cloud.google.com/products#product-launch-stages))
  * Secure Web Proxy



To learn more about policy profiles, see [Authorization policy overview](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview).

]]> April 10, 2026tag:google.com,2016:cloudloadbalancing-release-notes#April_10_20262026-04-10T00:00:00-07:00Feature 

Published service backends let you configure [supported load balancers](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#published-service-backend-support) or [regional Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/regional-cloud-service-mesh#configuring-published-service-backends) to route traffic to published services through Private Service Connect endpoints.

For more information, see [Published service backends](https://docs.cloud.google.com/load-balancing/docs/backend-service#Published-service-backends).

This feature is in **Preview**.

]]> April 05, 2026tag:google.com,2016:cloudloadbalancing-release-notes#April_05_20262026-04-05T00:00:00-07:00Feature 

Certificate Manager certificates are available in Google Cloud console while provisioning a load balancer.

You can select a certificate map for the following load balancers:

  * [Global external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute#ssl-cert)
  * [Classic Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/ext-https-lb-simple#ssl-cert)
  * [Global external proxy Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-global-ext-proxy-ssl#ssl-cert)
  * [Classic proxy Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/ssl/setting-up-ssl#ssl-cert)



You can select a Certificate Manager certificate for the following load balancers:

  * [Regional external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb#lb-config)
  * [Regional internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#lb-config)
  * [Cross-region internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-internal#lb-config)



This feature is in **General availability**.

]]> March 31, 2026tag:google.com,2016:cloudloadbalancing-release-notes#March_31_20262026-03-31T00:00:00-07:00Feature 

SNI-based routing for proxy Network Load Balancers is now available in **Preview**.

You can now route TLS traffic based on Server Name Indication (SNI) hostnames by using the new `TLSRoute` resource. The load balancer inspects the initial unencrypted `ClientHello` message to extract the SNI hostname and route connections to the appropriate backend service. This feature provides pure TLS passthrough without terminating the connection at the load balancer. Key benefits include:

  * **End-to-end encryption** : Clients can establish secure mTLS or TLS sessions directly with origin servers.
  * **Role-oriented management** : The `TLSRoute` API lets platform administrators to manage frontend infrastructure while service owners manage their own routes and backends independently.
  * **Simplified IP management** : Consolidate multiple services behind a single [Private Service Connect (PSC) endpoint](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints), reducing IPv4 address exhaustion.



This feature is available for regional and cross-region proxy Network Load Balancers.

For more information, see:

  * [Create a regional external proxy Network Load Balancer load balancer with TLS routes](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-ext-reg-tcp-proxy-migs#configure-lb-tls-routes)
  * [Create a regional internal proxy Network Load Balancer load balancer with TLS routes](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs#configure-lb-tls-routes)
  * [Create a cross-region internal proxy Network Load Balancer load balancer with TLS routes](https://docs.cloud.google.com/load-balancing/docs/tcp/setup-cross-reg-proxy-migs#configure-lb-tls-routes)

]]> February 24, 2026tag:google.com,2016:cloudloadbalancing-release-notes#February_24_20262026-02-24T00:00:00-08:00Other 

Backend Cloud Storage buckets are available for regional external Application Load Balancers, regional internal Application Load Balancers, and cross-region internal Application Load Balancers in a Shared VPC environment.

Support for this feature is available in **Preview** for regional external Application Load Balancers and regional internal Application Load Balancers and in **General availability** for cross-region internal Application Load Balancers. For more information, see:

  * [Set up a regional external Application Load Balancer with Cloud Storage buckets in a Shared VPC environment](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-shared-vpc-backend-buckets)
  * [Set up a regional internal Application Load Balancer with Cloud Storage buckets in a Shared VPC environment](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-regional-internal-shared-vpc-buckets)
  * [Set up a cross-region internal Application Load Balancer with Cloud Storage buckets in a Shared VPC environment](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-crilb-shared-vpc-backend-buckets)

]]> February 23, 2026tag:google.com,2016:cloudloadbalancing-release-notes#February_23_20262026-02-23T00:00:00-08:00Feature 

Backend mutual TLS (mTLS) and backend authenticated TLS is now **Generally available** for cross-region internal Application Load Balancers.

This update complements existing support for global and regional Application Load Balancers, allowing you to enforce bidirectional identity verification across your regional deployments.

For details, see the following:

  * [Backend mTLS overview](https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-backend-mtls)
  * [Set up backend authenticated TLS](https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-setup)
  * [Set up backend mTLS](https://docs.cloud.google.com/load-balancing/docs/backend-mtls-setup)

]]> January 28, 2026tag:google.com,2016:cloudloadbalancing-release-notes#January_28_20262026-01-28T00:00:00-08:00Feature 

To enhance security and help meet stringent compliance requirements like FedRAMP, you can now apply a FIPS-compliant SSL policy to your Application Load Balancers and proxy Network Load Balancers. This update also introduces the ability to enforce TLS 1.3 as the minimum protocol version.

**New`FIPS_202205` profile**

The new `FIPS_202205` profile, available as a predefined SSL policy, restricts the load balancer to use only FIPS 140-2/140-3 validated cryptographic modules and ciphers.

When this profile is selected, the load balancer:

  * Enforces strict TLS settings, negotiating connections only using TLS 1.2 or TLS 1.3.
  * Uses a limited set of approved cipher suites for TLS 1.2, such as the cipher suites in `ECDHE-RSA-AES-GCM` and `ECDHE-ECDSA-AES-GCM` families.
  * Excludes non-FIPS ciphers for TLS 1.3, such as `TLS_CHACHA20_POLY1305_SHA256`.



**Minimum TLS 1.3 Enforcement**

You can now specify TLS 1.3 as the minimum version for your SSL policy, which must be paired with the `RESTRICTED` profile. If you mandate TLS 1.3 as the minimum version, any clients attempting to connect via TLS 1.2 or lower will be rejected. Ensure your client ecosystem supports TLS 1.3 before enforcing this minimum TLS version.

For more information, see the following:

  * [SSL policies overview](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts)
  * [Use SSL policies](https://docs.cloud.google.com/load-balancing/docs/use-ssl-policies)



This feature is in **General availability**.

]]>
