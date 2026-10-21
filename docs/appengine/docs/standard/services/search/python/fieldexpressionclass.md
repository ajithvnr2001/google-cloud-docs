---
url: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/fieldexpressionclass/
title: The FieldExpression Class \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:47:55.169915+00:00
---

# The FieldExpression Class  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/services/search/python/fieldexpressionclass/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  The FieldExpression Class Stay organized with collections  Save and categorize content based on your preferences. 

Go Java PHP Python

Class `FieldExpression` allows you to compute customized content snippets for each result returned by a search.

`FieldExpression` is defined in the module `google.appengine.api.search`.

## Constructor

The constructor for class `FieldExpression` is defined as follows:

class FieldExpression(name, expression)

    

Construct an instance of class `FieldExpression`.

For example,
    
    
    FieldExpression(name='content_snippet',
                    expression='snippet("very important", content)')

constructs a field expression that returns a computed field named `content-snippet` with each search result, containing HTML snippets of the `content` field that match the query `"very` `important"`.

    

Arguments

name
    

Name of computed field.

expression
    

Expression to evaluate and return.

Result value

    

A new instance of class `FieldExpression`.

Exceptions

TypeError
    

A parameter has an invalid type, or an unknown attribute was passed.

ValueError
    

A parameter has an invalid value.

## Properties

An instance of class `FieldExpression` has the following properties:

name
    

Name of computed field.

expression
    

String containing expression to evaluate and return.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
