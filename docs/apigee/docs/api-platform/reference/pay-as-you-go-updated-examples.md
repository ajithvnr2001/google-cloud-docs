---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-examples/
title: Pay-as-you-go example pricing \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:02.290394+00:00
---

# Pay-as-you-go example pricing  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-examples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Resources ](https://docs.cloud.google.com/apigee/docs/release-notes)



Send feedback 

#  Pay-as-you-go example pricing Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

When you use Pay-as-you-go pricing for Apigee, you are charged for the following: 

  * The number of active environments per region.
  * The number of API calls to your proxies.
  * The number of proxy deployment units used.



The following examples show how the number and type of active environments used in your configuration, the number of API calls made to your proxies, and the number of proxy deployment units used can impact your projected costs. These examples include estimated network charges. Inbound and outbound network data transfer charges depend on the source and destination. For a current price list, see [ All networking pricing](https://cloud.google.com/vpc/network-pricing).

To generate a cost estimate for Pay-as-you-go, you can use the [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator). For more information about using the calculator for Apigee Pay-as-you-go, see [Use the Google Cloud pricing calculator](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-billing#calculator).

## Example 1

This example shows the estimated monthly charges where a customer creates an Apigee organization with **one** active Base environment used for development. In this scenario, the customer has **15 Standard API proxies** deployed in one region. Within a month, the customer expects **500K Standard API calls**.

Category  | Units  | Calculation  | Monthly Charge   
---|---|---|---  
**Active environments** | 1 | 1 active Base environment * $365 per month per region Base environment includes up to 20 proxy deployments | $365  
**API calls** | 0.5M Standard API calls | Standard: 0.5M * $0.00002/call  | $10   
**Payload and Network Traffic** | 1 TiB 25M calls | LB forwarding rules and network data transfer*: $27 Private Service Connect (Traffic between Private Service Connect NEG and the published service): $11 | $38  
|  | **Total per month (est.)** | $413  
  
## Example 2

This example shows the estimated monthly charges where a customer creates an Apigee organization with **three** active Intermediate environments. The customer has fewer than **50** Standard and Extensible API proxy deployments in each environment, in a single region. In this scenario, the customer expects **25M API calls per month** (10M in Standard API proxy calls and 15M in Extensible API proxy calls).

Category  | Units  | Calculation  | Monthly Charge   
---|---|---|---  
**Active environments** | 3 | 3 active Intermediate environments * $1460 per month per region Intermediate environment includes up to 50 proxy deployments | $4,380  
**API calls** | 10M Standard API calls 15M Extensible API calls | Standard: 10M * $0.00002/call Extensible: 15M * $0.0001/call | $200 $1,500  
**Payload and Network Traffic** | 1 TiB 25M calls | LB forwarding rules and network data transfer*: $46 Private Service Connect (Traffic between Private Service Connect NEG and the published service): $35 | $81  
|  | **Total per month (est.)** | $6,161  
  
## Example 3

This example shows pricing for a multi-region deployment. In this scenario, the customer has an Apigee organization with **two** active Comprehensive environments. The customer has **120** Standard and Extensible API proxy deployments in each environment, in two regions. The customer expects **500M API calls per month** (100M Standard API proxy calls and 400M Extensible API proxy calls).

Category  | Units  | Calculation  | Monthly Charge   
---|---|---|---  
**Active environments** | 2 | 2 active Comprehensive environments * $3,431 per month per region * 2 regions Comprehensive environment includes up to 100 proxy deployments | $13,724  
**Proxy overage usage** | 20 overage | 2 Comprehensive environments * 2 regions * 20 proxy deployments per region * $29.29/month  | $2,336  
**API calls** | 100M Standard API calls 400M Extensible API calls | Standard: (50M * $0.00002/call) + (50M * $0.000016/call) Extensible: (50M * $0.0001/call) + (350M * $0.00008/call) | $1,800 $33,000  
**Payload and Network Traffic** | 1 TiB 500M calls | LB forwarding rules and network data transfer*: $426 Private Service Connect (Traffic between Private Service Connect NEG and the published service): $510 | $936  
|  | **Total per month (est.)** | $51,796  
  
## Example 4

This example shows pricing for a multi-region deployment with the Apigee API Analytics add-on. In this scenario, the customer has an Apigee organization with **one** active Comprehensive environment. The customer has **80** Standard and Extensible API proxy deployments in three regions. The customer expects **100M API calls per month** (25M Standard API proxy calls and 75M Extensible API proxy calls).

Category  | Units  | Calculation  | Monthly Charge   
---|---|---|---  
**Active environments** | 1 | 1 active Comprehensive environment * $3,431 per month per region * 3 regions Comprehensive environment includes up to 100 proxy deployments | $10,293  
**API calls** | 25M Standard API calls 75M Extensible API calls | Standard: (25M * $0.00002/call) Extensible: (50M * $0.0001/call) + (25M * $0.00008/call) | $500 $7000  
**Add-on: Apigee API Analytics** | Analytics API calls | 100M | Apigee API Analytics add-on: 100M * $0.00002/hr | $2,000  
**Payload and Network Traffic** | 1 TiB 100M calls | LB forwarding rules and network data transfer*: $106 Private Service Connect (Traffic between Private Service Connect NEG and the published service): $110 | $216  
|  | **Total per month (est.)** | $20,009  
  
* Network data transfer charges depend on source and destination. For a full price list, see [All networking pricing](https://cloud.google.com/vpc/network-pricing).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
