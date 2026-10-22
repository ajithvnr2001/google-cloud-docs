---
url: https://docs.cloud.google.com/cdn/docs/dynamic-compression/
title: Enable dynamic compression \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:26.507110+00:00
---

# Enable dynamic compression  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/dynamic-compression/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Enable dynamic compression Stay organized with collections  Save and categorize content based on your preferences. 

Dynamic compression automatically compresses responses served by Cloud CDN. The size of the data sent over the network is reduced by [60% to 85% in typical cases](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/optimize-encoding-and-transfer#text_compression_with_gzip).

The size reduction reduces the time it takes to download content. For important assets like stylesheets (CSS), scripts (JavaScript), and video manifests (HLS/DASH), this can reduce page load and video start times.

You can learn more about the benefits of compressing responses in the [Web Fundamentals guide](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/optimize-encoding-and-transfer).

You can enable compression on a backend service or a backend bucket.

**Note:** Dynamic compression is configured on a backend service or a backend bucket and cannot be configured in a URL map. However, you can apply caching policies within a URL map for more granular control. If compression is enabled on the backend, the responses that meet the compression criteria will still be compressed.

## Example use cases

Dynamic compression directly reduces the size of data sent from the Cloud CDN edge to the client. This can directly do the following:

  * Reduce the size of CSS and JavaScript, helping web pages render faster and reducing the time to [First Contentful Paint](https://web.dev/first-contentful-paint/), an important web performance metric.
  * Have a large, positive impact when caching REST API responses, such as JSON payloads. These payloads compress well due to the repeated keys, whitespace, and braces. Caching public APIs for 5-10 seconds is a popular approach to reducing origin load while maintaining the freshness of data.

Even without caching, compressing these responses can reduce the total bytes sent by up to 90%.

  * Improve playback start time for video delivery and join latency for live streaming. Large live playlists (manifests) have a significant amount of repeated data, including the host + path prefix of each segment, as well as the HLS or DASH playlist metadata. The faster the playlist loads or playlist updates can be downloaded, the less time a client is waiting to parse and start downloading the referenced video segments. HLS and DASH playlists often see a total size reduction of more than 90%.




## Before you begin

Make sure that you have the following:

  * A Cloud CDN-enabled backend configured. If you don't have Cloud CDN configured, you can follow one of the [setup guides](https://docs.cloud.google.com/cdn/docs/using-cdn).
  * Your backend has compressible content ready to serve, such as web assets or video manifests between 1 KiB and 10 MiB (inclusive).
  * Clients don't rely on fetching partial content with range requests or with strong ETags. These are incompatible with dynamic compression.
  * Clients can handle responses without `Content-Length` headers. For example, cache misses that Cloud CDN compresses don't have `Content-Length` headers.
  * The IAM [Compute Load Balancer Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.loadBalancerAdmin) (`roles/compute.loadBalancerAdmin`), which is required to make changes to your backend configuration.



## Enable compression on a backend service or backend bucket

To enable compression, follow these steps.

### Console

**Add a new origin**

To add and set up a new origin, follow the instructions in [Setup overview](https://docs.cloud.google.com/cdn/docs/using-cdn) for the appropriate type of backend. When creating your origin, use the **Advanced options** section to configure dynamic compression by selecting **Automatic** in the **Compression mode** list.

**Edit an existing origin**

To edit an existing Cloud CDN origin:

  1. In the Google Cloud console, go to the Cloud CDN **Origins** page.

[Go to Origins](https://console.cloud.google.com/net-services/cdn/list)

  2. Click the origin name that you want to edit, and then click **Edit**.

  3. In the **Origin basics** section, click **Next**.

  4. In the **Host and path rules** section, click **Next**.

  5. In the **Cache performance** section, navigate to **Advanced options**.

  6. In the **Compression mode** list, select **Automatic**.

  7. To apply your changes, click **Done**.




### gcloud

For backend services, use the [`gcloud compute backend-services create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/create) or [`gcloud compute backend-services update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update) with the `--compression-mode` flag.

For backend buckets, use the [`gcloud compute backend-buckets create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/create) or the [`gcloud compute backend-buckets update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-buckets/update) with the `--compression-mode` flag.

For a new backend service, use the `create` command:
    
    
    gcloud compute backend-services create BACKEND_SERVICE_NAME \
        --compression-mode=AUTOMATIC
    

For an existing backend service, use the `update` command:
    
    
    gcloud compute backend-services update BACKEND_SERVICE_NAME \
        --compression-mode=AUTOMATIC
    

For a new backend bucket, use the `create` command:
    
    
    gcloud compute backend-buckets create BACKEND_BUCKET_NAME
        --compression-mode=AUTOMATIC
    

For an existing backend bucket, use the `update` command:
    
    
    gcloud compute backend-buckets update BACKEND_BUCKET_NAME
        --compression-mode=AUTOMATIC
    

The `compression-mode` can be one of the following:

  * `AUTOMATIC`: Automatically uses the best compression based on the `Accept-Encoding` header sent by the client. In most cases, this results in Brotli compression being favored.
  * `DISABLED` (default): Disables compression.



### API

For backend services, use the [`backendServices.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/insert) or the [`backendServices.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices/update).

For backend buckets, use the [`backendBuckets.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendBuckets/insert) or the [`backendBuckets.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendBuckets/update).

Use one of the following commands:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices
    
    
    
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE
    
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets
    
    
    
    PUT https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendBuckets/BACKEND_BUCKET
    

Add the following snippet to the JSON request body:
    
    
    "compressionMode": AUTOMATIC
    

The `compression-mode` can be one of the following:

  * `AUTOMATIC` (recommended): Automatically uses the best compression based on the `Accept-Encoding` header sent by the client. In most cases, this results in Brotli compression being favored.
  * `DISABLED` (default): Disables compression.



Within a few minutes, your configuration propagates to all edge locations. Compressible content served from the backend is compressed before being delivered to the client.

## Compression modes

The default compression mode is `DISABLED`.

`AUTOMATIC` mode allows Cloud CDN to choose the best compression method based on the following:

  * The client's accepted encoding
  * The response's anticipated compression ratio
  * Cloud CDN's compression speed (throughput)



Brotli can yield an additional 10% to 20% reduction in download size for most content types over gzip, with similar decompression performance, making it faster overall when considering download time _and_ decompression speed on the client.

Cloud CDN indicates the chosen compression method as `gzip` or `brotli` in the `Content-Encoding` header in the response.

Cloud CDN determines the compression level to balance total download size and CPU cost on the client. Higher compression levels don't always benefit performance, especially on lower-powered mobile devices.

When Cloud CDN initially compresses content, it removes the `Content-Length` header from the response; this is necessary to allow the response to be served as quickly as possible because the full content length is unknown until the entire response has been compressed. After a response has been compressed and cached, Cloud CDN might include the `Content-Length` header in subsequent responses. (For HTTP/1.1 and earlier, Cloud CDN uses `Transfer-Encoding: chunked` in the response when it doesn't use `Content-Length`.)

## When is a response compressed?

If a request has an `Accept-Encoding` header that explicitly lists support for either gzip or Brotli algorithms, then uncompressed responses served from the backend (origin) with a `Content-Type` header that matches the compressible content types are compressed with gzip or Brotli, accordingly. If a request has no `Accept-Encoding` header, or if it has `Accept-Encoding: *`, the response is not compressed.

For example, given an `Accept-Encoding` header in a client request, the response is compressed (or not) according to the information in the following table:

Accept-Encoding request header | Response encoding  
---|---  
`gzip, compress, br` | Brotli (br)  
`deflate` | Not compressed  
`deflate, gzip` | gzip  
`identity` | Not compressed  
`*` | Not compressed  
  
### Compressible content types

Dynamic compression applies to the following MIME types, based on the `Content-Type` HTTP response header. Responses that don't have a `Content-Type` response header aren't compressed.

Common content types and their MIME types include the following:

  * HTML content: `text/html`
  * Stylesheets: `text/css`
  * JavaScript: `application/javascript`
  * JSON: `application/json`
  * HLS playlists: `application/x-mpegURL` or `application/vnd.apple.mpegURL`
  * DASH manifests: `application/dash+xml`



The following table summarizes how the MIME type affects compressibility.

| Compressible MIME types  
---|---  
**Exact match** | application/x-javascript  
application/x-sdch-dictionary  
application/javascript  
application/xml  
application/csv  
application/json  
application/json+protobuf  
application/signed-exchange  
application/vnd.apple.mpegurl  
application/wasm  
application/x-plist  
application/x-protobuffer  
application/x-protobuf  
application/x-nacl  
application/x-pnacl  
font/ttf  
font/otf  
font/eot  
image/svg+xml  
image/pwg-raster  
image/x-icon  
image/vnd.microsoft.icon  
video/vnd.mpeg.dash.mpd  
audio/mpegURL  
application/dash+xml  
application/vnd.ms-sstr+xml   
**Pattern match** | application/*+json  
application/*+xml  
application/*mpegURL  
text/*   
  
Image and video formats (such as `image/jpeg`, `image/png`, and `video/mpeg4`) are almost always already compressed, so Cloud CDN doesn't compress them. Re-compressing an already compressed response rarely reduces file size, and clients might exhibit unexpected behavior when receiving a response of this kind.

## When is a response not compressed?

Dynamic compression doesn't compress a response that has one or more of the following characteristics:

  * The response doesn't have a `Content-Type` header that matches a compressible content type.
  * It doesn't have a `Content-Length` header.
  * It has a `Content-Encoding` header.
  * It's smaller than 1 KiB.

The time spent compressing and decompressing often offsets any benefits. There's also less content to compress, which can reduce the effectiveness of compression and lead to a lower compression ratio.

  * It's larger than 10 MiB.

  * The applicable cache-control response header (`CDN-Cache-Control` if present, or `Cache-Control` if `CDN-Cache-Control` is not present) contains the no-transform directive.




## Range requests

When Cloud CDN compresses a response, Cloud CDN adds an `Accept-Ranges: none` header and replaces any existing `Accept-Ranges` headers. Cache hits for such responses ignore `Range` headers.

This prevents serving incorrect partial content to clients because there is no way to be sure whether a client expects a range of bytes from the compressed or uncompressed form of a resource.

## ETags

When dynamic compression compresses a response, any strong ETag headers are weakened, as required by [RFC 7232 section 2.3](https://datatracker.ietf.org/doc/html/rfc7232#section-2.3). For example, `ETag: "xyzzy"` is replaced with `ETag: W/"xyzzy"`.

## Vary header

When serving a response that has the potential to be compressed (depending on the request), Cloud CDN adds the `Vary: Accept-Encoding` header to the response.

## Summary of response changes

The following table summarizes the changes that Cloud CDN makes to a response's headers when compression has occurred:

Response header | Header value after compression  
---|---  
`Content-Encoding` | Set to `gzip` or `brotli`.  
`ETag` | Any strong entity tag is replaced with a weakened version, indicated by the prefix `W/`.  
`Accept-Ranges` | Set to the value `none`.  
`Content-Length` | Might be removed entirely, or if present, set to the length of the compressed body content.  
`Transfer-Encoding` | For HTTP/1.1 and older protocols, if Cloud CDN removes `Content-Length`, it adds this header, with its value set to `chunked`, and chunks the body of the response.  
  
## Logging

The Cloud CDN logs include a `compressionStatus` field in the `jsonPayload` indicating whether the response was compressed by the load balancer as well as the compression type.
    
    
    {
      insertId: "1c02hw9g3gjay67"
      jsonPayload: {
        @type: "type.googleapis.com/google.cloud.loadbalancing.type.LoadBalancerLogEntry"
        statusDetails: "response_sent_by_backend"
        cacheId: "IAD-862d661f"
        compressionStatus: "br"
      }
    }
    

## Billing

When a response is compressed by Cloud CDN or Cloud Load Balancing, the relevant outbound cache data transfer or outbound internet data transfer (respectively) is measured against the final compressed bytes sent to the client.

If you are serving a large amount of compressible responses, this can result in a reduction in your monthly outbound data transfer fees, as well as increased performance for end users.

## Metrics

When compression is enabled, the existing `https/response_bytes_count` metric under `loadbalancing.googleapis.com` reports the compressed response size.

You can expect to see a drop in total response bytes (and outbound data transfer throughput).

If you are serving a large amount of text-based content that compresses well, such as HTML, CSS, JavaScript, or JSON, you might see a large drop in response bytes.

For more information, see [Monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#monitoring).

## What's next

  * To understand how cache modes make it easier to cache content, see [Change cache modes](https://docs.cloud.google.com/cdn/docs/using-cache-modes).
  * To enable Cloud CDN for your HTTP(S) load balanced instances and storage buckets, see [Setup overview](https://docs.cloud.google.com/cdn/docs/using-cdn).
  * To learn about invalidating caches, see [Cache invalidation overview](https://docs.cloud.google.com/cdn/docs/cache-invalidation-overview).
  * To find GFE points of presence, see [Cache locations](https://docs.cloud.google.com/cdn/docs/locations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
