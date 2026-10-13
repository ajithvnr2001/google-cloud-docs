---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ReleaseConfigOrBuilder
title: Interface ReleaseConfigOrBuilder (0.98.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:25:06.000372+00:00
---

# Interface ReleaseConfigOrBuilder (0.98.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ReleaseConfigOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ReleaseConfigOrBuilder (0.98.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.98.0 (latest)  0.94.0  0.93.0  0.92.0  0.90.0  0.87.0  0.86.0  0.84.0  0.82.0  0.81.0  0.80.0  0.79.0  0.77.0  0.75.0  0.74.0  0.73.0  0.72.0  0.71.0  0.69.0  0.67.0  0.66.0  0.63.0  0.62.0  0.61.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.4 
    
    
    public interface ReleaseConfigOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCodeCompilationConfig()
    
    
    public abstract CodeCompilationConfig getCodeCompilationConfig()

Optional. If set, fields of `code_compilation_config` override the default compilation settings that are specified in dataform.json.

` .google.cloud.dataform.v1.CodeCompilationConfig code_compilation_config = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CodeCompilationConfig](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CodeCompilationConfig)` | The codeCompilationConfig.  
  
### getCodeCompilationConfigOrBuilder()
    
    
    public abstract CodeCompilationConfigOrBuilder getCodeCompilationConfigOrBuilder()

Optional. If set, fields of `code_compilation_config` override the default compilation settings that are specified in dataform.json.

` .google.cloud.dataform.v1.CodeCompilationConfig code_compilation_config = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[CodeCompilationConfigOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.CodeCompilationConfigOrBuilder)` |   
  
### getCronSchedule()
    
    
    public abstract String getCronSchedule()

Optional. Optional schedule (in cron format) for automatic creation of compilation results.

`string cron_schedule = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The cronSchedule.  
  
### getCronScheduleBytes()
    
    
    public abstract ByteString getCronScheduleBytes()

Optional. Optional schedule (in cron format) for automatic creation of compilation results.

`string cron_schedule = 4 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for cronSchedule.  
  
### getDisabled()
    
    
    public abstract boolean getDisabled()

Optional. Disables automatic creation of compilation results.

`bool disabled = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The disabled.  
  
### getGitCommitish()
    
    
    public abstract String getGitCommitish()

Required. Git commit/tag/branch name at which the repository should be compiled. Must exist in the remote repository. Examples:

  * a commit SHA: `12ade345`
  * a tag: `tag1`
  * a branch name: `branch1`



`string git_commitish = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The gitCommitish.  
  
### getGitCommitishBytes()
    
    
    public abstract ByteString getGitCommitishBytes()

Required. Git commit/tag/branch name at which the repository should be compiled. Must exist in the remote repository. Examples:

  * a commit SHA: `12ade345`
  * a tag: `tag1`
  * a branch name: `branch1`



`string git_commitish = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for gitCommitish.  
  
### getInternalMetadata()
    
    
    public abstract String getInternalMetadata()

Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.

`optional string internal_metadata = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The internalMetadata.  
  
### getInternalMetadataBytes()
    
    
    public abstract ByteString getInternalMetadataBytes()

Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.

`optional string internal_metadata = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for internalMetadata.  
  
### getName()
    
    
    public abstract String getName()

Identifier. The release config's name.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Identifier. The release config's name.

`string name = 1 [(.google.api.field_behavior) = IDENTIFIER];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getRecentScheduledReleaseRecords(int index)
    
    
    public abstract ReleaseConfig.ScheduledReleaseRecord getRecentScheduledReleaseRecords(int index)

Output only. Records of the 10 most recent scheduled release attempts, ordered in descending order of `release_time`. Updated whenever automatic creation of a compilation result is triggered by cron_schedule.

` repeated .google.cloud.dataform.v1.ReleaseConfig.ScheduledReleaseRecord recent_scheduled_release_records = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReleaseConfig.ScheduledReleaseRecord](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ReleaseConfig.ScheduledReleaseRecord)` |   
  
### getRecentScheduledReleaseRecordsCount()
    
    
    public abstract int getRecentScheduledReleaseRecordsCount()

Output only. Records of the 10 most recent scheduled release attempts, ordered in descending order of `release_time`. Updated whenever automatic creation of a compilation result is triggered by cron_schedule.

` repeated .google.cloud.dataform.v1.ReleaseConfig.ScheduledReleaseRecord recent_scheduled_release_records = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getRecentScheduledReleaseRecordsList()
    
    
    public abstract List<ReleaseConfig.ScheduledReleaseRecord> getRecentScheduledReleaseRecordsList()

Output only. Records of the 10 most recent scheduled release attempts, ordered in descending order of `release_time`. Updated whenever automatic creation of a compilation result is triggered by cron_schedule.

` repeated .google.cloud.dataform.v1.ReleaseConfig.ScheduledReleaseRecord recent_scheduled_release_records = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ScheduledReleaseRecord](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ReleaseConfig.ScheduledReleaseRecord)>` |   
  
### getRecentScheduledReleaseRecordsOrBuilder(int index)
    
    
    public abstract ReleaseConfig.ScheduledReleaseRecordOrBuilder getRecentScheduledReleaseRecordsOrBuilder(int index)

Output only. Records of the 10 most recent scheduled release attempts, ordered in descending order of `release_time`. Updated whenever automatic creation of a compilation result is triggered by cron_schedule.

` repeated .google.cloud.dataform.v1.ReleaseConfig.ScheduledReleaseRecord recent_scheduled_release_records = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ReleaseConfig.ScheduledReleaseRecordOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-dataform/latest/com.google.cloud.dataform.v1.ReleaseConfig.ScheduledReleaseRecordOrBuilder)` |   
  
### getRecentScheduledReleaseRecordsOrBuilderList()
    
    
    public abstract List<? extends ReleaseConfig.ScheduledReleaseRecordOrBuilder> getRecentScheduledReleaseRecordsOrBuilderList()

Output only. Records of the 10 most recent scheduled release attempts, ordered in descending order of `release_time`. Updated whenever automatic creation of a compilation result is triggered by cron_schedule.

` repeated .google.cloud.dataform.v1.ReleaseConfig.ScheduledReleaseRecord recent_scheduled_release_records = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.dataform.v1.ReleaseConfig.ScheduledReleaseRecordOrBuilder>` |   
  
### getReleaseCompilationResult()
    
    
    public abstract String getReleaseCompilationResult()

Optional. The name of the currently released compilation result for this release config. This value is updated when a compilation result is automatically created from this release config (using cron_schedule), or when this resource is updated by API call (perhaps to roll back to an earlier release). The compilation result must have been created using this release config. Must be in the format `projects/*/locations/*/repositories/*/compilationResults/*`.

` string release_compilation_result = 6 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The releaseCompilationResult.  
  
### getReleaseCompilationResultBytes()
    
    
    public abstract ByteString getReleaseCompilationResultBytes()

Optional. The name of the currently released compilation result for this release config. This value is updated when a compilation result is automatically created from this release config (using cron_schedule), or when this resource is updated by API call (perhaps to roll back to an earlier release). The compilation result must have been created using this release config. Must be in the format `projects/*/locations/*/repositories/*/compilationResults/*`.

` string release_compilation_result = 6 [(.google.api.field_behavior) = OPTIONAL, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for releaseCompilationResult.  
  
### getTimeZone()
    
    
    public abstract String getTimeZone()

Optional. Specifies the time zone to be used when interpreting cron_schedule. Must be a time zone name from the [time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is `UTC`.

`string time_zone = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The timeZone.  
  
### getTimeZoneBytes()
    
    
    public abstract ByteString getTimeZoneBytes()

Optional. Specifies the time zone to be used when interpreting cron_schedule. Must be a time zone name from the [time zone database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones). If left unspecified, the default is `UTC`.

`string time_zone = 7 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for timeZone.  
  
### hasCodeCompilationConfig()
    
    
    public abstract boolean hasCodeCompilationConfig()

Optional. If set, fields of `code_compilation_config` override the default compilation settings that are specified in dataform.json.

` .google.cloud.dataform.v1.CodeCompilationConfig code_compilation_config = 3 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the codeCompilationConfig field is set.  
  
### hasInternalMetadata()
    
    
    public abstract boolean hasInternalMetadata()

Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.

`optional string internal_metadata = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the internalMetadata field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
