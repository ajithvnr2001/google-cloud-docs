---
url: https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.loader.BigtableLoader
title: Class BigtableLoader (0.8.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:28:35.854358+00:00
---

# Class BigtableLoader (0.8.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.loader.BigtableLoader

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BigtableLoader (0.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.8.0 (latest) ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/latest/langchain_google_bigtable.loader.BigtableLoader)
  * [ 0.7.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.7.0/langchain_google_bigtable.loader.BigtableLoader)
  * [ 0.6.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.6.0/langchain_google_bigtable.loader.BigtableLoader)
  * [ 0.5.0 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.5.0/langchain_google_bigtable.loader.BigtableLoader)
  * [ 0.4.4 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.4.4/langchain_google_bigtable.loader.BigtableLoader)
  * [ 0.3.1 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.3.1/langchain_google_bigtable.loader.BigtableLoader)
  * [ 0.2.3 ](https://docs.cloud.google.com/python/docs/reference/langchain-google-bigtable/0.2.3/langchain_google_bigtable.loader.BigtableLoader)


    
    
    BigtableLoader(
        instance_id: str,
        table_id: str,
        row_set: typing.Optional[google.cloud.bigtable.row_set.RowSet] = None,
        filter: typing.Optional[google.cloud.bigtable.row_filters.RowFilter] = None,
        client: typing.Optional[google.cloud.bigtable.client.Client] = None,
        content_encoding: langchain_google_bigtable.loader.Encoding = Encoding.UTF8,
        content_column_family: str = "langchain",
        content_column_name: str = "content",
        metadata_mappings: typing.List[
            langchain_google_bigtable.loader.MetadataMapping
        ] = [],
        metadata_as_json_column_family: typing.Optional[str] = None,
        metadata_as_json_column_name: typing.Optional[str] = None,
        metadata_as_json_encoding: langchain_google_bigtable.loader.Encoding = Encoding.UTF8,
    )

Load from the Google Cloud Platform `Bigtable`.

## Methods 

### BigtableLoader
    
    
    BigtableLoader(
        instance_id: str,
        table_id: str,
        row_set: typing.Optional[google.cloud.bigtable.row_set.RowSet] = None,
        filter: typing.Optional[google.cloud.bigtable.row_filters.RowFilter] = None,
        client: typing.Optional[google.cloud.bigtable.client.Client] = None,
        content_encoding: langchain_google_bigtable.loader.Encoding = Encoding.UTF8,
        content_column_family: str = "langchain",
        content_column_name: str = "content",
        metadata_mappings: typing.List[
            langchain_google_bigtable.loader.MetadataMapping
        ] = [],
        metadata_as_json_column_family: typing.Optional[str] = None,
        metadata_as_json_column_name: typing.Optional[str] = None,
        metadata_as_json_encoding: langchain_google_bigtable.loader.Encoding = Encoding.UTF8,
    )

Initialize Bigtable document loader.

### lazy_load
    
    
    lazy_load() -> typing.Iterator[langchain_core.documents.base.Document]

A lazy loader for Documents.

### load
    
    
    load() -> typing.List[langchain_core.documents.base.Document]

Load data into Document objects.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
