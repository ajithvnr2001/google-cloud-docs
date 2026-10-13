---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkehub.v1.ScopeFeatureStateOrBuilder
title: Interface ScopeFeatureStateOrBuilder (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:53.001293+00:00
---

# Interface ScopeFeatureStateOrBuilder (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkehub.v1.ScopeFeatureStateOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ScopeFeatureStateOrBuilder (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkehub.v1.ScopeFeatureStateOrBuilder)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.gkehub.v1.ScopeFeatureStateOrBuilder)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.gkehub.v1.ScopeFeatureStateOrBuilder)


    
    
    public interface ScopeFeatureStateOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getState()
    
    
    public abstract FeatureState getState()

Output only. The "running state" of the Feature in this Scope.

`.google.events.cloud.gkehub.v1.FeatureState state = 1;`

**Returns**  
---  
**Type** | **Description**  
`[FeatureState](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkehub.v1.FeatureState)` | The state.  
  
### getStateOrBuilder()
    
    
    public abstract FeatureStateOrBuilder getStateOrBuilder()

Output only. The "running state" of the Feature in this Scope.

`.google.events.cloud.gkehub.v1.FeatureState state = 1;`

**Returns**  
---  
**Type** | **Description**  
`[FeatureStateOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.gkehub.v1.FeatureStateOrBuilder)` |   
  
### hasState()
    
    
    public abstract boolean hasState()

Output only. The "running state" of the Feature in this Scope.

`.google.events.cloud.gkehub.v1.FeatureState state = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the state field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
