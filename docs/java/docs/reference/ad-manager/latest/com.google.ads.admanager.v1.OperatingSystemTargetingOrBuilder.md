---
url: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OperatingSystemTargetingOrBuilder
title: Interface OperatingSystemTargetingOrBuilder (0.58.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:09.787133+00:00
---

# Interface OperatingSystemTargetingOrBuilder (0.58.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/ad-manager/latest/com.google.ads.admanager.v1.OperatingSystemTargetingOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface OperatingSystemTargetingOrBuilder (0.58.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.58.0 (latest)  0.54.0  0.53.0  0.52.0  0.50.0  0.47.0  0.46.0  0.44.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.29.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface OperatingSystemTargetingOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getExcludedOperatingSystemVersions(int index)
    
    
    public abstract String getExcludedOperatingSystemVersions(int index)

Optional. A list of operating system version resource names that should be excluded.

` repeated string excluded_operating_system_versions = 8 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The excludedOperatingSystemVersions at the given index.  
  
### getExcludedOperatingSystemVersionsBytes(int index)
    
    
    public abstract ByteString getExcludedOperatingSystemVersionsBytes(int index)

Optional. A list of operating system version resource names that should be excluded.

` repeated string excluded_operating_system_versions = 8 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the excludedOperatingSystemVersions at the given index.  
  
### getExcludedOperatingSystemVersionsCount()
    
    
    public abstract int getExcludedOperatingSystemVersionsCount()

Optional. A list of operating system version resource names that should be excluded.

` repeated string excluded_operating_system_versions = 8 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of excludedOperatingSystemVersions.  
  
### getExcludedOperatingSystemVersionsList()
    
    
    public abstract List<String> getExcludedOperatingSystemVersionsList()

Optional. A list of operating system version resource names that should be excluded.

` repeated string excluded_operating_system_versions = 8 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the excludedOperatingSystemVersions.  
  
### getExcludedOperatingSystems(int index)
    
    
    public abstract String getExcludedOperatingSystems(int index)

Optional. A list of operating system resource names that should be excluded.

` repeated string excluded_operating_systems = 6 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The excludedOperatingSystems at the given index.  
  
### getExcludedOperatingSystemsBytes(int index)
    
    
    public abstract ByteString getExcludedOperatingSystemsBytes(int index)

Optional. A list of operating system resource names that should be excluded.

` repeated string excluded_operating_systems = 6 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the excludedOperatingSystems at the given index.  
  
### getExcludedOperatingSystemsCount()
    
    
    public abstract int getExcludedOperatingSystemsCount()

Optional. A list of operating system resource names that should be excluded.

` repeated string excluded_operating_systems = 6 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of excludedOperatingSystems.  
  
### getExcludedOperatingSystemsList()
    
    
    public abstract List<String> getExcludedOperatingSystemsList()

Optional. A list of operating system resource names that should be excluded.

` repeated string excluded_operating_systems = 6 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the excludedOperatingSystems.  
  
### getTargetedOperatingSystemVersions(int index)
    
    
    public abstract String getTargetedOperatingSystemVersions(int index)

Optional. A list of operating system version resource names that should be targeted/included.

` repeated string targeted_operating_system_versions = 7 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The targetedOperatingSystemVersions at the given index.  
  
### getTargetedOperatingSystemVersionsBytes(int index)
    
    
    public abstract ByteString getTargetedOperatingSystemVersionsBytes(int index)

Optional. A list of operating system version resource names that should be targeted/included.

` repeated string targeted_operating_system_versions = 7 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the targetedOperatingSystemVersions at the given index.  
  
### getTargetedOperatingSystemVersionsCount()
    
    
    public abstract int getTargetedOperatingSystemVersionsCount()

Optional. A list of operating system version resource names that should be targeted/included.

` repeated string targeted_operating_system_versions = 7 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of targetedOperatingSystemVersions.  
  
### getTargetedOperatingSystemVersionsList()
    
    
    public abstract List<String> getTargetedOperatingSystemVersionsList()

Optional. A list of operating system version resource names that should be targeted/included.

` repeated string targeted_operating_system_versions = 7 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the targetedOperatingSystemVersions.  
  
### getTargetedOperatingSystems(int index)
    
    
    public abstract String getTargetedOperatingSystems(int index)

Optional. A list of operating system resource names that should be targeted/included.

` repeated string targeted_operating_systems = 5 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The targetedOperatingSystems at the given index.  
  
### getTargetedOperatingSystemsBytes(int index)
    
    
    public abstract ByteString getTargetedOperatingSystemsBytes(int index)

Optional. A list of operating system resource names that should be targeted/included.

` repeated string targeted_operating_systems = 5 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the targetedOperatingSystems at the given index.  
  
### getTargetedOperatingSystemsCount()
    
    
    public abstract int getTargetedOperatingSystemsCount()

Optional. A list of operating system resource names that should be targeted/included.

` repeated string targeted_operating_systems = 5 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of targetedOperatingSystems.  
  
### getTargetedOperatingSystemsList()
    
    
    public abstract List<String> getTargetedOperatingSystemsList()

Optional. A list of operating system resource names that should be targeted/included.

` repeated string targeted_operating_systems = 5 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the targetedOperatingSystems.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
