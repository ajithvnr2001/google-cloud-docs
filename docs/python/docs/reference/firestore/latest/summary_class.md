---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/summary_class/
title: Package Classes (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:28.595072+00:00
---

# Package Classes (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 

Summary of entries of Classes for firestore.

## Classes 

### [FirestoreAdminClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client.FirestoreAdminClient)

The Cloud Firestore Admin API.

This API provides several administrative services for Cloud Firestore.

Project, Database, Namespace, Collection, Collection Group, and Document are used as defined in the Google Cloud Firestore API.

Operation: An Operation represents work being performed in the background.

The index service manages Cloud Firestore indexes.

Index creation is performed asynchronously. An Operation resource is created for each such asynchronous operation. The state of the operation (including any errors encountered) may be queried via the Operation resource.

The Operations collection provides a record of actions performed for the specified Project (including any Operations in progress). Operations are not created directly but through calls on other collections or resources.

An Operation that is done may be deleted so that it is no longer listed as part of the Operation collection. Operations are garbage collected after 30 days. By default, ListOperations will only return in progress and failed operations. To list completed operation, issue a ListOperations request with the filter `done: true`.

Operations are created by service `FirestoreAdmin`, but are accessed via service `google.longrunning.Operations`.

### [FirestoreBundle](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_bundle.bundle.FirestoreBundle)

A group of serialized documents and queries, suitable for longterm storage or query resumption.

If any queries are added to this bundle, all associated documents will be loaded and stored in memory for serialization.

Usage:
    
    
    from google.cloud.firestore import [Client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client.html), _helpers
    from google.cloud.firestore_bundle import FirestoreBundle
    
    db = Client()
    bundle = FirestoreBundle('my-bundle')
    bundle.[add_named_query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_bundle.bundle.FirestoreBundle.html#google_cloud_firestore_bundle_bundle_FirestoreBundle_add_named_query)('all-users', db.[collection](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client.html#google_cloud_firestore_v1_client_Client_collection)('users')._query())
    bundle.[add_named_query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_bundle.bundle.FirestoreBundle.html#google_cloud_firestore_bundle_bundle_FirestoreBundle_add_named_query)(
        'top-ten-hamburgers',
        db.[collection](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client.html#google_cloud_firestore_v1_client_Client_collection)('hamburgers').limit(limit=10),
    )
    serialized: str = bundle.[build](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_bundle.bundle.FirestoreBundle.html#google_cloud_firestore_bundle_bundle_FirestoreBundle_build)()
    
    # Store somewhere like a Google Cloud Storage bucket for retrieval by
    # a client SDK.
    

### [AggregationQuery](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.aggregation.AggregationQuery)

Represents an aggregation query to the Firestore API.

### [AsyncAggregationQuery](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_aggregation.AsyncAggregationQuery)

Represents an aggregation query to the Firestore API.

### [AsyncWriteBatch](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_batch.AsyncWriteBatch)

Accumulate write operations to be sent in a batch.

This has the same set of methods for write operations that xref_AsyncDocumentReference does, e.g. xref_create.

### [AsyncClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_client.AsyncClient)

Client for interacting with Google Cloud Firestore API.

**Note:** Since the Cloud Firestore API requires the gRPC transport, no `_http` argument is accepted by this class. 

### [AsyncCollectionReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_collection.AsyncCollectionReference)

A reference to a collection in a Firestore database.

The collection may already exist or this class can facilitate creation of documents within the collection.

### [AsyncDocumentReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_document.AsyncDocumentReference)

A reference to a document in a Firestore database.

The document may already exist or can be created by this class.

### [AsyncCollectionGroup](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_query.AsyncCollectionGroup)

Represents a Collection Group in the Firestore API.

This is a specialization of `.AsyncQuery` that includes all documents in the database that are contained in a collection or subcollection of the given parent.

### [AsyncQuery](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_query.AsyncQuery)

Represents a query to the Firestore API.

Instances of this class are considered immutable: all methods that would modify an instance instead return a new instance.

### [AsyncTransaction](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_transaction.AsyncTransaction)

Accumulate read-and-write operations to be sent in a transaction.

### [AggregationResult](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.AggregationResult)

A class representing result from Aggregation Query

### [AvgAggregation](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.AvgAggregation)

Helper class that provides a standard way to create an ABC using inheritance.

### [BaseAggregation](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.BaseAggregation)

Helper class that provides a standard way to create an ABC using inheritance.

### [BaseAggregationQuery](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.BaseAggregationQuery)

Represents an aggregation query to the Firestore API.

### [CountAggregation](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.CountAggregation)

Helper class that provides a standard way to create an ABC using inheritance.

### [SumAggregation](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation.SumAggregation)

Helper class that provides a standard way to create an ABC using inheritance.

### [BaseBatch](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_batch.BaseBatch)

Accumulate write operations to be sent in a batch.

This has the same set of methods for write operations that xref_DocumentReference does, e.g. xref_create.

### [BaseWriteBatch](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_batch.BaseWriteBatch)

Base class for a/sync implementations of the `commit` RPC. `commit` is useful for lower volumes or when the order of write operations is important.

### [BaseClient](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_client.BaseClient)

Client for interacting with Google Cloud Firestore API.

**Note:** Since the Cloud Firestore API requires the gRPC transport, no `_http` argument is accepted by this class. 

### [BaseCollectionReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_collection.BaseCollectionReference)

A reference to a collection in a Firestore database.

The collection may already exist or this class can facilitate creation of documents within the collection.

### [BaseDocumentReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document.BaseDocumentReference)

A reference to a document in a Firestore database.

The document may already exist or can be created by this class.

### [DocumentSnapshot](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document.DocumentSnapshot)

A snapshot of document data in a Firestore database.

This represents data retrieved at a specific time and may not contain all fields stored for the document (i.e. a hand-picked selection of fields may have been retrieved).

Instances of this class are not intended to be constructed by hand, rather they'll be returned as responses to various methods, such as xref_get.

### [And](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.And)

Class representation of an AND Filter.

### [BaseCollectionGroup](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.BaseCollectionGroup)

Represents a Collection Group in the Firestore API.

This is a specialization of `.Query` that includes all documents in the database that are contained in a collection or subcollection of the given parent.

### [BaseCompositeFilter](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.BaseCompositeFilter)

Base class for a Composite Filter. (either OR or AND).

### [BaseFilter](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.BaseFilter)

Base class for Filters

### [BaseQuery](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.BaseQuery)

Represents a query to the Firestore API.

Instances of this class are considered immutable: all methods that would modify an instance instead return a new instance.

### [FieldFilter](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.FieldFilter)

Class representation of a Field Filter.

### [Or](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.Or)

Class representation of an OR Filter.

### [QueryPartition](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query.QueryPartition)

Represents a bounded partition of a collection group query.

Contains cursors that can be used in a query as a starting and/or end point for the collection group query. The cursors may only be used in a query that matches the constraints of the query that produced this partition.

### [BaseTransaction](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_transaction.BaseTransaction)

Accumulate read-and-write operations to be sent in a transaction.

### [WriteBatch](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.batch.WriteBatch)

Accumulate write operations to be sent in a batch. Use this over `BulkWriteBatch` for lower volumes or when the order of operations within a given batch is important.

This has the same set of methods for write operations that xref_DocumentReference does, e.g. xref_create.

### [BulkWriter](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.bulk_writer.BulkWriter)

Accumulate and efficiently save large amounts of document write operations to the server.

BulkWriter can handle large data migrations or updates, buffering records in memory and submitting them to the server in batches of 20.

The submission of batches is internally parallelized with a ThreadPoolExecutor, meaning end developers do not need to manage an event loop or worry about asyncio to see parallelization speed ups (which can easily 10x throughput). Because of this, there is no companion `AsyncBulkWriter` class, as is usually seen with other utility classes.

Usage:
    
    
    # Instantiate the BulkWriter. This works from either `Client` or
    # `AsyncClient`.
    db = firestore.Client()
    bulk_writer = db.bulk_writer()
    
    # Attach an optional success listener to be called once per document.
    bulk_writer.on_write_result(
        lambda reference, result, bulk_writer: print(f'Saved {reference._document_path}')
    )
    
    # Queue an arbitrary amount of write operations.
    # Assume `my_new_records` is a list of (DocumentReference, dict,)
    # tuple-pairs that you supply.
    
    reference: DocumentReference
    data: dict
    for reference, data in my_new_records:
        bulk_writer.create(reference, data)
    
    # Block until all pooled writes are complete.
    bulk_writer.flush()
    

### [Client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client)

Client for interacting with Google Cloud Firestore API.

**Note:** Since the Cloud Firestore API requires the gRPC transport, no `_http` argument is accepted by this class. 

### [CollectionReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.collection.CollectionReference)

A reference to a collection in a Firestore database.

The collection may already exist or this class can facilitate creation of documents within the collection.

### [DocumentReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.document.DocumentReference)

A reference to a document in a Firestore database.

The document may already exist or can be created by this class.

### [FieldPath](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path.FieldPath)

Field Path object for client use.

A field path is a sequence of element keys, separated by periods. Each element key can be either a simple identifier, or a full unicode string.

In the string representation of a field path, non-identifier elements must be quoted using backticks, with internal backticks and backslashes escaped with a backslash.

### [CollectionGroup](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.CollectionGroup)

Represents a Collection Group in the Firestore API.

This is a specialization of `.Query` that includes all documents in the database that are contained in a collection or subcollection of the given parent.

### [Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query)

Represents a query to the Firestore API.

Instances of this class are considered immutable: all methods that would modify an instance instead return a new instance.

### [Transaction](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transaction.Transaction)

Accumulate read-and-write operations to be sent in a transaction.

### [ArrayRemove](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transforms.ArrayRemove)

Field transform: remove values from an array field.

See: <https://cloud.google.com/firestore/docs/reference/rpc/google.firestore.v1#google.firestore.v1.DocumentTransform.FieldTransform.FIELDS.google.firestore.v1.ArrayValue.google.firestore.v1.DocumentTransform.FieldTransform.remove_all_from_array>

### [ArrayUnion](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transforms.ArrayUnion)

Field transform: appends missing values to an array field.

See: <https://cloud.google.com/firestore/docs/reference/rpc/google.firestore.v1#google.firestore.v1.DocumentTransform.FieldTransform.FIELDS.google.firestore.v1.ArrayValue.google.firestore.v1.DocumentTransform.FieldTransform.append_missing_elements>

### [Increment](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transforms.Increment)

Field transform: increment a numeric field with specified value.

See: <https://cloud.google.com/firestore/docs/reference/rpc/google.firestore.v1#google.firestore.v1.DocumentTransform.FieldTransform.FIELDS.google.firestore.v1.ArrayValue.google.firestore.v1.DocumentTransform.FieldTransform.increment>

### [Maximum](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transforms.Maximum)

Field transform: bound numeric field with specified value.

See: <https://cloud.google.com/firestore/docs/reference/rpc/google.firestore.v1#google.firestore.v1.DocumentTransform.FieldTransform.FIELDS.google.firestore.v1.ArrayValue.google.firestore.v1.DocumentTransform.FieldTransform.maximum>

### [Minimum](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transforms.Minimum)

Field transform: bound numeric field with specified value.

See: <https://cloud.google.com/firestore/docs/reference/rpc/google.firestore.v1#google.firestore.v1.DocumentTransform.FieldTransform.FIELDS.google.firestore.v1.ArrayValue.google.firestore.v1.DocumentTransform.FieldTransform.minimum>

### [Sentinel](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transforms.Sentinel)

Sentinel objects used to signal special handling.

### [AggregationResult](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.AggregationResult)

The result of a single bucket from a Firestore aggregation query.

The keys of `aggregate_fields` are the same for all results in an aggregation query, unlike document queries which can have different fields present for each result.

### [AggregateFieldsEntry](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.AggregationResult.AggregateFieldsEntry)

The abstract base class for a message.

### [ArrayValue](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ArrayValue)

An array value.

### [BatchGetDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.BatchGetDocumentsRequest)

The request for `Firestore.BatchGetDocuments][google.firestore.v1.Firestore.BatchGetDocuments]`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BatchGetDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.BatchGetDocumentsResponse)

The streamed response for `Firestore.BatchGetDocuments][google.firestore.v1.Firestore.BatchGetDocuments]`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BatchWriteRequest](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.BatchWriteRequest)

The request for `Firestore.BatchWrite][google.firestore.v1.Firestore.BatchWrite]`.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.BatchWriteRequest.LabelsEntry)

The abstract base class for a message.

### [BatchWriteResponse](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.BatchWriteResponse)

The response from `Firestore.BatchWrite][google.firestore.v1.Firestore.BatchWrite]`.

### [BeginTransactionRequest](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.BeginTransactionRequest)

The request for `Firestore.BeginTransaction][google.firestore.v1.Firestore.BeginTransaction]`.

### [BeginTransactionResponse](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.BeginTransactionResponse)

The response for `Firestore.BeginTransaction][google.firestore.v1.Firestore.BeginTransaction]`.

### [BitSequence](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.BitSequence)

A sequence of bits, encoded in a byte array.

Each byte in the `bitmap` byte array stores 8 bits of the sequence. The only exception is the last byte, which may store 8 _or fewer_ bits. The `padding` defines the number of bits of the last byte to be ignored as "padding". The values of these "padding" bits are unspecified and must be ignored.

To retrieve the first bit, bit 0, calculate: `(bitmap[0] & 0x01) != 0`. To retrieve the second bit, bit 1, calculate: `(bitmap[0] & 0x02) != 0`. To retrieve the third bit, bit 2, calculate: `(bitmap[0] & 0x04) != 0`. To retrieve the fourth bit, bit 3, calculate: `(bitmap[0] & 0x08) != 0`. To retrieve bit n, calculate: `(bitmap[n / 8] & (0x01 << (n % 8))) != 0`.

The "size" of a `BitSequence` (the number of bits it contains) is calculated by this formula: `(bitmap.length * 8) - padding`.

### [BloomFilter](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.BloomFilter)

A bloom filter (<https://en.wikipedia.org/wiki/Bloom_filter>).

The bloom filter hashes the entries with MD5 and treats the resulting 128-bit hash as 2 distinct 64-bit hash values, interpreted as unsigned integers using 2's complement encoding.

These two hash values, named `h1` and `h2`, are then used to compute the `hash_count` hash values using the formula, starting at `i=0`:

::
    
    
    h(i) = h1 + (i * h2)
    

These resulting values are then taken modulo the number of bits in the bloom filter to get the bits of the bloom filter to test for the given entry.

### [CommitRequest](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.CommitRequest)

The request for `Firestore.Commit][google.firestore.v1.Firestore.Commit]`.

### [CommitResponse](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.CommitResponse)

The response for `Firestore.Commit][google.firestore.v1.Firestore.Commit]`.

### [CreateDocumentRequest](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.CreateDocumentRequest)

The request for `Firestore.CreateDocument][google.firestore.v1.Firestore.CreateDocument]`.

### [Cursor](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.Cursor)

A position in a query result set.

### [DeleteDocumentRequest](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.DeleteDocumentRequest)

The request for `Firestore.DeleteDocument][google.firestore.v1.Firestore.DeleteDocument]`.

### [Document](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.Document)

A Firestore document.

Must not exceed 1 MiB - 4 bytes.

### [FieldsEntry](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.Document.FieldsEntry)

The abstract base class for a message.

### [DocumentChange](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.DocumentChange)

A `Document][google.firestore.v1.Document]` has changed.

May be the result of multiple `writes][google.firestore.v1.Write]`, including deletes, that ultimately resulted in a new value for the `Document][google.firestore.v1.Document]`.

Multiple `DocumentChange][google.firestore.v1.DocumentChange]` messages may be returned for the same logical change, if multiple targets are affected.

### [DocumentDelete](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.DocumentDelete)

A `Document][google.firestore.v1.Document]` has been deleted.

May be the result of multiple `writes][google.firestore.v1.Write]`, including updates, the last of which deleted the `Document][google.firestore.v1.Document]`.

Multiple `DocumentDelete][google.firestore.v1.DocumentDelete]` messages may be returned for the same logical delete, if multiple targets are affected.

### [DocumentMask](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.DocumentMask)

A set of field paths on a document. Used to restrict a get or update operation on a document to a subset of its fields. This is different from standard field masks, as this is always scoped to a `Document][google.firestore.v1.Document]`, and takes in account the dynamic nature of `Value][google.firestore.v1.Value]`.

### [DocumentRemove](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.DocumentRemove)

A `Document][google.firestore.v1.Document]` has been removed from the view of the targets.

Sent if the document is no longer relevant to a target and is out of view. Can be sent instead of a DocumentDelete or a DocumentChange if the server can not send the new value of the document.

Multiple `DocumentRemove][google.firestore.v1.DocumentRemove]` messages may be returned for the same logical write or delete, if multiple targets are affected.

### [DocumentTransform](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.DocumentTransform)

A transformation of a document.

### [FieldTransform](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.DocumentTransform.FieldTransform)

A transformation of a field of the document.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ServerValue](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.DocumentTransform.FieldTransform.ServerValue)

A value that is calculated by the server.

### [ExecutePipelineRequest](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ExecutePipelineRequest)

The request for `Firestore.ExecutePipeline][google.firestore.v1.Firestore.ExecutePipeline]`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExecutePipelineResponse](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ExecutePipelineResponse)

