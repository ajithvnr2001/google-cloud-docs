---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/SortOptions/
title: google.appengine.api.search.SortOptions \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:59:57.867736+00:00
---

# google.appengine.api.search.SortOptions  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/SortOptions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.search.SortOptions Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L2194-L2251) Represents a multi-dimensional sort of Documents. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.api.search.search.SortOptions`
    
    
    google.appengine.api.search.SortOptions(
        expressions=None, match_scorer=None, limit=1000
    )
    

The following code shows how to sort documents based on product rating in descending order and then cheapest product within similarly rated products, sorting at most 1000 documents: SortOptions(expressions=[ SortExpression(expression='rating', direction=SortExpression.DESCENDING, default_value=0), SortExpression(expression='price + tax', direction=SortExpression.ASCENDING, default_value=999999.99)], limit=1000) | 

## Args  
  
---  
  
`expressions` |  An iterable of SortExpression representing a multi-dimensional sort of Documents.   
`match_scorer` |  A match scorer specification which may be used to score documents or in a SortExpression combined with other features.   
`limit` |  The limit on the number of documents to score or sort.   
  
## Raises  
  
---  
  
`TypeError` |  If any of the parameters has an invalid type, or an unknown attribute is passed.   
`ValueError` |  If any of the parameters has an invalid value.   
  
## Attributes  
  
---  
  
`expressions` |  A list of SortExpression specifying a multi-dimensional sort.   
`limit` |  Returns the limit on the number of documents to score or sort.   
`match_scorer` |  Returns a match scorer to score documents with.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
