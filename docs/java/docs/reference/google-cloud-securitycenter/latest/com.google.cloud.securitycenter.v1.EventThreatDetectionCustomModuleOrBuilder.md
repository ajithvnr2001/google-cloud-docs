---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.EventThreatDetectionCustomModuleOrBuilder
title: Interface EventThreatDetectionCustomModuleOrBuilder (2.107.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:47.922505+00:00
---

# Interface EventThreatDetectionCustomModuleOrBuilder (2.107.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.EventThreatDetectionCustomModuleOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface EventThreatDetectionCustomModuleOrBuilder (2.107.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.107.0 (latest)  2.103.0  2.102.0  2.101.0  2.99.0  2.96.0  2.95.0  2.93.0  2.91.0  2.90.0  2.88.0  2.86.0  2.84.0  2.83.0  2.82.0  2.81.0  2.80.0  2.78.0  2.76.0  2.75.0  2.72.0  2.71.0  2.70.0  2.68.0  2.67.0  2.66.0  2.65.0  2.64.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.57.0  2.56.0  2.55.0  2.54.0  2.53.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.10.0  2.9.0  2.8.0  2.7.1  2.6.0  2.5.6  2.3.2 
    
    
    public interface EventThreatDetectionCustomModuleOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAncestorModule()
    
    
    public abstract String getAncestorModule()

Output only. The closest ancestor module that this module inherits the enablement state from. The format is the same as the EventThreatDetectionCustomModule resource name.

` string ancestor_module = 3 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The ancestorModule.  
  
### getAncestorModuleBytes()
    
    
    public abstract ByteString getAncestorModuleBytes()

Output only. The closest ancestor module that this module inherits the enablement state from. The format is the same as the EventThreatDetectionCustomModule resource name.

` string ancestor_module = 3 [(.google.api.field_behavior) = OUTPUT_ONLY, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for ancestorModule.  
  
### getConfig()
    
    
    public abstract Struct getConfig()

Config for the module. For the resident module, its config value is defined at this level. For the inherited module, its config value is inherited from the ancestor module.

`.google.protobuf.Struct config = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Struct.html)` | The config.  
  
### getConfigOrBuilder()
    
    
    public abstract StructOrBuilder getConfigOrBuilder()

Config for the module. For the resident module, its config value is defined at this level. For the inherited module, its config value is inherited from the ancestor module.

`.google.protobuf.Struct config = 2;`

**Returns**  
---  
**Type** | **Description**  
`[StructOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.StructOrBuilder.html)` |   
  
### getDescription()
    
    
    public abstract String getDescription()

The description for the module.

`string description = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The description.  
  
### getDescriptionBytes()
    
    
    public abstract ByteString getDescriptionBytes()

The description for the module.

`string description = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for description.  
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

The human readable name to be displayed for the module.

`string display_name = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

The human readable name to be displayed for the module.

`string display_name = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getEnablementState()
    
    
    public abstract EventThreatDetectionCustomModule.EnablementState getEnablementState()

The state of enablement for the module at the given level of the hierarchy.

` .google.cloud.securitycenter.v1.EventThreatDetectionCustomModule.EnablementState enablement_state = 4; `

**Returns**  
---  
**Type** | **Description**  
`[EventThreatDetectionCustomModule.EnablementState](https://docs.cloud.google.com/java/docs/reference/google-cloud-securitycenter/latest/com.google.cloud.securitycenter.v1.EventThreatDetectionCustomModule.EnablementState)` | The enablementState.  
  
### getEnablementStateValue()
    
    
    public abstract int getEnablementStateValue()

The state of enablement for the module at the given level of the hierarchy.

` .google.cloud.securitycenter.v1.EventThreatDetectionCustomModule.EnablementState enablement_state = 4; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for enablementState.  
  
### getLastEditor()
    
    
    public abstract String getLastEditor()

Output only. The editor the module was last updated by.

`string last_editor = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The lastEditor.  
  
### getLastEditorBytes()
    
    
    public abstract ByteString getLastEditorBytes()

Output only. The editor the module was last updated by.

`string last_editor = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for lastEditor.  
  
### getName()
    
    
    public abstract String getName()

Immutable. The resource name of the Event Threat Detection custom module.

Its format is:

  * `organizations/{organization}/eventThreatDetectionSettings/customModules/{module}`.
  * `folders/{folder}/eventThreatDetectionSettings/customModules/{module}`.
  * `projects/{project}/eventThreatDetectionSettings/customModules/{module}`.



`string name = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Immutable. The resource name of the Event Threat Detection custom module.

Its format is:

  * `organizations/{organization}/eventThreatDetectionSettings/customModules/{module}`.
  * `folders/{folder}/eventThreatDetectionSettings/customModules/{module}`.
  * `projects/{project}/eventThreatDetectionSettings/customModules/{module}`.



`string name = 1 [(.google.api.field_behavior) = IMMUTABLE];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getType()
    
    
    public abstract String getType()

Type for the module. e.g. CONFIGURABLE_BAD_IP.

`string type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The type.  
  
### getTypeBytes()
    
    
    public abstract ByteString getTypeBytes()

Type for the module. e.g. CONFIGURABLE_BAD_IP.

`string type = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for type.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. The time the module was last updated.

`.google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The time the module was last updated.

`.google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasConfig()
    
    
    public abstract boolean hasConfig()

Config for the module. For the resident module, its config value is defined at this level. For the inherited module, its config value is inherited from the ancestor module.

`.google.protobuf.Struct config = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the config field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. The time the module was last updated.

`.google.protobuf.Timestamp update_time = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
