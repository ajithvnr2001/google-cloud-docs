---
url: https://docs.cloud.google.com/media-cdn/docs/cache-invalidation/
title: Invalidate cached content \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:57.273711+00:00
---

# Invalidate cached content  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/cache-invalidation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Invalidate cached content Stay organized with collections  Save and categorize content based on your preferences. 

Cache invalidation (or _cache purging_) is the process of declaring cached content to be invalid. This removes the content from the cache, ensuring that the next request is fetched directly from the origin server.

Media CDN supports multiple ways of selecting content to be invalidated, as follows:

  * Host and URL path
  * URL prefix (wildcard)
  * Cache tags, including built-in tags for `status`, `origin`, and `content-type`



You can combine these invalidation parameters to target specific cached responses and minimize origin load on the subsequent cache fill.

## Supported invalidation syntax

The supported invalidation syntax is as follows:

Type | Syntax | Example  
---|---|---  
Host invalidation  |  Invalidate cached responses for the specified host.  |  `gcloud edge-cache services invalidate-cache SERVICE_NAME \  
--host="media.example.com"`  
Path invalidation  |  Invalidate cached responses for the specified path or path prefix.  |  `gcloud edge-cache services invalidate-cache SERVICE_NAME \  
--path="/content/1234/hls/*"`   
`gcloud edge-cache services invalidate-cache SERVICE_NAME \  
--path="/videos/funny.mp4"`  
Cache tag invalidation on HTTP status code, origin name, or MIME type  |  Invalidate cached responses with a matching tag. Multiple tags are treated as a boolean `OR`.  |  `gcloud edge-cache services invalidate-cache SERVICE_NAME \  
--tags="status=404,origin=staging-origin"`   
`gcloud edge-cache services invalidate-cache SERVICE_NAME \  
--tags="content-type=application/x-mpegurl"`  
  
Notes:

  * Up to 10 cache tags can be specified in a single invalidation request.
  * You can combine `host`, `path`, and `tags` in a single invalidation request. They are treated as a boolean `AND`.
  * When multiple cache tags are specified, they are treated as a boolean `OR`. For example, if you specify `--tags="status=404,origin=staging-origin"`, _all_ responses with a cache tag of `status=404` are invalidated, as are _all_ responses with a cache tag of `origin=staging-origin`.



## Cache tags

Cache tags (or _surrogate keys_) let you invalidate content based on arbitrary metadata.

