---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.AccessRulesOptionsOrBuilder
title: Interface AccessRulesOptionsOrBuilder (0.39.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:24:31.233714+00:00
---

# Interface AccessRulesOptionsOrBuilder (0.39.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.AccessRulesOptionsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AccessRulesOptionsOrBuilder (0.39.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.39.0 (latest)  0.35.0  0.34.0  0.33.0  0.31.0  0.28.0  0.27.0  0.25.0  0.23.0  0.22.0  0.21.0  0.20.0  0.18.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.10.0  0.8.0  0.7.0  0.4.0  0.3.0  0.2.0 
    
    
    public interface AccessRulesOptionsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAccessRules(int index)
    
    
    public abstract AccessRulesOptions.AccessRule getAccessRules(int index)

Optional. The access rules for the instance.

` repeated .google.cloud.lustre.v1.AccessRulesOptions.AccessRule access_rules = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AccessRulesOptions.AccessRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.AccessRulesOptions.AccessRule)` |   
  
### getAccessRulesCount()
    
    
    public abstract int getAccessRulesCount()

Optional. The access rules for the instance.

` repeated .google.cloud.lustre.v1.AccessRulesOptions.AccessRule access_rules = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getAccessRulesList()
    
    
    public abstract List<AccessRulesOptions.AccessRule> getAccessRulesList()

Optional. The access rules for the instance.

` repeated .google.cloud.lustre.v1.AccessRulesOptions.AccessRule access_rules = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AccessRule](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.AccessRulesOptions.AccessRule)>` |   
  
### getAccessRulesOrBuilder(int index)
    
    
    public abstract AccessRulesOptions.AccessRuleOrBuilder getAccessRulesOrBuilder(int index)

Optional. The access rules for the instance.

` repeated .google.cloud.lustre.v1.AccessRulesOptions.AccessRule access_rules = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AccessRulesOptions.AccessRuleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.AccessRulesOptions.AccessRuleOrBuilder)` |   
  
### getAccessRulesOrBuilderList()
    
    
    public abstract List<? extends AccessRulesOptions.AccessRuleOrBuilder> getAccessRulesOrBuilderList()

Optional. The access rules for the instance.

` repeated .google.cloud.lustre.v1.AccessRulesOptions.AccessRule access_rules = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.lustre.v1.AccessRulesOptions.AccessRuleOrBuilder>` |   
  
### getDefaultSquashGid()
    
    
    public abstract int getDefaultSquashGid()

Optional. The user squash GID for the default access rule. This user squash GID applies to all root users connecting from clients that are not matched by any of the access rules. If not set, the default is 0 (no GID squash).

`int32 default_squash_gid = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The defaultSquashGid.  
  
### getDefaultSquashMode()
    
    
    public abstract AccessRulesOptions.SquashMode getDefaultSquashMode()

Required. The squash mode for the default access rule.

` .google.cloud.lustre.v1.AccessRulesOptions.SquashMode default_squash_mode = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[AccessRulesOptions.SquashMode](https://docs.cloud.google.com/java/docs/reference/google-cloud-lustre/latest/com.google.cloud.lustre.v1.AccessRulesOptions.SquashMode)` | The defaultSquashMode.  
  
### getDefaultSquashModeValue()
    
    
    public abstract int getDefaultSquashModeValue()

Required. The squash mode for the default access rule.

` .google.cloud.lustre.v1.AccessRulesOptions.SquashMode default_squash_mode = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for defaultSquashMode.  
  
### getDefaultSquashUid()
    
    
    public abstract int getDefaultSquashUid()

Optional. The user squash UID for the default access rule. This user squash UID applies to all root users connecting from clients that are not matched by any of the access rules. If not set, the default is 0 (no UID squash).

`int32 default_squash_uid = 3 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The defaultSquashUid.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
