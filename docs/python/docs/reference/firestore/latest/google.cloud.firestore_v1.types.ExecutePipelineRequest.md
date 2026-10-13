---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ExecutePipelineRequest
title: Class ExecutePipelineRequest (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:44.614988+00:00
---

# Class ExecutePipelineRequest (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ExecutePipelineRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ExecutePipelineRequest (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 
    
    
    ExecutePipelineRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The request for `Firestore.ExecutePipeline][google.firestore.v1.Firestore.ExecutePipeline]`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`database` |  `str`   
Required. Database identifier, in the form `projects/{project}/databases/{database}`.   
`structured_pipeline` |  `[google.cloud.firestore_v1.types.StructuredPipeline](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredPipeline)`   
A pipelined operation. This field is a member of `oneof`_ `pipeline_type`.   
`transaction` |  `bytes`   
Run the query within an already active transaction. The value here is the opaque transaction ID to execute the query in. This field is a member of `oneof`_ `consistency_selector`.   
`new_transaction` |  `[google.cloud.firestore_v1.types.TransactionOptions](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.TransactionOptions)`   
Execute the pipeline in a new transaction. The identifier of the newly created transaction will be returned in the first response on the stream. This defaults to a read-only transaction. This field is a member of `oneof`_ `consistency_selector`.   
`read_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Execute the pipeline in a snapshot transaction at the given time. This must be a microsecond precision timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days. This field is a member of `oneof`_ `consistency_selector`.   
`auto_commit_transaction` |  `bool`   
Optional. Automatically commits the transaction after the pipeline has been executed. Only permitted in combination with `transaction` or `new_transaction`.   
`request_options` |  `[google.cloud.firestore_v1.types.RequestOptions](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.RequestOptions)`   
Optional. Any additional options for the request.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