The response for [Firestore.Execute][].

### [ExecutionStats](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ExecutionStats)

Execution statistics for the query.

### [ExistenceFilter](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ExistenceFilter)

A digest of all the documents that match a given target.

### [ExplainMetrics](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ExplainMetrics)

Explain metrics for the query.

### [ExplainOptions](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ExplainOptions)

Explain options for the query.

### [ExplainStats](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ExplainStats)

Pipeline explain stats.

Depending on the explain options in the original request, this can contain the optimized plan and / or execution stats.

### [Function](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.Function)

Represents an unevaluated scalar expression.

For example, the expression `like(user_name, "%alice%")` is represented as:

::

name: "like" args { field_reference: "user_name" } args { string_value: "%alice%" }

### [OptionsEntry](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.Function.OptionsEntry)

The abstract base class for a message.

### [GetDocumentRequest](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.GetDocumentRequest)

The request for `Firestore.GetDocument][google.firestore.v1.Firestore.GetDocument]`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ListCollectionIdsRequest](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ListCollectionIdsRequest)

The request for `Firestore.ListCollectionIds][google.firestore.v1.Firestore.ListCollectionIds]`.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ListCollectionIdsResponse](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ListCollectionIdsResponse)

The response from `Firestore.ListCollectionIds][google.firestore.v1.Firestore.ListCollectionIds]`.

