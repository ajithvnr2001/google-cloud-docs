---
url: https://docs.cloud.google.com/load-balancing/docs/release-notes/
title: Cloud Load Balancing release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:05.079254+00:00
---

# Cloud Load Balancing release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Resources ](https://docs.cloud.google.com/load-balancing/docs/resources)



Send feedback 

#  Cloud Load Balancing release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for features and updates to Cloud Load Balancing. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/cloudloadbalancing-release-notes.xml) directly. 

## October 14, 2026

Change

Google-managed public SSL certificates signed by [Public Certificate Authority](https://docs.cloud.google.com/certificate-manager/docs/public-ca) (`pki.goog`) are gradually transitioning from a 90-day validity period to a 45-day validity period to improve security.

To align with modern industry-wide security standards and promote shorter certificate lifespans, Google-managed public certificates signed by Public Certificate Authority now rotate more frequently.

This proactive rotation enhances the overall security posture of load balancers. Transition requires no manual intervention or configuration changes as Google Cloud automatically manages issuance and renewal for both Certificate Manager and Compute Engine SSL certificates.

For more information, see [Renew a Google-managed SSL certificate](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs#renewal).

Feature

Service rate limiting policies are now available in **Preview** for regional internal Application Load Balancers and Secure Web Proxies.

Service rate limiting policies let you maintain service availability among trusted clients that might consume an inordinate amount of resources.

For more information, see the [Service rate limiting overview](https://docs.cloud.google.com/load-balancing/docs/srl-policy/service-rate-limiting-overview).

## October 12, 2026

Feature

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

## October 05, 2026

Feature

External IPv6 addresses are now supported for [Standard Tier](https://docs.cloud.google.com/network-tiers/docs/overview#standard_tier). For more information, see [IPv6 subnet ranges](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-ranges).

This feature is in **Preview**.

## September 30, 2026

Feature

A new quota system governing the configuration size of Application Load Balancers is now **generally available**. This update increases the individual URL map size limit from 64 KB and 128 KB to 1 MB. For more information, see [URL map size and quota units](https://docs.cloud.google.com/load-balancing/docs/url-map-size-quota).

Key aspects of this feature include:

  * Complexity-based quota: _Quota units_ reflect URL map complexity (number of rules, hostnames, and path matchers).
  * Scoped measurement: Quota is measured and enforced on a per-project, per-region, or per-VPC depending on Application Load Balancer type.
  * Active consumption: Only URL maps currently referenced by forwarding rules contribute to quota usage.
  * New URL map size limit: The new quota has a new URL map size limit increased to 1 MB for global and regional external and internal Application Load Balancers. Classic Application Load Balancers remain restricted to 64 KB.



For more information on increasing your limit, please contact [Google Cloud Support](https://cloud.google.com/support).

## September 28, 2026

Feature

Zonal network endpoint groups (NEGs) with `GCE_VM_IP` and `GCE_VM_IP_PORT` endpoints support IPv6-only endpoints that reference IPv6-only or dual-stack Compute Engine VM network interfaces.

This feature is available in **Preview**.

For more information, see [Zonal network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts).

## September 18, 2026

Feature

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

## August 27, 2026

Feature

For regional external passthrough Network Load Balancers, reserving specific or automatically allocated bring your own IP (BYOIP) IPv6 addresses before creating a load balancer, and promoting an ephemeral BYOIP IPv6 address in use by a load balancer to a reserved static IP address, is generally available (GA).

For more information, see the following documentation:

  * [Set up a regional external passthrough Network Load Balancer with a backend service](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service#byoip-ipv6).
  * [Set up a regional external passthrough Network Load Balancer for multiple IP protocols](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-networklb-multiple-protocols#byoip-ipv6)
  * [Set up a regional external passthrough Network Load Balancer with zonal NEGs](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-zonal-neg#byoip-ipv6)



## August 26, 2026

Feature

SSL policy cross-project referencing is now available for Application Load Balancers and proxy Network Load Balancers in **Preview**. You can use cross-project referencing to define and maintain a central SSL policy in an administrative project and reference it from target HTTPS proxies or target SSL proxies in different projects.

Cross-project referencing is supported for global and regional SSL policies. You can use cross-project referencing with the following load balancers:

  * Global external Application Load Balancer
  * Regional external Application Load Balancer
  * Cross-region internal Application Load Balancer
  * Regional internal Application Load Balancer
  * Global external proxy Network Load Balancer



For more information, see [Cross-project SSL policy referencing](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts#cross-project-referencing).

## August 19, 2026

Feature

Global Front End combines global external Application Load Balancers, Google Cloud Armor, Cloud CDN, and Service Extensions into one solution to help deliver, scale, and secure your internet-facing applications.

For more information, see [Global Front End](https://docs.cloud.google.com/load-balancing/docs/https#global-front-end).

This feature is available in **Preview**.

## August 04, 2026

Feature

Regular expression URL rewrites (`regexRewrite`) for route rules in URL maps are now available for Application Load Balancers. You can use regular expression pattern rewrite actions to rewrite URL paths by substituting or removing URL path components before forwarding requests to your backends.

For more information, see [Regular expression URL rewrites for route rules](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#regex-url-rewrite).

This feature is in **Preview**.

## July 31, 2026

Feature

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

## July 27, 2026

Feature

Service load balancing policies (`serviceLbPolicy`) are now supported for regional external Application Load Balancers and regional internal Application Load Balancers. This feature enables advanced load balancing optimizations such as custom load balancing algorithms, auto-capacity draining, failover thresholds, and the ability to designate preferred backends for these load balancers.

For more information, see [Advanced load balancing optimizations](https://docs.cloud.google.com/load-balancing/docs/service-lb-policy).

This feature is in **Preview**.

## July 20, 2026

Feature

For regional external passthrough Network Load Balancers, you can reserve specific or automatically allocated bring your own IP (BYOIP) IPv6 addresses before creating a load balancer, so that the IPv6 address persists independently of the load balancer's lifecycle. You can also promote an ephemeral BYOIP IPv6 address that is in use by a load balancer to a reserved static IP address.

For more information, see the following documentation:

  * [Set up a regional external passthrough Network Load Balancer with a backend service](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service#byoip-ipv6).
  * [Set up a regional external passthrough Network Load Balancer for multiple IP protocols](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-networklb-multiple-protocols#byoip-ipv6)
  * [Set up a regional external passthrough Network Load Balancer with zonal NEGs](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-zonal-neg#byoip-ipv6)



This feature is in **Preview**.

## June 30, 2026

Feature

**Regular expressions matchers in host and route rules in URL maps**

You can now use regular expressions to configure more flexible and precise traffic routing rules within URL maps for _Global external Application Load Balancers_.

**Note:** Regular expression support for regional and cross-region Application Load Balancers was added in a [previous release](https://docs.cloud.google.com/load-balancing/docs/release-notes#December_03_2025).

This feature lets you leverage the power of RE2 syntax for matching on:

  * **Route rules** : Within `pathMatchers`, the `matchRules` array now supports a `regexMatch` field to validate the URL path against a specified regex pattern.
  * **Header matches** : Within `matchRules`, the `headerMatches` array now supports a `regexMatch` field for pattern matching against HTTP header values.
  * **Query parameter matches** : Within `matchRules`, the `queryParameterMatches` array now supports a `regexMatch` field for pattern matching against HTTP query parameters values.



For more details on usage and syntax, see [URL map concepts: Regular expressions matchers in host and route rules](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#regex-support).

This feature is in **Preview.**

## June 02, 2026

Feature

TLS post-quantum key exchange support is now available for Application Load Balancers and external proxy Network Load Balancers. Post-quantum key exchange is essential for protecting today's traffic from future quantum computing decryption risks (_harvest now, decrypt later_ attacks). With post-quantum key exchange enabled, the load balancer uses post-quantum key exchange with clients that support TLS 1.3 and `X25519MLKEM768` key exchange.

This feature is rolling out in three phases:

  * Phase 1 (Until October 2026): Post-quantum key exchange is not enabled by default. Customers can elect to opt in and enable it using their SSL policy.

  * Phase 2 (October 2026 through October 2027): The feature is enabled by default. Customers can elect to defer (opt out) if required.

  * Phase 3 (After October 2027): The feature is enabled by default, and options to defer are no longer effective.




We strongly encourage you to enable post-quantum key exchange now, even before it is turned on by default. The opportunity to test this today will help you verify that clients and any intermediate network devices can properly negotiate post-quantum key exchange.

For more information, see [Post-quantum key exchange](https://docs.cloud.google.com/load-balancing/docs/post-quantum-tls#post-quantum-key-exchange).

## June 01, 2026

Feature

A modernized, component-centric interface for Cloud Load Balancing is available in **Preview**. This inaugural release provides an expanded perspective of load balancing infrastructure, offering enhanced transparency into individual component configurations.

[Go to Cloud Console](https://console.cloud.google.com/net-services/loadbalancing/advanced)

The key features of this release include the following:

  * **Comprehensive resource inventory** : A centralized, searchable, and sortable management layer for granular resources—including forwarding rules, target proxies, and TLSRoutes—facilitating detailed monitoring of resource status and interdependencies.

  * **Interactive resource topology** : A contextual visualization tool that maps traffic flow from forwarding rules through proxies to backends, enabling technical teams to efficiently analyze dependencies and accelerate issue resolution.

  * **Integrated audit logging** : Embedded audit logs within the console that offer a unified module for monitoring and tracking historical configuration changes.




## May 26, 2026

Feature

For global external Application Load Balancers, you can configure Cloud CDN cache policies at various levels of a URL map. This provides granular control over caching policies based on criteria like hostname, URL path, HTTP headers, and query parameters. This feature is in **General availability**.

For more information, see [Configure a Cloud CDN cache policy](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt#cdn-cache-policy).

Feature

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



## May 22, 2026

Feature

Application Load Balancers now support the configuration of a [traffic duration](https://docs.cloud.google.com/load-balancing/docs/backend-service#applb-csm-traffic-duration) setting when you add backends to backend services. You can configure this setting as `SHORT` or `LONG` based on the response time needed by backends to complete HTTP requests.

Application Load Balancers also support the use of the [_in-flight_ balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#bmtc-inflight) that lets you configure the load balancer's traffic distribution to supported backends when requests take more than a second to complete.

This feature is in **General availability**.

## May 21, 2026

Feature

Zonal affinity, which was previously available in Preview, is generally available (GA).

For more information, see [Zonal affinity for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/zonal-affinity).

## May 19, 2026

Feature

Google tag gateway for advertisers lets website owners host and deploy Google tags through Google Cloud. You can use a global external Application Load Balancer to route measurement traffic on your website through your domain for improved measurement data accuracy. This provides more reliable data for advertising campaign optimization.

For more information, see [Google tag gateway for advertisers](https://docs.cloud.google.com/load-balancing/docs/https#tag-gateway).

## May 14, 2026

Feature

You can use three new variables in custom request and response headers for Application Load Balancers:

  * `asn`: The Autonomous System Number (ASN) associated with the client's IP address.

  * `cloud_trace_id`: The trace ID extracted (or generated) from the HTTP request header.

  * `hostname`: The original hostname specified by the client in the `Host` HTTP request header. This allows preservation of the original host header (equivalent to `X-Forwarded-Host`).




These variables are available for both global external Application Load Balancers and classic Application Load Balancers.

For more information, see [Create custom headers in backend services](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers-global).

## April 30, 2026

Feature

Backend Cloud Storage buckets are available for regional external Application Load Balancers and regional internal Application Load Balancers.

For more information, see:

  * [Set up a regional external Application Load Balancer with Cloud Storage buckets](https://docs.cloud.google.com/load-balancing/docs/https/setup-reg-ext-app-lb-backend-buckets)
  * [Set up a regional internal Application Load Balancer with Cloud Storage buckets](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-regional-internal-buckets)
  * [Set up a regional external Application Load Balancer with Cloud Storage buckets in a Shared VPC environment](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-shared-vpc-backend-buckets)
  * [Set up a regional internal Application Load Balancer with Cloud Storage buckets in a Shared VPC environment](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-regional-internal-shared-vpc-buckets)



This feature is in **General availability**.

## April 27, 2026

Feature

A new quota system governing the configuration size of Application Load Balancer is now available in **Preview**. This update increases the individual URL map size limit from 64 KB and 128 KB to 1 MB. For more information, see [URL map size and quota units](https://docs.cloud.google.com/load-balancing/docs/url-map-size-quota).

Key aspects of this feature include:

  * Complexity-based quota: _Quota units_ reflect URL map complexity (number of rules, hostnames, and path matchers).
  * Scoped measurement: Quota is measured and enforced on a per-project, per-region, or per-VPC depending on Application Load Balancer type.
  * Active consumption: Only URL maps currently referenced by forwarding rules contribute to quota usage.
  * New URL map size limit: Projects enabled for the new quota have a new URL map size limit increased to 1 MB for global and regional external and internal Application Load Balancers. Classic Application Load Balancer remain restricted to 64 KB.



For more information on increasing your limit or to participate in the preview, please contact [Google Cloud Support](https://cloud.google.com/support).

## April 22, 2026

Feature

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

## April 10, 2026

Feature

Published service backends let you configure [supported load balancers](https://docs.cloud.google.com/vpc/docs/about-accessing-vpc-hosted-services-endpoints#published-service-backend-support) or [regional Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/regional-cloud-service-mesh#configuring-published-service-backends) to route traffic to published services through Private Service Connect endpoints.

For more information, see [Published service backends](https://docs.cloud.google.com/load-balancing/docs/backend-service#Published-service-backends).

This feature is in **Preview**.

## April 05, 2026

Feature

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

## March 31, 2026

Feature

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



## February 24, 2026

Other

Backend Cloud Storage buckets are available for regional external Application Load Balancers, regional internal Application Load Balancers, and cross-region internal Application Load Balancers in a Shared VPC environment.

Support for this feature is available in **Preview** for regional external Application Load Balancers and regional internal Application Load Balancers and in **General availability** for cross-region internal Application Load Balancers. For more information, see:

  * [Set up a regional external Application Load Balancer with Cloud Storage buckets in a Shared VPC environment](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-shared-vpc-backend-buckets)
  * [Set up a regional internal Application Load Balancer with Cloud Storage buckets in a Shared VPC environment](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-regional-internal-shared-vpc-buckets)
  * [Set up a cross-region internal Application Load Balancer with Cloud Storage buckets in a Shared VPC environment](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-crilb-shared-vpc-backend-buckets)



## February 23, 2026

Feature

Backend mutual TLS (mTLS) and backend authenticated TLS is now **Generally available** for cross-region internal Application Load Balancers.

This update complements existing support for global and regional Application Load Balancers, allowing you to enforce bidirectional identity verification across your regional deployments.

For details, see the following:

  * [Backend mTLS overview](https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-backend-mtls)
  * [Set up backend authenticated TLS](https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-setup)
  * [Set up backend mTLS](https://docs.cloud.google.com/load-balancing/docs/backend-mtls-setup)



## January 28, 2026

Feature

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

## January 23, 2026

Feature

Application Load Balancers now support the configuration of a [traffic duration](https://docs.cloud.google.com/load-balancing/docs/backend-service#applb-csm-traffic-duration) setting when you add backends to the backend services. You can configure this setting as `SHORT` or `LONG` based on the response time needed by backends to complete HTTP requests.

Application Load Balancers also support the use of a new [_in-flight_ balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#bmtc-inflight) that lets you configure the load balancer's traffic distribution to supported backends when requests take more than a second to complete.

This feature is available in **Preview**.

## January 19, 2026

Feature

Backend buckets are available for regional external Application Load Balancers and regional internal Application Load Balancers.

This feature enables to serve static content (such as images, video, and CSS) confined to a specific region, helping you meet strict data residency and compliance requirements for regulated workloads. This update ensures backend bucket availability across the entire Application Load Balancers portfolio.

For more information, see the following:

  * [Set up a regional external Application Load Balancer with Cloud Storage buckets](https://docs.cloud.google.com/load-balancing/docs/https/setup-reg-ext-app-lb-backend-buckets)
  * [Set up a regional internal Application Load Balancer with Cloud Storage buckets](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-regional-internal-buckets)



This feature is in **Preview**.

## January 16, 2026

Feature

**Managed workload identity** is available for **backend mutual TLS (mTLS)** in global external Application Load Balancers.

This feature allows to:

  * **Streamline certificate management** : Managed workload identity enables automated certificate and trust management for backend mTLS through seamless integration with Certificate Authority Service and Certificate Manager.

  * **Eliminate operational toil** : Certificates are automatically rotated based on the workload identity pool's configuration, removing the complexity and manual bottleneck of private key provisioning and maintenance.

  * **Improve visibility and governance** : Gain visibility into communication between distributed services and proactively apply governance to workloads across environments.




For more information, see [Backend mTLS with managed workload identity overview](https://docs.cloud.google.com/load-balancing/docs/managed-workload-identities-load-balancers-overview)

This feature is in **Preview**.

## December 17, 2025

Security

Starting _December 17, 2025_ , requests with request methods that aren't compliant with [RFC 9110, Section 5.6.2](https://datatracker.ietf.org/doc/html/rfc9110#section-5.6.2) will be rejected by a first-layer Google Front End (GFE) before reaching your load balancer or its backends. Previously, such non-compliant requests would have been rejected by the load balancer or its backends with a variety of error codes. With the GFE now handling such requests, you might observe a small decrease in error rates.

This change applies only to global external Application Load Balancers and classic Application Load Balancers.

## December 03, 2025

Feature

**Regular expressions matchers in host and route rules in URL maps**

You can now use regular expressions to configure more flexible and precise traffic routing rules within URL maps for Application Load Balancer. This feature lets you leverage the power of RE2 syntax for matching on:

  * **Route rules** : Within `pathMatchers`, the `matchRules` array now supports a `regexMatch` field to validate the URL path against a specified regex pattern.
  * **Header matches** : Within `matchRules`, the `headerMatches` array now supports a `regexMatch` field for pattern matching against HTTP header values.
  * **Query parameter matches** : Within `matchRules`, the `queryParameterMatches` array now supports a `regexMatch` field for pattern matching against HTTP query parameters values.



This feature is available for the following load balancers:

  * Regional internal Application Load Balancer
  * Cross-region internal Application Load Balancer
  * Regional external Application Load Balancer



For more details on usage and syntax, see [URL map concepts: Regular expressions matchers in host and route rules](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#regex-support).

This feature is in **Preview.**

## December 02, 2025

Feature

Backend mutual TLS (mTLS) and backend authenticated TLS are now **Generally available** for the following regional Application Load Balancers:

  * Regional external Application Load Balancers
  * Regional internal Application Load Balancers



This update complements existing support for global external Application Load Balancers, allowing you to enforce bidirectional identity verification across your regional deployments.

For details, see the following:

  * [Backend mTLS overview](https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-backend-mtls)
  * [Set up backend authenticated TLS](https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-setup)
  * [Set up backend mTLS](https://docs.cloud.google.com/load-balancing/docs/backend-mtls-setup)



## November 04, 2025

Feature

`GRPC_WITH_TLS` health checks are used for health checking gRPC backends with TLS enabled. For more information, see the following:

  * [Success criteria for gRPC](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-grpc)
  * [Create health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks#create-hc)



This feature is in **General availability**.

## October 31, 2025

Change

The global and classic external Application Load Balancers implemented on Google Front-Ends (GFEs) now reject TLS connections when the client and the load balancer support ALPN (Application-Layer Protocol Negotiation), but don't share common ALPN protocols.

Previously, if a client proposed a list of application protocols during the TLS handshake using the ALPN extension and none were supported by the load balancer, ALPN would be deactivated and the connection would default to using HTTP/1 as the default application protocol. After this update, the GFE instead returns an `SSL_TLSEXT_ERR_ALERT_FATAL` response which causes the load balancer to terminate the TLS handshake, and the connection to close. This change ensures that an application-layer protocol is always explicitly negotiated between the clients and the load balancers that support ALPN.

## October 29, 2025

Feature

You can specify a custom ephemeral `/96` IPv6 address range when creating a regional IPv6 forwarding rule. For more information, see the following:

  * [Internal passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/internal)
  * [Backend service-based external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service)
  * [Protocol forwarding overview](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding)



This feature is in **General availability**.

## October 28, 2025

Feature

Both internal passthrough Network Load Balancers and external passthrough Network Load Balancers support load balancing to managed instance groups (MIGs) comprised of IPv6-only VM instances.

For more details, see the following pages:

  * [Set up an external passthrough Network Load Balancer with a backend service](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service)
  * [Set up an internal passthrough Network Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal)



This feature is in **General availability**.

Feature

Application Load Balancers support authorization policies that let you establish access control checks for incoming traffic.

For details, see [Authorization policy overview](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview).

This feature is in **General availability**.

## October 06, 2025

Feature

Percentage-based request mirroring is now supported for the global and regional external Application Load Balancers (classic is not supported). By default, the mirrored backend service receives all requests, even if the original traffic is being split between multiple weighted backend services. You can now configure the mirrored backend service to receive only a percentage of the requests by using the `mirrorPercent` flag to specify the percentage of requests to be mirrored, expressed as a value between 0 and 100.0.

For an example, see [Set up traffic management for regional external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-traffic-mgmt#mirror_traffic).

This feature is available in **General availability**.

## September 17, 2025

Security

A security fix was made which changes the behavior of requests and responses sent with the `Transfer-Encoding: Chunked` header to be more RFC 9112 compliant. The [RFC states](https://datatracker.ietf.org/doc/html/rfc9112#name-chunked-transfer-coding) that both the `chunked_body` and the `last-chunk` fields must end in `CRLF`. This is now enforced.

## September 12, 2025

Change

The global and classic external Application Load Balancers implemented on Google Front-Ends (GFEs) now support HTTP/1.0 explicitly as a protocol during ALPN (Application-Layer Protocol Negotiation) negotiation.

Previously, when the GFEs didn't support HTTP/1.0 explicitly, the GFE would return an `SSL_TLSEXT_ERR_NOACK` response, disable ALPN, and fall back to using HTTP/1 (which includes HTTP/1.0 and HTTP/1.1) as the default application protocol. After this change, GFEs will instead return `HTTP/1.0`, which provides clients with positive confirmation that their advertised `HTTP/1.0` was accepted. 

You are not expected to make any changes with this update. If a TLS handshake with HTTP/1.0 is unsuccessful, please contact [support](https://docs.cloud.google.com/load-balancing/docs/getting-support).

## August 26, 2025

Feature

The internal and external passthrough Network Load Balancers now support load balancing to unmanaged instance groups comprised of IPv6-only VM instances. 

Protocol forwarding also supports IPv6-only target instances. 

For more details, see the following pages:

  * [Protocol forwarding overview](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding)
  * [Backend service-based external passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service)
  * [Internal passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/internal)
  * [Set up an internal passthrough Network Load Balancer with IPv6-only subnets and backends](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#configure-ipv6-only)



This feature is available in **General Availability**.

## August 05, 2025

Feature

Cross-region internal Application Load Balancers can now route requests for static content to Cloud Storage buckets.

For more information, see [Set up a cross-region internal Application Load Balancer with Cloud Storage buckets](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-cross-region-internal-https-buckets).

This capability is now in **General Availability**.

## July 30, 2025

Change

**Starting October 15, 2025, the global and classic external Application Load Balancers are improving HTTP header handling for headers with obs-fold values to comply with the[RFC 9112](https://www.rfc-editor.org/rfc/rfc9112.html#section-5.2) standard**

Previously, these load balancers would forward HTTP headers with obs-fold values (those split across multiple lines, with subsequent lines starting with a space or a tab) without any changes. Starting October 15, 2025, each obs-fold will be replaced with one or more space characters (SP octets) before forwarding the message upstream. This ensures that the header is correctly interpreted as a single line, as required by the HTTP specification.

**What you need to do**

Review your current client applications and backend services before October 15, 2025 and ensure that they generate HTTP headers with obs-fold values in a single-line format when communicating with these load balancers. 

Because the obs-fold header fields have been deprecated in RFC 9112, compliant clients and servers should already avoid using this format. However, there is a possibility that services that specifically rely on the old, non-compliant multi-line format of headers with obs-fold values might experience unexpected behavior. You should proactively check your backend service logs for any errors originating from your services due to the modified obs-fold headers.

For more information on the HTTP specification regarding headers with obs-fold values, review [RFC 9112, Section 5.2: Obsolete Line Folding](https://www.rfc-editor.org/rfc/rfc9112.html#section-5.2).

## July 28, 2025

Feature

Global external Application Load Balancers now support the [JA4 fingerprint](https://github.com/FoxIO-LLC/ja4/blob/main/technical_details/JA4.md). The JA4 fingerprint can be added to a [custom request header](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers-global?variables#variables) using the `tls_ja4_fingerprint` variable.

This capability is now in **General Availability**.

## July 09, 2025

Feature

Application Load Balancers and Proxy Network Load Balancers now support TLS certificates with large key sizes. Previously, these load balancers supported only certificates with RSA-2048 or ECDSA P-256 key types. With this update, you can now use self-managed certificates with RSA-3072, RSA-4096, and ECDSA P-384 keys.

**Key details** :

  * Supported key types (for self-managed certificates): RSA-2048, RSA-3072, RSA-4096, ECDSA P-256, and ECDSA P-384

  * Load balancing coverage for self managed certificates:

    * Certificate Manager SSL certificates: Global and regional load balancing

    * Compute Engine SSL Certificates: Regional load balancing

  * Pricing: An additional charge of $0.45 per 1 million connections applies with certificates that use RSA-3072 and RSA-4096 key types. There are no per-connection charges for certificates that use RSA-2048, ECDSA P-256, or ECDSA P-384 key types.




For more information, see the documentation for [Supported key types](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#key-types).

This capability is now in **General Availability**.

## July 08, 2025

Feature

Zonal affinity, configured on the backend service of an internal passthrough Network Load Balancer, lets you limit cross-zone traffic, reduce latency, and improve performance, all while maintaining the benefits of a multi-zonal architecture.

Internal passthrough Network Load Balancers support three zonal affinity options that offer varying degrees of preference for routing new connections to eligible backends that are in the same zone as a supported client. 

For more information, see [Zonal affinity for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/zonal-affinity).

This feature is in **Preview**.

## June 26, 2025

Feature

In typical HTTPS communication, neither the load balancer nor the backend verify each other's identity, assuming that they are within a secure perimeter and can be trusted. However, when perimeter security needs reinforcement or communication extends beyond the perimeter, backend mTLS becomes essential. Backend mTLS ensures secure communication by requiring both the load balancer and the backend to mutually verify their identities.

With _backend authenticated TLS_ , the load balancer verifies the backend server's certificate by checking its chain of trust, thereby confirming the backend's identity. Conversely, with _backend mTLS_ , the backend server verifies the client certificate presented by the load balancer. Together, these mechanisms enable backend mTLS, ensuring that both parties validate each other's identity.

Backend mTLS complements frontend mTLS, which is already generally available (GA).

For details, see the following:

  * [Backend mTLS overview](https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-backend-mtls)
  * [Set up backend authenticated TLS](https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-setup)
  * [Set up backend mTLS](https://docs.cloud.google.com/load-balancing/docs/backend-mtls-setup)



This capability is in **General Availability** for global external Application Load Balancers.

## June 13, 2025

Feature

Cloud Load Balancing supports load balancing to multi-NIC instances that use [Dynamic NICs](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts).

This capability is in **Preview**.

## June 03, 2025

Feature

Cleartext HTTP/2 over TCP, also known as H2C, lets you use HTTP/2 without TLS. H2C is supported by internal and external Application Load Balancers for both of the following connections:

  * Connections between clients and the load balancer. No special configuration is required. Support for this capability is already in **General Availability**.

  * Connections between the load balancer and its backends. Support for this capability is now in **General Availability**.

To configure H2C for connections between the load balancer and its backends, you set the backend service protocol to `H2C`.




Feature

Application Load Balancers now support the use of _custom metrics_ that let you configure your load balancer's traffic distribution behavior to be based on metrics specific to your application or infrastructure requirements, rather than Google Cloud's standard utilization or rate-based metrics. Defining custom metrics for your load balancer gives you the flexibility to route application requests to the backend instances and endpoints that are most optimal for your workload.

For more information, see [Custom metrics for Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/applb-custom-metrics).

This capability is in **General availability**.

## May 19, 2025

Feature

To take advantage of the new features of the global external Application Load Balancer, you can now migrate your classic Application Load Balancer resources to the global external Application Load Balancer infrastructure.

To migrate to the global external Application Load Balancer, you change the load balancing scheme of your load balancing resources—specifically, the backend services and forwarding rules—from `EXTERNAL` to `EXTERNAL_MANAGED`. You can also rollback resources to the classic Application Load Balancer infrastructure, as long as you do so within 90 days of changing the load balancing scheme.

Cloud Console support is also available to help you complete the migration process.

For more details on the migration process, see the following pages:

  * [Migration overview](https://docs.cloud.google.com/load-balancing/docs/https/migrate-to-global)
  * [Migrate resources from classic to global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/migrate-from-classic-global)
  * [Roll back migrated resources to classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/roll-back-migrated-resources)



This capability is available in **General availability**.

## May 16, 2025

Security

A security vulnerability was detected in the classic Application Load Balancer service prior to April 26, 2025.

[CVE-2025-4600](https://www.cve.org/CVERecord?id=CVE-2025-4600) allowed attackers to smuggle requests to classic Application Load Balancers due to incorrect parsing of oversized chunk bodies. This vulnerability was addressed within the classic Application Load Balancer service on April 26, 2025 through improved input validation and parsing logic.

No action is needed. For more information, see the [GCP-2025-027 security bulletin](https://docs.cloud.google.com/load-balancing/docs/security-bulletins#gcp-2025-027).

## May 14, 2025

Feature

Global and cross-region load balancers now support enabling _traffic isolation_ on the service load balancing policy. By default, these load balancers use the `WATERFALL_BY_REGION` algorithm which allows traffic overflow to other regions when backends in the region closest to the user are either full or unhealthy. Enabling traffic isolation lets the load balancer route traffic only to the region closest to the user, even if all the backends in that region are running at their configured capacity limit. You can also choose to prevent traffic overflow entirely by enabling this feature in `STRICT` mode.

For details, see [Traffic isolation](https://docs.cloud.google.com/load-balancing/docs/service-lb-policy#traffic-isolation).

This feature is in **Preview**.

## May 08, 2025

Feature

Global external Application Load Balancers that use HTTPS as the backend service protocol can now negotiate TLS 1.3 for the connection from the load balancer to the backend.

For more details, see [TLS support](https://docs.cloud.google.com/load-balancing/docs/https#tls_support).

This capability is available in **General Availability**.

## April 29, 2025

Feature

All Application and Proxy Network Load Balancers now support deployments where the load balancer frontend and the load balancer backend use different VPC networks. This is supported without the use of a [Shared VPC deployment](https://docs.cloud.google.com/vpc/docs/shared-vpc).

For regional and cross-region load balancers, connectivity between the load balancer's VPC network and the backend VPC network must be configured using either VPC Network Peering, Cloud VPN tunnels, Cloud Interconnect VLAN attachments, or a Network Connectivity Center framework.

For global and classic load balancers, the different VPC networks don't need to be connected using VPC Network Peering because GFEs communicate directly with backends in their respective VPC networks.

For more details, see the following pages:

  * [External Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/https#backends_and_networks)
  * [Internal Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/l7-internal#backends-networks)
  * [External Proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp#backends-networks)
  * [Internal Proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy#backends-networks)



## April 25, 2025

Deprecated

**Starting April 28, 2025, the Global external Application Load Balancer and the Classic Application Load Balancer will no longer allow the use of custom request headers that reference connection-specific hop-by-hop headers.**

**This change applies only to HTTP/1.1 traffic. Connection-specific hop-by-hop headers are already disallowed by the HTTP/2 and HTTP/3 protocols.**

This change is in accordance with [RFC 2616](https://datatracker.ietf.org/doc/html/rfc2616#section-13.5.1) which states that these connection-specific hop-by-hop headers are meaningful only for a single transport-level connection and should not be forwarded by proxies.

The impacted hop-by-hop headers are: `Connection`, `Keep-Alive`, `TE`, `Trailer`, `Transfer-Encoding`, and `Upgrade`.

**Starting April 28, 2025** , connection-specific hop-by-hop headers that were configured by using custom headers will no longer be applied. These headers will only be set by the load balancer during normal connection handling.

**Starting June 30, 2025** , any configuration changes that reference the connection-specific hop-by-hop custom headers will no longer be accepted.

**What you need to do**

If you are an HTTP/1.1 user affected by this change, complete the following steps:

  1. Determine if your application depends on the values of any hop-by-hop headers configured as custom headers. If any dependencies are found, replace them with an allowed custom header and modify your application accordingly.

  2. Review your backend service and URL map `headerAction` configuration to remove any references to connection-specific hop-by-hop headers.




## March 17, 2025

Announcement

Google Cloud periodically renews Google-managed certificates by requesting them from certificate authorities (CAs). Certificate authorities verify domain control by checking DNS settings of the domain and in case of [load balancer authorization](https://docs.cloud.google.com/certificate-manager/docs/how-it-works#domain-auth) attempting to contact the server behind the domain's IP address. The CAs that Google Cloud works with have introduced a verification method called **Multi-Perspective Issuance Corroboration** , that is becoming mandatory for all public CAs and that consists in performing the verification from multiple locations in the world. As a result, if DNS settings do not correctly and consistently resolve from all locations, the validation fails and Google-managed certificates will fail to renew.

To learn more about preventing multi-perspective domain validation failures for misconfigured DNS records, see [Multi-perspective domain validation](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/troubleshooting#multi-perspective-domain-validation).

## March 06, 2025

Feature

Cross-region internal Application Load Balancers can now route requests for static content to Cloud Storage buckets.

For more information, see [Set up a cross-region internal Application Load Balancer with Cloud Storage buckets](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-cross-region-internal-https-buckets).

This capability is in **Preview**.

## March 04, 2025

Feature

Application Load Balancers now support the use of _custom metrics_ that let you configure your load balancer's traffic distribution behavior to be based on metrics specific to your application or infrastructure requirements, rather than Google Cloud's standard utilization or rate-based metrics. Defining custom metrics for your load balancer gives you the flexibility to route application requests to the backend instances and endpoints that are most optimal for your workload.

For more information, see [Custom metrics for Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/applb-custom-metrics).

This capability is in **Preview**.

## February 27, 2025

Feature

In typical HTTPS communication, neither the load balancer nor the backend verify each other's identity, assuming that they are within a secure perimeter and can be trusted. However, when perimeter security needs reinforcement or communication extends beyond the perimeter, backend mTLS becomes essential. Backend mTLS ensures secure communication by requiring both the load balancer and the backend to mutually verify their identities.

With _backend authenticated TLS_ , the load balancer verifies the backend server's certificate by checking its chain of trust, thereby confirming the backend's identity. Conversely, with _backend mTLS_ , the backend server verifies the client certificate presented by the load balancer. Together, these mechanisms enable backend mTLS, ensuring that both parties validate each other's identity.

Backend mTLS complements frontend mTLS, which is already generally available (GA).

For details, see the following:

  * [Backend mTLS overview](https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-backend-mtls)
  * [Set up backend authenticated TLS](https://docs.cloud.google.com/load-balancing/docs/backend-authenticated-tls-setup)
  * [Set up backend mTLS](https://docs.cloud.google.com/load-balancing/docs/backend-mtls-setup)



This capability is in **Preview** for global external Application Load Balancers.

## February 20, 2025

Feature

Cleartext HTTP/2 over TCP, also known as H2C, lets you use HTTP/2 without TLS. H2C is supported by internal and external Application Load Balancers for both of the following connections:

  * Connections between clients and the load balancer. No special configuration is required. Support for this capability is in **General Availability**.

  * Connections between the load balancer and its backends. Support for this capability is in **Preview**. 

To configure H2C for connections between the load balancer and its backends, you set the backend service protocol to `H2C`.




## February 19, 2025

Feature

Internal and external passthrough Network Load Balancers now support connection draining for UDP and other non-TCP protocol traffic. For details, see [Enable connection draining](https://docs.cloud.google.com/load-balancing/docs/enabling-connection-draining).

This feature is now [generally available (GA)](https://cloud.google.com/products?e=48754805&hl=en#product-launch-stages).

## February 18, 2025

Feature

TLS 1.3 early data is now supported on the target HTTPS proxy of global external Application Load Balancers and classic Application Load Balancers.

TLS 1.3 early data, also known as _zero-round-trip time (0-RTT) data_ , can improve application performance for resumed connections by 30 to 50%.

For details, see [TLS 1.3 early data support](https://docs.cloud.google.com/load-balancing/docs/https#tls-early-data-support).

This feature is available in **General Availability**.

## January 24, 2025

Announcement

**Changes to RSA certificate requirements coming April 28, 2025**

We're changing how Application Load Balancers establish TLS connections to backends. This change fixes a problem where the keyUsage extension of RSA certificates is not being validated consistently and might allow a certificate that should have been rejected based on the keyUsage configuration.

**What you need to do**

_Starting April 28, 2025_ , RSA certificates that don't meet the keyUsage configuration requirements will no longer be considered valid for establishing TLS connections. We recommend that you check whether your backends' RSA certificates are invalid, and replace them with valid certificates if needed.

A valid RSA certificate is one that has the X509v3 Key Usage extension and includes both the Digital Signature and Key Encipherment parameters.

To identify an invalid RSA certificate, perform the following steps:

  1. First confirm that the certificate type is RSA by running the following command. 

`openssl x509 -text -in cert.crt | grep "Public Key Algorithm"`. 

For RSA certificates, this should output `rsaEncryption`. If it is a non-RSA certificate (for example, EC), you don't need to take any more action at this time.

  2. If it is an RSA certificate, examine the Key Usage configuration by running the following command:

`openssl x509 -text -in cert.crt | grep -A1 "X509v3 Key Usage"`

For a valid RSA certificate, the correct value is `Digital Signature, Key Encipherment`. If either of these values is not present, the RSA certificate is invalid.




For more information about the X.509 certificate format, see [RFC 5280 Key Usage](https://datatracker.ietf.org/doc/html/rfc5280#section-4.2.1.3).

## November 22, 2024

Feature

Cloud Load Balancing now supports failover for global, classic, and regional external Application Load Balancers. Failover is handled by creating two or more regional external Application Load Balancers in the regions where you want the traffic to failover to. _Only regional external Application Load Balancers can be used as failover backup load balancers._

For details, see [Failover for external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/applb-failover-overview).

This feature is available in **General availability**.

## November 20, 2024

Feature

Regional external Application Load Balancers, cross-region internal Application Load Balancers, regional internal Application Load Balancers, regional internal proxy Network Load Balancers, cross-region internal proxy Network Load Balancers, and regional external proxy Network Load Balancers now support IPv4 and IPv6 (dual-stack) backends.

The following backends have dual-stack support:

  * VM instance groups
  * Zonal NEGs (`GCE_VM_IP_PORT` endpoints)



You can also convert your existing single-stack load balancers from IPv4-only to dual stack (IPv4 and IPv6) deployments. 

For details, see the following pages:

  * [IPv6 overview](https://docs.cloud.google.com/load-balancing/docs/ipv6)
  * [Convert your existing Application Load Balancer to IPv6](https://docs.cloud.google.com/load-balancing/docs/https/convert-applb-dualstack)
  * [Convert your existing proxy Network Load Balancer to IPv6](https://docs.cloud.google.com/load-balancing/docs/tcp/convert-proxynetlb-dualstack)



This feature is available in **General Availability**.

## November 19, 2024

Feature

Percentage-based request mirroring is now supported for the cross-region and regional internal Application Load Balancers. By default, the mirrored backend service receives all requests, even if the original traffic is being split between multiple weighted backend services. You can now configure the mirrored backend service to receive only a percentage of the requests by using the `mirrorPercent` flag to specify the percentage of requests to be mirrored expressed as a value between 0 and 100.0.

For an example, see [Set up traffic management for regional internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-traffic-management#mirror_traffic).

This capability is available in **Preview**.

## November 12, 2024

Feature

Cloud Load Balancing resources now let you use custom constraints to define your own restrictions on Google Cloud services. To learn about which load balancing resources support custom constraints, and some sample use cases, see [Manage Cloud Load Balancing resources using custom constraints](https://docs.cloud.google.com/load-balancing/docs/custom-constraints). 

For more information about custom constraints, see the following:

  * [Custom organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview#custom-organization-policies)
  * [Custom constraint supported services](https://docs.cloud.google.com/resource-manager/docs/organization-policy/custom-constraint-supported-services)



This feature is available in **General Availability**.

## November 04, 2024

Feature

Percentage-based request mirroring is now supported for the global and regional external Application Load Balancers (classic is not supported). By default, the mirrored backend service receives all requests, even if the original traffic is being split between multiple weighted backend services. You can now configure the mirrored backend service to receive only a percentage of the requests by using the `mirrorPercent` flag to specify the percentage of requests to be mirrored expressed as a value between 0 and 100.0.

For an example, see [Set up traffic management for regional external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-traffic-mgmt#mirror_traffic).

This capability is available in **Preview**.

## October 31, 2024

Feature

Support for [IPv6 static routes](https://docs.cloud.google.com/vpc/docs/static-routes#static-route-next-hops) with a next hop internal passthrough Network Load Balancer (`next-hop-ilb`) is available in **Preview**.

## October 30, 2024

Feature

Service Extensions plugins are available for Google Cloud Application Load Balancers, excluding Classic, in **Preview**.

Service Extensions plugins help you insert WebAssembly (Wasm) plugins in a fully managed serverless environment directly into the data path of Application Load Balancers. 

For details, see [Plugins for Cloud Load Balancing](https://docs.cloud.google.com/service-extensions/docs/overview#integration-lb-plugins).

## October 29, 2024

Feature

All the Application Load Balancers, except the classic Application Load Balancer, now support stateful cookie-based session affinity. When you use stateful cookie-based affinity, the load balancer includes an HTTP cookie in the `Set-Cookie` header in response to the initial HTTP request. With stateful session affinity, customers can preserve stickiness to the selected backend.

For details, see [Stateful cookie-based session affinity](https://docs.cloud.google.com/load-balancing/docs/backend-service#stateful-session-affinity).

This capability is in **General Availability**.

## October 28, 2024

Feature

To take advantage of the new features of the global external Application Load Balancer, you can now migrate your classic Application Load Balancer resources to the global external Application Load Balancer infrastructure.

To migrate to the global external Application Load Balancer, you change the load balancing scheme of your load balancing resources—specifically, the backend services and forwarding rules—from `EXTERNAL` to `EXTERNAL_MANAGED`. You can also rollback resources to the classic Application Load Balancer infrastructure, as long as you do so within 90 days of changing the load balancing scheme.

For more details on the migration process, see the following pages:

  * [Migration overview](https://docs.cloud.google.com/load-balancing/docs/https/migrate-to-global)
  * [Migrate resources from classic to global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/migrate-from-classic-global)
  * [Roll back migrated resources to classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/roll-back-migrated-resources)



This capability is available in **Preview**.

## October 24, 2024

Feature

Global external Application Load Balancers and global external proxy Network Load Balancers can now load balance IPv6 traffic. The following backends have dual-stack support:

  * VM instance groups
  * Zonal NEGs (`GCE_VM_IP_PORT` endpoints)



You can also convert your existing single-stack load balancers from IPv4-only to dual stack (IPv4 and IPv6) deployments. 

For details, see the following pages:

  * [IPv6 overview](https://docs.cloud.google.com/load-balancing/docs/ipv6)
  * [Convert your existing Application Load Balancer to IPv6](https://docs.cloud.google.com/load-balancing/docs/https/convert-applb-dualstack)
  * [Convert your existing proxy Network Load Balancer to IPv6](https://docs.cloud.google.com/load-balancing/docs/tcp/convert-proxynetlb-dualstack)



This feature is available in **General Availability**.

## October 21, 2024

Feature

Internal and external passthrough Network Load Balancers now support connection draining for UDP and other non-TCP protocol traffic.

For details, see [Enable connection draining](https://docs.cloud.google.com/load-balancing/docs/enabling-connection-draining).

This feature is available in **Preview**.

## October 18, 2024

Change

Previously, the classic external Application Load Balancer had lenient HTTP/2 request parsing that did not reject requests containing certain invalid characters in the request path. The same requests would have been rejected if they had arrived over HTTP/1 or HTTP/3.

Now, all HTTP requests, including HTTP/2 requests, are rejected if the path contains a character that isn't one of the following:

  * An allowed ASCII character specified in [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986), sections 3.3 and 3.4.

  * One of the following special allowed characters: `[ ] { } | ^`




All other characters must be properly [URL encoded](https://www.w3schools.com/tags/ref_urlencode.ASP).

You can identify rejected requests in the proxy logs by looking for the following:

  * `responseCode`: 400
  * `response_code_details`: `invalid_http2_client_request_path`



Feature

You can now use the Google Cloud Console to create the following load balancers in Premium Tier:

  * Regional external Application Load Balancer
  * Regional external proxy Network Load Balancer



Previously, only Standard Tier support was available in the Console.

## September 30, 2024

Feature

The regional external Application Load Balancers, cross-region internal Application Load Balancers, regional internal Application Load Balancers, now support a configurable _client HTTP keepalive timeout_. The client HTTP keepalive timeout represents the maximum amount of time that a TCP connection can be idle between the (downstream) client and the target HTTP(S) proxy.

For details, see

  * External Application Load Balancers: [Client HTTP keepalive timeout](https://docs.cloud.google.com/load-balancing/docs/https#http-keepalive-timeout)
  * Internal Application Load Balancers: [Client HTTP keepalive timeout](https://docs.cloud.google.com/load-balancing/docs/l7-internal#http-keepalive-timeout)



This capability is available in **General Availability**.

## September 16, 2024

Feature

Envoy-based Application Load Balancers now support authorization policies that let you establish access control checks for incoming traffic. For details, see [Authorization policy](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview).

This feature is available in **Preview**.

## August 28, 2024

Deprecated

**The Global external Application Load Balancer and the Classic Application Load Balancer will no longer support TLS sessionID resumption. They continue to support modern forms of TLS resumption.**

The TLS protocol supports an optimization which allows a client reconnecting to a server with which it has communicated before to perform a cheaper _abbreviated handshake_. This optimization is available in several modes, which include the modern [PSK](https://datatracker.ietf.org/doc/html/rfc8446#section-2.2) and [ticket](https://datatracker.ietf.org/doc/html/rfc5077) mechanisms, as well as the long-obsolete [sessionID](https://datatracker.ietf.org/doc/html/rfc5246) mechanism.

The Global external Application Load Balancer and the Classic Application Load Balancer are the only Google Cloud products that currently support the obsolete sessionID mechanism.

This sessionID mechanism is going to be disabled over the next 4-5 weeks. Clients that currently make use of sessionID will transparently fall back to full TLS handshakes. To recover the performance optimization gains, we recommend that you upgrade clients to modern TLS libraries which support the PSK or ticket mechanisms.

## August 05, 2024

Feature

Regional external Application Load Balancer, regional internal Application Load Balancer, and cross-region internal Application Load Balancer support mutual TLS (mTLS).

With mTLS, the load balancer requests that the client send a certificate to authenticate itself during the TLS handshake with the load balancer. You can configure a trust store to validate the client certificate's chain of trust.

For details, see the following:

  * [Mutual TLS authentication](https://docs.cloud.google.com/load-balancing/docs/mtls)
  * [Set up mutual TLS with user-provided certificates](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ccm)
  * [Set up mutual TLS with a private CA](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ca-ccm)



This capability is in **General Availability**.

The global external Application Load Balancer and the classic Application Load Balancer already support frontend mTLS (General Availability).

## July 31, 2024

Feature

Cloud Load Balancing now supports failover for global, classic, and regional external Application Load Balancers. Failover is handled by creating two or more regional external Application Load Balancers in the regions where you want the traffic to failover to. _Only regional external Application Load Balancers can be used as failover backup load balancers._

For details, see [Failover for external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/applb-failover-overview).

This feature is available in **Preview**.

## July 29, 2024

Feature

All the Application Load Balancers, except the classic Application Load Balancer, now support _stateful cookie-based session affinity_. When you use stateful cookie-based affinity, the load balancer includes an HTTP cookie in the `Set-Cookie` response header of the initial HTTP request. 

For details, see [Stateful cookie-based session affinity](https://docs.cloud.google.com/load-balancing/docs/backend-service#stateful-session-affinity).

This capability is in **Preview**.

## July 19, 2024

Feature

Regional external Application Load Balancers, cross-region internal Application Load Balancers, regional internal Application Load Balancers, regional internal proxy Network Load Balancers, cross-region internal proxy Network Load Balancers, and regional external proxy Network Load Balancers support IPv4 and IPv6 (dual-stack) backends.

Ingress IPv4 traffic can now be proxied over an IPv4 or IPv6 connection to the IPv4 and IPv6 (dual-stack) backends.

The following backends support dual stack:

  * VM instance group
  * Zonal NEGs (GCE_VM_IP_PORT)



You can now convert the load balancers from IPv4 based deployments to dual stack (IPv4 and IPv6) deployments. 

For details, see:

  * [IPv6 overview](https://docs.cloud.google.com/load-balancing/docs/ipv6)

  * [Convert Application Load Balancer to IPv6](https://docs.cloud.google.com/load-balancing/docs/https/convert-applb-dualstack)

  * [Convert proxy Network Load Balancer to IPv6](https://docs.cloud.google.com/load-balancing/docs/tcp/convert-proxynetlb-dualstack)




This feature is available in **Preview**.

## July 15, 2024

Feature

Cloud Load Balancing introduces advanced cost, latency, and resiliency optimizations for your global external Application Load Balancers. These include the following capabilities:

  * You can use a _service load balancing policy_ to customize the parameters that influence how traffic is distributed within the backends associated with a backend service (for example, load balancing algorithm and auto-capacity draining).
  * You can designate specific backends as _preferred backends_.



For details, see [Advanced load balancing optimizations](https://docs.cloud.google.com/load-balancing/docs/service-lb-policy).

This feature is in **General Availability**.

## June 14, 2024

Feature

You can now access backend services residing in different projects than the external or internal Application Load Balancers with cross-project service referencing.

For details, see:

  * [Set up a global external Application Load Balancer with Shared VPC](https://docs.cloud.google.com/load-balancing/docs/https/set-up-global-ext-https-shared-vpc)

  * [Set up regional external Application Load Balancers with Shared VPC](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-shared-vpc)

  * [Set up an internal Application Load Balancer with Shared VPC](https://docs.cloud.google.com/load-balancing/docs/l7-internal/l7-internal-shared-vpc)




This feature is available in **General Availability**.

## June 03, 2024

Feature

Bring your own IP lets you [bring your own public IPv6 addresses](https://docs.cloud.google.com/vpc/docs/bring-your-own-ip#comparison) to Google Cloud. IPv6 BYOIP addresses can be used with [external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service#byoip-ipv6). Bring your own IP for IPv6 addresses is available in **General Availability**.

## May 21, 2024

Feature

Global external Application Load Balancers and global external proxy Network Load Balancers can now load balance IPv6 traffic. The following backends support dual stack:

  * VM instance group
  * Zonal NEGs (GCE_VM_IP_PORT)



You can now convert the load balancer from IPv4 based deployments to dual stack (IPv4 and IPv6) deployments. 

For details, see:

  * [IPv6](https://docs.cloud.google.com/load-balancing/docs/ipv6)

  * [Convert Application Load Balancer to IPv6](https://docs.cloud.google.com/load-balancing/docs/https/convert-applb-dualstack)

  * [Convert proxy Network Load Balancer to IPv6](https://docs.cloud.google.com/load-balancing/docs/tcp/convert-proxynetlb-dualstack)




This feature is available in **Preview**.

## April 16, 2024

Feature

Internal passthrough Network Load Balancer now supports load-balancing for TCP, UDP, ICMP, ICMPv6, SCTP, ESP, AH, and GRE protocols. To handle multiple protocol traffic, you set the load balancer's forwarding rule protocol to `L3_DEFAULT` and set the backend service protocol to `UNSPECIFIED`.

For details, see:

[Set up an internal passthrough Network Load Balancer with VM instance group backends for multiple protocols](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-ilb-multiple-protocols)

This feature is available in **General Availability**.

## April 08, 2024

Feature

Application Load Balancers now support Certificate Manager _allowlisted certificates_. For more information, see [Mutual TLS authentication](https://docs.cloud.google.com/load-balancing/docs/mtls#architecture).

This capability is in **General Availability**.

## April 03, 2024

Feature

The cross-region internal Application Load Balancer supports backends in multiple regions, provides seamless cross-region failover using Cloud DNS routing policies, and is globally accessible by clients from any Google Cloud region, on premise, or other clouds. Supports Google-managed certificates using Cloud Certificate Manager and Certificate Authority Service.

For details, see the [Internal Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/l7-internal).

To set up a cross-region internal Application Load Balancer, see the following pages:

  * [Instance group backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-internal)

  * [Mixed zonal and hybrid connectivity NEG backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-hybrid)

  * [Cloud Run backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-serverless)




This capability is in **General Availability**.

Feature

The cross-region internal proxy Network Load Balancer supports backends in multiple regions, provides seamless cross-region failover, and is globally accessible by clients from any Google Cloud region, on premise, or other clouds. 

For details, see the [Internal proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy).

To set up a cross-region internal proxy Network Load Balancer, see the following pages:

  * [Instance group backends](https://docs.cloud.google.com/load-balancing/docs/tcp/setup-cross-reg-proxy-migs)

  * [Mixed zonal and hybrid connectivity NEG backends](https://docs.cloud.google.com/load-balancing/docs/tcp/setup-cross-reg-proxy-hybrid)




This capability is in **General Availability**.

## April 01, 2024

Feature

You can now configure advanced traffic management using _flexible pattern matching_. This feature allows you to use wildcard syntax anywhere in your path matcher configuration. You can use this feature to customize origin routing for different types of traffic and request and response behaviors. In addition, you can now use results from your pattern matching to rewrite the path that is sent to the origin.

Pattern matching with wildcards is now supported for the following products:

  * Global external Application Load Balancer (launched previously)
  * Regional external Application Load Balancer
  * Cross-region internal Application Load Balancer
  * Regional internal Application Load Balancer
  * Traffic Director



For details, see [URL maps overview: Wildcards and pattern matching operators in path templates for route rules](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#wildcards-regx-dynamic-route).

This capability is available in **General availability**.

## March 27, 2024

Feature

Typically with HTTPS communication, the authentication works only one way: the client verifies the identity of the server. For applications that require the load balancer to authenticate the identity of clients that connect to it, regional external Application Load Balancer, regional internal Application Load Balancer, and cross-region internal Application Load Balancer support mutual TLS (mTLS).

With mTLS, the load balancer requests that the client send a certificate to authenticate itself during the TLS handshake with the load balancer. You can configure a trust store that the load balancer uses to validate the client certificate's chain of trust.

For details, see the following:

  * [Mutual TLS authentication](https://docs.cloud.google.com/load-balancing/docs/mtls)
  * [Set up mutual TLS with user-provided certificates](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ccm)
  * [Set up mutual TLS with a private CA](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ca-ccm)



This capability is in **Preview**.

Global external Application Load Balancer and global external Application Load Balancer (classic) already support frontend mTLS(General Availability).

## March 20, 2024

Feature

The Google Cloud Console has launched a new wizard experience to walk you through the process of selecting a new load balancer. The new wizard walks you through all the available options (internal or internet-facing, proxy or passthrough, global or regional) and guides you to the appropriate load balancer for your use-case.

Try out the new wizard in the Google Cloud Console at [Create a load balancer](https://console.cloud.google.com/net-services/loadbalancing/add).

## March 12, 2024

Feature

The global external Proxy Network Load Balancer is implemented on globally distributed GFEs and supports advanced traffic management capabilities. This load balancer can be configured to handle either TCP or SSL traffic by using either a target TCP proxy or a target SSL proxy respectively. Global external proxy Network Load Balancers support backends such as instance groups, hybrid NEGs, and Private Service Connect NEGs. For details, see the [External proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp).

To set up a global external Proxy Network Load Balancer, see the following pages:

  * [Instance group backends with SSL](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-global-ext-proxy-ssl)
  * [Instance group backends with TCP](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-global-ext-proxy-tcp)



This capability is in **General Availability**.

Feature

Regional external Application Load Balancers and regional internal Application Load Balancers now support Certificate Manager certificates. For more information, see [Certificates and Google Cloud load balancers](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#certificate-summary).

This capability is in **General Availability**.

## February 23, 2024

Feature

Global external Application Load Balancers now let you customize your own error responses when an HTTP error status code (`4xx` and `5xx`) is generated. You can customize error responses for errors generated by both the load balancer and the backend instances. You can also customize error responses for error response codes that are generated when traffic is denied by Cloud Armor.

For more information, see the following pages:

  * [Custom error responses overview](https://docs.cloud.google.com/load-balancing/docs/https/custom-error-response)
  * [Configure custom error responses](https://docs.cloud.google.com/load-balancing/docs/https/configure-custom-error-responses)



This feature is available in **Preview**.

## January 24, 2024

Feature

External passthrough Network Load balancers now support zonal NEGs with `GCE_VM_IP` endpoints. This also lets you add _any network interface_ of a VM as an endpoint for a zonal NEG backend, as long as the network interface belongs to the same subnetwork as the NEG. In comparison, you can only attach the `nic0` of a VM to an instance group backend.

For more details, see the following pages:

  * [External passthrough Network Load Balancer overview: Backends](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#zonal-negs)
  * [Zonal NEGs overview](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts)
  * [Set up an external passthrough Network Load Balancer with a GCE_VM_IP zonal NEG](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-zonal-neg)



## January 09, 2024

Feature

The following regional load balancers can now be configured in either Premium or Standard Network Service Tier:

  * Regional internal Application Load Balancers
  * Regional external Application Load Balancers
  * Regional internal proxy Network Load Balancers
  * Regional external proxy Network Load Balancers



For more information about Network Service Tiers, see the [Network Service Tiers overview](https://docs.cloud.google.com/network-tiers/docs/overview).

This feature is available in **General Availability**.

## November 17, 2023

Feature

Forwarding rules used with Application Load Balancers now let you specify any single port from1-65535.

For more information, see the following:

  * [Summary of load balancer types](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview#summary-of-google-cloud-load-balancers)
  * [External Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/https)
  * [Internal Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/l7-internal)



This feature is available in **General Availability**.

## November 14, 2023

Feature

Regional Application Load Balancers and regional proxy Network Load Balancers now support load balancing traffic to external backends outside Google Cloud. To define an external backend for a load balancer, you use a _regional_ internet network endpoint group (NEG).

For details, see the following:

  * [Internet NEG concepts](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts)
  * [Set up a regional external Application Load Balancer with an external backend](https://docs.cloud.google.com/load-balancing/docs/https/setup-regional-ext-https-external-backend)
  * [Set up a regional internal Application Load Balancer with an external backend](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-regional-int-https-external-backend)
  * [Set up a regional internal proxy Network Load Balancer with an external backend](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-internet)
  * [Set up a regional external proxy Network Load Balancer with an external backend](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-ext-reg-tcp-proxy-internet)



This capability is in **General Availability**.

## October 17, 2023

Feature

Service Extensions callouts are available for Google Cloud Application Load Balancers, excluding Classic.

By using this feature, you can direct your load balancers to make gRPC calls to user-managed or partner-hosted applications from within the Cloud Load Balancing data processing path. These applications can then apply various policies or functions, such as header or payload manipulation, security screening, or custom logging on the traffic before returning the traffic to the load balancer for further processing. 

For details, see the following topics in the Service Extensions documentation: 

  * [Cloud Load Balancing extensions overview](https://docs.cloud.google.com/service-extensions/docs/callouts-overview)
  * [Configure a callout extension](https://docs.cloud.google.com/service-extensions/docs/configure-callout)



Service Extensions is in **Preview**.

## September 29, 2023

Feature

Cloud Load Balancing introduces the global external Proxy Network Load Balancer. The global external Proxy Network Load Balancer is implemented on globally distributed GFEs and supports advanced traffic management capabilities. This load balancer can be configured to handle either TCP or SSL traffic by using either a target TCP proxy or a target SSL proxy respectively. Global external proxy Network Load Balancers support backends such as instance groups, hybrid NEGs, and Private Service Connect NEGs.

Load balancers that are already deployed in the classic mode are renamed as classic Proxy Network Load Balancer in the console.

For details, see the [External proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp).

To set up a global external Proxy Network Load Balancer, see the following pages:

  * [Instance group backends with SSL](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-global-ext-proxy-ssl)
  * [Instance group backends with TCP](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-global-ext-proxy-tcp)



This capability is in **Preview**.

With the launch of global external Proxy Network Load Balancer, we now support three deployment modes with the external Proxy Network Load Balancer—classic (General Availability), Regional (General Availability) and global (Preview). No changes have been made to the API.

For details, see the [External proxy Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/tcp).

Feature

Typically with HTTPS communication, the authentication works only one way: the client verifies the identity of the server. For applications that require the load balancer to authenticate the identity of clients that connect to it, both a global external Application Load Balancer and a global external Application Load Balancer (classic) support mutual TLS (mTLS).

With mTLS, the load balancer requests that the client send a certificate to authenticate itself during the TLS handshake with the load balancer. You can configure a trust store that the load balancer uses to validate the client certificate's chain of trust.

For details, see the following:

  * [Mutual TLS authentication](https://docs.cloud.google.com/load-balancing/docs/mtls)
  * [Set up mutual TLS with signed certificates](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ccm)
  * [Set up mutual TLS with a private CA](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ca-ccm)
  * [Set up mutual TLS for a global external Application Load Balancer (classic)](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ext-https)
  * [Set up mutual TLS for a global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-global-ext-https)



This capability is in **General Availability**.

## September 26, 2023

Feature

Regional external HTTP(S), internal HTTP(S), and the regional internal TCP proxy load balancers now use _distributed Envoy health checks_ instead of Google's centralized health checking mechanism. Envoy health check probes originate from the proxy-only subnet associated with the load balancer. 

For more details, see the Hybrid NEG documentation: [Distributed Envoy health checks](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts#envoy-health-checks).

This feature is available in **General availability**.

## September 06, 2023

Feature

Cloud Load Balancing is introducing new advanced cost, latency, and resiliency optimizations for your global external Application Load Balancer. These include the following capabilities:

  * You can use a _service load balancing policy_ to customize the parameters that influence how traffic is distributed within the backends associated with a backend service (for example, load balancing algorithm and auto-capacity draining).
  * You can designate specific backends as _preferred backends_.



For details, see [Advanced load balancing optimizations](https://docs.cloud.google.com/load-balancing/docs/service-lb-policy).

This feature is in **Preview**.

## August 21, 2023

Feature

Internal passthrough Network Load Balancers can now be configured to handle private IPv6 traffic within your VPC. To enable this, you must configure your dual-stack subnet, backend VMs, health checks, and the forwarding rules to handle IPv6 traffic. 

For details, see:

  * [Internal passthrough Network Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/internal)

  * [Set up load balancer with dual-stack subnets](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#configure-test-environment-ipv6)




This feature is available in **General Availability**.

## August 16, 2023

Change

The following changes have been made to the [Google Cloud console](https://console.cloud.google.com):

  * **Firewall rules** has moved to **Network security** > **Firewall policies**.
  * **SSL policies** has moved to **Network services** > **SSL policies**.



## August 15, 2023

Feature

Regional Application Load Balancers and regional proxy Network Load Balancers now support load balancing traffic to external backends outside Google Cloud. To define an external backend for a load balancer, you use a _regional_ internet network endpoint group (NEG).

For details, see the following:

  * [Internet NEG concepts](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts)
  * [Set up a regional internal Application Load Balancer with an external backend](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setup-regional-int-https-external-backend)
  * [Set up a regional internal proxy Network Load Balancer with an external backend](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-internet)



This capability is in **Preview**.

## August 14, 2023

Feature

Cloud Load Balancing introduces the cross-region internal Application Load Balancer.

The cross-region internal Application Load Balancer supports backends in multiple regions, provides seamless cross-region failover, and is globally accessible by clients from any Google Cloud region, on premise, or other clouds.

For details, see the [Internal Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/l7-internal).

To set up a cross-region internal Application Load Balancer, see the following pages:

  * [Instance group backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-internal)

  * [Mixed zonal and hybrid connectivity NEG backends](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-hybrid)




This capability is in **Preview**.

With the launch of cross-region internal Application Load Balancer, we now support two deployment modes with the internal Application Load Balancer—regional (General Availability) and cross-region (Preview). In the regional mode, you configure the Internal Application Load Balancer in a specific region, and associate it with backends only in the load balancer's region. Load balancers deployed in the regional mode are renamed as _regional internal Application Load Balancer_ in the console. No changes have been made to the API.

For details, see the [Internal Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/l7-internal).

## July 25, 2023

Feature

The global external Application Load Balancer now supports a configurable client HTTP keepalive timeout. The client HTTP keepalive timeout represents the maximum amount of time that a TCP connection can be idle between the (downstream) client and the target HTTP/S proxy.

For details, see 

  * [Client HTTP keepalive timeout](https://docs.cloud.google.com/load-balancing/docs/https#http-keepalive-timeout)
  * [Update client HTTP keepalive timeout](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-external-backend#update-keepalive-timeout)



This capability is available in **General Availability**.

## July 24, 2023

Feature

Internal passthrough Network Load Balancer now supports load-balancing for TCP, UDP, ICMP, ICMPv6, SCTP, ESP, AH, and GRE protocols. To handle multiple protocol traffic, you set the load balancer's forwarding rule protocol to `L3_DEFAULT` and set the backend service protocol to `UNSPECIFIED`.

For details, see:

[Set up an internal passthrough Network Load Balancer with VM instance group backends for multiple protocols](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-ilb-multiple-protocols)

This feature is available in Preview.

## July 06, 2023

Feature

The Cloud Load Balancing Console now allows you to see the equivalent API code for actions you take in the Console. When you create or update a load balancer, before you click **Create** or **Update** , you can click **Equivalent Code** to view the load balancer API resources that will be created, updated, or deleted.

This capability is in **General Availability**.

## June 28, 2023

Feature

Global external Application Load Balancers now support outlier detection for serverless NEG backends. Outlier detection analysis identifies unhealthy serverless NEGs based on their HTTP response patterns, and reduces the error rate by routing some of the new requests from unhealthy services to healthy services. For more details, see the following topics:

  * [Serverless NEG concepts: Outlier detection](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#outlier-detection)
  * [Enable outlier detection](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-serverless#outlier_detection)



## June 21, 2023

Announcement

We're announcing the rebranding of Cloud Load Balancing into two main types of load balancers: **Application Load Balancers** and **Network Load Balancers**.

Over the past few years, we've undertaken several initiatives to bring greater consistency across all flavors of Cloud Load Balancing - for example, by making Envoy proxy the consistent data plane for all new load balancing features. Now, to further help our users understand the different features available with Cloud Load Balancing, and help them quickly identify the best type of load balancer for their use-case, we're adopting a new naming convention.

**What is the new naming convention?**

Cloud Load Balancing now offers two types of load balancers: Application Load Balancers and Network Load Balancers. As a general rule, you'd choose an Application Load Balancer when you need a Layer 7 load balancer for your applications with HTTP(S) traffic. You'd choose a Network Load Balancer when you need a Layer 4 (TCP) load balancer that supports TLS offloading (with a proxy load balancer) or you need support for additional IP protocols such as UDP (with a passthrough load balancer). 

Application and Network Load Balancers can be configured in various deployment modes, for example, internal (private networks) or external (internet facing), global or regional.

For more details, see the following topics:

  * [Cloud Load Balancing overview](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)
  * [Choose a load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer)



The Google Cloud Console has also been updated to reflect these changes. No changes have been made to the API.

## June 07, 2023

Feature

The global external HTTP(S) load balancer now supports a configurable client HTTP Keepalive Timeout. The client HTTP keepalive timeout represents the maximum amount of time that a TCP connection can be idle between the (downstream) client and the target HTTP/S proxy.

For details, see 

  * [Client HTTP keepalive timeout](https://docs.cloud.google.com/load-balancing/docs/https#timeout-keepalive-clients)
  * [Update client HTTP keepalive timeout](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-external-backend#update-keepalive-timeout).



This capability is available in **Preview**.

## May 30, 2023

Feature

The global external HTTP(S) load balancer now supports _advanced traffic management using flexible pattern matching_. This allows you to use wildcards anywhere in your path matcher. You can use this to customize origin routing for different types of traffic and request and response behaviors. In addition, you can now use results from your pattern matching to rewrite the path that is sent to the origin.

For details, see [URL maps overview: Wildcards and pattern matching operators in path templates for route rules](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#wildcards-regx-dynamic-route).

This capability is available in **General availability**.

## May 24, 2023

Feature

Cloud Load Balancing introduces the external regional TCP proxy load balancer. This is an Envoy proxy-based regional layer 4 load balancer that enables you to run and scale your TCP service traffic in a single region behind an external regional IP address. External regional TCP proxy load balancer will load-balance external TCP traffic from the internet to backends in the same region.

For details, see the [External Regional TCP Proxy Load Balancing overview](https://docs.cloud.google.com/load-balancing/docs/tcp)

To set up an external regional TCP proxy load balancer, see the following pages:

  * [Instance group backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-ext-reg-tcp-proxy-migs)

  * [Zonal NEG backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-ext-reg-tcp-proxy-hybrid)

  * [Hybrid connectivity NEG backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-ext-reg-tcp-proxy-zonal)




This capability is in **General Availability**.

## May 10, 2023

Change

If you're using hybrid NEGs with [distributed Envoy health checks](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts#envoy-health-checks), you can't configure the same `NON_GCP_PRIVATE_IP_PORT` network endpoint in multiple hybrid NEGs. This configuration does not work with Envoy-based load balancers such as the regional external HTTP(S) load balancer, the internal HTTP(S) load balancer, and the internal TCP proxy load balancer.

## April 18, 2023

Feature

Typically with HTTPS communication, the authentication works only one way: the client verifies the identity of the server. For applications that require the load balancer to authenticate the identity of clients that connect to it, both a global external HTTP(S) load balancer and a global external HTTP(S) load balancer (classic) support mutual TLS (mTLS).

With mTLS, the load balancer requests that the client send a certificate to authenticate itself during the TLS handshake with the load balancer. You can configure a trust store that the load balancer uses to validate the client certificate's chain of trust.

For details, see the following:

  * [Mutual TLS authentication](https://docs.cloud.google.com/load-balancing/docs/mtls)
  * [Set up mutual TLS with signed certificates](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ccm)
  * [Set up mutual TLS with a private CA](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ca-ccm)
  * [Set up mutual TLS for a global external HTTP(S) load balancer (classic)](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-ext-https)
  * [Set up mutual TLS for a global external HTTP(S) load balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-mtls-global-ext-https)



This capability is in **Preview**.

## April 17, 2023

Feature

Global external HTTP(S) load balancers now support proxying traffic to external backends outside Google Cloud. To define an external backend for a load balancer, you use a global resource called an internet network endpoint group (NEG).

For details, see the following:

  * [Internet NEG concepts](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts)
  * [Set up a global external HTTP(S) load balancer with an external backend](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-external-backend)



This capability is in **Preview**.

## April 14, 2023

Change

We have added new fields in the logging support available for Regional external HTTP(S) load balancer and Internal HTTP(S) Load Balancer:

  * `proxyStatus` a string that specifies why the load balancer returned an error response

  * `tls` specifies the tls metadata for the connection between the client and the load balancer




For details, see

  * [Regional external HTTP(S) load balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-reg-logging-monitoring)
  * [Internal HTTP(S) Load Balancing logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/l7-internal/monitoring)



This enhancement is available in **General availability**.

## April 06, 2023

Feature

Regional external and regional internal HTTP(S) load balancers now support using Cloud Run services as backends for the load balancer. This is configured using a serverless network endpoint group (NEG).

For details, see:

  * [Serverless NEG concepts](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts)
  * [Set up a regional external HTTP(S) load balancer with a Cloud Run backend](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-serverless)
  * [Set up an internal HTTP(S) load balancer with a Cloud Run backend](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal-serverless)



This feature is available in **General availability**.

Feature

Forwarding rules for external TCP/UDP network load balancers can now be configured to direct traffic coming from a specific range of source IP addresses to a specific backend service (or target instance). This is called _traffic steering_.

For details, see:

  * [Network load balancer overview: Traffic steering](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#traffic-steering)
  * [Configure traffic steering](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service#configure-traffic-steering)



This capability is in **General availability**.

## April 03, 2023

Feature

Internal HTTP(S) load balancers and internal TCP proxy load balancers now support _global access_. By default, clients for these load balancers must be in the same region as the load balancer. With global access enabled, clients can access the load balancer from any region. They still must be in the same VPC network as the load balancer or in a VPC network that's connected to the load balancer's VPC network by using VPC Network Peering.

For instructions, see the following:

  * [Enable global access for internal HTTP(S) load balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#global-access)
  * [Enable global access for internal TCP proxy load balancers](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs#global-access)



This capability is in **General availability**.

## March 21, 2023

Feature

Network Load Balancing now supports user-specified weights on the backend service. This allows you to manage the backend load distribution of your load balancer and avoid overloading them.

For details, see:

  * [Weighted load balancing](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#weighted-lb)
  * [Configure weighted load balancing](https://docs.cloud.google.com/load-balancing/docs/network/configure-weighted-netlb)



This feature is in **General Availability**.

## March 07, 2023

Feature

The Cloud Load Balancing Console now allows you to see the equivalent API code for actions you take in the Console. When you create or update a load balancer, before you click **Create** or **Update** , you can click **Equivalent Code** to view the load balancer API resources that will be created, updated, or deleted.

This capability is in **Preview**.

## February 23, 2023

Feature

[Network Load Balancing logging](https://docs.cloud.google.com/load-balancing/docs/network/networklb-monitoring#netlb-logging) and [Internal TCP/UDP Load Balancing logging](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring#ilblb-logging) are now available in **General availability**.

## January 31, 2023

Feature

The global external HTTP(S) load balancer now supports _advanced traffic management using flexible pattern matching_. This allows you to use wildcards anywhere in your path matcher. You can use this to customize origin routing for different types of traffic and request and response behaviors. In addition, you can now use results from your pattern matching to rewrite the path that is sent to the origin.

For details, see [URL maps overview: Wildcards and pattern matching operators in path templates for route rules](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#wildcards-regx-dynamic-route).

This capability is available in **Preview**.

## January 17, 2023

Feature

Internal TCP/UDP load balancers can now be configured to handle private IPv6 traffic within your VPC. To enable this, you must configure your dual-stack subnet, backend VMs, health checks, and the forwarding rules to handle IPv6 traffic. 

For details, see:

  * [Internal TCP/UDP Load Balancing overview](https://docs.cloud.google.com/load-balancing/docs/internal)

  * [Set up load balancer with dual-stack subnets](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#configure-test-environment-ipv6)




This feature is available in **Preview**.

## December 05, 2022

Feature

Currently, health check probes for hybrid NEGs originate from Google's centralized health checking mechanism. If you cannot allow traffic that originates from the Google health check ranges to reach your hybrid endpoints and would prefer to have the health check probes originate from your own private IP addresses instead, speak to your Google account representative to get your project allowlisted for [distributed Envoy health checks](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts#envoy-health-checks).

This feature is available in **Preview** for allowlisted projects only.

## November 17, 2022

Feature

Internal HTTP(S) load balancers and internal TCP proxy load balancers now support _global access_. By default, clients for these load balancers must be in the same region as the load balancer. With global access enabled, clients can access the load balancer from any region. They still must be in the same VPC network as the load balancer or in a VPC network that's connected to the load balancer's VPC network by using VPC Network Peering.

For instructions, see the following:

  * [Enable global access for internal HTTP(S) load balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#global-access)
  * [Enable global access for internal TCP proxy load balancers](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs#global-access)



This capability is in **Preview**.

## November 14, 2022

Change

We're introducing a change in behavior for custom headers used with Global external HTTP(S) load balancers.

This change **_doesn't affect projects that have any traffic using custom headers before November 14, 2022_**. Only projects that aren't currently using any custom headers (with either backend services or URL maps) are affected. If you are using custom headers as of November 14, 2022, you'll still see the behavior in the **Before** column.

The following tables describe changes in behavior applicable only to the global external HTTP(S) load balancers with advanced traffic management. The classic external HTTP(S) load balancers already behave this way when you configure custom headers on backend services. Configuring custom headers on URL maps isn't supported by the classic external HTTP(S) load balancers.

**Custom headers configured on backend services**   


Before | After  
---|---  
Custom request header values are appended to headers on incoming requests. | Custom request header values replace headers on incoming requests.  
If a custom request header value resolves to an empty string, it is ignored. | If a custom request header value resolves to an empty string, it is added to the headers, and replaces the existing header value for this header name.  
  
For example, if this is your backend service configuration:
    
    
    customRequestHeaders: 'x-special-custom-header:'
    customRequestHeaders: 'x-resolvable-custom-header:{client_city}'
    

And this is the incoming client request:
    
    
    curl your-domain.com \
      -H "x-special-custom-header:client-value" \
      -H "x-resolvable-custom-header: NorthPole"
      -H "extra-header: some-content"
    

**_Before the change_** , this would be the request sent to the backend with the custom header appended to the client header:
    
    
    Host: your-domain.com
    x-special-custom-header: client-value
    x-resolvable-custom-header: NorthPole,ActualClientCity
    extra-header: some-content
    

**_After the change_** , this is the request sent to the backend with the custom header replacing the client header:
    
    
    Host: your-domain.com
    x-special-custom-header: 
    x-resolvable-custom-header: ActualClientCity
    extra-header: some-content
    

**Custom headers configured on URL maps**

Before | After  
---|---  
If a `headerValue` in `requestHeadersToAdd` cannot be resolved or resolves to an empty string, the header is ignored. | If a `headerValue` in `requestHeadersToAdd` cannot be resolved or resolves to an empty string, the header is added, either replacing or appending to existing values based on the `replace` field.  
When custom header variables are present, `requestHeaderToAdd` always defaults to `replace: false`. | When custom header variables are present, `requestHeaderToAdd` now defaults to `replace: true`.  
  
For example, if this is your URL map configuration:
    
    
    requestHeadersToAdd:
      - headerName: 'x-special-custom-header'
        headerValue: ''
    

And this is the incoming client request:
    
    
    curl your-domain.com \
      -H "x-special-custom-header:client-value"
    

**_Before the change_** , `requestHeaderToAdd` defaults to `replace: false`, so the custom header does not override the client value. The following is the request sent to the backend:
    
    
    Host: your-domain.com
    x-special-custom-header: client-value
    

**_After the change_** , `requestHeaderToAdd` defaults to `replace: true`, so the custom header value replaces the client value. The following is the request sent to the backend:
    
    
    Host: your-domain.com
    x-special-custom-header:
    

## November 10, 2022

Feature

Regional external and regional internal HTTP(S) load balancers now support regional SSL policies. SSL policies give you the ability to control the features of SSL that your Google Cloud load balancers negotiate with clients. 

For details, see:

  * [SSL policies overview](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts)
  * [Use SSL policies](https://docs.cloud.google.com/load-balancing/docs/use-ssl-policies)



This feature is in **General Availability**.

## October 31, 2022

Feature

Cloud Load Balancing introduces the _internal regional TCP proxy_ load balancer. This is an Envoy proxy-based regional layer 4 load balancer that enables you to run and scale your TCP service traffic behind an internal regional IP address that is accessible only to clients in the same VPC network or clients connected to your VPC network. 

The internal regional TCP proxy load balancer distributes TCP traffic to backends hosted on Google Cloud, on-premises, or other cloud environments.

For details, see the following:

  * [Internal TCP Proxy Load Balancing overview](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy)
  * Set up an internal TCP proxy load balancer: 
    * [Instance group backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs)
    * [Zonal NEG backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-zonal)
    * [Hybrid connectivity NEG backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid)



This capability is in **General Availability**.

## September 20, 2022

Feature

Regional internal and external HTTP(S) load balancers now support Shared VPC configurations where the load balancer's forwarding rule, target proxy, and URL map, can be created in a host or service project, while the backend services and backends can be distributed across multiple service projects in the Shared VPC environment. This is referred to as _cross-project service referencing_. Cross-project backend services can be referenced from a single URL map.

Cross-project service referencing gives service developers and admins autonomy over the exposure of their services through the centrally managed load balancer. 

For details, see:

  * [Shared VPC architectures](https://docs.cloud.google.com/load-balancing/docs/https#shared-vpc)
  * [Setting up a regional external HTTP(S) load balancer with Shared VPC](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-shared-vpc)
  * [Setting up an internal HTTP(S) load balancer with Shared VPC](https://docs.cloud.google.com/load-balancing/docs/l7-internal/l7-internal-shared-vpc)



You can use organization policy constraints to limit how Shared VPC is used across a project, folder, or organization. For details, see [Organization policy constraints for Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/org-policy-constraints).

This feature is available in **General Availability**.

## August 31, 2022

Feature

External TCP and SSL proxy load balancers now allow you to specify a forwarding rule with a global anycast IP address and any port from 1-65535. The target TCP or SSL proxy terminates IPv4 or IPv6 client traffic at the specified port and then proxies the traffic to backend instances.

For more information, see the following:

  * [Summary of load balancer types](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview#summary-of-google-cloud-load-balancers)
  * [SSL Proxy load balancer benefits](https://docs.cloud.google.com/load-balancing/docs/ssl#benefits)
  * [TCP Proxy load balancer benefits](https://docs.cloud.google.com/load-balancing/docs/tcp#benefits)



This feature is available in **General Availability**.

## August 10, 2022

Feature

[Network Load Balancing logging](https://docs.cloud.google.com/load-balancing/docs/network/networklb-monitoring#netlb-logging) and [Internal TCP/UDP Load Balancing logging](https://docs.cloud.google.com/load-balancing/docs/internal/internal-logging-monitoring#ilblb-logging) are now available in **Preview**.

## August 08, 2022

Feature

External TCP/UDP network load balancers can now be configured to handle IPv6 traffic from clients. To enable this, you must configure your subnet, backend VMs, and the forwarding rules to handle IPv6 traffic. 

This feature is only available for backend service-based network load balancers. 

For details, see:

  * [Backend service-based network load balancer overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service)

  * [Set up a backend service-based network load balancer](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service)




This feature is available in **General Availability**.

## July 25, 2022

Feature

Cloud Load Balancing introduces the _internal regional TCP proxy_ load balancer. This is an Envoy proxy-based regional layer 4 load balancer that enables you to run and scale your TCP service traffic behind an internal regional IP address that is accessible only to clients in the same VPC network or clients connected to your VPC network. 

The internal regional TCP proxy load balancer distributes TCP traffic to backends hosted on Google Cloud, on-premises, or other cloud environments.

For details, see the following:

  * [Internal TCP Proxy Load Balancing overview](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy)
  * Set up an internal TCP proxy load balancer: 
    * [Instance group backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-migs)
    * [Zonal NEG backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-zonal)
    * [Hybrid connectivity NEG backends](https://docs.cloud.google.com/load-balancing/docs/tcp/set-up-int-tcp-proxy-hybrid)



This capability is in **Preview**.

## July 21, 2022

Feature

Regional internal HTTP(S) load balancers and regional external HTTP(S) load balancers now support a combination of zonal NEGs (of type `GCE_VM_IP_PORT`) and hybrid NEGs (of type `NON_GCP_PRIVATE_IP_PORT`) in a single backend service. For all supported backend combinations, see the table at [Backend services](https://docs.cloud.google.com/load-balancing/docs/backend-service#supported-backends-scheme).

This feature is available in **General Availability**.

## July 13, 2022

Feature

External HTTP(S) Load Balancing is now available in a _regional_ mode. The new regional external HTTP(S) load balancer contains many of the features of our existing classic external HTTP(S) load balancer, but with an ever-growing list of advanced traffic management capabilities. You can use this load balancer for workloads with jurisdictional compliance requirements or to access the Standard Network Tier.

For details, see:

  * [External HTTPS(S) Load Balancing overview](https://docs.cloud.google.com/load-balancing/docs/https)
  * [Load balancer features (External HTTP(S) > Regional)](https://docs.cloud.google.com/load-balancing/docs/features)
  * [Set up a regional external HTTP(S) load balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb)
  * [Traffic management for regional external HTTP(S) load balancers](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-regional)



This load balancer is available in **General Availability**.

## June 20, 2022

Feature

Cloud Load Balancing introduces a new version of the external HTTP(S) load balancer. The new _global external HTTP(S) load balancer with advanced traffic management capabilities_ contains many of the features of our existing _classic_ HTTP(S) load balancer, but with an ever-growing list of traffic management capabilities such as weighted traffic splitting, request mirroring, outlier detection, fault injection, and so on.

For details on the new load balancer, see:

  * [External HTTPS(S) Load Balancing overview](https://docs.cloud.google.com/load-balancing/docs/https)
  * [Load balancer features (External HTTP(S) > Global )](https://cloud.google.com/load-balancing/docs/features)
  * [Setting up a global external HTTP(S) load balancer](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute)
  * [Traffic management for global external HTTP(S) load balancers](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global)



This load balancer is available in **General Availability**.

## June 06, 2022

Feature

External TCP/UDP Network Load Balancing now supports load-balancing GRE traffic. To handle GRE protocol traffic, you set the load balancer's forwarding rule protocol to `L3_DEFAULT` and set the backend service protocol to `UNSPECIFIED`.

For details, see:

  * [Backend service-based external TCP/UDP Network Load Balancing overview](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service)



This feature is available in **General Availability**.

## June 01, 2022

Feature

Forwarding rules for external TCP/UDP network load balancers can now be configured to direct traffic coming from a specific range of source IP addresses to a specific backend service (or target instance). This is called _traffic steering_.

For details, see:

  * [Network load balancer overview: Traffic steering](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#traffic-steering)
  * [Configure traffic steering](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service#configure-traffic-steering)



This capability is in **Preview**.

## May 26, 2022

Feature

Regional external and regional internal HTTP(S) load balancers now support regional SSL policies. SSL policies give you the ability to control the features of SSL that your Google Cloud load balancers negotiate with clients. 

For details, see:

  * [SSL policies overview](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts)
  * [Using SSL policies](https://docs.cloud.google.com/load-balancing/docs/use-ssl-policies)



This feature is in **Preview**.

## May 09, 2022

Feature

Regional external and regional internal HTTP(S) load balancers now support using Cloud Run services as backends for the load balancer. This is configured using a serverless network endpoint group (NEG).

For details, see:

  * [Serverless NEG concepts](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts)
  * [Setting up a regional external HTTP(S) load balancer with a Cloud Run backend](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-serverless)
  * [Setting up an internal HTTP(S) load balancer with a Cloud Run backend](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal-serverless)



This feature is available in **Preview**.

## May 05, 2022

Feature

Regional external HTTP(S) load balancers now support Shared VPC configurations where the load balancer's forwarding rule, target proxy, and URL map, can be created in a host or service project, while the backend services and backends can be distributed across multiple service projects in the Shared VPC environment. This is referred to as _cross-project service referencing_. Cross-project backend services can be referenced from a single URL map.

Cross-project service referencing gives service developers and admins autonomy over the exposure of their services through the centrally managed load balancer. 

For details, see:

  * [Shared VPC architectures](https://docs.cloud.google.com/load-balancing/docs/https#shared-vpc)
  * [Setting up a regional external HTTP(S) load balancer with Shared VPC](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-shared-vpc)



This feature is available in **Preview**.

## April 19, 2022

Feature

[Backend subsetting for internal HTTP(S) load balancers](https://docs.cloud.google.com/load-balancing/docs/backend-service#subsetting) improves performance and scalability by assigning a subset of backends to each of the proxy instances.

This feature is in **Preview**.

## April 08, 2022

Feature

TCP Proxy and SSL Proxy load balancers now support Google Cloud Armor. For more information, see the [Cloud Armor security policy overview](https://docs.cloud.google.com/armor/docs/security-policy-overview#policy-types).

This feature is available in **Preview**.

## March 14, 2022

Feature

[Backend subsetting for internal TCP/UDP load balancers](https://docs.cloud.google.com/load-balancing/docs/internal#subsetting) lets you scale your internal TCP/UDP load balancer to support a larger number of backend VM instances per internal backend service.

This feature is in **General availability**.

Announcement

Starting October 1, 2022, we'll apply an outbound data processing charge of $0.008 - $0.012 per GB (based on region) to all Cloud Load Balancing products in order to maintain consistency and alignment with the variable costs of the services across our Cloud Load Balancing portfolio. The charge will be called _Outbound data processed by load balancer_ and the price will mirror the existing price for the _Inbound data processed by load balancer_ charge.

If you are on an existing contract, your prices will not change for the lifetime of the contract, or until renewal.

The [current internal HTTP(S) load balancer pricing](https://docs.cloud.google.com/vpc/network-pricing#internal-https-lb) already includes this charge, so no changes are being made there.

To learn more about this change, see the Google Cloud Blog post: [Unlock more choice with updates to Google Cloud's infrastructure capabilities and pricing](https://docs.cloud.google.com/blog/products/infrastructure/updates-to-google-clouds-infrastructure-pricing).

## March 03, 2022

Feature

You can now use a combination of zonal NEGs (of type `GCE_VM_IP_PORT`) and hybrid NEGs (of type `NON_GCP_PRIVATE_IP_PORT`) as backends for your global external HTTP(S) load balancers. For all supported backend combinations, see the table at [Backend services](https://docs.cloud.google.com/load-balancing/docs/backend-service#supported-backends-scheme).

## February 21, 2022

Feature

Network Load Balancing introduces a new monitoring resource type `loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule` that lets you monitor all the supported protocols including TCP, UDP, ESP, and ICMP.

For details, see [Monitoring Network Load Balancing](https://docs.cloud.google.com/load-balancing/docs/network/networklb-monitoring).

This feature is available in **General Availability**.

## February 15, 2022

Feature

Internal TCP/UDP Load Balancing now supports [source-IP address session affinity (`CLIENT_IP_NO_DESTINATION`)](https://docs.cloud.google.com/load-balancing/docs/internal#session_affinity) in **Public Preview**.

## February 08, 2022

Feature

External TCP/UDP Network Load Balancing now allows you to configure a _connection tracking policy_. A connection tracking policy introduces the following new properties to let you customize your load balancer's connection tracking behavior: 

  * [Tracking mode](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#tracking-mode)
  * [Connection persistence on unhealthy backends](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#connection-persistence)



To learn about how connection tracking works, see [Backend selection and connection tracking](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#connection-tracking).

To learn how to configure a connection tracking policy, see [Configure a connection tracking policy](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service#configure-connection-tracking-policy).

This feature is available in **General Availability**.

Feature

Network Load Balancing now supports load-balancing ESP (Encapsulating Security Payload) and ICMP (Internet Control Message Protocol) traffic. To handle these protocols, you specify the new `L3_DEFAULT` protocol on the load balancer's forwarding rule. 

For details, see:

  * [Forwarding rule protocols for backend service-based network load balancers](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#forwarding-rule-protocols)
  * [Setting up Network Load Balancing for multiple protocols](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-networklb-multiple-protocols)



This feature is available in **General Availability**.

Feature

Network Load Balancing introduces a new monitoring resource type `loadbalancing.googleapis.com/ExternalNetworkLoadBalancerRule` that lets you monitor all the supported protocols including TCP, UDP, ESP, and ICMP.

For details, see [Monitoring Network Load Balancing](https://docs.cloud.google.com/load-balancing/docs/network/networklb-monitoring).

This feature is available in **Preview**.

## January 26, 2022

Feature

Internal HTTP(S) Load Balancing now supports Shared VPC configurations where the load balancer's frontend and URL map can be created in a host or service project, while the backend services and backends can be distributed across multiple service projects in the Shared VPC environment. This is referred to as _cross-project service referencing_. Cross-project backend services can be referenced in a single URL map.

Cross-project service referencing gives service developers and admins autonomy over the exposure of their services through the centrally managed load balancer. 

For details, see:

  * [Shared VPC architectures](https://docs.cloud.google.com/load-balancing/docs/l7-internal#shared_vpc)
  * [Setting up Internal HTTP(S) Load Balancing with Shared VPC](https://docs.cloud.google.com/load-balancing/docs/l7-internal/l7-internal-shared-vpc)



This feature is available in **Preview**.

## January 19, 2022

Change

The default behavior for HTTP/3 and Google QUIC is changing for global external HTTP(S) load balancers. The default setting of `quicOverride=NONE` will now advertise support for HTTP/3 to your clients. This change is currently rolling out globally. 

If you don't want this behavior to change, you can disable HTTP/3 by setting `quicOverride` to `DISABLE`. For instructions, see [Configuring HTTP/3](https://docs.cloud.google.com/load-balancing/docs/https#configuring-http3).

## December 20, 2021

Feature

Internal TCP/UDP Load Balancing now allows you to configure a connection tracking policy for the load balancer's backend service. A connection tracking policy introduces the following new properties to let you customize your load balancer's connection tracking behavior:

  * Tracking mode
  * Connection persistence on unhealthy backends
  * Idle timeout



To learn about how connection tracking works, see [Traffic distribution](https://docs.cloud.google.com/load-balancing/docs/internal#traffic_distribution).

This feature is available in **General Availability**.

## November 22, 2021

Feature

When you make an internal TCP/UDP load balancer the next hop of a static route, the route can have instance tags (also called _network tags_).

In addition, there are two different ways to specify the next hop:

  * Forwarding rule's name and the load balancer's region
  * Internal IP address of the forwarding rule.



This feature is now available in **General availability**.

For more information, see the following pages:

  * [Internal TCP/UDP load balancers as next hops](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview)
  * [Creating the static routes that define the load balancers as the next hops](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-ilb-next-hop#ilb_next_hop)



Note that this feature isn't supported in the Console. To configure the route with network tags, use `gcloud` or the API.

## November 15, 2021

Feature

Cloud Load Balancing introduces a new version of the external HTTP(S) load balancer. The new _global external HTTP(S) load balancer with advanced traffic management capabilities_ contains many of the features of our existing _classic_ HTTP(S) load balancer, but with an ever-growing list of traffic management capabilities such as weighted traffic splitting, request mirroring, outlier detection, fault injection, and so on.

For details on the new load balancer, see:

  * [External HTTPS(S) Load Balancing overview](https://docs.cloud.google.com/load-balancing/docs/https)
  * [Load balancer features (External HTTP(S) > Global)](https://docs.cloud.google.com/load-balancing/docs/features)
  * [Setting up a global external HTTP(S) load balancer](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute)
  * [Traffic management for global external HTTP(S) load balancers](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global)



This load balancer is available in **Public Preview**.

## November 01, 2021

Feature

Cloud Load Balancing announces a significant increase in the URL map limits for External and Internal HTTP(S) Load Balancing. The new limits let you scale to a much higher number of services behind a single load balancer. 

For example, URL maps for external HTTP(S) load balancers can now support up to 1000 host rules. The total size of the URL map is constrained to 64KB for External HTTP(S) Load Balancing and 128KB for Internal HTTP(S) Load Balancing

For the updated list of limits see, [URL map limits](https://docs.cloud.google.com/load-balancing/docs/quotas#url_maps)

## October 18, 2021

Change

Cloud Load Balancing now supports load-balancing traffic to endpoints that extend beyond Google Cloud, such as on-premises data centers and other public clouds that you can reach using [hybrid connectivity](https://docs.cloud.google.com/hybrid-connectivity).

Hybrid load balancing is supported by the following load balancers:

  * External HTTP(S) Load Balancing
  * Internal HTTP(S) Load Balancing
  * TCP Proxy and SSL Proxy Load Balancing



For details, see [Hybrid load balancing overview](https://docs.cloud.google.com/load-balancing/docs/hybrid).

This feature is available in **General Availability**.

## September 29, 2021

Feature

External HTTP(S) Load Balancing is now available in a _regional_ mode. The new regional external HTTP(S) load balancer contains many of the features of our existing global load balancer, but with an ever-growing list of advanced traffic management capabilities. You can use this load balancer for workloads with jurisdictional compliance requirements or to access the Standard Network Tier.

For details, see:

  * [External HTTPS(S) Load Balancing overview](https://docs.cloud.google.com/load-balancing/docs/https)
  * [Load balancer features (External HTTP(S): Global | Regional)](https://docs.cloud.google.com/load-balancing/docs/features)
  * [Setting up a regional external HTTP(S) load balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb)
  * [Traffic management for regional external HTTP(S) load balancers](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-regional)



This load balancer is available in **Public Preview**.

## September 23, 2021

Feature

Internal TCP/UDP Load Balancing now allows you to configure a connection tracking policy for the load balancer's backend service. A connection tracking policy introduces the following new properties to let you customize your load balancer's connection tracking behavior:

  * Tracking mode
  * Connection persistence on unhealthy backends
  * Idle timeout



To learn about how connection tracking works, see [Traffic distribution](https://docs.cloud.google.com/load-balancing/docs/internal#traffic_distribution).

This feature is available in **Preview**.

## September 07, 2021

Feature

Cloud Load Balancing now supports load-balancing traffic to endpoints that extend beyond Google Cloud, such as on-premises data centers and other public clouds that you can reach using [hybrid connectivity](https://docs.cloud.google.com/hybrid-connectivity).

Hybrid load balancing is supported by the following load balancers:

  * External HTTP(S) Load Balancing
  * Internal HTTP(S) Load Balancing
  * TCP Proxy and SSL Proxy Load Balancing



For details, see [Hybrid load balancing overview](https://docs.cloud.google.com/load-balancing/docs/hybrid).

This feature is available in **Preview**.

## August 23, 2021

Change

Added Terraform examples to automate load balancer configuration:

  * [External HTTP(S) Load Balancing](https://docs.cloud.google.com/load-balancing/docs/https/ext-http-lb-tf-module-examples)
  * [Internal HTTP(S) Load Balancing](https://docs.cloud.google.com/load-balancing/docs/l7-internal/int-https-lb-tf-examples)
  * [Internal TCP/UDP Load Balancing](https://docs.cloud.google.com/load-balancing/docs/internal/int-tcp-udp-lb-tf-module-examples)



## July 29, 2021

Feature

Cloud Monitoring now provides a new predefined dashboard called **External HTTP(S) Load Balancers**. The new dashboard provides powerful visualizations to help you understand and troubleshoot connectivity issues on your external HTTP(S) load balancers.

For details, see [HTTP(S) Load Balancing logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#predefined-dashboards).

## July 27, 2021

Feature

When you make an internal TCP/UDP load balancer the next hop of a static route, the route can now have instance tags (also called _network tags_).

In addition, you now have two different ways to specify the next hop: 

  * Forwarding rule's name and the load balancer's region
  * Internal IP address of the forwarding rule 



For more information, see the following pages:

  * [Internal TCP/UDP load balancers as next hops](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview)
  * [Creating the static routes that define the load balancers as the next hops](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-ilb-next-hop#ilb_next_hop)



## July 07, 2021

Feature

External TCP/UDP Network Load Balancing now allows you to configure a _connection tracking policy_. A connection tracking policy introduces the following new properties to let you customize your load balancer's connection tracking behavior: 

  * [Tracking mode](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#tracking-mode)
  * [Connection persistence on unhealthy backends](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#connection-persistence)



To learn about how connection tracking works, see [Backend selection and connection tracking](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#connection-tracking).

To learn how to configure a connection tracking policy, see [Configure a connection tracking policy](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service#configure-connection-tracking-policy).

This feature is available in **Preview**.

## June 22, 2021

Feature

External HTTP(S) Load Balancing and Cloud CDN now support HTTP/3. HTTP/3 is based on the IETF QUIC transport protocol. Compared to HTTP/2, it reduces request latency, improves throughput, and mitigates head-of-line blocking. HTTP/3 is already supported on most major web browsers.

To learn how to enable HTTP/3 on your external HTTP(S) load balancer, [visit the documentation](https://docs.cloud.google.com/load-balancing/docs/https#QUIC).

Feature

[Symmetric hashing for internal TCP/UDP load balancers as next hops](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview#symmetric-hashing)—When load balancing to multiple NICs on the backends, you no longer need to use source network address translation (SNAT). SNAT isn't required because Google Cloud uses symmetric hashing. This means that when packets belong to the same flow, Google Cloud calculates the same hash. In other words, the hash doesn't change when the source IP address:port is swapped with the destination IP address:port.

This feature is in **General Availability**.

## June 09, 2021

Feature

Network Load Balancing now supports load-balancing ESP (Encapsulating Security Payload) and ICMP (Internet Control Message Protocol) traffic. To handle these protocols, you specify the new `L3_DEFAULT` protocol on the load balancer's forwarding rule.

For details, see:

  * [Forwarding rule protocols for backend service-based network load balancers](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#forwarding-rule-protocols)
  * [Setting up Network Load Balancing for multiple protocols](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-networklb-multiple-protocols)



This feature is available in **Preview**.

## May 26, 2021

Announcement

Starting May 15, 2021, a newly-created custom static route using a next hop forwarding rule of an internal TCP/UDP load balancer will forward all protocol traffic, not just TCP and UDP traffic.

If a route created before May 15, 2021 is still in operation on August 14, 2021, it will automatically be migrated to forward all protocol traffic starting August 15, 2021. If you don't want to wait until then, you can enable forwarding of traffic for all protocols by creating new routes and deleting the old ones.

For more information, see [Processing of TCP, UDP, and other protocol traffic](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview#all-traffic).

## May 04, 2021

Feature

Zonal NEGs (with `GCE_VM_IP` network endpoints) can now be used as backends for internal TCP/UDP load balancers. For more information on this type of zonal NEG, see [Zonal NEGs overview](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts). For instructions on how to set up an internal TCP/UDP load balancer with a zonal NEG backend, see [Setting up Internal TCP/UDP Load Balancing with zonal NEGs](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal-zonal-neg)

This feature is in **General Availability**.

## April 28, 2021

Feature

Internal TCP/UDP Load Balancing now supports [session affinity for the UDP protocol](https://docs.cloud.google.com/load-balancing/docs/internal#session_affinity). This feature is available in **General Availability**.

## March 31, 2021

Feature

External TCP/UDP Network Load Balancing is now supported with backend services. Compared to the target pool backend, a backend service gives you more fine-grained control over your load balancer, including access to features such as connection draining, failover policies, and support for managed instance groups as backends.

Network load balancers with a backend service can also use health checks that match the traffic (TCP, SSL, HTTP, HTTPS, or HTTP/2) they are distributing.

To get started, see:

  * [Network Load Balancing with backend services](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service)
  * [Setting up a network load balancer with a backend service](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service)
  * [Transitioning a network load balancer from a target pool to a backend service](https://docs.cloud.google.com/load-balancing/docs/network/transition-to-backend-services)



This feature is available in **General Availability**.

## March 28, 2021

Security

Cloud CDN, external HTTP(S) Load Balancing and Cloud Storage customers are not affected by the [recent OpenSSL security advisory](https://www.openssl.org/news/secadv/20210325.txt) that relates to CA certificate checks (CVE-2021-3450) and TLS renegotiation (CVE-2021-3449).

These services use [BoringSSL](https://boringssl.googlesource.com/boringssl/) and are not affected by these OpenSSL-specific bugs.

## March 24, 2021

Feature

[Subsetting for internal TCP/UDP load balancers](https://docs.cloud.google.com/load-balancing/docs/internal#subsetting) lets you scale your internal TCP/UDP load balancer to support a larger number of backend VM instances per internal backend service.

This feature is in **Preview**.

## March 08, 2021

Feature

You can now use the [`gcloud compute url-maps validate`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/validate) command to test advanced route configurations such as routing based on headers and query parameters, HTTP to HTTPS redirects, and URL rewrites.

You can also use this command to independently run tests without saving changes to the URL map. This protects live traffic to your production services and prevents any unintended interruptions due to URL map misconfigurations. 

This feature is now available in **General Availability**.

## February 16, 2021

Feature

Zonal NEGs (with GCE_VM_IP network endpoints) can now be used as backends for internal TCP/UDP load balancers. For more information on this type of zonal NEG, see [Zonal NEGs overview](https://docs.cloud.google.com/load-balancing/docs/negs/zonal-neg-concepts). 

This feature is in **Preview**.

## February 03, 2021

Feature

[Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs) is supported with [Internal HTTP(S) Load Balancing](https://docs.cloud.google.com/load-balancing/docs/l7-internal). This support is available in **General Availability**.

## February 02, 2021

Feature

For internal TCP/UDP load balancers, you can create [multiple forwarding rules with the same IP address](https://docs.cloud.google.com/load-balancing/docs/internal/multiple-forwarding-rules-same-ip). The forwarding rules can have different protocols and ports. This feature is available in **General Availability**.

## December 09, 2020

Feature

[Health check logging](https://docs.cloud.google.com/load-balancing/docs/health-check-logging) is now available in **General Availability**.

## November 10, 2020

Feature

External TCP/UDP Network Load Balancing is now supported with backend services. Compared to the target pool backend, a backend service gives you more fine-grained control over your load balancer, including access to features such as connection draining, failover policies, and support for managed instance groups as backends. 

Network load balancers with a backend service can also use health checks that match the traffic (TCP, SSL, HTTP, HTTPS, or HTTP/2) they are distributing.

To get started, see:

  * [Network Load Balancing with backend services](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service)
  * [Setting up a network load balancer with a backend service](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network-backend-service)
  * [Transitioning a network load balancer from a target pool to a backend service](https://docs.cloud.google.com/load-balancing/docs/network/transition-to-backend-services)



This feature is available in **Preview**.

## October 20, 2020

Feature

For [HTTP requests](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#httprequest), the `httpRequest.remoteIp` and `httpRequest.serverIp` fields can include port information. For example `10.0.0.1:80`.

## October 08, 2020

Feature

External HTTP(S) Load Balancing is now supported for App Engine, Cloud Functions, and Cloud Run services. To configure this, you will need to use a new type of network endpoint group (NEG) called a [Serverless NEG](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts).

This feature is now available in **General Availability**.

## October 01, 2020

Change

Added a new [tutorial for delivering HTTP and HTTPS content over the same hostname when using Cloud CDN](https://docs.cloud.google.com/load-balancing/docs/tutorials/http-https-over-same-domain). While many browsers enforce the use of Transport Layer Security (TLS) and disallow non-secure content delivery, there are still use cases where non-secure delivery and secure delivery must be allowed over the same hostname.

## September 15, 2020

Feature

Added total latency to [external HTTP(S) load balancer Cloud Logging](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring) entries. Total latency measures from when the external HTTP(S) load balancer receives the first bytes of the incoming request headers until the external HTTP(S) load balancer finishes proxying the backend's response to the client. This feature is now available in **General Availability**.

## September 14, 2020

Feature

The External HTTP(S) Load Balancer now supports setting [custom response headers](https://docs.cloud.google.com/load-balancing/docs/custom-headers) on backend buckets and services. This feature is available in **Beta**.

Custom response headers make it easier to set common web security headers and override response headers from your application at the load balancer.

## September 09, 2020

Change

Added a new tutorial: [Faster web performance and improved web protection for load balancing](https://docs.cloud.google.com/load-balancing/docs/tutorials/faster-performance-improved-protection).

## August 31, 2020

Feature

Google Cloud internal HTTP(S) load balancers have native support for the WebSocket protocol when you use HTTP or HTTPS as the protocol to the backend. The load balancer does not need any configuration to [proxy WebSocket connections](https://docs.cloud.google.com/load-balancing/docs/l7-internal#websocket_support).

## August 19, 2020

Feature

The Organization policy constraint for [restricting Cloud Load Balancing creation](https://docs.cloud.google.com/load-balancing/docs/org-policy-constraints) is now available in **General Availability**.

## August 17, 2020

Feature

[Setting up Internal HTTP(S) Load Balancing in a Shared VPC _service_ project](https://docs.cloud.google.com/load-balancing/docs/l7-internal/l7-internal-shared-vpc) is now available in **General Availability**.

## July 25, 2020

Change

The introductory period during which you could use Internal HTTP(S) Load Balancing without charge has ended. Starting July 25, 2020, your usage of Internal HTTP(S) Load Balancing will be [billed to your project](https://docs.cloud.google.com/vpc/network-pricing#internal-https-lb).

## July 16, 2020

Feature

The Organization Policy for [restricting load balancer creation](https://docs.cloud.google.com/load-balancing/docs/org-policy-constraints) has launched into **Beta**.

## July 13, 2020

Feature

Internal TCP/UDP load balancers now support [regional health checks](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks). To configure, see [Health checks for backend services](https://docs.cloud.google.com/load-balancing/docs/health-checks#hc-to-bes). This feature is supported in **General Availability**.

## July 07, 2020

Feature

External HTTP(S) Load Balancing is now supported for App Engine, Cloud Functions, and Cloud Run services. To configure this, you will need to use a new type of network endpoint group (NEG) called a [Serverless NEG](https://docs.cloud.google.com/load-balancing/docs/negs/setting-up-serverless-negs). 

This feature is available in Beta.

## June 29, 2020

Feature

You can now [create an internal HTTP(S) load balancer in a Shared VPC  _service_ project](https://docs.cloud.google.com/load-balancing/docs/l7-internal#shared_vpc). 

This feature is available in **Alpha**. Please contact your Google account team to get access to this feature.

## June 25, 2020

Change

The introductory period during which you can use Internal HTTP(S) Load Balancing without charge is coming to an end. Starting on July 25, 2020, your usage of Internal HTTP(S) Load Balancing will be [billed to your project](https://docs.cloud.google.com/compute/network-pricing#internal-https-lb).

## June 03, 2020

Feature

[HTTP(S) Load Balancing logging](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#logging) is now available in **General Availability**.

## June 02, 2020

Feature

You can now use a [custom filter](https://docs.cloud.google.com/load-balancing/docs/negs/setting-up-zonal-negs#custom_filtering_when_you_list_endpoints_in_a_network_endpoint_group) when you list endpoints in a zonal network endpoint group. This feature is available as a Beta release.

## May 20, 2020

Feature

For internal TCP/UDP load balancers, you can create [multiple forwarding rules with the same IP address](https://docs.cloud.google.com/load-balancing/docs/internal/multiple-forwarding-rules-same-ip). The forwarding rules can have different protocols and ports. This feature is available in **Beta**.

## April 27, 2020

Feature

[Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/google-managed-certs) are available in **General Availability**.

## April 23, 2020

Feature

External HTTP(S) load balancers now support [header-based routing](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-traffic-management#http-header-based-routing) and [query parameter-based routing](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-traffic-management#query-parameter-routing).

These features are available in **General Availability**.

## April 20, 2020

Feature

[Internal TCP/UDP Load Balancing with failover groups](https://docs.cloud.google.com/load-balancing/docs/internal/failover-overview) is available in **General Availability**.

## April 14, 2020

Feature

External HTTP(S) load balancers now support [URL rewrites and redirects](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management). 

URL rewrites allow you to decouple the URLs that your external users use from those that your services use.

With URL redirects, you can redirect client requests from one URL to another URL.

These features are available in **General Availability**.

## April 10, 2020

Change

[Backend services documentation](https://docs.cloud.google.com/load-balancing/docs/backend-service) is updated through the Cloud Load Balancing doc set.

## April 09, 2020

Feature

TLS v1.3 is now enabled by default for all external HTTPS load balancers, SSL proxy load balancers, and Cloud CDN. Note that this change doesn't apply to internal HTTPS load balancers or Traffic Director.

TLS v1.3 supports modern ciphers with forward-secrecy as a baseline and, critically, reduces the number of round trips required to establish a TLS session, which directly improves performance seen by your end-users.

Clients that support TLS v1.3 include Chrome, Chromium-based browsers, and Android. These clients automatically negotiate TLS v1.3 without requiring any changes. Clients that do not support TLS v1.3 are unaffected.

## March 25, 2020

Feature

Network endpoint groups (NEGs) now support [global, internet endpoints](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts) that let you create [custom origins for Cloud CDN](https://docs.cloud.google.com/cdn/docs/custom-origins-overview) and deliver content over Google's high performance, distributed edge caching infrastructure when the content is hosted on-premises or in another cloud. This feature is available in **General Availability**.

## March 20, 2020

Change

To help you get started quickly, added two new examples for external HTTP(S) Load Balancing:

  * [Setting up a simple external HTTP load balancer](https://docs.cloud.google.com/load-balancing/docs/https/ext-http-lb-simple)
  * [Setting up a simple external HTTPS load balancer](https://docs.cloud.google.com/load-balancing/docs/https/ext-https-lb-simple)



Feature

[Health check logging](https://docs.cloud.google.com/load-balancing/docs/health-check-logging) is now available in **Beta**.

## March 18, 2020

Feature

IAM Conditions now supports [forwarding rule attributes](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions). You can use these attributes to specify the types of forwarding rules that a member can create. This feature is available in **General Availability**.

Feature

Internal HTTP(S) Load Balancing now supports [configurable idle timeouts](https://docs.cloud.google.com/load-balancing/docs/l7-internal#timeouts_and_retries).

## February 25, 2020

Feature

Internal HTTP(S) Load Balancing now supports [accessing your load balancer from a connected network](https://docs.cloud.google.com/load-balancing/docs/internal-lb-and-other-networks) through VPC Peering, Cloud VPN, and Cloud Interconnect.

Change

Updated and reorganized documentation for [SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates).

## February 21, 2020

Feature

For Internal TCP/UDP Load Balancing, [load balancing to multiple NICs on a single backend VM instance](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview#ilb-nh-multi-nic) is now available in **General Availability**.

## February 19, 2020

Feature

[Global access for Internal TCP/UDP Load Balancing](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#ilb-global-access) is now available in **General Availability**.

## February 10, 2020

Feature

Network endpoint groups (NEGs) now support [global, internet endpoints](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts) that let you create [custom origins for Cloud CDN](https://docs.cloud.google.com/cdn/docs/custom-origins-overview) and deliver content over Google's high performance, distributed edge caching infrastructure when the content is hosted on-premises or in another cloud. This feature is available in **Beta**.

## February 04, 2020

Feature

IAM Conditions now supports [forwarding rule](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions) attributes. You can use these attributes to specify the types of forwarding rules that a member can create. This feature is available in **Beta**.

## January 29, 2020

Feature

[Network Load Balancing monitoring](https://docs.cloud.google.com/load-balancing/docs/network/networklb-monitoring) is now available in **General Availability**.

## January 15, 2020

Change

Improved documentation for [Adding backend buckets to load balancers](https://docs.cloud.google.com/load-balancing/docs/https/adding-backend-buckets-to-load-balancers).

## January 06, 2020

Change

Added [load balancer feature tables](https://docs.cloud.google.com/load-balancing/docs/features).

## December 11, 2019

Feature

[Internal TCP/UDP Load Balancing with global access](https://docs.cloud.google.com/load-balancing/docs/internal/internal-tcp-udp-lb-and-other-networks#global_access) is available in **Beta**.

Feature

[Internal TCP/UDP Load Balancing as next hop](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview) is available in **General Availability**.

## December 10, 2019

Feature

[Internal HTTP(S) Load Balancing](https://docs.cloud.google.com/load-balancing/docs/l7-internal) is available in **General Availability**.

Feature

[Multiple domains for Google-managed SSL certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#multiplessl) is now available in **Beta**.

## November 18, 2019

Feature

For Internal TCP/UDP Load Balancing, [load balancing to multiple NICs](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview#ilb-nh-multi-nic) on a single backend VM instance is now available in **Beta**.

## October 18, 2019

Change

Added information about [TCP and UDP request and return packets](https://docs.cloud.google.com/load-balancing/docs/internal#tcp-udp-request-return) for Internal TCP/UDP Load Balancing.

Change

For the HTTP(S), TCP proxy, and SSL proxy load balancers, the Stackdriver logging timestamp field in the [LogEntry](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) now shows the time that requests arrived at the load balancer. Previously, the timestamp showed the time the response was sent by the load balancer back to the client.

Change

[Expanded information](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#ip-ranges) about the probe IP ranges for backend health checks.

## September 09, 2019

Feature

[HTTP(S) Load Balancing logging](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#logging) is now available in **Beta**.

## September 06, 2019

Change

Documentation update: Creation of [new load balancing tutorial](https://docs.cloud.google.com/load-balancing/docs/https/https-load-balancer-example) that is both content-based and cross-regional.

  * The Content-based load balancing tutorial has been modified to include cross-region functionality.
  * The Cross-region load balancing tutorial has been removed.
  * Links to both original tutorials now redirect to the combined tutorial.
  * Modified file [Adding a Cloud Storage bucket to content-based load balancing](https://docs.cloud.google.com/load-balancing/docs/https/adding-a-backend-bucket-to-content-based-load-balancing) to create two buckets and modify the load balancer accordingly.



## August 28, 2019

Feature

[Internal TCP/UDP Load Balancing as next hop](https://docs.cloud.google.com/load-balancing/docs/internal/ilb-next-hop-overview) is available in **Beta**.

## August 13, 2019

Change

External HTTP(S) load balancers validate protocol selection during ALPN negotiation. For more information, see [RFC 7301](https://tools.ietf.org/html/rfc7301).

## August 09, 2019

Change

[Creating user-defined request headers](https://docs.cloud.google.com/load-balancing/docs/user-defined-request-headers) is published. The information is removed from the [backend services documentation](https://docs.cloud.google.com/load-balancing/docs/backend-service)

## July 31, 2019

Feature

[Internal HTTP(S) Load Balancing](https://docs.cloud.google.com/load-balancing/docs/l7-internal) is available in **Beta**.

## July 26, 2019

Feature

[HTTP/2 between the load balancer and backends](https://docs.cloud.google.com/load-balancing/docs/backend-service#protocol_to_the_backends) is available in **General Availability**.

Feature

[HTTP/2 health checking](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) is available in **General Availability**.

## June 27, 2019

Feature

[The user-defined request header feature](https://docs.cloud.google.com/load-balancing/docs/user-defined-request-headers) is available in **General Availability**.

## June 20, 2019

Feature

[Network endpoint groups in load balancing](https://docs.cloud.google.com/load-balancing/docs/negs) is available in **General Availability**.

## May 16, 2019

Change

Documentation update: The quotas and limits for load balancing resources are now documented. See [Load Balancing Resource Quotas](https://docs.cloud.google.com/load-balancing/docs/quotas).

## May 15, 2019

Change

Documentation update: The global forwarding rules page (previously at /load-balancing/docs/https/global-forwarding-rules) is combined with [Forwarding rule concepts](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts).

## April 10, 2019

Feature

[Traffic Director](https://docs.cloud.google.com/traffic-director/docs) is available in **Beta**.

## April 09, 2019

Feature

[Internal TCP/UDP Load Balancing with failover groups](https://docs.cloud.google.com/load-balancing/docs/internal/failover-overview) is available in **Beta**.

## March 25, 2019

Feature

[Internal TCP/UDP Load Balancing support for all ports](https://docs.cloud.google.com/load-balancing/docs/internal#all_ports) is in **General Availability**.

## March 06, 2019

Change

**Documentation updates for Internal TCP/UDP Load Balancing** – The following documents have been updated or added:

  * [Internal TCP/UDP Load Balancing Concepts](https://docs.cloud.google.com/load-balancing/docs/internal)
  * [Setting Up Internal TCP/UDP Load Balancing](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal)
  * [Accessing Internal TCP/UDP Load Balancing from Connected Networks](https://docs.cloud.google.com/load-balancing/docs/internal/internal-tcp-udp-lb-and-other-networks)



## January 11, 2019

Feature

[DNS-based service discovery for your internally load-balanced services](https://docs.cloud.google.com/load-balancing/docs/dns-names) is available in **General Availability**.

## December 04, 2018

Feature

The HTTP(S) load balancer now supports sending an HTTP DELETE with a body to the load balancer.

## October 24, 2018

Feature

[Content-based HTTP(S) health checking](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-http) is now available in **General Availability**.

## June 28, 2018

Feature

[HTTP/2 and gRPC to backend VMs](https://docs.cloud.google.com/load-balancing/docs/https#backend_services) is now available in **Beta**.

Feature

[Content-based HTTP(S) health checking](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-http) is now available in **Beta**.

## June 13, 2018

Feature

[QUIC support for HTTPS Load Balancing](https://docs.cloud.google.com/load-balancing/docs/https#QUIC) is now available in **General Availability**.

## April 17, 2018

Feature

[SSL Policies configuration for HTTPS and SSL Proxy Load Balancing](https://docs.cloud.google.com/load-balancing/docs/use-ssl-policies) is now available in **General Availability**.

## April 10, 2018

Feature

[QUIC support for HTTPS Load Balancing](https://docs.cloud.google.com/load-balancing/docs/https#QUIC) is now available in **Beta**.

## April 04, 2018

Feature

[User-defined request headers for HTTP(S) Load Balancing](https://docs.cloud.google.com/load-balancing/docs/user-defined-request-headers) is now available in **Beta**.

## January 18, 2018

Feature

[SSL Policies for HTTPS and SSL Proxy Load Balancing](https://docs.cloud.google.com/load-balancing/docs/use-ssl-policies) is now available in **Beta**.

## December 20, 2017

Feature

[Internal Load Balancing access across VPN or Interconnect](https://docs.cloud.google.com/load-balancing/docs/internal/internal-tcp-udp-lb-and-other-networks) is now available in **General Availability**.

## November 20, 2017

Feature

[Internal Load Balancing access across VPN or Interconnect](https://docs.cloud.google.com/load-balancing/docs/internal/internal-tcp-udp-lb-and-other-networks) is now available in **Beta**.

## September 19, 2017

Feature

[IPv6 Termination for HTTP(S), SSL Proxy, and TCP Proxy Load Balancing](https://docs.cloud.google.com/load-balancing/docs/internal) is now available in **General Availability**.

## September 07, 2017

Feature

[Multiple SSL certificate support](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates) is now available in **General Availability**.

## July 19, 2017

Feature

[Regional instance groups for Internal Load Balancing](https://docs.cloud.google.com/load-balancing/docs/internal/setting-up-internal#internal_load_balancing_with_regional_instance_groups) is now available in **General Availability**.

## June 26, 2017

Feature

[TCP Proxy Load Balancing](https://docs.cloud.google.com/load-balancing/docs/ssl) is now available in **General Availability**.

## May 02, 2017

Feature

[IPv6 Termination for HTTP(S), SSL Proxy, and TCP Proxy Load Balancing](https://docs.cloud.google.com/load-balancing/docs/ipv6) is now available in **Beta**.

## April 19, 2017

Feature

[Websocket support for HTTP(S) Load Balancing](https://docs.cloud.google.com/load-balancing/docs/https#websocket_proxy_support) is now available in **General Availability**.

## April 06, 2017

Feature

[TCP Proxy Load Balancing](https://docs.cloud.google.com/load-balancing/docs/ssl) is now available in **Beta**.

## April 05, 2017

Feature

[Google Cloud Storage support for HTTP(S) Load Balancing](https://docs.cloud.google.com/load-balancing/docs/https/adding-a-backend-bucket-to-content-based-load-balancing) is now available in **General Availability**.

## March 06, 2017

Feature

[IPv6 Termination for HTTP(S), SSL Proxy, and TCP Proxy Load Balancing](https://docs.cloud.google.com/load-balancing/docs/ipv6) is now available in **Alpha**.

## December 08, 2016

Feature

[Internal Load Balancing](https://docs.cloud.google.com/load-balancing/docs/internal) is now available in **General Availability**.

## October 21, 2016

Feature

[Internal Load Balancing](https://docs.cloud.google.com/load-balancing/docs/internal) is now available in **Beta**.

## September 26, 2016

Feature

[Session Affinity for HTTP(S) Load Balancing](https://docs.cloud.google.com/load-balancing/docs/https#session_affinity) is now available in **General Availability**.

Feature

[SSL Proxy Load Balancing](https://docs.cloud.google.com/load-balancing/docs/tcp) is now available in **General Availability**.

## August 08, 2016

Feature

[SSL Proxy Load Balancing](https://docs.cloud.google.com/load-balancing/docs/tcp) is now available in **Beta**.

## October 29, 2015

Feature

[HTTP(S) Load Balancing](https://docs.cloud.google.com/load-balancing/docs/https) is now available in **General Availability**.

## June 03, 2015

Feature

[HTTPS Load Balancing](https://docs.cloud.google.com/load-balancing/docs/https) is now available in **Beta**.

## September 18, 2014

Feature

[HTTP Load Balancing](https://docs.cloud.google.com/load-balancing/docs/https) is now available in **Beta**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
