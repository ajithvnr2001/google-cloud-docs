---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/facetrangeclass/
title: The FacetRange Class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:43:51.538094+00:00
---

# The FacetRange Class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/facetrangeclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The FacetRange Class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Class `FacetRange` represents a numeric range with inclusive start and exclusive end values.

`FacetRange` is defined in the module `google.appengine.api.search`.

## Constructor

The constructor for class `FacetRange` is defined as follows:

class FacetRange(start=None, end=None)

    

Construct an instance of class `FacetRefinement`.

    

Arguments

start
    Sets the start property
end
    Sets the end property

Result value

    

A new instance of class `FacetRange`.

Exceptions

TypeError
    

If any of the parameters have invalid types, or an unknown attribute is passed.

ValueError
    

If any of the parameters have invalid values.

## Properties

An instance of class `FacetRange` has the following properties:

start
    

Inclusive start of the range.

end
    

Exclusive end of the range.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
