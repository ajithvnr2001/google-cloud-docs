---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJobOrBuilder
title: Interface HyperparameterTuningJobOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:24.772675+00:00
---

# Interface HyperparameterTuningJobOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJobOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface HyperparameterTuningJobOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public interface HyperparameterTuningJobOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### containsLabels(String key)
    
    
    public abstract boolean containsLabels(String key)

The labels with user-defined metadata to organize HyperparameterTuningJobs.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information and examples of labels.

`map<string, string> labels = 16;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCreateTime()
    
    
    public abstract Timestamp getCreateTime()

Output only. Time when the HyperparameterTuningJob was created.

`.google.protobuf.Timestamp create_time = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The createTime.  
  
### getCreateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCreateTimeOrBuilder()

Output only. Time when the HyperparameterTuningJob was created.

`.google.protobuf.Timestamp create_time = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getDisplayName()
    
    
    public abstract String getDisplayName()

Required. The display name of the HyperparameterTuningJob. The name can be up to 128 characters long and can consist of any UTF-8 characters.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The displayName.  
  
### getDisplayNameBytes()
    
    
    public abstract ByteString getDisplayNameBytes()

Required. The display name of the HyperparameterTuningJob. The name can be up to 128 characters long and can consist of any UTF-8 characters.

`string display_name = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for displayName.  
  
### getEncryptionSpec()
    
    
    public abstract EncryptionSpec getEncryptionSpec()

Customer-managed encryption key options for a HyperparameterTuningJob. If this is set, then all resources created by the HyperparameterTuningJob will be encrypted with the provided encryption key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 17;`

**Returns**  
---  
**Type** | **Description**  
`[EncryptionSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EncryptionSpec)` | The encryptionSpec.  
  
### getEncryptionSpecOrBuilder()
    
    
    public abstract EncryptionSpecOrBuilder getEncryptionSpecOrBuilder()

Customer-managed encryption key options for a HyperparameterTuningJob. If this is set, then all resources created by the HyperparameterTuningJob will be encrypted with the provided encryption key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 17;`

**Returns**  
---  
**Type** | **Description**  
`[EncryptionSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.EncryptionSpecOrBuilder)` |   
  
### getEndTime()
    
    
    public abstract Timestamp getEndTime()

Output only. Time when the HyperparameterTuningJob entered any of the following states: `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`.

`.google.protobuf.Timestamp end_time = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The endTime.  
  
### getEndTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getEndTimeOrBuilder()

Output only. Time when the HyperparameterTuningJob entered any of the following states: `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`.

`.google.protobuf.Timestamp end_time = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getError()
    
    
    public abstract Status getError()

Output only. Only populated when job's state is JOB_STATE_FAILED or JOB_STATE_CANCELLED.

`.google.rpc.Status error = 15 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.Status` | The error.  
  
### getErrorOrBuilder()
    
    
    public abstract StatusOrBuilder getErrorOrBuilder()

Output only. Only populated when job's state is JOB_STATE_FAILED or JOB_STATE_CANCELLED.

`.google.rpc.Status error = 15 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`com.google.rpc.StatusOrBuilder` |   
  
### getLabels() (deprecated)
    
    
    public abstract Map<String,String> getLabels()

Use [#getLabelsMap()](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.HyperparameterTuningJobOrBuilder#com_google_cloud_aiplatform_v1_HyperparameterTuningJobOrBuilder_getLabelsMap__) instead.

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsCount()
    
    
    public abstract int getLabelsCount()

The labels with user-defined metadata to organize HyperparameterTuningJobs.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information and examples of labels.

`map<string, string> labels = 16;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getLabelsMap()
    
    
    public abstract Map<String,String> getLabelsMap()

The labels with user-defined metadata to organize HyperparameterTuningJobs.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information and examples of labels.

`map<string, string> labels = 16;`

