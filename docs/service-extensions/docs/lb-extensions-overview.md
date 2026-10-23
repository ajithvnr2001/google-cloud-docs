---
url: https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview/
title: Cloud Load Balancing and Cloud CDN extensions overview \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:33:25.649127+00:00
---

# Cloud Load Balancing and Cloud CDN extensions overview  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Cloud Load Balancing and Cloud CDN extensions overview Stay organized with collections  Save and categorize content based on your preferences. 

Service Extensions lets you use extensions to instruct [supported Application Load Balancers](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs) to use plugins or send callouts from the load balancing data path to callout backend services or Google services. This page provides an overview about Cloud Load Balancing extensions.

You can configure Application Load Balancers to use the following types of extensions:

  * Edge extensions help you manipulate request headers to influence backend service selection and the content that Cloud CDN serves from cache. These extensions are configured to run early in the request processing lifecycle to influence caching and routing decisions, respectively, at the edge.

  * Route extensions help you influence backend service selection. These extensions are configured to run early in the request processing lifecycle.

  * Authorization extensions help you send authorization requests to your custom authorization engine. You configure these at the end of the processing cycle just before the load balancer sends requests to backends.

  * Traffic extensions help support additional custom security logic and traffic management capabilities. You configure these after authorization extensions but before the load balancer sends requests to backends or receives responses from them.




## Supported Application Load Balancers for user-managed extensions

Service Extensions supports user-managed extensions for the following [Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer):

Application Load Balancers | Extensions  
---|---  
Edge | Route | Authorization | Traffic  
Plugins | Plugins | Callouts | Callouts | Plugins | Callouts  
Global external Application Load Balancer | ✓ |  |  | ✓ | ✓ | ✓  
Regional external Application Load Balancer |  | ✓ | ✓ | ✓ | ✓ | ✓  
Regional internal Application Load Balancer |  | ✓ | ✓ | ✓ | ✓ | ✓  
Cross-region internal Application Load Balancer |  | ✓ | ✓ | ✓ | ✓ | ✓  
**Note:** Extensions aren't supported on classic Application Load Balancers.

## Extensibility points in the load balancing data path

Service Extensions supports extensions in different stages of the load balancing data path.

Figure 1 shows how Service Extensions supports extensions in the application security and traffic management stages for global external Application Load Balancers.