### [ListDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ListDocumentsRequest)

The request for `Firestore.ListDocuments][google.firestore.v1.Firestore.ListDocuments]`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ListDocumentsResponse](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ListDocumentsResponse)

The response for `Firestore.ListDocuments][google.firestore.v1.Firestore.ListDocuments]`.

### [ListenRequest](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ListenRequest)

A request for `Firestore.Listen][google.firestore.v1.Firestore.Listen]`

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ListenRequest.LabelsEntry)

The abstract base class for a message.

### [ListenResponse](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ListenResponse)

The response for `Firestore.Listen][google.firestore.v1.Firestore.Listen]`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [MapValue](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.MapValue)

A map value.

### [FieldsEntry](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.MapValue.FieldsEntry)

The abstract base class for a message.

### [PartitionQueryRequest](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.PartitionQueryRequest)

The request for `Firestore.PartitionQuery][google.firestore.v1.Firestore.PartitionQuery]`.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PartitionQueryResponse](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.PartitionQueryResponse)

The response for `Firestore.PartitionQuery][google.firestore.v1.Firestore.PartitionQuery]`.

### [Pipeline](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.Pipeline)

A Firestore query represented as an ordered list of operations / stages.

### [Stage](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.Pipeline.Stage)

A single operation within a pipeline.

