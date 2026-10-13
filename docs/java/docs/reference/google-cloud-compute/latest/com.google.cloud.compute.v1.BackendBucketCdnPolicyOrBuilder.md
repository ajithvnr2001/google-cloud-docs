---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketCdnPolicyOrBuilder
title: Interface BackendBucketCdnPolicyOrBuilder (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:45:18.669674+00:00
---

# Interface BackendBucketCdnPolicyOrBuilder (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketCdnPolicyOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BackendBucketCdnPolicyOrBuilder (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public interface BackendBucketCdnPolicyOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBypassCacheOnRequestHeaders(int index)
    
    
    public abstract BackendBucketCdnPolicyBypassCacheOnRequestHeader getBypassCacheOnRequestHeaders(int index)

Bypass the cache when the specified request headers are matched - e.g. Pragma or Authorization headers. Up to 5 headers can be specified. The cache is bypassed for all cdnPolicy.cacheMode settings.

` repeated .google.cloud.compute.v1.BackendBucketCdnPolicyBypassCacheOnRequestHeader bypass_cache_on_request_headers = 486203082; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackendBucketCdnPolicyBypassCacheOnRequestHeader](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketCdnPolicyBypassCacheOnRequestHeader)` |   
  
### getBypassCacheOnRequestHeadersCount()
    
    
    public abstract int getBypassCacheOnRequestHeadersCount()

Bypass the cache when the specified request headers are matched - e.g. Pragma or Authorization headers. Up to 5 headers can be specified. The cache is bypassed for all cdnPolicy.cacheMode settings.

` repeated .google.cloud.compute.v1.BackendBucketCdnPolicyBypassCacheOnRequestHeader bypass_cache_on_request_headers = 486203082; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getBypassCacheOnRequestHeadersList()
    
    
    public abstract List<BackendBucketCdnPolicyBypassCacheOnRequestHeader> getBypassCacheOnRequestHeadersList()

Bypass the cache when the specified request headers are matched - e.g. Pragma or Authorization headers. Up to 5 headers can be specified. The cache is bypassed for all cdnPolicy.cacheMode settings.

` repeated .google.cloud.compute.v1.BackendBucketCdnPolicyBypassCacheOnRequestHeader bypass_cache_on_request_headers = 486203082; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[BackendBucketCdnPolicyBypassCacheOnRequestHeader](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketCdnPolicyBypassCacheOnRequestHeader)>` |   
  
### getBypassCacheOnRequestHeadersOrBuilder(int index)
    
    
    public abstract BackendBucketCdnPolicyBypassCacheOnRequestHeaderOrBuilder getBypassCacheOnRequestHeadersOrBuilder(int index)

Bypass the cache when the specified request headers are matched - e.g. Pragma or Authorization headers. Up to 5 headers can be specified. The cache is bypassed for all cdnPolicy.cacheMode settings.

` repeated .google.cloud.compute.v1.BackendBucketCdnPolicyBypassCacheOnRequestHeader bypass_cache_on_request_headers = 486203082; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackendBucketCdnPolicyBypassCacheOnRequestHeaderOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketCdnPolicyBypassCacheOnRequestHeaderOrBuilder)` |   
  
### getBypassCacheOnRequestHeadersOrBuilderList()
    
    
    public abstract List<? extends BackendBucketCdnPolicyBypassCacheOnRequestHeaderOrBuilder> getBypassCacheOnRequestHeadersOrBuilderList()

Bypass the cache when the specified request headers are matched - e.g. Pragma or Authorization headers. Up to 5 headers can be specified. The cache is bypassed for all cdnPolicy.cacheMode settings.

` repeated .google.cloud.compute.v1.BackendBucketCdnPolicyBypassCacheOnRequestHeader bypass_cache_on_request_headers = 486203082; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.compute.v1.BackendBucketCdnPolicyBypassCacheOnRequestHeaderOrBuilder>` |   
  
### getCacheKeyPolicy()
    
    
    public abstract BackendBucketCdnPolicyCacheKeyPolicy getCacheKeyPolicy()

The CacheKeyPolicy for this CdnPolicy.

` optional .google.cloud.compute.v1.BackendBucketCdnPolicyCacheKeyPolicy cache_key_policy = 159263727; `

**Returns**  
---  
**Type** | **Description**  
`[BackendBucketCdnPolicyCacheKeyPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketCdnPolicyCacheKeyPolicy)` | The cacheKeyPolicy.  
  
### getCacheKeyPolicyOrBuilder()
    
    
    public abstract BackendBucketCdnPolicyCacheKeyPolicyOrBuilder getCacheKeyPolicyOrBuilder()

The CacheKeyPolicy for this CdnPolicy.

` optional .google.cloud.compute.v1.BackendBucketCdnPolicyCacheKeyPolicy cache_key_policy = 159263727; `

**Returns**  
---  
**Type** | **Description**  
`[BackendBucketCdnPolicyCacheKeyPolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketCdnPolicyCacheKeyPolicyOrBuilder)` |   
  
### getCacheMode()
    
    
    public abstract String getCacheMode()

Specifies the cache setting for all responses from this backend. The possible values are: USE_ORIGIN_HEADERS Requires the origin to set valid caching headers to cache content. Responses without these headers will not be cached at Google's edge, and will require a full trip to the origin on every request, potentially impacting performance and increasing load on the origin server. FORCE_CACHE_ALL Cache all content, ignoring any "private", "no-store" or "no-cache" directives in Cache-Control response headers. Warning: this may result in Cloud CDN caching private, per-user (user identifiable) content. CACHE_ALL_STATIC Automatically cache static content, including common image formats, media (video and audio), and web assets (JavaScript and CSS). Requests and responses that are marked as uncacheable, as well as dynamic content (including HTML), will not be cached.

If no value is provided for cdnPolicy.cacheMode, it defaults to CACHE_ALL_STATIC. Check the CacheMode enum for the list of possible values.

`optional string cache_mode = 28877888;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The cacheMode.  
  
