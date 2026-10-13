---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/backendBuckets/
title: REST Resource: backendBuckets \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:01:56.069104+00:00
---

# REST Resource: backendBuckets  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/backendBuckets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: backendBuckets Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: BackendBucket
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Methods



## Resource: BackendBucket

Represents a Cloud Storage Bucket resource.

This Cloud Storage bucket resource is referenced by a URL map of a load balancer. For more information, read [Backend Buckets](https://docs.cloud.google.com/load-balancing/docs/backend-bucket).

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "selfLink": string,
      "bucketName": string,
      "enableCdn": boolean,
      "cdnPolicy": {
        "signedUrlKeyNames": [
          string
        ],
        "signedUrlCacheMaxAgeSec": string,
        "requestCoalescing": boolean,
        "cacheMode": enum,
        "defaultTtl": integer,
        "maxTtl": integer,
        "clientTtl": integer,
        "negativeCaching": boolean,
        "negativeCachingPolicy": [
          {
            "code": integer,
            "ttl": integer
          }
        ],
        "bypassCacheOnRequestHeaders": [
          {
            "headerName": string
          }
        ],
        "serveWhileStale": integer,
        "cacheKeyPolicy": {
          "queryStringWhitelist": [
            string
          ],
          "includeHttpHeaders": [
            string
          ]
        }
      },
      "customResponseHeaders": [
        string
      ],
      "edgeSecurityPolicy": string,
      "compressionMode": enum,
      "loadBalancingScheme": enum,
      "params": {
        "resourceManagerTags": {
          string: string,
          ...
        }
      },
      "region": string,
      "usedBy": [
        {
          "reference": string
        }
      ]
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Unique identifier for the resource; defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`description` |  `string` An optional textual description of the resource; provided by the client when the resource is created.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`bucketName` |  `string` Cloud Storage bucket name.  
`enableCdn` |  `boolean` If true, enable Cloud CDN for this `BackendBucket`.  
`cdnPolicy` |  `object` Cloud CDN configuration for this `BackendBucket`.  
`cdnPolicy.signedUrlKeyNames[]` |  `string` Output only. Names of the keys for signing request URLs.  
`cdnPolicy.signedUrlCacheMaxAgeSec` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Maximum number of seconds the response to a signed URL request will be considered fresh. After this time period, the response will be revalidated before being served. Defaults to 1hr (3600s). When serving responses to signed URL requests, Cloud CDN will internally behave as though all responses from this backend had a `"Cache-Control: public, max-age=[TTL]"` header, regardless of any existing Cache-Control header. The actual headers served in responses will not be altered.  
`cdnPolicy.requestCoalescing` |  `boolean` If true then Cloud CDN will combine multiple concurrent cache fill requests into a small number of requests to the origin.  
`cdnPolicy.cacheMode` |  `enum` Specifies the cache setting for all responses from this backend. The possible values are:`USE_ORIGIN_HEADERS` Requires the origin to set valid caching headers to cache content. Responses without these headers will not be cached at Google's edge, and will require a full trip to the origin on every request, potentially impacting performance and increasing load on the origin server.`FORCE_CACHE_ALL` Cache all content, ignoring any "private", "no-store" or "no-cache" directives in Cache-Control response headers. Warning: this may result in Cloud CDN caching private, per-user (user identifiable) content.`CACHE_ALL_STATIC` Automatically cache static content, including common image formats, media (video and audio), and web assets (JavaScript and CSS). Requests and responses that are marked as uncacheable, as well as dynamic content (including HTML), will not be cached.If no value is provided for `cdnPolicy.cacheMode`, it defaults to `CACHE_ALL_STATIC`.  
`cdnPolicy.defaultTtl` |  `integer` Specifies the default TTL for cached content served by this origin for responses that do not have an existing valid TTL (max-age or s-maxage). Setting a TTL of "0" means "always revalidate". The value of defaultTTL cannot be set to a value greater than that of maxTTL, but can be equal. When the cacheMode is set to `FORCE_CACHE_ALL`, the defaultTTL will overwrite the TTL set in all responses. The maximum allowed value is 31,622,400s (1 year), noting that infrequently accessed objects may be evicted from the cache before the defined TTL.  
`cdnPolicy.maxTtl` |  `integer` Specifies the maximum allowed TTL for cached content served by this origin. Cache directives that attempt to set a max-age or s-maxage higher than this, or an Expires header more than maxTTL seconds in the future will be capped at the value of maxTTL, as if it were the value of an s-maxage Cache-Control directive. Headers sent to the client will not be modified. Setting a TTL of "0" means "always revalidate". The maximum allowed value is 31,622,400s (1 year), noting that infrequently accessed objects may be evicted from the cache before the defined TTL.  
`cdnPolicy.clientTtl` |  `integer` Specifies a separate client (e.g. browser client) maximum TTL. This is used to clamp the max-age (or Expires) value sent to the client. With FORCE_CACHE_ALL, the lesser of clientTtl and defaultTtl is used for the response max-age directive, along with a "public" directive. For cacheable content in CACHE_ALL_STATIC mode, clientTtl clamps the max-age from the origin (if specified), or else sets the response max-age directive to the lesser of the clientTtl and defaultTtl, and also ensures a "public" cache-control directive is present. If a client TTL is not specified, a default value (1 hour) will be used. The maximum allowed value is 31,622,400s (1 year).  
`cdnPolicy.negativeCaching` |  `boolean` Negative caching allows per-status code TTLs to be set, in order to apply fine-grained caching for common errors or redirects. This can reduce the load on your origin and improve end-user experience by reducing response latency. When the cache mode is set to CACHE_ALL_STATIC or USE_ORIGIN_HEADERS, negative caching applies to responses with the specified response code that lack any Cache-Control, Expires, or Pragma: no-cache directives. When the cache mode is set to FORCE_CACHE_ALL, negative caching applies to all responses with the specified response code, and override any caching headers. By default, Cloud CDN will apply the following default TTLs to these status codes: HTTP 300 (Multiple Choice), 301, 308 (Permanent Redirects): 10m HTTP 404 (Not Found), 410 (Gone), 451 (Unavailable For Legal Reasons): 120s HTTP 405 (Method Not Found), 501 (Not Implemented): 60s. These defaults can be overridden in negativeCachingPolicy.  
`cdnPolicy.negativeCachingPolicy[]` |  `object` Sets a cache TTL for the specified HTTP status code. negativeCaching must be enabled to configure negativeCachingPolicy. Omitting the policy and leaving negativeCaching enabled will use Cloud CDN's default cache TTLs. Note that when specifying an explicit negativeCachingPolicy, you should take care to specify a cache TTL for all response codes that you wish to cache. Cloud CDN will not apply any default negative caching when a policy exists.  
`cdnPolicy.negativeCachingPolicy[].code` |  `integer` The HTTP status code to define a TTL against. Only HTTP status codes 300, 301, 302, 307, 308, 404, 405, 410, 421, 451 and 501 can be specified as values, and you cannot specify a status code more than once.  
`cdnPolicy.negativeCachingPolicy[].ttl` |  `integer` The TTL (in seconds) for which to cache responses with the corresponding status code. The maximum allowed value is 1800s (30 minutes), noting that infrequently accessed objects may be evicted from the cache before the defined TTL.  
`cdnPolicy.bypassCacheOnRequestHeaders[]` |  `object` Bypass the cache when the specified request headers are matched - e.g. Pragma or Authorization headers. Up to 5 headers can be specified. The cache is bypassed for all cdnPolicy.cacheMode settings.  
`cdnPolicy.bypassCacheOnRequestHeaders[].headerName` |  `string` The header field name to match on when bypassing cache. Values are case-insensitive.  
`cdnPolicy.serveWhileStale` |  `integer` Serve existing content from the cache (if available) when revalidating content with the origin, or when an error is encountered when refreshing the cache. This setting defines the default "max-stale" duration for any cached responses that do not specify a max-stale directive. Stale responses that exceed the TTL configured here will not be served. The default limit (max-stale) is 86400s (1 day), which will allow stale content to be served up to this limit beyond the max-age (or s-maxage) of a cached response. The maximum allowed value is 604800 (1 week). Set this to zero (0) to disable serve-while-stale.  
`cdnPolicy.cacheKeyPolicy` |  `object` The CacheKeyPolicy for this CdnPolicy.  
`cdnPolicy.cacheKeyPolicy.queryStringWhitelist[]` |  `string` Names of query string parameters to include in cache keys. Default parameters are always included. '&' and '=' will be percent encoded and not treated as delimiters.  
`cdnPolicy.cacheKeyPolicy.includeHttpHeaders[]` |  `string` Allows HTTP request headers (by name) to be used in the cache key.  
`customResponseHeaders[]` |  `string` Headers that the Application Load Balancer should add to proxied responses.  
`edgeSecurityPolicy` |  `string` Output only. The resource URL for the edge security policy associated with this backend bucket.  
`compressionMode` |  `enum` Compress text responses using Brotli or gzip compression, based on the client's Accept-Encoding header.  
`loadBalancingScheme` |  `enum` The value can only be INTERNAL_MANAGED for cross-region internal layer 7 load balancer.If loadBalancingScheme is not specified, the backend bucket can be used by classic global external load balancers, or global application external load balancers, or both.  
`params` |  `object` Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload.  
`params.resourceManagerTags` |  `map (key: string, value: string)` Tag keys/values directly bound to this resource. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). The field is allowed for INSERT only. The keys/values to set on the resource should be specified in either ID { : } or Namespaced format { : }. For example the following are valid inputs: * {"tagKeys/333" : "tagValues/444", "tagKeys/123" : "tagValues/456"} * {"123/environment" : "production", "345/abc" : "xyz"} Note: * Invalid combinations of ID & namespaced format is not supported. For instance: {"123/environment" : "tagValues/444"} is invalid.  
`region` |  `string` Output only. URL of the region where the regional backend bucket resides. This field is not applicable to global backend buckets. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.  
`usedBy[]` |  `object` Output only. backendBuckets.list of resources referencing that backend bucket.  
`usedBy[].reference` |  `string` Output only. Server-defined URL for UrlMaps referencing that BackendBucket.  
  
