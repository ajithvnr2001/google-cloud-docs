---
url: https://docs.cloud.google.com/feeds/secure-web-proxy-release-notes.xml
title: Secure Web Proxy - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:26:56.312940+00:00
---

# Secure Web Proxy - Release notes

> Source: https://docs.cloud.google.com/feeds/secure-web-proxy-release-notes.xml

tag:google.com,2016:secure-web-proxy-release-notesSecure Web Proxy - Release notesGoogle Cloud Platform2026-10-14T00:00:00-07:00October 14, 2026tag:google.com,2016:secure-web-proxy-release-notes#October_14_20262026-10-14T00:00:00-07:00Feature 

Secure Web Proxy supports [service rate limiting policies](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#rate-limiting-policies). Use these policies to protect external destinations from traffic overloads and manage the costs of your outbound web traffic.

You can attach a service rate limiting policy to your Secure Web Proxy gateways, whether they use an [authorization policy](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#authorization-policies) or a [gateway security policy](https://docs.cloud.google.com/secure-web-proxy/docs/create-a-policy#gateway-security-policies). For more information, see [Configure service rate limiting policies](https://docs.cloud.google.com/secure-web-proxy/docs/configure-service-rate-limiting-policies).

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

]]> October 09, 2026tag:google.com,2016:secure-web-proxy-release-notes#October_09_20262026-10-09T00:00:00-07:00Feature 

Secure Web Proxy supports [global access](https://docs.cloud.google.com/secure-web-proxy/docs/configure-global-access). You can enable this feature when creating a Secure Web Proxy instance to make sure that clients from any Google Cloud region can connect to your proxy.

With global access, you can route your outbound traffic through specific regions to meet regulatory compliance or cost requirements. You can also use this option to simplify your network administration by managing outbound traffic from a centralized location.

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

]]> September 17, 2026tag:google.com,2016:secure-web-proxy-release-notes#September_17_20262026-09-17T00:00:00-07:00Feature 

Secure Web Proxy supports [distributed tracing](https://docs.cloud.google.com/secure-web-proxy/docs/distributed-tracing-overview) by integrating with [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview). With distributed tracing, you can [track the lifecycle of outbound requests](https://docs.cloud.google.com/secure-web-proxy/docs/monitor-traces) from internal workloads through your Secure Web Proxy gateways to external endpoints. This integration helps you detect latency bottlenecks and troubleshoot connectivity errors.

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

]]> August 20, 2026tag:google.com,2016:secure-web-proxy-release-notes#August_20_20262026-08-20T00:00:00-07:00Feature 

Secure Web Proxy supports the [local intermediate CA signing](https://docs.cloud.google.com/secure-web-proxy/docs/tls-inspection-overview#local_intermediate_ca_signing) certificate issuance mode for TLS inspection. By using this mode, Secure Web Proxy caches a single intermediate certificate authority (CA) certificate from your CA pool to sign leaf certificates locally for requested domains, reducing certificate issuance requests and transaction costs. To use this certificate issuance mode, you must make sure that your CA pool is configured to issue intermediate CA certificates.

For more information, see [Certificate issuance modes](https://docs.cloud.google.com/secure-web-proxy/docs/tls-inspection-overview#certificate_issuance_modes) and [Configure a local intermediate CA signing](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection#ca-pool-intermediate-ca-config).

This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

]]> June 16, 2026tag:google.com,2016:secure-web-proxy-release-notes#June_16_20262026-06-16T00:00:00-07:00Feature 

You can use [authorization policies](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#authorization-policies) to perform identity-based and content-based access control checks when processing outbound traffic requests through Secure Web Proxy.

By [configuring authorization policies](https://docs.cloud.google.com/secure-web-proxy/docs/setup-authz-policies), you can set rules for your workloads to access external destinations. You can also use these authorization policies to delegate complex authorization decisions to identity and content-scanning services like Service Extensions.

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

### Feature

You can [integrate frontend mutual TLS (mTLS) with Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/use-frontend-mtls-with-swp) to boost the security of your applications and workloads.

With this integration, you can use validated client identities in Secure Web Proxy [authorization policies](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#authorization-policies) to enforce granular access control for outbound traffic.

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

]]> May 21, 2026tag:google.com,2016:secure-web-proxy-release-notes#May_21_20262026-05-21T00:00:00-07:00Feature 

When you deploy your Secure Web Proxy instance as a [next hop](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop), you can configure the gateway to listen on all ports (`1` through `65535`). With this feature, your proxy automatically intercepts all outbound traffic and enforces security policies and rules on it. This removes the need to manage specific port lists.

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

]]> August 18, 2025tag:google.com,2016:secure-web-proxy-release-notes#August_18_20252025-08-18T00:00:00-07:00Feature 

Secure Web Proxy supports [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_swp). For more information, see [Configure VPC Service Controls for Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/vpc-sc-support).

This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

]]> January 20, 2025tag:google.com,2016:secure-web-proxy-release-notes#January_20_20252025-01-20T00:00:00-08:00Feature 

Secure Web Proxy uses a [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) gateway to allow external communication between Google Cloud workloads and internet destinations. When you set up your Secure Web Proxy instance, a [network address translation (NAT)](https://www.wikipedia.org/wiki/Network_address_translation) gateway is automatically created.

To limit the number of IP addresses that are used, the Cloud NAT gateway uses [dynamic port allocation (DPA)](https://docs.cloud.google.com/nat/docs/ports-and-addresses#dynamic-port) for Secure Web Proxy. For more information, see [Use Cloud NAT for Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/use-cloud-nat-for-swp).

This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

]]> October 28, 2024tag:google.com,2016:secure-web-proxy-release-notes#October_28_20242024-10-28T00:00:00-07:00Feature 

You can configure your Secure Web Proxy instance as a [next hop](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop) to route web traffic within your Virtual Private Cloud (VPC) network. To deploy your Secure Web Proxy instance as a next hop, you can use either [policy-based routes](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop#policy-based-routes) or [static routes](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop#static-routes).

This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

]]> September 17, 2024tag:google.com,2016:secure-web-proxy-release-notes#September_17_20242024-09-17T00:00:00-07:00Feature 

The [Direct Virtual Private Cloud (VPC) egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) feature of Cloud Run supports Secure Web Proxy. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

]]> June 03, 2024tag:google.com,2016:secure-web-proxy-release-notes#June_03_20242024-06-03T00:00:00-07:00Feature 

You can deploy your Secure Web Proxy instance as a [Private Service Connect (PSC) service attachment](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-service-attachment). Use this deployment mode to centralize and apply gateway security policies on your outbound web traffic.

This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

]]> May 22, 2023tag:google.com,2016:secure-web-proxy-release-notes#May_22_20232023-05-22T00:00:00-07:00Feature 

[Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview) is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

]]> March 14, 2023tag:google.com,2016:secure-web-proxy-release-notes#March_14_20232023-03-14T00:00:00-07:00Feature 

Secure Web Proxy supports [Transport Layer Security (TLS) inspection](https://docs.cloud.google.com/secure-web-proxy/docs/tls-inspection-overview). You can use TLS inspection to intercept TLS traffic, inspect encrypted requests, and enforce [gateway security policies and rules](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#policies-overview).

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

]]> October 31, 2022tag:google.com,2016:secure-web-proxy-release-notes#October_31_20222022-10-31T00:00:00-07:00Feature 

Cloud Secure Web Gateway helps protect your outbound HTTP and HTTPS traffic. To sign up to use Secure Web Gateway, contact your sales representative.

Secure Web Gateway is available in [Preview](https://cloud.google.com/products#product-launch-stages).

]]>
