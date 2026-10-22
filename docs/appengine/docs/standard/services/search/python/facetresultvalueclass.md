---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/facetresultvalueclass/
title: The FacetResultValue Class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:50.661215+00:00
---

# The FacetResultValue Class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/facetresultvalueclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The FacetResultValue Class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Class `FacetResultValue` Represents a facet value as part of search result.

`FacetResultValue` is defined in the module `google.appengine.api.search`.

## Constructor

The constructor for class `FacetResultValue` is defined as follows:

class FacetResultValue(label, count, refinement)

    

Construct an instance of class `FacetRefinement`.

    

Arguments

label
    Sets the label property
count
    Sets the count property
refinement
    Sets the refinement property

Result value

    

A new instance of class `FacetResultValue`.

Exceptions

TypeError
    

If any of the parameters have invalid types, or an unknown attribute is passed.

ValueError
    

If any of the parameters have invalid values.

## Properties

An instance of class `FacetResultValue` has the following properties:

label
    

The label for this facet value. For an atom facet, the label is the facet's string value, For numeric facet values, it's a string representing the value range.

count
    

The number of documents (in the current query results) that match this FacetResultValue.

refinement_token
    

The FacetRefinement object for this FacetResultValue. Passing this object or its string token to the next query will refine the result based on this facet value.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
