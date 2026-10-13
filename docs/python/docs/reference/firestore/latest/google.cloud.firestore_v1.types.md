---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types
title: Package types (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:38.881129+00:00
---

# Package types (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 

API documentation for `firestore_v1.types` package.

## Classes 

### [AggregationResult](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.AggregationResult)

The result of a single bucket from a Firestore aggregation query.

The keys of `aggregate_fields` are the same for all results in an aggregation query, unlike document queries which can have different fields present for each result.

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

### [ListenResponse](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.ListenResponse)

The response for `Firestore.Listen][google.firestore.v1.Firestore.Listen]`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [MapValue](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.MapValue)

A map value.

### [PartitionQueryRequest](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.PartitionQueryRequest)

The request for `Firestore.PartitionQuery][google.firestore.v1.Firestore.PartitionQuery]`.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PartitionQueryResponse](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.PartitionQueryResponse)

The response for `Firestore.PartitionQuery][google.firestore.v1.Firestore.PartitionQuery]`.

### [Pipeline](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.Pipeline)

A Firestore query represented as an ordered list of operations / stages.

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

### [StructuredPipeline](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.StructuredPipeline)

A Firestore query represented as an ordered list of operations / stages.

This is considered the top-level function which plans and executes a query. It is logically equivalent to `query(stages, options)`, but prevents the client from having to build a function wrapper.

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



### [Target](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.Target)

A specification of a set of documents to listen to.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TargetChange](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.TargetChange)

Targets being watched have changed.

### [TransactionOptions](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.TransactionOptions)

Options for creating a new transaction.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

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

### [WriteResponse](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.WriteResponse)

The response for `Firestore.Write][google.firestore.v1.Firestore.Write]`.

### [WriteResult](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.WriteResult)

The result of applying a write.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
