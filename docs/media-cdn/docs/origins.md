---
url: https://docs.cloud.google.com/media-cdn/docs/origins/
title: Origins overview \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:31.513121+00:00
---

# Origins overview  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/origins/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Origins overview Stay organized with collections  Save and categorize content based on your preferences. 

Media CDN lets you fetch content from your origin infrastructure, whether content is hosted within Google Cloud, in another cloud, or on-premises.

Each configuration can have one or more origins associated with it. Origin configurations tell Media CDN how to connect to your infrastructure, when and how to fail over, retry, and time out, and what protocol to use when connecting.

Origins have the following features:

  * Origins can be defined per host and per route, which allows a single `EdgeCacheService` resource to map to multiple origins that contain, for example, manifests, video segments, and other static content.
  * Origins can be reached over HTTP/2, HTTPS, and unencrypted HTTP/1.1.
  * You can configure firewall rules to allow only specific Google IP addresses so that only Media CDN can access your origins.
  * Retries and failover behaviors are configured per origin, and can allow the service to fail over on hard errors (such as connectivity failure) or retry based on HTTP `404 Not Found` or HTTP `429 Too Many Requests` responses. These operations are performed only for the safer HTTP methods, including `GET`, `HEAD`, and `OPTIONS`. For more information about safe HTTP methods, refer to [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html#name-safe-methods).
  * Private resources inside Google Cloud or on-premises can be reached by configuring an [external Application Load Balancer as an origin](https://docs.cloud.google.com/media-cdn/docs/configure-origin#load-balancer-origins) behind Media CDN.
  * Redirect-following behavior is configured per origin. You can enable Media CDN to follow redirects to other origin servers.



## Origin requirements

To allow Media CDN to cache origin responses larger than 1 MiB, an origin must include the following in the response headers for `GET` requests, unless specified otherwise:

  * A `Last-Modified` _or_ `ETag` HTTP response header (a _validator_).
  * A valid HTTP `Date` header.
  * A valid `Content-Length` header.
  * The `Content-Range` response header, in response to a `Range GET` request. The `Content-Range` header must have a valid value in the form of `bytes x-y/z` (where `z` is the object size).



The default origin protocol is HTTP/2. If your origins only support HTTP/1.1, you can set the protocol field explicitly for each origin.

**Note:** Small responses (less than 1 MiB) that lack the full set of headers listed previously might be evicted from cache more quickly than larger responses.

## Origin shielding

Media CDN provides a deeply tiered edge infrastructure that is designed to actively minimize cache fill wherever possible.

There are three primary layers of caching infrastructure:

  1. Deep edge caches, which serve the majority of traffic and off-load within a service providers network.
  2. Google's peering edge, which is connected to thousands of ISPs and acts as the mid-tier cache for edge caches, and for cases where those are not present within a given ISP, the user-facing cache.
  3. Long-tail caches within Google's network that other downstream caches fill from prior to the origin. These caches support significant fan-in, have substantial cache storage capacity, and act as an origin _shield_.



An overview of this topology is shown here:

[ ![Topology overview.](https://docs.cloud.google.com/static/media-cdn/images/topology-overview.svg)](https://docs.cloud.google.com/static/media-cdn/images/topology-overview.svg) Topology overview (click to enlarge).

Media CDN provides origin shielding by default using a limited set of key, global locations. The default origin shielding operates based on the location of the end user and not of the origin. This works well and provides strong offload benefits when end-users and origin servers are in the same region and when global origin servers are located in multiple regions.

### Flexible shielding

**Important:** Flexible shielding is an advanced configuration. Choosing an inappropriate shielding region can negatively impact performance, potentially increasing latency compared to the default behavior. Default origin shielding is highly recommended unless your primary use case involves a centralized origin serving content to widely distributed global end users.

In scenarios where your origin is centralized in one region but your users are globally distributed, the default origin shielding behavior, which is based on user location, might be suboptimal in the following ways:

  * Increase latency for cache misses when the default shield location is geographically distant from your centralized origin
  * Reduced origin offload by scattering cache-fill requests across multiple global default shield locations instead of concentrating them



Flexible shielding helps you overcome these limitations by [configuring a single, specific geographic region for origin shielding](https://docs.cloud.google.com/media-cdn/docs/configure-origin#configure-flex-shielding-region), typically selected to be near your centralized origin. Flexible shielding then routes all cache fill requests through shield caches located in or near the configured region. This consolidates load to your origin through those regionally-focused caches.

By configuring a flexible shielding region in the same geographical region as your centralized origin, you can optimize the following:

  * Cache hit rate at the shield layer
  * Origin offload
  * Latency for cache misses and uncacheable content
  * Performance stability



Flexible shielding is compatible with any origin type configured in Media CDN.

## Request collapsing

Request collapsing actively collapses multiple user-driven cache fill requests for the same cache key into a single origin request, per edge node.

All layers of caching support request collapsing (or _coalescing_) to further reduce origin load. Based on observed, real-world workloads at scale:

  * > 95% of cache fill uses a dedicated long-tail cache node within the region, in order to reduce cache fill costs and latency.
  * Cache fill between the origin and Google's own edge infrastructure is entirely over Google's global private backbone network, which reduces cache fill latency and improves reliability—both are active benefits for live streaming workloads.
  * Caches cross-fill from each other where advantageous to do so, further driving down cache fill rates.
  * Media CDN has significant storage capacity across caches, which minimizes the eviction rates even for long-tail, less popular content.



Customers might see different offload rates depending on their cache configuration, user load, workloads (such as live versus on-demand), user distribution, and how much long-tail content (total corpus size) they serve to users across regions.

Combined with origin shielding, request collapsing further reduces origin load and egress bandwidth needs, and is the default behavior for Media CDN.

Collapsed requests have both the client-facing request logged and the (collapsed) cache fill request logged. The _leader_ of the collapsed session is used to make the origin fill request, which means that the origin sees the headers (including the User-Agent) of only that client.

Requests that don't share the same cache key cannot be collapsed.

## Origin connectivity

The following sections describe how Media CDN connects to origins, how HTTP requests are made, and how you can authenticate requests.

### Supported origins and protocols

Media CDN directly supports any publicly reachable HTTP endpoint as an origin, including the following:

  * Cloud Storage buckets, including [private buckets](https://docs.cloud.google.com/media-cdn/docs/configure-origin#private-storage-buckets) through Identity and Access Management service accounts
  * [External Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https)
  * Amazon S3-compatible buckets, including [private buckets](https://docs.cloud.google.com/media-cdn/docs/connect-to-s3-compatible-buckets) that use AWS Signature Version 4
  * Other publicly available object storage, such as Azure Blob Storage
  * Publicly available web servers, such as public VMs or on-premises hosts



Connectivity to origins is over secure tunnels and Google's global backbone network.

The following table details the supported origin protocols.

Protocol | Supported | SSL (TLS) required  
---|---|---  
HTTP/2 | Yes (default) | Yes  
HTTPS (HTTP/1.1 over TLS) | Yes | Yes  
HTTP/1.1 | Yes | No  
  
Media CDN uses HTTP/2 (h2) to connect to an origin by default. HTTP/2 and HTTPS both require a valid, publicly trusted TLS (SSL) certificate. A valid certificate is one that is unexpired, signed by a public Certificate Authority, and has a Subject Alternative Name matching the hostname sent to the origin.

Notes:

  * If your origin doesn't support HTTP/2, you can explicitly set the protocol (on a per-origin basis) to `HTTP` (HTTP/1.1) or `HTTPS` (HTTP/1.1 over TLS).
  * When configuring HTTPS or HTTP/1.1 as the origin protocol, Media CDN doesn't negotiate an alternative protocol (such as HTTP/2). Similarly, when configuring HTTP/2, the connection doesn't fall back to HTTP/1.1, in order to be explicit about origin connectivity behavior.
  * Media CDN automatically uses the correct port based on the protocol: port `80` for HTTP or port `443` for HTTPS and HTTP/2.



### Origin request headers

When connecting to an origin, Media CDN uses the `Host` header from the client request by default.

The following table documents what the origin sees in the incoming request under different configuration scenarios:

Client Request | `EdgeCacheService.hostRewrite` | `EdgeCacheOrigin.hostRewrite` | originAddress | Host header /  
TLS SNI at origin  
---|---|---|---|---  
media.example.com | None | None | backend.example.com | media.example.com  
media.example.com | service.example.com | None | backend.example.com | service.example.com  
media.example.com | None | origin.example.com | backend.example.com | origin.example.com  
media.example.com | service.example.com | origin.example.com | backend.example.com | origin.example.com  
media.example.com | service.example.com | origin.example.com | gs://vod-content-bucket | set automatically based on the bucket name  
  
The primary origin and any failover origins see the same host header if they share the same `routeRule` or `hostRewrite` configuration.

Any `hostRewrite` settings are ignored when using a Cloud Storage bucket as the origin because alternative host header values are not supported by Cloud Storage buckets. The host header is automatically set based on the bucket name.

The TLS SNI (Server Name Indication) value in the request (for HTTP/3, HTTP/2, and HTTPS requests) is set to the same value as the host header sent to the origin.

For information about rewriting host headers for per-route configuration, see [Configure service routes](https://docs.cloud.google.com/media-cdn/docs/routing). For information about setting per-origin override actions, see [Origin failover without redirect following](https://docs.cloud.google.com/media-cdn/docs/configure-origin#failover-example).

### Allow the origin to receive traffic from Media CDN

To reduce the risk of unauthorized access to your content, use an IP allowlist at the origin to block access to all IP addresses except the specific IP address ranges that Google uses to send requests to external origins. That way, only Media CDN can connect to your origin servers.

The following table summarizes the required source IP address ranges for firewall rules:

IP address type | Request source IP range  
---|---  
IPv4  | 136.124.4.0/22   
IPv6 | 2001:4860:4864:a::/64   
**Note:** These IP address ranges might change. For uninterrupted and secure communication with your origins, check the [Media CDN release notes](https://docs.cloud.google.com/media-cdn/docs/release-notes) frequently, and when required, update the Google Cloud IP address ranges in your firewall configurations.

Use the following URL to access the JSON file that contains the updated Google-assigned IP address ranges.
    
    
    https://www.gstatic.com/ipranges/mediacdn.json
    

## Failover and timeouts

The following sections describe these configuration options:

  * Timeouts: Determine how long Media CDN waits to connect to your origin or for it to respond to a request.
  * Retries: Determine whether Media CDN retries an origin HTTP request to your origin, and under what conditions.
  * Failover: Determine whether Media CDN attempts to connect to a failover origin if the first is unavailable or returns a specific status code.

**Note:** Retry or failover attempts are made only for `GET`, `HEAD`, and `OPTIONS` requests.

### Origin timeouts

Timeouts let you configure when origin retry and failover behaviors are triggered and when subsequent client failover can be triggered.

The following describes the configurable timeouts that Media CDN supports:

  * `connectTimeout` and `maxAttemptsTimeout` limit how long Media CDN takes to find a usable response.

Both timeouts include the time that the origin takes to return headers and to determine whether to use a failover or redirect. `connectTimeout` applies independently for each origin attempt, while `maxAttemptsTimeout` includes the time required to connect across all origin attempts, including failovers and redirects. Following a redirect counts as an additional attempt to connect to the origin, and counts toward the `maxAttempts` set for the configured origin.

When Media CDN encounters a nonredirect response, such as from a redirect or failover origin, the `readTimeout` and `responseTimeout` values apply. Redirected origins use the `connectTimeout`, `readTimeout`, and `responseTimeout` values configured for the `EdgeCacheOrigin` that encountered the redirect.

  * `responseTimeout` and `readTimeout` control how long a streamed response can take. After Media CDN determines that it's going to use an upstream response, neither `connectTimeout` nor `maxAttemptsTimeout` matter. At this point, `readTimeout` and `responseTimeout` come into effect.




Media CDN makes at most four origin attempts across all origins, regardless of the `maxAttempts` set by each `EdgeCacheOrigin`. Media CDN uses the `maxAttemptsTimeout` value from the primary `EdgeCacheOrigin`. The per-attempt timeout values (`connectTimeout`, `readTimeout`, and `responseTimeout`) are configured for the `EdgeCacheOrigin` of each attempt.

The following table describes the timeout fields:

Field | Default | Description  
---|---|---  
**connectTimeout** | 5 seconds | The maximum amount of time Media CDN can take from starting the request to the origin until Media CDN determines whether the response is usable. Practically, `connectTimeout` covers the time starting with creating the request, then doing DNS lookups, then doing TLS handshakes, TCP/QUIC connection establishment, through getting the response headers that contain the HTTP status code. The timeout must be a value between 1 second and 15 seconds.  
**maxAttemptsTimeout** | 15 seconds | The maximum time across all connection attempts to the origin, including failover origins, before returning an error to the client. An HTTP `504` status code is returned if the timeout is reached before a response is returned. The timeout must be a value between 1 second and 30 seconds. This setting defines the _total_ duration for _all_ origin connection attempts, including failover origins, in order to cap the total time clients have to wait for content to start streaming. Only the first `maxAttemptsTimeout` value is used, where the _first_ is defined by the origin configured for the given route.  
**readTimeout** | 15 seconds | The maximum duration to wait between reads of a single HTTP response. The `readTimeout` is capped by the `responseTimeout`. All reads of the HTTP response must be completed by the deadline set by the `responseTimeout`. The timeout must be a value between 1 second and 30 seconds. If this timeout is reached before the response is complete, the response is truncated and logged.  
**responseTimeout** | 30 seconds | The maximum duration to allow for a response to complete. The timeout must be a value between 1 second and 120 seconds. The duration is measured from the time that the first body bytes are received. If this timeout is reached before the response is complete, the response is truncated and logged.  
  
Consider the following examples:

  * `Origin A` matches requests to "/segments/" and has a `maxAttemptsTimeout` value of `5s`, a `maxAttempts` value of `1`, and a `failover_origin` value of `Origin B`. The `connectTimeout` value is at its default of `5s`. If you attempt to connect to `Origin A`, and it fails within 1 second due to an invalid TLS certificate, you have ~4 seconds left to make a successful connection to `Origin B`.

  * `Origin C` matches requests to "/manifests/*, has a `maxAttemptsTimeout` value of `10s`, a `maxAttempts` value of `3`, and `failover_origin` not configured. The `connectTimeout` value is at its default of `5s`. Media CDN attempts to connect to `Origin C` up to three times, allowing up to 10 seconds (the `maxAttemptsTimeout` limit) to make a successful connection.




### Retry origin requests

Media CDN supports origin retries, allowing unsuccessful requests to the origin to be retried. You can specify how many times the current origin can be retried against before a failover origin (if configured) is attempted.

  * Media CDN retries only the requests that use safe HTTP methods,`GET`, `HEAD`, or `OPTIONS`.

**Note:** If a request using an unsafe method fails on the first attempt to the primary origin, Media CDN responds to the client with an HTTP `502 Bad Gateway` status code. It doesn't attempt any retries to another origin.
  * Media CDN attempts to reach the primary origin up to the configured `maxAttempts` value, which defaults to `1`.

  * Media CDN retries origin connections up to a maximum of three times before failing and returning an HTTP `502 Bad Gateway` error to the user. This includes any failover origin connections, which count towards the limit of three.

  * When configuring an origin resource, you can configure a primary origin by using the `originAddress` field, and then an optional `failoverOrigin`. The `failoverOrigin` points at another origin resource.




The `retryConditions` for each origin specifies what types of failures triggers a retry:

Condition | Default | Description  
---|---|---  
CONNECT_FAILURE | ✔️ | Retry on failures include routing, DNS and TLS handshake errors, and TCP/UDP timeouts.   
HTTP_5XX |  | Retry on any HTTP `5 _xx_` status code.  
GATEWAY_ERROR |  | Similar to `5 _xx_`, but applies only to status codes `502`, `503`, or `504`.  
RETRIABLE_4XX |  | Retry for `4 _xx_` status codes that can be retried, including `409` and `429`.  
NOT_FOUND |  | Retry on an HTTP `404` status code.  
FORBIDDEN |  | Retry on an HTTP `403` status code.  
  
If you require active health-checking, round-robin, or load-aware steering across origins, you can [configure an external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https) as the primary origin.

### Failover behavior

Failover attempts are made only for the requests that use safer HTTP methods, `GET`,`HEAD`, or `OPTIONS`.

**Note:** If a request using an unsafe method fails on the first attempt to the primary origin, Media CDN responds to the client with an HTTP `502 Bad Gateway` status code. It doesn't attempt failover to another origin.

The following table describes how failover operates, and what response a client would observe:

Scenario | Failover configured | User-facing status  
---|---|---  
Media CDN attempts to connect to your origin, and receives no HTTP response after two attempts (default).  | No | HTTP `502 Bad Gateway`  
Media CDN attempts to connect to your primary origin, and fails to connect (TLS handshake error). An attempt is made against your configured failover origin, which returns an HTTP `404` error.  | Yes | HTTP `404 Not Found`  
Media CDN attempts to connect to both your primary and failover origin, but receives no HTTP status code.  | Yes | HTTP `502 Bad Gateway`  
  
If Media CDN receives a status code matching any configured `retryConditions`, such as an HTTP `404 Not Found` or HTTP `429 Too Many Requests` error, and subsequent retry and failover origin requests continue to fail, an HTTP `502 Bad Gateway` error is returned to the client after origin attempts are exhausted.

### Best practices for origin failover

When configuring multiple origins for failover or load balancing, verify that your media content and `Vary`, `ETag`, and `Last-Modified` header behaviors are consistent between your origins.

**Warning:** Configuring redirects from an untrusted or an attacker-controlled origin service might expose your Media CDN configuration to open redirect vulnerabilities.

As a best practice, configure origin redirection only for origins that you trust and control. Ensure that you trust every origin in a redirect chain because each origin produces content that is served by your `EdgeCacheService`.

## What's next

  * [Configure an origin](https://docs.cloud.google.com/media-cdn/docs/configure-origin)
  * [Use a private Amazon S3-compatible bucket as an origin](https://docs.cloud.google.com/media-cdn/docs/connect-to-s3-compatible-buckets)
  * [Configure service routes](https://docs.cloud.google.com/media-cdn/docs/routing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
