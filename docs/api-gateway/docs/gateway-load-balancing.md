---
url: https://docs.cloud.google.com/api-gateway/docs/gateway-load-balancing/
title: Load balancing for API Gateway \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:17.420175+00:00
---

# Load balancing for API Gateway  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/api-gateway/docs/gateway-load-balancing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ API Gateway ](https://docs.cloud.google.com/api-gateway/docs)
  * [ Guides ](https://docs.cloud.google.com/api-gateway/docs/secure-traffic-gcloud)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Load balancing for API Gateway

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The integration of [Global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) and [Classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) support for API Gateway enables your serverless backends to take advantage of all the features provided by Cloud Load Balancing. By combining API Gateway with a global external Application Load Balancer or classic Application Load Balancer using a [serverless Network Endpoint Group (serverless NEG)](https://docs.cloud.google.com/load-balancing/docs/negs), you can:

  * Host gateways with custom branded domains
  * Configure TLS for gateways using certificates issued by a preferred certificate authority
  * Create a common entry point for a gateway routing to multiple backends
  * Deploy gateways in multiple geographic regions for high availability without managing URLs for each region
  * Protect gateways with [Cloud Armor](https://docs.cloud.google.com/armor/docs)
  * Improve gateway response time by leveraging [Cloud CDN](https://docs.cloud.google.com/cdn/docs)



## Using a serverless NEG for API Gateway

A [network endpoint group (NEG)](https://docs.cloud.google.com/load-balancing/docs/negs) specifies a group of backend endpoints for a load balancer. A _serverless NEG_ is a backend that points to a Google-hosted serverless backend like [Cloud Run](https://docs.cloud.google.com/run/docs), [App Engine](https://docs.cloud.google.com/appengine/docs), or API Gateway. A serverless NEG backend for API Gateway can represent:

  * An API Gateway instance
  * A group of gateways configured with the same API config



The following figure shows how serverless NEGs can be used in the Cloud Load Balancing model:

![diagram of serverless neg as backend for multi-region gateways](https://docs.cloud.google.com/static/api-gateway/docs/images/serverless-neg-diagram.png)

As illustrated in an earlier example, a backend service can be managed by several serverless NEGs. Each serverless NEG can contain a single API Gateway instance or use a [URL mask](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#url_masks) to point to multiple gateways. Because all NEGs acting as a backend service are used for load balancing, they should represent functionally equivalent gateway deployments. For example, all NEGs should have the same API config deployed to each gateway in different regions. If a backend service contains several NEGs, the load balancer will balance traffic between these NEGs while minimizing request latency.

## Limitations on serverless NEGs and API Gateway

A few limitations should be considered when using serverless NEGs to integrate Cloud Load Balancing for API Gateway. Most notably:

  * Serverless NEGs cannot have any [Network Endpoints](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkEndpointGroups/attachNetworkEndpoints), such as IP addresses or ports, attached.
  * Serverless NEGs can only point to API Gateway instances residing in the same region where the NEG is created.
  * Serverless NEGs can only point to API Gateway instances created in the same project as the load balancer using the Serverless NEG backend.
  * API Gateway doesn't support Ingress control settings. As a result, there is no way to disable access to your API Gateway using a service-generated gateway URL and ensure that all traffic is handled by the load balancer.



For more information on restrictions pertaining to serverless NEGs and backend services generally, see [Limitations](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#limitations).

## Limitations on serverless NEGs in backend service configurations

A [backend service](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices) defines how Cloud Load Balancing distributes traffic. The backend service configuration contains a set of values, such as the protocol used to connect to backends, various distribution and session settings, health checks, and timeouts. For serverless NEGs used as a backend service for API Gateway, these settings provide fine-grained control over how your load balancer behaves.

The resource definition of a backend service has the following implications for your load balancing design:

  * Serverless NEGs cannot be used with other types of NEGs in the same backend service. For example, you cannot route to a GKE cluster and an API Gateway instance from the same backend service.
  * All serverless NEGs combined in a backend service must use the same type of backend. This means API Gateway serverless NEGs can only be combined with other API Gateway serverless NEGs, App Engine serverless NEGs can only be combined with App Engine serverless NEGs.
  * A backend service may only contain one Serverless NEG per region.



When defining a backend service configuration that routes to a serverless NEG, the following field limitations apply:

  * The `balancingMode` cannot be specified
  * The `healthCheck` field must be empty and cannot be specified
  * Ports cannot be specified
  * Only HTTP and HTTPS protocols are supported.
  * Values specified in `utilization` or `connection`-related fields are not supported.



The `IAP`, `cdnPolicy`, and `securityPolicy` fields in the backend service configuration are valid for serverless NEGs. These fields can be used to set up [Identity-Aware Proxy](https://docs.cloud.google.com/iap/docs), [Cloud CDN](https://docs.cloud.google.com/cdn/docs), and [Cloud Armor](https://docs.cloud.google.com/armor/docs) respectively with your API Gateway service.

## What's next?

  * Configure a load balancer with [Getting started with global external Application Load Balancer for API Gateway](https://docs.cloud.google.com/api-gateway/docs/gateway-serverless-neg)

  * Walk through [Creating multi-region deployments](https://docs.cloud.google.com/api-gateway/docs/multi-region-deployment) for API Gateway

  * Learn more about [Using custom domains](https://docs.cloud.google.com/api-gateway/docs/using-custom-domains)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
