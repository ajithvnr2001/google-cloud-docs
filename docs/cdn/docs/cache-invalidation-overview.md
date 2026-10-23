---
url: https://docs.cloud.google.com/cdn/docs/cache-invalidation-overview/
title: Cache invalidation overview \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:23.653911+00:00
---

# Cache invalidation overview  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/cache-invalidation-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Cache invalidation overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of Cloud CDN cache invalidation.

## What is cache invalidation?

After an object is cached, it normally remains in the cache until it expires or is evicted to make room for new content. You might want to remove an object from the cache before its normal expiration time. You can force an object or set of objects to be ignored by the cache by requesting a cache invalidation.

Cache invalidation, sometimes called _cache purging_ , is the process of declaring cached content to be invalid. This process causes the entry to be removed from the cache and then refilled from the backend server the next time that the content is requested.

Cloud CDN supports the use of cache tags and invalidation matchers, such as host and URL path, for invalidation requests.

You can combine these invalidation parameters to target specific cached responses and minimize backend load on the subsequent cache fill.

It's important to ensure that the backend server is returning the correct content before you request the cache invalidation. Otherwise, when Cloud CDN requests the content again, it might cache the incorrect content.

Invalidations requests are rate limited. You can submit up to 500 invalidation requests per minute. Each invalidation request takes effect in about 10 seconds.

Cloud CDN doesn't restrict the number of objects or the total size of all invalidated objects for each request.

## Invalidation by URLs

Each invalidation request specifies a path pattern that identifies the object or set of objects that should be invalidated. The path pattern can be either a specific path, such as `/cat.jpg`, or a path prefix, such as `/picture*`. The following rules apply to path patterns:

  * The path pattern must start with `/`.
  * It cannot include `?` or `#`.
  * It must not include an `*` except as the final character.
  * If a path ends with `*`, all objects whose paths begin with the string that precedes `*` are invalidated. For example, for the invalidation path `/picture*`, the prefix is `/picture`. Any object path beginning with `/picture` is invalidated, including `/picture/cat.jpg`, `/pictures/dog.jpg`, and `/picture1.jpg`.
  * If you want to invalidate all objects in a directory, include the trailing `/` in the path pattern, for example, `/pictures/*`.



The path pattern is compared with the path component of the URL, which is everything between the hostname and any `?` or `#` that might be present.

If you have URLs that contain a query string, for example `/images.php?image=fred.png`, you cannot selectively invalidate objects that differ only by query string. For example, if you have two images, `/images.php?image=fred.png` and `/images.php?image=barney.png`, you cannot invalidate only `fred.png`. To invalidate all images served by images.php, use `/images.php` as the path pattern.

## Invalidation for a single host

Cache invalidation invalidates the path for all your hostnames. For example, if you have `example.com` and `example2.com` pointed to the same load balancer, and you invalidate `/images/cat.jpg`, both `example.com/images/cat.jpg` and `example2.com/images/cat.jpg` are invalidated.

You can restrict the invalidation to only one of the hosts by specifying the host.

## Invalidation by cache tags

Cache tags (or _surrogate keys_) let you invalidate content based on arbitrary metadata.

**Note:** Cache tags are different from [cache keys](https://docs.cloud.google.com/cdn/docs/caching#cache-keys).

These tags are defined with the `Cache-Tag` HTTP header in a backend response. Cache tags from the backend in the `Cache-Tag` HTTP response header are sent to the client.

**Tag format requirements**

  * Tags must be provided in the header as a comma-separated list

  * Leading and trailing spaces around each tag are trimmed

  * Both `tag1`,`tag2` and `tag1`, `tag2` are valid




For example,

`Cache-Tag: release-v1,frontend,js`

Cache tags have the following limits:

  * Must not exceed 120 bytes per tag
  * Must not exceed 4 KiBs (4096 bytes) of total tag names per cached object
  * Must not exceed 50 tags per object



If these tag limits are exceeded, the response isn't cached and this decision is logged as `RESPONSE_CACHE_TAG_INVALID` in `LoadBalancerLogEntry.cacheDecision`.

You can specify up to 10 cache tags per invalidation request. When multiple tags are specified in a single invalidation request, they are treated as a logical `OR`. Consider an example in which you have the following cached objects:

  * Cached object #1 with tags `js`, `2020-12-23`, and `prod`
  * Cached object #2 with tags `css`, `2020-11-30`, and `prod`
  * Cached object #3 with tags `img` `2020-11-30`, and `staging`



When you issue a request to invalidate objects that match `tags="prod,2020-11-30"`, all three cached objects are invalidated. This approach means that you don't need to know or specify all possible tag combinations when you want to invalidate an object.

If you specify invalidation matchers along with cache tags, the invalidation request applies only to the tagged objects that match the invalidation matchers. Consider an example with the following cached objects:

  * Cached object #1 with URL `https://staging.example.com/img/cat.jpg` and tag `a`
  * Cached object #2 with URL `https://example.com/img/cat.jpg` and tag `a`
  * Cached object #3 with URL `https://staging.example.com/js/cat.js` and tag `a`
  * Cached object #4 with URL `https://staging.example.com/img/logo.jpg` and tag `b`



When you issue a request to invalidate objects where the host is `staging.example.com`, the path `/img/*`, and the tag `a`, only object #1 is invalidated. Objects #2, #3, and #4 don't match the host, path, or tag, respectively.

## Invalidation latency

Because Cloud CDN is a distributed system, it might report that an invalidation has completed even though a small number of caches have not yet processed the invalidation request. This situation is rare and corrects itself automatically.

## Best practices

Invalidate only what you must because invalidating too much might cause a spike in requests that the caches were serving to suddenly hit your instances or buckets.

Invalidation is intended for use in exceptional circumstances, not as part of your normal workflow. Invalidations don't affect cached copies in web browser caches or caches operated by third-party internet service providers.

As an alternative to routine invalidations, you can proactively set appropriate expiration times on responses or use different URLs for different versions of your content. For more information about expiration times, see [Expiration times and validation requests](https://docs.cloud.google.com/cdn/docs/caching#expiration).

## Invalidation with Shared VPC cross-project service referencing

Cache invalidation is configured in the frontend project; that is, the project that has the forwarding rule, target proxy, and URL map of the load balancer. So, when you're using a [global external Application Load Balancer with Shared VPC cross-project service referencing](https://docs.cloud.google.com/load-balancing/docs/https#shared-vpc), by default, service project administrators don't have the required permissions to request cache invalidations.

Cache invalidations can be issued only by principals who have the Identity and Access Management (IAM) roles for configuring load balancer resources in the frontend projects—for example, the Compute Network Admin role (`roles/compute.networkAdmin`).

Service administrators, who control provisioning of the backend services in a separate project, can work with the load balancer administrator of the frontend project to issue cache invalidation for their cross-project services. For URL rewrites, ensure that the invalidation matches the pre-rewrite host and path that the client sends.

## What's next

  * To learn how to invalidate your Cloud CDN cached content, see [Invalidating cached content](https://docs.cloud.google.com/cdn/docs/invalidating-cached-content).

  * To learn about which content is cacheable or non-cacheable, see [Caching overview](https://docs.cloud.google.com/cdn/docs/caching).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
