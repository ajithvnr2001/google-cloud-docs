---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaAdjusterSettingsOrBuilder
title: Interface QuotaAdjusterSettingsOrBuilder (0.67.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:10:16.942515+00:00
---

# Interface QuotaAdjusterSettingsOrBuilder (0.67.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaAdjusterSettingsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface QuotaAdjusterSettingsOrBuilder (0.67.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.67.0 (latest)  0.63.0  0.62.0  0.61.0  0.59.0  0.56.0  0.55.0  0.53.0  0.51.0  0.50.0  0.49.0  0.48.0  0.46.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.36.0  0.35.0  0.32.0  0.31.0  0.30.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface QuotaAdjusterSettingsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getEnablement()
    
    
    public abstract QuotaAdjusterSettings.Enablement getEnablement()

Optional. The configured value of the enablement at the given resource.

` .google.api.cloudquotas.v1.QuotaAdjusterSettings.Enablement enablement = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[QuotaAdjusterSettings.Enablement](https://docs.cloud.google.com/java/docs/reference/google-cloud-cloudquotas/latest/com.google.api.cloudquotas.v1.QuotaAdjusterSettings.Enablement)` | The enablement.  
  
### getEnablementValue()
    
    
    public abstract int getEnablementValue()

Optional. The configured value of the enablement at the given resource.

` .google.api.cloudquotas.v1.QuotaAdjusterSettings.Enablement enablement = 2 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for enablement.  
  
### getEtag()
    
    
    public abstract String getEtag()

Optional. The current ETag of the QuotaAdjusterSettings. If an ETag is provided on update and does not match the current server's ETag in the QuotaAdjusterSettings, the request is blocked and returns an ABORTED error. See <https://google.aip.dev/134#etags> for more details on ETags.

`string etag = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The etag.  
  
### getEtagBytes()
    
    
    public abstract ByteString getEtagBytes()

Optional. The current ETag of the QuotaAdjusterSettings. If an ETag is provided on update and does not match the current server's ETag in the QuotaAdjusterSettings, the request is blocked and returns an ABORTED error. See <https://google.aip.dev/134#etags> for more details on ETags.

`string etag = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for etag.  
  
### getInherited()
    
    
    public abstract boolean getInherited()

Optional. Indicates whether the setting is inherited or explicitly specified.

`bool inherited = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The inherited.  
  
### getInheritedFrom()
    
    
    public abstract String getInheritedFrom()

Output only. The resource container from which the setting is inherited. This refers to the nearest ancestor with enablement set (either ENABLED or DISABLED). The value can be an organizations/{organization_id}, folders/{folder_id}, or can be 'default' if no ancestor exists with enablement set. The value will be empty when enablement is directly set on this container.

`string inherited_from = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The inheritedFrom.  
  
### getInheritedFromBytes()
    
    
    public abstract ByteString getInheritedFromBytes()

Output only. The resource container from which the setting is inherited. This refers to the nearest ancestor with enablement set (either ENABLED or DISABLED). The value can be an organizations/{organization_id}, folders/{folder_id}, or can be 'default' if no ancestor exists with enablement set. The value will be empty when enablement is directly set on this container.

`string inherited_from = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for inheritedFrom.  
  
### getName()
    
    
    public abstract String getName()

Identifier. Name of the configuration, in the formats below:

  * For a project: projects/PROJECT_NUMBER/locations/global/quotaAdjusterSettings
  * For a folder: folders/FOLDER_NUMBER/locations/global/quotaAdjusterSettings
  * For an organization: organizations/ORGANIZATION_NUMBER/locations/global/quotaAdjusterSettings



`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. Name of the configuration, in the formats below:

  * For a project: projects/PROJECT_NUMBER/locations/global/quotaAdjusterSettings
  * For a folder: folders/FOLDER_NUMBER/locations/global/quotaAdjusterSettings
  * For an organization: organizations/ORGANIZATION_NUMBER/locations/global/quotaAdjusterSettings



`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. The timestamp when the QuotaAdjusterSettings resource was last updated.

`.google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. The timestamp when the QuotaAdjusterSettings resource was last updated.

`.google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. The timestamp when the QuotaAdjusterSettings resource was last updated.

`.google.protobuf.Timestamp update_time = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
