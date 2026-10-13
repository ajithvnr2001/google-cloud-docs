---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.evals.AsyncEvals
title: Class AsyncEvals (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:47.099664+00:00
---

# Class AsyncEvals (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.evals.AsyncEvals

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AsyncEvals (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    AsyncEvals(api_client_: google.genai._api_client.BaseApiClient)

API documentation for `AsyncEvals` class.

## Methods 

### batch_evaluate
    
    
    batch_evaluate(
        *,
        dataset: typing.Union[
            vertexai._genai.types.common.EvaluationDataset,
            vertexai._genai.types.common.EvaluationDatasetDict,
        ],
        metrics: list[
            typing.Union[
                vertexai._genai.types.common.Metric, vertexai._genai.types.common.MetricDict
            ]
        ],
        dest: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.EvaluateDatasetConfig,
                vertexai._genai.types.common.EvaluateDatasetConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.EvaluateDatasetOperation

Evaluates a dataset based on a set of given metrics.

### create_evaluation_experiment
    
    
    create_evaluation_experiment(
        *,
        display_name: typing.Optional[str] = None,
        labels: typing.Optional[dict[str, str]] = None,
        merge_strategy: typing.Optional[
            vertexai._genai.types.common.EvaluationExperimentMergeStrategy
        ] = None,
        metadata: typing.Optional[dict[str, typing.Any]] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CreateEvaluationExperimentConfig,
                vertexai._genai.types.common.CreateEvaluationExperimentConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.EvaluationExperiment

Creates an EvaluationExperiment.

### create_evaluation_item
    
    
    create_evaluation_item(
        *,
        evaluation_item_type: vertexai._genai.types.common.EvaluationItemType,
        gcs_uri: str,
        display_name: typing.Optional[str] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CreateEvaluationItemConfig,
                vertexai._genai.types.common.CreateEvaluationItemConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.EvaluationItem

Creates an EvaluationItem.

### create_evaluation_metric
    
    
    create_evaluation_metric(
        *,
        display_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        metric: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.Metric, vertexai._genai.types.common.MetricDict
            ]
        ] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CreateEvaluationMetricConfig,
                vertexai._genai.types.common.CreateEvaluationMetricConfigDict,
            ]
        ] = None
    ) -> str

Creates an EvaluationMetric.

### create_evaluation_run
    
    
    create_evaluation_run(
        *,
        dataset: typing.Union[
            vertexai._genai.types.common.EvaluationRunDataSource,
            vertexai._genai.types.common.EvaluationDataset,
        ],
        dest: str,
        metrics: list[
            typing.Union[
                vertexai._genai.types.common.EvaluationRunMetric,
                vertexai._genai.types.common.EvaluationRunMetricDict,
            ]
        ],
        name: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        evaluation_experiment: typing.Optional[str] = None,
        agent_info: typing.Optional[vertexai._genai.types.evals.AgentInfo] = None,
        agent: typing.Optional[str] = None,
        user_simulator_config: typing.Optional[
            typing.Union[
                vertexai._genai.types.evals.UserSimulatorConfig,
                vertexai._genai.types.evals.UserSimulatorConfigDict,
            ]
        ] = None,
        inference_configs: typing.Optional[
            dict[
                str,
                typing.Union[
                    vertexai._genai.types.common.EvaluationRunInferenceConfig,
                    vertexai._genai.types.common.EvaluationRunInferenceConfigDict,
                ],
            ]
        ] = None,
        red_teaming_config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RedTeamingAnalysisConfig,
                vertexai._genai.types.common.RedTeamingAnalysisConfigDict,
            ]
        ] = None,
        labels: typing.Optional[dict[str, str]] = None,
        loss_analysis_metrics: typing.Optional[
            list[
                typing.Union[
                    str,
                    vertexai._genai.types.common.Metric,
                    vertexai._genai.types.common.MetricDict,
                ]
            ]
        ] = None,
        loss_analysis_configs: typing.Optional[
            list[
                typing.Union[
                    vertexai._genai.types.common.LossAnalysisConfig,
                    vertexai._genai.types.common.LossAnalysisConfigDict,
                ]
            ]
        ] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CreateEvaluationRunConfig,
                vertexai._genai.types.common.CreateEvaluationRunConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.EvaluationRun

Creates an EvaluationRun.

