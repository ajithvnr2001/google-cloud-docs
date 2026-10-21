---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/QueryOptions/
title: google.appengine.api.search.QueryOptions \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:10:10.458454+00:00
---

# google.appengine.api.search.QueryOptions  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/QueryOptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.search.QueryOptions Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L3003-L3169) Options for post-processing results for a query. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.api.search.search.QueryOptions`
    
    
    google.appengine.api.search.QueryOptions(
        limit=20,
        number_found_accuracy=None,
        cursor=None,
        offset=None,
        sort_options=None,
        returned_fields=None,
        ids_only=False,
        snippeted_fields=None,
        returned_expressions=None
    )
    

Options include the ability to sort results, control which document fields to return, produce snippets of fields and compute and sort by complex scoring expressions. If you wish to randomly access pages of search results, you can use an offset:

# get the first set of results

page_size = 10 results = index.search(Query(query_string='some stuff', QueryOptions(limit=page_size))

# calculate pages

pages = results.found_count / page_size

# user chooses page and hence an offset into results

next_page = ith * page_size

# get the search results for that page

results = index.search(Query(query_string='some stuff', QueryOptions(limit=page_size, offset=next_page)) | 

## Args  
  
---  
  
`limit` |  The limit on number of documents to return in results.   
`number_found_accuracy` |  The minimum accuracy requirement for SearchResults.number_found. If set, the number_found will be accurate up to at least that number. For example, when set to 100, any SearchResults with number_found <= 100 is accurate. This option may add considerable latency/expense, especially when used with returned_fields.   
`cursor` |  A Cursor describing where to get the next set of results, or to provide next cursors in SearchResults.   
`offset` |  The offset is number of documents to skip in search results. This is an alternative to using a query cursor, but allows random access into the results. Using offsets rather than cursors are more expensive. You can only use either cursor or offset, but not both. Using an offset means that no cursor is returned in SearchResults.cursor, nor in each ScoredDocument.cursor.   
`sort_options` |  A SortOptions specifying a multi-dimensional sort over search results.   
`returned_fields` |  An iterable of names of fields to return in search results.   
`ids_only` |  Only return document ids, do not return any fields.   
`snippeted_fields` |  An iterable of names of fields to snippet and return in search result expressions.   
`returned_expressions` |  An iterable of FieldExpression to evaluate and return in search results.   
  
## Raises  
  
---  
  
`TypeError` |  If an unknown iterator_options or sort_options is passed.   
`ValueError` |  If ids_only and returned_fields are used together.   
`ExpressionError` |  If one of the returned expression strings is not parseable.   
  
## Attributes  
  
---  
  
`cursor` |  Returns the Cursor for the query.   
`ids_only` |  Returns whether to return only document ids in search results.   
`limit` |  Returns a limit on number of documents to return in results.   
`number_found_accuracy` |  Returns minimum accuracy requirement for SearchResults.number_found.   
`offset` |  Returns the number of documents in search results to skip.   
`returned_expressions` |  Returns iterable of FieldExpression to return in results.   
`returned_fields` |  Returns an iterable of names of fields to return in search results.   
`snippeted_fields` |  Returns iterable of field names to snippet and return in results.   
`sort_options` |  Returns a SortOptions.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
