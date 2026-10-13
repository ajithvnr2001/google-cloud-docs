---
url: https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.FieldDescriptorProtoOrBuilder
title: Interface DescriptorProtos.FieldDescriptorProtoOrBuilder (3.19.4) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:01.741797+00:00
---

# Interface DescriptorProtos.FieldDescriptorProtoOrBuilder (3.19.4)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.FieldDescriptorProtoOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DescriptorProtos.FieldDescriptorProtoOrBuilder (3.19.4) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static interface DescriptorProtos.FieldDescriptorProtoOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder)

## Methods 

### getDefaultValue()
    
    
    public abstract String getDefaultValue()

For numeric types, contains the original text representation of the value. For booleans, "true" or "false". For strings, contains the default text contents (not escaped in any way). For bytes, contains the C escaped value. All bytes >= 128 are escaped. TODO(kenton): Base-64 encode?

`optional string default_value = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The defaultValue.  
  
### getDefaultValueBytes()
    
    
    public abstract ByteString getDefaultValueBytes()

For numeric types, contains the original text representation of the value. For booleans, "true" or "false". For strings, contains the default text contents (not escaped in any way). For bytes, contains the C escaped value. All bytes >= 128 are escaped. TODO(kenton): Base-64 encode?

`optional string default_value = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString)` | The bytes for defaultValue.  
  
### getExtendee()
    
    
    public abstract String getExtendee()

For extensions, this is the name of the type being extended. It is resolved in the same manner as type_name.

`optional string extendee = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The extendee.  
  
### getExtendeeBytes()
    
    
    public abstract ByteString getExtendeeBytes()

For extensions, this is the name of the type being extended. It is resolved in the same manner as type_name.

`optional string extendee = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString)` | The bytes for extendee.  
  
### getJsonName()
    
    
    public abstract String getJsonName()

JSON name of this field. The value is set by protocol compiler. If the user has set a "json_name" option on this field, that option's value will be used. Otherwise, it's deduced from the field's name by converting it to camelCase.

`optional string json_name = 10;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The jsonName.  
  
### getJsonNameBytes()
    
    
    public abstract ByteString getJsonNameBytes()

JSON name of this field. The value is set by protocol compiler. If the user has set a "json_name" option on this field, that option's value will be used. Otherwise, it's deduced from the field's name by converting it to camelCase.

`optional string json_name = 10;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString)` | The bytes for jsonName.  
  
### getLabel()
    
    
    public abstract DescriptorProtos.FieldDescriptorProto.Label getLabel()

`optional .google.protobuf.FieldDescriptorProto.Label label = 4;`

**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.FieldDescriptorProto.Label](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.FieldDescriptorProto.Label)` | The label.  
  
### getName()
    
    
    public abstract String getName()

`optional string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

`optional string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString)` | The bytes for name.  
  
### getNumber()
    
    
    public abstract int getNumber()

`optional int32 number = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The number.  
  
### getOneofIndex()
    
    
    public abstract int getOneofIndex()

If set, gives the index of a oneof in the containing type's oneof_decl list. This field is a member of that oneof.

`optional int32 oneof_index = 9;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The oneofIndex.  
  
### getOptions()
    
    
    public abstract DescriptorProtos.FieldOptions getOptions()

`optional .google.protobuf.FieldOptions options = 8;`

**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.FieldOptions](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.FieldOptions)` | The options.  
  
### getOptionsOrBuilder()
    
    
    public abstract DescriptorProtos.FieldOptionsOrBuilder getOptionsOrBuilder()

`optional .google.protobuf.FieldOptions options = 8;`

**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.FieldOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.FieldOptionsOrBuilder)` |   
  
### getProto3Optional()
    
    
    public abstract boolean getProto3Optional()

If true, this is a proto3 "optional". When a proto3 field is optional, it tracks presence regardless of field type. When proto3_optional is true, this field must be belong to a oneof to signal to old proto3 clients that presence is tracked for this field. This oneof is known as a "synthetic" oneof, and this field must be its sole member (each proto3 optional field gets its own synthetic oneof). Synthetic oneofs exist in the descriptor only, and do not generate any API. Synthetic oneofs must be ordered after all "real" oneofs. For message fields, proto3_optional doesn't create any semantic change, since non-repeated message fields always track presence. However it still indicates the semantic detail of whether the user wrote "optional" or not. This can be useful for round-tripping the .proto file. For consistency we give message fields a synthetic oneof also, even though it is not required to track presence. This is especially important because the parser can't tell if a field is a message or an enum, so it must always create a synthetic oneof. Proto2 optional fields do not set this flag, because they already indicate optional with `LABEL_OPTIONAL`.

`optional bool proto3_optional = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The proto3Optional.  
  
