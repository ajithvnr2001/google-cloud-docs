---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Context
title: Class Context (0.13.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:03:50.140932+00:00
---

# Class Context (0.13.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Context

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Context (0.13.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.5 (latest)  0.13.4  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    Context(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A collection of context to apply to this conversation

## Attributes  
  
---  
**Name** | **Description**  
`system_instruction` |  `str`   
Optional. The basic entry point for data owners creating domain knowledge for Agent. Why: Business jargon (e.g., YTD revenue is calculated as…, Retirement Age is 65 in the USA, etc) and system instructions (e.g., answer like a Pirate) can help the model understand the business context around a user question. Must be at most 250,000 bytes (approx. 250,000 characters for English text).   
`datasource_references` |  `[google.cloud.geminidataanalytics_v1.types.DatasourceReferences](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.DatasourceReferences)`   
Required. Data sources that are available for answering the question.   
`options` |  `[google.cloud.geminidataanalytics_v1.types.ConversationOptions](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ConversationOptions)`   
Optional. Additional options for the conversation.   
`example_queries` |  `MutableSequence[[google.cloud.geminidataanalytics_v1.types.ExampleQuery](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.ExampleQuery)]`   
Optional. A list of example queries, providing examples of relevant and commonly used SQL queries and their corresponding natural language queries optionally present. Currently only used for BigQuery data sources and databases (alloydb, cloudsql, spanner) data sources.   
`looker_golden_queries` |  `MutableSequence[[google.cloud.geminidataanalytics_v1.types.LookerGoldenQuery](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.LookerGoldenQuery)]`   
Optional. A list of golden queries, providing examples of relevant and commonly used Looker queries and their corresponding natural language queries optionally present. Only supported for Looker data sources.   
`glossary_terms` |  `MutableSequence[[google.cloud.geminidataanalytics_v1.types.GlossaryTerm](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.GlossaryTerm)]`   
Optional. Term definitions (currently, only user authored) Not supported for databases (alloydb, cloudsql, spanner) data sources.   
`schema_relationships` |  `MutableSequence[[google.cloud.geminidataanalytics_v1.types.Context.SchemaRelationship](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.Context.SchemaRelationship)]`   
Optional. Relationships between table schema, including referencing and referenced columns.   
`user_functions` |  `[google.cloud.geminidataanalytics_v1.types.UserFunctions](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.types.UserFunctions)`   
Optional. A collection of user functions to be included in context.   
  
## Classes 

### SchemaRelationship
    
    
    SchemaRelationship(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The relationship between two tables, including referencing and referenced columns. This is a derived context retrieved from Dataplex Dataset Insights.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
