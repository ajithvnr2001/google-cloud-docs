---
url: https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.FieldDescriptorProto
title: proto library Client - Class FieldDescriptorProto (v5.36.2) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:37.603710+00:00
---

# proto library Client - Class FieldDescriptorProto (v5.36.2)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.FieldDescriptorProto

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  proto library Client - Class FieldDescriptorProto (v5.36.2) Stay organized with collections  Save and categorize content based on your preferences. 

Reference documentation and code samples for the proto library Client class FieldDescriptorProto.

Describes a field within a message.

Generated from protobuf message `google.protobuf.FieldDescriptorProto`

## Namespace

Google \ Protobuf \ Internal

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ name` |  `string`   
  
`↳ number` |  `int`   
  
`↳ label` |  `int`   
  
`↳ type` |  `int`   
If type_name is set, this need not be set. If both this and type_name are set, this must be one of TYPE_ENUM, TYPE_MESSAGE or TYPE_GROUP.  
`↳ type_name` |  `string`   
For message and enum types, this is the name of the type. If the name starts with a '.', it is fully-qualified. Otherwise, C++-like scoping rules are used to find the type (i.e. first the nested types within this message are searched, then within the parent, on up to the root namespace).  
`↳ extendee` |  `string`   
For extensions, this is the name of the type being extended. It is resolved in the same manner as type_name.  
`↳ default_value` |  `string`   
For numeric types, contains the original text representation of the value. For booleans, "true" or "false". For strings, contains the default text contents (not escaped in any way). For bytes, contains the C escaped value. All bytes >= 128 are escaped.  
`↳ oneof_index` |  `int`   
If set, gives the index of a oneof in the containing type's oneof_decl list. This field is a member of that oneof.  
`↳ json_name` |  `string`   
JSON name of this field. The value is set by protocol compiler. If the user has set a "json_name" option on this field, that option's value will be used. Otherwise, it's deduced from the field's name by converting it to camelCase.  
`↳ options` |  `[FieldOptions](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.FieldOptions)`   
  
`↳ proto3_optional` |  `bool`   
If true, this is a proto3 "optional". When a proto3 field is optional, it tracks presence regardless of field type. When proto3_optional is true, this field must belong to a oneof to signal to old proto3 clients that presence is tracked for this field. This oneof is known as a "synthetic" oneof, and this field must be its sole member (each proto3 optional field gets its own synthetic oneof). Synthetic oneofs exist in the descriptor only, and do not generate any API. Synthetic oneofs must be ordered after all "real" oneofs. For message fields, proto3_optional doesn't create any semantic change, since non-repeated message fields always track presence. However it still indicates the semantic detail of whether the user wrote "optional" or not. This can be useful for round-tripping the .proto file. For consistency we give message fields a synthetic oneof also, even though it is not required to track presence. This is especially important because the parser can't tell if a field is a message or an enum, so it must always create a synthetic oneof. Proto2 optional fields do not set this flag, because they already indicate optional with `LABEL_OPTIONAL`.  
  
### getName

Generated from protobuf field `optional string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasName

### clearName

### setName

Generated from protobuf field `optional string name = 1;`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getNumber

Generated from protobuf field `optional int32 number = 3;`

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### hasNumber

### clearNumber

### setNumber

Generated from protobuf field `optional int32 number = 3;`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLabel

Generated from protobuf field `optional .google.protobuf.FieldDescriptorProto.Label label = 4;`

**Returns**  
---  
**Type** | **Description**  
`int` | one of the values in {@see \Google\Protobuf\Internal\FieldDescriptorProto\Label}  
  
### hasLabel

### clearLabel

### setLabel

Generated from protobuf field `optional .google.protobuf.FieldDescriptorProto.Label label = 4;`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
one of the values in [FieldDescriptorProto\Label](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.FieldDescriptorProto.Label)  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getType

If type_name is set, this need not be set. If both this and type_name are set, this must be one of TYPE_ENUM, TYPE_MESSAGE or TYPE_GROUP.

**Returns**  
---  
**Type** | **Description**  
`int` | one of the values in {@see \Google\Protobuf\Internal\FieldDescriptorProto\Type}  
  
### hasType

### clearType

### setType

If type_name is set, this need not be set. If both this and type_name are set, this must be one of TYPE_ENUM, TYPE_MESSAGE or TYPE_GROUP.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
one of the values in [FieldDescriptorProto\Type](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.FieldDescriptorProto.Type)  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTypeName

For message and enum types, this is the name of the type. If the name starts with a '.', it is fully-qualified. Otherwise, C++-like scoping rules are used to find the type (i.e. first the nested types within this message are searched, then within the parent, on up to the root namespace).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasTypeName

### clearTypeName

### setTypeName

For message and enum types, this is the name of the type. If the name starts with a '.', it is fully-qualified. Otherwise, C++-like scoping rules are used to find the type (i.e. first the nested types within this message are searched, then within the parent, on up to the root namespace).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getExtendee

For extensions, this is the name of the type being extended. It is resolved in the same manner as type_name.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasExtendee

### clearExtendee

### setExtendee

For extensions, this is the name of the type being extended. It is resolved in the same manner as type_name.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDefaultValue

For numeric types, contains the original text representation of the value.

For booleans, "true" or "false". For strings, contains the default text contents (not escaped in any way). For bytes, contains the C escaped value. All bytes >= 128 are escaped.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasDefaultValue

### clearDefaultValue

### setDefaultValue

For numeric types, contains the original text representation of the value.

For booleans, "true" or "false". For strings, contains the default text contents (not escaped in any way). For bytes, contains the C escaped value. All bytes >= 128 are escaped.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOneofIndex

If set, gives the index of a oneof in the containing type's oneof_decl list. This field is a member of that oneof.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### hasOneofIndex

### clearOneofIndex

### setOneofIndex

If set, gives the index of a oneof in the containing type's oneof_decl list. This field is a member of that oneof.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getJsonName

JSON name of this field. The value is set by protocol compiler. If the user has set a "json_name" option on this field, that option's value will be used. Otherwise, it's deduced from the field's name by converting it to camelCase.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### hasJsonName

### clearJsonName

### setJsonName

JSON name of this field. The value is set by protocol compiler. If the user has set a "json_name" option on this field, that option's value will be used. Otherwise, it's deduced from the field's name by converting it to camelCase.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOptions

Generated from protobuf field `optional .google.protobuf.FieldOptions options = 8;`

**Returns**  
---  
**Type** | **Description**  
`[FieldOptions](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.FieldOptions)|null` |   
  
### hasOptions

### clearOptions

### setOptions

Generated from protobuf field `optional .google.protobuf.FieldOptions options = 8;`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[FieldOptions](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.FieldOptions)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getProto3Optional

If true, this is a proto3 "optional". When a proto3 field is optional, it tracks presence regardless of field type.

When proto3_optional is true, this field must belong to a oneof to signal to old proto3 clients that presence is tracked for this field. This oneof is known as a "synthetic" oneof, and this field must be its sole member (each proto3 optional field gets its own synthetic oneof). Synthetic oneofs exist in the descriptor only, and do not generate any API. Synthetic oneofs must be ordered after all "real" oneofs. For message fields, proto3_optional doesn't create any semantic change, since non-repeated message fields always track presence. However it still indicates the semantic detail of whether the user wrote "optional" or not. This can be useful for round-tripping the .proto file. For consistency we give message fields a synthetic oneof also, even though it is not required to track presence. This is especially important because the parser can't tell if a field is a message or an enum, so it must always create a synthetic oneof. Proto2 optional fields do not set this flag, because they already indicate optional with `LABEL_OPTIONAL`.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### hasProto3Optional

### clearProto3Optional

### setProto3Optional

If true, this is a proto3 "optional". When a proto3 field is optional, it tracks presence regardless of field type.

When proto3_optional is true, this field must belong to a oneof to signal to old proto3 clients that presence is tracked for this field. This oneof is known as a "synthetic" oneof, and this field must be its sole member (each proto3 optional field gets its own synthetic oneof). Synthetic oneofs exist in the descriptor only, and do not generate any API. Synthetic oneofs must be ordered after all "real" oneofs. For message fields, proto3_optional doesn't create any semantic change, since non-repeated message fields always track presence. However it still indicates the semantic detail of whether the user wrote "optional" or not. This can be useful for round-tripping the .proto file. For consistency we give message fields a synthetic oneof also, even though it is not required to track presence. This is especially important because the parser can't tell if a field is a message or an enum, so it must always create a synthetic oneof. Proto2 optional fields do not set this flag, because they already indicate optional with `LABEL_OPTIONAL`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
