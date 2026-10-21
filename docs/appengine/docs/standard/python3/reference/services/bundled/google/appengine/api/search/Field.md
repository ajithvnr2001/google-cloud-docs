---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/Field/
title: google.appengine.api.search.Field \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:36:06.004347+00:00
---

# google.appengine.api.search.Field  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/search/Field/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.search.Field Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/search/search.py#L976-L1060) An abstract base class which represents a field of a document. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)

#### View aliases

**Main aliases** `google.appengine.api.search.search.Field`
    
    
    google.appengine.api.search.Field(
        name, value, language=None
    )
    

This class should not be directly instantiated. | 

## Args  
  
---  
  
`name` |  The name of the field. Field names must have maximum length MAXIMUM_FIELD_NAME_LENGTH and match pattern "[A-Za-z][A-Za-z0-9_]*".   
`value` |  The value of the field which can be a str, unicode or date.   
`language` |  The ISO 693-1 two letter code of the language used in the value. See http://www.sil.org/iso639-3/codes.asp?order=639_1&letter=%25 for a list of valid codes. Correct specification of language code will assist in correct tokenization of the field. If None is given, then the language code of the document will be used.   
  
## Raises  
  
---  
  
`TypeError` |  If any of the parameters have invalid types, or an unknown attribute is passed.   
`ValueError` |  If any of the parameters have invalid values.   
  
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
