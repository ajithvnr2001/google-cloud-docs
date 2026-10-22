---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/sortexpressionclass/
title: The SortExpression Class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:48.578293+00:00
---

# The SortExpression Class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/sortexpressionclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The SortExpression Class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Class `SortExpression` allows you to customize how your search results are sorted.

`SortExpression` is defined in the `google.appengine.api.search` module.

## Constructor

The constructor for class `SortExpression` is defined as follows:

class SortExpression(expression=None, direction=DESCENDING, default_value=None) 
    

Sort results by the specified scoring expression. 

    

Arguments

expression
    

An expression to be evaluated when sorting results for each matching document. The expression can simply be a field name, or some compound expression such as `_score + count(likes) * 0.1` which will add the score from a scorer to a count of the values of a `likes` field weighted by a factor of 0.1.

direction
    

The direction to sort the search results, either ASCENDING or DESCENDING.

default_value
    

The default value of the expression, if no field is present and cannot be calculated for a document. A text value must be specified for text sorts. A numeric value must be specified for numeric sorts.

Result value

    

A new instance of class `SortExpression`.

Exceptions

TypeError
    

If any of the parameters have an invalid type, or an unknown attribute is passed.

ValueError
    

If any parameter has an invalid value.

## Properties

An instance of class `SortExpression` has the following properties:

expression
    

Returns the expression used to sort matched results.

direction
    

Returns the direction of sort expression: `ASCENDING` or `DESCENDING`.

default_value
    

Returns a default value for the expression if no other value could be computed.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
