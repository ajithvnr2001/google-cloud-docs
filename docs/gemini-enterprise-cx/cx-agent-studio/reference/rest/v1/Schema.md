---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Schema/
title: Schema \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:40.193039+00:00
---

# Schema  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Schema Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Schema.Type



Represents a select subset of an OpenAPI 3.0 schema object.

JSON representation  
---  
      
    
    {
      "type": enum ([Schema.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Schema#Schema.Type)),
      "properties": {
        string: {
          object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Schema))
        },
        ...
      },
      "required": [
        string
      ],
      "description": string,
      "items": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Schema))
      },
      "nullable": boolean,
      "uniqueItems": boolean,
      "prefixItems": [
        {
          object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Schema))
        }
      ],
      "additionalProperties": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Schema))
      },
      "anyOf": [
        {
          object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Schema))
        }
      ],
      "enum": [
        string
      ],
      "default": value,
      "ref": string,
      "defs": {
        string: {
          object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Schema))
        },
        ...
      },
      "title": string,
      "minItems": string,
      "maxItems": string,
      "minimum": number,
      "maximum": number
    }  
  
Fields  
---  
`type` |  `enum (`[Schema.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Schema#Schema.Type)`)` Required. The type of the data.  
`properties` |  `map (key: string, value: object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Schema)`))` Optional. Properties of Type.OBJECT.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`required[]` |  `string` Optional. Required properties of Type.OBJECT.  
`description` |  `string` Optional. The description of the data.  
`items` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Schema)`)` Optional. Schema of the elements of Type.ARRAY.  
`nullable` |  `boolean` Optional. Indicates if the value may be null.  
`uniqueItems` |  `boolean` Optional. Indicate the items in the array must be unique. Only applies to TYPE.ARRAY.  
`prefixItems[]` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Schema)`)` Optional. Schemas of initial elements of Type.ARRAY.  
`additionalProperties` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Schema)`)` Optional. Can either be a boolean or an object, controls the presence of additional properties.  
`anyOf[]` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Schema)`)` Optional. The value should be validated against any (one or more) of the subschemas in the list.  
`enum[]` |  `string` Optional. Possible values of the element of primitive type with enum format. Examples: 1. We can define direction as : {type:STRING, format:enum, enum:["EAST", NORTH", "SOUTH", "WEST"]} 2. We can define apartment number as : {type:INTEGER, format:enum, enum:["101", "201", "301"]}  
`default` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Optional. Default value of the data.  
`ref` |  `string` Optional. Allows indirect references between schema nodes. The value should be a valid reference to a child of the root `defs`.For example, the following schema defines a reference to a schema node named "Pet":
    
    
    type: object
    properties:
      pet:
        ref: #/defs/Pet
    defs:
      Pet:
        type: object
        properties:
          name:
            type: string
    

The value of the "pet" property is a reference to the schema node named "Pet". See details in <https://json-schema.org/understanding-json-schema/structuring>.  
`defs` |  `map (key: string, value: object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Schema)`))` Optional. A map of definitions for use by `ref`. Only allowed at the root of the schema.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`title` |  `string` Optional. The title of the schema.  
`minItems` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Minimum number of the elements for Type.ARRAY.  
`maxItems` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Maximum number of the elements for Type.ARRAY.  
`minimum` |  `number` Optional. Minimum value for Type.INTEGER and Type.NUMBER.  
`maximum` |  `number` Optional. Maximum value for Type.INTEGER and Type.NUMBER.  
  
## Schema.Type

OpenAPI data types.

Enums  
---  
`TYPE_UNSPECIFIED` | Type unspecified.  
`STRING` | String type.  
`INTEGER` | Integer type.  
`NUMBER` | Number type.  
`BOOLEAN` | Boolean type.  
`OBJECT` | Object type.  
`ARRAY` | Array type.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-01 UTC."],[],[]] 
