---
url: https://docs.cloud.google.com/feeds/service-extensions-release-notes.xml
title: Service Extensions - Release notes
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:56:39.581190+00:00
---

# Service Extensions - Release notes

> Source: https://docs.cloud.google.com/feeds/service-extensions-release-notes.xml

tag:google.com,2016:service-extensions-release-notesService Extensions - Release notesGoogle Cloud Platform2026-09-23T00:00:00-07:00September 23, 2026tag:google.com,2016:service-extensions-release-notes#September_23_20262026-09-23T00:00:00-07:00Feature 

Support for [route](https://docs.cloud.google.com/service-extensions/docs/configure-route-extensions#configure-route-plugins) and [traffic](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions#configure-traffic-plugins) extensions that use plugins is [generally available (GA)](https://cloud.google.com/products#product-launch-stages) for regional external Application Load Balancers and regional internal Application Load Balancers.

For more information, see [Supported Application Load Balancers for user-managed extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#supported-lbs).

]]> August 31, 2026tag:google.com,2016:service-extensions-release-notes#August_31_20262026-08-31T00:00:00-07:00Feature 

[Agent Gateway](https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview) supports Service Extensions to evaluate requests and delegate authorization decisions for agent traffic to either Google services or custom authorization services. This feature is [generally available (GA)](https://cloud.google.com/products#product-launch-stages).

For more information, see [Integration with Agent Gateway](https://docs.cloud.google.com/service-extensions/docs/integration-with-google-services#integration-with-agent-gateway).

]]> August 20, 2026tag:google.com,2016:service-extensions-release-notes#August_20_20262026-08-20T00:00:00-07:00Feature 

[Global Front End](https://docs.cloud.google.com/docs/networking/cross-cloud-network/global-front-end/gfee-overview) is a unified offering that combines Service Extensions, global external Application Load Balancer, Google Cloud Armor, and Cloud CDN into one solution to help deliver, scale, and secure your internet-facing applications. Service Extensions is included in the Global Front End Enterprise billing tier. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see the [Global Front End](https://docs.cloud.google.com/service-extensions/docs/overview#global-front-end) section on the [Service Extensions overview](https://docs.cloud.google.com/service-extensions/docs/overview) page.

]]> June 17, 2026tag:google.com,2016:service-extensions-release-notes#June_17_20262026-06-17T00:00:00-07:00Feature 

Support for the [`ext_authz` Envoy gRPC API protocol](https://docs.cloud.google.com/service-extensions/docs/callouts-overview#ext-authz) is [generally available (GA)](https://cloud.google.com/products#product-launch-stages) for regional external Application Load Balancers and regional internal Application Load Balancers.

]]> April 17, 2026tag:google.com,2016:service-extensions-release-notes#April_17_20262026-04-17T00:00:00-07:00Feature 

Authorization extensions support authorization policy request and content profiles. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [How authorization extensions work](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#authorization-extensions).

### Feature

You can use authorization extensions to insert custom services directly into the Secure Web Proxy processing path. This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

For more information, see [Secure Web Proxy extensions overview](https://docs.cloud.google.com/service-extensions/docs/swp-extensions-overview).

]]> April 10, 2026tag:google.com,2016:service-extensions-release-notes#April_10_20262026-04-10T00:00:00-07:00Feature 

When configuring extensions by using plugins or callouts, you can specify some request and connection attributes to forward to backend services. For more information, see [supported attributes](https://docs.cloud.google.com/service-extensions/docs/attributes).

]]> April 09, 2026tag:google.com,2016:service-extensions-release-notes#April_09_20262026-04-09T00:00:00-07:00Feature 

Google Kubernetes Engine (GKE) Gateway support for using extensions by using callouts to add custom logic into the load balancing processing path is in **General Availability**. For more information, see [GKE extensions](https://docs.cloud.google.com/service-extensions/docs/overview#integration-gke).

]]> December 08, 2025tag:google.com,2016:service-extensions-release-notes#December_08_20252025-12-08T00:00:00-08:00Feature 

You can use Service Extensions to implement [dynamic forwarding](https://docs.cloud.google.com/service-extensions/docs/lb-advanced-use-cases#dynamic-forwarding), which helps you map tenants to endpoints programmatically, without having to update your URL maps. This feature is in **Preview**.

]]> November 17, 2025tag:google.com,2016:service-extensions-release-notes#November_17_20252025-11-17T00:00:00-08:00Feature 

For authorization extensions, in addition to the ext_proc Envoy gRPC API, the [ext_authz gRPC API](https://docs.cloud.google.com/service-extensions/docs/callouts-overview##ext-authz) is also supported. This capability allows seamless integration with the broader authorization ecosystem. This feature is in **Preview**.

]]> November 13, 2025tag:google.com,2016:service-extensions-release-notes#November_13_20252025-11-13T00:00:00-08:00Feature 

Regional external and internal Application Load Balancers support [route](https://docs.cloud.google.com/service-extensions/docs/configure-route-extensions#configure-route-plugins) and [traffic](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions#configure-traffic-plugins) extensions using plugins. This feature is in **Preview**.

### Feature

[Edge extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#edge-extensions) help you manipulate request headers early in the processing lifecycle of global external Application Load Balancers to influence caching and routing decisions. This feature is in **General Availability**.

]]> November 05, 2025tag:google.com,2016:service-extensions-release-notes#November_05_20252025-11-05T00:00:00-08:00Feature 

