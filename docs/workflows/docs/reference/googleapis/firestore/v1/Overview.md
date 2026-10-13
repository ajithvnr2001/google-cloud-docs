---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview/
title: Types overview \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:44:02.542414+00:00
---

# Types overview  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Types overview Stay organized with collections  Save and categorize content based on your preferences. 

## ArrayValue

An array value. Fields  
---  
`values[]` |  `object ([Value](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Value))` Values in the array.  
  
## BatchGetDocumentsRequest

The request for Firestore.BatchGetDocuments. Fields  
---  
`documents[]` |  `string` The names of the documents to retrieve. In the format: `projects/{project_id}/databases/{database_id}/documents/{document_path}`. The request will fail if any of the document is not a child resource of the given `database`. Duplicate names will be elided.  
`mask` |  `object ([DocumentMask](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#DocumentMask))` The fields to return. If not set, returns all fields. If a document has a field that is not present in this mask, that field will not be returned in the response.  
`newTransaction` |  `object ([TransactionOptions](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#TransactionOptions))` Starts a new transaction and reads the documents. Defaults to a read-only transaction. The new transaction ID will be returned as the first response in the stream.  
`readTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` Reads documents as they were at the given time. This may not be older than 270 seconds.  
`transaction` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Reads documents in a transaction.  
  
## BatchGetDocumentsResponse

The streamed response for Firestore.BatchGetDocuments. Fields  
---  
`found` |  `object ([Document](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Document))` A document that was requested.  
`missing` |  `string` A document name that was requested but does not exist. In the format: `projects/{project_id}/databases/{database_id}/documents/{document_path}`.  
`readTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` The time at which the document was read. This may be monotically increasing, in this case the previous documents in the result stream are guaranteed not to have changed between their read_time and this one.  
`transaction` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The transaction that was started as part of this request. Will only be set in the first response, and only if BatchGetDocumentsRequest.new_transaction was set in the request.  
  
## BatchWriteRequest

The request for Firestore.BatchWrite. Fields  
---  
`labels` |  `map (key: string, value: string)` Labels associated with this batch write.  
`writes[]` |  `object ([Write](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Write))` The writes to apply. Method does not apply writes atomically and does not guarantee ordering. Each write succeeds or fails independently. You cannot write to the same document more than once per request.  
  
## BatchWriteResponse

The response from Firestore.BatchWrite. Fields  
---  
`status[]` |  `object ([Status](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Status))` The status of applying the writes. This i-th write status corresponds to the i-th write in the request.  
`writeResults[]` |  `object ([WriteResult](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#WriteResult))` The result of applying the writes. This i-th write result corresponds to the i-th write in the request.  
  
## BeginTransactionRequest

The request for Firestore.BeginTransaction. Fields  
---  
`options` |  `object ([TransactionOptions](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#TransactionOptions))` The options for the transaction. Defaults to a read-write transaction.  
  
## BeginTransactionResponse

The response for Firestore.BeginTransaction. Fields  
---  
`transaction` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The transaction that was started.  
  
## CollectionSelector

A selection of a collection, such as `messages as m1`. Fields  
---  
`allDescendants` |  `boolean` When false, selects only collections that are immediate children of the `parent` specified in the containing `RunQueryRequest`. When true, selects all descendant collections.  
`collectionId` |  `string` The collection ID. When set, selects only collections with this ID.  
  
## CommitRequest

