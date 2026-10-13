---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-parallelstore/latest/google.cloud.parallelstore_v1beta.types.ExportDataRequest
title: Class ExportDataRequest (0.6.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:16:27.922554+00:00
---

# Class ExportDataRequest (0.6.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-parallelstore/latest/google.cloud.parallelstore_v1beta.types.ExportDataRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ExportDataRequest (0.6.2) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    ExportDataRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Export data from Parallelstore to Cloud Storage.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`source_parallelstore` |  `[google.cloud.parallelstore_v1beta.types.SourceParallelstore](https://docs.cloud.google.com/python/docs/reference/google-cloud-parallelstore/latest/google.cloud.parallelstore_v1beta.types.SourceParallelstore)`   
Parallelstore source. This field is a member of `oneof`_ `source`.   
`destination_gcs_bucket` |  `[google.cloud.parallelstore_v1beta.types.DestinationGcsBucket](https://docs.cloud.google.com/python/docs/reference/google-cloud-parallelstore/latest/google.cloud.parallelstore_v1beta.types.DestinationGcsBucket)`   
Cloud Storage destination. This field is a member of `oneof`_ `destination`.   
`name` |  `str`   
Required. Name of the resource.   
`request_id` |  `str`   
Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).   
`service_account` |  `str`   
Optional. User-specified Service Account (SA) credentials to be used when performing the transfer. Use one of the following formats: \- `{EMAIL_ADDRESS_OR_UNIQUE_ID}` \- `projects/{PROJECT_ID_OR_NUMBER}/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}` \- `projects/-/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}` If unspecified, the Parallelstore service agent is used: `service-`  
`metadata_options` |  `[google.cloud.parallelstore_v1beta.types.TransferMetadataOptions](https://docs.cloud.google.com/python/docs/reference/google-cloud-parallelstore/latest/google.cloud.parallelstore_v1beta.types.TransferMetadataOptions)`   
Optional. The metadata options for the export data.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
