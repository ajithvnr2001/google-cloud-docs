---
url: https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-overview/
title: Apigee Extension Processor overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:15.668037+00:00
---

# Apigee Extension Processor overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Apigee Extension Processor overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The Apigee Extension Processor lets Apigee customers add API management capabilities to Google Cloud products and services, or external services, exposed using Cloud Load Balancing. 

To get started using the Apigee Extension Processor, see the [ Apigee Extension Processor quickstart](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-quickstart).

## Use cases for the Apigee Extension Processor

Apigee customers using the Extension Processor can select from a range of Apigee policies that apply API management capabilities to any products or services exposed using a Google Cloud load balancer.

With the Extension Processor, you can: 

  * **Secure access to Google Cloud workloads.**

Choose from a wide range of Apigee policies to apply to your load balancer traffic, including [VerifyApiKey](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-api-key-policy), [OAuthV2](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy), and [VerifyJWS](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/verify-jws-policy).

  * **Apply quota enforcement to network traffic.**

This capability lets API providers enforce limits on the number of API calls made to backend services over a specified time period. For example, you can use the [Quota](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy) policy to limit calls to 1 request per minute, or to 10,000 requests per month.

  * **Manage Google token injection for authenticating requests.**

Using the Extension Processor and the [AssignMessage](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/assign-message-policy) policy, you can inject a [Google access token](https://docs.cloud.google.com/docs/authentication/token-types#access) or [Google ID token](https://docs.cloud.google.com/docs/authentication/token-types#id) into client request headers to manage access to Google-authenticated backend services and products.

  * **Support native protocols.**

The Extension Processor unlocks support for native protocols such as [gRPC bi-directional streaming](https://grpc.io/docs/what-is-grpc/core-concepts/#service-definition), [server-sent events (SSE)](https://docs.cloud.google.com/apigee/docs/api-platform/develop/server-sent-events), and [HTTP/3](https://docs.cloud.google.com/load-balancing/docs/https#QUIC).




## Benefits

In addition to supporting the use cases described earlier, the Extension Processor provides all the benefits of built-in Apigee features, such as: 

  * **Security** : Advanced API Security continually monitors and analyzes your API traffic to identify suspicious API requests and provides tools to block or flag those requests.
  * **Monetization** : Generate revenue whenever your APIs are used by adding rate plans to customized API products you create within Apigee.
  * **Traceability** : Apigee's distributed tracing system lets you track requests in distributed systems across multiple applications, services, and databases, and proxies. 
  * **Business intelligence** : Apigee API Analytics collects the wealth of information flowing through your load balancer, providing data visualization in the UI or the ability to download data for offline analysis.



## How Apigee Extension Processor works

The Apigee Extension Processor is a traffic extension (a type of [service extension](https://docs.cloud.google.com/service-extensions/docs/lb-extensions-overview)) that lets you use Cloud Load Balancing to send callouts to Apigee from the data processing path of the application load balancer. Once the application load balancer and service extension are configured, traffic flowing through the application load balancer will trigger calls to Apigee proxies using the service extension, as shown in the following figure: ![Flow diagram for the Apigee extension processor](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/ext-proc-setup-3-full.png)**Figure 1** : Infrastructure and dataflow for the Apigee Extension Processor.

The diagram outlines the required components of the Apigee Extension Processor configuration: 

  * An Application Load Balancer with a backend service configured with a Network Endpoint Group (NEG) covering all application backends.
  * An Apigee instance with a dedicated environment for the Extension Processor and the property `apigee-service-extension-enabled` set to `true`.
  * A [traffic extension](https://docs.cloud.google.com/service-extensions/docs/configure-traffic-extensions) (a type of service extension) configured to use a Private Service Connect endpoint to connect to the Apigee runtime plane.
  * An [Apigee API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/build-simple-api-proxy) running in a special environment. The proxy is used to apply API management capabilities to the load balancer traffic. The Extension Processor supports the use of **no-target** and **Server-sent event (SSE)-enabled** proxies.



As shown in the flow diagram: 

  * **1** : The client sends a request to the Application Load Balancer.
  * **2** : The Application Load Balancer reviews the traffic and calls out to the Service Extension.
  * **3** : The Service Extension implementation in the Apigee message processor applies any relevant API management policies and returns the request, with any modifications, to the Application Load Balancer.
  * **4** : The Application Load Balancer completes processing and forwards the request to the backend service. Similar processing occurs for the response path from the backend service to the Application Load Balancer and to the client.



For more information, see [Cloud Load Balancing extensions](https://docs.cloud.google.com/service-extensions/docs/overview#integration-lb-callouts).

## Limitations

The Apigee Extension Processor has the following known limitations:

  * The Extension Processor is applied at the load balancer level. All traffic passing through the load balancer is processed by the same proxy, with no base path or URL distinction.
  * Traffic through the Extension Processor is subject to the same quotas as the Cloud Load Balancing. 

Relevant limits and quotas include the following: 

    * Maximum number of traffic extensions per load balancer: 1
    * Maximum traffic extensions per project: 100
    * Maximum extension chains per project: 5
    * Maximum extensions per resource: 3

For more information, see [Quotas and limits](https://docs.cloud.google.com/load-balancing/docs/quotas).

  * Additional limits apply to environments, environment groups, and API proxies when using the Extension Processor: 
    * A maximum of **one** environment can be attached to the environment group used to configure the Extension Processor.
    * The environment used when configuring the Extension Processor can have a maximum of **50** API proxies deployed.
    * The API proxies deployed in the dedicated environment for the Extension Processor must all be of the same [_proxy type_](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#proxy-types). The API proxies must be either all **standard** API proxies or all **extensible** API proxies. Standard and extensible API proxies can't be mixed in the Extension Processor environment.

For more information, see [Create an Apigee environment](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-quickstart#create-apigee-environment).

For more information on Apigee limits generally, see [Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits).

  * The following Apigee policies are not supported for use with the Extension Processor: 
    * [Publish message](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/publish-message-policy)
    * [ExternalCallout](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/external-callout-policy)
    * [IntegrationCallout](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/integration-callout-policy)
    * [ServiceCallout](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/service-callout-policy)
    * [SetIntegrationRequest](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-integration-request-policy)
    * [MessageLogging](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/message-logging-policy)
    * [GenerateJWT](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/generate-jwt-policy)

**Note:** If you are using the Extension Processor with SSE-enabled proxies, note that the Extension Processor does not support the use of the `PublishMessage` or `MessageLogging` policies within `EventFlows`.

## Pricing

In addition to costs associated with your Apigee Subscription or Pay-as-you-go pricing plans, the following networking costs may apply when using Apigee Extension Processor: 

  * [Service Extensions pricing](https://docs.cloud.google.com/service-extensions/pricing)
  * [Backend service pricing](https://cloud.google.com/vpc/network-pricing#lb)
  * [Private Service Connect charges](https://cloud.google.com/vpc/network-pricing#psc-consumer-data-processing)



## What's next

  * Learn how to [Get started with the Apigee Extension Processor](https://docs.cloud.google.com/apigee/docs/api-platform/service-extensions/extension-processor-quickstart).
  * Learn more about working with [Service Extensions](https://docs.cloud.google.com/service-extensions/docs/overview).
  * Explore how Apigee Extension Processor works with the [ Apigee Operator for Kubernetes](https://docs.cloud.google.com/apigee/docs/api-platform/apigee-kubernetes/apigee-apim-operator-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
