---
url: https://docs.cloud.google.com/python/docs/reference/langchain-google-cloud-sql-mssql/latest/langchain_google_cloud_sql_mssql.loader
title: Module loader (0.3.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:18:44.574802+00:00
---

# Module loader (0.3.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/langchain-google-cloud-sql-mssql/latest/langchain_google_cloud_sql_mssql.loader

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module loader (0.3.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.3.0 (latest) ](https://docs.cloud.google.com/python/docs/reference/langchain-google-cloud-sql-mssql/latest/langchain_google_cloud_sql_mssql.loader)
  * [ 0.2.1 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-cloud-sql-mssql/0.2.1/langchain_google_cloud_sql_mssql.loader)



API documentation for `loader` module.

## Classes 

### [MSSQLDocumentSaver](https://docs.cloud.google.com/python/docs/reference/langchain-google-cloud-sql-mssql/latest/langchain_google_cloud_sql_mssql.loader.MSSQLDocumentSaver)
    
    
    MSSQLDocumentSaver(
        engine: langchain_google_cloud_sql_mssql.engine.MSSQLEngine,
        table_name: str,
        content_column: typing.Optional[str] = None,
        metadata_json_column: typing.Optional[str] = None,
    )

A class for saving langchain documents into a Cloud SQL MSSQL database table.

### [MSSQLLoader](https://docs.cloud.google.com/python/docs/reference/langchain-google-cloud-sql-mssql/latest/langchain_google_cloud_sql_mssql.loader.MSSQLLoader)
    
    
    MSSQLLoader(
        engine: langchain_google_cloud_sql_mssql.engine.MSSQLEngine,
        table_name: str = "",
        query: str = "",
        content_columns: typing.Optional[typing.List[str]] = None,
        metadata_columns: typing.Optional[typing.List[str]] = None,
        metadata_json_column: typing.Optional[str] = None,
    )

A class for loading langchain documents from a Cloud SQL MSSQL database.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
