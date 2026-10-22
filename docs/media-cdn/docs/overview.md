---
url: https://docs.cloud.google.com/media-cdn/docs/overview/
title: Media CDN overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:52.589276+00:00
---

# Media CDN overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Media CDN overview Stay organized with collections  Save and categorize content based on your preferences. 

Media CDN is Google Cloud's media delivery solution. Media CDN complements [Cloud CDN](https://docs.cloud.google.com/cdn), which is Google Cloud's web acceleration solution. Media CDN is optimized for high-throughput egress workloads, such as streaming video and large file downloads.

An edge cache is typically server infrastructure that stores content closer to end users, located within points of presence (PoPs) or partner ISPs. Media CDN uses Google's global edge-caching infrastructure to serve your content as close to your users as possible. By using Google's infrastructure to serve content, you can reduce load on your origin infrastructure.

Media CDN lets you fetch content from publicly accessible HTTP endpoints. You can use Media CDN with your existing origin infrastructure, whether the content is hosted within Cloud Storage, in another cloud, or within your on-premises infrastructure.

You can control how content is cached for each URI you serve in a _route_. Using a route lets you optimize behavior based on the type of content, client attributes, and your freshness requirements for each route you define with Media CDN.

For guidance on which CDN product to use, see [Choose a CDN product](https://docs.cloud.google.com/media-cdn/docs/choose-cdn-product). You can use both products if they both meet your needs.

## How Media CDN works

Media CDN has three major components:

  * A router
  * A cache
  * A cache filler



Conceptually, the components are connected as depicted in the following diagram:

![An image that depicts that communication occurs between a downstream
     user agent and a Media CDN router, between the router and the
     cache, between the cache and the cache filler, and between the cache
     filler and the upstream origin.](https://docs.cloud.google.com/static/media-cdn/images/media-cdn-components.svg)**Figure 1.** Media CDN components.

The router and cache component are configured with the IP addresses and protocols that they use, security and cache policies, and a routing configuration. The configuration is contained in an [`EdgeCacheService`](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices) resource. The router uses the [`HeaderAction`](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices#headeraction), described in `EdgeCacheService`, to determine how the router modifies requests (including header manipulation and path rewrites).

Media CDN terminates user HTTP requests at a reverse proxy. The reverse proxy matches the HTTP requests to a [`Routing` configuration](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices#routing). The routing configuration defines how HTTP requests are routed, modified, cached, and filled.

If the configured cache component is missing the content requested by the user, known as a _cache miss_ , then the cache component requests content from the configured upstream origin. Media CDN uses request parameters, such as the host, path, and query parameters, as a _cache key_. You can configure what items Media CDN considers as part of a cache key, which can reduce requests from Media CDN to the upstream origin. For more information, see [Cache keys](https://docs.cloud.google.com/media-cdn/docs/caching#cache-keys).

The cache filler makes a new request each time it contacts the upstream origin. When the cache filler contacts the upstream origin, it saves the original request. Then, for each attempt to fill the cache for the item requested by the cache, the cache filler copies the headers of the original request and modifies the request based on the settings in [`EdgeCacheOrigin`](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheOrigins).

Because the cache component sits downstream from the router, the cache filler only has access to headers that the router has already modified. The cache filler can't undo these router-level changes. Instead, it applies only the header configurations defined in the active `EdgeCacheOrigin` resource.

When the cache component has the requested content, it returns the content to the router to return to the downstream user agent.

## Media CDN capabilities

The following sections briefly describe Media CDN's capabilities.

### SSL (TLS) certificate support

Media CDN has built-in support for serving TLS-encrypted (HTTPS) traffic from your own domain. Media CDN is served from your own domain as a bring-your-own (BYO) domain, and doesn't require a Google-hosted domain.

There are no additional charges associated with serving SSL (TLS) traffic, or for obtaining Google-managed SSL certificates.

For more information, see [SSL (TLS) Certificates](https://docs.cloud.google.com/media-cdn/docs/ssl-certificates).

### Google Cloud Armor support

Media CDN supports Cloud Armor edge security policies. Media CDN uses Google Cloud Armor to allow or deny access to content. Cloud Armor supports IP address allowlists and denylists, geographic and layer 7 header filtering controls, and decorate requests by inserting custom headers. Additionally, Cloud Armor for Media CDN integrates with Google Threat Intelligence to enable advanced protection against known malicious IP addresses and traffic patterns.

Cloud Armor also supports Autonomous System Numbers (ASNs) in [edge security policies](https://docs.cloud.google.com/armor/docs/security-policy-overview#network-edge-policies) for Media CDN. This feature helps you permit or block network traffic originating from specific ASNs.

For more information, see [Configure security policies](https://docs.cloud.google.com/media-cdn/docs/security-policies).

### Extensibility

Media CDN lets you add custom code to the request-response processing path by using Service Extensions plugins ([Preview](https://cloud.google.com/products/#product-launch-stages)). Such customization unlocks a wide variety of lightweight use cases, such as header normalization and custom tokenization.

For more information, see [Deploy Service Extensions plugins in Media CDN routes](https://docs.cloud.google.com/media-cdn/docs/deploy-plugins).

### Origin authentication

Media CDN supports private Cloud Storage buckets as an origin through _origin authentication_. You can grant Media CDN access to your private Cloud Storage buckets and authenticate requests to ensure that only valid Media CDN requests are granted.

For more information, see [Origin connectivity and shielding](https://docs.cloud.google.com/media-cdn/docs/origins).

### Advanced routing features

Media CDN provides advanced HTTP routing capabilities that let you map traffic to specific edge configurations and origins at a fine-grained level.

For more information, see [Advanced routing](https://docs.cloud.google.com/media-cdn/docs/routing).

### Client connectivity features

Media CDN supports modern networking protocols such as HTTP/2 and QUIC from the client to the edge, increasing throughput and reducing overall network latency.

For more information, see [Client connectivity and IP addresses](https://docs.cloud.google.com/media-cdn/docs/client-connectivity).

### Cache invalidation

Cache invalidation, also called _cache purging_ , is when cached content is declared invalid. When content is declared invalid, the content is removed from the cache and then refilled from the origin server the next time that the content is requested.

Media CDN supports the following ways of invalidating content:

  * By host and URL path
  * By URL prefix and wildcard
  * By cache tags, including built-in tags for status, origin, and media type



You can combine the invalidation parameters to target specific cached responses and to minimize origin load on the subsequent cache fill.

For more information, see [Cache invalidation](https://docs.cloud.google.com/media-cdn/docs/cache-invalidation).

### Custom HTTP headers

Media CDN lets you specify custom HTTP headers. Custom request headers support static values, whereas custom response headers support both static and dynamic values.

Custom headers let you do the following:

  * Return geographic data about the client to show localized content, such as country, region, or city.

  * Determine whether a response was served fully or partially from the cache, and identify the specific cache location.

  * Modify header behavior by stripping or replacing both request and response headers.




For more information, see [Define custom headers](https://docs.cloud.google.com/media-cdn/docs/custom-headers).

### Integration with Cloud Logging

Media CDN also offers integration with Google Cloud's logging services.

Media CDN logs each HTTP request between the client and edge, and between Media CDN and the origin, to [Cloud Logging](https://docs.cloud.google.com/logging/docs). Logs are typically delivered in near real time. You can query logs in Logging and export them to [Cloud Storage](https://docs.cloud.google.com/storage/docs) or [Pub/Sub](https://docs.cloud.google.com/pubsub/docs).

For more information, see [Logging guide](https://docs.cloud.google.com/media-cdn/docs/logging).

### Signed requests

Media CDN supports signed cookies and signed URLs for content authentication. Signed requests let you scope access to an exact URL prefix for a limited time and to a specific client.

**Warning:** Do not include confidential, sensitive, or personally identifiable information in your URL paths or query parameters. URLs, including host, path and query parameters, are treated as non-identifiable service data in accordance with Section 12 (Resource Fields) of the [Service Specific Terms](https://cloud.google.com/terms/service-terms). As a privacy and security best practice, URL components should be opaque system-generated identifiers, not derived from end user input.

For more information, see [Use signed requests](https://docs.cloud.google.com/media-cdn/docs/signed-requests).

## Request access

To get started with Media CDN, [contact your Google Cloud sales representative](https://cloud.google.com/contact) or account team to get it enabled for your project. You can then use [Quickstart](https://docs.cloud.google.com/media-cdn/docs/quickstart) to set up Media CDN.

## What's next

  * To find Media CDN points of presence, see [Cache locations](https://docs.cloud.google.com/media-cdn/docs/locations). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