### create_evaluation_set
    
    
    create_evaluation_set(
        *,
        evaluation_items: list[str],
        display_name: typing.Optional[str] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CreateEvaluationSetConfig,
                vertexai._genai.types.common.CreateEvaluationSetConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.EvaluationSet

Creates an EvaluationSet.

### delete_evaluation_experiment
    
    
    delete_evaluation_experiment(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteEvaluationExperimentConfig,
                vertexai._genai.types.common.DeleteEvaluationExperimentConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.DeleteEvaluationExperimentOperation

Deletes an EvaluationExperiment.

### delete_evaluation_metric
    
    
    delete_evaluation_metric(
        *,
        metric_resource_name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteEvaluationMetricConfig,
                vertexai._genai.types.common.DeleteEvaluationMetricConfigDict,
            ]
        ] = None
    ) -> None

Deletes an EvaluationMetric.

### evaluate_instances
    
    
    evaluate_instances(
        *, metric_config: vertexai._genai.types.common._EvaluateInstancesRequestParameters
    ) -> vertexai._genai.types.common.EvaluateInstancesResponse

Evaluates an instance of a model.

### generate_conversation_scenarios
    
    
    generate_conversation_scenarios(
        *,
        agent_info: typing.Union[
            vertexai._genai.types.evals.AgentInfo, vertexai._genai.types.evals.AgentInfoDict
        ],
        config: typing.Union[
            vertexai._genai.types.evals.UserScenarioGenerationConfig,
            vertexai._genai.types.evals.UserScenarioGenerationConfigDict,
        ],
        allow_cross_region_model: typing.Optional[bool] = None
    ) -> vertexai._genai.types.common.EvaluationDataset

Generates an evaluation dataset with user scenarios, which helps to generate conversations between a simulated user and the agent under test.

### generate_loss_clusters
    
    
    generate_loss_clusters(
        *,
        eval_result: vertexai._genai.types.common.EvaluationResult,
        metric: typing.Optional[
            typing.Union[
                str,
                vertexai._genai.types.common.Metric,
                vertexai._genai.types.common.MetricDict,
            ]
        ] = None,
        candidate: typing.Optional[str] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.LossAnalysisConfig,
                vertexai._genai.types.common.LossAnalysisConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.GenerateLossClustersResponse

Generates loss clusters from evaluation results.

Analyzes "Pass/Fail" signals from rubric-based autoraters and groups them into semantic "Loss Patterns" (e.g., "Hallucination of Action").

This method calls the GenerateLossClusters LRO and polls until completion, returning the results directly.

If `metric` or `candidate` are not provided, they will be auto-inferred from `eval_result` when unambiguous (i.e., when the eval result contains exactly one metric or one candidate). For multi-metric or multi-candidate evaluations, provide them explicitly.

Available candidate names can be found in `eval_result.metadata.candidate_names`.

Note: This API is only available in the `global` region.

### get_evaluation_experiment
    
    
    get_evaluation_experiment(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetEvaluationExperimentConfig,
                vertexai._genai.types.common.GetEvaluationExperimentConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.EvaluationExperiment

Retrieves an EvaluationExperiment from the resource name.

### get_evaluation_item
    
    
    get_evaluation_item(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetEvaluationItemConfig,
                vertexai._genai.types.common.GetEvaluationItemConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.EvaluationItem

Retrieves an EvaluationItem from the resource name.

### get_evaluation_metric
    
    
    get_evaluation_metric(
        *,
        metric_resource_name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetEvaluationMetricConfig,
                vertexai._genai.types.common.GetEvaluationMetricConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.EvaluationMetric

Retrieves an EvaluationMetric from the resource name.

### get_evaluation_run
    
    
    get_evaluation_run(
        *,
        name: str,
        include_evaluation_items: bool = False,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetEvaluationRunConfig,
                vertexai._genai.types.common.GetEvaluationRunConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.EvaluationRun

Retrieves the EvaluationRun from the resource name.

**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If the name is empty or invalid.  
  
### get_evaluation_set
    
    
    get_evaluation_set(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetEvaluationSetConfig,
                vertexai._genai.types.common.GetEvaluationSetConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.EvaluationSet

Retrieves an EvaluationSet from the resource name.

### list_evaluation_experiments
    
    
    list_evaluation_experiments(
        *,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListEvaluationExperimentsConfig,
                vertexai._genai.types.common.ListEvaluationExperimentsConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.ListEvaluationExperimentsResponse

Lists EvaluationExperiments.

### list_evaluation_metrics
    
    
    list_evaluation_metrics(
        *,
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListEvaluationMetricsConfig,
                vertexai._genai.types.common.ListEvaluationMetricsConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.ListEvaluationMetricsResponse

Lists EvaluationMetrics.

### update_evaluation_experiment
    
    
    update_evaluation_experiment(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.UpdateEvaluationExperimentConfig,
                vertexai._genai.types.common.UpdateEvaluationExperimentConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.EvaluationExperiment

Updates an EvaluationExperiment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
