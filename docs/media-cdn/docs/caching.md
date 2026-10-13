---
url: https://docs.cloud.google.com/media-cdn/docs/caching/
title: Configure caching behavior \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:43:58.692396+00:00
---

# Configure caching behavior  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/caching/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Configure caching behavior Stay organized with collections  Save and categorize content based on your preferences. 

Media CDN serves content as close to users as possible by using Google's global edge caching infrastructure to cache content and reduce load on origin infrastructure.

You can control how content is cached for each route. This lets you optimize behavior based on the type of content, client request attributes, and your freshness requirements.

## Cacheability

The following sections describe what responses Media CDN caches and how to improve cache offload.

### Default caching behavior

By default, the following cache-related settings apply to each Edge Cache service:

  * Default cache mode of `CACHE_ALL_STATIC`:

    * Respects origin cache directives, such as `Cache-Control` or `Expires`, up to a configurable max TTL.
    * Caches static media types automatically with a default TTL of 3600s, if no origin cache directives are present.
    * Caches HTTP 200, 204, and 206 status codes (negative caching is not enabled).
  * Does not cache responses that have `no-store` or `private` cache-control directives or that are otherwise uncacheable.




Responses that are not static content or that are missing valid cache directives are not cached unless caching is explicitly configured. To learn how to override the default behavior, see the documentation on cache modes .

The default behavior is equivalent to the following `cdnPolicy`. Routes without an explicit `cdnPolicy` configured behave as if they have the following configuration:
    
    
    cdnPolicy:
      cacheMode: CACHE_ALL_STATIC
      defaultTtl: 3600s
      cacheKeyPolicy:
        includeProtocol: false
        excludeHost: false
        excludeQueryString: false
      signedRequestMode: DISABLED
      negativeCaching: false

### Cacheable responses

A cacheable response is an HTTP response that Media CDN can store and quickly retrieve, thus allowing for faster load times. Not all HTTP responses are cacheable.

You can configure cache modes for each route to override this behavior (for example, using the `CACHE_ALL_STATIC` cache mode to cache common media types) even if the origin does not set a cache control directive in the response.

Requests and responses that meet the criteria defined in uncacheable responses supersedes cacheability.

The following table describes the requirements to cache particular HTTP responses. Both `GET` and `HEAD` responses must adhere to these requirements.

HTTP attribute | Requirements  
---|---  
**Status code** | The response status code must be one of 200, 203, 204, 206, 300, 301, 302, 307, 308, 400, 403, 404, 405, 410, 451, 500, 501, 502, 503, or 504.  
**HTTP methods** | `GET` and `HEAD`  
**Request headers** | Most caching request directives are ignored. For more information, see Cache control directives.  
**Response headers** | Contains a valid HTTP caching directive such as `Cache-Control: max-age=3600, public`. Has a cache mode that caches that content, or has an `Expires` header with a date in the future.  
**Response size** | Up to 100 GiB.  
  
