---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_collection.AsyncCollectionReference
title: Class AsyncCollectionReference (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:31.659931+00:00
---

# Class AsyncCollectionReference (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_collection.AsyncCollectionReference

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AsyncCollectionReference (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 
    
    
    AsyncCollectionReference(*path, **kwargs)

A reference to a collection in a Firestore database.

The collection may already exist or this class can facilitate creation of documents within the collection.

## Parameters  
  
---  
**Name** | **Description**  
`path` |  `Tuple[str, ...]`   
The components in the collection path. This is a series of strings representing each collection and sub-collection ID, as well as the document IDs for any documents that contain a sub-collection.  
`kwargs` |  `dict`   
The keyword arguments for the constructor. The only supported keyword is `client` and it must be a [Client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client) if provided. It represents the client that created this collection reference.  
  
## Methods 

### add
    
    
    add(
        document_data: dict,
        document_id: typing.Optional[str] = None,
        retry: (
            google.api_core.retry.retry_unary_async.AsyncRetry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
    ) -> typing.Tuple[typing.Any, typing.Any]

Create a document in the Firestore database with the provided data.

**Parameters**  
---  
**Name** | **Description**  
`document_data` |  `dict`   
Property names and values to use for creating the document.  
`document_id` |  `Optional[str]`   
The document identifier within the current collection. If not provided, an ID will be automatically assigned by the server (the assigned ID will be a random 20 character string composed of digits, uppercase and lowercase letters).  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried. Defaults to a system-specified policy.  
`timeout` |  `float`   
The timeout for this request. Defaults to a system-specified value.  
**Exceptions**  
---  
**Type** | **Description**  
`google.cloud.exceptions.Conflict` | If `document_id` is provided and the document already exists.  
**Returns**  
---  
**Type** | **Description**  
`Tuple[`google.protobuf.timestamp_pb2.Timestamp`, [AsyncDocumentReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.async_document.AsyncDocumentReference)]` | Pair of * The `update_time` when the document was created/overwritten. * A document reference for the created document.  
  
### document
    
    
    document(document_id: str | None = None) -> AsyncDocumentReference

Create a sub-document underneath the current collection.

**Parameter**  
---  
**Name** | **Description**  
`document_id` |  `Optional[str]`   
The document identifier within the current collection. If not provided, will default to a random 20 character string composed of digits, uppercase and lowercase and letters.  
**Returns**  
---  
**Type** | **Description**  
`AsyncDocumentReference` | The child document.  
  
### get
    
    
    get(
        transaction: Optional[transaction.Transaction] = None,
        retry: retries.AsyncRetry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: Optional[float] = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> QueryResultsList[DocumentSnapshot]

Read the documents in this collection.

This sends a `RunQuery` RPC and returns a list of documents returned in the stream of `RunQueryResponse` messages.

**Parameters**  
---  
**Name** | **Description**  
`retry` |  `Optional[google.api_core.retry.Retry]`   
Designation of what errors, if any, should be retried. Defaults to a system-specified policy.  
`timeout` |  `Otional[float]`   
The timeout for this request. Defaults to a system-specified value.  
`read_time` |  `Optional[datetime.datetime] If a `transaction` is used and it already has write operations added, this method cannot be used (i.e. read-after-write is not allowed).`   
If set, reads documents as they were at the given time. This must be a timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days. If no timezone is specified in the `datetime.datetime` object, it is assumed to be UTC.  
**Returns**  
---  
**Type** | **Description**  
`QueryResultsList[DocumentSnapshot]` | The documents in this collection that match the query.  
  
### list_documents
    
    
    list_documents(
        page_size: int | None = None,
        retry: retries.AsyncRetry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: float | None = None,
        *,
        read_time: datetime.datetime | None = None
    ) -> AsyncGenerator[AsyncDocumentReference, None]

List all subdocuments of the current collection.

**Parameters**  
---  
**Name** | **Description**  
`page_size` |  `Optional[int]]`   
The maximum number of documents in each page of results from this request. Non-positive values are ignored. Defaults to a sensible value set by the API.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried. Defaults to a system-specified policy.  
`timeout` |  `float`   
The timeout for this request. Defaults to a system-specified value.  
`read_time` |  `Optional[datetime.datetime]`   
If set, reads documents as they were at the given time. This must be a timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days. If no timezone is specified in the `datetime.datetime` object, it is assumed to be UTC.  
**Returns**  
---  
**Type** | **Description**  
`Sequence[DocumentReference]` | iterator of subdocuments of the current collection. If the collection does not exist at the time of `snapshot`, the iterator will be empty  
  
### stream
    
    
    stream(
        transaction: Optional[transaction.Transaction] = None,
        retry: retries.AsyncRetry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: Optional[float] = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> AsyncStreamGenerator[DocumentSnapshot]

Read the documents in this collection.

This sends a `RunQuery` RPC and then returns a generator which consumes each document returned in the stream of `RunQueryResponse` messages.

**Note:** The underlying stream of responses will time out after the `max_rpc_timeout_millis` value set in the GAPIC client configuration for the `RunQuery` API. Snapshots not consumed from the iterator before that point will be lost. 

**Parameters**  
---  
**Name** | **Description**  
`transaction` |  `Optional[ Transaction]`   
An existing transaction that the query will run in.  
`retry` |  `Optional[google.api_core.retry.Retry]`   
Designation of what errors, if any, should be retried. Defaults to a system-specified policy.  
`timeout` |  `Optional[float]`   
The timeout for this request. Defaults to a system-specified value.  
`read_time` |  `Optional[datetime.datetime]`   
If set, reads documents as they were at the given time. This must be a timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days. If no timezone is specified in the `datetime.datetime` object, it is assumed to be UTC.  
**Returns**  
---  
**Type** | **Description**  
``AsyncStreamGenerator[DocumentSnapshot]`` | A generator of the query results.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
