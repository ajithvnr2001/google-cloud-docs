---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-infra-manager/latest/com.google.cloud.config.v1.PropertyChangeOrBuilder
title: Interface PropertyChangeOrBuilder (0.76.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:19.529684+00:00
---

# Interface PropertyChangeOrBuilder (0.76.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-infra-manager/latest/com.google.cloud.config.v1.PropertyChangeOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PropertyChangeOrBuilder (0.76.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.76.0 (latest)  0.72.0  0.71.0  0.70.0  0.68.0  0.65.0  0.64.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.55.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.47.0  0.45.0  0.44.0  0.41.0  0.40.0  0.39.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.1.0 
    
    
    public interface PropertyChangeOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAfter()
    
    
    public abstract Value getAfter()

Output only. Representations of the object value after the actions.

`.google.protobuf.Value after = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)` | The after.  
  
### getAfterOrBuilder()
    
    
    public abstract ValueOrBuilder getAfterOrBuilder()

Output only. Representations of the object value after the actions.

`.google.protobuf.Value after = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ValueOrBuilder.html)` |   
  
### getAfterSensitivePaths(int index)
    
    
    public abstract String getAfterSensitivePaths(int index)

Output only. The paths of sensitive fields in `after`. Paths are relative to `path`.

`repeated string after_sensitive_paths = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The afterSensitivePaths at the given index.  
  
### getAfterSensitivePathsBytes(int index)
    
    
    public abstract ByteString getAfterSensitivePathsBytes(int index)

Output only. The paths of sensitive fields in `after`. Paths are relative to `path`.

`repeated string after_sensitive_paths = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the afterSensitivePaths at the given index.  
  
### getAfterSensitivePathsCount()
    
    
    public abstract int getAfterSensitivePathsCount()

Output only. The paths of sensitive fields in `after`. Paths are relative to `path`.

`repeated string after_sensitive_paths = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of afterSensitivePaths.  
  
### getAfterSensitivePathsList()
    
    
    public abstract List<String> getAfterSensitivePathsList()

Output only. The paths of sensitive fields in `after`. Paths are relative to `path`.

`repeated string after_sensitive_paths = 4 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the afterSensitivePaths.  
  
### getBefore()
    
    
    public abstract Value getBefore()

Output only. Representations of the object value before the actions.

`.google.protobuf.Value before = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[Value](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Value.html)` | The before.  
  
### getBeforeOrBuilder()
    
    
    public abstract ValueOrBuilder getBeforeOrBuilder()

Output only. Representations of the object value before the actions.

`.google.protobuf.Value before = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ValueOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ValueOrBuilder.html)` |   
  
### getBeforeSensitivePaths(int index)
    
    
    public abstract String getBeforeSensitivePaths(int index)

Output only. The paths of sensitive fields in `before`. Paths are relative to `path`.

`repeated string before_sensitive_paths = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The beforeSensitivePaths at the given index.  
  
### getBeforeSensitivePathsBytes(int index)
    
    
    public abstract ByteString getBeforeSensitivePathsBytes(int index)

Output only. The paths of sensitive fields in `before`. Paths are relative to `path`.

`repeated string before_sensitive_paths = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the beforeSensitivePaths at the given index.  
  
### getBeforeSensitivePathsCount()
    
    
    public abstract int getBeforeSensitivePathsCount()

Output only. The paths of sensitive fields in `before`. Paths are relative to `path`.

`repeated string before_sensitive_paths = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of beforeSensitivePaths.  
  
### getBeforeSensitivePathsList()
    
    
    public abstract List<String> getBeforeSensitivePathsList()

Output only. The paths of sensitive fields in `before`. Paths are relative to `path`.

`repeated string before_sensitive_paths = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the beforeSensitivePaths.  
  
### getPath()
    
    
    public abstract String getPath()

Output only. The path of the property change.

`string path = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The path.  
  
### getPathBytes()
    
    
    public abstract ByteString getPathBytes()

Output only. The path of the property change.

`string path = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for path.  
  
### hasAfter()
    
    
    public abstract boolean hasAfter()

Output only. Representations of the object value after the actions.

`.google.protobuf.Value after = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the after field is set.  
  
### hasBefore()
    
    
    public abstract boolean hasBefore()

Output only. Representations of the object value before the actions.

`.google.protobuf.Value before = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the before field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
