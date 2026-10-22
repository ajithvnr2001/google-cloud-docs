---
url: https://docs.cloud.google.com/media-cdn/docs/logging/
title: Request logging overview \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:12:03.833742+00:00
---

# Request logging overview  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Request logging overview Stay organized with collections  Save and categorize content based on your preferences. 

Media CDN logs each HTTP request to Cloud Logging. These requests include client requests to the `EdgeCacheService` resource and requests from the `EdgeCacheOrigin` resource to the configured origin for cache fills. Logs are typically delivered in near real time. This includes being queryable in Logging and exportable to Cloud Storage and Pub/Sub.

Log entries contain the following types of information:

  * General information shown in most Google Cloud logs, such as severity, the project ID, the project number, and the timestamp.
  * [HttpRequest](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#HttpRequest) log fields.
  * Additional metadata about the request within the structPayload, including the following:

    * Client ASN
    * Client location data
    * ID (city) of the caches used to fulfill the response
    * Time to first byte (TTFB) and time to last byte (TTLB), in milliseconds, for the HTTP-level response
    * TLS SNI hostname
    * TLS version used
    * Common Media Client Data (CMCD) information



## Cache-specific fields

The `jsonPayload` object of a Media CDN log contains metadata specific to how Media CDN serves an object, whether the object was cached, and any error states encountered.

These fields, as well as example values, are shown in the following table.

Field | Example value | Details  
---|---|---  
**backendInitialLatency** | 0.126644940s | The [Duration](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration) it takes the backend to initially respond to a request. Measured from when the CDN has finished proxying the request to the origin until the CDN begins receiving response bytes from the origin. This field appears only in logs for cache fill from an `EdgeCacheOrigin` resource.  
**backendLatency** | 0.126666342s | The Duration it takes the backend to fully respond to a request. Measured from when the CDN has finished proxying the request to the origin until the CDN has received the complete response from the backend. This field appears only in logs for cache fill from an `EdgeCacheOrigin` resource.  
**cacheId** | `maa-123456` | The IATA (airport) code of the city nearest the cache and an opaque identifier of the cache instance. If multiple tiers of caching are required to serve the request due to a full or partial cache miss, the chain of cache locations is provided—for example, `del-234567, bom-345678, sin-456789`, where the rightmost cache is the closest to the user.  
**cacheKeyFingerprint** | f63925711b0dd8a9ff861cd303774e6e | An opaque fingerprint of the cache key. Requests that map to the same cache key—for example, requests where query parameters are not included, or where the host is not included—should have the same fingerprint. If your total number of requests is similar to the total number of unique fingerprints, it might indicate that your cache keys are too specific.  
**cacheMode** | USE_ORIGIN_HEADERS | The `cdnPolicy.cacheMode` configured on the route that matched this request.   
**cacheStatus** | Cache hit: `hit` Full cache miss: `fetch, miss, miss` | The cache status at each cache node between the user and the origin shield, where the rightmost value represents the cache closest to the user. For more information about how to interpret this field, see [Cache status values](https://docs.cloud.google.com/media-cdn/docs/custom-headers#cache-status).  
**clientAsn** |  | The ASN (Autonomous System Number), based on the connecting client's IP address.   
**clientCity** | Mountain View | Name of the city from which the request originated—for example, Mountain View, California. This can also be added to both request and response headers and mirrors the `client_city` header variable.  
**clientRegionCode** | US | The country (or region) associated with the client's IP address. This is a Unicode CLDR region code, such as US or FR. For most countries, these codes correspond directly to ISO-3166-2 codes. This can also be added to both request and response headers and mirrors the `client_region` header variable.  
**cmcd** |  | The [CMCD](https://cdn.cta.tech/cta/media/media/resources/standards/pdfs/cta-5004-final.pdf) keys in the client request that help inform the client-side quality of service. Media CDN supports data transmitted through HTTP request headers or query parameters and does not log values for the following keys: `dl` (deadline), `nor` (next object request), `nrr` (next range request), `ot` (object type), `rtp` (requested maximum throughput), `sf` (streaming format), `su` (startup), `tb` (top bitrate), or `v` (CMCD version).   
**compressionAlgorithmApplied** | br | The algorithm used to compress the response referred to in this log entry. Possible values include `br` and `gzip`.   
**enforcedSecurityPolicy** |  | The [Google Cloud Armor edge security policy](https://docs.cloud.google.com/media-cdn/docs/security-policies) that applies to the client's request. This includes additional information about the policy name, the priority, and the action taken. It also includes information about Google Threat Intelligence evaluations, if applicable.   
**flexShieldingRegion** | US_EAST4 | The region used for flexible shielding, if any. This field appears only in logs for cache fill from an `EdgeCacheOrigin` resource.  
**flexShieldingStatus** | SHIELDED | The status of flexible shielding for a cache fill request. The value can be one of the following: 

  * `DEFAULT_GLOBAL`: indicates that flexible shielding isn't configured
  * `SHIELDED`: indicates that the region configured using `flexShieldingRegion` was used to serve the request
  * `SPILLED`: indicates that the region configured using `flexShieldingRegion` couldn't be used for the request; the default origin was used

This field appears only in logs for cache fill from an `EdgeCacheOrigin` resource.  
**httpTtfb** | 0.157228207s | The Duration from when the proxy begins receiving request bytes until the first byte of the response is sent (not received).   
**latency** | 0.157415635s | The Duration from when the proxy begins receiving request bytes until it has finished writing the response to the client.   
**location** |  | The `Location` header in the response.   
**metroIataCode** | MAA | The IATA (airport) code of the city nearest the proxy.   
**origin** |  | The `EdgeCacheOrigin` resource from which the response was proxied.   
**originalRequestId** | 19d92668-3948-49d8-9244-25f8252043e4 | The unique identifier assigned to the request that originally generated this response. Populated only if this is different than `request_id` for cached responses.   
**originIp** |  | The IP address used to contact the `EdgeCacheOrigin` resource from which the response was proxied.   
**previewSecurityPolicy** |  | The [Google Cloud Armor edge security policy](https://docs.cloud.google.com/media-cdn/docs/security-policies) that applies to the client's request, with the [preview rules](https://docs.cloud.google.com/armor/docs/security-policy-overview#preview_mode) taken into account. This includes additional information about the policy name, the priority, and the action taken.   
**proxyRegionCode** | US | The country (or region) that the proxy is located in. This is a Unicode CLDR region code, such as US or FR. For most countries, these codes correspond directly to ISO-3166-2 codes.   
**proxyStatus** |  | A list of intermediary HTTP proxies in the response path. The value is defined by [RFC 9209](https://www.rfc-editor.org/rfc/rfc9209). This corresponds to the `proxy_status` [dynamic header variable](https://docs.cloud.google.com/media-cdn/docs/custom-headers#header-variables).   
**rangeHeader** |  | The `Range` header in the request.   
**requestId** | 4bde6381-cd17-47e1-8c2a-1aaa424a1156 | The unique identifier assigned to the request by the proxy.   
**tlsCipherSuite** | 009C | The cipher suite negotiated during the TLS handshake. The value is four hex digits defined by the IANA TLS Cipher Suite Registry—for example, 009C for TLS_RSA_WITH_AES_128_GCM_SHA256. This value is empty for unencrypted client connections.   
**tlsSniHostname** |  | Server name indication (as defined in RFC 6066), if provided by the client during the TLS or QUIC handshake. The hostname is converted to lowercase and any trailing dot is removed.   
**tlsVersion** | TLS 1.3 | TLS version negotiated between the client and the CDN during the SSL handshake. Possible values include TLS 1, TLS 1.1, TLS 1.2, and TLS 1.3.   
  
### Example log entry

The following provides an example log entry for a response served from cache:
    
    
    {
      "insertId": "617fa16e-0000-2ac9-9993-d4f547fe67d4@a1",
      "jsonPayload": {
        "@type": "type.googleapis.com/google.cloud.edgecache.v1.EdgeCacheLogEntry",
        "tlsVersion": "TLS 1.3",
        "tlsCipherSuite": "009C",
        "cacheId": "maa-132eed13faa13",
        "clientAsn": "9299",
        "origin": "example_origin",
        "clientRegionCode": "IN",
        "metroIataCode": "bom",
        "clientCity": "Mumbai",
        "latency": "0.005105200s",
        "proxyStatus": "Google-Edge-Cache",
        "httpTtfb": "0.005056080s",
        "cacheMode": "FORCE_CACHE_ALL",
        "cacheKeyFingerprint": "c360ac18849b6336",
        "cacheStatus": "hit,stale",
        "compressionAlgorithmApplied": "br",
        "enforcedSecurityPolicy": {
          "outcome": "ACCEPT",
          "configuredAction": "ACCEPT",
          "name": "example_policy",
          "priority": 1000,
          "configuredAction": "DENY",
          "threatIntelligence": {
            "categories": [
              0: "iplist-public-clouds"
            ]
          }
        },
        "originalRequestId": "19d92668-3948-49d8-9244-25f8252043e5",
        "proxyRegionCode": "IN",
        "requestId": "4bde6381-cd17-47e1-8c2a-1aaa424a1156",
        "originIp": "74.125.128.128"
      },
      "httpRequest": {
        "requestMethod": "GET",
        "requestUrl": "https://example.com/image.jpg",
        "requestSize": "3545",
        "status": 200,
        "responseSize": "3716",
        "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
        "remoteIp": "62.36.0.43",
        "protocol": "HTTP/2"
      },
      "resource": {
        "type": "edgecache.googleapis.com/EdgeCacheRouteRule",
        "labels": {
          "matched_path": "/",
          "path_matcher_name": "routes",
          "service_name": "example_service",
          "resource_container": "projects/123456789",
          "location": "global",
          "route_destination": "projects/123456789/locations/global/edgeCacheOrigins/example_origin",
          "route_type": "ORIGIN"
        }
      },
      "timestamp": "2022-11-19T00:24:13.695328200Z",
      "logName": "projects/my-project/logs/edgecache.googleapis.com%2Fedge_cache_request",
      "receiveTimestamp": "2022-11-19T00:24:16.715871645Z"
    }

You can [configure request logging](https://docs.cloud.google.com/media-cdn/docs/configure-request-logging) in a few ways. To reduce log volume and overall Logging charges, logs can optionally be sampled or filtered as needed.

You can also [route logs to Pub/Sub, Cloud Storage, or BigQuery](https://docs.cloud.google.com/logging/docs/routing/overview) for analysis in Google Cloud or your existing log analysis tools.

## Retention policies

Logging supports setting [custom retention policies](https://docs.cloud.google.com/logging/docs/storage#logs-retention), including on a per-sink basis.

## What's next

  * To understand more about how to set up logs-based metrics to define your own metrics values based on logged requests, see the [Log-based metrics overview](https://docs.cloud.google.com/logging/docs/logs-based-metrics).
  * To learn more about the pricing for Logging, see [Google Cloud Observability pricing](https://cloud.google.com/stackdriver/pricing).
  * To read about how audit logging works and how to enable and configure audit logs for administrative activity, see the [Cloud Audit Logs documentation](https://docs.cloud.google.com/logging/docs/audit).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
