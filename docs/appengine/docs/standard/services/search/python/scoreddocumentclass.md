---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/scoreddocumentclass/
title: class ScoredDocument \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:24:24.113913+00:00
---

# class ScoredDocument  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/scoreddocumentclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  class ScoredDocument Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Class `ScoredDocument` represents a scored document returned from a search. You do not build this class explicitly; rather, it is returned as a result of `[Index.search()](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/indexclass)`.

`ScoredDocument` is defined in the `google.appengine.api.search` module.

## Constructor

The constructor for class `MatchScorer` is defined as follows:

class ScoredDocument(doc_id=None, fields=None, language='en', sort_scores=None, expressions=None, cursor=None, rank=None)
    

Represents a scored document returned from a search.

    

Arguments

doc_id
    

The visible, printable ASCII string identifying the document. Must not begin with '!'. Whitespace is excluded from ids. If no id is provided, the search service will provide one.

fields
    

An iterable of Field instances representing the content of the document.

language
    

The two-letter [ISO 639.2 language code](http://www.loc.gov/standards/iso639-2/php/code_list.php) of the language used in the field values.

sort_scores
    

The list of scores assigned during sort evaluation. Each sort dimension is included. Positive scores are used for ascending sorts; negative scores for descending.

expressions
    

The list of computed fields which are the result of expressions requested.

cursor
    

A cursor associated with the document.

rank
    

The document rank is used to specify the order this document will be returned in search results, where 0 <= rank <= sys.maxint. If not specified, the number of seconds since 1st Jan 2011 is used. Documents are returned in descending order of the order ID.

Result value

    

A new instance of class `ScoredDocument`.

Exceptions

TypeError
    

If any of the parameters have an invalid type, or an unknown attribute is passed.

ValueError
    

If any parameter has an invalid value.

## Properties

An instance of class `ScoredDocument` has the following properties:

sort_scores
    

Returns the list of scores assigned while the API is sorting the results of a search. Each sort dimension is included. Positive scores are used for ascending sorts and negative scores for descending.

expressions
    

The list of computed fields the result of expression evaluation. For example, the following [field expression](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/fieldexpressionclass) seeks to compute a snippet field containing HTML snippets extracted from the matching of the query `'good story'` in the `content` field: 
    
    
    FieldExpression(name='snippet', 'snippet("good story", content)')

Given this query, the API would return the following `ScoredDocument.expression`: 
    
    
    HtmlField(name='snippet', value='that was a **good story** to finish')

cursor
    

A cursor associated with a result used as a starting point from which to return the next set of search results. This property will not return unless you set the `Index.cursor_type` to `Index.RESULT_CURSOR`; otherwise the property returns be `None`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