### getCacheModeBytes()
    
    
    public abstract ByteString getCacheModeBytes()

Specifies the cache setting for all responses from this backend. The possible values are: USE_ORIGIN_HEADERS Requires the origin to set valid caching headers to cache content. Responses without these headers will not be cached at Google's edge, and will require a full trip to the origin on every request, potentially impacting performance and increasing load on the origin server. FORCE_CACHE_ALL Cache all content, ignoring any "private", "no-store" or "no-cache" directives in Cache-Control response headers. Warning: this may result in Cloud CDN caching private, per-user (user identifiable) content. CACHE_ALL_STATIC Automatically cache static content, including common image formats, media (video and audio), and web assets (JavaScript and CSS). Requests and responses that are marked as uncacheable, as well as dynamic content (including HTML), will not be cached.

If no value is provided for cdnPolicy.cacheMode, it defaults to CACHE_ALL_STATIC. Check the CacheMode enum for the list of possible values.

`optional string cache_mode = 28877888;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for cacheMode.  
  
### getClientTtl()
    
    
    public abstract int getClientTtl()

Specifies a separate client (e.g. browser client) maximum TTL. This is used to clamp the max-age (or Expires) value sent to the client. With FORCE_CACHE_ALL, the lesser of client_ttl and default_ttl is used for the response max-age directive, along with a "public" directive. For cacheable content in CACHE_ALL_STATIC mode, client_ttl clamps the max-age from the origin (if specified), or else sets the response max-age directive to the lesser of the client_ttl and default_ttl, and also ensures a "public" cache-control directive is present. If a client TTL is not specified, a default value (1 hour) will be used. The maximum allowed value is 31,622,400s (1 year).

`optional int32 client_ttl = 29034360;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The clientTtl.  
  
### getDefaultTtl()
    
    
    public abstract int getDefaultTtl()

Specifies the default TTL for cached content served by this origin for responses that do not have an existing valid TTL (max-age or s-maxage). Setting a TTL of "0" means "always revalidate". The value of defaultTTL cannot be set to a value greater than that of maxTTL, but can be equal. When the cacheMode is set to FORCE_CACHE_ALL, the defaultTTL will overwrite the TTL set in all responses. The maximum allowed value is 31,622,400s (1 year), noting that infrequently accessed objects may be evicted from the cache before the defined TTL.

`optional int32 default_ttl = 100253422;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The defaultTtl.  
  
### getMaxTtl()
    
    
    public abstract int getMaxTtl()

Specifies the maximum allowed TTL for cached content served by this origin. Cache directives that attempt to set a max-age or s-maxage higher than this, or an Expires header more than maxTTL seconds in the future will be capped at the value of maxTTL, as if it were the value of an s-maxage Cache-Control directive. Headers sent to the client will not be modified. Setting a TTL of "0" means "always revalidate". The maximum allowed value is 31,622,400s (1 year), noting that infrequently accessed objects may be evicted from the cache before the defined TTL.

`optional int32 max_ttl = 307578001;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxTtl.  
  
### getNegativeCaching()
    
    
    public abstract boolean getNegativeCaching()

