---
url: https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Internal.BooleanList
title: Interface Internal.BooleanList (3.19.4) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:49.777485+00:00
---

# Interface Internal.BooleanList (3.19.4)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Internal.BooleanList

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Internal.BooleanList (3.19.4) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public static interface Internal.BooleanList extends Internal.ProtobufList<Boolean>

A [java.util.List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html) implementation that avoids boxing the elements into Booleans if possible. Does not support null elements.

## Implements

com.google.protobuf.Internal.ProtobufList<java.lang.Boolean>

## Methods 

### addBoolean(boolean element)
    
    
    public abstract void addBoolean(boolean element)

Like #add(Object) but more efficient in that it doesn't box the element.

**Parameter**  
---  
**Name** | **Description**  
`element` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
  
### getBoolean(int index)
    
    
    public abstract boolean getBoolean(int index)

Like #get(int) but more efficient in that it doesn't box the returned value.

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### mutableCopyWithCapacity(int capacity)
    
    
    public abstract Internal.BooleanList mutableCopyWithCapacity(int capacity)

Returns a mutable clone of this list with the specified capacity.

**Parameter**  
---  
**Name** | **Description**  
`capacity` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Internal.BooleanList](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Internal.BooleanList)` |   
  
### setBoolean(int index, boolean element)
    
    
    public abstract boolean setBoolean(int index, boolean element)

Like #set(int, Object) but more efficient in that it doesn't box the element.

**Parameters**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
`element` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-30 UTC."],[],[]] 
