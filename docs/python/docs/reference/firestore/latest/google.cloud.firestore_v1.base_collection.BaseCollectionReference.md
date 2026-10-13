---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_collection.BaseCollectionReference
title: Class BaseCollectionReference (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:35.878966+00:00
---

# Class BaseCollectionReference (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_collection.BaseCollectionReference

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BaseCollectionReference (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 
    
    
    BaseCollectionReference(*path, **kwargs)

A reference to a collection in a Firestore database.

The collection may already exist or this class can facilitate creation of documents within the collection.

## Parameters  
  
---  
**Name** | **Description**  
`path` |  `Tuple[str, ...]`   
The components in the collection path. This is a series of strings representing each collection and sub-collection ID, as well as the document IDs for any documents that contain a sub-collection.  
`kwargs` |  `dict`   
The keyword arguments for the constructor. The only supported keyword is `client` and it must be a [Client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client) if provided. It represents the client that created this collection reference.  
  
## Properties 

### id

The collection identifier.

**Returns**  
---  
**Type** | **Description**  
`str` | The last component of the path.  
  
### parent

Document that owns the current collection.

**Returns**  
---  
**Type** | **Description**  
`Optional[[DocumentReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.document.DocumentReference)]` | The parent document, if the current collection is not a top-level collection.  
  
## Methods 

### avg
    
    
    avg(field_ref: str | FieldPath, alias=None)

Adds an avg over the nested query.

**Parameters**  
---  
**Name** | **Description**  
`field_ref` |  `Union[str, [google.cloud.firestore_v1.field_path.FieldPath](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path.FieldPath)]`   
The field to aggregate across.  
`alias` |  `Optional[str]`   
Optional name of the field to store the result of the aggregation into. If not provided, Firestore will pick a default name following the format field_<incremental_id++>.  
  
### count
    
    
    count(alias=None)

Adds a count over the nested query.

**Parameter**  
---  
**Name** | **Description**  
`alias` |  `str`   
(Optional) The alias for the count  
  
### document
    
    
    document(
        document_id: typing.Optional[str] = None,
    ) -> google.cloud.firestore_v1.base_document.BaseDocumentReference

Create a sub-document underneath the current collection.

**Parameter**  
---  
**Name** | **Description**  
`document_id` |  `Optional[str]`   
The document identifier within the current collection. If not provided, will default to a random 20 character string composed of digits, uppercase and lowercase and letters.  
**Returns**  
---  
**Type** | **Description**  
`[BaseDocumentReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document.BaseDocumentReference)` | The child document.  
  
### end_at
    
    
    end_at(document_fields: Union[DocumentSnapshot, dict, list, tuple]) -> QueryType

End query at a cursor with this collection as parent.

See xref_end_at for more information on this method.

**Parameter**  
---  
**Name** | **Description**  
`document_fields` |  `Union[DocumentSnapshot, dict, list, tuple]`   
A document snapshot or a dictionary/list/tuple of fields representing a query results cursor. A cursor is a collection of values that represent a position in a query result set.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)` | A query with cursor.  
  
### end_before
    
    
    end_before(
        document_fields: Union[DocumentSnapshot, dict, list, tuple],
    ) -> QueryType

End query before a cursor with this collection as parent.

See xref_end_before for more information on this method.

**Parameter**  
---  
**Name** | **Description**  
`document_fields` |  `Union[DocumentSnapshot, dict, list, tuple]`   
A document snapshot or a dictionary/list/tuple of fields representing a query results cursor. A cursor is a collection of values that represent a position in a query result set.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)` | A query with cursor.  
  
### find_nearest
    
    
    find_nearest(
        vector_field: str,
        query_vector: Union[Vector, Sequence[float]],
        limit: int,
        distance_measure: DistanceMeasure,
        *,
        distance_result_field: Optional[str] = None,
        distance_threshold: Optional[float] = None
    ) -> VectorQuery

Finds the closest vector embeddings to the given query vector.

**Parameters**  
---  
**Name** | **Description**  
`vector_field` |  `str`   
An indexed vector field to search upon. Only documents which contain vectors whose dimensionality match the query_vector can be returned.  
`query_vector` |  `Union[Vector, Sequence[float]]`   
The query vector that we are searching on. Must be a vector of no more than 2048 dimensions.  
`limit` |  `int`   
The number of nearest neighbors to return. Must be a positive integer of no more than 1000.  
`distance_measure` |  ``DistanceMeasure``   
The Distance Measure to use.  
`distance_result_field` |  `Optional[str]`   
Name of the field to output the result of the vector distance calculation  
`distance_threshold` |  `Optional[float]`   
A threshold for which no less similar documents will be returned.  
  
### limit
    
    
    limit(count: int) -> google.cloud.firestore_v1.base_query.QueryType

Create a limited query with this collection as parent.

**Note:** `limit` and `limit_to_last` are mutually exclusive. Setting `limit` will drop previously set `limit_to_last`.  See xref_limit for more information on this method.

**Parameter**  
---  
**Name** | **Description**  
`count` |  `int`   
Maximum number of documents to return that match the query.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)` | A limited query.  
  
### limit_to_last
    
    
    limit_to_last(count: int)

Create a limited to last query with this collection as parent.

**Note:** `limit` and `limit_to_last` are mutually exclusive. Setting `limit_to_last` will drop previously set `limit`.  See xref_limit_to_last for more information on this method.

**Parameter**  
---  
**Name** | **Description**  
`count` |  `int`   
Maximum number of documents to return that match the query.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)` | A limited to last query.  
  
