---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-parallelstore/latest/google.cloud.parallelstore_v1beta.types.TransferOperationMetadata
title: Class TransferOperationMetadata (0.6.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:30:05.848336+00:00
---

# Class TransferOperationMetadata (0.6.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-parallelstore/latest/google.cloud.parallelstore_v1beta.types.TransferOperationMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class TransferOperationMetadata (0.6.2) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    TransferOperationMetadata(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Long-running operation metadata related to a data transfer.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`source_parallelstore` |  `[google.cloud.parallelstore_v1beta.types.SourceParallelstore](https://docs.cloud.google.com/python/docs/reference/google-cloud-parallelstore/latest/google.cloud.parallelstore_v1beta.types.SourceParallelstore)`   
Output only. Parallelstore source. This field is a member of `oneof`_ `source`.   
`source_gcs_bucket` |  `[google.cloud.parallelstore_v1beta.types.SourceGcsBucket](https://docs.cloud.google.com/python/docs/reference/google-cloud-parallelstore/latest/google.cloud.parallelstore_v1beta.types.SourceGcsBucket)`   
Output only. Cloud Storage source. This field is a member of `oneof`_ `source`.   
`destination_gcs_bucket` |  `[google.cloud.parallelstore_v1beta.types.DestinationGcsBucket](https://docs.cloud.google.com/python/docs/reference/google-cloud-parallelstore/latest/google.cloud.parallelstore_v1beta.types.DestinationGcsBucket)`   
Output only. Cloud Storage destination. This field is a member of `oneof`_ `destination`.   
`destination_parallelstore` |  `[google.cloud.parallelstore_v1beta.types.DestinationParallelstore](https://docs.cloud.google.com/python/docs/reference/google-cloud-parallelstore/latest/google.cloud.parallelstore_v1beta.types.DestinationParallelstore)`   
Output only. Parallelstore destination. This field is a member of `oneof`_ `destination`.   
`counters` |  `[google.cloud.parallelstore_v1beta.types.TransferCounters](https://docs.cloud.google.com/python/docs/reference/google-cloud-parallelstore/latest/google.cloud.parallelstore_v1beta.types.TransferCounters)`   
Output only. The progress of the transfer operation.   
`transfer_type` |  `[google.cloud.parallelstore_v1beta.types.TransferType](https://docs.cloud.google.com/python/docs/reference/google-cloud-parallelstore/latest/google.cloud.parallelstore_v1beta.types.TransferType)`   
Output only. The type of transfer occurring.   
`error_summary` |  `MutableSequence[[google.cloud.parallelstore_v1beta.types.TransferErrorSummary](https://docs.cloud.google.com/python/docs/reference/google-cloud-parallelstore/latest/google.cloud.parallelstore_v1beta.types.TransferErrorSummary)]`   
Output only. List of files that failed to be transferred. This list will have a maximum size of 5 elements.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
