---
url: https://docs.cloud.google.com/secure-web-proxy/docs/distributed-tracing-overview/
title: Distributed tracing overview \u00a0|\u00a0 Secure Web Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:09:14.497827+00:00
---

# Distributed tracing overview  |  Secure Web Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-web-proxy/docs/distributed-tracing-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Web Proxy ](https://docs.cloud.google.com/secure-web-proxy/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-web-proxy/docs/quickstart)



Send feedback 

#  Distributed tracing overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Distributed tracing for Secure Web Proxy provides end-to-end request visibility for outbound web traffic that passes through your proxy gateways to external APIs and third-party services.

Secure Web Proxy integrates with [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview) to capture detailed timing insights and request attributes for each outbound connection. This information helps you detect latency bottlenecks and troubleshoot connectivity errors.

## Key benefits

Distributed tracing with Trace provides the following key benefits:

  * **End-to-end request lifecycle visibility** : track outbound requests from internal workloads through Secure Web Proxy to external endpoints.
  * **Decoupled telemetry policies** : define trace sampling rates in independent `TelemetryPolicy` resources without modifying proxy routing or security rules.
  * **Cross-telemetry correlation** : correlate Trace with Secure Web Proxy [proxy transaction logs](https://docs.cloud.google.com/secure-web-proxy/docs/view-proxy-transaction-logs) and Cloud Monitoring metrics by using unified trace IDs.



## Architecture of telemetry policies

Distributed tracing for Secure Web Proxy is managed by using `TelemetryPolicy` resources in the Network Services API.

The key architectural principles include the following:

  * **Regional policy management** : telemetry policies for Secure Web Proxy are regional resources and are created and managed in the same region as the target gateways.
  * **Independent lifecycle** : telemetry policies are separate from gateway security policies and rules. You can create, modify, or delete telemetry policies without affecting how the gateway handles traffic or security.
  * **Multi-gateway targeting** : a single telemetry policy can target multiple Secure Web Proxy gateways within the same region, ensuring consistent tracing standards across several regional deployments.



## Parent-based sampling

Parent-based sampling provides dynamic control over trace collection based on upstream sampling decisions. When you enable parent-based sampling, Secure Web Proxy automatically samples requests if the incoming trace context indicates that the upstream client or microservice has already decided to sample the trace.

For requests that don't carry upstream trace context, Secure Web Proxy applies the baseline `samplingRate` configured in the telemetry policy.

## What's next

  * [Trace outbound traffic with Cloud Trace](https://docs.cloud.google.com/secure-web-proxy/docs/monitor-traces)
  * [Troubleshoot distributed tracing errors](https://docs.cloud.google.com/secure-web-proxy/docs/troubleshoot-distributed-tracing-errors)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
