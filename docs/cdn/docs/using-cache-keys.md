---
url: https://docs.cloud.google.com/cdn/docs/using-cache-keys/
title: Customize cache keys \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:19:39.123427+00:00
---

# Customize cache keys  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/using-cache-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Customize cache keys Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to customize Cloud CDN cache keys.

Changing cache key configuration might result in a sudden drop in the cache hit ratio if new requests start using cache keys that are different from old cache key entries. Similarly, changing the cache key creator does not necessarily invalidate cached entries if new requests use the same key as old cache keys. To invalidate existing cached entries, see [Invalidate cached content](https://docs.cloud.google.com/cdn/docs/invalidating-cached-content).

**Caution:** Excluding components from cache keys can cause Cloud CDN to serve content intended for one user to another. Before excluding a component, ensure that responses from your backend service don't vary based on that component.

## Before you begin

This page assumes an understanding of [Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview), [Cloud CDN cache keys](https://docs.cloud.google.com/cdn/docs/caching#cache-keys), and load balanced [backend services](https://docs.cloud.google.com/load-balancing/docs/backend-service). We recommend reviewing these pages before proceeding.

## Enable Cloud CDN and customize cache keys

These instructions activate Cloud CDN for a load balanced backend service and customize the cache key. If you don't already have a load balancer to use as an origin, see the [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) documentation for instructions to create one.

Backend buckets don't include the protocol or host in the cache key because these don't influence how objects are referenced within a Cloud Storage bucket. However, they include a set of query string parameters that are specific to Cloud Storage, which might affect the response and might be extended by a customizable list of parameter names.

### Console

  1. In the Google Cloud console, go to the **Cloud CDN** page.

[Go to Cloud CDN](https://console.cloud.google.com/networking/cdn/list)

  2. Click the name of the origin that you want to update.

  3. Click **Edit**.

If more than one load balancer is attached to the origin, select the load balancer that you want to update from the **Edit** menu.

  4. To expand the **Cache performance** section, click **Next**.

  5. For **Cache key** , select **Custom**.

  6. In the **Cache key components** section, by default, all components are selected. Clear checkboxes for any components that you want to exclude from the cache key.

  7. Click **Done**.




### gcloud

To exclude one or more components from the cache keys for a backend service, use the [`gcloud compute backend-services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update).
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --no-cache-key-include-protocol \
        --no-cache-key-include-host \
        --no-cache-key-include-query-string
    

For backend buckets, use the [`gcloud compute backend-buckets update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update).

### API

To exclude one or more components from the cache key, specify configuration options in the `cacheKeyPolicy` section of `cdnPolicy` for the [`backendServices` resource](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#resource:-backendservice).

For backend services, use the [`backendServices.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/update) API call.
    
    
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE
    

For backend buckets, use the [`backendBuckets.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendBuckets/update) API call.
    
    
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/BACKEND_BUCKET
    

Add the following snippet to the JSON request body:
    
    
    "cdnPolicy": {
      "cacheKeyPolicy": [
        {
          "includeProtocol": false,
          "includeHost": false,
          "includeQueryString": false
        }
      ]
    }
    

## Update cache keys to add the protocol, host, and query string

By default, backend services configured to use Cloud CDN include all components of the request URI in cache keys. If you previously indicated that one or more components should be excluded, you can use the following steps to include them again.

These instructions add the protocol, host, and query string to the cache key for an existing backend service that already has Cloud CDN enabled.

### Console

  1. In the Google Cloud console, go to the **Cloud CDN** page.

[Go to Cloud CDN](https://console.cloud.google.com/networking/cdn/list)

  2. Click the name of the origin that you want to update.

  3. Click **Edit**.

If more than one load balancer is attached to the origin, select the load balancer that you want to update from the **Edit** menu.

  4. To expand the **Cache performance** section, click **Next**.

  5. For **Cache key** , select **Custom**.

  6. In the **Cache key components** section, select the **Protocol** , **Host** , and **Query string** checkboxes.

  7. Click **Done**.




### gcloud

To add one or more components to the cache keys for a backend service, use the `gcloud compute backend-services update` command.

Any unspecified flags are left unchanged.
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --cache-key-include-protocol \
        --cache-key-include-host \
        --cache-key-include-query-string
    

### API

To add one or more components to the cache key, specify configuration options in the `cacheKeyPolicy` section of `cdnPolicy` for the `backendServices` resource.

Add the following snippet to the JSON request body:
    
    
    "cdnPolicy": {
      "cacheKeyPolicy": [
        {
          "includeProtocol": true,
          "includeHost": true,
          "includeQueryString": true
        }
      ]
    }
    

## Update cache keys to use an include or exclude list of query string parameters

These instructions set Cloud CDN cache keys to use an include list or exclude list with query string parameters.

### Console

  1. In the Google Cloud console, go to the **Cloud CDN** page.

[Go to Cloud CDN](https://console.cloud.google.com/networking/cdn/list)

  2. Click the name of the origin that you want to update.

  3. Click **Edit**.

If more than one load balancer is attached to the origin, select the load balancer that you want to update from the **Edit** menu.

  4. To expand the **Cache performance** section, click **Next**.

  5. For **Cache key** , select **Custom**.

  6. In the **Cache key components** section, select the **Query string** checkbox. Then, select either of the following options:

     * If you want to specify query string parameters that must be part of the cache key, select **Include only selected**.

     * If you want to specify that all query string parameters except the ones that you list are included in the cache key, select **Include all but selected**.

  7. Click **Add parameter** and specify the parameters.

  8. Click **Done**.




### gcloud

To specify an include list or an exclude list for a backend service, specify query string parameters by using the `gcloud compute backend-services update` command.

Use this command to set the query string parameter `user` to the include list of a backend service.
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --cache-key-include-query-string \
        --cache-key-query-string-whitelist user
    

Use this command to set the query string parameter `user` to the exclude list of a backend service.
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --cache-key-include-query-string \
        --cache-key-query-string-blacklist user
    

Use this command to set the query string parameter `user` to the include list of a backend bucket.
    
    
    gcloud compute backend-buckets update BACKEND_BUCKET \
        --cache-key-query-string-whitelist user
    

### API

To specify an include list or an exclude list for a backend service, specify query string parameters in the `cacheKeyPolicy` section of `cdnPolicy` for the `backendServices` resource.

To specify an include list, add the following snippet to the JSON request body:
    
    
    "cdnPolicy": {
      "cacheKeyPolicy": [
        {
          "queryStringWhitelist": [QUERY_STRINGS]
        }
      ]
    }
    

Replace QUERY_STRINGS with a comma-separated list of query string parameters.

To specify an exclude list, add the following snippet:
    
    
    "cdnPolicy": {
      "cacheKeyPolicy": [
        {
          "queryStringBlacklist": [QUERY_STRINGS]
        }
      ]
    }
    

## Update cache keys to use HTTP headers

**Note:** Make sure that you're using gcloud CLI version 369.0.0 or later.

These instructions set Cloud CDN cache keys to use HTTP headers, which can include allowed [custom variables](https://docs.cloud.google.com/cdn/docs/caching#using-custom-variables).

### Console

  1. In the Google Cloud console, go to the **Cloud CDN** page.

[Go to Cloud CDN](https://console.cloud.google.com/networking/cdn/list)

  2. Click the name of the origin that you want to update./

  3. Click **Edit**.

If more than one load balancer is attached to the origin, select the load balancer that you want to update from the **Edit** menu.

  4. To expand the **Cache performance** section, click **Next**.

  5. For **Cache key** , select **Custom**.

  6. In the **Cache key components** section, select the **HTTP headers** checkbox.

  7. To specify one or more HTTP headers, click **Add HTTP header**.

  8. Click **Done**.




### gcloud

Use the `gcloud compute backend-services update` command with the `cache-key-include-http-header` option.
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --cache-key-include-http-header=[HEADER_FIELD_NAMES,...]
    

Replace HEADER_FIELD_NAMES with a comma-separated list of header names.

### API

Specify HTTP headers for cache keys in the `cacheKeyPolicy` section of `cdnPolicy` for the `backendServices` resource.

Add the following snippet to the JSON request body:
    
    
    "cdnPolicy": {
      "cacheKeyPolicy": [
        {
          "includeHttpHeaders": [HEADER_FIELD_NAMES]
        }
      ]
    }
    

Replace HEADER_FIELD_NAMES with a comma-separated list of header names.

If the specified cache key header is also specified as a custom request header, you can't use the [full range of variables](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers#variables).

For more information, see [Use custom variables with request headers](https://docs.cloud.google.com/cdn/docs/caching#use-custom-variables).

## Update cache keys to use named cookies

**Note:** Make sure that you're using gcloud CLI version 369.0.0 or later.

These instructions set Cloud CDN cache keys to use HTTP cookies.

### Console

  1. In the Google Cloud console, go to the **Cloud CDN** page.

[Go to Cloud CDN](https://console.cloud.google.com/networking/cdn/list)

  2. Click the name of the origin that you want to update.

  3. Click **Edit**.

If more than one load balancer is attached to the origin, select the load balancer that you want to update from the **Edit** menu.

  4. To expand the **Cache performance** section, click **Next**.

  5. For **Cache key** , select **Custom**.

  6. In the **Cache key components** section, select the **Named cookies** checkbox.

  7. To specify one or more cookies, click **Add named cookie**.

  8. Click **Done**.




### gcloud

Use the `gcloud compute backend-services update` command with the `cache-key-include-named-cookie` option.
    
    
    gcloud compute backend-services update BACKEND_SERVICE \
        --cache-key-include-named-cookie=[NAMED_COOKIES,...]
    

Replace NAMED_COOKIES with a comma-separated list of named cookies.

### API

To specify an include list or an exclude list for a backend service, specify query string parameters in the `cacheKeyPolicy` section of `cdnPolicy` for the `backendServices` resource.

To specify an include list, add the following snippet to the JSON request body:
    
    
    "cdnPolicy": {
      "cacheKeyPolicy": [
        {
          "includeNamedCookies": [NAMED_COOKIES]
        }
      ]
    }
    

Replace NAMED_COOKIES with a comma-separated list of query string parameters.

## What's next

  * To check whether Cloud CDN is serving responses from cache, see [Logs and metrics for caching](https://docs.cloud.google.com/cdn/docs/logging).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
