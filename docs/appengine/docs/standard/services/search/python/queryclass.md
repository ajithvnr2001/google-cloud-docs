---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/queryclass/
title: The Query Class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:53:39.410373+00:00
---

# The Query Class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/queryclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The Query Class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Class `Query` represents a request on the search service to query the index.

`Query` is defined in the `google.appengine.api.search` module.

## Introduction

The `Query` class allows you to specify a query string and other options, such as sort order, limit, and a cursor, for a search on an index. You set these options by instantiating the `[QueryOptions](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/queryoptionsclass)` class to the `Query.options` parameter.

For example, the following code fragment requests a search for documents where `first` occurs in subject and `good` occurs anywhere, returning at most 20 documents, returning a single document cursor for the results, sorting by subject in descending order, returning the author, subject, and summary fields as well as a snippeted field content.
    
    
    from google.appengine.api import search
    
    ...
    results = index.search(search.Query(
        # Specify the query string using the Search API's [Query language](https://docs.cloud.google.com/appengine/docs/standard/services/search/query-strings).
        query_string='subject:first good',
        options=search.QueryOptions(
            limit=20,
            cursor=search.Cursor(),
            sort_options=search.SortOptions(
                expressions=[
                    search.SortExpression(expression='subject', default_value='')],
                limit=1000),
            returned_fields=['author', 'subject', 'summary'],
            snippeted_fields=['content'])))
    ...

You have the option to return a cursor with each set of search results. This cursor allows you to more easily page through search results. To get a Cursor, specify it in `[QueryOptions.cursor](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/queryoptionsclass)` and extract the cursor for the next request from `[SearchResults.cursor](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/searchresultsclass)`. This allows you to continue your search from the last found document, as shown below: 
    
    
    ...
    results = index.search(
        search.Query(query_string='subject:first good',
              options=search.QueryOptions(cursor=results.cursor)))

## Constructor

The constructor for class `Query` is defined as follows:

class Query(query_string, options=None, enable_facet_discovery=False, return_facets=None, facet_options=None, facet_refinements=None)

    

Request the search service to query an index, specifying parameters for that query.

    

Arguments

query_string
    

The query to match against documents in the index. A query is a boolean expression containing terms. For example, the query `job tag:"very important" sent < 2011-02-28 ` finds documents with the term `job` in any field, and also contain the phrase `very important` in a `tag` field, and a `sent` date prior to February 28, 2011.

options
    

Instantiation of the `[QueryOptions](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/queryoptionsclass)` class with instructions for post-processing search results.

enable_facet_discovery
    

Enable the discovery of the most relevant facets used by the documents that satisfy this search query and return them.

return_facets
    

An iterable of FacetRequest or basestring as facet name to return specific facet with the result.

facet_options
    

A FacetOption describing processing of facets.

facet_refinements
    

An iterable of FacetRefinement objects or refinement token strings used to filter out search results based on a facet value. refinements for different facets will be conjunction and refinements for the same facet will be disjunction.

Result value

    

A new instance of class `Query`.

Exceptions

TypeError
    

Raised when `query_string` is not a string or `options` is not a `QueryOptions` object.

ValueError
    

Raised when the `query_string` could not be parsed.

## Properties

An instance of class `Query` has the following properties:

query_string
    

Returns the query string to search in this request.

options
    

Returns the `[QueryOptions](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/queryoptionsclass)` defining post-processing of the search results.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
