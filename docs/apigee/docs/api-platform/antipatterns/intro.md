---
url: https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/intro/
title: Introduction to antipatterns \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:49.363241+00:00
---

# Introduction to antipatterns  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/intro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Introduction to antipatterns Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/antipatterns/intro) documentation._

This section is about common antipatterns that arise when API proxies are deployed on Apigee.

## What is an antipattern?

An [_antipattern_](https://en.wikipedia.org/wiki/Anti-pattern) is a software design practice that is ineffective or counterproductive—in other words, the opposite of a "best practice." To put it another way, an antipattern is something that the software allows you to do, but that may have an adverse functional or performance impact.

For example, consider the omnipotent-sounding "God Class/Object". In objected oriented programming, a _god class_ is a class that controls too many classes for a given application, as illustrated by the following reference tree:

![TBD](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/antipatterns/godclass.png)**Figure 1** : God class

As the image illustrates, the god class uses and references too many classes.

The framework on which the application was developed does not prevent the creation of such a class, but it has many disadvantages, the primary ones being:

  * Hard to maintain
  * Single point of failure when the application runs



Consequently, such a class is an antipattern that you should avoid creating.

The good news is that you can identify these antipatterns and rectify them with appropriate best practices, which will make the APIs you deploy on Apigee best serve their intended purpose.

## Summary of antipatterns

The following table lists some common API antipatterns:

Category | Antipatterns  
---|---  
Policy antipatterns | 

  * [Issuing refresh tokens without invoking refresh flow](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/issuing-refresh-tokens)
  * [Use waitForComplete() in JavaScript code](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/wait-for-complete)
  * [Set a long expiration time for OAuth tokens](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/oauth-long-expiration)
  * [Use greedy quantifiers in the RegularExpressionProtection policy](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/greedy-quantifiers)
  * [Cache error responses](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/caching-error)
  * [Store data greater than 256 KB size in cache](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/caching-large)
  * [Invoke MessageLogging multiple times in an API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/messagelogging-multiple-times)
  * [ High-cardinality identifiers in Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/high-cardinality-identifiers-quota-policy)
  * [Configure non-distributed quota](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/non-distributed-quota)
  * [Reuse a Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/reusing-quota)
  * [Use the RaiseFault policy under inappropriate conditions](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/raise-fault-conditions)
  * [Access multi-value HTTP headers incorrectly in an API Proxy](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/multi-value-http-headers)
  * [Use Service Callout to invoke backend service in no target proxy](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/service-callout-no-target)

  
Generic antipatterns | 

  * [Invoke Management API calls from an API Proxy](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/invoking-management)
  * [Invoke a proxy within a proxy using custom code or as a target](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/proxy-within-proxy)
  * [Manage Apigee resources without using source control management](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/no-source-control)
  * [Load Balance with a single target server with MaxFailures set to a non-zero value](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/load-balancing-maxfailures)
  * [Access the request/response payload when streaming is enabled](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/payload-with-streaming)
  * [Define multiple ProxyEndpoints in an API Proxy](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/multiple-proxyendpoints)

  
Backend antipatterns | 

  * [Allow a slow backend](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/slow-backend)
  * [Disable HTTP persistent (reusable keep-alive) connections](https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/disable-persistent-connections)

  
  
### Download antipatterns eBook

In addition to the links above, you can also download the antipatterns in eBook format:

  * [The Book of Apigee Antipatterns v2.0 (PDF)](https://docs.apigee.com/files/Apigee_Edge_Antipatterns_2_0.pdf)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
