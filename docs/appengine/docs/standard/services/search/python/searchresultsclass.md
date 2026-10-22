---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/searchresultsclass/
title: The SearchResults Class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:49.018953+00:00
---

# The SearchResults Class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/searchresultsclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The SearchResults Class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Class `SearchResults` represents the result of executing a search request using `[Index.search()](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/indexclass)`.

`SearchResults` is defined in the `google.appengine.api.search` module.

## Constructor

The constructor for class `SearchResults` is defined as follows:

class SearchResults(number_found, results=None, cursor=None)
    

Request the search service to query an index, specifying parameters for that query..

    

Arguments

number_found
    

The number of documents found for the query.

results
    

The list of [ScoredDocument](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/scoreddocumentclass) objects returned from executing a search request.

cursor
    

A [Cursor](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/cursorclass) object allowing you to continue the search from the end of the current search results.

Result value

    

A new instance of class `SearchRequest` representing the results of executing [Index.search()](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/indexclass).

Exceptions

TypeError
    

If any of the parameters have an invalid type, or an unknown attribute is passed.

ValueError
    

If any parameter has an invalid value.

## Properties

An instance of class `SearchResults` has the following properties:

results
    

Returns the list of [ScoredDocument](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/scoreddocumentclass) objects matching the query.

number_found
    

Returns an approximate number of documents matching the query. `[QueryOptions](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/queryoptionsclass)` defining post-processing of the search results. If the `QueryOptions.number_found_accuracy` parameter were set to 100, then `number_found` <= 100 is accurate.

cursor
    For this field to be populated, you must pass a cursor in the search's [QueryOptions](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/queryoptionsclass), otherwise this will be None. Returns a results [Cursor](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/cursorclass) that can be used to continue the search from the last result. If there are no more results after the current result, returns None.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
