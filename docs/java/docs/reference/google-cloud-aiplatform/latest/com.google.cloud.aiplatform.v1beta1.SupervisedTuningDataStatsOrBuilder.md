---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SupervisedTuningDataStatsOrBuilder
title: Interface SupervisedTuningDataStatsOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:20.261373+00:00
---

# Interface SupervisedTuningDataStatsOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SupervisedTuningDataStatsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface SupervisedTuningDataStatsOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public interface SupervisedTuningDataStatsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDroppedExampleReasons(int index)
    
    
    public abstract String getDroppedExampleReasons(int index)

Output only. For each index in `truncated_example_indices`, the user-facing reason why the example was dropped.

` repeated string dropped_example_reasons = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The droppedExampleReasons at the given index.  
  
### getDroppedExampleReasonsBytes(int index)
    
    
    public abstract ByteString getDroppedExampleReasonsBytes(int index)

Output only. For each index in `truncated_example_indices`, the user-facing reason why the example was dropped.

` repeated string dropped_example_reasons = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the droppedExampleReasons at the given index.  
  
### getDroppedExampleReasonsCount()
    
    
    public abstract int getDroppedExampleReasonsCount()

Output only. For each index in `truncated_example_indices`, the user-facing reason why the example was dropped.

` repeated string dropped_example_reasons = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of droppedExampleReasons.  
  
### getDroppedExampleReasonsList()
    
    
    public abstract List<String> getDroppedExampleReasonsList()

Output only. For each index in `truncated_example_indices`, the user-facing reason why the example was dropped.

` repeated string dropped_example_reasons = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the droppedExampleReasons.  
  
### getTotalBillableCharacterCount() (deprecated)
    
    
    public abstract long getTotalBillableCharacterCount()

**Deprecated.** _google.cloud.aiplatform.v1beta1.SupervisedTuningDataStats.total_billable_character_count is deprecated. See google/cloud/aiplatform/v1beta1/tuning_job.proto;l=280_

Output only. Number of billable characters in the tuning dataset.

` int64 total_billable_character_count = 3 [deprecated = true, (.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The totalBillableCharacterCount.  
  
### getTotalBillableTokenCount()
    
    
    public abstract long getTotalBillableTokenCount()

Output only. Number of billable tokens in the tuning dataset.

`int64 total_billable_token_count = 9 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The totalBillableTokenCount.  
  
### getTotalTruncatedExampleCount()
    
    
    public abstract long getTotalTruncatedExampleCount()

Output only. The number of examples in the dataset that have been dropped. An example can be dropped for reasons including: too many tokens, contains an invalid image, contains too many images, etc.

`int64 total_truncated_example_count = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The totalTruncatedExampleCount.  
  
### getTotalTuningCharacterCount()
    
    
    public abstract long getTotalTuningCharacterCount()

Output only. Number of tuning characters in the tuning dataset.

`int64 total_tuning_character_count = 2 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The totalTuningCharacterCount.  
  
### getTruncatedExampleIndices(int index)
    
    
    public abstract long getTruncatedExampleIndices(int index)

Output only. A partial sample of the indices (starting from 1) of the dropped examples.

` repeated int64 truncated_example_indices = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The truncatedExampleIndices at the given index.  
  
### getTruncatedExampleIndicesCount()
    
    
    public abstract int getTruncatedExampleIndicesCount()

Output only. A partial sample of the indices (starting from 1) of the dropped examples.

` repeated int64 truncated_example_indices = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of truncatedExampleIndices.  
  
### getTruncatedExampleIndicesList()
    
    
    public abstract List<Long> getTruncatedExampleIndicesList()

Output only. A partial sample of the indices (starting from 1) of the dropped examples.

` repeated int64 truncated_example_indices = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Long](https://docs.oracle.com/javase/8/docs/api/java/lang/Long.html)>` | A list containing the truncatedExampleIndices.  
  
### getTuningDatasetExampleCount()
    
    
    public abstract long getTuningDatasetExampleCount()

Output only. Number of examples in the tuning dataset.

`int64 tuning_dataset_example_count = 1 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The tuningDatasetExampleCount.  
  
### getTuningStepCount()
    
    
    public abstract long getTuningStepCount()

Output only. Number of tuning steps for this Tuning Job.

`int64 tuning_step_count = 4 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The tuningStepCount.  
  
### getUserDatasetExamples(int index)
    
    
    public abstract Content getUserDatasetExamples(int index)

Output only. Sample user messages in the training dataset uri.

` repeated .google.cloud.aiplatform.v1beta1.Content user_dataset_examples = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Content](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Content)` |   
  
### getUserDatasetExamplesCount()
    
    
    public abstract int getUserDatasetExamplesCount()

Output only. Sample user messages in the training dataset uri.

