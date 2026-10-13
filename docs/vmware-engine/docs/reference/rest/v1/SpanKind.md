---
url: https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/SpanKind/
title: SpanKind \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:59.696269+00:00
---

# SpanKind  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/reference/rest/v1/SpanKind/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)



Send feedback 

#  SpanKind Stay organized with collections  Save and categorize content based on your preferences. 

Type of span. Can be used to specify additional relationships between spans in addition to a parent/child relationship.

Enums  
---  
`SPAN_KIND_UNSPECIFIED` | Unspecified. Do NOT use as default. Implementations MAY assume SpanKind.INTERNAL to be default.  
`INTERNAL` | Indicates that the span is used internally. Default value.  
`SERVER` | Indicates that the span covers server-side handling of an RPC or other remote network request.  
`CLIENT` | Indicates that the span covers the client-side wrapper around an RPC or other remote request.  
`PRODUCER` | Indicates that the span describes producer sending a message to a broker. Unlike client and server, there is no direct critical path latency relationship between producer and consumer spans (e.g. publishing a message to a pubsub service).  
`CONSUMER` | Indicates that the span describes consumer receiving a message from a broker. Unlike client and server, there is no direct critical path latency relationship between producer and consumer spans (e.g. receiving a message from a pubsub service subscription).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-30 UTC."],[],[]] 
