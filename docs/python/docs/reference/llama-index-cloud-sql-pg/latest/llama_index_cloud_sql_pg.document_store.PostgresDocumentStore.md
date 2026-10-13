---
url: https://docs.cloud.google.com/python/docs/reference/llama-index-cloud-sql-pg/latest/llama_index_cloud_sql_pg.document_store.PostgresDocumentStore
title: Class PostgresDocumentStore (0.3.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:08.174721+00:00
---

# Class PostgresDocumentStore (0.3.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/llama-index-cloud-sql-pg/latest/llama_index_cloud_sql_pg.document_store.PostgresDocumentStore

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class PostgresDocumentStore (0.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.3.1 (latest)  0.2.3 
    
    
    PostgresDocumentStore(
        key: object,
        engine: llama_index_cloud_sql_pg.engine.PostgresEngine,
        document_store: llama_index_cloud_sql_pg.async_document_store.AsyncPostgresDocumentStore,
    )

Document Store Table stored in an Cloud SQL for PostgreSQL database.

## Properties 

### docs

Get all documents.

**Returns**  
---  
**Type** | **Description**  
`dict[str, BaseDocument]` | documents  
  
## Methods 

### PostgresDocumentStore
    
    
    PostgresDocumentStore(
        key: object,
        engine: llama_index_cloud_sql_pg.engine.PostgresEngine,
        document_store: llama_index_cloud_sql_pg.async_document_store.AsyncPostgresDocumentStore,
    )

"PostgresDocumentStore constructor.

**Parameters**  
---  
**Name** | **Description**  
`key` |  `object`   
Key to prevent direct constructor usage.  
`engine` |  `PostgresEngine`   
Database connection pool.  
`document_store` |  `AsyncPostgresDocumentStore`   
The async only DocumentStore implementation  
**Exceptions**  
---  
**Type** | **Description**  
`Exception` | If constructor is directly called by the user.  
  
### add_documents
    
    
    add_documents(
        docs: typing.Sequence[llama_index.core.schema.BaseNode],
        allow_update: bool = True,
        batch_size: int = 1,
        store_text: bool = True,
    ) -> None

Adds a document to the store.

**Parameters**  
---  
**Name** | **Description**  
`docs` |  `Sequence[BaseDocument]`   
documents  
`allow_update` |  `bool`   
allow update of docstore from document  
`batch_size` |  `int`   
batch_size to insert the rows. Defaults to 1.  
`store_text` |  `bool`   
allow the text content of the node to stored. Defaults to "True".  
  
### adelete_document
    
    
    adelete_document(doc_id: str, raise_error: bool = True) -> None

Delete a document from the store.

**Parameters**  
---  
**Name** | **Description**  
`doc_id` |  `str`   
Id of the document / node to be deleted.  
`raise_error` |  `bool`   
to raise error if document is not found.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If a node is not found and `raise_error` is set to True.  
  
### adelete_ref_doc
    
    
    adelete_ref_doc(ref_doc_id: str, raise_error: bool = True) -> None

Delete a ref_doc and all it's associated nodes.

**Parameters**  
---  
**Name** | **Description**  
`ref_doc_id` |  `str`   
Ref_doc_id which needs to be deleted.  
`raise_error` |  `bool`   
to raise error if ref_doc_info for the ref_doc_id is not found.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If ref_doc_info for the ref_doc_id doesn't exist and `raise_error` is set to True.  
  
### adocument_exists
    
    
    adocument_exists(doc_id: str) -> bool

Check if document exists.

**Parameter**  
---  
**Name** | **Description**  
`doc_id` |  `str`   
The document / node id which needs to be found.  
**Returns**  
---  
**Type** | **Description**  
`bool` | True if document exists in the table.  
  
### aget_all_document_hashes
    
    
    aget_all_document_hashes() -> dict[str, str]

Get the stored hash for all documents.

Returns: A dictionary mapping document hashes to document IDs.

### aget_all_ref_doc_info
    
    
    aget_all_ref_doc_info() -> (
        typing.Optional[dict[str, llama_index.core.storage.docstore.types.RefDocInfo]]
    )

Get a mapping of ref_doc_id -> RefDocInfo for all ingested documents.

Returns: A dictionary mapping ref_doc_ids to `RefDocInfo` objects, or None if no documents have been ingested.

### aget_document
    
    
    aget_document(
        doc_id: str, raise_error: bool = True
    ) -> typing.Optional[llama_index.core.schema.BaseNode]

Retrieves a document from the table by its doc_id.

**Parameters**  
---  
**Name** | **Description**  
`doc_id` |  `str`   
Id of the document / node to be retrieved.  
`raise_error` |  `bool`   
to raise error if document is not found.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If a node doesn't exist and `raise_error` is set to True.  
**Returns**  
---  
**Type** | **Description**  
`Optional[BaseNode]` | Returns a `BaseNode` object if the document is found  
  
### aget_document_hash
    
    
    aget_document_hash(doc_id: str) -> typing.Optional[str]

Get the stored hash for a document, if it exists.

**Returns**  
---  
**Type** | **Description**  
`Optional[str]` | The hash for the given doc_id, if available.  
  
### aget_ref_doc_info
    
    
    aget_ref_doc_info(
        ref_doc_id: str,
    ) -> typing.Optional[llama_index.core.storage.docstore.types.RefDocInfo]

Get the RefDocInfo for a given ref_doc_id.

**Parameter**  
---  
**Name** | **Description**  
`ref_doc_id` |  `str`   
The ref_doc_id whose ref_doc_info is to be retrieved.  
**Returns**  
---  
**Type** | **Description**  
`Optional[RefDocInfo]` | Returns a `RefDocInfo` object if it exists.  
  
### aref_doc_exists
    
    
    aref_doc_exists(ref_doc_id: str) -> bool

Check if a ref_doc_id has been ingested.

**Parameter**  
---  
**Name** | **Description**  
`ref_doc_id` |  `str`   
The ref_doc_id whose ref_doc_info is to be found.  
**Returns**  
---  
**Type** | **Description**  
`bool` | True if document exists as a ref doc in the table.  
  
### aset_document_hash
    
    
    aset_document_hash(doc_id: str, doc_hash: str) -> None

Set the hash for a given doc_id.

**Parameters**  
---  
**Name** | **Description**  
`doc_id` |  `str`   
Id to be updated with the doc_hash.  
`doc_hash` |  `str`   
Doc_hash to be updated into the table.  
  
### aset_document_hashes
    
    
    aset_document_hashes(doc_hashes: dict[str, str]) -> None

Set the hash for a given doc_id.

**Parameter**  
---  
**Name** | **Description**  
`doc_hashes` |  `dict[str, str]`   
Dictionary with doc_id as key and doc_hash as value.  
  
### async_add_documents
    
    
    async_add_documents(
        docs: typing.Sequence[llama_index.core.schema.BaseNode],
        allow_update: bool = True,
        batch_size: int = 1,
        store_text: bool = True,
    ) -> None

Adds a document to the store.

**Parameters**  
---  
**Name** | **Description**  
`docs` |  `Sequence[BaseDocument]`   
documents  
`allow_update` |  `bool`   
allow update of docstore from document  
`batch_size` |  `int`   
batch_size to insert the rows. Defaults to 1.  
`store_text` |  `bool`   
allow the text content of the node to stored. Defaults to "True".  
  
### create
    
    
    create(
        engine: llama_index_cloud_sql_pg.engine.PostgresEngine,
        table_name: str,
        schema_name: str = "public",
        batch_size: int = 1,
    ) -> llama_index_cloud_sql_pg.document_store.PostgresDocumentStore

Create a new PostgresDocumentStore instance.

**Parameters**  
---  
**Name** | **Description**  
`engine` |  `PostgresEngine`   
Postgres engine to use.  
`table_name` |  `str`   
Table name that stores the documents.  
`schema_name` |  `str`   
The schema name where the table is located. Defaults to "public"  
`batch_size` |  `str`   
The default batch size for bulk inserts. Defaults to 1.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If the table provided does not contain required schema.  
**Returns**  
---  
**Type** | **Description**  
`PostgresDocumentStore` | A newly created instance of PostgresDocumentStore.  
  
### create_sync
    
    
    create_sync(
        engine: llama_index_cloud_sql_pg.engine.PostgresEngine,
        table_name: str,
        schema_name: str = "public",
        batch_size: int = 1,
    ) -> llama_index_cloud_sql_pg.document_store.PostgresDocumentStore

Create a new PostgresDocumentStore sync instance.

**Parameters**  
---  
**Name** | **Description**  
`engine` |  `PostgresEngine`   
Postgres engine to use.  
`table_name` |  `str`   
Table name that stores the documents.  
`schema_name` |  `str`   
The schema name where the table is located. Defaults to "public"  
`batch_size` |  `str`   
The default batch size for bulk inserts. Defaults to 1.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If the table provided does not contain required schema.  
**Returns**  
---  
**Type** | **Description**  
`PostgresDocumentStore` | A newly created instance of PostgresDocumentStore.  
  
### delete_document
    
    
    delete_document(doc_id: str, raise_error: bool = True) -> None

Delete a document from the store.

**Parameters**  
---  
**Name** | **Description**  
`doc_id` |  `str`   
Id of the document / node to be deleted.  
`raise_error` |  `bool`   
to raise error if document is not found.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If a node is not found and `raise_error` is set to True.  
  
### delete_ref_doc
    
    
    delete_ref_doc(ref_doc_id: str, raise_error: bool = True) -> None

Delete a ref_doc and all it's associated nodes.

**Parameters**  
---  
**Name** | **Description**  
`ref_doc_id` |  `str`   
Ref_doc_id which needs to be deleted.  
`raise_error` |  `bool`   
to raise error if ref_doc_info for the ref_doc_id is not found.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If ref_doc_info for the ref_doc_id doesn't exist and `raise_error` is set to True.  
  
### document_exists
    
    
    document_exists(doc_id: str) -> bool

Check if document exists.

**Parameter**  
---  
**Name** | **Description**  
`doc_id` |  `str`   
The document / node id which needs to be found.  
**Returns**  
---  
**Type** | **Description**  
`bool` | True if document exists in the table.  
  
### get_all_document_hashes
    
    
    get_all_document_hashes() -> dict[str, str]

Get the stored hash for all documents.

Returns: A dictionary mapping document hashes to document IDs.

### get_all_ref_doc_info
    
    
    get_all_ref_doc_info() -> (
        typing.Optional[dict[str, llama_index.core.storage.docstore.types.RefDocInfo]]
    )

Get a mapping of ref_doc_id -> RefDocInfo for all ingested documents.

Returns: A dictionary mapping ref_doc_ids to `RefDocInfo` objects, or None if no documents have been ingested.

### get_document
    
    
    get_document(
        doc_id: str, raise_error: bool = True
    ) -> typing.Optional[llama_index.core.schema.BaseNode]

Retrieves a document from the table by its doc_id.

**Parameters**  
---  
**Name** | **Description**  
`doc_id` |  `str`   
Id of the document / node to be retrieved.  
`raise_error` |  `bool`   
to raise error if document is not found.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If a node doesn't exist and `raise_error` is set to True.  
**Returns**  
---  
**Type** | **Description**  
`Optional[BaseNode]` | Returns a `BaseNode` object if the document is found  
  
### get_document_hash
    
    
    get_document_hash(doc_id: str) -> typing.Optional[str]

Get the stored hash for a document, if it exists.

**Returns**  
---  
**Type** | **Description**  
`Optional[str]` | The hash for the given doc_id, if available.  
  
### get_ref_doc_info
    
    
    get_ref_doc_info(
        ref_doc_id: str,
    ) -> typing.Optional[llama_index.core.storage.docstore.types.RefDocInfo]

Get the RefDocInfo for a given ref_doc_id.

**Parameter**  
---  
**Name** | **Description**  
`ref_doc_id` |  `str`   
The ref_doc_id whose ref_doc_info is to be retrieved.  
**Returns**  
---  
**Type** | **Description**  
`Optional[RefDocInfo]` | Returns a `RefDocInfo` object if it exists.  
  
### ref_doc_exists
    
    
    ref_doc_exists(ref_doc_id: str) -> bool

Check if a ref_doc_id has been ingested.

**Parameter**  
---  
**Name** | **Description**  
`ref_doc_id` |  `str`   
The ref_doc_id whose ref_doc_info is to be found.  
**Returns**  
---  
**Type** | **Description**  
`bool` | True if document exists as a ref doc in the table.  
  
### set_document_hash
    
    
    set_document_hash(doc_id: str, doc_hash: str) -> None

Set the hash for a given doc_id.

**Parameters**  
---  
**Name** | **Description**  
`doc_id` |  `str`   
Id to be updated with the doc_hash.  
`doc_hash` |  `str`   
Doc_hash to be updated into the table.  
  
### set_document_hashes
    
    
    set_document_hashes(doc_hashes: dict[str, str]) -> None

Set the hash for a given doc_id.

**Parameter**  
---  
**Name** | **Description**  
`doc_hashes` |  `dict[str, str]`   
Dictionary with doc_id as key and doc_hash as value.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-20 UTC."],[],[]] 
