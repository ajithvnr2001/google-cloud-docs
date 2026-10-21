---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/facetoptionsclass/
title: The FacetOptions Class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:20:30.550421+00:00
---

# The FacetOptions Class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/facetoptionsclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The FacetOptions Class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Class `FacetOptions` provides options for processing facet results of a query.

`FacetOptions` is defined in the `google.appengine.api.search` module.

## Introduction

Class `FacetOptions` provides options for processing facet results of a query. Options include number of facets to discover, number of values for each facet and the depth of the result to be considered for facet computation.

## Constructor

The constructor for class `FacetOptions` is defined as follows:

facet_option = FacetOptions(discovery_limit=5, discovery_value_limit=None, depth=None)

    

Specify options for processing facet results of a query.

    

Arguments

discovery_limit
discovery_value_limit
depth

Result value

    

A new instance of class `FacetOptions`.

Exceptions

TypeError
    

If an unknown attribute is passed.

ValueError
    

If any of the parameters have invalid values (e.g., a negative depth).

## Properties

An instance of class `FacetOptions` has the following properties:

discovery_limit
    

Number of facets to discover if facet discovery is turned on. If None, discover facets will be disabled.

discovery_value_limit
    

Number of values to be discovered for each of the top discovered facets.

depth
    

Number of documents in query results to evaluate to gather facet information.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
