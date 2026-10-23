---
url: https://docs.cloud.google.com/load-balancing/docs/https/migrate-to-global/
title: Migration overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:25:51.522111+00:00
---

# Migration overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/migrate-to-global/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Migration overview Stay organized with collections  Save and categorize content based on your preferences. 

This page gives you an overview of the differences between the global external Application Load Balancer and classic Application Load Balancer, and a detailed overview of how you can migrate your existing classic Application Load Balancer resources to the global external Application Load Balancer.

To take advantage of the [advanced traffic management](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global) features of the global external Application Load Balancer, we recommend that you migrate your classic Application Load Balancer resources to the global external Application Load Balancer infrastructure.

## Compare classic Application Load Balancers and global external Application Load Balancers

Before you migrate resources, understand the differences between classic Application Load Balancers and global external Application Load Balancers.

### Feature differences

The following features are not supported with the global external Application Load Balancer. They are only available with the classic Application Load Balancer:

  * [Standard Network Tier](https://docs.cloud.google.com/network-tiers/docs/overview)
  * [GKE Ingress controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress)

To deploy global external Application Load Balancers for GKE clusters, use the [GKE Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api) instead. For setup instructions, see [Deploying Gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways).




### Data plane differences

The following table highlights differences in the data plane between the classic Application Load Balancer and the global external Application Load Balancer. These differences affect how the load balancers respond to some common events.

**Event** | **Classic Application Load Balancer response** | **Global external Application Load Balancer response**  
---|---|---  
**Status/error codes**  
All backends are unhealthy  | Returns HTTP 502  | Returns HTTP 503   
Request uses a banned SSL cipher  | Returns HTTP 502  | Returns HTTP 503   
Early upstream connection reset by the backend  | Returns HTTP 502 | Returns HTTP 503   
Failed connection upgrade (for example, while upgrading to Websockets)  | Returns HTTP 400  | Returns HTTP 403   
Header is too large  | Returns HTTP 413  | Returns HTTP 431   
**Quotas and limits**  
URL map configuration | There are significant differences in the URL map configuration limits between the two load balancers. For details, see the [Quotas: URL maps](https://docs.cloud.google.com/load-balancing/docs/quotas#url_maps) documentation.  
**Header handling**  
Request uses a custom HTTP method with no body  | Adds the `Transfer Encoding: Chunked` header to request sent to backend  | Adds the `Content-Length: 0` header to request sent to backend   
Format of the `X-Forwarded-For` header added to requests sent to backend  | Uses '`, `' delimiter between IPs  | Uses '`,`' delimiter between IPs (no space after the comma)   
Header case preservation  | Header case is preserved  | All header keys are transformed to lowercase   
Repeated headers with the same name | Allowed | Repeated headers may be combined into a single header, with the values appended in order and comma separated, as allowed by [RFC 7230](https://www.rfc-editor.org/rfc/rfc7230).  
**(HTTP/1.1 only)** Invalid header name (for example, unsupported characters in header)  | Allowed (for HTTP/1.1)  | Returns HTTP 502 (for HTTP/1.1)   
**(HTTP/1.1 only)** Repeated (but same) `Content-Length` header in request  | Allowed (for HTTP/1.1)  | Returns HTTP 502 (for HTTP/1.1)   
**(HTTP/1.1 only)** Multiple hosts in header | When 2 or more hosts are added, and the first one is valid, the header is accepted  | When 2 or more hosts are added, and any are invalid, the load balancer returns HTTP 502  
**(HTTP/1.1 only)** `Connection: Keep-Alive` header  | Adds the `Keep-Alive header` in requests sent to backend by default  | Does not add this header by default   
**Request handling**  
Backwards slashes in request | URL left unchanged  | Converts to forward slash   
Merge duplicate slashes in request | Leaves slashes unmerged  | Merges slashes   
`#` in request path  | Allowed  | Returns HTTP 400   
**(HTTP/1.1 only)** Illegal characters in request path (for example, `\\\x7f\\\x7f`) | Allowed (for HTTP/1.1)  | Returns HTTP 502 (for HTTP/1.1)  
**Traffic distribution (URL map configuration)**  
Client request includes a port number | The port number is ignored even if you have configured hosts with ports in the URL map. Only the hostname is considered. For example, requests for `example.com:5000` are matched to the backend service for `example.com`.  | Both the hostname and the port number are considered. For example, requests for `example.com:5000` are matched to the backend service for `example.com:5000`. If there isn't a match, the default backend service is used.   
  
Due to architectural differences, when migrating to the global external Application Load Balancer, you might see an increase in the number of connections to your backends, especially when using the HTTP/1.1 protocol. This can lead to increased memory consumption on the backend instances. Monitor your backend resource usage during and after migration. 

To learn more about the differences and supported features, see [Load balancer feature comparison](https://docs.cloud.google.com/load-balancing/docs/features) and [Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer).

## Migrate from classic to global external Application Load Balancer

To migrate to the global external Application Load Balancer, you change the load balancing scheme of your load balancing resources—specifically, the backend services and forwarding rules—from `EXTERNAL` to `EXTERNAL_MANAGED`. To do this, you perform a series of migration steps where you can test parts of your network traffic with the new load balancing scheme before actually finalizing the migration. During resource migration, you control what percentage of requests is sent to either the classic Application Load Balancer infrastructure or the global external Application Load Balancer infrastructure.

The following diagram shows the load balancing schemes of your load balancing resources before and after the migration.

[ ![Migration process for classic Application Load Balancer resources.](https://docs.cloud.google.com/static/load-balancing/images/classic-global-migration.svg)](https://docs.cloud.google.com/static/load-balancing/images/classic-global-migration.svg) Migration process for classic Application Load Balancer resources (click to enlarge).

In the previous diagram, note the following:

  * Before resources are migrated, all requests use the classic Application Load Balancer infrastructure.
  * While the resources are migrated, some requests are sent to the global external Application Load Balancer infrastructure and the remaining requests are sent to the classic Application Load Balancer infrastructure.
  * After resources are migrated, all requests use the global external Application Load Balancer infrastructure.



To help ensure a smooth transition, migrate the following classic Application Load Balancer resources in the specified order:

  1. Migrate all backend services attached to the load balancer's forwarding rules.

  2. Migrate all backend buckets attached to the load balancer's forwarding rules. You do this at the forwarding rule level because backend buckets don't have load balancing schemes.

  3. Migrate the load balancer's forwarding rules.

You can only migrate a forwarding rule after all the backend services and backend buckets attached to the forwarding rule have already been migrated.




### Migration states

You migrate resources by setting them to different states before changing their load balancing scheme to `EXTERNAL_MANAGED`.

  1. `PREPARE`: set a resource to this state to prepare it for migration.
  2. `TEST_BY_PERCENTAGE`: to test a prepared resource, set the resource to this state to send a percentage of the network traffic. This stage is optional.
  3. `TEST_ALL_TRAFFIC`: set a resource to this state to send all network traffic to the resource through the global external Application Load Balancer infrastructure instead of the classic Application Load Balancer infrastructure.

**Note:** After you change a resource's state from `PREPARE` to `TEST_BY_PERCENTAGE` or `TEST_ALL_TRAFFIC`, wait for some time (approximately six minutes) for the resource to be ready to accept traffic. The resource must be in the `TEST_ALL_TRAFFIC` state before you change the load balancing scheme.

### Migration process

To help ensure no downtime, you migrate resources in a specific order from the classic Application Load Balancer infrastructure to the global external Application Load Balancer infrastructure, and then change the load balancing scheme from `EXTERNAL` to `EXTERNAL_MANAGED` to finalize the migration.

  1. Migrate the load balancer's backend services.

Repeat the following steps for each backend service.

     1. Prepare the backend service for migration.

Before any traffic can be sent through the global external Application Load Balancer infrastructure, set the state of the backend service to `PREPARE`. This prepares the backend service to handle global external Application Load Balancer infrastructure network traffic. A backend service takes some time (approximately six minutes) to be ready to send traffic through the global external Application Load Balancer infrastructure.

     2. Optional: Test the prepared backend service.

After the backend service is in the `PREPARE` state, set its state to `TEST_BY_PERCENTAGE` and set a percentage of the classic Application Load Balancer network traffic to the global external Application Load Balancer infrastructure.

Though this stage is optional, we recommend that you test the traffic before migrating a backend service. Start with a small percentage value and monitor logs of the resources. If the backend service behaves as expected, gradually increase the percentage to 100%.

In the `TEST_BY_PERCENTAGE` state, you can't use the additional capabilities of the global external Application Load Balancer infrastructure.

     3. Send all classic Application Load Balancer network traffic to the prepared backend service.

After the testing of the backend service is successful, set its state to `TEST_ALL_TRAFFIC` and send all classic Application Load Balancer network traffic to the prepared backend service. A backend service takes some time (approximately six minutes) to be ready to handle the network traffic.

In the `TEST_ALL_TRAFFIC` state, you can't use the additional capabilities of the global external Application Load Balancer infrastructure.

     4. Change the load balancing scheme of migrated backend service to `EXTERNAL_MANAGED`.

After testing your prepared backend service on the global external Application Load Balancer infrastructure, change its load balancing scheme to `EXTERNAL_MANAGED`. A backend service takes some time (approximately six minutes) to be fully migrated. After the load balancing scheme of the backend service changes to `EXTERNAL_MANAGED`, you can use the advanced features of the global external Application Load Balancer infrastructure.

  2. Migrate the load balancer's backend buckets. You do this at the forwarding rule level because backend buckets don't have load balancing schemes.

Repeat the following steps for each bucket.

     1. Prepare the backend bucket for migration.

Before any traffic can be sent through the global external Application Load Balancer infrastructure, set the state of the backend bucket to `PREPARE`, and wait for some time (approximately six minutes).

     2. Optional: Test the prepared backend service.

After the backend bucket is in the `PREPARE` state, set its state to `TEST_BY_PERCENTAGE` and set a percentage of the classic Application Load Balancer network traffic to the global external Application Load Balancer infrastructure.

     3. Send all classic Application Load Balancer network traffic to the prepared backend bucket.

Set the state of the backend bucket to `TEST_ALL_TRAFFIC` and send all classic Application Load Balancer network traffic to it. A backend bucket takes some time (approximately six minutes) to be ready to handle the network traffic.

In the `TEST_ALL_TRAFFIC` state, you can't use the additional capabilities of the global external Application Load Balancer infrastructure.

  3. Migrate the forwarding rules.

For each forwarding rule, change the load balancing scheme of the forwarding rule to `EXTERNAL_MANAGED`, and wait for some time (approximately six minutes). After the load balancing scheme of the forwarding rule changes to `EXTERNAL_MANAGED`, you can use the advanced features of the global external Application Load Balancer infrastructure.




For a detailed step-by-step process, see [Migrate resources from classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/migrate-from-classic-global).

The following diagram shows the classic Application Load Balancer resources in the different states of migration.

[ ![Migration states of classic Application Load Balancer resources.](https://docs.cloud.google.com/static/load-balancing/images/classic-migration-states.svg)](https://docs.cloud.google.com/static/load-balancing/images/classic-migration-states.svg) Migration states of classic Application Load Balancer resources (click to enlarge).

After migrating a resource, if you want to roll it back to classic Application Load Balancer, change its load balancing scheme within 90 days of its migration. You can't roll back a resource after the 90-day window has passed.

### Using session affinity

Consider the following caveats when migrating classic Application Load Balancer backend services with session affinity:

  * Setting a value for `TEST_BY_PERCENTAGE` redirects some traffic targeting the classic Application Load Balancer to the global external Application Load Balancer. This breaks the [client IP affinity](https://docs.cloud.google.com/load-balancing/docs/backend-service#client_ip_affinity). Changing the migration percentage (for example, increasing it by 10%) breaks the session affinity for the same percentage of client IP addresses (10% in this example), until the affinity is re-established on the next request.

  * Setting a value for `TEST_BY_PERCENTAGE` redirects that percentage of traffic without a [session cookie](https://docs.cloud.google.com/load-balancing/docs/backend-service#generated_cookie_affinity) to the global external Application Load Balancer. It also redirects all traffic with a session cookie to the load balancer fleet that generated the cookie.

  * Setting a value for `TEST_BY_PERCENTAGE` to 0%, or leaving it unset, or setting the backend service to the `PREPARE` state, invalidates all existing cookies that are directed to the global external Application Load Balancer.

  * Changing the load balancing scheme of the backend service to `EXTERNAL_MANAGED` invalidates all cookies generated by the classic Application Load Balancer fleet. This lets you roll back traffic if there's an issue with your application using the global external Application Load Balancer. For example, if a client presents a cookie from the classic Application Load Balancer fleet, but the backend service scheme is `EXTERNAL_MANAGED`, the client's cookie is not honored. The global external Application Load Balancer ignores the cookie and creates a new one.




## Roll back migrated resources

After migrating a resource, if you want to roll it back from the global external Application Load Balancer infrastructure to the classic Application Load Balancer infrastructure, you can do so within 90 days of changing its load balancing scheme.

Rolling back a backend service to the `EXTERNAL` scheme requires rolling back the forwarding rule. Rolling back a forwarding rule to the `EXTERNAL` scheme doesn't require rolling back the backend services.

To roll back resources, follow these steps:

  1. Remove any new advanced traffic management features of global external Application Load Balancer configured on the resource.
  2. Roll back the forwarding rules.

Change the load balancing scheme of forwarding rules from `EXTERNAL_MANAGED` to `EXTERNAL`.

  3. Roll back the backend buckets.

     1. Set the migration state of backend buckets to `TEST_ALL_TRAFFIC`, and wait for some time (approximately six minutes).
     2. Optional: To decrease the traffic, set the migration state of backend buckets to `TEST_BY_PERCENTAGE` and set a percentage of the traffic.
     3. Set the migration state of backend buckets to `PREPARE`.
     4. Revert backend buckets to their pre-migration states.
  4. Roll back the backend services.

     1. Set the migration state of backend services to `TEST_ALL_TRAFFIC`, and wait for some time (approximately six minutes).
     2. Optional: To decrease the traffic, set the migration state of backend services to `TEST_BY_PERCENTAGE` and set a percentage of the traffic.
     3. Set the migration state of backend services to `PREPARE`.
     4. Revert backend services to their pre-migration states.



For a detailed step-by-step process, see [Roll back migrated resources to classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/roll-back-migrated-resources).

## Track your migration process

While migrating your resources, you can check their load balancing schemes by viewing the following:

  * The logging and monitoring dashboards of the global external Application Load Balancer. For more information, see [Global external Application Load Balancer logging and monitoring](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring).

  * The values of the following HTTP request and response headers:

    * `X-External-Managed-Migration-Scheme-Override`: this request header routes the request based on its value. If the header value is `EXTERNAL`, it directs the request to the classic Application Load Balancer infrastructure. If the value is `EXTERNAL_MANAGED`, it routes the request through the global external Application Load Balancer infrastructure.

Use this header to direct a request to a particular load balancer fleet.

    * `X-External-Managed-Migration-Selected-Scheme`: this request and response header informs the backend and the client about the load balancing scheme used to route the request. The header is returned to the client and passed to the customer's backend.

If the request is routed through the classic Application Load Balancer infrastructure, its value is `EXTERNAL`. If the request is routed through the global external Application Load Balancer infrastructure, its value is `EXTERNAL_MANAGED`.




## What's next

  * [Migrate resources from classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/migrate-from-classic-global)
  * [Roll back migrated resources to classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/roll-back-migrated-resources)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
