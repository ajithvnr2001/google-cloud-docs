---
url: https://docs.cloud.google.com/storage/docs/caching/
title: Caching with Cloud Storage built-in cache \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:09:31.341443+00:00
---

# Caching with Cloud Storage built-in cache  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/caching/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Caching with Cloud Storage built-in cache Stay organized with collections  Save and categorize content based on your preferences. 

This page discusses the options you have to control how your Cloud Storage objects are cached. This page focuses on the Cloud Storage built-in cache and [Cloud CDN](https://docs.cloud.google.com/cdn/docs), but Cloud Storage is also compatible with third-party Content Delivery Networks (CDNs).

## Overview

Control caching for your Cloud Storage objects to enhance application performance and help maintain content freshness. Caching object data stores copies of the data in Google or internet caches, which accelerates future data read requests. Cloud Storage offers built-in caching that behaves like a CDN. You manage this built-in caching through the `Cache-Control` metadata, which defines how and for how long caches store your objects.

For more advanced control, use Cloud Storage caching with Cloud CDN or explore Rapid Cache.

### Caching with Rapid Cache

Rapid Cache provides a fully-managed, always consistent SSD-backed zonal read cache that can be created in the same zones as your workloads in compute. The caches are used to accelerate serving data for large, data-intensive workloads. Data that's read from a cache is charged [reduced data transfer fees](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache) compared to data that's read directly from multi-region buckets, letting you optimize costs.

For more information, see [Rapid Cache](https://docs.cloud.google.com/storage/docs/rapid/rapid-cache).

## Built-in caching for Cloud Storage

Cloud Storage can behave like a Content Delivery Network (CDN) with no work on your part, because an object's data is cached in the Cloud Storage network if its [`Cache-Control` metadata](https://docs.cloud.google.com/storage/docs/metadata#cache-control) is set to allow caching and the following criteria are met:

  * The object is [publicly accessible](https://docs.cloud.google.com/storage/docs/access-control/making-data-public).
  * The object is not stored in a bucket that has [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) enabled and does not reside within a [Virtual Private Cloud service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).
  * The object is not encrypted using [customer-managed encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) or [customer-supplied encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys).

**Important:** Proxies or browsers might cache object data and subsequently serve object data from their cache based solely on the object's `Cache-Control` metadata. Additionally, depending on the network path, once object data has left Cloud Storage, the `Cache-Control` value associated with it might be overwritten, for example by a CDN that the data passes through.

Cloud Storage respects [standard values](https://datatracker.ietf.org/doc/html/rfc7234#section-5.2) for `Cache-Control`, such as the following:

  * `public`: the object can be cached.

  * `private`: the object won't be cached by Cloud Storage, but can be cached in a requester's local cache.

  * `no-cache`: the object can be cached, but cannot be used to satisfy future requests unless first validated by Cloud Storage.

  * `no-store`: the object can't be cached.

  * `max-age=TIME_IN_SECONDS`: the length of time an object can be cached before it's considered stale. You can set `max-age` to any length of time. Stale objects are not served from caches, except in [special circumstances](https://datatracker.ietf.org/doc/html/rfc7234#section-4.2.4).




To set the `Cache-Control` metadata for an object, see [Editing object metadata](https://docs.cloud.google.com/storage/docs/viewing-editing-metadata#edit).

### Built-in caching behavior with IAM Deny policies

When there's an organization-level IAM Deny policy that restricts read access for an object from the [principal identifier `allUsers`](https://docs.cloud.google.com/iam/docs/principal-identifiers), built-in caching is disabled for the object, even if there's a bucket-level IAM policy that grants read access for the object to `allUsers`. However, if the IAM Deny policy only restricts individual users, built-in caching remains enabled for the object.

### Performance considerations

Performance can be much better for publicly cacheable objects. If you have an object being used to control many clients and thus want to disable caching to provide the latest data:

  * Consider instead setting the object's `Cache-Control` metadata to `public` with `max-age` of 15-60 seconds. Most applications can tolerate having an object be out of date for a few seconds, in exchange for performance improvements.

  * Use `Cache-Control: no-store` for an object to indicate that the object must not be cached for subsequent requests in any cache.




## Cloud Storage with Cloud CDN

For the best performance when delivering content to users, we recommend using Cloud Storage with [Cloud CDN](https://docs.cloud.google.com/cdn/docs). Compared to the caching capabilities you get with Cloud Storage alone, Cloud CDN offers enhanced performance, larger cacheable file sizes, and features like cache invalidation.

To use Cloud CDN, you must use an [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) with your Cloud Storage buckets as a backend. For a tutorial on setting up an HTTP(S) load balancer with a Cloud Storage bucket, see [Hosting a static website](https://docs.cloud.google.com/storage/docs/hosting-static-website).

[Cloud CDN cache modes](https://docs.cloud.google.com/cdn/docs/caching#cache-modes) allow you to apply a unified caching configuration across all your objects. Cloud CDN uses the `Cache-Control` metadata set on your objects to determine [how they should be cached](https://docs.cloud.google.com/cdn/docs/caching#cacheability), unless you override the `Cache-Control` metadata using a cache mode or [TTL limit](https://docs.cloud.google.com/cdn/docs/using-ttl-overrides).

Consider the differences in capabilities and pricing implications when choosing between Cloud Storage built-in caching and Cloud CDN:

### Differences in capabilities

Feature | Cloud Storage | Cloud CDN  
---|---|---  
Max cacheable file size | 10 MiB | 100 GiB 1  
Default cache expiration | 1 hour | 1 hour (configurable)  
Support for custom domains over HTTPS | No | Yes  
Cache invalidation | No | Yes  
  
1The maximum cacheable file size for Cloud CDN is 100 GiB if the origin server supports byte range requests. If the origin server doesn't support byte range requests, the maximum cacheable file size for Cloud CDN is 10 MiB.

### Pricing considerations

In terms of pricing, the choice between Cloud Storage built-in caching and Cloud CDN depends on how much data you serve every month, which determines the amount of networking costs you incur.

  * If you serve less than a few GiB of cacheable data a month, it may be cheaper overall for you to rely on Cloud Storage built-in caching. Cloud Storage caching may incur higher networking costs than Cloud CDN, since cached and uncached objects are charged the same outbound data transfer cost (which means you pay full price for cache hits). However, you only pay for data storage and operations usage costs associated with Cloud Storage, instead of the combination of Cloud Storage, Cloud CDN, and Cloud Load Balancing.

  * If you regularly serve 100 GiB or more of cacheable data a month, or need to use per-request logging and custom headers, it may be cheaper overall for you to rely on Cloud CDN. You incur Cloud Storage outbound data transfer and Cloud CDN cache fill costs for cache fill, and Cloud CDN networking prices apply after the cache is full. The networking cost savings you gain from using Cloud CDN may be worth the higher operating costs associated with maintaining the external Application Load Balancer and Cloud CDN along with Cloud Storage.




## What's next

  * Read more about the [`Cache-Control` metadata](https://docs.cloud.google.com/storage/docs/metadata#cache-control).
  * Learn more about the [RFC `Cache-Control` directives](https://datatracker.ietf.org/doc/html/rfc7234#section-5.2).
  * Read the [caching overview for Cloud CDN](https://docs.cloud.google.com/cdn/docs/caching).
  * Learn how to [create an external HTTP(S) load balancer to serve requests from your Cloud Storage bucket](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-buckets).
  * Read the pricing details for [external Application Load Balancers](https://docs.cloud.google.com/vpc/network-pricing#lb) and [Cloud CDN](https://docs.cloud.google.com/cdn/pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