**Note:** Cache tags are different from [cache keys](https://docs.cloud.google.com/media-cdn/docs/caching#cache-keys).

These tags are defined by the following:

  * Setting the `Cache-Tag` HTTP header in an origin response, with tags specified as a comma-separated list of values.
  * Built-in tags based on the HTTP status code of the response, the MIME type from the `Content-Type` HTTP response header, or the name of the origin that the response was fetched from.



When multiple tags are specified in a single invalidation request, they are treated as a boolean `OR`.

Consider the following example:

  * You have the following cached objects:

    * Cached object #1 with tags `status=200`, `content-type=video/mp4`
    * Cached object #2 with tags `status=404`, `content-type=text/plain`
    * Cached object #3 with tags `status=200`, `content-type=application/x-mpegurl`
  * You issue a request to invalidate objects with `tags="status=200,content-type=text/plain"`

  * Outcome: All three cached objects are invalidated at the same time. This is to prevent having to specify all possible tag combinations, some of which might be unknown.




Notes:

  * The default cache tags are _not_ included in the client-facing response because they reflect either existing headers (such as the status line or Content-Type) or internal configuration details.
  * Cache tags sent by the origin in the `Cache-Tag` HTTP response header are sent to the client. If you want to prevent these from being sent to the client, use the `responseHeadersToRemove` feature on a `routeRule` to remove the `Cache-Tag` header. For examples, see the [custom headers](https://docs.cloud.google.com/media-cdn/docs/custom-headers#set-custom-headers) documentation.



### Built-in tags

Responses automatically have the following cache tags applied to support invalidating content based on status code, MIME type, or the origin that the content was fetched from. You don't need to specify these tags in your origin responses.

Tag | Details  
---|---  
`status=HTTP_STATUS_CODE` |  The `status` cache tag is set based on the returned HTTP status code of the cached response. For example, you can invalidate all cached HTTP 404 responses by specifying `status=404` in an invalidation request.  
`content-type=MIME_TYPE` |  The `content-type` cache tag is set based on the MIME type set in the [Content-Type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Type) HTTP response header. For example, the MIME type of an HLS playlist is `application/x-mpegURL` or `vnd.apple.mpegURL`. This lets you invalidate specific types of content.  
`origin=ORIGIN_NAME` |  The `origin` cache tag is set based on the name of the origin the content was fetched from. The `origin` value references the value of `.routing.routeRules[].origin`, and lets you invalidate content from a misconfigured or potentially misbehaving origin server.  
  
### Cache tag limitations

Cache tags have the following restrictions:

  * Must not exceed 120 bytes per tag
  * Must not exceed 4 KiB (4096 bytes) of total tag names per cached object
  * Must not exceed 50 tags per object, not including default tags added by Media CDN
  * Must be a valid HTTP token name, as defined in Section 3.2.6 of HTTP RFC 7230
  * Must not include the built-in `status=`, `origin=`, or `content-type=` prefixes (which are ignored).



Tags that don't fall within these limits or meet these requirements are ignored. In some cases (such as when the response headers are too large), the response fails and isn't cached.

## Permissions

The `networkservices.EdgeCacheServices.invalidateCache` permission controls access to the [`invalidateCache` API](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices/invalidateCache). This permission is included in the `networkservices.edgeCacheAdmin` and `networkservices.edgeCacheUser` Identity and Access Management roles.

## Examples

The following examples show how to invalidate cached responses for a Media CDN service.

You can combine the `host`, `path`, and `tags` fields in a single invalidation request to invalidate a specific set of content.

### Invalidate by host

###  Console 

  1. In the Google Cloud console, go to the **Media CDN** page. 

[Go to Media CDN](https://console.cloud.google.com/net-services/media-cdn)

  2. Click the **Services** tab.
  3. Click a service.
  4. Click the **Cache invalidation** tab.
  5. To invalidate the cache by host, for **Host** , specify a hostname unless you want to invalidate the path for all hostnames. The hostname can't include `*`.
  6. Click **Invalidate** and then click **Confirm** to indicate that you want Media CDN to invalidate the content matching the host.



###  gcloud 
    
    
    gcloud edge-cache services invalidate-cache SERVICE_NAME \
        --host=HOST
    

Replace the following:

  * `SERVICE_NAME` with the name of the Edge Cache service.
  * `HOST` with the complete hostname of the cache entry to be invalidated.



For example:
    
    
    gcloud edge-cache services invalidate-cache SERVICE_NAME \
        --host="media.example.com"
    

Invalidating all content associated with a host can be risky and impact performance. Consider reducing the invalidation scope by providing a specific path or relevant cache tags.

### Invalidate by path

###  Console 

  1. In the Google Cloud console, go to the **Media CDN** page. 

[Go to Media CDN](https://console.cloud.google.com/net-services/media-cdn)

  2. Click the **Services** tab.
  3. Click a service.
  4. Click the **Cache invalidation** tab.
  5. To invalidate the cache by path, for **Path** , specify the path and the filename—for example,`/videos/funny.mp4` or `/segments/e94a6b1f731/*`.
  6. Click **Invalidate**.



###  gcloud 
    
    
    gcloud edge-cache services invalidate-cache SERVICE_NAME \
        --path=PREFIX
    

Replace the following:

  * `SERVICE_NAME` with the name of the Edge Cache service.
  * `PREFIX` with a path prefix ending in '*' that matches cache entries to be invalidated.



For example:
    
    
    gcloud edge-cache services invalidate-cache SERVICE_NAME \
        --path="/segments/e94a6b1f731/*"
    

You can also invalidate an exact path by omitting the trailing `*` character. Passing `--path="/videos/funny.mp4"` invalidates the cached response (if any) matching that path.

### Invalidate by cache tag

**Note:** Use host, path, and tags together to reduce the volume of cached content invalidated at the same time. Invalidated responses are re-fetched from the origin in full, and invalidating too much content at the same time can result in increased load on your origin server.

###  Console 

  1. In the Google Cloud console, go to the **Media CDN** page. 

[Go to Media CDN](https://console.cloud.google.com/net-services/media-cdn)

  2. Click the **Services** tab.
  3. Click a service.
  4. Click the **Cache invalidation** tab.
  5. To invalidate the cache by tags, for **Cache tags** , specify one or more tags to invalidate the cache. Use spaces or commas to separate tags. You can add a maximum of 10 cache tags for invalidation.
  6. Click **Invalidate**.



###  gcloud 
    
    
    gcloud edge-cache services invalidate-cache SERVICE_NAME \
        --tags=TAGS
    

Replace the following:

  * `SERVICE_NAME` with the name of the Edge Cache service.
  * `TAGS` with a comma-separated list of tags.



For example:
    
    
    gcloud edge-cache services invalidate-cache SERVICE_NAME \
        --tags="status=404,content-type=text/plain"
    

## Invalidation latency

Cache invalidation across Media CDN's thousands of locations typically completes within one minute globally.

In some cases, invalidation can take longer, depending on system load, connectivity, and the volume of content being invalidated.

## Logging

If audit logs are enabled, invalidation calls are logged to Cloud Logging.

## Limitations

Invalidations are rate-limited. If you exceed the [invalidations rate limit](https://docs.cloud.google.com/media-cdn/quotas#api-rate-limits), you get an HTTP `429` error message with the status `RESOURCE_EXHAUSTED`.

Each invalidation request counts as a single operation against your rate limit, regardless of the size or scope of the path. For example, invalidating a single file (`/images/my-image.png`) or a wildcard path (`/images/*`) both count as one invalidation request.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