[Cloud Load Balancing callouts](https://docs.cloud.google.com/service-extensions/docs/callouts-overview) have full duplex streaming support.

]]> October 28, 2025tag:google.com,2016:service-extensions-release-notes#October_28_20252025-10-28T00:00:00-07:00Feature 

[Authorization extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#authorization-extensions) help you configure Cloud Load Balancing authorization policies to use custom authorization engines. This feature is in **General Availability**.

]]> September 15, 2025tag:google.com,2016:service-extensions-release-notes#September_15_20252025-09-15T00:00:00-07:00Feature 

To protect AI workloads, you can [configure traffic extensions to call the Model Armor service](https://docs.cloud.google.com/service-extensions/docs/configure-extensions-to-google-services#configure-traffic-ma) on supported Application Load Balancers. This feature is in **General Availability**.

]]> July 24, 2025tag:google.com,2016:service-extensions-release-notes#July_24_20252025-07-24T00:00:00-07:00Feature 

To [upload your Wasm plugin code](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code#generic-repository) to Artifact Registry, you can use generic format repositories, in addition to Docker repositories. This feature is in **Preview**.

]]> July 01, 2025tag:google.com,2016:service-extensions-release-notes#July_01_20252025-07-01T00:00:00-07:00Feature 

[Plugins for Cloud Load Balancing](https://docs.cloud.google.com/service-extensions/docs/overview#integration-lb-plugins) help you insert WebAssembly (Wasm) code in a fully managed serverless environment directly into the data path of most Cloud Load Balancing Application Load Balancers. This feature is in **General Availability**.

]]> June 23, 2025tag:google.com,2016:service-extensions-release-notes#June_23_20252025-06-23T00:00:00-07:00Feature 

[Edge extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#edge-extensions) help you manipulate request headers early in the request processing lifecycle of global external Application Load Balancers to influence caching and routing decisions. This feature is in **Preview**.

Learn how to [configure an edge extension](https://docs.cloud.google.com/service-extensions/docs/configure-edge-extensions).

]]> April 09, 2025tag:google.com,2016:service-extensions-release-notes#April_09_20252025-04-09T00:00:00-07:00Feature 

The Google Kubernetes Engine (GKE) Gateway supports using extensions to add custom logic into the load balancing processing path. For more information, see [GKE extensions](https://docs.cloud.google.com/service-extensions/docs/overview#integration-gke). This feature is in **Preview**.

### Feature

You can configure Model Armor with Service Extensions to protect AI workloads on supported Application Load Balancers. For more information, see [Callouts to Google services](https://docs.cloud.google.com/service-extensions/docs/overview#integration-lb-callouts-gservices). This feature is in **Preview**.

]]> February 12, 2025tag:google.com,2016:service-extensions-release-notes#February_12_20252025-02-12T00:00:00-08:00Feature 

Service Extensions plugins support Go-compiled Wasm, in addition to Rust and C++. For more information, see [Prepare the plugin code](https://docs.cloud.google.com/service-extensions/docs/prepare-plugin-code#go).

]]> October 30, 2024tag:google.com,2016:service-extensions-release-notes#October_30_20242024-10-30T00:00:00-07:00Feature 

Service Extensions plugins help you insert WebAssembly (Wasm) plugins in a fully managed serverless environment directly into the data path of most Cloud Load Balancing Application Load Balancers. This feature is in **Preview**.

For details, see [Plugins for Cloud Load Balancing](https://docs.cloud.google.com/service-extensions/docs/overview#integration-lb-plugins).

]]> September 16, 2024tag:google.com,2016:service-extensions-release-notes#September_16_20242024-09-16T00:00:00-07:00Feature 

[Authorization extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#authorization-extensions) help you configure Cloud Load Balancing authorization policies to use custom authorization engines. This feature is in **Preview**.

### Feature

You can now also host an extension on a backend service that uses serverless NEGs pointing to Cloud Run services. For more information, see [Supported backends for extension services](https://docs.cloud.google.com/service-extensions/docs/callouts-overview#supported-backends).

]]> April 02, 2024tag:google.com,2016:service-extensions-release-notes#April_02_20242024-04-02T00:00:00-07:00Announcement 

Service Extensions is **Generally Available** for callout extensions for [most Google Cloud Application Load Balancers](https://docs.cloud.google.com/service-extensions/docs/callouts-overview#supported-lbs).

You can also [configure Cloud Load Balancing user-managed callout extensions](https://docs.cloud.google.com/service-extensions/docs/configure-callout) by using the Console.

]]> October 17, 2023tag:google.com,2016:service-extensions-release-notes#October_17_20232023-10-17T00:00:00-07:00Feature 

Service Extensions callouts are available for Google Cloud Application Load Balancers, excluding Classic.

With the introduction of this feature, users instruct load balancers to forward traffic from within the Cloud Load Balancing data processing path through gRPC to user-managed or partner-hosted applications. These applications can apply various policies or functions, such as header or payload manipulation, security screening, or custom logging on the traffic before returning the traffic to the load balancer for further processing.

For details, see [Cloud Load Balancing callouts overview](https://docs.cloud.google.com/service-extensions/docs/callouts-overview).

]]> October 28, 2022tag:google.com,2016:service-extensions-release-notes#October_28_20222022-10-28T00:00:00-07:00Announcement 

Initial release of [Service Extensions](https://docs.cloud.google.com/service-extensions/docs/overview).

Service Extensions helps you insert plugins inline in the Media CDN data path. You build these plugins by using WebAssembly (Wasm) and Proxy-Wasm ABI.

This product is in **Preview**.

]]>
