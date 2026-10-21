---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.monitoring.v3
title: Package google.monitoring.v3 \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:35.359347+00:00
---

# Package google.monitoring.v3  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.monitoring.v3

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Package google.monitoring.v3 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[SpanContext](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.monitoring.v3#google.monitoring.v3.SpanContext)` (message)



## SpanContext

The context of a span, attached to [Exemplars][google.api.Distribution.Exemplars] in `[Distribution](https://docs.cloud.google.com/service-infrastructure/docs/service-control/reference/rpc/google.api#google.api.Distribution)` values during aggregation.

It contains the name of a span with format:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/traces/[TRACE_ID]/spans/[SPAN_ID]
    

Fields  
---  
`span_name` |  `string` The resource name of the span. The format is:
    
    
    projects/[PROJECT_ID_OR_NUMBER]/traces/[TRACE_ID]/spans/[SPAN_ID]
    

`[TRACE_ID]` is a unique identifier for a trace within a project; it is a 32-character hexadecimal encoding of a 16-byte array.`[SPAN_ID]` is a unique identifier for a span within a trace; it is a 16-character hexadecimal encoding of an 8-byte array.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