A stage is made up of a unique name, and a list of arguments. The exact number of arguments & types is dependent on the stage type.

To give an example, the stage `filter(state = "MD")` would be encoded as:

::

name: "filter" args { function_value { name: "eq" args { field_reference_value: "state" } args { string_value: "MD" } } }

See public documentation for the full list.

### [OptionsEntry](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.Pipeline.Stage.OptionsEntry)

The abstract base class for a message.

### [PlanSummary](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.PlanSummary)

Planning phase information for the query.

### [Precondition](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.Precondition)

A precondition on a document, used for conditional operations.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RequestOptions](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.RequestOptions)

Options for a server request.

### [RollbackRequest](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.RollbackRequest)

The request for `Firestore.Rollback][google.firestore.v1.Firestore.Rollback]`.

### [RunAggregationQueryRequest](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.RunAggregationQueryRequest)

The request for `Firestore.RunAggregationQuery][google.firestore.v1.Firestore.RunAggregationQuery]`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RunAggregationQueryResponse](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.RunAggregationQueryResponse)

The response for `Firestore.RunAggregationQuery][google.firestore.v1.Firestore.RunAggregationQuery]`.

### [RunQueryRequest](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.RunQueryRequest)

The request for `Firestore.RunQuery][google.firestore.v1.Firestore.RunQuery]`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RunQueryResponse](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.RunQueryResponse)

