---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.language_models
title: Module language_models (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:26.575765+00:00
---

# Module language_models (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.language_models

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Module language_models (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 

Classes for working with language models.

## Classes 

### [ChatMessage](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.language_models.ChatMessage)
    
    
    ChatMessage(content: str, author: str)

A chat message.

### [CountTokensResponse](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.language_models.CountTokensResponse)
    
    
    CountTokensResponse(
        total_tokens: int,
        total_billable_characters: int,
        _count_tokens_response: typing.Any,
    )

The response from a count_tokens request. .. attribute:: total_tokens

The total number of tokens counted across all instances passed to the request.

:type: int

### [EvaluationClassificationMetric](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.language_models.EvaluationClassificationMetric)
    
    
    EvaluationClassificationMetric(
        label_name: typing.Optional[str] = None,
        auPrc: typing.Optional[float] = None,
        auRoc: typing.Optional[float] = None,
        logLoss: typing.Optional[float] = None,
        confidenceMetrics: typing.Optional[
            typing.List[typing.Dict[str, typing.Any]]
        ] = None,
        confusionMatrix: typing.Optional[typing.Dict[str, typing.Any]] = None,
    )

The evaluation metric response for classification metrics.

**Parameters**  
---  
**Name** | **Description**  
`label_name` |  `str`   
Optional. The name of the label associated with the metrics. This is only returned when `only_summary_metrics=False` is passed to evaluate().  
`auPrc` |  `float`   
Optional. The area under the precision recall curve.  
`auRoc` |  `float`   
Optional. The area under the receiver operating characteristic curve.  
`logLoss` |  `float`   
Optional. Logarithmic loss.  
`confidenceMetrics` |  `List[Dict[str, Any]]`   
Optional. This is only returned when `only_summary_metrics=False` is passed to evaluate().  
`confusionMatrix` |  `Dict[str, Any]`   
Optional. This is only returned when `only_summary_metrics=False` is passed to evaluate().  
  
### [EvaluationMetric](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.language_models.EvaluationMetric)
    
    
    EvaluationMetric(
        bleu: typing.Optional[float] = None, rougeLSum: typing.Optional[float] = None
    )

The evaluation metric response.

**Parameters**  
---  
**Name** | **Description**  
`bleu` |  `float`   
Optional. BLEU (Bilingual evauation understudy). Scores based on sacrebleu implementation.  
`rougeLSum` |  `float`   
Optional. ROUGE-L (Longest Common Subsequence) scoring at summary level.  
  
### [EvaluationQuestionAnsweringSpec](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.language_models.EvaluationQuestionAnsweringSpec)
    
    
    EvaluationQuestionAnsweringSpec(
        ground_truth_data: typing.Union[typing.List[str], str, pandas.core.frame.DataFrame],
        task_name: str = "question-answering",
    )

Spec for question answering model evaluation tasks.

### [EvaluationTextClassificationSpec](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.language_models.EvaluationTextClassificationSpec)
    
    
    EvaluationTextClassificationSpec(
        ground_truth_data: typing.Union[typing.List[str], str, pandas.core.frame.DataFrame],
        target_column_name: str,
        class_names: typing.List[str],
    )

Spec for text classification model evaluation tasks.

**Parameters**  
---  
**Name** | **Description**  
`target_column_name` |  `str`   
Required. The label column in the dataset provided in `ground_truth_data`. Required when task_name='text-classification'.  
`class_names` |  `List[str]`   
Required. A list of all possible label names in your dataset. Required when task_name='text-classification'.  
  
### [EvaluationTextGenerationSpec](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.language_models.EvaluationTextGenerationSpec)
    
    
    EvaluationTextGenerationSpec(
        ground_truth_data: typing.Union[typing.List[str], str, pandas.core.frame.DataFrame],
    )

Spec for text generation model evaluation tasks.

### [EvaluationTextSummarizationSpec](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.language_models.EvaluationTextSummarizationSpec)
    
    
    EvaluationTextSummarizationSpec(
        ground_truth_data: typing.Union[typing.List[str], str, pandas.core.frame.DataFrame],
        task_name: str = "summarization",
    )

Spec for text summarization model evaluation tasks.

### [InputOutputTextPair](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.language_models.InputOutputTextPair)
    
    
    InputOutputTextPair(input_text: str, output_text: str)

InputOutputTextPair represents a pair of input and output texts.

### [TextEmbedding](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.language_models.TextEmbedding)
    
    
    TextEmbedding(
        values: typing.List[float],
        statistics: typing.Optional[
            vertexai.language_models.TextEmbeddingStatistics
        ] = None,
        _prediction_response: typing.Optional[
            google.cloud.aiplatform.models.Prediction
        ] = None,
    )

Text embedding vector and statistics.

### [TextEmbeddingInput](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.language_models.TextEmbeddingInput)
    
    
    TextEmbeddingInput(
        text: str,
        task_type: typing.Optional[str] = None,
        title: typing.Optional[str] = None,
    )

Structural text embedding input.

### [TextGenerationResponse](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.language_models.TextGenerationResponse)
    
    
    TextGenerationResponse(text: str, _prediction_response: typing.Any, is_blocked: bool = False, errors: typing.Tuple[int] = (), safety_attributes: typing.Dict[str, float] = <factory>, grounding_metadata: typing.Optional[vertexai.language_models._language_models.GroundingMetadata] = None)

TextGenerationResponse represents a response of a language model. .. attribute:: text

The generated text

:type: str

### [TuningEvaluationSpec](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.language_models.TuningEvaluationSpec)
    
    
    TuningEvaluationSpec(
        evaluation_data: typing.Optional[str] = None,
        evaluation_interval: typing.Optional[int] = None,
        enable_early_stopping: typing.Optional[bool] = None,
        enable_checkpoint_selection: typing.Optional[bool] = None,
        tensorboard: typing.Optional[
            typing.Union[
                google.cloud.aiplatform.tensorboard.tensorboard_resource.Tensorboard, str
            ]
        ] = None,
    )

Specification for model evaluation to perform during tuning.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
