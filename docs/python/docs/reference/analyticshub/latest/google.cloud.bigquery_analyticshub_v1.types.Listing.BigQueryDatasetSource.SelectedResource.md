---
url: https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_analyticshub_v1.types.Listing.BigQueryDatasetSource.SelectedResource
title: Class SelectedResource (0.6.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:55:39.224871+00:00
---

# Class SelectedResource (0.6.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/analyticshub/latest/google.cloud.bigquery_analyticshub_v1.types.Listing.BigQueryDatasetSource.SelectedResource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SelectedResource (0.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.9.0  0.8.0  0.7.0  0.6.0  0.5.20  0.4.20  0.3.2  0.2.1  0.1.1 
    
    
    SelectedResource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Resource in this dataset that is selectively shared.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`table` |  `str`   
Optional. Format: For table: `projects/{projectId}/datasets/{datasetId}/tables/{tableId}` Example:"projects/test_project/datasets/test_dataset/tables/test_table". This field is a member of `oneof`_ `resource`.   
`routine` |  `str`   
Optional. Format: For routine: `projects/{projectId}/datasets/{datasetId}/routines/{routineId}` Example:"projects/test_project/datasets/test_dataset/routines/test_routine". This field is a member of `oneof`_ `resource`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