The request for Firestore.Commit. Fields  
---  
`transaction` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` If set, applies all writes in this transaction, and commits it.  
`writes[]` |  `object ([Write](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Write))` The writes to apply. Always executed atomically and in order.  
  
## CommitResponse

The response for Firestore.Commit. Fields  
---  
`commitTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` The time at which the commit occurred. Any read with an equal or greater `read_time` is guaranteed to see the effects of the commit.  
`writeResults[]` |  `object ([WriteResult](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#WriteResult))` The result of applying the writes. This i-th write result corresponds to the i-th write in the request.  
  
## CompositeFilter

A filter that merges multiple other filters using the given operator. Fields  
---  
`filters[]` |  `object ([Filter](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Filter))` The list of filters to combine. Must contain at least one filter.  
`op` |  `enum` The operator for combining multiple filters.  
Enum type. Can be one of the following:  
`OPERATOR_UNSPECIFIED` | Unspecified. This value must not be used.  
`AND` | The results are required to satisfy each of the combined filters.  
  
## Cursor

A position in a query result set. Fields  
---  
`before` |  `boolean` If the position is just before or just after the given values, relative to the sort order defined by the query.  
`values[]` |  `object ([Value](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Value))` The values that represent a position, in the order they appear in the order by clause of a query. Can contain fewer values than specified in the order by clause.  
  
## Document

A Firestore document. Must not exceed 1 MiB - 4 bytes. Fields  
---  
`createTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` Output only. The time at which the document was created. This value increases monotonically when a document is deleted then recreated. It can also be compared to values from other documents and the `read_time` of a query.  
`fields` |  `map (key: string, value: object ([Value](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Value)))` The document's fields. The map keys represent field names. A simple field name contains only characters `a` to `z`, `A` to `Z`, `0` to `9`, or `_`, and must not start with `0` to `9`. For example, `foo_bar_17`. Field names matching the regular expression `__.*__` are reserved. Reserved field names are forbidden except in certain documented contexts. The map keys, represented as UTF-8, must not exceed 1,500 bytes and cannot be empty. Field paths may be used in other contexts to refer to structured fields defined here. For `map_value`, the field path is represented by the simple or quoted field names of the containing fields, delimited by `.`. For example, the structured field `"foo" : { map_value: { "x&y" : { string_value: "hello" }}}` would be represented by the field path `foo.x&y`. Within a field path, a quoted field name starts and ends with ``` and may contain any character. Some characters, including ```, must be escaped using a `\`. For example, ``x&y`` represents `x&y` and ``bak\`tik`` represents `bak`tik`.  
`name` |  `string` The resource name of the document, for example `projects/{project_id}/databases/{database_id}/documents/{document_path}`.  
`updateTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` Output only. The time at which the document was last changed. This value is initially set to the `create_time` then increases monotonically with each change to the document. It can also be compared to values from other documents and the `read_time` of a query.  
  
## DocumentChange

A Document has changed. May be the result of multiple writes, including deletes, that ultimately resulted in a new value for the Document. Multiple DocumentChange messages may be returned for the same logical change, if multiple targets are affected. Fields  
---  
`document` |  `object ([Document](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Document))` The new state of the Document. If `mask` is set, contains only fields that were updated or added.  
`removedTargetIds[]` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` A set of target IDs for targets that no longer match this document.  
`targetIds[]` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` A set of target IDs of targets that match this document.  
  
## DocumentDelete

A Document has been deleted. May be the result of multiple writes, including updates, the last of which deleted the Document. Multiple DocumentDelete messages may be returned for the same logical delete, if multiple targets are affected. Fields  
---  
`document` |  `string` The resource name of the Document that was deleted.  
`readTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` The read timestamp at which the delete was observed. Greater or equal to the `commit_time` of the delete.  
`removedTargetIds[]` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` A set of target IDs for targets that previously matched this entity.  
  
## DocumentMask

A set of field paths on a document. Used to restrict a get or update operation on a document to a subset of its fields. This is different from standard field masks, as this is always scoped to a Document, and takes in account the dynamic nature of Value. Fields  
---  
`fieldPaths[]` |  `string` The list of field paths in the mask. See Document.fields for a field path syntax reference.  
  
## DocumentRemove

A Document has been removed from the view of the targets. Sent if the document is no longer relevant to a target and is out of view. Can be sent instead of a DocumentDelete or a DocumentChange if the server can not send the new value of the document. Multiple DocumentRemove messages may be returned for the same logical write or delete, if multiple targets are affected. Fields  
---  
`document` |  `string` The resource name of the Document that has gone out of view.  
`readTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` The read timestamp at which the remove was observed. Greater or equal to the `commit_time` of the change/delete/remove.  
`removedTargetIds[]` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` A set of target IDs for targets that previously matched this document.  
  
## DocumentTransform

A transformation of a document. Fields  
---  
`document` |  `string` The name of the document to transform.  
`fieldTransforms[]` |  `object ([FieldTransform](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#FieldTransform))` The list of transformations to apply to the fields of the document, in order. This must not be empty.  
  
## DocumentsTarget

A target specified by a set of documents names. Fields  
---  
`documents[]` |  `string` The names of the documents to retrieve. In the format: `projects/{project_id}/databases/{database_id}/documents/{document_path}`. The request will fail if any of the document is not a child resource of the given `database`. Duplicate names will be elided.  
  
## ExistenceFilter

A digest of all the documents that match a given target. Fields  
---  
`count` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The total count of documents that match target_id. If different from the count of documents in the client that match, the client must manually determine which documents no longer match the target.  
`targetId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The target ID to which this filter applies.  
  
## FieldFilter

A filter on a specific field. Fields  
---  
`field` |  `object ([FieldReference](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#FieldReference))` The field to filter by.  
`op` |  `enum` The operator to filter by.  
Enum type. Can be one of the following:  
`OPERATOR_UNSPECIFIED` | Unspecified. This value must not be used.  
`LESS_THAN` | The given `field` is less than the given `value`. Requires: * That `field` come first in `order_by`.  
`LESS_THAN_OR_EQUAL` | The given `field` is less than or equal to the given `value`. Requires: * That `field` come first in `order_by`.  
`GREATER_THAN` | The given `field` is greater than the given `value`. Requires: * That `field` come first in `order_by`.  
`GREATER_THAN_OR_EQUAL` | The given `field` is greater than or equal to the given `value`. Requires: * That `field` come first in `order_by`.  
`EQUAL` | The given `field` is equal to the given `value`.  
`NOT_EQUAL` | The given `field` is not equal to the given `value`. Requires: * No other `NOT_EQUAL`, `NOT_IN`, `IS_NOT_NULL`, or `IS_NOT_NAN`. * That `field` comes first in the `order_by`.  
`ARRAY_CONTAINS` | The given `field` is an array that contains the given `value`.  
`IN` | The given `field` is equal to at least one value in the given array. Requires: * That `value` is a non-empty `ArrayValue` with at most 10 values. * No other `IN` or `ARRAY_CONTAINS_ANY` or `NOT_IN`.  
`ARRAY_CONTAINS_ANY` | The given `field` is an array that contains any of the values in the given array. Requires: * That `value` is a non-empty `ArrayValue` with at most 10 values. * No other `IN` or `ARRAY_CONTAINS_ANY` or `NOT_IN`.  
`NOT_IN` | The value of the `field` is not in the given array. Requires: * That `value` is a non-empty `ArrayValue` with at most 10 values. * No other `IN`, `ARRAY_CONTAINS_ANY`, `NOT_IN`, `NOT_EQUAL`, `IS_NOT_NULL`, or `IS_NOT_NAN`. * That `field` comes first in the `order_by`.  
`value` |  `object ([Value](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Value))` The value to compare to.  
  
## FieldReference

A reference to a field, such as `max(messages.time) as max_time`. Fields  
---  
`fieldPath` |  `string` (No description provided)  
  
## FieldTransform

A transformation of a field of the document. Fields  
---  
`appendMissingElements` |  `object ([ArrayValue](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#ArrayValue))` Append the given elements in order if they are not already present in the current field value. If the field is not an array, or if the field does not yet exist, it is first set to the empty array. Equivalent numbers of different types (e.g. 3L and 3.0) are considered equal when checking if a value is missing. NaN is equal to NaN, and Null is equal to Null. If the input contains multiple equivalent values, only the first will be considered. The corresponding transform_result will be the null value.  
`fieldPath` |  `string` The path of the field. See Document.fields for the field path syntax reference.  
`increment` |  `object ([Value](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Value))` Adds the given value to the field's current value. This must be an integer or a double value. If the field is not an integer or double, or if the field does not yet exist, the transformation will set the field to the given value. If either of the given value or the current field value are doubles, both values will be interpreted as doubles. Double arithmetic and representation of double values follow IEEE 754 semantics. If there is positive/negative integer overflow, the field is resolved to the largest magnitude positive/negative integer.  
`maximum` |  `object ([Value](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Value))` Sets the field to the maximum of its current value and the given value. This must be an integer or a double value. If the field is not an integer or double, or if the field does not yet exist, the transformation will set the field to the given value. If a maximum operation is applied where the field and the input value are of mixed types (that is - one is an integer and one is a double) the field takes on the type of the larger operand. If the operands are equivalent (e.g. 3 and 3.0), the field does not change. 0, 0.0, and -0.0 are all zero. The maximum of a zero stored value and zero input value is always the stored value. The maximum of any numeric value x and NaN is NaN.  
`minimum` |  `object ([Value](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Value))` Sets the field to the minimum of its current value and the given value. This must be an integer or a double value. If the field is not an integer or double, or if the field does not yet exist, the transformation will set the field to the input value. If a minimum operation is applied where the field and the input value are of mixed types (that is - one is an integer and one is a double) the field takes on the type of the smaller operand. If the operands are equivalent (e.g. 3 and 3.0), the field does not change. 0, 0.0, and -0.0 are all zero. The minimum of a zero stored value and zero input value is always the stored value. The minimum of any numeric value x and NaN is NaN.  
`removeAllFromArray` |  `object ([ArrayValue](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#ArrayValue))` Remove all of the given elements from the array in the field. If the field is not an array, or if the field does not yet exist, it is set to the empty array. Equivalent numbers of the different types (e.g. 3L and 3.0) are considered equal when deciding whether an element should be removed. NaN is equal to NaN, and Null is equal to Null. This will remove all equivalent values if there are duplicates. The corresponding transform_result will be the null value.  
`setToServerValue` |  `enum` Sets the field to the given server value.  
Enum type. Can be one of the following:  
`SERVER_VALUE_UNSPECIFIED` | Unspecified. This value must not be used.  
`REQUEST_TIME` | The time at which the server processed the request, with millisecond precision. If used on multiple fields (same or different documents) in a transaction, all the fields will get the same server timestamp.  
  
## Filter

A filter. Fields  
---  
`compositeFilter` |  `object ([CompositeFilter](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#CompositeFilter))` A composite filter.  
`fieldFilter` |  `object ([FieldFilter](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#FieldFilter))` A filter on a document field.  
`unaryFilter` |  `object ([UnaryFilter](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#UnaryFilter))` A filter that takes exactly one argument.  
  
## GoogleFirestoreAdminV1ExportDocumentsMetadata

Metadata for google.longrunning.Operation results from FirestoreAdmin.ExportDocuments. Fields  
---  
`collectionIds[]` |  `string` Which collection ids are being exported.  
`endTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` The time this operation completed. Will be unset if operation still in progress.  
`operationState` |  `enum` The state of the export operation.  
Enum type. Can be one of the following:  
`OPERATION_STATE_UNSPECIFIED` | Unspecified.  
`INITIALIZING` | Request is being prepared for processing.  
`PROCESSING` | Request is actively being processed.  
`CANCELLING` | Request is in the process of being cancelled after user called google.longrunning.Operations.CancelOperation on the operation.  
`FINALIZING` | Request has been processed and is in its finalization stage.  
`SUCCESSFUL` | Request has completed successfully.  
`FAILED` | Request has finished being processed, but encountered an error.  
`CANCELLED` | Request has finished being cancelled after user called google.longrunning.Operations.CancelOperation.  
`outputUriPrefix` |  `string` Where the entities are being exported to.  
`progressBytes` |  `object ([GoogleFirestoreAdminV1Progress](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#GoogleFirestoreAdminV1Progress))` The progress, in bytes, of this operation.  
`progressDocuments` |  `object ([GoogleFirestoreAdminV1Progress](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#GoogleFirestoreAdminV1Progress))` The progress, in documents, of this operation.  
`startTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` The time this operation started.  
  
## GoogleFirestoreAdminV1ExportDocumentsRequest

The request for FirestoreAdmin.ExportDocuments. Fields  
---  
`collectionIds[]` |  `string` Which collection ids to export. Unspecified means all collections.  
`outputUriPrefix` |  `string` The output URI. Currently only supports Google Cloud Storage URIs of the form: `gs://BUCKET_NAME[/NAMESPACE_PATH]`, where `BUCKET_NAME` is the name of the Google Cloud Storage bucket and `NAMESPACE_PATH` is an optional Google Cloud Storage namespace path. When choosing a name, be sure to consider Google Cloud Storage naming guidelines: https://cloud.google.com/storage/docs/naming. If the URI is a bucket (without a namespace path), a prefix will be generated based on the start time.  
  
## GoogleFirestoreAdminV1ExportDocumentsResponse

Returned in the google.longrunning.Operation response field. Fields  
---  
`outputUriPrefix` |  `string` Location of the output files. This can be used to begin an import into Cloud Firestore (this project or another project) after the operation completes successfully.  
  
## GoogleFirestoreAdminV1Field

Represents a single field in the database. Fields are grouped by their "Collection Group", which represent all collections in the database with the same id. Fields  
---  
`indexConfig` |  `object ([GoogleFirestoreAdminV1IndexConfig](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#GoogleFirestoreAdminV1IndexConfig))` The index configuration for this field. If unset, field indexing will revert to the configuration defined by the `ancestor_field`. To explicitly remove all indexes for this field, specify an index config with an empty list of indexes.  
`name` |  `string` Required. A field name of the form `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/fields/{field_path}` A field path may be a simple field name, e.g. `address` or a path to fields within map_value , e.g. `address.city`, or a special field path. The only valid special field is `*`, which represents any field. Field paths may be quoted using `(backtick). The only character that needs to be escaped within a quoted field path is the backtick character itself, escaped using a backslash. Special characters in field paths that must be quoted include:`_`,`.`, ``` (backtick),`[`,`]`, as well as any ascii symbolic characters. Examples: (Note: Comments here are written in markdown syntax, so there is an additional layer of backticks to represent a code block)``address.city``represents a field named`address.city`, not the map key`city`in the field`address`.``_``represents a field named` _`, not any field. A special`Field`contains the default indexing settings for all fields. This field's resource name is:`projects/{project_id}/databases/{database_id}/collectionGroups/**default** /fields/_`Indexes defined on this`Field`will be applied to all fields which do not have their own`Field` index configuration.  
  
## GoogleFirestoreAdminV1FieldOperationMetadata

Metadata for google.longrunning.Operation results from FirestoreAdmin.UpdateField. Fields  
---  
`endTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` The time this operation completed. Will be unset if operation still in progress.  
`field` |  `string` The field resource that this operation is acting on. For example: `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/fields/{field_path}`  
`indexConfigDeltas[]` |  `object ([GoogleFirestoreAdminV1IndexConfigDelta](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#GoogleFirestoreAdminV1IndexConfigDelta))` A list of IndexConfigDelta, which describe the intent of this operation.  
`progressBytes` |  `object ([GoogleFirestoreAdminV1Progress](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#GoogleFirestoreAdminV1Progress))` The progress, in bytes, of this operation.  
`progressDocuments` |  `object ([GoogleFirestoreAdminV1Progress](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#GoogleFirestoreAdminV1Progress))` The progress, in documents, of this operation.  
`startTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` The time this operation started.  
`state` |  `enum` The state of the operation.  
Enum type. Can be one of the following:  
`OPERATION_STATE_UNSPECIFIED` | Unspecified.  
`INITIALIZING` | Request is being prepared for processing.  
`PROCESSING` | Request is actively being processed.  
`CANCELLING` | Request is in the process of being cancelled after user called google.longrunning.Operations.CancelOperation on the operation.  
`FINALIZING` | Request has been processed and is in its finalization stage.  
`SUCCESSFUL` | Request has completed successfully.  
`FAILED` | Request has finished being processed, but encountered an error.  
`CANCELLED` | Request has finished being cancelled after user called google.longrunning.Operations.CancelOperation.  
  
## GoogleFirestoreAdminV1ImportDocumentsMetadata

Metadata for google.longrunning.Operation results from FirestoreAdmin.ImportDocuments. Fields  
---  
`collectionIds[]` |  `string` Which collection ids are being imported.  
`endTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` The time this operation completed. Will be unset if operation still in progress.  
`inputUriPrefix` |  `string` The location of the documents being imported.  
`operationState` |  `enum` The state of the import operation.  
Enum type. Can be one of the following:  
`OPERATION_STATE_UNSPECIFIED` | Unspecified.  
`INITIALIZING` | Request is being prepared for processing.  
`PROCESSING` | Request is actively being processed.  
`CANCELLING` | Request is in the process of being cancelled after user called google.longrunning.Operations.CancelOperation on the operation.  
`FINALIZING` | Request has been processed and is in its finalization stage.  
`SUCCESSFUL` | Request has completed successfully.  
`FAILED` | Request has finished being processed, but encountered an error.  
`CANCELLED` | Request has finished being cancelled after user called google.longrunning.Operations.CancelOperation.  
`progressBytes` |  `object ([GoogleFirestoreAdminV1Progress](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#GoogleFirestoreAdminV1Progress))` The progress, in bytes, of this operation.  
`progressDocuments` |  `object ([GoogleFirestoreAdminV1Progress](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#GoogleFirestoreAdminV1Progress))` The progress, in documents, of this operation.  
`startTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` The time this operation started.  
  
## GoogleFirestoreAdminV1ImportDocumentsRequest

The request for FirestoreAdmin.ImportDocuments. Fields  
---  
`collectionIds[]` |  `string` Which collection ids to import. Unspecified means all collections included in the import.  
`inputUriPrefix` |  `string` Location of the exported files. This must match the output_uri_prefix of an ExportDocumentsResponse from an export that has completed successfully. See: google.firestore.admin.v1.ExportDocumentsResponse.output_uri_prefix.  
  
## GoogleFirestoreAdminV1Index

Cloud Firestore indexes enable simple and complex queries against documents in a database. Fields  
---  
`fields[]` |  `object ([GoogleFirestoreAdminV1IndexField](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#GoogleFirestoreAdminV1IndexField))` The fields supported by this index. For composite indexes, this is always 2 or more fields. The last field entry is always for the field path `__name__`. If, on creation, `__name__` was not specified as the last field, it will be added automatically with the same direction as that of the last field defined. If the final field in a composite index is not directional, the `__name__` will be ordered ASCENDING (unless explicitly specified). For single field indexes, this will always be exactly one entry with a field path equal to the field path of the associated field.  
`name` |  `string` Output only. A server defined name for this index. The form of this name for composite indexes will be: `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{composite_index_id}` For single field indexes, this field will be empty.  
`queryScope` |  `enum` Indexes with a collection query scope specified allow queries against a collection that is the child of a specific document, specified at query time, and that has the same collection id. Indexes with a collection group query scope specified allow queries against all collections descended from a specific document, specified at query time, and that have the same collection id as this index.  
Enum type. Can be one of the following:  
`QUERY_SCOPE_UNSPECIFIED` | The query scope is unspecified. Not a valid option.  
`COLLECTION` | Indexes with a collection query scope specified allow queries against a collection that is the child of a specific document, specified at query time, and that has the collection id specified by the index.  
`COLLECTION_GROUP` | Indexes with a collection group query scope specified allow queries against all collections that has the collection id specified by the index.  
`state` |  `enum` Output only. The serving state of the index.  
Enum type. Can be one of the following:  
`STATE_UNSPECIFIED` | The state is unspecified.  
`CREATING` | The index is being created. There is an active long-running operation for the index. The index is updated when writing a document. Some index data may exist.  
`READY` | The index is ready to be used. The index is updated when writing a document. The index is fully populated from all stored documents it applies to.  
`NEEDS_REPAIR` | The index was being created, but something went wrong. There is no active long-running operation for the index, and the most recently finished long-running operation failed. The index is not updated when writing a document. Some index data may exist. Use the google.longrunning.Operations API to determine why the operation that last attempted to create this index failed, then re-create the index.  
  
## GoogleFirestoreAdminV1IndexConfig

The index configuration for this field. Fields  
---  
`ancestorField` |  `string` Output only. Specifies the resource name of the `Field` from which this field's index configuration is set (when `uses_ancestor_config` is true), or from which it _would_ be set if this field had no index configuration (when `uses_ancestor_config` is false).  
`indexes[]` |  `object ([GoogleFirestoreAdminV1Index](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#GoogleFirestoreAdminV1Index))` The indexes supported for this field.  
`reverting` |  `boolean` Output only When true, the `Field`'s index configuration is in the process of being reverted. Once complete, the index config will transition to the same state as the field specified by `ancestor_field`, at which point `uses_ancestor_config` will be `true` and `reverting` will be `false`.  
`usesAncestorConfig` |  `boolean` Output only. When true, the `Field`'s index configuration is set from the configuration specified by the `ancestor_field`. When false, the `Field`'s index configuration is defined explicitly.  
  
## GoogleFirestoreAdminV1IndexConfigDelta

Information about an index configuration change. Fields  
---  
`changeType` |  `enum` Specifies how the index is changing.  
Enum type. Can be one of the following:  
`CHANGE_TYPE_UNSPECIFIED` | The type of change is not specified or known.  
`ADD` | The single field index is being added.  
`REMOVE` | The single field index is being removed.  
`index` |  `object ([GoogleFirestoreAdminV1Index](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#GoogleFirestoreAdminV1Index))` The index being changed.  
  
## GoogleFirestoreAdminV1IndexField

A field in an index. The field_path describes which field is indexed, the value_mode describes how the field value is indexed. Fields  
---  
`arrayConfig` |  `enum` Indicates that this field supports operations on `array_value`s.  
Enum type. Can be one of the following:  
`ARRAY_CONFIG_UNSPECIFIED` | The index does not support additional array queries.  
`CONTAINS` | The index supports array containment queries.  
`fieldPath` |  `string` Can be **name**. For single field indexes, this must match the name of the field or may be omitted.  
`order` |  `enum` Indicates that this field supports ordering by the specified order or comparing using =, !=, <, <=, >, >=.  
Enum type. Can be one of the following:  
`ORDER_UNSPECIFIED` | The ordering is unspecified. Not a valid option.  
`ASCENDING` | The field is ordered by ascending field value.  
`DESCENDING` | The field is ordered by descending field value.  
  
## GoogleFirestoreAdminV1IndexOperationMetadata

Metadata for google.longrunning.Operation results from FirestoreAdmin.CreateIndex. Fields  
---  
`endTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` The time this operation completed. Will be unset if operation still in progress.  
`index` |  `string` The index resource that this operation is acting on. For example: `projects/{project_id}/databases/{database_id}/collectionGroups/{collection_id}/indexes/{index_id}`  
`progressBytes` |  `object ([GoogleFirestoreAdminV1Progress](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#GoogleFirestoreAdminV1Progress))` The progress, in bytes, of this operation.  
`progressDocuments` |  `object ([GoogleFirestoreAdminV1Progress](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#GoogleFirestoreAdminV1Progress))` The progress, in documents, of this operation.  
`startTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` The time this operation started.  
`state` |  `enum` The state of the operation.  
Enum type. Can be one of the following:  
`OPERATION_STATE_UNSPECIFIED` | Unspecified.  
`INITIALIZING` | Request is being prepared for processing.  
`PROCESSING` | Request is actively being processed.  
`CANCELLING` | Request is in the process of being cancelled after user called google.longrunning.Operations.CancelOperation on the operation.  
`FINALIZING` | Request has been processed and is in its finalization stage.  
`SUCCESSFUL` | Request has completed successfully.  
`FAILED` | Request has finished being processed, but encountered an error.  
`CANCELLED` | Request has finished being cancelled after user called google.longrunning.Operations.CancelOperation.  
  
## GoogleFirestoreAdminV1ListFieldsResponse

The response for FirestoreAdmin.ListFields. Fields  
---  
`fields[]` |  `object ([GoogleFirestoreAdminV1Field](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#GoogleFirestoreAdminV1Field))` The requested fields.  
`nextPageToken` |  `string` A page token that may be used to request another page of results. If blank, this is the last page.  
  
## GoogleFirestoreAdminV1ListIndexesResponse

The response for FirestoreAdmin.ListIndexes. Fields  
---  
`indexes[]` |  `object ([GoogleFirestoreAdminV1Index](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#GoogleFirestoreAdminV1Index))` The requested indexes.  
`nextPageToken` |  `string` A page token that may be used to request another page of results. If blank, this is the last page.  
  
## GoogleFirestoreAdminV1Progress

Describes the progress of the operation. Unit of work is generic and must be interpreted based on where Progress is used. Fields  
---  
`completedWork` |  `string ([int64](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The amount of work completed.  
`estimatedWork` |  `string ([int64](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The amount of work estimated.  
  
## GoogleLongrunningListOperationsResponse

The response message for Operations.ListOperations. Fields  
---  
`nextPageToken` |  `string` The standard List next-page token.  
`operations[]` |  `object ([GoogleLongrunningOperation](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#GoogleLongrunningOperation))` A list of operations that matches the specified filter in the request.  
  
## GoogleLongrunningOperation

This resource represents a long-running operation that is the result of a network API call. Fields  
---  
`done` |  `boolean` If the value is `false`, it means the operation is still in progress. If `true`, the operation is completed, and either `error` or `response` is available.  
`error` |  `object ([Status](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Status))` The error result of the operation in case of failure or cancellation.  
`metadata` |  `map (key: string, value: any)` Service-specific metadata associated with the operation. It typically contains progress information and common metadata such as create time. Some services might not provide such metadata. Any method that returns a long-running operation should document the metadata type, if any.  
`name` |  `string` The server-assigned name, which is only unique within the same service that originally returns it. If you use the default HTTP mapping, the `name` should be a resource name ending with `operations/{unique_id}`.  
`response` |  `map (key: string, value: any)` The normal response of the operation in case of success. If the original method returns no data on success, such as `Delete`, the response is `google.protobuf.Empty`. If the original method is standard `Get`/`Create`/`Update`, the response should be the resource. For other methods, the response should have the type `XxxResponse`, where `Xxx` is the original method name. For example, if the original method name is `TakeSnapshot()`, the inferred response type is `TakeSnapshotResponse`.  
  
## LatLng

An object that represents a latitude/longitude pair. This is expressed as a pair of doubles to represent degrees latitude and degrees longitude. Unless specified otherwise, this object must conform to the WGS84 standard. Values must be within normalized ranges. Fields  
---  
`latitude` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The latitude in degrees. It must be in the range [-90.0, +90.0].  
`longitude` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The longitude in degrees. It must be in the range [-180.0, +180.0].  
  
## ListCollectionIdsRequest

The request for Firestore.ListCollectionIds. Fields  
---  
`pageSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The maximum number of results to return.  
`pageToken` |  `string` A page token. Must be a value from ListCollectionIdsResponse.  
  
## ListCollectionIdsResponse

The response from Firestore.ListCollectionIds. Fields  
---  
`collectionIds[]` |  `string` The collection ids.  
`nextPageToken` |  `string` A page token that may be used to continue the list.  
  
## ListDocumentsResponse

The response for Firestore.ListDocuments. Fields  
---  
`documents[]` |  `object ([Document](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Document))` The Documents found.  
`nextPageToken` |  `string` The next page token.  
  
## ListLocationsResponse

The response message for Locations.ListLocations. Fields  
---  
`locations[]` |  `object ([Location](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Location))` A list of locations that matches the specified filter in the request.  
`nextPageToken` |  `string` The standard List next-page token.  
  
## ListenRequest

A request for Firestore.Listen Fields  
---  
`addTarget` |  `object ([Target](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Target))` A target to add to this stream.  
`labels` |  `map (key: string, value: string)` Labels associated with this target change.  
`removeTarget` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The ID of a target to remove from this stream.  
  
## ListenResponse

The response for Firestore.Listen. Fields  
---  
`documentChange` |  `object ([DocumentChange](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#DocumentChange))` A Document has changed.  
`documentDelete` |  `object ([DocumentDelete](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#DocumentDelete))` A Document has been deleted.  
`documentRemove` |  `object ([DocumentRemove](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#DocumentRemove))` A Document has been removed from a target (because it is no longer relevant to that target).  
`filter` |  `object ([ExistenceFilter](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#ExistenceFilter))` A filter to apply to the set of documents previously returned for the given target. Returned when documents may have been removed from the given target, but the exact documents are unknown.  
`targetChange` |  `object ([TargetChange](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#TargetChange))` Targets have changed.  
  
## Location

A resource that represents Google Cloud Platform location. Fields  
---  
`displayName` |  `string` The friendly name for this location, typically a nearby city name. For example, "Tokyo".  
`labels` |  `map (key: string, value: string)` Cross-service attributes for the location. For example {"cloud.googleapis.com/region": "us-east1"}  
`locationId` |  `string` The canonical id for this location. For example: `"us-east1"`.  
`metadata` |  `map (key: string, value: any)` Service-specific metadata. For example the available capacity at the given location.  
`name` |  `string` Resource name for the location, which may vary between implementations. For example: `"projects/example-project/locations/us-east1"`  
  
## MapValue

A map value. Fields  
---  
`fields` |  `map (key: string, value: object ([Value](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Value)))` The map's fields. The map keys represent field names. Field names matching the regular expression `__.*__` are reserved. Reserved field names are forbidden except in certain documented contexts. The map keys, represented as UTF-8, must not exceed 1,500 bytes and cannot be empty.  
  
## Order

An order on a field. Fields  
---  
`direction` |  `enum` The direction to order by. Defaults to `ASCENDING`.  
Enum type. Can be one of the following:  
`DIRECTION_UNSPECIFIED` | Unspecified.  
`ASCENDING` | Ascending.  
`DESCENDING` | Descending.  
`field` |  `object ([FieldReference](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#FieldReference))` The field to order by.  
  
## PartitionQueryRequest

The request for Firestore.PartitionQuery. Fields  
---  
`pageSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The maximum number of partitions to return in this call, subject to `partition_count`. For example, if `partition_count` = 10 and `page_size` = 8, the first call to PartitionQuery will return up to 8 partitions and a `next_page_token` if more results exist. A second call to PartitionQuery will return up to 2 partitions, to complete the total of 10 specified in `partition_count`.  
`pageToken` |  `string` The `next_page_token` value returned from a previous call to PartitionQuery that may be used to get an additional set of results. There are no ordering guarantees between sets of results. Thus, using multiple sets of results will require merging the different result sets. For example, two subsequent calls using a page_token may return: * cursor B, cursor M, cursor Q * cursor A, cursor U, cursor W To obtain a complete result set ordered with respect to the results of the query supplied to PartitionQuery, the results sets should be merged: cursor A, cursor B, cursor M, cursor Q, cursor U, cursor W  
`partitionCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The desired maximum number of partition points. The partitions may be returned across multiple pages of results. The number must be positive. The actual number of partitions returned may be fewer. For example, this may be set to one fewer than the number of parallel queries to be run, or in running a data pipeline job, one fewer than the number of workers or compute instances available.  
`structuredQuery` |  `object ([StructuredQuery](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#StructuredQuery))` A structured query. Query must specify collection with all descendants and be ordered by name ascending. Other filters, order bys, limits, offsets, and start/end cursors are not supported.  
  
## PartitionQueryResponse

The response for Firestore.PartitionQuery. Fields  
---  
`nextPageToken` |  `string` A page token that may be used to request an additional set of results, up to the number specified by `partition_count` in the PartitionQuery request. If blank, there are no more results.  
`partitions[]` |  `object ([Cursor](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Cursor))` Partition results. Each partition is a split point that can be used by RunQuery as a starting or end point for the query results. The RunQuery requests must be made with the same query supplied to this PartitionQuery request. The partition cursors will be ordered according to same ordering as the results of the query supplied to PartitionQuery. For example, if a PartitionQuery request returns partition cursors A and B, running the following three queries will return the entire result set of the original query: * query, end_at A * query, start_at A, end_at B * query, start_at B An empty result may indicate that the query has too few results to be partitioned.  
  
## Precondition

A precondition on a document, used for conditional operations. Fields  
---  
`exists` |  `boolean` When set to `true`, the target document must exist. When set to `false`, the target document must not exist.  
`updateTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` When set, the target document must exist and have been last updated at that time.  
  
## Projection

The projection of document's fields to return. Fields  
---  
`fields[]` |  `object ([FieldReference](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#FieldReference))` The fields to return. If empty, all fields are returned. To only return the name of the document, use `['__name__']`.  
  
## QueryTarget

A target specified by a query. Fields  
---  
`parent` |  `string` The parent resource name. In the format: `projects/{project_id}/databases/{database_id}/documents` or `projects/{project_id}/databases/{database_id}/documents/{document_path}`. For example: `projects/my-project/databases/my-database/documents` or `projects/my-project/databases/my-database/documents/chatrooms/my-chatroom`  
`structuredQuery` |  `object ([StructuredQuery](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#StructuredQuery))` A structured query.  
  
## ReadOnly

Options for a transaction that can only be used to read documents. Fields  
---  
`readTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` Reads documents at the given time. This may not be older than 60 seconds.  
  
## ReadWrite

Options for a transaction that can be used to read and write documents. Fields  
---  
`retryTransaction` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` An optional transaction to retry.  
  
## RollbackRequest

The request for Firestore.Rollback. Fields  
---  
`transaction` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Required. The transaction to roll back.  
  
## RunQueryRequest

The request for Firestore.RunQuery. Fields  
---  
`newTransaction` |  `object ([TransactionOptions](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#TransactionOptions))` Starts a new transaction and reads the documents. Defaults to a read-only transaction. The new transaction ID will be returned as the first response in the stream.  
`readTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` Reads documents as they were at the given time. This may not be older than 270 seconds.  
`structuredQuery` |  `object ([StructuredQuery](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#StructuredQuery))` A structured query.  
`transaction` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` Reads documents in a transaction.  
  
## RunQueryResponse

The response for Firestore.RunQuery. Fields  
---  
`document` |  `object ([Document](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Document))` A query result. Not set when reporting partial progress.  
`readTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` The time at which the document was read. This may be monotonically increasing; in this case, the previous documents in the result stream are guaranteed not to have changed between their `read_time` and this one. If the query returns no results, a response with `read_time` and no `document` will be sent, and this represents the time at which the query was run.  
`skippedResults` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of results that have been skipped due to an offset between the last response and the current response.  
`transaction` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The transaction that was started as part of this request. Can only be set in the first response, and only if RunQueryRequest.new_transaction was set in the request. If set, no other fields will be set in this response.  
  
## Status

The `Status` type defines a logical error model that is suitable for different programming environments, including REST APIs and RPC APIs. It is used by [gRPC](https://github.com/grpc). Each `Status` message contains three pieces of data: error code, error message, and error details. You can find out more about this error model and how to work with it in the [API Design Guide](https://cloud.google.com/apis/design/errors). Fields  
---  
`code` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The status code, which should be an enum value of google.rpc.Code.  
`details[]` |  `object` A list of messages that carry the error details. There is a common set of message types for APIs to use.  
`message` |  `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the google.rpc.Status.details field, or localized by the client.  
  
## StructuredQuery

A Firestore query. Fields  
---  
`endAt` |  `object ([Cursor](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Cursor))` A end point for the query results.  
`from[]` |  `object ([CollectionSelector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#CollectionSelector))` The collections to query.  
`limit` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The maximum number of results to return. Applies after all other constraints. Must be >= 0 if specified.  
`offset` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The number of results to skip. Applies before limit, but after all other constraints. Must be >= 0 if specified.  
`orderBy[]` |  `object ([Order](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Order))` The order to apply to the query results. Firestore guarantees a stable ordering through the following rules: * Any field required to appear in `order_by`, that is not already specified in `order_by`, is appended to the order in field name order by default. * If an order on `__name__` is not specified, it is appended by default. Fields are appended with the same sort direction as the last order specified, or 'ASCENDING' if no order was specified. For example: * `SELECT * FROM Foo ORDER BY A` becomes `SELECT * FROM Foo ORDER BY A, __name__` * `SELECT * FROM Foo ORDER BY A DESC` becomes `SELECT * FROM Foo ORDER BY A DESC, __name__ DESC` * `SELECT * FROM Foo WHERE A > 1` becomes `SELECT * FROM Foo WHERE A > 1 ORDER BY A, __name__`  
`select` |  `object ([Projection](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Projection))` The projection to return.  
`startAt` |  `object ([Cursor](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Cursor))` A starting point for the query results.  
`where` |  `object ([Filter](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Filter))` The filter to apply.  
  
## Target

A specification of a set of documents to listen to. Fields  
---  
`documents` |  `object ([DocumentsTarget](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#DocumentsTarget))` A target specified by a set of document names.  
`once` |  `boolean` If the target should be removed once it is current and consistent.  
`query` |  `object ([QueryTarget](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#QueryTarget))` A target specified by a query.  
`readTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` Start listening after a specific `read_time`. The client must know the state of matching documents at this time.  
`resumeToken` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` A resume token from a prior TargetChange for an identical target. Using a resume token with a different target is unsupported and may fail.  
`targetId` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The target ID that identifies the target on the stream. Must be a positive number and non-zero.  
  
## TargetChange

Targets being watched have changed. Fields  
---  
`cause` |  `object ([Status](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Status))` The error that resulted in this change, if applicable.  
`readTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` The consistent `read_time` for the given `target_ids` (omitted when the target_ids are not at a consistent snapshot). The stream is guaranteed to send a `read_time` with `target_ids` empty whenever the entire stream reaches a new consistent snapshot. ADD, CURRENT, and RESET messages are guaranteed to (eventually) result in a new consistent snapshot (while NO_CHANGE and REMOVE messages are not). For a given stream, `read_time` is guaranteed to be monotonically increasing.  
`resumeToken` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` A token that can be used to resume the stream for the given `target_ids`, or all targets if `target_ids` is empty. Not set on every target change.  
`targetChangeType` |  `enum` The type of change that occurred.  
Enum type. Can be one of the following:  
`NO_CHANGE` | No change has occurred. Used only to send an updated `resume_token`.  
`ADD` | The targets have been added.  
`REMOVE` | The targets have been removed.  
`CURRENT` | The targets reflect all changes committed before the targets were added to the stream. This will be sent after or with a `read_time` that is greater than or equal to the time at which the targets were added. Listeners can wait for this change if read-after-write semantics are desired.  
`RESET` | The targets have been reset, and a new initial state for the targets will be returned in subsequent changes. After the initial state is complete, `CURRENT` will be returned even if the target was previously indicated to be `CURRENT`.  
`targetIds[]` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The target IDs of targets that have changed. If empty, the change applies to all targets. The order of the target IDs is not defined.  
  
## TransactionOptions

Options for creating a new transaction. Fields  
---  
`readOnly` |  `object ([ReadOnly](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#ReadOnly))` The transaction can only be used for read operations.  
`readWrite` |  `object ([ReadWrite](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#ReadWrite))` The transaction can be used for both read and write operations.  
  
## UnaryFilter

A filter with a single operand. Fields  
---  
`field` |  `object ([FieldReference](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#FieldReference))` The field to which to apply the operator.  
`op` |  `enum` The unary operator to apply.  
Enum type. Can be one of the following:  
`OPERATOR_UNSPECIFIED` | Unspecified. This value must not be used.  
`IS_NAN` | The given `field` is equal to `NaN`.  
`IS_NULL` | The given `field` is equal to `NULL`.  
`IS_NOT_NAN` | The given `field` is not equal to `NaN`. Requires: * No other `NOT_EQUAL`, `NOT_IN`, `IS_NOT_NULL`, or `IS_NOT_NAN`. * That `field` comes first in the `order_by`.  
`IS_NOT_NULL` | The given `field` is not equal to `NULL`. Requires: * A single `NOT_EQUAL`, `NOT_IN`, `IS_NOT_NULL`, or `IS_NOT_NAN`. * That `field` comes first in the `order_by`.  
  
## Value

A message that can hold any of the supported value types. Fields  
---  
`arrayValue` |  `object ([ArrayValue](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#ArrayValue))` An array value. Cannot directly contain another array value, though can contain an map which contains another array.  
`booleanValue` |  `boolean` A boolean value.  
`bytesValue` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` A bytes value. Must not exceed 1 MiB - 89 bytes. Only the first 1,500 bytes are considered by queries.  
`doubleValue` |  `number ([double](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` A double value.  
`geoPointValue` |  `object ([LatLng](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#LatLng))` A geo point value representing a point on the surface of Earth.  
`integerValue` |  `string ([int64](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` An integer value.  
`mapValue` |  `object ([MapValue](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#MapValue))` A map value.  
`nullValue` |  `enum` A null value.  
Enum type. Can be one of the following:  
`NULL_VALUE` | Null value.  
`referenceValue` |  `string` A reference to a document. For example: `projects/{project_id}/databases/{database_id}/documents/{document_path}`.  
`stringValue` |  `string` A string value. The string, represented as UTF-8, must not exceed 1 MiB - 89 bytes. Only the first 1,500 bytes of the UTF-8 representation are considered by queries.  
`timestampValue` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` A timestamp value. Precise only to microseconds. When stored, any additional precision is rounded down.  
  
## Write

A write on a document. Fields  
---  
`currentDocument` |  `object ([Precondition](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Precondition))` An optional precondition on the document. The write will fail if this is set and not met by the target document.  
`delete` |  `string` A document name to delete. In the format: `projects/{project_id}/databases/{database_id}/documents/{document_path}`.  
`transform` |  `object ([DocumentTransform](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#DocumentTransform))` Applies a transformation to a document.  
`update` |  `object ([Document](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Document))` A document to write.  
`updateMask` |  `object ([DocumentMask](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#DocumentMask))` The fields to update in this write. This field can be set only when the operation is `update`. If the mask is not set for an `update` and the document exists, any existing data will be overwritten. If the mask is set and the document on the server has fields not covered by the mask, they are left unchanged. Fields referenced in the mask, but not present in the input document, are deleted from the document on the server. The field paths in this mask must not contain a reserved field name.  
`updateTransforms[]` |  `object ([FieldTransform](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#FieldTransform))` The transforms to perform after update. This field can be set only when the operation is `update`. If present, this write is equivalent to performing `update` and `transform` to the same document atomically and in order.  
  
## WriteRequest

The request for Firestore.Write. The first request creates a stream, or resumes an existing one from a token. When creating a new stream, the server replies with a response containing only an ID and a token, to use in the next request. When resuming a stream, the server first streams any responses later than the given token, then a response containing only an up-to-date token, to use in the next request. Fields  
---  
`labels` |  `map (key: string, value: string)` Labels associated with this write request.  
`streamId` |  `string` The ID of the write stream to resume. This may only be set in the first message. When left empty, a new write stream will be created.  
`streamToken` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` A stream token that was previously sent by the server. The client should set this field to the token from the most recent WriteResponse it has received. This acknowledges that the client has received responses up to this token. After sending this token, earlier tokens may not be used anymore. The server may close the stream if there are too many unacknowledged responses. Leave this field unset when creating a new stream. To resume a stream at a specific point, set this field and the `stream_id` field. Leave this field unset when creating a new stream.  
`writes[]` |  `object ([Write](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Write))` The writes to apply. Always executed atomically and in order. This must be empty on the first request. This may be empty on the last request. This must not be empty on all other requests.  
  
## WriteResponse

The response for Firestore.Write. Fields  
---  
`commitTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` The time at which the commit occurred. Any read with an equal or greater `read_time` is guaranteed to see the effects of the write.  
`streamId` |  `string` The ID of the stream. Only set on the first message, when a new stream was created.  
`streamToken` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` A token that represents the position of this response in the stream. This can be used by a client to resume the stream at this point. This field is always set.  
`writeResults[]` |  `object ([WriteResult](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#WriteResult))` The result of applying the writes. This i-th write result corresponds to the i-th write in the request.  
  
## WriteResult

The result of applying a write. Fields  
---  
`transformResults[]` |  `object ([Value](https://docs.cloud.google.com/workflows/docs/reference/googleapis/firestore/v1/Overview#Value))` The results of applying each DocumentTransform.FieldTransform, in the same order.  
`updateTime` |  `string ([Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#timestamp) format)` The last update time of the document after applying the write. Not set after a `delete`. If the write did not actually change the document, this will be the previous update_time.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
