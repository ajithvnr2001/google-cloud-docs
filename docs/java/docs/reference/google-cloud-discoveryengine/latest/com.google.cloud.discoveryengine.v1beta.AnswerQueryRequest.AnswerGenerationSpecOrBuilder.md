---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.AnswerQueryRequest.AnswerGenerationSpecOrBuilder
title: Interface AnswerQueryRequest.AnswerGenerationSpecOrBuilder (0.95.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:24:34.817437+00:00
---

# Interface AnswerQueryRequest.AnswerGenerationSpecOrBuilder (0.95.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.AnswerQueryRequest.AnswerGenerationSpecOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface AnswerQueryRequest.AnswerGenerationSpecOrBuilder (0.95.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.95.0 (latest)  0.91.0  0.90.0  0.89.0  0.87.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.68.0  0.66.0  0.64.0  0.63.0  0.60.0  0.59.0  0.58.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public static interface AnswerQueryRequest.AnswerGenerationSpecOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAnswerLanguageCode()
    
    
    public abstract String getAnswerLanguageCode()

Language code for Answer. Use language tags defined by [BCP47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). Note: This is an experimental feature.

`string answer_language_code = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The answerLanguageCode.  
  
### getAnswerLanguageCodeBytes()
    
    
    public abstract ByteString getAnswerLanguageCodeBytes()

Language code for Answer. Use language tags defined by [BCP47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt). Note: This is an experimental feature.

`string answer_language_code = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for answerLanguageCode.  
  
### getIgnoreAdversarialQuery()
    
    
    public abstract boolean getIgnoreAdversarialQuery()

Specifies whether to filter out adversarial queries. The default value is `false`.

Google employs search-query classification to detect adversarial queries. No answer is returned if the search query is classified as an adversarial query. For example, a user might ask a question regarding negative comments about the company or submit a query designed to generate unsafe, policy-violating output. If this field is set to `true`, we skip generating answers for adversarial queries and return fallback messages instead.

`bool ignore_adversarial_query = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ignoreAdversarialQuery.  
  
### getIgnoreJailBreakingQuery()
    
    
    public abstract boolean getIgnoreJailBreakingQuery()

Optional. Specifies whether to filter out jail-breaking queries. The default value is `false`.

Google employs search-query classification to detect jail-breaking queries. No summary is returned if the search query is classified as a jail-breaking query. A user might add instructions to the query to change the tone, style, language, content of the answer, or ask the model to act as a different entity, e.g. "Reply in the tone of a competing company's CEO". If this field is set to `true`, we skip generating summaries for jail-breaking queries and return fallback messages instead.

`bool ignore_jail_breaking_query = 8 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ignoreJailBreakingQuery.  
  
### getIgnoreLowRelevantContent()
    
    
    public abstract boolean getIgnoreLowRelevantContent()

Specifies whether to filter out queries that have low relevance.

If this field is set to `false`, all search results are used regardless of relevance to generate answers. If set to `true` or unset, the behavior will be determined automatically by the service.

`optional bool ignore_low_relevant_content = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ignoreLowRelevantContent.  
  
### getIgnoreNonAnswerSeekingQuery()
    
    
    public abstract boolean getIgnoreNonAnswerSeekingQuery()

Specifies whether to filter out queries that are not answer-seeking. The default value is `false`.

Google employs search-query classification to detect answer-seeking queries. No answer is returned if the search query is classified as a non-answer seeking query. If this field is set to `true`, we skip generating answers for non-answer seeking queries and return fallback messages instead.

`bool ignore_non_answer_seeking_query = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The ignoreNonAnswerSeekingQuery.  
  
### getIncludeCitations()
    
    
    public abstract boolean getIncludeCitations()

Specifies whether to include citation metadata in the answer. The default value is `false`.

`bool include_citations = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The includeCitations.  
  
### getModelSpec()
    
    
    public abstract AnswerQueryRequest.AnswerGenerationSpec.ModelSpec getModelSpec()

Answer generation model specification.

` .google.cloud.discoveryengine.v1beta.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec model_spec = 1; `

**Returns**  
---  
**Type** | **Description**  
`[AnswerQueryRequest.AnswerGenerationSpec.ModelSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec)` | The modelSpec.  
  
### getModelSpecOrBuilder()
    
    
    public abstract AnswerQueryRequest.AnswerGenerationSpec.ModelSpecOrBuilder getModelSpecOrBuilder()

Answer generation model specification.

` .google.cloud.discoveryengine.v1beta.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec model_spec = 1; `

**Returns**  
---  
**Type** | **Description**  
`[AnswerQueryRequest.AnswerGenerationSpec.ModelSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.AnswerQueryRequest.AnswerGenerationSpec.ModelSpecOrBuilder)` |   
  
### getMultimodalSpec()
    
    
    public abstract AnswerQueryRequest.AnswerGenerationSpec.MultimodalSpec getMultimodalSpec()

Optional. Multimodal specification.

` .google.cloud.discoveryengine.v1beta.AnswerQueryRequest.AnswerGenerationSpec.MultimodalSpec multimodal_spec = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AnswerQueryRequest.AnswerGenerationSpec.MultimodalSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.AnswerQueryRequest.AnswerGenerationSpec.MultimodalSpec)` | The multimodalSpec.  
  
### getMultimodalSpecOrBuilder()
    
    
    public abstract AnswerQueryRequest.AnswerGenerationSpec.MultimodalSpecOrBuilder getMultimodalSpecOrBuilder()

Optional. Multimodal specification.

` .google.cloud.discoveryengine.v1beta.AnswerQueryRequest.AnswerGenerationSpec.MultimodalSpec multimodal_spec = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[AnswerQueryRequest.AnswerGenerationSpec.MultimodalSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.AnswerQueryRequest.AnswerGenerationSpec.MultimodalSpecOrBuilder)` |   
  
### getPromptSpec()
    
    
    public abstract AnswerQueryRequest.AnswerGenerationSpec.PromptSpec getPromptSpec()

Answer generation prompt specification.

` .google.cloud.discoveryengine.v1beta.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec prompt_spec = 2; `

**Returns**  
---  
**Type** | **Description**  
`[AnswerQueryRequest.AnswerGenerationSpec.PromptSpec](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec)` | The promptSpec.  
  
### getPromptSpecOrBuilder()
    
    
    public abstract AnswerQueryRequest.AnswerGenerationSpec.PromptSpecOrBuilder getPromptSpecOrBuilder()

Answer generation prompt specification.

` .google.cloud.discoveryengine.v1beta.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec prompt_spec = 2; `

**Returns**  
---  
**Type** | **Description**  
`[AnswerQueryRequest.AnswerGenerationSpec.PromptSpecOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-discoveryengine/latest/com.google.cloud.discoveryengine.v1beta.AnswerQueryRequest.AnswerGenerationSpec.PromptSpecOrBuilder)` |   
  
### hasIgnoreLowRelevantContent()
    
    
    public abstract boolean hasIgnoreLowRelevantContent()

Specifies whether to filter out queries that have low relevance.

If this field is set to `false`, all search results are used regardless of relevance to generate answers. If set to `true` or unset, the behavior will be determined automatically by the service.

`optional bool ignore_low_relevant_content = 7;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the ignoreLowRelevantContent field is set.  
  
### hasModelSpec()
    
    
    public abstract boolean hasModelSpec()

Answer generation model specification.

` .google.cloud.discoveryengine.v1beta.AnswerQueryRequest.AnswerGenerationSpec.ModelSpec model_spec = 1; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the modelSpec field is set.  
  
### hasMultimodalSpec()
    
    
    public abstract boolean hasMultimodalSpec()

Optional. Multimodal specification.

` .google.cloud.discoveryengine.v1beta.AnswerQueryRequest.AnswerGenerationSpec.MultimodalSpec multimodal_spec = 9 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the multimodalSpec field is set.  
  
### hasPromptSpec()
    
    
    public abstract boolean hasPromptSpec()

Answer generation prompt specification.

` .google.cloud.discoveryengine.v1beta.AnswerQueryRequest.AnswerGenerationSpec.PromptSpec prompt_spec = 2; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the promptSpec field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
