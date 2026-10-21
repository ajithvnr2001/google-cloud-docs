---
url: https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/high-cardinality-identifiers-quota-policy/
title: Antipattern: Use high-cardinality identifiers in Quota policies \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:18.567348+00:00
---

# Antipattern: Use high-cardinality identifiers in Quota policies  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/high-cardinality-identifiers-quota-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Antipattern: Use high-cardinality identifiers in Quota policies Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/antipatterns/high-cardinality-identifiers-quota-policy) documentation._

The [ Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy) is used to count the number of requests received by an API proxy. This capability enables API providers to enforce limits on the number of API calls made by apps over an interval of time. 

The Quota policy can include an [ `identifier`](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy#identifier) element that identifies the quota "bucket" in which each request is counted. 

## Antipattern

When using the Quota policy, do not use high-cardinality identifiers. 

Cardinality refers to the number of unique data values in a set. An identifier with high cardinality has a large number of distinct possible values. High-cardinality identifiers include unique request IDs or session IDs that change with every API call. 

Using high-cardinality identifiers can significantly undermine the effectiveness of your quota enforcement. 

## Impact

Using high-cardinality identifiers for your quota policy's identifier element causes: 

  * **Ineffective Quota Enforcement:** Each unique identifier is treated as a separate counter. If every request has a new, unique ID, your quota system essentially creates a new "bucket" for every API call. This means your overall quota limit is measured against individual, single-use counters rather than by actual groups of requests you want to limit, rendering the policy useless for traffic control. 
  * **Increased Resource Consumption:** Generating and managing a massive number of unique quota counters places unnecessary strain on the Apigee platform, leading to increased resource usage and potential performance issues. 
  * **Monitoring Challenges:** It becomes difficult to monitor and understand actual API consumption trends when the data is fragmented across large numbers of unique identifiers. You lose the ability to see which applications, developers, or products are consuming your API resources. 



## Best practice

Choose identifiers with low to medium cardinality that also represent a stable and meaningful grouping for quota enforcement. These help you manage API usage effectively and gain insights into your traffic. Examples include: 

  * developer.app.name
  * client_id
  * apiproduct.name



With appropriate identifiers, your Quota policy can more effectively manage API traffic, prevent unintended overages, and provide clear insights into usage patterns. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
