---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/SortExpression/
title: google.appengine.api.search.SortExpression \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:25:43.210547+00:00
---

# google.appengine.api.search.SortExpression  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/SortExpression/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.search.SortExpression Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L2362-L2468) Sort by a user specified scoring expression. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.api.search.search.SortExpression`
    
    
    google.appengine.api.search.SortExpression(
        expression, direction=DESCENDING, default_value=None
    )
    

For example, the following will sort documents on a numeric field named 'length' in ascending order, assigning a default value of sys.maxint for documents which do not specify a 'length' field. SortExpression(expression='length', direction=sort.SortExpression.ASCENDING, default_value=sys.maxint) The following example will sort documents on a date field named 'published_date' in descending order, assigning a default value of 1999-12-31 for documents which do not specify a 'published_date' field. SortExpression(expression='published_date', default_value=datetime.date(year=1999, month=12, day=31)) The following example will sort documents on a text field named 'subject' in descending order, assigning a default value of '' for documents which do not specify a 'subject' field. SortExpression(expression='subject') | 

## Args  
  
---  
  
`expression` |  An expression to be evaluated on each matching document to sort by. The expression must evaluate to a text or numeric value. The expression can simply be a field name, or some compound expression such as "_score + count(likes) * 0.1" which will add the score from a scorer to a count of the values of a likes field times 0.1. See https://developers.google.com/appengine/docs/python/search/overview#Expressions for a list of legal expressions.   
`direction` |  The direction to sort the search results, either ASCENDING or DESCENDING   
`default_value` |  The default value of the expression. The default_value is returned if expression cannot be calculated, for example, if the expression is a field name and no value for that named field exists. A text value must be specified for text sorts. A numeric value must be specified for numeric sorts. A date value must be specified for date sorts.   
  
## Raises  
  
---  
  
`TypeError` |  If any of the parameters has an invalid type, or an unknown attribute is passed.   
`ValueError` |  If any of the parameters has an invalid value.   
`ExpressionError` |  If the expression string is not parseable.   
  
## Attributes  
  
---  
  
`default_value` |  Returns a default value for the expression if no value computed.   
`direction` |  Returns the direction to sort expression: ASCENDING or DESCENDING.   
`expression` |  Returns the expression to sort by.   
  
## Class Variables  
  
---  
  
ASCENDING |  `'ASCENDING'`  
DESCENDING |  `'DESCENDING'`  
MAX_FIELD_VALUE |  `'\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff\U0010ffff'`  
MIN_FIELD_VALUE |  `''`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
