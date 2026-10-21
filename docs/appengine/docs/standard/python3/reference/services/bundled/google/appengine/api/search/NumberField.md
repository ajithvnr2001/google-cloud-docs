---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/NumberField/
title: google.appengine.api.search.NumberField \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:47:00.208224+00:00
---

# google.appengine.api.search.NumberField  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/NumberField/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.search.NumberField Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L1677-L1707) A Field that has a numeric value. Inherits From: [`Field`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/Field), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.api.search.search.NumberField`
    
    
    google.appengine.api.search.NumberField(
        name, value=None
    )
    

The following example shows a number field named size: NumberField(name='size', value=10) | 

## Args  
  
---  
  
`name` |  The name of the field.   
`value` |  A numeric value.   
  
## Raises  
  
---  
  
`TypeError` |  If value is not numeric.   
`ValueError` |  If value is out of range.   
  
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