Negative caching allows per-status code TTLs to be set, in order to apply fine-grained caching for common errors or redirects. This can reduce the load on your origin and improve end-user experience by reducing response latency. When the cache mode is set to CACHE_ALL_STATIC or USE_ORIGIN_HEADERS, negative caching applies to responses with the specified response code that lack any Cache-Control, Expires, or Pragma: no-cache directives. When the cache mode is set to FORCE_CACHE_ALL, negative caching applies to all responses with the specified response code, and override any caching headers. By default, Cloud CDN will apply the following default TTLs to these status codes: HTTP 300 (Multiple Choice), 301, 308 (Permanent Redirects): 10m HTTP 404 (Not Found), 410 (Gone), 451 (Unavailable For Legal Reasons): 120s HTTP 405 (Method Not Found), 501 (Not Implemented): 60s. These defaults can be overridden in negative_caching_policy.

`optional bool negative_caching = 336110005;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The negativeCaching.  
  
### getNegativeCachingPolicy(int index)
    
    
    public abstract BackendBucketCdnPolicyNegativeCachingPolicy getNegativeCachingPolicy(int index)

Sets a cache TTL for the specified HTTP status code. negative_caching must be enabled to configure negative_caching_policy. Omitting the policy and leaving negative_caching enabled will use Cloud CDN's default cache TTLs. Note that when specifying an explicit negative_caching_policy, you should take care to specify a cache TTL for all response codes that you wish to cache. Cloud CDN will not apply any default negative caching when a policy exists.

` repeated .google.cloud.compute.v1.BackendBucketCdnPolicyNegativeCachingPolicy negative_caching_policy = 155359996; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackendBucketCdnPolicyNegativeCachingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketCdnPolicyNegativeCachingPolicy)` |   
  
### getNegativeCachingPolicyCount()
    
    
    public abstract int getNegativeCachingPolicyCount()

Sets a cache TTL for the specified HTTP status code. negative_caching must be enabled to configure negative_caching_policy. Omitting the policy and leaving negative_caching enabled will use Cloud CDN's default cache TTLs. Note that when specifying an explicit negative_caching_policy, you should take care to specify a cache TTL for all response codes that you wish to cache. Cloud CDN will not apply any default negative caching when a policy exists.

` repeated .google.cloud.compute.v1.BackendBucketCdnPolicyNegativeCachingPolicy negative_caching_policy = 155359996; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getNegativeCachingPolicyList()
    
    
    public abstract List<BackendBucketCdnPolicyNegativeCachingPolicy> getNegativeCachingPolicyList()

Sets a cache TTL for the specified HTTP status code. negative_caching must be enabled to configure negative_caching_policy. Omitting the policy and leaving negative_caching enabled will use Cloud CDN's default cache TTLs. Note that when specifying an explicit negative_caching_policy, you should take care to specify a cache TTL for all response codes that you wish to cache. Cloud CDN will not apply any default negative caching when a policy exists.

` repeated .google.cloud.compute.v1.BackendBucketCdnPolicyNegativeCachingPolicy negative_caching_policy = 155359996; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[BackendBucketCdnPolicyNegativeCachingPolicy](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketCdnPolicyNegativeCachingPolicy)>` |   
  
### getNegativeCachingPolicyOrBuilder(int index)
    
    
    public abstract BackendBucketCdnPolicyNegativeCachingPolicyOrBuilder getNegativeCachingPolicyOrBuilder(int index)

Sets a cache TTL for the specified HTTP status code. negative_caching must be enabled to configure negative_caching_policy. Omitting the policy and leaving negative_caching enabled will use Cloud CDN's default cache TTLs. Note that when specifying an explicit negative_caching_policy, you should take care to specify a cache TTL for all response codes that you wish to cache. Cloud CDN will not apply any default negative caching when a policy exists.

` repeated .google.cloud.compute.v1.BackendBucketCdnPolicyNegativeCachingPolicy negative_caching_policy = 155359996; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[BackendBucketCdnPolicyNegativeCachingPolicyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.BackendBucketCdnPolicyNegativeCachingPolicyOrBuilder)` |   
  
### getNegativeCachingPolicyOrBuilderList()
    
    
    public abstract List<? extends BackendBucketCdnPolicyNegativeCachingPolicyOrBuilder> getNegativeCachingPolicyOrBuilderList()

