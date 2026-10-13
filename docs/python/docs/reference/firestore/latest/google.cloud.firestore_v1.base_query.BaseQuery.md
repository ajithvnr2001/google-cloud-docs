---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.BaseQuery
title: Class BaseQuery (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:35.128759+00:00
---

# Class BaseQuery (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.BaseQuery

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BaseQuery (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 
    
    
    BaseQuery(
        parent,
        projection=None,
        field_filters=(),
        orders=(),
        limit=None,
        limit_to_last=False,
        offset=None,
        start_at=None,
        end_at=None,
        all_descendants=False,
        recursive=False,
    )

Represents a query to the Firestore API.

Instances of this class are considered immutable: all methods that would modify an instance instead return a new instance.

## Parameters  
  
---  
**Name** | **Description**  
`parent` |  `[CollectionReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.collection.CollectionReference)`   
The collection that this query applies to.  
`projection` |  `Optional[Projection]`   
A projection of document fields to limit the query results to.  
`field_filters` |  `Optional[Tuple[FieldFilter, ...]]`   
The filters to be applied in the query.  
`orders` |  `Optional[Tuple[Order, ...]]`   
The "order by" entries to use in the query.  
`limit` |  `Optional[int]`   
The maximum number of documents the query is allowed to return.  
`limit_to_last` |  `Optional[bool]`   
Denotes whether a provided limit is applied to the end of the result set.  
`offset` |  `Optional[int]`   
The number of results to skip.  
`start_at` |  `Optional[Tuple[dict, bool]]`   
Two-tuple of : * a mapping of fields. Any field that is present in this mapping must also be present in `orders` * an `after` flag The fields and the flag combine to form a cursor used as a starting point in a query result set. If the `after` flag is :data:`True`, the results will start just after any documents which have fields matching the cursor, otherwise any matching documents will be included in the result set. When the query is formed, the document values will be used in the order given by `orders`.  
`end_at` |  `Optional[Tuple[dict, bool]]`   
Two-tuple of: * a mapping of fields. Any field that is present in this mapping must also be present in `orders` * a `before` flag The fields and the flag combine to form a cursor used as an ending point in a query result set. If the `before` flag is :data:`True`, the results will end just before any documents which have fields matching the cursor, otherwise any matching documents will be included in the result set. When the query is formed, the document values will be used in the order given by `orders`.  
`all_descendants` |  `Optional[bool]`   
When false, selects only collections that are immediate children of the `parent` specified in the containing `RunQueryRequest`. When true, selects all descendant collections.  
`recursive` |  `Optional[bool]`   
When true, returns all documents and all documents in any subcollections below them. Defaults to false.  
  
## Methods 

### end_at
    
    
    end_at(
        document_fields_or_snapshot: typing.Optional[
            typing.Union[
                google.cloud.firestore_v1.base_document.DocumentSnapshot, dict, list, tuple
            ]
        ],
    ) -> google.cloud.firestore_v1.base_query.QueryType

End query results at a particular document value.

The result set will **include** the document specified by `document_fields_or_snapshot`.

If the current query already has specified an end cursor -- either via this method or xref_end_before -- this will overwrite it.

When the query is sent to the server, the `document_fields_or_snapshot` will be used in the order given by fields set by xref_order_by.

**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)` | A query with cursor. Acts as a copy of the current query, modified with the newly added "end at" cursor.  
  
### end_before
    
    
    end_before(
        document_fields_or_snapshot: typing.Optional[
            typing.Union[
                google.cloud.firestore_v1.base_document.DocumentSnapshot, dict, list, tuple
            ]
        ],
    ) -> google.cloud.firestore_v1.base_query.QueryType

End query results before a particular document value.

The result set will **exclude** the document specified by `document_fields_or_snapshot`.

If the current query already has specified an end cursor -- either via this method or xref_end_at -- this will overwrite it.

When the query is sent to the server, the `document_fields_or_snapshot` will be used in the order given by fields set by xref_order_by.

**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)` | A query with cursor. Acts as a copy of the current query, modified with the newly added "end before" cursor.  
  
### limit
    
    
    limit(count: int) -> google.cloud.firestore_v1.base_query.QueryType

Limit a query to return at most `count` matching results.

If the current query already has a `limit` set, this will override it.

**Note:** `limit` and `limit_to_last` are mutually exclusive. Setting `limit` will drop previously set `limit_to_last`. 

**Parameter**  
---  
**Name** | **Description**  
`count` |  `int`   
Maximum number of documents to return that match the query.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)` | A limited query. Acts as a copy of the current query, modified with the newly added "limit" filter.  
  
### limit_to_last
    
    
    limit_to_last(count: int) -> google.cloud.firestore_v1.base_query.QueryType

Limit a query to return the last `count` matching results. If the current query already has a `limit_to_last` set, this will override it.

**Note:** `limit` and `limit_to_last` are mutually exclusive. Setting `limit_to_last` will drop previously set `limit`. 

**Parameter**  
---  
**Name** | **Description**  
`count` |  `int`   
Maximum number of documents to return that match the query.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)` | A limited query. Acts as a copy of the current query, modified with the newly added "limit" filter.  
  
