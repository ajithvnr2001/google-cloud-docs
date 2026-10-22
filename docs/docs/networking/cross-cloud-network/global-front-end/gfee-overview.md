---
url: https://docs.cloud.google.com/docs/networking/cross-cloud-network/global-front-end/gfee-overview/
title: Global Front End overview \u00a0|\u00a0 Networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:21:51.646249+00:00
---

# Global Front End overview  |  Networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/networking/cross-cloud-network/global-front-end/gfee-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Guides ](https://docs.cloud.google.com/docs/networking/cross-cloud-network/global-front-end/gfee-overview)



Send feedback 

#  Global Front End overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Global Front End is a Cross-Cloud Network solution that improves the performance and availability of applications. Using the Google Cloud network of more than 200 points of presence (PoPs), Global Front End acts as the unified edge gateway and distribution platform between public internet users and backend services hosted in any cloud, colocation facility, or data center.

Enterprise network architects, security administrators, and platform engineering teams use Global Front End to manage and secure applications distributed across multicloud and hybrid environments. Common deployment scenarios include the following:

  * Hosting an ecommerce application or website.
  * Accelerating API endpoints.
  * Meeting strong compliance needs for serving firmware downloads.
  * Serving static website assets and application APIs for web portals.

**Note:** A Global Front End is _different_ from a Google Front End (GFE). The GFE is a reverse proxy that terminates TCP connections, whereas a Global Front End lets you deliver, scale, and secure your internet-facing applications. Global Front End Enterprise consolidates the pricing of different Google Cloud networking services into one bundled pricing tier.

## Global Front End services

