---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/facetresultclass/
title: The FacetResult Class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:50.744445+00:00
---

# The FacetResult Class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/facetresultclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The FacetResult Class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Class `FacetResult` Represents a facet result returned from a search with faceted search.

`FacetResult` is defined in the module `google.appengine.api.search`.

## Constructor

The constructor for class `FacetResult` is defined as follows:

class FacetResult(name, values=None)

    

Construct an instance of class `FacetRefinement`.

    

Arguments

name
    Sets the name property
values
    Sets the values property

Result value

    

A new instance of class `FacetResult`.

Exceptions

TypeError
    

If any of the parameters have invalid types, or an unknown attribute is passed.

ValueError
    

If any of the parameters have invalid values.

## Properties

An instance of class `FacetResult` has the following properties:

name
    

The name of this facet result.

values
    

The values for this facet result.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
