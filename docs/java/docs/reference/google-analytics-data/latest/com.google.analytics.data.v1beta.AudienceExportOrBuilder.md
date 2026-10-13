---
url: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceExportOrBuilder
title: Interface AudienceExportOrBuilder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:11:26.531329+00:00
---

# Interface AudienceExportOrBuilder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceExportOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AudienceExportOrBuilder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0 
    
    
    public interface AudienceExportOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAudience()
    
    
    public abstract String getAudience()

Required. The audience resource name. This resource name identifies the audience being listed and is shared between the Analytics Data & Admin APIs.

Format: `properties/{property}/audiences/{audience}`

`string audience = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The audience.  
  
### getAudienceBytes()
    
    
    public abstract ByteString getAudienceBytes()

Required. The audience resource name. This resource name identifies the audience being listed and is shared between the Analytics Data & Admin APIs.

Format: `properties/{property}/audiences/{audience}`

`string audience = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for audience.  
  
### getAudienceDisplayName()
    
    
    public abstract String getAudienceDisplayName()

Output only. The descriptive display name for this audience. For example, "Purchasers".

`string audience_display_name = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The audienceDisplayName.  
  
### getAudienceDisplayNameBytes()
    
    
    public abstract ByteString getAudienceDisplayNameBytes()

Output only. The descriptive display name for this audience. For example, "Purchasers".

`string audience_display_name = 3 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for audienceDisplayName.  
  
### getBeginCreatingTime()
    
    
    public abstract Timestamp getBeginCreatingTime()

Output only. The time when CreateAudienceExport was called and the AudienceExport began the `CREATING` state.

` optional .google.protobuf.Timestamp begin_creating_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The beginCreatingTime.  
  
### getBeginCreatingTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getBeginCreatingTimeOrBuilder()

Output only. The time when CreateAudienceExport was called and the AudienceExport began the `CREATING` state.

` optional .google.protobuf.Timestamp begin_creating_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getCreationQuotaTokensCharged()
    
    
    public abstract int getCreationQuotaTokensCharged()

Output only. The total quota tokens charged during creation of the AudienceExport. Because this token count is based on activity from the `CREATING` state, this tokens charged will be fixed once an AudienceExport enters the `ACTIVE` or `FAILED` states.

`int32 creation_quota_tokens_charged = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The creationQuotaTokensCharged.  
  
### getDimensions(int index)
    
    
    public abstract AudienceDimension getDimensions(int index)

Required. The dimensions requested and displayed in the query response.

` repeated .google.analytics.data.v1beta.AudienceDimension dimensions = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AudienceDimension](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceDimension)` |   
  
### getDimensionsCount()
    
    
    public abstract int getDimensionsCount()

Required. The dimensions requested and displayed in the query response.

` repeated .google.analytics.data.v1beta.AudienceDimension dimensions = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getDimensionsList()
    
    
    public abstract List<AudienceDimension> getDimensionsList()

Required. The dimensions requested and displayed in the query response.

` repeated .google.analytics.data.v1beta.AudienceDimension dimensions = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[AudienceDimension](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceDimension)>` |   
  
### getDimensionsOrBuilder(int index)
    
    
    public abstract AudienceDimensionOrBuilder getDimensionsOrBuilder(int index)

Required. The dimensions requested and displayed in the query response.

` repeated .google.analytics.data.v1beta.AudienceDimension dimensions = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[AudienceDimensionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceDimensionOrBuilder)` |   
  
### getDimensionsOrBuilderList()
    
    
    public abstract List<? extends AudienceDimensionOrBuilder> getDimensionsOrBuilderList()

Required. The dimensions requested and displayed in the query response.

` repeated .google.analytics.data.v1beta.AudienceDimension dimensions = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.analytics.data.v1beta.AudienceDimensionOrBuilder>` |   
  
### getErrorMessage()
    
    
    public abstract String getErrorMessage()

Output only. Error message is populated when an audience export fails during creation. A common reason for such a failure is quota exhaustion.

`optional string error_message = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The errorMessage.  
  
### getErrorMessageBytes()
    
    
    public abstract ByteString getErrorMessageBytes()

Output only. Error message is populated when an audience export fails during creation. A common reason for such a failure is quota exhaustion.

`optional string error_message = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for errorMessage.  
  
### getName()
    
    
    public abstract String getName()

Output only. Identifier. The audience export resource name assigned during creation. This resource name identifies this `AudienceExport`.

Format: `properties/{property}/audienceExports/{audience_export}`

` string name = 1 [(.google.api.field_behavior) = IDENTIFIER, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. Identifier. The audience export resource name assigned during creation. This resource name identifies this `AudienceExport`.

Format: `properties/{property}/audienceExports/{audience_export}`

` string name = 1 [(.google.api.field_behavior) = IDENTIFIER, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getPercentageCompleted()
    
    
    public abstract double getPercentageCompleted()

Output only. The percentage completed for this audience export ranging between 0 to 100.

`optional double percentage_completed = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[double](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The percentageCompleted.  
  
### getRowCount()
    
    
    public abstract int getRowCount()

Output only. The total number of rows in the AudienceExport result.

`optional int32 row_count = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The rowCount.  
  
### getState()
    
    
    public abstract AudienceExport.State getState()

Output only. The current state for this AudienceExport.

` optional .google.analytics.data.v1beta.AudienceExport.State state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[AudienceExport.State](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.AudienceExport.State)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. The current state for this AudienceExport.

` optional .google.analytics.data.v1beta.AudienceExport.State state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### hasBeginCreatingTime()
    
    
    public abstract boolean hasBeginCreatingTime()

Output only. The time when CreateAudienceExport was called and the AudienceExport began the `CREATING` state.

` optional .google.protobuf.Timestamp begin_creating_time = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the beginCreatingTime field is set.  
  
### hasErrorMessage()
    
    
    public abstract boolean hasErrorMessage()

Output only. Error message is populated when an audience export fails during creation. A common reason for such a failure is quota exhaustion.

`optional string error_message = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the errorMessage field is set.  
  
### hasPercentageCompleted()
    
    
    public abstract boolean hasPercentageCompleted()

Output only. The percentage completed for this audience export ranging between 0 to 100.

`optional double percentage_completed = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the percentageCompleted field is set.  
  
### hasRowCount()
    
    
    public abstract boolean hasRowCount()

Output only. The total number of rows in the AudienceExport result.

`optional int32 row_count = 8 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the rowCount field is set.  
  
### hasState()
    
    
    public abstract boolean hasState()

Output only. The current state for this AudienceExport.

` optional .google.analytics.data.v1beta.AudienceExport.State state = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the state field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
