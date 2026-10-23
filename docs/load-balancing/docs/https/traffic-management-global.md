---
url: https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global/
title: Traffic management overview for global external Application Load Balancers \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:39.043617+00:00
---

# Traffic management overview for global external Application Load Balancers  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Traffic management overview for global external Application Load Balancers Stay organized with collections  Save and categorize content based on your preferences. 

This page gives you an overview of the advanced traffic management capabilities available for global external Application Load Balancers. This page is for the global external Application Load Balancer only. These load balancers are always global and always in Premium Tier. If you use a load balancer in a different mode, see one of the following pages:

  * [Traffic management overview for a classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management)

  * [Traffic management overview for regional external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-regional)


Global external Application Load Balancers support the following advanced traffic management features: 
  * **Traffic steering**. Intelligently route traffic based on HTTP(S) parameters (for example, host, path, headers, and other request parameters).
  * **Traffic actions**. Perform request-based and response-based actions (for example, redirects and header transformations).
  * **Traffic policies**. Fine-tune load balancing behavior (for example, advanced load balancing algorithms).



You can set up these features by using URL maps and backend services. For more information, see the following topics:

  * [URL map overview](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts)
  * [Using URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map)
  * [Understanding backend services](https://docs.cloud.google.com/load-balancing/docs/backend-service)



## Use case examples

Traffic management addresses many use cases. This section provides a few high-level examples.

### Traffic steering: header-based routing

Traffic steering lets you direct traffic to service instances based on HTTP parameters such as request headers. For example, if a user's device is a mobile device with `user-agent:Mobile` in the request header, traffic steering can send that traffic to service instances designated to handle mobile traffic, and send traffic that doesn't have `user-agent:Mobile` to instances designated to handle traffic from other devices.

[ ![Cloud Load Balancing traffic steering.](https://docs.cloud.google.com/static/load-balancing/images/traffic-steering.svg)](https://docs.cloud.google.com/static/load-balancing/images/traffic-steering.svg) **Figure 1.** Cloud Load Balancing traffic steering (click to enlarge).

### Traffic actions: weight-based traffic splitting

Deploying a new version of an existing production service generally incurs some risk. Even if your tests pass in staging, you probably don't want to subject 100% of your users to the new version immediately. With traffic management, you can define percentage-based traffic splits across multiple backend services.

For example, you can send 95% of the traffic to the previous version of your service and 5% to the new version of your service. After you've validated that the new production version works as expected, you can gradually shift the percentages until 100% of the traffic reaches the new version of your service. Traffic splitting is typically used for deploying new versions, A/B testing, service migration, and similar processes.

[ ![Cloud Load Balancing traffic splitting.](https://docs.cloud.google.com/static/load-balancing/images/traffic-splitting.svg)](https://docs.cloud.google.com/static/load-balancing/images/traffic-splitting.svg) **Figure 2.** Cloud Load Balancing traffic splitting (click to enlarge). Don't configure session affinity if you're using weighted traffic splitting. If you do, the weighted traffic splitting configuration takes precedence. 

### Traffic policies: request mirroring

Your organization might have specific compliance requirements mandating that all traffic be mirrored to an additional service that can, for example, record the request details in a database for later replay.

## Extensibility with Service Extensions

The integration with [Service Extensions](https://docs.cloud.google.com/service-extensions/docs/overview#integration-lb) lets you insert custom logic into the load balancing data path of [supported Application Load Balancers](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs) by using callouts and plugins.

You can configure these extensions at various points in the processing path: [authorization](https://docs.cloud.google.com/service-extensions/docs/configure-authorization-extensions), [edge](https://docs.cloud.google.com/service-extensions/docs/configure-edge-extensions), [route](https://docs.cloud.google.com/service-extensions/docs/configure-route-extensions), and [traffic](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions).

You can also use Service Extensions to configure advanced features, such as [dynamic forwarding](https://docs.cloud.google.com/service-extensions/docs/lb-advanced-use-cases#dynamic-forwarding).

For more information, see [Service Extensions overview](https://docs.cloud.google.com/service-extensions/docs/overview).

## Traffic management components

At a high level, load balancers provide traffic management by leveraging [global URL maps](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps) and [global backend services](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices) resources. 

You can set up traffic steering and traffic actions by using URL maps. Google Cloud resources that are associated with URL maps include the following:

  * Route rule
  * Rule match
  * Rule action



You can set up traffic policies by using backend services. Google Cloud resources that are associated with backend services include the following:

  * Locality load balancer policy
  * Consistent hash load balancer settings
  * Outlier detection



The following diagram shows the resources that are used to implement each feature.

[ ![Cloud Load Balancing data model.](https://docs.cloud.google.com/static/load-balancing/images/lb-data-model.svg)](https://docs.cloud.google.com/static/load-balancing/images/lb-data-model.svg) **Figure 3.** Cloud Load Balancing data model (click to enlarge).

## Routing requests to backends

In global external Application Load Balancers, the backend for your traffic is determined by using a two-phased approach: 

  * The load balancer selects a backend service or backend bucket based on rules defined in a [global URL map](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps).
  * The backend service selects a backend instance based on policies defined in a [global backend service](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices). 



When you configure routing, you can choose between the following modes:

  * Simple host and path rule
  * Advanced host, path, and route rule



The two modes are mutually exclusively. Each URL map can contain only one mode or the other mode.

### Simple host and path rule

In a simple host and path rule, URL maps work as described in the [URL map overview](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts#url-map-components).

The following diagram shows the logical flow of a simple host and path rule.

[ ![URL map flow with a simple host and path rule.](https://docs.cloud.google.com/static/load-balancing/images/url-map-simple-1.svg)](https://docs.cloud.google.com/static/load-balancing/images/url-map-simple-1.svg) **Figure 4.** URL map flow with a simple host and path rule (click to enlarge).

A request is initially evaluated by using host rules. A host is the domain specified by the request. If the request `host` matches one of the entries in the `hosts` field, the associated path matcher is used.

Next, the path matcher is evaluated. Path rules are evaluated on the longest-path-matches-first basis, and you can specify path rules in any order. After the most specific match is found, the request is routed to the corresponding backend service. If the request doesn't match, the default backend service is used.

A typical simple host and path rule might look something like the following, where video traffic goes to `video-backend-service`, and all other traffic goes to `web-backend-service`. The `defaultService` and `service` can point to a backend service or a backend bucket. This example shows backend services. 
    
    
    gcloud compute url-maps describe lb-map
    
    
    
    defaultService: global/backendServices/web-backend-service
    hostRules:
    - hosts:
      - '*'
      pathMatcher: pathmap
    name: lb-map
    pathMatchers:
    - defaultService: global/backendServices/web-backend-service
      name: pathmap
      pathRules:
      - paths:
        - /video
        - /video/*
        service: global/backendServices/video-backend-service
    

### Advanced host, path, and route rule

Advanced host, path, and route rules provide additional configuration options compared to simple host and path rules. These options enable more advanced traffic management patterns and also modify some of the semantics. For example, route rules have an associated priority value and are interpreted in priority order (rather than by using longest-path-matches-first semantics).

As in the earlier simple host and path rule example, you can configure advanced traffic management by using a URL map. For example, the following URL map configures routing where 95% of the traffic is routed to one backend service, and 5% of the traffic is routed to another backend service.

The `defaultService` and `service` can point to a backend service or a backend bucket. This example shows backend services.
    
    
    gcloud compute url-maps describe lb-map
    
    
    
    defaultService: global/backendServices/service-a
    hostRules:
    - hosts:
      - '*'
      pathMatcher: matcher1
    name: lb-map
    pathMatchers:
    - defaultService: global/backendServices/service-a
      name: matcher1
      routeRules:
      - matchRules:
        - prefixMatch: ''
        routeAction:
          weightedBackendServices:
          - backendService: global/backendServices/service-a
            weight: 95
          - backendService: global/backendServices/service-b
            weight: 5
    

#### Host rules

When a request reaches your load balancer, the request's `host` field is evaluated against the `hostRules` defined in the URL map. Each host rule consists of a list of one or more hosts and a single path matcher (`pathMatcher`). If no `hostRules` are defined, the request is routed to the `defaultService`.

For more information, see `hostRules[]` and `defaultService` in the [global URL map API documentation](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps). 

#### Path matchers

After a request matches a host rule, the load balancer evaluates the path matcher corresponding to the host.

A path matcher is made up of the following:

  * One or more path rules (`pathRules`) _or_ route rules (`routeRules`).
  * A default service (`defaultService`), which is the default backend service or backend bucket that is used when no other backend services or backend buckets match.

For more information, see `pathMatchers[]`, `pathMatchers[].pathRules[]`, and `pathMatchers[].routeRules[]` in the [global URL map API documentation](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps). 

#### Path rules

Path rules (`pathRules`) specify one or more URL paths, such as `/` or `/video`. Path rules are generally intended for the type of simple host and path-based routing described previously.

For more information, see `pathRules[]` in the [global URL map API documentation](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps). 

#### Route rules

A route rule (`routeRules`) matches information in an incoming request and makes a routing decision based on the match.

Route rules can contain a variety of different match rules (`matchRules`) and a variety of different route actions (`routeAction`).

A match rule evaluates the incoming request based on the HTTP(S) request's path, headers, and query parameters. Match rules support various types of matches (for example, prefix match) as well as modifiers (for example, case insensitivity). This lets you, for example, send HTTP(S) requests to a set of backends based on the presence of a custom-defined HTTP header.

Note: Match options and semantics differ depending on the request portion that you match. For more information, see `matchRules[]` in the [global URL map API documentation](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps). 

If you have multiple route rules, the load balancer executes them in priority order (based on the `priority` field), which lets you specify custom logic for matching, routing, and other actions.

Within a given route rule, when the first match is made, the load balancer stops evaluating the match rules, and any remaining match rules are ignored.

Google Cloud performs the following actions:

  1. Looks for the first match rule that matches the request.
  2. Stops looking at any other match rules.
  3. Applies the actions in the corresponding route actions.



Route rules have several components, as described in the following table.

Route rule component (`API field name`) | Description  
---|---  
Priority (`priority`) | A number from 0 through 2,147,483,647 (that is, (2^31)-1) assigned to a route rule within a given path matcher.  
  
The priority determines the order of route rule evaluation. The priority of a rule decreases as its number increases so that a rule with priority `4` is evaluated before a rule with priority `25`. The first rule that matches the request is applied.   
  
Priority numbers can have gaps. You cannot create more than one rule with the same priority.   
Description (`description`) | An optional description of up to 1,024 characters.  
Service (`service`) | The full or partial URL of the backend service resource to which traffic is directed if this rule is matched.   
Match rules (`matchRules`) | One or more rules that are evaluated against the request. These `matchRules` can match all or a subset of the request's HTTP attributes, such as the path, HTTP headers, and query (GET) parameters.  
  
Within a `matchRule`, all matching criteria must be met for the `routeRule`'s `routeActions` to take effect. If a `routeRule` has multiple `matchRules`, the `routeActions` of the `routeRule` take effect when a request matches any of the `routeRule`'s `matchRules`.   
Route action (`routeAction`) | Lets you specify what actions to take when the match rule criteria are met. These actions include traffic splitting, URL rewrites, retry and mirroring, fault injection, and CORS policies.   
Redirect action (`urlRedirect`) | You can configure an action to respond with an HTTP redirect when the match rule criteria are met. This field cannot be used in conjunction with a route action.   
Header action (`headerAction`) | You can configure request and response header transformation rules when the criteria within `matchRules` are met.   
For more information about the following fields, see the [global URL map API documentation](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps). 

  * `routeRules[]`
  * `routeRules[].priority`
  * `routeRules[].description`
  * `routeRules[].service`
  * `routeRules[].matchRules[]`
  * `routeRules[].routeAction`
  * `routeRules[].urlRedirect`
  * `routeRules[].headerAction`



#### Match rules

Match rules (`matchRules`) match one or more attributes of a request and take actions specified in the route rule. The following list provides some examples of request attributes that can be matched by using match rules:

  * Host: a hostname is the domain name portion of a URL; for example, the hostname portion of the URL `http://example.net/video/hd` is `example.net`. In the request, the hostname comes from the `Host` header, as shown in this example curl command, where `10.1.2.9` is the load-balanced IP address:
        
        curl -v http://10.1.2.9/video/hd --header 'Host: example.com'
        

  * Paths follow the hostname—for example, `/images`. The rule can specify whether the entire path or only the leading portion of the path needs to match.

  * Other HTTP request parameters, such as HTTP headers, which allow cookie matching, as well as matching based on query parameters (GET variables).


For a complete list of supported match rules, see `pathMatchers[].routeRules[].matchRules[]` in the [global URL map API documentation](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps). 

#### Route actions

Route actions are specific actions to take when a route rule matches the attributes of a request.

Route action (`API field name`) | Description  
---|---  
Redirects (`urlRedirect`) | Returns a configurable 3 _xx_ response code. It also sets the `Location` response header with the appropriate URI, replacing the host and path as specified in the redirect action.   
URL rewrites (`urlRewrite`) | Rewrites the hostname portion of the URL, the path portion of the URL, or both, before sending a request to the selected backend service. For the path portion rewrites, you can use wildcards in `pathTemplateRewrite`.   
Header transformations (`headerAction`) | Adds or removes request headers before sending a request to the backend service. You can also add or remove response headers after receiving a response from the backend service. Attempting to add and remove the same header results in the header being removed, unless the `replace: True` flag is used with the `requestHeadersToAdd` operation.   
Traffic mirroring (`requestMirrorPolicy`) | In addition to forwarding the request to the selected backend service, sends an identical request to the configured mirror backend service on a _fire and forget_ basis. The load balancer doesn't wait for a response from the backend to which it sends the mirrored request.  
  
Mirroring is useful for testing a new version of a backend service. You can also use it to debug production errors on a debug version of your backend service, rather than on the production version. Note the following limitations when using traffic mirroring:

  * Traffic mirroring is supported when both backend services have managed instance groups, zonal NEGs, or hybrid NEGs backends. It is not supported for internet NEGs, serverless NEGs, and Private Service Connect backends.
  * Requests to the mirrored backend service do not generate any logs or metrics for Cloud Logging and Cloud Monitoring. 

  
Weighted traffic splitting (`weightedBackendServices`) | Allows traffic for a matched rule to be distributed to multiple backend services, proportional to a user-defined weight assigned to the individual backend service. This capability is useful for configuring staged deployments or A/B testing. For example, the route action could be configured such that 99% of the traffic is sent to a service that's running a stable version of an application, while 1% of the traffic is sent to a separate service running a newer version of that application.  
Retries (`retryPolicy`) | Configures the conditions under which the load balancer retries failed requests, how long the load balancer waits before retrying, and the maximum number of retries permitted. To learn more about retries, see the [Retries](https://docs.cloud.google.com/load-balancing/docs/https/request-distribution#retries_2) section in the _Request distribution overview_ page.  
Timeout (`timeout`) | Specifies the timeout for the selected route. Timeout is computed from the time that the request is fully processed up until the time that the response is fully processed. Timeout includes all retries.  
Fault injection (`faultInjectionPolicy`) | Introduces errors when servicing requests to simulate failures, including high latency, service overload, service failures, and network partitioning. This feature is useful for testing the resiliency of a service to simulated faults.   
Delay injection (`faultInjectionPolicy`) | Introduces delays for a user-defined portion of requests before sending the request to the selected backend service.   
Abort injection (`faultInjectionPolicy`) | Responds directly to a fraction of requests with user-defined HTTP status codes instead of forwarding those requests to the backend service.   
Security policies (`corsPolicy`) | Cross-origin resource sharing (CORS) policies handle settings for enforcing CORS requests.   
  
You can specify one of the following route actions:

  * Route traffic to a single service (`service`).
  * Split traffic between multiple services (`weightedBackendServices weight:x`, where _x_ must be from 0 to 1000).
  * Redirect URLs (`urlRedirect`).



In addition, you can combine any one of the previously mentioned route actions with one or more of the following route actions:

  * Mirror traffic (`requestMirrorPolicy`).
  * Rewrite URL host and path (`urlRewrite`).
  * Retry failed requests (`retryPolicy`).
  * Set timeout (`timeout`).
  * Introduce faults to a percentage of the traffic (`faultInjectionPolicy`).
  * Add CORS policy (`corsPolicy`).
  * Manipulate request or response headers (`headerAction`).

For more information about the configuration and semantics of route actions, see the following in the [global URL map API documentation](https://docs.cloud.google.com/compute/docs/reference/rest/v1/urlMaps). 

  * `urlRedirect`
  * `urlRewrite`
  * `headerAction`
  * `requestMirrorPolicy`
  * `weightedBackendServices`
  * `retryPolicy`
  * `timeout`
  * `faultInjectionPolicy`
  * `corsPolicy`



#### HTTP-to-HTTPS redirects

If you need to redirect HTTP traffic to HTTPS, you can create two forwarding rules with a common IP address.

For a complete example, see [Set up HTTP-to-HTTPS redirect for global external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-http-https-redirect). 

## Traffic policies

By using backend service resources, you can configure traffic policies to fine-tune load balancing within an instance group or network endpoint group (NEG). These policies only take effect after a backend service has been selected by using your URL map (as described previously).

Traffic policies enable you to:

  * Control the load balancing algorithm among instances within the backend service.
  * Control the volume of connections to an upstream service.
  * Control the eviction of unhealthy hosts from a backend service.

The following traffic policy features are configured in the [global backend service](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices). **Note:** Traffic policies (including load balancing locality policy, session affinity, and outlier detection) aren't supported with internet NEG backends. Traffic policy (`API field name`) | Description  
---|---  
Load balancing locality policy (`LocalityLbPolicy`) |  For a backend service or bucket, traffic distribution is based on a _load balancing mode_ and a _load balancing locality policy_.  The balancing mode determines the fraction of traffic that must be sent to each backend (bucket, instance group, or `GCE_VM_IP_PORT` NEG). The load balancing policy (`LocalityLbPolicy`) determines how backends within the zone or in the group are load balanced. When a backend service receives traffic, it first directs traffic to a backend (bucket, instance group, or `GCE_VM_IP_PORT` NEG) according to the backend's balancing mode. After a backend is selected, traffic is then distributed among instances or endpoints within each zone according to the locality policy. For regional managed instance groups, the locality policy applies to each constituent zone.  For the balancing modes supported, see [Balancing mode](https://docs.cloud.google.com/load-balancing/docs/backend-service#balancing-mode).  For the load balancing policy algorithms supported, see `localityLbPolicy` in the [global backend service API documentation](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices).   
Session affinity (`consistentHash`) |  Includes HTTP cookie-based affinity, HTTP header-based affinity, client IP address affinity, stateful cookie-based session affinity, and generated cookie affinity. Session affinity provides a best-effort attempt to send requests from a particular client to the same backend for as long as the backend is healthy and has capacity.  Session affinity settings are fulfilled only if the load balancing locality policy is set to `RING_HASH` or `MAGLEV`. For more information about session affinity, see `consistentHash` in the [global backend service API documentation](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices).   
Outlier detection (`outlierDetection`) |  A set of policies that specify the criteria for eviction of unhealthy backend VMs or endpoints in NEGs, along with criteria defining when a backend or endpoint is considered healthy enough to receive traffic again.  For more information about outlier detection, see `outlierDetection` in the [global backend service API documentation](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices).   
  
## What's next

  * To configure traffic management for global external Application Load Balancer, see [Setting up traffic management for global external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
