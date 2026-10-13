---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.FunctionOrBuilder
title: Interface FunctionOrBuilder (3.49.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:42:40.244349+00:00
---

# Interface FunctionOrBuilder (3.49.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.FunctionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface FunctionOrBuilder (3.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.49.0 (latest)  3.45.0  3.44.0  3.43.1  3.41.0  3.38.0  3.37.0  3.36.0  3.35.1  3.33.4  3.32.2  3.31.9  3.30.11  3.28.0  3.27.2  3.26.5  3.25.1  3.24.3  3.22.0  3.21.4  3.20.0  3.17.0  3.16.3  3.15.7  3.14.4  3.13.2  3.12.1  3.11.0  3.10.0  3.9.6  3.8.2  3.7.10  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.1.0  3.0.21 
    
    
    public interface FunctionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsOptions(String key)
    
    
    public abstract boolean containsOptions(String key)

Optional. Optional named arguments that certain functions may support.

` map<string, .google.firestore.v1.Value> options = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getArgs(int index)
    
    
    public abstract Value getArgs(int index)

Optional. Ordered list of arguments the given function expects.

`repeated .google.firestore.v1.Value args = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.Value)` |   
  
### getArgsCount()
    
    
    public abstract int getArgsCount()

Optional. Ordered list of arguments the given function expects.

`repeated .google.firestore.v1.Value args = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getArgsList()
    
    
    public abstract List<Value> getArgsList()

Optional. Ordered list of arguments the given function expects.

`repeated .google.firestore.v1.Value args = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.Value)>` |   
  
### getArgsOrBuilder(int index)
    
    
    public abstract ValueOrBuilder getArgsOrBuilder(int index)

Optional. Ordered list of arguments the given function expects.

`repeated .google.firestore.v1.Value args = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.ValueOrBuilder)` |   
  
### getArgsOrBuilderList()
    
    
    public abstract List<? extends ValueOrBuilder> getArgsOrBuilderList()

Optional. Ordered list of arguments the given function expects.

`repeated .google.firestore.v1.Value args = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.firestore.v1.ValueOrBuilder>` |   
  
### getName()
    
    
    public abstract String getName()

Required. The name of the function to evaluate.

**Requires:**

  * must be in snake case (lower case with underscore separator).



`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Required. The name of the function to evaluate.

**Requires:**

  * must be in snake case (lower case with underscore separator).



`string name = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getOptions() (deprecated)
    
    
    public abstract Map<String,Value> getOptions()

Use [#getOptionsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.FunctionOrBuilder#com_google_firestore_v1_FunctionOrBuilder_getOptionsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.Value)>` |   
  
### getOptionsCount()
    
    
    public abstract int getOptionsCount()

Optional. Optional named arguments that certain functions may support.

` map<string, .google.firestore.v1.Value> options = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getOptionsMap()
    
    
    public abstract Map<String,Value> getOptionsMap()

Optional. Optional named arguments that certain functions may support.

` map<string, .google.firestore.v1.Value> options = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.Value)>` |   
  
### getOptionsOrDefault(String key, Value defaultValue)
    
    
    public abstract Value getOptionsOrDefault(String key, Value defaultValue)

Optional. Optional named arguments that certain functions may support.

` map<string, .google.firestore.v1.Value> options = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.Value)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.Value)` |   
  
### getOptionsOrThrow(String key)
    
    
    public abstract Value getOptionsOrThrow(String key)

Optional. Optional named arguments that certain functions may support.

` map<string, .google.firestore.v1.Value> options = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Value](https://docs.cloud.google.com/java/docs/reference/google-cloud-firestore/latest/com.google.firestore.v1.Value)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
