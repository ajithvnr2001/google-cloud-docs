---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.RunQueryResponse
title: Class RunQueryResponse (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:52.166210+00:00
---

# Class RunQueryResponse (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.RunQueryResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class RunQueryResponse (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 
    
    
    RunQueryResponse(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The response for `Firestore.RunQuery][google.firestore.v1.Firestore.RunQuery]`.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`transaction` |  `bytes`   
The transaction that was started as part of this request. Can only be set in the first response, and only if `RunQueryRequest.new_transaction][google.firestore.v1.RunQueryRequest.new_transaction]` was set in the request. If set, no other fields will be set in this response.   
`document` |  `[google.cloud.firestore_v1.types.Document](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.Document)`   
A query result, not set when reporting partial progress.   
`read_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
The time at which the document was read. This may be monotonically increasing; in this case, the previous documents in the result stream are guaranteed not to have changed between their `read_time` and this one. If the query returns no results, a response with `read_time` and no `document` will be sent, and this represents the time at which the query was run.   
`skipped_results` |  `int`   
The number of results that have been skipped due to an offset between the last response and the current response.   
`done` |  `bool`   
If present, Firestore has completely finished the request and no more documents will be returned. This field is a member of `oneof`_ `continuation_selector`.   
`explain_metrics` |  `[google.cloud.firestore_v1.types.ExplainMetrics](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ExplainMetrics)`   
Query explain metrics. This is only present when the `RunQueryRequest.explain_options][google.firestore.v1.RunQueryRequest.explain_options]` is provided, and it is sent only once with the last response in the stream.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