Global Front End integrates the following Google Cloud services:

  * [Global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) to balance application traffic globally.

    * **Global Anycast routing:** Directs traffic to the nearest healthy backend with capacity to reduce latency.
    * **Advanced routing:** Routes requests based on HTTP parameters such as host, path, and headers.
    * **Traffic management:** Applies traffic actions, including URL rewrites, redirects, header modifications, and traffic mirroring.
  * [Google Cloud Armor](https://docs.cloud.google.com/armor/docs) for web application firewall (WAF) and distributed denial-of-service (DDoS) protection.

    * **Security policies:** Enforces Layer 3 through Layer 7 firewall and security policies.
    * **Rate limiting:** Protects backends from traffic spikes and overuse.
    * **Adaptive Protection:** Uses machine learning to detect attacks and deploy rules automatically.
    * **Google Threat Intelligence:** Create rules based on threat intelligence categories, including known malicious sources, search engines, and cloud hosting providers.
    * **Address groups:** Groups IP addresses for security rules.
    * **DDoS attack visibility:** Displays real-time metrics and attack telemetry.
  * [Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview) to cache content at the edge and lower latency.

    * **Extended cache policies:** Granular control over caching policies using [cache policies in URL maps](https://docs.cloud.google.com/cdn/docs/caching#cache-policies-url-maps).
    * **Cache invalidation:** Clears cached content across edge locations.
    * **Request characterization:** Uses location and device metadata to define caching behaviour.
  * [Service Extensions](https://docs.cloud.google.com/service-extensions/docs/overview) to run custom plugins and callouts in the data path to add modify request and response attributes.

    * **Plugins:** Runs plugins inside Google-managed sandbox environments.
    * **Callouts:** Makes custom gRPC callouts to user-managed compute instances.



The following diagram shows the architecture of the Global Front End:

[ ![Global Front End](https://docs.cloud.google.com/static/architecture/images/webapp.svg)](https://docs.cloud.google.com/static/architecture/images/webapp.svg) Global Front End

For more information about the architecture of the Global Front End, see [Use Google Cloud Armor, Cloud Load Balancing, and Cloud CDN to deploy programmable global front ends](https://docs.cloud.google.com/architecture/deploy-programmable-gfe-cloud-armor-lb-cdn).

## Benefits of Global Front End

When you deploy applications with Global Front End, you gain the following architectural and operational benefits:

  * **Multicloud and hybrid routing:** Provides centralized traffic routing and applies unified security policies across application origins, regardless of where they are hosted.

  * **Global performance:** Built on the global edge infrastructure of Google Cloud, the platform caches content at more than 200 PoPs worldwide.

  * **Global security:** Provides built-in Layer 3 and Layer 4 DDoS mitigation, along with machine learning-driven Layer 7 protection.

  * **Centralized multi-backend routing:** Routes traffic and applies unified policies across diverse backend types. Supported backends include Google Cloud resources (such as Compute Engine VM instances, GKE pods, Cloud Run services, and Cloud Storage buckets) and external backends on-premises or in other clouds.




## Global Front End billing models

To use Global Front End, you configure the individual Google Cloud services, such as Cloud Load Balancing, Cloud CDN, and Google Cloud Armor. You can choose one of the following billing models:

  * **À la carte or Standard billing:** You pay individual pricing for each service and the [SKUs](https://cloud.google.com/skus) that you use in your solution. This is the default billing model.
  * **Global Front End Enterprise billing:** You enable Global Front End Enterprise in your Google Cloud project to simplify billing and consolidate charges. By consolidating the edge network with the Global Front End Enterprise, you can lower operational costs compared to procuring, configuring, and maintaining separate standalone products.



### Global Front End Enterprise

Using the standard billing model, you must estimate costs across the SKUs with multiple pricing options. To simplify your billing, you can enable Global Front End Enterprise in your Google Cloud project.

Global Front End Enterprise is a billing tier that integrates core Google Cloud networking and security services into a single project-level tier. When you enable Global Front End Enterprise in a project, all global external Application Load Balancers in that project gain access to Google Cloud Armor Enterprise tier features. For a complete list of covered features, see [Cloud Armor Enterprise and Global Front End](https://docs.cloud.google.com/armor/docs/armor-enterprise-overview#global-front-end).

To enable Global Front End Enterprise in a project, see [Enable and manage Global Front End Enterprise in your Google Cloud project](https://docs.cloud.google.com/docs/networking/cross-cloud-network/global-front-end/gfee-manage).

**Note:** You can enable Global Front End Enterprise only at the Google Cloud project level, not for individual [forwarding rules](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts).

### Global Front End Enterprise billing SKUs

Global Front End Enterprise consolidates individual product SKUs into the following billing SKUs:

  * **Global Front End instance:** charges a flat hourly rate for each [forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) that you associate with your deployed services.
  * **Global Front End requests:** charges a single rate per 10,000 requests that covers both application traffic and edge-cached Cloud CDN traffic.
  * **Global Front End data processing:** charges a tiered rate per GiB (Gibibyte) for processed ingress and egress traffic.



For more information about Global Front End Enterprise pricing, see [Network pricing](https://docs.cloud.google.com/vpc/network-pricing#global-front-end-enterprise).

## Important considerations

Before you configure your project, review the following design and billing characteristics:

  * **Project-level scope:** Enabling Global Front End Enterprise applies the billing model to all compatible forwarding rules within that project.
  * **Cross-project backend billing:** If a global external Application Load Balancer routes traffic to backends in other projects, Global Front End Enterprise pricing applies only to the project where the load balancer frontend components reside. Usage and charges in projects that contain the backend components follow individual product pricing.
  * **Cloud Armor tier scope:** Enabling Global Front End Enterprise provides security capabilities for your global external Application Load Balancers, but it doesn't change the Cloud Armor tier of your project.
  * **Disabling behavior:** If you disable Global Front End Enterprise in a project, Google Cloud doesn't retain your previous Cloud Armor security configurations. You must associate your backend services with an alternate Cloud Armor tier.



## What's next

  * [Enable and manage Global Front End Enterprise in your Google Cloud project](https://docs.cloud.google.com/docs/networking/cross-cloud-network/global-front-end/gfee-manage)
  * [Use Google Cloud Armor, Cloud Load Balancing, and Cloud CDN to deploy programmable global front ends](https://docs.cloud.google.com/architecture/deploy-programmable-gfe-cloud-armor-lb-cdn)
  * [Global Front End for global external Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https#global-front-end)
  * [Network pricing](https://docs.cloud.google.com/vpc/network-pricing#global-front-end-enterprise)
  * [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
