---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.SystemMessage
title: Class SystemMessage (0.13.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:04:04.004607+00:00
---

# Class SystemMessage (0.13.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.SystemMessage

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class SystemMessage (0.13.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.5 (latest)  0.13.4  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    SystemMessage(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A message from the system in response to the user. This message can also be a message from the user as historical context for multi-turn conversations with the system.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`text` |  `[google.cloud.geminidataanalytics_v1.types.TextMessage](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.TextMessage)`   
A direct natural language response to the user message. This field is a member of `oneof`_ `kind`.   
`schema` |  `[google.cloud.geminidataanalytics_v1.types.SchemaMessage](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.SchemaMessage)`   
A message produced during schema resolution. This field is a member of `oneof`_ `kind`.   
`data` |  `[google.cloud.geminidataanalytics_v1.types.DataMessage](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.DataMessage)`   
A message produced during data retrieval. This field is a member of `oneof`_ `kind`.   
`analysis` |  `[google.cloud.geminidataanalytics_v1.types.AnalysisMessage](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.AnalysisMessage)`   
A message produced during analysis. This field is a member of `oneof`_ `kind`.   
`chart` |  `[google.cloud.geminidataanalytics_v1.types.ChartMessage](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ChartMessage)`   
A message produced during chart generation. This field is a member of `oneof`_ `kind`.   
`error` |  `[google.cloud.geminidataanalytics_v1.types.ErrorMessage](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ErrorMessage)`   
An error message. This field is a member of `oneof`_ `kind`.   
`example_queries` |  `[google.cloud.geminidataanalytics_v1.types.ExampleQueries](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ExampleQueries)`   
Optional. A message containing example queries. This field is a member of `oneof`_ `kind`.   
`group_id` |  `int`   
Identifies the group that the event belongs to. Similar events are deemed to be logically relevant to each other and should be shown together in the UI. This field is a member of `oneof`_ `_group_id`.   
`citation` |  `[google.cloud.geminidataanalytics_v1.types.Citation](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Citation)`   
Output only. Citation information for the system message.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
