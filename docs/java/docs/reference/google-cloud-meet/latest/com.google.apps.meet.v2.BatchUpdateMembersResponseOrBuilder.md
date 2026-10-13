---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2.BatchUpdateMembersResponseOrBuilder
title: Interface BatchUpdateMembersResponseOrBuilder (0.66.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:52.358295+00:00
---

# Interface BatchUpdateMembersResponseOrBuilder (0.66.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2.BatchUpdateMembersResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BatchUpdateMembersResponseOrBuilder (0.66.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.66.0 (latest)  0.62.0  0.61.0  0.60.0  0.58.0  0.55.0  0.54.0  0.52.0  0.50.0  0.49.0  0.47.0  0.45.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.37.0  0.35.0  0.34.0  0.31.0  0.30.0  0.29.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface BatchUpdateMembersResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getMembers(int index)
    
    
    public abstract Member getMembers(int index)

Members updated.

`repeated .google.apps.meet.v2.Member members = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Member](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2.Member)` |   
  
### getMembersCount()
    
    
    public abstract int getMembersCount()

Members updated.

`repeated .google.apps.meet.v2.Member members = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMembersList()
    
    
    public abstract List<Member> getMembersList()

Members updated.

`repeated .google.apps.meet.v2.Member members = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Member](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2.Member)>` |   
  
### getMembersOrBuilder(int index)
    
    
    public abstract MemberOrBuilder getMembersOrBuilder(int index)

Members updated.

`repeated .google.apps.meet.v2.Member members = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[MemberOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-meet/latest/com.google.apps.meet.v2.MemberOrBuilder)` |   
  
### getMembersOrBuilderList()
    
    
    public abstract List<? extends MemberOrBuilder> getMembersOrBuilderList()

Members updated.

`repeated .google.apps.meet.v2.Member members = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.apps.meet.v2.MemberOrBuilder>` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
