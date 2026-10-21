---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/SearchResults/
title: google.appengine.api.search.SearchResults \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:36:18.881782+00:00
---

# google.appengine.api.search.SearchResults  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/SearchResults/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.search.SearchResults Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L2651-L2727) Represents the result of executing a search request. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.api.search.search.SearchResults`
    
    
    google.appengine.api.search.SearchResults(
        number_found, results=None, cursor=None, facets=None
    )
    

| 

## Args  
  
---  
  
`number_found` |  The number of documents found for the query.   
`results` |  The list of ScoredDocuments returned from executing a search request.   
`cursor` |  A Cursor to continue the search from the end of the search results.   
`facets` |  The list of FacetResults returned from executing a search request with faceted search enabled.   
  
## Raises  
  
---  
  
`TypeError` |  If any of the parameters have an invalid type, or an unknown attribute is passed.   
`ValueError` |  If any of the parameters have an invalid value.   
  
## Attributes  
  
---  
  
`cursor` |  Returns a cursor that can be used to continue search from last result. This corresponds to using a ResultsCursor in QueryOptions, otherwise this will be None.   
`facets` |  Return the list of FacetResults that found in matched documents.   
`number_found` |  Returns the number of documents which were found for the search. Note that this is an approximation and not an exact count. If QueryOptions.number_found_accuracy parameter is set to 100 for example, then number_found <= 100 is accurate.   
`results` |  Returns the list of ScoredDocuments that matched the query.   
  
## Methods

### `__iter__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L2679-L2682)
    
    
    __iter__()
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