**Returns**  
---  
**Type** | **Description**  
`[Map](https://docs.oracle.com/javase/8/docs/api/java/util/Map.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html),[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### getLabelsOrDefault(String key, String defaultValue)
    
    
    public abstract String getLabelsOrDefault(String key, String defaultValue)

The labels with user-defined metadata to organize HyperparameterTuningJobs.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information and examples of labels.

`map<string, string> labels = 16;`

**Parameters**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
`defaultValue` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getLabelsOrThrow(String key)
    
    
    public abstract String getLabelsOrThrow(String key)

The labels with user-defined metadata to organize HyperparameterTuningJobs.

Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed.

See <https://goo.gl/xmQnxf> for more information and examples of labels.

`map<string, string> labels = 16;`

**Parameter**  
---  
**Name** | **Description**  
`key` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### getMaxFailedTrialCount()
    
    
    public abstract int getMaxFailedTrialCount()

The number of failed Trials that need to be seen before failing the HyperparameterTuningJob.

If set to 0, Vertex AI decides how many Trials must fail before the whole job fails.

`int32 max_failed_trial_count = 7;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxFailedTrialCount.  
  
### getMaxTrialCount()
    
    
    public abstract int getMaxTrialCount()

Required. The desired total number of Trials.

`int32 max_trial_count = 5 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The maxTrialCount.  
  
### getName()
    
    
    public abstract String getName()

Output only. Resource name of the HyperparameterTuningJob.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Output only. Resource name of the HyperparameterTuningJob.

`string name = 1 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getParallelTrialCount()
    
    
    public abstract int getParallelTrialCount()

Required. The desired number of Trials to run in parallel.

`int32 parallel_trial_count = 6 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The parallelTrialCount.  
  
### getSatisfiesPzi()
    
    
    public abstract boolean getSatisfiesPzi()

Output only. Reserved for future use.

`bool satisfies_pzi = 20 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The satisfiesPzi.  
  
### getSatisfiesPzs()
    
    
    public abstract boolean getSatisfiesPzs()

Output only. Reserved for future use.

`bool satisfies_pzs = 19 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The satisfiesPzs.  
  
### getStartTime()
    
    
    public abstract Timestamp getStartTime()

Output only. Time when the HyperparameterTuningJob for the first time entered the `JOB_STATE_RUNNING` state.

`.google.protobuf.Timestamp start_time = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The startTime.  
  
### getStartTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getStartTimeOrBuilder()

Output only. Time when the HyperparameterTuningJob for the first time entered the `JOB_STATE_RUNNING` state.

`.google.protobuf.Timestamp start_time = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getState()
    
    
    public abstract JobState getState()

Output only. The detailed state of the job.

` .google.cloud.aiplatform.v1.JobState state = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[JobState](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.JobState)` | The state.  
  
### getStateValue()
    
    
    public abstract int getStateValue()

Output only. The detailed state of the job.

` .google.cloud.aiplatform.v1.JobState state = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for state.  
  
### getStudySpec()
    
    
    public abstract StudySpec getStudySpec()

Required. Study configuration of the HyperparameterTuningJob.

` .google.cloud.aiplatform.v1.StudySpec study_spec = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[StudySpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpec)` | The studySpec.  
  
### getStudySpecOrBuilder()
    
    
    public abstract StudySpecOrBuilder getStudySpecOrBuilder()

Required. Study configuration of the HyperparameterTuningJob.

` .google.cloud.aiplatform.v1.StudySpec study_spec = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[StudySpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.StudySpecOrBuilder)` |   
  
### getTrialJobSpec()
    
    
    public abstract CustomJobSpec getTrialJobSpec()

Required. The spec of a trial job. The same spec applies to the CustomJobs created in all the trials.

` .google.cloud.aiplatform.v1.CustomJobSpec trial_job_spec = 8 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[CustomJobSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJobSpec)` | The trialJobSpec.  
  
### getTrialJobSpecOrBuilder()
    
    
    public abstract CustomJobSpecOrBuilder getTrialJobSpecOrBuilder()

Required. The spec of a trial job. The same spec applies to the CustomJobs created in all the trials.

