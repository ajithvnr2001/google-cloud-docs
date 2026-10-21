---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/queryoptionsclass/
title: The QueryOptions Class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:38:22.939986+00:00
---

# The QueryOptions Class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/queryoptionsclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The QueryOptions Class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Class `QueryOptions` provides options for post-processing query results based on the needs of your application. You construct the class as the `options` in the [Query.options](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/queryclass) argument.

`Query` is defined in the `google.appengine.api.search` module.

## Introduction

Class `QueryOptions` provides options for post-processing the results for a specific query. Options include the ability to sort results, control which document fields to return, produce snippets of fields and compute and sort by complex scoring expressions.

If you wish to randomly access pages of search results, you can use an offset:
    
    
    from google.appengine.api import search
    ...
    # get the first set of results
    page_size = 10
    results = index.search(search.Query(query_string='some stuff',
        options=search.QueryOptions(limit=page_size))
    
    # calculate pages
    pages = results.number_found / page_size
    
    # user chooses page and hence an offset into results
    next_page = ith * page_size
    
    # get the search results for that page
    results = index.search(search.Query(query_string='some stuff',
        options=search.QueryOptions(limit=page_size, offset=next_page))

For example, the following code fragment requests a search for documents where `first` occurs in the `subject` field and `good` occurs in any field, returning at most 20 documents, requesting the cursor for the next page of results, returning another cursor for the next set of results, sorting by subject in descending order, returning the author, subject, and summary fields as well as a snippeted field content:
    
    
    ...
    results = index.search(search.Query(
        query='subject:first good',
        options=search.QueryOptions(
            limit=20,
            cursor=search.Cursor(),
            sort_options=search.SortOptions(
                expressions=[
                    search.SortExpression(expression='subject', default_value='')],
                limit=1000),
            returned_fields=['author', 'subject', 'summary'],
            snippeted_fields=['content'])))

## Constructor

The constructor for class `QueryOptions` is defined as follows:

class QueryOptions(limit=20, number_found_accuracy=None, cursor=None, offset=None, sort_options=None, returned_fields=None, ids_only=False, snippeted_fields=None, returned_expressions=None)

    

Specify options defining search query results..

    

Arguments

limit
    

The limit on number of documents to return in results.

number_found_accuracy
    

The minimum accuracy requirement for `SearchResults.number_found`. If set, remains accurate up to at least that number. For example, when set to 100, any `SearchResults` object with `number_found_accuracy` <= 100 is accurate.

**Caution!** This option may add considerable latency/expense, especially when used with `returned_fields`.
cursor
    

A Cursor describing where to get the next set of results, or to provide next cursors in SearchResults.

offset
    

The offset represents the number of documents to skip in search results. This is an alternative to using a query cursor. It allows random access to the results. Offsets are more expensive (in terms of [instance hours](https://docs.cloud.google.com/appengine/docs/pricing)) than cursors. You can use either cursor or offset, but not both. Using an offset means that no cursor is returned in [`ScoredDocument.cursor`](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/searchresultsclass) or `ScoredDocument.cursor`.

sort_options
    

A `[SortOptions](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/sortoptionsclass)` object specifying a multi-dimensional sort over search results.

returned_fields
    

An iterable of names of fields to return in search results.

ids_only
    

Only return document ids, do not return any fields.

snippeted_fields
    

An iterable of names of fields to snippet and return in search result expressions.

returned_expressions
    

An iterable of FieldExpression to evaluate and return in search results.

Result value

    

A new instance of class `QueryOptions`.

Exceptions

TypeError
    

If an unknown iterator_options or sort_options is passed.

ValueError
    

If `ids_only` and `returned_fields` are used together.

## Properties

An instance of class `Query` has the following properties:

limit
    

Returns a limit on number of documents to return in results.

number_found_accuracy
    

Returns minimum accuracy requirement for [SearchResults.number_found](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/searchresultsclass).

cursor
    

Returns the cursor for the query.

offset
    

Returns the number of documents in search results to skip.

sort_options
    

Returns a [SortOptions](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/sortoptionsclass) object.

returned_fields
    

Returns an iterable of names of fields to return in search results.

ids_only
    

Returns only ` ` in search results.

snippeted_fields
    

Returns iterable of field names to snippet and return in results.

returned_expressions
    

Returns iterable of [FieldExpression](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/fieldexpressionclass) to return in results.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
