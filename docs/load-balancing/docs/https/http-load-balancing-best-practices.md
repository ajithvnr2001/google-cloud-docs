---
url: https://docs.cloud.google.com/load-balancing/docs/https/http-load-balancing-best-practices/
title: External Application Load Balancer performance best practices \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:41.958078+00:00
---

# External Application Load Balancer performance best practices  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/http-load-balancing-best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  External Application Load Balancer performance best practices Stay organized with collections  Save and categorize content based on your preferences. 

[Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) provides mechanisms to distribute user traffic to multiple instances of an application. They do this by spreading the load across application instances and delivering optimal application performance to end users. This page describes some best practices to ensure that the load balancer is optimized for your application. To ensure optimal performance, we recommend benchmarking your application's traffic patterns.

## Place backends close to clients

The closer your users or client applications are to your workloads (load balancer backends), the lower the network latency between them. Therefore, create your load balancer backends in the region closest to where you anticipate your users' traffic to arrive at the Google frontend. In many cases, running your backends in multiple regions is necessary to minimize latency to clients in different parts of the world.

For more information, see the following topics:

  * [Traffic distribution for external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https#load_distribution_algorithm)
  * [Best practices for Compute Engine region selection](https://docs.cloud.google.com/solutions/best-practices-compute-engine-region-selection)



## Enable caching with Cloud CDN

Turn on Cloud CDN and caching as part of your default, global external Application Load Balancer configuration. For more information, see [Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview).

When you enable Cloud CDN, it might take a few minutes before responses begin to be cached. Cloud CDN caches only responses with [cacheable content](https://docs.cloud.google.com/cdn/docs/caching#cacheability). If responses for a URL aren't being cached, check which response headers are being returned for that URL, and how cacheability is [configured](https://docs.cloud.google.com/cdn/docs/using-cache-modes) for your backend. For more details, see [Cloud CDN troubleshooting](https://docs.cloud.google.com/cdn/docs/troubleshooting-steps#responses-not-cached).

## Forwarding rule protocol selection

  * **For the global external Application Load Balancer and the classic Application Load Balancer** , we recommend HTTP/3 which is an internet protocol built on top of [IETF QUIC](https://datatracker.ietf.org/doc/rfc9000/). HTTP/3 is enabled by default in all major browsers, [Android Cronet](https://developer.android.com/guide/topics/connectivity/cronet), and [iOS](https://developer.apple.com/documentation/technotes/tn3102-http3-in-your-app). To use HTTP/3 for your applications, ensure that UDP traffic is not blocked or rate-limited on your network and that HTTP/3 was not previously [disabled on your global external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https#QUIC). Clients that don't yet support HTTP/3, such as older browsers or networking libraries, won't be impacted. For more information, see [HTTP/3 QUIC](https://cloud.google.com/blog/products/networking/cloud-cdn-and-load-balancing-support-http3).

  * **For the regional external Application Load Balancer** , we support HTTP/1.1, HTTPS, and HTTP/2. Both HTTPS and HTTP/2 require some upfront overhead to set up TLS.




## Backend service protocol selection

Your choice of backend protocol (HTTP, HTTPS, or HTTP/2) impacts application latency and the network bandwidth available for your application. For example, using HTTP/2 between the load balancer and the backend instance can require significantly more TCP connections to the instance than HTTP(S). Connection pooling, an optimization that reduces the number of these connections with HTTP(S), is not available with HTTP/2. As a result, you might see high backend latencies because backend connections are made more frequently.

The backend service protocol also impacts how the traffic is [encrypted in transit](https://docs.cloud.google.com/docs/security/encryption-in-transit#how_traffic_gets_routed). With external HTTP(S) load balancers, all traffic going to backends that reside within Google Cloud VPC networks is automatically encrypted. This is called automatic network-level encryption. However, automatic network-level encryption is only available for communications with instance groups and zonal NEG backends. For all other backend types, we recommend you use secure protocol options such as HTTPS and HTTP/2 to encrypt communication with the backend service. For details, see [Encryption from the load balancer to the backends](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates/encryption-to-the-backends#encryption-to-backends).

## Recommended connection duration

Network conditions change and the set of backends might change based on load. For applications which generate a lot of traffic to a single service, a long running connection isn't always an optimal setup. Instead of using a single connection to the backend indefinitely, we recommend that you choose a maximum connection lifetime (for example, between 10 and 20 minutes) and/or a maximum number of requests (for example, between 1000 and 2000 requests), after which a new connection is used for new requests. The old connection is closed when all active requests using it are done.

This lets the client application benefit from changes in the set of backends, which include the load balancer's proxies and any network reoptimization that's required to serve the clients.

## Balancing mode selection criteria

For better performance, consider choosing the backend group for each new request based on which backend is the most responsive. This can be achieved by using the `RATE` balancing mode. In this case, the backend group with the lowest average latency over recent requests, or, for HTTP/2 and HTTP/3, the backend group with the fewest outstanding requests, is chosen.

The `UTILIZATION` balancing mode applies only to instance group backends and distributes traffic based on the utilization of VM instances in an instance group.

## Configure session affinity

In some cases, it might be beneficial for the same backend to handle requests that are from the same end users, or related to the same end user, at least for a short period of time. This can be configured by using _session affinity_ , a setting configured on the backend service. Session affinity controls the distribution of new connections from clients to the load balancer's backends. You can use session affinity to ensure that the same backend handles requests from the same resource, for example, related to the same user account or from the same document.

Session affinity is specified for the entire backend service resource, and not on a per backend basis. However, a URL map can point to multiple backend services. Therefore, you don't have to use just one session affinity type for the load balancer. Depending on your application, you can use different backend services with different session affinity settings. For example, if a part of your application is serving static content to many users, it is unlikely to benefit from session affinity. You would use a [Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview)-enabled backend service to serve cached responses instead.

For more information, see [session affinity](https://docs.cloud.google.com/load-balancing/docs/backend-service#session_affinity).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
