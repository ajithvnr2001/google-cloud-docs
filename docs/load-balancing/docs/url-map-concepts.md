---
url: https://docs.cloud.google.com/load-balancing/docs/url-map-concepts/
title: URL maps overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:49:21.630481+00:00
---

# URL maps overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/url-map-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  URL maps overview Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Application Load Balancers and Cloud Service Mesh use a Google Cloud configuration resource called a _URL map_ to route HTTP(S) requests to backend services or backend buckets.

For example, with an external Application Load Balancer, you can use a single URL map to route requests to different destinations based on the rules configured in the URL map:

  * Requests for `https://example.com/video` go to one backend service.
  * Requests for `https://example.com/audio` go to a different backend service.


  * Requests for `https://example.com/images` go to a Cloud Storage backend bucket.


  * Requests for any other host and path combination go to a default backend service.



URL maps are used with the following Google Cloud products:

  * [External Application Load Balancer (global, regional, and classic modes)](https://docs.cloud.google.com/load-balancing/docs/https)
  * [Internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal) (cross-region and regional modes)
  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/traffic-director-concepts), when Cloud Service Mesh is deployed with the load balancing APIs



There are two types of URL map resources available: global and regional.

  * Global [`urlMaps`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps) are used by global external Application Load Balancers, classic Application Load Balancers, cross-region internal Application Load Balancers, and Cloud Service Mesh.

  * [`regionUrlMaps`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionUrlMaps) are used by regional external Application Load Balancers, regional internal Application Load Balancers, and Cloud Service Mesh.




The type of resource that you use depends on the product's load balancing scheme.

Product | Load-balancing scheme | URL map resource type | Supported destinations  
---|---|---|---  
Global external Application Load Balancer | `EXTERNAL_MANAGED` | Global | Backend services, backend buckets  
Classic Application Load Balancer | `EXTERNAL` | Global | Backend services, backend buckets  
Regional external Application Load Balancer | `EXTERNAL_MANAGED` | Regional | Backend services, backend buckets  
Cross-region internal Application Load Balancer | `INTERNAL_MANAGED` | Global | Backend services, backend buckets  
Regional internal Application Load Balancer | `INTERNAL_MANAGED` | Regional | Backend services, backend buckets  
Cloud Service Mesh | `INTERNAL_SELF_MANAGED` | Global | Backend services  
Cloud Service Mesh | `INTERNAL_SELF_MANAGED` | Regional | Backend services  
  
Not all URL map features are available for all products. URL maps used with global external Application Load Balancers, regional external Application Load Balancers, internal Application Load Balancers and Cloud Service Mesh also support several advanced traffic management features. For more information about these differences, see [Load balancer feature comparison: Routing and traffic management](https://docs.cloud.google.com/load-balancing/docs/features#routing-traffic-management). In addition, regional URL maps can be a resource that's designated as a service in [App Hub applications](https://docs.cloud.google.com/app-hub/docs/overview).

## How URL maps work

When a request arrives at the load balancer, the load balancer routes the request to a particular backend service or a backend bucket based on the rules defined in the URL map.

A backend service represents a collection of backends, which are instances of an application or microservice. A backend bucket is a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets), which is commonly used to host static content, such as images.