` .google.cloud.aiplatform.v1.CustomJobSpec trial_job_spec = 8 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[CustomJobSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.CustomJobSpecOrBuilder)` |   
  
### getTrials(int index)
    
    
    public abstract Trial getTrials(int index)

Output only. Trials of the HyperparameterTuningJob.

` repeated .google.cloud.aiplatform.v1.Trial trials = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Trial](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Trial)` |   
  
### getTrialsCount()
    
    
    public abstract int getTrialsCount()

Output only. Trials of the HyperparameterTuningJob.

` repeated .google.cloud.aiplatform.v1.Trial trials = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getTrialsList()
    
    
    public abstract List<Trial> getTrialsList()

Output only. Trials of the HyperparameterTuningJob.

` repeated .google.cloud.aiplatform.v1.Trial trials = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Trial](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.Trial)>` |   
  
### getTrialsOrBuilder(int index)
    
    
    public abstract TrialOrBuilder getTrialsOrBuilder(int index)

Output only. Trials of the HyperparameterTuningJob.

` repeated .google.cloud.aiplatform.v1.Trial trials = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[TrialOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1.TrialOrBuilder)` |   
  
### getTrialsOrBuilderList()
    
    
    public abstract List<? extends TrialOrBuilder> getTrialsOrBuilderList()

Output only. Trials of the HyperparameterTuningJob.

` repeated .google.cloud.aiplatform.v1.Trial trials = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.aiplatform.v1.TrialOrBuilder>` |   
  
### getUpdateTime()
    
    
    public abstract Timestamp getUpdateTime()

Output only. Time when the HyperparameterTuningJob was most recently updated.

`.google.protobuf.Timestamp update_time = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The updateTime.  
  
### getUpdateTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getUpdateTimeOrBuilder()

Output only. Time when the HyperparameterTuningJob was most recently updated.

`.google.protobuf.Timestamp update_time = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### hasCreateTime()
    
    
    public abstract boolean hasCreateTime()

Output only. Time when the HyperparameterTuningJob was created.

`.google.protobuf.Timestamp create_time = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the createTime field is set.  
  
### hasEncryptionSpec()
    
    
    public abstract boolean hasEncryptionSpec()

Customer-managed encryption key options for a HyperparameterTuningJob. If this is set, then all resources created by the HyperparameterTuningJob will be encrypted with the provided encryption key.

`.google.cloud.aiplatform.v1.EncryptionSpec encryption_spec = 17;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the encryptionSpec field is set.  
  
### hasEndTime()
    
    
    public abstract boolean hasEndTime()

Output only. Time when the HyperparameterTuningJob entered any of the following states: `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, `JOB_STATE_CANCELLED`.

`.google.protobuf.Timestamp end_time = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the endTime field is set.  
  
### hasError()
    
    
    public abstract boolean hasError()

Output only. Only populated when job's state is JOB_STATE_FAILED or JOB_STATE_CANCELLED.

`.google.rpc.Status error = 15 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the error field is set.  
  
### hasStartTime()
    
    
    public abstract boolean hasStartTime()

Output only. Time when the HyperparameterTuningJob for the first time entered the `JOB_STATE_RUNNING` state.

`.google.protobuf.Timestamp start_time = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the startTime field is set.  
  
### hasStudySpec()
    
    
    public abstract boolean hasStudySpec()

Required. Study configuration of the HyperparameterTuningJob.

` .google.cloud.aiplatform.v1.StudySpec study_spec = 4 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the studySpec field is set.  
  
### hasTrialJobSpec()
    
    
    public abstract boolean hasTrialJobSpec()

Required. The spec of a trial job. The same spec applies to the CustomJobs created in all the trials.

` .google.cloud.aiplatform.v1.CustomJobSpec trial_job_spec = 8 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the trialJobSpec field is set.  
  
### hasUpdateTime()
    
    
    public abstract boolean hasUpdateTime()

Output only. Time when the HyperparameterTuningJob was most recently updated.

`.google.protobuf.Timestamp update_time = 14 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
