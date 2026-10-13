---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.firebase.analytics.v1.UserPropertyValueOrBuilder
title: Interface UserPropertyValueOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:02.101000+00:00
---

# Interface UserPropertyValueOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.firebase.analytics.v1.UserPropertyValueOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface UserPropertyValueOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.firebase.analytics.v1.UserPropertyValueOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.firebase.analytics.v1.UserPropertyValueOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.firebase.analytics.v1.UserPropertyValueOrBuilder)


    
    
    public interface UserPropertyValueOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getIndex()
    
    
    public abstract int getIndex()

Index for user property (one-based).

`int32 index = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The index.  
  
### getSetTimestampUsec()
    
    
    public abstract long getSetTimestampUsec()

UTC client time when user property was last set.

`int64 set_timestamp_usec = 2;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The setTimestampUsec.  
  
### getValue()
    
    
    public abstract AnalyticsValue getValue()

Last set value of user property.

`.google.events.firebase.analytics.v1.AnalyticsValue value = 1;`

**Returns**  
---  
**Type** | **Description**  
`[AnalyticsValue](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.firebase.analytics.v1.AnalyticsValue)` | The value.  
  
### getValueOrBuilder()
    
    
    public abstract AnalyticsValueOrBuilder getValueOrBuilder()

Last set value of user property.

`.google.events.firebase.analytics.v1.AnalyticsValue value = 1;`

**Returns**  
---  
**Type** | **Description**  
`[AnalyticsValueOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.firebase.analytics.v1.AnalyticsValueOrBuilder)` |   
  
### hasValue()
    
    
    public abstract boolean hasValue()

Last set value of user property.

`.google.events.firebase.analytics.v1.AnalyticsValue value = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the value field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
