---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/sortoptionsclass/
title: The SortOptions Class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:48.521565+00:00
---

# The SortOptions Class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/sortoptionsclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The SortOptions Class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Class `SortExpression` represents a multi-dimensional sort of Documents.

The following code shows how to sort documents based on product rating in descending order and then cheapest product within similarly rated products, sorting at most 1000 documents:
    
    
         SortOptions(expressions=[
             SortExpression(expression='rating',
                 direction=SortExpression.DESCENDING, default_value=0),
             SortExpression(expression='price + tax',
                 direction=SortExpression.ASCENDING, default_value=999999.99)],
             limit=1000)

`SortOptions` is defined in the `google.appengine.api.search` module.

## Constructor

The constructor for class `SortOptions` is defined as follows:

class SortOptions(expressions=None, match_scorer=None, limit=1000) 
    

Sort documents according to the specified options. 

    

Arguments

expressions
    

An iterable of SortExpression representing a multi-dimensional sort of Documents.

match_scorer
    

A match scorer specification which may be used to score documents or in a SortExpression combined with other features.

limit
    

The limit on the number of documents to score. It is advisable to set this limit on large indexes.

Result value

    

A new instance of class `SortOptions`.

Exceptions

TypeError
    

If any of the parameters have an invalid type, or an unknown attribute is passed.

ValueError
    

If any parameter has an invalid value.

## Properties

An instance of class `SortOptions` has the following properties:

expressions
    

Returns a list of SortExpression specifying a multi-dimensional sort.

match_scorer
    

Returns a match scorer used to score documents.

limit
    

Returns the limit on the number of documents to score.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
