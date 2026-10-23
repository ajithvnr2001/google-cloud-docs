---
url: https://docs.cloud.google.com/secure-web-proxy/docs/release-notes/
title: Secure Web Proxy release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:10.993363+00:00
---

# Secure Web Proxy release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Resources ](https://docs.cloud.google.com/secure-web-proxy/docs/resources)



Send feedback 

#  Secure Web Proxy release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Secure Web Proxy. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/secure-web-proxy-release-notes.xml) directly. 

## October 14, 2026

Feature

Secure Web Proxy supports [service rate limiting policies](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#rate-limiting-policies). Use these policies to protect external destinations from traffic overloads and manage the costs of your outbound web traffic.

You can attach a service rate limiting policy to your Secure Web Proxy gateways, whether they use an [authorization policy](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#authorization-policies) or a [gateway security policy](https://docs.cloud.google.com/secure-web-proxy/docs/create-a-policy#gateway-security-policies). For more information, see [Configure service rate limiting policies](https://docs.cloud.google.com/secure-web-proxy/docs/configure-service-rate-limiting-policies).

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## October 09, 2026

Feature

Secure Web Proxy supports [global access](https://docs.cloud.google.com/secure-web-proxy/docs/configure-global-access). You can enable this feature when creating a Secure Web Proxy instance to make sure that clients from any Google Cloud region can connect to your proxy.

With global access, you can route your outbound traffic through specific regions to meet regulatory compliance or cost requirements. You can also use this option to simplify your network administration by managing outbound traffic from a centralized location.

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## September 17, 2026

Feature

Secure Web Proxy supports [distributed tracing](https://docs.cloud.google.com/secure-web-proxy/docs/distributed-tracing-overview) by integrating with [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview). With distributed tracing, you can [track the lifecycle of outbound requests](https://docs.cloud.google.com/secure-web-proxy/docs/monitor-traces) from internal workloads through your Secure Web Proxy gateways to external endpoints. This integration helps you detect latency bottlenecks and troubleshoot connectivity errors.

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## August 20, 2026

Feature

Secure Web Proxy supports the [local intermediate CA signing](https://docs.cloud.google.com/secure-web-proxy/docs/tls-inspection-overview#local_intermediate_ca_signing) certificate issuance mode for TLS inspection. By using this mode, Secure Web Proxy caches a single intermediate certificate authority (CA) certificate from your CA pool to sign leaf certificates locally for requested domains, reducing certificate issuance requests and transaction costs. To use this certificate issuance mode, you must make sure that your CA pool is configured to issue intermediate CA certificates.

For more information, see [Certificate issuance modes](https://docs.cloud.google.com/secure-web-proxy/docs/tls-inspection-overview#certificate_issuance_modes) and [Configure a local intermediate CA signing](https://docs.cloud.google.com/secure-web-proxy/docs/enable-tls-inspection#ca-pool-intermediate-ca-config).

This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## June 16, 2026

Feature

You can use [authorization policies](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#authorization-policies) to perform identity-based and content-based access control checks when processing outbound traffic requests through Secure Web Proxy.

By [configuring authorization policies](https://docs.cloud.google.com/secure-web-proxy/docs/setup-authz-policies), you can set rules for your workloads to access external destinations. You can also use these authorization policies to delegate complex authorization decisions to identity and content-scanning services like Service Extensions.

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

You can [integrate frontend mutual TLS (mTLS) with Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/use-frontend-mtls-with-swp) to boost the security of your applications and workloads.

With this integration, you can use validated client identities in Secure Web Proxy [authorization policies](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#authorization-policies) to enforce granular access control for outbound traffic.

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## May 21, 2026

Feature

When you deploy your Secure Web Proxy instance as a [next hop](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop), you can configure the gateway to listen on all ports (`1` through `65535`). With this feature, your proxy automatically intercepts all outbound traffic and enforces security policies and rules on it. This removes the need to manage specific port lists.

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## August 18, 2025

Feature

Secure Web Proxy supports [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_swp). For more information, see [Configure VPC Service Controls for Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/vpc-sc-support).

This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## January 20, 2025

Feature

Secure Web Proxy uses a [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) gateway to allow external communication between Google Cloud workloads and internet destinations. When you set up your Secure Web Proxy instance, a [network address translation (NAT)](https://www.wikipedia.org/wiki/Network_address_translation) gateway is automatically created.

To limit the number of IP addresses that are used, the Cloud NAT gateway uses [dynamic port allocation (DPA)](https://docs.cloud.google.com/nat/docs/ports-and-addresses#dynamic-port) for Secure Web Proxy. For more information, see [Use Cloud NAT for Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/use-cloud-nat-for-swp).

This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## October 28, 2024

Feature

You can configure your Secure Web Proxy instance as a [next hop](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop) to route web traffic within your Virtual Private Cloud (VPC) network. To deploy your Secure Web Proxy instance as a next hop, you can use either [policy-based routes](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop#policy-based-routes) or [static routes](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-next-hop#static-routes).

This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## September 17, 2024

Feature

The [Direct Virtual Private Cloud (VPC) egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) feature of Cloud Run supports Secure Web Proxy. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## June 03, 2024

Feature

You can deploy your Secure Web Proxy instance as a [Private Service Connect (PSC) service attachment](https://docs.cloud.google.com/secure-web-proxy/docs/deploy-service-attachment). Use this deployment mode to centralize and apply gateway security policies on your outbound web traffic.

This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## May 22, 2023

Feature

[Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview) is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

## March 14, 2023

Feature

Secure Web Proxy supports [Transport Layer Security (TLS) inspection](https://docs.cloud.google.com/secure-web-proxy/docs/tls-inspection-overview). You can use TLS inspection to intercept TLS traffic, inspect encrypted requests, and enforce [gateway security policies and rules](https://docs.cloud.google.com/secure-web-proxy/docs/policies-and-rules-overview#policies-overview).

This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## October 31, 2022

Feature

Cloud Secure Web Gateway helps protect your outbound HTTP and HTTPS traffic. To sign up to use Secure Web Gateway, contact your sales representative.

Secure Web Gateway is available in [Preview](https://cloud.google.com/products#product-launch-stages).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
