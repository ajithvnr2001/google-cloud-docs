---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.ValueOrBuilder
title: Interface ValueOrBuilder (0.22.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:24.864427+00:00
---

# Interface ValueOrBuilder (0.22.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.ValueOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ValueOrBuilder (0.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.0 (latest)  0.18.0  0.17.0  0.16.0  0.14.0  0.11.0  0.10.0  0.8.0  0.6.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface ValueOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBoolValue()
    
    
    public abstract boolean getBoolValue()

`bool bool_value = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The boolValue.  
  
### getDoubleValue()
    
    
    public abstract double getDoubleValue()

`double double_value = 3;`

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The doubleValue.  
  
### getInt64Value()
    
    
    public abstract long getInt64Value()

`int64 int64_value = 1;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The int64Value.  
  
### getStringValue()
    
    
    public abstract String getStringValue()

`string string_value = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The stringValue.  
  
### getStringValueBytes()
    
    
    public abstract ByteString getStringValueBytes()

`string string_value = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for stringValue.  
  
### getValueCase()
    
    
    public abstract Value.ValueCase getValueCase()

**Returns**  
---  
**Type** | **Description**  
`[Value.ValueCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-capacityplanner/latest/com.google.cloud.capacityplanner.v1beta.Value.ValueCase)` |   
  
### hasBoolValue()
    
    
    public abstract boolean hasBoolValue()

`bool bool_value = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the boolValue field is set.  
  
### hasDoubleValue()
    
    
    public abstract boolean hasDoubleValue()

`double double_value = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the doubleValue field is set.  
  
### hasInt64Value()
    
    
    public abstract boolean hasInt64Value()

`int64 int64_value = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the int64Value field is set.  
  
### hasStringValue()
    
    
    public abstract boolean hasStringValue()

`string string_value = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the stringValue field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
