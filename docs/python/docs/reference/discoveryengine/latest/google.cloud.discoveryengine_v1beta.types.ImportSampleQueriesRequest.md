---
url: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportSampleQueriesRequest
title: Class ImportSampleQueriesRequest (0.20.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:43:59.068338+00:00
---

# Class ImportSampleQueriesRequest (0.20.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportSampleQueriesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ImportSampleQueriesRequest (0.20.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.5 (latest)  0.20.4  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.12  0.12.3  0.11.14  0.10.0  0.9.1  0.8.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.1  0.2.1  0.1.1 
    
    
    ImportSampleQueriesRequest(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Request message for SampleQueryService.ImportSampleQueries method.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`inline_source` |  `[google.cloud.discoveryengine_v1beta.types.ImportSampleQueriesRequest.InlineSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportSampleQueriesRequest.InlineSource)`   
The Inline source for sample query entries. This field is a member of `oneof`_ `source`.   
`gcs_source` |  `[google.cloud.discoveryengine_v1beta.types.GcsSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.GcsSource)`   
Cloud Storage location for the input content. This field is a member of `oneof`_ `source`.   
`bigquery_source` |  `[google.cloud.discoveryengine_v1beta.types.BigQuerySource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.BigQuerySource)`   
BigQuery input source. This field is a member of `oneof`_ `source`.   
`parent` |  `str`   
Required. The parent sample query set resource name, such as `projects/{project}/locations/{location}/sampleQuerySets/{sampleQuerySet}`. If the caller does not have permission to list SampleQuerys under this sample query set, regardless of whether or not this sample query set exists, a `PERMISSION_DENIED` error is returned.   
`error_config` |  `[google.cloud.discoveryengine_v1beta.types.ImportErrorConfig](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1beta.types.ImportErrorConfig)`   
The desired location of errors incurred during the Import.   
  
## Classes 

### InlineSource
    
    
    InlineSource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The inline source for SampleQuerys.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
