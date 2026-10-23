---
url: https://docs.cloud.google.com/service-extensions/docs/release-notes/
title: Service Extensions release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:42:04.832244+00:00
---

# Service Extensions release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Resources ](https://docs.cloud.google.com/service-extensions/docs/resources)



Send feedback 

#  Service Extensions release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Service Extensions. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/service-extensions-release-notes.xml) directly. 

## September 23, 2026

Feature

Support for [route](https://docs.cloud.google.com/service-extensions/docs/configure-route-extensions#configure-route-plugins) and [traffic](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions#configure-traffic-plugins) extensions that use plugins is [generally available (GA)](https://cloud.google.com/products#product-launch-stages) for regional external Application Load Balancers and regional internal Application Load Balancers.

For more information, see [Supported Application Load Balancers for user-managed extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs).

## August 31, 2026

Feature

[Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) supports Service Extensions to evaluate requests and delegate authorization decisions for agent traffic to either Google services or custom authorization services. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

For more information, see [Integration with Agent Gateway](https://docs.cloud.google.com/service-extensions/docs/integration-with-google-services#integration-with-agent-gateway).

## August 20, 2026

Feature

[Global Front End](https://docs.cloud.google.com/docs/networking/cross-cloud-network/global-front-end/gfee-overview) is a unified offering that combines Service Extensions, global external Application Load Balancer, Google Cloud Armor, and Cloud CDN into one solution to help deliver, scale, and secure your internet-facing applications. Service Extensions is included in the Global Front End Enterprise billing tier. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see the [Global Front End](https://docs.cloud.google.com/service-extensions/docs/overview#global-front-end) section on the [Service Extensions overview](https://docs.cloud.google.com/service-extensions/docs/overview) page.

## June 17, 2026

Feature

Support for the [`ext_authz` Envoy gRPC API protocol](https://docs.cloud.google.com/service-extensions/docs/callouts-overview#ext-authz) is [generally available (GA)](https://cloud.google.com/products#product-launch-stages) for regional external Application Load Balancers and regional internal Application Load Balancers.

## April 17, 2026

Feature

Authorization extensions support authorization policy request and content profiles. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [How authorization extensions work](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#authorization-extensions).

Feature

You can use authorization extensions to insert custom services directly into the Secure Web Proxy processing path. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Secure Web Proxy extensions overview](https://docs.cloud.google.com/service-extensions/docs/swp-extensions-overview).

## April 10, 2026

Feature

When configuring extensions by using plugins or callouts, you can specify some request and connection attributes to forward to backend services. For more information, see [supported attributes](https://docs.cloud.google.com/service-extensions/docs/attributes).

## April 09, 2026

Feature

Google Kubernetes Engine (GKE) Gateway support for using extensions by using callouts to add custom logic into the load balancing processing path is in **General Availability**. For more information, see [GKE extensions](https://docs.cloud.google.com/service-extensions/docs/overview#integration-gke).

## December 08, 2025

Feature

You can use Service Extensions to implement [dynamic forwarding](https://docs.cloud.google.com/service-extensions/docs/lb-advanced-use-cases#dynamic-forwarding), which helps you map tenants to endpoints programmatically, without having to update your URL maps. This feature is in **Preview**.

## November 17, 2025

Feature

For authorization extensions, in addition to the ext_proc Envoy gRPC API, the [ext_authz gRPC API](https://docs.cloud.google.com/service-extensions/docs/callouts-overview#ext-authz) is also supported. This capability allows seamless integration with the broader authorization ecosystem. This feature is in **Preview**.

## November 13, 2025

Feature

Regional external and internal Application Load Balancers support [route](https://docs.cloud.google.com/service-extensions/docs/configure-route-extensions#configure-route-plugins) and [traffic](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions#configure-traffic-plugins) extensions using plugins. This feature is in **Preview**.

Feature

[Edge extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#edge-extensions) help you manipulate request headers early in the processing lifecycle of global external Application Load Balancers to influence caching and routing decisions. This feature is in **General Availability**.

## November 05, 2025

Feature

[Cloud Load Balancing callouts](https://docs.cloud.google.com/service-extensions/docs/callouts-overview) have full duplex streaming support.

## October 28, 2025

Feature

[Authorization extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#authorization-extensions) help you configure Cloud Load Balancing authorization policies to use custom authorization engines. This feature is in **General Availability**.

## September 15, 2025

Feature

To protect AI workloads, you can [configure traffic extensions to call the Model Armor service](https://docs.cloud.google.com/service-extensions/docs/configure-extensions-to-google-services#configure-traffic-ma) on supported Application Load Balancers. This feature is in **General Availability**.

## July 24, 2025

Feature

To [upload your Wasm plugin code](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code#generic-repository) to Artifact Registry, you can use generic format repositories, in addition to Docker repositories. This feature is in **Preview**.

## July 01, 2025

Feature

[Plugins for Cloud Load Balancing](https://docs.cloud.google.com/service-extensions/docs/overview#integration-lb-plugins) help you insert WebAssembly (Wasm) code in a fully managed serverless environment directly into the data path of most Cloud Load Balancing Application Load Balancers. This feature is in **General Availability**.

## June 23, 2025

Feature

[Edge extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#edge-extensions) help you manipulate request headers early in the request processing lifecycle of global external Application Load Balancers to influence caching and routing decisions. This feature is in **Preview**.

Learn how to [configure an edge extension](https://docs.cloud.google.com/service-extensions/docs/configure-edge-extensions).

## April 09, 2025

Feature

The Google Kubernetes Engine (GKE) Gateway supports using extensions to add custom logic into the load balancing processing path. For more information, see [GKE extensions](https://docs.cloud.google.com/service-extensions/docs/overview#integration-gke). This feature is in **Preview**.

Feature

You can configure Model Armor with Service Extensions to protect AI workloads on supported Application Load Balancers. For more information, see [Callouts to Google services](https://docs.cloud.google.com/service-extensions/docs/overview#integration-lb-callouts-gservices). This feature is in **Preview**.

## February 12, 2025

Feature

Service Extensions plugins support Go-compiled Wasm, in addition to Rust and C++. For more information, see [Prepare the plugin code](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code#go).

## October 30, 2024

Feature

Service Extensions plugins help you insert WebAssembly (Wasm) plugins in a fully managed serverless environment directly into the data path of most Cloud Load Balancing Application Load Balancers. This feature is in **Preview**.

For details, see [Plugins for Cloud Load Balancing](https://docs.cloud.google.com/service-extensions/docs/overview#integration-lb-plugins).

## September 16, 2024

Feature

[Authorization extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#authorization-extensions) help you configure Cloud Load Balancing authorization policies to use custom authorization engines. This feature is in **Preview**.

Feature

You can now also host an extension on a backend service that uses serverless NEGs pointing to Cloud Run services. For more information, see [Supported backends for extension services](https://docs.cloud.google.com/service-extensions/docs/callouts-overview#supported-backends).

## April 02, 2024

Announcement

Service Extensions is **Generally Available** for callout extensions for [most Google Cloud Application Load Balancers](https://docs.cloud.google.com/service-extensions/docs/callouts-overview#supported-lbs).

You can also [configure Cloud Load Balancing user-managed callout extensions](https://docs.cloud.google.com/service-extensions/docs/configure-callout) by using the Console.

## October 17, 2023

Feature

Service Extensions callouts are available for Google Cloud Application Load Balancers, excluding Classic.

With the introduction of this feature, users instruct load balancers to forward traffic from within the Cloud Load Balancing data processing path through gRPC to user-managed or partner-hosted applications. These applications can apply various policies or functions, such as header or payload manipulation, security screening, or custom logging on the traffic before returning the traffic to the load balancer for further processing.

For details, see [Cloud Load Balancing callouts overview](https://docs.cloud.google.com/service-extensions/docs/callouts-overview).

## October 28, 2022

Announcement

Initial release of [Service Extensions](https://docs.cloud.google.com/service-extensions/docs/overview).

Service Extensions helps you insert plugins inline in the Media CDN data path. You build these plugins by using WebAssembly (Wasm) and Proxy-Wasm ABI.

This product is in **Preview**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
