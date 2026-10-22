---
url: https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts/
title: Serverless network endpoint groups overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:13.922052+00:00
---

# Serverless network endpoint groups overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Serverless network endpoint groups overview Stay organized with collections  Save and categorize content based on your preferences. 

A network endpoint group (NEG) specifies a group of backend endpoints for a load balancer. A _serverless NEG_ is a backend that points to a [Cloud Run](https://docs.cloud.google.com/run/docs), [App Engine](https://docs.cloud.google.com/appengine/docs), [Cloud Run functions](https://docs.cloud.google.com/functions/docs), or [API Gateway](https://docs.cloud.google.com/api-gateway/docs) resource.

A serverless NEG can represent one of the following:

  * A Cloud Run resource or a group of resources.
  * A Cloud Run function or group of functions (formerly Cloud Run functions 2nd gen).
  * A Cloud Run function (1st gen) or group of functions
  * An App Engine standard environment or App Engine flexible environment app, a specific service within an app, a specific version of an app, or a group of services.
  * An API Gateway that provides access to your services through a [REST API](https://docs.cloud.google.com/compute/docs/reference/rest/beta/globalNetworkEndpointGroups) consistent across all services, regardless of service implementation. This capability is in **Preview**.

**Important:** For a group of resources to be in the same serverless NEG, they must have a common URL pattern.

## Supported load balancers

The following table lists the serverless products supported by each Application Load Balancer. Serverless NEGs are not supported by proxy Network Load Balancers and passthrough Network Load Balancers.

Serverless NEG type | Application Load Balancers  
---|---  
Regional  
internal | Cross-region  
internal | Global  
external | Classic | Regional  
external  
**Cloud Run** Supports Cloud Run and Cloud Run functions (2nd gen) |  |  |  |  |   
**App Engine** |  |  |  |  |   
**Cloud Functions** Supports Cloud Run functions (1st gen), formerly known as Cloud Functions 1st gen |  |  |  |  |   
  
## Use cases

When your load balancer is enabled for serverless apps, you can do the following:

  * Configure your serverless app to serve from a dedicated IPv4 IP address that is not shared with other services.
  * Map a single URL to multiple serverless functions or services that serve at the same domain. In this document, see URL masks.
  * Share URL space with other Google Cloud compute platforms. By using multiple backend services, a single load balancer can send traffic to multiple backend types. The load balancer selects the correct backend service based on the host or path of the request URL.
  * Reuse the same SSL certificates and private keys that you use for Compute Engine, Google Kubernetes Engine, and Cloud Storage. Reusing the same certificates eliminates the need to manage separate certificates for serverless apps.



### Global external Application Load Balancer and classic Application Load Balancer

Setting up a [global external Application Load Balancer or a classic Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https#load-balancer-mode) enables your serverless apps to integrate with existing cloud services. You can do the following:

  * Protect your service with [Google Cloud Armor](https://docs.cloud.google.com/armor), an edge DDoS defense and WAF security product available to all services accessed through an external Application Load Balancer. There are some limitations associated with this capability, especially for Cloud Run and App Engine.
  * Enable your service to optimize delivery using [Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview). Cloud CDN caches content close to your users. Cloud CDN provides capabilities like cache invalidation and Cloud CDN signed URLs.
  * Use Google's Edge infrastructure to terminate user's HTTP(S) connections closer to the user, thus decreasing latency.



To learn how to configure a load balancer with a serverless compute backend, see the following documentation:

  * [Set up a global external Application Load Balancer with Cloud Run, App Engine, or Cloud Run functions](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-serverless)
  * [Set up a classic Application Load Balancer with Cloud Run, App Engine, or Cloud Run functions](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-serverless)



Integrating an external Application Load Balancer with API Gateway enables your serverless backends to take advantage of all the features provided by Cloud Load Balancing. For more information, see [External Application Load Balancer for API Gateway](https://docs.cloud.google.com/api-gateway/docs/gateway-load-balancing). To configure an external Application Load Balancer to route traffic to an API Gateway, see [Getting started with an external Application Load Balancer forAPI Gateway](https://docs.cloud.google.com/api-gateway/docs/gateway-serverless-neg). This capability is in **Preview**.

### Regional external Application Load Balancer

Using a [regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https#load-balancer-mode) lets you run workloads with regulatory or compliance requirements on Cloud Run or Cloud Run functions (2nd gen) backends. For example, if you require that your application's network configurations and traffic termination reside in a specific region, a regional external Application Load Balancer is often the preferred option to comply with the necessary jurisdictional controls.

To learn how to configure a regional external Application Load Balancer with a serverless compute backend, see [Set up a regional external Application Load Balancer with Cloud Run](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-serverless).

### Regional internal Application Load Balancer and cross-region internal Application Load Balancer

When an internal Application Load Balancer is configured with Cloud Run or Cloud Run functions (2nd gen) backends, you can do the following:

  * Enable [advanced traffic management features](https://docs.cloud.google.com/load-balancing/docs/features#routing_and_traffic_management) such as fault injection, header rewrites, redirects, traffic splitting, and more, for your Cloud Run and Cloud Run functions (2nd gen) services.
  * Seamlessly migrate legacy services from Compute Engine, GKE, or on-premises, to Cloud Run and Cloud Run functions (2nd gen) to take advantage of weight-based traffic splitting to gradually shift traffic to Cloud Run without any downtime.
  * Protect your [Cloud Run and Cloud Run functions (2nd gen) services with VPC Service Controls](https://docs.cloud.google.com/run/docs/securing/using-vpc-service-controls).
  * Establish a single, policy-enforcing internal ingress point for your services running in Cloud Run, Cloud Run functions (2nd gen), Compute Engine, and GKE.



To learn how to configure a regional internal Application Load Balancer with a serverless compute backend, see [Set up a regional internal Application Load Balancer with Cloud Run](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal-serverless).

The rest of this page discusses how to use serverless NEGs with your Application Load Balancers. For more information about other types of NEGs, see [Network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs).

## Endpoint types

Serverless NEGs don't have any network endpoints such as ports or IP addresses. They can only point to an existing [Cloud Run](https://docs.cloud.google.com/run/docs), [App Engine](https://docs.cloud.google.com/appengine/docs), [API Gateway](https://docs.cloud.google.com/api-gateway/docs), or [Cloud Run functions](https://docs.cloud.google.com/functions/docs) resource residing in the same region as the NEG.

When you create a serverless NEG, you specify the fully qualified domain name (FQDN) of the Cloud Run, App Engine, API Gateway, or Cloud Run functions resource. The endpoint is of type `SERVERLESS`. Other endpoint types are not supported in a serverless NEG.

A serverless NEG can't have more than one endpoint. The endpoint points to either a serverless application or a URL mask. The load balancer serves as the frontend for the serverless compute application and proxies traffic to the specified endpoint. However, if the backend service contains multiple serverless NEGs in different regions, the load balancer sends traffic to the NEG in the closest region to minimize request latency.

## Network tier

For global external Application Load Balancers, you can use a serverless NEG in a load balancer using either Standard or Premium Network Service Tiers. The Premium Tier is required only if you want to set up serverless NEGs in multiple regions.

Regional external Application Load Balancers are always Standard Tier.

Cross-region internal Application Load Balancers and regional internal Application Load Balancers are always Premium tier.

## Load balancing components

A load balancer using a serverless NEG backend requires special configuration only for the backend service. The frontend configuration is the same as any other proxy-based Google Cloud load balancer. Additionally, internal Application Load Balancers require a [proxy-only subnet](https://docs.cloud.google.com/load-balancing/docs/l7-internal#proxy-only_subnet) to run Envoy proxies on your behalf.

The following diagrams show a sample serverless NEG deployment.

###  Global external 

This diagram shows how a serverless NEG fits into a global external Application Load Balancer architecture.

[ ![Global external Application Load Balancer for serverless apps.](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-simple-ext-https.svg)](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-simple-ext-https.svg) Global external Application Load Balancer for serverless apps (click to enlarge).

###  Regional external 

This diagram shows how a serverless NEG fits into a regional external Application Load Balancer architecture.

[ ![Regional external Application Load Balancer for serverless apps.](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-simple-reg-ext-https.svg)](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-simple-reg-ext-https.svg) Regional external Application Load Balancer for serverless apps (click to enlarge).

###  Regional internal 

This diagram shows how a serverless NEG fits into the regional internal Application Load Balancer model.

[ ![Regional internal Application Load Balancer for serverless apps.](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-simple-int-https.svg)](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-run-int-https.svg) Regional internal Application Load Balancer for serverless apps (click to enlarge).

###  Cross-region 

This diagram shows how a serverless NEG fits into the cross-region internal Application Load Balancer model.

[ ![Cross-region internal Application Load Balancer with Cloud Run deployment.](https://docs.cloud.google.com/static/load-balancing/images/cross-reg-int-cloudrun.svg)](https://docs.cloud.google.com/static/load-balancing/images/cross-reg-int-cloudrun.svg) Cross-region internal Application Load Balancer with Cloud Run deployment (click to enlarge).

### Frontend components

No special frontend configuration is required for load balancing with serverless NEG backends. [Forwarding rules](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) are used to route traffic by IP address, port, and protocol to a target proxy. The [target proxy](https://docs.cloud.google.com/load-balancing/docs/target-proxies) then terminates connections from clients.

[URL maps](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts) are used by Application Load Balancers to set up URL-based routing of requests to the appropriate backend services.

For more details on each of these components, refer the architecture sections of the specific load balancer overviews:

  * [External Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https#component)
  * [Internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal#components)



### Backend service

Backend services provide configuration information to the load balancer. Load balancers use the information in a backend service to direct incoming traffic to one or more attached backends. Serverless NEGs can be used as backends for certain load balancers.

The following restrictions apply depending on the type of load balancer:

  * A global backend service used by global external Application Load Balancers can have several serverless NEGs attached to it, but only one serverless NEG _per region_.
  * A regional backend service used by regional internal Application Load Balancers and regional external Application Load Balancers can only have one serverless NEG attached to it.
  * A global backend service used by cross-region internal Application Load Balancers can only have Cloud Run and Cloud Run functions (2nd gen) resources attached to it.



Each serverless NEG can point to either of the following:

  * The FQDN for a single resource
  * A _URL mask_ that points to multiple resources that serve at the same domain



A URL mask is a URL schema template that tells the serverless NEG backend how to map the user request to the correct service. URL masks are useful if you are using a custom domain for your serverless application and have multiple services serving at the same domain. Instead of creating a separate serverless NEG for each resource, you can create the NEG with a generic URL mask for the custom domain. For more information and examples, see [URL masks](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#url_masks).

For additional restrictions when adding a serverless NEG as a backend, see [Limitations](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#limitations).

#### Outlier detection for serverless NEGs

Outlier detection is an optional configuration that can be enabled on a global backend service that has serverless NEGs attached to it. The outlier detection analysis is only available for a cross-region internal Application Load Balancer, global external Application Load Balancer, and not for a classic Application Load Balancer. The outlier detection analysis identifies unhealthy serverless NEGs based on their HTTP response patterns, and reduces the error rate by routing most new requests from unhealthy resources to healthy resources. To learn how the outlier detection algorithm works and understand its limitations, see the following example.

Assume that there is a backend service with two serverless NEGs attached to it—one in the `REGION_A` region and another in the `REGION_B` region. If the serverless NEG that serves as a backend to a global external Application Load Balancer in the `REGION_A` region is not responsive, outlier detection identifies the serverless NEG as unhealthy. Based on outlier detection analysis, some of the new requests are then sent to the serverless NEG in the `REGION_B` region.

Based on the type of server error that is encountered, you can use one of the following outlier detection methods to enable outlier detection:

  * **Consecutive 5xx errors.** A `5xx` series HTTP status code qualifies as an error.
  * **Consecutive gateway errors.** Only `502`, `503`, and `504` HTTP status codes qualify as an error.



Note that even after enabling outlier detection, you'll likely see some requests being sent to the unhealthy resource and thus returning 5XX errors to the clients. This is because results of the outlier detection algorithm (ejection of endpoints from the load balancing pool and returning them back to the pool) are executed independently by each proxy instance of the load balancer. In most cases, more than one proxy instance handles the traffic received by a backend service. Thus, it is possible that an unhealthy endpoint is detected and ejected by only some of the proxies, and while this happens, other proxies may continue to send requests to the same unhealthy endpoint.

To reduce error rates further, you can configure more aggressive outlier detection parameters. We recommend configuring higher values for the ejection thresholds (`outlierDetection.baseEjectionTime`). For example, our tests show that setting `outlierDetection.baseEjectionTime` to 180 seconds with a sustained QPS of higher than 100 results in less than 5% observed error rates. To learn more about the outlier detection API, see [`outlierDetection`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices#BackendService.FIELDS.outlier_detection) in the [global backend service API documentation](https://docs.cloud.google.com/compute/docs/reference/rest/v1/backendServices).

The following `outlierDetection` fields are not supported when the backend service has a serverless NEG attached to it:

  * `outlierDetection.enforcingSuccessRate`
  * `outlierDetection.successRateMinimumHosts`
  * `outlierDetection.successRateRequestVolume`
  * `outlierDetection.successRateStdevFactor`



To learn how to configure outlier detection, see [Set up a global external Application Load Balancer with a serverless backend: Enable outlier detection](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-serverless#outlier_detection).

**Note:** Outlier detection analysis for serverless NEGs can't be configured on backend services that have Identity-Aware Proxy (IAP) enabled. This is because the outlier detection analysis process on an IAP-enabled backend service can't identify unhealthy serverless resources. As a result, it can't route new requests to a healthy serverless resource.

### URL masks

A serverless NEG backend can point to either a single Cloud Run (or App Engine or Cloud Run functions if applicable) resource, or a _URL mask_ that points to multiple resources. A URL mask is a template of your URL schema. The serverless NEG uses this template to map the request to the appropriate resource.

URL masks are an optional feature that make it easier to configure serverless NEGs when your serverless application is comprised of multiple Cloud Run, Cloud Run functions, or App Engine resources. Serverless NEGs used with internal Application Load Balancers can only use a URL mask that points to Cloud Run or Cloud Run functions (2nd gen) services.

URL masks are useful if your serverless app is mapped to a custom domain rather than the default address that Google Cloud provides. With a custom domain such as `example.com`, you could have multiple resources deployed to different subdomains or paths on the same domain. In such cases, instead of creating a separate serverless NEG backend for each resource, you can create a single serverless NEG with a generic URL mask for the custom domain (for example, `example.com/<service>`). The NEG extracts the service name from the request's URL.

The following illustration shows an external Application Load Balancer with a single backend service and serverless NEG that uses a URL mask to map user requests to different services.

[ ![Distributing traffic to serverless apps.](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-url-mask.svg)](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-url-mask.svg) Using a URL mask to distribute traffic to different services (click to enlarge).

URL masks work best when your application's resources use a predictable URL schema. The advantage of using a URL mask instead of a URL map is that you don't need to create separate serverless NEGs for the `login` and `search` services. You also don't need to modify your load balancer configuration each time you add a new resource to your application.

## Limitations

  * A serverless NEG can't have any network endpoints such as IP address or port.
  * Serverless NEGs can point only to serverless resources residing in the same region where the NEG is created.
  * For a load balancer that is using a Serverless NEG backend, the serverless NEG must be created in the same project as the backing Cloud Run, App Engine, API Gateway, or Cloud Run functions resources pointed to by the NEG. You might see requests failing if you connect a service that is not in the same project as the serverless NEG.
  * Unless you have configured [Cloud Run service health](https://docs.cloud.google.com/run/docs/multiple-regions#service-health) or enabled outlier detection, a load balancer configured with a serverless NEG can't detect whether the underlying resource is working as expected. This means that even if your resource is returning errors, the load balancer continues to direct traffic to it. Make sure to thoroughly test new versions of your resources before routing user traffic to them.

To automate traffic failover away from unhealthy serverless NEGs, you can use the following methods on global and cross-region load balancers:

    * _Outlier detection_ : Supported on global external Application Load Balancers and cross-region internal Application Load Balancers to identify unhealthy serverless NEGs based on HTTP response patterns.
    * _Cloud Run service health_ : Supported on global external Application Load Balancers and cross-region internal Application Load Balancers configured with serverless NEG backends.
  * **Google Cloud console**. You can only create serverless NEGs while you are creating or editing a load balancer by using the [**Load balancing** page in the Google Cloud console](https://console.cloud.google.com/projectselector2/net-services/loadbalancing/list). While you can't create or edit serverless NEGs on the [**Network endpoint groups** page](https://console.cloud.google.com/projectselector2/compute/networkendpointgroups/list), you can use this page to see a list of all the serverless NEGs in your project.




### Limitations with backend services

The following limitations apply to backend services that have a serverless NEG backend:

  * A global backend service used by global external Application Load Balancers can have only one serverless NEG _per region_. To combine multiple serverless NEGs in a single backend service, all the NEGs must represent functionally equivalent deployments in different regions. For example, the NEGs can point to the same Cloud Run, App Engine, or Cloud Run functions resource deployed in different regions.
  * A global backend service used by cross-region internal Application Load Balancers can have only one Cloud Run or Cloud Run functions (2nd gen) resource attached to it.
  * A regional backend service can only have one serverless NEG attached to it.
  * [Cross-project service referencing](https://docs.cloud.google.com/load-balancing/docs/https#cross-project) in a Shared VPC deployment is supported with configurations that contain a serverless NEG. To use this feature, you create the load balancer's frontend components (IP address, forwarding rule, target proxy, and URL map) in a project different from load balancer's backend components (backend service and serverless NEGs). Note that the backend service, associated serverless NEGs, and the backing serverless resource (Cloud Run, App Engine, API Gateway, or Cloud Run functions), must always be created in the same project.
  * The [backend service timeout setting](https://docs.cloud.google.com/load-balancing/docs/backend-service#timeout-setting) does not apply to backend services with serverless NEG backends. Attempting to modify the backend service's `resource.timeoutSec` property results in the following error: `Timeout sec is not supported for a backend service with Serverless network endpoint groups`.  
For backend services with serverless NEG backends, the default timeout is 60 minutes. This timeout is not configurable. If your application needs long-running connections, configure your clients to retry requests on failure.
  * All serverless NEGs combined in a backend service must also use the same type of backend. This means Cloud Run serverless NEGs can only be combined with other Cloud Run serverless NEGs, and App Engine serverless NEGs can only be combined with App Engine serverless NEGs.
  * You can't mix serverless NEGs with other types of NEGs in the same backend service. For example, you can't route to a GKE cluster and a Cloud Run service from the same backend service.
  * When setting up backend services that route to serverless NEGs, certain fields are restricted: 
    * You can't specify a balancing mode. That is, the `RATE`,`UTILIZATION`, and `CONNECTION` values have no effect on the load balancer's traffic distribution.
    * Health checks are not supported for serverless backends. Therefore, backend services that contain serverless NEG backends can't be configured with health checks. However, you can optionally enable outlier detection to identify unhealthy serverless resources and route new requests to a healthy serverless resource.
  * You can't use the [`gcloud compute backend-services edit`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/edit) command to modify a backend service with a serverless NEG backend. As a workaround, use the [`gcloud compute backend-services update`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/backend-services/update) command instead.



Additional limitations apply depending on the type of load balancer and the serverless backend.

### Limitations with regional internal Application Load Balancers and regional external Application Load Balancers

  * Serverless NEGs used with regional internal Application Load Balancers or regional external Application Load Balancers can only point to Cloud Run or Cloud Run functions (2nd gen) resources.
  * For projects that are using serverless NEGs, the queries per second (QPS) limit is 5000 QPS per project for traffic sent to any serverless NEGs configured with regional external Application Load Balancers or regional internal Application Load Balancers. This limit is aggregated across all regional external Application Load Balancers and regional internal Application Load Balancers in the project. This is not a per load balancer limit.



### Limitations with cross-region internal Application Load Balancers

  * Serverless NEGs used with cross-region internal Application Load Balancers can only point to Cloud Run or Cloud Run functions (2nd gen) resources.



### Limitations with global external Application Load Balancers

This sections lists the limitations you'll encounter when configuring serverless NEGs with global external Application Load Balancers.

#### Limitations with Cloud Run

  * An external Application Load Balancer with serverless NEGs does not support Knative serving.
  * External Application Load Balancers don't support [authenticating end-user requests](https://docs.cloud.google.com/run/docs/authenticating/end-users) to Cloud Run resources. However, you can use [IAP to authenticate users within your organization](https://docs.cloud.google.com/iap/docs/enabling-cloud-run). If you want to enable IAP, you should remember that IAP and Cloud CDN are incompatible with each other. They can't be enabled on the same backend service.



#### Limitations with App Engine

  * Multi-region load balancing is not supported with App Engine. This is because App Engine requires 1 region per project.
  * If you're using IAP, you must use the same OAuth client ID for all App Engine services associated with a single load balancer.
  * Only one IAP policy is allowed on the request path. For example, if you have already set an IAP policy in the backend service, you shouldn't set another IAP policy on the App Engine app.
  * Global external Application Load Balancers with both App Engine flexible environment backends and App Engine standard environment backends don't support [cross-project service referencing](https://docs.cloud.google.com/load-balancing/docs/https#cross-project). 


  * We recommend that you [use ingress controls](https://docs.cloud.google.com/appengine/docs/standard/application-security#ingress_controls) so that your app only receives requests sent from the load balancer (and the VPC if you use it). Otherwise, users can use your app's App Engine URL to bypass the load balancer, Cloud Armor security policies, SSL certificates, and private keys that are passed through the load balancer.



#### Limitations with API Gateway

For more information, see [Limitations on serverless NEGs and API Gateway](https://docs.cloud.google.com/api-gateway/docs/gateway-load-balancing#limitations_on_serverless_negs_and).

#### Limitations with traffic management features

  * [Advanced traffic management](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global#traffic_policies) features like load balancing locality policy and session affinity aren't supported with serverless NEG backends.
  * Specifying a [session affinity](https://docs.cloud.google.com/load-balancing/docs/backend-service#session_affinity) on a backend service with a serverless NEG backend won't work. As a workaround for Cloud Run, use its specific [session affinity](https://docs.cloud.google.com/run/docs/configuring/session-affinity#set_session_affinity) feature.



## Pricing

For pricing information, see [Network pricing: Cloud Load Balancing](https://cloud.google.com/vpc/network-pricing#cloud-load-balancing).

## What's next

  * [Set up a global external Application Load Balancer with Cloud Run, App Engine, or Cloud Run functions](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-serverless)
  * [Set up a classic Application Load Balancer with Cloud Run, App Engine, or Cloud Run functions](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-serverless)
  * [Set up a regional external Application Load Balancer with a Cloud Run backend](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-serverless)
  * [Set up a regional internal Application Load Balancer with a Cloud Run backend](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal-serverless)
  * [Set up a cross-region internal Application Load Balancer with Cloud Run](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-serverless)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
