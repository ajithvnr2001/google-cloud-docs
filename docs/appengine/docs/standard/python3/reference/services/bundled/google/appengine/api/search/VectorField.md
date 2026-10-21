---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/VectorField/
title: google.appengine.api.search.VectorField \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:54:30.035259+00:00
---

# google.appengine.api.search.VectorField  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/VectorField/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.search.VectorField Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L1559-L1587) A vector field that can be used in a dot product expression. Inherits From: [`Field`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/Field), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.api.search.search.VectorField`
    
    
    google.appengine.api.search.VectorField(
        name, value=None
    )
    

The following example shows a vector field named scores: VectorField(name='scores', value=[1, 2, 3]) That can be used in a sort/field expression like this: dot(scores, vector(3, 2, 1)) | 

## Args  
  
---  
  
`name` |  The name of the field.   
`value` |  The vector field value.   
  
## Raises  
  
---  
  
`TypeError` |  If vector elements are not numbers.   
`ValueError` |  If value elements are not finite numbers.   
  
## Attributes  
  
---  
  
`language` |  Returns the code of the language the content in value is written in.   
`name` |  Returns the name of the field.   
`value` |  Returns the value of the field.   
  
## Methods

### `__eq__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L1043-L1044)
    
    
    __eq__(
        other
    )
    

Return self==value.

### `__ne__`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L1046-L1047)
    
    
    __ne__(
        other
    )
    

Return self!=value.

## Class Variables  
  
---  
  
ATOM |  `'ATOM'`  
DATE |  `'DATE'`  
GEO_POINT |  `'GEO_POINT'`  
HTML |  `'HTML'`  
NUMBER |  `'NUMBER'`  
TEXT |  `'TEXT'`  
TOKENIZED_PREFIX |  `'TOKENIZED_PREFIX'`  
UNTOKENIZED_PREFIX |  `'UNTOKENIZED_PREFIX'`  
VECTOR |  `'VECTOR'`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
