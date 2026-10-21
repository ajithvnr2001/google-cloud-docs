---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/FieldExpression/
title: google.appengine.api.search.FieldExpression \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:22:30.562235+00:00
---

# google.appengine.api.search.FieldExpression  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/FieldExpression/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.search.FieldExpression Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L2135-L2185) Represents an expression that will be computed for each result returned. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.api.search.search.FieldExpression`
    
    
    google.appengine.api.search.FieldExpression(
        name, expression
    )
    

For example, FieldExpression(name='content_snippet', expression='snippet("very important", content)') means a computed field 'content_snippet' will be returned with each search result, which contains HTML snippets of the 'content' field which match the query 'very important'. | 

## Args  
  
---  
  
`name` |  The name of the computed field for the expression.   
`expression` |  The expression to evaluate and return in a field with given name in results. See https://developers.google.com/appengine/docs/python/search/overview#Expressions for a list of legal expressions.   
  
## Raises  
  
---  
  
`TypeError` |  If any of the parameters has an invalid type, or an unknown attribute is passed.   
`ValueError` |  If any of the parameters has an invalid value.   
`ExpressionError` |  If the expression string is not parseable.   
  
## Attributes  
  
---  
  
`expression` |  Returns a string containing an expression returned in search results.   
`name` |  Returns name of the expression to return in search results.   
  
## Class Variables  
  
---  
  
MAXIMUM_EXPRESSION_LENGTH |  `1000`  
MAXIMUM_OPERATOR_LENGTH |  `100`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
