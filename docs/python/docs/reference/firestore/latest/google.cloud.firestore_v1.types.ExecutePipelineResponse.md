---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ExecutePipelineResponse
title: Class ExecutePipelineResponse (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:45.106142+00:00
---

# Class ExecutePipelineResponse (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ExecutePipelineResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ExecutePipelineResponse (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 
    
    
    ExecutePipelineResponse(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The response for [Firestore.Execute][].

## Attributes  
  
---  
**Name** | **Description**  
`transaction` |  `bytes`   
Newly created transaction identifier. This field is only specified as part of the first response from the server, alongside the `results` field when the original request specified [ExecuteRequest.new_transaction][].   
`results` |  `MutableSequence[[google.cloud.firestore_v1.types.Document](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.Document)]`   
An ordered batch of results returned executing a pipeline. The batch size is variable, and can even be zero for when only a partial progress message is returned. The fields present in the returned documents are only those that were explicitly requested in the pipeline, this includes those like [`__name__`][google.firestore.v1.Document.name] and [`__update_time__`][google.firestore.v1.Document.update_time]. This is explicitly a divergence from `Firestore.RunQuery` / `Firestore.GetDocument` RPCs which always return such fields even when they are not specified in the [`mask`][google.firestore.v1.DocumentMask].   
`execution_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
The time at which the results are valid. This is a (not strictly) monotonically increasing value across multiple responses in the same stream. The API guarantees that all previously returned results are still valid at the latest `execution_time`. This allows the API consumer to treat the query if it ran at the latest `execution_time` returned. If the query returns no results, a response with `execution_time` and no `results` will be sent, and this represents the time at which the operation was run.   
`explain_stats` |  `[google.cloud.firestore_v1.types.ExplainStats](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ExplainStats)`   
Query explain stats. This is present on the **last** response if the request configured explain to run in 'analyze' or 'explain' mode in the pipeline options. If the query does not return any results, a response with `explain_stats` and no `results` will still be sent.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
