---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Attribute
title: Class Attribute (0.7.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:29:29.277526+00:00
---

# Class Attribute (0.7.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Attribute

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Attribute (0.7.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.1 (latest)  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.7 
    
    
    Attribute(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An attribute in the API Hub. An attribute is a name value pair which can be attached to different resources in the API hub based on the scope of the attribute. Attributes can either be pre-defined by the API Hub or created by users.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The name of the attribute in the API Hub. Format: `projects/{project}/locations/{location}/attributes/{attribute}`  
`display_name` |  `str`   
Required. The display name of the attribute.   
`description` |  `str`   
Optional. The description of the attribute.   
`definition_type` |  `[google.cloud.apihub_v1.types.Attribute.DefinitionType](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Attribute.DefinitionType)`   
Output only. The definition type of the attribute.   
`scope` |  `[google.cloud.apihub_v1.types.Attribute.Scope](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Attribute.Scope)`   
Required. The scope of the attribute. It represents the resource in the API Hub to which the attribute can be linked.   
`data_type` |  `[google.cloud.apihub_v1.types.Attribute.DataType](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Attribute.DataType)`   
Required. The type of the data of the attribute.   
`allowed_values` |  `MutableSequence[[google.cloud.apihub_v1.types.Attribute.AllowedValue](https://docs.cloud.google.com/python/docs/reference/google-cloud-apihub/latest/google.cloud.apihub_v1.types.Attribute.AllowedValue)]`   
Optional. The list of allowed values when the attribute value is of type enum. This is required when the data_type of the attribute is ENUM. The maximum number of allowed values of an attribute will be 1000.   
`cardinality` |  `int`   
Optional. The maximum number of values that the attribute can have when associated with an API Hub resource. Cardinality 1 would represent a single-valued attribute. It must not be less than 1 or greater than 20. If not specified, the cardinality would be set to 1 by default and represent a single-valued attribute.   
`mandatory` |  `bool`   
Output only. When mandatory is true, the attribute is mandatory for the resource specified in the scope. Only System defined attributes can be mandatory.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time at which the attribute was created.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time at which the attribute was last updated.   
  
## Classes 

### AllowedValue
    
    
    AllowedValue(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The value that can be assigned to the attribute when the data type is enum.

### DataType
    
    
    DataType(value)

Enumeration of attribute's data type.

### DefinitionType
    
    
    DefinitionType(value)

Enumeration of attribute definition types.

### Scope
    
    
    Scope(value)

Enumeration for the scope of the attribute representing the resource in the API Hub to which the attribute can be linked.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
