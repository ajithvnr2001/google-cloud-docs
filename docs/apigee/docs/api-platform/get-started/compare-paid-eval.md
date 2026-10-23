---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/compare-paid-eval/
title: Compare evaluation and paid organizations in Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:08.784865+00:00
---

# Compare evaluation and paid organizations in Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/compare-paid-eval/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Compare evaluation and paid organizations in Apigee Stay organized with collections  Save and categorize content based on your preferences. 

This topic compares the lifespan, infrastructure allowances, and scaling capabilities of Apigee's free trial (evaluation) and paid organization offerings.

You can evaluate Apigee at no cost for 60 days with a trial (evaluation) Apigee organization. Evaluation organizations are an excellent way to test the functionality and feature offerings of Apigee, subject to the following limitations: 

  * Free trial (evaluation) organizations are limited to a 60-day lifespan, after which the organization is deleted.
  * Evaluation organizations are subject to Google's [Pre-GA Offerings terms](https://cloud.google.com/terms/service-terms) and should not be used for production workloads or to store sensitive data.
  * Apigee's evaluation organizations are not regularly updated with the latest Apigee features and security patches.
  * Evaluation organizations can't be converted to paid organizations.



The following table shows the key differences between Subscription, Pay-as-you-go, and evaluation organizations: 

Function | Org Type | Description  
---|---|---  
Paid/Subscription | Paid/Pay-as-you-go | Evaluation  
**Lifespan** | Based on contract | Until decommissioning of Pay-as-you-go org | 60 days |  For an eval org, you will get a notification after 30 days that its lifespan is limited. After 60 days, Google deletes the eval org. You cannot extend its lifespan. For more information, see [Apigee Pricing](https://cloud.google.com/apigee/pricing) or contact [Apigee Sales](https://pages.apigee.com/contact-sales-reg.html).   
**Requires VPC peering?** | No | No | No | You can choose to provision with or without VPC peering. See [ Apigee networking options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options).   
**Required network size with the VPC peering option** | /22 + /28 | /22 + /28 | /22 | For more information, see [Peering ranges](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/peering-ranges).  
**Required network size with the non-VPC peering option** | N/A | N/A | N/A | For more information, see [ Apigee networking options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options).   
**[Proxy access](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-routing)** | External or private/local access | External or private/local access | External or private/local access |  By default, API proxies can be accessed internally only. You can, however, configure your load balancer to accept external requests for either an eval or paid account.   
**Supported instances** | Based on contract | Billed by usage | 1 | The number of runtime instances.  
**Environments** | Based on contract | Billed by usage | 2 |  The number of runtime environments. Does not affect the number of environment groups. Apigee creates two environments during provisioning, so an eval org must delete one to create a new one.  
**Runtime fault tolerance** | Regional | Regional | Regional |  Runtimes for production and evaluation orgs use regional clustering, which means that if a zone goes down, Apigee can re-route requests to the runtimes in other zones within the region.  For more information about regions and zones, see [Regions and zones](https://docs.cloud.google.com/compute/docs/regions-zones).   
**Analytics data** | Regional | Regional | Regional |  Analytics data is regional for all.  
**Customer managed encryption keys for runtime data** | Yes | Yes | No |   
**SLA** | Yes. See [ Apigee Service Level Agreement (SLA)](https://cloud.google.com/apigee/sla) | Yes. See [ Apigee Service Level Agreement (SLA)](https://cloud.google.com/apigee/sla) | No |   
**Scalability and sizing** | Evaluation orgs have limited/restricted infrastructure. They are not suitable for performance/load testing.  
**JavaScript execution time** | Configurable | Limited to 200 ms. | For more information, see the [ JavaScript policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/javascript-policy#JavaScript).   
**Integrations and Connectors** | No | No | Based on Subscription contract 

  * Maximum execution of 500 tasks per day across all the integrations
  * Maximum of 2 integrations can run in parallel
  * You can only use the connectors supported in the Apigee eval org's region
  * Maximum of 4 connections can be created

  
**Organization policy constraints** | Yes | Yes | No | If you have CMEK organization policy constraints on your Google Cloud project, Apigee will enforce compliance with those constraints, guide you in choosing a valid configuration, and prevent you from using Apigee features that are not CMEK compliant.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