The response for `Firestore.RunQuery][google.firestore.v1.Firestore.RunQuery]`.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [StructuredAggregationQuery](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredAggregationQuery)

Firestore query for running an aggregation over a `StructuredQuery][google.firestore.v1.StructuredQuery]`.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Aggregation](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredAggregationQuery.Aggregation)

Defines an aggregation that produces a single result.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Avg](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredAggregationQuery.Aggregation.Avg)

Average of the values of the requested field.

  * Only numeric values will be aggregated. All non-numeric values including `NULL` are skipped.

  * If the aggregated values contain `NaN`, returns `NaN`. Infinity math follows IEEE-754 standards.

  * If the aggregated value set is empty, returns `NULL`.

  * Always returns the result as a double.




### [Count](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredAggregationQuery.Aggregation.Count)

Count of documents that match the query.

The `COUNT(*)` aggregation function operates on the entire document so it does not require a field reference.

### [Sum](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredAggregationQuery.Aggregation.Sum)

Sum of the values of the requested field.

  * Only numeric values will be aggregated. All non-numeric values including `NULL` are skipped.

  * If the aggregated values contain `NaN`, returns `NaN`. Infinity math follows IEEE-754 standards.

  * If the aggregated value set is empty, returns 0.

  * Returns a 64-bit integer if all aggregated numbers are integers and the sum result does not overflow. Otherwise, the result is returned as a double. Note that even if all the aggregated values are integers, the result is returned as a double if it cannot fit within a 64-bit signed integer. When this occurs, the returned value will lose precision.

  * When underflow occurs, floating-point aggregation is non-deterministic. This means that running the same query repeatedly without any changes to the underlying values could produce slightly different results each time. In those cases, values should be stored as integers over floating-point numbers.




