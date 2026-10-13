---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Datasource
title: Class Datasource (0.13.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:03:54.572382+00:00
---

# Class Datasource (0.13.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Datasource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Datasource (0.13.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.5 (latest)  0.13.4  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    Datasource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A datasource that can be used to answer questions.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`bigquery_table_reference` |  `[google.cloud.geminidataanalytics_v1.types.BigQueryTableReference](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.BigQueryTableReference)`   
A reference to a BigQuery table. This field is a member of `oneof`_ `reference`.   
`studio_datasource_id` |  `str`   
A reference to a Looker Studio datasource. This field is a member of `oneof`_ `reference`.   
`looker_explore_reference` |  `[google.cloud.geminidataanalytics_v1.types.LookerExploreReference](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.LookerExploreReference)`   
A reference to a Looker explore. This field is a member of `oneof`_ `reference`.   
`bigquery_property_graph_reference` |  `[google.cloud.geminidataanalytics_v1.types.BigQueryPropertyGraphReference](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.BigQueryPropertyGraphReference)`   
A reference to a BigQuery property graph. This field is a member of `oneof`_ `reference`.   
`schema` |  `[google.cloud.geminidataanalytics_v1.types.Schema](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Schema)`   
Optional. The schema of the datasource.   
`struct_schema` |  `google.protobuf.struct_pb2.Struct`   
Optional. A struct representation of the schema. This is populated for datasources with schemas that cannot be fully represented by the strongly-typed `schema` field. For Looker datasources, this maps to the LookmlModelExplore type: https://cloud.google.com/looker/docs/reference/looker-api/latest/types/LookmlModelExplore   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
