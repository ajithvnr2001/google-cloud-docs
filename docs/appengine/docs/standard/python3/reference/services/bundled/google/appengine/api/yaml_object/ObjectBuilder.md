---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_object/ObjectBuilder/
title: google.appengine.api.yaml_object.ObjectBuilder \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:09.423766+00:00
---

# google.appengine.api.yaml_object.ObjectBuilder  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_object/ObjectBuilder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.yaml_object.ObjectBuilder Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_object.py#L93-L282) Builder used for constructing validated objects. Inherits From: [`Builder`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_builder/Builder), [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type)
    
    
    google.appengine.api.yaml_object.ObjectBuilder(
        default_class
    )
    

Given a class that implements [`validation.ValidatedBase`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/ValidatedBase), it will parse a YAML document and attempt to build an instance of the class. `ObjectBuilder` will only map YAML fields that are accepted by the `ValidatedBase`'s `GetValidator` function. Lists are mapped to validated. Repeated attributes and maps are mapped to `validated.Type` properties. For a YAML map to be compatible with a class, the class must have a constructor that can be called with no parameters. If the provided type does not have such a constructor a parse time error will occur. The constructor initializes the validated object builder. | 

## Args  
  
---  
  
`default_class` |  Class that is instantiated upon the detection of a new document. An instance of this class will act as the document itself.   
  
## Methods

### `AppendTo`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_object.py#L269-L282)
    
    
    AppendTo(
        subject, value
    )
    

Append a value to a sequence.

Args  
---  
  
`subject` |  `_ObjectSequence` that is receiving new value.   
`value` |  Value that is being appended to sequence.   
  
### `BuildDocument`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_object.py#L135-L141)
    
    
    BuildDocument()
    

Instantiate new root validated object.

Returns  
---  
New instance of validated object.   
  
### `BuildMapping`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_object.py#L143-L157)
    
    
    BuildMapping(
        top_value
    )
    

New instance of object mapper for opening map scope.

Args  
---  
  
`top_value` |  Parent of nested object.   
  
Returns  
---  
New instance of object mapper.   
  
### `BuildSequence`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_object.py#L191-L200)
    
    
    BuildSequence(
        top_value
    )
    

New instance of object sequence.

Args  
---  
  
`top_value` |  Object that contains the new sequence.   
  
Returns  
---  
A new `_ObjectSequencer` instance.   
  
### `EndMapping`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_object.py#L159-L189)
    
    
    EndMapping(
        top_value, mapping
    )
    

When leaving scope, ensures the new object is initialized.

This method is mainly for picking up on any missing required attributes.

Args  
---  
  
`top_value` |  Parent of closing mapping object.   
`mapping` |  `_ObjectMapper` instance that is leaving scope.   
  
### `EndSequence`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_builder.py#L128-L137)
    
    
    EndSequence(
        top_value, sequence
    )
    

Previously constructed sequence scope is at an end.

Called when the end of a sequence block is encountered. Useful for additional clean up or end of scope validation.

Args  
---  
  
`top_value` |  Value which is the parent of the sequence.   
`sequence` |  Sequence which is at the end of its scope.   
  
### `InitializeDocument`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_builder.py#L74-L86)
    
    
    InitializeDocument(
        document, value
    )
    

Initializes document with a value from the top level of a YAML document.

This method is called when the root document element is encountered at the top level of a YAML document. It should get called immediately after `BuildDocument`.

Receiving the `None` value indicates the empty document.

Args  
---  
  
`document` |  Document as constructed in `BuildDocument`.   
`value` |  Scalar value to initialize the document with.   
  
### `MapTo`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_object.py#L202-L267)
    
    
    MapTo(
        subject, key, value
    )
    

Maps key-value pair to an objects attribute.

Args  
---  
  
`subject` |  `_ObjectMapper` of object that will receive new attribute.   
`key` |  Key of attribute.   
`value` |  Value of new attribute.   
  
Raises  
---  
`UnexpectedAttribute` when the key is not a validated attribute of the subject value class.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