### [StructuredPipeline](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredPipeline)

A Firestore query represented as an ordered list of operations / stages.

This is considered the top-level function which plans and executes a query. It is logically equivalent to `query(stages, options)`, but prevents the client from having to build a function wrapper.

### [OptionsEntry](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredPipeline.OptionsEntry)

The abstract base class for a message.

### [StructuredQuery](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredQuery)

A Firestore query.

The query stages are executed in the following order:

  1. from
  2. where
  3. select
  4. order_by + start_at + end_at
  5. offset
  6. limit
  7. find_nearest



### [CollectionSelector](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredQuery.CollectionSelector)

A selection of a collection, such as `messages as m1`.

### [CompositeFilter](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredQuery.CompositeFilter)

A filter that merges multiple other filters using the given operator.

### [Operator](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredQuery.CompositeFilter.Operator)

A composite filter operator.

### [Direction](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredQuery.Direction)

A sort direction.

### [FieldFilter](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredQuery.FieldFilter)

A filter on a specific field.

### [Operator](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredQuery.FieldFilter.Operator)

A field filter operator.
    
    
        Requires:
    
        - That `field` come first in `order_by`.
    LESS_THAN_OR_EQUAL (2):
        The given `field` is less than or equal to the given
        `value`.
    
        Requires:
    
        - That `field` come first in `order_by`.
    GREATER_THAN (3):
        The given `field` is greater than the given `value`.
    
        Requires:
    
        - That `field` come first in `order_by`.
    GREATER_THAN_OR_EQUAL (4):
        The given `field` is greater than or equal to the given
        `value`.
    
        Requires:
    
        - That `field` come first in `order_by`.
    EQUAL (5):
        The given `field` is equal to the given `value`.
    NOT_EQUAL (6):
        The given `field` is not equal to the given `value`.
    
        Requires:
    
        - No other `NOT_EQUAL`, `NOT_IN`, `IS_NOT_NULL`, or
          `IS_NOT_NAN`.
        - That `field` comes first in the `order_by`.
    ARRAY_CONTAINS (7):
        The given `field` is an array that contains the given
        `value`.
    IN (8):
        The given `field` is equal to at least one value in the
        given array.
    
        Requires:
    
        - That `value` is a non-empty `ArrayValue`, subject to
          disjunction limits.
        - No `NOT_IN` filters in the same query.
    ARRAY_CONTAINS_ANY (9):
        The given `field` is an array that contains any of the
        values in the given array.
    
        Requires:
    
        - That `value` is a non-empty `ArrayValue`, subject to
          disjunction limits.
        - No other `ARRAY_CONTAINS_ANY` filters within the same
          disjunction.
        - No `NOT_IN` filters in the same query.
    NOT_IN (10):
        The value of the `field` is not in the given array.
    
        Requires:
    
        - That `value` is a non-empty `ArrayValue` with at most
          10 values.
        - No other `OR`, `IN`, `ARRAY_CONTAINS_ANY`,
          `NOT_IN`, `NOT_EQUAL`, `IS_NOT_NULL`, or
          `IS_NOT_NAN`.
        - That `field` comes first in the `order_by`.
    

