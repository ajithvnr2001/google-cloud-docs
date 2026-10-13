---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ResourceInfoOrBuilder
title: Interface ResourceInfoOrBuilder (0.97.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:24.977399+00:00
---

# Interface ResourceInfoOrBuilder (0.97.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ResourceInfoOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ResourceInfoOrBuilder (0.97.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.97.0 (latest)  0.93.0  0.92.0  0.91.0  0.89.0  0.86.0  0.85.0  0.83.0  0.81.0  0.80.0  0.79.0  0.78.0  0.76.0  0.74.0  0.73.0  0.72.0  0.71.0  0.70.0  0.68.0  0.66.0  0.65.0  0.62.0  0.61.0  0.60.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface ResourceInfoOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getId()
    
    
    public abstract String getId()

Required. Unique Id for the resource.

`string id = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The id.  
  
### getIdBytes()
    
    
    public abstract ByteString getIdBytes()

Required. Unique Id for the resource.

`string id = 1 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for id.  
  
### getResource()
    
    
    public abstract Any getResource()

Specific details for the resource. This is for internal use only.

`.google.protobuf.Any resource = 3;`

**Returns**  
---  
**Type** | **Description**  
`[Any](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Any.html)` | The resource.  
  
### getResourceOrBuilder()
    
    
    public abstract AnyOrBuilder getResourceOrBuilder()

Specific details for the resource. This is for internal use only.

`.google.protobuf.Any resource = 3;`

**Returns**  
---  
**Type** | **Description**  
`[AnyOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.AnyOrBuilder.html)` |   
  
### getStatus()
    
    
    public abstract HealthStatus getStatus()

Overall health status. Overall status is derived based on the status of each sub level resources.

`.google.cloud.beyondcorp.appconnectors.v1.HealthStatus status = 2;`

**Returns**  
---  
**Type** | **Description**  
`[HealthStatus](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.HealthStatus)` | The status.  
  
### getStatusValue()
    
    
    public abstract int getStatusValue()

Overall health status. Overall status is derived based on the status of each sub level resources.

`.google.cloud.beyondcorp.appconnectors.v1.HealthStatus status = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for status.  
  
### getSub(int index)
    
    
    public abstract ResourceInfo getSub(int index)

List of Info for the sub level resources.

`repeated .google.cloud.beyondcorp.appconnectors.v1.ResourceInfo sub = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResourceInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ResourceInfo)` |   
  
### getSubCount()
    
    
    public abstract int getSubCount()

List of Info for the sub level resources.

`repeated .google.cloud.beyondcorp.appconnectors.v1.ResourceInfo sub = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getSubList()
    
    
    public abstract List<ResourceInfo> getSubList()

List of Info for the sub level resources.

`repeated .google.cloud.beyondcorp.appconnectors.v1.ResourceInfo sub = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ResourceInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ResourceInfo)>` |   
  
### getSubOrBuilder(int index)
    
    
    public abstract ResourceInfoOrBuilder getSubOrBuilder(int index)

List of Info for the sub level resources.

`repeated .google.cloud.beyondcorp.appconnectors.v1.ResourceInfo sub = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ResourceInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-beyondcorp-appconnectors/latest/com.google.cloud.beyondcorp.appconnectors.v1.ResourceInfoOrBuilder)` |   
  
### getSubOrBuilderList()
    
    
    public abstract List<? extends ResourceInfoOrBuilder> getSubOrBuilderList()

List of Info for the sub level resources.

`repeated .google.cloud.beyondcorp.appconnectors.v1.ResourceInfo sub = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.beyondcorp.appconnectors.v1.ResourceInfoOrBuilder>` |   
  
### getTime()
    
    
    public abstract Timestamp getTime()

The timestamp to collect the info. It is suggested to be set by the topmost level resource only.

`.google.protobuf.Timestamp time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The time.  
  
### getTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getTimeOrBuilder()

The timestamp to collect the info. It is suggested to be set by the topmost level resource only.

`.google.protobuf.Timestamp time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasResource()
    
    
    public abstract boolean hasResource()

Specific details for the resource. This is for internal use only.

`.google.protobuf.Any resource = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the resource field is set.  
  
### hasTime()
    
    
    public abstract boolean hasTime()

The timestamp to collect the info. It is suggested to be set by the topmost level resource only.

`.google.protobuf.Timestamp time = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the time field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