` repeated .google.cloud.aiplatform.v1beta1.Content user_dataset_examples = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getUserDatasetExamplesList()
    
    
    public abstract List<Content> getUserDatasetExamplesList()

Output only. Sample user messages in the training dataset uri.

` repeated .google.cloud.aiplatform.v1beta1.Content user_dataset_examples = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Content](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.Content)>` |   
  
### getUserDatasetExamplesOrBuilder(int index)
    
    
    public abstract ContentOrBuilder getUserDatasetExamplesOrBuilder(int index)

Output only. Sample user messages in the training dataset uri.

` repeated .google.cloud.aiplatform.v1beta1.Content user_dataset_examples = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ContentOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ContentOrBuilder)` |   
  
### getUserDatasetExamplesOrBuilderList()
    
    
    public abstract List<? extends ContentOrBuilder> getUserDatasetExamplesOrBuilderList()

Output only. Sample user messages in the training dataset uri.

` repeated .google.cloud.aiplatform.v1beta1.Content user_dataset_examples = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.aiplatform.v1beta1.ContentOrBuilder>` |   
  
### getUserInputTokenDistribution()
    
    
    public abstract SupervisedTuningDatasetDistribution getUserInputTokenDistribution()

Output only. Dataset distributions for the user input tokens.

` .google.cloud.aiplatform.v1beta1.SupervisedTuningDatasetDistribution user_input_token_distribution = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SupervisedTuningDatasetDistribution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SupervisedTuningDatasetDistribution)` | The userInputTokenDistribution.  
  
### getUserInputTokenDistributionOrBuilder()
    
    
    public abstract SupervisedTuningDatasetDistributionOrBuilder getUserInputTokenDistributionOrBuilder()

Output only. Dataset distributions for the user input tokens.

` .google.cloud.aiplatform.v1beta1.SupervisedTuningDatasetDistribution user_input_token_distribution = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SupervisedTuningDatasetDistributionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SupervisedTuningDatasetDistributionOrBuilder)` |   
  
### getUserMessagePerExampleDistribution()
    
    
    public abstract SupervisedTuningDatasetDistribution getUserMessagePerExampleDistribution()

Output only. Dataset distributions for the messages per example.

` .google.cloud.aiplatform.v1beta1.SupervisedTuningDatasetDistribution user_message_per_example_distribution = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SupervisedTuningDatasetDistribution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SupervisedTuningDatasetDistribution)` | The userMessagePerExampleDistribution.  
  
### getUserMessagePerExampleDistributionOrBuilder()
    
    
    public abstract SupervisedTuningDatasetDistributionOrBuilder getUserMessagePerExampleDistributionOrBuilder()

Output only. Dataset distributions for the messages per example.

` .google.cloud.aiplatform.v1beta1.SupervisedTuningDatasetDistribution user_message_per_example_distribution = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SupervisedTuningDatasetDistributionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SupervisedTuningDatasetDistributionOrBuilder)` |   
  
### getUserOutputTokenDistribution()
    
    
    public abstract SupervisedTuningDatasetDistribution getUserOutputTokenDistribution()

Output only. Dataset distributions for the user output tokens.

` .google.cloud.aiplatform.v1beta1.SupervisedTuningDatasetDistribution user_output_token_distribution = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SupervisedTuningDatasetDistribution](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SupervisedTuningDatasetDistribution)` | The userOutputTokenDistribution.  
  
### getUserOutputTokenDistributionOrBuilder()
    
    
    public abstract SupervisedTuningDatasetDistributionOrBuilder getUserOutputTokenDistributionOrBuilder()

Output only. Dataset distributions for the user output tokens.

` .google.cloud.aiplatform.v1beta1.SupervisedTuningDatasetDistribution user_output_token_distribution = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[SupervisedTuningDatasetDistributionOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.SupervisedTuningDatasetDistributionOrBuilder)` |   
  
### hasUserInputTokenDistribution()
    
    
    public abstract boolean hasUserInputTokenDistribution()

Output only. Dataset distributions for the user input tokens.

` .google.cloud.aiplatform.v1beta1.SupervisedTuningDatasetDistribution user_input_token_distribution = 5 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the userInputTokenDistribution field is set.  
  
### hasUserMessagePerExampleDistribution()
    
    
    public abstract boolean hasUserMessagePerExampleDistribution()

Output only. Dataset distributions for the messages per example.

` .google.cloud.aiplatform.v1beta1.SupervisedTuningDatasetDistribution user_message_per_example_distribution = 7 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the userMessagePerExampleDistribution field is set.  
  
### hasUserOutputTokenDistribution()
    
    
    public abstract boolean hasUserOutputTokenDistribution()

Output only. Dataset distributions for the user output tokens.

` .google.cloud.aiplatform.v1beta1.SupervisedTuningDatasetDistribution user_output_token_distribution = 6 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the userOutputTokenDistribution field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
