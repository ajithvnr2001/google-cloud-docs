---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UsageMetadataOrBuilder
title: Interface UsageMetadataOrBuilder (3.100.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:50.641333+00:00
---

# Interface UsageMetadataOrBuilder (3.100.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UsageMetadataOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface UsageMetadataOrBuilder (3.100.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.100.0 (latest)  3.96.0  3.95.0  3.94.0  3.92.0  3.89.0  3.88.0  3.86.0  3.84.0  3.83.0  3.82.0  3.81.0  3.79.0  3.77.0  3.76.0  3.75.0  3.74.0  3.73.0  3.71.0  3.69.0  3.68.0  3.65.0  3.64.0  3.63.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.2  3.3.0  3.2.0  3.0.0  2.9.8  2.8.9  2.7.4  2.5.3  2.4.0 
    
    
    public interface UsageMetadataOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCacheTokensDetails(int index)
    
    
    public abstract ModalityTokenCount getCacheTokensDetails(int index)

Output only. A detailed breakdown of the token count for each modality in the cached content.

` repeated .google.cloud.aiplatform.v1beta1.ModalityTokenCount cache_tokens_details = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModalityTokenCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModalityTokenCount)` |   
  
### getCacheTokensDetailsCount()
    
    
    public abstract int getCacheTokensDetailsCount()

Output only. A detailed breakdown of the token count for each modality in the cached content.

` repeated .google.cloud.aiplatform.v1beta1.ModalityTokenCount cache_tokens_details = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCacheTokensDetailsList()
    
    
    public abstract List<ModalityTokenCount> getCacheTokensDetailsList()

Output only. A detailed breakdown of the token count for each modality in the cached content.

` repeated .google.cloud.aiplatform.v1beta1.ModalityTokenCount cache_tokens_details = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ModalityTokenCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModalityTokenCount)>` |   
  
### getCacheTokensDetailsOrBuilder(int index)
    
    
    public abstract ModalityTokenCountOrBuilder getCacheTokensDetailsOrBuilder(int index)

Output only. A detailed breakdown of the token count for each modality in the cached content.

` repeated .google.cloud.aiplatform.v1beta1.ModalityTokenCount cache_tokens_details = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModalityTokenCountOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModalityTokenCountOrBuilder)` |   
  
### getCacheTokensDetailsOrBuilderList()
    
    
    public abstract List<? extends ModalityTokenCountOrBuilder> getCacheTokensDetailsOrBuilderList()

Output only. A detailed breakdown of the token count for each modality in the cached content.

` repeated .google.cloud.aiplatform.v1beta1.ModalityTokenCount cache_tokens_details = 10 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.aiplatform.v1beta1.ModalityTokenCountOrBuilder>` |   
  
### getCachedContentTokenCount()
    
    
    public abstract int getCachedContentTokenCount()

Output only. The number of tokens in the cached content that was used for this request.

`int32 cached_content_token_count = 5 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The cachedContentTokenCount.  
  
### getCandidatesTokenCount()
    
    
    public abstract int getCandidatesTokenCount()

The total number of tokens in the generated candidates.

`int32 candidates_token_count = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The candidatesTokenCount.  
  
### getCandidatesTokensDetails(int index)
    
    
    public abstract ModalityTokenCount getCandidatesTokensDetails(int index)

Output only. A detailed breakdown of the token count for each modality in the generated candidates.

` repeated .google.cloud.aiplatform.v1beta1.ModalityTokenCount candidates_tokens_details = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModalityTokenCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModalityTokenCount)` |   
  
### getCandidatesTokensDetailsCount()
    
    
    public abstract int getCandidatesTokensDetailsCount()

Output only. A detailed breakdown of the token count for each modality in the generated candidates.

` repeated .google.cloud.aiplatform.v1beta1.ModalityTokenCount candidates_tokens_details = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getCandidatesTokensDetailsList()
    
    
    public abstract List<ModalityTokenCount> getCandidatesTokensDetailsList()

Output only. A detailed breakdown of the token count for each modality in the generated candidates.

` repeated .google.cloud.aiplatform.v1beta1.ModalityTokenCount candidates_tokens_details = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ModalityTokenCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModalityTokenCount)>` |   
  
### getCandidatesTokensDetailsOrBuilder(int index)
    
    
    public abstract ModalityTokenCountOrBuilder getCandidatesTokensDetailsOrBuilder(int index)

Output only. A detailed breakdown of the token count for each modality in the generated candidates.

` repeated .google.cloud.aiplatform.v1beta1.ModalityTokenCount candidates_tokens_details = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModalityTokenCountOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModalityTokenCountOrBuilder)` |   
  
### getCandidatesTokensDetailsOrBuilderList()
    
    
    public abstract List<? extends ModalityTokenCountOrBuilder> getCandidatesTokensDetailsOrBuilderList()

Output only. A detailed breakdown of the token count for each modality in the generated candidates.

` repeated .google.cloud.aiplatform.v1beta1.ModalityTokenCount candidates_tokens_details = 11 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.aiplatform.v1beta1.ModalityTokenCountOrBuilder>` |   
  
### getPromptTokenCount()
    
    
    public abstract int getPromptTokenCount()

The total number of tokens in the prompt. This includes any text, images, or other media provided in the request. When `cached_content` is set, this also includes the number of tokens in the cached content.

