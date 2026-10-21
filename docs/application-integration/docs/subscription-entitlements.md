---
url: https://docs.cloud.google.com/application-integration/docs/subscription-entitlements/
title: Subscription entitlements \u00a0|\u00a0 Application Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:17:35.874485+00:00
---

# Subscription entitlements  |  Application Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-integration/docs/subscription-entitlements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Integration ](https://docs.cloud.google.com/application-integration/docs)
  * [ Guides ](https://docs.cloud.google.com/application-integration/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Subscription entitlements

This page describes the subscription entitlement model for Application Integration, which is available as a stand-alone subscription. 

## Subscription entitlements 2024 (current plan)

The following table outlines the Application Integration subscription and add-on entitlements for the 2024 plan. For information on entitlements for the older plan, see the Subscription entitlements 2023 section. 

Subscription | Entitlements  
---|---  
**Base Subscription**  
Application Integration (Base) | 

  * 24 million Integration calls annually (1), (4)
  * 50 Application Connector units (3), (6)
  * Up to 3,600 GiB of data processing (2)
  * Up to 3,600 GiB of Connector data processing (2)

  
**Add-on Packs**  
Application Integration 50M Call Pack | 

  * Additional 50 million Integration calls annually (1)
  * Additional 2,000 GiB of data processing (2)
  * Additional 2,000 GiB of Connector data processing (2)

  
Application Connector 50 Unit Pack | 

  * Additional 50 Application Connector units (3), (6)
    * Application Connector units are an abstraction used to purchase connections. Google and technical connections use 5 units per connection, while application connections use 10 units per connection.

  
  
* * *

All offerings and add-ons are subject to [Application Integration product limits](https://cloud.google.com/application-integration/docs/quotas). You can add entitlements for Application Integration into multiple Google Cloud projects as you want without buying _Org Packs_. However, each project needs to have its own connection units, as a connection from one project cannot be used in another project. 

## Subscription entitlements 2023 (older plan)

The following table outlines the Application Integration subscription and add-on entitlements for the 2023 plan.

Subscription | Entitlements  
---|---  
**Base Subscription**  
Application Integration (Base) | 

  * 24 million Integration calls per year (1)
  * 20 Class G and 10 Class 1 connections included (6)
  * Entitles the subscription to be used in 2 organizations, which can be increased with an Org Pack.

  
**Add-on Packs**  
Application Integration Call Pack | 

  * Additional 50 million Integration calls per year (1)

  
Connector Unit Pack | 

  * Additional 50 Application Connector units (6)
    * Application Connector units are an abstraction used to purchase connections. In this pricing mode, the number of connection units necessary to use a connection depends on its class (6).

  
Concurrency Pack | 

  * 10 concurrent Integrations. Increases the limit on concurrent Integrations (5).

  
Org Pack | 

  * Access to Integration in one additional organization.

  
  
* * *

(1) Integration call: A runtime execution of an Integration flow. Similar to Integration execution in the Pay-As-You-Go (PAYG) model. Every 100 task executions counts as another Integration call. The default quota is 50 concurrent Integrations (5).  
(2) Data processing: The amount of data (in GiB) ingress or egress from an Integration execution or to and from a connection. This measures the data processed by Application Integration or by a connection and does not include any network egress charges from Google Cloud networking SKUs, which are billed separately. Additional call packs must be purchased for more data processing, even if the Integration calls are not fully consumed.  
(3) Connector or Application Connection units: An abstraction of connection purchase units. Connectors are regional resources, and configuration deployed to 2 regions counts as 2 connections. There are two classes of connections: Google and technical connections (5 units per connection, including service targets like BigQuery and technical Connectors like HTTP/FTP) and Application/3p Application connections (10 units per connection, including all other connections). All connections in the subscription model include 2 nodes for a high-availability (HA) setup with autoscaling.  
(4) Successful Integration call: The completion of an Integration workflow without errors due to the incorrect functioning of the Application Integration platform. Call failures not attributable to the platform (e.g., failures to connect to targets due to customer configuration errors) do not count against the SLA.  
(5) Concurrent Integrations: The number of integrations that are executing concurrently. This is limited to 50 concurrent Integrations by default and can be increased upon request. Please contact sales for higher limits.  
(6) Class: A class is a classification of Connectors based on the business value of the data used by the application or technology the Connector works with and/or the complexity of integrating with the Application. For example, SAP data is generally more valuable than MySQL data and is much more complex to integrate with. Please contact your Google representative for the full Connector class details.  
Incidentals: The customer is charged for incidentals like Gemini Code Assist, Secret Manager, Cloud Key Management Service, Google Cloud networking (including ILBs, PSC, and other networking products), which are billed directly from those services.  


Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
