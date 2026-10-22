---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/facetrefinementclass/
title: The FacetRefinement Class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:53:40.837241+00:00
---

# The FacetRefinement Class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/facetrefinementclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The FacetRefinement Class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Class `FacetRefinement` is used to narrow search results based on a facet value.

The recommended way to use facet refinement is to use its token string. Each FacetResult will have a token that is acceptable instead of this class. To provide manual FacetRefinement, an instance of this class can be passed to SearchOptions.

`FacetRefinement` is defined in the module `google.appengine.api.search`.

## Constructor

The constructor for class `FacetRefinement` is defined as follows:

class FacetRefinement(name, value=None, facet_range=None)

    

Construct an instance of class `FacetRefinement`.

NOTE: Either the value or the facet_range should be set but not both.

    

Arguments

name
    

Sets the name property

value
    

Sets the value property

facet_range
    

Sets the facet_range property

Result value

    

A new instance of class `FacetRefinement`.

Exceptions

TypeError
    

If any of the parameters have invalid types, or an unknown attribute is passed.

ValueError
    

If any of the parameters have invalid values.

## Properties

An instance of class `FacetRefinement` has the following properties:

name
    

name of the facet refinement.

value
    

string value of the facet refinement.

range
    

numeric range of the facet refinement.

## Instance Methods

Instances of class `FacetRefinement` have the following methods:

ToTokenString()
    

Converts this refinement to a token string safe to be used in HTML. The format of this string may change.

    

Result value

    

A token string safe to be used in HTML for this facet refinement.

FromTokenString()
    

This static method converts a token string to a FacetRefinement object. Do not store token strings between different versions of API as key could be incompatible.

    

Arguments

token_string
    

A token string created by ToTokenString method or returned by a search result.

Result value

    

A FacetRefinement object.

Exceptions

ValueError
    

If the token_string is invalid.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