### [FieldReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredQuery.FieldReference)

A reference to a field in a document, ex: `stats.operations`.

### [Filter](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredQuery.Filter)

A filter.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [FindNearest](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredQuery.FindNearest)

Nearest Neighbors search config. The ordering provided by FindNearest supersedes the order_by stage. If multiple documents have the same vector distance, the returned document order is not guaranteed to be stable between queries.

### [DistanceMeasure](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredQuery.FindNearest.DistanceMeasure)

The distance measure to use when comparing vectors.

### [Order](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredQuery.Order)

An order on a field.

### [Projection](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredQuery.Projection)

The projection of document's fields to return.

### [UnaryFilter](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredQuery.UnaryFilter)

A filter with a single operand.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Operator](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredQuery.UnaryFilter.Operator)

A unary operator.
    
    
        Requires:
    
        - No other `NOT_EQUAL`, `NOT_IN`, `IS_NOT_NULL`, or
          `IS_NOT_NAN`.
        - That `field` comes first in the `order_by`.
    IS_NOT_NULL (5):
        The given `field` is not equal to `NULL`.
    
        Requires:
    
        - A single `NOT_EQUAL`, `NOT_IN`, `IS_NOT_NULL`, or
          `IS_NOT_NAN`.
        - That `field` comes first in the `order_by`.
    

### [Target](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.Target)

A specification of a set of documents to listen to.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DocumentsTarget](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.Target.DocumentsTarget)

A target specified by a set of documents names.

### [QueryTarget](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.Target.QueryTarget)

A target specified by a query.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TargetChange](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.TargetChange)

Targets being watched have changed.

### [TargetChangeType](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.TargetChange.TargetChangeType)

The type of change.
    
    
        This will be sent after or with a `read_time` that is
        greater than or equal to the time at which the targets were
        added.
    
        Listeners can wait for this change if read-after-write
        semantics are desired.
    RESET (4):
        The targets have been reset, and a new initial state for the
        targets will be returned in subsequent changes.
    
        After the initial state is complete, `CURRENT` will be
        returned even if the target was previously indicated to be
        `CURRENT`.
    

### [TransactionOptions](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.TransactionOptions)

Options for creating a new transaction.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConcurrencyMode](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.TransactionOptions.ConcurrencyMode)

The type of concurrency control mode for transactions.

### [ReadOnly](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.TransactionOptions.ReadOnly)

Options for a transaction that can only be used to read documents.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ReadWrite](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.TransactionOptions.ReadWrite)

Options for a transaction that can be used to read and write documents.

### [UpdateDocumentRequest](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.UpdateDocumentRequest)

The request for `Firestore.UpdateDocument][google.firestore.v1.Firestore.UpdateDocument]`.

### [Value](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.Value)

A message that can hold any of the supported value types.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Write](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.Write)

A write on a document.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [WriteRequest](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.WriteRequest)

The request for `Firestore.Write][google.firestore.v1.Firestore.Write]`.

The first request creates a stream, or resumes an existing one from a token.

When creating a new stream, the server replies with a response containing only an ID and a token, to use in the next request.

