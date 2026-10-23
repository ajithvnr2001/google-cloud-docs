---
url: https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt/
title: Set up traffic management for global external Application Load Balancers \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:40.746180+00:00
---

# Set up traffic management for global external Application Load Balancers  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Set up traffic management for global external Application Load Balancers Stay organized with collections  Save and categorize content based on your preferences. 

This document shows examples of using traffic management for some specific use cases using YAML configuration. Many other use cases are possible.

The document contains examples for global external Application Load Balancers. Global external Application Load Balancers use the `EXTERNAL_MANAGED` load balancing scheme and global load balancing components, such as the forwarding rule, URL map, and backend service.

For information about traffic management with a classic Application Load Balancer, see [Traffic management overview for a classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management).

For information about traffic management with regional external Application Load Balancers, see [Traffic management overview for regional external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-regional).

In addition to the advanced routing features described on this page, [supported Application Load Balancers](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs) integrate with Service Extensions to let you [insert custom logic](https://docs.cloud.google.com/service-extensions/docs/overview#integration-lb) into the load balancing data path.

## Before you begin

Make sure that you understand how traffic management works. For more information, see [Traffic management overview for global external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global).

## Configure and test traffic management

Within your chosen configuration environment, you set up traffic management by using YAML configurations. A URL map and a backend service each has its own YAML file. Depending on the chosen feature, you need to write either a URL map YAML file, a backend service YAML file, or both.

For help writing these YAML files, you can use the examples on this page and the Cloud Load Balancing API documentation.

The [global URL map API ](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps) and the [ global backend service API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices) documentation provides a full list of fields, including semantics regarding relationships, restrictions, and cardinality.

You can add configuration tests to a URL map to ensure that your URL map routes requests as intended. You can experiment with different URL map rules and run as many tests as needed to be confident that the map routes traffic to the appropriate backend service or backend bucket. For details, see [Add tests to a URL map](https://docs.cloud.google.com/load-balancing/docs/url-map#test-url-map). If you want to test new changes to a URL map without actually deploying the map, see [Validate the URL map configuration](https://docs.cloud.google.com/load-balancing/docs/url-map#validate-url-map).

### Use the YAML examples in the Google Cloud console

To use YAML examples in the Google Cloud console:

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)

  2. Click **Create load balancer**.
  3. Complete the steps of the wizard to create a global external Application Load Balancer.
  4. In the **Routing rules** configuration, select **Advanced host and path rule**.
  5. Click **Add host and path rule**. 
  6. Do one of the following:
     * In the **Path matcher** box, paste the YAML examples from this document.
     * Click the **Code guidance** link.
The **Path matcher YAML examples** page appears. You can paste examples from the **Path matcher YAML examples** page to the **Path matcher** box.
  7. Click **Done**.



## Map traffic to a single service

Send all traffic to a single service. Make sure to replace the placeholders.
    
    
        defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
        hostRules:
        - hosts:
          - '*'
          pathMatcher: matcher1
        name: URL_MAP_NAME
        pathMatchers:
        - defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
          name: matcher1
          routeRules:
          - matchRules:
            - prefixMatch: /PREFIX
            priority: PRIORITY  # 0 is highest
            routeAction:
              weightedBackendServices:
              - backendService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
                weight: 100
    

## Split traffic between two services

Split traffic between two or among multiple services. Make sure to replace the placeholders.
    
    
       defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
       hostRules:
       - hosts:
         - '*'
         pathMatcher: matcher1
       name: URL_MAP_NAME
       pathMatchers:
       - defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
         name: matcher1
         routeRules:
         - matchRules:
           - prefixMatch: /PREFIX
           priority: 2
           routeAction:
             weightedBackendServices:
             - backendService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
               weight: 95
             - backendService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_2
               weight: 5
    

## Configure a URL redirect

The following example returns a configurable 301 `MOVED_PERMANENTLY_DEFAULT` response code. The example also sets the `Location` response header with the appropriate URI, replacing the host and path as specified in the redirect action.

To create a redirect for a backend bucket, use `projects/PROJECT_ID/global/backendBuckets/BACKEND_BUCKET` for the `defaultService` field.
    
    
       defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
       name: <var>URL_MAP_NAME</var>
       hostRules:
       - hosts:
         - "HOST TO REDIRECT FROM" # Use * for all hosts
         pathMatcher: matcher1
       pathMatchers:
       - defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
         name: matcher1
         defaultUrlRedirect:
           hostRedirect: "HOST TO REDIRECT TO" # Omit to keep the requested host
           pathRedirect: "PATH TO REDIRECT TO" # Omit to keep the requested path
           redirectResponseCode: MOVED_PERMANENTLY_DEFAULT
           stripQuery: True
    

## Mirror traffic

In addition to forwarding the request to the selected backend service, you can send an identical request to the configured mirror backend service on a _fire and forget_ basis. This means that the load balancer doesn't wait for a response from the backend to which it sends the mirrored request. Request mirroring is useful for testing a new version of a backend service. You can also use it to debug production errors on a debug version of your backend service, rather than on the production version.

By default, the mirrored backend service receives _all_ requests, even if the original traffic is being split between multiple weighted backend services. You can configure the mirrored backend service to receive only a percentage of the requests by using the optional `mirrorPercent` flag to specify the percentage of requests to be mirrored expressed as a value between 0 and 100.0.

**Note:** A prefix match (`pathMatchers[].routeRules[].matchRules[].prefixMatch`) uses `*` as a literal character and not as a wildcard character. If you want to use `*` as a wildcard character, you can use [path templates for route rules](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#wildcards-regx-dynamic-route) (`pathMatchers[].routeRules[].matchRules[].pathTemplateMatch`).
    
    
       defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
       name: global-lb-map
       hostRules:
       - hosts:
         - '*'
         pathMatcher: matcher1
       pathMatchers:
       - defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
         name: matcher1
         routeRules:
           - matchRules:
               - prefixMatch: /PREFIX
             priority: PRIORITY  # 0 is highest
             routeAction:
               weightedBackendServices:
                 - backendService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
                   weight: 100
               requestMirrorPolicy:
                 backendService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_2
                 mirrorPercent: 50.0
    

If you have multiple weighted backend services and want to record which backend service was used to serve the original request, you can add a custom header that includes this information to all the requests. The following example adds a custom header called `x-weighted-picked-backend` to all client requests. For the header value, use the name of the backend service that served the original request.
    
    
       defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
       name: global-lb-map
       hostRules:
       - hosts:
         - '*'
         pathMatcher: matcher1
       pathMatchers:
       - defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
         name: matcher1
         routeRules:
           - matchRules:
               - prefixMatch: /PREFIX
             priority: PRIORITY  # 0 is highest
             routeAction:
               weightedBackendServices:
                - backendService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
                  weight: 95
                  headerAction:
                    requestHeadersToAdd:
                    - headerName: x-weighted-picked-backend
                      headerValue: BACKEND_SERVICE_1
                      replace: True
                - backendService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_2
                  weight: 5
                  headerAction:
                    requestHeadersToAdd:
                    - headerName: x-weighted-picked-backend
                      headerValue: BACKEND_SERVICE_2
                      replace: True
               requestMirrorPolicy:
                 backendService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_3
    

Note the following limitations when using traffic mirroring:

  * Traffic mirroring is supported when both backend services have managed instance groups, zonal NEGs, or hybrid NEGs backends. It is not supported for internet NEGs, serverless NEGs, and Private Service Connect backends.
  * Requests to the mirrored backend service do not generate any logs or metrics for Cloud Logging and Cloud Monitoring. 



## Rewrite the requested URL

Rewrite the hostname portion of the URL, the path portion of the URL, or both, before sending a request to the selected backend service. Make sure to replace the placeholders.
    
    
       defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
       name: global-lb-map
       hostRules:
       - hosts:
         - '*'
         pathMatcher: matcher1
       pathMatchers:
       - defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
         name: matcher1
         routeRules:
           - matchRules:
               - prefixMatch: /PREFIX
             priority: PRIORITY  # 0 is highest
             routeAction:
               weightedBackendServices:
                 - backendService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
                   weight: 100
               urlRewrite:
                 hostRewrite: "new-host-name.com" # Omit to keep the requested host
                 pathPrefixRewrite: "/new-path/" # Omit to keep the requested path
    

**Note:** The `pathPrefixRewrite` route action is best suited for use with `prefixMatch` rules where it can effectively modify the matched prefix only. We don't recommend using `fullPathMatch` rules with `pathPrefixRewrite`. 

## Retry a request

Configure the conditions under which the load balancer retries failed requests, how long the load balancer waits before retrying, and the maximum number of retries permitted.
    
    
       defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
       name: global-lb-map
       hostRules:
       - hosts:
         - '*'
         pathMatcher: matcher1
       pathMatchers:
       - defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
         name: matcher1
         routeRules:
           - matchRules:
               - prefixMatch: /PREFIX
             priority: PRIORITY  # 0 is highest
             routeAction:
               weightedBackendServices:
                 - backendService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
                   weight: 100
               retryPolicy:
                 retryConditions: 502, 504
                 numRetries: 3
                 perTryTimeout:
                   seconds: 1
                   nanos: 500000000
    

## Specify the route timeout

Specify the timeout for the selected route. Timeout is computed from the time the request is fully processed until the response is fully processed. Timeout includes all retries. Make sure to replace the placeholders.
    
    
       defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
       name: global-lb-map
       hostRules:
       - hosts:
         - '*'
         pathMatcher: matcher1
       pathMatchers:
       - defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
         name: matcher1
         routeRules:
           - matchRules:
               - prefixMatch: /PREFIX
             priority: PRIORITY  # 0 is highest
             routeAction:
               weightedBackendServices:
                 - backendService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
                   weight: 100
               timeout:
                 seconds: 30
                 nanos: 0
    

## Configure fault injection

Introduce errors when servicing requests to simulate failures, including high latency, service overload, service failures, and network partitioning. This feature is useful for testing the resiliency of a service to simulated faults.
    
    
       defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
       name: global-lb-map
       hostRules:
       - hosts:
         - '*'
         pathMatcher: matcher1
       pathMatchers:
       - defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
         name: matcher1
         routeRules:
           - matchRules:
               - prefixMatch: /PREFIX
             priority: PRIORITY  # 0 is highest
             routeAction:
               weightedBackendServices:
                 - backendService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
                   weight: 100
               faultInjectionPolicy:
                 delay:
                   fixedDelay:
                     seconds: 10
                     nanos: 0
                   percentage: 25
                 abort:
                   httpStatus: 503
                   percentage: 50
    

## Configure a Cloud CDN cache policy

Apart from a backend service or a backend bucket, you can configure [Cloud CDN cache policies](https://docs.cloud.google.com/cdn/docs/caching) at various levels of a URL map. This provides granular control over caching policies based on criteria like hostname, URL path, HTTP headers, and query parameters.

You can configure one or more cache policies anywhere a `routeAction` or a `defaultRouteAction` is supported in a URL map. This includes the following four levels of a URL map:

URL map level | API | When is the cache policy applied?  
---|---|---  
Root | `urlMap.defaultRouteAction.cachePolicy` | Applied when a request's hostname does not match any existing host rules.  
Path matchers | `urlMap.pathMatchers[].defaultRouteAction.cachePolicy` | Applied when a request's hostname matches a host rule, but none of its path rules or route rules match.  
Path rules | `urlMap.pathMatchers[].pathRules[].routeAction.cachePolicy` | Applied when a request's path matches a path rule.  
Route rules | `urlMap.pathMatchers[].routeRules[].routeAction.cachePolicy` | Applied when a request's path matches the path, header, or query parameter conditions of a route rule.  
  
Note the following points when cache policies are configured in a URL map:

  * A cache policy defined at any level of the URL map takes precedence over the backend's `cdnPolicy` for a given route.

  * The cache policy does not fall back to a cache policy defined at a higher level of the URL map. For example, if a request matches a specific `routeRule` that lacks a cache policy, the load balancer does not fall back to a cache policy defined at the higher `pathMatcher` level or root `urlMap` level. Instead, it applies the caching configuration defined in the `cdnPolicy`, which is configured on the backend service or backend bucket.

  * [Signed URLs](https://docs.cloud.google.com/cdn/docs/using-signed-urls) and [dynamic compression](https://docs.cloud.google.com/cdn/docs/dynamic-compression) can only be enabled on a backend service or a backend bucket, and cannot be defined in the URL map. When a request arrives, the load balancer applies the `cachePolicy` defined in the URL map. If that request is routed to a backend service or a backed bucket configured with signed URLs or dynamic compression, those features are automatically applied. Consequently, the request's final routing and caching behavior is determined by combining the URL map's cache policy with the backend's compression and signed URL configurations.




In the following YAML configuration of a URL map, a cache policy is configured at the root `urlMap` level, `pathMatchers` level, and `routeRules` level.

URL map level | Caching behavior  
---|---  
`routeRules` |  If a request matches `www.example.com` and the path matches the `/users/{username=*}/carts/{cartid=**}` pattern, it is routed to BACKEND_SERVICE_2. For these requests, the cache policy is set to `CACHE_ALL_STATIC`, which means that static content like images, CSS, and JavaScript is automatically cached for 1 hour (3600 seconds). It also explicitly configures [negative caching](https://docs.cloud.google.com/cdn/docs/using-negative-caching) to cache `404 Not Found` errors for 5 minutes (300 seconds).  
`pathMatchers` |  If a request matches `www.example.com` but the path does not match the `/users/{username=*}/carts/{cartid=**}` pattern, the request is routed to BACKEND_SERVICE_1. Here, the cache policy is set to `USE_ORIGIN_HEADERS`, which means that Cloud CDN relies on the origin server's `Cache-Control` headers to determine what to cache. The `cacheKeyPolicy` ensures that separate cache entries are created depending on the protocol (HTTP versus HTTPS) and the specific hostname.  
`urlMap` |  If a request arrives with a completely unmatched hostname, the request is routed to the URL map's default backend service, which is BACKEND_SERVICE_DEFAULT. The cache policy is set to `CACHE_ALL_STATIC`, which means that static content is cached for 1 hour (3600 seconds).  
      
    
    defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_DEFAULT
    # This cache policy is applied if the request hostname does not match
    # any hosts specified in the hostRules
    defaultRouteAction:
      cachePolicy:
        cacheMode: CACHE_ALL_STATIC
        defaultTtl:
          seconds: 3600
        negativeCaching: true
    hostRules:
    - hosts:
      - www.example.com
      pathMatcher: cart-matcher
    pathMatchers:
    - name: cart-matcher
      defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
      # This cache policy is applied if there is a host match but no specific route rule match.
      defaultRouteAction:
        cachePolicy:
          cacheMode: USE_ORIGIN_HEADERS
          cacheKeyPolicy:
            includeProtocol: true
            includeHost: true
      routeRules:
      - description: CartService
        matchRules:
          - pathTemplateMatch: '/users/{username=*}/carts/{cartid=**}'
        service: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_2
        priority: PRIORITY  # 0 is highest
        # This cache policy is applied if there is a route rule match.
        routeAction:
          cachePolicy:
            cacheMode: CACHE_ALL_STATIC
            defaultTtl:
              seconds: 3600
            negativeCaching: true
            negativeCachingPolicy:
              - code: 404
                ttl:
                 seconds: 300
    

To configure and manage cache policies at various levels of the URL map, see [Configure a Cloud CDN cache policy](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute#cdn-cache-policy).

## Configure CORS

Configure cross-origin resource sharing (CORS) policies to control how your load balancer handles cross-origin requests.

### CORS policy applied at the path matcher level

In this configuration, the CORS policy is defined in the `defaultRouteAction` of the path matcher (`pathMatchers[].defaultRouteAction.corsPolicy`). This means the policy is applied to all requests that are routed through the default path matcher, regardless of the specific path or route.

This approach is suitable when you want a single, consistent CORS policy for all routes managed by a path matcher.
    
    
    defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
    name: global-lb-map
    hostRules:
    - hosts:
      - '*'
      pathMatcher: path-matcher-1
    pathMatchers:
    - defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
      name: path-matcher-1
    - defaultRouteAction:
        corsPolicy:
          allowCredentials: true
          allowOrigins: [ "http://example.com" ]
          allowMethods: [ "GET", "POST" ]
          allowHeaders: [ "Authorization", "Content-Type" ]
    

#### How it works

  * The load balancer enforces the CORS policy for all requests handled by the path matcher.
  * Only requests from host `example.com` using GET or POST methods, and with the allowed headers (Authorization, Content-Type), are permitted.
  * Credentials (such as cookies or authorization headers) are allowed in cross-origin requests.
  * The backend service receives only requests that comply with this CORS policy.



### CORS policy applied at the route rule level

In this configuration, the CORS policy is defined within a `routeAction` for a specific route rule (`pathMatchers[].routeRules[].routeAction.corsPolicy`). This lets you apply different CORS policies to different routes or path prefixes.

This approach is suitable when you need fine-grained control, such as applying different CORS policies to different API endpoints or paths.
    
    
       defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
       name: global-lb-map
       hostRules:
       - hosts:
         - '*'
         pathMatcher: matcher1
       pathMatchers:
       - defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
         name: matcher1
         routeRules:
           - matchRules:
               - prefixMatch: /PREFIX
             priority: PRIORITY  # 0 is highest
             routeAction:
               weightedBackendServices:
                 - backendService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
                   weight: 100
               corsPolicy:
                   allowOrigins: [ "http://example.com" ]
                   allowMethods: [ "GET", "POST" ]
                   allowHeaders: [ "Authorization", "Content-Type" ]
                   maxAge: 1200
                   allowCredentials: true
    

#### How it works

  * The CORS policy is enforced only for requests that match the specified path prefix (for example, `/PREFIX`).
  * Only requests from the host `example.com` using GET or POST methods, and with the allowed headers, are permitted for this route.
  * The `maxAge` field specifies how long the results of a preflight request can be cached by the browser (in seconds).
  * Credentials are allowed in cross-origin requests.
  * Other routes can have different CORS policies or none at all.



You can also define a CORS policy at the following levels of a URL map:

  * `defaultRouteAction.corsPolicy`
  * `pathMatchers[].pathRules[].routeAction.corsPolicy`



## Add and remove request and response headers

**Note:** We announced a change in behavior for custom headers configured on URL maps and backend services. This change does not affect projects that had existing traffic that used custom headers before November 14, 2022. For details, see the release note for [November 14, 2022](https://docs.cloud.google.com/load-balancing/docs/release-notes#November_14_2022). 

Add and remove request headers before sending a request to the backend service. Also add and remove response headers after receiving a response from the backend service.

There are restrictions on valid values for `headerName` and `headerValue`. For details, see [How custom headers work](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers-global#how-custom-headers-work).
    
    
       defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
       name: global-lb-map
       hostRules:
       - hosts:
         - '*'
         pathMatcher: matcher1
       pathMatchers:
       - defaultService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
         name: matcher1
         routeRules:
           - matchRules:
               - prefixMatch: /PREFIX
             priority: PRIORITY  # 0 is highest
             routeAction:
               weightedBackendServices:
                 - backendService: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
                   headerAction:
                     requestHeadersToAdd:
                     - headerName: header-1-name
                       headerValue: header-1-value
                       replace: True
                     requestHeadersToRemove:
                     - header-2-name
                     - header-3-name
                     responseHeadersToAdd:
                     - headerName: header-4-name
                       headerValue: header-4-value
                       replace: True
                    responseHeadersToRemove:
                    - header-5-name
                    - header-6-name
    
    

## Configure outlier detection

Specify the criteria for eviction of unhealthy backend VMs or endpoints in NEGs, along with criteria defining when a backend or endpoint is considered healthy enough to receive traffic again. Make sure to replace the placeholders.
    
    
        loadBalancingScheme: EXTERNAL_MANAGED
        localityLbPolicy: RANDOM
        name: projects/PROJECT_ID/global/backendServices/BACKEND_SERVICE_1
        outlierDetection:
          baseEjectionTime:
            nanos: 0
            seconds: 30
          consecutiveErrors: 5
          consecutiveGatewayFailure: 3
          enforcingConsecutiveErrors: 2
          enforcingConsecutiveGatewayFailure: 100
          enforcingSuccessRate: 100
          interval:
            nanos: 0
            seconds: 1
          maxEjectionPercent: 50
          successRateMinimumHosts: 5
          successRateRequestVolume: 100
          successRateStdevFactor: 1900
    

## Set up traffic splitting: detailed steps

**Note:** Don't configure session affinity if you're using weighted traffic splitting. If you do, the weighted traffic splitting configuration takes precedence.

This example demonstrates the following steps:

  1. Create distinct templates for different services.

  2. Create instance groups for those templates.

  3. Create routing rules that set up 95% / 5% traffic splitting.

  4. Send curl commands showing that the traffic split percentages roughly match the configuration.




These instructions assume the following:

  * A target proxy and forwarding rule have been created, along with a URL map named `global-lb-map`.

  * The URL map sends all traffic to one backend service, called `red-service`, which is the default backend service.

  * You set up an alternate path that sends 5% of the traffic to `blue-service` and 95% of traffic to `green-service`.

  * A path matcher is used.

  * You are using [Cloud Shell](https://docs.cloud.google.com/shell/docs) or another environment with bash installed.




### Define the services

The following bash function creates a backend service, including the instance template and the managed instance group.

These instructions assume that an HTTP health check (`global-lb-basic-check`) has been created. For instructions, see one of the following pages:

  * [Setting up a global external Application Load Balancer with a Compute Engine backend](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-compute)
  * [Setting up a global external Application Load Balancer with a backend bucket](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-buckets)
  * [Setting up a global external Application Load Balancer with hybrid connectivity](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-ext-global-https-hybrid)
  * [Setting up a global external Application Load Balancer with Cloud Run, App Engine, or Cloud Run functions](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-serverless)


    
    
    function make_service() {
      local name="$1"
      local region="$2"
      local zone="$3"
      local network="$4"
      local subnet="$5"
      local subdir="$6"
    
      www_dir="/var/www/html/$subdir"
    
      (set -x; \
      gcloud compute instance-templates create "${name}-template" \
        --region="$region" \
        --network="$network" \
        --subnet="$subnet" \
        --tags=allow-ssh,load-balanced-backend \
        --image-family=debian-12 \
        --image-project=debian-cloud \
        --metadata=startup-script="#! /bin/bash
      apt-get update
      apt-get install apache2 -y
      a2ensite default-ssl
      a2enmod ssl
      sudo mkdir -p $www_dir
      /bin/hostname | sudo tee ${www_dir}index.html
      systemctl restart apache2"; \
      gcloud compute instance-groups managed create \
        "${name}-instance-group" \
        --zone="$zone" \
        --size=2 \
        --template="${name}-template"; \
      gcloud compute backend-services create "${name}-service" \
        --load-balancing-scheme=EXTERNAL_MANAGED \
        --protocol=HTTP \
        --health-checks=global-lb-basic-check \
        --global \
      gcloud compute backend-services add-backend "${name}-service" \
        --balancing-mode='UTILIZATION' \
        --instance-group="${name}-instance-group" \
        --instance-group-zone="$zone" \
        --global)
    }
    

### Create the services

Call the function to make three services, `red`, `green`, and `blue`. The `red` service acts as the default service for requests to `/`. The `green` and `blue` services are both set up on `/prefix` to handle 95% and 5% of the traffic, respectively.
    
    
    make_service red us-west1 us-west1-a lb-network backend-subnet ""
    make_service green us-west1 us-west1-a lb-network backend-subnet /prefix
    make_service blue us-west1 us-west1-a lb-network backend-subnet /prefix
    

### Create the URL map

###  Console 

  1. Go to the **Load balancing** page in the Google Cloud console.   
[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/add)
  2. Click the **global-lb-map** link.
  3. Click **Edit** edit .



### Configure the new routing rules

  1. Under **Routing rules** , select **Advanced host and path rule**.
  2. Under **New hosts and path matcher** , to create the default action, set the **Service** to `red-service`.
  3. Click **Done**.
  4. Click **Add hosts and path rule**.
  5. In the **Hosts** field, enter the IP address of your load balancer's forwarding rule.
  6. In the **Path matcher** box, paste the following YAML content:
         
         defaultService: projects/PROJECT_ID/global/backendServices/red-service
         name: matcher1
         routeRules:
         - priority: 2
           matchRules:
             - prefixMatch: /PREFIX
           routeAction:
             weightedBackendServices:
               - backendService: projects/PROJECT_ID/global/backendServices/green-service
                 weight: 95
               - backendService: projects/PROJECT_ID/global/backendServices/blue-service
                 weight: 5
         

  7. Click **Done**.

  8. Click **Update**.




###  gcloud 

  1. Export the existing URL map using the [`gcloud compute url-maps export`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/export) command:
         
         gcloud compute url-maps export global-lb-map \
           --destination=global-lb-map-config.yaml \
           --global
         

  2. Update the URL map file `global-lb-map-config.yaml` by adding this to the end of the file:
         
         hostRules:
         - hosts:
           - '*'
           pathMatcher: matcher1
         pathMatchers:
         - defaultService: projects/PROJECT_ID/global/backendServices/red-service
           name: matcher1
           routeRules:
           - priority: 2
             matchRules:
               - prefixMatch: /PREFIX
             routeAction:
               weightedBackendServices:
                 - backendService: projects/PROJECT_ID/global/backendServices/green-service
                   weight: 95
                 - backendService: projects/PROJECT_ID/global/backendServices/blue-service
                   weight: 5
         

  3. Update the URL map using the [`gcloud compute url-maps import`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/import) command:
         
         gcloud compute url-maps import global-lb-map \
            --global \
            --source=global-lb-map-config.yaml
         




### Test the configuration

To test the configuration, first ensure that requests to the load balancer's IP address set up earlier are handled by the default `red` configuration.

Then check to make sure that requests sent to `FORWARDING_RULE_IP_ADDRESS/prefix` are split as expected.

## Set up session affinity based on `HTTP_COOKIE`

Traffic control lets you configure session affinity based on a provided cookie. To configure HTTP_COOKIE based session affinity for a backend service named `red-service`, follow these directions.

  1. Use the [`gcloud compute backend_services export`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/export) command to get the backend service configuration.
         
         gcloud compute backend-services export red-service \
             --destination=red-service-config.yaml \
             --global
         

  2. Update the `red-service-config.yaml` file as follows:
         
         sessionAffinity: 'HTTP_COOKIE'
         localityLbPolicy: 'RING_HASH'
         consistentHash:
          httpCookie:
           name: 'http_cookie'
           path: '/cookie_path'
           ttl:
             seconds: 100
             nanos: 0
          minimumRingSize: 10000
         

  3. In the `red-service-config.yaml` file, delete the following line:
         
         sessionAffinity: NONE
         

  4. Update the backend service configuration file:
         
         gcloud compute backend-services import red-service \
             --source=red-service-config.yaml \
             --global
         




## Troubleshooting

Use this information for troubleshooting when traffic isn't being routed according to the route rules and traffic policies that you configured.

For information about logging and monitoring, see [External HTTP(S) logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring).

Symptoms:

  * Increased traffic to services in rules above the rule in question.
  * An unexpected increase in 4xx and 5xx HTTP responses for a given route rule.



Solution: Check the order of your route rules. Route rules are interpreted in the order in which they are specified.

Route rules within a URL map are interpreted in the order in which they are specified. This is different from the way that path rules are interpreted by longest prefix match. For a path rule, the global external Application Load Balancer only selects a single path rule; however, when you use route rules, more than one might apply.

When you define route rules, check to be sure that rules at the top of the list don't inadvertently route traffic that would otherwise have been routed by a subsequent route rule. The service that receives misdirected traffic would likely reject requests, and the service in your route rules would receive reduced traffic or no traffic at all.

## What's next

  * [Clean up the load balancer setup](https://docs.cloud.google.com/load-balancing/docs/cleaning-up-lb-setup).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
