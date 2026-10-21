---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/IndexClass/
title: google.appengine.api.search.Index \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:48:05.590544+00:00
---

# google.appengine.api.search.Index  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/IndexClass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.search.Index Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L3398-L4038) Represents an index allowing indexing, deleting and searching documents. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.api.search.search.Index`
    
    
    google.appengine.api.search.Index(
        name, namespace=None, source=SEARCH
    )
    

The following code fragment shows how to add documents, then search the index for documents matching a query.
    
    
      # Get the index.
      index = Index(name='index-name')
    
      # Create a document.
      doc = Document(doc_id='document-id',
                     fields=[TextField(name='subject', value='my first email'),
                             HtmlField(name='body',
                                       value='<html>some content here</html>')])
    
      # Index the document.
      try:
        index.put(doc)
      except search.Error, e:
        # possibly retry indexing or log error
    
      # Query the index.
      try:
        results = index.search('subject:first body:here')
    
        # Iterate through the search results.
        for scored_document in results:
           print scored_document
    
      except search.Error, e:
        # possibly log the failure
    

Once an index is created with a given specification, that specification is immutable. Search results may contain some out of date documents. However, any two changes to any document stored in an index are applied in the correct order. | 

## Args  
  
---  
  
`name` |  The name of the index. An index name must be a visible printable ASCII string not starting with '!'. Whitespace characters are excluded.   
`namespace` |  The namespace of the index name. If not set, then the current namespace is used.   
`source` |  Deprecated as of 1.7.6. The source of the index: SEARCH - The Index was created by adding documents through this search API. DATASTORE - The Index was created as a side-effect of putting entities into Datastore. CLOUD_STORAGE - The Index was created as a side-effect of adding objects into a Cloud Storage bucket.   
  
## Raises  
  
---  
  
`TypeError` |  If an unknown attribute is passed.   
`ValueError` |  If invalid namespace is given.   
  
## Attributes  
  
---  
  
`name` |  Returns the name of the index.   
`namespace` |  Returns the namespace of the name of the index.   
`schema` |  Returns the schema mapping field names to list of types supported. Only valid for Indexes returned by search.get_indexes method.   
`source` |  Returns the source of the index. **Deprecated:** from 1.7.6, source is no longer available.   
`storage_limit` |  The maximum allowable storage for this index, in bytes. Returns None for indexes not obtained from search.get_indexes.   
`storage_usage` |  The approximate number of bytes used by this index. The number may be slightly stale, as it may not reflect the results of recent changes. Returns None for indexes not obtained from search.get_indexes.   
  
## Methods

### `delete`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L3659-L3680)
    
    
    delete(
        document_ids, deadline=None
    )
    

Delete the documents with the corresponding document ids from the index.

If no document exists for the identifier in the list, then that document identifier is ignored.

Args  
---  
  
`document_ids` |  A single identifier or list of identifiers of documents to delete.   
  
#### Kwargs:

  * **`deadline`** : Deadline for RPC call in seconds; if None use the default.



Raises  
---  
  
`DeleteError` |  If one or more documents failed to remove or number removed did not match requested.   
`ValueError` |  If document_ids is not a string or iterable of valid document identifiers or number of document ids is larger than MAXIMUM_DOCUMENTS_PER_PUT_REQUEST or deadline is a negative number.   
  
### `delete_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L3682-L3719)
    
    
    delete_async(
        document_ids, deadline=None
    )
    

Asynchronously deletes the documents with the corresponding document ids.

Identical to delete() except that it returns a future. Call get_result() on the return value to block on the call and get its result.

### `delete_schema`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L3721-L3751)
    
    
    delete_schema()
    

Delete the schema from the index.

To fully delete an index, you must delete both the index's documents and schema. This method deletes the index's schema, which contains field names and field types of previously indexed documents.

Raises  
---  
  
`DeleteError` |  If the schema failed to be deleted.   
  
Returns  
---  
None   
  
### `get`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L3824-L3844)
    
    
    get(
        doc_id, deadline=None
    )
    

Retrieve a document by document ID.

Args  
---  
  
`doc_id` |  The ID of the document to retrieve.   
  
#### Kwargs:

  * **`deadline`** : Deadline for RPC call in seconds; if None use the default.



Returns  
---  
If the document ID exists, returns the associated document. Otherwise, returns None.   
  
Raises  
---  
  
`TypeError` |  If any of the parameters have invalid types, or an unknown attribute is passed.   
`ValueError` |  If any of the parameters have invalid values (e.g., a negative deadline).   
  
### `get_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L3846-L3858)
    
    
    get_async(
        doc_id, deadline=None
    )
    

Asynchronously retrieve a document by document ID.

Identical to get() except that it returns a future. Call get_result() on the return value to block on the call and get its result.

### `get_range`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L3971-L4000)
    
    
    get_range(
        start_id=None,
        include_start_object=True,
        limit=100,
        ids_only=False,
        deadline=None,
        **kwargs
    )
    

