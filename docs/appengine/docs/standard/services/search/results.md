---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/results/
title: Handling search results \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:44:01.900225+00:00
---

# Handling search results  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/results/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Handling search results Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

When a query call completes normally, it returns the result as a [`SearchResults`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/searchresultsclass) object. The results object tells you how many matching documents were found in the index, and how many matched documents were returned. It also includes a list of matching [`ScoredDocuments`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/scoreddocumentclass). The list usually contains a portion of all the matching documents found, since search returns a limited number of documents each time it's called. By using an offset or a cursor you can retrieve all the matching documents, a subset at a time.

## Results
    
    
    def query_results(index, query_string):
        result = index.search(query_string)
        total_matches = result.number_found
        list_of_docs = result.results
        number_of_docs_returned = len(list_of_docs)
        return total_matches, list_of_docs, number_of_docs_returned

Depending on the value of the `limit` [query option](https://docs.cloud.google.com/appengine/docs/standard/services/search/options#queryoptions), the number of matching documents returned in the result may be less than the number found. Remember that the number found will be an estimate if the number found accuracy is less than the number found. No matter how you configure the search options, a `search()` call will find no more than 10,000 matching documents.

If more documents were found than returned, and you want to retrieve all of them, you need to repeat the search using either an offset or a cursor, as explained below.

**Note:** Your calling code should be prepared to handle exceptions which might be thrown if the query is invalid or there were problems processing it.

## Scored documents

The search results will include a list of [`ScoredDocuments`]/appengine/docs/standard/services/search/python/scoreddocumentclass) that match the query. You can iterate over the list to process each document in turn:
    
    
    for scored_document in results:
            print(scored_document)
    

By default, a scored document contains all the fields of the original document that was indexed. If your [query options](https://docs.cloud.google.com/appengine/docs/standard/services/search/python#queryoptions) specified ` returned_fields `, only those fields appear in the [fields](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/documentclass#Document_fields) property of the document. If you created any computed fields by specifying ` returned_expressions ` or ` snippeted_fields ` they will appear separately in the [expressions](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/scoreddocumentclass#SortExpression_expressions) property of the document.

## Using offsets

If your search finds more documents than you can return at once, use an offset to index into the list of matching documents. For example, the default query limit is 20 documents. After you've executed a search the first time (with offset 0) and retrieved the first 20 documents, retrieve the next 20 documents by setting the offset to 20 and running the same search again. Keep repeating the search, incrementing the offset each time by the number of documents returned:
    
    
    def query_offset(index, query_string):
        offset = 0
    
        while True:
            # Build the query using the current offset.
            options = search.QueryOptions(offset=offset)
            query = search.Query(query_string=query_string, options=options)
    
            # Get the results
            results = index.search(query)
    
            number_retrieved = len(results.results)
            if number_retrieved == 0:
                break
    
            # Add the number of documents found to the offset, so that the next
            # iteration will grab the next page of documents.
            offset += number_retrieved
    
            # Process the matched documents
            for document in results:
                print(document)

Offsets can be inefficient when iterating over a very large result set.

## Using cursors

You can also use cursors to retrieve a subrange of results. Cursors are useful when you intend to present your search results in consecutive pages and you want to be sure you do not skip any documents in the case where an index could be modified between queries. Cursors are also more efficient when iterating across a very large result set.

In order to use cursors, you must create an initial cursor and include it in the query options. There are two kinds of cursors, _per-query_ and _per-result_. A per-query cursor causes a separate cursor to be associated with the results object returned by the search call. A per-result cursor causes a cursor to be associated with every scored document in the results.

### Using a per-query cursor

By default, a newly constructed cursor is a per-query cursor. This cursor holds the position of the last document returned in the search's results. It is updated with each search. To enumerate all matching documents in an index, execute the same search until the result returns a null cursor:
    
    
    def query_cursor(index, query_string):
        cursor = search.Cursor()
    
        while cursor:
            # Build the query using the cursor.
            options = search.QueryOptions(cursor=cursor)
            query = search.Query(query_string=query_string, options=options)
    
            # Get the results and the next cursor
            results = index.search(query)
            cursor = results.cursor
    
            for document in results:
                print(document)

### Using a per-result cursor

To create per-result cursors, you must set the cursor per_result property to true when you create the initial cursor. When the search returns, every document will have a cursor associated with it. You can use that cursor to specify a new search with results that begin with a specific document. Note that when you pass a per-result cursor to search, there will be no per-query cursor associated with the result itself; result.getCursor() will return null so you can't use this to test whether you've retrieved all the matches.
    
    
    def query_per_document_cursor(index, query_string):
        cursor = search.Cursor(per_result=True)
    
        # Build the query using the cursor.
        options = search.QueryOptions(cursor=cursor)
        query = search.Query(query_string=query_string, options=options)
    
        # Get the results.
        results = index.search(query)
    
        document_cursor = None
        for document in results:
            # discover some document of interest and grab its cursor, for this
            # sample we'll just use the first document.
            document_cursor = document.cursor
            break
    
        # Start the next search from the document of interest.
        if document_cursor is None:
            return
    
        options = search.QueryOptions(cursor=document_cursor)
        query = search.Query(query_string=query_string, options=options)
        results = index.search(query)
    
        for document in results:
            print(document)

### Saving and restoring cursors

A cursor can be serialized as a web-safe string, saved, and then restored for later use:
    
    
    def saving_and_restoring_cursor(cursor):
        # Convert the cursor to a web-safe string.
        cursor_string = cursor.web_safe_string
        # Restore the cursor from a web-safe string.
        cursor = search.Cursor(web_safe_string=cursor_string)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
