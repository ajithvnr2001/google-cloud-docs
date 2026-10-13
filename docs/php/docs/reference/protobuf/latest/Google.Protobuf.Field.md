---
url: https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Field
title: proto library Client - Class Field (v5.36.2) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:06.651594+00:00
---

# proto library Client - Class Field (v5.36.2)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Field

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  proto library Client - Class Field (v5.36.2) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the proto library Client class Field.

A single field of a message type.

New usages of this message as an alternative to FieldDescriptorProto are strongly discouraged. This message does not reliability preserve all information necessary to model the schema and preserve semantics. Instead make use of FileDescriptorSet which preserves the necessary information.

Generated from protobuf message `google.protobuf.Field`

## Namespace

Google \ Protobuf

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ kind` |  `int`   
The field type.  
`↳ cardinality` |  `int`   
The field cardinality.  
`↳ number` |  `int`   
The field number.  
`↳ name` |  `string`   
The field name.  
`↳ type_url` |  `string`   
The field type URL, without the scheme, for message or enumeration types. Example: `"type.googleapis.com/google.protobuf.Timestamp"`.  
`↳ oneof_index` |  `int`   
The index of the field type in `Type.oneofs`, for message or enumeration types. The first type has index 1; zero means the type is not in the list.  
`↳ packed` |  `bool`   
Whether to use alternative packed wire representation.  
`↳ options` |  `array<[Option](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Option)>`   
The protocol buffer options.  
`↳ json_name` |  `string`   
The field JSON name.  
`↳ default_value` |  `string`   
The string value of the default value of this field. Proto2 syntax only.  
  
### getKind

The field type.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [Kind](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Field.Kind). one of the values in {@see \Google\Protobuf\Field\Kind}  
  
### setKind

The field type.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [Kind](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Field.Kind). one of the values in [Field\Kind](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Field.Kind)  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCardinality

The field cardinality.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [Cardinality](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Field.Cardinality). one of the values in {@see \Google\Protobuf\Field\Cardinality}  
  
### setCardinality

The field cardinality.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [Cardinality](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Field.Cardinality). one of the values in [Field\Cardinality](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Field.Cardinality)  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getNumber

The field number.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setNumber

The field number.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getName

The field name.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

The field name.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTypeUrl

The field type URL, without the scheme, for message or enumeration types. Example: `"type.googleapis.com/google.protobuf.Timestamp"`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setTypeUrl

The field type URL, without the scheme, for message or enumeration types. Example: `"type.googleapis.com/google.protobuf.Timestamp"`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOneofIndex

The index of the field type in `Type.oneofs`, for message or enumeration types. The first type has index 1; zero means the type is not in the list.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setOneofIndex

The index of the field type in `Type.oneofs`, for message or enumeration types. The first type has index 1; zero means the type is not in the list.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPacked

Whether to use alternative packed wire representation.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setPacked

Whether to use alternative packed wire representation.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOptions

The protocol buffer options.

**Returns**  
---  
**Type** | **Description**  
`[RepeatedField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.RepeatedField)<[Option](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Option)>` |   
  
### setOptions

The protocol buffer options.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[Option](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Option)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getJsonName

The field JSON name.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setJsonName

The field JSON name.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDefaultValue

The string value of the default value of this field. Proto2 syntax only.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDefaultValue

The string value of the default value of this field. Proto2 syntax only.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