### offset
    
    
    offset(num_to_skip: int) -> google.cloud.firestore_v1.base_query.QueryType

Skip to an offset in a query with this collection as parent.

See xref_offset for more information on this method.

**Parameter**  
---  
**Name** | **Description**  
`num_to_skip` |  `int`   
The number of results to skip at the beginning of query results. (Must be non-negative.)  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)` | An offset query.  
  
### order_by
    
    
    order_by(
        field_path: str, **kwargs
    ) -> google.cloud.firestore_v1.base_query.QueryType

Create an "order by" query with this collection as parent.

See xref_order_by for more information on this method.

**Parameters**  
---  
**Name** | **Description**  
`field_path` |  `str`   
A field path (`.`-delimited list of field names) on which to order the query results.  
`kwargs` |  `Dict[str, Any]`   
The keyword arguments to pass along to the query. The only supported keyword is `direction`, see order_by for more information.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)` | An "order by" query.  
  
### select
    
    
    select(
        field_paths: typing.Iterable[str],
    ) -> google.cloud.firestore_v1.base_query.QueryType

Create a "select" query with this collection as parent.

See xref_select for more information on this method.

**Parameter**  
---  
**Name** | **Description**  
`field_paths` |  `Iterable[str, ...]`   
An iterable of field paths (`.`-delimited list of field names) to use as a projection of document fields in the query results.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)` | A "projected" query.  
  
### start_after
    
    
    start_after(
        document_fields: Union[DocumentSnapshot, dict, list, tuple],
    ) -> QueryType

Start query after a cursor with this collection as parent.

See xref_start_after for more information on this method.

**Parameter**  
---  
**Name** | **Description**  
`document_fields` |  `Union[DocumentSnapshot, dict, list, tuple]`   
A document snapshot or a dictionary/list/tuple of fields representing a query results cursor. A cursor is a collection of values that represent a position in a query result set.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)` | A query with cursor.  
  
### start_at
    
    
    start_at(document_fields: Union[DocumentSnapshot, dict, list, tuple]) -> QueryType

Start query at a cursor with this collection as parent.

See xref_start_at for more information on this method.

**Parameter**  
---  
**Name** | **Description**  
`document_fields` |  `Union[DocumentSnapshot, dict, list, tuple]`   
A document snapshot or a dictionary/list/tuple of fields representing a query results cursor. A cursor is a collection of values that represent a position in a query result set.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)` | A query with cursor.  
  
### sum
    
    
    sum(field_ref: str | FieldPath, alias=None)

Adds a sum over the nested query.

**Parameters**  
---  
**Name** | **Description**  
`field_ref` |  `Union[str, [google.cloud.firestore_v1.field_path.FieldPath](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path.FieldPath)]`   
The field to aggregate across.  
`alias` |  `Optional[str]`   
Optional name of the field to store the result of the aggregation into. If not provided, Firestore will pick a default name following the format field_<incremental_id++>.  
  
### where
    
    
    where(
        field_path: typing.Optional[str] = None,
        op_string: typing.Optional[str] = None,
        value=None,
        *,
        filter=None
    ) -> google.cloud.firestore_v1.base_query.QueryType

Create a "where" query with this collection as parent.

See xref_where for more information on this method.

**Parameters**  
---  
**Name** | **Description**  
`field_path` |  `str`   
A field path (`.`-delimited list of field names) for the field to filter on. Optional.  
`op_string` |  `str`   
A comparison operation in the form of a string. Acceptable values are `<`, `<=`, `==`, `>=`, `>`, and `in`. Optional.  
`value` |  `Any`   
The value to compare the field against in the filter. If `value` is :data:`None` or a NaN, then `==` is the only allowed operation. If `op_string` is `in`, `value` must be a sequence of values. Optional.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | if both the positional arguments (field_path, op_string, value): and the filter keyword argument are passed at the same time.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)` | A filtered query.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
