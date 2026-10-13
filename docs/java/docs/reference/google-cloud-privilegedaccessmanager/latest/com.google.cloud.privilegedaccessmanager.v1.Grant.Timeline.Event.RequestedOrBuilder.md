---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-privilegedaccessmanager/latest/com.google.cloud.privilegedaccessmanager.v1.Grant.Timeline.Event.RequestedOrBuilder
title: Interface Grant.Timeline.Event.RequestedOrBuilder (0.53.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:19.363655+00:00
---

# Interface Grant.Timeline.Event.RequestedOrBuilder (0.53.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-privilegedaccessmanager/latest/com.google.cloud.privilegedaccessmanager.v1.Grant.Timeline.Event.RequestedOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface Grant.Timeline.Event.RequestedOrBuilder (0.53.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.53.0 (latest)  0.49.0  0.48.0  0.47.0  0.45.0  0.42.0  0.41.0  0.39.0  0.37.0  0.36.0  0.34.0  0.32.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.24.0  0.22.0  0.21.0  0.18.0  0.17.0  0.16.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface Grant.Timeline.Event.RequestedOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getExpireTime()
    
    
    public abstract Timestamp getExpireTime()

Output only. The time at which this grant expires unless the approval workflow completes. If omitted, then the request never expires.

` .google.protobuf.Timestamp expire_time = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The expireTime.  
  
### getExpireTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getExpireTimeOrBuilder()

Output only. The time at which this grant expires unless the approval workflow completes. If omitted, then the request never expires.

` .google.protobuf.Timestamp expire_time = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasExpireTime()
    
    
    public abstract boolean hasExpireTime()

Output only. The time at which this grant expires unless the approval workflow completes. If omitted, then the request never expires.

` .google.protobuf.Timestamp expire_time = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the expireTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