For Cloud Service Mesh, possible destinations are the following:

  * Default [backend service](https://docs.cloud.google.com/compute/docs/load-balancing/http/backend-service)
  * Non-default backend service



Additionally, Application Load Balancers support the following:

  * Default [backend bucket](https://docs.cloud.google.com/load-balancing/docs/backend-bucket)
  * Non-default backend bucket



For example, assume that you have the following setup:

  * One IP address: 
    * All requests to your organization go to the same IP address and the same load balancer.
    * Traffic is directed to different backend services based on the request URL.
  * Two domains: 
    * `example.net` hosts training videos.
    * `example.org` hosts your organization website.
  * Four sets of servers: 
    * One hosts your organization website (backend service: `org-site`).
    * One hosts the overall training video website (backend service: `video-site`).
    * One hosts high definition (HD) training videos (backend service: `video-hd`).
    * One hosts standard definition (SD) training videos (backend service: `video-sd`).



You want the following to happen:

  * Requests to `example.org` (or any domain other than `example.net`) to go to the `org-site` backend service.
  * Requests to `example.net` that don't match more specific paths to go to the `video-site` backend service.
  * Requests to `example.net/video/hd/*` to go to the `video-hd` backend service.
  * Requests to `example.net/video/sd/*` to go to the `video-sd` backend service.



A `--path-rule` for `/video/*` matches URIs such as `/video/test1` and `/video/test2`. However, this path rule doesn't match the path `/video`.

If the load balancer receives a request with `/../` in the URL, the load balancer transforms the URL by removing the path segment before the `..`, and responds with the transformed URL. For example, when a request is sent for `http://example.net/video/../abc`, the load balancer responds with a 302 redirect to `http://example.net/abc`. Most clients then react by issuing a request to the URL returned by the load balancer (in this case, `http://example.net/abc`). This 302 redirection isn't logged in Cloud Logging.

The URL map lets you set up this type of host and path-based routing.

[ ![Example backend service setup.](https://docs.cloud.google.com/static/load-balancing/images/url-map-model.svg)](https://docs.cloud.google.com/static/load-balancing/images/url-map-model.svg) Example backend service setup (click to enlarge).

## Load balancer naming

For Application Load Balancers, the name of the load balancer is always the same as the name of the URL map. The behavior for each Google Cloud interface is as follows:

  * **Google Cloud console**. If you create an Application Load Balancer by using the Google Cloud console, the URL map is automatically assigned the same name that you entered for the load balancer name.
  * **Google Cloud CLI or API**. If you create an Application Load Balancer by using the gcloud CLI or the API, you enter a name of your choice while creating the URL map. This URL map name is then reflected in the Google Cloud console as the name of the load balancer.



To learn about how naming works for Proxy Network Load Balancers and Passthrough Network Load Balancers, see [Backend services overview: Load balancer naming](https://docs.cloud.google.com/load-balancing/docs/backend-service#naming).

## URL map components

A URL map is a [set of Google Cloud configuration resources](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps/insert) that direct requests for URLs to backend services or backend buckets. The URL map does so by using the _hostname_ and _path_ portions for each URL it processes:

  * A **hostname** is the domain name portion of a URL; for example, the hostname portion of the URL `http://example.net/video/hd` is `example.net`.
  * A **path** is the portion of a URL following the hostname and optional port number; for example, the path portion of the URL `http://example.net/video/hd` is `/video/hd`.

[ ![Load balancer configuration with basic URL map.](https://docs.cloud.google.com/static/load-balancing/images/url-map-simple-1.svg)](https://docs.cloud.google.com/static/load-balancing/images/url-map-simple-1.svg) Load balancer configuration with basic URL map (click to enlarge).

This diagram shows the structure of the load balancing configuration objects in relation to each other.

**Note:** The diagram isn't intended to show the processing flow for requests.

You control which backend services or backend buckets receive incoming requests by using the following URL map configuration parameters:

  * **Default backend service** or **default backend bucket.** When you create a URL map, you must specify either a default backend service or a default backend bucket, but not both. This default represents the backend service or backend bucket to which Google Cloud directs requests for URLs with any hostname, unless there is an applicable _host rule_.

**Note:** Backend buckets are not supported with Cloud Service Mesh.
  * **Host rule (`hostRules`).** A host rule directs requests sent to one or more associated hostnames to a single _path matcher_ (`pathMatchers`). The hostname portion of a URL is either exactly matched or matched using regular expressions against the set of the host rule's configured hostnames. In a URL map host and path rule, if you omit the host, the rule matches any requested host. To direct requests for `http://example.net/video/hd` to a path matcher, you need a single host rule that at least includes the hostname `example.net`. That same host rule could also handle requests for other hostnames, but it would direct them to the same path matcher.

If you need to direct requests to different path matchers, you must use different host rules. Two host rules in a URL map can't include the same hostname.

It is possible to match all hostnames by specifying the wildcard character `*` in the host rule. For example, for the URLs `http://example.org`, `http://example.net/video/hd`, and `http://example.com/audio`, all three hostnames `example.org`, `example.net`, and `example.com` can be matched by specifying `*` in the host rule. It is also possible to match a partial hostname by specifying the wildcard character `*`. For example, a host rule `*.example.net` is matched against both hostnames `news.example.net` and `finance.example.net`.

**Port number.** Classic Application Load Balancers handle port numbers differently than other Application Load Balancers. In the case of the classic Application Load Balancer, only the hostname in the URL is considered when matching a host rule. For example, `example.net` requests for port 8080 and port 80 match the host rule `example.net`. For all other Application Load Balancers, you can use the **Host rule** parameter to specify a port number. For example, to direct `example.net` requests for port 8080, set the host rule to `example.net:8080`.

**Note:** The load balancer doesn't validate the value of the hostname in the URL. Clients can set arbitrary values for the hostname, for example by setting the `Host` header. You shouldn't use the hostname field to implement access control for your application.
  * **Path matcher (`pathMatchers`).** A path matcher is the configuration parameter referenced by a host rule. It defines the relationship between the path portion of a URL and the backend service or backend bucket that should serve the request. A path matcher consists of two elements:

    * **Path matcher default backend service** or **path matcher default backend bucket.** For each path matcher, you must at least specify a default backend service or default backend bucket, but not both. This default represents the backend service or backend bucket to which Google Cloud directs requests for URLs whose hostnames match a host rule associated with the path matcher, and whose URL paths don't match any path rule in the path matcher.

    * **Path rules.** For each path matcher, you can specify one or more path rules, which are key-value pairs mapping a URL path to a single backend service or backend bucket.

Flexible pattern matching operators let you match multiple parts of a URL path, including partial URLs and suffixes (file extensions), by using wildcard syntax. These operators can be helpful when you need to route traffic and execute rewrites based on complex URL paths. You can also associate one or more path components with named variables and then refer to those variables when rewriting the URL. With named variables, you can reorder and remove URL components before the request is sent to your origin. For details, see Wildcards, regular expressions, and dynamic URLs in path rules.

If you need more advanced routing capabilities, for example, if you want to direct traffic for a unique URL to multiple services, you can use route rules instead of path rules.

    * **Route rules.** Route rules can be used as an alternative to path rules when you need advanced traffic routing capabilities such as routing traffic based on the URL path, HTTP headers, and query parameters.

You can configure route rules with flexible pattern matching operators and named variables. These operators can be helpful when you need to route traffic and execute rewrites based on complex URL paths. For details, see Wildcards and pattern matching operators in path templates for route rules.

You can also configure route rules to be matched against regular expressions that match the path, query parameters, or headers in the incoming request. For details, see Regular expressions in route rules.

To learn more about the configuration options for route rules, see [Advanced host, path, and route rule](https://docs.cloud.google.com/load-balancing/docs/l7-internal/traffic-management#advanced_host_path_and_route_rule).




### Hostname and host rule relationship

  * A hostname can only reference a single host rule.

  * A single host rule can process multiple hostnames.




### Host rule and path matcher relationship

  * Multiple host rules can reference a single path matcher.

  * A host rule can only reference a single path matcher.




### URL and backend relationship

Each unique URL is directed to only one backend service or backend bucket. Consequently:

  * Google Cloud uses the hostname portion of a URL to select a single host rule and its referenced path matcher.

  * When you use path rules in a path matcher, you cannot create more than one path rule for the same path. For example, requests for `/videos/hd` cannot be directed to more than one backend service or backend bucket. Backend services can have backend instance groups or backend network endpoint groups (NEGs) in different zones and regions, and you can create backend buckets that use Multi-Regional Storage classes.

To direct traffic for a unique URL to multiple services, you can use route rules instead of path rules. If you configure the path matcher with route rules for header or parameter matches, a unique URL can be directed to more than one backend service or bucket, based on the contents of headers or query parameters on the URL.

Similarly for regional external Application Load Balancers and Cloud Service Mesh, weighted backend services on route actions can direct the same URL to multiple backend services or buckets, depending on the weights set on the weighted backend service.




### URL maps and protocols

You can use the same URL map, host rules, and path matchers to process both HTTP and HTTPS requests submitted by clients, as long as both a target HTTP proxy and a target HTTPS proxy reference the URL map.

### Simplest URL map

The simplest URL map only has a default backend service or a default backend bucket. It contains no host rules and no path matchers. Either the default backend service or the default backend bucket (whichever one you defined) handles all requested URLs.

If you define a default backend service, Google Cloud directs requests to its backend instance groups or backend NEGs according to the backend service's configuration.

[ ![URL map with no rules except default.](https://docs.cloud.google.com/static/load-balancing/images/url-map-no-rules-1.svg)](https://docs.cloud.google.com/static/load-balancing/images/url-map-no-rules-1.svg) URL map with no rules except default (click to enlarge).

## Order of operations

For a given hostname and path in a requested URL, Google Cloud uses the following procedure to direct the request to the correct backend service or backend bucket, as configured in your URL map:

  * If the URL map does _not_ contain a host rule for the URL's hostname, Google Cloud directs requests to the URL map's default backend service or default backend bucket, depending on which one you defined.

  * If the URL map contains a host rule that includes the URL's hostname, the path matcher referenced by that host rule is consulted:

    * If the path matcher contains a path rule that _exactly matches_ the URL's path, Google Cloud directs requests to the backend service or backend bucket for that path rule.

    * If the path matcher does _not_ contain a path rule that exactly matches the URL's path, but does contain a path rule ending in `/*` whose prefix matches the _longest section_ of the URL's path, then Google Cloud directs requests to the backend service or backend bucket for that path rule. For example, for the URL map containing two path matcher rules `/video/hd/movie1` and `/video/hd/*`, if the URL contains the exact path `/video/hd/movie1`, it is matched against that path rule.

    * If neither of the previous conditions is true, Google Cloud directs requests to the path matcher's default backend service or default backend bucket, depending on which one you defined.




## URL map configuration constraints

The following sections describe certain configuration constraints for URL map components.

### Regular expressions matchers in host and route rules

**Host rules** allow you to match the hostname portion of a URL against the set of the host rule's configured hostnames. You can choose to use either a specific hostname or a wildcard `*` in the `hostRules[].hosts[]` field to be matched against the hostname in the incoming request.

**Route rules** allow you to define match rules that can match a regular expression either in the path or in the query string or in a header in the incoming request. Route rules support the use of regular expressions for the following URL map fields:

  * `pathMatchers[].routeRules[].matchRules[].regexMatch`: A regular expression that is used to match the path of the incoming request.
  * `pathMatchers[].routeRules[].matchRules[].headerMatches[].regexMatch`: A regular expression that contains a predicate that matches a header of the incoming request.
  * `pathMatchers[].routeRules[].matchRules[].queryParameterMatches[].regexMatch`: A regular expression that contains a predicate that matches a query parameter of the incoming request.



A request is considered to have matched a routeRule when any of the matchRules are satisfied. However predicates within a given matchRule have `AND` semantics. That is, all predicates within a matchRule must match for the request to match the rule.

Additional usage notes:

  * Regular expressions are supported only for the following products:

    * Regional internal Application Load Balancers
    * Cross-region internal Application Load Balancers
    * Regional external Application Load Balancers
    * Global external Application Load Balancers

Classic Application Load Balancers don't support regular expressions.

  * You must use [RE2 syntax](https://github.com/google/re2/wiki/Syntax) to construct your regular expressions. For the complete list of limitations and operators permitted in URL maps, see [RE2 specifications for URL maps](https://docs.cloud.google.com/load-balancing/docs/re2-support).

  * Regular expression matching is expensive in terms of memory consumption and request processing latencies. If you choose to use regular expression matching, you must factor in the performance degradation when you plan your deployment. For example, if you have a URL map with a single regular expression, you can expect the load balancer latency to increase by 100 microseconds per request. If your URL map has 5 regular expressions to be matched, you can expect latency to increase by 200 microseconds per request.




#### Example #1: Use a regular expression to match path

The path is considered a match if it matches the regular expression specified by `regexMatch` after removing any query parameters and anchors supplied with the original URL. For example, in the following sample URL maps, the route rule regular expression, `/videos/hd.*`, would apply to a URL with the path `/videos/hd-abcd?key=245`.
    
    
    defaultService: projects/example-project/global/backendServices/org-site
    name: rule-match-url-map
    hostRules:
    - hosts:
      - '*' # Match any host
      pathMatcher: video-matcher
    - hosts:
      - example.net
      pathMatcher: video-matcher
    pathMatchers:
    - name: video-matcher
      # Optional: default service for this path matcher if no routeRules match
      defaultService: projects/example-project/global/backendServices/video-site
      routeRules:
      - priority: 100000
        matchRules:
        - regexMatch: /videos/hd.*
        routeAction:
          weightedBackendServices:
          - backendService: projects/example-project/global/backendServices/video-hd
            weight: 100
    

Here is an explanation for each field of the sample URL map:

  * `defaultService`: Specifies the default backend service to use if no other rules in the URL map match the incoming request.
  * `name`: Assigns the name _rule-match-url-map_ to this URL map configuration.
  * `hostRules`: Defines a list of rules for matching the host header of incoming requests. The first rule matches any host (`*`) and directs traffic to the `pathMatcher` named _video-matcher_. The second rule specifically matches the host `example.net` and also directs traffic to the path matcher named _video-matcher_.
  * `pathMatchers`: Defines a list of named path matchers.
  * `name`: Defines a path matcher named _video-matcher_.
  * `defaultService`: Sets the default service for this path. matcher. This service is used if a request matches the host rule(s) pointing to _video-matcher_ but doesn't match any of the `routeRules` within it.
  * `routeRules`: Contains a list of rules to match the URL path.
  * `priority`: Sets the priority of this rule to 100000. Rules are evaluated in order from lowest to highest priority number.
  * `matchRules`: Contains the conditions for this route rule to be matched.
  * `regexMatch`: This condition checks if the URL path matches the regular expression `/videos/hd.*` (for example, "/videos/hd" and "/videos/hd-caching").
  * `routeAction`: Specifies the action to take if all conditions in `matchRules` are met.
  * `weightedBackendServices`: Distributes traffic among a list of backend services based on weights.
  * `backendService`: Specifies the backend service to route traffic to.
  * `weight`: Assigns a weight of 100 to this backend service. Since it's the only service in the list, it will receive 100% of the traffic that matches this routeRule.



The following URL map shows a similar example without using a `routeAction`.
    
    
    defaultService: projects/example-project/global/backendServices/video-site
    name: path-matcher-videos
    routeRules:
      matchRules:
      - regexMatch: /videos/hd.*
      priority: 100000
      service: projects/example-project/global/backendServices/video-hd
    

#### Example #2: Use a regular expression to match headers

The header is considered a match if the value of the header matches the regular expression specified by `regexMatch`. For example, in the following sample URL map, the header name regular expression, `.*Android.*-hd`, would apply to a request with the header `User-Agent:123Androidabc-hd`.
    
    
    defaultService: projects/example-project/regions/us-central1/backendServices/default-backend-service
    name: header-match-url-map
    hostRules:
    - hosts:
      - '*'  # Match any host
      pathMatcher: header-matcher
    pathMatchers:
    - name: header-matcher
      # Optional: default service for this path matcher if no routeRules match
      defaultService: projects/example-project/regions/us-central1/backendServices/default-backend-service
      routeRules:
      - priority: 1
        matchRules:
        - headerMatches:
          - headerName: User-Agent
            regexMatch: .*Android.*-hd
        # This prefix match applies to the path part of the URL
        - prefixMatch: /video/
        # service: can be used instead of routeAction if no other actions are needed
        service: projects/example-project/regions/us-central1/backendServices/video-backend-service
        # Alternatively, use routeAction to specify the service:
        # routeAction:
        #   weightedBackendServices:
        #   - backendService: projects/example-project/regions/us-central1/backendServices/video-backend-service
        #     weight: 100
    

Here is an explanation for each field of the sample URL map:

  * `defaultService`: Specifies the default backend service to use if no other rules in the URL map match the incoming request.
  * `name`: Assigns the name _header-match-url-map_ to this URL map configuration.
  * `hostRules`: Defines a list of rules for matching the host header of incoming requests. The rule matches any host ('*') and directs traffic to the `pathMatcher` named header-matcher.
  * `pathMatchers`: Defines a list of named path matchers.
  * `name`: Defines a path matcher named _header-matcher_.
  * `defaultService`: Sets the default service for this path matcher. This service is used if a request matches the host rule but doesn't match any of the `routeRules` within this path matcher.
  * `routeRules`: Contains a list of rules to match incoming requests based on headers and paths.
  * `priority`: Sets the priority of this rule to 1. Rules are evaluated in order from lowest to highest priority number.
  * `matchRules`: Contains a list of conditions that must all be true for the rule to match.
  * `headerMatches`: Specifies conditions based on request headers.
  * `headerName`: Looks for the User-Agent header.
  * `regexMatch`: Checks if the User-Agent header value matches the regular expression `.*Android.*-hd`. This would match User-Agents indicating an Android device, with a string containing "-hd".
  * `prefixMatch`: Set to `/video/`, this condition checks if the URL path starts with "/video/".
  * `service`: If all `matchRules` conditions are met, traffic is directed to this backend service.
  * The commented-out `routeAction` section shows an alternative way to specify the backend service, which would be necessary if you needed to configure other route actions like URL rewrites, header transformations, or weighted backend services.



#### Example #3: Use a regular expression to match query parameters

The query parameter is considered a match if the value of the path with the query parameters matches the regular expression specified by `regexMatch`. For example, in the following sample URL map, the query parameter regular expression, `/im.*/.*.html`, would apply to a URL with query parameters such as `/images/random_page.html?param1=param_value_123abc-hd`.
    
    
    defaultService: projects/example-project/regions/us-central1/backendServices/sample-bs
    name: query-match-url-map
    hostRules:
    - hosts:
      - '*'  # Match any host
      pathMatcher: query-matcher
    pathMatchers:
    - name: query-matcher
      # Optional: default service for this path matcher if no routeRules match
      defaultService: projects/example-project/regions/us-central1/backendServices/sample-bs
      routeRules:
      - priority: 1
        matchRules:
        - queryParameterMatches:
          - name: param1   #parameter name in query
            regexMatch: param_value_.*-hd
        # This regexMatch applies to the path part of the URL
        - regexMatch: /im.*/.*.html
        # Directs traffic to this service if all conditions in matchRules are met
        service: projects/example-project/regions/us-central1/backendServices/sample-images-bs
    

Here is an explanation for each field of the sample URL map:

  * `hostRules`: Adds a rule to match all hosts (`*`) and directs traffic to the `pathMatcher` named _query-matcher_.
  * `pathMatchers`: Defines a path matcher named _query-matcher_.
  * `routeRules`: Places the provided `routeRules` block within _query-matcher_.
  * `priority`: Sets the priority of this rule to 1. Rules are evaluated in order from lowest to highest priority number.
  * `matchRules`: Contains the conditions for the `routeRules`.
  * `queryParameterMatches`: Checks if the query parameter named "param1" matches the regular expression `param_value_.*-hd`.
  * `regexMatch`: The `/im.*/.*.html` regular expression applies to the path of the URL (for example, /images/random_page.html), before the query string.
  * `service`: Specifies the backend service to use if all conditions within the `matchRules` are true.



### Regular expression URL rewrites for route rules

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can use regular expression pattern rewrite actions (`regexRewrite`) to rewrite URL paths by substituting or removing URL path components before forwarding requests to your backends.

You specify regular expressions using the following fields:

  * `pathMatchers[].routeRules[].routeAction.urlRewrite.regexRewrite.pathPattern`: A regular expression in [RE2 syntax](https://github.com/google/re2/wiki/Syntax) used to match and capture portions of the incoming request path.
  * `pathMatchers[].routeRules[].routeAction.urlRewrite.regexRewrite.pathSubstitution`: A string used to reconstruct the path before sending the request to the backend service. You can reference captured groups from `pathPattern` by using named syntax `\g<name>` (for named groups like `(?<name>re)`) or numbered syntax such as `\1` or `\2`.



#### How RE2 capture groups work

RE2 capture groups are portions of a regular expression enclosed in parentheses `(...)` that save the matched text for later use or extraction. They let you capture path segments and rewrite the URL before it is sent to the backend.

Capture groups are defined in the `pathPattern` field by using the format `(?<name>re)` or `(?P<name>re)`, where `name` is the variable name assigned to the captured section of the URL path to be replaced, and `re` is the regular expression pattern used to match that section. Captured groups are then referenced for substitution in the `pathSubstitution` field by using the format `\g<name>`.

For example:

  * Incoming client request URL path: `/api/users/21334/profile.json`
  * `pathPattern`: `/api/users/(?<id>\d+)/(?<path>[a-z]+\.json)`
  * `pathSubstitution`: `/users/\g<id>/\g<path>`
  * Path sent to backend: `/users/21334/profile.json`



Note that capture groups written in the format `(?<name>re)` are both numbered and named. You can refer to them either by their name, `\g<name>`, or by their number, `\1`.

Additional usage notes:

  * Regular expression URL rewrites are supported only for the following products:

    * Regional internal Application Load Balancers
    * Cross-region internal Application Load Balancers
    * Regional external Application Load Balancers
    * Global external Application Load Balancers

Classic Application Load Balancers don't support regular expressions.

  * You must use RE2 syntax to construct your regular expressions. For the complete list of limitations and operators permitted in URL maps, see [RE2 specifications for URL maps](https://docs.cloud.google.com/load-balancing/docs/re2-support).

  * You can specify only one URL rewrite action per route rule. `regexRewrite` can't be used together with `pathPrefixRewrite` or `pathTemplateRewrite`.

  * The `pathSubstitution` field supports a maximum of eight capture groups which must be defined in the `pathPattern` field.

  * The `pathPattern` and `pathSubstitution` fields are each limited to a maximum of 250 characters.




#### Example: Rewrite URL using regular expression capture groups

The following example shows how to configure a URL map to capture parts of a request path using named capture groups and substitute them into a new path.

In this example, incoming request URLs such as `/region/us-central1/bucket/my-bucket/stage/dev/object.pdf` are rewritten to `/us-central1/my-bucket-dev/object.pdf` before being proxied to the backend service.
    
    
    defaultService: projects/example-project/regions/us-central1/backendServices/default-bs
    name: regex-rewrite-url-map
    pathMatchers:
    - name: region-matcher
      defaultService: projects/example-project/regions/us-central1/backendServices/default-bs
      routeRules:
      - matchRules:
        - prefixMatch: /region/
        priority: 1
        service: projects/example-project/regions/us-central1/backendServices/rewrite-bs
        routeAction:
          urlRewrite:
            regexRewrite:
              pathPattern: "/region/(?<reg>[a-z0-9-]+)/bucket/(?<bkt>[a-z0-9-]+)/stage/(?<stg>[a-z0-9-]+)/object\\.pdf"
              pathSubstitution: "/\\g<reg>/\\g<bkt>-\\g<stg>/object.pdf"
    

Here is an explanation of the fields used in the example URL map:

  * `defaultService`: Specifies the default backend service that requests will be routed to if no other `routeRules` match the incoming request.
  * `name`: A user-defined name for this URL map.
  * `routeRules`: A list of rules that define how traffic is matched and routed. Rules are evaluated in order of their priority.
  * `matchRules`: An array of conditions that must be met for this rule to be applied.
  * `prefixMatch`: Matches the beginning of the URL path. In the corrected example, it ensures the rule only applies to paths starting with `/region/`.
  * `priority`: An integer that determines the order in which rules are evaluated. Lower numbers have higher priority.
  * `service`: The backend service to which traffic will be forwarded if this rule's `matchRules` are met and the route action is executed.
  * `routeAction`: Specifies the action to take when a request matches the `matchRules`.
  * `urlRewrite`: Defines how the URL should be modified before being proxied to the backend service.
  * `regexRewrite`: Configures URL rewriting using regular expressions.
  * `pathPattern`: The regular expression (using Google RE2 syntax) used to match the incoming URL path. Named capture groups using the format `(?<name>re)` are used to capture parts of the path. In the example, `"/region/(?<reg>[a-z0-9-]+)/bucket/(?<bkt>[a-z0-9-]+)/stage/(?<stg>[a-z0-9-]+)/object\\.pdf"` captures the region (`reg`), the bucket name (`bkt`), and the stage name (`stg`).
  * `pathSubstitution`: The string used to reconstruct the path. It references the named capture groups from the pattern using the syntax `\g<name>`. In the example, `"/\\g<reg>/\\g<bkt>-\\g<stg>/object.pdf"` uses the captured `reg`, `bkt`, and `stg` values to build the new path: `/us-central1/my-bucket-dev/object.pdf`.



### Wildcards, regular expressions, and dynamic URLs in path rules and prefix match

  * A path rule (`pathMatchers[].pathRules[]`) can only include a wildcard character (`*`) after a forward slash character (`/`). For example, `/videos/*` and `/videos/hd/*` are valid for path rules, but `/videos*` and `/videos/hd*` are not.

  * Path rules don't use regular expressions or substring matching. PathTemplateMatch can use simplified path matching operators. For example, path rules for either `/videos/hd` or `/videos/hd/*` don't apply to a URL with the path `/video/hd-abcd`. However, a path rule for `/video/*` does apply to that path.

  * A prefix match (`pathMatchers[].routeRules[].matchRules[].prefixMatch`) does _not_ treat `*` as a wildcard character, but as a literal character.

  * Path matchers (and URL maps in general) don't offer features that function like Apache's `<LocationMatch>` directive. If you have an application that generates dynamic URL paths that have a common prefix, such as `/videos/hd-abcd` and `/videos/hd-pqrs`, and you need to send requests made to those paths to different backend services, you might not be able to do that with a URL map. For cases containing only a few possible dynamic URLs, you _might_ be able to create a path matcher with a limited set of path rules. For more complex cases, you need to do path-based regular expression matching on your backends.




### Wildcards and pattern matching operators in path templates for route rules

Flexible pattern matching operators let you match multiple parts of a URL path, including partial URLs and suffixes (file extensions), by using wildcard syntax. These operators can be helpful when you need to route traffic and execute rewrites based on complex URL paths. You can also associate one or more path components with named variables and then refer to those variables when rewriting the URL. With named variables, you can reorder and remove URL components before the request is sent to your origin.

Pattern matching with wildcards is supported only for the following products:

  * Global external Application Load Balancer


  * Regional external Application Load Balancer
  * Regional internal Application Load Balancer


  * Cross-region internal Application Load Balancer
  * Cloud Service Mesh



The following example routes traffic for an eCommerce application that has separate services for cart information and user information. You can configure `routeRules` with flexible pattern matching operators and named variables to send the user's unique ID to a user account details page and the user's cart information to a cart processing service after rewriting the URL.
    
    
      pathMatchers:
        - name: cart-matcher
          routeRules:
            - description: CartService
              matchRules:
                - pathTemplateMatch: '/xyzwebservices/v2/xyz/users/{username=*}/carts/{cartid=**}'
              service: cart-backend
              priority: 1
              routeAction:
                urlRewrite:
                  pathTemplateRewrite: '/{username}-{cartid}/'
        - name: user-matcher
          routeRules:
            - description: UserService
              matchRules:
                - pathTemplateMatch: '/xyzwebservices/v2/xyz/users/*/accountinfo/*'
              service: user-backend
              priority: 1
    

Here's what happens when a client requests `/xyzwebservices/v2/xyz/users/abc@xyz.com/carts/FL0001090004/entries/SJFI38u3401nms?fields=FULL&client_type=WEB`, which has both user information and cart information:

  1. The request path matches the `pathTemplateMatch` within the `cart-matcher` pathMatcher. The `{username=*}` variable matches `abc@xyz.com` and the `{cartid=**}` variable matches `FL0001090004/entries/SJFI38u3401nms`.
  2. The query parameters are split off from the path, the path is rewritten based on `pathTemplateRewrite`, and the query parameters are appended to the rewritten path. We must only use the same variables that we used to define the `pathTemplateMatch` in our `pathTemplateRewrite`.
  3. The rewritten request is sent to `cart-backend` with the rewritten URL path: `/abc@xyz.com-FL0001090004/entries/SJFI38u3401nms?fields=FULL&client_type=WEB`.



The following happens when a client requests `/xyzwebservices/v2/xyz/users/abc%40xyz.com/accountinfo/abc-1234` instead, which has only user and account information:

  1. The request path matches the `pathTemplateMatch` within the `user-matcher` pathMatcher. The first `*` matches `abc%40xyz.com` and the second `*` matches `abc-1234`.
  2. The request is sent to `user-backend`.



The following table outlines the syntax for path template patterns.

Operator | Matches  
---|---  
**`*`** | A single path segment, not including the surrounding path separator `/` characters.  
**`**`** | Matches zero or more characters, including any path separator `/` characters between multiple path segments. If other operators are included, the `**` operator must be the last operator.  
**`{name}` or `{name=*}`** | A named variable matching one path segment. Matches a single path segment, not including the surrounding path separator `/` characters.  
**`{name=news/*}`** | A named variable explicitly matching two path segments: `news` and a `*` wildcard segment.  
**`{name=*/news/*}`** | A named variable matching three path segments.  
**`{name=**}`** | A named variable matching zero or more characters. If present, must be the last operator.  
  
When you use these operators for flexible pattern matching, keep these considerations in mind:

  * Multiple operators can be combined in a single pattern.
  * Query parameters are split off from the path, the path is rewritten based on `pathTemplateRewrite`, and the query parameters are appended to the rewritten path.
  * Requests are not percent-encoding normalized. For example, a URL with a percent-encoded slash character (%2F) is not decoded into the unencoded form.
  * Each variable name, such as `{segment}` or `{region}`, can appear only once in the same pattern. Multiple variables of the same name are invalid and are rejected.
  * Variable names are case-sensitive and must be valid identifiers. To check if a variable name is valid, ensure that it matches the regular expression `^[a-zA-Z][a-zA-Z0-9_]*$`. 
    * `{API}`, `{api}`, and `{api_v1}` are all valid identifiers. They identify three distinct variables.
    * `{1}`, `{_api}`, and `{10alpha}` are not valid identifiers.
  * There's a limit of five operators per template pattern.



To execute an optional URL rewrite before the request is sent to the origin, you can use the same variables that you defined to capture a path. For example, you can reference, reorder, or omit variables in the `pathTemplateRewrite` field when defining `urlRewrite`.

When you use variables and operators for flexible pattern matching for URL rewrites, keep these considerations in mind:

  * When rewriting a URL, you can omit variables if they're not required as part of the rewritten URL.
  * Prior to any rewrites, you can identify the URL sent by the client at your origin by inspecting response headers. The original client URL is populated with the `x-client-request-url` header and the `x-envoy-original-path` header.



## Example URL map workflow with an external Application Load Balancer

The following example illustrates the order of operations for a URL map. This example configures only the URL map for an existing classic Application Load Balancer. For conceptual simplicity, it only uses backend services; however, you can substitute backend buckets instead. To learn how to create the load balancer's other components, see [Create a classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https).

For more information about creating and configuring URL maps with path matchers and host rules, see the [`gcloud compute url-maps create` documentation](https://docs.cloud.google.com/sdk/gcloud/reference/compute/url-maps/create).

  1. Create a URL map for the load balancer and specify a default backend service. This example creates a URL map named `video-org-url-map` that references an existing backend service named `org-site`.
         
         gcloud compute url-maps create video-org-url-map \
             --default-service=org-site
         

  2. Create a path matcher named `video-matcher` with the following characteristics:

     * The default backend service is `video-site`, an existing backend service.
     * Add path rules that direct requests for the exact URL path `/video/hd` or the URL path prefix `/video/hd/*` to an existing backend service named `video-hd`.
     * Add path rules that direct requests for the exact URL path `/video/sd` or the URL path prefix `/video/sd/*` to an existing backend service named `video-sd`.
    
    gcloud compute url-maps add-path-matcher video-org-url-map \
        --path-matcher-name=video-matcher \
        --default-service=video-site \
        --path-rules=/video/hd=video-hd,/video/hd/*=video-hd,/video/sd=video-sd,/video/sd/*=video-sd
    

  3. Create a host rule for the `example.net` hostname that references the `video-matcher` path matcher.
         
         gcloud compute url-maps add-host-rule video-org-url-map \
             --hosts=example.net \
             --path-matcher-name=video-matcher
         




The `video-org-url-map` URL map should look like this:
    
    
    gcloud compute url-maps describe video-org-url-map
    
    
    
    creationTimestamp: '2021-03-05T13:34:15.833-08:00'
    defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/org-site
    fingerprint: mfyJIT7Zurs=
    hostRules:
    - hosts:
      - '*'
      pathMatcher: video-matcher
    - hosts:
      - example.net
      pathMatcher: video-matcher
    id: '8886405179645041976'
    kind: compute#urlMap
    name: video-org-url-map
    pathMatchers:
    - defaultService: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/video-site
      name: video-matcher
      pathRules:
      - paths:
        - /video/hd
        - /video/hd/*
        service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/video-hd
      - paths:
        - /video/sd
        - /video/sd/*
        service: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices/video-sd
    selfLink: https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/urlMaps/video-org-url-map
    

The `video-org-url-map` URL map directs requested URLs to backends in the following way.

[ ![URL map with a path rule, path matchers, and a host rule.](https://docs.cloud.google.com/static/load-balancing/images/url-map-detail-3.svg)](https://docs.cloud.google.com/static/load-balancing/images/url-map-detail-3.svg) URL map with a path rule, path matchers, and a host rule (click to enlarge).

The following table explains the request processing shown in the preceding diagram.

Hostname | URL paths | Selected backend service | Reason for selection  
---|---|---|---  
Hostname:  
`example.org` and all other hostnames _different from_  
`example.net` | all paths | `org-site` | The hostname is not in any host rule of the URL map, so the request is directed to the URL map's default backend service.  
Hostname:  
`example.net` | `/video`  
`/video/examples` | `video-site` | The request goes to the default backend service because there is no path rule for `/video/` or `/video/*`. The host rule for `example.net` references a path matcher, but that path matcher does not have any path rules that would apply to these paths.   
Hostname:  
`example.net` | `/video/hd`  
`/video/hd/movie1`  
`/video/hd/movies/movie2`  
Other URLs that begin with `/video/hd/*` | `video-hd` | A host rule for `example.net` references a path matcher whose path rules direct requests for URL paths that either exactly match `/video/hd` or that begin with `/video/hd/*` to the `video-hd` backend service.  
Hostname:  
`example.net` | `/video/sd`  
`/video/sd/show1`  
`/video/sd/shows/show2`  
Other URLs that begin with `/video/sd/*` | `video-sd` | A host rule for `example.net` references a path matcher whose path rules direct requests for URL paths that either exactly match `/video/sd` or that begin with `/video/sd/*` to the `video-sd` backend service.  
  
## URL redirects

A _URL redirect_ redirects your domain's visitors from one URL to another.

A _default URL redirect_ is not conditioned on matching any particular pattern in the incoming request. For example, you might want to use a default URL redirect to redirect _any_ hostname to a hostname of your choice.

There are several ways to create a URL redirect, as outlined in the following table.

Method | Configuration  
---|---  
URL map's default URL redirect | Top-level `defaultUrlRedirect`  
A path matcher's default URL redirect | `pathMatchers[].defaultUrlRedirect[]`  
A path matcher's path rule's URL redirect | `pathMatchers[].pathRules[].urlRedirect`  
A path matcher's route rule's URL redirect | `pathMatchers[].routeRules[].urlRedirect`  
  
Inside of a `defaultUrlRedirect` or `urlRedirect`, `pathRedirect` always works as follows:

  * The entire request path is replaced with the path you specify.



Inside of a `defaultUrlRedirect` or `urlRedirect`, how the`prefixRedirect` works depends on how you use it:

  * If you use a `defaultUrlRedirect`, `prefixRedirect` is effectively a prefix prepend because the matched path is always `/`.
  * If you use a `urlRedirect` within a path matcher's route rule or path rule, `prefixRedirect` is a prefix _replacement_ based on how the requested path was matched _as defined in the path rule or route rule_.



### Redirect examples

The following table provides some examples of redirect configurations. The right-hand column shows the API configuration for a default URL redirect.

You want | Accomplished using a default URL redirect  
---|---  
HTTP-to-HTTPS redirect  
  
Redirect  
http://host.name/path  
to  
https://host.name/path  | 
    
    
                kind: compute#urlMap
                name: web-map-http
                defaultUrlRedirect:
                  httpsRedirect: True
                 
  
HTTP-to-HTTPS + Host redirect  
  
Redirect  
http://_any-host-name_ /path  
to  
https://www.example.com/path  | 
    
    
                kind: compute#urlMap
                name: web-map-http
                defaultUrlRedirect:
                  httpsRedirect: True
                  hostRedirect: "www.example.com"
                
  
HTTP-to-HTTPS + Host redirect + Full path redirect  
  
Redirect  
http://_any-host-name_ /path  
to  
https://www.example.com/newPath  | 
    
    
                kind: compute#urlMap
                name: web-map-http
                defaultUrlRedirect:
                  httpsRedirect: True
                  hostRedirect: "www.example.com"
                  pathRedirect: "/newPath"
                 
  
HTTP-to-HTTPS + Host redirect + Prefix redirect  
  
Redirect  
http://_any-host-name_ /**originalPath**  
to  
https://www.example.com/newPrefix/**originalPath** | 
    
    
                kind: compute#urlMap
                name: web-map-http
                defaultUrlRedirect:
                  httpsRedirect: True
                  hostRedirect: "www.example.com"
                  prefixRedirect: "/newPrefix"
                  
  
The following partial snippet annotates each API resource:
    
    
    defaultUrlRedirect:
       redirectResponseCode: MOVED_PERMANENTLY_DEFAULT
       httpsRedirect: True # True if you want https://, false if you want http://
       hostRedirect: "new-host-name.com" # Omit to keep the requested host
       pathRedirect: "/new-path" # Omit to keep the requested path; mutually exclusive to prefixRedirect
       prefixRedirect: "/newPrefix" # Omit to keep the requested path; mutually exclusive to pathRedirect
       stripQuery: False # True to omit everything in the URL after ?
       ...
    

## What's next

  * To add, validate, test, list, or delete a URL map, see [Use URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map). 

  * For information about routing rule maps with Cloud Service Mesh, see [Cloud Service Mesh routing rule maps overview](https://docs.cloud.google.com/service-mesh/docs/route-rule-map-concepts).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
