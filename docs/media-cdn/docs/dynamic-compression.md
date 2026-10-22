---
url: https://docs.cloud.google.com/media-cdn/docs/dynamic-compression/
title: Enable dynamic compression \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:39.500800+00:00
---

# Enable dynamic compression  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/dynamic-compression/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Enable dynamic compression Stay organized with collections  Save and categorize content based on your preferences. 

Dynamic compression automatically compresses responses served by Media CDN. The size of the data sent over the network is reduced by [60% to 85% in typical cases](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/optimize-encoding-and-transfer#text_compression_with_compression_algorithms).

The size reduction accelerates the download of important assets, such as stylesheets (CSS), scripts (JavaScript), and video manifests (HLS/DASH), which can significantly reduce page load and video start times.

Large live video playlists (manifests) have a significant amount of repeated data and fetches, including the host and path prefix of each segment, as well as the HLS or DASH playlist metadata. The faster the playlist loads or playlist updates can be downloaded, the less time that a client needs to wait to parse and start downloading the referenced video segments. HLS and DASH playlists often undergo a total size reduction of more than 90%.

For more information about the benefits of compressing responses, see the [Web Fundamentals guide](https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/optimize-encoding-and-transfer).

## How dynamic compression works

When dynamic compression is enabled, [compressible content](https://docs.cloud.google.com/media-cdn/docs/dynamic-compression#compressible-content) that is served from the origin can be compressed before being delivered if the client accepts one of the supported compression algorithms (`br` or `gzip`).

Media CDN adds a `Vary: Accept-Encoding` header to all responses eligible for compression. For related information, see [Incompressible content](https://docs.cloud.google.com/media-cdn/docs/dynamic-compression#response-not-compressed).

Additionally, if the request's `Accept-Encoding` header indicates a preference for compressed content by specifying `br` or `gzip` (and optionally including a nonzero `q` parameter), Media CDN does the following:

  * Removes the `Content-Length` header from the response; this is necessary to allow the response to be served as quickly as possible because the full content length is unknown until the entire response has been compressed. For HTTP/1.1 and earlier, Media CDN uses `Transfer-Encoding: chunked` in the response when it doesn't use `Content-Length`.

After a response has been compressed and cached, Media CDN can include the `Content-Length` header in subsequent responses and set the value to the length of the compressed body content.

  * Sets `Accept-Ranges` to `none`. This informs clients that range requests for this resource are ignored.

  * Weakens any strong `ETag` response headers, as required by [RFC 9110 section 8.8.3](https://datatracker.ietf.org/doc/html/rfc9110#section-8.8.3). For example, `ETag: "xyzzy"` is replaced with `ETag: W/"xyzzy"`.

  * Sets the `Content-Encoding` header to `br` or `gzip`, which signifies the chosen compression algorithm.

Media CDN chooses the best compression algorithm based on the anticipated compression ratio of the response and the compression speed or throughput.

    * Brotli compression is used if the client supports it, even if other compression algorithms have higher `q` values in the `Accept-Encoding` header.

    * HLS manifests are compressed using only `gzip`.

Media CDN determines the compression level to balance the total download size and CPU cost on the client. Higher compression levels don't always benefit performance, especially on lower-powered mobile devices.




## Configure dynamic compression

You can enable dynamic compression on routes serving requests.

### Before you begin

Do the following:

  * Identify or [create a Media CDN origin](https://docs.cloud.google.com/media-cdn/docs/quickstart#create-origin) with compressible content that is ready to serve.

  * Identify or [create a Media CDN service](https://docs.cloud.google.com/media-cdn/docs/quickstart#create-service) with at least one [route rule](https://docs.cloud.google.com/media-cdn/docs/routing#configure-route-rule).




### Enable dynamic compression for a route rule

By default, the compression mode for a route rule is disabled.

Setting the mode to automatic enables dynamic compression for every eligible response. Further, it instructs Media CDN to automatically choose the best compression algorithm.

To enable dynamic compression, do the following:

### Console

  1. In the Google Cloud console, go to the **Media CDN** page.

[Go to Media CDN](https://console.cloud.google.com/net-services/media-cdn)

  2. To open the **Details** page of the service for which you want to configure a route rule, click the service name.

  3. To switch to the edit mode, click the **Edit** button.

  4. To navigate to the **Routing** section, click **Next**.

  5. To edit a host rule, click the arrow to expand it.

  6. To edit a route rule, click edit**Edit** on the respective row.

  7. In the **Edit route rule** pane, click **Advanced configurations**.

  8. Optional: For **Route action** , add a [CDN policy](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1alpha1/projects.locations.edgeCacheServices#cdnpolicy) item.

A CDN policy lets Media CDN compress content once and serve it multiple times, which saves bandwidth and speeds up delivery.

  9. In the **Dynamic compression** section, select **Enable compression**.

  10. To save the route rule, click **Save**.

  11. To save your changes to the service, click **Update service**.




###  gcloud and YAML 

  1. [Export your Media CDN configuration](https://docs.cloud.google.com/media-cdn/docs/configuration#import-and-export) into a YAML file. Use the [`gcloud edge-cache services export` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/export).
         
         gcloud edge-cache services export SERVICE_NAME \
             --destination=FILENAME.yaml
         

Replace the following:

     * `SERVICE_NAME`: the name of your service
     * `FILENAME` : the name of your YAML file
  2. In the route definition in the YAML file, under `routeAction`, set `compressionMode` to `AUTOMATIC`, as shown in the following sample:
         
         routing:
         hostRules:
         - hosts:
           - media.example.com
           pathMatcher: routes
         pathMatchers:
         - name: routes
           routeRules:
             - priority: 2
         origin: origin1
         matchRules:
         - pathTemplateMatch: "/**.m3u8" # HLS playlists
         - pathTemplateMatch: "/**.mpd" # DASH manifests
         routeAction:
           cdnPolicy:
             defaultTtl: 5s
           compressionMode: AUTOMATIC
         

  3. To update the service, [import your Media CDN configuration](https://docs.cloud.google.com/media-cdn/docs/configuration#import-and-export) from the YAML file. Use the [`gcloud edge-cache services import` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/import).
         
         gcloud edge-cache services import SERVICE_NAME \
             --source=FILENAME.yaml
         




###  Terraform 

The following Terraform snippet shows a route rule with dynamic compression enabled.
    
    
    route_rule {
      description = "a route rule with dynamic compression, priority=2 (high)"
      priority    = 2
      match_rule {
        path_template_match = "/**.m3u8" # HLS playlists
      }
      match_rule {
        path_template_match = "/**.mpd" # DASH manifests
      }
      origin = google_network_services_edge_cache_origin.default.name
      route_action {
        cdn_policy {
          cache_mode = "FORCE_CACHE_ALL"
          client_ttl = "300s"
        }
    **compression_mode = "AUTOMATIC"**
      }
      header_action {
        response_header_to_add {
          header_name  = "x-cache-status"
          header_value = "{cdn_cache_status}"
        }
      }
    }

Your configuration shortly propagates to all edge locations.

When dynamic compression is enabled for a route and the new configuration takes effect in production machines, Media CDN begins compressing eligible responses, even if uncompressed cached versions exist. While Media CDN fetches and compresses new content, there might be a temporary spike in the traffic to your origin.

### Disable dynamic compression for a route rule

To disable dynamic compression, do the following:

### Console

  1. In the Google Cloud console, go to the **Media CDN** page.

[Go to Media CDN](https://console.cloud.google.com/net-services/media-cdn)

  2. To open the **Details** page of the service for which you want to configure the route rule, click the service name.

  3. To switch to the edit mode, click the **Edit** button.

  4. To navigate to the **Routing** section, click **Next**.

  5. To edit a host rule, click the arrow to expand it.

  6. To edit a route rule, click edit**Edit** on the respective row.

  7. In the **Edit route rule** pane, click **Advanced configurations**.

  8. In the **Dynamic compression** section, deselect **Enable compression**.

  9. To save the route rule, click **Save**.

  10. To save your changes to the service, click **Update service**.




###  gcloud and YAML 

  1. [Export your Media CDN configuration](https://docs.cloud.google.com/media-cdn/docs/configuration#import-and-export) into a YAML file. Use the [`gcloud edge-cache services export` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/export).
         
         gcloud edge-cache services export SERVICE_NAME \
             --destination=FILENAME.yaml
         

Replace the following:

     * `SERVICE_NAME`: the name of your service
     * `FILENAME` : the name of your YAML file
  2. In the route definition in the YAML file, set `compressionMode` to `DISABLED`.

  3. To update the service, [import your Media CDN configuration](https://docs.cloud.google.com/media-cdn/docs/configuration#import-and-export) from the YAML file. Use the [`gcloud edge-cache services import` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/import).
         
         gcloud edge-cache services import SERVICE_NAME \
             --source=FILENAME.yaml
         




If you encounter issues with dynamic compression for a specific route, such as compatibility problems with certain clients (for example, smart TVs or streaming devices), to prevent Media CDN from serving compressed content on that route, disable dynamic compression.

Disabling dynamic compression for a route causes Media CDN to stop serving compressed content from cache. All previously cached compressed responses become invalid, and the CDN fetches uncompressed versions from your origin.

## Compressible content types

Dynamic compression applies to the following MIME types, based on the `Content-Type` HTTP response header. Responses that don't have a `Content-Type` header aren't compressed.

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
**Exact match** |  application/csv  
application/javascript  
application/json  
application/json+protobuf  
application/signed-exchange  
application/wasm  
application/x-javascript  
application/x-nacl  
application/x-plist  
application/x-pnacl  
application/x-protobuf  
application/x-protobuffer  
application/x-sdch-dictionary  
application/xml  
audio/mpegURL  
font/eot  
font/otf  
font/ttf  
image/pwg-raster  
image/svg+xml  
image/vnd.microsoft.icon  
image/x-icon  
video/vnd.mpeg.dash.mpd  
  
**Pattern match** | application/*+json  
application/*+xml  
application/*mpegURL  
text/*   
  
Image and video formats (such as `image/jpeg`, `image/png`, and `video/mpeg4`) are almost always already compressed. So, Media CDN doesn't compress them. Re-compressing an already compressed response rarely reduces file size, and clients might exhibit unexpected behavior when receiving a response of this kind.

## Incompressible responses

Media CDN doesn't compress a response that has one or more of the following characteristics:

  * The response doesn't have a `Content-Type` header that matches a compressible content type.
  * The response doesn't have a `Content-Length` header.
  * The response has a `Content-Encoding` header. This implies that the origin has already compressed the response. So Media CDN must not do any additional dynamic compression.
  * The response is smaller than 1 KiB.

The time spent compressing and decompressing often offsets any benefits. There's also less content to compress, which can reduce the effectiveness of compression and lead to a lower compression ratio.

  * The response is larger than 1 MiB.

Media CDN compresses responses up to the size allowed for caching objects without byte-range caching.

  * The response has a `Cache-Control: no-transform` header.




## Logging and monitoring

When compression is enabled, the existing `https/response_bytes_count` metric under `edgecache.googleapis.com/EdgeCacheRouteRule` reports the compressed response size. You can expect to see a drop in total response bytes and outbound data transfer throughput for compressible content.

The Media CDN logs include a `compressionAlgorithmApplied` field in the `jsonPayload`, which indicates whether the response was compressed by the load balancer as well as the compression type.
    
    
    {
      insertId: "1c02hw9g3gjay67"
      jsonPayload: {
        @type: "type.googleapis.com/google.cloud.edgecache.v1.EdgeCacheLogEntry",
        cacheId: "IAD-862d661f",
        cacheStatus": "hit,stale",
        compressionAlgorithmApplied: "br"
      },
    }
    

## Billing

When a response is compressed by Media CDN, the relevant outbound cache or internet data transfer charges are based on the final compressed bytes sent to the client.

If you are serving a large amount of compressible responses, this can result in a reduction in your monthly outbound data transfer fees, as well as increased performance for end users.

## What's next

  * [Configure service routes](https://docs.cloud.google.com/media-cdn/docs/routing)
  * [Configure request logging](https://docs.cloud.google.com/media-cdn/docs/configure-request-logging)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