Get a range of Documents in the index, in id order.

Args  
---  
  
`start_id` |  String containing the Id from which to list Documents from. By default, starts at the first Id.   
`include_start_object` |  If true, include the Document with the Id specified by the start_id parameter.   
`limit` |  The maximum number of Documents to return.   
`ids_only` |  If true, the Documents returned only contain their keys.   
  
#### Kwargs:

  * **`deadline`** : Deadline for RPC call in seconds; if None use the default.



Returns  
---  
A GetResponse containing a list of Documents, ordered by Id.   
  
Raises  
---  
  
`Error` |  Some subclass of Error is raised if an error occurred processing the request.   
`TypeError` |  If any of the parameters have invalid types, or an unknown attribute is passed.   
`ValueError` |  If any of the parameters have invalid values (e.g., a negative deadline).   
  
### `get_range_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L4002-L4038)
    
    
    get_range_async(
        start_id=None,
        include_start_object=True,
        limit=100,
        ids_only=False,
        deadline=None,
        **kwargs
    )
    

Asynchronously gets a range of Documents in the index, in id order.

Identical to get_range() except that it returns a future. Call get_result() on the return value to block on the call and get its result.

### `put`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L3560-L3584)
    
    
    put(
        documents, deadline=None
    )
    

Index the collection of documents.

If any of the documents are already in the index, then reindex them with their corresponding fresh document.

Args  
---  
  
`documents` |  A Document or iterable of Documents to index.   
  
#### Kwargs:

  * **`deadline`** : Deadline for RPC call in seconds; if None use the default.



Returns  
---  
A list of PutResult, one per Document requested to be indexed.   
  
Raises  
---  
  
`PutError` |  If one or more documents failed to index or number indexed did not match requested.   
`TypeError` |  If an unknown attribute is passed.   
`ValueError` |  If documents is not a Document or iterable of Document or number of the documents is larger than MAXIMUM_DOCUMENTS_PER_PUT_REQUEST or deadline is a negative number.   
  
### `put_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L3586-L3641)
    
    
    put_async(
        documents, deadline=None
    )
    

Asynchronously indexes the collection of documents.

Identical to put() except that it returns a future. Call get_result() on the return value to block on the call and get its result.

### `search`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L3860-L3924)
    
    
    search(
        query, deadline=None, **kwargs
    )
    

Search the index for documents matching the query.

For example, the following code fragment requests a search for documents where 'first' occurs in subject and 'good' occurs anywhere, returning at most 20 documents, starting the search from 'cursor token', returning another single cursor for the response, sorting by subject in descending order, returning the author, subject, and summary fields as well as a snippeted field content.

results = index.search( query=Query('subject:first good', options=QueryOptions(limit=20, cursor=Cursor(), sort_options=SortOptions( expressions=[SortExpression(expression='subject')], limit=1000), returned_fields=['author', 'subject', 'summary'], snippeted_fields=['content'])))

The following code fragment shows how to use a results cursor

cursor = results.cursor for result in results: # process result

results = index.search( Query('subject:first good', options=QueryOptions(cursor=cursor)))

The following code fragment shows how to use a per_result cursor

results = index.search( query=Query('subject:first good', options=QueryOptions(limit=20, cursor=Cursor(per_result=True), ...)))

cursor = None for result in results: cursor = result.cursor

results = index.search( Query('subject:first good', options=QueryOptions(cursor=cursor)))

See http://developers.google.com/appengine/docs/python/search/query_strings for more information about query syntax.

Args  
---  
  
`query` |  The Query to match against documents in the index.   
  
#### Kwargs:

  * **`deadline`** : Deadline for RPC call in seconds; if None use the default.



Returns  
---  
A SearchResults containing a list of documents matched, number returned and number matched by the query.   
  
Raises  
---  
  
`TypeError` |  If any of the parameters have invalid types, or an unknown attribute is passed.   
`ValueError` |  If any of the parameters have invalid values (e.g., a negative deadline).   
  
### `search_async`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L3926-L3944)
    
    
    search_async(
        query, deadline=None, **kwargs
    )
    

Asynchronously searches the index for documents matching the query.

Identical to search() except that it returns a future. Call get_result() on the return value to block on the call and get its result.

### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L3527-L3529)
    
    
    __eq__(
        other
    )
    

Return self==value.

### `__ne__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L3531-L3532)
    
    
    __ne__(
        other
    )
    

Return self!=value.

## Class Variables  
  
---  
  
CLOUD_STORAGE |  `'CLOUD_STORAGE'`  
DATASTORE |  `'DATASTORE'`  
RESPONSE_CURSOR |  `'RESPONSE_CURSOR'`  
RESULT_CURSOR |  `'RESULT_CURSOR'`  
SEARCH |  `'SEARCH'`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
