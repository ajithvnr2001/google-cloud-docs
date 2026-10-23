---
url: https://docs.cloud.google.com/media-cdn/docs/custom-headers/
title: Define custom headers \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:58.618213+00:00
---

# Define custom headers  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/custom-headers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Define custom headers Stay organized with collections  Save and categorize content based on your preferences. 

Media CDN lets you specify custom request and response headers.

Custom headers let you do the following:

  * Return geographic data about the client, such as country, region, or city, that you can use to show localized content.
  * Determine whether a response was served from cache (in full or in part) and which cache location it was served from.
  * Remove, replace, or append to both request and response headers.



## Set custom headers

Headers are set on each route, which lets you add and remove headers for different content, such as manifests or video segments.

Set per-route custom request headers early in the CDN processing path, prior to caching decisions. For example, if you set a `cache-control` header as a per-route custom header, it affects caching behavior in the CDN.

By default, added header values are comma-separated and appended to the response or request headers with the same field names.

To overwrite existing values, set `replace` to `true`.

###  gcloud and YAML 

To list the YAML configuration for the `EdgeCacheService` resource, use the following command:
    
    
    gcloud edge-cache services describe prod-media-service
    

The `.routing.pathMatchers[].routeRules[].headerAction` section shows the headers to be added and removed:
    
    
    routeRules:
    - priority: 1
       description: "video routes"
       matchRules:
          - prefixMatch: "/video/"
       headerAction:
          responseHeadersToAdd:
          # Return the country (or region) associated with the client's IP address.
          - headerName: "client-geo"
             headerValue: "{client_region}"
             replace: true
          requestHeadersToAdd:
          # Inform the upstream origin server the request is from Media CDN
          - headerName: "x-downstream-cdn"
             headerValue: "Media CDN"
          responseHeadersToRemove:
          - headerName: "X-User-ID"
          - headerName: "X-Other-Internal-Header"
    

###  Terraform 

The following Terraform snippet shows a route rule with custom headers.
    
    
    route_rule {
      description = "video routes"
      priority    = 1
      match_rule {
        prefix_match = "/video/"
      }
      origin = google_network_services_edge_cache_origin.default.name
    **header_action {**
    **response_header_to_add {**
    **# Return the country (or region) associated with the client's IP address.**
    **header_name  = "client-geo"**
    **header_value = "{client_region}"**
    **replace      = true**
    **}**
    **request_header_to_add {**
    **# Inform the upstream origin server that the request is from Media CDN.**
    **header_name  = "x-downstream-cdn"**
    **header_value = "Media CDN"**
    **}**
    **response_header_to_remove {**
    **header_name = "X-User-ID"**
    **}**
    **response_header_to_remove {**
    **header_name = "X-Other-Internal-Header"**
    **}**
      }
    }

This example does the following:

  * Adds a custom `client-geo` header to the response by using the `{client_region}` variable, which returns the country (or region) associated with the client's IP address.
  * Adds a custom `x-downstream-cdn` header to the request by using a static string.
  * Removes two internal headers.



