---
url: https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/non-distributed-quota/
title: Antipattern: Configure non-distributed quota \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:22:17.919228+00:00
---

# Antipattern: Configure non-distributed quota  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/non-distributed-quota/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Antipattern: Configure non-distributed quota Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/antipatterns/non-distributed-quota) documentation._

Apigee provides the ability to configure the number of allowed requests to an API Proxy for a specific period of time using the [Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy).

## Antipattern

An API proxy request can be served by one or more distributed Apigee components called _Message Processors_. If there are multiple Message Processors configured for serving API requests, then the quota will likely be exceeded because each Message Processor keeps it's own "count" of the requests it processes.

Let's explain this with the help of an example. Consider the following [Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy) for an API proxy:
    
    
    <!-- /antipatterns/examples/1-6.xml -->
    <Quota name="CheckTrafficQuota">
      <Interval>1</Interval>
      <TimeUnit>hour</TimeUnit>
      <Allow count="100"/>
    </Quota>

The above configuration should allow a total of 100 requests per hour.

In practice, however, when multiple message processors are serving the API requests, the following happens:

![TBD](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/antipatterns/request-to-mps.png)

In the above illustration: 

  * The quota policy is configured to allow 100 requests per hour.
  * The requests to the API Proxy are being served by two Message Processors.
  * Each Message Processor maintains its own quota count variable, `quota_count_mp1` and `quota_count_mp2`, to track the number of requests they are processing.
  * Therefore each of the Message Processor will allow 100 API requests separately. The net effect is that a total of 200 requests are processed instead of 100 requests.



## Impact

This situation defeats the purpose of the quota configuration and can have detrimental effects on the backend servers that are serving the requests.

The backend servers can:

  * Be stressed due to higher than expected incoming traffic
  * Become unresponsive to newer API requests leading to 503 errors



## Best Practice

Consider, setting the `<Distributed>` element to `true` in the [Quota policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/quota-policy) to ensure that a common counter is used to track the API requests across all Message Processors. The `<Distributed>` element can be set as shown in the code snippet below:
    
    
    <!-- /antipatterns/examples/1-7.xml -->
    <Quota name="CheckTrafficQuota">
      <Interval>1</Interval>
      <TimeUnit>hour</TimeUnit>
      <Distributed>true</Distributed>
      <Allow count="100"/>
    </Quota>

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
