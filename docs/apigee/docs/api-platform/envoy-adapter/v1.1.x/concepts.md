---
url: https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.1.x/concepts/
title: Apigee Adapter for Envoy overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:08:09.039236+00:00
---

# Apigee Adapter for Envoy overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.1.x/concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Apigee Adapter for Envoy overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## What is Apigee Adapter for Envoy?

Apigee Adapter for Envoy is an Apigee-managed API gateway that uses [Envoy](https://www.envoyproxy.io/docs/envoy/latest/intro/what_is_envoy) to proxy API traffic. Envoy is a popular, open source edge and service proxy designed for cloud-native applications. You can run Apigee Adapter for Envoy on premises or in a multi-cloud environment.

With Apigee Adapter for Envoy, you get a relatively small footprint API gateway application running close to your backend applications. Apigee Adapter for Envoy relies on Apigee for:

  * API authentication and authorization (with API keys and OAuth)
  * Quota management
  * API analytics



**Watch videos:**

This video offers an overview and demo of Google Cloud's Apigee Adapter for Envoy.

This video describes using the Apigee Adapter for Envoy with Service Mesh.

##  Installation options 

You can use the Apigee Adapter for Envoy in the following context: 

  * As a service deployed to the Istio service mesh integrated with Apigee hybrid. See [ Using Apigee Adapter for Envoy with Apigee hybrid](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.1.x/example-hybrid).



##  Apigee Adapter for Envoy 

The following figure shows the high level architecture for Apigee Adapter for Envoy. This architecture consists of management plane components deployed on Google Cloud Platform (GCP) and data plane components running remotely on premises or in a cloud provider environment. The data plane includes the Envoy proxy and Apigee Remote Service. The role of each component is described following the figure. 

![A high-level
  view of the Envoy Adapter integrated into an Apigee hybrid environment, including the management plane, runtime plane, and GCP services](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/envoy-adapter-hybrid.png)

  1. A consumer or client app accesses an API endpoint exposed by the Envoy proxy.
  2. The Envoy proxy passes the security context (using HTTP headers) to the Apigee Remote Service. The Apigee Remote Service acts as a policy decision point (PDP) and advises Envoy to allow or deny access to the API consumer for the request.
  3. If the call is allowed, the Envoy proxy forwards the request to the backend.
  4. The Apigee Remote Service asynchronously polls the management plane and downloads proxy, API product, and other configuration that it needs to operate.



## Why use Apigee Adapter for Envoy?

Moving the API management component close to backend target applications can reduce network latency. While you can install Apigee hybrid in a private data center, a full deployment of Apigee hybrid is necessarily large and complex to support its full feature-set and data-heavy features like key management, monetization, and analytics. This means that deploying Apigee hybrid on premises in each data-center is not always desirable.

Benefits of using Apigee Adapter for Envoy include:

  * Reduced latency of API traffic for services that run in close proximity.

  * Use of the full suite of Apigee Analytics metrics, dashboards, and APIs.
  * Keeps API traffic within the enterprise-approved boundaries for security or compliance purposes.
  * Asynchronous communication with Apigee allows API traffic data to be captured and sent to Apigee without affecting latency.
  * The adapter can tolerate temporary communication interruptions with the management plane. Over time, however, an interruption can lead to loss of functionality. The adapter requires communication with the management plane for: 
    * Generating OAuth tokens
    * Verifying API keys (connection is required for the first verification, after which it is cached)
    * Enforcing quotas
    * Sending analytics data to the management plane



##  Next step 

[Install Apigee Adapter for Envoy](https://docs.cloud.google.com/apigee/docs/api-platform/envoy-adapter/v1.1.x/getting-started)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
