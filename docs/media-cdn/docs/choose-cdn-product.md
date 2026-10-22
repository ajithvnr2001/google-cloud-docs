---
url: https://docs.cloud.google.com/media-cdn/docs/choose-cdn-product/
title: Choose a CDN product \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:47.527947+00:00
---

# Choose a CDN product  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/choose-cdn-product/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Choose a CDN product Stay organized with collections  Save and categorize content based on your preferences. 

[Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview) is Google Cloud's web acceleration Content Delivery Network platform that helps you cache regularly accessed static content closer to your users. Cloud CDN is optimized for serving a mix of static and dynamic latency-sensitive web assets, such as CSS, JavaScript, HTML, and image files.

[Media CDN](https://docs.cloud.google.com/media-cdn/docs/overview) is Google Cloud's media delivery CDN platform that complements Cloud CDN. Media CDN is optimized for high-throughput egress workloads such as streaming video and large file downloads.

Using Cloud CDN and Media CDN can improve performance for your users, lower your origin infrastructure resource usage, and reduce your network delivery costs.

The two products support a similar set of features, but each product is optimized for certain use cases. Comparing Cloud CDN to Media CDN is similar to comparing Cloud SQL to BigQuery. Cloud CDN and Cloud SQL are for _small_ queries at scale. Media CDN and BigQuery are designed for throughput and extreme scale. Using Media CDN for serving JavaScript or CSS (web workloads) is similar to trying to use BigQuery for 5-GB tables with a few thousand rows. It works, but it's not optimized for that use case.

## Use cases

The following table describes some common use cases and the recommended CDN product.

Use case | Recommended CDN product  
---|---  
Serve workloads with both standard web content and media content, such as social media sites. |  You can have two configurations in this scenario: 

  * Use Cloud CDN to serve static website assets, in combination with an external Application Load Balancer to serve your application APIs, such as your web portal.
  * Use Media CDN to serve streaming video, downloads, or other high-throughput content.

  
Serve a website quickly to users. | Cloud CDN is the right choice for workloads that tend to deliver very small objects at high rates, such as ad tech and ecommerce platforms. Its strength is serving static web content, such as JavaScript, CSS, fonts, and inline images.   
Serve large software downloads. | If you anticipate a large demand for software downloads, consider Media CDN. If software downloads are a small fraction of your overall web workload, consider Cloud CDN.  
Deliver streaming video over HLS and DASH. | If you have large-scale video streaming needs, Media CDN is the right choice due to improved origin shielding, Tbps-scale capacity, and detailed logging and metrics.   
Meet strong compliance needs for serving firmware downloads—for example, to government agencies or healthcare providers.  |  Cloud CDN is the right choice. Cloud CDN has [Federal Risk and Authorization Management Program (FedRAMP)](https://cloud.google.com/security/compliance/fedramp) authorization and is best positioned to meet strong compliance needs. Unless you are using signed requests, content stored in a CDN cache is typically publicly accessible by URL. As with any CDN, consider using your own digital rights management (DRM) or encryption schemes where needed.  
Serve user-generated image content to users. | Cloud CDN is the right choice for most image-serving platforms.   
  
### Exceptions

The following table describes use cases where Cloud CDN or Media CDN aren't suitable.

Use case | Suggestion  
---|---  
Deliver video over Real-Time Messaging Protocol (RTMP). | Media CDN and Cloud CDN don't support RTMP-based delivery to clients. You can configure a regional external passthrough Network Load Balancer to deliver RTMP if you have any legacy RTMP-based services. You can also use Live Stream API to package RTMP source streams into HLS/DASH assets for delivery through Media CDN.  
Deliver user-to-user video over WebRTC. |  Media CDN and Cloud CDN don't support WebRTC delivery. You can configure a regional external passthrough Network Load Balancer to manage WebRTC-based services.   
Use WebSockets for user-server communication. | Set up a global external Application Load Balancer. WebSocket traffic is not cacheable, and it benefits from the global backbone that connects Google's locations—where the external Application Load Balancer runs—to your backends.   
Serve sensitive workloads, such as health data or other user-specific data. | Don't use Cloud CDN or Media CDN for serving sensitive workloads or user-specific data.  
  
## Get started with a CDN product

To start working with a CDN product, see the following pages:

  * [Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview)

  * [Media CDN](https://docs.cloud.google.com/media-cdn/docs/overview)




## Supported CDN features

The following tables summarize the features available in Cloud CDN and Media CDN.

### Origin and backend support

Feature | Cloud CDN | Media CDN  
---|---|---  
Cloud Storage buckets, including redundant multi-region storage | ✓ | ✓  
Compute Engine virtual machine (VM) instances | ✓ | ✓  
Google Kubernetes Engine (GKE) container instances | ✓ | ✓  
External backends (custom origins)—on-premises, multicloud | ✓[info](https://docs.cloud.google.com/cdn/docs/ext-backend-internet-neg-overview) | ✓  
App Engine, Cloud Run functions, or Cloud Run services | ✓ | ✓  
Origin failover |  | ✓[info](https://docs.cloud.google.com/media-cdn/docs/origins#failover-and-timeouts)  
Configurable timeouts | ✓[info](https://docs.cloud.google.com/load-balancing/docs/https/request-distribution#timeouts_and_retries) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/origins#failover-and-timeouts)  
  
### Caching

Feature | Cloud CDN | Media CDN  
---|---|---  
Request collapsing (coalescing) | ✓[info](https://docs.cloud.google.com/cdn/docs/caching#request-coalescing) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/origins#request-collapsing)  
Origin shielding |  | ✓[info](https://docs.cloud.google.com/media-cdn/docs/origins#origin-shielding)  
Custom cache keys | ✓[info](https://docs.cloud.google.com/cdn/docs/using-cache-keys) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/caching#cache-keys)  
Configurable caching overrides | ✓[info](https://docs.cloud.google.com/cdn/docs/using-cache-modes) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/caching#cache-modes)  
Programmatic cache invalidation | ✓[info](https://docs.cloud.google.com/cdn/docs/cache-invalidation-overview) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/cache-invalidation)  
Standard `Cache-Control` directives | ✓[info](https://docs.cloud.google.com/cdn/docs/caching#cache_control_directives) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/caching#cacheablity)  
Configurable TTLs | ✓[info](https://docs.cloud.google.com/cdn/docs/using-ttl-overrides) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/caching#configuring-ttls)  
Negative caching | ✓[info](https://docs.cloud.google.com/cdn/docs/using-negative-caching) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/caching#negative-caching)  
Asynchronous content validation | ✓[info](https://docs.cloud.google.com/cdn/docs/serving-stale-content) |   
Bypass the cache | ✓[info](https://docs.cloud.google.com/cdn/docs/caching#bypassing-cache) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/caching#bypass-cache)  
Per-origin cache policies | ✓[info](https://docs.cloud.google.com/cdn/docs/caching#cache-modes) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/caching#cache-modes)  
Per-route cache policies | ✓[info](https://docs.cloud.google.com/cdn/docs/caching#cache-policies-url-maps) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/caching#cache-modes)  
Dynamic compression | ✓[info](https://docs.cloud.google.com/cdn/docs/dynamic-compression) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/dynamic-compression)  
  
### Route matching and origin selection

Feature | Cloud CDN | Media CDN  
---|---|---  
Host-based and path-based backend selection | ✓[info](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/routing#path-matching)  
URL redirects | ✓[info](https://docs.cloud.google.com/cdn/docs/setting-up-http-https-redirect) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/routing#redirect-requests)  
URL rewrites | ✓[info](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-url-rewrite) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/routing#url-rewrites)  
Header and query parameter matching | ✓[info](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-query-and-header-routing) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/routing#matching-header-query)  
Pattern (wildcard) matching | ✓[info](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#wildcards-regx-dynamic) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/routing#pattern-matching)  
Dynamic header injection—client geography, cache status, TLS version | ✓[info](https://docs.cloud.google.com/cdn/docs/caching#http-headers-cookies) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/custom-headers#header-variables)  
Built-in cross-origin resource sharing (CORS) policies |  | ✓[info](https://docs.cloud.google.com/media-cdn/docs/routing#cors)  
  
### Supported protocols

Feature | Cloud CDN | Media CDN  
---|---|---  
Global Anycast—IPv4 and IPv6 | ✓ | ✓  
HTTP/3, based on IETF QUIC | ✓ | ✓  
HTTP/2 | ✓ | ✓  
HTTP/1.1 | ✓ | ✓  
TLS 1.3 | ✓ | ✓  
Early data for TLS 1.3 | ✓[info](https://docs.cloud.google.com/cdn/docs/best-practices#tls-early-data) |   
TLS 1.2 | ✓ | ✓  
TLS 1.0 and 1.1 support for legacy devices | ✓ |   
  
### Logging and monitoring

Feature | Cloud CDN | Media CDN  
---|---|---  
Detailed request logs | ✓[info](https://docs.cloud.google.com/cdn/docs/logging) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/logging)  
Near real-time log delivery | ✓ | ✓[info](https://docs.cloud.google.com/media-cdn/docs/logging)  
Cache-hit rate reporting | ✓ | ✓  
Request and response metrics | ✓ | ✓  
[Export](https://docs.cloud.google.com/logging/docs/export#sinks) to Cloud Storage, BigQuery, or external tools | ✓ | ✓  
[Alerts](https://docs.cloud.google.com/monitoring/alerts) for supported products | ✓ | ✓  
  
### Automation and APIs

Feature | Cloud CDN | Media CDN  
---|---|---  
REST APIs | ✓[info](https://docs.cloud.google.com/cdn/docs/apis) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/reference/rest)  
Google Cloud console | ✓ | ✓  
Google Cloud CLI | ✓[info](https://docs.cloud.google.com/cdn/docs/apis) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/quickstart#gcloud)  
[Terraform](https://www.terraform.io/docs/providers/google/index.html) support | ✓[info](https://docs.cloud.google.com/cdn/docs/cdn-terraform-examples) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/quickstart#terraform)  
  
### Security

Feature | Cloud CDN | Media CDN  
---|---|---  
Managed SSL (TLS) certificates | ✓ | ✓[info](https://docs.cloud.google.com/media-cdn/docs/ssl-certificates)  
Managed SSL (TLS) certificates, no additional cost |  | ✓[info](https://docs.cloud.google.com/media-cdn/docs/ssl-certificates)  
Bring-your-own SSL (TLS) certificates, no additional cost |  | ✓[info](https://docs.cloud.google.com/media-cdn/docs/ssl-certificates)  
Customizable SSL policies—versions, ciphers | ✓[info](https://docs.cloud.google.com/load-balancing/docs/ssl-policies-concepts) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/ssl-certificates)  
Encryption at rest | ✓ | ✓  
Audit logging | ✓[info](https://docs.cloud.google.com/cdn/docs/audit-logging) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/audit-logging)  
Google Cloud Armor support  | ✓[info](https://docs.cloud.google.com/cdn/docs/overview#google-cloud-armor) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/security-policies#creating-a-policy)  
Identity and Access Management | ✓[info](https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-mig#set_up_permissions) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/configuration#permissions)  
  
### Edge computing

Feature | Cloud CDN | Media CDN  
---|---|---  
Custom code using Service Extensions plugins | ✓[info](https://docs.cloud.google.com/cdn/docs/integration-with-service-extensions) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/deploy-plugins) ([Preview](https://cloud.google.com/products/#product-launch-stages))  
  
### Content authentication

Feature | Cloud CDN | Media CDN  
---|---|---  
Signed URLs | ✓[info](https://docs.cloud.google.com/cdn/docs/using-signed-urls) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/prevent-unauthorized-distribution-overview)  
Signed cookies | ✓[info](https://docs.cloud.google.com/cdn/docs/using-signed-cookies) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/prevent-unauthorized-distribution-overview)  
Signed tokens |  | ✓[info](https://docs.cloud.google.com/media-cdn/docs/generate-tokens)  
Dual-token authentication |  | ✓[info](https://docs.cloud.google.com/media-cdn/docs/use-dual-token-authentication)  
Private origin authentication | ✓[info](https://docs.cloud.google.com/cdn/docs/configure-private-origin-authentication) | ✓[info](https://docs.cloud.google.com/media-cdn/docs/connect-to-s3-compatible-buckets)  
Support for header and IP attributes in signed requests |  | ✓[info](https://docs.cloud.google.com/media-cdn/docs/signed-requests)  
Support for HMAC-SHA1 in signed requests | ✓ | ✓  
Support for Ed25519 and HMAC-SHA-256 in signed requests |  | ✓  
  
### Compliance

Compliance standard | Cloud CDN | Media CDN  
---|---|---  
HIPAA | ✓ |   
PCI-DSS | ✓ | ✓  
SOC1, SOC2, SOC3 | ✓ | ✓  
ISO 27001, ISO 27017, ISO 27018, ISO 27701 | ✓ | ✓  
FedRAMP Moderate | ✓ |   
  
## Transition between the two products

If you already have a multi-CDN deployment with CDN steering and switching products, you can transition between them by using DNS, or configure one of them as an additional CDN.

[Cloud DNS server policies](https://docs.cloud.google.com/dns/docs/policies) might be an option for routing traffic between CDNs or transitioning from one CDN to the other.

## Use a multi-CDN strategy

To optimize performance and lower costs, you can use Cloud CDN and Media CDN with each other or with other CDNs by implementing multi-CDN deployment strategies.

Multi-CDN strategies, where your content is hosted with more than one CDN provider, can help you optimize CDN services by region and CDN capabilities offered by different providers. They can also be useful if you host high-traffic events and need to distribute traffic to multiple providers. In the case of micro-outages with one provider, you can quickly shift traffic to another CDN provider.

A CDN deployment with a primary CDN and a secondary CDN is an example of a multi-CDN deployment strategy. The primary CDN serves the majority of traffic, and the secondary serves a minority. If there are issues with the primary CDN, users can direct traffic to the secondary CDN as a failover strategy and not have to wait the usual period for the cache to get hot while already serving content.

To get started, route traffic to each CDN or split a portion of your existing traffic to a new CDN using [DNS server policies](https://docs.cloud.google.com/dns/docs/policies) or similar traffic redirection services.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