To configure origin-specific custom headers, see [Configure origin-specific host rewrites or header modifications](https://docs.cloud.google.com/media-cdn/docs/configure-origin#configure-rewrites).

## Dynamic header variables

Custom headers can contain one or more dynamic variables.

Request headers that are a part of cache key policy (`cacheKeyPolicy.includedHeaderNames`) can contain one or more custom variables. Request headers that contain other dynamic variables can't be a part of the cache key.

Variable | Description | Supported for request headers | Supported for request headers in a cache key | Supported for response headers  
---|---|---|---|---  
`cdn_cache_status` | A comma-separated list of the locations (IATA code of the nearest airport) and statuses of each cache node in the request/response path, where the rightmost value represents the cache closest to the user. |  |  | ✔  
`client_city` | The name of the city from which the request originated—for example, `Mountain View` for Mountain View, California. There is no canonical list of valid values for this variable. The city names can contain US-ASCII letters, numbers, spaces, and the following characters: `!#$%&'*+-.^_`|~`. | ✔ |  | ✔  
`client_city_lat_long` | The latitude and longitude of the city from which the request originated—for example, `37.386051,-122.083851` for a request from Mountain View. | ✔ |  | ✔  
`client_region` | The country (or region) associated with the client's IP address. This is a Unicode CLDR region code, such as `US` or `FR`. For most countries, these codes correspond directly to [ISO-3166-1 alpha-2 codes](https://wikipedia.org/wiki/ISO_3166-1_alpha-2). | ✔ | ✔ | ✔  
`client_region_subdivision` | The subdivision—for example, the province or state—of the country associated with the client's IP address. This is a Unicode CLDR subdivision ID, such as `USCA` or `CAON`. These Unicode codes are derived from the subdivisions defined by the [ISO-3166-2 standard](https://en.wikipedia.org/wiki/ISO_3166-2). | ✔ | ✔ | ✔  
`client_rtt_msec` | The estimated round-trip transmission time between the CDN and the HTTP(S) client, in milliseconds. This is the smoothed round-trip time (SRTT) parameter measured by the CDN's TCP stack, per [RFC 2988](https://tools.ietf.org/html/rfc2988). | ✔ |  | ✔  
`device_request_type` | The type of device that the client is using. These are the valid values: `DESKTOP`, `MOBILE`, `TABLET`, `SMART_TV`, `GAME_CONSOLE`, `WEARABLE`, and `UNDETERMINED`. | ✔ | ✔ |   
`edge_location_country_code` | Identifies the geographical country/region of the specific Media CDN edge cache server that is serving the client's request. This is an ISO 3166-1 alpha-2 country code, such as `US` or `JP`. These two-letter codes are derived from the official country codes defined by the [ISO 3166-1 standard](https://www.iso.org/obp/ui/). | ✔ |  | ✔  
`host` | The host and port number of the server to which the client request was originally sent, corresponding to the value of the `Host` request header for HTTP/1.1 or the `:authority` pseudo-header for HTTP/2. | ✔ |  | ✔  
`original_request_id` | The unique identifier assigned to the request that originally generated this response. Populated only if this is different than `request_id` for cached responses. |  |  | ✔  
`origin_name` | The `EdgeCacheOrigin` resource from which the response was proxied. |  |  | ✔  
`origin_request_header` | Reflects the value of the Origin header in the request for Cross-Origin Resource Sharing (CORS) use cases. |  |  | ✔  
`proxy_status` | A list of intermediary HTTP proxies in the response path. The value is defined by [RFC 9209](https://www.rfc-editor.org/rfc/rfc9209). An `EdgeCacheService` resource is represented by `Google-Edge-Cache`. If the response was fetched from the origin, an `EdgeCacheOrigin` resource is represented by `Google-Edge-Cache-Origin`. |  |  | ✔  
`tls_sni_hostname` | The server name indication (as defined in [RFC 6066](https://tools.ietf.org/html/rfc6066.html)), if provided by the client during the TLS or QUIC handshake. The hostname is converted to lowercase, and any trailing dot is removed. | ✔ |  | ✔  
`tls_version` | The TLS version negotiated between the client and the load balancer during the SSL handshake. Possible values include `TLSv1`, `TLSv1.1`, `TLSv1.2`, and `TLSv1.3`. If the client connects by using QUIC instead of TLS, the value is QUIC. | ✔ |  | ✔  
`tls_cipher_suite` | The cipher suite negotiated during the TLS handshake. The value is defined by the [IANA TLS Cipher Suite Registry](https://www.iana.org/assignments/tls-parameters/tls-parameters.xhtml)—for example, `TLS_RSA_WITH_AES_128_GCM_SHA256`. This value is empty for QUIC and unencrypted client connections. | ✔ |  | ✔  
`user_agent_family` | The browser family that the client is using. These are the valid values: `APPLE`, `APPLEWEBKIT`, `BLACKBERRY`, `DOCOMO`, `GECKO`, `GOOGLE`, `KHTML`, `KOREAN`, `MICROSOFT`, `MSIE`, `NOKIA`, `NETFRONT`, `OBIGO`, `OPENWAVE`, `OPERA`, `OTHER`, `POLARIS`, `TELECA`, `SEMC`, `SMIT`, and `USER_DEFINED`. | ✔ | ✔ |   
  
The following considerations apply to custom variables:

  * Existing request and response headers are preserved, except for the following, which are removed:

    * `X-User-IP`
    * Any headers with `X-Google` or `X-GFE`
  * Header keys and values must be compliant with [RFC 7230](https://tools.ietf.org/html/rfc7230), with obsolete forms disallowed.

  * All header keys are lowercased (per HTTP/2).

  * Some headers are coalesced. When there are multiple instances of the same header key (for example, `Via`), the load balancer combines their values into a single comma-separated list for a single header key. Only the headers whose values can be represented as a comma-separated list are coalesced. Other headers, such as `Set-Cookie`, are never coalesced.

  * Some headers are added, or values are appended to them. Media CDN always adds or modifies certain headers, such as `X-Forwarded-For`.

  * Media CDN expands any response header with a supported variable, even if set by the client or origin. This lets you set dynamic headers from your client (such as a video player) or origin infrastructure, in addition to configuring custom headers.

  * As an example, as per the rules described earlier, `X-Goog-` and `X-Amz-` headers are preserved and lowercased.




## Cache status values

The `{cdn_cache_status}` header variable can return multiple values corresponding to the tier of cache that served the response. Consider the following guidelines for interpreting the `{cdn_cache_status}` header variable:

  * If the header contains `hit`, the requested content was retrieved from the cache.
  * If the header contains `miss`, the requested content was not found in a cache node and had to be retrieved from an upstream node.
  * If the header contains `chunked`, the requested content was not found in a cache node and had to be retrieved from an upstream node, and the upstream response did not include a `Content-Length` header.
  * If the header contains `fetch`, the requested content was retrieved from the origin.
  * If the header contains `bypassed`, the cache was bypassed by request configuration.
  * If the header contains `uncacheable`, the requested content was considered uncacheable by some or all components of the caching infrastructure.

    * If the header also contains `hit` or `miss`, the requested content was considered uncacheable by some caching components and cacheable by others.
    * If the header does not also contain `hit` or `miss`, the requested content was considered uncacheable by all caching components, and all requests for this content are fetched from the origin. To ensure that your content is cached appropriately, review the Media CDN [origin requirements](https://docs.cloud.google.com/media-cdn/docs/origins#origin-requirements).



## Default headers

Media CDN adds the following request and response headers to origin requests and client responses, respectively.

Header | Description | Request | Response  
---|---|---|---  
`x-request-id` | A unique identifier for the given request. This value is also added to the request log as `jsonPayload.requestId`, which lets you correlate a client request/response to a log entry. |  | ✔  
`age` | Returns the age of the cached object (number of seconds it has been in the cache). The age is typically calculated based on when the object was initially cached in a long-tail (shield) cache location. Responses without an `age` header are not served from cache. |  | ✔  
`server` | Is set as `Google-Edge-Cache`. |  | ✔  
`cdn-loop` | Identifies _loops_ —for example, where the origin host is the same as the user-facing (edge) host. A token of `google` is appended to the header as per RFC 8586. The token cannot be changed. | ✔ |   
`forwarded` | The structured version of the `x-forwarded-for` header. The `forwarded` header is [defined in RFC 7239](https://tools.ietf.org/html/rfc7239#section-4). These headers allow you to identify the IP address of the connecting client when a proxy (or proxies) are in the path. For example, if a client with IP address `192.0.2.60` connects to Media CDN over HTTPS, the `forwarded` header is populated as follows: `forwarded: [for=192.0.2.60;proto=https]` In the case of multiple client-side proxies, the client that connected to Media CDN is the last address appended in the header value. | ✔ |   
`x-forwarded-for` | The unstructured and de-facto standard version of the `forwarded` header. Values are typically comma-separated. Both headers are sent in a request to support legacy origins that might not be aware of the `forwarded` header. | ✔ |   
  
Header keys are lowercased for both request and response headers because header keys are case-insensitive.

Other headers, including the edge point of presence (PoP) location and cache status (such as `hit` and `miss`), can be added by using dynamic header variables.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