`int32 prompt_token_count = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The promptTokenCount.  
  
### getPromptTokensDetails(int index)
    
    
    public abstract ModalityTokenCount getPromptTokensDetails(int index)

Output only. A detailed breakdown of the token count for each modality in the prompt.

` repeated .google.cloud.aiplatform.v1beta1.ModalityTokenCount prompt_tokens_details = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModalityTokenCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModalityTokenCount)` |   
  
### getPromptTokensDetailsCount()
    
    
    public abstract int getPromptTokensDetailsCount()

Output only. A detailed breakdown of the token count for each modality in the prompt.

` repeated .google.cloud.aiplatform.v1beta1.ModalityTokenCount prompt_tokens_details = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPromptTokensDetailsList()
    
    
    public abstract List<ModalityTokenCount> getPromptTokensDetailsList()

Output only. A detailed breakdown of the token count for each modality in the prompt.

` repeated .google.cloud.aiplatform.v1beta1.ModalityTokenCount prompt_tokens_details = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ModalityTokenCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModalityTokenCount)>` |   
  
### getPromptTokensDetailsOrBuilder(int index)
    
    
    public abstract ModalityTokenCountOrBuilder getPromptTokensDetailsOrBuilder(int index)

Output only. A detailed breakdown of the token count for each modality in the prompt.

` repeated .google.cloud.aiplatform.v1beta1.ModalityTokenCount prompt_tokens_details = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModalityTokenCountOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModalityTokenCountOrBuilder)` |   
  
### getPromptTokensDetailsOrBuilderList()
    
    
    public abstract List<? extends ModalityTokenCountOrBuilder> getPromptTokensDetailsOrBuilderList()

Output only. A detailed breakdown of the token count for each modality in the prompt.

` repeated .google.cloud.aiplatform.v1beta1.ModalityTokenCount prompt_tokens_details = 9 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.aiplatform.v1beta1.ModalityTokenCountOrBuilder>` |   
  
### getThoughtsTokenCount()
    
    
    public abstract int getThoughtsTokenCount()

Output only. The number of tokens that were part of the model's generated "thoughts" output, if applicable.

`int32 thoughts_token_count = 14 [(.google.api.field_behavior) = OUTPUT_ONLY];`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The thoughtsTokenCount.  
  
### getToolUsePromptTokenCount()
    
    
    public abstract int getToolUsePromptTokenCount()

Output only. The number of tokens in the results from tool executions, which are provided back to the model as input, if applicable.

`int32 tool_use_prompt_token_count = 13 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The toolUsePromptTokenCount.  
  
### getToolUsePromptTokensDetails(int index)
    
    
    public abstract ModalityTokenCount getToolUsePromptTokensDetails(int index)

Output only. A detailed breakdown by modality of the token counts from the results of tool executions, which are provided back to the model as input.

` repeated .google.cloud.aiplatform.v1beta1.ModalityTokenCount tool_use_prompt_tokens_details = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModalityTokenCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModalityTokenCount)` |   
  
### getToolUsePromptTokensDetailsCount()
    
    
    public abstract int getToolUsePromptTokensDetailsCount()

Output only. A detailed breakdown by modality of the token counts from the results of tool executions, which are provided back to the model as input.

` repeated .google.cloud.aiplatform.v1beta1.ModalityTokenCount tool_use_prompt_tokens_details = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getToolUsePromptTokensDetailsList()
    
    
    public abstract List<ModalityTokenCount> getToolUsePromptTokensDetailsList()

Output only. A detailed breakdown by modality of the token counts from the results of tool executions, which are provided back to the model as input.

` repeated .google.cloud.aiplatform.v1beta1.ModalityTokenCount tool_use_prompt_tokens_details = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[ModalityTokenCount](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModalityTokenCount)>` |   
  
### getToolUsePromptTokensDetailsOrBuilder(int index)
    
    
    public abstract ModalityTokenCountOrBuilder getToolUsePromptTokensDetailsOrBuilder(int index)

Output only. A detailed breakdown by modality of the token counts from the results of tool executions, which are provided back to the model as input.

` repeated .google.cloud.aiplatform.v1beta1.ModalityTokenCount tool_use_prompt_tokens_details = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[ModalityTokenCountOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.ModalityTokenCountOrBuilder)` |   
  
### getToolUsePromptTokensDetailsOrBuilderList()
    
    
    public abstract List<? extends ModalityTokenCountOrBuilder> getToolUsePromptTokensDetailsOrBuilderList()

Output only. A detailed breakdown by modality of the token counts from the results of tool executions, which are provided back to the model as input.

` repeated .google.cloud.aiplatform.v1beta1.ModalityTokenCount tool_use_prompt_tokens_details = 12 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.aiplatform.v1beta1.ModalityTokenCountOrBuilder>` |   
  
### getTotalTokenCount()
    
    
    public abstract int getTotalTokenCount()

The total number of tokens for the entire request. This is the sum of `prompt_token_count`, `candidates_token_count`, `tool_use_prompt_token_count`, and `thoughts_token_count`.

`int32 total_token_count = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The totalTokenCount.  
  
### getTrafficType()
    
    
    public abstract UsageMetadata.TrafficType getTrafficType()

Output only. The traffic type for this request.

` .google.cloud.aiplatform.v1beta1.UsageMetadata.TrafficType traffic_type = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[UsageMetadata.TrafficType](https://docs.cloud.google.com/java/docs/reference/google-cloud-aiplatform/latest/com.google.cloud.aiplatform.v1beta1.UsageMetadata.TrafficType)` | The trafficType.  
  
### getTrafficTypeValue()
    
    
    public abstract int getTrafficTypeValue()

Output only. The traffic type for this request.

` .google.cloud.aiplatform.v1beta1.UsageMetadata.TrafficType traffic_type = 8 [(.google.api.field_behavior) = OUTPUT_ONLY]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for trafficType.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
