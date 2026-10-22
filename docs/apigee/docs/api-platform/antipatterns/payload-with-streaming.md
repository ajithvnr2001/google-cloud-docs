---
url: https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/payload-with-streaming/
title: Antipattern: Accessing the request/response payload when streaming is enabled \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:53.010037+00:00
---

# Antipattern: Accessing the request/response payload when streaming is enabled  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/antipatterns/payload-with-streaming/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  Antipattern: Accessing the request/response payload when streaming is enabled Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/antipatterns/payload-with-streaming) documentation._

In Apigee, the default behavior is that HTTP request and response payloads are stored in an in-memory buffer before they are processed by the policies in the API Proxy.

If streaming is enabled, then request and response payloads are streamed without modification to the client app (for responses) and the target endpoint (for requests). Streaming is useful especially if an application accepts or returns large payloads, or if there's an application that returns data in chunks over time.

## Antipattern

Accessing the request/response payload with streaming enabled causes Apigee to go back to the default buffering mode.

![Request to Message Processor Quota Polilcy to Message Processor Extract Variables to Target.
            Target to Message Processor JSONToXML to Response.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/antipatterns/payload-with-streaming.png)**Figure 1** : Accessing request/response payload with streaming enabled

The illustration above shows that we are trying to extract variables from the request payload and converting the JSON response payload to XML using JSONToXML policy. This will disable the streaming in Apigee.

## Impact

  * Streaming will be disabled which can lead to increased latencies in processing the data
  * Increase in the heap memory usage or `OutOfMemory` errors can be observed on Message Processors due to use of in-memory buffers especially if we have large request/response payloads



## Best practice

  * Don't access the request/response payload when streaming is enabled.



## Further reading

  * [Streaming requests and responses](https://docs.cloud.google.com/apigee/docs/api-platform/develop/enabling-streaming)
  * [How does Apigee streaming work?](https://www.googlecloudcommunity.com/gc/Apigee/How-does-APIGEE-Edge-Streaming-work/td-p/38511)
  * [How to handle streaming data together with normal request/response payload in a single API Proxy](https://www.googlecloudcommunity.com/gc/Apigee/How-to-handle-streaming-data-together-with-normal-request/m-p/49986)
  * [Best practices for API proxy design and development](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/best-practices-api-proxy-design-and-development)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
