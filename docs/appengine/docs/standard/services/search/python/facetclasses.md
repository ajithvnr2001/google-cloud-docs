---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/facetclasses/
title: Facet Classes \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:53:41.998855+00:00
---

# Facet Classes  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/facetclasses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Facet Classes Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Class `Facet` is an abstract base class representing a facet of a document. This class should not be directly instantiated.

`Facet` is defined in the module `google.appengine.api.search`.

## Properties

An instance of class `Facet` has the following properties:

name
    

The name of the facet. Facet names must have maximum length MAXIMUM_FIELD_NAME_LENGTH and match pattern "[A-Za-z][A-Za- z0-9_]*".

value
    

The value of the facet which can be a str, unicode or number.

## Subclasses

Class `Facet` has the following subclasses:

class AtomFacet
    

A Facet that has content to be treated as a single token for indexing.

The facet's value is a str or unicode object to be treated as an indivisible text value. The following example shows an atom facet named wine_type:
    
    
    AtomFacet(name='wine_type', value='Red')

    

Exceptions

TypeError
    

Value supplied is not a text string.

ValueError
    

Value exceeds maximum allowable length.

class NumberFacet
    

A Facet that has a numeric value.

The following example shows a number facet named wine_vintage:
    
    
    NumberFacet(name='wine_vintage', value=2000)

    

Exceptions

TypeError
    

Value supplied is not numeric.

ValueError
    

Value is out of range.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
