---
url: https://docs.cloud.google.com/load-balancing/docs/https/use-cases/
title: External Application Load Balancer use cases \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:04:20.957623+00:00
---

# External Application Load Balancer use cases  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/use-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)



Send feedback 

#  External Application Load Balancer use cases Stay organized with collections  Save and categorize content based on your preferences. 

The external Application Load Balancers address many use cases. This page provides some high-level examples.

## Three-tier web services

You can use an external Application Load Balancer to support traditional three-tier web services. The following example shows how you can use three types of Google Cloud load balancers to scale three tiers. At each tier, the load balancer type depends on your traffic type:

  * **Web tier:** Traffic enters from the internet and is load balanced by using an [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https).

  * **Application tier:** The application tier is scaled by using a regional internal Application Load Balancer.

  * **Database tier:** The database tier is scaled by using an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/internal).




The diagram shows how traffic moves through the tiers:

  1. An external Application Load Balancer (the subject of this overview) distributes traffic from the internet to a set of web frontend instance groups in various regions.
  2. These web frontends send the HTTP(S) traffic to a set of regional, internal Application Load Balancers. For the external Application Load Balancer to forward traffic to an internal Application Load Balancer, the external Application Load Balancer must have backend instances with web server software (such as Netscaler or NGINX) configured to forward the traffic to the frontend of the internal Application Load Balancer.
  3. The internal Application Load Balancers distribute the traffic to middleware instance groups.
  4. These middleware instance groups send the traffic to internal passthrough Network Load Balancers, which load balance the traffic to data storage clusters.

[ ![Layer 7-based routing for internal tiers in a multitier app.](https://docs.cloud.google.com/static/load-balancing/images/ilb-l7-tiers.svg)](https://docs.cloud.google.com/static/load-balancing/images/ilb-l7-tiers.svg) Layer 7-based routing for internal tiers in a multitier app (click to enlarge).

## Multi-region load balancing

When you configure an external Application Load Balancer in Premium Tier, it uses a global external IP address and can intelligently route requests from users to the closest backend instance group or NEG, based on proximity. For example, if you set up instance groups in North America, Europe, and Asia, and attach them to a load balancer's backend service, user requests around the world are automatically sent to the VMs closest to the users, assuming the VMs pass health checks and have enough capacity (defined by the balancing mode). If the closest VMs are all unhealthy, or if the closest instance group is at capacity and another instance group is not at capacity, the load balancer automatically sends requests to the next closest region with capacity.

In Premium Tier, the external Application Load Balancer provides multi-region load balancing, using multiple backend services, each with backend instance groups or NEGs in multiple regions.

[ ![Representation of multiregion load balancing.](https://docs.cloud.google.com/static/load-balancing/images/https-load-balancer-diagram.svg)](https://docs.cloud.google.com/static/load-balancing/images/https-load-balancer-diagram.svg) Representation of multiregion load balancing (click to enlarge).

## Workloads with jurisdictional compliance

Some workloads with regulatory or compliance requirements require that network configurations and traffic termination reside in a specific region. For these workloads, a regional external Application Load Balancer is often the preferred option to provide the jurisdictional controls these workloads require.

## Advanced traffic management

With global external Application Load Balancers and regional external Application Load Balancers, you can add advanced traffic management capabilities that give you fine-grained control over how traffic is handled. These capabilities help you to meet your availability and performance objectives. One of the benefits of using external Application Load Balancers for these use cases is that you can update how traffic is managed without needing to modify your application code.

For more details, see the following:

  * [Traffic management overview for global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global).
  * [Traffic management overview for regional external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-regional).



## Load balancing with request routing

The external Application Load Balancer supports request routing by using URL maps to select a backend service based on the requested host name, request path, or both. For example, you can use a set of instance groups or NEGs to handle your video content and another set to handle everything else.

You can also use external Application Load Balancers with [Cloud Storage](https://docs.cloud.google.com/storage) [buckets](https://docs.cloud.google.com/storage/docs/json_api/v1/buckets). After you have your load balancer set up, you can [add Cloud Storage buckets](https://docs.cloud.google.com/load-balancing/docs/https/ext-load-balancer-backend-buckets) to it.

For more information, see [URL map concepts](https://docs.cloud.google.com/load-balancing/docs/url-map-concepts).

## Load balancing for GKE applications

There are two ways to deploy external Application Load Balancers for GKE clusters:

  * **[GKE Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).** Supported by the global external Application Load Balancer and the classic Application Load Balancer. For setup instructions, see [Deploying gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways).
  * **[GKE Ingress controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-xlb).** Supported by the classic Application Load Balancer and the regional external Application Load Balancer. For setup instructions, see [Configuring Ingress for external Application Load Balancers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/load-balance-ingress).



## Load balancing for Cloud Run, Cloud Run functions, and App Engine applications

You can use a global external Application Load Balancer as the frontend for your Cloud Run, Cloud Run functions, and App Engine applications. To set this up, you use a serverless NEG for the load balancer's backend.

This diagram shows how a serverless NEG fits into the external Application Load Balancer model.

[ ![HTTPS load balancing for serverless apps.](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-simple-ext-https.svg)](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-simple-ext-https.svg) HTTPS load balancing for serverless apps (click to enlarge).

Related documentation:

  * [Serverless NEGs overview](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts)
  * [Setting up an external Application Load Balancer with Cloud Run, Cloud Run functions, or App Engine](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-serverless)



## Proxying traffic to external backends with internet connectivity

Cloud Load Balancing supports proxying traffic to external backends outside Google Cloud. You can use this type of deployment when you want to serve content from an external backend, but you want your Google Cloud load balancer to be the frontend. The load balancer proxies traffic to your external endpoint by using Google's highly reliable backbone network for most of its journey, and only hands off to the public internet close to the destination.

[ ![Internet network endpoint groups in load balancing.](https://docs.cloud.google.com/static/load-balancing/images/internet-neg-sample-arch.svg)](https://docs.cloud.google.com/static/load-balancing/images/internet-neg-sample-arch.svg) Internet network endpoint groups in load balancing (click to enlarge).

Related documentation:

  * [Set up a global external Application Load Balancer with an internet NEG](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-external-backend)
  * [Set up a classic Application Load Balancer with an internet NEG](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-external-backend-internet-neg)



## Load balancing with hybrid connectivity

Cloud Load Balancing supports load-balancing traffic to endpoints that extend beyond Google Cloud, such as on-premises data centers and other public clouds that you can use [hybrid connectivity](https://cloud.google.com/hybrid-connectivity) to reach.

The following diagram demonstrates a hybrid deployment with a global external Application Load Balancer.

[ ![Hybrid connectivity with an external Application Load Balancer.](https://docs.cloud.google.com/static/load-balancing/images/ext-https-hybrid.svg)](https://docs.cloud.google.com/static/load-balancing/images/ext-https-hybrid.svg) Hybrid connectivity with an external Application Load Balancer (click to enlarge).

Related documentation:

  * [Hybrid connectivity NEGs overview](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts)
  * [Setting up an external Application Load Balancer with on-premises or other cloud backends](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-ext-https-hybrid)



## Load balancing with Private Service Connect

You can use a global external Application Load Balancer to access services that are published using Private Service Connect.

For more information, see [About Private Service Connect backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