### offset
    
    
    offset(num_to_skip: int) -> google.cloud.firestore_v1.base_query.QueryType

Skip to an offset in a query.

If the current query already has specified an offset, this will overwrite it.

**Parameter**  
---  
**Name** | **Description**  
`num_to_skip` |  `int`   
The number of results to skip at the beginning of query results. (Must be non-negative.)  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)` | An offset query. Acts as a copy of the current query, modified with the newly added "offset" field.  
  
### order_by
    
    
    order_by(
        field_path: str, direction: str = "ASCENDING"
    ) -> google.cloud.firestore_v1.base_query.QueryType

Modify the query to add an order clause on a specific field.

See xref_field_path for more information on **field paths**.

Successive xref_order_by calls will further refine the ordering of results returned by the query (i.e. the new "order by" fields will be added to existing ones).

**Parameters**  
---  
**Name** | **Description**  
`field_path` |  `str`   
A field path (`.`-delimited list of field names) on which to order the query results.  
`direction` |  `Optional[str]`   
The direction to order by. Must be one of `ASCENDING` or `DESCENDING`, defaults to `ASCENDING`.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If `field_path` is invalid.  
`ValueError` | If `direction` is not one of `ASCENDING` or `DESCENDING`.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)` | An ordered query. Acts as a copy of the current query, modified with the newly added "order by" constraint.  
  
### recursive
    
    
    recursive() -> google.cloud.firestore_v1.base_query.QueryType

Returns a copy of this query whose iterator will yield all matching documents as well as each of their descendent subcollections and documents.

This differs from the `all_descendents` flag, which only returns descendents whose subcollection names match the parent collection's name. To return all descendents, regardless of their subcollection name, use this.

### select
    
    
    select(
        field_paths: typing.Iterable[str],
    ) -> google.cloud.firestore_v1.base_query.QueryType

Project documents matching query to a limited set of fields.

See xref_field_path for more information on **field paths**.

If the current query already has a projection set (i.e. has already called xref_select), this will overwrite it.

**Parameter**  
---  
**Name** | **Description**  
`field_paths` |  `Iterable[str, ...]`   
An iterable of field paths (`.`-delimited list of field names) to use as a projection of document fields in the query results.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If any `field_path` is invalid.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)` | A "projected" query. Acts as a copy of the current query, modified with the newly added projection.  
  
### start_after
    
    
    start_after(
        document_fields_or_snapshot: typing.Optional[
            typing.Union[
                google.cloud.firestore_v1.base_document.DocumentSnapshot, dict, list, tuple
            ]
        ],
    ) -> google.cloud.firestore_v1.base_query.QueryType

Start query results after a particular document value.

The result set will **exclude** the document specified by `document_fields_or_snapshot`.

If the current query already has specified a start cursor -- either via this method or xref_start_at -- this will overwrite it.

When the query is sent to the server, the `document_fields_or_snapshot` will be used in the order given by fields set by xref_order_by.

**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)` | A query with cursor. Acts as a copy of the current query, modified with the newly added "start after" cursor.  
  
### start_at
    
    
    start_at(
        document_fields_or_snapshot: typing.Optional[
            typing.Union[
                google.cloud.firestore_v1.base_document.DocumentSnapshot, dict, list, tuple
            ]
        ],
    ) -> google.cloud.firestore_v1.base_query.QueryType

Start query results at a particular document value.

The result set will **include** the document specified by `document_fields_or_snapshot`.

If the current query already has specified a start cursor -- either via this method or xref_start_after -- this will overwrite it.

When the query is sent to the server, the `document_fields` will be used in the order given by fields set by xref_order_by.

**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)` | A query with cursor. Acts as a copy of the current query, modified with the newly added "start at" cursor.  
  
### where
    
    
    where(
        field_path: typing.Optional[str] = None,
        op_string: typing.Optional[str] = None,
        value=None,
        *,
        filter=None
    ) -> google.cloud.firestore_v1.base_query.QueryType

Filter the query on a field.

See xref_field_path for more information on **field paths**.

Returns a new xref_Query that filters on a specific field path, according to an operation (e.g. `==` or "equals") and a particular value to be paired with that operation.

**Parameters**  
---  
**Name** | **Description**  
`field_path` |  `Optional[str]`   
A field path (`.`-delimited list of field names) for the field to filter on.  
`op_string` |  `Optional[str]`   
A comparison operation in the form of a string. Acceptable values are `<`, `<=`, `==`, `!=`, `>=`, `>`, `in`, `not-in`, `array_contains` and `array_contains_any`.  
`value` |  `Any`   
The value to compare the field against in the filter. If `value` is :data:`None` or a NaN, then `==` is the only allowed operation.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If * `field_path` is invalid. * If `value` is a NaN or :data:`None` and `op_string` is not `==`. * FieldFilter was passed without using the filter keyword argument. * `And` or `Or` was passed without using the filter keyword argument . * Both the positional arguments and the keyword argument `filter` were passed.  
**Returns**  
---  
**Type** | **Description**  
`[Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)` | A filtered query. Acts as a copy of the current query, modified with the newly added filter.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
