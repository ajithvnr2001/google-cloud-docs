---
url: https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TextFormatParseInfoTree
title: Class TextFormatParseInfoTree (3.19.4) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:44:37.053568+00:00
---

# Class TextFormatParseInfoTree (3.19.4)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TextFormatParseInfoTree

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class TextFormatParseInfoTree (3.19.4) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public class TextFormatParseInfoTree

Data structure which is populated with the locations of each field value parsed from the text.

The locations of primary fields values are retrieved by `getLocation` or ` getLocations`. The locations of sub message values are within nested ` TextFormatParseInfoTree`s and are retrieve by `getNestedTree` or `getNestedTrees`.

The `TextFormatParseInfoTree` is created by a Builder.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > TextFormatParseInfoTree

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Methods 

### builder()
    
    
    public static TextFormatParseInfoTree.Builder builder()

Create a builder for a `ParseInfoTree`.

**Returns**  
---  
**Type** | **Description**  
`[TextFormatParseInfoTree.Builder](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TextFormatParseInfoTree.Builder)` | the builder  
  
## Methods 

### getLocation(Descriptors.FieldDescriptor fieldDescriptor, int index)
    
    
    public TextFormatParseLocation getLocation(Descriptors.FieldDescriptor fieldDescriptor, int index)

Get the location in the source of a field's value.

Returns the [TextFormatParseLocation](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TextFormatParseLocation) for index-th value of the field in the parsed text.

**Parameters**  
---  
**Name** | **Description**  
`fieldDescriptor` | `[Descriptors.FieldDescriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor)`  
the [FieldDescriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor) of the desired field  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the index of the value.  
**Returns**  
---  
**Type** | **Description**  
`[TextFormatParseLocation](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TextFormatParseLocation)` | the [TextFormatParseLocation](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TextFormatParseLocation) of the value  
  
### getLocations(Descriptors.FieldDescriptor fieldDescriptor)
    
    
    public List<TextFormatParseLocation> getLocations(Descriptors.FieldDescriptor fieldDescriptor)

Retrieve all the locations of a field.

**Parameter**  
---  
**Name** | **Description**  
`fieldDescriptor` | `[Descriptors.FieldDescriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor)`  
the [FieldDescriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor) of the desired field  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TextFormatParseLocation](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TextFormatParseLocation)>` | a list of the locations of values of the field. If there are not values or the field doesn't exist, an empty list is returned.  
  
### getNestedTree(Descriptors.FieldDescriptor fieldDescriptor, int index)
    
    
    public TextFormatParseInfoTree getNestedTree(Descriptors.FieldDescriptor fieldDescriptor, int index)

Returns the parse info tree for the given field, which must be a message type.

**Parameters**  
---  
**Name** | **Description**  
`fieldDescriptor` | `[Descriptors.FieldDescriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor)`  
the [FieldDescriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor) of the desired sub message  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the index of message value.  
**Returns**  
---  
**Type** | **Description**  
`[TextFormatParseInfoTree](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TextFormatParseInfoTree)` | the `ParseInfoTree` of the message value. `null` is returned if the field doesn't exist or the index is out of range.  
  
### getNestedTrees(Descriptors.FieldDescriptor fieldDescriptor)
    
    
    public List<TextFormatParseInfoTree> getNestedTrees(Descriptors.FieldDescriptor fieldDescriptor)

Retrieve a list of all the location information trees for a sub message field.

**Parameter**  
---  
**Name** | **Description**  
`fieldDescriptor` | `[Descriptors.FieldDescriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor)`  
the [FieldDescriptor](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Descriptors.FieldDescriptor) of the desired field  
**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[TextFormatParseInfoTree](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TextFormatParseInfoTree)>` | A list of [TextFormatParseInfoTree](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TextFormatParseInfoTree)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