Sets a cache TTL for the specified HTTP status code. negative_caching must be enabled to configure negative_caching_policy. Omitting the policy and leaving negative_caching enabled will use Cloud CDN's default cache TTLs. Note that when specifying an explicit negative_caching_policy, you should take care to specify a cache TTL for all response codes that you wish to cache. Cloud CDN will not apply any default negative caching when a policy exists.

` repeated .google.cloud.compute.v1.BackendBucketCdnPolicyNegativeCachingPolicy negative_caching_policy = 155359996; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.compute.v1.BackendBucketCdnPolicyNegativeCachingPolicyOrBuilder>` |   
  
### getRequestCoalescing()
    
    
    public abstract boolean getRequestCoalescing()

If true then Cloud CDN will combine multiple concurrent cache fill requests into a small number of requests to the origin.

`optional bool request_coalescing = 532808276;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The requestCoalescing.  
  
### getServeWhileStale()
    
    
    public abstract int getServeWhileStale()

Serve existing content from the cache (if available) when revalidating content with the origin, or when an error is encountered when refreshing the cache. This setting defines the default "max-stale" duration for any cached responses that do not specify a max-stale directive. Stale responses that exceed the TTL configured here will not be served. The default limit (max-stale) is 86400s (1 day), which will allow stale content to be served up to this limit beyond the max-age (or s-maxage) of a cached response. The maximum allowed value is 604800 (1 week). Set this to zero (0) to disable serve-while-stale.

`optional int32 serve_while_stale = 236682203;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The serveWhileStale.  
  
### getSignedUrlCacheMaxAgeSec()
    
    
    public abstract long getSignedUrlCacheMaxAgeSec()

Maximum number of seconds the response to a signed URL request will be considered fresh. After this time period, the response will be revalidated before being served. Defaults to 1hr (3600s). When serving responses to signed URL requests, Cloud CDN will internally behave as though all responses from this backend had a "Cache-Control: public, max-age=[TTL]" header, regardless of any existing Cache-Control header. The actual headers served in responses will not be altered.

`optional int64 signed_url_cache_max_age_sec = 269374534;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The signedUrlCacheMaxAgeSec.  
  
### getSignedUrlKeyNames(int index)
    
    
    public abstract String getSignedUrlKeyNames(int index)

[Output Only] Names of the keys for signing request URLs.

`repeated string signed_url_key_names = 371848885;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The signedUrlKeyNames at the given index.  
  
### getSignedUrlKeyNamesBytes(int index)
    
    
    public abstract ByteString getSignedUrlKeyNamesBytes(int index)

[Output Only] Names of the keys for signing request URLs.

`repeated string signed_url_key_names = 371848885;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the signedUrlKeyNames at the given index.  
  
### getSignedUrlKeyNamesCount()
    
    
    public abstract int getSignedUrlKeyNamesCount()

[Output Only] Names of the keys for signing request URLs.

`repeated string signed_url_key_names = 371848885;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of signedUrlKeyNames.  
  
### getSignedUrlKeyNamesList()
    
    
    public abstract List<String> getSignedUrlKeyNamesList()

[Output Only] Names of the keys for signing request URLs.

`repeated string signed_url_key_names = 371848885;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the signedUrlKeyNames.  
  
### hasCacheKeyPolicy()
    
    
    public abstract boolean hasCacheKeyPolicy()

The CacheKeyPolicy for this CdnPolicy.

` optional .google.cloud.compute.v1.BackendBucketCdnPolicyCacheKeyPolicy cache_key_policy = 159263727; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cacheKeyPolicy field is set.  
  
### hasCacheMode()
    
    
    public abstract boolean hasCacheMode()

Specifies the cache setting for all responses from this backend. The possible values are: USE_ORIGIN_HEADERS Requires the origin to set valid caching headers to cache content. Responses without these headers will not be cached at Google's edge, and will require a full trip to the origin on every request, potentially impacting performance and increasing load on the origin server. FORCE_CACHE_ALL Cache all content, ignoring any "private", "no-store" or "no-cache" directives in Cache-Control response headers. Warning: this may result in Cloud CDN caching private, per-user (user identifiable) content. CACHE_ALL_STATIC Automatically cache static content, including common image formats, media (video and audio), and web assets (JavaScript and CSS). Requests and responses that are marked as uncacheable, as well as dynamic content (including HTML), will not be cached.

If no value is provided for cdnPolicy.cacheMode, it defaults to CACHE_ALL_STATIC. Check the CacheMode enum for the list of possible values.

