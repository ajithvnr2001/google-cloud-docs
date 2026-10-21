---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/UntokenizedPrefixField/
title: google.appengine.api.search.UntokenizedPrefixField \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:46:13.428766+00:00
---

# google.appengine.api.search.UntokenizedPrefixField  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/UntokenizedPrefixField/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.search.UntokenizedPrefixField Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L1590-L1616) A field that matches searches on prefixes of the whole field. Inherits From: [`Field`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/Field), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.api.search.search.UntokenizedPrefixField`
    
    
    google.appengine.api.search.UntokenizedPrefixField(
        name, value=None, language=None
    )
    

The following example shows an untokenized prefix field named title: UntokenizedPrefixField(name='title', value='how to swim freestyle') | 

## Args  
  
---  
  
`name` |  The name of the field.   
`value` |  The untokenized prefix field value.   
`language` |  The code of the language the value is encoded in.   
  
## Raises  
  
---  
  
`TypeError` |  If value is not a string.   
`ValueError` |  If value is longer than allowed.   
  
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
