---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSettingOrBuilder
title: Interface FloorSettingOrBuilder (0.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:12:14.955755+00:00
---

# Interface FloorSettingOrBuilder (0.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSettingOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface FloorSettingOrBuilder (0.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.40.0 (latest)  0.36.0  0.35.0  0.34.0  0.32.0  0.29.0  0.28.0  0.26.0  0.24.0  0.23.0  0.21.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.11.0  0.9.0  0.8.0  0.5.0  0.4.0  0.3.0  0.1.0 
    
    
    public interface FloorSettingOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAiPlatformFloorSetting()
    
    
    public abstract AiPlatformFloorSetting getAiPlatformFloorSetting()

Optional. AI Platform floor setting.

` optional .google.cloud.modelarmor.v1.AiPlatformFloorSetting ai_platform_floor_setting = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AiPlatformFloorSetting](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.AiPlatformFloorSetting)` | The aiPlatformFloorSetting.  
  
### getAiPlatformFloorSettingOrBuilder()
    
    
    public abstract AiPlatformFloorSettingOrBuilder getAiPlatformFloorSettingOrBuilder()

Optional. AI Platform floor setting.

` optional .google.cloud.modelarmor.v1.AiPlatformFloorSetting ai_platform_floor_setting = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AiPlatformFloorSettingOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.AiPlatformFloorSettingOrBuilder)` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. [Output only] Create timestamp

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. [Output only] Create timestamp

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getEnableFloorSettingEnforcement()
    
    
    public abstract boolean getEnableFloorSettingEnforcement()

Optional. Floor Settings enforcement status.

` optional bool enable_floor_setting_enforcement = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enableFloorSettingEnforcement.  
  
### getFilterConfig()
    
    
    public abstract FilterConfig getFilterConfig()

Required. ModelArmor filter configuration.

` .google.cloud.modelarmor.v1.FilterConfig filter_config = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[FilterConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FilterConfig)` | The filterConfig.  
  
### getFilterConfigOrBuilder()
    
    
    public abstract FilterConfigOrBuilder getFilterConfigOrBuilder()

Required. ModelArmor filter configuration.

` .google.cloud.modelarmor.v1.FilterConfig filter_config = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[FilterConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FilterConfigOrBuilder)` |   
  
### getFloorSettingMetadata()
    
    
    public abstract FloorSetting.FloorSettingMetadata getFloorSettingMetadata()

Optional. Metadata for FloorSetting

` .google.cloud.modelarmor.v1.FloorSetting.FloorSettingMetadata floor_setting_metadata = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FloorSetting.FloorSettingMetadata](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.FloorSettingMetadata)` | The floorSettingMetadata.  
  
### getFloorSettingMetadataOrBuilder()
    
    
    public abstract FloorSetting.FloorSettingMetadataOrBuilder getFloorSettingMetadataOrBuilder()

Optional. Metadata for FloorSetting

` .google.cloud.modelarmor.v1.FloorSetting.FloorSettingMetadata floor_setting_metadata = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FloorSetting.FloorSettingMetadataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.FloorSettingMetadataOrBuilder)` |   
  
### getIntegratedServices(int index)
    
    
    public abstract FloorSetting.IntegratedService getIntegratedServices(int index)

Optional. List of integrated services for which the floor setting is applicable.

` repeated .google.cloud.modelarmor.v1.FloorSetting.IntegratedService integrated_services = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[FloorSetting.IntegratedService](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.IntegratedService)` | The integratedServices at the given index.  
  
### getIntegratedServicesCount()
    
    
    public abstract int getIntegratedServicesCount()

Optional. List of integrated services for which the floor setting is applicable.

` repeated .google.cloud.modelarmor.v1.FloorSetting.IntegratedService integrated_services = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of integratedServices.  
  
### getIntegratedServicesList()
    
    
    public abstract List<FloorSetting.IntegratedService> getIntegratedServicesList()

Optional. List of integrated services for which the floor setting is applicable.

` repeated .google.cloud.modelarmor.v1.FloorSetting.IntegratedService integrated_services = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[IntegratedService](https://docs.cloud.google.com/java/docs/reference/google-cloud-modelarmor/latest/com.google.cloud.modelarmor.v1.FloorSetting.IntegratedService)>` | A list containing the integratedServices.  
  
### getIntegratedServicesValue(int index)
    
    
    public abstract int getIntegratedServicesValue(int index)

Optional. List of integrated services for which the floor setting is applicable.

` repeated .google.cloud.modelarmor.v1.FloorSetting.IntegratedService integrated_services = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire of integratedServices at the given index.  
  
### getIntegratedServicesValueList()
    
    
    public abstract List<Integer> getIntegratedServicesValueList()

Optional. List of integrated services for which the floor setting is applicable.

` repeated .google.cloud.modelarmor.v1.FloorSetting.IntegratedService integrated_services = 6 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Integer](https://docs.oracle.com/javase/8/docs/api/java/lang/Integer.html)>` | A list containing the enum numeric values on the wire for integratedServices.  
  
### getName()
    
    
    public abstract String getName()

Identifier. The resource name.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The resource name.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. [Output only] Update timestamp

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. [Output only] Update timestamp

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasAiPlatformFloorSetting()
    
    
    public abstract boolean hasAiPlatformFloorSetting()

Optional. AI Platform floor setting.

` optional .google.cloud.modelarmor.v1.AiPlatformFloorSetting ai_platform_floor_setting = 7 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the aiPlatformFloorSetting field is set.  
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. [Output only] Create timestamp

`.google.protobuf.Timestamp create_time = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasEnableFloorSettingEnforcement()
    
    
    public abstract boolean hasEnableFloorSettingEnforcement()

Optional. Floor Settings enforcement status.

` optional bool enable_floor_setting_enforcement = 5 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the enableFloorSettingEnforcement field is set.  
  
### hasFilterConfig()
    
    
    public abstract boolean hasFilterConfig()

Required. ModelArmor filter configuration.

` .google.cloud.modelarmor.v1.FilterConfig filter_config = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the filterConfig field is set.  
  
### hasFloorSettingMetadata()
    
    
    public abstract boolean hasFloorSettingMetadata()

Optional. Metadata for FloorSetting

` .google.cloud.modelarmor.v1.FloorSetting.FloorSettingMetadata floor_setting_metadata = 8 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the floorSettingMetadata field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. [Output only] Update timestamp

`.google.protobuf.Timestamp update_time = 3 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