## Methods  
  
---  
  
### `[addSignedUrlKey](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/backendBuckets/addSignedUrlKey)`

|  Adds a key for validating requests with signed URLs for this backend bucket.  
  
### `[aggregatedList](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/backendBuckets/aggregatedList)`

|  Retrieves the list of all BackendBucket resources, regional and global, available to the specified project.  
  
### `[delete](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/backendBuckets/delete)`

|  Deletes the specified BackendBucket resource.  
  
### `[deleteSignedUrlKey](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/backendBuckets/deleteSignedUrlKey)`

|  Deletes a key for validating requests with signed URLs for this backend bucket.  
  
### `[get](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/backendBuckets/get)`

|  Returns the specified BackendBucket resource.  
  
### `[getIamPolicy](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/backendBuckets/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[insert](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/backendBuckets/insert)`

|  Creates a BackendBucket resource in the specified project using the data included in the request.  
  
### `[list](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/backendBuckets/list)`

|  Retrieves the list of BackendBucket resources available to the specified project.  
  
### `[listUsable](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/backendBuckets/listUsable)`

|  Retrieves a list of all usable backend buckets in the specified project.  
  
### `[patch](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/backendBuckets/patch)`

|  Updates the specified BackendBucket resource with the data included in the request.  
  
### `[setEdgeSecurityPolicy](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/backendBuckets/setEdgeSecurityPolicy)`

|  Sets the edge security policy for the specified backend bucket.  
  
### `[setIamPolicy](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/backendBuckets/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/backendBuckets/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
### `[update](https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/backendBuckets/update)`

|  Updates the specified BackendBucket resource with the data included in the request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
