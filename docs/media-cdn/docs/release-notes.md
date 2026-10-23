---
url: https://docs.cloud.google.com/media-cdn/docs/release-notes/
title: Media CDN release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:39:34.360491+00:00
---

# Media CDN release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Resources ](https://docs.cloud.google.com/media-cdn/docs/resources)



Send feedback 

#  Media CDN release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for features and updates to Media CDN. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/mediacdn-release-notes.xml) directly. 

## June 12, 2026

Feature

The maximum cacheable object size for Media CDN can be increased up to 1 TiB. To request a limit increase for your project, contact your Google support representative. This feature is **Generally Available**.

For more information, see [Quotas and limits](https://docs.cloud.google.com/media-cdn/quotas).

Feature

Media CDN lets you identify the country codes of the edge caches serving client requests. This feature is **Generally Available**.

For more information, see [Custom headers](https://docs.cloud.google.com/media-cdn/docs/custom-headers#header-variables).

## December 17, 2025

Feature

Media CDN no longer requires a `HEAD` request before fetching objects from your origin. This enhancement streamlines content delivery, reduces overhead, and improves overall performance. See [origin requirements](https://docs.cloud.google.com/media-cdn/docs/caching#origin-requirements).

**Note:** This feature is available globally, except in India for now. In India, Media CDN continues to require both `HEAD` and `GET` requests.

## December 05, 2025

Feature

Media CDN supports multipart range requests, which enable users to request multiple non-contiguous segments of a file in a single HTTP request. This feature is **Generally Available**.

For more information, see [Multipart range requests](https://docs.cloud.google.com/media-cdn/docs/caching#multipart-range-requests).

## November 03, 2025

Feature

Media CDN supports flexible shielding. You can specify a single geographic region for origin shielding. This way, cache fills route through this configured region, offering a more efficient configuration for centralized origins than the default user-location-based approach. This feature is **Generally Available**.

For more information, see [flexible shielding](https://docs.cloud.google.com/media-cdn/docs/origins#flex-shielding).

## October 10, 2025

Feature

Media CDN supports multipart range requests, which enable users to request multiple non-contiguous segments of a file in a single HTTP request. This feature is in **Preview**.

For more information, see [Multipart range requests](https://docs.cloud.google.com/media-cdn/docs/caching#multipart-range-requests).

## September 24, 2025

Feature

You can use Autonomous System Numbers (ASN) based rules from Cloud Armor for Media CDN. ASN-based rules allow you to create security policies that specifically permit or deny traffic based on the ASN of the client requesting your content. This feature is **Generally Available**.

For more information, see [Google Cloud Armor support](https://docs.cloud.google.com/media-cdn/docs/overview#armor-support).

Feature

You can use Network Threat Intelligence (NTI) from Cloud Armor in Edge Security Policies for Media CDN edge cache services for Enterprise users. NTI helps identify and block requests originating from known malicious IP addresses and networks. This feature is **Generally Available**.

For an example, see [Example: Block traffic from known malicious IPs](https://cloud.google.com/media-cdn/docs/security-policies#example-block-malicious-using-NTI).

For more information, see [Google Cloud Armor support](https://docs.cloud.google.com/media-cdn/docs/overview#armor-support).

## August 08, 2025

Feature

You can use Autonomous System Numbers (ASN) based rules from Cloud Armor for Media CDN. ASN-based rules allow you to create security policies that specifically permit or deny traffic based on the ASN of the client requesting your content. This feature is in **Preview**. 

For more information, see [Google Cloud Armor support](https://docs.cloud.google.com/media-cdn/docs/overview#armor-support).

## June 30, 2025

Announcement

Media CDN supports a dedicated range of IPs for requests to external origin servers. [IP allowlisting](https://cloud.google.com/media-cdn/docs/origins#allow-ip) at the origin helps you restrict access to your content by only allowing traffic from Media CDN's IP addresses. This capability is **Generally Available**.

## June 25, 2025

Feature

Media CDN supports flexible shielding. You can specify a single geographic region for origin shielding. This way, cache fills route through this configured region, which offers a more efficient configuration for centralized origins than the default user-location-based approach. This feature is in **Preview**.

For more information, see [Flexible shielding](https://docs.cloud.google.com/media-cdn/docs/origins#flex-shielding).

## June 18, 2025

Feature

You can use Network Threat Intelligence (NTI) from Cloud Armor in Edge Security Policies for Media CDN edge cache services for Enterprise users. NTI helps identify and block requests originating from known malicious IP addresses and networks. This feature is in **Preview**.

For an example, see [Example: Block traffic from known malicious IPs](https://cloud.google.com/media-cdn/docs/security-policies#example-block-malicious-using-NTI).

## March 24, 2025

Feature

Media CDN supports [dynamic compression](https://docs.cloud.google.com/media-cdn/docs/dynamic-compression) in **General Availability**.

## January 06, 2025

Feature

In **Preview** , Media CDN supports dynamic compression for compressible content by using Brotli and gzip algorithms. Enabling dynamic compression can help you achieve faster page load times, speed up playback speed for video content, and optimize egress costs. For more information, see [Enable dynamic compression](https://docs.cloud.google.com/media-cdn/docs/dynamic-compression).

## September 16, 2024

Feature

[HTTP method filtering](https://docs.cloud.google.com/media-cdn/docs/routing#method-filtering) for specific route rules is now **Generally Available**. You can now also implement such filtering by using the GUI.

## June 25, 2024

Feature

Globally scoped Cloud Armor edge security policies for Layer 7 filtering are now Generally Available. For an example, see [Example: Deny requests for cached content with specific headers](https://docs.cloud.google.com/media-cdn/docs/security-policies#example-deny-incoming-requests-with-specific-header-content).

## June 04, 2024

Feature

By default, Media CDN proxies only `GET`, `HEAD`, and `OPTIONS` methods to your origin and filters out the methods that can modify your origin. In **Preview** , you can [override this default behavior for a specific route rule](https://docs.cloud.google.com/media-cdn/docs/routing#method-filtering) by specifying other supported methods that you would like proxied to your origin.

## May 24, 2024

Feature

You can use the globally scoped edge security policies of Cloud Armor for Layer 7 filtering. This feature is in **Preview**. For an example, see [Example: Deny requests for cached content with specific headers](https://docs.cloud.google.com/media-cdn/docs/security-policies#example-deny-incoming-requests-with-specific-header-content).

Feature

[Dual-token authentication](https://docs.cloud.google.com/media-cdn/docs/use-dual-token-authentication) is Generally Available. You can now enable this feature by using the Google Cloud Console in addition to the gcloud SDK and REST API. When this feature is enabled, Media CDN uses a short-duration token and a long-duration token to authenticate requests.

## May 13, 2024

Feature

Media CDN supports [content targeting](https://docs.cloud.google.com/media-cdn/docs/custom-headers#header-variables), which helps you cache and deliver assets that are customized for your end-user contexts. It enables device characterization and geo-targeting, which are useful for implementing responsive websites, language customization, and currency settings.

## December 06, 2023

Feature

The Media CDN capability to [use a private S3-compatible bucket as an origin](https://docs.cloud.google.com/media-cdn/docs/connect-to-s3-compatible-buckets) is now Generally Available. You can also use the GUI to configure such origins.

## January 31, 2023

Feature

The following Media CDN features are now Generally Available: 

  * Configuring Media CDN to follow origin redirects 
  * Manipulating headers on a per-origin basis



For more information, see [Failover and timeouts](https://docs.cloud.google.com/media-cdn/docs/origins#failover-and-timeouts) and [Example: Failover with redirect following](https://docs.cloud.google.com/media-cdn/docs/origins#failover-with-redirect-following).

## October 28, 2022

Feature

Media CDN now lets you add custom code to the request-response processing path by using Service Extensions plugins in **Preview**. Such customization unlocks a wide variety of lightweight use cases, such as header normalization and custom tokenization.

For more information, see [Deploy Service Extensions plugins in Media CDN routes](https://docs.cloud.google.com/media-cdn/docs/deploy-plugins).

## October 06, 2022

Feature

Media CDN now supports origin redirect following and origin header overrides in [Preview](https://cloud.google.com/products#product-launch-stages).

You can improve performance and caching for frequent redirection by configuring origin redirect following in Media CDN. When configured, Media CDN follows origin redirect responses and caches the final retrieved object. For more information, see [Configure following origin redirects](https://docs.cloud.google.com/media-cdn/docs/origins#configure-following-origin-redirects).

You can also configure Media CDN to manipulate headers on a per-origin basis, which supports distinct host rewrites and static authorization headers for failover origins. For more information, see [Failover and timeouts](https://docs.cloud.google.com/media-cdn/docs/origins#failover-and-timeouts) and [Example: Failover with redirect following](https://docs.cloud.google.com/media-cdn/docs/origins#failover-with-redirect-following).

## September 13, 2022

Feature

Media CDN now supports token-based client authentication and private external origin authentication for enhanced content protection and improved interoperability with multi-CDN and multi-cloud architectures in [Preview](https://cloud.google.com/products#product-launch-stages).

Token-based authentication enables signing arbitrary data (like custom user identifiers), HMAC-based cryptography, and dual token exchange for token propagation through the duration of a playback session. For more information, see [Prevent unauthorized distribution](https://docs.cloud.google.com/media-cdn/docs/prevent-unauthorized-distribution-overview).

Private external origin authentication allows Media CDN to support [private S3-compatible origins](https://docs.cloud.google.com/media-cdn/docs/connect-to-s3-compatible-buckets) by dynamically generating signed requests with AWS Signature Version 4.

## August 12, 2022

Feature

Media CDN now supports native logging and metrics for Common Media Client Data (CMCD) information that is transmitted through HTTP request headers or query parameters. CMCD provides visibility into the quality of service and experience for your end viewers. 

For more information, see the CMCD row in [Cache-specific logging fields](https://docs.cloud.google.com/media-cdn/docs/logging#cache-fields) and [Media CDN metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-edgecache).

## March 21, 2022

Announcement

Cloud Media Edge is now [Media CDN](https://docs.cloud.google.com/media-cdn/docs).

## November 09, 2021

Announcement

[Cloud Media Edge](https://docs.cloud.google.com/media-edge) is available in **General Availability**.

## June 30, 2021

Feature

Cloud Media Edge now supports host, path, and tag based cache invalidation.

Cache tags allow you to invalidate the cache based on status codes, MIME type (`Content-Type`), and the origin the content was originally fetched from.

To learn how to use the `gcloud` SDK and REST API to invalidate cached responses, see the [cache invalidation documentation](https://docs.cloud.google.com/media-edge/docs/cache-invalidation).

## June 25, 2021

Feature

Cloud Media Edge services now support the ability to match and rewrite incoming requests using pattern matching. 

Pattern matching (or "wildcard matching") allows you to configure match rules with wildcard operators anywhere within a URL with `pathTemplateMatch`, capture path components, and rewrite URLs with `pathTemplateRewrite` before the request is sent to your origin.

Visit the [pattern matching documentation](https://docs.cloud.google.com/media-edge/docs/routing#pattern-matching) to learn the pattern matching syntax, and see the [suffix-matching example](https://docs.cloud.google.com/media-edge/docs/routing#example_matching_on_a_file_extension) for how to match on file extensions.

## June 16, 2021

Feature

Cloud Media Edge now supports connecting to private (non-public) Cloud Storage buckets. This allows you to restrict direct access to a storage bucket and/or only serve objects via your Media Edge services.

To learn how to configure private Cloud Storage access, [visit the documentation](https://docs.cloud.google.com/media-edge/docs/origins#private-storage-buckets).

## February 10, 2021

Announcement

Initial release of [Cloud Media Edge](https://docs.cloud.google.com/media-edge). This product is in **Private Preview**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
