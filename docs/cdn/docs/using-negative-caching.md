---
url: https://docs.cloud.google.com/cdn/docs/using-negative-caching/
title: Use negative caching \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:41.117750+00:00
---

# Use negative caching  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/using-negative-caching/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Use negative caching Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for using negative caching with Cloud CDN. Negative caching lets you set a different time to live (TTL) for each status code.

The reason to do this is to apply fine-grained control over caching for common errors or redirects. This can reduce the load on your origins and improve the end-user experience by reducing response latency.

## Before you begin

  * Read about [cache modes and static content](https://docs.cloud.google.com/cdn/docs/caching#cache-modes).

  * Ensure that Cloud CDN is enabled; for instructions, see [Using Cloud CDN](https://docs.cloud.google.com/cdn/docs/using-cdn).

  * If necessary, update to the latest version of the Google Cloud CLI:
        
        gcloud components update
        

**Note:** Make sure that you're using gcloud CLI version `316.0.0` or later.



## Status codes and default TTLs

Negative caching applies to specific status codes, which are listed in the following table.

**Note:** The TTL values for HTTP success codes (HTTP 2xx) are controlled by the values of [default TTL and max TTL](https://docs.cloud.google.com/cdn/docs/using-ttl-overrides).

Cloud CDN applies the following default TTLs to these status codes:

Status code | Meaning | TTL  
---|---|---  
HTTP 300 | Multiple choices | 10 minutes  
HTTP 301 and 308 | Permanent redirects | 10 minutes  
HTTP 302 and 307 | Temporary redirects | Not cached by default  
HTTP 404 | Not found | 120 seconds  
HTTP 405 | Method not found | 60 seconds  
HTTP 410 | Gone | 120 seconds  
HTTP 451 | Unavailable for legal reasons | 120 seconds  
HTTP 501 | Not implemented | 60 seconds  
  
You can override these default values by using negative caching to set a cache TTL for the specified HTTP status code.

## Setting up negative caching

Negative caching lets you configure your service to cache failures as well as successes. This allows Cloud CDN to shield origins from requests that generate errors (like 404 Not Found) in the same way that it shields origins from requests that generate successful responses.

### Console

  1. In the Google Cloud console, go to the **Load Balancing** page. 

[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click the name of your external Application Load Balancer.
  3. Click **Edit** edit.
  4. In **Backend configuration** , select a backend and click **Edit** edit.
  5. Make sure that **Enable Cloud CDN** is selected.
  6. At the bottom of the window, click **Advanced configurations**.
  7. Click **Enable negative caching**.
  8. Click **Add negative caching policy**. 
     1. Enter an **HTTP status code**.
     2. Select a **Cache time to live (TTL)**.
  9. Click **Update**.
  10. Click **Update** again.



### gcloud

For backend buckets, use the [gcloud compute backend-buckets create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/create) or [gcloud compute backend-buckets update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update) command with the `--negative-caching` flag.

For backend services, use the [gcloud compute backend-services create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) or [gcloud compute backend-services update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update) command with the `--negative-caching` flag.
    
    
    gcloud compute backend-buckets (create | update) BACKEND_BUCKET_NAME
        --negative-caching
    
    
    
    gcloud compute backend-services (create | update) BACKEND_SERVICE_NAME
        --negative-caching
    

To enable negative caching of only two specific error responses, for example, set responses with status code `404` to be cached for 60 seconds, and responses with status code `405` to be cached for 120 seconds.
    
    
    gcloud compute backend-services update BACKEND_SERVICE_NAME \
        --negative-caching \
        --cache-mode=CACHE_ALL_STATIC \
        --default-ttl=86400 \
        --negative-caching-policy='404=60,405=120'
    

### api

For backend buckets, use the [Method: backendBuckets.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendBuckets/insert) or [Method: backendBuckets.update](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendBuckets/update) API call.

For backend services, use the [Method: backendServices.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/insert) or [Method: backendServices.update](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/update) API call.

Use one of the following API calls:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/BACKEND_BUCKET
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE
    

Add the following snippet to the JSON request body:
    
    
    "cdnPolicy": {
      "negativeCaching": ON,
      "negativeCachingPolicy": [
        {
          "code": STATUS_CODE,
          "ttl": TTL_SECONDS
        }
      ]
    }
    

Negative caching must be enabled to configure the `negativeCachingPolicy` settings. If you omit the policy and have `negativeCaching` enabled, Cloud CDN uses the default values listed in Status codes and default TTLs.

When specifying a negative caching policy, make sure to specify a cache TTL for _all_ response codes that you want to cache. Cloud CDN doesn't apply any default negative caching when a policy exists.

For STATUS_CODE, you can specify the following HTTP status codes:

  * `300`, `301`, `302`, `307`, `308`
  * `404`, `405`, `410`, `421`, `451`
  * `501`



For each status code, you can specify a number of seconds to cache responses. To disable negative caching for the status code, exclude the code from your negative caching policy.

**Note:** Explicitly including a code and setting the TTL to `0` disables caching, but doing so is not recommended because the use of a TTL value of `0` in this context is different from other uses in Cloud CDN. For example, a `max-age=0` directive in a response `cache-control` header means that the cache must always revalidate the response, rather than that the response is not cacehable.

The maximum allowed value is 1800 seconds (30 minutes); however, infrequently accessed objects might be evicted from the cache before the defined TTL.

When the cache mode is set to `CACHE_ALL_STATIC` or `USE_ORIGIN_HEADERS`, negative caching is applied to responses with specific HTTP status codes, such as `302`, `404`, or `501`. The duration for which these negative responses are cached is determined by the following rule of precedence:

  * If the negative response from the origin includes explicit `Cache-Control` or `Expires` response headers, Cloud CDN caches the negative response for the duration specified by these headers.

For example, if your origin returns `404 Not Found` with a `Cache-Control: public,max-age=60` setting, the `404` status code is cached for `60` seconds, and the negative caching policy is ignored for that specific request.

  * If the negative response from the origin doesn't have any `Cache-Control` or `Expires` headers, Cloud CDN applies the configured negative caching policy TTLs. For example, if your origin returns `404 Not Found` with no caching headers, the response is cached for the TTL specified in `cdnPolicy.negativeCachingPolicy` for the `404 status code`.




When the cache mode is set to `FORCE_CACHE_ALL`, negative caching overrides any caching headers set by the origin. Cloud CDN caches the response for the length of time specified by the TTL, or doesn't cache it if no TTL is set.

In addition, when the cache mode is set to `FORCE_CACHE_ALL`, Cloud CDN also modifies the `max-age` sent to the client in the `Cache-Control` header. In particular, if a given error has a configured TTL setting, Cloud CDN considers the lower TTL value and the `client_ttl` configuration and sends a `Cache-Control: public,max-age=N` header with that value. If a given error doesn't have a configured TTL setting, Cloud CDN removes any `Cache-Control` header sent by the origin. Cloud CDN also always removes any `Expires` header sent by the origin.

If an origin has negative caching initially enabled but then disabled (either manually or by disabling caching for a particular response code), cached error responses are considered valid based only on their `Cache-Control` or `Expires` headers. Therefore, once negative caching is disabled, a response with no caching age directives in its headers is not served from cache.

Cloud CDN caches in response to `GET` requests. For more information, see [Cacheable content](https://docs.cloud.google.com/cdn/docs/caching#cacheability).

Each cache entry is identified by a [cache key](https://docs.cloud.google.com/cdn/docs/caching#cache-keys).

### Disable negative caching

### Console

  1. In the Google Cloud console, go to the **Load Balancing** page. 

[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click the name of your external Application Load Balancer.
  3. Click **Edit** edit.
  4. In **Backend configuration** , select a backend and click **Edit** edit.
  5. Make sure that **Enable Cloud CDN** is selected.
  6. At the bottom of the window, click **Advanced configurations**.
  7. Clear the checkbox next to **Enable negative caching**.
  8. Click **Update**.
  9. Click **Update** again.



### gcloud

For backend buckets, use the [gcloud compute backend-buckets create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/create) or [gcloud compute backend-buckets update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update) command with the `--no-negative-caching` flag.

For backend services, use the [gcloud compute backend-services create](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) or [gcloud compute backend-services update](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update) command with the `--no-negative-caching` flag.
    
    
    gcloud compute backend-services (create | update) (BACKEND_SERVICE_NAME | BACKEND_BUCKET_NAME)
        --no-negative-caching
    

### api

For backend buckets, use the [Method: backendBuckets.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendBuckets/insert) or [Method: backendBuckets.update](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendBuckets/update) API call.

For backend services, use the [Method: backendServices.insert](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/insert) or [Method: backendServices.update](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/update) API call.

Use one of the following API calls:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/BACKEND_BUCKET
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE
    

Add the following snippet to the JSON request body:
    
    
    "cdnPolicy": {
      "negativeCaching": OFF
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
