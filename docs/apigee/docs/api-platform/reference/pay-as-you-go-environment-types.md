---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-environment-types/
title: Apigee Pay-as-you-go environment types \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:54.362624+00:00
---

# Apigee Pay-as-you-go environment types  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-environment-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Apigee Pay-as-you-go environment types Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Apigee's Pay-as-you-go pricing attributes are based in part upon the _environment types_ you attach to your [Apigee instance](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-working-with#environments-and-instances). An _environment_ is a unit of infrastructure within an organization where you can [create](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-proxy) and [deploy API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/deploy-proxy). When you provision an Apigee organization using the Pay-as-you-go pricing model, an Intermediate environment is created in your organization. After the organization is provisioned, you can add additional environments of any type to your organization.

The Apigee Pay-as-you-go pricing model introduces three different types of deployment environments, with varying costs: 

  * Base environment
  * Intermediate environment
  * Comprehensive environment



With the ability to use multiple types of environments in a single organization, you can create a pricing scheme tailored to your usage. This topic addresses the features, limitations, and recommended use cases for each environment type.

## Base environment type

When you select a _Base environment_ to attach to your Apigee instance, you can do the following: 

  * Deploy and run [Standard API Proxies](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#proxy-types).
  * Utilize [Apigee API monitoring](https://docs.cloud.google.com/apigee/docs/api-monitoring) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs).
  * Access Apigee proxy development tools.
  * Leverage other Google Cloud services.
  * Register your APIs with Apigee's [API Hub](https://docs.cloud.google.com/apigee/docs/api-hub/what-is-api-hub) _(Preview)_.



As the lowest-cost environment type, the Base environment is recommended for the following API management use cases: 

  * Proxying API traffic for prototyping, internal development, or small-scale applications.
  * Onboarding your program to Apigee and maintaining low ongoing costs.
  * Implementing a fully-managed gateway with the option to add advanced capabilities when required.



## Intermediate environment type

With an _Intermediate environment_ attached to your Apigee instance, you can access all the functionality of the Base environment type, along with the following: 

  * Deploy and run [Extensible API Proxies](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#proxy-types) and Standard API Proxies.
  * Create [API products](https://docs.cloud.google.com/apigee/docs/api-platform/publish/what-api-product) and publish those products in a [developer portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/intro-portals).
  * Access add-on Apigee capabilities available for purchase like [Apigee API Analytics](https://docs.cloud.google.com/apigee/docs/api-platform/analytics/analytics-services-overview), [Advanced API Security](https://docs.cloud.google.com/apigee/docs/api-security), and [Monetization](https://docs.cloud.google.com/apigee/docs/api-platform/monetization/overview)*.



With these expanded capabilities, the Intermediate environment is recommended for the following API management use cases: 

  * Building and publishing API products for developers.
  * Managing a portfolio of APIs with growing adoption.
  * Performing complex transformations or mediations in your API traffic.



* The Monetization add-on is currently unavailable for purchase.

## Comprehensive environment type

If you attach a _Comprehensive environment_ to your Apigee instance, you can access all the functionality of the Intermediate environment type, along with the ability to do following: 

  * Perform at-scale deployments with multiple regions.
  * Purchase additional proxy deployments per environment.
  * Access high-performance operational tools like auto-scaling QPS, [debug masking](https://docs.cloud.google.com/apigee/docs/api-platform/security/data-masking), and [distributed tracing](https://docs.cloud.google.com/apigee/docs/api-platform/develop/enabling-distributed-trace) _(Preview)_.



The Comprehensive environment is recommended for API management use cases that require: 

  * Supporting mission critical applications with high reliability and performance.
  * Maintaining precision control over API operations.



## Comparison of environment types

The following table provides a comparison of the features and limitations of each environment type: 

| Base | Intermediate | Comprehensive  
---|---|---|---  
Max environment per org | 5 | 5 | Up to limit (85)  
Standard API Proxy | Yes | Yes | Yes  
Extensible API Proxy | No | Yes | Yes  
Shared Flows | N/A | Available | Available  
Proxy deployment units* per environment per region | 20 included per environment | 50 included per environment | 100 included per environment, ability to purchase up to limit (6000)  
API Products and Developer Portals | N/A | Available | Available  
Add-ons | N/A | Apigee API Analytics, Advanced API Security, Monetization** (for purchase)  | Apigee API Analytics, Advanced API Security, Monetization** (for purchase)   
Max throughput | Up to 50 QPS | Up to 100 QPS | Autoscaled QPS  
Multi-region support | N/A | N/A | Available  
SLA | up to 99% | up to 99% | 99.9% for environments deployed to 1 region 99.99% for environments deployed to 2 or more regions  
  
* Proxy deployment unit = 1 API proxy (standard or extensible) _or_ 1 shared flow revision deployment.

** The Monetization add-on is currently unavailable for purchase.

## Add or remove environments

If you have an Apigee organization provisioned with Pay-as-you-go pricing, you can create additional environments of any type, up to the limits specified in Comparison of environment types.

When you [ create a new environment](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-working-with#create), you can deploy any existing proxies to the new environment. If an environment is no longer required, you can undeploy your proxies and [delete the environment](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-working-with#delete) to prevent any Pay-as-you-go charges from accruing.

## Update types for existing environments

Alternatively, you can upgrade or downgrade the type of an existing environment to add or remove feature capabilities and manage your Apigee Pay-as-you-go billing and resource usage. 

For example, you can: 

  * Upgrade a **Base** environment type to an **Intermediate** environment type to use Shared Flows in your deployments.
  * Downgrade an **Intermediate** environment that contains only Standard API proxies to a **Base** environment type to decrease environment usage costs.



For more information on using the Apigee APIs or Apigee UI in the Google Cloud console to change the type of an existing environment, see [Update Pay-as-you-go environment types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/update-environment-types).

If your API management program grows beyond the capabilities provided by the Comprehensive environment type, you can speak to your Google Cloud sales specialist about available [ Subscription pricing plans](https://cloud.google.com/contact?direct=true&pre_product=apigee). 

## What's next?

For more information about environment types, see: 

  * [About environments and environment groups](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/environments-overview)
  * [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)
  * [Pay-as-you-go FAQ](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-faq)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
