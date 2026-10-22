---
url: https://docs.cloud.google.com/cdn/docs/serving-stale-content/
title: Serve stale content \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:46.221906+00:00
---

# Serve stale content  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/serving-stale-content/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Serve stale content Stay organized with collections  Save and categorize content based on your preferences. 

This page provides information about serving stale, expired content with Cloud CDN. Serving stale content lets Google's global cache continue to serve content when your origin server is unreachable or is returning errors to Cloud CDN.

The reasons to do this are as follows:

  * You prefer to serve stale content to users rather than returning errors to users.
  * Serving stale content avoids latency when the cache gets a request for content that has just expired. Rather than having to wait for a synchronous revalidation to the backend, the cache serves the stale content that has just expired, while triggering a separate revalidation.



Cloud CDN offers the following two methods to control how long a stale object can be served while a revalidation request is sent to the origin:

  * At the origin: You can specify the `Cache-Control: stale-while-revalidate` directive in the response header. Cloud CDN honors this directive, serving the stale content for the specified number of seconds past the cache entry expiration time. During this period, Cloud CDN asynchronously sends a request to the origin to revalidate and refresh the content.

**Note:** `Cache-Control: stale-while-revalidate` directive is not honored in `FORCE_CACHE_ALL` mode. `FORCE_CACHE_ALL` caches all content and ignores any `stale-while-revalidate` directive from the origin.
  * Through the policy: This is a Cloud CDN configuration setting that dictates a maximum duration, after the response has expired, for which Cloud CDN can continue serving a stale version. This is configured using the `serve-while-stale` option. If the `stale-while-revalidate` directive isn't present in the response, this setting is used. If a value isn't specified, the default value, `86400s` (1 day), is used.




Cloud CDN doesn't support the `stale-if-error` directive. This directive instructs the cache to avoid serving stale content unless synchronous revalidation with the origin server has failed with particular error status codes.

The default, minimum, and maximum values are as follows:

  * Default: 86,400 seconds (one day)
  * Minimum: 0 seconds (disables the feature)
  * Maximum: 604,800 seconds (one week)



Stale content is served up to the specified limit past the cache entry expiration time, which is defined by the `max-age`, `s-maxage`, or `Expires` headers. For more information, see [Expiration times and validation requests](https://docs.cloud.google.com/cdn/docs/caching#expiration).

If a Cloud CDN edge cache does not have a cached copy of the object to serve stale, or the object has reached the maximum stale TTL, Cloud CDN synchronously revalidates the content with the origin. If the origin returns an error at that time, Cloud CDN returns the origin error.

## Logging and User Agent

The asynchronous requests made by Cloud CDN appear to your origin server exactly like the normal revalidation requests that occur when not serving stale content. The exception is that they are tagged with a `User-Agent` header containing `Cloud-CDN-Google`.

Asynchronous requests are also separately logged to Cloud Logging, so a user request that is served stale generates two log entries: the first for the content actually served to the user, and the second for the revalidation request to the origin. Like synchronous revalidations, Cloud CDN may send a [conditional request](https://docs.cloud.google.com/cdn/docs/caching#response-headers-validate) in some circumstances, or just re-request the content unconditionally. In either case, the response code logged to Cloud Logging corresponds to the original request to Cloud CDN; for example, a `200 OK` for an unconditional request, or a `304 Not Modified` if the user's original response was conditional.

## Client `max-stale` request directive

Clients can request a shorter stale service time by specifying a `max-stale` cache-control directive. If specified, this directive controls the amount of staleness the client tolerates.

If the cached content is more stale than the client's `max-stale` value, Cloud CDN revalidates the content before serving.

The client cannot request a `max-stale` value greater than the value configured with the `serve-while-stale` configuration option and the `stale-while-revalidate` cache-control directive from the origin.

## Before you begin

  * Read about [cache modes and static content](https://docs.cloud.google.com/cdn/docs/caching#cache-modes).

  * Ensure that Cloud CDN is enabled; for instructions, see [Using Cloud CDN](https://docs.cloud.google.com/cdn/docs/using-cdn).

  * If necessary, update to the latest version of the Google Cloud CLI:
        
        gcloud components update
        

**Note:** Make sure that you're using gcloud CLI version `322.0.0` or later.



## Serve stale content while revalidating

### Console

  1. In the Google Cloud console, go to the **Load balancing** page. 

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click the name of your external Application Load Balancer.
  3. Click edit**Edit**.
  4. For **Backend configuration** , select a backend, and then click edit**Edit**.
  5. Make sure that **Enable Cloud CDN** is selected.
  6. At the bottom of the window, click **Advanced configurations**.
  7. For **Additional CDN options** , select one of the following options for **Serve while stale** : 
     * 1 minute
     * 5 minutes
     * 10 minutes
     * 30 minutes
     * 1 day (recommended)
     * 7 days
  8. Click **Update**.
  9. Click **Update** again.



### gcloud

For backend buckets, use the [`gcloud compute backend-buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/create) or the [`gcloud compute backend-buckets update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update) with the `--serve-while-stale` flag.

For backend services, use the [`gcloud compute backend-services create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) or the [`gcloud compute backend-services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update) with the `--serve-while-stale` flag.
    
    
    gcloud compute backend-buckets (create | update) BACKEND_BUCKET_NAME
        --serve-while-stale=SECONDS
    
    
    
    gcloud compute backend-services (create | update) BACKEND_SERVICE_NAME
        --serve-while-stale=SECONDS
    

For example:
    
    
    gcloud compute backend-services update my-backend-service
        --serve-while-stale=180s
    

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
      "serveWhileStale": SECONDS
    }
    

## Disable serving stale content

### Console

  1. In the Google Cloud console, go to the **Load balancing** page. 

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click the name of your external Application Load Balancer.
  3. Click edit**Edit**.
  4. For **Backend configuration** , select a backend, and then click edit**Edit**.
  5. Make sure that **Enable Cloud CDN** isn't selected.
  6. At the bottom of the window, click **Advanced configurations**.
  7. For **Additional CDN options** > **Serve while stale** , select **Disable serve while stale**.
  8. Click **Update**.
  9. Click **Update** again.



### gcloud

For backend buckets, use the [`gcloud compute backend-buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/create) or [`gcloud compute backend-buckets update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update) with the `--serve-while-stale` flag value set to `0`.

For backend services, use the [`gcloud compute backend-services create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) or the [`gcloud compute backend-services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update) with the `--serve-while-stale` flag value set to `0`.
    
    
    gcloud compute backend-services (create | update) (BACKEND_SERVICE_NAME | BACKEND_BUCKET_NAME)
        --serve-while-stale=0
    

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
      "serveWhileStale": 0
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
