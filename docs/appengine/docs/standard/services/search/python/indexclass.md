---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/indexclass/
title: The Index Class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:49.634119+00:00
---

# The Index Class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/indexclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The Index Class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Class `Index` represents an index allowing documents to be indexed, deleted, and searched.

`Index` is defined in the `google.appengine.api.search` module.

**Note:** There are asynchronous methods corresponding to each instance method: `put_async`, `delete_async`, `get_async`, `search_async`, and `get_range_async`. These are identical to the synchronous methods, except they all return a future. To get the actual result, call `get_result()` on the returned value; that call will block. 

## Introduction

The `Index` class provides arguments to construct an index as well as functions allowing you to add, list, search, and delete [documents](https://docs.cloud.google.com/appengine/docs/standard/search/documentclass) (or an iterable collection of documents) within the index. You construct an index using arguments to the `Index` class, including the name and namespace of the index.

The following code shows how to put documents into an index, then search it for documents matching a query:
    
    
    # Get the index.
    index = search.Index(name='index-name')
    
    # Create a document.
    doc = search.Document(
        doc_id='document-id',
        fields=[search.TextField(name='subject', value='my first email'),
                search.HtmlField(name='body', value='<html>some content here</html>')])
    
    # Index the document.
    try:
        index.put(doc)
    except search.PutError, e:
        result = e.results[0]
        if result.code == search.OperationResult.TRANSIENT_ERROR:
            # possibly retry indexing result.object_id
    except search.Error, e:
        # possibly log the failure
    
    # Query the index.
    try:
        results = index.search('subject:first body:here')
    
        # Iterate through the search results.
        for scored_document in results:
            # process the scored_document
    
    except search.Error, e:
        # possibly log the failure

## Constructor

The constructor for class `Index` is defined as follows:

Index(name, namespace=None)

    

Construct an instance of class `Index`.

    

Arguments

name
    

Index name (see name property, below, for details).

namespace
    

For [multitenant applications](https://docs.cloud.google.com/appengine/docs/standard/services/multitenancy), the namespace in which index name is defined.

Result value

    

A new instance of class `Index`.

## Properties

An instance of class `Index` has the following properties:

schema
    

Schema mapping field names to the list of types supported. Valid only for indexes returned by the `[search.get_indexes](https://docs.cloud.google.com/appengine/docs/standard/services/search/pythonfunctions#get_indexes)` method.

name
    

Index name, a human-readable ASCII string identifying the index. Must contain no whitespace characters and not start with an exclamation point (`!`).

namespace
    

Namespace in which index name is defined.

storage_usage
    

The approximate number of bytes used by this index. The number may not reflect the results of recent changes. Valid only for indexes returned by the `[search.get_indexes](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/functions#get_indexes)` method.

storage_limit
    

The maximum allowable storage for this index, in bytes. Valid only for indexes returned by the `[search.get_indexes](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/functions#get_indexes)` method.

## Instance Methods

Instances of class `Index` have the following methods:

put(self, documents, deadline=None)
    

If the specified documents have already been put into the index, and if they have the same `doc_ids`, they are reindexed with updated contents.

    

Arguments

documents
    

Document (or iterable collection of documents) to index.

deadline
    

Deadline for RPC call in seconds.

Result value

    

List of results (`PutResult`), one for each document requested to be indexed.

Exceptions

PutError
    

One or more documents failed to index, or number indexed did not match number requested.

TypeError
    

Unknown attribute passed.

ValueError
    

Argument not a document or iterable collection of documents, or number of documents larger than `MAXIMUM_DOCUMENTS_PER_PUT_REQUEST`.

delete(self, document_ids, deadline=None)
    

Delete documents from index.

If no document exists for an identifier in the list, that identifier is ignored.

    

Arguments

document_ids
    

Identifier (or list of identifiers) of documents to delete.

deadline
    

Deadline for RPC call in seconds.

Exceptions

DeleteError
    

One or more documents failed to delete, or number deleted did not match number requested.

ValueError
    

Argument not a string or iterable collection of valid document identifiers, or number of document identifiers larger than `MAXIMUM_DOCUMENTS_PER_PUT_REQUEST`.

get(self,doc_id, deadline=None)
    

Retrieves a [Document](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/documentclass) from the index using the document's identifier. If the document is not found, returns `None`.

    

Arguments

doc_id
    

The identifier of the document to retrieve.

deadline
    

Deadline for RPC call in seconds.

Result value

    

A [Document](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/documentclass) object whose identifier matches the one supplied by doc_id.

search(query, deadline=None)
    

Search the index for documents matching the query. The query may be either a string or a [Query](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/queryclass) object.

For example, the following code fragment requests a search for documents where 'first' occurs in subject and 'good' occurs anywhere, returning at most 20 documents, starting the search from 'cursor token', returning another single cursor for the response, sorting by subject in descending order, returning the author, subject, and summary fields as well as a snippeted field content.
    
    
    results = index.search(
              # Define the query by using a Query object.
              query=Query('subject:first good',
                  options=QueryOptions(limit=20,
                      cursor=Cursor(),
                      sort_options=SortOptions(
                          expressions=[SortExpression(expression='subject',
                                                      default_value='')],
                          limit=1000),
                      returned_fields=['author', 'subject', 'summary'],
                      snippeted_fields=['content'])))

The following code fragment shows how to use a results cursor.
    
    
    cursor = results.cursor
    for result in results:
         # process result
    results = index.search(Query('subject:first good',
                           options=QueryOptions(cursor=cursor))
                          )

The following code fragment shows how to use a `per_result` cursor:
    
    
    results = index.search(query=Query('subject:first good',
                           options=QueryOptions(limit=20,
                           cursor=Cursor(per_result=True),
                           ...))
                           )
    
    cursor = None
    for result in results:
        cursor = result.cursor
    
    results = index.search(
              Query('subject:first good', options=QueryOptions(cursor=cursor))
                   )

    

Arguments

query
    

The query to match against documents in the index, described in a [Query](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/queryclass) object. For more information, please see the [Query Language Overview](https://docs.cloud.google.com/appengine/docs/standard/services/search#Query_Language_Overview).

deadline
    

Deadline for RPC call in seconds.

Result value

    

A [SearchResults](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/searchresultsclass) object containing a list of documents matched, number returned and number matched by the query.

Exceptions

TypeError
    

A parameter has an invalid type, or an unknown attribute was passed.

ValueError
    

A parameter has an invalid value.

get_range(self, start_id=None, include_start_object=True, limit=100, ids_only=False, deadline=None) 
    

Get a range of documents from an index, in `doc_id` order.

    

Arguments

start_id
    

String containing the document identifier from which to list documents. By default, starts at the first document identifier.

include_start_object
    

If `true`, include document specified by `start_id`.

limit
    

Maximum number of documents to return.

ids_only
    

If `true`, return only document identifiers instead of full documents.

deadline
    

Deadline for RPC call in seconds.

Result value

    

`A [GetResponse](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/getresponseclass)` object containing a list of the retrieved documents, ordered by document identifier.

Exceptions

TypeError
    

Unknown attribute passed.

Error
    

Some subclass of `Error` occurred while processing request.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
