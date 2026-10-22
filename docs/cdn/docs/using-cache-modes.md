---
url: https://docs.cloud.google.com/cdn/docs/using-cache-modes/
title: Change cache modes \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:52.301864+00:00
---

# Change cache modes  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/using-cache-modes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Change cache modes Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for changing cache modes with Cloud CDN. Cache modes let you configure how Cloud CDN caches your content.

## Before you begin

  * Read about [cache modes and static content](https://docs.cloud.google.com/cdn/docs/caching#cache-modes).

  * Ensure that Cloud CDN is enabled; for instructions, see [Setup overview](https://docs.cloud.google.com/cdn/docs/using-cdn).

  * If necessary, update to the latest version of the Google Cloud CLI:
        
        gcloud components update
        

**Note:** Make sure that you're using gcloud CLI version `309.0.0` or later.



## Setting the cache mode

To configure cache modes for a Cloud CDN-enabled backend, do the following:

### Console

  1. In the Google Cloud console, go to the **Load Balancing** page. 

[Go to the Load balancing page](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click the name of your external Application Load Balancer.
  3. Click **Edit** edit.
  4. In **Backend configuration** , select a backend and click **Edit** edit.
  5. Make sure that **Enable Cloud CDN** is selected.
  6. Under **Cache mode** , select one of the following options: 
     * **Cache static content (recommended)** : Static content is web assets that don't change for each user. Static content is based on the `Content-Type` in the response. For more information, see [static content](https://docs.cloud.google.com/cdn/docs/caching#static).
     * **Use origin settings based on Cache-Control headers** : Cache responses with [valid cache directives](https://docs.cloud.google.com/cdn/docs/caching#cacheability) in the response headers. For details on how Cloud CDN interprets these headers and their precedence, see [Cache control header precedence](https://docs.cloud.google.com/cdn/docs/caching#cache-control-headers).
     * **Force cache all content** : Cache all successful content served by the origin, ignoring any `private` or `no-store` directives.
  7. Click **Save**.



### gcloud

For backend services, use the [`gcloud compute backend-services create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) or [`gcloud compute backend-services update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update) command with the `--cache-mode` flag.

For backend buckets, use the [`gcloud compute backend-buckets create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/create) or [`gcloud compute backend-buckets update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update) command with the `--cache-mode` flag.
    
    
    gcloud compute backend-services (create | update) BACKEND_SERVICE_NAME
        --cache-mode=CACHE_MODE
    
    
    
    gcloud compute backend-buckets (create | update) BACKEND_BUCKET_NAME
        --cache-mode=CACHE_MODE
    

Replace `CACHE_MODE` with one of the following:

  * `CACHE_ALL_STATIC` (default): Automatically caches [static content](https://docs.cloud.google.com/cdn/docs/caching#static). Responses that are marked as uncacheable (`private` or `no-store` directives in `Cache-Control` response headers) aren't cached. To cache dynamic content, the content must have [valid caching headers](https://docs.cloud.google.com/cdn/docs/caching#cacheability).

  * `USE_ORIGIN_HEADERS`: Requires the origin to set [valid caching headers](https://docs.cloud.google.com/cdn/docs/caching#cacheability) to cache content. Responses without these headers aren't cached at Google's edge and require a full trip to the origin on every request, potentially impacting performance and increasing load on the origin server. For details on how Cloud CDN interprets these headers and their precedence, see [Cache control header precedence](https://docs.cloud.google.com/cdn/docs/caching#cache-control-headers).

  * `FORCE_CACHE_ALL`: Caches all content (that is, successful responses), ignoring any `private` or `no-store` directives in `Cache-Control` response headers. This might result in caching of private, per-user (user identifiable) content. Only enable this on backends that are not serving private or dynamic content, such as Cloud Storage buckets. Don't enable this on backends that are serving private or dynamic content.




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
      "cacheMode": (CACHE_ALL_STATIC | USE_ORIGIN_HEADERS | FORCE_CACHE_ALL)
    

Replace `CACHE_MODE` with one of the following:

  * `CACHE_ALL_STATIC` (default): Automatically caches [static content](https://docs.cloud.google.com/cdn/docs/caching#static) if the origin does not set [valid caching headers](https://docs.cloud.google.com/cdn/docs/caching#cacheability). Responses that are marked as uncacheable (`private` or `no-store` directives in `Cache-Control` response headers) aren't cached. To cache dynamic content, the content must have [valid caching headers](https://docs.cloud.google.com/cdn/docs/caching#cacheability).

  * `USE_ORIGIN_HEADERS`: Requires the origin to set [valid caching headers](https://docs.cloud.google.com/cdn/docs/caching#cacheability) to cache content. Responses without these headers aren't cached at Google's edge and require a full trip to the origin on every request, potentially impacting performance and increasing load on the origin server. For details on how Cloud CDN interprets these headers and their precedence, see [Cache control header precedence](https://docs.cloud.google.com/cdn/docs/caching#cache-control-headers).

  * `FORCE_CACHE_ALL`: Caches all content (that is, successful responses), ignoring any `private` or `no-store` directives in `Cache-Control` response headers. This might result in caching of private, per-user (user identifiable) content. You should only enable this on backends that are not serving private or dynamic content, such as Cloud Storage buckets.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
