---
url: https://docs.cloud.google.com/cdn/docs/using-ttl-overrides/
title: Change TTL settings and overrides \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:29:51.715487+00:00
---

# Change TTL settings and overrides  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/using-ttl-overrides/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Change TTL settings and overrides Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to change TTL overrides with Cloud CDN. TTL overrides give you fine-grained control over how long Cloud CDN caches your content before revalidating it.

The TTL settings are summarized in the following table.

| Default TTL | Max TTL | Client TTL  
---|---|---|---  
Reason to configure | Improve cache hit rates for content that doesn't change often | Force Cloud CDN to revalidate content more often than specified by an origin header  | Force clients to revalidate content more often against Cloud CDN   
Used when | One of the following is true, for a successful response:  


  * cache mode = `FORCE_CACHE_ALL`
  * cache mode = `CACHE_ALL_STATIC`, the content-type is statically cacheable, and a TTL isn't set by origin headers (`max-age`, `s-maxage`, or `Expires`)

| All of the following are true:  


  * cache mode = `CACHE_ALL_STATIC`
  * A TTL is set by origin headers (`max-age`, `s-maxage`, or `Expires`)
  * The TTL specified in the origin header is greater than the max TTL value

| One of the following is true:  


  * cache mode = `FORCE_CACHE_ALL`, and the client TTL value is less than Cloud CDN's TTL
  * cache mode = `CACHE_ALL_STATIC`, and the client TTL is less than the TTL set by the origin header (or default TTL if no origin header information is present)

  
Default value | 3600 seconds (1 hour) | 86,400 seconds (1 day) | 3600 seconds (1 hour)  
Max allowed value | 31,622,400 seconds (1 year) | 31,622,400 seconds (1 year) | 31,622,400 seconds (1 year)  
Notes | Must be less than or equal to the max TTL  
  
`--default-ttl=0`  
forces the response to be revalidated at the origin  |  | Must be less than or equal to the max TTL  
  
