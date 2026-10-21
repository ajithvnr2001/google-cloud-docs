---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor/
title: Tensor \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:04:49.901847+00:00
---

# Tensor  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Tensor Stay organized with collections  Save and categorize content based on your preferences. 

A tensor value type.

Fields  
  
`dtype` `enum (`[DataType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor#DataType)`)` The data type of tensor. | `shape[]` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Shape of the tensor. | `boolVal[]` `boolean` type specific representations that make it easy to create tensor protos in all languages. Only the representation corresponding to "dtype" can be set. The values hold the flattened representation of the tensor in row major order.`[BOOL](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor#DataType.ENUM_VALUES.BOOL)` | `stringVal[]` `string` `[STRING](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor#DataType.ENUM_VALUES.STRING)` | `bytesVal[]` `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` `[STRING](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor#DataType.ENUM_VALUES.STRING)`A base64-encoded string. | `floatVal[]` `number` `[FLOAT](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor#DataType.ENUM_VALUES.FLOAT)` | `doubleVal[]` `number` `[DOUBLE](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor#DataType.ENUM_VALUES.DOUBLE)` | `intVal[]` `integer` `[INT_8](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor#DataType.ENUM_VALUES.INT8)` `[INT_16](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor#DataType.ENUM_VALUES.INT16)` `[INT_32](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor#DataType.ENUM_VALUES.INT32)` | `int64Val[]` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` `[INT64](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor#DataType.ENUM_VALUES.INT64)` | `uintVal[]` `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` `[UINT8](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor#DataType.ENUM_VALUES.UINT8)` `[UINT16](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor#DataType.ENUM_VALUES.UINT16)` `[UINT32](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor#DataType.ENUM_VALUES.UINT32)` | `uint64Val[]` `string` `[UINT64](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor#DataType.ENUM_VALUES.UINT64)` | `listVal[]` `object (`[Tensor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor)`)` A list of tensor values. | `structVal` `map (key: string, value: object (`[Tensor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor)`))` A map of string to tensor. | `tensorVal` `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Serialized raw tensor content.A base64-encoded string. | JSON representation  
---  
      
    
    {
      "dtype": enum ([DataType](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor#DataType)),
      "shape": [
        string
      ],
      "boolVal": [
        boolean
      ],
      "stringVal": [
        string
      ],
      "bytesVal": [
        string
      ],
      "floatVal": [
        number
      ],
      "doubleVal": [
        number
      ],
      "intVal": [
        integer
      ],
      "int64Val": [
        string
      ],
      "uintVal": [
        integer
      ],
      "uint64Val": [
        string
      ],
      "listVal": [
        {
          object ([Tensor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor))
        }
      ],
      "structVal": {
        string: {
          object ([Tensor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/Tensor))
        },
        ...
      },
      "tensorVal": string
    }  
  
## DataType

data type of the tensor.

Enums  
---  
`DATA_TYPE_UNSPECIFIED` | Not a legal value for datatype. Used to indicate a datatype field has not been set.  
`BOOL` | data types that all computation devices are expected to be capable to support.  
`STRING` |   
`FLOAT` |   
`DOUBLE` |   
`INT8` |   
`INT16` |   
`INT32` |   
`INT64` |   
`UINT8` |   
`UINT16` |   
`UINT32` |   
`UINT64` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-06 UTC."],[],[]] 
