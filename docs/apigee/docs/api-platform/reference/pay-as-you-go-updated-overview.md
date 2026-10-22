---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview/
title: Pay-as-you-go pricing overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:43.086368+00:00
---

# Pay-as-you-go pricing overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Pay-as-you-go pricing overview Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Apigee offers a Pay-as-you-go pricing model, making it possible to start using Apigee at a significantly reduced initial cost. With the introduction of a new lightweight API proxy and three different environment types for deployment, you can develop an API program sized specifically for your needs, with service costs based on actual usage.

Getting started with Pay-as-you-go pricing is ideal for Google Cloud customers who want to: 

  * Unlock Apigee with no upfront commitment and pay only for what you use.
  * Develop an API program starting with high value/low volume APIs.
  * Establish usage and networking patterns to monitor and control costs.
  * Maintain flexibility to right-size ongoing costs.
  * Manage and protect applications built on Google cloud infrastructure.
  * Migrate or modernize your API management services gradually without disruption.



## How does Pay-as-you-go pricing work?

When you use Apigee with Pay-as-you-go pricing, you are charged for the following: 

  * **The number of active environments per region.**

An _environment_ is a unit of infrastructure used to deploy and run an API proxy. You can choose from three different environment types, which offer different functionalities. You are charged for the use of the environment you select. To learn more about environment types, see [Apigee Pay-as-you-go environment types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-environment-types).

  * **The number of API calls to your proxies.**

You are charged for the number of API calls made to the proxies deployed in your environments. Pricing per API call is based on the [proxy type](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#proxy-types), with calls to standard API proxies costing 1/5 of calls to extensible API proxies. For more information on standard and extensible policies and their impact on API proxy type, see [ Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types). 

  * **The number of proxy deployment units used.**

A _proxy deployment unit_ describes the capacity required to deploy an [API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#whatisanapiproxy) or [shared flow](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/shared-flows) in a given environment type. Each environment type has a limited reserved capacity for these deployments, expressed in terms of proxy deployment units. You are charged for the number of proxy deployment units used in an environment, per hour, per region. For more information on the proxy deployment units available in each environment type, see  Apigee Pay-as-you-go billing rates.




Beyond the charges incurred by the Apigee resources listed above, your total cost will also include your use of Google Cloud network infrastructure. An Apigee [instance](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/instances) is available only on the network with which it is peered. You can expose the instance externally by creating a [Google Cloud load balancer](https://docs.cloud.google.com/load-balancing/docs). You pay for all related network charges (such as IP address, network data transfer, and forwarding rules) on the peered network based on actual usage. Network egress charges from Apigee instances (up to 1 TB/month) are waived until March 31, 2024 as a promotional offering.

## Apigee Pay-as-you-go billing rates

The following table lists billing rates for Pay-as-you-go pricing: 

Attribute | Base environment | Intermediate environment | Comprehensive environment  
---|---|---|---  
Standard API Proxy calls (per 1M API calls) | $20 (up to 50M calls) $16 (50M to 500M calls) $13 (>500M calls)  
Extensible API Proxy calls (per 1M API calls) | N/A | $100 (up to 50M calls) $80 (50M to 500M calls) $64 (>500M calls)  
Environment usage (per hour per region) | $0.5 | $2.0 | $4.7  
Proxy deployment units | 20 included per environment per region | 50 included per environment per region | 100 included per environment per region Additional capacity available for purchase at $0.04 per hour per region  
Apigee API Analytics add-on (per 1M Analytics API calls) | N/A | $20 | $20  
Apigee Advanced API Security add-on (per 1M Advanced API Security API calls) | N/A | $350 | $350  
**Note** : In the Pay-as-you-go pricing model, Apigee API Analytics and Advanced API Security are available as paid add-on capabilities. For more information, see [Comparison of environment types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-environment-types#compare-env-table).

## Get started with Pay-as-you-go pricing

New and existing Google Cloud customers can get up and running quickly on Apigee with Pay-as-you-go pricing. Whether you are an existing Google customer or new to Google, you can set up a billing account and install Apigee on your own. 

### Provision a new Apigee paid organization

New Apigee customers who want to use Pay-as-you-go pricing can start by installing and configuring a paid Apigee [organization](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure). We call the installation and configuration process _provisioning_.

If you are new to Google Cloud, review the [Prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/prerequisites) and set up your Cloud billing account, create a Cloud project, and install the [Google Cloud SDK](https://docs.cloud.google.com/sdk/install) before you begin.

If you are an existing Google Cloud customer, you can follow the Pay-as-you-go provisioning flow outlined in [Introduction to provisioning](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro#provisioning-options). 

### Add a Pay-as-you-go environment alongside a Subscription environment

Existing Apigee Subscription customers who want to add a Pay-as-you-go environment alongside their Subscription environments are encouraged to follow the Pay-as-you-go provisioning flow outlined in [Introduction to provisioning](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro). 

## Support for Pay-as-you-go pricing

Google Cloud Apigee customers with a **Pay-as-you-go** pricing plan can access support by signing up for a Google Cloud support plan. More information and detailed descriptions of available support plans are available from [Cloud Customer Care](https://docs.cloud.google.com/support). Once enrolled, customers can request help and submit cases in the console to [Google Cloud Support](https://cloud.google.com/support-hub).

## What's next?

For more information on using Pay-as-you-go pricing, see the following: 

  * [Monitor Pay-as-you-go billing](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-billing)
  * [View Pay-as-you-go resource usage](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-usage)
  * [Pay-as-you-go example pricing](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-examples)
  * [API Proxy types](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#proxy-types)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
