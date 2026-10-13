---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ListRolloutsResponseOrBuilder
title: Interface ListRolloutsResponseOrBuilder (0.33.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:52.765156+00:00
---

# Interface ListRolloutsResponseOrBuilder (0.33.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.ListRolloutsResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ListRolloutsResponseOrBuilder (0.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.33.0 (latest)  0.29.0  0.28.0  0.27.0  0.25.0  0.22.0  0.21.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.4.0  0.2.0  0.1.0 
    
    
    public interface ListRolloutsResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getNextPageToken()
    
    
    public abstract String getNextPageToken()

A token identifying a page of results the server should return.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nextPageToken.  
  
### getNextPageTokenBytes()
    
    
    public abstract ByteString getNextPageTokenBytes()

A token identifying a page of results the server should return.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nextPageToken.  
  
### getRollouts(int index)
    
    
    public abstract Rollout getRollouts(int index)

The list of Rollouts

`repeated .google.cloud.configdelivery.v1beta.Rollout rollouts = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.Rollout)` |   
  
### getRolloutsCount()
    
    
    public abstract int getRolloutsCount()

The list of Rollouts

`repeated .google.cloud.configdelivery.v1beta.Rollout rollouts = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getRolloutsList()
    
    
    public abstract List<Rollout> getRolloutsList()

The list of Rollouts

`repeated .google.cloud.configdelivery.v1beta.Rollout rollouts = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Rollout](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.Rollout)>` |   
  
### getRolloutsOrBuilder(int index)
    
    
    public abstract RolloutOrBuilder getRolloutsOrBuilder(int index)

The list of Rollouts

`repeated .google.cloud.configdelivery.v1beta.Rollout rollouts = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[RolloutOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-configdelivery/latest/com.google.cloud.configdelivery.v1beta.RolloutOrBuilder)` |   
  
### getRolloutsOrBuilderList()
    
    
    public abstract List<? extends RolloutOrBuilder> getRolloutsOrBuilderList()

The list of Rollouts

`repeated .google.cloud.configdelivery.v1beta.Rollout rollouts = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.configdelivery.v1beta.RolloutOrBuilder>` |   
  
### getUnreachable(int index)
    
    
    public abstract String getUnreachable(int index)

Unordered list. Locations that could not be reached.

`repeated string unreachable = 3 [(.google.api.field_behavior) = UNORDERED_LIST];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The unreachable at the given index.  
  
### getUnreachableBytes(int index)
    
    
    public abstract ByteString getUnreachableBytes(int index)

Unordered list. Locations that could not be reached.

`repeated string unreachable = 3 [(.google.api.field_behavior) = UNORDERED_LIST];`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the unreachable at the given index.  
  
### getUnreachableCount()
    
    
    public abstract int getUnreachableCount()

Unordered list. Locations that could not be reached.

`repeated string unreachable = 3 [(.google.api.field_behavior) = UNORDERED_LIST];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of unreachable.  
  
### getUnreachableList()
    
    
    public abstract List<String> getUnreachableList()

Unordered list. Locations that could not be reached.

`repeated string unreachable = 3 [(.google.api.field_behavior) = UNORDERED_LIST];`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the unreachable.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
