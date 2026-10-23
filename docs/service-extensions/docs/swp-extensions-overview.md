---
url: https://docs.cloud.google.com/service-extensions/docs/swp-extensions-overview/
title: Secure Web Proxy extensions overview \u00a0|\u00a0 Service Extensions \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:34:06.564473+00:00
---

# Secure Web Proxy extensions overview  |  Service Extensions  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-extensions/docs/swp-extensions-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Service Extensions ](https://docs.cloud.google.com/service-extensions/docs)
  * [ Guides ](https://docs.cloud.google.com/service-extensions/docs/overview)



Send feedback 

#  Secure Web Proxy extensions overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Secure Web Proxy provides centralized, policy-based control for your organization's outbound web traffic. Service Extensions extensions for Secure Web Proxy help you insert your custom services directly into the Secure Web Proxy traffic processing path by using callouts. This page provides an overview about Secure Web Proxy extensions.

Secure Web Proxy supports [authorization extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#authorization-extensions) by using callouts.

## How Secure Web Proxy extensions work

Service Extensions callout extensions can send gRPC callouts from the traffic processing path to custom services.

[ ![Secure Web Proxy uses callouts to add custom services in the traffic processing path.](https://docs.cloud.google.com/static/service-extensions/images/swp-processing-path.svg)](https://docs.cloud.google.com/static/service-extensions/images/swp-processing-path.svg) Secure Web Proxy uses callouts to custom services in the traffic processing path (click to enlarge).

By making a real-time gRPC call to an external service that you manage, you can inspect, modify, or even block traffic before it continues to its destination. This feature transforms Secure Web Proxy into a programmable platform that helps you integrate your outbound data transfer flows and AI agent flows with specialized security providers, implement custom authentication or authorization solutions, and enforce bespoke business logic.

Service Extensions for Secure Web Proxy supports the use of [authorization extensions](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview#authorization-extensions) to intercept and evaluate requests and content that pass through a Secure Web Proxy instance.

When a client sends an outbound data transfer request through a Secure Web Proxy instance, the extension inspects the data based on the the configured [authorization policy](https://docs.cloud.google.com/load-balancing/docs/auth-policy/auth-policy-overview).

In the data path, authorization policies are evaluated after performing TLS interception on the inner payload. Authorization extensions based on request authorization policies run before those based on content authorization policies.

## What's next

  * [Cloud Load Balancing callouts overview](https://docs.cloud.google.com/service-extensions/docs/callouts-overview)
  * [Configure an extension for Secure Web Proxy](https://docs.cloud.google.com/service-extensions/docs/configure-extensions-for-swp)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
