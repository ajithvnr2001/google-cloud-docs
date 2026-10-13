---
url: https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store
title: Module key_value_store (0.8.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:30:23.958991+00:00
---

# Module key_value_store (0.8.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module key_value_store (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.8.0 (latest) ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store)
  * [ 0.7.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.7.0/langchain_google_bigtable.key_value_store)
  * [ 0.6.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.6.0/langchain_google_bigtable.key_value_store)
  * [ 0.5.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.5.0/langchain_google_bigtable.key_value_store)
  * [ 0.4.4 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.4.4/langchain_google_bigtable.key_value_store)
  * [ 0.3.1 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.3.1/langchain_google_bigtable.key_value_store)
  * [ 0.2.3 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.2.3/langchain_google_bigtable.key_value_store)



API documentation for `key_value_store` module.

## Classes 

### [BigtableByteStore](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.key_value_store.BigtableByteStore)
    
    
    BigtableByteStore(
        engine: langchain_google_bigtable.engine.BigtableEngine,
        instance_id: str,
        table_id: str,
        column_family: str = "kv",
        column_qualifier: bytes = b"val",
        app_profile_id: typing.Optional[str] = None,
    )

LangChain Key-value store implementation for Google Cloud Bigtable, supporting both sync and async methods using BigtableEngine.

## Modules Functions 

### init_key_value_store_table
    
    
    init_key_value_store_table(
        instance_id: str,
        table_id: str,
        project_id: typing.Optional[str] = None,
        client: typing.Optional[google.cloud.bigtable.client.Client] = None,
        column_families: typing.List[str] = ["kv"],
    ) -> None

Create a table for saving of LangChain Key-value pairs.

**Parameters**  
---  
**Name** | **Description**  
`instance_id` |  `str`   
The Instance ID for the table to be created for.  
`table_id` |  `str`   
The Table ID for the table.  
`column_families` |  `Optional[List[str]]`   
The column families for the new table.  
**Exceptions**  
---  
**Type** | **Description**  
`I` | raises ValueError if a table with the given table_id already exists.:  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
