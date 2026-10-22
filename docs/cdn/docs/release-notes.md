---
url: https://docs.cloud.google.com/cdn/docs/release-notes/
title: Cloud CDN release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:45.473122+00:00
---

# Cloud CDN release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Resources ](https://docs.cloud.google.com/cdn/docs/resources)



Send feedback 

#  Cloud CDN release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for features and updates to Cloud CDN. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/cloudcdn-release-notes.xml) directly. 

## August 19, 2026

Feature

[Global Front End](https://docs.cloud.google.com/docs/networking/cross-cloud-network/global-front-end/gfee-overview) is a unified offering that simplifies billing by consolidating pricing across networking products, including Cloud CDN, global external Application Load Balancer, Google Cloud Armor, and Service Extensions, into one solution to help deliver, scale, and secure your internet-facing applications. Cloud CDN is included in the Global Front End Enterprise billing tier. This feature is available in **Preview**.

For more information, see [Global Front End](https://docs.cloud.google.com/cdn/docs/overview#cdn_with_globalfrontend).

## August 17, 2026

Feature

Cloud CDN supports the targeted `CDN-Cache-Control` HTTP response header [RFC 9213](https://www.rfc-editor.org/rfc/rfc9213). You can use this header to specify caching directives specifically for Cloud CDN edge caches without affecting browser-level caching.

For details, see [Cache control header precedence](https://docs.cloud.google.com/cdn/docs/caching#cache-control-headers).

## August 04, 2026

Feature

Cloud CDN supports native image optimization at the Google network edge for global external Application Load Balancers. This feature offloads compute-intensive image transformations, such as resizing, cropping, and format conversion to reduce origin server load and egress costs. This feature is in **Preview**.

**Note:** During the Preview phase, image optimization is available free of charge. Charges will apply once it becomes Generally Available (GA).

For more information, see [Optimize images with Cloud CDN](https://docs.cloud.google.com/cdn/docs/imageoptimization).

## July 03, 2026

Feature

Cloud CDN and external Application Load Balancers support self-service Private Bucket Access for Cloud Storage buckets. This feature allows you to securely serve content without making your storage buckets public. The access on the buckets is managed securely via IAM permissions on a Google-managed service account. This feature is **Generally Available**.

For more information, see [Private bucket access](https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-bucket#enable_private_bucket_access).

## May 26, 2026

Feature

For [global external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt#cdn-cache-policy), you can configure Cloud CDN cache policies at various levels of a URL map, providing more granular control over caching. You can now apply specific caching logic based on hostnames, URL paths, HTTP headers, and query parameters. This feature is **Generally Available**.

For more information, see [Cache policies in URL maps](https://docs.cloud.google.com/cdn/docs/caching#cache-policies-url-maps).

## April 30, 2026

Feature

Google Kubernetes Engine (GKE) Gateway supports Cloud CDN to help you cache content closer to your users, improve application latency, and reduce origin load. Using GKE Gateway APIs, you can configure, manage, and fine-tune caching configurations for different segments of your traffic. This feature is **Generally Available**.

For more information, see [Configure Cloud CDN for Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-cdn-for-gateway).

## April 13, 2026

Feature

Google Kubernetes Engine (GKE) Gateway supports Cloud CDN to help you cache content closer to your users, improve application latency, and reduce origin load. Using GKE Gateway APIs, you can configure, manage, and fine-tune caching configurations for different segments of your traffic. This feature is in **Preview**.

For more information, see [Configure Cloud CDN for Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/configure-cdn-for-gateway).

## March 30, 2026

Feature

For [global external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt#cdn-cache-policy), you can configure Cloud CDN cache policies at various levels of a URL map, providing more granular control over caching. You can now apply specific caching logic based on hostnames, URL paths, HTTP headers, and query parameters. This feature is in **Preview**.

For more information, see [Cache policies in URL maps](https://docs.cloud.google.com/cdn/docs/caching#cache-policies-url-maps).

## November 13, 2025

Feature

Cloud CDN lets you [add custom code to the request processing path](https://docs.cloud.google.com/cdn/docs/integration-with-service-extensions) of global external Application Load Balancers by using Service Extensions edge extensions (pre-cache) and traffic extensions (post-cache). These extensions help you manipulate request headers early in the processing lifecycle to influence caching and routing decisions. This feature is in **General Availability**.

## October 07, 2025

Feature

Cloud CDN provides predefined dashboards that are enabled by default for a quick insight into system health and performance. These dashboards display key metrics that enable you to monitor traffic distribution and cache effectiveness without manual configuration. This feature is **Generally Available**.

For more information, see [Predefined dashboards](https://docs.cloud.google.com/cdn/docs/logging#predefined-cdn-dashboards).

## June 23, 2025

Feature

Cloud CDN lets you add custom code to the request processing path of global external Application Load Balancers by using Service Extensions edge extensions. These extensions help you implement customizations in the request path pre-cache, which can influence how content is cached and the backend service is selected on the Application Load Balancer. This feature is in **Preview**.

For more information, see [Use Service Extensions for edge computing](https://docs.cloud.google.com/cdn/docs/integration-with-service-extensions).

## May 19, 2025

Feature

Cloud CDN supports [content targeting](https://docs.cloud.google.com/cdn/docs/caching#using-custom-variables), which helps you cache and deliver assets that are customized for your end-user contexts. It enables device characterization and geo-targeting, which are useful for implementing responsive websites, language customization, and currency settings. This feature is now [Generally Available](https://cloud.google.com/products/#general-availability).

## May 05, 2025

Feature

Invalidation using cache tags is [Generally Available](https://cloud.google.com/products/#general-availability). 

Cloud CDN now also offers faster performance and higher rate limits for invalidation requests using all invalidation matchers. For more information, see [Cache validation overview](https://docs.cloud.google.com/cdn/docs/cache-invalidation-overview).

## February 18, 2025

Feature

External HTTP(S) Load Balancing and Cloud CDN support [early data for TLS 1.3](https://docs.cloud.google.com/cdn/docs/best-practices#tls-early-data), also known as 0-RTT or zero round trip. Early data helps clients include HTTP request data with a TLS handshake, which can improve web performance for resumed connections.

## February 13, 2025

Feature

Cloud CDN supports [invalidation by using cache tags](https://docs.cloud.google.com/cdn/docs/cache-invalidation-overview#cache-tags) with faster performance and higher rate limits in **Preview**. By grouping objects together using cache tags, you can remove and refresh content at scale.

## October 31, 2024

Feature

You can also use the Google Cloud Console to enable [private origin authentication](https://docs.cloud.google.com/cdn/docs/configure-private-origin-authentication) for Amazon Simple Storage Service (Amazon S3) and compatible object stores.

## September 14, 2023

Feature

The Cloud CDN [private origin authentication](https://docs.cloud.google.com/cdn/docs/configure-private-origin-authentication) capability for Amazon Simple Storage Service (Amazon S3) and compatible object stores is now [Generally Available](https://cloud.google.com/products/#general-availability).

## May 30, 2023

Feature

The advanced traffic management using flexible pattern matching capability with Global External HTTP(S) Load Balancer is now [Generally Available](https://cloud.google.com/products/#general-availability).

## January 31, 2023

Feature

Cloud CDN supports advanced traffic management using flexible pattern matching with Global External HTTP(S) Load Balancer. This capability allows you to use wildcards anywhere in your path matcher and customize origin routing for different types of traffic and request and response behaviors. In addition, you can use results from your pattern matching to rewrite the path that's sent to the origin. This feature is in **Preview**.

## January 17, 2023

Feature

Cloud CDN supports [private origin authentication](https://docs.cloud.google.com/cdn/docs/configure-private-origin-authentication) for Amazon Simple Storage Service (Amazon S3) and compatible object stores. This capability improves security by allowing only trusted connections to access the content on your private origins and preventing users from directly accessing it. This feature is supported in **Preview**.

## September 20, 2022

Feature

Cloud CDN support for dynamic compression is now [Generally Available](https://cloud.google.com/products#product-launch-stages). Cloud CDN supports dynamic compression using Brotli and gzip algorithms, which can reduce data sent over the network by 60-80% for compressible content. Enabling dynamic compression can help you achieve faster page load times, speed up playback speed for video content, and optimize egress costs. For more information, see [Dynamic Compression](https://docs.cloud.google.com/cdn/docs/dynamic-compression).

## February 16, 2022

Feature

[Dynamic compression](https://docs.cloud.google.com/cdn/docs/dynamic-compression) allows Cloud CDN to automatically compress responses as they are being served between the origin and the client. The size of the data sent over the network is reduced by [60% to 85% in typical cases](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/optimize-encoding-and-transfer#text_compression_with_gzip). This feature is supported in **Preview**.

## January 28, 2022

Feature

Cloud CDN support for custom named cookies and headers in the cache key are [Generally Available](https://cloud.google.com/products/#general-availability). You can use these features for A/B (multivariate) testing, canary testing, and similar scenarios. Allowlisting of query parameters is now also enabled for backend buckets, to allow for cache busting.

For details, see the [caching documentation](https://docs.cloud.google.com/cdn/docs/caching#cache-keys).

## September 22, 2021

Feature

Cloud CDN now supports custom named cookies and headers in the cache key, to enable A/B (multivariate) testing, canarying, and similar scenarios. Allowlisting of query parameters is now also enabled for backend buckets, to allow for cache busting. These features are available in **Preview**.

For details, see the [caching documentation](https://docs.cloud.google.com/cdn/docs/caching#cache-keys).

## July 19, 2021

Change

Cloud CDN now treats HTTP responses with a **max-age** or **s-maxage** directive as cacheable, even if those responses do not have a **Cache-Control: public** directive.

This allows Cloud CDN to cache additional responses and better align with HTTP standards.

For details, see the [caching documentation](https://docs.cloud.google.com/cdn/docs/caching#cache_control_directives).

## June 22, 2021

Feature

External HTTP(S) Load Balancing and Cloud CDN now support HTTP/3. HTTP/3 is based on the IETF QUIC transport protocol. Compared to HTTP/2, it reduces request latency, improves throughput, and mitigates head-of-line blocking. HTTP/3 is already supported on most major web browsers.

To learn how to enable HTTP/3 on your external HTTP(S) load balancer, [visit the documentation](https://docs.cloud.google.com/load-balancing/docs/https#QUIC).

## April 07, 2021

Announcement

[Serve stale](https://docs.cloud.google.com/cdn/docs/serving-stale-content), [bypassing cache](https://docs.cloud.google.com/cdn/docs/caching#bypassing-cache), and [negative caching](https://docs.cloud.google.com/cdn/docs/using-negative-caching) are now **Generally Available**. 

These features are available when configuring Cloud CDN enabled backend services and backend buckets in the Cloud Console, in addition to the gcloud SDK and REST API.

Feature

Cloud CDN now supports [configuring negative caching](https://docs.cloud.google.com/cdn/docs/using-negative-caching#status-code-default-ttl) for HTTP 302 (Found) and HTTP 307 (Temporary Redirect) status codes.

To learn how to enable negative caching for these status codes, [visit the documentation](https://docs.cloud.google.com/cdn/docs/using-negative-caching#negative-caching).

## April 02, 2021

Change

Cloud CDN now treats HTTP responses with a valid, future date in the `Expires` header as cacheable, even if those responses do not have a `Cache-Control: public` directive.

This will allow Cloud CDN to cache additional responses and better align with HTTP standards.

Review the [caching documentation](https://docs.cloud.google.com/cdn/docs/caching#cache_control_directives) for details on what content Cloud CDN considers cacheable vs. uncacheable.

## March 29, 2021

Change

Cloud CDN now treats the `no-cache` Cache-Control directive in a response as per [RFC 7234](https://tools.ietf.org/html/rfc7234#section-5.2.2) and allows these responses to be cached, provided that they are validated every time before being reused.

Visit the [caching documentation](https://docs.cloud.google.com/cdn/docs/caching#cache_control_directives) to review how Cloud CDN handles the full set of HTTP caching directives.

## March 28, 2021

Security

Cloud CDN, external HTTP(S) Load Balancing and Cloud Storage customers are not affected by the [recent OpenSSL security advisory](https://www.openssl.org/news/secadv/20210325.txt) that relates to CA certificate checks (CVE-2021-3450) and TLS renegotiation (CVE-2021-3449).

These services use [BoringSSL](https://boringssl.googlesource.com/boringssl/) and are not affected by these OpenSSL-specific bugs.

## March 22, 2021

Announcement

Cloud CDN now defaults to the [Cache All Static](https://docs.cloud.google.com/cdn/docs/caching#cache-modes) cache mode for newly created backend buckets and backend services, which allows Cloud CDN to cache [static content](https://docs.cloud.google.com/cdn/docs/caching#static) more readily.

The Cache All Static cache mode caches positive responses with [valid caching directives](https://docs.cloud.google.com/cdn/docs/caching#cacheability), and will default to caching static content (videos, images, and web assets) for 1 hour. Responses that set a `no-store`, `private`, or `no-cache` cache directive will not be cached.

Existing backends remain unchanged and default to the [Use Origin Headers](https://docs.cloud.google.com/cdn/docs/caching#cache-modes) cache mode.

Change

[Request coalescing](https://docs.cloud.google.com/cdn/docs/caching#request-coalescing) (or _collapsing_) is now enabled by default on all backend services and backend buckets.

Customers with a high number of requests to cached resources that are updated often, or live streaming workloads, should see a notable reduction in bandwidth from, and requests to, their origin(s).

## March 05, 2021

Announcement

Support for [item request coalescing](https://docs.cloud.google.com/cdn/docs/caching#request-coalescing) is now **Generally Available**. 

Item request coalescing allows multiple requests for a small object to be coalesced (collapsed) into a single origin request for the same cache key into a single origin request per edge node.

This enhances Cloud CDN's existing request coalescing behaviour for large objects, such as video and file downloads.

To enable request coalescing for your Cloud CDN enabled backends, [visit the documentation](https://docs.cloud.google.com/cdn/docs/caching#request-coalescing).

## January 31, 2021

Feature

Cloud CDN now supports [serving stale content](https://docs.cloud.google.com/cdn/docs/serving-stale-content) and the ability to [bypass the cache](https://docs.cloud.google.com/cdn/docs/caching#bypassing-cache) based on request header(s).

Serving stale content lets Google's global cache continue to serve content to users when your origin server is unreachable or is returning errors to Cloud CDN. You can configure how long Cloud CDN will serve content beyond expiry by setting the `serveWhileStale` value for each backend service or bucket.

These features are available when configuring Cloud CDN enabled backend services and backend buckets in the Cloud Console, in addition to the [gcloud SDK](https://docs.cloud.google.com/sdk/docs/install) and REST API.

These features are available in **Preview** .

## December 14, 2020

Change

[Cache modes](https://docs.cloud.google.com/cdn/docs/using-cache-modes), [TTL overrides](https://docs.cloud.google.com/cdn/docs/using-ttl-overrides) and [custom response headers](https://docs.cloud.google.com/load-balancing/docs/custom-headers) are now supported on backend buckets and backend services, and are now **Generally Available**.

Cache modes allow Cloud CDN to automatically cache static content types, including web assets like CSS, JavaScript and fonts, as well as image and video content.

TTL overrides support fine-tuning how long Cloud CDN caches your responses, and custom response headers introduce a new {cdn_cache_status} variable that is populated with the cache status response.

The Google [Terraform provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs) also supports these latest Cloud CDN features, including cache modes, TTL overrides, and custom response headers. Refer [the documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_backend_bucket) for `compute_backend_bucket` and `compute_backend_service` for how to configure and use the new features with Terraform.

## December 08, 2020

Feature

The Google [Terraform provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs) now supports the latest Cloud CDN features, including [cache modes](https://docs.cloud.google.com/cdn/docs/using-cache-modes), TTL overrides, and custom response headers.

Refer to [the documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_backend_bucket) for the `compute_backend_bucket` and `compute_backend_service` for how to configure and use the new features with Terraform.

## November 04, 2020

Announcement

Added a new tutorial for configuring Cloud CDN with a serverless app: [Setting up Cloud CDN with Cloud Run, Cloud Functions, or App Engine](https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-serverless)

## November 02, 2020

Feature

You can now configure [cache modes](https://docs.cloud.google.com/cdn/docs/using-cache-modes#console), [cache TTLs](https://docs.cloud.google.com/cdn/docs/using-ttl-overrides#console) and set [custom response headers](https://docs.cloud.google.com/load-balancing/docs/custom-headers) in the Cloud Console, in addition to the existing gcloud and REST API support.

## October 27, 2020

Change

Added a new tutorial: [Setting up an HTTP-to-HTTPS redirect](https://docs.cloud.google.com/cdn/docs/setting-up-http-https-redirect)

## October 26, 2020

Feature

Cloud CDN can now cache more response codes, including common error codes such as 404 (Not Found), 301 (Permanent Redirect), 302 (Temporary Redirect), and [many others](https://docs.cloud.google.com/cdn/docs/caching?hl=en#cacheability).

If you are sending [valid cache directives](https://docs.cloud.google.com/cdn/docs/caching?hl=en#cacheability) from your origin, you do not need to make any changes to benefit from this.

You can also set (and override) per-status code TTLs by [configuring negative caching](https://docs.cloud.google.com/cdn/docs/using-negative-caching) as of [gcloud SDK 316.0.0](https://docs.cloud.google.com/sdk/docs/release-notes#31600_2020-10-27).

## October 01, 2020

Change

Added a new [tutorial for delivering HTTP and HTTPS content over the same hostname when using Cloud CDN](https://docs.cloud.google.com/cdn/docs/http-https-over-same-domain). While many browsers enforce the use of Transport Layer Security (TLS) and disallow non-secure content delivery, there are still use cases where non-secure delivery and secure delivery must be allowed over the same hostname.

## September 29, 2020

Feature

Improvements to Cloud CDN's request collapsing behavior: If your deployment serves large objects, these improvements reduce origin load during revalidation and cache fill. Live video workloads will see the largest benefit. For more information, see [Support for byte range requests](https://docs.cloud.google.com/cdn/docs/caching?hl=en#byte-range-requests).

## September 14, 2020

Feature

[Cache Modes](https://docs.cloud.google.com/cdn/docs/using-cache-modes), [TTL overrides](https://docs.cloud.google.com/cdn/docs/using-ttl-overrides) and [custom response headers](https://docs.cloud.google.com/load-balancing/docs/custom-headers) are now supported on backend buckets and backend services, and are available in [beta](https://cloud.google.com/products/#product-launch-stages).

Cache modes allow Cloud CDN to automatically cache [static content types](https://docs.cloud.google.com/cdn/docs/caching#static), including web assets like CSS, JavaScript and fonts, as well as image and video content.

TTL overrides support fine-tuning how long Cloud CDN caches your responses, and custom response headers introduce a new `{cdn_cache_status}` variable that is populated with the cache status response.

Feature

External HTTP(S) Load Balancing now supports setting [custom response headers](https://docs.cloud.google.com/load-balancing/docs/custom-headers) on backend buckets and services. This feature is available in [beta](https://cloud.google.com/products/#product-launch-stages).

Custom response headers make it easier to set common web security headers and/or override response headers from your application at the load balancer.

## September 09, 2020

Change

Added a new tutorial: [Faster web performance and improved web protection for load balancing](https://docs.cloud.google.com/load-balancing/docs/tutorials/faster-performance-improved-protection).

## September 02, 2020

Change

Reduced [cache fill pricing](https://cloud.google.com/cdn/pricing#cache-fill) from Cloud Storage, Compute Engine, and external origins by up to 80% starting September 1st.

Google Cloud has also removed cache-to-cache fill and cache invalidation charges.

## July 13, 2020

Change

Added a new [setup guide](https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-external-origin) for custom (external) origins with Cloud CDN and external HTTP(S) Load Balancing.

## June 10, 2020

Feature

HTTP(S) Load Balancing with [Cloud CDN logging](https://docs.cloud.google.com/cdn/docs/logging) is available in **General Availability**.

## May 29, 2020

Change

To help you get started quickly, added two new examples for setting up Cloud CDN:

  * [Setting up Cloud CDN with a managed instance group](https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-mig)
  * [Setting up Cloud CDN with a backend bucket](https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-bucket)



## May 01, 2020

Change

Added a new [Features page](https://docs.cloud.google.com/cdn/docs/features) that summarizes all Cloud CDN capabilities.

## April 17, 2020

Feature

Cloud CDN [request logs](https://docs.cloud.google.com/cdn/docs/logging) now include a `cacheId` field, which captures the location and cache node the client connected to. A `cacheId` of `LHR-1209ea83` indicates a client connected to an edge cache near London, with `1209ea83` representing the opaque ID of the cache instance their response was served from.

Location codes map to ⁠[IATA codes](https://en.wikipedia.org/wiki/IATA_airport_code). The `cacheId` field can be found within the `jsonPayload` object in each log entry.

## April 15, 2020

Feature

[Signed Cookies](https://docs.cloud.google.com/cdn/docs/using-signed-cookies) are available in **General Availability**. Signed Cookies complement our existing [Signed URLs](https://docs.cloud.google.com/cdn/docs/using-signed-urls) functionality by allowing you to sign a URL prefix and issue a cookie to a client, avoiding the need to sign content on a per-URL basis when protecting media or other content cached by Cloud CDN. Support for authorizing a URL prefix is extended to Signed URLs as an alternative signing scheme.

## April 09, 2020

Feature

TLS v1.3 is now enabled by default for all external HTTPS load balancers, SSL proxy load balancers, and Cloud CDN. Note that this change doesn't apply to internal HTTPS load balancers or Traffic Director. 

TLS v1.3 supports modern ciphers with forward-secrecy as a baseline and, critically, reduces the number of round trips required to establish a TLS session, which directly improves performance seen by your end-users.

Clients that support TLS v1.3 include Chrome, Chromium-based browsers, and Android. These clients automatically negotiate TLS v1.3 without requiring any changes. Clients that do not support TLS v1.3 are unaffected.

## March 25, 2020

Feature

Cloud CDN [custom origins](https://docs.cloud.google.com/cdn/docs/custom-origins-overview) is available in **General Availability**. You can now use Cloud CDN's distributed edge caching infrastructure to connect to an origin hosted outside of GCP, such as on-premises or in another cloud.

## February 10, 2020

Feature

Cloud CDN [custom origins](https://docs.cloud.google.com/cdn/docs/custom-origins-overview) support is available in **Beta**. This feature lets you deliver content over Google's high performance, distributed edge caching infrastructure when the content is hosted on-premises or in another cloud.

## August 01, 2018

Feature

[Cloud CDN Large Object Caching](https://docs.cloud.google.com/cdn/docs/caching#maximum-size) support is available in **General Availability**. This feature allows Cloud CDN to cache objects up to 5 TB in size.

## June 26, 2018

Feature

[Cloud CDN Signed URLs](https://docs.cloud.google.com/cdn/docs/using-signed-urls) support is available in **General Availability**. This feature allows you to serve responses from Google Cloud Platform's globally distributed caches even when you need requests to be authorized.

## May 01, 2018

Feature

[Cloud CDN Signed URLs](https://docs.cloud.google.com/cdn/docs/using-signed-urls) support is available in **Beta**. This feature allows you to serve responses from Google Cloud Platform's globally distributed caches even when you need requests to be authorized.

## April 04, 2018

Feature

[Cloud CDN Large Object Caching](https://docs.cloud.google.com/cdn/docs/caching#maximum-size) support is available in **Beta**. This feature allows Cloud CDN to cache objects up to 5 TB in size.

## April 19, 2017

Feature

[Cloud CDN Custom Cache Keys](https://docs.cloud.google.com/cdn/docs/using-cache-keys) support is available in **General Availability**.

## March 22, 2017

Feature

[Cloud CDN](https://docs.cloud.google.com/cdn/docs) support for [Google Cloud Storage with HTTP(S) Load Balancing](https://docs.cloud.google.com/load-balancing/docs/https/adding-a-backend-bucket-to-content-based-load-balancing) is available in **General Availability**.

## March 15, 2017

Feature

[Cloud CDN Custom Cache Keys](https://docs.cloud.google.com/cdn/docs/using-cache-keys) support is available in **Beta**.

## February 01, 2017

Feature

[Cloud CDN](https://docs.cloud.google.com/cdn/docs) support for [Google Cloud Storage with HTTP(S) Load Balancing](https://docs.cloud.google.com/load-balancing/docs/https/adding-a-backend-bucket-to-content-based-load-balancing) is available in **Beta**.

## January 19, 2017

Feature

Support for [cache invalidation for a single host](https://docs.cloud.google.com/cdn/docs/cache-invalidation-overview#invalidating_the_cache_for_a_single_host) is available in **General Availability**.

## June 27, 2016

Feature

[Cloud CDN](https://docs.cloud.google.com/cdn/docs) is available in **General Availability**.

## April 13, 2016

Feature

[Cloud CDN](https://docs.cloud.google.com/cdn/docs) is available in **Beta**.

## November 11, 2015

Feature

[Cloud CDN](https://docs.cloud.google.com/cdn/docs) is available in **Alpha**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
