---
url: https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai.evaluation.EvalTask
title: Class EvalTask (1.153.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:23.479633+00:00
---

# Class EvalTask (1.153.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai.evaluation.EvalTask

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class EvalTask (1.153.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.153.1 (latest)  1.153.0  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0 
    
    
    EvalTask(
        *,
        dataset: typing.Union[pd.DataFrame, str, typing.Dict[str, typing.Any]],
        metrics: typing.List[
            typing.Union[
                typing.Literal[
                    "exact_match",
                    "bleu",
                    "rouge_1",
                    "rouge_2",
                    "rouge_l",
                    "rouge_l_sum",
                    "tool_call_valid",
                    "tool_name_match",
                    "tool_parameter_key_match",
                    "tool_parameter_kv_match",
                ],
                vertexai.evaluation.CustomMetric,
                vertexai.evaluation.metrics._base._AutomaticMetric,
                vertexai.evaluation.metrics._base._TranslationMetric,
                vertexai.evaluation.metrics.pointwise_metric.PointwiseMetric,
                vertexai.evaluation.metrics.pairwise_metric.PairwiseMetric,
            ]
        ],
        experiment: typing.Optional[str] = None,
        metric_column_mapping: typing.Optional[typing.Dict[str, str]] = None,
        output_uri_prefix: typing.Optional[str] = ""
    )

A class representing an EvalTask.

An evaluation task assesses the ability of a Gen AI model, agent or application to perform a specific task in response to prompts. Each evaluation task includes an evaluation dataset, which can be a set of test cases and a set of metrics for assessment. These tasks provide the framework for running evaluations in a standardized and repeatable way, allowing for comparative assessment with varying run-specific parameters.

Dataset Details:
    
    
    Default dataset column names:
        * prompt_column_name: "prompt"
        * reference_column_name: "reference"
        * response_column_name: "response"
        * baseline_model_response_column_name: "baseline_model_response"
        * rubrics_column_name: "rubrics"
    
    
    Requirement for different use cases:
      * Bring-your-own-response (BYOR): You already have the data that you
          want to evaluate stored in the dataset. Response column name can be
          customized by providing `response_column_name` parameter, or in the
          `metric_column_mapping`. For BYOR pairwise evaluation, the baseline
          model response column name can be customized by providing
          `baseline_model_response_column_name` parameter, or
          in the `metric_column_mapping`. If the `response` column or
          `baseline_model_response` column is present while the
          corresponding model is specified, an error will be raised.
    
      * Perform model/agent inference without a prompt template: You have a dataset
          containing the input prompts to the model/agent and want to perform
          inference before evaluation. A column named `prompt` is required
          in the evaluation dataset and is used directly as input to the model/agent.
    
      * Perform model/agent inference with a prompt template: You have a dataset
          containing the input variables to the prompt template and want to
          assemble the prompts for inference. Evaluation dataset
          must contain column names corresponding to the variable names in
          the prompt template. For example, if prompt template is
          "Instruction: {instruction}, context: {context}", the dataset must
          contain `instruction` and `context` columns.
    

Metrics Details:
    
    
    The supported metrics descriptions, rating rubrics, and the required
    input variables can be found on the Vertex AI public documentation page.
    [Evaluation methods and metrics](https://cloud.google.com/vertex-ai/generative-ai/docs/models/determine-eval).
    

Usage Examples:
    
    
    1. To perform bring-your-own-response(BYOR) evaluation, provide the model
    responses in the `response` column in the dataset. If a pairwise metric is
    used for BYOR evaluation, provide the baseline model responses in the
    `baseline_model_response` column.
    
      ```
      eval_dataset = pd.DataFrame({
              "prompt"  : [...],
              "reference": [...],
              "response" : [...],
              "baseline_model_response": [...],
      })
      eval_task = EvalTask(
        dataset=eval_dataset,
        metrics=[
                "bleu",
                "rouge_l_sum",
                MetricPromptTemplateExamples.Pointwise.FLUENCY,
                MetricPromptTemplateExamples.Pairwise.SAFETY
        ],
        experiment="my-experiment",
      )
      eval_result = eval_task.evaluate(experiment_run_name="eval-experiment-run")
      ```
    
    2. To perform evaluation with Gemini model inference, specify the `model`
    parameter with a model name string. The input column name to the
    model is `prompt` and must be present in the dataset.
    
      ```
      eval_dataset = pd.DataFrame({
            "reference": [...],
            "prompt"  : [...],
      })
      result = EvalTask(
          dataset=eval_dataset,
          metrics=["exact_match", "bleu", "rouge_1", "rouge_l_sum"],
          experiment="my-experiment",
      ).evaluate(
          model="gemini-2.5-flash",
          experiment_run_name="gemini-eval-run"
      )
      ```
    
    3. If a `prompt_template` is specified, the `prompt` column is not required.
    Prompts can be assembled from the evaluation dataset, and all prompt
    template variable names must be present in the dataset columns.
      ```
      eval_dataset = pd.DataFrame({
          "context"    : [...],
          "instruction": [...],
      })
      result = EvalTask(
          dataset=eval_dataset,
          metrics=[MetricPromptTemplateExamples.Pointwise.SUMMARIZATION_QUALITY],
      ).evaluate(
          model="gemini-2.5-flash",
          prompt_template="{instruction}. Article: {context}. Summary:",
      )
      ```
    
    4. To perform evaluation with custom model inference, specify the `model`
    parameter with a custom inference function. The input column name to the
    custom inference function is `prompt` and must be present in the dataset.
    
      ```
      from openai import OpenAI
      client = OpenAI()
      def custom_model_fn(input: str) -> str:
        response = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
            {"role": "user", "content": input}
          ]
        )
        return response.choices[0].message.content
    
      eval_dataset = pd.DataFrame({
            "prompt"  : [...],
            "reference": [...],
      })
      result = EvalTask(
          dataset=eval_dataset,
          metrics=[MetricPromptTemplateExamples.Pointwise.SAFETY],
          experiment="my-experiment",
      ).evaluate(
          model=custom_model_fn,
          experiment_run_name="gpt-eval-run"
      )
      ```
    
    5. To perform pairwise metric evaluation with model inference step, specify
    the `baseline_model` input to a `PairwiseMetric` instance and the candidate
    `model` input to the `EvalTask.evaluate()` function. The input column name
    to both models is `prompt` and must be present in the dataset.
    
      ```
      baseline_model = "gemini-2.5-pro"
      candidate_model = "gemini-2.5-flash"
    
      pairwise_groundedness = PairwiseMetric(
          metric_prompt_template=MetricPromptTemplateExamples.get_prompt_template(
              "pairwise_groundedness"
          ),
          baseline_model=baseline_model,
      )
      eval_dataset = pd.DataFrame({
            "prompt"  : [...],
      })
      result = EvalTask(
          dataset=eval_dataset,
          metrics=[pairwise_groundedness],
          experiment="my-pairwise-experiment",
      ).evaluate(
          model=candidate_model,
          experiment_run_name="gemini-pairwise-eval-run",
      )
      ```
    

## Properties 

### dataset

Returns evaluation dataset.

### experiment

Returns experiment name.

### metrics

Returns metrics.

## Methods 

### EvalTask
    
    
    EvalTask(
        *,
        dataset: typing.Union[pd.DataFrame, str, typing.Dict[str, typing.Any]],
        metrics: typing.List[
            typing.Union[
                typing.Literal[
                    "exact_match",
                    "bleu",
                    "rouge_1",
                    "rouge_2",
                    "rouge_l",
                    "rouge_l_sum",
                    "tool_call_valid",
                    "tool_name_match",
                    "tool_parameter_key_match",
                    "tool_parameter_kv_match",
                ],
                vertexai.evaluation.CustomMetric,
                vertexai.evaluation.metrics._base._AutomaticMetric,
                vertexai.evaluation.metrics._base._TranslationMetric,
                vertexai.evaluation.metrics.pointwise_metric.PointwiseMetric,
                vertexai.evaluation.metrics.pairwise_metric.PairwiseMetric,
            ]
        ],
        experiment: typing.Optional[str] = None,
        metric_column_mapping: typing.Optional[typing.Dict[str, str]] = None,
        output_uri_prefix: typing.Optional[str] = ""
    )

Initializes an EvalTask.

### display_runs
    
    
    display_runs()

Displays experiment runs associated with this EvalTask.

### evaluate
    
    
    evaluate(
        *,
        model: typing.Optional[
            typing.Union[
                str, vertexai.generative_models.GenerativeModel, typing.Callable[[str], str]
            ]
        ] = None,
        prompt_template: typing.Optional[str] = None,
        experiment_run_name: typing.Optional[str] = None,
        response_column_name: typing.Optional[str] = None,
        baseline_model_response_column_name: typing.Optional[str] = None,
        evaluation_service_qps: typing.Optional[float] = None,
        retry_timeout: float = 120.0,
        output_file_name: typing.Optional[str] = None
    ) -> vertexai.evaluation.EvalResult

Runs an evaluation for the EvalTask.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
