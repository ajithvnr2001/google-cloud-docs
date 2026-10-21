---
url: https://docs.cloud.google.com/cdn/docs/integration-with-service-extensions/
title: Use Service Extensions for edge compute \u00a0|\u00a0 Cloud CDN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:29:50.852663+00:00
---

# Use Service Extensions for edge compute  |  Cloud CDN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cdn/docs/integration-with-service-extensions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud CDN ](https://docs.cloud.google.com/cdn/docs)
  * [ Guides ](https://docs.cloud.google.com/cdn/docs/overview)



Send feedback 

#  Use Service Extensions for edge compute Stay organized with collections  Save and categorize content based on your preferences. 

You can use [Service Extensions](https://docs.cloud.google.com/service-extensions/docs/overview) to run your own [WebAssembly (Wasm)](https://webassembly.org/) code in a fully serverless, Google-managed compute environment. This page describes extensibility by using Service Extensions.

## About Service Extensions edge extensions for Cloud CDN

You build plugins using Wasm and the [Proxy-Wasm ABI](https://github.com/proxy-wasm). The Proxy-Wasm ABI offers support for Rust, C++, and Go. [Service Extensions plugins](https://docs.cloud.google.com/service-extensions/docs/plugins-overview) run on a fully serverless, Google-managed infrastructure. They run close to the data plane, and latency optimization is managed. Service Extensions plugins are intended for lightweight use cases with tight limits on CPU and memory.

As the following diagram shows, you attach Service Extensions plugins to global external Application Load Balancer by using [edge extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#edge-extensions) and [traffic extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#traffic-extensions) at different stages of the networking data path.

[ ![Extensibility in the networking data path.](https://docs.cloud.google.com/static/cdn/images/cdn-overview-response-flow.svg)](https://docs.cloud.google.com/static/cdn/images/cdn-overview-response-flow.svg) Extensibility in the networking data path (click to enlarge).

## Common use cases

Use Service Extensions plugins with global external Application Load Balancers in the following sample scenarios:

**Custom traffic steering**
    Manipulate request headers to influence backend service selection.
**Cache optimization**
    Influence which content is served from a Cloud CDN cache.
**Exception handling**
    Redirect clients to a custom error page for certain response classes.
**Custom logging**
    Log user-defined headers or custom data into Cloud Logging.
**Header addition**
    Create new headers relevant for your applications or specific customers.
    Insert new headers for request.
**Header manipulation**
    Rewrite existing request headers or override client headers on their way to the backend.
**Security**
    Write custom security policies based on client requests and make enforcement decisions within your plugin.

## Get started

  1. [Create a plugin](https://docs.cloud.google.com/service-extensions/docs/create-plugin)
  2. [Configure an edge extension](https://docs.cloud.google.com/service-extensions/docs/configure-edge-extensions)



## What's next

  * Learn more about [Service Extensions](https://docs.cloud.google.com/service-extensions/docs/overview) concepts.
  * View Rust, Go, and C++ plugin examples and testing tools in the [Service Extensions GitHub repository for plugins](https://github.com/GoogleCloudPlatform/service-extensions/tree/main/plugins#docs).
  * Learn how to [prepare and upload the files required](https://docs.cloud.google.com/service-extensions/docs/access-control) to create plugins by using Service Extensions.
  * Learn how to [create a plugin](https://docs.cloud.google.com/service-extensions/docs/create-plugin).
  * Learn how to [configure an edge extension](https://docs.cloud.google.com/service-extensions/docs/configure-edge-extensions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
