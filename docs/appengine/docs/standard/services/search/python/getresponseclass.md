---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/getresponseclass/
title: The GetResponse Class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:26:35.653914+00:00
---

# The GetResponse Class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/getresponseclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The GetResponse Class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Class `GetResponse` represents the results of methods invoked to return information about documents and indexes. 

`GetResponse` is defined in the module `google.appengine.api.search`.

## Introduction

A `GetResponse` object is returned from a call to either [index.get_range()](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/indexclass#Index_get_range) or [search.get_indexes()](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/functions#get_indexes). You can iterate over an instance of `GetResponse`, which will return the members of its results property. The contents of the property are determined by the type of call that created the instance of `GetResponse`.

For example, the following code shows how `GetResponse` could be used to determine which documents were successfully deleted. In this case the iteration returns [Documents](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/documentclass).
    
    
    response = index.get_range()
    for document in response:
        print "document ", document

## Constructor

The constructor for class `GetResponse` is defined as follows:

class GetResponse(results=None) 
    

Construct an instance of class `GetResponse`.

    

**Argument**

results
    

Initial value of its `results` property.

Result value

    

A new instance of class `GetResponse`.

Exceptions

TypeError
    

A parameter has an invalid type, or an unknown attribute was passed.

ValueError
    

A parameter has an invalid value.

## Properties

An instance of class `GetResponse` has the following property:

results
    

A list of results, whose type depends on the call that returns the object. If returning from a call to [get_range()](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/indexclass#Index_get_range), `results` is a list of [Documents](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/documentclass) in descending order of their identifiers. If returning from a call to [search.get_indexes()](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/functions#get_indexes), `results` is a list of [Indexes](https://docs.cloud.google.com/appengine/docs/standard/services/search/python/indexclass). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