The [HTTP `Age` header](https://docs.cloud.google.com/media-cdn/docs/custom-headers#default-headers) is set based on when Media CDN first cached the response, and typically represents the seconds since the object was cached at an [origin shielding](https://docs.cloud.google.com/media-cdn/docs/origins#origin-shielding) location. If your origin generates an Age response header, use the `FORCE_CACHE_ALL` cache mode to prevent revalidations when Age exceeds the cache TTL.

For more information about how Media CDN interprets HTTP caching directives, see Cache control directives.

### Origin requirements

To allow Media CDN to cache origin responses larger than 1 MiB, an origin must include the following in the response headers for `GET` requests, unless specified otherwise:

  * A `Last-Modified` _or_ `ETag` HTTP response header (a _validator_).
  * A valid HTTP `Date` header.
  * A valid `Content-Length` header.
  * The `Content-Range` response header, in response to a `Range GET` request. The `Content-Range` header must have a valid value in the form of `bytes x-y/z` (where `z` is the object size).



The default origin protocol is HTTP/2. If your origins only support HTTP/1.1, you can set the protocol field explicitly for each origin.

**Note:** Small responses (less than 1 MiB) that lack the full set of headers listed previously might be evicted from cache more quickly than larger responses.

### Uncacheable responses

The following table details the request and response attributes that prevent a response from being cached. Responses that are cacheable but that match "uncacheable" criteria aren't cached.

HTTP attribute | Requirement  
---|---  
**Status code** | A status code other than those defined as cacheable, such as HTTP 401, HTTP 412, or HTTP 505. These status codes are typically representative of client-facing issues and not origin status. Caching those responses can lead to "cache poisoning" scenarios where a user-triggered "bad" response is cached for all users.  
**Request headers** | For requests with an `Authorization` request header, responses must include a `public` Cache-Control directive to be cached. A `no-store` directive in the request causes the response not to be cached. For more information, see Cache control directives.  
**Response headers** | Has a `Set-Cookie` header. Has a `Vary` header other than `Accept`, `Accept-Encoding`, `Access-Control-Request-Headers`, `Access-Control-Request-Method`, `Origin`, `Sec-Fetch-Dest`, `Sec-Fetch-Mode`, `Sec-Fetch-Site`, `X-Goog-Allowed-Resources`, or `X-Origin`. In `CACHE_ALL_STATIC` or `USE_ORIGIN_HEADERS` mode, has a `no-store` or `private` cache control directive.  
**Response size** | Greater than 100 GiB.  
  
These rules apply in addition to the configured cache mode. Specifically:

  * With the `CACHE_ALL_STATIC` cache mode configured, only responses that are considered static content or responses with valid cache directives in their response headers are cached. Other responses are proxied as is.
  * The `FORCE_CACHE_ALL` cache mode caches all responses unconditionally, subject to the uncacheability requirements stated earlier.
  * The `USE_ORIGIN_HEADERS` cache mode requires responses to set valid cache directives in their response headers in addition to being a cacheable status code.



Notes:

  * Responses that are not cached don't have their cache control directives or other headers changed and are proxied as is.
  * Responses can have their `Cache-Control` and `Expires` headers collapsed into a single `Cache-Control` field. For example, a response with `Cache-Control: public` and `Cache-Control: max-age=100` on separate lines would be collapsed as `Cache-Control: public,max-age=100`.
  * Uncacheable responses (responses that would never be cached) are not counted as `Cache Egress` from a billing perspective.



### Using cache modes

Cache modes allow you to configure when Media CDN should respect origin cache directives, cache static media types, and cache all responses from the origin, regardless of the directives set.

Cache modes are configured at the route-level and, combined with TTL overrides, allow you to configure cache behavior by host, path, query parameters, and headers (any matchable request parameters).

  * By default, Media CDN uses the `CACHE_ALL_STATIC` cache mode, which automatically caches common static media types for 1 hour (3600 seconds), while prioritizing any cache directives specified by the origin for cacheable responses.
  * You can increase or decrease the cache TTL applied to responses without an explicit cache TTL set (a `max-age` or `s-maxage` directive) by setting the `cdnPolicy.defaultTtl` field on a route.
  * To prevent caching non-success responses for longer than intended, non-2xx (non-success) status codes are not cached according to their `Content-Type` (MIME type) and don't have the default TTL applied.

**Note:** To configure how non-2xx responses such as redirects (3xx) are cached, see Negative caching.

The available cache modes, which are set on the `cdnPolicy.cacheMode` of each route, are shown in the following table.

Cache mode | Behavior  
---|---  
**`USE_ORIGIN_HEADERS`** | Requires origin responses to set valid cache directives and valid caching headers. For a full list of requirements, see Cacheable responses.  
**`CACHE_ALL_STATIC`** | Automatically caches successful responses with static content, unless they have a `no-store` or `private` directive. Valid caching directives from the origin are prioritized. Static content includes video, audio, images, and common web assets as defined by the MIME type in the `Content-Type` response header.  
**`FORCE_CACHE_ALL`** | Unconditionally caches successful responses, overriding any cache directives set by the origin. Make sure not to serve private, per-user content (such as dynamic HTML or API responses) with this mode configured.  
**BYPASS_CACHE** | Any request that matches a route with this cache mode configured bypasses the cache, even if there is a cached object that matches that cache key. We recommend using this only for debugging because Media CDN is designed as a planet-scale cache infrastructure and not a general purpose proxy.  
  
### Static content MIME types

The `CACHE_ALL_STATIC` cache mode allows Media CDN to automatically cache common static content such as video, audio, images, and common web assets based on the MIME type returned in the `Content-Type` HTTP response header. However, regardless of media type, Media CDN prioritizes any explicit `Cache-Control` or `Expires` headers in the origin response.

The following table lists the MIME types that can be cached automatically with the `CACHE_ALL_STATIC` cache mode.

Responses are not automatically cached if they don't have a `Content-Type` response header with a value that matches the following values. You must ensure that the response sets a valid cache directive, or you must use the `FORCE_CACHE_ALL` cache mode to unconditionally cache responses.

Category | MIME types  
---|---  
**Web assets** | text/css text/ecmascript text/javascript application/javascript  
**Fonts** | Any Content-Type matching font/*  
**Images** | Any Content-Type matching image/*  
**Videos** | Any Content-Type matching video/*  
**Audio** | Any Content-Type matching audio/*  
**Formatted document types** | application/pdf and application/postscript  
  
Note the following:

  * Your origin's web server software must set the `Content-Type` for each response. Many web servers automatically set the `Content-Type` header, including NGINX, Varnish, and Apache.
  * Cloud Storage sets the `Content-Type` header [automatically on upload](https://docs.cloud.google.com/storage/docs/metadata#content-type) when you use the Google Cloud console or the gcloud CLI to upload content.
  * Cloud Storage always provides a `Cache-Control` header to Media CDN. If no value is explicitly chosen, it sends a default value. As a result, all successful Cloud Storage responses are cached according to Cloud Storage default values, unless you explicitly adjust the [cache control metadata](https://docs.cloud.google.com/storage/docs/metadata#cache-control) for objects in Cloud Storage or use `FORCE_CACHE_ALL` mode to override the values sent by Cloud Storage.



If a response is cacheable based on its MIME type but has a `Cache-Control` response directive of `private` or `no-store` or a `Set-Cookie` header, it isn't cached.

Other media types, such as HTML (`text/html`) and JSON (`application/json`), are not cached by default. These types of responses are typically dynamic (per user), and are also not well suited for Media CDN's architecture. We recommend using [Cloud CDN](https://docs.cloud.google.com/cdn) for serving web assets and for caching API responses.

### Configure cache TTLs

Time to live (TTL) overrides let you set default TTL values for cached content and override TTL values set in the `max-age` and `s-maxage` cache control directives (or `Expires` headers) set by your origins.

TTLs, whether set by overrides or by using a cache directive, are optimistic. Content that is rarely accessed or unpopular might be evicted from the cache prior to the TTL being reached.

The following table shows three TTL settings.

Setting | Default | Minimum | Maximum | Description | Applicable cache modes  
---|---|---|---|---|---  
**Default TTL** | 1 hour  
(3600 seconds) | 0 seconds | 1 year  
(31,536,000 seconds) | The TTL to set when the origin has not specified a `max-age` or an `s-maxage` header. If the origin specifies an `s-maxage` header, it is used instead of the default TTL value here. When using `FORCE_CACHE_ALL` to unconditionally cache all responses, the default TTL is used to set the cache TTL. All other values and directives are ignored. | `CACHE_ALL_STATIC` `FORCE_CACHE_ALL`  
**Max TTL** | 1 day  
(86400 seconds) | 0 seconds | 1 year  
(31,536,000 seconds) | For cacheable responses, the maximum TTL to allow. Values greater than this are capped at the value of `maxTtl`.  | `CACHE_ALL_STATIC`  
**Client TTL** | Not set by default. | 0 seconds | 1 day  
(86400 seconds) | For cacheable responses, the maximum TTL to allow in the downstream (client-facing) response if this needs to be different from other TTL values.  | `CACHE_ALL_STATIC` `FORCE_CACHE_ALL`  
  
Setting any TTL value to zero (0 seconds) causes every request to be revalidated with the origin before a response is served and increases load to the origin if set too broadly.

When the cache mode is set to `Use Origin Headers`, TTL settings cannot be configured because Media CDN relies on the origin to drive behavior.

Notes:

  * The value for max TTL must always be greater than (or equal to) the value of default TTL.
  * The value for client TTL must always be smaller than (or equal to) the value of max TTL.
  * When Media CDN overrides an origin TTL value, the `Cache-Control` header to the client also reflects that value.
  * If the origin sets an `Expires` header and Media CDN overrides the effective TTL (based on the timestamp), the `Expires` header is replaced with a `Cache-Control` header in the downstream response to the client.



### Negative caching

Negative caching defines how non-success HTTP status codes (those other than 2xx) are cached by Media CDN.

This lets you cache error responses such as redirects (HTTP 301 and 308) and not found (HTTP 404) responses closer to users, as well as reduce origin load more broadly if the response is unlikely to change and can be cached.

**Note:** To configure how success responses (2xx status codes) are cached, see cache modes.

By default, negative caching is disabled. The following table shows the default values for each status code when negative caching is enabled and `negativeCachingPolicy` isn't used.

Status codes | Reason-phrase | TTL  
---|---|---  
**HTTP 300** | Multiple Choices | 10 minutes  
**HTTP 301 and HTTP 308** | Permanent Redirect | 10 minutes  
**HTTP 404** | Not Found | 120 seconds  
**HTTP 405** | Method Not Found | 60 seconds  
**HTTP 410** | Gone | 120 seconds  
**HTTP 451** | Unavailable for Legal Reasons | 120 seconds  
**HTTP 501** | Not Implemented | 60 seconds  
  
The default set of negative caching codes matches the heuristically cacheable status codes described in [HTTP RFC 9110](https://tools.ietf.org/html/rfc9110#section-15.1), with the following exceptions:

  * HTTP code 414 (URI Too Long) is not supported for caching, to avoid cache poisoning.
  * HTTP code 451 (Unavailable for Legal Reasons) is supported for caching, as described in [HTTP RFC 7725](https://tools.ietf.org/html/rfc7725#section-3).



If you need to configure your own per-status code TTLs, and override the default behavior, you can configure a `cdnPolicy.negativeCachingPolicy`. This lets you set the TTL for any of the status codes allowed by Media CDN: 300, 301, 302, 307, 308, 400, 403, 404, 405, 410, 451, 500, 501, 502, 503, and 504.

For example, to set a short, 5-second TTL for HTTP 404 (Not Found) responses, and a 10-second TTL for HTTP 405 (Method Not Allowed) responses, use the following YAML definition on each applicable route:
    
    
    cdnPolicy:
      negativeCaching: true
      negativeCachingPolicy:
        "404": 5s
        "405": 10s
      # other status codes to apply TTLs for

**Important:** When you configure a `negativeCachingPolicy`, specify all of the status codes (and their TTLs) that you want to cache. The default TTLs (described on this page) don't apply when a policy exists.

To prevent cache poisoning, we don't recommend enabling caching for either status code 400 (Bad Request) or 403 (Forbidden). Ensure that your origin server returns either code as a result of examining only the components of the request that are included in the cache key. Cache poisoning can occur, for example, when the origin server responds with a 403 error response in the absence of a correct `Authorization` header. In this case, caching the 403 error response results in Media CDN serving the 403 error response to all subsequent requests until the TTL expires, even if the requests have a correct `Authorization` header.

To disable negative caching:

  * To **disable the default negative caching behavior** , set `cdnPolicy.negativeCaching: false` on a route. Note that origin responses with valid cache directives and cacheable status codes are still cached.
  * To **prevent negative caching for a specific status code, but still respect origin cache directives** , omit the status code (`cdnPolicy.negativeCachingPolicy[].code`) in your `negativeCachingPolicy` definition.
  * To **explicitly ignore the origin cache directives for a specific status code** , set `cdnPolicy.negativeCachingPolicy[].ttl` to `0` (zero) for that status code.



Notes:

  * When `negativeCaching` is enabled on a route, and a response defines valid cache directives, the cache directives in the response take precedence.
  * If you configure an explicit `negativeCachingPolicy`, and there is a TTL defined for the given status code, the TTL defined in the policy is always used.
  * The maximum value for a TTL set by `negativeCachingPolicy` is 1800 seconds (30 minutes), but origin cache directives with a higher TTL are respected.
  * If the cache mode is configured as `FORCE_CACHE_ALL`, origin directives are ignored in all cases.



### Cache control directives

Media CDN's behavior with respect to [`Cache-Control` directives](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Cache-Control) is defined here.

If the directive is not applicable to a request or response, such as `only-if-cached` (a client-only directive), then "N/A" is marked in that column.

Directive | Request | Response  
---|---|---  
`no-cache` | The `no-cache` request directive is ignored to prevent clients from potentially initiating or forcing revalidation to the origin. | A response with `no-cache` is cached, but requires validation with the origin before it can be served. This can be overridden on a per-route basis with the `FORCE_CACHE_ALL` cache mode.  
`no-store` | The response to a request with `no-store` isn't cached. | A response with `no-store` isn't cached. This can be overridden on a per-route basis with the `FORCE_CACHE_ALL` cache mode.  
`public` | N/A | A response with the `public` directive is cached if the response is considered cacheable as a whole _and_ the response has a `max-age` or an `s-maxage` directive as well. When using the `CACHE_ALL_STATIC` cache or `FORCE_CACHE_ALL` modes, this is not required.  
`private` | N/A | A response with the `private` directive isn't cached by Media CDN, even if the response is otherwise considered cacheable. Clients (such as browsers) might still cache the result. This can be overridden on a per-route basis with the `FORCE_CACHE_ALL` cache mode. Use `no-store` to prevent all caching of responses.  
`max-age=SECONDS` | The max-age request directive is ignored. A cached response is returned as if this header was not included in the request. | A response with the `max-age` directive is cached up to the defined `SECONDS`.  
`s-maxage=SECONDS` | N/A | A response with the `s-maxage` directive is cached up to the defined `SECONDS`. If both `max-age` and `s-maxage` are present, `s-maxage` is used by the server. Note that `s-max-age` (two hyphens) is not valid for the purposes of caching.  
`min-fresh=SECONDS` | The `min-fresh` request directive is ignored. A cached response is returned as if this header was not included in the request. | N/A  
`max-stale=SECONDS` | The `max-stale` request directive is ignored. A cached response is returned as if this header was not included in the request. | N/A  
`stale-while-revalidate=SECONDS` | N/A | No effect. This is passed on to the client in the response.  
`stale-if-error=SECONDS` | The `stale-if-error` request directive is ignored. A cached response is returned as if this header was not included in the request. | No effect. This is passed on to the client in the response.  
`must-revalidate` | N/A | A response with `must-revalidate` is revalidated with the origin server after it's expired.  
`proxy-revalidate` | N/A | A response with `proxy-revalidate` is revalidated with the origin server after it's expired.  
`immutable` | N/A | No effect. This is passed on to the client in the response.  
`no-transform` | N/A | No transforms are applied by Media CDN.  
`only-if-cached` | The `only-if-cached` request directive is ignored. A cached response is returned as if this header was not included in the request. | N/A  
  
Where possible, Media CDN is RFC-compliant (HTTP [RFC 7234](https://tools.ietf.org/html/rfc7234)), but favors optimizing for cache offload and minimizing the impact that clients can have on hit rate and overall origin load.

For responses that use the HTTP/1.1 `Expires` header:

  * The value of the `Expires` header must be a valid HTTP-date as [defined in RFC 7231](https://tools.ietf.org/html/rfc7231#section-7.1.1.1)
  * A date value in the past, an invalid date, or a value of `0` indicates that the content has already expired and requires revalidation.
  * Media CDN ignores the `Expires` header if a `Cache-Control` header is present in the response.



The HTTP/1.0 `Pragma` header, if present in a response, is ignored and passed through as-is to the client.

## Cache keys

You can reduce the number of times Media CDN needs to contact your origin by considering what uniquely identifies a request, and removing components that might often change between requests. The set of request components are often referred to as a 'cache key'.

The following sections describe how to configure cache keys.

### Cache key components

A cache key is the set of request parameters (such as the host, path, and query parameters) that a cached object is referenced by.

By default, cache keys for Edge Cache services include the request host, path and query parameters from the request, and are scoped to a specific EdgeCacheService.

**Warning:** Do not include confidential, sensitive, or personally identifiable information in your URL paths or query parameters. URLs, including host, path and query parameters, are treated as non-identifiable service data in accordance with Section 12 (Resource Fields) of the [Service Specific Terms](https://cloud.google.com/terms/service-terms). As a privacy and security best practice, URL components should be opaque system-generated identifiers, not derived from end user input.Component | Included by default? | Details  
---|---|---  
**Protocol** | No | Requests over HTTP and HTTPS reference the same cached object. If you want to return the different responses to http: and https: requests, set `cacheKeyPolicy.includeProtocol` to true on the associated routes.  
**Host** | Yes | Different hosts don't reference the same cached objects. If you have multiple hostnames directed at the same EdgeCacheService, and they are serving the same content, set `cdnPolicy.excludeHost` to true.  
**Path** | Yes | Always included in the cache key and cannot be removed. The path is the minimum representation of an object in cache.   
**Query parameters** | Yes | If query parameters don't distinguish between different responses, set `cacheKeyPolicy.excludeQueryString` to true. If only some query parameters should be included in a cache key, set `includedQueryParameters` or `excludedQueryParameters`, as appropriate.  
**Headers** | No | Set `cacheKeyPolicy.includedHeaderNames` with the names of headers to include in the cache key. Specifying multiple headers that combine to have a large range of values (for example, the combined header values identify a single user) dramatically lowers the cache hit rate and can result in a higher eviction rate and reduced performance.  
**Cookies** | No | Set `cacheKeyPolicy.includedCookieNames` with the names of cookies to include in the cache key. Specifying multiple cookies that combine to have a large range of values (for example, the combined cookie values identify a single user) dramatically lowers the cache hit rate and can result in a higher eviction rate and reduced performance.  
  
Note the following:

  * Cache keys are not attached to a configured origin, allowing you to update an origin configuration (or replace the origin entirely) without risk of "flushing" the cache (for example, when migrating origin storage between providers).
  * Cache keys are constrained to an EdgeCacheService. Different EdgeCacheServices have different cache namespaces, which prevents you from accidentally caching objects between prod, staging, and other testing environments, even if the host, path, or other cache key components would match. Deleting an EdgeCacheService effectively invalidates all cached objects for that service.
  * Cache keys are not scoped to an individual route. Multiple routes might refer to the same cache key, especially if those routes match on components that are not included in the cache key, such as request headers or excluded parameters. This can be useful if you want multiple routes to share the same cache but return different response headers or CORS configuration.
  * Cache keys don't include URL rewrite configuration—for example, a cache key is based on the user-facing request and not the final "rewritten" request.
  * When signed requests are configured on a route, the signed attributes are not included in the cache key. The request is treated as if the (signed) query parameters or path component, starting with `edge-cache-token` and ending at the next path separator ("/"), are not part of the URL.



### Include or exclude query parameters

You can include or exclude specific query parameters from a cache key by adding the parameter name to the `includedQueryParameters` or `excludedQueryParameters` cache key configuration on a given route.

For example, to include the `contentID` and `country` query parameters and ignore all others from the cache key:
    
    
    cdnPolicy:
      cacheMode: CACHE_ALL_STATIC
      defaultTtl: 86400s
      cacheKeyPolicy:
        includedQueryParameters: ["contentID", "country"]

Make sure to include the query parameters that uniquely identify content, and exclude those that don't. For example, exclude analytics query parameters, playback session IDs, or other parameters that are only unique to the client. Including more query parameters than necessary can decrease cache hit rates.

Alternatively, instead of specifying which parameters to include in the cache key, you can choose which parameters to exclude from the cache key. For example, to exclude client-specific playback ID and timestamp information from the cache key, configure the following:
    
    
    cdnPolicy:
      cacheMode: CACHE_ALL_STATIC
      defaultTtl: 86400s
      cacheKeyPolicy:
        excludedQueryParameters: ["playback-id", "timestamp"]

For a given route, you can specify one of `includedQueryParameters` or `excludedQueryParameters`.

If query parameters are never used to uniquely identify content across requests, you can remove all query parameters from the cache key for a route. Do this by setting `excludeQueryString` to `true`, as follows:
    
    
    cdnPolicy:
      cacheMode: CACHE_ALL_STATIC
      defaultTtl: 3600s
      cacheKeyPolicy:
        excludeQueryString: true

If [Signed requests](https://docs.cloud.google.com/media-cdn/docs/signed-requests) are enabled on a route, query parameters used for signing are not included in the query string, and are ignored if included. Including the signed parameters in the cache key effectively makes each user request unique, and requires that each request be served from the origin.

### Query parameter sorting

Query parameters (_query strings_) are sorted by default to improve cache hit rates, because clients might re-order or otherwise request the same cached object with a different order of query parameters.

For example, the query parameters `b=world&a=hello&z=zulu&p=paris` and `p=paris&a=hello&z=zulu&b=world` are sorted as `a=hello&b=world&p=paris&z=zulu` before the cache key is derived. This allows both requests to map to the same cached object, avoiding an unnecessary request to (and response from) the origin.

If there are multiple instances of a query parameter key, each with distinct values, the parameters are sorted by their full value (for example, `a=hello` is sorted ahead of `a=world`). Sorting cannot be disabled.

### Include headers

Header names are case-insensitive and are converted to lowercase by Media CDN.

The following headers cannot be included in the cache key:

  * Any header starting with `access-control-`
  * Any header starting with `sec-fetch-`
  * `accept-encoding`
  * `accept`
  * `authorization`
  * `connection`
  * `content-md5`
  * `content-type`
  * `cookie`
  * `date`
  * `forwarded`
  * `from`
  * `host`
  * `if-match`
  * `if-modified-since`
  * `if-none-match`
  * `origin`
  * `proxy-authorization`
  * `range`
  * `referer`
  * `referrer`
  * `user-agent`
  * `want-digest`
  * `x-csrf-token`
  * `x-csrftoken`
  * `x-forwarded-for`



To include the HTTP method in the cache key, use the special header name `:method`.

### Include cookies

Cookie names are case-sensitive.

Cookies starting with `edge-cache-` in any variation of uppercase or lowercase letters cannot be used in the cache key.

### Revalidation, eviction, and expiry

Content delivery networks, including Media CDN, operate by caching the most popular content as close to users as possible.

Media CDN's extensive storage, as well as [origin shielding](https://docs.cloud.google.com/media-cdn/docs/origins#origin-shielding), limits the need to evict even unpopular content. Content that is accessed a small number of times per day might eventually be evicted.

  * Cached responses that reach their configured TTL might not be immediately evicted. For popular content, Media CDN revalidates that the cached response is the latest version by issuing a `HEAD` request to the origin to confirm that the headers have not changed.
  * Responses that set a `max-age` or an `s-maxage` cache directive or that use a TTL override to specify a high TTL value (for example, 30 days) might not be stored in cache for the full TTL. There is no guarantee that an object is stored in the cache for the full duration, especially if it is infrequently accessed.



If you are seeing a high rate of evictions, you should ensure that you have configured your cache keys to exclude parameters that don't uniquely identify a response.

## Other considerations

The following considerations might also apply with regard to caching.

### `Vary` headers

The `Vary` header indicates that the response varies depending on the client's request headers. If a `Vary` header is present in the response, Media CDN doesn't cache it, unless the header specifies either one of the headers that are configured as a cache key setting or one of the following values:

  * **Accept:** used to indicate which media types the client accepts
  * **Accept-Encoding:** used to indicate which compression types the client accepts
  * **Access-Control-Request-Headers/Access-Control-Request-Method:** used to support CORS preflight replies
  * **Origin/X-Origin:** typically used for cross-origin resource sharing
  * **X-Goog-Allowed-Resources:** supports [Google Cloud organization restriction](https://docs.cloud.google.com/storage/docs/xml-api/reference-headers#xgoogallowedresources)
  * **Sec-Fetch-Dest/Sec-Fetch-Mode/Sec-Fetch-Site:** used to [fetch metadata request headers](https://www.w3.org/TR/fetch-metadata)



Media CDN caches responses with a `Vary` header in the response by using the value of the header as part of the cache key. If the `Vary` header in the response has multiple values, they are sorted lexicographically to ensure that the cache key is deterministic.

Media CDN caches up to 100 variants for a given cache key and randomly evicts variants from the cache beyond that limit. When explicitly [invalidating](https://docs.cloud.google.com/media-cdn/docs/cache-invalidation) the cache for a given URL or cache tag, all variants are invalidated.

### Bypass the cache

You can configure the `BYPASS_CACHE` cache mode on a route to intentionally bypass the cache on matching requests. This can be useful if you need to bypass the cache for a small fraction of non-critical traffic, or debug origin connectivity.

For cases where you need to serve dynamic responses, such as API backends, we recommend configuring an [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https).

It is recommended that you generally limit use of this to debugging scenarios, to avoid unintentional origin load. Traffic egressed when bypassing the cache is priced at [internet egress rates](https://docs.cloud.google.com/vpc/network-pricing#internet_egress).

### Cache invalidation

See [cache invalidation](https://docs.cloud.google.com/media-cdn/docs/cache-invalidation).

### Byte-range requests

Media CDN supports HTTP range requests as defined in [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110#name-range-requests).

In addition, Media CDN uses range requests to fetch larger responses from the origin. This allows Media CDN to cache individual byte ranges, and does not require the entire object to be fetched at one time to be cached.

  * Objects larger than 1 MiB are fetched as byte-range requests of up to 2 MiB each.
  * Responses up to 1 MiB can be fetched without support for byte ranges at the origin.
  * Responses larger than 1 MiB aren't served if byte ranges are not supported on the origin.



Origin support for byte range requests is determined by the following:

  * An HTTP status code of 200 (OK) or 206 (Partial Content).
  * A valid `Content-Length` or `Content-Range` response header.
  * A response validator (`ETag` or `Last-Modified`).



Individual origin fill requests for each byte range are logged as discrete log entries and associated with their parent client request. You can group these requests by matching the value of `jsonPayload.cacheKeyFingerprint` for each request.

For more details about what is logged, see the [Cloud Logging documentation](https://docs.cloud.google.com/media-cdn/docs/logging).

### Multipart range requests

Media CDN supports multipart range requests, which enable users to request multiple non-contiguous segments of a file in a single HTTP request—for example, `Range: bytes=0-499, 1000-1499`.

To maximize client performance and origin offload, Media CDN can serve the requested individual byte ranges from its cache, consolidating them into a single response with an HTTP `206 Partial Response` status code to the client with the `Content-Type` set to `multipart/byteranges`.

For cacheable responses, when a client requests a multipart range, Media CDN optimizes the process by converting the request into a set of single-part range requests. Each request is sized at 2 MB to cover all the parts of byte ranges requested by the client. Media CDN then uses the responses to generate a single multipart response at the edge. This approach enables efficient cache utilization, reduces redundant origin fetches and supports high-volume use-cases, such as app store downloads and OS updates.

For non-cacheable content, Media CDN forwards the request to the origin directly.

#### Open-ended range requests

Media CDN supports "open ended" `Range` requests (for example, a request with `Range: bytes=0-`) that keep a request open against the origin until the response is closed by the origin (for example, the origin writes all bytes to the wire) or times out.

**Note:** Your origin infrastructure must also support streaming objects in response to open-ended `Range` requests before they are fully written. Some origins, such as Cloud Storage and Amazon S3, support open-ended range requests, but only serve objects after they've been fully written.

Open-ended byte ranges are typically used by clients requesting Apple's [Low-Latency HLS](https://developer.apple.com/documentation/http_live_streaming/enabling_low-latency_hls) segments: as each CMAF chunk is written to the wire, the CDN can cache and deliver that chunk to clients.

In other cases, such as when interoperability with DASH is not required, the media playlist indicates to the player which bytes represent each chunk:
    
    
      #EXTINF:4.08,
      fs270.mp4
      #EXT-X-PART:DURATION=1.02,URI="fs271.mp4",BYTERANGE=20000@0
      #EXT-X-PART:DURATION=1.02,URI="fs271.mp4",BYTERANGE=23000@20000
      #EXT-X-PART:DURATION=1.02,URI="fs271.mp4",BYTERANGE=18000@43000
      #EXT-X-PRELOAD-HINT:TYPE=PART,URI="fs271.mp4",BYTERANGE-START=61000
    

You can configure how long Media CDN waits between reads by using the `EdgeCacheOrigin.timeouts.readTimeout` configuration value. This should typically be configured to a multiple (for example, 2x) of your target duration.

### Livestream expansion

Customers using Media CDN to deliver live streaming video can enable Livestream expansion, an optional feature that further optimizes the workflow for low-latency delivery.

Livestream expansion alters the caching layers used at the edge, which helps ensure improved Quality of Experience (QoE) metrics that are critical for live events.

#### Caching Behavior with Livestream expansion

  * Object size limit: When Livestream expansion is enabled, the maximum size of an object that can be cached in the edge caches is 25 MiB.
  * Objects larger than 25 MiB: Objects exceeding the 25 MiB limit are not stored in Media CDN edge caches. By default, Media CDN proxies all requests for these objects directly to your origin server, resulting in an origin request for every client request. 
    * To protect your origin server from excessive load, you can enable an optional configuration. With this setting, Media CDN returns a `503 Service Unavailable` response for cacheable objects larger than the 25 MiB limit, instead of proxying the request to the origin.

**Note:** Livestream expansion is an allowlist-only feature and is not enabled by default. To have this feature enabled for your Media CDN service, contact your Google Cloud Sales or Account team. They can help assess suitability for your live streaming workload and initiate the enablement process.

## What's next

  * Review [advanced routing](https://docs.cloud.google.com/media-cdn/docs/routing).
  * Understand how to [connect to different origins](https://docs.cloud.google.com/media-cdn/docs/origins).
  * [Set up TLS (SSL) certificates](https://docs.cloud.google.com/media-cdn/docs/ssl-certificates) for your service.
  * Configure [signed requests](https://docs.cloud.google.com/media-cdn/docs/signed-requests) to authenticate access to content.
  * For more details about configuring `EdgeCacheService` resources by using Terraform, see the [Terraform Registry documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_services_edge_cache_service).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
