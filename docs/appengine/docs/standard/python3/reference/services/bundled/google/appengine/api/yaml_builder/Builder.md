---
url: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_builder/Builder/
title: google.appengine.api.yaml_builder.Builder \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:55:04.508978+00:00
---

# google.appengine.api.yaml_builder.Builder  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_builder/Builder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  google.appengine.api.yaml_builder.Builder Stay organized with collections  Save and categorize content based on your preferences. 

[ ![](https://www.tensorflow.org/images/GitHub-Mark-32px.png) View source on GitHub ](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_builder.py#L52-L160) Interface for building documents and type from YAML events. Inherits From: [`expected_type`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/validation/Validator/expected_type) Implement this interface to create a new builder. Builders are passed to the `BuilderHandler` and used as a factory and assembler for creating concrete representations of YAML files.

## Methods

### `AppendTo`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_builder.py#L151-L160)
    
    
    AppendTo(
        subject, value
    )
    

Append value to a sequence representation. Implementation is defined by sub-class of `Builder`. | Args  
---  
  
`subject` |  Object that represents sequence. Value returned from BuildSequence   
`value` |  Value to be appended to a subject. Can be any kind of value.   
  
### `BuildDocument`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_builder.py#L60-L72)
    
    
    BuildDocument()
    

Builds a new document.

The object built by this method becomes the top level entity that the builder handler constructs. The actual type is determined by the sub-class of the `Builder` class and can essentially be any type at all. This method is always called when the parser encounters the start of a new document.

Returns  
---  
New object instance representing concrete document which is returned to user via [`BuilderHandler.GetResults()`](https://docs.cloud.google.com/appengine/docs/standard/python3/reference/services/bundled/google/appengine/api/yaml_builder/BuilderHandler#GetResults).   
  
### `BuildMapping`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_builder.py#L88-L100)
    
    
    BuildMapping(
        top_value
    )
    

Builds a new mapping representation.

Called when the `StartMapping` event is received. The type of object is determined by the `Builder` sub-class.

Args  
---  
  
`top_value` |  Object that will be the new mapping parent. This object is returned from previous call to `BuildMapping` or `BuildSequence`.   
  
Returns  
---  
Instance of the new object that represents a mapping type in target model.   
  
### `BuildSequence`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_builder.py#L113-L126)
    
    
    BuildSequence(
        top_value
    )
    

Builds a new sequence representation.

Called when the `StartSequence` event is received. The type of object is determined by the `Builder` sub-class.

Args  
---  
  
`top_value` |  The object that will be the new sequences parent. The object will be returned from previous call to `BuildMapping` or `BuildSequence`.   
  
Returns  
---  
Instance of new object that represents a sequence type in target model.   
  
### `EndMapping`

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_builder.py#L102-L111)
    
    
    EndMapping(
        top_value, mapping
    )
    

Previously constructed mapping scope is at an end.

Called when the end of a mapping block is encountered. This is useful for additional clean up or end-of-scope validation.

Args  
---  
  
`top_value` |  Value which is the parent of the mapping.   
`mapping` |  Mapping which is at the end of its scope.   
  
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

[View source](https://github.com/GoogleCloudPlatform/appengine-python-standard/tree/main/src/google/appengine/api/yaml_builder.py#L139-L149)
    
    
    MapTo(
        subject, key, value
    )
    

Maps value to a mapping representation.

Implementation is defined by the sub-class of `Builder`.

Args  
---  
  
`subject` |  Object that represents mapping. Value returned from `BuildMapping`.   
`key` |  Key used to map value to subject. Can be any scalar value.   
`value` |  Value which is mapped to subject. Can be any kind of value.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-16 UTC."],[],[]] 
