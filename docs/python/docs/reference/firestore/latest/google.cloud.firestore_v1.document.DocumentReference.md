---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.document.DocumentReference
title: Class DocumentReference (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:36.760735+00:00
---

# Class DocumentReference (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.document.DocumentReference

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DocumentReference (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 
    
    
    DocumentReference(*path, **kwargs)

A reference to a document in a Firestore database.

The document may already exist or can be created by this class.

## Parameters  
  
---  
**Name** | **Description**  
`path` |  `Tuple[str, ...]`   
The components in the document path. This is a series of strings representing each collection and sub-collection ID, as well as the document IDs for any documents that contain a sub-collection (as well as the base document).  
`kwargs` |  `dict`   
The keyword arguments for the constructor. The only supported keyword is `client` and it must be a [Client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client). It represents the client that created this document reference.  
  
## Methods 

### collections
    
    
    collections(
        page_size: typing.Optional[int] = None,
        retry: (
            google.api_core.retry.retry_unary.Retry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
        *,
        read_time: typing.Optional[datetime.datetime] = None
    ) -> typing.Generator[typing.Any, typing.Any, None]

List subcollections of the current document.

**Parameters**  
---  
**Name** | **Description**  
`page_size` |  `Optional[int]]`   
The maximum number of collections in each page of results from this request. Non-positive values are ignored. Defaults to a sensible value set by the API.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried. Defaults to a system-specified policy.  
`timeout` |  `float`   
The timeout for this request. Defaults to a system-specified value.  
`read_time` |  `Optional[datetime.datetime]`   
If set, reads documents as they were at the given time. This must be a timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days. If no timezone is specified in the `datetime.datetime` object, it is assumed to be UTC.  
**Returns**  
---  
**Type** | **Description**  
`Sequence[[CollectionReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.collection.CollectionReference)]` | iterator of subcollections of the current document. If the document does not exist at the time of `snapshot`, the iterator will be empty  
  
### create
    
    
    create(
        document_data: dict,
        retry: (
            google.api_core.retry.retry_unary.Retry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
    ) -> google.cloud.firestore_v1.types.write.WriteResult

Create a document in the Firestore database.

> > > document_data = {"a": 1, "b": {"c": "Two"}} document.get().to_dict() is None # does not exist True document.create(document_data) document.get().to_dict() == document_data # exists True

**Parameters**  
---  
**Name** | **Description**  
`document_data` |  `dict`   
Property names and values to use for creating a document.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried. Defaults to a system-specified policy.  
`timeout` |  `float`   
The timeout for this request. Defaults to a system-specified value.  
**Exceptions**  
---  
**Type** | **Description**  
`google.cloud.exceptions.Conflict` | If the document already exists.  
**Returns**  
---  
**Type** | **Description**  
`[WriteResult](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.WriteResult)` | The write result corresponding to the committed document. A write result contains an `update_time` field.  
  
### delete
    
    
    delete(
        option: typing.Optional[google.cloud.firestore_v1._helpers.WriteOption] = None,
        retry: (
            google.api_core.retry.retry_unary.Retry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
    ) -> google.protobuf.timestamp_pb2.Timestamp

Delete the current document in the Firestore database.

**Parameters**  
---  
**Name** | **Description**  
`option` |  `Optional[WriteOption]`   
A write option to make assertions / preconditions on the server state of the document before applying changes.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried. Defaults to a system-specified policy.  
`timeout` |  `float`   
The timeout for this request. Defaults to a system-specified value.  
**Returns**  
---  
**Type** | **Description**  
``google.protobuf.timestamp_pb2.Timestamp`` | The time that the delete request was received by the server. If the document did not exist when the delete was sent (i.e. nothing was deleted), this method will still succeed and will still return the time that the request was received by the server.  
  
### get
    
    
    get(
        field_paths: typing.Optional[typing.Iterable[str]] = None,
        transaction=None,
        retry: (
            google.api_core.retry.retry_unary.Retry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
        *,
        read_time: typing.Optional[datetime.datetime] = None
    ) -> google.cloud.firestore_v1.base_document.DocumentSnapshot

Retrieve a snapshot of the current document.

See xref_field_path for more information on **field paths**.

If a `transaction` is used and it already has write operations added, this method cannot be used (i.e. read-after-write is not allowed).

**Parameters**  
---  
**Name** | **Description**  
`field_paths` |  `Optional[Iterable[str, ...]]`   
An iterable of field paths (`.`-delimited list of field names) to use as a projection of document fields in the returned results. If no value is provided, all fields will be returned.  
`transaction` |  `Optional[[Transaction](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transaction.Transaction)]`   
An existing transaction that this reference will be retrieved in.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if an y, should be retried. Defaults to a system-specified policy.  
`timeout` |  `float`   
The timeout for this request. Defaults to a system-specified value.  
`read_time` |  `Optional[datetime.datetime]`   
If set, reads documents as they were at the given time. This must be a timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days. If no timezone is specified in the `datetime.datetime` object, it is assumed to be UTC.  
**Returns**  
---  
**Type** | **Description**  
`[DocumentSnapshot](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document.DocumentSnapshot)` | A snapshot of the current document. If the document does not exist at the time of the snapshot is taken, the snapshot's `reference`, `data`, `update_time`, and `create_time` attributes will all be `None` and its `exists` attribute will be `False`.  
  
### on_snapshot
    
    
    on_snapshot(callback: typing.Callable) -> google.cloud.firestore_v1.watch.Watch

Watch this document.

This starts a watch on this document using a background thread. The provided callback is run on the snapshot.

**Parameter**  
---  
**Name** | **Description**  
`callback` |  `Callable[[[DocumentSnapshot](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.base_document.DocumentSnapshot)], NoneType] Example: .. code-block:: python from google.cloud import firestore_v1 db = firestore_v1.Client() collection_ref = db.collection(u'users') def on_snapshot(document_snapshot, changes, read_time): doc = document_snapshot print(u'{} => {}'.format(doc.id, doc.to_dict())) doc_ref = db.collection(u'users').document( u'alovelace' + unique_resource_id()) # Watch this document doc_watch = doc_ref.on_snapshot(on_snapshot) # Terminate this watch doc_watch.unsubscribe()`   
a callback to run when a change occurs  
  
### set
    
    
    set(
        document_data: dict,
        merge: bool = False,
        retry: (
            google.api_core.retry.retry_unary.Retry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
    ) -> google.cloud.firestore_v1.types.write.WriteResult

Create / replace / merge a document in the Firestore database.

  * To "upsert" a document (create if it doesn't exist, replace completely if it does), leave the `merge` argument at its default:

> > > document_data = {"a": 1, "b": {"c": "Two"}} document.get().to_dict() is None # document exists False document.set(document_data) document.get().to_dict() == document_data # exists True

  * To "merge" `document_data` with an existing document (creating if the document does not exist), pass `merge` as True`:

> > > document_data = {"a": 1, "b": {"c": "Two"}} document.get().to_dict() == {"d": "Three", "b": {}} # exists document.set(document_data, merge=True) document.get().to_dict() == {"a": 1, "d": "Three", "b": {"c": "Two"}} True

In this case, existing documents with top-level keys which are not present in `document_data` (`"d"`) will preserve the values of those keys.

  * To merge only specific fields of `document_data` with existing documents (creating if the document does not exist), pass `merge` as a list of field paths:




> > > document_data = {"a": 1, "b": {"c": "Two"}} document.get().to_dict() == {"b": {"c": "One", "d": "Four" }} # exists True document.set(document_data, merge=["b.c"]) document.get().to_dict() == {"b": {"c": "Two", "d": "Four" }} True

For more information on field paths, see xref_field_path.

**Parameters**  
---  
**Name** | **Description**  
`document_data` |  `dict`   
Property names and values to use for replacing a document.  
`merge` |  `Optional[bool] or Optional[List`   
If True, apply merging instead of overwriting the state of the document.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried. Defaults to a system-specified policy.  
`timeout` |  `float`   
The timeout for this request. Defaults to a system-specified value.  
**Returns**  
---  
**Type** | **Description**  
`[WriteResult](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.WriteResult)` | The write result corresponding to the committed document. A write result contains an `update_time` field.  
  
### update
    
    
    update(
        field_updates: dict[str, typing.Any],
        option: typing.Optional[google.cloud.firestore_v1._helpers.WriteOption] = None,
        retry: (
            google.api_core.retry.retry_unary.Retry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
    ) -> google.cloud.firestore_v1.types.write.WriteResult

Update an existing document in the Firestore database.

By default, this method verifies that the document exists on the server before making updates. A write `option` can be specified to override these preconditions.

Each key in `field_updates` can either be a field name or a **field path** (For more information on field paths, see xref_field_path.) To illustrate this, consider a document with
    
    
    >>> snapshot = document.get()
    >>> snapshot.to_dict()
    {
        'foo': {
            'bar': 'baz',
        },
        'other': True,
    }
    

stored on the server. If the field name is used in the update:
    
    
    >>> field_updates = {
    ...     'foo': {
    ...         'quux': 800,
    ...     },
    ... }
    >>> document.update(field_updates)
    

then all of `foo` will be overwritten on the server and the new value will be
    
    
    >>> snapshot = document.get()
    >>> snapshot.to_dict()
    {
        'foo': {
            'quux': 800,
        },
        'other': True,
    }
    

On the other hand, if a `.`-delimited **field path** is used in the update:
    
    
    >>> field_updates = {
    ...     'foo.quux': 800,
    ... }
    >>> document.update(field_updates)
    

then only `foo.quux` will be updated on the server and the field `foo.bar` will remain intact:
    
    
    >>> snapshot = document.get()
    >>> snapshot.to_dict()
    {
        'foo': {
            'bar': 'baz',
            'quux': 800,
        },
        'other': True,
    }
    

**Warning:** A **field path** can only be used as a top-level key in `field_updates`. 
    
    
    >>> field_updates = {
    ...     'other': firestore.DELETE_FIELD,
    ... }
    >>> document.update(field_updates)
    

would update the value on the server to:
    
    
    >>> snapshot = document.get()
    >>> snapshot.to_dict()
    {
        'foo': {
            'bar': 'baz',
        },
    }
    

To set a field to the current time on the server when the update is received, use the xref_SERVER_TIMESTAMP sentinel. Sending
    
    
    >>> field_updates = {
    ...     'foo.now': firestore.SERVER_TIMESTAMP,
    ... }
    >>> document.update(field_updates)
    

would update the value on the server to:
    
    
    >>> snapshot = document.get()
    >>> snapshot.to_dict()
    {
        'foo': {
            'bar': 'baz',
            'now': datetime.datetime(2012, ...),
        },
        'other': True,
    }
    

**Parameters**  
---  
**Name** | **Description**  
`field_updates` |  `dict`   
Field names or paths to update and values to update with.  
`option` |  `Optional[WriteOption]`   
A write option to make assertions / preconditions on the server state of the document before applying changes.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried. Defaults to a system-specified policy.  
`timeout` |  `float`   
The timeout for this request. Defaults to a system-specified value.  
**Exceptions**  
---  
**Type** | **Description**  
`google.cloud.exceptions.NotFound` | If the document does not exist.  
**Returns**  
---  
**Type** | **Description**  
`[WriteResult](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.types.WriteResult)` | The write result corresponding to the updated document. A write result contains an `update_time` field.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
