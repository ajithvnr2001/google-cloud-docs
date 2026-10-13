---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.evaluation
title: Package evaluation (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:06.956564+00:00
---

# Package evaluation (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.evaluation

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package evaluation (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 

API documentation for `evaluation` package.

## Classes 

### [CustomMetric](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.evaluation.CustomMetric)

The custom evaluation metric.

A fully-customized CustomMetric that can be used to evaluate a single model by defining a metric function for a computation-based metric. The CustomMetric is computed on the client-side using the user-defined metric function in SDK only, not by the Vertex Gen AI Evaluation Service.

Attributes: name: The name of the metric. metric_function: The user-defined evaluation function to compute a metric score. Must use the dataset row dictionary as the metric function input and return per-instance metric result as a dictionary output. The metric score must mapped to the name of the CustomMetric as key.

### [EvalResult](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.evaluation.EvalResult)

Evaluation result.

### [EvalTask](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.evaluation.EvalTask)

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
    

### [MetricPromptTemplateExamples](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.evaluation.MetricPromptTemplateExamples)

Examples of metric prompt templates for model-based evaluation.

### [PairwiseMetric](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.evaluation.PairwiseMetric)

A Model-based Pairwise Metric.

A model-based evaluation metric that compares two generative models' responses side-by-side, and allows users to A/B test their generative models to determine which model is performing better.

For more details on when to use pairwise metrics, see [Evaluation methods and metrics](https://cloud.google.com/vertex-ai/generative-ai/docs/models/determine-eval#pointwise_versus_pairwise).

Result Details:
    
    
    * In `EvalResult.summary_metrics`, win rates for both the baseline and
    candidate model are computed. The win rate is computed as proportion of
    wins of one model's responses to total attempts as a decimal value
    between 0 and 1.
    
    * In `EvalResult.metrics_table`, a pairwise metric produces two
    evaluation results per dataset row:
        * `pairwise_choice`: The choice shows whether the candidate model or
          the baseline model performs better, or if they are equally good.
        * `explanation`: The rationale behind each verdict using
          chain-of-thought reasoning. The explanation helps users scrutinize
          the judgment and builds appropriate trust in the decisions.
    
    See [documentation
    page](https://cloud.google.com/vertex-ai/generative-ai/docs/models/determine-eval#understand-results)
    for more details on understanding the metric results.
    

Usage Examples:
    
    
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
    pairwise_task = EvalTask(
        dataset=eval_dataset,
        metrics=[pairwise_groundedness],
        experiment="my-pairwise-experiment",
    )
    pairwise_result = pairwise_task.evaluate(
        model=candidate_model,
        experiment_run_name="gemini-pairwise-eval-run",
    )
    ```
    

### [PairwiseMetricPromptTemplate](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.evaluation.PairwiseMetricPromptTemplate)

Pairwise metric prompt template for pairwise model-based metrics.

### [PointwiseMetric](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.evaluation.PointwiseMetric)

A Model-based Pointwise Metric.

A model-based evaluation metric that evaluate a single generative model's response.

For more details on when to use model-based pointwise metrics, see [Evaluation methods and metrics](https://cloud.google.com/vertex-ai/generative-ai/docs/models/determine-eval).

Usage Examples:
    
    
    ```
    candidate_model = "gemini-2.5-pro"
    eval_dataset = pd.DataFrame({
        "prompt"  : [...],
    })
    fluency_metric = PointwiseMetric(
        metric="fluency",
        metric_prompt_template=MetricPromptTemplateExamples.get_prompt_template('fluency'),
    )
    pointwise_eval_task = EvalTask(
        dataset=eval_dataset,
        metrics=[
            fluency_metric,
            MetricPromptTemplateExamples.Pointwise.GROUNDEDNESS,
        ],
    )
    pointwise_result = pointwise_eval_task.evaluate(
        model=candidate_model,
    )
    ```
    

### [PointwiseMetricPromptTemplate](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.evaluation.PointwiseMetricPromptTemplate)

Pointwise metric prompt template for pointwise model-based metrics.

### [PromptTemplate](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.evaluation.PromptTemplate)

A prompt template for creating prompts with variables.

The `PromptTemplate` class allows users to define a template string with variables represented in curly braces `{variable}`. The variable names cannot contain spaces and must start with a letter or underscore, followed by letters, digits, or underscore. These variables can be replaced with specific values using the `assemble` method, providing flexibility in generating dynamic prompts.

Usage:
    
    
    ```
    template_str = "Hello, {name}! Today is {day}. How are you?"
    prompt_template = PromptTemplate(template_str)
    completed_prompt = prompt_template.assemble(name="John", day="Monday")
    print(completed_prompt)
    ```
    

### [Rouge](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.evaluation.Rouge)

The ROUGE Metric.

Calculates the recall of n-grams in prediction as compared to reference and returns a score ranging between 0 and 1. Supported rouge types are rougen[1-9], rougeL, and rougeLsum.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
