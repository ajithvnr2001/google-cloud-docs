---
url: https://docs.cloud.google.com/load-balancing/docs/application-load-balancer/
title: Application Load Balancer overview \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:02.106866+00:00
---

# Application Load Balancer overview  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/application-load-balancer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Application Load Balancer overview Stay organized with collections  Save and categorize content based on your preferences. 

The Application Load Balancer is a proxy-based Layer 7 load balancer that lets you run and scale your services. The Application Load Balancer distributes HTTP and HTTPS traffic to backends hosted on a variety of Google Cloud platforms—such as Compute Engine, Google Kubernetes Engine (GKE), Cloud Storage, and Cloud Run—as well as external backends connected over the internet or by using hybrid connectivity.

Application Load Balancers are available in the following modes of deployment:

  * **External Application Load Balancer** : Load balances traffic coming from clients on the internet. For architecture details, see [external Application Load Balancer architecture](https://docs.cloud.google.com/load-balancing/docs/https#component).

Deployment mode | Network service tier | Load balancing scheme | IP address | Frontend ports  
---|---|---|---|---  
Global external | Premium Tier | EXTERNAL_MANAGED | IPv4   
IPv6  | Can reference exactly one port from 1-65535.  
Regional external | Premium or Standard Tier | EXTERNAL_MANAGED | IPv4   
IPv6 ([Preview](https://cloud.google.com/products#product-launch-stages))   
Classic | Global in Premium Tier Regional in Standard Tier | EXTERNAL* | IPv4   
IPv6 (requires Premium Tier)   
  
* It is possible to attach `EXTERNAL_MANAGED` backend services to `EXTERNAL` forwarding rules. However, `EXTERNAL` backend services cannot be attached to `EXTERNAL_MANAGED` forwarding rules. To take advantage of [new features available only with the global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https#load-balancer-mode), we recommend that you migrate your existing `EXTERNAL` resources to `EXTERNAL_MANAGED` by using the migration process described at [Migrate resources from classic to global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/migrate-from-classic-global). 

  * **Internal Application Load Balancer** : Load balances traffic within your VPC network or networks connected to your VPC network. For architecture details, see [internal Application Load Balancer architecture](https://docs.cloud.google.com/load-balancing/docs/l7-internal#component).

Deployment mode | Network service tier | Load balancing scheme | IP address | Frontend ports  
---|---|---|---|---  
Regional internal | Premium Tier | INTERNAL_MANAGED | IPv4   
IPv6 ([Preview](https://cloud.google.com/products#product-launch-stages))  | Can reference exactly one port from 1-65535.  
Cross-region internal* | Premium Tier | INTERNAL_MANAGED | IPv4   
IPv6 ([Preview](https://cloud.google.com/products#product-launch-stages))   
  
* The load balancer uses global resources and can be deployed in one or multiple Google Cloud regions that you choose.




The _load balancing scheme_ is an attribute on the [forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) and the [backend service](https://docs.cloud.google.com/load-balancing/docs/backend-service) of a load balancer and indicates whether the load balancer can be used for internal or external traffic. The term `__MANAGED_` in the load balancing scheme indicates that the load balancer is implemented as a managed service either on [Google Front Ends (GFEs)](https://docs.cloud.google.com/docs/security/infrastructure/design#google-frontend-service) or on the open source [Envoy proxy](https://www.envoyproxy.io/). In a load balancing scheme that is `_MANAGED`, requests are routed either to the GFE or to the Envoy proxy.

## External Application Load Balancer

**Preview — Cross-region, regional external, and regional internal Application Load Balancers support terminating IPv6 traffic**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

External Application Load Balancers are implemented using Google Front Ends (GFEs) or managed proxies. Global external Application Load Balancers and classic Application Load Balancers use GFEs that are [distributed globally](https://docs.cloud.google.com/load-balancing/docs/locations), operating together by using Google's global network and control plane. GFEs offer multi-region load balancing in the Premium tier, directing traffic to the closest healthy backend that has capacity and terminating HTTP(S) traffic as close as possible to your users. Global external Application Load Balancers and regional external Application Load Balancers use the open source [Envoy proxy](https://www.envoyproxy.io/) software to enable advanced traffic management capabilities.

These load balancers can be deployed in one of the following modes: global, regional, or classic.

External Application Load Balancers support the following capabilities:

  * **IPv6 termination**. The external load balancers support both IPv4 and [IPv6 addresses](https://docs.cloud.google.com/load-balancing/docs/ipv6) for client traffic. Client IPv6 requests are terminated at the load balancing layer and then proxied over IPv4 or IPv6 (provided the backends are configured as dual-stack) connections to your backends. Note that classic load balancers only support proxying over IPv4 to your backends.
  * **Advanced traffic management**. Features include traffic mirroring, weight-based traffic splitting, and request/response-based header transformations. For details, see [Traffic management overview](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global).
  * **Diverse backend support**. Load balances traffic to backends hosted on a variety of Google Cloud platforms such as Compute Engine, Google Kubernetes Engine (GKE), Cloud Run, and more. Backend support depends on the deployment mode of the load balancer. For details, see the [External Application Load Balancer overview](https://docs.cloud.google.com/load-balancing/docs/https#backend-service).
  * **Cached responses**. Integrates with [Cloud CDN](https://docs.cloud.google.com/cdn) to cache responses.
  * **Integration with Cloud Armor**. Provides protection from DDoS or other web attacks by using [Google Cloud Armor](https://docs.cloud.google.com/armor).
  * **GKE integration**. Supports load balancing to GKE by using either Ingress or Gateway (fully orchestrated) or [standalone NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg).
  * Organization of global, regional, and cross-region Application Load Balancers and proxy Network Load Balancers in [App Hub applications](https://docs.cloud.google.com/app-hub/docs/overview) to understand the load balancer interactions and support business functions.



The following diagram shows a sample external Application Load Balancer architecture.

[ ![External Application Load Balancer architecture.](https://docs.cloud.google.com/static/load-balancing/images/external-application-load-balancer.svg)](https://docs.cloud.google.com/static/load-balancing/images/external-application-load-balancer.svg) External Application Load Balancer architecture.

For a complete overview, see [Architecture overview for External Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https).

## Internal Application Load Balancer

**Preview — Cross-region, regional external, and regional internal Application Load Balancers support terminating IPv6 traffic**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The internal Application Load Balancers are Envoy proxy-based regional Layer 7 load balancers that enable you to run and scale your HTTP application traffic behind an internal IP address. Internal Application Load Balancers support backends in one region, but can be configured to be globally accessible by clients from any Google Cloud region.

The load balancer distributes traffic to backends hosted on Google Cloud, on-premises, or in other cloud environments. Internal Application Load Balancers also support the following features:

  * **IPv6 termination**. The internal load balancers support both IPv4 and [IPv6 addresses](https://docs.cloud.google.com/load-balancing/docs/ipv6) for client traffic. Client IPv6 requests are terminated at the load balancing layer and then proxied over IPv4 or IPv6 (provided the backends are configured as dual-stack) connections to your backends.
  * **Locality policies.** Within a backend instance group or network endpoint group, you can configure how requests are distributed to member instances or endpoints. For details, see [Traffic management](https://docs.cloud.google.com/load-balancing/docs/l7-internal/traffic-management).
  * **Global access.** When global access is enabled, clients from any region can access the load balancer. For details, see [Enable global access](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#global-access).
  * **Access from connected networks.** You can make your load balancer accessible to clients from networks beyond its own Google Cloud Virtual Private Cloud (VPC) network. The other networks must be connected to the load balancer's VPC network by using either VPC Network Peering, Cloud VPN, or Cloud Interconnect. For details, see [Access connected networks](https://docs.cloud.google.com/load-balancing/docs/l7-internal/internal-https-lb-and-other-networks).
  * Compatibility with GKE by using Ingress (fully orchestrated). For details, see [Configure Ingress for internal Application Load Balancers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balance-ingress).
  * Organization of cross-region internal Application Load Balancers and regional internal Application Load Balancers in [App Hub applications](https://docs.cloud.google.com/app-hub/docs/overview) to understand the load balancer interactions and support business functions.

[ ![Internal Application Load Balancer architecture.](https://docs.cloud.google.com/static/load-balancing/images/internal-application-load-balancer.svg)](https://docs.cloud.google.com/static/load-balancing/images/internal-application-load-balancer.svg) Internal Application Load Balancer architecture.

For a complete overview, see [Architecture overview for internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal).

## Use cases

The following sections depict some common use cases for Application Load Balancers.

### Three-tier web services

You can deploy a combination of Application Load Balancers and Network Load Balancers to support conventional three-tier web services. The following example shows how you can deploy each tier, depending on your traffic type:

  * **Web tier.** The application's frontend is served by an external Application Load Balancer with instance group backends. Traffic enters from the internet and is proxied from the load balancer to a set of instance group backends in various regions. These backends send HTTP(S) traffic to a set of internal Application Load Balancers.
  * **Application tier.** The application's middleware is deployed and scaled by using an internal Application Load Balancer and instance group backends. The load balancers distribute the traffic to middleware instance groups. These middleware instance groups then send the traffic to internal passthrough Network Load Balancers.
  * **Database tier.** The Network Load Balancers serve as frontends for the database tier. They distribute traffic to data storage backends in various regions.

[ ![Layer 7-based routing in a three-tier web application.](https://docs.cloud.google.com/static/load-balancing/images/ilb-l7-tiers.svg)](https://docs.cloud.google.com/static/load-balancing/images/ilb-l7-tiers.svg) Layer 7-based routing in a three-tier web application.

#### Global access for regional internal Application Load Balancers

If you [enable global access for your regional internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal#global-access), your web-tier client VMs can be in another region.

This multitiered application example shows the following:

  * A globally available internet-facing web tier that load balances traffic by using an external Application Load Balancer.
  * An internal backend load-balanced database tier in the `us-east1` region that is accessed by the global web tier.
  * A client VM that is part of the web tier in the `europe-west1` region that accesses the internal load-balanced database tier located in `us-east1`.

[ ![Three-tier web app with an external Application Load Balancer, global access, and an
         internal Application Load Balancer.](https://docs.cloud.google.com/static/load-balancing/images/global-access-ilb-multi-tier.svg)](https://docs.cloud.google.com/static/load-balancing/images/global-access-ilb-multi-tier.svg) Three-tier web app with an external Application Load Balancer, global access, and an internal Application Load Balancer (click to enlarge).

### Workloads with jurisdictional compliance

Some workloads with regulatory or compliance requirements require that network configurations and traffic termination reside in a specific region. For these workloads, a regional external Application Load Balancer is often the preferred option to provide the jurisdictional controls these workloads require.

### Advanced traffic management

The Application Load Balancers support advanced traffic management features that give you fine-grained control over how your traffic is handled. These capabilities include the following:

  * You can update how traffic is managed without needing to modify your application code.
  * You can intelligently route traffic based on HTTP(S) parameters, such as host, path, headers, and other request parameters. For example, you can use Cloud Storage buckets to handle any static video content, and you can use instance groups or NEGs to handle all other requests.
  * You can mitigate risks when deploying a new version of your application by using weight-based traffic splitting. For example, you can send 95% of the traffic to the previous version of your service and 5% to the new version of your service. After you validate that the new version works as expected, you can gradually shift the percentages until 100% of the traffic reaches the new version of your service. Traffic splitting is typically used for deploying new versions, A/B testing, service migration, modernizing legacy services, and similar processes.



Following is an example of path-based routing implemented by using an internal Application Load Balancer. Each path is handled by a different backend.

[ ![Path-based routing with internal Application Load Balancers.](https://docs.cloud.google.com/static/load-balancing/images/l7-ilb-micro.svg)](https://docs.cloud.google.com/static/load-balancing/images/l7-ilb-micro.svg) Path-based routing with internal Application Load Balancers.

For more details, see the following:

  * [Traffic management overview for global external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global)
  * [Traffic management overview for regional external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-regional)



### Extensibility with Service Extensions

The integration with [Service Extensions](https://docs.cloud.google.com/service-extensions/docs/overview#integration-lb) lets you inject custom logic into the load balancing path of [supported Application Load Balancers](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs).

For more information, see [Service Extensions overview](https://docs.cloud.google.com/service-extensions/docs/overview).

### Migrating legacy services to Google Cloud

Migrating an existing service to Google Cloud lets you free up on-premises capacity and reduce the cost and burden of maintaining an on-premises infrastructure. You can temporarily set up a hybrid deployment that lets you route traffic to both your current on-premises service and a corresponding Google Cloud service endpoint.

The following diagram demonstrates this setup with an internal Application Load Balancer. If you are using an internal load balancer, you can configure the Google Cloud load balancer to use weight-based traffic splitting to split traffic across the two services. Traffic splitting lets you start by sending 0% of the traffic to the Google Cloud service and 100% to the on-premises service. You can then gradually increase the proportion of traffic sent to the Google Cloud service. Eventually, you send 100% of the traffic to the Google Cloud service, and you can retire the on-premises service.

[ ![Migrate legacy services to Google Cloud.](https://docs.cloud.google.com/static/load-balancing/images/migrate-hybrid.svg)](https://docs.cloud.google.com/static/load-balancing/images/migrate-hybrid.svg) Migrate legacy services to Google Cloud.

### Load balancing for GKE applications

There are three ways to deploy Application Load Balancers for GKE clusters:

  * **[GKE Gateway controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api).** Supported only by the global external Application Load Balancers, classic Application Load Balancers, and regional internal Application Load Balancers. For setup instructions, see [Deploying gateways](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-gateways).
  * **[GKE Ingress controller](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/ingress-xlb).** You can use the built-in GKE Ingress controller, which deploys Google Cloud load balancers on behalf of GKE users. This is the same as the standalone load-balancing architecture, except that its lifecycle is fully automated and controlled by GKE. Supported by both external and internal Application Load Balancers. For setup instructions, see the following: 
    * [Configuring Ingress for external Application Load Balancers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/load-balance-ingress)
    * [Configuring Ingress for internal Application Load Balancers](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balance-ingress)
  * **[Standalone zonal NEGs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/standalone-neg).** Standalone NEGs are deployed and managed through the GKE NEG controller, but all the load balancing resources (forwarding rules, health checks, and so on) are deployed manually. These are supported by both external and internal Application Load Balancers.



### Load balancing for Cloud Run, Cloud Run functions, and App Engine applications

You can use an Application Load Balancer as the frontend for your Google Cloud serverless applications. This lets you configure your serverless applications to serve requests from a dedicated IP address that is not shared with any other services.

To set this up, you use a serverless NEG as the load balancer's backend. The following diagrams show how a serverless application is integrated with an Application Load Balancer.

###  Global external 

This diagram shows how a serverless NEG fits into a global external Application Load Balancer architecture.

[ ![Global external Application Load Balancer architecture for serverless apps.](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-simple-ext-https.svg)](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-simple-ext-https.svg) Global external Application Load Balancer architecture for serverless apps.

###  Regional external 

This diagram shows how a serverless NEG fits into a regional external Application Load Balancer architecture. This load balancer only supports Cloud Run backends.

[ ![Regional external Application Load Balancer architecture for serverless apps.](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-simple-reg-ext-https.svg)](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-simple-reg-ext-https.svg) Regional external Application Load Balancer architecture for serverless apps.

###  Regional internal 

This diagram shows how a serverless NEG fits into the regional internal Application Load Balancer model. This load balancer only supports Cloud Run backends.

[ ![Regional internal Application Load Balancer architecture for serverless apps.](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-simple-int-https.svg)](https://docs.cloud.google.com/static/load-balancing/images/lb-serverless-run-int-https.svg) Regional internal Application Load Balancer architecture for serverless apps.

###  Cross-region internal 

This diagram shows how a serverless NEG fits into the cross-region internal Application Load Balancer model. This load balancer only supports Cloud Run backends.

[ ![Cross-region internal Application Load Balancer architecture for serverless apps.](https://docs.cloud.google.com/static/load-balancing/images/cross-reg-int-cloudrun.svg)](https://docs.cloud.google.com/static/load-balancing/images/cross-reg-int-cloudrun.svg) Cross-region internal Application Load Balancer architecture for serverless apps (click to enlarge).

Related documentation:

  * [Serverless NEGs overview](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts)
  * [Set up a global external Application Load Balancer with a Cloud Run, Cloud Run functions, or App Engine backend](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-serverless)
  * [Set up a regional external Application Load Balancer with a Cloud Run backend](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-serverless)
  * [Set up a regional internal Application Load Balancer with a Cloud Run backend](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal-serverless)
  * [Set up a cross-region internal Application Load Balancer with Cloud Run](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-cross-reg-serverless)



### Load balancing to backends outside Google Cloud

Application Load Balancers support load-balancing traffic to endpoints that extend beyond Google Cloud, such as on-premises data centers and other cloud environments. External backends are typically accessible in one of the following ways:

  * **Accessible over the public internet.** For these endpoints, you use an internet NEG as the load balancer's backend. The internet NEG is configured to point to a single FQDN:Port or IP:Port endpoint on the external backend. Internet NEGs can be global or regional.

The following diagram demonstrates how to connect to external backends accessible over the public internet using a global internet NEG.

[ ![Global external Application Load Balancer with an external backend.](https://docs.cloud.google.com/static/load-balancing/images/internet-neg-external-backend.svg)](https://docs.cloud.google.com/static/load-balancing/images/internet-neg-external-backend.svg) Global external Application Load Balancer with an external backend.

For more details, see [Internet NEGs overview](https://docs.cloud.google.com/load-balancing/docs/negs/internet-neg-concepts).

  * **Accessible by using hybrid connectivity (Cloud Interconnect or Cloud VPN).** For these endpoints, you use a hybrid NEG as the load balancer's backend. The hybrid NEG is configured to point to IP:Port endpoints on the external backend.

The following diagrams demonstrate how to connect to external backends accessible by using Cloud Interconnect or Cloud VPN.

###  External 

[ ![Hybrid connectivity with global external Application Load Balancers.](https://docs.cloud.google.com/static/load-balancing/images/ext-https-hybrid.svg)](https://docs.cloud.google.com/static/load-balancing/images/ext-https-hybrid.svg) Hybrid connectivity with global external Application Load Balancers.

###  Internal 

[ ![Hybrid connectivity with internal Application Load Balancers.](https://docs.cloud.google.com/static/load-balancing/images/int-https-hybrid.svg)](https://docs.cloud.google.com/static/load-balancing/images/int-https-hybrid.svg) Hybrid connectivity with internal Application Load Balancers.

For more details, see [Hybrid NEGs overview](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts).




### Integration with Private Service Connect

Private Service Connect allows private consumption of services across VPC networks that belong to different groups, teams, projects, or organizations. You can use Private Service Connect to access Google APIs and services or managed services in another VPC network.

You can use a global external Application Load Balancer to access services that are published by using Private Service Connect. For more information, see [About Private Service Connect backends](https://docs.cloud.google.com/vpc/docs/private-service-connect-backends).

You can use an internal Application Load Balancer to send requests to supported regional Google APIs and services. For more information, see [Access Google APIs through backends](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-controls).

### High availability and cross-region failover

Cross-region failover is only available with global external Application Load Balancers, classic Application Load Balancers, and cross-region internal Application Load Balancers. These load balancers let you improve service availability when you create global backend services with backends in multiple regions. If backends in a particular region are down, traffic fails over to another region gracefully.

To learn more about how failover works, see the following topics:

  * [Global external Application Load Balancers: How requests are distributed](https://docs.cloud.google.com/load-balancing/docs/https#request-distribution)
  * [Cross-region internal Application Load Balancers: High availability and cross-region failover](https://docs.cloud.google.com/load-balancing/docs/l7-internal#cross-region-failover)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