When resuming a stream, the server first streams any responses later than the given token, then a response containing only an up-to-date token, to use in the next request.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.WriteRequest.LabelsEntry)

The abstract base class for a message.

### [WriteResponse](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.WriteResponse)

The response for `Firestore.Write][google.firestore.v1.Firestore.Write]`.

### [WriteResult](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.WriteResult)

The result of applying a write.

## Modules 

### [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_admin_v1.services.firestore_admin.client)

API documentation for `firestore_admin_v1.services.firestore_admin.client` module.

### [bundle](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_bundle.bundle)

Classes for representing bundles for the Google Cloud Firestore API.

### [aggregation](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.aggregation)

Classes for representing aggregation queries for the Google Cloud Firestore API.

A [AggregationQuery](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.aggregation.AggregationQuery) can be created directly from a Collection and that can be a more common way to create an aggregation query than direct usage of the constructor.

### [async_aggregation](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_aggregation)

Classes for representing Async aggregation queries for the Google Cloud Firestore API.

A [AsyncAggregationQuery](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_aggregation.AsyncAggregationQuery) can be created directly from a AsyncCollection and that can be a more common way to create an aggregation query than direct usage of the constructor.

### [async_batch](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_batch)

Helpers for batch requests to the Google Cloud Firestore API.

### [async_client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_client)

Client for interacting with the Google Cloud Firestore API.

This is the base from which all interactions with the API occur.

In the hierarchy of API concepts

  * a [Client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client) owns a [AsyncCollectionReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_collection.AsyncCollectionReference)
  * a [Client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client) owns a [AsyncDocumentReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_document.AsyncDocumentReference)



### [async_collection](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_collection)

Classes for representing collections for the Google Cloud Firestore API.

### [async_document](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_document)

Classes for representing documents for the Google Cloud Firestore API.

### [async_query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_query)

Classes for representing queries for the Google Cloud Firestore API.

A [Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query) can be created directly from a Collection and that can be a more common way to create a query than direct usage of the constructor.

### [async_transaction](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_transaction)

Helpers for applying Google Cloud Firestore changes in a transaction.

### [base_aggregation](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_aggregation)

Classes for representing aggregation queries for the Google Cloud Firestore API.

A [AggregationQuery](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.aggregation.AggregationQuery) can be created directly from a Collection and that can be a more common way to create an aggregation query than direct usage of the constructor.

### [base_batch](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_batch)

Helpers for batch requests to the Google Cloud Firestore API.

### [base_client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_client)

Client for interacting with the Google Cloud Firestore API.

This is the base from which all interactions with the API occur.

In the hierarchy of API concepts

  * a [Client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client) owns a [CollectionReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.collection.CollectionReference)
  * a [Client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client) owns a [DocumentReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.document.DocumentReference)



### [base_collection](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_collection)

Classes for representing collections for the Google Cloud Firestore API.

### [base_document](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document)

Classes for representing documents for the Google Cloud Firestore API.

### [base_query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_query)

Classes for representing queries for the Google Cloud Firestore API.

A [Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query) can be created directly from a Collection and that can be a more common way to create a query than direct usage of the constructor.

### [base_transaction](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_transaction)

Helpers for applying Google Cloud Firestore changes in a transaction.

### [batch](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.batch)

Helpers for batch requests to the Google Cloud Firestore API.

### [client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client)

Client for interacting with the Google Cloud Firestore API.

This is the base from which all interactions with the API occur.

In the hierarchy of API concepts

  * a [Client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client) owns a [CollectionReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.collection.CollectionReference)
  * a [Client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client) owns a [DocumentReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.document.DocumentReference)



### [collection](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.collection)

Classes for representing collections for the Google Cloud Firestore API.

### [document](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.document)

Classes for representing documents for the Google Cloud Firestore API.

### [field_path](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.field_path)

Utilities for managing / converting field paths to / from strings.

### [query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query)

Classes for representing queries for the Google Cloud Firestore API.

A [Query](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.query.Query) can be created directly from a Collection and that can be a more common way to create a query than direct usage of the constructor.

### [transaction](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transaction)

Helpers for applying Google Cloud Firestore changes in a transaction.

### [transforms](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transforms)

Helpful constants to use for Google Cloud Firestore.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
