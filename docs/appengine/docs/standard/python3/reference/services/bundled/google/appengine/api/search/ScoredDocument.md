---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/ScoredDocument/
title: google.appengine.api.search.ScoredDocument \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:32:20.646960+00:00
---

# google.appengine.api.search.ScoredDocument  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/ScoredDocument/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.search.ScoredDocument Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L2549-L2648) Represents a scored document returned from a search. Inherits From: [`Document`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/Document), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.api.search.search.ScoredDocument`
    
    
    google.appengine.api.search.ScoredDocument(
        doc_id=None,
        fields=None,
        language='en',
        sort_scores=None,
        expressions=None,
        cursor=None,
        rank=None,
        facets=None
    )
    

| 

## Args  
  
---  
  
`doc_id` |  The visible printable ASCII string identifying the document which does not start with '!'. Whitespace is excluded from ids. If no id is provided, the search service will provide one.   
`fields` |  An iterable of Field instances representing the content of the document.   
`language` |  The code of the language used in the field values.   
`sort_scores` |  The list of scores assigned during sort evaluation. Each sort dimension is included. Positive scores are used for ascending sorts; negative scores for descending.   
`expressions` |  The list of computed fields which are the result of expressions requested.   
`cursor` |  A cursor associated with the document.   
`rank` |  The rank of this document. A rank must be a non-negative integer less than sys.maxint. If not specified, the number of seconds since 1st Jan 2011 is used. Documents are returned in descending order of their rank.   
`facets` |  An iterable of Facet instances representing the facets for this document.   
  
## Raises  
  
---  
  
`TypeError` |  If any of the parameters have invalid types, or an unknown attribute is passed.   
`ValueError` |  If any of the parameters have invalid values.   
  
## Attributes  
  
---  
  
`cursor` |  A cursor associated with a result, a continued search starting point. To get this cursor to appear, set the Index.cursor_type to Index.RESULT_CURSOR, otherwise this will be None.   
`doc_id` |  Returns the document identifier.   
`expressions` |  The list of computed fields the result of expression evaluation. For example, if a request has FieldExpression(name='snippet', 'snippet("good story", content)') meaning to compute a snippet field containing HTML snippets extracted from the matching of the query 'good story' on the field 'content'. This means a field such as the following will be returned in expressions for the search result: HtmlField(name='snippet', value='that was a **good story** to finish')   
`facets` |  Returns a list of facets of the document.   
`fields` |  Returns a list of fields of the document.   
`language` |  Returns the code of the language the document fields are written in.   
`rank` |  Returns the rank of this document.   
`sort_scores` |  Deprecated: the list of scores assigned during sort evaluation. The right way to retrieve a score is to use '_score' in a FieldExpression.   
  
## Methods

### `facet`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L2003-L2012)
    
    
    facet(
        facet_name
    )
    

Returns list of facets with the provided name.

Args  
---  
  
`facet_name` |  The name of the facet to return.   
  
Returns  
---  
A list of facets with the given name.   
  
### `field`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L1984-L2001)
    
    
    field(
        field_name
    )
    

Returns the field with the provided field name.

Args  
---  
  
`field_name` |  The name of the field to return.   
  
Returns  
---  
A field with the given name.   
  
Raises  
---  
  
`ValueError` |  There is not exactly one field with the given name.   
  
### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L2070-L2073)
    
    
    __eq__(
        other
    )
    

Return self==value.

### `__getitem__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L2018-L2028)
    
    
    __getitem__(
        field_name
    )
    

Returns a list of all fields with the provided field name.

Args  
---  
  
`field_name` |  The name of the field to return.   
  
Returns  
---  
All fields with the given name, or an empty list if no field with that name exists.   
  
### `__iter__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L2030-L2035)
    
    
    __iter__()
    

Documents do not support iteration.

This is provided to raise an explicit exception.

### `__ne__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L2075-L2076)
    
    
    __ne__(
        other
    )
    

Return self!=value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
