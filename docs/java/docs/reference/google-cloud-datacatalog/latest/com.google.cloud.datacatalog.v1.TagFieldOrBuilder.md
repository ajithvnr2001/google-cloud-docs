---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagFieldOrBuilder
title: Interface TagFieldOrBuilder (1.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:42:48.784759+00:00
---

# Interface TagFieldOrBuilder (1.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagFieldOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TagFieldOrBuilder (1.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.101.0 (latest)  1.100.0  1.99.0  1.97.0  1.94.0  1.93.0  1.91.0  1.89.0  1.88.0  1.87.0  1.86.0  1.84.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.76.0  1.74.0  1.73.0  1.70.0  1.69.0  1.68.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.60.0  1.59.0  1.58.0  1.57.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.5  1.8.4  1.7.2  1.6.2  1.5.4 
    
    
    public interface TagFieldOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBoolValue()
    
    
    public abstract boolean getBoolValue()

The value of a tag field with a boolean type.

`bool bool_value = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The boolValue.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Output only. The display name of this field.

`string display_name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Output only. The display name of this field.

`string display_name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getDoubleValue()
    
    
    public abstract double getDoubleValue()

The value of a tag field with a double type.

`double double_value = 2;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The doubleValue.  
  
### getEnumValue()
    
    
    public abstract TagField.EnumValue getEnumValue()

The value of a tag field with an enum type.

This value must be one of the allowed values listed in this enum.

`.google.cloud.datacatalog.v1.TagField.EnumValue enum_value = 6;`

**Returns**  
---  
**Type** | **Description**  
`[TagField.EnumValue](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagField.EnumValue)` | The enumValue.  
  
### getEnumValueOrBuilder()
    
    
    public abstract TagField.EnumValueOrBuilder getEnumValueOrBuilder()

The value of a tag field with an enum type.

This value must be one of the allowed values listed in this enum.

`.google.cloud.datacatalog.v1.TagField.EnumValue enum_value = 6;`

**Returns**  
---  
**Type** | **Description**  
`[TagField.EnumValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagField.EnumValueOrBuilder)` |   
  
### getKindCase()
    
    
    public abstract TagField.KindCase getKindCase()

**Returns**  
---  
**Type** | **Description**  
`[TagField.KindCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-datacatalog/latest/com.google.cloud.datacatalog.v1.TagField.KindCase)` |   
  
### getOrder()
    
    
    public abstract int getOrder()

Output only. The order of this field with respect to other fields in this tag. Can be set by Tag.

For example, a higher value can indicate a more important field. The value can be negative. Multiple fields can have the same order, and field orders within a tag don't have to be sequential.

`int32 order = 7 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The order.  
  
### getRichtextValue()
    
    
    public abstract String getRichtextValue()

The value of a tag field with a rich text type.

The maximum length is 10 MiB as this value holds HTML descriptions including encoded images. The maximum length of the text without images is 100 KiB.

`string richtext_value = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The richtextValue.  
  
### getRichtextValueBytes()
    
    
    public abstract ByteString getRichtextValueBytes()

The value of a tag field with a rich text type.

The maximum length is 10 MiB as this value holds HTML descriptions including encoded images. The maximum length of the text without images is 100 KiB.

`string richtext_value = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for richtextValue.  
  
### getStringValue()
    
    
    public abstract String getStringValue()

The value of a tag field with a string type.

The maximum length is 2000 UTF-8 characters.

`string string_value = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The stringValue.  
  
### getStringValueBytes()
    
    
    public abstract ByteString getStringValueBytes()

The value of a tag field with a string type.

The maximum length is 2000 UTF-8 characters.

`string string_value = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for stringValue.  
  
### getTimestampValue()
    
    
    public abstract Timestamp getTimestampValue()

The value of a tag field with a timestamp type.

`.google.protobuf.Timestamp timestamp_value = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The timestampValue.  
  
### getTimestampValueOrBuilder()
    
    
    public abstract TimestampOrBuilder getTimestampValueOrBuilder()

The value of a tag field with a timestamp type.

`.google.protobuf.Timestamp timestamp_value = 5;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasBoolValue()
    
    
    public abstract boolean hasBoolValue()

The value of a tag field with a boolean type.

`bool bool_value = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the boolValue field is set.  
  
### hasDoubleValue()
    
    
    public abstract boolean hasDoubleValue()

The value of a tag field with a double type.

`double double_value = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the doubleValue field is set.  
  
### hasEnumValue()
    
    
    public abstract boolean hasEnumValue()

The value of a tag field with an enum type.

This value must be one of the allowed values listed in this enum.

`.google.cloud.datacatalog.v1.TagField.EnumValue enum_value = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the enumValue field is set.  
  
### hasRichtextValue()
    
    
    public abstract boolean hasRichtextValue()

The value of a tag field with a rich text type.

The maximum length is 10 MiB as this value holds HTML descriptions including encoded images. The maximum length of the text without images is 100 KiB.

`string richtext_value = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the richtextValue field is set.  
  
### hasStringValue()
    
    
    public abstract boolean hasStringValue()

The value of a tag field with a string type.

The maximum length is 2000 UTF-8 characters.

`string string_value = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the stringValue field is set.  
  
### hasTimestampValue()
    
    
    public abstract boolean hasTimestampValue()

The value of a tag field with a timestamp type.

`.google.protobuf.Timestamp timestamp_value = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the timestampValue field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-04 UTC."],[],[]] 