### getType()
    
    
    public abstract DescriptorProtos.FieldDescriptorProto.Type getType()

If type_name is set, this need not be set. If both this and type_name are set, this must be one of TYPE_ENUM, TYPE_MESSAGE or TYPE_GROUP.

`optional .google.protobuf.FieldDescriptorProto.Type type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[DescriptorProtos.FieldDescriptorProto.Type](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.DescriptorProtos.FieldDescriptorProto.Type)` | The type.  
  
### getTypeName()
    
    
    public abstract String getTypeName()

For message and enum types, this is the name of the type. If the name starts with a '.', it is fully-qualified. Otherwise, C++-like scoping rules are used to find the type (i.e. first the nested types within this message are searched, then within the parent, on up to the root namespace).

`optional string type_name = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The typeName.  
  
### getTypeNameBytes()
    
    
    public abstract ByteString getTypeNameBytes()

For message and enum types, this is the name of the type. If the name starts with a '.', it is fully-qualified. Otherwise, C++-like scoping rules are used to find the type (i.e. first the nested types within this message are searched, then within the parent, on up to the root namespace).

`optional string type_name = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString)` | The bytes for typeName.  
  
### hasDefaultValue()
    
    
    public abstract boolean hasDefaultValue()

For numeric types, contains the original text representation of the value. For booleans, "true" or "false". For strings, contains the default text contents (not escaped in any way). For bytes, contains the C escaped value. All bytes >= 128 are escaped. TODO(kenton): Base-64 encode?

`optional string default_value = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the defaultValue field is set.  
  
### hasExtendee()
    
    
    public abstract boolean hasExtendee()

For extensions, this is the name of the type being extended. It is resolved in the same manner as type_name.

`optional string extendee = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the extendee field is set.  
  
### hasJsonName()
    
    
    public abstract boolean hasJsonName()

JSON name of this field. The value is set by protocol compiler. If the user has set a "json_name" option on this field, that option's value will be used. Otherwise, it's deduced from the field's name by converting it to camelCase.

`optional string json_name = 10;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the jsonName field is set.  
  
### hasLabel()
    
    
    public abstract boolean hasLabel()

`optional .google.protobuf.FieldDescriptorProto.Label label = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the label field is set.  
  
### hasName()
    
    
    public abstract boolean hasName()

`optional string name = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the name field is set.  
  
### hasNumber()
    
    
    public abstract boolean hasNumber()

`optional int32 number = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the number field is set.  
  
### hasOneofIndex()
    
    
    public abstract boolean hasOneofIndex()

If set, gives the index of a oneof in the containing type's oneof_decl list. This field is a member of that oneof.

`optional int32 oneof_index = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the oneofIndex field is set.  
  
### hasOptions()
    
    
    public abstract boolean hasOptions()

`optional .google.protobuf.FieldOptions options = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the options field is set.  
  
### hasProto3Optional()
    
    
    public abstract boolean hasProto3Optional()

If true, this is a proto3 "optional". When a proto3 field is optional, it tracks presence regardless of field type. When proto3_optional is true, this field must be belong to a oneof to signal to old proto3 clients that presence is tracked for this field. This oneof is known as a "synthetic" oneof, and this field must be its sole member (each proto3 optional field gets its own synthetic oneof). Synthetic oneofs exist in the descriptor only, and do not generate any API. Synthetic oneofs must be ordered after all "real" oneofs. For message fields, proto3_optional doesn't create any semantic change, since non-repeated message fields always track presence. However it still indicates the semantic detail of whether the user wrote "optional" or not. This can be useful for round-tripping the .proto file. For consistency we give message fields a synthetic oneof also, even though it is not required to track presence. This is especially important because the parser can't tell if a field is a message or an enum, so it must always create a synthetic oneof. Proto2 optional fields do not set this flag, because they already indicate optional with `LABEL_OPTIONAL`.

`optional bool proto3_optional = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the proto3Optional field is set.  
  
### hasType()
    
    
    public abstract boolean hasType()

If type_name is set, this need not be set. If both this and type_name are set, this must be one of TYPE_ENUM, TYPE_MESSAGE or TYPE_GROUP.

`optional .google.protobuf.FieldDescriptorProto.Type type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the type field is set.  
  
### hasTypeName()
    
    
    public abstract boolean hasTypeName()

For message and enum types, this is the name of the type. If the name starts with a '.', it is fully-qualified. Otherwise, C++-like scoping rules are used to find the type (i.e. first the nested types within this message are searched, then within the parent, on up to the root namespace).

`optional string type_name = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the typeName field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