[ ![](https://docs.cloud.google.com/static/service-extensions/images/callouts-glb.svg)](https://docs.cloud.google.com/static/service-extensions/images/callouts-glb.svg) **Figure 1.** Global external Application Load Balancers support extensions at the edge routing, application security, and traffic management stages (click to enlarge).

Figure 2 shows how Service Extensions supports extensions in the routing, application security, and traffic management stages for these types of load balancers: Regional external Application Load Balancer, Regional internal Application Load Balancer, and Cross-region internal Application Load Balancer.

[ ![](https://docs.cloud.google.com/static/service-extensions/images/callouts-rlb.svg)](https://docs.cloud.google.com/static/service-extensions/images/callouts-rlb.svg) **Figure 2.** Regional external Application Load Balancers, regional internal Application Load Balancers, and cross-region internal Application Load Balancers support extensions at the routing and traffic management stages (click to enlarge).

### How edge extensions work

Edge extensions run first on the request processing path and let you use request headers to influence backend service selection and the content that Cloud CDN serves from cache.

**Note:** Load balancers call edge extensions only during request processing and only for request headers.

After a load balancer calls an edge extension, it does the following:

  * Selects the backend service by evaluating the URL map
  * Applies [Google Cloud Armor policies](https://docs.cloud.google.com/armor/docs/security-policy-overview) security policies
  * Does a cache lookup and serves from cache if there is a cache hit
  * Applies Cloud Armor policies for the selected backend service
  * Applies CORS policies
  * Applies the stateful session affinity policy
  * Applies [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview) policies for the selected backend service
  * Calls authorization extensions, if any are configured in the processing path of the selected backend service
  * Performs fault injection
  * Calls traffic extensions, if any
  * Performs URL rewrites
  * Performs header manipulation according to the URL map and adds custom request header variables
  * Performs redirects or routing to the selected backend service while applying timeouts and retry policies in the URL map and the load balancing settings for the backend service
  * Performs request mirroring



### How route extensions work

Route extensions run first in the request processing path when the load balancer receives request headers and before it evaluates the [URL map](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts).

**Note:** Load balancers invoke route extensions only during request processing and only for request headers.

After a load balancer calls a route extension for a request, it does the following:

  * Selects the backend service by evaluating the URL map
  * Applies Cloud Armor policies for the selected backend service
  * Applies IAP policies for the selected backend service
  * Performs fault injection
  * Performs request header transformations and resolves custom request header variables
  * Calls traffic extensions, if they exist in the processing path of the selected backend service
  * Performs URL rewrites
  * Performs redirects or routing to the selected backend service and applies timeouts and retry policies in the URL map and other load balancing settings for the backend service



### How authorization extensions work

You can configure authorization policies with authorization extensions to delegate authorization decisions to custom authorization engines. For more information about authorization policies, see [Authorization policy overview](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview).

Authorization extensions are called on the request path after route extensions are called and a backend for the request has been selected. These extensions can't influence backend service selection.

In [Preview](https://cloud.google.com/products#product-launch-stages), for regional external Application Load Balancers and regional internal Application Load Balancers, authorization policies are invoked after route extensions. When designing authorization extensions, consider the following points:

  * Extensions invoked by authorization policies of the `REQUEST_AUTHZ` profile type receive and evaluate only HTTP request headers with the [`ext_proc`](https://docs.cloud.google.com/service-extensions/docs/callouts-overview#ext_proc) or [`ext_authz`](https://docs.cloud.google.com/service-extensions/docs/callouts-overview#ext_authz) protocol.

  * Extensions invoked by authorization policies of the `CONTENT_AUTHZ` profile type receive headers, body, and trailers of requests and responses. These must be configured in `FULL_DUPLEX_STREAMED` [body processing mode](https://docs.cloud.google.com/service-extensions/docs/callouts-overview#body-processing-modes) of the `ext_proc` protocol.




In the data path, authorization extensions based on request authorization policies run before those based on content authorization policies.

### How traffic extensions work

Load balancers run traffic extensions last in the request processing path and first in the response processing path.

These extensions let you modify the headers and payloads of both requests and responses without impacting the choice of the backend service. You can also use traffic extensions for custom logging by specifying the information that you want to log, the format, and the external provider.

Before a load balancer calls a traffic extension on the request path for a request, it does the following:

  * Performs fault injection
  * Selects a backend service for the request
  * Applies Cloud Armor policies for the selected backend service
  * Applies IAP policies for the selected backend service
  * Applies [Cloud CDN caching](https://docs.cloud.google.com/cdn/docs/caching) policies for the selected backend service in the case of global external Application Load Balancers



After a load balancer calls a traffic extension on the request path for a request, it does the following:

  * Performs URL rewrites
  * Performs header manipulation according to the URL map and adds custom request header variables
  * Performs redirects or routing to the selected backend service while applying timeouts and retry policies in the URL map and the load balancing settings for the backend service
  * Performs request mirroring



After a load balancer calls a traffic extension on the response path for a request, it does the following:

  * Performs response header transformations and resolves custom response header variables
  * Performs logging by using [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview)
  * Performs Cloud CDN caching in the case of global external Application Load Balancers



## Custom headers

In the traffic path, edge and route extensions run at extensibility points before the stage at which the load balancer adds [custom headers](https://docs.cloud.google.com/load-balancing/docs/https/custom-headers#variables). As such, the headers that the edge and route extensions receive don't contain the custom headers that the load balancer adds.

To make information that you might usually put in custom headers available to edge and route extensions, consider using a [supported attribute](https://docs.cloud.google.com/service-extensions/docs/attributes) instead.

## Limitations of extensions

  * A forwarding rule can have only one `LbEdgeExtension` resource, one `LbTrafficExtension` resource, and one `LbRouteExtension` resource.
  * For callouts, the callout backend service must be in the same project as the forwarding rule.
  * Cross-project referencing between extensions and forwarding rules isn't supported.



## What's next

  * [Plugins overview](https://docs.cloud.google.com/service-extensions/docs/plugins-overview)
  * [Cloud Load Balancing callouts overview](https://docs.cloud.google.com/service-extensions/docs/callouts-overview)
  * [Integration with Google services](https://docs.cloud.google.com/service-extensions/docs/integration-with-google-services)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
