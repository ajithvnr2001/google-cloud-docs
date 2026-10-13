---
url: https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai.evaluation.PairwiseMetric
title: Class PairwiseMetric (1.153.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:25.589058+00:00
---

# Class PairwiseMetric (1.153.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai.evaluation.PairwiseMetric

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class PairwiseMetric (1.153.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.153.1 (latest)  1.153.0  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0 
    
    
    PairwiseMetric(
        *,
        metric: str,
        metric_prompt_template: typing.Union[
            vertexai.evaluation.metrics.metric_prompt_template.PairwiseMetricPromptTemplate,
            str,
        ],
        baseline_model: typing.Optional[
            typing.Union[
                str, vertexai.generative_models.GenerativeModel, typing.Callable[[str], str]
            ]
        ] = None
    )

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
    

## Methods 

### PairwiseMetric
    
    
    PairwiseMetric(
        *,
        metric: str,
        metric_prompt_template: typing.Union[
            vertexai.evaluation.metrics.metric_prompt_template.PairwiseMetricPromptTemplate,
            str,
        ],
        baseline_model: typing.Optional[
            typing.Union[
                str, vertexai.generative_models.GenerativeModel, typing.Callable[[str], str]
            ]
        ] = None
    )

Initializes a pairwise evaluation metric.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