`optional string cache_mode = 28877888;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cacheMode field is set.  
  
### hasClientTtl()
    
    
    public abstract boolean hasClientTtl()

Specifies a separate client (e.g. browser client) maximum TTL. This is used to clamp the max-age (or Expires) value sent to the client. With FORCE_CACHE_ALL, the lesser of client_ttl and default_ttl is used for the response max-age directive, along with a "public" directive. For cacheable content in CACHE_ALL_STATIC mode, client_ttl clamps the max-age from the origin (if specified), or else sets the response max-age directive to the lesser of the client_ttl and default_ttl, and also ensures a "public" cache-control directive is present. If a client TTL is not specified, a default value (1 hour) will be used. The maximum allowed value is 31,622,400s (1 year).

`optional int32 client_ttl = 29034360;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the clientTtl field is set.  
  
### hasDefaultTtl()
    
    
    public abstract boolean hasDefaultTtl()

Specifies the default TTL for cached content served by this origin for responses that do not have an existing valid TTL (max-age or s-maxage). Setting a TTL of "0" means "always revalidate". The value of defaultTTL cannot be set to a value greater than that of maxTTL, but can be equal. When the cacheMode is set to FORCE_CACHE_ALL, the defaultTTL will overwrite the TTL set in all responses. The maximum allowed value is 31,622,400s (1 year), noting that infrequently accessed objects may be evicted from the cache before the defined TTL.

`optional int32 default_ttl = 100253422;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the defaultTtl field is set.  
  
### hasMaxTtl()
    
    
    public abstract boolean hasMaxTtl()

Specifies the maximum allowed TTL for cached content served by this origin. Cache directives that attempt to set a max-age or s-maxage higher than this, or an Expires header more than maxTTL seconds in the future will be capped at the value of maxTTL, as if it were the value of an s-maxage Cache-Control directive. Headers sent to the client will not be modified. Setting a TTL of "0" means "always revalidate". The maximum allowed value is 31,622,400s (1 year), noting that infrequently accessed objects may be evicted from the cache before the defined TTL.

`optional int32 max_ttl = 307578001;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the maxTtl field is set.  
  
### hasNegativeCaching()
    
    
    public abstract boolean hasNegativeCaching()

Negative caching allows per-status code TTLs to be set, in order to apply fine-grained caching for common errors or redirects. This can reduce the load on your origin and improve end-user experience by reducing response latency. When the cache mode is set to CACHE_ALL_STATIC or USE_ORIGIN_HEADERS, negative caching applies to responses with the specified response code that lack any Cache-Control, Expires, or Pragma: no-cache directives. When the cache mode is set to FORCE_CACHE_ALL, negative caching applies to all responses with the specified response code, and override any caching headers. By default, Cloud CDN will apply the following default TTLs to these status codes: HTTP 300 (Multiple Choice), 301, 308 (Permanent Redirects): 10m HTTP 404 (Not Found), 410 (Gone), 451 (Unavailable For Legal Reasons): 120s HTTP 405 (Method Not Found), 501 (Not Implemented): 60s. These defaults can be overridden in negative_caching_policy.

`optional bool negative_caching = 336110005;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the negativeCaching field is set.  
  
### hasRequestCoalescing()
    
    
    public abstract boolean hasRequestCoalescing()

If true then Cloud CDN will combine multiple concurrent cache fill requests into a small number of requests to the origin.

`optional bool request_coalescing = 532808276;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the requestCoalescing field is set.  
  
### hasServeWhileStale()
    
    
    public abstract boolean hasServeWhileStale()

Serve existing content from the cache (if available) when revalidating content with the origin, or when an error is encountered when refreshing the cache. This setting defines the default "max-stale" duration for any cached responses that do not specify a max-stale directive. Stale responses that exceed the TTL configured here will not be served. The default limit (max-stale) is 86400s (1 day), which will allow stale content to be served up to this limit beyond the max-age (or s-maxage) of a cached response. The maximum allowed value is 604800 (1 week). Set this to zero (0) to disable serve-while-stale.

`optional int32 serve_while_stale = 236682203;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the serveWhileStale field is set.  
  
### hasSignedUrlCacheMaxAgeSec()
    
    
    public abstract boolean hasSignedUrlCacheMaxAgeSec()

Maximum number of seconds the response to a signed URL request will be considered fresh. After this time period, the response will be revalidated before being served. Defaults to 1hr (3600s). When serving responses to signed URL requests, Cloud CDN will internally behave as though all responses from this backend had a "Cache-Control: public, max-age=[TTL]" header, regardless of any existing Cache-Control header. The actual headers served in responses will not be altered.

`optional int64 signed_url_cache_max_age_sec = 269374534;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the signedUrlCacheMaxAgeSec field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
