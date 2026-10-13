---
url: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transaction.Transaction
title: Class Transaction (2.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:37.842768+00:00
---

# Class Transaction (2.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.transaction.Transaction

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Transaction (2.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.34.0 (latest)  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.0  2.23.0  2.22.0  2.21.0  2.20.2  2.19.0  2.18.0  2.17.2  2.16.1  2.15.0  2.14.0  2.13.1  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.1  2.5.3  2.4.0  2.3.4  2.2.0  2.1.3  2.0.2  1.9.2  1.8.1  1.7.0  1.6.2  1.5.0  1.4.0  1.3.0 
    
    
    Transaction(client, max_attempts=5, read_only=False)

Accumulate read-and-write operations to be sent in a transaction.

## Parameters  
  
---  
**Name** | **Description**  
`client` |  `[Client](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.client.Client)`   
The client that created this transaction.  
`max_attempts` |  `Optional[int]`   
The maximum number of attempts for the transaction (i.e. allowing retries). Defaults to MAX_ATTEMPTS.  
`read_only` |  `Optional[bool]`   
Flag indicating if the transaction should be read-only or should allow writes. Defaults to :data:`False`.  
  
## Properties 

### id

Get the current transaction ID.

**Returns**  
---  
**Type** | **Description**  
`Optional[bytes]` | The transaction ID (or :data:`None` if the current transaction is not in progress).  
  
### in_progress

Determine if this transaction has already begun.

**Returns**  
---  
**Type** | **Description**  
`bool` | Indicates if the transaction has started.  
  
## Methods 

### commit
    
    
    commit(
        retry: (
            google.api_core.retry.retry_unary.Retry | object | None
        ) = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Optional[float] = None,
    ) -> list

Commit the changes accumulated in this batch.

**Parameters**  
---  
**Name** | **Description**  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried. Defaults to a system-specified policy.  
`timeout` |  `float`   
The timeout for this request. Defaults to a system-specified value.  
**Returns**  
---  
**Type** | **Description**  
`List[WriteResult, ...]` | The write results corresponding to the changes committed, returned in the same order as the changes were applied to this batch. A write result contains an `update_time` field.  
  
### create
    
    
    create(
        reference: google.cloud.firestore_v1.base_document.BaseDocumentReference,
        document_data: dict[str, typing.Any],
    ) -> None

Add a "change" to this batch to create a document.

If the document given by `reference` already exists, then this batch will fail when `commit`-ed.

**Parameters**  
---  
**Name** | **Description**  
`reference` |  `[DocumentReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.document.DocumentReference)`   
A document reference to be created in this batch.  
`document_data` |  `dict`   
Property names and values to use for creating a document.  
  
### delete
    
    
    delete(
        reference: google.cloud.firestore_v1.base_document.BaseDocumentReference,
        option: typing.Optional[google.cloud.firestore_v1._helpers.WriteOption] = None,
    ) -> None

Add a "change" to delete a document.

See xref_delete for more information on how `option` determines how the change is applied.

**Parameters**  
---  
**Name** | **Description**  
`reference` |  `[DocumentReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.document.DocumentReference)`   
A document reference that will be deleted in this batch.  
`option` |  `Optional[WriteOption]`   
A write option to make assertions / preconditions on the server state of the document before applying changes.  
  
### get
    
    
    get(
        ref_or_query: DocumentReference | Query,
        retry: retries.Retry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: Optional[float] = None,
        *,
        explain_options: Optional[ExplainOptions] = None,
        read_time: Optional[datetime.datetime] = None
    ) -> StreamGenerator[DocumentSnapshot] | Generator[DocumentSnapshot, Any, None]

Retrieve a document or a query result from the database.

**Parameters**  
---  
**Name** | **Description**  
`ref_or_query` |  `DocumentReference Query`   
The document references or query object to return.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried. Defaults to a system-specified policy.  
`timeout` |  `float`   
The timeout for this request. Defaults to a system-specified value.  
`read_time` |  `Optional[datetime.datetime] :Yields: *.DocumentSnapshot* -- The next document snapshot that fulfills the query, or :data:`None` if the document does not exist.`   
If set, reads documents as they were at the given time. This must be a timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days. If no timezone is specified in the `datetime.datetime` object, it is assumed to be UTC.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | if `ref_or_query` is not one of the supported types, or  
`explain_option` | is provided when `ref_or_query` is a document:  
`reference.` |   
  
### get_all
    
    
    get_all(
        references: list,
        retry: retries.Retry | object | None = _MethodDefault._DEFAULT_VALUE,
        timeout: float | None = None,
        *,
        read_time: datetime.datetime | None = None
    ) -> Generator[DocumentSnapshot, Any, None]

Retrieves multiple documents from Firestore.

**Parameters**  
---  
**Name** | **Description**  
`references` |  `List[.DocumentReference, ...]`   
Iterable of document references to be retrieved.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried. Defaults to a system-specified policy.  
`timeout` |  `float`   
The timeout for this request. Defaults to a system-specified value.  
`read_time` |  `Optional[datetime.datetime] :Yields: *.DocumentSnapshot* -- The next document snapshot that fulfills the query, or :data:`None` if the document does not exist.`   
If set, reads documents as they were at the given time. This must be a timestamp within the past one hour, or if Point-in-Time Recovery is enabled, can additionally be a whole minute timestamp within the past 7 days. If no timezone is specified in the `datetime.datetime` object, it is assumed to be UTC.  
  
### set
    
    
    set(
        reference: google.cloud.firestore_v1.base_document.BaseDocumentReference,
        document_data: dict,
        merge: typing.Union[bool, list] = False,
    ) -> None

Add a "change" to replace a document.

See xref_set for more information on how `option` determines how the change is applied.

**Parameters**  
---  
**Name** | **Description**  
`reference` |  `[DocumentReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.document.DocumentReference)`   
A document reference that will have values set in this batch.  
`document_data` |  `dict`   
Property names and values to use for replacing a document.  
`merge` |  `Optional[bool] or Optional[List`   
If True, apply merging instead of overwriting the state of the document.  
  
### update
    
    
    update(
        reference: google.cloud.firestore_v1.base_document.BaseDocumentReference,
        field_updates: dict[str, typing.Any],
        option: typing.Optional[google.cloud.firestore_v1._helpers.WriteOption] = None,
    ) -> None

Add a "change" to update a document.

See xref_update for more information on `field_updates` and `option`.

**Parameters**  
---  
**Name** | **Description**  
`reference` |  `[DocumentReference](https://docs.cloud.google.com/python/docs/reference/firestore/latest/google.cloud.firestore_v1.document.DocumentReference)`   
A document reference that will be updated in this batch.  
`field_updates` |  `dict`   
Field names or paths to update and values to update with.  
`option` |  `Optional[WriteOption]`   
A write option to make assertions / preconditions on the server state of the document before applying changes.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
