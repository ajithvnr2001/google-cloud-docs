---
url: https://docs.cloud.google.com/media-cdn/docs/routing/
title: Configure service routes \u00a0|\u00a0 Media CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:49.374923+00:00
---

# Configure service routes  |  Media CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/media-cdn/docs/routing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Media CDN ](https://docs.cloud.google.com/media-cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/media-cdn/docs/overview)



Send feedback 

#  Configure service routes Stay organized with collections  Save and categorize content based on your preferences. 

Media CDN provides advanced HTTP routing capabilities that allow you to map traffic to specific edge configurations and origins at a fine-grained level.

## Configure a route rule

Configure a route rule for a Media CDN service.

### Console

  1. In the Google Cloud console, go to the **Media CDN** page.

[Go to Media CDN](https://console.cloud.google.com/net-services/media-cdn)

  2. To open the **Details** page of the service for which you want to configure a route rule, click the service name.

  3. To switch to the edit mode, click the **Edit** button.

  4. To navigate to the **Routing** section, click **Next**.

  5. Specify at least one host rule. Click **Add host rule**. Then, do the following:

     1. For **Hosts** , specify at least one [host for matching](https://docs.cloud.google.com/media-cdn/docs/routing#host-matching).

     2. For **Description** , provide a brief description for the host rule.

Alternatively, to edit a host rule, click the arrow to expand it.

  6. Specify at least one route rule. Click **Add route rule**.

Alternatively, to edit a route rule, click edit**Edit** on the respective row.

  7. In the **Edit route rule** pane, for **Priority** , set a value for [route priority](https://docs.cloud.google.com/media-cdn/docs/routing#route-priority).

  8. For **Description** , provide a brief description that can help identify the rule in a list of rules.

  9. In the **Match** section, specify at least one match condition. Click **Add a match condition**. Then, do the following:

     1. For **Match type** , select any [path match](https://docs.cloud.google.com/media-cdn/docs/routing#path-matching) option.
     2. For **Path match** , specify the names, paths, or templates. Consider using [wildcard pattern matching](https://docs.cloud.google.com/media-cdn/docs/routing#pattern-matching).

If required, also select **Enable case sensitivity for path value**.

     3. Optional: Select **Headers match** and **Query parameters match**. Then, click the relevant buttons to add headers and query parameters. For each, specify the name, match type, and value.

For more information, see [Match on headers and query parameters](https://docs.cloud.google.com/media-cdn/docs/routing#matching-header-query).

     4. To save the match condition, click **Done**.

  10. For **Primary action** , select one of the following options:

     * **Fetch from an origin** : To direct requests to a specific origin, select this option, and then select an origin.

     * **URL redirect** : To [redirect requests](https://docs.cloud.google.com/media-cdn/docs/routing#redirect-requests), select this option. Then, specify the type of redirect, the path, and the status code.

Optionally, select the options to [redirect all responses to HTTPS](https://docs.cloud.google.com/media-cdn/docs/routing#https-redirect), or to strip the query.

  11. Click **Advanced configurations**.

     1. In the **Header action** section, click **Add an item**.

Select a type of action and then specify a header as a name and value pair. Then, click **Done**.

     2. In the **Route action** section, click **Add an item**.

Specify a type of action and its related options. Then, click **Done**.

  12. For **HTTP method filtering** , select **Customize HTTP method filtering**.

Then, select the [HTTP methods](https://docs.cloud.google.com/media-cdn/docs/routing#method-filtering) that you want proxied to your origin.

  13. To save the route rule, click **Save**.

  14. To save your changes to the service, click **Update service**.




###  gcloud and YAML 

  1. [Export your Media CDN configuration](https://docs.cloud.google.com/media-cdn/docs/configuration#import-and-export) into a YAML file. Use the [`gcloud edge-cache services export` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/export).
         
         gcloud edge-cache services export SERVICE_NAME \
             --destination=FILENAME.yaml
         

Replace the following:

     * `SERVICE_NAME`: the name of your service
     * `FILENAME` : the name of your YAML file
  2. Update the YAML file with the required configuration as described in the sections on this page.

  3. To update the service, [import your Media CDN configuration](https://docs.cloud.google.com/media-cdn/docs/configuration#import-and-export) from the YAML file. Use the [`gcloud edge-cache services import` command](https://docs.cloud.google.com/sdk/gcloud/reference/edge-cache/services/import).
         
         gcloud edge-cache services import SERVICE_NAME \
             --source=FILENAME.yaml
         




## Match requests

A Media CDN configuration contains a set of routes defined in the [Routing](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices#routing) section for an [`EdgeCacheService`](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices#resource:-edgecacheservice) resource. These routes match requests based on (at least) a host. For more details about how traffic is directed to an origin, see [`HostRule`](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices#hostrule) and [`PathMatcher`](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices#pathmatcher). Each route is able to define its own CDN configuration, rewrites, redirects, CORS policies, custom HTTP headers, and origin mapping. Routes can share origins.

For example, you can route requests for manifests to a specific origin and define a [short-lived cache TTL](https://docs.cloud.google.com/media-cdn/docs/caching#cache-modes) and a [negative caching policy](https://docs.cloud.google.com/media-cdn/docs/caching#negative-caching). Requests for segments can be split to another origin by using [headers and query parameters](https://docs.cloud.google.com/media-cdn/docs/caching#cache-keys) to break out specific manifest types or users.

The following example shows how to route requests that match a specific header, query parameter, and path prefix for the host `media.example.com`:
    
    
    name: prod-service
    routing:
      hostRules:
      - hosts:
        - media.example.com
        pathMatcher: example_routes
      pathMatchers:
      - name: example_routes
        routeRules:
        - priority: 10
          origin: staging-live-origin
          matchRules:
          - prefixMatch: /vod/
            headerMatches:
            - headerName: "x-staging-client"
              presentMatch: true
            queryParameterMatches:
            - name: "live"
              exactMatch: "yes"
          routeAction:
            cdnPolicy:
              defaultTtl: 5s

### Path matching

Media CDN supports full (exact), prefix, and wildcard path matching. Path matching can be combined with host, header, and query parameter-based matching to construct fine-grained request routing rules.

**Warning:** Do not include confidential, sensitive, or personally identifiable information in your URL paths or query parameters. URLs, including host, path and query parameters, are treated as non-identifiable service data in accordance with Section 12 (Resource Fields) of the [Service Specific Terms](https://cloud.google.com/terms/service-terms). As a privacy and security best practice, URL components should be opaque system-generated identifiers, not derived from end user input.

Following are three ways to match on a URL path.

Field | Description | Example  
---|---|---  
`matchRules[].fullPathMatch` |  The `fullPathMatch` condition matches the full URL path, which does not include the query string. You must specify trailing slashes, if relevant.  |  A route with a match rule of `fullPathMatch: "/stream/"` matches `/stream/` but not `/stream` or `/stream/us/hls/1234.ts`. A `fullPathMatch` is an explicit (exact) match.  
`matchRules[].prefixMatch` |  The `prefixMatch` condition matches the URL path prefix; URLs that start with the same string match.  |  A route with a match rule of `prefixMatch: "/videos/"` matches both `/videos/hls/58481314/manifest.m3u8` and `/videos/dash` because they both contain the `/videos/` prefix.  
`matchRules[].pathTemplateMatch` |  The `pathTemplateMatch` condition supports wildcard operators, allowing you to match complex URL patterns and path segments, as well as capture named variables for rewriting URLs.  |  A route with a match rule of `pathTemplateMatch: "/**.m3u8"` matches any URL path ending with `.m3u8`. Both `/content/en-GB/13/51491/manifest_193193.m3u8` and `/p/abc/1234/manifest_1080p5000.m3u8` match this pattern. For more examples, see the pattern matching section.   
  
For more details, see the API specification for [`MatchRule`](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices#matchrule).

**Caution:** A route must have a `matchRule` with exactly one of `prefixMatch`, `fullPathMatch`, or `pathTemplateMatch` defined. If you don't include one of those fields, the API returns an error.

For example, to match all requests starting with `/stream/`, create a route rule similar to the following:
    
    
    name: prod-service
    routing:
      hostRules:
      - hosts:
        - media.example.com
        - *.vod.example.com
        pathMatcher: example_routes
      pathMatchers:
      - name: example_routes
        routeRules:
        - priority: 1
          matchRules:
          - prefixMatch: /stream/

This example explicitly includes the trailing slash in the match rule:

  * A request to `media.example.com/stream/id/1234/hls/manifest.m3u8` matches this route.
  * A request to `media.example.com/stream-eu/id/4567/hls/manifest.m3u8` does not match this route.



In the second case, Media CDN returns an HTTP `404` error, unless there was another route or a catch-all route configured.

For guidance about how predecence works for routes with similar prefixes, see the route priority and ordering section.

### Pattern (wildcard) matching

Pattern matching lets you match multiple parts of a URL, including partial URLs and suffixes (file extensions), by using wildcard syntax.

You can also associate one or more path segments with named variables in a `pathTemplateMatch` field, and then refer to those variables when rewriting the URL in a `pathTemplateRewrite` field. This lets you reorder and remove URL segments before the request is sent to your origin.

The following example shows how you can match on two different URL suffixes:
    
    
    # EdgeCacheService.routing.pathMatchers[]
        routeRules:
        - priority: 1
          description: "Match video segments"
          matchRules:
          - pathTemplateMatch: "/**.ts"
          - pathTemplateMatch: "/**.m4s"
          origin: prod-video-storage

The supported syntax includes the following.

Operator | Matches | Example  
---|---|---  
`*` |  Matches a single path segment, up to the next path separator: `/` |  `/videos/*/*/*.m4s` matches `/videos/123414/hls/1080p5000_00001.m4s`.   
`**` |  Matches zero or more path segments. If present, must be the last operator.  |  `/**.mpd` matches `/content/123/india/dash/55/manifest.mpd`.   
`{name} or {name=*}` |  A named variable matching one path segment.  Matches a single path segment, up to the next path separator: `/`.  |  `/content/{format}/{lang}/{id}/{file}.vtt` matches `/content/hls/en-us/12345/en_193913.vtt` and captures `format="hls"`, `lang="en-us"`, `id="12345"`, and `file="en_193913"` as variables.   
`{name=videos/*}` |  A named variable matching more than one path segment. The path segment matching `videos/*` is captured as the named variable.  |  `/videos/{language=lang/*}/*` matches `/videos/lang/en/video.m4s` and populates the path variable `language` with the value `lang/en`.   
`{name=**}` |  A named variable matching zero or more path segments.  If present, must be the last operator.  |  `/**.m3u8` or `/{path=**}.m3u8` matches all path segments up to the extension.  `/videos/{file=**}` matches `/videos/en-GB/def566/manifest.m3u8`, including the extension, and captures the path variable `file="en-GB/def566/manifest.m3u8`.   
  
Notes:

  * If you aren't rewriting a URL, use the simpler `*` and `**` operators.
  * When using variables to capture path segments, any parts of the URL that aren't captured by a variable can't be referenced in a subsequent `pathTemplateRewrite`. For an example, see the capturing path variables section.
  * You can't refer to variables in a subsequent `pathTemplateRewrite` that don't exist in the `pathTemplateMatch` on the same route.
  * Variables are case-sensitive, with`{FORMAT}`, `{forMAT}`, and `{format}` representing different variables and values.
  * You can specify up to 10 operators (wildcards or variables) in a match. The `pathTemplateMatch` and `pathTemplateRewrite` fields must not exceed 255 characters.



#### Example: Match on a file extension

The following example shows a common use-case for wildcard operators: matching all path segments up to a suffix.

In this case, you do the following:

  * Fetch video manifests (playlists) ending in `.m3u8` and `.mpd` from the manifest origin, applying a short (5-second) TTL to these responses because they change regularly.
  * Fetch video segments ending in `.ts` and `.m4s` from the segment origin, and apply a longer (1-day) TTL to these responses.



This approach is often employed when using SSAI (Server-Side Ad Injection) or DAI (Dynamic Ad Insertion) services, and for live video where the manifest is updated every few seconds.

The following configuration demonstrates how to configure your Media CDN routing to support this:
    
    
    name: prod-service
    routing:
      hostRules:
      - hosts:
        - media.example.com
        pathMatcher: example_routes
      pathMatchers:
      - name: example_routes
        routeRules:
        # the first route only matches video manifests
        - priority: 1
          matchRules:
          - pathTemplateMatch: "/**.m3u8" # "**" matches all path segments
          - pathTemplateMatch: "/**.mpd"
          origin: manifest-origin
          routeAction:
            cdnPolicy:
              cacheMode: FORCE_CACHE_ALL
              defaultTtl: 5s
        # the second route matches video segments, fetches them
        # from a separate origin server, caching them for a longer
        # duration (1 day).
        - priority: 2
          matchRules:
          - pathTemplateMatch: "/**.ts"
          - pathTemplateMatch: "/**.m4s"
          origin: segment-origin
          routeAction:
            cdnPolicy:
              cacheMode: FORCE_CACHE_ALL
              defaultTtl: 86400s

#### Example: Capture path variables

The following example shows how to use named variables to describe one or more path segments.

These variables can be used in a `pathTemplateRewrite` to rewrite the path prior to the request being sent to the origin, or to make a complex `pathTemplateMatch` self-describing.
    
    
    routing:
      hostRules:
      - hosts:
        - media.example.com
        pathMatcher: example_routes
      pathMatchers:
      - name: example_routes
        routeRules:
        - priority: 1
          matchRules:
          # Matches a request of "/us/en/hls/123139139/segments/00001.ts"
          - pathTemplateMatch: "/{country}/{lang}/{format}/{id}/{file=**}"
          origin: my-origin
          routeAction:
            urlRewrite:
              # Rewrites to "/123139139/hls/segments/00001.ts"
              pathTemplateRewrite: "/{id}/{format}/{file}"

Specifically:

  * Each `{name}` variable captures a single path segment. A path segment is all characters between a pair of `/` ("slashes") in a URL path.
  * A variable of `{name=**}` captures all remaining path segments; in this case, it matches both `segments/00001.ts` and `master.m3u8`.
  * In the `pathTemplateRewrite` _on the same route_ , you refer back to _some_ of the variables that you captured in the `pathTemplateMatch`. You explicitly omit the `{country}` and `{lang}` variables because they don't match the directory structure on the origin.



With this example, the following occurs:

  * An incoming request URL of `/us/en/hls/123139139/segment_00001.ts` matches the `pathTemplateMatch` and is rewritten to `/123139139/hls/segment_00001.ts` prior to being sent to the origin.
  * An incoming request URL of `/us/123139139/master.m3u8` does _not_ match the `pathTemplateMatch`, and receives an HTTP `404 (Not Found)` status code.
  * An incoming request URL of `/br/es/dash/c966cbbe6ae3/subtitle_00001.vtt` also matches the `pathTemplateMatch` and is rewritten to `/c966cbbe6ae3/dash/subtitle_00001.vtt` prior to being sent to the origin.



To learn more about how wildcard matching interoperates with URL rewriting, see the rewrites section.

### Host matching

Each service can match on multiple hostnames, with each set of hostnames containing their own group of routes (known as _path matchers_). In the most common case, all hostnames for a service map to a single set of shared routes with a single list of hosts and a single path matcher.
    
    
    name: prod-service
    routing:
      hostRules:
      - hosts:
        - media.example.com
        - *.vod.example.com
        pathMatcher: example_routes
      pathMatchers:
      - name: example_routes
        routeRules:
        # list of routes for the configured hosts
        - priority: 999
          matchRules:
          - prefixMatch: /
          origin: DEFAULT_ORIGIN

Hosts that don't match are served a default HTTP `404` page. To accept any host, you can include the wildcard character `*` as a `hostRules[].hosts[]` entry.

You can also define groups of routes (for example, grouping by country or live versus on-demand). Because each service has a single security policy, we generally recommend having one service for each market (geography) or workload that you have.

Notes:

  * Host (or HTTP/2 `:authority`) headers that contain a port are implicitly matched against a configured host. You don't need to explicitly specify the ports.
  * If the request is over HTTP, a `hostRules[].hosts[]` entry of `*.vod.example.com` matches `us.vod.example.com` and `us.vod.example.com:80`.
  * If the request is over HTTPS (TLS), a `hostRules[].hosts[]` entry of `*.vod.example.com` matches `us.vod.example.com:443`.



For more details, see the API specification for [`HostRule`](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices#hostrule).

### Match on headers and query parameters

You can configure routes to match on specific header and query parameter names, as well as the presence of a header value (prefix, suffix, or exact match).

Query parameter and header matching are logical "AND"—the request must match all of the query parameters and header keys (and values, if specified) to match the given route.

For example, if you want to route requests with a specific header field name and header value to an origin named `alternate-origin`, configure your match conditions within `routeRules[].matchRules[].headerMatches[]`:
    
    
    name: prod-service
    routing:
      hostRules:
      - hosts:
        - media.example.com
        pathMatcher: example_routes
      pathMatchers:
      - name: example_routes
        routeRules:
        - priority: 1
          origin: alternate-origin
          matchRules:
          - prefixMatch: "/videos/"
            headerMatches:
            - headerName: "x-device-name"
              exactMatch: "roku"

In this example, requests with `/videos/` at the beginning of the URL and the `x-device-name: roku` header match this route. Requests missing this header name or with a different value don't match this route.

**Note:** If you have routes that match the same request path at a higher `priority` than routes that specify additional header and query parameter matching conditions, the lower `priority` routes are not matched. Ensure that routes with more specific matching conditions have a higher (smaller number) `priority` set.

For more details, see the API specification for [`HeaderMatch`](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices#headermatch).

Similarly, to match against query parameters, specify one or more `queryParameterMatches` as follows:
    
    
    name: prod-service
    routing:
      hostRules:
      - hosts:
        - media.example.com
        pathMatcher: example_routes
      pathMatchers:
      - name: example_routes
        routeRules:
        - priority: 1
          origin: eu-live-origin-prod
          matchRules:
          - prefixMatch: "/videos/"
            queryParameterMatches:
            - name: "playback_type"
              exactMatch: "live"
            - name: "geo"
              exactMatch: "eu"

In this example, a client request of `https://cdn.example.com/videos/1234/abcd/xyz.m3u8?playback_type=live&geo=eu` matches this route.

For more details, see the API specification for [`QueryParameterMatcher`](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices#queryparametermatcher).

### Define a catch-all (default) route

By default, Media CDN returns an HTTP `404 (Not Found)` error if a request doesn't match any configured routes.

To configure a _catch-all_ route, for a given `pathMatcher` (collection of routes), do the following:

  * Create a `routeRule` with the lowest priority (highest number)—for example, 999, which is the lowest possible route priority.
  * Configure a `matchRule` with a prefix match of `/` (matches all request paths).
  * Configure (one of) an `origin` or `urlRedirect` on the route.



For example, to configure a catch-all route that directs all unmatched requests to a default origin named `my-origin`, create a new route with `priority: 999` and a `matchRules[].prefixMatch` of `/` as follows:
    
    
    name: prod-service
    routing:
      hostRules:
      - hosts:
        - cdn.example.com
        pathMatcher: example_routes
      pathMatchers:
      - name: example_routes
        routeRules:
        - priority: 999
          origin: my-origin
          matchRules:
          - prefixMatch: /

You can optionally rewrite the URL prior to the origin fetch, or redirect to a default page (such as your landing page) instead of sending the request "as is" to the origin.

### Route priority and ordering

Each route in an array of `routeRules[]` must have a `priority` associated with it.

More specific routes should be set to a higher priority (smaller number). A route matching a prefix of `/stream/` with a priority of 1 otherwise prevents a more specific route of `/stream/live/eu/` with a priority of 5 from matching any requests.

  * The highest priority route is "1", and the lowest is "999".
  * You can't configure two or more routeRules with the same priority. Priority for each rule must be set to a number between 1 and 999 inclusive.
  * Defining a catch-all route lets you send all non-matching requests to a default origin or redirect them to a landing page or endpoint.



In the following example, you can see that the `/live/us/` route would never be matched because the `/live/` route is at a higher priority:
    
    
    routeRules:
    - priority: 1
      description: "Live routes"
      matchRules:
      - prefixMatch: /live/
      routeAction:
        cdnPolicy:
          defaultTtl: 5s
    - priority: 2
      description: "U.S based live streams"
      matchRules:
      # This would never be matched, as the /live/ prefixMatch at priority 1
      # would always take precedence.
      - prefixMatch: /live/us/
      routeAction:
        cdnPolicy:
          defaultTtl: 5s
    - priority: 999
      description: "Catch-all route"
      matchRules:
      - prefixMatch: /

To address this, you put the more specific (longer) route at a higher priority:
    
    
    routeRules:
    - priority: 1
      description: "U.S based live streams"
      matchRules:
      # The more specific (longer) match is at a higher priority, and now
      # matches requests as expected.
      - prefixMatch: /live/us/
      routeAction:
        cdnPolicy:
          defaultTtl: 5s
    - priority: 2
      description: "Live routes"
      matchRules:
      - prefixMatch: /live/
      routeAction:
        cdnPolicy:
          defaultTtl: 5s
    - priority: 999
      description: "Catch-all route"
      matchRules:
      - prefixMatch: /

This allows the more specific route to match requests correctly. A request prefixed with `/live/eu/` would still fall through to the `/live/` route at priority 2.

### Method filtering

By default, Media CDN proxies only `GET`, `HEAD`, and `OPTIONS` methods to your origin and filters out the methods that can modify your origin.

You can override this default behavior for a specific route rule by specifying the methods that you would like proxied to your origin. Besides `GET`, `HEAD`, and `OPTIONS`, Media CDN supports `PUT`, `POST`, `DELETE`, and `PATCH`.

Media CDN only retries or attempts failover for requests that use the safer HTTP methods, such as `GET`, `HEAD`, or `OPTIONS`.

**Note:** If a request using an unsafe method fails on the first attempt to the primary origin, Media CDN responds to the client with an HTTP `502 Bad Gateway` status code. It doesn't attempt any retries or failover to another origin. For more information on retries, see [Retry origin requests](https://docs.cloud.google.com/media-cdn/docs/origins#retry-origin-requests).

To configure support for a set of methods for a route rule, specify a `routeMethods` section that has an `allowed_methods` value for each method.
    
    
    routeRules:
    - priority: 5
      description: "Video uploads"
      routeMethods:
        allowedMethods: ["PUT", "POST", "OPTIONS"]
      matchRules:
      - pathTemplateMatch: "/uploads/**.ts"
      origin: prod-video-storage
    - priority: 10
      description: "Video serving"
      routeMethods:
        allowedMethods: ["GET", "HEAD"]
      matchRules:
      - pathTemplateMatch: "/videos/**.ts"
      origin: prod-video-storage

### Path normalization

Path normalization describes how Media CDN combines multiple representations of a URL into a single, canonical representation under specific scenarios.

Path normalization can directly improve cache hit rates by reducing the number of request URLs that represent the same content, and by mitigating origin errors for origins that expect normalized paths.

Incoming requests are normalized as per the following:

  * Multiple consecutive slashes are merged into a single slash. For example, a URL path of `/videos///12345/manifest.mpd` is normalized to `/videos/12345/manifest.mpd`.
  * Path segments are normalized according to [RFC 3986 Section 6.2.2.3](https://tools.ietf.org/html/rfc3986#section-6.2.2.3). For example, the path `/a/b/c/./../../g` is normalized to `/a/g` based on the "[remove dot segments](https://tools.ietf.org/html/rfc3986#section-5.2.4)" algorithm defined in RFC 3986. This normalization happens before checking the cache or forwarding the request to the origin.
  * Requests are **not** percent-encoding normalized. For example, a URL with a percent-encoded slash character (`%2F`) is not decoded into the un-encoded form.



URLs remain case-sensitive and are _not_ case-normalized. Many URLs contain case-sensitive base64 encodings, including URLs with [signed request](https://docs.cloud.google.com/media-cdn/docs/signed-requests) tokens.

## Rewrites and redirects

The following sections provide examples on how to rewrite requests and configure redirects.

### Rewrite request URLs

Media CDN supports host and path rewrites. Rewrites change the URL sent to the origin and let you modify hosts and paths as needed. Host and path rewrites are at the route level, letting you define what specific requests are rewritten based on any matcher, including path, query parameter, and request header.

**Warning:** Do not include confidential, sensitive, or personally identifiable information in your URL paths or query parameters. URLs, including host, path and query parameters, are treated as non-identifiable service data in accordance with Section 12 (Resource Fields) of the [Service Specific Terms](https://cloud.google.com/terms/service-terms). As a privacy and security best practice, URL components should be opaque system-generated identifiers, not derived from end user input.

For more details, see the API specification for [`RouteAction.UrlRewrite`](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices#urlrewrite).

Following are three ways to rewrite a request:

Field | Description  
---|---  
`urlRewrite.pathPrefixRewrite` |  Rewrites the path, removing the prefix specified in the `prefixMatch` that matched the request.  Only one of `pathPrefixRewrite` or `pathTemplateRewrite` can be specified in a single route rule.   
`urlRewrite.pathTemplateRewrite` |  `pathTemplateRewrite` can only be used with a corresponding `pathTemplateMatch` match rule on the same route.  Only one of `pathPrefixRewrite` or `pathTemplateRewrite` can be specified in a single route rule.   
`urlRewrite.hostRewrite` |  Rewrites the host before the request is sent to the origin server.   
  
Notes:

  * Rewritten URLs don't change the cache key. The cache key is based on the request URL sent by the client.
  * Rewriting occurs after route matching and signed request validation. Routes aren't _re-matched_ against another match rule.



#### Example: Remove a path prefix

For example, to rewrite a client request URL from `/vod/videos/hls/1234/abc.ts` to `/videos/hls/1234/abc.ts` (removing `/vod` from the path), you can use the `pathPrefixRewrite` feature:
    
    
    name: prod-service
    routing:
      hostRules:
      - hosts:
        - cdn.example.com
        pathMatcher: example_routes
      pathMatchers:
      - name: example_routes
        routeRules:
        - priority: 1
          origin: my-origin
          matchRules:
          - prefixMatch: "/vod/videos/"
          routeAction:
            urlRewrite:
              pathPrefixRewrite: "/videos/"

A `pathPrefixRewrite` works by replacing the entire path prefix matched in the `matchRules[].prefixMatch` with the value of `pathPrefixRewrite`.

To rewrite a hostname (for example, rewriting `cdn.example.com` to `my-bucket.s3.us-west-2.amazonaws.com`), you can configure the following:
    
    
    name: prod-service
    routing:
      hostRules:
      - hosts:
        - cdn.example.com
        pathMatcher: example_routes
      pathMatchers:
      - name: example_routes
        routeRules:
        - priority: 1
          origin: my-origin
          matchRules:
          - prefixMatch: "/videos/"
          routeAction:
            urlRewrite:
              hostRewrite: "my-bucket.s3.us-west-2.amazonaws.com"

In this case, the origin request URL would change from `cdn.example.com/videos/*` to `my-bucket.s3.us-west-2.amazonaws.com/videos/*`. You can also combine both host and path rewrites within a single route.

#### Example: Use variables to rewrite URLs

To use `pathTemplateMatch` and `pathTemplateRewrite` to rewrite parts of an incoming request URL, see the capturing variables section.

### Redirect requests

Media CDN supports three types of redirects:

  * Host redirects, which redirect only the host (domain), keeping the path and query parameters unchanged.
  * Path redirects, which replace the path in full.
  * Path prefix redirects, which only replace the matching prefix.



Redirects default to `HTTP 301 (Moved Permanently)`, but can be configured to return different redirect status codes on a per-route basis.

The following configuration is an example of a prefix-based redirect, where you redirect users visiting `https://cdn.example.com/on-demand/*` to `https://cdn.example.com/streaming/*`.
    
    
    name: prod-service
    routing:
      hostRules:
      - hosts:
        - cdn.example.com
        pathMatcher: example_routes
      pathMatchers:
      - name: example_routes
        routeRules:
        - priority: 10
          matchRules:
          - prefixMatch: "/on-demand/"
          urlRedirect:
            # The prefix matched in matchRules.prefixMatch is replaced
            # by this value
            prefixRedirect: "/streaming/"
            redirectResponseCode: TEMPORARY_REDIRECT # corresponds to a HTTP 307

This example also changes the redirect to a temporary redirect, which prevents clients (such as browsers) from caching it. This can be useful if you expect to change it in the near future.

The supported `redirectResponseCode` values are shown in the following table.

Redirect response code | HTTP status code  
---|---  
**`MOVED_PERMANENTLY_DEFAULT`** | HTTP 301 (Moved Permanently)  
**`FOUND`** | HTTP 302 (Found)  
**`SEE_OTHER`** | HTTP 303 (See Other)  
**`TEMPORARY_REDIRECT`** | HTTP 307 (Temporary Redirect)  
**`PERMANENT_REDIRECT`** | HTTP 308 (Permanent Redirect)  
  
Notes:

  * A route can either direct traffic to an origin or return a redirect to the client. You can't set both the `origin` and `urlRedirect` fields at the same time.
  * Routes that redirect to HTTPS require that at least one [SSL certificate](https://docs.cloud.google.com/media-cdn/docs/ssl-certificates) is attached to the service.



For more details, see the API specification for [`RouteRule.UrlRedirect`](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices#urlredirect).

### Redirect all requests to HTTPS

To redirect all requests to HTTPS (instead of HTTP), you can configure each of your services to redirect all client requests to HTTPS automatically. Clients connecting over HTTP are sent an HTTP `301 (Permanent Redirect)` status code with the `Location` header set to the same URL by using "https://" instead of "http://".

###  gcloud 
    
    
    gcloud edge-cache services update SERVICE_NAME \
        --require-tls
    
    
    Request issued for: [SERVICE_NAME]
    Updated service [SERVICE_NAME].
    

The command returns a description of your service, with `requireTls` now set to `true`.
    
    
      name: SERVICE_NAME
      requireTls: true

**Note:** This overrides per-route `pathMatcher[].routeRules[].routeAction.urlRedirect.httpsRedirect` settings. All traffic is redirected to HTTP/HTTPS with an HTTP `301 (Permanent Redirect)` status code.

You can also choose to set the [Strict-Transport-Security](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security) header as a response header to direct clients to always connect directly over HTTPS.

### Use third-party storage backends

Media CDN supports connecting to publicly reachable HTTP endpoints outside of Google Cloud, including AWS S3 storage buckets, Azure Blob Storage, and other storage providers. This can be useful if you have a multicloud architecture, or are yet to migrate data to Cloud Storage [using the Storage Transfer Service](https://docs.cloud.google.com/storage-transfer-service).

A minimal origin configuration that configures a [virtual-hosted bucket](https://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html) in AWS S3:
    
    
    name: MY_S3_ORIGIN
    originAddress: BUCKET-NAME.s3.REGION.amazonaws.com

If you aren't using a bucket name that matches the hostnames configured for your `EdgeCacheService` resources, you must also configure a host rewrite for routes associated with this origin (or origins). Otherwise, the Host header set by the client request is used when fetching from the origin.

For example, to map all requests with a path prefix of `/legacy/` to your external bucket, you can configure both a `hostRewrite` and a `pathPrefixRewrite` to strip this prefix from the origin request:
    
    
    routeRules:
      - description: legacy backend
        matchRules:
        - prefixMatch: "/legacy/"
        routeAction:
          urlRewrite:
            hostRewrite: BUCKET-NAME.s3.REGION.amazonaws.com
            pathPrefixRewrite: /
          cdnPolicy:
            cacheMode: CACHE_ALL_STATIC
            defaultTtl: 3600s

For more information about how the host header is set on origin requests, see the [origin request headers](https://docs.cloud.google.com/media-cdn/docs/origins#origin-request-headers) documentation.

## Cross-Origin Resource Sharing (CORS)

[Cross-Origin Resource Sharing](https://web.dev/cross-origin-resource-sharing/) (CORS) is a browser-centric approach to securely making cross-origin requests. CORS policies allow you to automatically set CORS headers, such as `Access-Control-Allow-Origins`, based on a per-route policy.

### Configure CORS

Media CDN lets you define a CORS policy on a route for an [`EdgeCacheService`](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices#resource:-edgecacheservice).

A CORS policy defines these rules with a common set of HTTP headers. You can set common CORS headers in responses, such as `Access-Control-Allow-Origin`, `Access-Control-Max-Age`, and `Access-Control-Allow-Headers`. These headers allow you to make cross-origin calls to your Media CDN services that might be hosted on a different domain (origin) from your website's frontend and might prevent cross-origin requests that you don't explicitly permit.

**Important:** `corsPolicy` takes precedence over `routeAction.responseHeadersToAdd`. If `corsPolicy` is configured, Media CDN overwrites any manually defined `Access-Control-Allow-Origin`, `Access-Control-Allow-Credentials`, and `Access-Control-Expose-Headers` in the response, even if they were added using custom response header filters.

For example, `player.example.com` and `api.example.com` are different origins (in the browser sense), and you might want to have your frontend application make requests to `api.example.com` to fetch the next playlist or refresh a listing of related content. Similarly, `player.example.com` might need to reach out to `cdn.example.com` to fetch video playlists and video segments: `cdn.example.com` needs to indicate that this is OK, and that `player.example.com` is an `allowed origin`, as well as any other rules (allowed headers, whether cookies can be included).

To take another example, if you want to allow `stream.example.com` as an origin and a `X-Client-ID` header in CORS requests, you can configure a `corsPolicy` on a route, as follows:
    
    
    corsPolicy: maxAge: 600 allowOrigins: ["stream.example.com"] allowHeaders:
    ["X-Client-ID"]

A `corsPolicy` is configured at `routing.pathMatchers[].routeRules[].routeAction.corsPolicy` within an EdgeCacheService. Each `routeRule` can define a different `corsPolicy` as needed, or none at all.

**Important:** HTTP _OPTIONS_ requests that match a route with a CORS policy configured are served directly from Media CDN and don't need to be sent to the origin. This reduces the number of requests sent to the origin and improves the off-load rate.

If you define a `corsPolicy` value and also set a custom response header by using the `responseHeadersToAdd` fields on a route with the same name, the `corsPolicy` value takes precedence.

If the origin response sets HTTP headers, and you have a `corsPolicy` value set, the `corsPolicy` values are used instead. The values are not collapsed or combined to avoid sending invalid header values to a client, or unintentionally setting a more permissive policy than intended.

The special `{origin_request_header}` is populated with the `Origin` HTTP header in the client request. This can be set as a custom response header value on a route, for the `Access-Control-Allow-Origin` header.

For more details, see the API specification for [`RouteAction.CORSPolicy`](https://docs.cloud.google.com/media-cdn/docs/reference/rest/v1/projects.locations.edgeCacheServices#corspolicy).

### CORS policy fields

The following table describes the fields that a CORS policy contains.

Field | Description | Example  
---|---|---  
allowOrigins  |  Sets the `Access-Control-Allow-Origins` response header, which specifies which origins can make cross-origin requests in a browser environment. For example, if your video content is served from `https://video.example.com` but your user-facing portal is served from `https://stream.example.com`, you would add `https://stream.example.com` as an allowed origin.  Wildcard behavior: when `allowOrigins` is set to ***** , Media CDN doesn't return a literal ***** in the `Access-Control-Allow-Origin` header. Instead, it dynamically reflects the value of the origin header from the request. |  `Access-Control-Allow-Origins: https://stream.example.com`  
maxAge  |  Sets the `Access-Control-Max-Age` response header, which specifies how long, in seconds, a browser client should cache the response to a CORS pre-flight request. Some browsers cap this to 2 hours or less, even if the maximum value (86400s) is specified. |  `Access-Control-Max-Age: 7200`  
allowMethods  |  Sets the `Access-Control-Allow-Methods` response header, which specifies which HTTP methods are allowed to access the resource. By default, Media CDN supports only the `GET`, `HEAD`, and `OPTIONS` methods. To configure support for other methods, see [Route methods](https://docs.cloud.google.com/media-cdn/docs/routing#route-methods). |  `Access-Control-Allow-Methods: GET, OPTIONS, HEAD`  
allowHeaders  |  Sets the `Access-Control-Allow-Headers` header, which determines which headers can be sent in a CORS request. This is often required by video players, which need to access some response headers for video content when requesting it cross-origin. |  `Access-Control-Allow-Headers: Content-Type, If-Modified-Since, Range, User-Agent`  
exposeHeaders  |  Sets the `Access-Control-Expose-Headers` response header, which determines which headers can be accessed by client-side JavaScript. This is often required by video players, which might need to access specific response headers for video content when requesting content cross-origin. |  `Access-Control-Expose-Headers: Date, Cache-Status, Content-Type, Content-Length`  
allowCredentials  |  Sets the `Access-Control-Allow-Credentials` response header, which allows client-side JavaScript to inspect the response for requests with credentials included. This header is omitted when set to false. |  `Access-Control-Allow-Credentials: true`  
disabled  |  Disables the `corsPolicy` without removing it. Pre-flight `OPTIONS` requests are proxied to the origin.  |  N/A   
  
### Example corsPolicy

The following configuration example shows a basic `corsPolicy` configuration:
    
    
    routeRules:
    - priority: 1
      matchRules:
      - prefixMatch: /stream/
      routeAction:
        cdnPolicy:
          defaultTtl: 3600s
        corsPolicy:
          allowOrigins:
          - "https://stream.example.com"
          - "https://stream-staging.example.com"
          maxAge: 86400s # some browsers might only honor up to 7200s or less
          allowMethods:
          - "GET"
          - "HEAD"
          - "OPTIONS"
          allowHeaders:
          - "Content-Type"
          - "If-Modified-Since"
          - "Range"
          - "User-Agent"
          exposeHeaders:
          - "Content-Type"
          - "Content-Length"
          - "Date"

## Troubleshoot routing

If some requests don't retrieve matching results or return errors, check the following:

  * A route must have a `matchRule` with exactly one of `prefixMatch`, `fullPathMatch`, or `pathTemplateMatch` defined. The API returns an error if you don't include one of those fields.
  * Ensure that the `priority` of each route is set correctly: more specific (longer) routes should be given a higher priority over shorter, broader route matches.
  * By default, only `GET`, `HEAD`, and `OPTIONS` requests are supported. To configure support for other methods, see [Route methods](https://docs.cloud.google.com/media-cdn/docs/routing#route-methods). The methods that are not enabled for a particular route are rejected with an HTTP `405 (Method Not Allowed)` error.
  * HTTP `GET` requests with a body, or any request with trailers, are rejected with an HTTP `400` error, because request bodies are not allowed in `GET` requests.
  * Query parameter and header matching are logical "AND"—the request must match all of the query parameter or header keys (and values, if specified) to match the given route.



## What's next

  * Review the documentation about [configuring caching](https://docs.cloud.google.com/media-cdn/docs/caching).
  * Understand how to [connect to different origins](https://docs.cloud.google.com/media-cdn/docs/origins).
  * [Set up TLS (SSL) certificates](https://docs.cloud.google.com/media-cdn/docs/ssl-certificates) for your service.
  * Configure [signed requests](https://docs.cloud.google.com/media-cdn/docs/signed-requests) to authenticate access to content.
  * For more details about configuring `EdgeCacheService` resources by using Terraform, see the [Terraform Registry documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/network_services_edge_cache_service).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