## Before you begin

  * Read about [cache modes](https://docs.cloud.google.com/cdn/docs/caching#cache-modes).

  * Ensure that Cloud CDN is enabled; for instructions, see [Using Cloud CDN](https://docs.cloud.google.com/cdn/docs/using-cdn).

  * If necessary, update to the latest version of the Google Cloud CLI:
        
        gcloud components update
        

**Note:** Make sure that you're using gcloud CLI version `309.0.0` or later.



## Set the default TTL

To improve cache hit rates for content that doesn't change often, you can override the default TTL so that Cloud CDN revalidates content at the origin less frequently. Note that infrequently accessed objects might be evicted from the cache before the defined TTL.

When the cache mode is `FORCE_CACHE_ALL`, the default TTL overwrites the TTL set in all responses (including those that have a TTL set by origin headers). In this mode, the default TTL is visible to clients, because Cloud CDN sets the `public` and `max-age` attributes of the responses served to clients.

For `CACHE_ALL_STATIC` mode, the default TTL applies to cached content served by an origin for responses that don't have an existing valid TTL (`max-age`, `s-maxage`, or `Expires` header). In `CACHE_ALL_STATIC` mode, the default TTL doesn't modify the `Cache-Control` header served to clients. To modify the `Cache-Control` header in the `CACHE_ALL_STATIC` mode, you must set the client TTL.

When you set the cache mode to use origin headers (`USE_ORIGIN_HEADERS`), the default TTL value doesn't apply and cannot be set because Cloud CDN uses the `max-age` or `s-maxage` origin directive or the `Expires` header instead.

### Console

  1. In the Google Cloud console, go to the **Load Balancing** page. 

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click the name of your external Application Load Balancer.
  3. Click **Edit** edit.
  4. In **Backend configuration** , select a backend and click **Edit** edit.
  5. Make sure that **Enable Cloud CDN** is selected.
  6. Make sure that the cache mode is **Cache static content (recommended)** or **Force cache all content**. Overriding the TTL values isn't supported when the cache mode is **Use origin settings based on Cache-Control headers**.
  7. Under **Default time to live** , select a value.
  8. Click **Save**.



### gcloud

For backend services, use the [`gcloud compute backend-services create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) or [`gcloud compute backend-services update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update) command with the `--default-ttl` flag.

For backend buckets, use the [`gcloud compute backend-buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/create) or [`gcloud compute backend-buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update) command with the `--default-ttl` flag.
    
    
    gcloud compute backend-services (create | update) BACKEND_SERVICE_NAME
        --default-ttl=DEFAULT_TTL
    
    
    
    gcloud compute backend-buckets (create | update) BACKEND_BUCKET_NAME
        --default-ttl=DEFAULT_TTL
    

Replace `DEFAULT_TTL` with a value up to 31,622,400 seconds (1 year).

### API

For backend buckets, use the [`Method: backendBuckets.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendBuckets/insert) or [`Method: backendBuckets.update`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendBuckets/update) API call.

For backend services, use the [`Method: backendServices.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/insert) or [`Method: backendServices.update`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/update) API call.

Use one of the following API calls:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/BACKEND_BUCKET
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE
    

Add the following snippet to the JSON request body:
    
    
    "cdnPolicy": {
      "defaultTtl": DEFAULT_TTL
    }
    

Replace `DEFAULT_TTL` with a value up to 31,622,400 seconds (1 year).

## Set the max TTL

The maximum (max) TTL specifies the maximum allowed TTL within Cloud CDN for cached content served by an origin.

The TTL of a response is capped by the max TTL if one of the following is true:

  * The response attempts to set a `max-age` or `s-maxage` higher than the max TTL value.
  * The response has an `Expires` header more than `cdnPolicy.maxTtl` seconds in the future.



The max TTL setting does not change the `max-age` value sent to the client; for more information, see Overriding the maximum client TTL. The max TTL setting only affects how long Cloud CDN attempts to cache the content.

This setting is only used when the cache mode is `CACHE_ALL_STATIC`. The maximum allowed value is 31,622,400 seconds (1 year). Note that infrequently accessed objects might be evicted from the cache before the defined TTL.

With `FORCE_CACHE_ALL`, the TTL is always set to the default TTL; you can't set a max TTL.

### Console

  1. In the Google Cloud console, go to the **Load Balancing** page. 

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click the name of your external Application Load Balancer.
  3. Click **Edit** edit.
  4. In **Backend configuration** , select a backend and click **Edit** edit.
  5. Make sure that **Enable Cloud CDN** is selected.
  6. Make sure that the cache mode is **Cache static content (recommended)**.
  7. Under **Maximum time to live** , select a value.
  8. Click **Save**.



### gcloud

For backend services, use the [`gcloud compute backend-services create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) or [`gcloud compute backend-services update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update) command with the `--max-ttl` flag.

For backend buckets, use the [`gcloud compute backend-buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/create) or [`gcloud compute backend-buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update) command with the `--max-ttl` flag.
    
    
    gcloud compute backend-services (create | update) BACKEND_SERVICE_NAME
        --max-ttl=MAX_TTL
    
    
    
    gcloud compute backend-buckets (create | update) BACKEND_BUCKET_NAME
        --max-ttl=MAX_TTL
    

Replace `MAX_TTL` with a value up to 31,622,400 seconds (1 year).

### API

For backend buckets, use the [`Method: backendBuckets.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendBuckets/insert) or [`Method: backendBuckets.update`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendBuckets/update) API call.

For backend services, use the [`Method: backendServices.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/insert) or [`Method: backendServices.update`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/update) API call.

Use one of the following API calls:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/BACKEND_BUCKET
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE
    

Add the following snippet to the JSON request body:
    
    
    "cdnPolicy": {
      "maxTtl": MAX_TTL
    }
    

Replace `MAX_TTL` with a value up to 31,622,400 seconds (1 year).

## Override the client TTL

For all [cache modes](https://docs.cloud.google.com/cdn/docs/using-cache-modes), Cloud CDN passes `Cache-Control` headers to the client.

The client TTL lets you set a maximum TTL for what is sent to [browsers or clients](https://developer.mozilla.org/en-US/docs/Web/HTTP/Caching) so that clients revalidate content against Cloud CDN more often, without requiring revalidation at the origin. This way, content can be [invalidated](https://docs.cloud.google.com/cdn/docs/invalidating-cached-content) within Cloud CDN when necessary, and browsers can discover that the content is invalidated as soon as the client TTL expires.

In `FORCE_CACHE_ALL` mode, Cloud CDN normally passes the same `max-age` to the client that it uses internally for proxy caching; however, if a client TTL is specified and is a smaller value, the client TTL is passed to the client in the `max-age` directive instead. Similarly, in `CACHE_ALL_STATIC` mode, the client TTL serves as a clamp for whatever `max-age` is specified by the origin server so that the `max-age` sent to the browser or client won't be larger than the configured client TTL. If no `max-age` is specified by the origin, the lesser of Cloud CDN's TTL and the client TTL value is used as the `max-age` sent to the browser or client.

If an `Expires` header is present in the origin response, it is removed and replaced with a `Cache-Control: max-age` directive with the appropriate TTL. For error responses, if no negative caching TTL is set, the `Cache-Control` header is also removed.

Because the client TTL is treated as a maximum value for what is sent to browsers or clients, it can't be used to increase the `max-age` value that would otherwise be sent. If the `max-age` value that is sent to browsers and clients is lower than you would like, you must increase the `max-age` directive value in the response returned by the origin, or adjust the default TTL or [negative caching](https://docs.cloud.google.com/cdn/docs/using-negative-caching) settings appropriately.

Typically, a client TTL setting of about one day is a good practical upper bound. A one-day setting means that browsers check in with at least that frequency and can learn about cache invalidations that might have occurred in Cloud CDN. You can set the client TTL much higher (up to a year) as a way of allowing the origin and the configured TTLs to fully control what is sent to the client. This can be useful if you don't want the browser to perform more-frequent validations against Cloud CDN.

### Console

  1. In the Google Cloud console, go to the **Load Balancing** page. 

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click the name of your external Application Load Balancer.
  3. Click **Edit** edit.
  4. In **Backend configuration** , select a backend and click **Edit** edit.
  5. Make sure that **Enable Cloud CDN** is selected.
  6. Make sure that the cache mode is **Cache static content (recommended)** or **Force cache all content**. Overriding the TTL values isn't supported when the cache mode is **Use origin settings based on Cache-Control headers**.
  7. Under **Client time to live** , select a value up to 1 year.
  8. Click **Save**.



### gcloud

For backend services, use the [`gcloud compute backend-services create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) or [`gcloud compute backend-services update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update) command with the `--client-ttl` flag.

For backend buckets, use the [`gcloud compute backend-buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/create) or [`gcloud compute backend-buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update) command with the `--client-ttl` flag.
    
    
    gcloud compute backend-services (create | update) BACKEND_SERVICE_NAME
        --client-ttl=CLIENT_TTL
    
    
    
    gcloud compute backend-buckets (create | update) BACKEND_BUCKET_NAME
        --client-ttl=CLIENT_TTL
    

Replace `CLIENT_TTL` with a value up to 31,622,400 seconds (1 year).

### API

For backend buckets, use the [`Method: backendBuckets.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendBuckets/insert) or [`Method: backendBuckets.update`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendBuckets/update) API call.

For backend services, use the [`Method: backendServices.insert`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/insert) or [`Method: backendServices.update`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/update) API call.

Use one of the following API calls:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/BACKEND_BUCKET
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE
    

Add the following snippet to the JSON request body:
    
    
    "cdnPolicy": {
      "clientTtl": CLIENT_TTL
    }
    

Replace `CLIENT_TTL` with a value up to 31,622,400 seconds (1 year).

## What's next

  * To learn the reasons for serving stale, expired content, see [Serve stale content](https://docs.cloud.google.com/cdn/docs/serving-stale-content).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
