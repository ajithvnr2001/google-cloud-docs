---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/summary_method/
title: Package Methods (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:01.362919+00:00
---

# Package Methods (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 

Summary of entries of Methods for aiplatform.

## 

### vertexai.init
    
    
    init(
        *,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        experiment: typing.Optional[str] = None,
        experiment_description: typing.Optional[str] = None,
        experiment_tensorboard: typing.Optional[
            typing.Union[
                str,
                google.cloud.aiplatform.tensorboard.tensorboard_resource.Tensorboard,
                bool,
            ]
        ] = None,
        staging_bucket: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        network: typing.Optional[str] = None,
        service_account: typing.Optional[str] = None,
        api_endpoint: typing.Optional[str] = None,
        api_key: typing.Optional[str] = None,
        api_transport: typing.Optional[str] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = None
    )

Updates common initialization parameters with provided options.

See more: [vertexai.init](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai#vertexai_init)

### vertexai.agent_engines.create
    
    
    create(
        agent_engine: typing.Union[
            None,
            vertexai.agent_engines.AsyncQueryable,
            vertexai.agent_engines.AsyncStreamQueryable,
            vertexai.agent_engines._agent_engines.BidiStreamQueryable,
            vertexai.agent_engines.OperationRegistrable,
            vertexai.agent_engines.Queryable,
            vertexai.agent_engines.StreamQueryable,
        ] = None,
        *,
        requirements: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        display_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        gcs_dir_name: typing.Optional[str] = None,
        extra_packages: typing.Optional[typing.Sequence[str]] = None,
        env_vars: typing.Optional[
            typing.Union[
                typing.Sequence[str],
                typing.Dict[
                    str,
                    typing.Union[str, google.cloud.aiplatform_v1.types.env_var.SecretRef],
                ],
            ]
        ] = None,
        build_options: typing.Optional[typing.Dict[str, typing.Sequence[str]]] = None,
        service_account: typing.Optional[str] = None,
        identity_type: typing.Optional[
            typing.Union[
                str,
                google.cloud.aiplatform_v1.types.reasoning_engine.ReasoningEngineSpec.IdentityType,
            ]
        ] = None,
        psc_interface_config: typing.Optional[
            google.cloud.aiplatform_v1.types.service_networking.PscInterfaceConfig
        ] = None,
        min_instances: typing.Optional[int] = None,
        max_instances: typing.Optional[int] = None,
        resource_limits: typing.Optional[typing.Dict[str, str]] = None,
        container_concurrency: typing.Optional[int] = None,
        encryption_spec: typing.Optional[
            google.cloud.aiplatform_v1.types.encryption_spec.EncryptionSpec
        ] = None
    ) -> vertexai.agent_engines.AgentEngine

Creates a new Agent Engine.

See more: [vertexai.agent_engines.create](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines#vertexai_agent_engines_create)

### vertexai.agent_engines.delete
    
    
    delete(resource_name: str, *, force: bool = False, **kwargs) -> None

Delete an Agent Engine resource.

See more: [vertexai.agent_engines.delete](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines#vertexai_agent_engines_delete)

### vertexai.agent_engines.get
    
    
    get(resource_name: str) -> vertexai.agent_engines.AgentEngine

Retrieves an Agent Engine resource.

See more: [vertexai.agent_engines.get](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines#vertexai_agent_engines_get)

### vertexai.agent_engines.list
    
    
    list(*, filter: str = "") -> typing.Iterable[vertexai.agent_engines.AgentEngine]

List all instances of Agent Engine matching the filter.

See more: [vertexai.agent_engines.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines#vertexai_agent_engines_list)

### vertexai.agent_engines.update
    
    
    update(
        resource_name: str,
        *,
        agent_engine: typing.Optional[
            typing.Union[
                vertexai.agent_engines.Queryable,
                vertexai.agent_engines.OperationRegistrable,
            ]
        ] = None,
        requirements: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        display_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        gcs_dir_name: typing.Optional[str] = None,
        extra_packages: typing.Optional[typing.Sequence[str]] = None,
        env_vars: typing.Optional[
            typing.Union[
                typing.Sequence[str],
                typing.Dict[
                    str,
                    typing.Union[str, google.cloud.aiplatform_v1.types.env_var.SecretRef],
                ],
            ]
        ] = None,
        build_options: typing.Optional[typing.Dict[str, typing.Sequence[str]]] = None,
        service_account: typing.Optional[str] = None,
        identity_type: typing.Optional[
            typing.Union[
                str,
                google.cloud.aiplatform_v1.types.reasoning_engine.ReasoningEngineSpec.IdentityType,
            ]
        ] = None,
        psc_interface_config: typing.Optional[
            google.cloud.aiplatform_v1.types.service_networking.PscInterfaceConfig
        ] = None,
        min_instances: typing.Optional[int] = None,
        max_instances: typing.Optional[int] = None,
        resource_limits: typing.Optional[typing.Dict[str, str]] = None,
        container_concurrency: typing.Optional[int] = None,
        encryption_spec: typing.Optional[
            google.cloud.aiplatform_v1.types.encryption_spec.EncryptionSpec
        ] = None
    ) -> vertexai.agent_engines.AgentEngine

Updates an existing Agent Engine.

See more: [vertexai.agent_engines.update](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines#vertexai_agent_engines_update)

### vertexai.preview.end_run
    
    
    end_run(
        state: google.cloud.aiplatform_v1.types.execution.Execution.State = State.COMPLETE,
    )

Ends the the current experiment run.

See more: [vertexai.preview.end_run](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview#vertexai_preview_end_run)

### vertexai.preview.get_experiment_df
    
    
    get_experiment_df(
        experiment: typing.Optional[str] = None, *, include_time_series: bool = True
    ) -> pd.DataFrame

Returns a Pandas DataFrame of the parameters and metrics associated with one experiment.

See more: [vertexai.preview.get_experiment_df](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview#vertexai_preview_get_experiment_df)

### vertexai.preview.log_classification_metrics
    
    
    log_classification_metrics(
        *,
        labels: typing.Optional[typing.List[str]] = None,
        matrix: typing.Optional[typing.List[typing.List[int]]] = None,
        fpr: typing.Optional[typing.List[float]] = None,
        tpr: typing.Optional[typing.List[float]] = None,
        threshold: typing.Optional[typing.List[float]] = None,
        display_name: typing.Optional[str] = None
    ) -> (
        google.cloud.aiplatform.metadata.schema.google.artifact_schema.ClassificationMetrics
    )

Create an artifact for classification metrics and log to ExperimentRun.

See more: [vertexai.preview.log_classification_metrics](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview#vertexai_preview_log_classification_metrics)

### vertexai.preview.log_metrics
    
    
    log_metrics(metrics: typing.Dict[str, typing.Union[float, int, str]])

Log single or multiple Metrics with specified key and value pairs.

See more: [vertexai.preview.log_metrics](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview#vertexai_preview_log_metrics)

### vertexai.preview.log_params
    
    
    log_params(params: typing.Dict[str, typing.Union[float, int, str]])

Log single or multiple parameters with specified key and value pairs.

See more: [vertexai.preview.log_params](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview#vertexai_preview_log_params)

### vertexai.preview.log_time_series_metrics
    
    
    log_time_series_metrics(
        metrics: typing.Dict[str, float],
        step: typing.Optional[int] = None,
        wall_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
    )

Logs time series metrics to to this Experiment Run.

See more: [vertexai.preview.log_time_series_metrics](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview#vertexai_preview_log_time_series_metrics)

### vertexai.preview.start_run
    
    
    start_run(
        run: str,
        *,
        tensorboard: typing.Optional[
            typing.Union[
                google.cloud.aiplatform.tensorboard.tensorboard_resource.Tensorboard, str
            ]
        ] = None,
        resume=False
    ) -> google.cloud.aiplatform.metadata.experiment_run_resource.ExperimentRun

Start a run to current session.

See more: [vertexai.preview.start_run](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview#vertexai_preview_start_run)

### vertexai.preview.tuning.sft.preview_train
    
    
    preview_train(
        *,
        source_model: typing.Union[
            str,
            vertexai.generative_models.GenerativeModel,
            vertexai.preview.tuning._tuning.SourceModel,
        ],
        train_dataset: typing.Union[
            str, google.cloud.aiplatform.preview.datasets.MultimodalDataset
        ],
        validation_dataset: typing.Optional[
            typing.Union[str, google.cloud.aiplatform.preview.datasets.MultimodalDataset]
        ] = None,
        tuned_model_display_name: typing.Optional[str] = None,
        tuning_mode: typing.Optional[typing.Literal["FULL", "PEFT_ADAPTER"]] = None,
        epochs: typing.Optional[int] = None,
        learning_rate: typing.Optional[float] = None,
        learning_rate_multiplier: typing.Optional[float] = None,
        adapter_size: typing.Optional[typing.Literal[1, 4, 8, 16, 32]] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        output_uri: typing.Optional[str] = None
    ) -> vertexai.preview.tuning._supervised_tuning.SupervisedTuningJob

Tunes a model using supervised training.

See more: [vertexai.preview.tuning.sft.preview_train](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.tuning.sft#vertexai_preview_tuning_sft_preview_train)

### vertexai.preview.tuning.sft.rebase_tuned_model
    
    
    rebase_tuned_model(
        tuned_model_ref: str,
        *,
        artifact_destination: typing.Optional[str] = None,
        deploy_to_same_endpoint: typing.Optional[bool] = False
    )

Re-runs fine tuning on top of a new foundational model.

See more: [vertexai.preview.tuning.sft.rebase_tuned_model](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.tuning.sft#vertexai_preview_tuning_sft_rebase_tuned_model)

### vertexai.preview.tuning.sft.train
    
    
    train(
        *,
        source_model: typing.Union[
            str,
            vertexai.generative_models.GenerativeModel,
            vertexai.tuning._tuning.SourceModel,
        ],
        train_dataset: typing.Union[
            str, google.cloud.aiplatform.preview.datasets.MultimodalDataset
        ],
        validation_dataset: typing.Optional[
            typing.Union[str, google.cloud.aiplatform.preview.datasets.MultimodalDataset]
        ] = None,
        tuned_model_display_name: typing.Optional[str] = None,
        tuning_mode: typing.Optional[typing.Literal["FULL", "PEFT_ADAPTER"]] = None,
        epochs: typing.Optional[int] = None,
        learning_rate: typing.Optional[float] = None,
        learning_rate_multiplier: typing.Optional[float] = None,
        adapter_size: typing.Optional[typing.Literal[1, 4, 8, 16, 32]] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        output_uri: typing.Optional[str] = None
    ) -> vertexai.tuning._supervised_tuning.SupervisedTuningJob

Tunes a model using supervised training.

See more: [vertexai.preview.tuning.sft.train](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.tuning.sft#vertexai_preview_tuning_sft_train)

### vertexai.Client
    
    
    Client(
        *,
        api_key: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        debug_config: typing.Optional[google.genai.client.DebugConfig] = None,
        http_options: typing.Optional[
            typing.Union[google.genai.types.HttpOptions, google.genai.types.HttpOptionsDict]
        ] = None
    )

Initializes the client.

See more: [vertexai.Client](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.Client#vertexai_Client_Client)

### vertexai._genai.agent_engines.AgentEngines.append_session_event
    
    
    append_session_event(
        *,
        name: str,
        author: str,
        invocation_id: str,
        timestamp: datetime.datetime,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.AppendAgentEngineSessionEventConfig,
                vertexai._genai.types.common.AppendAgentEngineSessionEventConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AppendAgentEngineSessionEventResponse

Deprecated.

See more: [vertexai._genai.agent_engines.AgentEngines.append_session_event](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AgentEngines#vertexai__genai_agent_engines_AgentEngines_append_session_event)

### vertexai._genai.agent_engines.AgentEngines.cancel_query_job
    
    
    cancel_query_job(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CancelQueryJobAgentEngineConfig,
                vertexai._genai.types.common.CancelQueryJobAgentEngineConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.CancelQueryJobResult

Cancels a long-running query job on an Agent Engine.

See more: [vertexai._genai.agent_engines.AgentEngines.cancel_query_job](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AgentEngines#vertexai__genai_agent_engines_AgentEngines_cancel_query_job)

### vertexai._genai.agent_engines.AgentEngines.check_query_job
    
    
    check_query_job(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CheckQueryJobAgentEngineConfig,
                vertexai._genai.types.common.CheckQueryJobAgentEngineConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.CheckQueryJobResult

Checks a query job on an agent engine and optionally returns the results.

See more: [vertexai._genai.agent_engines.AgentEngines.check_query_job](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AgentEngines#vertexai__genai_agent_engines_AgentEngines_check_query_job)

### vertexai._genai.agent_engines.AgentEngines.create
    
    
    create(
        *,
        agent_engine: typing.Optional[typing.Any] = None,
        agent: typing.Optional[typing.Any] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.AgentEngineConfig,
                vertexai._genai.types.common.AgentEngineConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngine

Creates an agent engine.

See more: [vertexai._genai.agent_engines.AgentEngines.create](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AgentEngines#vertexai__genai_agent_engines_AgentEngines_create)

### vertexai._genai.agent_engines.AgentEngines.create_memory
    
    
    create_memory(
        *,
        name: str,
        fact: str,
        scope: dict[str, str],
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.AgentEngineMemoryConfig,
                vertexai._genai.types.common.AgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngineMemoryOperation

Deprecated.

See more: [vertexai._genai.agent_engines.AgentEngines.create_memory](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AgentEngines#vertexai__genai_agent_engines_AgentEngines_create_memory)

### vertexai._genai.agent_engines.AgentEngines.create_session
    
    
    create_session(
        *,
        name: str,
        user_id: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CreateAgentEngineSessionConfig,
                vertexai._genai.types.common.CreateAgentEngineSessionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngineSessionOperation

Deprecated.

See more: [vertexai._genai.agent_engines.AgentEngines.create_session](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AgentEngines#vertexai__genai_agent_engines_AgentEngines_create_session)

### vertexai._genai.agent_engines.AgentEngines.delete
    
    
    delete(
        *,
        name: str,
        force: typing.Optional[bool] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteAgentEngineConfig,
                vertexai._genai.types.common.DeleteAgentEngineConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.DeleteAgentEngineOperation

Delete an Agent Engine resource.

See more: [vertexai._genai.agent_engines.AgentEngines.delete](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AgentEngines#vertexai__genai_agent_engines_AgentEngines_delete)

### vertexai._genai.agent_engines.AgentEngines.delete_memory
    
    
    delete_memory(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteAgentEngineMemoryConfig,
                vertexai._genai.types.common.DeleteAgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.DeleteAgentEngineMemoryOperation

Deprecated.

See more: [vertexai._genai.agent_engines.AgentEngines.delete_memory](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AgentEngines#vertexai__genai_agent_engines_AgentEngines_delete_memory)

### vertexai._genai.agent_engines.AgentEngines.delete_session
    
    
    delete_session(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteAgentEngineSessionConfig,
                vertexai._genai.types.common.DeleteAgentEngineSessionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.DeleteAgentEngineSessionOperation

Deprecated.

See more: [vertexai._genai.agent_engines.AgentEngines.delete_session](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AgentEngines#vertexai__genai_agent_engines_AgentEngines_delete_session)

### vertexai._genai.agent_engines.AgentEngines.generate_memories
    
    
    generate_memories(
        *,
        name: str,
        vertex_session_source: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GenerateMemoriesRequestVertexSessionSource,
                vertexai._genai.types.common.GenerateMemoriesRequestVertexSessionSourceDict,
            ]
        ] = None,
        direct_contents_source: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GenerateMemoriesRequestDirectContentsSource,
                vertexai._genai.types.common.GenerateMemoriesRequestDirectContentsSourceDict,
            ]
        ] = None,
        direct_memories_source: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GenerateMemoriesRequestDirectMemoriesSource,
                vertexai._genai.types.common.GenerateMemoriesRequestDirectMemoriesSourceDict,
            ]
        ] = None,
        scope: typing.Optional[dict[str, str]] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GenerateAgentEngineMemoriesConfig,
                vertexai._genai.types.common.GenerateAgentEngineMemoriesConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngineGenerateMemoriesOperation

Deprecated.

See more: [vertexai._genai.agent_engines.AgentEngines.generate_memories](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AgentEngines#vertexai__genai_agent_engines_AgentEngines_generate_memories)

### vertexai._genai.agent_engines.AgentEngines.get
    
    
    get(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetAgentEngineConfig,
                vertexai._genai.types.common.GetAgentEngineConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngine

Gets an agent engine.

See more: [vertexai._genai.agent_engines.AgentEngines.get](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AgentEngines#vertexai__genai_agent_engines_AgentEngines_get)

### vertexai._genai.agent_engines.AgentEngines.get_memory
    
    
    get_memory(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetAgentEngineMemoryConfig,
                vertexai._genai.types.common.GetAgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Memory

Deprecated.

See more: [vertexai._genai.agent_engines.AgentEngines.get_memory](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AgentEngines#vertexai__genai_agent_engines_AgentEngines_get_memory)

### vertexai._genai.agent_engines.AgentEngines.get_session
    
    
    get_session(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetAgentEngineSessionConfig,
                vertexai._genai.types.common.GetAgentEngineSessionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Session

Deprecated.

See more: [vertexai._genai.agent_engines.AgentEngines.get_session](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AgentEngines#vertexai__genai_agent_engines_AgentEngines_get_session)

### vertexai._genai.agent_engines.AgentEngines.list
    
    
    list(
        *,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineConfig,
                vertexai._genai.types.common.ListAgentEngineConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[vertexai._genai.types.common.AgentEngine]

List all instances of Agent Engine matching the filter.

See more: [vertexai._genai.agent_engines.AgentEngines.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AgentEngines#vertexai__genai_agent_engines_AgentEngines_list)

### vertexai._genai.agent_engines.AgentEngines.list_memories
    
    
    list_memories(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineMemoryConfig,
                vertexai._genai.types.common.ListAgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[vertexai._genai.types.common.Memory]

Deprecated.

See more: [vertexai._genai.agent_engines.AgentEngines.list_memories](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AgentEngines#vertexai__genai_agent_engines_AgentEngines_list_memories)

### vertexai._genai.agent_engines.AgentEngines.list_session_events
    
    
    list_session_events(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineSessionEventsConfig,
                vertexai._genai.types.common.ListAgentEngineSessionEventsConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[vertexai._genai.types.common.SessionEvent]

Deprecated.

See more: [vertexai._genai.agent_engines.AgentEngines.list_session_events](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AgentEngines#vertexai__genai_agent_engines_AgentEngines_list_session_events)

### vertexai._genai.agent_engines.AgentEngines.list_sessions
    
    
    list_sessions(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineSessionsConfig,
                vertexai._genai.types.common.ListAgentEngineSessionsConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[vertexai._genai.types.common.Session]

Deprecated.

See more: [vertexai._genai.agent_engines.AgentEngines.list_sessions](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AgentEngines#vertexai__genai_agent_engines_AgentEngines_list_sessions)

### vertexai._genai.agent_engines.AgentEngines.retrieve_memories
    
    
    retrieve_memories(
        *,
        name: str,
        scope: dict[str, str],
        similarity_search_params: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RetrieveMemoriesRequestSimilaritySearchParams,
                vertexai._genai.types.common.RetrieveMemoriesRequestSimilaritySearchParamsDict,
            ]
        ] = None,
        simple_retrieval_params: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RetrieveMemoriesRequestSimpleRetrievalParams,
                vertexai._genai.types.common.RetrieveMemoriesRequestSimpleRetrievalParamsDict,
            ]
        ] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RetrieveAgentEngineMemoriesConfig,
                vertexai._genai.types.common.RetrieveAgentEngineMemoriesConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[
        vertexai._genai.types.common.RetrieveMemoriesResponseRetrievedMemory
    ]

Deprecated.

See more: [vertexai._genai.agent_engines.AgentEngines.retrieve_memories](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AgentEngines#vertexai__genai_agent_engines_AgentEngines_retrieve_memories)

### vertexai._genai.agent_engines.AgentEngines.run_query_job
    
    
    run_query_job(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RunQueryJobAgentEngineConfig,
                vertexai._genai.types.common.RunQueryJobAgentEngineConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.RunQueryJobResult

Launches a long-running query job on an Agent Engine .

See more: [vertexai._genai.agent_engines.AgentEngines.run_query_job](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AgentEngines#vertexai__genai_agent_engines_AgentEngines_run_query_job)

### vertexai._genai.agent_engines.AgentEngines.update
    
    
    update(
        *,
        name: str,
        agent: typing.Optional[typing.Any] = None,
        agent_engine: typing.Optional[typing.Any] = None,
        config: typing.Union[
            vertexai._genai.types.common.AgentEngineConfig,
            vertexai._genai.types.common.AgentEngineConfigDict,
        ]
    ) -> vertexai._genai.types.common.AgentEngine

Updates an existing Agent Engine.

See more: [vertexai._genai.agent_engines.AgentEngines.update](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AgentEngines#vertexai__genai_agent_engines_AgentEngines_update)

### vertexai._genai.agent_engines.AsyncAgentEngines.append_session_event
    
    
    append_session_event(
        *,
        name: str,
        author: str,
        invocation_id: str,
        timestamp: datetime.datetime,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.AppendAgentEngineSessionEventConfig,
                vertexai._genai.types.common.AppendAgentEngineSessionEventConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AppendAgentEngineSessionEventResponse

Deprecated.

See more: [vertexai._genai.agent_engines.AsyncAgentEngines.append_session_event](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AsyncAgentEngines#vertexai__genai_agent_engines_AsyncAgentEngines_append_session_event)

### vertexai._genai.agent_engines.AsyncAgentEngines.cancel_query_job
    
    
    cancel_query_job(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CancelQueryJobAgentEngineConfig,
                vertexai._genai.types.common.CancelQueryJobAgentEngineConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.CancelQueryJobResult

Cancels a long-running query job on an Agent Engine.

See more: [vertexai._genai.agent_engines.AsyncAgentEngines.cancel_query_job](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AsyncAgentEngines#vertexai__genai_agent_engines_AsyncAgentEngines_cancel_query_job)

### vertexai._genai.agent_engines.AsyncAgentEngines.delete
    
    
    delete(
        *,
        name: str,
        force: typing.Optional[bool] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteAgentEngineConfig,
                vertexai._genai.types.common.DeleteAgentEngineConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.DeleteAgentEngineOperation

Delete an Agent Engine resource.

See more: [vertexai._genai.agent_engines.AsyncAgentEngines.delete](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AsyncAgentEngines#vertexai__genai_agent_engines_AsyncAgentEngines_delete)

### vertexai._genai.agent_engines.AsyncAgentEngines.delete_memory
    
    
    delete_memory(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteAgentEngineMemoryConfig,
                vertexai._genai.types.common.DeleteAgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.DeleteAgentEngineMemoryOperation

Deprecated.

See more: [vertexai._genai.agent_engines.AsyncAgentEngines.delete_memory](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AsyncAgentEngines#vertexai__genai_agent_engines_AsyncAgentEngines_delete_memory)

### vertexai._genai.agent_engines.AsyncAgentEngines.delete_session
    
    
    delete_session(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteAgentEngineSessionConfig,
                vertexai._genai.types.common.DeleteAgentEngineSessionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.DeleteAgentEngineSessionOperation

Deprecated.

See more: [vertexai._genai.agent_engines.AsyncAgentEngines.delete_session](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AsyncAgentEngines#vertexai__genai_agent_engines_AsyncAgentEngines_delete_session)

### vertexai._genai.agent_engines.AsyncAgentEngines.get_memory
    
    
    get_memory(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetAgentEngineMemoryConfig,
                vertexai._genai.types.common.GetAgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Memory

Deprecated.

See more: [vertexai._genai.agent_engines.AsyncAgentEngines.get_memory](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AsyncAgentEngines#vertexai__genai_agent_engines_AsyncAgentEngines_get_memory)

### vertexai._genai.agent_engines.AsyncAgentEngines.get_session
    
    
    get_session(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetAgentEngineSessionConfig,
                vertexai._genai.types.common.GetAgentEngineSessionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Session

Deprecated.

See more: [vertexai._genai.agent_engines.AsyncAgentEngines.get_session](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.agent_engines.AsyncAgentEngines#vertexai__genai_agent_engines_AsyncAgentEngines_get_session)

### vertexai._genai.evals.AsyncEvals.batch_evaluate
    
    
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

See more: [vertexai._genai.evals.AsyncEvals.batch_evaluate](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.AsyncEvals#vertexai__genai_evals_AsyncEvals_batch_evaluate)

### vertexai._genai.evals.AsyncEvals.create_evaluation_experiment
    
    
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

See more: [vertexai._genai.evals.AsyncEvals.create_evaluation_experiment](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.AsyncEvals#vertexai__genai_evals_AsyncEvals_create_evaluation_experiment)

### vertexai._genai.evals.AsyncEvals.create_evaluation_item
    
    
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

See more: [vertexai._genai.evals.AsyncEvals.create_evaluation_item](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.AsyncEvals#vertexai__genai_evals_AsyncEvals_create_evaluation_item)

### vertexai._genai.evals.AsyncEvals.create_evaluation_metric
    
    
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

See more: [vertexai._genai.evals.AsyncEvals.create_evaluation_metric](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.AsyncEvals#vertexai__genai_evals_AsyncEvals_create_evaluation_metric)

### vertexai._genai.evals.AsyncEvals.create_evaluation_run
    
    
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

See more: [vertexai._genai.evals.AsyncEvals.create_evaluation_run](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.AsyncEvals#vertexai__genai_evals_AsyncEvals_create_evaluation_run)

### vertexai._genai.evals.AsyncEvals.create_evaluation_set
    
    
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

See more: [vertexai._genai.evals.AsyncEvals.create_evaluation_set](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.AsyncEvals#vertexai__genai_evals_AsyncEvals_create_evaluation_set)

### vertexai._genai.evals.AsyncEvals.delete_evaluation_experiment
    
    
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

See more: [vertexai._genai.evals.AsyncEvals.delete_evaluation_experiment](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.AsyncEvals#vertexai__genai_evals_AsyncEvals_delete_evaluation_experiment)

### vertexai._genai.evals.AsyncEvals.delete_evaluation_metric
    
    
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

See more: [vertexai._genai.evals.AsyncEvals.delete_evaluation_metric](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.AsyncEvals#vertexai__genai_evals_AsyncEvals_delete_evaluation_metric)

### vertexai._genai.evals.AsyncEvals.evaluate_instances
    
    
    evaluate_instances(
        *, metric_config: vertexai._genai.types.common._EvaluateInstancesRequestParameters
    ) -> vertexai._genai.types.common.EvaluateInstancesResponse

Evaluates an instance of a model.

See more: [vertexai._genai.evals.AsyncEvals.evaluate_instances](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.AsyncEvals#vertexai__genai_evals_AsyncEvals_evaluate_instances)

### vertexai._genai.evals.AsyncEvals.generate_conversation_scenarios
    
    
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

See more: [vertexai._genai.evals.AsyncEvals.generate_conversation_scenarios](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.AsyncEvals#vertexai__genai_evals_AsyncEvals_generate_conversation_scenarios)

### vertexai._genai.evals.AsyncEvals.generate_loss_clusters
    
    
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

See more: [vertexai._genai.evals.AsyncEvals.generate_loss_clusters](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.AsyncEvals#vertexai__genai_evals_AsyncEvals_generate_loss_clusters)

### vertexai._genai.evals.AsyncEvals.get_evaluation_experiment
    
    
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

See more: [vertexai._genai.evals.AsyncEvals.get_evaluation_experiment](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.AsyncEvals#vertexai__genai_evals_AsyncEvals_get_evaluation_experiment)

### vertexai._genai.evals.AsyncEvals.get_evaluation_item
    
    
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

See more: [vertexai._genai.evals.AsyncEvals.get_evaluation_item](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.AsyncEvals#vertexai__genai_evals_AsyncEvals_get_evaluation_item)

### vertexai._genai.evals.AsyncEvals.get_evaluation_metric
    
    
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

See more: [vertexai._genai.evals.AsyncEvals.get_evaluation_metric](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.AsyncEvals#vertexai__genai_evals_AsyncEvals_get_evaluation_metric)

### vertexai._genai.evals.AsyncEvals.get_evaluation_run
    
    
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

See more: [vertexai._genai.evals.AsyncEvals.get_evaluation_run](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.AsyncEvals#vertexai__genai_evals_AsyncEvals_get_evaluation_run)

### vertexai._genai.evals.AsyncEvals.get_evaluation_set
    
    
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

See more: [vertexai._genai.evals.AsyncEvals.get_evaluation_set](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.AsyncEvals#vertexai__genai_evals_AsyncEvals_get_evaluation_set)

### vertexai._genai.evals.AsyncEvals.list_evaluation_experiments
    
    
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

See more: [vertexai._genai.evals.AsyncEvals.list_evaluation_experiments](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.AsyncEvals#vertexai__genai_evals_AsyncEvals_list_evaluation_experiments)

### vertexai._genai.evals.AsyncEvals.list_evaluation_metrics
    
    
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

See more: [vertexai._genai.evals.AsyncEvals.list_evaluation_metrics](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.AsyncEvals#vertexai__genai_evals_AsyncEvals_list_evaluation_metrics)

### vertexai._genai.evals.AsyncEvals.update_evaluation_experiment
    
    
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

See more: [vertexai._genai.evals.AsyncEvals.update_evaluation_experiment](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.AsyncEvals#vertexai__genai_evals_AsyncEvals_update_evaluation_experiment)

### vertexai._genai.evals.Evals.batch_evaluate
    
    
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

See more: [vertexai._genai.evals.Evals.batch_evaluate](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_batch_evaluate)

### vertexai._genai.evals.Evals.create_evaluation_experiment
    
    
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

See more: [vertexai._genai.evals.Evals.create_evaluation_experiment](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_create_evaluation_experiment)

### vertexai._genai.evals.Evals.create_evaluation_item
    
    
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

See more: [vertexai._genai.evals.Evals.create_evaluation_item](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_create_evaluation_item)

### vertexai._genai.evals.Evals.create_evaluation_metric
    
    
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

See more: [vertexai._genai.evals.Evals.create_evaluation_metric](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_create_evaluation_metric)

### vertexai._genai.evals.Evals.create_evaluation_run
    
    
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
        agent_info: typing.Optional[
            typing.Union[
                vertexai._genai.types.evals.AgentInfo,
                vertexai._genai.types.evals.AgentInfoDict,
            ]
        ] = None,
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
        red_teaming_config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RedTeamingAnalysisConfig,
                vertexai._genai.types.common.RedTeamingAnalysisConfigDict,
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

See more: [vertexai._genai.evals.Evals.create_evaluation_run](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_create_evaluation_run)

### vertexai._genai.evals.Evals.create_evaluation_set
    
    
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

See more: [vertexai._genai.evals.Evals.create_evaluation_set](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_create_evaluation_set)

### vertexai._genai.evals.Evals.delete_evaluation_experiment
    
    
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

See more: [vertexai._genai.evals.Evals.delete_evaluation_experiment](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_delete_evaluation_experiment)

### vertexai._genai.evals.Evals.delete_evaluation_metric
    
    
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

See more: [vertexai._genai.evals.Evals.delete_evaluation_metric](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_delete_evaluation_metric)

### vertexai._genai.evals.Evals.evaluate
    
    
    evaluate(
        *,
        dataset: typing.Union[
            pandas.core.frame.DataFrame,
            vertexai._genai.types.common.EvaluationDataset,
            vertexai._genai.types.common.EvaluationDatasetDict,
            list[
                typing.Union[
                    vertexai._genai.types.common.EvaluationDataset,
                    vertexai._genai.types.common.EvaluationDatasetDict,
                ]
            ],
        ],
        metrics: typing.Optional[
            list[
                typing.Union[
                    vertexai._genai.types.common.Metric,
                    vertexai._genai.types.common.MetricDict,
                ]
            ]
        ] = None,
        location: typing.Optional[str] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.EvaluateMethodConfig,
                vertexai._genai.types.common.EvaluateMethodConfigDict,
            ]
        ] = None,
        **kwargs: typing.Any
    ) -> vertexai._genai.types.common.EvaluationResult

Evaluates candidate responses in the provided dataset(s) using the specified metrics.

See more: [vertexai._genai.evals.Evals.evaluate](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_evaluate)

### vertexai._genai.evals.Evals.evaluate_instances
    
    
    evaluate_instances(
        *, metric_config: vertexai._genai.types.common._EvaluateInstancesRequestParameters
    ) -> vertexai._genai.types.common.EvaluateInstancesResponse

Evaluates an instance of a model.

See more: [vertexai._genai.evals.Evals.evaluate_instances](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_evaluate_instances)

### vertexai._genai.evals.Evals.generate_conversation_scenarios
    
    
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

See more: [vertexai._genai.evals.Evals.generate_conversation_scenarios](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_generate_conversation_scenarios)

### vertexai._genai.evals.Evals.generate_loss_clusters
    
    
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

See more: [vertexai._genai.evals.Evals.generate_loss_clusters](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_generate_loss_clusters)

### vertexai._genai.evals.Evals.generate_rubrics
    
    
    generate_rubrics(
        *,
        src: typing.Union[
            str, pd.DataFrame, vertexai._genai.types.common.EvaluationDataset
        ],
        rubric_group_name: str,
        prompt_template: typing.Optional[str] = None,
        generator_model_config: typing.Optional[genai_types.AutoraterConfigOrDict] = None,
        rubric_content_type: typing.Optional[types.RubricContentType] = None,
        rubric_type_ontology: typing.Optional[list[str]] = None,
        predefined_spec_name: typing.Optional[
            typing.Union[str, types.PrebuiltMetric]
        ] = None,
        metric_spec_parameters: typing.Optional[dict[str, typing.Any]] = None,
        metric: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.Metric, vertexai._genai.types.common.MetricDict
            ]
        ] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RubricGenerationConfig,
                vertexai._genai.types.common.RubricGenerationConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.EvaluationDataset

Generates rubrics for each prompt in the source and adds them as a new column structured as a dictionary.

See more: [vertexai._genai.evals.Evals.generate_rubrics](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_generate_rubrics)

### vertexai._genai.evals.Evals.get_evaluation_experiment
    
    
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

See more: [vertexai._genai.evals.Evals.get_evaluation_experiment](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_get_evaluation_experiment)

### vertexai._genai.evals.Evals.get_evaluation_item
    
    
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

See more: [vertexai._genai.evals.Evals.get_evaluation_item](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_get_evaluation_item)

### vertexai._genai.evals.Evals.get_evaluation_metric
    
    
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

See more: [vertexai._genai.evals.Evals.get_evaluation_metric](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_get_evaluation_metric)

### vertexai._genai.evals.Evals.get_evaluation_run
    
    
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

Retrieves an EvaluationRun from the resource name.

See more: [vertexai._genai.evals.Evals.get_evaluation_run](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_get_evaluation_run)

### vertexai._genai.evals.Evals.get_evaluation_set
    
    
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

See more: [vertexai._genai.evals.Evals.get_evaluation_set](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_get_evaluation_set)

### vertexai._genai.evals.Evals.list_evaluation_experiments
    
    
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

See more: [vertexai._genai.evals.Evals.list_evaluation_experiments](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_list_evaluation_experiments)

### vertexai._genai.evals.Evals.list_evaluation_metrics
    
    
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

See more: [vertexai._genai.evals.Evals.list_evaluation_metrics](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_list_evaluation_metrics)

### vertexai._genai.evals.Evals.run_inference
    
    
    run_inference(
        *,
        src: typing.Union[
            str, pandas.core.frame.DataFrame, vertexai._genai.types.common.EvaluationDataset
        ],
        model: typing.Optional[
            typing.Union[str, typing.Callable[[typing.Any], typing.Any]]
        ] = None,
        agent: typing.Optional[
            typing.Union[str, vertexai._genai.types.common.AgentEngine]
        ] = None,
        location: typing.Optional[str] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.EvalRunInferenceConfig,
                vertexai._genai.types.common.EvalRunInferenceConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.EvaluationDataset

Runs inference on a dataset for evaluation.

See more: [vertexai._genai.evals.Evals.run_inference](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_run_inference)

### vertexai._genai.evals.Evals.update_evaluation_experiment
    
    
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

See more: [vertexai._genai.evals.Evals.update_evaluation_experiment](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.evals.Evals#vertexai__genai_evals_Evals_update_evaluation_experiment)

### vertexai._genai.memories.AsyncMemories.create
    
    
    create(
        *,
        name: str,
        fact: str,
        scope: dict[str, str],
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.AgentEngineMemoryConfig,
                vertexai._genai.types.common.AgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngineMemoryOperation

Creates a new memory in the Agent Engine.

See more: [vertexai._genai.memories.AsyncMemories.create](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memories.AsyncMemories#vertexai__genai_memories_AsyncMemories_create)

### vertexai._genai.memories.AsyncMemories.delete
    
    
    delete(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteAgentEngineMemoryConfig,
                vertexai._genai.types.common.DeleteAgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.DeleteAgentEngineMemoryOperation

Delete an Agent Engine memory.

See more: [vertexai._genai.memories.AsyncMemories.delete](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memories.AsyncMemories#vertexai__genai_memories_AsyncMemories_delete)

### vertexai._genai.memories.AsyncMemories.generate
    
    
    generate(
        *,
        name: str,
        vertex_session_source: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GenerateMemoriesRequestVertexSessionSource,
                vertexai._genai.types.common.GenerateMemoriesRequestVertexSessionSourceDict,
            ]
        ] = None,
        direct_contents_source: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GenerateMemoriesRequestDirectContentsSource,
                vertexai._genai.types.common.GenerateMemoriesRequestDirectContentsSourceDict,
            ]
        ] = None,
        direct_memories_source: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GenerateMemoriesRequestDirectMemoriesSource,
                vertexai._genai.types.common.GenerateMemoriesRequestDirectMemoriesSourceDict,
            ]
        ] = None,
        scope: typing.Optional[dict[str, str]] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GenerateAgentEngineMemoriesConfig,
                vertexai._genai.types.common.GenerateAgentEngineMemoriesConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngineGenerateMemoriesOperation

Generates memories for the agent engine.

See more: [vertexai._genai.memories.AsyncMemories.generate](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memories.AsyncMemories#vertexai__genai_memories_AsyncMemories_generate)

### vertexai._genai.memories.AsyncMemories.get
    
    
    get(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetAgentEngineMemoryConfig,
                vertexai._genai.types.common.GetAgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Memory

Gets an agent engine memory.

See more: [vertexai._genai.memories.AsyncMemories.get](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memories.AsyncMemories#vertexai__genai_memories_AsyncMemories_get)

### vertexai._genai.memories.AsyncMemories.ingest_events
    
    
    ingest_events(
        *,
        name: str,
        scope: dict[str, str],
        stream_id: str = "",
        direct_contents_source: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.IngestionDirectContentsSource,
                vertexai._genai.types.common.IngestionDirectContentsSourceDict,
            ]
        ] = None,
        generation_trigger_config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.MemoryGenerationTriggerConfig,
                vertexai._genai.types.common.MemoryGenerationTriggerConfigDict,
            ]
        ] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.IngestEventsConfig,
                vertexai._genai.types.common.IngestEventsConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.MemoryBankIngestEventsOperation

Ingests events into an Agent Engine.

See more: [vertexai._genai.memories.AsyncMemories.ingest_events](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memories.AsyncMemories#vertexai__genai_memories_AsyncMemories_ingest_events)

### vertexai._genai.memories.AsyncMemories.list
    
    
    list(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineMemoryConfig,
                vertexai._genai.types.common.ListAgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> google.genai.pagers.AsyncPager[vertexai._genai.types.common.Memory]

Lists Agent Engine memories.

See more: [vertexai._genai.memories.AsyncMemories.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memories.AsyncMemories#vertexai__genai_memories_AsyncMemories_list)

### vertexai._genai.memories.AsyncMemories.purge
    
    
    purge(
        *,
        name: str,
        filter: typing.Optional[str] = None,
        filter_groups: typing.Optional[
            typing.List[vertexai._genai.types.common.MemoryConjunctionFilter]
        ] = None,
        force: bool = False,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.PurgeAgentEngineMemoriesConfig,
                vertexai._genai.types.common.PurgeAgentEngineMemoriesConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEnginePurgeMemoriesOperation

Purges memories from an Agent Engine.

See more: [vertexai._genai.memories.AsyncMemories.purge](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memories.AsyncMemories#vertexai__genai_memories_AsyncMemories_purge)

### vertexai._genai.memories.AsyncMemories.retrieve
    
    
    retrieve(
        *,
        name: str,
        scope: dict[str, str],
        similarity_search_params: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RetrieveMemoriesRequestSimilaritySearchParams,
                vertexai._genai.types.common.RetrieveMemoriesRequestSimilaritySearchParamsDict,
            ]
        ] = None,
        simple_retrieval_params: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RetrieveMemoriesRequestSimpleRetrievalParams,
                vertexai._genai.types.common.RetrieveMemoriesRequestSimpleRetrievalParamsDict,
            ]
        ] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RetrieveAgentEngineMemoriesConfig,
                vertexai._genai.types.common.RetrieveAgentEngineMemoriesConfigDict,
            ]
        ] = None
    ) -> google.genai.pagers.AsyncPager[
        vertexai._genai.types.common.RetrieveMemoriesResponseRetrievedMemory
    ]

Retrieves memories for the agent.

See more: [vertexai._genai.memories.AsyncMemories.retrieve](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memories.AsyncMemories#vertexai__genai_memories_AsyncMemories_retrieve)

### vertexai._genai.memories.AsyncMemories.retrieve_profiles
    
    
    retrieve_profiles(
        *,
        name: str,
        scope: dict[str, str],
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RetrieveMemoryProfilesConfig,
                vertexai._genai.types.common.RetrieveMemoryProfilesConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.RetrieveProfilesResponse

Retrieves memory profiles for an Agent Engine.

See more: [vertexai._genai.memories.AsyncMemories.retrieve_profiles](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memories.AsyncMemories#vertexai__genai_memories_AsyncMemories_retrieve_profiles)

### vertexai._genai.memories.AsyncMemories.rollback
    
    
    rollback(
        *,
        name: str,
        target_revision_id: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RollbackAgentEngineMemoryConfig,
                vertexai._genai.types.common.RollbackAgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngineRollbackMemoryOperation

Rolls back a memory to a previous revision.

See more: [vertexai._genai.memories.AsyncMemories.rollback](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memories.AsyncMemories#vertexai__genai_memories_AsyncMemories_rollback)

### vertexai._genai.memories.Memories.create
    
    
    create(
        *,
        name: str,
        fact: str,
        scope: dict[str, str],
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.AgentEngineMemoryConfig,
                vertexai._genai.types.common.AgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngineMemoryOperation

Creates a new memory in the Agent Engine.

See more: [vertexai._genai.memories.Memories.create](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memories.Memories#vertexai__genai_memories_Memories_create)

### vertexai._genai.memories.Memories.delete
    
    
    delete(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteAgentEngineMemoryConfig,
                vertexai._genai.types.common.DeleteAgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.DeleteAgentEngineMemoryOperation

Delete an Agent Engine memory.

See more: [vertexai._genai.memories.Memories.delete](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memories.Memories#vertexai__genai_memories_Memories_delete)

### vertexai._genai.memories.Memories.generate
    
    
    generate(
        *,
        name: str,
        vertex_session_source: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GenerateMemoriesRequestVertexSessionSource,
                vertexai._genai.types.common.GenerateMemoriesRequestVertexSessionSourceDict,
            ]
        ] = None,
        direct_contents_source: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GenerateMemoriesRequestDirectContentsSource,
                vertexai._genai.types.common.GenerateMemoriesRequestDirectContentsSourceDict,
            ]
        ] = None,
        direct_memories_source: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GenerateMemoriesRequestDirectMemoriesSource,
                vertexai._genai.types.common.GenerateMemoriesRequestDirectMemoriesSourceDict,
            ]
        ] = None,
        scope: typing.Optional[dict[str, str]] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GenerateAgentEngineMemoriesConfig,
                vertexai._genai.types.common.GenerateAgentEngineMemoriesConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngineGenerateMemoriesOperation

Generates memories for the agent engine.

See more: [vertexai._genai.memories.Memories.generate](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memories.Memories#vertexai__genai_memories_Memories_generate)

### vertexai._genai.memories.Memories.get
    
    
    get(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetAgentEngineMemoryConfig,
                vertexai._genai.types.common.GetAgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Memory

Gets an agent engine memory.

See more: [vertexai._genai.memories.Memories.get](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memories.Memories#vertexai__genai_memories_Memories_get)

### vertexai._genai.memories.Memories.ingest_events
    
    
    ingest_events(
        *,
        name: str,
        scope: dict[str, str],
        stream_id: str = "",
        direct_contents_source: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.IngestionDirectContentsSource,
                vertexai._genai.types.common.IngestionDirectContentsSourceDict,
            ]
        ] = None,
        generation_trigger_config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.MemoryGenerationTriggerConfig,
                vertexai._genai.types.common.MemoryGenerationTriggerConfigDict,
            ]
        ] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.IngestEventsConfig,
                vertexai._genai.types.common.IngestEventsConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.MemoryBankIngestEventsOperation

Ingests events into an Agent Engine.

See more: [vertexai._genai.memories.Memories.ingest_events](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memories.Memories#vertexai__genai_memories_Memories_ingest_events)

### vertexai._genai.memories.Memories.list
    
    
    list(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineMemoryConfig,
                vertexai._genai.types.common.ListAgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[vertexai._genai.types.common.Memory]

Lists Agent Engine memories.

See more: [vertexai._genai.memories.Memories.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memories.Memories#vertexai__genai_memories_Memories_list)

### vertexai._genai.memories.Memories.purge
    
    
    purge(
        *,
        name: str,
        filter: typing.Optional[str] = None,
        filter_groups: typing.Optional[
            typing.List[vertexai._genai.types.common.MemoryConjunctionFilter]
        ] = None,
        force: bool = False,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.PurgeAgentEngineMemoriesConfig,
                vertexai._genai.types.common.PurgeAgentEngineMemoriesConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEnginePurgeMemoriesOperation

Purges memories from an Agent Engine.

See more: [vertexai._genai.memories.Memories.purge](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memories.Memories#vertexai__genai_memories_Memories_purge)

### vertexai._genai.memories.Memories.retrieve
    
    
    retrieve(
        *,
        name: str,
        scope: dict[str, str],
        similarity_search_params: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RetrieveMemoriesRequestSimilaritySearchParams,
                vertexai._genai.types.common.RetrieveMemoriesRequestSimilaritySearchParamsDict,
            ]
        ] = None,
        simple_retrieval_params: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RetrieveMemoriesRequestSimpleRetrievalParams,
                vertexai._genai.types.common.RetrieveMemoriesRequestSimpleRetrievalParamsDict,
            ]
        ] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RetrieveAgentEngineMemoriesConfig,
                vertexai._genai.types.common.RetrieveAgentEngineMemoriesConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[
        vertexai._genai.types.common.RetrieveMemoriesResponseRetrievedMemory
    ]

Retrieves memories for the agent.

See more: [vertexai._genai.memories.Memories.retrieve](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memories.Memories#vertexai__genai_memories_Memories_retrieve)

### vertexai._genai.memories.Memories.retrieve_profiles
    
    
    retrieve_profiles(
        *,
        name: str,
        scope: dict[str, str],
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RetrieveMemoryProfilesConfig,
                vertexai._genai.types.common.RetrieveMemoryProfilesConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.RetrieveProfilesResponse

Retrieves memory profiles for an Agent Engine.

See more: [vertexai._genai.memories.Memories.retrieve_profiles](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memories.Memories#vertexai__genai_memories_Memories_retrieve_profiles)

### vertexai._genai.memories.Memories.rollback
    
    
    rollback(
        *,
        name: str,
        target_revision_id: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RollbackAgentEngineMemoryConfig,
                vertexai._genai.types.common.RollbackAgentEngineMemoryConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngineRollbackMemoryOperation

Rolls back a memory to a previous revision.

See more: [vertexai._genai.memories.Memories.rollback](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memories.Memories#vertexai__genai_memories_Memories_rollback)

### vertexai._genai.memory_revisions.AsyncMemoryRevisions.get
    
    
    get(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetAgentEngineMemoryRevisionConfig,
                vertexai._genai.types.common.GetAgentEngineMemoryRevisionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.MemoryRevision

Gets an agent engine memory revision.

See more: [vertexai._genai.memory_revisions.AsyncMemoryRevisions.get](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memory_revisions.AsyncMemoryRevisions#vertexai__genai_memory_revisions_AsyncMemoryRevisions_get)

### vertexai._genai.memory_revisions.AsyncMemoryRevisions.list
    
    
    list(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineMemoryRevisionsConfig,
                vertexai._genai.types.common.ListAgentEngineMemoryRevisionsConfigDict,
            ]
        ] = None
    ) -> google.genai.pagers.AsyncPager[vertexai._genai.types.common.MemoryRevision]

Lists Agent Engine memory revisions.

See more: [vertexai._genai.memory_revisions.AsyncMemoryRevisions.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memory_revisions.AsyncMemoryRevisions#vertexai__genai_memory_revisions_AsyncMemoryRevisions_list)

### vertexai._genai.memory_revisions.MemoryRevisions.get
    
    
    get(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetAgentEngineMemoryRevisionConfig,
                vertexai._genai.types.common.GetAgentEngineMemoryRevisionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.MemoryRevision

Gets an agent engine memory revision.

See more: [vertexai._genai.memory_revisions.MemoryRevisions.get](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memory_revisions.MemoryRevisions#vertexai__genai_memory_revisions_MemoryRevisions_get)

### vertexai._genai.memory_revisions.MemoryRevisions.list
    
    
    list(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineMemoryRevisionsConfig,
                vertexai._genai.types.common.ListAgentEngineMemoryRevisionsConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[vertexai._genai.types.common.MemoryRevision]

Lists Agent Engine memory revisions.

See more: [vertexai._genai.memory_revisions.MemoryRevisions.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.memory_revisions.MemoryRevisions#vertexai__genai_memory_revisions_MemoryRevisions_list)

### vertexai._genai.prompt_optimizer.AsyncPromptOptimizer.optimize
    
    
    optimize(
        method: vertexai._genai.types.common.PromptOptimizerMethod,
        config: typing.Union[
            vertexai._genai.types.common.PromptOptimizerConfig,
            vertexai._genai.types.common.PromptOptimizerConfigDict,
        ],
    ) -> vertexai._genai.types.common.CustomJob

Call async Vertex AI Prompt Optimizer (VAPO).

See more: [vertexai._genai.prompt_optimizer.AsyncPromptOptimizer.optimize](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompt_optimizer.AsyncPromptOptimizer#vertexai__genai_prompt_optimizer_AsyncPromptOptimizer_optimize)

### vertexai._genai.prompt_optimizer.AsyncPromptOptimizer.optimize_prompt
    
    
    optimize_prompt(
        *,
        prompt: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.OptimizeConfig,
                vertexai._genai.types.common.OptimizeConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.OptimizeResponse

Makes an async request to _optimize_prompt and returns an optimized prompt.

See more: [vertexai._genai.prompt_optimizer.AsyncPromptOptimizer.optimize_prompt](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompt_optimizer.AsyncPromptOptimizer#vertexai__genai_prompt_optimizer_AsyncPromptOptimizer_optimize_prompt)

### vertexai._genai.prompt_optimizer.PromptOptimizer.optimize
    
    
    optimize(
        method: vertexai._genai.types.common.PromptOptimizerMethod,
        config: typing.Union[
            vertexai._genai.types.common.PromptOptimizerConfig,
            vertexai._genai.types.common.PromptOptimizerConfigDict,
        ],
    ) -> vertexai._genai.types.common.CustomJob

Call PO-Data optimizer.

See more: [vertexai._genai.prompt_optimizer.PromptOptimizer.optimize](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompt_optimizer.PromptOptimizer#vertexai__genai_prompt_optimizer_PromptOptimizer_optimize)

### vertexai._genai.prompt_optimizer.PromptOptimizer.optimize_prompt
    
    
    optimize_prompt(
        *,
        prompt: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.OptimizeConfig,
                vertexai._genai.types.common.OptimizeConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.OptimizeResponse

Makes an API request to _optimize_prompt and returns the parsed response.

See more: [vertexai._genai.prompt_optimizer.PromptOptimizer.optimize_prompt](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompt_optimizer.PromptOptimizer#vertexai__genai_prompt_optimizer_PromptOptimizer_optimize_prompt)

### vertexai._genai.prompts.AsyncPrompts.create
    
    
    create(
        *,
        prompt: typing.Union[
            vertexai._genai.types.common.Prompt, vertexai._genai.types.common.PromptDict
        ],
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CreatePromptConfig,
                vertexai._genai.types.common.CreatePromptConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Prompt

Creates a new prompt in a Vertex Dataset resource.

See more: [vertexai._genai.prompts.AsyncPrompts.create](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.AsyncPrompts#vertexai__genai_prompts_AsyncPrompts_create)

### vertexai._genai.prompts.AsyncPrompts.create_version
    
    
    create_version(
        *,
        prompt: typing.Union[
            vertexai._genai.types.common.Prompt, vertexai._genai.types.common.PromptDict
        ],
        prompt_id: typing.Optional[str] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CreatePromptVersionConfig,
                vertexai._genai.types.common.CreatePromptVersionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Prompt

Creates a prompt resource and an initial prompt version.

See more: [vertexai._genai.prompts.AsyncPrompts.create_version](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.AsyncPrompts#vertexai__genai_prompts_AsyncPrompts_create_version)

### vertexai._genai.prompts.AsyncPrompts.delete
    
    
    delete(
        *,
        prompt_id: str,
        config: typing.Optional[vertexai._genai.types.common.DeletePromptConfig] = None
    ) -> None

Deletes a prompt resource.

See more: [vertexai._genai.prompts.AsyncPrompts.delete](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.AsyncPrompts#vertexai__genai_prompts_AsyncPrompts_delete)

### vertexai._genai.prompts.AsyncPrompts.delete_version
    
    
    delete_version(
        *,
        prompt_id: str,
        version_id: str,
        config: typing.Optional[vertexai._genai.types.common.DeletePromptConfig] = None
    ) -> None

Deletes a prompt version resource.

See more: [vertexai._genai.prompts.AsyncPrompts.delete_version](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.AsyncPrompts#vertexai__genai_prompts_AsyncPrompts_delete_version)

### vertexai._genai.prompts.AsyncPrompts.get
    
    
    get(
        *,
        prompt_id: str,
        config: typing.Optional[vertexai._genai.types.common.GetPromptConfig] = None
    ) -> vertexai._genai.types.common.Prompt

Gets a prompt resource from a Vertex Dataset.

See more: [vertexai._genai.prompts.AsyncPrompts.get](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.AsyncPrompts#vertexai__genai_prompts_AsyncPrompts_get)

### vertexai._genai.prompts.AsyncPrompts.get_version
    
    
    get_version(
        *,
        prompt_id: str,
        version_id: str,
        config: typing.Optional[vertexai._genai.types.common.GetPromptConfig] = None
    ) -> vertexai._genai.types.common.Prompt

Gets a prompt resource from a Vertex Dataset.

See more: [vertexai._genai.prompts.AsyncPrompts.get_version](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.AsyncPrompts#vertexai__genai_prompts_AsyncPrompts_get_version)

### vertexai._genai.prompts.AsyncPrompts.launch_optimization_job
    
    
    launch_optimization_job(
        method: vertexai._genai.types.common.PromptOptimizerMethod,
        config: typing.Union[
            vertexai._genai.types.common.PromptOptimizerConfig,
            vertexai._genai.types.common.PromptOptimizerConfigDict,
        ],
    ) -> vertexai._genai.types.common.CustomJob

Call async Vertex AI Prompt Optimizer (VAPO).

See more: [vertexai._genai.prompts.AsyncPrompts.launch_optimization_job](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.AsyncPrompts#vertexai__genai_prompts_AsyncPrompts_launch_optimization_job)

### vertexai._genai.prompts.AsyncPrompts.list
    
    
    list(
        *,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListPromptsConfig,
                vertexai._genai.types.common.ListPromptsConfigDict,
            ]
        ] = None
    ) -> typing.AsyncIterator[vertexai._genai.types.common.PromptRef]

Lists prompt resources in a project.

See more: [vertexai._genai.prompts.AsyncPrompts.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.AsyncPrompts#vertexai__genai_prompts_AsyncPrompts_list)

### vertexai._genai.prompts.AsyncPrompts.list_versions
    
    
    list_versions(
        *,
        prompt_id: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListPromptsConfig,
                vertexai._genai.types.common.ListPromptsConfigDict,
            ]
        ] = None
    ) -> typing.AsyncIterator[vertexai._genai.types.common.PromptVersionRef]

Lists prompt version resources for a provided prompt_id.

See more: [vertexai._genai.prompts.AsyncPrompts.list_versions](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.AsyncPrompts#vertexai__genai_prompts_AsyncPrompts_list_versions)

### vertexai._genai.prompts.AsyncPrompts.optimize
    
    
    optimize(
        *,
        prompt: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.OptimizeConfig,
                vertexai._genai.types.common.OptimizeConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.OptimizeResponse

Makes an async request to the optimizePrompt endpoint and returns an optimized prompt.

See more: [vertexai._genai.prompts.AsyncPrompts.optimize](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.AsyncPrompts#vertexai__genai_prompts_AsyncPrompts_optimize)

### vertexai._genai.prompts.AsyncPrompts.restore_version
    
    
    restore_version(
        *,
        prompt_id: str,
        version_id: str,
        config: typing.Optional[vertexai._genai.types.common.RestoreVersionConfig] = None
    ) -> vertexai._genai.types.common.Prompt

Restores the provided prompt version to the latest version.

See more: [vertexai._genai.prompts.AsyncPrompts.restore_version](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.AsyncPrompts#vertexai__genai_prompts_AsyncPrompts_restore_version)

### vertexai._genai.prompts.AsyncPrompts.update
    
    
    update(
        *,
        prompt_id: str,
        prompt: typing.Union[
            vertexai._genai.types.common.Prompt, vertexai._genai.types.common.PromptDict
        ],
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.UpdatePromptConfig,
                vertexai._genai.types.common.UpdatePromptConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Prompt

Updates an existing prompt and creates a new version for the prompt associated with the provided prompt_id.

See more: [vertexai._genai.prompts.AsyncPrompts.update](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.AsyncPrompts#vertexai__genai_prompts_AsyncPrompts_update)

### vertexai._genai.prompts.Prompts.create
    
    
    create(
        *,
        prompt: typing.Union[
            vertexai._genai.types.common.Prompt, vertexai._genai.types.common.PromptDict
        ],
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CreatePromptConfig,
                vertexai._genai.types.common.CreatePromptConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Prompt

Creates a new prompt in a Vertex Dataset resource.

See more: [vertexai._genai.prompts.Prompts.create](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.Prompts#vertexai__genai_prompts_Prompts_create)

### vertexai._genai.prompts.Prompts.create_version
    
    
    create_version(
        *,
        prompt: typing.Union[
            vertexai._genai.types.common.Prompt, vertexai._genai.types.common.PromptDict
        ],
        prompt_id: typing.Optional[str] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CreatePromptVersionConfig,
                vertexai._genai.types.common.CreatePromptVersionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Prompt

Creates a prompt resource and an initial prompt version.

See more: [vertexai._genai.prompts.Prompts.create_version](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.Prompts#vertexai__genai_prompts_Prompts_create_version)

### vertexai._genai.prompts.Prompts.delete
    
    
    delete(
        *,
        prompt_id: str,
        config: typing.Optional[vertexai._genai.types.common.DeletePromptConfig] = None
    ) -> None

Deletes a prompt resource.

See more: [vertexai._genai.prompts.Prompts.delete](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.Prompts#vertexai__genai_prompts_Prompts_delete)

### vertexai._genai.prompts.Prompts.delete_version
    
    
    delete_version(
        *,
        prompt_id: str,
        version_id: str,
        config: typing.Optional[vertexai._genai.types.common.DeletePromptConfig] = None
    ) -> None

Deletes a prompt version resource.

See more: [vertexai._genai.prompts.Prompts.delete_version](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.Prompts#vertexai__genai_prompts_Prompts_delete_version)

### vertexai._genai.prompts.Prompts.get
    
    
    get(
        *,
        prompt_id: str,
        config: typing.Optional[vertexai._genai.types.common.GetPromptConfig] = None
    ) -> vertexai._genai.types.common.Prompt

Gets a prompt resource from a Vertex Dataset.

See more: [vertexai._genai.prompts.Prompts.get](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.Prompts#vertexai__genai_prompts_Prompts_get)

### vertexai._genai.prompts.Prompts.get_version
    
    
    get_version(
        *,
        prompt_id: str,
        version_id: str,
        config: typing.Optional[vertexai._genai.types.common.GetPromptConfig] = None
    ) -> vertexai._genai.types.common.Prompt

Gets a prompt resource from a Vertex Dataset.

See more: [vertexai._genai.prompts.Prompts.get_version](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.Prompts#vertexai__genai_prompts_Prompts_get_version)

### vertexai._genai.prompts.Prompts.launch_optimization_job
    
    
    launch_optimization_job(
        method: vertexai._genai.types.common.PromptOptimizerMethod,
        config: typing.Union[
            vertexai._genai.types.common.PromptOptimizerConfig,
            vertexai._genai.types.common.PromptOptimizerConfigDict,
        ],
    ) -> vertexai._genai.types.common.CustomJob

Call PO-Data optimizer.

See more: [vertexai._genai.prompts.Prompts.launch_optimization_job](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.Prompts#vertexai__genai_prompts_Prompts_launch_optimization_job)

### vertexai._genai.prompts.Prompts.list
    
    
    list(
        *,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListPromptsConfig,
                vertexai._genai.types.common.ListPromptsConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[vertexai._genai.types.common.PromptRef]

Lists prompt resources in a project.

See more: [vertexai._genai.prompts.Prompts.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.Prompts#vertexai__genai_prompts_Prompts_list)

### vertexai._genai.prompts.Prompts.list_versions
    
    
    list_versions(
        *,
        prompt_id: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListPromptsConfig,
                vertexai._genai.types.common.ListPromptsConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[vertexai._genai.types.common.PromptVersionRef]

Lists prompt version resources for a provided prompt_id.

See more: [vertexai._genai.prompts.Prompts.list_versions](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.Prompts#vertexai__genai_prompts_Prompts_list_versions)

### vertexai._genai.prompts.Prompts.optimize
    
    
    optimize(
        *,
        prompt: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.OptimizeConfig,
                vertexai._genai.types.common.OptimizeConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.OptimizeResponse

Makes an API request to optimize a prompt and returns the parsed response.

See more: [vertexai._genai.prompts.Prompts.optimize](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.Prompts#vertexai__genai_prompts_Prompts_optimize)

### vertexai._genai.prompts.Prompts.restore_version
    
    
    restore_version(
        *,
        prompt_id: str,
        version_id: str,
        config: typing.Optional[vertexai._genai.types.common.RestoreVersionConfig] = None
    ) -> vertexai._genai.types.common.Prompt

Restores the provided prompt version to the latest version.

See more: [vertexai._genai.prompts.Prompts.restore_version](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.Prompts#vertexai__genai_prompts_Prompts_restore_version)

### vertexai._genai.prompts.Prompts.update
    
    
    update(
        *,
        prompt_id: str,
        prompt: typing.Union[
            vertexai._genai.types.common.Prompt, vertexai._genai.types.common.PromptDict
        ],
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.UpdatePromptConfig,
                vertexai._genai.types.common.UpdatePromptConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Prompt

Updates an existing prompt and creates a new version for the prompt associated with the provided prompt_id.

See more: [vertexai._genai.prompts.Prompts.update](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.prompts.Prompts#vertexai__genai_prompts_Prompts_update)

### vertexai._genai.sandboxes.Sandboxes.create
    
    
    create(
        *,
        name: str,
        poll_interval_seconds: float = 0.1,
        spec: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.SandboxEnvironmentSpec,
                vertexai._genai.types.common.SandboxEnvironmentSpecDict,
            ]
        ] = None,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CreateAgentEngineSandboxConfig,
                vertexai._genai.types.common.CreateAgentEngineSandboxConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngineSandboxOperation

Creates a new sandbox in the Agent Engine.

See more: [vertexai._genai.sandboxes.Sandboxes.create](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.sandboxes.Sandboxes#vertexai__genai_sandboxes_Sandboxes_create)

### vertexai._genai.sandboxes.Sandboxes.delete
    
    
    delete(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteAgentEngineSandboxConfig,
                vertexai._genai.types.common.DeleteAgentEngineSandboxConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.DeleteAgentEngineSandboxOperation

Deletes an agent engine sandbox.

See more: [vertexai._genai.sandboxes.Sandboxes.delete](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.sandboxes.Sandboxes#vertexai__genai_sandboxes_Sandboxes_delete)

### vertexai._genai.sandboxes.Sandboxes.execute_code
    
    
    execute_code(
        *,
        name: str,
        input_data: dict[str, typing.Any],
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ExecuteCodeAgentEngineSandboxConfig,
                vertexai._genai.types.common.ExecuteCodeAgentEngineSandboxConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.ExecuteSandboxEnvironmentResponse

Executes code in the Agent Engine sandbox.

See more: [vertexai._genai.sandboxes.Sandboxes.execute_code](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.sandboxes.Sandboxes#vertexai__genai_sandboxes_Sandboxes_execute_code)

### vertexai._genai.sandboxes.Sandboxes.generate_access_token
    
    
    generate_access_token(service_account_email: str, timeout: int = 3600) -> str

Signs a JWT with a Google Cloud service account.

See more: [vertexai._genai.sandboxes.Sandboxes.generate_access_token](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.sandboxes.Sandboxes#vertexai__genai_sandboxes_Sandboxes_generate_access_token)

### vertexai._genai.sandboxes.Sandboxes.generate_browser_ws_headers
    
    
    generate_browser_ws_headers(
        sandbox_environment: vertexai._genai.types.common.SandboxEnvironment,
        service_account_email: str,
        port: str = "8080",
        timeout: int = 3600,
        psc_endpoint: typing.Optional[str] = None,
    ) -> tuple[str, dict[str, str]]

Generates the websocket upgrade headers for the browser.

See more: [vertexai._genai.sandboxes.Sandboxes.generate_browser_ws_headers](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.sandboxes.Sandboxes#vertexai__genai_sandboxes_Sandboxes_generate_browser_ws_headers)

### vertexai._genai.sandboxes.Sandboxes.get
    
    
    get(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetAgentEngineSandboxConfig,
                vertexai._genai.types.common.GetAgentEngineSandboxConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.SandboxEnvironment

Gets an agent engine sandbox.

See more: [vertexai._genai.sandboxes.Sandboxes.get](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.sandboxes.Sandboxes#vertexai__genai_sandboxes_Sandboxes_get)

### vertexai._genai.sandboxes.Sandboxes.list
    
    
    list(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineSandboxesConfig,
                vertexai._genai.types.common.ListAgentEngineSandboxesConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[vertexai._genai.types.common.SandboxEnvironment]

Lists Agent Engine sandboxes.

See more: [vertexai._genai.sandboxes.Sandboxes.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.sandboxes.Sandboxes#vertexai__genai_sandboxes_Sandboxes_list)

### vertexai._genai.sandboxes.Sandboxes.send_command
    
    
    send_command(
        *,
        http_method: str,
        access_token: str,
        sandbox_environment: vertexai._genai.types.common.SandboxEnvironment,
        port: str = "8080",
        path: typing.Optional[str] = None,
        query_params: typing.Optional[dict[str, object]] = None,
        headers: typing.Optional[dict[str, str]] = None,
        request_dict: typing.Optional[dict[str, object]] = None,
        psc_endpoint: typing.Optional[str] = None
    ) -> google.genai.types.HttpResponse

Sends a command to the sandbox.

See more: [vertexai._genai.sandboxes.Sandboxes.send_command](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.sandboxes.Sandboxes#vertexai__genai_sandboxes_Sandboxes_send_command)

### vertexai._genai.session_events.AsyncSessionEvents.append
    
    
    append(
        *,
        name: str,
        author: str,
        invocation_id: str,
        timestamp: datetime.datetime,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.AppendAgentEngineSessionEventConfig,
                vertexai._genai.types.common.AppendAgentEngineSessionEventConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AppendAgentEngineSessionEventResponse

Appends Agent Engine session event.

See more: [vertexai._genai.session_events.AsyncSessionEvents.append](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.session_events.AsyncSessionEvents#vertexai__genai_session_events_AsyncSessionEvents_append)

### vertexai._genai.session_events.AsyncSessionEvents.list
    
    
    list(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineSessionEventsConfig,
                vertexai._genai.types.common.ListAgentEngineSessionEventsConfigDict,
            ]
        ] = None
    ) -> google.genai.pagers.AsyncPager[vertexai._genai.types.common.SessionEvent]

Lists Agent Engine session events.

See more: [vertexai._genai.session_events.AsyncSessionEvents.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.session_events.AsyncSessionEvents#vertexai__genai_session_events_AsyncSessionEvents_list)

### vertexai._genai.session_events.SessionEvents.append
    
    
    append(
        *,
        name: str,
        author: str,
        invocation_id: str,
        timestamp: datetime.datetime,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.AppendAgentEngineSessionEventConfig,
                vertexai._genai.types.common.AppendAgentEngineSessionEventConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AppendAgentEngineSessionEventResponse

Appends Agent Engine session event.

See more: [vertexai._genai.session_events.SessionEvents.append](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.session_events.SessionEvents#vertexai__genai_session_events_SessionEvents_append)

### vertexai._genai.session_events.SessionEvents.list
    
    
    list(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineSessionEventsConfig,
                vertexai._genai.types.common.ListAgentEngineSessionEventsConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[vertexai._genai.types.common.SessionEvent]

Lists Agent Engine session events.

See more: [vertexai._genai.session_events.SessionEvents.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.session_events.SessionEvents#vertexai__genai_session_events_SessionEvents_list)

### vertexai._genai.sessions.AsyncSessions.create
    
    
    create(
        *,
        name: str,
        user_id: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CreateAgentEngineSessionConfig,
                vertexai._genai.types.common.CreateAgentEngineSessionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngineSessionOperation

Creates a new session in the Agent Engine.

See more: [vertexai._genai.sessions.AsyncSessions.create](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.sessions.AsyncSessions#vertexai__genai_sessions_AsyncSessions_create)

### vertexai._genai.sessions.AsyncSessions.delete
    
    
    delete(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteAgentEngineSessionConfig,
                vertexai._genai.types.common.DeleteAgentEngineSessionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.DeleteAgentEngineSessionOperation

Delete an Agent Engine session.

See more: [vertexai._genai.sessions.AsyncSessions.delete](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.sessions.AsyncSessions#vertexai__genai_sessions_AsyncSessions_delete)

### vertexai._genai.sessions.AsyncSessions.get
    
    
    get(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetAgentEngineSessionConfig,
                vertexai._genai.types.common.GetAgentEngineSessionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Session

Gets an agent engine session.

See more: [vertexai._genai.sessions.AsyncSessions.get](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.sessions.AsyncSessions#vertexai__genai_sessions_AsyncSessions_get)

### vertexai._genai.sessions.AsyncSessions.list
    
    
    list(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineSessionsConfig,
                vertexai._genai.types.common.ListAgentEngineSessionsConfigDict,
            ]
        ] = None
    ) -> google.genai.pagers.AsyncPager[vertexai._genai.types.common.Session]

Lists Agent Engine sessions.

See more: [vertexai._genai.sessions.AsyncSessions.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.sessions.AsyncSessions#vertexai__genai_sessions_AsyncSessions_list)

### vertexai._genai.sessions.Sessions.create
    
    
    create(
        *,
        name: str,
        user_id: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CreateAgentEngineSessionConfig,
                vertexai._genai.types.common.CreateAgentEngineSessionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.AgentEngineSessionOperation

Creates a new session in the Agent Engine.

See more: [vertexai._genai.sessions.Sessions.create](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.sessions.Sessions#vertexai__genai_sessions_Sessions_create)

### vertexai._genai.sessions.Sessions.delete
    
    
    delete(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteAgentEngineSessionConfig,
                vertexai._genai.types.common.DeleteAgentEngineSessionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.DeleteAgentEngineSessionOperation

Delete an Agent Engine session.

See more: [vertexai._genai.sessions.Sessions.delete](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.sessions.Sessions#vertexai__genai_sessions_Sessions_delete)

### vertexai._genai.sessions.Sessions.get
    
    
    get(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetAgentEngineSessionConfig,
                vertexai._genai.types.common.GetAgentEngineSessionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Session

Gets an agent engine session.

See more: [vertexai._genai.sessions.Sessions.get](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.sessions.Sessions#vertexai__genai_sessions_Sessions_get)

### vertexai._genai.sessions.Sessions.list
    
    
    list(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListAgentEngineSessionsConfig,
                vertexai._genai.types.common.ListAgentEngineSessionsConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[vertexai._genai.types.common.Session]

Lists Agent Engine sessions.

See more: [vertexai._genai.sessions.Sessions.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.sessions.Sessions#vertexai__genai_sessions_Sessions_list)

### vertexai._genai.skill_revisions.AsyncSkillRevisions.get
    
    
    get(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetSkillRevisionConfig,
                vertexai._genai.types.common.GetSkillRevisionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.SkillRevision

Gets a Skill Revision.

See more: [vertexai._genai.skill_revisions.AsyncSkillRevisions.get](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.skill_revisions.AsyncSkillRevisions#vertexai__genai_skill_revisions_AsyncSkillRevisions_get)

### vertexai._genai.skill_revisions.AsyncSkillRevisions.list
    
    
    list(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListSkillRevisionsConfig,
                vertexai._genai.types.common.ListSkillRevisionsConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.ListSkillRevisionsResponse

Lists Skill Revisions.

See more: [vertexai._genai.skill_revisions.AsyncSkillRevisions.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.skill_revisions.AsyncSkillRevisions#vertexai__genai_skill_revisions_AsyncSkillRevisions_list)

### vertexai._genai.skill_revisions.SkillRevisions.get
    
    
    get(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetSkillRevisionConfig,
                vertexai._genai.types.common.GetSkillRevisionConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.SkillRevision

Gets a Skill Revision.

See more: [vertexai._genai.skill_revisions.SkillRevisions.get](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.skill_revisions.SkillRevisions#vertexai__genai_skill_revisions_SkillRevisions_get)

### vertexai._genai.skill_revisions.SkillRevisions.list
    
    
    list(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListSkillRevisionsConfig,
                vertexai._genai.types.common.ListSkillRevisionsConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.ListSkillRevisionsResponse

Lists Skill Revisions.

See more: [vertexai._genai.skill_revisions.SkillRevisions.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.skill_revisions.SkillRevisions#vertexai__genai_skill_revisions_SkillRevisions_list)

### vertexai._genai.skills.AsyncSkills.create
    
    
    create(
        *,
        display_name: str,
        description: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CreateSkillConfig,
                vertexai._genai.types.common.CreateSkillConfigDict,
            ]
        ] = None
    ) -> typing.Union[
        vertexai._genai.types.common.Skill, vertexai._genai.types.common.SkillOperation
    ]

Creates a new Skill asynchronously.

See more: [vertexai._genai.skills.AsyncSkills.create](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.skills.AsyncSkills#vertexai__genai_skills_AsyncSkills_create)

### vertexai._genai.skills.AsyncSkills.delete
    
    
    delete(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteSkillConfig,
                vertexai._genai.types.common.DeleteSkillConfigDict,
            ]
        ] = None
    ) -> typing.Optional[vertexai._genai.types.common.DeleteSkillOperation]

Deletes a Skill asynchronously.

See more: [vertexai._genai.skills.AsyncSkills.delete](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.skills.AsyncSkills#vertexai__genai_skills_AsyncSkills_delete)

### vertexai._genai.skills.AsyncSkills.get
    
    
    get(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetSkillConfig,
                vertexai._genai.types.common.GetSkillConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Skill

Gets a Skill.

See more: [vertexai._genai.skills.AsyncSkills.get](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.skills.AsyncSkills#vertexai__genai_skills_AsyncSkills_get)

### vertexai._genai.skills.AsyncSkills.list
    
    
    list(
        *,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListSkillsConfig,
                vertexai._genai.types.common.ListSkillsConfigDict,
            ]
        ] = None
    ) -> google.genai.pagers.AsyncPager[vertexai._genai.types.common.Skill]

Lists Skills in the Skill Registry asynchronously.

See more: [vertexai._genai.skills.AsyncSkills.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.skills.AsyncSkills#vertexai__genai_skills_AsyncSkills_list)

### vertexai._genai.skills.AsyncSkills.retrieve
    
    
    retrieve(
        *,
        query: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RetrieveSkillsConfig,
                vertexai._genai.types.common.RetrieveSkillsConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.RetrieveSkillsResponse

Retrieves skills semantically matched to a query.

See more: [vertexai._genai.skills.AsyncSkills.retrieve](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.skills.AsyncSkills#vertexai__genai_skills_AsyncSkills_retrieve)

### vertexai._genai.skills.AsyncSkills.update
    
    
    update(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.UpdateSkillConfig,
                vertexai._genai.types.common.UpdateSkillConfigDict,
            ]
        ] = None
    ) -> typing.Union[
        vertexai._genai.types.common.Skill, vertexai._genai.types.common.SkillOperation
    ]

Updates an existing Skill asynchronously.

See more: [vertexai._genai.skills.AsyncSkills.update](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.skills.AsyncSkills#vertexai__genai_skills_AsyncSkills_update)

### vertexai._genai.skills.Skills.create
    
    
    create(
        *,
        display_name: str,
        description: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.CreateSkillConfig,
                vertexai._genai.types.common.CreateSkillConfigDict,
            ]
        ] = None
    ) -> typing.Union[
        vertexai._genai.types.common.Skill, vertexai._genai.types.common.SkillOperation
    ]

Creates a new Skill.

See more: [vertexai._genai.skills.Skills.create](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.skills.Skills#vertexai__genai_skills_Skills_create)

### vertexai._genai.skills.Skills.delete
    
    
    delete(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteSkillConfig,
                vertexai._genai.types.common.DeleteSkillConfigDict,
            ]
        ] = None
    ) -> typing.Optional[vertexai._genai.types.common.DeleteSkillOperation]

Deletes a Skill.

See more: [vertexai._genai.skills.Skills.delete](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.skills.Skills#vertexai__genai_skills_Skills_delete)

### vertexai._genai.skills.Skills.get
    
    
    get(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.GetSkillConfig,
                vertexai._genai.types.common.GetSkillConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.Skill

Gets a Skill.

See more: [vertexai._genai.skills.Skills.get](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.skills.Skills#vertexai__genai_skills_Skills_get)

### vertexai._genai.skills.Skills.list
    
    
    list(
        *,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.ListSkillsConfig,
                vertexai._genai.types.common.ListSkillsConfigDict,
            ]
        ] = None
    ) -> typing.Iterator[vertexai._genai.types.common.Skill]

Lists Skills in the Skill Registry.

See more: [vertexai._genai.skills.Skills.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.skills.Skills#vertexai__genai_skills_Skills_list)

### vertexai._genai.skills.Skills.retrieve
    
    
    retrieve(
        *,
        query: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.RetrieveSkillsConfig,
                vertexai._genai.types.common.RetrieveSkillsConfigDict,
            ]
        ] = None
    ) -> vertexai._genai.types.common.RetrieveSkillsResponse

Retrieves skills semantically matched to a query.

See more: [vertexai._genai.skills.Skills.retrieve](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.skills.Skills#vertexai__genai_skills_Skills_retrieve)

### vertexai._genai.skills.Skills.update
    
    
    update(
        *,
        name: str,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.UpdateSkillConfig,
                vertexai._genai.types.common.UpdateSkillConfigDict,
            ]
        ] = None
    ) -> typing.Union[
        vertexai._genai.types.common.Skill, vertexai._genai.types.common.SkillOperation
    ]

Updates an existing Skill.

See more: [vertexai._genai.skills.Skills.update](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.skills.Skills#vertexai__genai_skills_Skills_update)

### vertexai._genai.types.A2aTask
    
    
    A2aTask(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.A2aTask](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.A2aTask#vertexai__genai_types_A2aTask_A2aTask)

### vertexai._genai.types.AgentEngine
    
    
    AgentEngine(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AgentEngine](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AgentEngine#vertexai__genai_types_AgentEngine_AgentEngine)

### vertexai._genai.types.AgentEngine.delete
    
    
    delete(
        force: bool = False,
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteAgentEngineConfig,
                vertexai._genai.types.common.DeleteAgentEngineConfigDict,
            ]
        ] = None,
    ) -> None

Deletes the agent engine.

See more: [vertexai._genai.types.AgentEngine.delete](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AgentEngine#vertexai__genai_types_AgentEngine_delete)

### vertexai._genai.types.AgentEngine.operation_schemas
    
    
    operation_schemas() -> typing.Optional[list[typing.Dict[str, typing.Any]]]

Returns the schemas of all registered operations for the agent.

See more: [vertexai._genai.types.AgentEngine.operation_schemas](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AgentEngine#vertexai__genai_types_AgentEngine_operation_schemas)

### vertexai._genai.types.AgentEngineConfig
    
    
    AgentEngineConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AgentEngineConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AgentEngineConfig#vertexai__genai_types_AgentEngineConfig_AgentEngineConfig)

### vertexai._genai.types.AgentEngineGenerateMemoriesOperation
    
    
    AgentEngineGenerateMemoriesOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AgentEngineGenerateMemoriesOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AgentEngineGenerateMemoriesOperation#vertexai__genai_types_AgentEngineGenerateMemoriesOperation_AgentEngineGenerateMemoriesOperation)

### vertexai._genai.types.AgentEngineMemoryConfig
    
    
    AgentEngineMemoryConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AgentEngineMemoryConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AgentEngineMemoryConfig#vertexai__genai_types_AgentEngineMemoryConfig_AgentEngineMemoryConfig)

### vertexai._genai.types.AgentEngineMemoryOperation
    
    
    AgentEngineMemoryOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AgentEngineMemoryOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AgentEngineMemoryOperation#vertexai__genai_types_AgentEngineMemoryOperation_AgentEngineMemoryOperation)

### vertexai._genai.types.AgentEngineOperation
    
    
    AgentEngineOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AgentEngineOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AgentEngineOperation#vertexai__genai_types_AgentEngineOperation_AgentEngineOperation)

### vertexai._genai.types.AgentEnginePurgeMemoriesOperation
    
    
    AgentEnginePurgeMemoriesOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AgentEnginePurgeMemoriesOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AgentEnginePurgeMemoriesOperation#vertexai__genai_types_AgentEnginePurgeMemoriesOperation_AgentEnginePurgeMemoriesOperation)

### vertexai._genai.types.AgentEngineRollbackMemoryOperation
    
    
    AgentEngineRollbackMemoryOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AgentEngineRollbackMemoryOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AgentEngineRollbackMemoryOperation#vertexai__genai_types_AgentEngineRollbackMemoryOperation_AgentEngineRollbackMemoryOperation)

### vertexai._genai.types.AgentEngineRuntimeRevision
    
    
    AgentEngineRuntimeRevision(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AgentEngineRuntimeRevision](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AgentEngineRuntimeRevision#vertexai__genai_types_AgentEngineRuntimeRevision_AgentEngineRuntimeRevision)

### vertexai._genai.types.AgentEngineRuntimeRevision.delete
    
    
    delete(
        config: typing.Optional[
            typing.Union[
                vertexai._genai.types.common.DeleteAgentEngineRuntimeRevisionConfig,
                vertexai._genai.types.common.DeleteAgentEngineRuntimeRevisionConfigDict,
            ]
        ] = None,
    ) -> None

Deletes the agent engine runtime revision.

See more: [vertexai._genai.types.AgentEngineRuntimeRevision.delete](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AgentEngineRuntimeRevision#vertexai__genai_types_AgentEngineRuntimeRevision_delete)

### vertexai._genai.types.AgentEngineRuntimeRevision.operation_schemas
    
    
    operation_schemas() -> typing.Optional[list[typing.Dict[str, typing.Any]]]

Returns the schemas of all registered operations for the agent.

See more: [vertexai._genai.types.AgentEngineRuntimeRevision.operation_schemas](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AgentEngineRuntimeRevision#vertexai__genai_types_AgentEngineRuntimeRevision_operation_schemas)

### vertexai._genai.types.AgentEngineSandboxOperation
    
    
    AgentEngineSandboxOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AgentEngineSandboxOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AgentEngineSandboxOperation#vertexai__genai_types_AgentEngineSandboxOperation_AgentEngineSandboxOperation)

### vertexai._genai.types.AgentEngineSandboxSnapshotOperation
    
    
    AgentEngineSandboxSnapshotOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AgentEngineSandboxSnapshotOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AgentEngineSandboxSnapshotOperation#vertexai__genai_types_AgentEngineSandboxSnapshotOperation_AgentEngineSandboxSnapshotOperation)

### vertexai._genai.types.AgentEngineSessionOperation
    
    
    AgentEngineSessionOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AgentEngineSessionOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AgentEngineSessionOperation#vertexai__genai_types_AgentEngineSessionOperation_AgentEngineSessionOperation)

### vertexai._genai.types.AgentRunConfig
    
    
    AgentRunConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AgentRunConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AgentRunConfig#vertexai__genai_types_AgentRunConfig_AgentRunConfig)

### vertexai._genai.types.AggregatedMetricResult
    
    
    AggregatedMetricResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AggregatedMetricResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AggregatedMetricResult#vertexai__genai_types_AggregatedMetricResult_AggregatedMetricResult)

### vertexai._genai.types.AnalysisConfig
    
    
    AnalysisConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AnalysisConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AnalysisConfig#vertexai__genai_types_AnalysisConfig_AnalysisConfig)

### vertexai._genai.types.AppendAgentEngineSessionEventConfig
    
    
    AppendAgentEngineSessionEventConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AppendAgentEngineSessionEventConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AppendAgentEngineSessionEventConfig#vertexai__genai_types_AppendAgentEngineSessionEventConfig_AppendAgentEngineSessionEventConfig)

### vertexai._genai.types.AppendAgentEngineSessionEventResponse
    
    
    AppendAgentEngineSessionEventResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AppendAgentEngineSessionEventResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AppendAgentEngineSessionEventResponse#vertexai__genai_types_AppendAgentEngineSessionEventResponse_AppendAgentEngineSessionEventResponse)

### vertexai._genai.types.AppendAgentEngineTaskEventConfig
    
    
    AppendAgentEngineTaskEventConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AppendAgentEngineTaskEventConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AppendAgentEngineTaskEventConfig#vertexai__genai_types_AppendAgentEngineTaskEventConfig_AppendAgentEngineTaskEventConfig)

### vertexai._genai.types.AppendAgentEngineTaskEventResponse
    
    
    AppendAgentEngineTaskEventResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AppendAgentEngineTaskEventResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AppendAgentEngineTaskEventResponse#vertexai__genai_types_AppendAgentEngineTaskEventResponse_AppendAgentEngineTaskEventResponse)

### vertexai._genai.types.AssembleDataset
    
    
    AssembleDataset(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AssembleDataset](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AssembleDataset#vertexai__genai_types_AssembleDataset_AssembleDataset)

### vertexai._genai.types.AssembleDatasetConfig
    
    
    AssembleDatasetConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AssembleDatasetConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AssembleDatasetConfig#vertexai__genai_types_AssembleDatasetConfig_AssembleDatasetConfig)

### vertexai._genai.types.AssessDatasetConfig
    
    
    AssessDatasetConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AssessDatasetConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AssessDatasetConfig#vertexai__genai_types_AssessDatasetConfig_AssessDatasetConfig)

### vertexai._genai.types.AttackCategoryResult
    
    
    AttackCategoryResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.AttackCategoryResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.AttackCategoryResult#vertexai__genai_types_AttackCategoryResult_AttackCategoryResult)

### vertexai._genai.types.BatchPredictionResourceUsageAssessmentConfig
    
    
    BatchPredictionResourceUsageAssessmentConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.BatchPredictionResourceUsageAssessmentConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.BatchPredictionResourceUsageAssessmentConfig#vertexai__genai_types_BatchPredictionResourceUsageAssessmentConfig_BatchPredictionResourceUsageAssessmentConfig)

### vertexai._genai.types.BatchPredictionResourceUsageAssessmentResult
    
    
    BatchPredictionResourceUsageAssessmentResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.BatchPredictionResourceUsageAssessmentResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.BatchPredictionResourceUsageAssessmentResult#vertexai__genai_types_BatchPredictionResourceUsageAssessmentResult_BatchPredictionResourceUsageAssessmentResult)

### vertexai._genai.types.BatchPredictionValidationAssessmentConfig
    
    
    BatchPredictionValidationAssessmentConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.BatchPredictionValidationAssessmentConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.BatchPredictionValidationAssessmentConfig#vertexai__genai_types_BatchPredictionValidationAssessmentConfig_BatchPredictionValidationAssessmentConfig)

### vertexai._genai.types.BatchPredictionValidationAssessmentResult
    
    
    BatchPredictionValidationAssessmentResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.BatchPredictionValidationAssessmentResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.BatchPredictionValidationAssessmentResult#vertexai__genai_types_BatchPredictionValidationAssessmentResult_BatchPredictionValidationAssessmentResult)

### vertexai._genai.types.BigQueryRequestSet
    
    
    BigQueryRequestSet(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.BigQueryRequestSet](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.BigQueryRequestSet#vertexai__genai_types_BigQueryRequestSet_BigQueryRequestSet)

### vertexai._genai.types.BleuInstance
    
    
    BleuInstance(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.BleuInstance](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.BleuInstance#vertexai__genai_types_BleuInstance_BleuInstance)

### vertexai._genai.types.BleuResults
    
    
    BleuResults(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.BleuResults](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.BleuResults#vertexai__genai_types_BleuResults_BleuResults)

### vertexai._genai.types.CancelQueryJobAgentEngineConfig
    
    
    CancelQueryJobAgentEngineConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CancelQueryJobAgentEngineConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CancelQueryJobAgentEngineConfig#vertexai__genai_types_CancelQueryJobAgentEngineConfig_CancelQueryJobAgentEngineConfig)

### vertexai._genai.types.CancelQueryJobResult
    
    
    CancelQueryJobResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CancelQueryJobResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CancelQueryJobResult#vertexai__genai_types_CancelQueryJobResult_CancelQueryJobResult)

### vertexai._genai.types.CandidateResponse
    
    
    CandidateResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CandidateResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CandidateResponse#vertexai__genai_types_CandidateResponse_CandidateResponse)

### vertexai._genai.types.CandidateResult
    
    
    CandidateResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CandidateResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CandidateResult#vertexai__genai_types_CandidateResult_CandidateResult)

### vertexai._genai.types.CheckQueryJobAgentEngineConfig
    
    
    CheckQueryJobAgentEngineConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CheckQueryJobAgentEngineConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CheckQueryJobAgentEngineConfig#vertexai__genai_types_CheckQueryJobAgentEngineConfig_CheckQueryJobAgentEngineConfig)

### vertexai._genai.types.CheckQueryJobResponse
    
    
    CheckQueryJobResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CheckQueryJobResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CheckQueryJobResponse#vertexai__genai_types_CheckQueryJobResponse_CheckQueryJobResponse)

### vertexai._genai.types.CheckQueryJobResult
    
    
    CheckQueryJobResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CheckQueryJobResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CheckQueryJobResult#vertexai__genai_types_CheckQueryJobResult_CheckQueryJobResult)

### vertexai._genai.types.Chunk
    
    
    Chunk(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.Chunk](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.Chunk#vertexai__genai_types_Chunk_Chunk)

### vertexai._genai.types.CodeExecutionMetric
    
    
    CodeExecutionMetric(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CodeExecutionMetric](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CodeExecutionMetric#vertexai__genai_types_CodeExecutionMetric_CodeExecutionMetric)

### vertexai._genai.types.CodeExecutionMetric.model_post_init
    
    
    model_post_init(context: Any, /) -> None

This function is meant to behave like a BaseModel method to initialize private attributes.

See more: [vertexai._genai.types.CodeExecutionMetric.model_post_init](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CodeExecutionMetric#vertexai__genai_types_CodeExecutionMetric_model_post_init)

### vertexai._genai.types.CodeExecutionMetric.validate_code
    
    
    validate_code(value: typing.Optional[str]) -> typing.Optional[str]

API documentation for `validate_code` method.

See more: [vertexai._genai.types.CodeExecutionMetric.validate_code](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CodeExecutionMetric#vertexai__genai_types_CodeExecutionMetric_validate_code)

### vertexai._genai.types.CometResult
    
    
    CometResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CometResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CometResult#vertexai__genai_types_CometResult_CometResult)

### vertexai._genai.types.ContainerSpec
    
    
    ContainerSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ContainerSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ContainerSpec#vertexai__genai_types_ContainerSpec_ContainerSpec)

### vertexai._genai.types.ContentMap
    
    
    ContentMap(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ContentMap](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ContentMap#vertexai__genai_types_ContentMap_ContentMap)

### vertexai._genai.types.ContentMapContents
    
    
    ContentMapContents(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ContentMapContents](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ContentMapContents#vertexai__genai_types_ContentMapContents_ContentMapContents)

### vertexai._genai.types.CreateAgentEngineConfig
    
    
    CreateAgentEngineConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CreateAgentEngineConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CreateAgentEngineConfig#vertexai__genai_types_CreateAgentEngineConfig_CreateAgentEngineConfig)

### vertexai._genai.types.CreateAgentEngineSandboxConfig
    
    
    CreateAgentEngineSandboxConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CreateAgentEngineSandboxConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CreateAgentEngineSandboxConfig#vertexai__genai_types_CreateAgentEngineSandboxConfig_CreateAgentEngineSandboxConfig)

### vertexai._genai.types.CreateAgentEngineSandboxSnapshotConfig
    
    
    CreateAgentEngineSandboxSnapshotConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CreateAgentEngineSandboxSnapshotConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CreateAgentEngineSandboxSnapshotConfig#vertexai__genai_types_CreateAgentEngineSandboxSnapshotConfig_CreateAgentEngineSandboxSnapshotConfig)

### vertexai._genai.types.CreateAgentEngineSessionConfig
    
    
    CreateAgentEngineSessionConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CreateAgentEngineSessionConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CreateAgentEngineSessionConfig#vertexai__genai_types_CreateAgentEngineSessionConfig_CreateAgentEngineSessionConfig)

### vertexai._genai.types.CreateAgentEngineTaskConfig
    
    
    CreateAgentEngineTaskConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CreateAgentEngineTaskConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CreateAgentEngineTaskConfig#vertexai__genai_types_CreateAgentEngineTaskConfig_CreateAgentEngineTaskConfig)

### vertexai._genai.types.CreateDatasetConfig
    
    
    CreateDatasetConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CreateDatasetConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CreateDatasetConfig#vertexai__genai_types_CreateDatasetConfig_CreateDatasetConfig)

### vertexai._genai.types.CreateDatasetVersionConfig
    
    
    CreateDatasetVersionConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CreateDatasetVersionConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CreateDatasetVersionConfig#vertexai__genai_types_CreateDatasetVersionConfig_CreateDatasetVersionConfig)

### vertexai._genai.types.CreateEvaluationExperimentConfig
    
    
    CreateEvaluationExperimentConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CreateEvaluationExperimentConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CreateEvaluationExperimentConfig#vertexai__genai_types_CreateEvaluationExperimentConfig_CreateEvaluationExperimentConfig)

### vertexai._genai.types.CreateEvaluationItemConfig
    
    
    CreateEvaluationItemConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CreateEvaluationItemConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CreateEvaluationItemConfig#vertexai__genai_types_CreateEvaluationItemConfig_CreateEvaluationItemConfig)

### vertexai._genai.types.CreateEvaluationMetricConfig
    
    
    CreateEvaluationMetricConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CreateEvaluationMetricConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CreateEvaluationMetricConfig#vertexai__genai_types_CreateEvaluationMetricConfig_CreateEvaluationMetricConfig)

### vertexai._genai.types.CreateEvaluationRunConfig
    
    
    CreateEvaluationRunConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CreateEvaluationRunConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CreateEvaluationRunConfig#vertexai__genai_types_CreateEvaluationRunConfig_CreateEvaluationRunConfig)

### vertexai._genai.types.CreateEvaluationSetConfig
    
    
    CreateEvaluationSetConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CreateEvaluationSetConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CreateEvaluationSetConfig#vertexai__genai_types_CreateEvaluationSetConfig_CreateEvaluationSetConfig)

### vertexai._genai.types.CreateMultimodalDatasetConfig
    
    
    CreateMultimodalDatasetConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CreateMultimodalDatasetConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CreateMultimodalDatasetConfig#vertexai__genai_types_CreateMultimodalDatasetConfig_CreateMultimodalDatasetConfig)

### vertexai._genai.types.CreatePromptConfig
    
    
    CreatePromptConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CreatePromptConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CreatePromptConfig#vertexai__genai_types_CreatePromptConfig_CreatePromptConfig)

### vertexai._genai.types.CreatePromptVersionConfig
    
    
    CreatePromptVersionConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CreatePromptVersionConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CreatePromptVersionConfig#vertexai__genai_types_CreatePromptVersionConfig_CreatePromptVersionConfig)

### vertexai._genai.types.CreateSandboxEnvironmentTemplateConfig
    
    
    CreateSandboxEnvironmentTemplateConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CreateSandboxEnvironmentTemplateConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CreateSandboxEnvironmentTemplateConfig#vertexai__genai_types_CreateSandboxEnvironmentTemplateConfig_CreateSandboxEnvironmentTemplateConfig)

### vertexai._genai.types.CreateSkillConfig
    
    
    CreateSkillConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CreateSkillConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CreateSkillConfig#vertexai__genai_types_CreateSkillConfig_CreateSkillConfig)

### vertexai._genai.types.CustomCodeExecutionSpec
    
    
    CustomCodeExecutionSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CustomCodeExecutionSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CustomCodeExecutionSpec#vertexai__genai_types_CustomCodeExecutionSpec_CustomCodeExecutionSpec)

### vertexai._genai.types.CustomJob
    
    
    CustomJob(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CustomJob](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CustomJob#vertexai__genai_types_CustomJob_CustomJob)

### vertexai._genai.types.CustomJobSpec
    
    
    CustomJobSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.CustomJobSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.CustomJobSpec#vertexai__genai_types_CustomJobSpec_CustomJobSpec)

### vertexai._genai.types.Dataset
    
    
    Dataset(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.Dataset](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.Dataset#vertexai__genai_types_Dataset_Dataset)

### vertexai._genai.types.DatasetOperation
    
    
    DatasetOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DatasetOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DatasetOperation#vertexai__genai_types_DatasetOperation_DatasetOperation)

### vertexai._genai.types.DatasetVersion
    
    
    DatasetVersion(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DatasetVersion](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DatasetVersion#vertexai__genai_types_DatasetVersion_DatasetVersion)

### vertexai._genai.types.DeleteAgentEngineConfig
    
    
    DeleteAgentEngineConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteAgentEngineConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteAgentEngineConfig#vertexai__genai_types_DeleteAgentEngineConfig_DeleteAgentEngineConfig)

### vertexai._genai.types.DeleteAgentEngineMemoryConfig
    
    
    DeleteAgentEngineMemoryConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteAgentEngineMemoryConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteAgentEngineMemoryConfig#vertexai__genai_types_DeleteAgentEngineMemoryConfig_DeleteAgentEngineMemoryConfig)

### vertexai._genai.types.DeleteAgentEngineMemoryOperation
    
    
    DeleteAgentEngineMemoryOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteAgentEngineMemoryOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteAgentEngineMemoryOperation#vertexai__genai_types_DeleteAgentEngineMemoryOperation_DeleteAgentEngineMemoryOperation)

### vertexai._genai.types.DeleteAgentEngineOperation
    
    
    DeleteAgentEngineOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteAgentEngineOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteAgentEngineOperation#vertexai__genai_types_DeleteAgentEngineOperation_DeleteAgentEngineOperation)

### vertexai._genai.types.DeleteAgentEngineRuntimeRevisionConfig
    
    
    DeleteAgentEngineRuntimeRevisionConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteAgentEngineRuntimeRevisionConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteAgentEngineRuntimeRevisionConfig#vertexai__genai_types_DeleteAgentEngineRuntimeRevisionConfig_DeleteAgentEngineRuntimeRevisionConfig)

### vertexai._genai.types.DeleteAgentEngineRuntimeRevisionOperation
    
    
    DeleteAgentEngineRuntimeRevisionOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteAgentEngineRuntimeRevisionOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteAgentEngineRuntimeRevisionOperation#vertexai__genai_types_DeleteAgentEngineRuntimeRevisionOperation_DeleteAgentEngineRuntimeRevisionOperation)

### vertexai._genai.types.DeleteAgentEngineSandboxConfig
    
    
    DeleteAgentEngineSandboxConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteAgentEngineSandboxConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteAgentEngineSandboxConfig#vertexai__genai_types_DeleteAgentEngineSandboxConfig_DeleteAgentEngineSandboxConfig)

### vertexai._genai.types.DeleteAgentEngineSandboxOperation
    
    
    DeleteAgentEngineSandboxOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteAgentEngineSandboxOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteAgentEngineSandboxOperation#vertexai__genai_types_DeleteAgentEngineSandboxOperation_DeleteAgentEngineSandboxOperation)

### vertexai._genai.types.DeleteAgentEngineSessionConfig
    
    
    DeleteAgentEngineSessionConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteAgentEngineSessionConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteAgentEngineSessionConfig#vertexai__genai_types_DeleteAgentEngineSessionConfig_DeleteAgentEngineSessionConfig)

### vertexai._genai.types.DeleteAgentEngineSessionOperation
    
    
    DeleteAgentEngineSessionOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteAgentEngineSessionOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteAgentEngineSessionOperation#vertexai__genai_types_DeleteAgentEngineSessionOperation_DeleteAgentEngineSessionOperation)

### vertexai._genai.types.DeleteAgentEngineTaskConfig
    
    
    DeleteAgentEngineTaskConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteAgentEngineTaskConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteAgentEngineTaskConfig#vertexai__genai_types_DeleteAgentEngineTaskConfig_DeleteAgentEngineTaskConfig)

### vertexai._genai.types.DeleteEvaluationExperimentConfig
    
    
    DeleteEvaluationExperimentConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteEvaluationExperimentConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteEvaluationExperimentConfig#vertexai__genai_types_DeleteEvaluationExperimentConfig_DeleteEvaluationExperimentConfig)

### vertexai._genai.types.DeleteEvaluationExperimentOperation
    
    
    DeleteEvaluationExperimentOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteEvaluationExperimentOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteEvaluationExperimentOperation#vertexai__genai_types_DeleteEvaluationExperimentOperation_DeleteEvaluationExperimentOperation)

### vertexai._genai.types.DeleteEvaluationMetricConfig
    
    
    DeleteEvaluationMetricConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteEvaluationMetricConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteEvaluationMetricConfig#vertexai__genai_types_DeleteEvaluationMetricConfig_DeleteEvaluationMetricConfig)

### vertexai._genai.types.DeleteEvaluationMetricOperation
    
    
    DeleteEvaluationMetricOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteEvaluationMetricOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteEvaluationMetricOperation#vertexai__genai_types_DeleteEvaluationMetricOperation_DeleteEvaluationMetricOperation)

### vertexai._genai.types.DeletePromptConfig
    
    
    DeletePromptConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeletePromptConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeletePromptConfig#vertexai__genai_types_DeletePromptConfig_DeletePromptConfig)

### vertexai._genai.types.DeletePromptOperation
    
    
    DeletePromptOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeletePromptOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeletePromptOperation#vertexai__genai_types_DeletePromptOperation_DeletePromptOperation)

### vertexai._genai.types.DeletePromptVersionOperation
    
    
    DeletePromptVersionOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeletePromptVersionOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeletePromptVersionOperation#vertexai__genai_types_DeletePromptVersionOperation_DeletePromptVersionOperation)

### vertexai._genai.types.DeleteSandboxEnvironmentSnapshotConfig
    
    
    DeleteSandboxEnvironmentSnapshotConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteSandboxEnvironmentSnapshotConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteSandboxEnvironmentSnapshotConfig#vertexai__genai_types_DeleteSandboxEnvironmentSnapshotConfig_DeleteSandboxEnvironmentSnapshotConfig)

### vertexai._genai.types.DeleteSandboxEnvironmentSnapshotOperation
    
    
    DeleteSandboxEnvironmentSnapshotOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteSandboxEnvironmentSnapshotOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteSandboxEnvironmentSnapshotOperation#vertexai__genai_types_DeleteSandboxEnvironmentSnapshotOperation_DeleteSandboxEnvironmentSnapshotOperation)

### vertexai._genai.types.DeleteSandboxEnvironmentTemplateConfig
    
    
    DeleteSandboxEnvironmentTemplateConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteSandboxEnvironmentTemplateConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteSandboxEnvironmentTemplateConfig#vertexai__genai_types_DeleteSandboxEnvironmentTemplateConfig_DeleteSandboxEnvironmentTemplateConfig)

### vertexai._genai.types.DeleteSandboxEnvironmentTemplateOperation
    
    
    DeleteSandboxEnvironmentTemplateOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteSandboxEnvironmentTemplateOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteSandboxEnvironmentTemplateOperation#vertexai__genai_types_DeleteSandboxEnvironmentTemplateOperation_DeleteSandboxEnvironmentTemplateOperation)

### vertexai._genai.types.DeleteSkillConfig
    
    
    DeleteSkillConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteSkillConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteSkillConfig#vertexai__genai_types_DeleteSkillConfig_DeleteSkillConfig)

### vertexai._genai.types.DeleteSkillOperation
    
    
    DeleteSkillOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DeleteSkillOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DeleteSkillOperation#vertexai__genai_types_DeleteSkillOperation_DeleteSkillOperation)

### vertexai._genai.types.DiskSpec
    
    
    DiskSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DiskSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DiskSpec#vertexai__genai_types_DiskSpec_DiskSpec)

### vertexai._genai.types.DnsPeeringConfig
    
    
    DnsPeeringConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.DnsPeeringConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.DnsPeeringConfig#vertexai__genai_types_DnsPeeringConfig_DnsPeeringConfig)

### vertexai._genai.types.EnvVar
    
    
    EnvVar(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EnvVar](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EnvVar#vertexai__genai_types_EnvVar_EnvVar)

### vertexai._genai.types.EvalCase
    
    
    EvalCase(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvalCase](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvalCase#vertexai__genai_types_EvalCase_EvalCase)

### vertexai._genai.types.EvalCaseMetricResult
    
    
    EvalCaseMetricResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvalCaseMetricResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvalCaseMetricResult#vertexai__genai_types_EvalCaseMetricResult_EvalCaseMetricResult)

### vertexai._genai.types.EvalCaseResult
    
    
    EvalCaseResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvalCaseResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvalCaseResult#vertexai__genai_types_EvalCaseResult_EvalCaseResult)

### vertexai._genai.types.EvalRunInferenceConfig
    
    
    EvalRunInferenceConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvalRunInferenceConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvalRunInferenceConfig#vertexai__genai_types_EvalRunInferenceConfig_EvalRunInferenceConfig)

### vertexai._genai.types.EvaluateDatasetConfig
    
    
    EvaluateDatasetConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluateDatasetConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluateDatasetConfig#vertexai__genai_types_EvaluateDatasetConfig_EvaluateDatasetConfig)

### vertexai._genai.types.EvaluateDatasetRequestParameters
    
    
    EvaluateDatasetRequestParameters(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluateDatasetRequestParameters](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluateDatasetRequestParameters#vertexai__genai_types_EvaluateDatasetRequestParameters_EvaluateDatasetRequestParameters)

### vertexai._genai.types.EvaluateInstancesConfig
    
    
    EvaluateInstancesConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluateInstancesConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluateInstancesConfig#vertexai__genai_types_EvaluateInstancesConfig_EvaluateInstancesConfig)

### vertexai._genai.types.EvaluateInstancesResponse
    
    
    EvaluateInstancesResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluateInstancesResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluateInstancesResponse#vertexai__genai_types_EvaluateInstancesResponse_EvaluateInstancesResponse)

### vertexai._genai.types.EvaluateMethodConfig
    
    
    EvaluateMethodConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluateMethodConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluateMethodConfig#vertexai__genai_types_EvaluateMethodConfig_EvaluateMethodConfig)

### vertexai._genai.types.EvaluationDataset
    
    
    EvaluationDataset(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluationDataset](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationDataset#vertexai__genai_types_EvaluationDataset_EvaluationDataset)

### vertexai._genai.types.EvaluationDataset.load_from_adk_eval_set
    
    
    load_from_adk_eval_set(
        eval_set: typing.Union[str, os.PathLike[str], dict[str, typing.Any]],
    ) -> vertexai._genai.types.common.EvaluationDataset

Loads an ADK eval set (`.evalset.json`) into an EvaluationDataset.

See more: [vertexai._genai.types.EvaluationDataset.load_from_adk_eval_set](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationDataset#vertexai__genai_types_EvaluationDataset_load_from_adk_eval_set)

### vertexai._genai.types.EvaluationDataset.load_from_observability_eval_cases
    
    
    load_from_observability_eval_cases(
        cases: list["ObservabilityEvalCase"],
    ) -> vertexai._genai.types.common.EvaluationDataset

Fetches GenAI Observability data from GCS and parses into a DataFrame.

See more: [vertexai._genai.types.EvaluationDataset.load_from_observability_eval_cases](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationDataset#vertexai__genai_types_EvaluationDataset_load_from_observability_eval_cases)

### vertexai._genai.types.EvaluationDataset.show
    
    
    show() -> None

Shows the evaluation dataset.

See more: [vertexai._genai.types.EvaluationDataset.show](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationDataset#vertexai__genai_types_EvaluationDataset_show)

### vertexai._genai.types.EvaluationExperiment
    
    
    EvaluationExperiment(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluationExperiment](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationExperiment#vertexai__genai_types_EvaluationExperiment_EvaluationExperiment)

### vertexai._genai.types.EvaluationInstance
    
    
    EvaluationInstance(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluationInstance](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationInstance#vertexai__genai_types_EvaluationInstance_EvaluationInstance)

### vertexai._genai.types.EvaluationItem
    
    
    EvaluationItem(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluationItem](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationItem#vertexai__genai_types_EvaluationItem_EvaluationItem)

### vertexai._genai.types.EvaluationItemRequest
    
    
    EvaluationItemRequest(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluationItemRequest](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationItemRequest#vertexai__genai_types_EvaluationItemRequest_EvaluationItemRequest)

### vertexai._genai.types.EvaluationItemResult
    
    
    EvaluationItemResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluationItemResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationItemResult#vertexai__genai_types_EvaluationItemResult_EvaluationItemResult)

### vertexai._genai.types.EvaluationMetric
    
    
    EvaluationMetric(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluationMetric](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationMetric#vertexai__genai_types_EvaluationMetric_EvaluationMetric)

### vertexai._genai.types.EvaluationPrompt
    
    
    EvaluationPrompt(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluationPrompt](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationPrompt#vertexai__genai_types_EvaluationPrompt_EvaluationPrompt)

### vertexai._genai.types.EvaluationResult
    
    
    EvaluationResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluationResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationResult#vertexai__genai_types_EvaluationResult_EvaluationResult)

### vertexai._genai.types.EvaluationResult.show
    
    
    show(candidate_names: typing.Optional[typing.List[str]] = None) -> None

Shows the evaluation result.

See more: [vertexai._genai.types.EvaluationResult.show](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationResult#vertexai__genai_types_EvaluationResult_show)

### vertexai._genai.types.EvaluationRun
    
    
    EvaluationRun(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluationRun](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationRun#vertexai__genai_types_EvaluationRun_EvaluationRun)

### vertexai._genai.types.EvaluationRun.show
    
    
    show() -> None

Shows the evaluation result.

See more: [vertexai._genai.types.EvaluationRun.show](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationRun#vertexai__genai_types_EvaluationRun_show)

### vertexai._genai.types.EvaluationRunAgentConfig
    
    
    EvaluationRunAgentConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluationRunAgentConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationRunAgentConfig#vertexai__genai_types_EvaluationRunAgentConfig_EvaluationRunAgentConfig)

### vertexai._genai.types.EvaluationRunConfig
    
    
    EvaluationRunConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluationRunConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationRunConfig#vertexai__genai_types_EvaluationRunConfig_EvaluationRunConfig)

### vertexai._genai.types.EvaluationRunDataSource
    
    
    EvaluationRunDataSource(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluationRunDataSource](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationRunDataSource#vertexai__genai_types_EvaluationRunDataSource_EvaluationRunDataSource)

### vertexai._genai.types.EvaluationRunInferenceConfig
    
    
    EvaluationRunInferenceConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluationRunInferenceConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationRunInferenceConfig#vertexai__genai_types_EvaluationRunInferenceConfig_EvaluationRunInferenceConfig)

### vertexai._genai.types.EvaluationRunMetadata
    
    
    EvaluationRunMetadata(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluationRunMetadata](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationRunMetadata#vertexai__genai_types_EvaluationRunMetadata_EvaluationRunMetadata)

### vertexai._genai.types.EvaluationRunMetric
    
    
    EvaluationRunMetric(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluationRunMetric](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationRunMetric#vertexai__genai_types_EvaluationRunMetric_EvaluationRunMetric)

### vertexai._genai.types.EvaluationRunPromptTemplate
    
    
    EvaluationRunPromptTemplate(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluationRunPromptTemplate](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationRunPromptTemplate#vertexai__genai_types_EvaluationRunPromptTemplate_EvaluationRunPromptTemplate)

### vertexai._genai.types.EvaluationRunResults
    
    
    EvaluationRunResults(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluationRunResults](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationRunResults#vertexai__genai_types_EvaluationRunResults_EvaluationRunResults)

### vertexai._genai.types.EvaluationSet
    
    
    EvaluationSet(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EvaluationSet](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EvaluationSet#vertexai__genai_types_EvaluationSet_EvaluationSet)

### vertexai._genai.types.Event
    
    
    Event(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.Event](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.Event#vertexai__genai_types_Event_Event)

### vertexai._genai.types.EventActions
    
    
    EventActions(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EventActions](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EventActions#vertexai__genai_types_EventActions_EventActions)

### vertexai._genai.types.EventMetadata
    
    
    EventMetadata(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.EventMetadata](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.EventMetadata#vertexai__genai_types_EventMetadata_EventMetadata)

### vertexai._genai.types.ExactMatchInstance
    
    
    ExactMatchInstance(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ExactMatchInstance](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ExactMatchInstance#vertexai__genai_types_ExactMatchInstance_ExactMatchInstance)

### vertexai._genai.types.ExactMatchResults
    
    
    ExactMatchResults(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ExactMatchResults](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ExactMatchResults#vertexai__genai_types_ExactMatchResults_ExactMatchResults)

### vertexai._genai.types.ExactMatchSpec
    
    
    ExactMatchSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ExactMatchSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ExactMatchSpec#vertexai__genai_types_ExactMatchSpec_ExactMatchSpec)

### vertexai._genai.types.ExecuteCodeAgentEngineSandboxConfig
    
    
    ExecuteCodeAgentEngineSandboxConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ExecuteCodeAgentEngineSandboxConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ExecuteCodeAgentEngineSandboxConfig#vertexai__genai_types_ExecuteCodeAgentEngineSandboxConfig_ExecuteCodeAgentEngineSandboxConfig)

### vertexai._genai.types.ExecuteSandboxEnvironmentResponse
    
    
    ExecuteSandboxEnvironmentResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ExecuteSandboxEnvironmentResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ExecuteSandboxEnvironmentResponse#vertexai__genai_types_ExecuteSandboxEnvironmentResponse_ExecuteSandboxEnvironmentResponse)

### vertexai._genai.types.FailedRubric
    
    
    FailedRubric(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.FailedRubric](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.FailedRubric#vertexai__genai_types_FailedRubric_FailedRubric)

### vertexai._genai.types.GeminiExample
    
    
    GeminiExample(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GeminiExample](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GeminiExample#vertexai__genai_types_GeminiExample_GeminiExample)

### vertexai._genai.types.GeminiRequestReadConfig
    
    
    GeminiRequestReadConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GeminiRequestReadConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GeminiRequestReadConfig#vertexai__genai_types_GeminiRequestReadConfig_GeminiRequestReadConfig)

### vertexai._genai.types.GeminiRequestReadConfig.single_turn_template
    
    
    single_turn_template(
        *,
        prompt: str,
        response: typing.Optional[str] = None,
        system_instruction: typing.Optional[str] = None,
        model: typing.Optional[str] = None,
        cached_content: typing.Optional[str] = None,
        tools: typing.Optional[
            list[typing.Union[google.genai.types.Tool, dict[str, typing.Any]]]
        ] = None,
        tool_config: typing.Optional[
            typing.Union[google.genai.types.ToolConfig, dict[str, typing.Any]]
        ] = None,
        safety_settings: typing.Optional[
            list[typing.Union[google.genai.types.SafetySetting, dict[str, typing.Any]]]
        ] = None,
        generation_config: typing.Optional[
            typing.Union[google.genai.types.GenerationConfig, dict[str, typing.Any]]
        ] = None,
        field_mapping: typing.Optional[dict[str, str]] = None
    ) -> vertexai._genai.types.common.GeminiRequestReadConfig

Constructs a GeminiRequestReadConfig object for single-turn cases.

See more: [vertexai._genai.types.GeminiRequestReadConfig.single_turn_template](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GeminiRequestReadConfig#vertexai__genai_types_GeminiRequestReadConfig_single_turn_template)

### vertexai._genai.types.GeminiTemplateConfig
    
    
    GeminiTemplateConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GeminiTemplateConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GeminiTemplateConfig#vertexai__genai_types_GeminiTemplateConfig_GeminiTemplateConfig)

### vertexai._genai.types.GenerateAgentEngineMemoriesConfig
    
    
    GenerateAgentEngineMemoriesConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GenerateAgentEngineMemoriesConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GenerateAgentEngineMemoriesConfig#vertexai__genai_types_GenerateAgentEngineMemoriesConfig_GenerateAgentEngineMemoriesConfig)

### vertexai._genai.types.GenerateInstanceRubricsResponse
    
    
    GenerateInstanceRubricsResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GenerateInstanceRubricsResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GenerateInstanceRubricsResponse#vertexai__genai_types_GenerateInstanceRubricsResponse_GenerateInstanceRubricsResponse)

### vertexai._genai.types.GenerateLossClustersConfig
    
    
    GenerateLossClustersConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GenerateLossClustersConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GenerateLossClustersConfig#vertexai__genai_types_GenerateLossClustersConfig_GenerateLossClustersConfig)

### vertexai._genai.types.GenerateLossClustersOperation
    
    
    GenerateLossClustersOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GenerateLossClustersOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GenerateLossClustersOperation#vertexai__genai_types_GenerateLossClustersOperation_GenerateLossClustersOperation)

### vertexai._genai.types.GenerateLossClustersResponse
    
    
    GenerateLossClustersResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GenerateLossClustersResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GenerateLossClustersResponse#vertexai__genai_types_GenerateLossClustersResponse_GenerateLossClustersResponse)

### vertexai._genai.types.GenerateLossClustersResponse.show
    
    
    show() -> None

Shows the loss pattern analysis report with rich HTML visualization.

See more: [vertexai._genai.types.GenerateLossClustersResponse.show](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GenerateLossClustersResponse#vertexai__genai_types_GenerateLossClustersResponse_show)

### vertexai._genai.types.GenerateMemoriesRequestDirectContentsSource
    
    
    GenerateMemoriesRequestDirectContentsSource(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GenerateMemoriesRequestDirectContentsSource](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GenerateMemoriesRequestDirectContentsSource#vertexai__genai_types_GenerateMemoriesRequestDirectContentsSource_GenerateMemoriesRequestDirectContentsSource)

### vertexai._genai.types.GenerateMemoriesRequestDirectMemoriesSource
    
    
    GenerateMemoriesRequestDirectMemoriesSource(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GenerateMemoriesRequestDirectMemoriesSource](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GenerateMemoriesRequestDirectMemoriesSource#vertexai__genai_types_GenerateMemoriesRequestDirectMemoriesSource_GenerateMemoriesRequestDirectMemoriesSource)

### vertexai._genai.types.GenerateMemoriesRequestDirectMemoriesSourceDirectMemory
    
    
    GenerateMemoriesRequestDirectMemoriesSourceDirectMemory(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GenerateMemoriesRequestDirectMemoriesSourceDirectMemory](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GenerateMemoriesRequestDirectMemoriesSourceDirectMemory#vertexai__genai_types_GenerateMemoriesRequestDirectMemoriesSourceDirectMemory_GenerateMemoriesRequestDirectMemoriesSourceDirectMemory)

### vertexai._genai.types.GenerateMemoriesRequestVertexSessionSource
    
    
    GenerateMemoriesRequestVertexSessionSource(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GenerateMemoriesRequestVertexSessionSource](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GenerateMemoriesRequestVertexSessionSource#vertexai__genai_types_GenerateMemoriesRequestVertexSessionSource_GenerateMemoriesRequestVertexSessionSource)

### vertexai._genai.types.GenerateMemoriesResponse
    
    
    GenerateMemoriesResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GenerateMemoriesResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GenerateMemoriesResponse#vertexai__genai_types_GenerateMemoriesResponse_GenerateMemoriesResponse)

### vertexai._genai.types.GenerateMemoriesResponseGeneratedMemory
    
    
    GenerateMemoriesResponseGeneratedMemory(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GenerateMemoriesResponseGeneratedMemory](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GenerateMemoriesResponseGeneratedMemory#vertexai__genai_types_GenerateMemoriesResponseGeneratedMemory_GenerateMemoriesResponseGeneratedMemory)

### vertexai._genai.types.GenerateUserScenariosResponse
    
    
    GenerateUserScenariosResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GenerateUserScenariosResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GenerateUserScenariosResponse#vertexai__genai_types_GenerateUserScenariosResponse_GenerateUserScenariosResponse)

### vertexai._genai.types.GetAgentEngineConfig
    
    
    GetAgentEngineConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GetAgentEngineConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GetAgentEngineConfig#vertexai__genai_types_GetAgentEngineConfig_GetAgentEngineConfig)

### vertexai._genai.types.GetAgentEngineMemoryConfig
    
    
    GetAgentEngineMemoryConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GetAgentEngineMemoryConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GetAgentEngineMemoryConfig#vertexai__genai_types_GetAgentEngineMemoryConfig_GetAgentEngineMemoryConfig)

### vertexai._genai.types.GetAgentEngineMemoryRevisionConfig
    
    
    GetAgentEngineMemoryRevisionConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GetAgentEngineMemoryRevisionConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GetAgentEngineMemoryRevisionConfig#vertexai__genai_types_GetAgentEngineMemoryRevisionConfig_GetAgentEngineMemoryRevisionConfig)

### vertexai._genai.types.GetAgentEngineRuntimeRevisionConfig
    
    
    GetAgentEngineRuntimeRevisionConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GetAgentEngineRuntimeRevisionConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GetAgentEngineRuntimeRevisionConfig#vertexai__genai_types_GetAgentEngineRuntimeRevisionConfig_GetAgentEngineRuntimeRevisionConfig)

### vertexai._genai.types.GetAgentEngineSandboxConfig
    
    
    GetAgentEngineSandboxConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GetAgentEngineSandboxConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GetAgentEngineSandboxConfig#vertexai__genai_types_GetAgentEngineSandboxConfig_GetAgentEngineSandboxConfig)

### vertexai._genai.types.GetAgentEngineSessionConfig
    
    
    GetAgentEngineSessionConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GetAgentEngineSessionConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GetAgentEngineSessionConfig#vertexai__genai_types_GetAgentEngineSessionConfig_GetAgentEngineSessionConfig)

### vertexai._genai.types.GetAgentEngineTaskConfig
    
    
    GetAgentEngineTaskConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GetAgentEngineTaskConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GetAgentEngineTaskConfig#vertexai__genai_types_GetAgentEngineTaskConfig_GetAgentEngineTaskConfig)

### vertexai._genai.types.GetDatasetOperationConfig
    
    
    GetDatasetOperationConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GetDatasetOperationConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GetDatasetOperationConfig#vertexai__genai_types_GetDatasetOperationConfig_GetDatasetOperationConfig)

### vertexai._genai.types.GetEvaluationExperimentConfig
    
    
    GetEvaluationExperimentConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GetEvaluationExperimentConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GetEvaluationExperimentConfig#vertexai__genai_types_GetEvaluationExperimentConfig_GetEvaluationExperimentConfig)

### vertexai._genai.types.GetEvaluationItemConfig
    
    
    GetEvaluationItemConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GetEvaluationItemConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GetEvaluationItemConfig#vertexai__genai_types_GetEvaluationItemConfig_GetEvaluationItemConfig)

### vertexai._genai.types.GetEvaluationMetricConfig
    
    
    GetEvaluationMetricConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GetEvaluationMetricConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GetEvaluationMetricConfig#vertexai__genai_types_GetEvaluationMetricConfig_GetEvaluationMetricConfig)

### vertexai._genai.types.GetEvaluationRunConfig
    
    
    GetEvaluationRunConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GetEvaluationRunConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GetEvaluationRunConfig#vertexai__genai_types_GetEvaluationRunConfig_GetEvaluationRunConfig)

### vertexai._genai.types.GetEvaluationSetConfig
    
    
    GetEvaluationSetConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GetEvaluationSetConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GetEvaluationSetConfig#vertexai__genai_types_GetEvaluationSetConfig_GetEvaluationSetConfig)

### vertexai._genai.types.GetMultimodalDatasetOperationConfig
    
    
    GetMultimodalDatasetOperationConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GetMultimodalDatasetOperationConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GetMultimodalDatasetOperationConfig#vertexai__genai_types_GetMultimodalDatasetOperationConfig_GetMultimodalDatasetOperationConfig)

### vertexai._genai.types.GetPromptConfig
    
    
    GetPromptConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GetPromptConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GetPromptConfig#vertexai__genai_types_GetPromptConfig_GetPromptConfig)

### vertexai._genai.types.GetSandboxEnvironmentSnapshotConfig
    
    
    GetSandboxEnvironmentSnapshotConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GetSandboxEnvironmentSnapshotConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GetSandboxEnvironmentSnapshotConfig#vertexai__genai_types_GetSandboxEnvironmentSnapshotConfig_GetSandboxEnvironmentSnapshotConfig)

### vertexai._genai.types.GetSandboxEnvironmentTemplateConfig
    
    
    GetSandboxEnvironmentTemplateConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GetSandboxEnvironmentTemplateConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GetSandboxEnvironmentTemplateConfig#vertexai__genai_types_GetSandboxEnvironmentTemplateConfig_GetSandboxEnvironmentTemplateConfig)

### vertexai._genai.types.GetSkillConfig
    
    
    GetSkillConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.GetSkillConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.GetSkillConfig#vertexai__genai_types_GetSkillConfig_GetSkillConfig)

### vertexai._genai.types.IngestEventsConfig
    
    
    IngestEventsConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.IngestEventsConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.IngestEventsConfig#vertexai__genai_types_IngestEventsConfig_IngestEventsConfig)

### vertexai._genai.types.IngestionDirectContentsSource
    
    
    IngestionDirectContentsSource(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.IngestionDirectContentsSource](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.IngestionDirectContentsSource#vertexai__genai_types_IngestionDirectContentsSource_IngestionDirectContentsSource)

### vertexai._genai.types.IngestionDirectContentsSourceEvent
    
    
    IngestionDirectContentsSourceEvent(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.IngestionDirectContentsSourceEvent](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.IngestionDirectContentsSourceEvent#vertexai__genai_types_IngestionDirectContentsSourceEvent_IngestionDirectContentsSourceEvent)

### vertexai._genai.types.IntermediateExtractedMemory
    
    
    IntermediateExtractedMemory(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.IntermediateExtractedMemory](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.IntermediateExtractedMemory#vertexai__genai_types_IntermediateExtractedMemory_IntermediateExtractedMemory)

### vertexai._genai.types.KeepAliveProbe
    
    
    KeepAliveProbe(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.KeepAliveProbe](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.KeepAliveProbe#vertexai__genai_types_KeepAliveProbe_KeepAliveProbe)

### vertexai._genai.types.KeepAliveProbeHttpGet
    
    
    KeepAliveProbeHttpGet(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.KeepAliveProbeHttpGet](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.KeepAliveProbeHttpGet#vertexai__genai_types_KeepAliveProbeHttpGet_KeepAliveProbeHttpGet)

### vertexai._genai.types.LLMMetric
    
    
    LLMMetric(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.LLMMetric](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.LLMMetric#vertexai__genai_types_LLMMetric_LLMMetric)

### vertexai._genai.types.LLMMetric.load
    
    
    load(
        config_path: str, client: typing.Optional[typing.Any] = None
    ) -> vertexai._genai.types.common.LLMMetric

Loads a metric configuration from a YAML or JSON file.

See more: [vertexai._genai.types.LLMMetric.load](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.LLMMetric#vertexai__genai_types_LLMMetric_load)

### vertexai._genai.types.LLMMetric.model_post_init
    
    
    model_post_init(context: Any, /) -> None

This function is meant to behave like a BaseModel method to initialize private attributes.

See more: [vertexai._genai.types.LLMMetric.model_post_init](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.LLMMetric#vertexai__genai_types_LLMMetric_model_post_init)

### vertexai._genai.types.LLMMetric.validate_judge_model_sampling_count
    
    
    validate_judge_model_sampling_count(
        value: typing.Optional[int],
    ) -> typing.Optional[int]

Validates judge_model_sampling_count to be between 1 and 32.

See more: [vertexai._genai.types.LLMMetric.validate_judge_model_sampling_count](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.LLMMetric#vertexai__genai_types_LLMMetric_validate_judge_model_sampling_count)

### vertexai._genai.types.LLMMetric.validate_prompt_template
    
    
    validate_prompt_template(
        value: typing.Union[str, vertexai._genai.types.common.MetricPromptBuilder],
    ) -> str

Validates prompt template to be a non-empty string.

See more: [vertexai._genai.types.LLMMetric.validate_prompt_template](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.LLMMetric#vertexai__genai_types_LLMMetric_validate_prompt_template)

### vertexai._genai.types.ListAgentEngineConfig
    
    
    ListAgentEngineConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListAgentEngineConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListAgentEngineConfig#vertexai__genai_types_ListAgentEngineConfig_ListAgentEngineConfig)

### vertexai._genai.types.ListAgentEngineMemoryConfig
    
    
    ListAgentEngineMemoryConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListAgentEngineMemoryConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListAgentEngineMemoryConfig#vertexai__genai_types_ListAgentEngineMemoryConfig_ListAgentEngineMemoryConfig)

### vertexai._genai.types.ListAgentEngineMemoryRevisionsConfig
    
    
    ListAgentEngineMemoryRevisionsConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListAgentEngineMemoryRevisionsConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListAgentEngineMemoryRevisionsConfig#vertexai__genai_types_ListAgentEngineMemoryRevisionsConfig_ListAgentEngineMemoryRevisionsConfig)

### vertexai._genai.types.ListAgentEngineMemoryRevisionsResponse
    
    
    ListAgentEngineMemoryRevisionsResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListAgentEngineMemoryRevisionsResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListAgentEngineMemoryRevisionsResponse#vertexai__genai_types_ListAgentEngineMemoryRevisionsResponse_ListAgentEngineMemoryRevisionsResponse)

### vertexai._genai.types.ListAgentEngineRuntimeRevisionsConfig
    
    
    ListAgentEngineRuntimeRevisionsConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListAgentEngineRuntimeRevisionsConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListAgentEngineRuntimeRevisionsConfig#vertexai__genai_types_ListAgentEngineRuntimeRevisionsConfig_ListAgentEngineRuntimeRevisionsConfig)

### vertexai._genai.types.ListAgentEngineSandboxesConfig
    
    
    ListAgentEngineSandboxesConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListAgentEngineSandboxesConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListAgentEngineSandboxesConfig#vertexai__genai_types_ListAgentEngineSandboxesConfig_ListAgentEngineSandboxesConfig)

### vertexai._genai.types.ListAgentEngineSandboxesResponse
    
    
    ListAgentEngineSandboxesResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListAgentEngineSandboxesResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListAgentEngineSandboxesResponse#vertexai__genai_types_ListAgentEngineSandboxesResponse_ListAgentEngineSandboxesResponse)

### vertexai._genai.types.ListAgentEngineSessionEventsConfig
    
    
    ListAgentEngineSessionEventsConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListAgentEngineSessionEventsConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListAgentEngineSessionEventsConfig#vertexai__genai_types_ListAgentEngineSessionEventsConfig_ListAgentEngineSessionEventsConfig)

### vertexai._genai.types.ListAgentEngineSessionEventsResponse
    
    
    ListAgentEngineSessionEventsResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListAgentEngineSessionEventsResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListAgentEngineSessionEventsResponse#vertexai__genai_types_ListAgentEngineSessionEventsResponse_ListAgentEngineSessionEventsResponse)

### vertexai._genai.types.ListAgentEngineSessionsConfig
    
    
    ListAgentEngineSessionsConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListAgentEngineSessionsConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListAgentEngineSessionsConfig#vertexai__genai_types_ListAgentEngineSessionsConfig_ListAgentEngineSessionsConfig)

### vertexai._genai.types.ListAgentEngineTaskEventsConfig
    
    
    ListAgentEngineTaskEventsConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListAgentEngineTaskEventsConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListAgentEngineTaskEventsConfig#vertexai__genai_types_ListAgentEngineTaskEventsConfig_ListAgentEngineTaskEventsConfig)

### vertexai._genai.types.ListAgentEngineTaskEventsResponse
    
    
    ListAgentEngineTaskEventsResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListAgentEngineTaskEventsResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListAgentEngineTaskEventsResponse#vertexai__genai_types_ListAgentEngineTaskEventsResponse_ListAgentEngineTaskEventsResponse)

### vertexai._genai.types.ListAgentEngineTasksConfig
    
    
    ListAgentEngineTasksConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListAgentEngineTasksConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListAgentEngineTasksConfig#vertexai__genai_types_ListAgentEngineTasksConfig_ListAgentEngineTasksConfig)

### vertexai._genai.types.ListAgentEngineTasksResponse
    
    
    ListAgentEngineTasksResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListAgentEngineTasksResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListAgentEngineTasksResponse#vertexai__genai_types_ListAgentEngineTasksResponse_ListAgentEngineTasksResponse)

### vertexai._genai.types.ListDatasetVersionsResponse
    
    
    ListDatasetVersionsResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListDatasetVersionsResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListDatasetVersionsResponse#vertexai__genai_types_ListDatasetVersionsResponse_ListDatasetVersionsResponse)

### vertexai._genai.types.ListDatasetsResponse
    
    
    ListDatasetsResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListDatasetsResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListDatasetsResponse#vertexai__genai_types_ListDatasetsResponse_ListDatasetsResponse)

### vertexai._genai.types.ListEvaluationExperimentsConfig
    
    
    ListEvaluationExperimentsConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListEvaluationExperimentsConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListEvaluationExperimentsConfig#vertexai__genai_types_ListEvaluationExperimentsConfig_ListEvaluationExperimentsConfig)

### vertexai._genai.types.ListEvaluationExperimentsResponse
    
    
    ListEvaluationExperimentsResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListEvaluationExperimentsResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListEvaluationExperimentsResponse#vertexai__genai_types_ListEvaluationExperimentsResponse_ListEvaluationExperimentsResponse)

### vertexai._genai.types.ListEvaluationMetricsConfig
    
    
    ListEvaluationMetricsConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListEvaluationMetricsConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListEvaluationMetricsConfig#vertexai__genai_types_ListEvaluationMetricsConfig_ListEvaluationMetricsConfig)

### vertexai._genai.types.ListEvaluationMetricsResponse
    
    
    ListEvaluationMetricsResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListEvaluationMetricsResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListEvaluationMetricsResponse#vertexai__genai_types_ListEvaluationMetricsResponse_ListEvaluationMetricsResponse)

### vertexai._genai.types.ListMultimodalDatasetsConfig
    
    
    ListMultimodalDatasetsConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListMultimodalDatasetsConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListMultimodalDatasetsConfig#vertexai__genai_types_ListMultimodalDatasetsConfig_ListMultimodalDatasetsConfig)

### vertexai._genai.types.ListMultimodalDatasetsResponse
    
    
    ListMultimodalDatasetsResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListMultimodalDatasetsResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListMultimodalDatasetsResponse#vertexai__genai_types_ListMultimodalDatasetsResponse_ListMultimodalDatasetsResponse)

### vertexai._genai.types.ListPromptsConfig
    
    
    ListPromptsConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListPromptsConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListPromptsConfig#vertexai__genai_types_ListPromptsConfig_ListPromptsConfig)

### vertexai._genai.types.ListReasoningEnginesMemoriesResponse
    
    
    ListReasoningEnginesMemoriesResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListReasoningEnginesMemoriesResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListReasoningEnginesMemoriesResponse#vertexai__genai_types_ListReasoningEnginesMemoriesResponse_ListReasoningEnginesMemoriesResponse)

### vertexai._genai.types.ListReasoningEnginesResponse
    
    
    ListReasoningEnginesResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListReasoningEnginesResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListReasoningEnginesResponse#vertexai__genai_types_ListReasoningEnginesResponse_ListReasoningEnginesResponse)

### vertexai._genai.types.ListReasoningEnginesRuntimeRevisionsResponse
    
    
    ListReasoningEnginesRuntimeRevisionsResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListReasoningEnginesRuntimeRevisionsResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListReasoningEnginesRuntimeRevisionsResponse#vertexai__genai_types_ListReasoningEnginesRuntimeRevisionsResponse_ListReasoningEnginesRuntimeRevisionsResponse)

### vertexai._genai.types.ListReasoningEnginesSessionsResponse
    
    
    ListReasoningEnginesSessionsResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListReasoningEnginesSessionsResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListReasoningEnginesSessionsResponse#vertexai__genai_types_ListReasoningEnginesSessionsResponse_ListReasoningEnginesSessionsResponse)

### vertexai._genai.types.ListSandboxEnvironmentSnapshotsConfig
    
    
    ListSandboxEnvironmentSnapshotsConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListSandboxEnvironmentSnapshotsConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListSandboxEnvironmentSnapshotsConfig#vertexai__genai_types_ListSandboxEnvironmentSnapshotsConfig_ListSandboxEnvironmentSnapshotsConfig)

### vertexai._genai.types.ListSandboxEnvironmentSnapshotsResponse
    
    
    ListSandboxEnvironmentSnapshotsResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListSandboxEnvironmentSnapshotsResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListSandboxEnvironmentSnapshotsResponse#vertexai__genai_types_ListSandboxEnvironmentSnapshotsResponse_ListSandboxEnvironmentSnapshotsResponse)

### vertexai._genai.types.ListSandboxEnvironmentTemplatesConfig
    
    
    ListSandboxEnvironmentTemplatesConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListSandboxEnvironmentTemplatesConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListSandboxEnvironmentTemplatesConfig#vertexai__genai_types_ListSandboxEnvironmentTemplatesConfig_ListSandboxEnvironmentTemplatesConfig)

### vertexai._genai.types.ListSandboxEnvironmentTemplatesResponse
    
    
    ListSandboxEnvironmentTemplatesResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListSandboxEnvironmentTemplatesResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListSandboxEnvironmentTemplatesResponse#vertexai__genai_types_ListSandboxEnvironmentTemplatesResponse_ListSandboxEnvironmentTemplatesResponse)

### vertexai._genai.types.ListSkillsConfig
    
    
    ListSkillsConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListSkillsConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListSkillsConfig#vertexai__genai_types_ListSkillsConfig_ListSkillsConfig)

### vertexai._genai.types.ListSkillsResponse
    
    
    ListSkillsResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ListSkillsResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ListSkillsResponse#vertexai__genai_types_ListSkillsResponse_ListSkillsResponse)

### vertexai._genai.types.LossAnalysisConfig
    
    
    LossAnalysisConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.LossAnalysisConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.LossAnalysisConfig#vertexai__genai_types_LossAnalysisConfig_LossAnalysisConfig)

### vertexai._genai.types.LossAnalysisResult
    
    
    LossAnalysisResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.LossAnalysisResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.LossAnalysisResult#vertexai__genai_types_LossAnalysisResult_LossAnalysisResult)

### vertexai._genai.types.LossAnalysisResult.show
    
    
    show() -> None

Shows the loss analysis result with rich HTML visualization.

See more: [vertexai._genai.types.LossAnalysisResult.show](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.LossAnalysisResult#vertexai__genai_types_LossAnalysisResult_show)

### vertexai._genai.types.LossCluster
    
    
    LossCluster(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.LossCluster](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.LossCluster#vertexai__genai_types_LossCluster_LossCluster)

### vertexai._genai.types.LossExample
    
    
    LossExample(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.LossExample](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.LossExample#vertexai__genai_types_LossExample_LossExample)

### vertexai._genai.types.LossTaxonomyEntry
    
    
    LossTaxonomyEntry(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.LossTaxonomyEntry](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.LossTaxonomyEntry#vertexai__genai_types_LossTaxonomyEntry_LossTaxonomyEntry)

### vertexai._genai.types.LustreMount
    
    
    LustreMount(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.LustreMount](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.LustreMount#vertexai__genai_types_LustreMount_LustreMount)

### vertexai._genai.types.MachineSpec
    
    
    MachineSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MachineSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MachineSpec#vertexai__genai_types_MachineSpec_MachineSpec)

### vertexai._genai.types.MapInstance
    
    
    MapInstance(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MapInstance](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MapInstance#vertexai__genai_types_MapInstance_MapInstance)

### vertexai._genai.types.Memory
    
    
    Memory(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.Memory](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.Memory#vertexai__genai_types_Memory_Memory)

### vertexai._genai.types.MemoryBankCustomizationConfig
    
    
    MemoryBankCustomizationConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MemoryBankCustomizationConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MemoryBankCustomizationConfig#vertexai__genai_types_MemoryBankCustomizationConfig_MemoryBankCustomizationConfig)

### vertexai._genai.types.MemoryBankCustomizationConfigConsolidationConfig
    
    
    MemoryBankCustomizationConfigConsolidationConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MemoryBankCustomizationConfigConsolidationConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MemoryBankCustomizationConfigConsolidationConfig#vertexai__genai_types_MemoryBankCustomizationConfigConsolidationConfig_MemoryBankCustomizationConfigConsolidationConfig)

### vertexai._genai.types.MemoryBankCustomizationConfigGenerateMemoriesExample
    
    
    MemoryBankCustomizationConfigGenerateMemoriesExample(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MemoryBankCustomizationConfigGenerateMemoriesExample](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MemoryBankCustomizationConfigGenerateMemoriesExample#vertexai__genai_types_MemoryBankCustomizationConfigGenerateMemoriesExample_MemoryBankCustomizationConfigGenerateMemoriesExample)

### vertexai._genai.types.MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSource
    
    
    MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSource(
        **data: typing.Any,
    )

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSource](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSource#vertexai__genai_types_MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSource_MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSource)

### vertexai._genai.types.MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSourceEvent
    
    
    MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSourceEvent(
        **data: typing.Any,
    )

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSourceEvent](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSourceEvent#vertexai__genai_types_MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSourceEvent_MemoryBankCustomizationConfigGenerateMemoriesExampleConversationSourceEvent)

### vertexai._genai.types.MemoryBankCustomizationConfigGenerateMemoriesExampleGeneratedMemory
    
    
    MemoryBankCustomizationConfigGenerateMemoriesExampleGeneratedMemory(
        **data: typing.Any,
    )

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MemoryBankCustomizationConfigGenerateMemoriesExampleGeneratedMemory](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MemoryBankCustomizationConfigGenerateMemoriesExampleGeneratedMemory#vertexai__genai_types_MemoryBankCustomizationConfigGenerateMemoriesExampleGeneratedMemory_MemoryBankCustomizationConfigGenerateMemoriesExampleGeneratedMemory)

### vertexai._genai.types.MemoryBankCustomizationConfigMemoryTopic
    
    
    MemoryBankCustomizationConfigMemoryTopic(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MemoryBankCustomizationConfigMemoryTopic](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MemoryBankCustomizationConfigMemoryTopic#vertexai__genai_types_MemoryBankCustomizationConfigMemoryTopic_MemoryBankCustomizationConfigMemoryTopic)

### vertexai._genai.types.MemoryBankCustomizationConfigMemoryTopicCustomMemoryTopic
    
    
    MemoryBankCustomizationConfigMemoryTopicCustomMemoryTopic(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MemoryBankCustomizationConfigMemoryTopicCustomMemoryTopic](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MemoryBankCustomizationConfigMemoryTopicCustomMemoryTopic#vertexai__genai_types_MemoryBankCustomizationConfigMemoryTopicCustomMemoryTopic_MemoryBankCustomizationConfigMemoryTopicCustomMemoryTopic)

### vertexai._genai.types.MemoryBankCustomizationConfigMemoryTopicManagedMemoryTopic
    
    
    MemoryBankCustomizationConfigMemoryTopicManagedMemoryTopic(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MemoryBankCustomizationConfigMemoryTopicManagedMemoryTopic](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MemoryBankCustomizationConfigMemoryTopicManagedMemoryTopic#vertexai__genai_types_MemoryBankCustomizationConfigMemoryTopicManagedMemoryTopic_MemoryBankCustomizationConfigMemoryTopicManagedMemoryTopic)

### vertexai._genai.types.MemoryBankIngestEventsOperation
    
    
    MemoryBankIngestEventsOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MemoryBankIngestEventsOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MemoryBankIngestEventsOperation#vertexai__genai_types_MemoryBankIngestEventsOperation_MemoryBankIngestEventsOperation)

### vertexai._genai.types.MemoryConjunctionFilter
    
    
    MemoryConjunctionFilter(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MemoryConjunctionFilter](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MemoryConjunctionFilter#vertexai__genai_types_MemoryConjunctionFilter_MemoryConjunctionFilter)

### vertexai._genai.types.MemoryFilter
    
    
    MemoryFilter(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MemoryFilter](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MemoryFilter#vertexai__genai_types_MemoryFilter_MemoryFilter)

### vertexai._genai.types.MemoryGenerationTriggerConfig
    
    
    MemoryGenerationTriggerConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MemoryGenerationTriggerConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MemoryGenerationTriggerConfig#vertexai__genai_types_MemoryGenerationTriggerConfig_MemoryGenerationTriggerConfig)

### vertexai._genai.types.MemoryGenerationTriggerConfigGenerationTriggerRule
    
    
    MemoryGenerationTriggerConfigGenerationTriggerRule(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MemoryGenerationTriggerConfigGenerationTriggerRule](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MemoryGenerationTriggerConfigGenerationTriggerRule#vertexai__genai_types_MemoryGenerationTriggerConfigGenerationTriggerRule_MemoryGenerationTriggerConfigGenerationTriggerRule)

### vertexai._genai.types.MemoryMetadataValue
    
    
    MemoryMetadataValue(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MemoryMetadataValue](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MemoryMetadataValue#vertexai__genai_types_MemoryMetadataValue_MemoryMetadataValue)

### vertexai._genai.types.MemoryProfile
    
    
    MemoryProfile(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MemoryProfile](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MemoryProfile#vertexai__genai_types_MemoryProfile_MemoryProfile)

### vertexai._genai.types.MemoryRevision
    
    
    MemoryRevision(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MemoryRevision](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MemoryRevision#vertexai__genai_types_MemoryRevision_MemoryRevision)

### vertexai._genai.types.MemoryStructuredContent
    
    
    MemoryStructuredContent(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MemoryStructuredContent](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MemoryStructuredContent#vertexai__genai_types_MemoryStructuredContent_MemoryStructuredContent)

### vertexai._genai.types.MemoryTopicId
    
    
    MemoryTopicId(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MemoryTopicId](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MemoryTopicId#vertexai__genai_types_MemoryTopicId_MemoryTopicId)

### vertexai._genai.types.Message
    
    
    Message(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.Message](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.Message#vertexai__genai_types_Message_Message)

### vertexai._genai.types.Metadata
    
    
    Metadata(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.Metadata](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.Metadata#vertexai__genai_types_Metadata_Metadata)

### vertexai._genai.types.Metric
    
    
    Metric(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.Metric](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.Metric#vertexai__genai_types_Metric_Metric)

### vertexai._genai.types.Metric.model_post_init
    
    
    model_post_init(context: Any, /) -> None

This function is meant to behave like a BaseModel method to initialize private attributes.

See more: [vertexai._genai.types.Metric.model_post_init](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.Metric#vertexai__genai_types_Metric_model_post_init)

### vertexai._genai.types.Metric.to_yaml_file
    
    
    to_yaml_file(file_path: str, version: typing.Optional[str] = None) -> None

Dumps the metric object to a YAML file.

See more: [vertexai._genai.types.Metric.to_yaml_file](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.Metric#vertexai__genai_types_Metric_to_yaml_file)

### vertexai._genai.types.Metric.validate_name
    
    
    validate_name(
        model: vertexai._genai.types.common.Metric,
    ) -> vertexai._genai.types.common.Metric

API documentation for `validate_name` method.

See more: [vertexai._genai.types.Metric.validate_name](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.Metric#vertexai__genai_types_Metric_validate_name)

### vertexai._genai.types.MetricPromptBuilder
    
    
    MetricPromptBuilder(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MetricPromptBuilder](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MetricPromptBuilder#vertexai__genai_types_MetricPromptBuilder_MetricPromptBuilder)

### vertexai._genai.types.MetricPromptBuilder.__str__
    
    
    __str__() -> str

Returns the fully constructed prompt template text.

See more: [vertexai._genai.types.MetricPromptBuilder.__str__](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MetricPromptBuilder#vertexai__genai_types_MetricPromptBuilder___str__)

### vertexai._genai.types.MetricResult
    
    
    MetricResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MetricResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MetricResult#vertexai__genai_types_MetricResult_MetricResult)

### vertexai._genai.types.MetricSource
    
    
    MetricSource(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MetricSource](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MetricSource#vertexai__genai_types_MetricSource_MetricSource)

### vertexai._genai.types.MetricxResult
    
    
    MetricxResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MetricxResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MetricxResult#vertexai__genai_types_MetricxResult_MetricxResult)

### vertexai._genai.types.MultimodalDataset
    
    
    MultimodalDataset(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MultimodalDataset](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MultimodalDataset#vertexai__genai_types_MultimodalDataset_MultimodalDataset)

### vertexai._genai.types.MultimodalDataset.set_bigquery_uri
    
    
    set_bigquery_uri(bigquery_uri: str) -> None

Sets the bigquery uri in the dataset metadata.

See more: [vertexai._genai.types.MultimodalDataset.set_bigquery_uri](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MultimodalDataset#vertexai__genai_types_MultimodalDataset_set_bigquery_uri)

### vertexai._genai.types.MultimodalDataset.set_read_config
    
    
    set_read_config(
        *,
        read_config: typing.Union[
            vertexai._genai.types.common.GeminiRequestReadConfig,
            vertexai._genai.types.common.GeminiRequestReadConfigDict,
        ]
    ) -> None

Sets the read config in the dataset metadata.

See more: [vertexai._genai.types.MultimodalDataset.set_read_config](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MultimodalDataset#vertexai__genai_types_MultimodalDataset_set_read_config)

### vertexai._genai.types.MultimodalDataset.to_bigframes
    
    
    to_bigframes() -> bigframes.pandas.DataFrame

Converts the multimodal dataset to a BigFrames dataframe.

See more: [vertexai._genai.types.MultimodalDataset.to_bigframes](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MultimodalDataset#vertexai__genai_types_MultimodalDataset_to_bigframes)

### vertexai._genai.types.MultimodalDatasetOperation
    
    
    MultimodalDatasetOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.MultimodalDatasetOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.MultimodalDatasetOperation#vertexai__genai_types_MultimodalDatasetOperation_MultimodalDatasetOperation)

### vertexai._genai.types.NfsMount
    
    
    NfsMount(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.NfsMount](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.NfsMount#vertexai__genai_types_NfsMount_NfsMount)

### vertexai._genai.types.ObservabilityEvalCase
    
    
    ObservabilityEvalCase(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ObservabilityEvalCase](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ObservabilityEvalCase#vertexai__genai_types_ObservabilityEvalCase_ObservabilityEvalCase)

### vertexai._genai.types.OptimizeConfig
    
    
    OptimizeConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.OptimizeConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.OptimizeConfig#vertexai__genai_types_OptimizeConfig_OptimizeConfig)

### vertexai._genai.types.OptimizeJobConfig
    
    
    OptimizeJobConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.OptimizeJobConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.OptimizeJobConfig#vertexai__genai_types_OptimizeJobConfig_OptimizeJobConfig)

### vertexai._genai.types.OptimizeResponse
    
    
    OptimizeResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.OptimizeResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.OptimizeResponse#vertexai__genai_types_OptimizeResponse_OptimizeResponse)

### vertexai._genai.types.OptimizeResponseEndpoint
    
    
    OptimizeResponseEndpoint(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.OptimizeResponseEndpoint](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.OptimizeResponseEndpoint#vertexai__genai_types_OptimizeResponseEndpoint_OptimizeResponseEndpoint)

### vertexai._genai.types.PairwiseMetricInput
    
    
    PairwiseMetricInput(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.PairwiseMetricInput](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.PairwiseMetricInput#vertexai__genai_types_PairwiseMetricInput_PairwiseMetricInput)

### vertexai._genai.types.PairwiseMetricInstance
    
    
    PairwiseMetricInstance(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.PairwiseMetricInstance](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.PairwiseMetricInstance#vertexai__genai_types_PairwiseMetricInstance_PairwiseMetricInstance)

### vertexai._genai.types.PointwiseMetricInput
    
    
    PointwiseMetricInput(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.PointwiseMetricInput](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.PointwiseMetricInput#vertexai__genai_types_PointwiseMetricInput_PointwiseMetricInput)

### vertexai._genai.types.PointwiseMetricInstance
    
    
    PointwiseMetricInstance(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.PointwiseMetricInstance](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.PointwiseMetricInstance#vertexai__genai_types_PointwiseMetricInstance_PointwiseMetricInstance)

### vertexai._genai.types.Prompt
    
    
    Prompt(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.Prompt](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.Prompt#vertexai__genai_types_Prompt_Prompt)

### vertexai._genai.types.Prompt.assemble_contents
    
    
    assemble_contents() -> list[google.genai.types.Content]

Transforms a Prompt object into a list with a single genai_types.Content object.

See more: [vertexai._genai.types.Prompt.assemble_contents](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.Prompt#vertexai__genai_types_Prompt_assemble_contents)

### vertexai._genai.types.Prompt.model_post_init
    
    
    model_post_init(context: Any, /) -> None

This function is meant to behave like a BaseModel method to initialize private attributes.

See more: [vertexai._genai.types.Prompt.model_post_init](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.Prompt#vertexai__genai_types_Prompt_model_post_init)

### vertexai._genai.types.PromptOptimizerConfig
    
    
    PromptOptimizerConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.PromptOptimizerConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.PromptOptimizerConfig#vertexai__genai_types_PromptOptimizerConfig_PromptOptimizerConfig)

### vertexai._genai.types.PromptRef
    
    
    PromptRef(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.PromptRef](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.PromptRef#vertexai__genai_types_PromptRef_PromptRef)

### vertexai._genai.types.PromptTemplate
    
    
    PromptTemplate(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.PromptTemplate](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.PromptTemplate#vertexai__genai_types_PromptTemplate_PromptTemplate)

### vertexai._genai.types.PromptTemplate.assemble
    
    
    assemble(**kwargs: typing.Any) -> str

Assembles the prompt template with the given keyword arguments.

See more: [vertexai._genai.types.PromptTemplate.assemble](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.PromptTemplate#vertexai__genai_types_PromptTemplate_assemble)

### vertexai._genai.types.PromptTemplate.text_must_not_be_empty
    
    
    text_must_not_be_empty(value: str) -> str

API documentation for `text_must_not_be_empty` method.

See more: [vertexai._genai.types.PromptTemplate.text_must_not_be_empty](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.PromptTemplate#vertexai__genai_types_PromptTemplate_text_must_not_be_empty)

### vertexai._genai.types.PromptTemplateData
    
    
    PromptTemplateData(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.PromptTemplateData](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.PromptTemplateData#vertexai__genai_types_PromptTemplateData_PromptTemplateData)

### vertexai._genai.types.PromptVersionRef
    
    
    PromptVersionRef(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.PromptVersionRef](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.PromptVersionRef#vertexai__genai_types_PromptVersionRef_PromptVersionRef)

### vertexai._genai.types.PscInterfaceConfig
    
    
    PscInterfaceConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.PscInterfaceConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.PscInterfaceConfig#vertexai__genai_types_PscInterfaceConfig_PscInterfaceConfig)

### vertexai._genai.types.PurgeAgentEngineMemoriesConfig
    
    
    PurgeAgentEngineMemoriesConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.PurgeAgentEngineMemoriesConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.PurgeAgentEngineMemoriesConfig#vertexai__genai_types_PurgeAgentEngineMemoriesConfig_PurgeAgentEngineMemoriesConfig)

### vertexai._genai.types.PurgeMemoriesResponse
    
    
    PurgeMemoriesResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.PurgeMemoriesResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.PurgeMemoriesResponse#vertexai__genai_types_PurgeMemoriesResponse_PurgeMemoriesResponse)

### vertexai._genai.types.PythonPackageSpec
    
    
    PythonPackageSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.PythonPackageSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.PythonPackageSpec#vertexai__genai_types_PythonPackageSpec_PythonPackageSpec)

### vertexai._genai.types.QueryAgentEngineConfig
    
    
    QueryAgentEngineConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.QueryAgentEngineConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.QueryAgentEngineConfig#vertexai__genai_types_QueryAgentEngineConfig_QueryAgentEngineConfig)

### vertexai._genai.types.QueryAgentEngineRuntimeRevisionConfig
    
    
    QueryAgentEngineRuntimeRevisionConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.QueryAgentEngineRuntimeRevisionConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.QueryAgentEngineRuntimeRevisionConfig#vertexai__genai_types_QueryAgentEngineRuntimeRevisionConfig_QueryAgentEngineRuntimeRevisionConfig)

### vertexai._genai.types.QueryReasoningEngineResponse
    
    
    QueryReasoningEngineResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.QueryReasoningEngineResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.QueryReasoningEngineResponse#vertexai__genai_types_QueryReasoningEngineResponse_QueryReasoningEngineResponse)

### vertexai._genai.types.ReasoningEngine
    
    
    ReasoningEngine(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngine](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngine#vertexai__genai_types_ReasoningEngine_ReasoningEngine)

### vertexai._genai.types.ReasoningEngineContextSpec
    
    
    ReasoningEngineContextSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineContextSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineContextSpec#vertexai__genai_types_ReasoningEngineContextSpec_ReasoningEngineContextSpec)

### vertexai._genai.types.ReasoningEngineContextSpecMemoryBankConfig
    
    
    ReasoningEngineContextSpecMemoryBankConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineContextSpecMemoryBankConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineContextSpecMemoryBankConfig#vertexai__genai_types_ReasoningEngineContextSpecMemoryBankConfig_ReasoningEngineContextSpecMemoryBankConfig)

### vertexai._genai.types.ReasoningEngineContextSpecMemoryBankConfigGenerationConfig
    
    
    ReasoningEngineContextSpecMemoryBankConfigGenerationConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineContextSpecMemoryBankConfigGenerationConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineContextSpecMemoryBankConfigGenerationConfig#vertexai__genai_types_ReasoningEngineContextSpecMemoryBankConfigGenerationConfig_ReasoningEngineContextSpecMemoryBankConfigGenerationConfig)

### vertexai._genai.types.ReasoningEngineContextSpecMemoryBankConfigSimilaritySearchConfig
    
    
    ReasoningEngineContextSpecMemoryBankConfigSimilaritySearchConfig(
        **data: typing.Any,
    )

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineContextSpecMemoryBankConfigSimilaritySearchConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineContextSpecMemoryBankConfigSimilaritySearchConfig#vertexai__genai_types_ReasoningEngineContextSpecMemoryBankConfigSimilaritySearchConfig_ReasoningEngineContextSpecMemoryBankConfigSimilaritySearchConfig)

### vertexai._genai.types.ReasoningEngineContextSpecMemoryBankConfigTtlConfig
    
    
    ReasoningEngineContextSpecMemoryBankConfigTtlConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineContextSpecMemoryBankConfigTtlConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineContextSpecMemoryBankConfigTtlConfig#vertexai__genai_types_ReasoningEngineContextSpecMemoryBankConfigTtlConfig_ReasoningEngineContextSpecMemoryBankConfigTtlConfig)

### vertexai._genai.types.ReasoningEngineContextSpecMemoryBankConfigTtlConfigGranularTtlConfig
    
    
    ReasoningEngineContextSpecMemoryBankConfigTtlConfigGranularTtlConfig(
        **data: typing.Any,
    )

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineContextSpecMemoryBankConfigTtlConfigGranularTtlConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineContextSpecMemoryBankConfigTtlConfigGranularTtlConfig#vertexai__genai_types_ReasoningEngineContextSpecMemoryBankConfigTtlConfigGranularTtlConfig_ReasoningEngineContextSpecMemoryBankConfigTtlConfigGranularTtlConfig)

### vertexai._genai.types.ReasoningEngineRuntimeRevision
    
    
    ReasoningEngineRuntimeRevision(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineRuntimeRevision](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineRuntimeRevision#vertexai__genai_types_ReasoningEngineRuntimeRevision_ReasoningEngineRuntimeRevision)

### vertexai._genai.types.ReasoningEngineSpec
    
    
    ReasoningEngineSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineSpec#vertexai__genai_types_ReasoningEngineSpec_ReasoningEngineSpec)

### vertexai._genai.types.ReasoningEngineSpecBuildSpec
    
    
    ReasoningEngineSpecBuildSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineSpecBuildSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineSpecBuildSpec#vertexai__genai_types_ReasoningEngineSpecBuildSpec_ReasoningEngineSpecBuildSpec)

### vertexai._genai.types.ReasoningEngineSpecContainerSpec
    
    
    ReasoningEngineSpecContainerSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineSpecContainerSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineSpecContainerSpec#vertexai__genai_types_ReasoningEngineSpecContainerSpec_ReasoningEngineSpecContainerSpec)

### vertexai._genai.types.ReasoningEngineSpecDeploymentSpec
    
    
    ReasoningEngineSpecDeploymentSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineSpecDeploymentSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineSpecDeploymentSpec#vertexai__genai_types_ReasoningEngineSpecDeploymentSpec_ReasoningEngineSpecDeploymentSpec)

### vertexai._genai.types.ReasoningEngineSpecDeploymentSpecAgentGatewayConfig
    
    
    ReasoningEngineSpecDeploymentSpecAgentGatewayConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineSpecDeploymentSpecAgentGatewayConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineSpecDeploymentSpecAgentGatewayConfig#vertexai__genai_types_ReasoningEngineSpecDeploymentSpecAgentGatewayConfig_ReasoningEngineSpecDeploymentSpecAgentGatewayConfig)

### vertexai._genai.types.ReasoningEngineSpecDeploymentSpecAgentGatewayConfigAgentToAnywhereConfig
    
    
    ReasoningEngineSpecDeploymentSpecAgentGatewayConfigAgentToAnywhereConfig(
        **data: typing.Any,
    )

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineSpecDeploymentSpecAgentGatewayConfigAgentToAnywhereConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineSpecDeploymentSpecAgentGatewayConfigAgentToAnywhereConfig#vertexai__genai_types_ReasoningEngineSpecDeploymentSpecAgentGatewayConfigAgentToAnywhereConfig_ReasoningEngineSpecDeploymentSpecAgentGatewayConfigAgentToAnywhereConfig)

### vertexai._genai.types.ReasoningEngineSpecDeploymentSpecAgentGatewayConfigClientToAgentConfig
    
    
    ReasoningEngineSpecDeploymentSpecAgentGatewayConfigClientToAgentConfig(
        **data: typing.Any,
    )

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineSpecDeploymentSpecAgentGatewayConfigClientToAgentConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineSpecDeploymentSpecAgentGatewayConfigClientToAgentConfig#vertexai__genai_types_ReasoningEngineSpecDeploymentSpecAgentGatewayConfigClientToAgentConfig_ReasoningEngineSpecDeploymentSpecAgentGatewayConfigClientToAgentConfig)

### vertexai._genai.types.ReasoningEngineSpecPackageSpec
    
    
    ReasoningEngineSpecPackageSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineSpecPackageSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineSpecPackageSpec#vertexai__genai_types_ReasoningEngineSpecPackageSpec_ReasoningEngineSpecPackageSpec)

### vertexai._genai.types.ReasoningEngineSpecSourceCodeSpec
    
    
    ReasoningEngineSpecSourceCodeSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineSpecSourceCodeSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineSpecSourceCodeSpec#vertexai__genai_types_ReasoningEngineSpecSourceCodeSpec_ReasoningEngineSpecSourceCodeSpec)

### vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecAgentConfigSource
    
    
    ReasoningEngineSpecSourceCodeSpecAgentConfigSource(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecAgentConfigSource](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecAgentConfigSource#vertexai__genai_types_ReasoningEngineSpecSourceCodeSpecAgentConfigSource_ReasoningEngineSpecSourceCodeSpecAgentConfigSource)

### vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecAgentConfigSourceAdkConfig
    
    
    ReasoningEngineSpecSourceCodeSpecAgentConfigSourceAdkConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecAgentConfigSourceAdkConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecAgentConfigSourceAdkConfig#vertexai__genai_types_ReasoningEngineSpecSourceCodeSpecAgentConfigSourceAdkConfig_ReasoningEngineSpecSourceCodeSpecAgentConfigSourceAdkConfig)

### vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecDeveloperConnectConfig
    
    
    ReasoningEngineSpecSourceCodeSpecDeveloperConnectConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecDeveloperConnectConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecDeveloperConnectConfig#vertexai__genai_types_ReasoningEngineSpecSourceCodeSpecDeveloperConnectConfig_ReasoningEngineSpecSourceCodeSpecDeveloperConnectConfig)

### vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecDeveloperConnectSource
    
    
    ReasoningEngineSpecSourceCodeSpecDeveloperConnectSource(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecDeveloperConnectSource](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecDeveloperConnectSource#vertexai__genai_types_ReasoningEngineSpecSourceCodeSpecDeveloperConnectSource_ReasoningEngineSpecSourceCodeSpecDeveloperConnectSource)

### vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecImageSpec
    
    
    ReasoningEngineSpecSourceCodeSpecImageSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecImageSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecImageSpec#vertexai__genai_types_ReasoningEngineSpecSourceCodeSpecImageSpec_ReasoningEngineSpecSourceCodeSpecImageSpec)

### vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecInlineSource
    
    
    ReasoningEngineSpecSourceCodeSpecInlineSource(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecInlineSource](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecInlineSource#vertexai__genai_types_ReasoningEngineSpecSourceCodeSpecInlineSource_ReasoningEngineSpecSourceCodeSpecInlineSource)

### vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecPythonSpec
    
    
    ReasoningEngineSpecSourceCodeSpecPythonSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecPythonSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineSpecSourceCodeSpecPythonSpec#vertexai__genai_types_ReasoningEngineSpecSourceCodeSpecPythonSpec_ReasoningEngineSpecSourceCodeSpecPythonSpec)

### vertexai._genai.types.ReasoningEngineTrafficConfig
    
    
    ReasoningEngineTrafficConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineTrafficConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineTrafficConfig#vertexai__genai_types_ReasoningEngineTrafficConfig_ReasoningEngineTrafficConfig)

### vertexai._genai.types.ReasoningEngineTrafficConfigTrafficSplitAlwaysLatest
    
    
    ReasoningEngineTrafficConfigTrafficSplitAlwaysLatest(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineTrafficConfigTrafficSplitAlwaysLatest](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineTrafficConfigTrafficSplitAlwaysLatest#vertexai__genai_types_ReasoningEngineTrafficConfigTrafficSplitAlwaysLatest_ReasoningEngineTrafficConfigTrafficSplitAlwaysLatest)

### vertexai._genai.types.ReasoningEngineTrafficConfigTrafficSplitManual
    
    
    ReasoningEngineTrafficConfigTrafficSplitManual(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineTrafficConfigTrafficSplitManual](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineTrafficConfigTrafficSplitManual#vertexai__genai_types_ReasoningEngineTrafficConfigTrafficSplitManual_ReasoningEngineTrafficConfigTrafficSplitManual)

### vertexai._genai.types.ReasoningEngineTrafficConfigTrafficSplitManualTarget
    
    
    ReasoningEngineTrafficConfigTrafficSplitManualTarget(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReasoningEngineTrafficConfigTrafficSplitManualTarget](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReasoningEngineTrafficConfigTrafficSplitManualTarget#vertexai__genai_types_ReasoningEngineTrafficConfigTrafficSplitManualTarget_ReasoningEngineTrafficConfigTrafficSplitManualTarget)

### vertexai._genai.types.RedTeamingAnalysisConfig
    
    
    RedTeamingAnalysisConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RedTeamingAnalysisConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RedTeamingAnalysisConfig#vertexai__genai_types_RedTeamingAnalysisConfig_RedTeamingAnalysisConfig)

### vertexai._genai.types.RedTeamingAnalysisResult
    
    
    RedTeamingAnalysisResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RedTeamingAnalysisResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RedTeamingAnalysisResult#vertexai__genai_types_RedTeamingAnalysisResult_RedTeamingAnalysisResult)

### vertexai._genai.types.ReservationAffinity
    
    
    ReservationAffinity(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ReservationAffinity](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ReservationAffinity#vertexai__genai_types_ReservationAffinity_ReservationAffinity)

### vertexai._genai.types.ResponseCandidate
    
    
    ResponseCandidate(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ResponseCandidate](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ResponseCandidate#vertexai__genai_types_ResponseCandidate_ResponseCandidate)

### vertexai._genai.types.ResponseCandidateResult
    
    
    ResponseCandidateResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ResponseCandidateResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ResponseCandidateResult#vertexai__genai_types_ResponseCandidateResult_ResponseCandidateResult)

### vertexai._genai.types.RestoreVersionConfig
    
    
    RestoreVersionConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RestoreVersionConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RestoreVersionConfig#vertexai__genai_types_RestoreVersionConfig_RestoreVersionConfig)

### vertexai._genai.types.RestoreVersionOperation
    
    
    RestoreVersionOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RestoreVersionOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RestoreVersionOperation#vertexai__genai_types_RestoreVersionOperation_RestoreVersionOperation)

### vertexai._genai.types.RetrieveAgentEngineMemoriesConfig
    
    
    RetrieveAgentEngineMemoriesConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RetrieveAgentEngineMemoriesConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RetrieveAgentEngineMemoriesConfig#vertexai__genai_types_RetrieveAgentEngineMemoriesConfig_RetrieveAgentEngineMemoriesConfig)

### vertexai._genai.types.RetrieveMemoriesRequestSimilaritySearchParams
    
    
    RetrieveMemoriesRequestSimilaritySearchParams(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RetrieveMemoriesRequestSimilaritySearchParams](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RetrieveMemoriesRequestSimilaritySearchParams#vertexai__genai_types_RetrieveMemoriesRequestSimilaritySearchParams_RetrieveMemoriesRequestSimilaritySearchParams)

### vertexai._genai.types.RetrieveMemoriesRequestSimpleRetrievalParams
    
    
    RetrieveMemoriesRequestSimpleRetrievalParams(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RetrieveMemoriesRequestSimpleRetrievalParams](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RetrieveMemoriesRequestSimpleRetrievalParams#vertexai__genai_types_RetrieveMemoriesRequestSimpleRetrievalParams_RetrieveMemoriesRequestSimpleRetrievalParams)

### vertexai._genai.types.RetrieveMemoriesResponse
    
    
    RetrieveMemoriesResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RetrieveMemoriesResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RetrieveMemoriesResponse#vertexai__genai_types_RetrieveMemoriesResponse_RetrieveMemoriesResponse)

### vertexai._genai.types.RetrieveMemoriesResponseRetrievedMemory
    
    
    RetrieveMemoriesResponseRetrievedMemory(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RetrieveMemoriesResponseRetrievedMemory](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RetrieveMemoriesResponseRetrievedMemory#vertexai__genai_types_RetrieveMemoriesResponseRetrievedMemory_RetrieveMemoriesResponseRetrievedMemory)

### vertexai._genai.types.RetrieveMemoryProfilesConfig
    
    
    RetrieveMemoryProfilesConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RetrieveMemoryProfilesConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RetrieveMemoryProfilesConfig#vertexai__genai_types_RetrieveMemoryProfilesConfig_RetrieveMemoryProfilesConfig)

### vertexai._genai.types.RetrieveProfilesResponse
    
    
    RetrieveProfilesResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RetrieveProfilesResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RetrieveProfilesResponse#vertexai__genai_types_RetrieveProfilesResponse_RetrieveProfilesResponse)

### vertexai._genai.types.RetrieveSkillsConfig
    
    
    RetrieveSkillsConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RetrieveSkillsConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RetrieveSkillsConfig#vertexai__genai_types_RetrieveSkillsConfig_RetrieveSkillsConfig)

### vertexai._genai.types.RetrieveSkillsResponse
    
    
    RetrieveSkillsResponse(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RetrieveSkillsResponse](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RetrieveSkillsResponse#vertexai__genai_types_RetrieveSkillsResponse_RetrieveSkillsResponse)

### vertexai._genai.types.RetrievedSkill
    
    
    RetrievedSkill(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RetrievedSkill](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RetrievedSkill#vertexai__genai_types_RetrievedSkill_RetrievedSkill)

### vertexai._genai.types.RollbackAgentEngineMemoryConfig
    
    
    RollbackAgentEngineMemoryConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RollbackAgentEngineMemoryConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RollbackAgentEngineMemoryConfig#vertexai__genai_types_RollbackAgentEngineMemoryConfig_RollbackAgentEngineMemoryConfig)

### vertexai._genai.types.RougeInput
    
    
    RougeInput(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RougeInput](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RougeInput#vertexai__genai_types_RougeInput_RougeInput)

### vertexai._genai.types.RougeInstance
    
    
    RougeInstance(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RougeInstance](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RougeInstance#vertexai__genai_types_RougeInstance_RougeInstance)

### vertexai._genai.types.RougeResults
    
    
    RougeResults(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RougeResults](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RougeResults#vertexai__genai_types_RougeResults_RougeResults)

### vertexai._genai.types.Rubric
    
    
    Rubric(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.Rubric](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.Rubric#vertexai__genai_types_Rubric_Rubric)

### vertexai._genai.types.RubricBasedMetricInput
    
    
    RubricBasedMetricInput(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RubricBasedMetricInput](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RubricBasedMetricInput#vertexai__genai_types_RubricBasedMetricInput_RubricBasedMetricInput)

### vertexai._genai.types.RubricBasedMetricInstance
    
    
    RubricBasedMetricInstance(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RubricBasedMetricInstance](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RubricBasedMetricInstance#vertexai__genai_types_RubricBasedMetricInstance_RubricBasedMetricInstance)

### vertexai._genai.types.RubricBasedMetricResult
    
    
    RubricBasedMetricResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RubricBasedMetricResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RubricBasedMetricResult#vertexai__genai_types_RubricBasedMetricResult_RubricBasedMetricResult)

### vertexai._genai.types.RubricBasedMetricSpec
    
    
    RubricBasedMetricSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RubricBasedMetricSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RubricBasedMetricSpec#vertexai__genai_types_RubricBasedMetricSpec_RubricBasedMetricSpec)

### vertexai._genai.types.RubricContent
    
    
    RubricContent(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RubricContent](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RubricContent#vertexai__genai_types_RubricContent_RubricContent)

### vertexai._genai.types.RubricContentProperty
    
    
    RubricContentProperty(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RubricContentProperty](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RubricContentProperty#vertexai__genai_types_RubricContentProperty_RubricContentProperty)

### vertexai._genai.types.RubricEnhancedContents
    
    
    RubricEnhancedContents(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RubricEnhancedContents](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RubricEnhancedContents#vertexai__genai_types_RubricEnhancedContents_RubricEnhancedContents)

### vertexai._genai.types.RubricGenerationConfig
    
    
    RubricGenerationConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RubricGenerationConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RubricGenerationConfig#vertexai__genai_types_RubricGenerationConfig_RubricGenerationConfig)

### vertexai._genai.types.RubricGroup
    
    
    RubricGroup(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RubricGroup](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RubricGroup#vertexai__genai_types_RubricGroup_RubricGroup)

### vertexai._genai.types.RubricVerdict
    
    
    RubricVerdict(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RubricVerdict](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RubricVerdict#vertexai__genai_types_RubricVerdict_RubricVerdict)

### vertexai._genai.types.RunQueryJobAgentEngineConfig
    
    
    RunQueryJobAgentEngineConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RunQueryJobAgentEngineConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RunQueryJobAgentEngineConfig#vertexai__genai_types_RunQueryJobAgentEngineConfig_RunQueryJobAgentEngineConfig)

### vertexai._genai.types.RunQueryJobResult
    
    
    RunQueryJobResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.RunQueryJobResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.RunQueryJobResult#vertexai__genai_types_RunQueryJobResult_RunQueryJobResult)

### vertexai._genai.types.SamplingConfig
    
    
    SamplingConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SamplingConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SamplingConfig#vertexai__genai_types_SamplingConfig_SamplingConfig)

### vertexai._genai.types.SandboxEnvironment
    
    
    SandboxEnvironment(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SandboxEnvironment](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SandboxEnvironment#vertexai__genai_types_SandboxEnvironment_SandboxEnvironment)

### vertexai._genai.types.SandboxEnvironmentConnectionInfo
    
    
    SandboxEnvironmentConnectionInfo(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SandboxEnvironmentConnectionInfo](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SandboxEnvironmentConnectionInfo#vertexai__genai_types_SandboxEnvironmentConnectionInfo_SandboxEnvironmentConnectionInfo)

### vertexai._genai.types.SandboxEnvironmentSnapshot
    
    
    SandboxEnvironmentSnapshot(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SandboxEnvironmentSnapshot](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SandboxEnvironmentSnapshot#vertexai__genai_types_SandboxEnvironmentSnapshot_SandboxEnvironmentSnapshot)

### vertexai._genai.types.SandboxEnvironmentSpec
    
    
    SandboxEnvironmentSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SandboxEnvironmentSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SandboxEnvironmentSpec#vertexai__genai_types_SandboxEnvironmentSpec_SandboxEnvironmentSpec)

### vertexai._genai.types.SandboxEnvironmentSpecCodeExecutionEnvironment
    
    
    SandboxEnvironmentSpecCodeExecutionEnvironment(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SandboxEnvironmentSpecCodeExecutionEnvironment](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SandboxEnvironmentSpecCodeExecutionEnvironment#vertexai__genai_types_SandboxEnvironmentSpecCodeExecutionEnvironment_SandboxEnvironmentSpecCodeExecutionEnvironment)

### vertexai._genai.types.SandboxEnvironmentSpecComputerUseEnvironment
    
    
    SandboxEnvironmentSpecComputerUseEnvironment(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SandboxEnvironmentSpecComputerUseEnvironment](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SandboxEnvironmentSpecComputerUseEnvironment#vertexai__genai_types_SandboxEnvironmentSpecComputerUseEnvironment_SandboxEnvironmentSpecComputerUseEnvironment)

### vertexai._genai.types.SandboxEnvironmentTemplate
    
    
    SandboxEnvironmentTemplate(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SandboxEnvironmentTemplate](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SandboxEnvironmentTemplate#vertexai__genai_types_SandboxEnvironmentTemplate_SandboxEnvironmentTemplate)

### vertexai._genai.types.SandboxEnvironmentTemplateCustomContainerEnvironment
    
    
    SandboxEnvironmentTemplateCustomContainerEnvironment(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SandboxEnvironmentTemplateCustomContainerEnvironment](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SandboxEnvironmentTemplateCustomContainerEnvironment#vertexai__genai_types_SandboxEnvironmentTemplateCustomContainerEnvironment_SandboxEnvironmentTemplateCustomContainerEnvironment)

### vertexai._genai.types.SandboxEnvironmentTemplateCustomContainerSpec
    
    
    SandboxEnvironmentTemplateCustomContainerSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SandboxEnvironmentTemplateCustomContainerSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SandboxEnvironmentTemplateCustomContainerSpec#vertexai__genai_types_SandboxEnvironmentTemplateCustomContainerSpec_SandboxEnvironmentTemplateCustomContainerSpec)

### vertexai._genai.types.SandboxEnvironmentTemplateDefaultContainerEnvironment
    
    
    SandboxEnvironmentTemplateDefaultContainerEnvironment(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SandboxEnvironmentTemplateDefaultContainerEnvironment](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SandboxEnvironmentTemplateDefaultContainerEnvironment#vertexai__genai_types_SandboxEnvironmentTemplateDefaultContainerEnvironment_SandboxEnvironmentTemplateDefaultContainerEnvironment)

### vertexai._genai.types.SandboxEnvironmentTemplateEgressControlConfig
    
    
    SandboxEnvironmentTemplateEgressControlConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SandboxEnvironmentTemplateEgressControlConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SandboxEnvironmentTemplateEgressControlConfig#vertexai__genai_types_SandboxEnvironmentTemplateEgressControlConfig_SandboxEnvironmentTemplateEgressControlConfig)

### vertexai._genai.types.SandboxEnvironmentTemplateNetworkPort
    
    
    SandboxEnvironmentTemplateNetworkPort(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SandboxEnvironmentTemplateNetworkPort](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SandboxEnvironmentTemplateNetworkPort#vertexai__genai_types_SandboxEnvironmentTemplateNetworkPort_SandboxEnvironmentTemplateNetworkPort)

### vertexai._genai.types.SandboxEnvironmentTemplateOperation
    
    
    SandboxEnvironmentTemplateOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SandboxEnvironmentTemplateOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SandboxEnvironmentTemplateOperation#vertexai__genai_types_SandboxEnvironmentTemplateOperation_SandboxEnvironmentTemplateOperation)

### vertexai._genai.types.SandboxEnvironmentTemplateResourceRequirements
    
    
    SandboxEnvironmentTemplateResourceRequirements(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SandboxEnvironmentTemplateResourceRequirements](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SandboxEnvironmentTemplateResourceRequirements#vertexai__genai_types_SandboxEnvironmentTemplateResourceRequirements_SandboxEnvironmentTemplateResourceRequirements)

### vertexai._genai.types.SavedQuery
    
    
    SavedQuery(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SavedQuery](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SavedQuery#vertexai__genai_types_SavedQuery_SavedQuery)

### vertexai._genai.types.Scheduling
    
    
    Scheduling(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.Scheduling](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.Scheduling#vertexai__genai_types_Scheduling_Scheduling)

### vertexai._genai.types.SchemaPredictParamsGroundingConfig
    
    
    SchemaPredictParamsGroundingConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaPredictParamsGroundingConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaPredictParamsGroundingConfig#vertexai__genai_types_SchemaPredictParamsGroundingConfig_SchemaPredictParamsGroundingConfig)

### vertexai._genai.types.SchemaPredictParamsGroundingConfigSourceEntry
    
    
    SchemaPredictParamsGroundingConfigSourceEntry(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaPredictParamsGroundingConfigSourceEntry](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaPredictParamsGroundingConfigSourceEntry#vertexai__genai_types_SchemaPredictParamsGroundingConfigSourceEntry_SchemaPredictParamsGroundingConfigSourceEntry)

### vertexai._genai.types.SchemaPromptApiSchema
    
    
    SchemaPromptApiSchema(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaPromptApiSchema](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaPromptApiSchema#vertexai__genai_types_SchemaPromptApiSchema_SchemaPromptApiSchema)

### vertexai._genai.types.SchemaPromptInstancePromptExecution
    
    
    SchemaPromptInstancePromptExecution(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaPromptInstancePromptExecution](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaPromptInstancePromptExecution#vertexai__genai_types_SchemaPromptInstancePromptExecution_SchemaPromptInstancePromptExecution)

### vertexai._genai.types.SchemaPromptInstanceVariableValue
    
    
    SchemaPromptInstanceVariableValue(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaPromptInstanceVariableValue](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaPromptInstanceVariableValue#vertexai__genai_types_SchemaPromptInstanceVariableValue_SchemaPromptInstanceVariableValue)

### vertexai._genai.types.SchemaPromptSpecAppBuilderData
    
    
    SchemaPromptSpecAppBuilderData(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaPromptSpecAppBuilderData](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaPromptSpecAppBuilderData#vertexai__genai_types_SchemaPromptSpecAppBuilderData_SchemaPromptSpecAppBuilderData)

### vertexai._genai.types.SchemaPromptSpecAppBuilderDataLinkedResource
    
    
    SchemaPromptSpecAppBuilderDataLinkedResource(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaPromptSpecAppBuilderDataLinkedResource](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaPromptSpecAppBuilderDataLinkedResource#vertexai__genai_types_SchemaPromptSpecAppBuilderDataLinkedResource_SchemaPromptSpecAppBuilderDataLinkedResource)

### vertexai._genai.types.SchemaPromptSpecInteractionData
    
    
    SchemaPromptSpecInteractionData(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaPromptSpecInteractionData](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaPromptSpecInteractionData#vertexai__genai_types_SchemaPromptSpecInteractionData_SchemaPromptSpecInteractionData)

### vertexai._genai.types.SchemaPromptSpecMultimodalPrompt
    
    
    SchemaPromptSpecMultimodalPrompt(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaPromptSpecMultimodalPrompt](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaPromptSpecMultimodalPrompt#vertexai__genai_types_SchemaPromptSpecMultimodalPrompt_SchemaPromptSpecMultimodalPrompt)

### vertexai._genai.types.SchemaPromptSpecPartList
    
    
    SchemaPromptSpecPartList(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaPromptSpecPartList](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaPromptSpecPartList#vertexai__genai_types_SchemaPromptSpecPartList_SchemaPromptSpecPartList)

### vertexai._genai.types.SchemaPromptSpecPromptMessage
    
    
    SchemaPromptSpecPromptMessage(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaPromptSpecPromptMessage](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaPromptSpecPromptMessage#vertexai__genai_types_SchemaPromptSpecPromptMessage_SchemaPromptSpecPromptMessage)

### vertexai._genai.types.SchemaPromptSpecReferenceSentencePair
    
    
    SchemaPromptSpecReferenceSentencePair(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaPromptSpecReferenceSentencePair](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaPromptSpecReferenceSentencePair#vertexai__genai_types_SchemaPromptSpecReferenceSentencePair_SchemaPromptSpecReferenceSentencePair)

### vertexai._genai.types.SchemaPromptSpecReferenceSentencePairList
    
    
    SchemaPromptSpecReferenceSentencePairList(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaPromptSpecReferenceSentencePairList](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaPromptSpecReferenceSentencePairList#vertexai__genai_types_SchemaPromptSpecReferenceSentencePairList_SchemaPromptSpecReferenceSentencePairList)

### vertexai._genai.types.SchemaPromptSpecStructuredPrompt
    
    
    SchemaPromptSpecStructuredPrompt(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaPromptSpecStructuredPrompt](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaPromptSpecStructuredPrompt#vertexai__genai_types_SchemaPromptSpecStructuredPrompt_SchemaPromptSpecStructuredPrompt)

### vertexai._genai.types.SchemaPromptSpecTranslationExample
    
    
    SchemaPromptSpecTranslationExample(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaPromptSpecTranslationExample](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaPromptSpecTranslationExample#vertexai__genai_types_SchemaPromptSpecTranslationExample_SchemaPromptSpecTranslationExample)

### vertexai._genai.types.SchemaPromptSpecTranslationOption
    
    
    SchemaPromptSpecTranslationOption(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaPromptSpecTranslationOption](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaPromptSpecTranslationOption#vertexai__genai_types_SchemaPromptSpecTranslationOption_SchemaPromptSpecTranslationOption)

### vertexai._genai.types.SchemaPromptSpecTranslationPrompt
    
    
    SchemaPromptSpecTranslationPrompt(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaPromptSpecTranslationPrompt](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaPromptSpecTranslationPrompt#vertexai__genai_types_SchemaPromptSpecTranslationPrompt_SchemaPromptSpecTranslationPrompt)

### vertexai._genai.types.SchemaTablesDatasetMetadata
    
    
    SchemaTablesDatasetMetadata(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaTablesDatasetMetadata](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaTablesDatasetMetadata#vertexai__genai_types_SchemaTablesDatasetMetadata_SchemaTablesDatasetMetadata)

### vertexai._genai.types.SchemaTablesDatasetMetadataBigQuerySource
    
    
    SchemaTablesDatasetMetadataBigQuerySource(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaTablesDatasetMetadataBigQuerySource](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaTablesDatasetMetadataBigQuerySource#vertexai__genai_types_SchemaTablesDatasetMetadataBigQuerySource_SchemaTablesDatasetMetadataBigQuerySource)

### vertexai._genai.types.SchemaTablesDatasetMetadataInputConfig
    
    
    SchemaTablesDatasetMetadataInputConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaTablesDatasetMetadataInputConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaTablesDatasetMetadataInputConfig#vertexai__genai_types_SchemaTablesDatasetMetadataInputConfig_SchemaTablesDatasetMetadataInputConfig)

### vertexai._genai.types.SchemaTextPromptDatasetMetadata
    
    
    SchemaTextPromptDatasetMetadata(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SchemaTextPromptDatasetMetadata](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SchemaTextPromptDatasetMetadata#vertexai__genai_types_SchemaTextPromptDatasetMetadata_SchemaTextPromptDatasetMetadata)

### vertexai._genai.types.SecretEnvVar
    
    
    SecretEnvVar(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SecretEnvVar](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SecretEnvVar#vertexai__genai_types_SecretEnvVar_SecretEnvVar)

### vertexai._genai.types.SecretRef
    
    
    SecretRef(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SecretRef](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SecretRef#vertexai__genai_types_SecretRef_SecretRef)

### vertexai._genai.types.Session
    
    
    Session(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.Session](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.Session#vertexai__genai_types_Session_Session)

### vertexai._genai.types.SessionEvent
    
    
    SessionEvent(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SessionEvent](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SessionEvent#vertexai__genai_types_SessionEvent_SessionEvent)

### vertexai._genai.types.Skill
    
    
    Skill(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.Skill](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.Skill#vertexai__genai_types_Skill_Skill)

### vertexai._genai.types.SkillOperation
    
    
    SkillOperation(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SkillOperation](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SkillOperation#vertexai__genai_types_SkillOperation_SkillOperation)

### vertexai._genai.types.StructuredMemoryConfig
    
    
    StructuredMemoryConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.StructuredMemoryConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.StructuredMemoryConfig#vertexai__genai_types_StructuredMemoryConfig_StructuredMemoryConfig)

### vertexai._genai.types.StructuredMemorySchemaConfig
    
    
    StructuredMemorySchemaConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.StructuredMemorySchemaConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.StructuredMemorySchemaConfig#vertexai__genai_types_StructuredMemorySchemaConfig_StructuredMemorySchemaConfig)

### vertexai._genai.types.SummaryMetric
    
    
    SummaryMetric(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.SummaryMetric](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.SummaryMetric#vertexai__genai_types_SummaryMetric_SummaryMetric)

### vertexai._genai.types.TaskArtifact
    
    
    TaskArtifact(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.TaskArtifact](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.TaskArtifact#vertexai__genai_types_TaskArtifact_TaskArtifact)

### vertexai._genai.types.TaskArtifactChange
    
    
    TaskArtifactChange(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.TaskArtifactChange](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.TaskArtifactChange#vertexai__genai_types_TaskArtifactChange_TaskArtifactChange)

### vertexai._genai.types.TaskEvent
    
    
    TaskEvent(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.TaskEvent](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.TaskEvent#vertexai__genai_types_TaskEvent_TaskEvent)

### vertexai._genai.types.TaskEventData
    
    
    TaskEventData(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.TaskEventData](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.TaskEventData#vertexai__genai_types_TaskEventData_TaskEventData)

### vertexai._genai.types.TaskMessage
    
    
    TaskMessage(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.TaskMessage](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.TaskMessage#vertexai__genai_types_TaskMessage_TaskMessage)

### vertexai._genai.types.TaskMetadataChange
    
    
    TaskMetadataChange(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.TaskMetadataChange](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.TaskMetadataChange#vertexai__genai_types_TaskMetadataChange_TaskMetadataChange)

### vertexai._genai.types.TaskOutput
    
    
    TaskOutput(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.TaskOutput](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.TaskOutput#vertexai__genai_types_TaskOutput_TaskOutput)

### vertexai._genai.types.TaskOutputChange
    
    
    TaskOutputChange(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.TaskOutputChange](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.TaskOutputChange#vertexai__genai_types_TaskOutputChange_TaskOutputChange)

### vertexai._genai.types.TaskStateChange
    
    
    TaskStateChange(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.TaskStateChange](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.TaskStateChange#vertexai__genai_types_TaskStateChange_TaskStateChange)

### vertexai._genai.types.TaskStatusDetails
    
    
    TaskStatusDetails(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.TaskStatusDetails](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.TaskStatusDetails#vertexai__genai_types_TaskStatusDetails_TaskStatusDetails)

### vertexai._genai.types.TaskStatusDetailsChange
    
    
    TaskStatusDetailsChange(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.TaskStatusDetailsChange](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.TaskStatusDetailsChange#vertexai__genai_types_TaskStatusDetailsChange_TaskStatusDetailsChange)

### vertexai._genai.types.ToolCallValidInput
    
    
    ToolCallValidInput(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ToolCallValidInput](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ToolCallValidInput#vertexai__genai_types_ToolCallValidInput_ToolCallValidInput)

### vertexai._genai.types.ToolCallValidInstance
    
    
    ToolCallValidInstance(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ToolCallValidInstance](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ToolCallValidInstance#vertexai__genai_types_ToolCallValidInstance_ToolCallValidInstance)

### vertexai._genai.types.ToolCallValidMetricValue
    
    
    ToolCallValidMetricValue(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ToolCallValidMetricValue](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ToolCallValidMetricValue#vertexai__genai_types_ToolCallValidMetricValue_ToolCallValidMetricValue)

### vertexai._genai.types.ToolCallValidResults
    
    
    ToolCallValidResults(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ToolCallValidResults](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ToolCallValidResults#vertexai__genai_types_ToolCallValidResults_ToolCallValidResults)

### vertexai._genai.types.ToolCallValidSpec
    
    
    ToolCallValidSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ToolCallValidSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ToolCallValidSpec#vertexai__genai_types_ToolCallValidSpec_ToolCallValidSpec)

### vertexai._genai.types.ToolNameMatchInput
    
    
    ToolNameMatchInput(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ToolNameMatchInput](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ToolNameMatchInput#vertexai__genai_types_ToolNameMatchInput_ToolNameMatchInput)

### vertexai._genai.types.ToolNameMatchInstance
    
    
    ToolNameMatchInstance(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ToolNameMatchInstance](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ToolNameMatchInstance#vertexai__genai_types_ToolNameMatchInstance_ToolNameMatchInstance)

### vertexai._genai.types.ToolNameMatchMetricValue
    
    
    ToolNameMatchMetricValue(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ToolNameMatchMetricValue](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ToolNameMatchMetricValue#vertexai__genai_types_ToolNameMatchMetricValue_ToolNameMatchMetricValue)

### vertexai._genai.types.ToolNameMatchResults
    
    
    ToolNameMatchResults(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ToolNameMatchResults](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ToolNameMatchResults#vertexai__genai_types_ToolNameMatchResults_ToolNameMatchResults)

### vertexai._genai.types.ToolNameMatchSpec
    
    
    ToolNameMatchSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ToolNameMatchSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ToolNameMatchSpec#vertexai__genai_types_ToolNameMatchSpec_ToolNameMatchSpec)

### vertexai._genai.types.ToolParameterKVMatchInput
    
    
    ToolParameterKVMatchInput(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ToolParameterKVMatchInput](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ToolParameterKVMatchInput#vertexai__genai_types_ToolParameterKVMatchInput_ToolParameterKVMatchInput)

### vertexai._genai.types.ToolParameterKVMatchInstance
    
    
    ToolParameterKVMatchInstance(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ToolParameterKVMatchInstance](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ToolParameterKVMatchInstance#vertexai__genai_types_ToolParameterKVMatchInstance_ToolParameterKVMatchInstance)

### vertexai._genai.types.ToolParameterKVMatchMetricValue
    
    
    ToolParameterKVMatchMetricValue(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ToolParameterKVMatchMetricValue](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ToolParameterKVMatchMetricValue#vertexai__genai_types_ToolParameterKVMatchMetricValue_ToolParameterKVMatchMetricValue)

### vertexai._genai.types.ToolParameterKVMatchResults
    
    
    ToolParameterKVMatchResults(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ToolParameterKVMatchResults](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ToolParameterKVMatchResults#vertexai__genai_types_ToolParameterKVMatchResults_ToolParameterKVMatchResults)

### vertexai._genai.types.ToolParameterKVMatchSpec
    
    
    ToolParameterKVMatchSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ToolParameterKVMatchSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ToolParameterKVMatchSpec#vertexai__genai_types_ToolParameterKVMatchSpec_ToolParameterKVMatchSpec)

### vertexai._genai.types.ToolParameterKeyMatchInput
    
    
    ToolParameterKeyMatchInput(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ToolParameterKeyMatchInput](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ToolParameterKeyMatchInput#vertexai__genai_types_ToolParameterKeyMatchInput_ToolParameterKeyMatchInput)

### vertexai._genai.types.ToolParameterKeyMatchInstance
    
    
    ToolParameterKeyMatchInstance(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ToolParameterKeyMatchInstance](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ToolParameterKeyMatchInstance#vertexai__genai_types_ToolParameterKeyMatchInstance_ToolParameterKeyMatchInstance)

### vertexai._genai.types.ToolParameterKeyMatchMetricValue
    
    
    ToolParameterKeyMatchMetricValue(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ToolParameterKeyMatchMetricValue](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ToolParameterKeyMatchMetricValue#vertexai__genai_types_ToolParameterKeyMatchMetricValue_ToolParameterKeyMatchMetricValue)

### vertexai._genai.types.ToolParameterKeyMatchResults
    
    
    ToolParameterKeyMatchResults(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ToolParameterKeyMatchResults](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ToolParameterKeyMatchResults#vertexai__genai_types_ToolParameterKeyMatchResults_ToolParameterKeyMatchResults)

### vertexai._genai.types.ToolParameterKeyMatchSpec
    
    
    ToolParameterKeyMatchSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.ToolParameterKeyMatchSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.ToolParameterKeyMatchSpec#vertexai__genai_types_ToolParameterKeyMatchSpec_ToolParameterKeyMatchSpec)

### vertexai._genai.types.TuningResourceUsageAssessmentConfig
    
    
    TuningResourceUsageAssessmentConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.TuningResourceUsageAssessmentConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.TuningResourceUsageAssessmentConfig#vertexai__genai_types_TuningResourceUsageAssessmentConfig_TuningResourceUsageAssessmentConfig)

### vertexai._genai.types.TuningResourceUsageAssessmentResult
    
    
    TuningResourceUsageAssessmentResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.TuningResourceUsageAssessmentResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.TuningResourceUsageAssessmentResult#vertexai__genai_types_TuningResourceUsageAssessmentResult_TuningResourceUsageAssessmentResult)

### vertexai._genai.types.TuningValidationAssessmentConfig
    
    
    TuningValidationAssessmentConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.TuningValidationAssessmentConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.TuningValidationAssessmentConfig#vertexai__genai_types_TuningValidationAssessmentConfig_TuningValidationAssessmentConfig)

### vertexai._genai.types.TuningValidationAssessmentResult
    
    
    TuningValidationAssessmentResult(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.TuningValidationAssessmentResult](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.TuningValidationAssessmentResult#vertexai__genai_types_TuningValidationAssessmentResult_TuningValidationAssessmentResult)

### vertexai._genai.types.UnifiedMetric
    
    
    UnifiedMetric(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.UnifiedMetric](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.UnifiedMetric#vertexai__genai_types_UnifiedMetric_UnifiedMetric)

### vertexai._genai.types.UpdateAgentEngineConfig
    
    
    UpdateAgentEngineConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.UpdateAgentEngineConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.UpdateAgentEngineConfig#vertexai__genai_types_UpdateAgentEngineConfig_UpdateAgentEngineConfig)

### vertexai._genai.types.UpdateAgentEngineMemoryConfig
    
    
    UpdateAgentEngineMemoryConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.UpdateAgentEngineMemoryConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.UpdateAgentEngineMemoryConfig#vertexai__genai_types_UpdateAgentEngineMemoryConfig_UpdateAgentEngineMemoryConfig)

### vertexai._genai.types.UpdateAgentEngineSessionConfig
    
    
    UpdateAgentEngineSessionConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.UpdateAgentEngineSessionConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.UpdateAgentEngineSessionConfig#vertexai__genai_types_UpdateAgentEngineSessionConfig_UpdateAgentEngineSessionConfig)

### vertexai._genai.types.UpdateEvaluationExperimentConfig
    
    
    UpdateEvaluationExperimentConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.UpdateEvaluationExperimentConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.UpdateEvaluationExperimentConfig#vertexai__genai_types_UpdateEvaluationExperimentConfig_UpdateEvaluationExperimentConfig)

### vertexai._genai.types.UpdatePromptConfig
    
    
    UpdatePromptConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.UpdatePromptConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.UpdatePromptConfig#vertexai__genai_types_UpdatePromptConfig_UpdatePromptConfig)

### vertexai._genai.types.UpdateSkillConfig
    
    
    UpdateSkillConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.UpdateSkillConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.UpdateSkillConfig#vertexai__genai_types_UpdateSkillConfig_UpdateSkillConfig)

### vertexai._genai.types.VertexBaseConfig
    
    
    VertexBaseConfig(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.VertexBaseConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.VertexBaseConfig#vertexai__genai_types_VertexBaseConfig_VertexBaseConfig)

### vertexai._genai.types.VulnerableTool
    
    
    VulnerableTool(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.VulnerableTool](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.VulnerableTool#vertexai__genai_types_VulnerableTool_VulnerableTool)

### vertexai._genai.types.WinRateStats
    
    
    WinRateStats(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.WinRateStats](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.WinRateStats#vertexai__genai_types_WinRateStats_WinRateStats)

### vertexai._genai.types.WorkerPoolSpec
    
    
    WorkerPoolSpec(**data: typing.Any)

Create a new model by parsing and validating input data from keyword arguments.

See more: [vertexai._genai.types.WorkerPoolSpec](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai._genai.types.WorkerPoolSpec#vertexai__genai_types_WorkerPoolSpec_WorkerPoolSpec)

### vertexai.agent_engines.AG2Agent
    
    
    AG2Agent(
        model: str,
        runnable_name: str,
        *,
        api_type: typing.Optional[str] = None,
        llm_config: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        system_instruction: typing.Optional[str] = None,
        runnable_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        runnable_builder: typing.Optional[typing.Callable[[...], ConversableAgent]] = None,
        tools: typing.Optional[typing.Sequence[typing.Callable[[...], typing.Any]]] = None,
        enable_tracing: bool = False,
        instrumentor_builder: typing.Optional[typing.Callable[[...], typing.Any]] = None
    )

Initializes the AG2 Agent.

See more: [vertexai.agent_engines.AG2Agent](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AG2Agent#vertexai_agent_engines_AG2Agent_AG2Agent)

### vertexai.agent_engines.AG2Agent.clone
    
    
    clone() -> vertexai.agent_engines.templates.ag2.AG2Agent

Returns a clone of the AG2Agent.

See more: [vertexai.agent_engines.AG2Agent.clone](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AG2Agent#vertexai_agent_engines_AG2Agent_clone)

### vertexai.agent_engines.AG2Agent.query
    
    
    query(
        *,
        input: typing.Union[str, typing.Mapping[str, typing.Any]],
        max_turns: typing.Optional[int] = None,
        **kwargs: typing.Any
    ) -> typing.Dict[str, typing.Any]

Queries the Agent with the given input.

See more: [vertexai.agent_engines.AG2Agent.query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AG2Agent#vertexai_agent_engines_AG2Agent_query)

### vertexai.agent_engines.AG2Agent.set_up
    
    
    set_up()

Sets up the agent for execution of queries at runtime.

See more: [vertexai.agent_engines.AG2Agent.set_up](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AG2Agent#vertexai_agent_engines_AG2Agent_set_up)

### vertexai.agent_engines.AdkApp
    
    
    AdkApp(
        *,
        app: App = None,
        agent: BaseAgent = None,
        app_name: typing.Optional[str] = None,
        plugins: typing.Optional[typing.List[BasePlugin]] = None,
        enable_tracing: typing.Optional[bool] = None,
        session_service_builder: typing.Optional[
            typing.Callable[[...], BaseSessionService]
        ] = None,
        artifact_service_builder: typing.Optional[
            typing.Callable[[...], BaseArtifactService]
        ] = None,
        memory_service_builder: typing.Optional[
            typing.Callable[[...], BaseMemoryService]
        ] = None,
        instrumentor_builder: typing.Optional[typing.Callable[[...], typing.Any]] = None
    )

An ADK Application.

See more: [vertexai.agent_engines.AdkApp](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AdkApp#vertexai_agent_engines_AdkApp_AdkApp)

### vertexai.agent_engines.AdkApp.async_add_session_to_memory
    
    
    async_add_session_to_memory(*, session: typing.Dict[str, typing.Any])

Generates memories.

See more: [vertexai.agent_engines.AdkApp.async_add_session_to_memory](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AdkApp#vertexai_agent_engines_AdkApp_async_add_session_to_memory)

### vertexai.agent_engines.AdkApp.async_create_session
    
    
    async_create_session(
        *,
        user_id: str,
        session_id: typing.Optional[str] = None,
        state: typing.Optional[typing.Dict[str, typing.Any]] = None,
        **kwargs
    )

Creates a new session.

See more: [vertexai.agent_engines.AdkApp.async_create_session](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AdkApp#vertexai_agent_engines_AdkApp_async_create_session)

### vertexai.agent_engines.AdkApp.async_delete_session
    
    
    async_delete_session(*, user_id: str, session_id: str, **kwargs)

Deletes a session for the given user.

See more: [vertexai.agent_engines.AdkApp.async_delete_session](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AdkApp#vertexai_agent_engines_AdkApp_async_delete_session)

### vertexai.agent_engines.AdkApp.async_get_session
    
    
    async_get_session(*, user_id: str, session_id: str, **kwargs)

Get a session for the given user.

See more: [vertexai.agent_engines.AdkApp.async_get_session](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AdkApp#vertexai_agent_engines_AdkApp_async_get_session)

### vertexai.agent_engines.AdkApp.async_list_sessions
    
    
    async_list_sessions(*, user_id: str, **kwargs)

List sessions for the given user.

See more: [vertexai.agent_engines.AdkApp.async_list_sessions](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AdkApp#vertexai_agent_engines_AdkApp_async_list_sessions)

### vertexai.agent_engines.AdkApp.async_search_memory
    
    
    async_search_memory(*, user_id: str, query: str)

Searches memories for the given user.

See more: [vertexai.agent_engines.AdkApp.async_search_memory](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AdkApp#vertexai_agent_engines_AdkApp_async_search_memory)

### vertexai.agent_engines.AdkApp.async_stream_query
    
    
    async_stream_query(
        *,
        message: typing.Union[str, typing.Dict[str, typing.Any]],
        user_id: str,
        session_id: typing.Optional[str] = None,
        session_events: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None,
        run_config: typing.Optional[typing.Dict[str, typing.Any]] = None,
        **kwargs
    ) -> typing.AsyncIterable[typing.Dict[str, typing.Any]]

Streams responses asynchronously from the ADK application.

See more: [vertexai.agent_engines.AdkApp.async_stream_query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AdkApp#vertexai_agent_engines_AdkApp_async_stream_query)

### vertexai.agent_engines.AdkApp.clone
    
    
    clone()

Returns a clone of the ADK application.

See more: [vertexai.agent_engines.AdkApp.clone](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AdkApp#vertexai_agent_engines_AdkApp_clone)

### vertexai.agent_engines.AdkApp.create_session
    
    
    create_session(
        *,
        user_id: str,
        session_id: typing.Optional[str] = None,
        state: typing.Optional[typing.Dict[str, typing.Any]] = None,
        **kwargs
    )

Deprecated.

See more: [vertexai.agent_engines.AdkApp.create_session](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AdkApp#vertexai_agent_engines_AdkApp_create_session)

### vertexai.agent_engines.AdkApp.delete_session
    
    
    delete_session(*, user_id: str, session_id: str, **kwargs)

Deprecated.

See more: [vertexai.agent_engines.AdkApp.delete_session](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AdkApp#vertexai_agent_engines_AdkApp_delete_session)

### vertexai.agent_engines.AdkApp.get_session
    
    
    get_session(*, user_id: str, session_id: str, **kwargs)

Deprecated.

See more: [vertexai.agent_engines.AdkApp.get_session](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AdkApp#vertexai_agent_engines_AdkApp_get_session)

### vertexai.agent_engines.AdkApp.list_sessions
    
    
    list_sessions(*, user_id: str, **kwargs)

Deprecated.

See more: [vertexai.agent_engines.AdkApp.list_sessions](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AdkApp#vertexai_agent_engines_AdkApp_list_sessions)

### vertexai.agent_engines.AdkApp.register_operations
    
    
    register_operations() -> typing.Dict[str, typing.List[str]]

Registers the operations of the ADK application.

See more: [vertexai.agent_engines.AdkApp.register_operations](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AdkApp#vertexai_agent_engines_AdkApp_register_operations)

### vertexai.agent_engines.AdkApp.set_up
    
    
    set_up()

Sets up the ADK application.

See more: [vertexai.agent_engines.AdkApp.set_up](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AdkApp#vertexai_agent_engines_AdkApp_set_up)

### vertexai.agent_engines.AdkApp.stream_query
    
    
    stream_query(
        *,
        message: typing.Union[str, typing.Dict[str, typing.Any]],
        user_id: str,
        session_id: typing.Optional[str] = None,
        run_config: typing.Optional[typing.Dict[str, typing.Any]] = None,
        **kwargs
    )

Deprecated.

See more: [vertexai.agent_engines.AdkApp.stream_query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AdkApp#vertexai_agent_engines_AdkApp_stream_query)

### vertexai.agent_engines.AdkApp.streaming_agent_run_with_events
    
    
    streaming_agent_run_with_events(request_json: str)

Streams responses asynchronously from the ADK application.

See more: [vertexai.agent_engines.AdkApp.streaming_agent_run_with_events](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AdkApp#vertexai_agent_engines_AdkApp_streaming_agent_run_with_events)

### vertexai.agent_engines.AgentEngine
    
    
    AgentEngine(resource_name: str)

Retrieves an Agent Engine resource.

See more: [vertexai.agent_engines.AgentEngine](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AgentEngine#vertexai_agent_engines_AgentEngine_AgentEngine)

### vertexai.agent_engines.AgentEngine.create
    
    
    create(
        agent_engine: typing.Union[
            None,
            vertexai.agent_engines.AsyncQueryable,
            vertexai.agent_engines.AsyncStreamQueryable,
            vertexai.agent_engines._agent_engines.BidiStreamQueryable,
            vertexai.agent_engines.OperationRegistrable,
            vertexai.agent_engines.Queryable,
            vertexai.agent_engines.StreamQueryable,
        ] = None,
        *,
        requirements: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        display_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        gcs_dir_name: typing.Optional[str] = None,
        extra_packages: typing.Optional[typing.Sequence[str]] = None,
        env_vars: typing.Optional[
            typing.Union[
                typing.Sequence[str],
                typing.Dict[
                    str,
                    typing.Union[str, google.cloud.aiplatform_v1.types.env_var.SecretRef],
                ],
            ]
        ] = None,
        build_options: typing.Optional[typing.Dict[str, typing.Sequence[str]]] = None,
        service_account: typing.Optional[str] = None,
        identity_type: typing.Optional[
            typing.Union[
                str,
                google.cloud.aiplatform_v1.types.reasoning_engine.ReasoningEngineSpec.IdentityType,
            ]
        ] = None,
        psc_interface_config: typing.Optional[
            google.cloud.aiplatform_v1.types.service_networking.PscInterfaceConfig
        ] = None,
        min_instances: typing.Optional[int] = None,
        max_instances: typing.Optional[int] = None,
        resource_limits: typing.Optional[typing.Dict[str, str]] = None,
        container_concurrency: typing.Optional[int] = None,
        encryption_spec: typing.Optional[
            google.cloud.aiplatform_v1.types.encryption_spec.EncryptionSpec
        ] = None
    ) -> vertexai.agent_engines.AgentEngine

Creates a new Agent Engine.

See more: [vertexai.agent_engines.AgentEngine.create](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AgentEngine#vertexai_agent_engines_AgentEngine_create)

### vertexai.agent_engines.AgentEngine.delete
    
    
    delete(*, force: bool = False, **kwargs) -> None

Deletes the ReasoningEngine.

See more: [vertexai.agent_engines.AgentEngine.delete](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AgentEngine#vertexai_agent_engines_AgentEngine_delete)

### vertexai.agent_engines.AgentEngine.list
    
    
    list(
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        parent: typing.Optional[str] = None,
    ) -> typing.List[google.cloud.aiplatform.base.VertexAiResourceNoun]

List all instances of this Vertex AI Resource.

See more: [vertexai.agent_engines.AgentEngine.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AgentEngine#vertexai_agent_engines_AgentEngine_list)

### vertexai.agent_engines.AgentEngine.operation_schemas
    
    
    operation_schemas() -> typing.Sequence[typing.Dict[str, typing.Any]]

Returns the (Open)API schemas for the Agent Engine.

See more: [vertexai.agent_engines.AgentEngine.operation_schemas](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AgentEngine#vertexai_agent_engines_AgentEngine_operation_schemas)

### vertexai.agent_engines.AgentEngine.to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

See more: [vertexai.agent_engines.AgentEngine.to_dict](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AgentEngine#vertexai_agent_engines_AgentEngine_to_dict)

### vertexai.agent_engines.AgentEngine.update
    
    
    update(
        *,
        agent_engine: typing.Union[
            None,
            vertexai.agent_engines.AsyncQueryable,
            vertexai.agent_engines.AsyncStreamQueryable,
            vertexai.agent_engines._agent_engines.BidiStreamQueryable,
            vertexai.agent_engines.OperationRegistrable,
            vertexai.agent_engines.Queryable,
            vertexai.agent_engines.StreamQueryable,
        ] = None,
        requirements: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        display_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        gcs_dir_name: typing.Optional[str] = None,
        extra_packages: typing.Optional[typing.Sequence[str]] = None,
        env_vars: typing.Optional[
            typing.Union[
                typing.Sequence[str],
                typing.Dict[
                    str,
                    typing.Union[str, google.cloud.aiplatform_v1.types.env_var.SecretRef],
                ],
            ]
        ] = None,
        build_options: typing.Optional[typing.Dict[str, typing.Sequence[str]]] = None,
        service_account: typing.Optional[str] = None,
        identity_type: typing.Optional[
            typing.Union[
                str,
                google.cloud.aiplatform_v1.types.reasoning_engine.ReasoningEngineSpec.IdentityType,
            ]
        ] = None,
        psc_interface_config: typing.Optional[
            google.cloud.aiplatform_v1.types.service_networking.PscInterfaceConfig
        ] = None,
        min_instances: typing.Optional[int] = None,
        max_instances: typing.Optional[int] = None,
        resource_limits: typing.Optional[typing.Dict[str, str]] = None,
        container_concurrency: typing.Optional[int] = None,
        encryption_spec: typing.Optional[
            google.cloud.aiplatform_v1.types.encryption_spec.EncryptionSpec
        ] = None
    ) -> vertexai.agent_engines.AgentEngine

Updates an existing Agent Engine.

See more: [vertexai.agent_engines.AgentEngine.update](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AgentEngine#vertexai_agent_engines_AgentEngine_update)

### vertexai.agent_engines.AgentEngine.wait
    
    
    wait()

Helper method that blocks until all futures are complete.

See more: [vertexai.agent_engines.AgentEngine.wait](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AgentEngine#vertexai_agent_engines_AgentEngine_wait)

### vertexai.agent_engines.AsyncQueryable.async_query
    
    
    async_query(**kwargs) -> typing.Coroutine[typing.Any, typing.Any, typing.Any]

Runs the Agent Engine to serve the user query asynchronously.

See more: [vertexai.agent_engines.AsyncQueryable.async_query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AsyncQueryable#vertexai_agent_engines_AsyncQueryable_async_query)

### vertexai.agent_engines.AsyncStreamQueryable.async_stream_query
    
    
    async_stream_query(**kwargs) -> typing.AsyncIterable[typing.Any]

Asynchronously stream responses to serve the user query.

See more: [vertexai.agent_engines.AsyncStreamQueryable.async_stream_query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.AsyncStreamQueryable#vertexai_agent_engines_AsyncStreamQueryable_async_stream_query)

### vertexai.agent_engines.Cloneable.clone
    
    
    clone() -> typing.Any

Return a clone of the object.

See more: [vertexai.agent_engines.Cloneable.clone](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.Cloneable#vertexai_agent_engines_Cloneable_clone)

### vertexai.agent_engines.LangchainAgent
    
    
    LangchainAgent(
        model: str,
        *,
        system_instruction: typing.Optional[str] = None,
        prompt: typing.Optional[RunnableSerializable] = None,
        tools: typing.Optional[_ToolsType] = None,
        output_parser: typing.Optional[RunnableSerializable] = None,
        chat_history: typing.Optional[GetSessionHistoryCallable] = None,
        model_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        model_tool_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        agent_executor_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        runnable_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        model_builder: typing.Optional[typing.Callable] = None,
        runnable_builder: typing.Optional[typing.Callable] = None,
        enable_tracing: bool = False,
        instrumentor_builder: typing.Optional[typing.Callable[[...], typing.Any]] = None
    )

Initializes the LangchainAgent.

See more: [vertexai.agent_engines.LangchainAgent](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.LangchainAgent#vertexai_agent_engines_LangchainAgent_LangchainAgent)

### vertexai.agent_engines.LangchainAgent.clone
    
    
    clone() -> vertexai.agent_engines.templates.langchain.LangchainAgent

Returns a clone of the LangchainAgent.

See more: [vertexai.agent_engines.LangchainAgent.clone](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.LangchainAgent#vertexai_agent_engines_LangchainAgent_clone)

### vertexai.agent_engines.LangchainAgent.query
    
    
    query(
        *,
        input: typing.Union[str, typing.Mapping[str, typing.Any]],
        config: typing.Optional[RunnableConfig] = None,
        **kwargs: typing.Any
    ) -> typing.Dict[str, typing.Any]

Queries the Agent with the given input and config.

See more: [vertexai.agent_engines.LangchainAgent.query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.LangchainAgent#vertexai_agent_engines_LangchainAgent_query)

### vertexai.agent_engines.LangchainAgent.set_up
    
    
    set_up()

Sets up the agent for execution of queries at runtime.

See more: [vertexai.agent_engines.LangchainAgent.set_up](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.LangchainAgent#vertexai_agent_engines_LangchainAgent_set_up)

### vertexai.agent_engines.LangchainAgent.stream_query
    
    
    stream_query(
        *,
        input: typing.Union[str, typing.Mapping[str, typing.Any]],
        config: typing.Optional[RunnableConfig] = None,
        **kwargs
    ) -> typing.Iterable[typing.Any]

Stream queries the Agent with the given input and config.

See more: [vertexai.agent_engines.LangchainAgent.stream_query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.LangchainAgent#vertexai_agent_engines_LangchainAgent_stream_query)

### vertexai.agent_engines.LanggraphAgent
    
    
    LanggraphAgent(
        model: str,
        *,
        tools: typing.Optional[typing.Sequence[_ToolLike]] = None,
        model_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        model_tool_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        model_builder: typing.Optional[typing.Callable[[...], BaseLanguageModel]] = None,
        runnable_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        runnable_builder: typing.Optional[typing.Callable[[...], typing.Any]] = None,
        checkpointer_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        checkpointer_builder: typing.Optional[
            typing.Callable[[...], BaseCheckpointSaver]
        ] = None,
        enable_tracing: bool = False,
        instrumentor_builder: typing.Optional[typing.Callable[[...], typing.Any]] = None
    )

Initializes the LangGraph Agent.

See more: [vertexai.agent_engines.LanggraphAgent](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.LanggraphAgent#vertexai_agent_engines_LanggraphAgent_LanggraphAgent)

### vertexai.agent_engines.LanggraphAgent.clone
    
    
    clone() -> vertexai.agent_engines.templates.langgraph.LanggraphAgent

Returns a clone of the LanggraphAgent.

See more: [vertexai.agent_engines.LanggraphAgent.clone](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.LanggraphAgent#vertexai_agent_engines_LanggraphAgent_clone)

### vertexai.agent_engines.LanggraphAgent.get_state
    
    
    get_state(
        config: typing.Optional[dict[str, typing.Any]] = None, **kwargs: typing.Any
    ) -> typing.Dict[str, typing.Any]

Gets the current state of the Agent.

See more: [vertexai.agent_engines.LanggraphAgent.get_state](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.LanggraphAgent#vertexai_agent_engines_LanggraphAgent_get_state)

### vertexai.agent_engines.LanggraphAgent.get_state_history
    
    
    get_state_history(
        config: typing.Optional[dict[str, typing.Any]] = None, **kwargs: typing.Any
    ) -> typing.Iterable[typing.Any]

Gets the state history of the Agent.

See more: [vertexai.agent_engines.LanggraphAgent.get_state_history](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.LanggraphAgent#vertexai_agent_engines_LanggraphAgent_get_state_history)

### vertexai.agent_engines.LanggraphAgent.query
    
    
    query(
        *,
        input: typing.Union[str, typing.Mapping[str, typing.Any]],
        config: typing.Optional[dict[str, typing.Any]] = None,
        **kwargs: typing.Any
    ) -> typing.Dict[str, typing.Any]

Queries the Agent with the given input and config.

See more: [vertexai.agent_engines.LanggraphAgent.query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.LanggraphAgent#vertexai_agent_engines_LanggraphAgent_query)

### vertexai.agent_engines.LanggraphAgent.register_operations
    
    
    register_operations() -> typing.Mapping[str, typing.Sequence[str]]

Registers the operations of the Agent.

See more: [vertexai.agent_engines.LanggraphAgent.register_operations](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.LanggraphAgent#vertexai_agent_engines_LanggraphAgent_register_operations)

### vertexai.agent_engines.LanggraphAgent.set_up
    
    
    set_up()

Sets up the agent for execution of queries at runtime.

See more: [vertexai.agent_engines.LanggraphAgent.set_up](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.LanggraphAgent#vertexai_agent_engines_LanggraphAgent_set_up)

### vertexai.agent_engines.LanggraphAgent.stream_query
    
    
    stream_query(
        *,
        input: typing.Union[str, typing.Mapping[str, typing.Any]],
        config: typing.Optional[dict[str, typing.Any]] = None,
        **kwargs
    ) -> typing.Iterable[typing.Any]

Stream queries the Agent with the given input and config.

See more: [vertexai.agent_engines.LanggraphAgent.stream_query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.LanggraphAgent#vertexai_agent_engines_LanggraphAgent_stream_query)

### vertexai.agent_engines.LanggraphAgent.update_state
    
    
    update_state(
        config: typing.Optional[dict[str, typing.Any]] = None, **kwargs: typing.Any
    ) -> typing.Dict[str, typing.Any]

Updates the state of the Agent.

See more: [vertexai.agent_engines.LanggraphAgent.update_state](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.LanggraphAgent#vertexai_agent_engines_LanggraphAgent_update_state)

### vertexai.agent_engines.ModuleAgent
    
    
    ModuleAgent(
        *,
        module_name: str,
        agent_name: str,
        register_operations: typing.Dict[str, typing.Sequence[str]],
        sys_paths: typing.Optional[typing.Sequence[str]] = None,
        agent_framework: typing.Optional[str] = None
    )

Initializes a module-based agent.

See more: [vertexai.agent_engines.ModuleAgent](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.ModuleAgent#vertexai_agent_engines_ModuleAgent_ModuleAgent)

### vertexai.agent_engines.ModuleAgent.clone
    
    
    clone()

Return a clone of the agent.

See more: [vertexai.agent_engines.ModuleAgent.clone](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.ModuleAgent#vertexai_agent_engines_ModuleAgent_clone)

### vertexai.agent_engines.ModuleAgent.register_operations
    
    
    register_operations(**kwargs) -> typing.Dict[str, typing.Sequence[str]]

Register the user provided operations (modes and methods).

See more: [vertexai.agent_engines.ModuleAgent.register_operations](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.ModuleAgent#vertexai_agent_engines_ModuleAgent_register_operations)

### vertexai.agent_engines.ModuleAgent.set_up
    
    
    set_up() -> None

Sets up the agent for execution of queries at runtime.

See more: [vertexai.agent_engines.ModuleAgent.set_up](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.ModuleAgent#vertexai_agent_engines_ModuleAgent_set_up)

### vertexai.agent_engines.OperationRegistrable.register_operations
    
    
    register_operations(**kwargs) -> typing.Dict[str, typing.Sequence[str]]

Register the user provided operations (modes and methods).

See more: [vertexai.agent_engines.OperationRegistrable.register_operations](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.OperationRegistrable#vertexai_agent_engines_OperationRegistrable_register_operations)

### vertexai.agent_engines.Queryable.query
    
    
    query(**kwargs) -> typing.Any

Runs the Agent Engine to serve the user query.

See more: [vertexai.agent_engines.Queryable.query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.Queryable#vertexai_agent_engines_Queryable_query)

### vertexai.agent_engines.StreamQueryable.stream_query
    
    
    stream_query(**kwargs) -> typing.Iterable[typing.Any]

Stream responses to serve the user query.

See more: [vertexai.agent_engines.StreamQueryable.stream_query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.agent_engines.StreamQueryable#vertexai_agent_engines_StreamQueryable_stream_query)

### vertexai.evaluation.CustomMetric
    
    
    CustomMetric(
        name: str,
        metric_function: typing.Callable[
            [typing.Dict[str, typing.Any]], typing.Dict[str, typing.Any]
        ],
    )

Initializes the evaluation metric.

See more: [vertexai.evaluation.CustomMetric](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.CustomMetric#vertexai_evaluation_CustomMetric_CustomMetric)

### vertexai.evaluation.EvalTask
    
    
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

See more: [vertexai.evaluation.EvalTask](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.EvalTask#vertexai_evaluation_EvalTask_EvalTask)

### vertexai.evaluation.EvalTask.display_runs
    
    
    display_runs()

Displays experiment runs associated with this EvalTask.

See more: [vertexai.evaluation.EvalTask.display_runs](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.EvalTask#vertexai_evaluation_EvalTask_display_runs)

### vertexai.evaluation.EvalTask.evaluate
    
    
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

See more: [vertexai.evaluation.EvalTask.evaluate](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.EvalTask#vertexai_evaluation_EvalTask_evaluate)

### vertexai.evaluation.MetricPromptTemplateExamples.get_prompt_template
    
    
    get_prompt_template(metric_name: str) -> str

Returns the prompt template for the given metric name.

See more: [vertexai.evaluation.MetricPromptTemplateExamples.get_prompt_template](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.MetricPromptTemplateExamples#vertexai_evaluation_MetricPromptTemplateExamples_get_prompt_template)

### vertexai.evaluation.MetricPromptTemplateExamples.list_example_metric_names
    
    
    list_example_metric_names() -> typing.List[str]

Returns a list of all metric prompt templates.

See more: [vertexai.evaluation.MetricPromptTemplateExamples.list_example_metric_names](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.MetricPromptTemplateExamples#vertexai_evaluation_MetricPromptTemplateExamples_list_example_metric_names)

### vertexai.evaluation.PairwiseMetric
    
    
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

See more: [vertexai.evaluation.PairwiseMetric](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.PairwiseMetric#vertexai_evaluation_PairwiseMetric_PairwiseMetric)

### vertexai.evaluation.PairwiseMetricPromptTemplate
    
    
    PairwiseMetricPromptTemplate(
        *,
        criteria: typing.Dict[str, str],
        rating_rubric: typing.Dict[str, str],
        input_variables: typing.Optional[typing.List[str]] = None,
        instruction: typing.Optional[str] = None,
        metric_definition: typing.Optional[str] = None,
        evaluation_steps: typing.Optional[typing.Dict[str, str]] = None,
        few_shot_examples: typing.Optional[typing.List[str]] = None
    )

Initializes a pairwise metric prompt template.

See more: [vertexai.evaluation.PairwiseMetricPromptTemplate](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.PairwiseMetricPromptTemplate#vertexai_evaluation_PairwiseMetricPromptTemplate_PairwiseMetricPromptTemplate)

### vertexai.evaluation.PairwiseMetricPromptTemplate.__str__
    
    
    __str__()

Serializes the pairwise metric prompt template to a string.

See more: [vertexai.evaluation.PairwiseMetricPromptTemplate.**str**](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.PairwiseMetricPromptTemplate#vertexai_evaluation_PairwiseMetricPromptTemplate___str__)

### vertexai.evaluation.PairwiseMetricPromptTemplate.assemble
    
    
    assemble(**kwargs) -> vertexai.evaluation.prompt_template.PromptTemplate

Replaces only the provided variables in the template with specific values.

See more: [vertexai.evaluation.PairwiseMetricPromptTemplate.assemble](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.PairwiseMetricPromptTemplate#vertexai_evaluation_PairwiseMetricPromptTemplate_assemble)

### vertexai.evaluation.PairwiseMetricPromptTemplate.get_default_pairwise_evaluation_steps
    
    
    get_default_pairwise_evaluation_steps() -> typing.Dict[str, str]

Returns the default evaluation steps for the metric prompt template.

See more: [vertexai.evaluation.PairwiseMetricPromptTemplate.get_default_pairwise_evaluation_steps](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.PairwiseMetricPromptTemplate#vertexai_evaluation_PairwiseMetricPromptTemplate_get_default_pairwise_evaluation_steps)

### vertexai.evaluation.PairwiseMetricPromptTemplate.get_default_pairwise_instruction
    
    
    get_default_pairwise_instruction() -> str

Returns the default instruction for the metric prompt template.

See more: [vertexai.evaluation.PairwiseMetricPromptTemplate.get_default_pairwise_instruction](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.PairwiseMetricPromptTemplate#vertexai_evaluation_PairwiseMetricPromptTemplate_get_default_pairwise_instruction)

### vertexai.evaluation.PointwiseMetric
    
    
    PointwiseMetric(
        *,
        metric: str,
        metric_prompt_template: typing.Union[
            vertexai.evaluation.metrics.metric_prompt_template.PointwiseMetricPromptTemplate,
            str,
        ]
    )

Initializes a pointwise evaluation metric.

See more: [vertexai.evaluation.PointwiseMetric](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.PointwiseMetric#vertexai_evaluation_PointwiseMetric_PointwiseMetric)

### vertexai.evaluation.PointwiseMetricPromptTemplate
    
    
    PointwiseMetricPromptTemplate(
        *,
        criteria: typing.Dict[str, str],
        rating_rubric: typing.Dict[str, str],
        input_variables: typing.Optional[typing.List[str]] = None,
        instruction: typing.Optional[str] = None,
        metric_definition: typing.Optional[str] = None,
        evaluation_steps: typing.Optional[typing.Dict[str, str]] = None,
        few_shot_examples: typing.Optional[typing.List[str]] = None
    )

Initializes a pointwise metric prompt template.

See more: [vertexai.evaluation.PointwiseMetricPromptTemplate](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.PointwiseMetricPromptTemplate#vertexai_evaluation_PointwiseMetricPromptTemplate_PointwiseMetricPromptTemplate)

### vertexai.evaluation.PointwiseMetricPromptTemplate.__str__
    
    
    __str__()

Serializes the pointwise metric prompt template to a string.

See more: [vertexai.evaluation.PointwiseMetricPromptTemplate.**str**](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.PointwiseMetricPromptTemplate#vertexai_evaluation_PointwiseMetricPromptTemplate___str__)

### vertexai.evaluation.PointwiseMetricPromptTemplate.assemble
    
    
    assemble(**kwargs) -> vertexai.evaluation.prompt_template.PromptTemplate

Replaces only the provided variables in the template with specific values.

See more: [vertexai.evaluation.PointwiseMetricPromptTemplate.assemble](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.PointwiseMetricPromptTemplate#vertexai_evaluation_PointwiseMetricPromptTemplate_assemble)

### vertexai.evaluation.PointwiseMetricPromptTemplate.get_default_pointwise_evaluation_steps
    
    
    get_default_pointwise_evaluation_steps() -> typing.Dict[str, str]

Returns the default evaluation steps for the metric prompt template.

See more: [vertexai.evaluation.PointwiseMetricPromptTemplate.get_default_pointwise_evaluation_steps](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.PointwiseMetricPromptTemplate#vertexai_evaluation_PointwiseMetricPromptTemplate_get_default_pointwise_evaluation_steps)

### vertexai.evaluation.PointwiseMetricPromptTemplate.get_default_pointwise_instruction
    
    
    get_default_pointwise_instruction() -> str

Returns the default instruction for the metric prompt template.

See more: [vertexai.evaluation.PointwiseMetricPromptTemplate.get_default_pointwise_instruction](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.PointwiseMetricPromptTemplate#vertexai_evaluation_PointwiseMetricPromptTemplate_get_default_pointwise_instruction)

### vertexai.evaluation.PromptTemplate
    
    
    PromptTemplate(template: str)

Initializes the PromptTemplate with a given template.

See more: [vertexai.evaluation.PromptTemplate](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.PromptTemplate#vertexai_evaluation_PromptTemplate_PromptTemplate)

### vertexai.evaluation.PromptTemplate.__repr__
    
    
    __repr__() -> str

Returns a string representation of the PromptTemplate.

See more: [vertexai.evaluation.PromptTemplate.**repr**](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.PromptTemplate#vertexai_evaluation_PromptTemplate___repr__)

### vertexai.evaluation.PromptTemplate.__str__
    
    
    __str__() -> str

Returns the template string.

See more: [vertexai.evaluation.PromptTemplate.**str**](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.PromptTemplate#vertexai_evaluation_PromptTemplate___str__)

### vertexai.evaluation.PromptTemplate.assemble
    
    
    assemble(**kwargs) -> vertexai.evaluation.prompt_template.PromptTemplate

Replaces only the provided variables in the template with specific values.

See more: [vertexai.evaluation.PromptTemplate.assemble](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.PromptTemplate#vertexai_evaluation_PromptTemplate_assemble)

### vertexai.evaluation.Rouge
    
    
    Rouge(
        *,
        rouge_type: typing.Literal[
            "rouge1",
            "rouge2",
            "rouge3",
            "rouge4",
            "rouge5",
            "rouge6",
            "rouge7",
            "rouge8",
            "rouge9",
            "rougeL",
            "rougeLsum",
        ],
        use_stemmer: bool = False,
        split_summaries: bool = False
    )

Initializes the ROUGE metric.

See more: [vertexai.evaluation.Rouge](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.evaluation.Rouge#vertexai_evaluation_Rouge_Rouge)

### vertexai.generative_models.ChatSession.send_message

Generates content.

See more: [vertexai.generative_models.ChatSession.send_message](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.ChatSession#vertexai_generative_models_ChatSession_send_message)

### vertexai.generative_models.ChatSession.send_message_async

Generates content asynchronously.

See more: [vertexai.generative_models.ChatSession.send_message_async](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.ChatSession#vertexai_generative_models_ChatSession_send_message_async)

### vertexai.generative_models.FunctionDeclaration
    
    
    FunctionDeclaration(
        *,
        name: str,
        parameters: typing.Dict[str, typing.Any],
        description: typing.Optional[str] = None,
        response: typing.Optional[typing.Dict[str, typing.Any]] = None
    )

Constructs a FunctionDeclaration.

See more: [vertexai.generative_models.FunctionDeclaration](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.FunctionDeclaration#vertexai_generative_models_FunctionDeclaration_FunctionDeclaration)

### vertexai.generative_models.GenerationConfig
    
    
    GenerationConfig(
        *,
        temperature: typing.Optional[float] = None,
        top_p: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        candidate_count: typing.Optional[int] = None,
        max_output_tokens: typing.Optional[int] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None,
        presence_penalty: typing.Optional[float] = None,
        frequency_penalty: typing.Optional[float] = None,
        response_mime_type: typing.Optional[str] = None,
        response_schema: typing.Optional[typing.Dict[str, typing.Any]] = None,
        seed: typing.Optional[int] = None,
        audio_timestamp: typing.Optional[bool] = None,
        routing_config: typing.Optional[RoutingConfig] = None,
        logprobs: typing.Optional[int] = None,
        response_logprobs: typing.Optional[bool] = None,
        response_modalities: typing.Optional[typing.List[GenerationConfig.Modality]] = None,
        model_config: typing.Optional[GenerationConfig.ModelConfig] = None
    )

Constructs a GenerationConfig object.

See more: [vertexai.generative_models.GenerationConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.GenerationConfig#vertexai_generative_models_GenerationConfig_GenerationConfig)

### vertexai.generative_models.GenerationConfig.ModelConfig.__delattr__
    
    
    __delattr__(key)

Delete the value on the given field.

See more: [vertexai.generative_models.GenerationConfig.ModelConfig.**delattr**](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.GenerationConfig.ModelConfig#vertexai_generative_models_GenerationConfig_ModelConfig___delattr__)

### vertexai.generative_models.GenerationConfig.ModelConfig.__eq__
    
    
    __eq__(other)

Return True if the messages are equal, False otherwise.

See more: [vertexai.generative_models.GenerationConfig.ModelConfig.**eq**](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.GenerationConfig.ModelConfig#vertexai_generative_models_GenerationConfig_ModelConfig___eq__)

### vertexai.generative_models.GenerationConfig.ModelConfig.__ne__
    
    
    __ne__(other)

Return True if the messages are unequal, False otherwise.

See more: [vertexai.generative_models.GenerationConfig.ModelConfig.**ne**](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.GenerationConfig.ModelConfig#vertexai_generative_models_GenerationConfig_ModelConfig___ne__)

### vertexai.generative_models.GenerationConfig.ModelConfig.__setattr__
    
    
    __setattr__(key, value)

Set the value on the given field.

See more: [vertexai.generative_models.GenerationConfig.ModelConfig.**setattr**](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.GenerationConfig.ModelConfig#vertexai_generative_models_GenerationConfig_ModelConfig___setattr__)

### vertexai.generative_models.GenerationConfig.RoutingConfig.AutoRoutingMode
    
    
    AutoRoutingMode(
        *,
        model_routing_preference: google.cloud.aiplatform_v1beta1.types.content.GenerationConfig.RoutingConfig.AutoRoutingMode.ModelRoutingPreference
    )

AutoRouingMode constructor .

See more: [vertexai.generative_models.GenerationConfig.RoutingConfig.AutoRoutingMode](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.GenerationConfig.RoutingConfig.AutoRoutingMode#vertexai_generative_models_GenerationConfig_RoutingConfig_AutoRoutingMode_AutoRoutingMode)

### vertexai.generative_models.GenerationConfig.RoutingConfig.ManualRoutingMode
    
    
    ManualRoutingMode(*, model_name: str)

ManualRoutingMode constructor .

See more: [vertexai.generative_models.GenerationConfig.RoutingConfig.ManualRoutingMode](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.GenerationConfig.RoutingConfig.ManualRoutingMode#vertexai_generative_models_GenerationConfig_RoutingConfig_ManualRoutingMode_ManualRoutingMode)

### vertexai.generative_models.GenerativeModel.compute_tokens
    
    
    compute_tokens(
        contents: ContentsType,
    ) -> google.cloud.aiplatform_v1beta1.types.llm_utility_service.ComputeTokensResponse

Computes tokens.

See more: [vertexai.generative_models.GenerativeModel.compute_tokens](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.GenerativeModel#vertexai_generative_models_GenerativeModel_compute_tokens)

### vertexai.generative_models.GenerativeModel.compute_tokens_async
    
    
    compute_tokens_async(
        contents: ContentsType,
    ) -> google.cloud.aiplatform_v1beta1.types.llm_utility_service.ComputeTokensResponse

Computes tokens asynchronously.

See more: [vertexai.generative_models.GenerativeModel.compute_tokens_async](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.GenerativeModel#vertexai_generative_models_GenerativeModel_compute_tokens_async)

### vertexai.generative_models.GenerativeModel.count_tokens
    
    
    count_tokens(
        contents: ContentsType,
        *,
        tools: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Tool]
        ] = None
    ) -> google.cloud.aiplatform_v1beta1.types.prediction_service.CountTokensResponse

Counts tokens.

See more: [vertexai.generative_models.GenerativeModel.count_tokens](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.GenerativeModel#vertexai_generative_models_GenerativeModel_count_tokens)

### vertexai.generative_models.GenerativeModel.count_tokens_async
    
    
    count_tokens_async(
        contents: ContentsType,
        *,
        tools: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Tool]
        ] = None
    ) -> google.cloud.aiplatform_v1beta1.types.prediction_service.CountTokensResponse

Counts tokens asynchronously.

See more: [vertexai.generative_models.GenerativeModel.count_tokens_async](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.GenerativeModel#vertexai_generative_models_GenerativeModel_count_tokens_async)

### vertexai.generative_models.GenerativeModel.from_cached_content
    
    
    from_cached_content(
        cached_content: typing.Union[str, CachedContent],
        *,
        generation_config: typing.Optional[GenerationConfigType] = None,
        safety_settings: typing.Optional[SafetySettingsType] = None
    ) -> _GenerativeModel

Creates a model from cached content.

See more: [vertexai.generative_models.GenerativeModel.from_cached_content](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.GenerativeModel#vertexai_generative_models_GenerativeModel_from_cached_content)

### vertexai.generative_models.GenerativeModel.generate_content
    
    
    generate_content(
        contents: ContentsType,
        *,
        generation_config: typing.Optional[GenerationConfigType] = None,
        safety_settings: typing.Optional[SafetySettingsType] = None,
        tools: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Tool]
        ] = None,
        tool_config: typing.Optional[
            vertexai.generative_models._generative_models.ToolConfig
        ] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        stream: bool = False
    ) -> typing.Union[
        vertexai.generative_models._generative_models.GenerationResponse,
        typing.Iterable[vertexai.generative_models._generative_models.GenerationResponse],
    ]

Generates content.

See more: [vertexai.generative_models.GenerativeModel.generate_content](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.GenerativeModel#vertexai_generative_models_GenerativeModel_generate_content)

### vertexai.generative_models.GenerativeModel.generate_content_async
    
    
    generate_content_async(
        contents: ContentsType,
        *,
        generation_config: typing.Optional[GenerationConfigType] = None,
        safety_settings: typing.Optional[SafetySettingsType] = None,
        tools: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Tool]
        ] = None,
        tool_config: typing.Optional[
            vertexai.generative_models._generative_models.ToolConfig
        ] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        stream: bool = False
    ) -> typing.Union[
        vertexai.generative_models._generative_models.GenerationResponse,
        typing.AsyncIterable[
            vertexai.generative_models._generative_models.GenerationResponse
        ],
    ]

Generates content asynchronously.

See more: [vertexai.generative_models.GenerativeModel.generate_content_async](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.GenerativeModel#vertexai_generative_models_GenerativeModel_generate_content_async)

### vertexai.generative_models.GenerativeModel.start_chat
    
    
    start_chat(
        *,
        history: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Content]
        ] = None,
        response_validation: bool = True
    ) -> vertexai.generative_models._generative_models.ChatSession

Creates a stateful chat session.

See more: [vertexai.generative_models.GenerativeModel.start_chat](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.GenerativeModel#vertexai_generative_models_GenerativeModel_start_chat)

### vertexai.generative_models.Image.from_bytes
    
    
    from_bytes(data: bytes) -> vertexai.generative_models._generative_models.Image

Loads image from image bytes.

See more: [vertexai.generative_models.Image.from_bytes](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.Image#vertexai_generative_models_Image_from_bytes)

### vertexai.generative_models.Image.load_from_file
    
    
    load_from_file(
        location: str,
    ) -> vertexai.generative_models._generative_models.Image

Loads image from file.

See more: [vertexai.generative_models.Image.load_from_file](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.Image#vertexai_generative_models_Image_load_from_file)

### vertexai.generative_models.ResponseValidationError.with_traceback


Exception.with_traceback(tb) -- set self.**traceback** to tb and return self.

See more: [vertexai.generative_models.ResponseValidationError.with_traceback](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.ResponseValidationError#vertexai_generative_models_ResponseValidationError_with_traceback)

### vertexai.generative_models.SafetySetting
    
    
    SafetySetting(
        *,
        category: google.cloud.aiplatform_v1beta1.types.content.HarmCategory,
        threshold: google.cloud.aiplatform_v1beta1.types.content.SafetySetting.HarmBlockThreshold,
        method: typing.Optional[
            google.cloud.aiplatform_v1beta1.types.content.SafetySetting.HarmBlockMethod
        ] = None
    )

Safety settings.

See more: [vertexai.generative_models.SafetySetting](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.SafetySetting#vertexai_generative_models_SafetySetting_SafetySetting)

### vertexai.generative_models.grounding.DynamicRetrievalConfig
    
    
    DynamicRetrievalConfig(
        mode: google.cloud.aiplatform_v1beta1.types.tool.DynamicRetrievalConfig.Mode = Mode.MODE_UNSPECIFIED,
        dynamic_threshold: typing.Optional[float] = None,
    )

Initializes a DynamicRetrievalConfig.

See more: [vertexai.generative_models.grounding.DynamicRetrievalConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.grounding.DynamicRetrievalConfig#vertexai_generative_models_grounding_DynamicRetrievalConfig_DynamicRetrievalConfig)

### vertexai.generative_models.grounding.GoogleSearchRetrieval
    
    
    GoogleSearchRetrieval(
        dynamic_retrieval_config: typing.Optional[
            vertexai.generative_models._generative_models.grounding.DynamicRetrievalConfig
        ] = None,
    )

Initializes a Google Search Retrieval tool.

See more: [vertexai.generative_models.grounding.GoogleSearchRetrieval](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.grounding.GoogleSearchRetrieval#vertexai_generative_models_grounding_GoogleSearchRetrieval_GoogleSearchRetrieval)

### vertexai.generative_models.grounding.Retrieval
    
    
    Retrieval(
        source: vertexai.generative_models._generative_models.grounding.VertexAISearch,
        disable_attribution: typing.Optional[bool] = None,
    )

Initializes a Retrieval tool.

See more: [vertexai.generative_models.grounding.Retrieval](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.grounding.Retrieval#vertexai_generative_models_grounding_Retrieval_Retrieval)

### vertexai.generative_models.grounding.VertexAISearch
    
    
    VertexAISearch(
        datastore: str,
        *,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None
    )

Initializes a Vertex AI Search tool.

See more: [vertexai.generative_models.grounding.VertexAISearch](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.generative_models.grounding.VertexAISearch#vertexai_generative_models_grounding_VertexAISearch_VertexAISearch)

### vertexai.language_models.ChatModel
    
    
    ChatModel(model_id: str, endpoint_name: typing.Optional[str] = None)

Creates a LanguageModel.

See more: [vertexai.language_models.ChatModel](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.ChatModel#vertexai_language_models_ChatModel_ChatModel)

### vertexai.language_models.ChatModel.from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

See more: [vertexai.language_models.ChatModel.from_pretrained](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.ChatModel#vertexai_language_models_ChatModel_from_pretrained)

### vertexai.language_models.ChatModel.get_tuned_model
    
    
    get_tuned_model(
        tuned_model_name: str,
    ) -> vertexai.language_models._language_models._LanguageModel

Loads the specified tuned language model.

See more: [vertexai.language_models.ChatModel.get_tuned_model](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.ChatModel#vertexai_language_models_ChatModel_get_tuned_model)

### vertexai.language_models.ChatModel.list_tuned_model_names
    
    
    list_tuned_model_names() -> typing.Sequence[str]

Lists the names of tuned models.

See more: [vertexai.language_models.ChatModel.list_tuned_model_names](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.ChatModel#vertexai_language_models_ChatModel_list_tuned_model_names)

### vertexai.language_models.ChatModel.start_chat
    
    
    start_chat(
        *,
        context: typing.Optional[str] = None,
        examples: typing.Optional[
            typing.List[vertexai.language_models.InputOutputTextPair]
        ] = None,
        max_output_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        top_p: typing.Optional[float] = None,
        message_history: typing.Optional[
            typing.List[vertexai.language_models.ChatMessage]
        ] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None
    ) -> vertexai.language_models.ChatSession

Starts a chat session with the model.

See more: [vertexai.language_models.ChatModel.start_chat](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.ChatModel#vertexai_language_models_ChatModel_start_chat)

### vertexai.language_models.ChatModel.tune_model
    
    
    tune_model(
        training_data: typing.Union[str, pandas.core.frame.DataFrame],
        *,
        train_steps: typing.Optional[int] = None,
        learning_rate_multiplier: typing.Optional[float] = None,
        tuning_job_location: typing.Optional[str] = None,
        tuned_model_location: typing.Optional[str] = None,
        model_display_name: typing.Optional[str] = None,
        default_context: typing.Optional[str] = None,
        accelerator_type: typing.Optional[typing.Literal["TPU", "GPU"]] = None,
        tuning_evaluation_spec: typing.Optional[
            vertexai.language_models.TuningEvaluationSpec
        ] = None
    ) -> vertexai.language_models._language_models._LanguageModelTuningJob

Tunes a model based on training data.

See more: [vertexai.language_models.ChatModel.tune_model](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.ChatModel#vertexai_language_models_ChatModel_tune_model)

### vertexai.language_models.ChatModel.tune_model_rlhf
    
    
    tune_model_rlhf(
        *,
        prompt_data: typing.Union[str, pandas.core.frame.DataFrame],
        preference_data: typing.Union[str, pandas.core.frame.DataFrame],
        model_display_name: typing.Optional[str] = None,
        prompt_sequence_length: typing.Optional[int] = None,
        target_sequence_length: typing.Optional[int] = None,
        reward_model_learning_rate_multiplier: typing.Optional[float] = None,
        reinforcement_learning_rate_multiplier: typing.Optional[float] = None,
        reward_model_train_steps: typing.Optional[int] = None,
        reinforcement_learning_train_steps: typing.Optional[int] = None,
        kl_coeff: typing.Optional[float] = None,
        default_context: typing.Optional[str] = None,
        tuning_job_location: typing.Optional[str] = None,
        accelerator_type: typing.Optional[typing.Literal["TPU", "GPU"]] = None,
        tuning_evaluation_spec: typing.Optional[
            vertexai.language_models.TuningEvaluationSpec
        ] = None
    ) -> vertexai.language_models._language_models._LanguageModelTuningJob

Tunes a model using reinforcement learning from human feedback.

See more: [vertexai.language_models.ChatModel.tune_model_rlhf](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.ChatModel#vertexai_language_models_ChatModel_tune_model_rlhf)

### vertexai.language_models.ChatSession.send_message
    
    
    send_message(
        message: str,
        *,
        max_output_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        top_p: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None,
        candidate_count: typing.Optional[int] = None,
        grounding_source: typing.Optional[
            typing.Union[
                vertexai.language_models._language_models.WebSearch,
                vertexai.language_models._language_models.VertexAISearch,
                vertexai.language_models._language_models.InlineContext,
            ]
        ] = None
    ) -> vertexai.language_models.MultiCandidateTextGenerationResponse

Sends message to the language model and gets a response.

See more: [vertexai.language_models.ChatSession.send_message](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.ChatSession#vertexai_language_models_ChatSession_send_message)

### vertexai.language_models.ChatSession.send_message_async
    
    
    send_message_async(
        message: str,
        *,
        max_output_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        top_p: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None,
        candidate_count: typing.Optional[int] = None,
        grounding_source: typing.Optional[
            typing.Union[
                vertexai.language_models._language_models.WebSearch,
                vertexai.language_models._language_models.VertexAISearch,
                vertexai.language_models._language_models.InlineContext,
            ]
        ] = None
    ) -> vertexai.language_models.MultiCandidateTextGenerationResponse

Asynchronously sends message to the language model and gets a response.

See more: [vertexai.language_models.ChatSession.send_message_async](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.ChatSession#vertexai_language_models_ChatSession_send_message_async)

### vertexai.language_models.ChatSession.send_message_streaming
    
    
    send_message_streaming(
        message: str,
        *,
        max_output_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        top_p: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None
    ) -> typing.Iterator[vertexai.language_models.TextGenerationResponse]

Sends message to the language model and gets a streamed response.

See more: [vertexai.language_models.ChatSession.send_message_streaming](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.ChatSession#vertexai_language_models_ChatSession_send_message_streaming)

### vertexai.language_models.ChatSession.send_message_streaming_async
    
    
    send_message_streaming_async(
        message: str,
        *,
        max_output_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        top_p: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None
    ) -> typing.AsyncIterator[vertexai.language_models.TextGenerationResponse]

Asynchronously sends message to the language model and gets a streamed response.

See more: [vertexai.language_models.ChatSession.send_message_streaming_async](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.ChatSession#vertexai_language_models_ChatSession_send_message_streaming_async)

### vertexai.language_models.CodeChatModel
    
    
    CodeChatModel(model_id: str, endpoint_name: typing.Optional[str] = None)

Creates a LanguageModel.

See more: [vertexai.language_models.CodeChatModel](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.CodeChatModel#vertexai_language_models_CodeChatModel_CodeChatModel)

### vertexai.language_models.CodeChatModel.from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

See more: [vertexai.language_models.CodeChatModel.from_pretrained](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.CodeChatModel#vertexai_language_models_CodeChatModel_from_pretrained)

### vertexai.language_models.CodeChatModel.get_tuned_model
    
    
    get_tuned_model(
        tuned_model_name: str,
    ) -> vertexai.language_models._language_models._LanguageModel

Loads the specified tuned language model.

See more: [vertexai.language_models.CodeChatModel.get_tuned_model](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.CodeChatModel#vertexai_language_models_CodeChatModel_get_tuned_model)

### vertexai.language_models.CodeChatModel.list_tuned_model_names
    
    
    list_tuned_model_names() -> typing.Sequence[str]

Lists the names of tuned models.

See more: [vertexai.language_models.CodeChatModel.list_tuned_model_names](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.CodeChatModel#vertexai_language_models_CodeChatModel_list_tuned_model_names)

### vertexai.language_models.CodeChatModel.start_chat
    
    
    start_chat(
        *,
        context: typing.Optional[str] = None,
        max_output_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[float] = None,
        message_history: typing.Optional[
            typing.List[vertexai.language_models.ChatMessage]
        ] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None
    ) -> vertexai.language_models.CodeChatSession

Starts a chat session with the code chat model.

See more: [vertexai.language_models.CodeChatModel.start_chat](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.CodeChatModel#vertexai_language_models_CodeChatModel_start_chat)

### vertexai.language_models.CodeChatModel.tune_model
    
    
    tune_model(
        training_data: typing.Union[str, pandas.core.frame.DataFrame],
        *,
        train_steps: typing.Optional[int] = None,
        learning_rate_multiplier: typing.Optional[float] = None,
        tuning_job_location: typing.Optional[str] = None,
        tuned_model_location: typing.Optional[str] = None,
        model_display_name: typing.Optional[str] = None,
        default_context: typing.Optional[str] = None,
        accelerator_type: typing.Optional[typing.Literal["TPU", "GPU"]] = None,
        tuning_evaluation_spec: typing.Optional[
            vertexai.language_models.TuningEvaluationSpec
        ] = None
    ) -> vertexai.language_models._language_models._LanguageModelTuningJob

Tunes a model based on training data.

See more: [vertexai.language_models.CodeChatModel.tune_model](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.CodeChatModel#vertexai_language_models_CodeChatModel_tune_model)

### vertexai.language_models.CodeChatSession.send_message
    
    
    send_message(
        message: str,
        *,
        max_output_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None,
        candidate_count: typing.Optional[int] = None
    ) -> vertexai.language_models.MultiCandidateTextGenerationResponse

Sends message to the code chat model and gets a response.

See more: [vertexai.language_models.CodeChatSession.send_message](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.CodeChatSession#vertexai_language_models_CodeChatSession_send_message)

### vertexai.language_models.CodeChatSession.send_message_async
    
    
    send_message_async(
        message: str,
        *,
        max_output_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[float] = None,
        candidate_count: typing.Optional[int] = None
    ) -> vertexai.language_models.MultiCandidateTextGenerationResponse

Asynchronously sends message to the code chat model and gets a response.

See more: [vertexai.language_models.CodeChatSession.send_message_async](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.CodeChatSession#vertexai_language_models_CodeChatSession_send_message_async)

### vertexai.language_models.CodeChatSession.send_message_streaming
    
    
    send_message_streaming(
        message: str,
        *,
        max_output_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None
    ) -> typing.Iterator[vertexai.language_models.TextGenerationResponse]

Sends message to the language model and gets a streamed response.

See more: [vertexai.language_models.CodeChatSession.send_message_streaming](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.CodeChatSession#vertexai_language_models_CodeChatSession_send_message_streaming)

### vertexai.language_models.CodeChatSession.send_message_streaming_async
    
    
    send_message_streaming_async(
        message: str,
        *,
        max_output_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None
    ) -> typing.AsyncIterator[vertexai.language_models.TextGenerationResponse]

Asynchronously sends message to the language model and gets a streamed response.

See more: [vertexai.language_models.CodeChatSession.send_message_streaming_async](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.CodeChatSession#vertexai_language_models_CodeChatSession_send_message_streaming_async)

### vertexai.language_models.CodeGenerationModel.batch_predict
    
    
    batch_predict(
        *,
        dataset: typing.Union[str, typing.List[str]],
        destination_uri_prefix: str,
        model_parameters: typing.Optional[typing.Dict] = None
    ) -> google.cloud.aiplatform.jobs.BatchPredictionJob

Starts a batch prediction job with the model.

See more: [vertexai.language_models.CodeGenerationModel.batch_predict](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.CodeGenerationModel#vertexai_language_models_CodeGenerationModel_batch_predict)

### vertexai.language_models.CodeGenerationModel.from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

See more: [vertexai.language_models.CodeGenerationModel.from_pretrained](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.CodeGenerationModel#vertexai_language_models_CodeGenerationModel_from_pretrained)

### vertexai.language_models.CodeGenerationModel.get_tuned_model
    
    
    get_tuned_model(
        tuned_model_name: str,
    ) -> vertexai.language_models._language_models._LanguageModel

Loads the specified tuned language model.

See more: [vertexai.language_models.CodeGenerationModel.get_tuned_model](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.CodeGenerationModel#vertexai_language_models_CodeGenerationModel_get_tuned_model)

### vertexai.language_models.CodeGenerationModel.list_tuned_model_names
    
    
    list_tuned_model_names() -> typing.Sequence[str]

Lists the names of tuned models.

See more: [vertexai.language_models.CodeGenerationModel.list_tuned_model_names](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.CodeGenerationModel#vertexai_language_models_CodeGenerationModel_list_tuned_model_names)

### vertexai.language_models.CodeGenerationModel.predict
    
    
    predict(
        prefix: str,
        suffix: typing.Optional[str] = None,
        *,
        max_output_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None,
        candidate_count: typing.Optional[int] = None
    ) -> vertexai.language_models.TextGenerationResponse

Gets model response for a single prompt.

See more: [vertexai.language_models.CodeGenerationModel.predict](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.CodeGenerationModel#vertexai_language_models_CodeGenerationModel_predict)

### vertexai.language_models.CodeGenerationModel.predict_async
    
    
    predict_async(
        prefix: str,
        suffix: typing.Optional[str] = None,
        *,
        max_output_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None,
        candidate_count: typing.Optional[int] = None
    ) -> vertexai.language_models.TextGenerationResponse

Asynchronously gets model response for a single prompt.

See more: [vertexai.language_models.CodeGenerationModel.predict_async](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.CodeGenerationModel#vertexai_language_models_CodeGenerationModel_predict_async)

### vertexai.language_models.CodeGenerationModel.predict_streaming
    
    
    predict_streaming(
        prefix: str,
        suffix: typing.Optional[str] = None,
        *,
        max_output_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None
    ) -> typing.Iterator[vertexai.language_models.TextGenerationResponse]

Predicts the code based on previous code.

See more: [vertexai.language_models.CodeGenerationModel.predict_streaming](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.CodeGenerationModel#vertexai_language_models_CodeGenerationModel_predict_streaming)

### vertexai.language_models.CodeGenerationModel.predict_streaming_async
    
    
    predict_streaming_async(
        prefix: str,
        suffix: typing.Optional[str] = None,
        *,
        max_output_tokens: typing.Optional[int] = None,
        temperature: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None
    ) -> typing.AsyncIterator[vertexai.language_models.TextGenerationResponse]

Asynchronously predicts the code based on previous code.

See more: [vertexai.language_models.CodeGenerationModel.predict_streaming_async](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.CodeGenerationModel#vertexai_language_models_CodeGenerationModel_predict_streaming_async)

### vertexai.language_models.CodeGenerationModel.tune_model
    
    
    tune_model(
        training_data: typing.Union[str, pandas.core.frame.DataFrame],
        *,
        train_steps: typing.Optional[int] = None,
        learning_rate_multiplier: typing.Optional[float] = None,
        tuning_job_location: typing.Optional[str] = None,
        tuned_model_location: typing.Optional[str] = None,
        model_display_name: typing.Optional[str] = None,
        tuning_evaluation_spec: typing.Optional[
            vertexai.language_models.TuningEvaluationSpec
        ] = None,
        accelerator_type: typing.Optional[typing.Literal["TPU", "GPU"]] = None,
        max_context_length: typing.Optional[str] = None
    ) -> vertexai.language_models._language_models._LanguageModelTuningJob

Tunes a model based on training data.

See more: [vertexai.language_models.CodeGenerationModel.tune_model](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.CodeGenerationModel#vertexai_language_models_CodeGenerationModel_tune_model)

### vertexai.language_models.TextEmbeddingModel.batch_predict
    
    
    batch_predict(
        *,
        dataset: typing.Union[str, typing.List[str]],
        destination_uri_prefix: str,
        model_parameters: typing.Optional[typing.Dict] = None
    ) -> google.cloud.aiplatform.jobs.BatchPredictionJob

Starts a batch prediction job with the model.

See more: [vertexai.language_models.TextEmbeddingModel.batch_predict](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.TextEmbeddingModel#vertexai_language_models_TextEmbeddingModel_batch_predict)

### vertexai.language_models.TextEmbeddingModel.count_tokens
    
    
    count_tokens(
        prompts: typing.List[str],
    ) -> vertexai.preview.language_models.CountTokensResponse

Counts the tokens and billable characters for a given prompt.

See more: [vertexai.language_models.TextEmbeddingModel.count_tokens](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.TextEmbeddingModel#vertexai_language_models_TextEmbeddingModel_count_tokens)

### vertexai.language_models.TextEmbeddingModel.deploy_tuned_model
    
    
    deploy_tuned_model(
        tuned_model_name: str,
        machine_type: typing.Optional[str] = None,
        accelerator: typing.Optional[str] = None,
        accelerator_count: typing.Optional[int] = None,
    ) -> vertexai.language_models._language_models._LanguageModel

Loads the specified tuned language model.

See more: [vertexai.language_models.TextEmbeddingModel.deploy_tuned_model](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.TextEmbeddingModel#vertexai_language_models_TextEmbeddingModel_deploy_tuned_model)

### vertexai.language_models.TextEmbeddingModel.from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

See more: [vertexai.language_models.TextEmbeddingModel.from_pretrained](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.TextEmbeddingModel#vertexai_language_models_TextEmbeddingModel_from_pretrained)

### vertexai.language_models.TextEmbeddingModel.get_embeddings
    
    
    get_embeddings(
        texts: typing.List[typing.Union[str, vertexai.language_models.TextEmbeddingInput]],
        *,
        auto_truncate: bool = True,
        output_dimensionality: typing.Optional[int] = None
    ) -> typing.List[vertexai.language_models.TextEmbedding]

Calculates embeddings for the given texts.

See more: [vertexai.language_models.TextEmbeddingModel.get_embeddings](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.TextEmbeddingModel#vertexai_language_models_TextEmbeddingModel_get_embeddings)

### vertexai.language_models.TextEmbeddingModel.get_embeddings_async
    
    
    get_embeddings_async(
        texts: typing.List[typing.Union[str, vertexai.language_models.TextEmbeddingInput]],
        *,
        auto_truncate: bool = True,
        output_dimensionality: typing.Optional[int] = None
    ) -> typing.List[vertexai.language_models.TextEmbedding]

Asynchronously calculates embeddings for the given texts.

See more: [vertexai.language_models.TextEmbeddingModel.get_embeddings_async](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.TextEmbeddingModel#vertexai_language_models_TextEmbeddingModel_get_embeddings_async)

### vertexai.language_models.TextEmbeddingModel.get_tuned_model
    
    
    get_tuned_model(*args, **kwargs)

Loads the specified tuned language model.

See more: [vertexai.language_models.TextEmbeddingModel.get_tuned_model](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.TextEmbeddingModel#vertexai_language_models_TextEmbeddingModel_get_tuned_model)

### vertexai.language_models.TextEmbeddingModel.list_tuned_model_names
    
    
    list_tuned_model_names() -> typing.Sequence[str]

Lists the names of tuned models.

See more: [vertexai.language_models.TextEmbeddingModel.list_tuned_model_names](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.TextEmbeddingModel#vertexai_language_models_TextEmbeddingModel_list_tuned_model_names)

### vertexai.language_models.TextEmbeddingModel.tune_model
    
    
    tune_model(
        *,
        training_data: typing.Optional[str] = None,
        corpus_data: typing.Optional[str] = None,
        queries_data: typing.Optional[str] = None,
        test_data: typing.Optional[str] = None,
        validation_data: typing.Optional[str] = None,
        batch_size: typing.Optional[int] = None,
        train_steps: typing.Optional[int] = None,
        tuned_model_location: typing.Optional[str] = None,
        model_display_name: typing.Optional[str] = None,
        task_type: typing.Optional[str] = None,
        machine_type: typing.Optional[str] = None,
        accelerator: typing.Optional[str] = None,
        accelerator_count: typing.Optional[int] = None,
        output_dimensionality: typing.Optional[int] = None,
        learning_rate_multiplier: typing.Optional[float] = None
    ) -> vertexai.language_models._language_models._TextEmbeddingModelTuningJob

Tunes a model based on training data.

See more: [vertexai.language_models.TextEmbeddingModel.tune_model](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.TextEmbeddingModel#vertexai_language_models_TextEmbeddingModel_tune_model)

### vertexai.language_models.TextGenerationModel.batch_predict
    
    
    batch_predict(
        *,
        dataset: typing.Union[str, typing.List[str]],
        destination_uri_prefix: str,
        model_parameters: typing.Optional[typing.Dict] = None
    ) -> google.cloud.aiplatform.jobs.BatchPredictionJob

Starts a batch prediction job with the model.

See more: [vertexai.language_models.TextGenerationModel.batch_predict](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.TextGenerationModel#vertexai_language_models_TextGenerationModel_batch_predict)

### vertexai.language_models.TextGenerationModel.from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

See more: [vertexai.language_models.TextGenerationModel.from_pretrained](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.TextGenerationModel#vertexai_language_models_TextGenerationModel_from_pretrained)

### vertexai.language_models.TextGenerationModel.get_tuned_model
    
    
    get_tuned_model(
        tuned_model_name: str,
    ) -> vertexai.language_models._language_models._LanguageModel

Loads the specified tuned language model.

See more: [vertexai.language_models.TextGenerationModel.get_tuned_model](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.TextGenerationModel#vertexai_language_models_TextGenerationModel_get_tuned_model)

### vertexai.language_models.TextGenerationModel.list_tuned_model_names
    
    
    list_tuned_model_names() -> typing.Sequence[str]

Lists the names of tuned models.

See more: [vertexai.language_models.TextGenerationModel.list_tuned_model_names](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.TextGenerationModel#vertexai_language_models_TextGenerationModel_list_tuned_model_names)

### vertexai.language_models.TextGenerationModel.predict
    
    
    predict(
        prompt: str,
        *,
        max_output_tokens: typing.Optional[int] = 128,
        temperature: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        top_p: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None,
        candidate_count: typing.Optional[int] = None,
        grounding_source: typing.Optional[
            typing.Union[
                vertexai.language_models._language_models.WebSearch,
                vertexai.language_models._language_models.VertexAISearch,
                vertexai.language_models._language_models.InlineContext,
            ]
        ] = None,
        logprobs: typing.Optional[int] = None,
        presence_penalty: typing.Optional[float] = None,
        frequency_penalty: typing.Optional[float] = None,
        logit_bias: typing.Optional[typing.Dict[str, float]] = None,
        seed: typing.Optional[int] = None
    ) -> vertexai.language_models.MultiCandidateTextGenerationResponse

Gets model response for a single prompt.

See more: [vertexai.language_models.TextGenerationModel.predict](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.TextGenerationModel#vertexai_language_models_TextGenerationModel_predict)

### vertexai.language_models.TextGenerationModel.predict_async
    
    
    predict_async(
        prompt: str,
        *,
        max_output_tokens: typing.Optional[int] = 128,
        temperature: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        top_p: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None,
        candidate_count: typing.Optional[int] = None,
        grounding_source: typing.Optional[
            typing.Union[
                vertexai.language_models._language_models.WebSearch,
                vertexai.language_models._language_models.VertexAISearch,
                vertexai.language_models._language_models.InlineContext,
            ]
        ] = None,
        logprobs: typing.Optional[int] = None,
        presence_penalty: typing.Optional[float] = None,
        frequency_penalty: typing.Optional[float] = None,
        logit_bias: typing.Optional[typing.Dict[str, float]] = None,
        seed: typing.Optional[int] = None
    ) -> vertexai.language_models.MultiCandidateTextGenerationResponse

Asynchronously gets model response for a single prompt.

See more: [vertexai.language_models.TextGenerationModel.predict_async](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.TextGenerationModel#vertexai_language_models_TextGenerationModel_predict_async)

### vertexai.language_models.TextGenerationModel.predict_streaming
    
    
    predict_streaming(
        prompt: str,
        *,
        max_output_tokens: int = 128,
        temperature: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        top_p: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None,
        logprobs: typing.Optional[int] = None,
        presence_penalty: typing.Optional[float] = None,
        frequency_penalty: typing.Optional[float] = None,
        logit_bias: typing.Optional[typing.Dict[str, float]] = None,
        seed: typing.Optional[int] = None
    ) -> typing.Iterator[vertexai.language_models.TextGenerationResponse]

Gets a streaming model response for a single prompt.

See more: [vertexai.language_models.TextGenerationModel.predict_streaming](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.TextGenerationModel#vertexai_language_models_TextGenerationModel_predict_streaming)

### vertexai.language_models.TextGenerationModel.predict_streaming_async
    
    
    predict_streaming_async(
        prompt: str,
        *,
        max_output_tokens: int = 128,
        temperature: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        top_p: typing.Optional[float] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None,
        logprobs: typing.Optional[int] = None,
        presence_penalty: typing.Optional[float] = None,
        frequency_penalty: typing.Optional[float] = None,
        logit_bias: typing.Optional[typing.Dict[str, float]] = None,
        seed: typing.Optional[int] = None
    ) -> typing.AsyncIterator[vertexai.language_models.TextGenerationResponse]

Asynchronously gets a streaming model response for a single prompt.

See more: [vertexai.language_models.TextGenerationModel.predict_streaming_async](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.TextGenerationModel#vertexai_language_models_TextGenerationModel_predict_streaming_async)

### vertexai.language_models.TextGenerationModel.tune_model
    
    
    tune_model(
        training_data: typing.Union[str, pandas.core.frame.DataFrame],
        *,
        train_steps: typing.Optional[int] = None,
        learning_rate_multiplier: typing.Optional[float] = None,
        tuning_job_location: typing.Optional[str] = None,
        tuned_model_location: typing.Optional[str] = None,
        model_display_name: typing.Optional[str] = None,
        tuning_evaluation_spec: typing.Optional[
            vertexai.language_models.TuningEvaluationSpec
        ] = None,
        accelerator_type: typing.Optional[typing.Literal["TPU", "GPU"]] = None,
        max_context_length: typing.Optional[str] = None
    ) -> vertexai.language_models._language_models._LanguageModelTuningJob

Tunes a model based on training data.

See more: [vertexai.language_models.TextGenerationModel.tune_model](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.TextGenerationModel#vertexai_language_models_TextGenerationModel_tune_model)

### vertexai.language_models.TextGenerationModel.tune_model_rlhf
    
    
    tune_model_rlhf(
        *,
        prompt_data: typing.Union[str, pandas.core.frame.DataFrame],
        preference_data: typing.Union[str, pandas.core.frame.DataFrame],
        model_display_name: typing.Optional[str] = None,
        prompt_sequence_length: typing.Optional[int] = None,
        target_sequence_length: typing.Optional[int] = None,
        reward_model_learning_rate_multiplier: typing.Optional[float] = None,
        reinforcement_learning_rate_multiplier: typing.Optional[float] = None,
        reward_model_train_steps: typing.Optional[int] = None,
        reinforcement_learning_train_steps: typing.Optional[int] = None,
        kl_coeff: typing.Optional[float] = None,
        default_context: typing.Optional[str] = None,
        tuning_job_location: typing.Optional[str] = None,
        accelerator_type: typing.Optional[typing.Literal["TPU", "GPU"]] = None,
        tuning_evaluation_spec: typing.Optional[
            vertexai.language_models.TuningEvaluationSpec
        ] = None
    ) -> vertexai.language_models._language_models._LanguageModelTuningJob

Tunes a model using reinforcement learning from human feedback.

See more: [vertexai.language_models.TextGenerationModel.tune_model_rlhf](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models.TextGenerationModel#vertexai_language_models_TextGenerationModel_tune_model_rlhf)

### vertexai.language_models._language_models._TunableModelMixin
    
    
    _TunableModelMixin(model_id: str, endpoint_name: typing.Optional[str] = None)

Creates a LanguageModel.

See more: [vertexai.language_models._language_models._TunableModelMixin](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models._language_models._TunableModelMixin#vertexai_language_models__language_models__TunableModelMixin__TunableModelMixin)

### vertexai.language_models._language_models._TunableModelMixin.tune_model
    
    
    tune_model(
        training_data: typing.Union[str, pandas.core.frame.DataFrame],
        *,
        corpus_data: typing.Optional[str] = None,
        queries_data: typing.Optional[str] = None,
        test_data: typing.Optional[str] = None,
        validation_data: typing.Optional[str] = None,
        batch_size: typing.Optional[int] = None,
        train_steps: typing.Optional[int] = None,
        learning_rate: typing.Optional[float] = None,
        learning_rate_multiplier: typing.Optional[float] = None,
        tuning_job_location: typing.Optional[str] = None,
        tuned_model_location: typing.Optional[str] = None,
        model_display_name: typing.Optional[str] = None,
        tuning_evaluation_spec: typing.Optional[
            vertexai.language_models.TuningEvaluationSpec
        ] = None,
        default_context: typing.Optional[str] = None,
        task_type: typing.Optional[str] = None,
        machine_type: typing.Optional[str] = None,
        accelerator: typing.Optional[str] = None,
        accelerator_count: typing.Optional[int] = None,
        accelerator_type: typing.Optional[typing.Literal["TPU", "GPU"]] = None,
        max_context_length: typing.Optional[str] = None,
        output_dimensionality: typing.Optional[int] = None
    ) -> vertexai.language_models._language_models._LanguageModelTuningJob

Tunes a model based on training data.

See more: [vertexai.language_models._language_models._TunableModelMixin.tune_model](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.language_models._language_models._TunableModelMixin#vertexai_language_models__language_models__TunableModelMixin_tune_model)

### vertexai.preview.generative_models.AutomaticFunctionCallingResponder
    
    
    AutomaticFunctionCallingResponder(max_automatic_function_calls: int = 1)

Initializes the responder.

See more: [vertexai.preview.generative_models.AutomaticFunctionCallingResponder](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.AutomaticFunctionCallingResponder#vertexai_preview_generative_models_AutomaticFunctionCallingResponder_AutomaticFunctionCallingResponder)

### vertexai.preview.generative_models.CallableFunctionDeclaration
    
    
    CallableFunctionDeclaration(
        name: str,
        function: typing.Callable[[...], typing.Any],
        parameters: typing.Dict[str, typing.Any],
        description: typing.Optional[str] = None,
    )

Constructs a FunctionDeclaration.

See more: [vertexai.preview.generative_models.CallableFunctionDeclaration](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.CallableFunctionDeclaration#vertexai_preview_generative_models_CallableFunctionDeclaration_CallableFunctionDeclaration)

### vertexai.preview.generative_models.CallableFunctionDeclaration.from_func
    
    
    from_func(
        func: typing.Callable[[...], typing.Any],
    ) -> vertexai.generative_models._generative_models.CallableFunctionDeclaration

Automatically creates a CallableFunctionDeclaration from a Python function.

See more: [vertexai.preview.generative_models.CallableFunctionDeclaration.from_func](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.CallableFunctionDeclaration#vertexai_preview_generative_models_CallableFunctionDeclaration_from_func)

### vertexai.preview.generative_models.ChatSession.send_message
    
    
    send_message(
        content: PartsType,
        *,
        generation_config: typing.Optional[GenerationConfigType] = None,
        safety_settings: typing.Optional[SafetySettingsType] = None,
        tools: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Tool]
        ] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        stream: bool = False
    ) -> typing.Union[
        vertexai.generative_models._generative_models.GenerationResponse,
        typing.Iterable[vertexai.generative_models._generative_models.GenerationResponse],
    ]

Generates content.

See more: [vertexai.preview.generative_models.ChatSession.send_message](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.ChatSession#vertexai_preview_generative_models_ChatSession_send_message)

### vertexai.preview.generative_models.ChatSession.send_message_async
    
    
    send_message_async(
        content: PartsType,
        *,
        generation_config: typing.Optional[GenerationConfigType] = None,
        safety_settings: typing.Optional[SafetySettingsType] = None,
        tools: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Tool]
        ] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        stream: bool = False
    ) -> typing.Union[
        typing.Awaitable[vertexai.generative_models._generative_models.GenerationResponse],
        typing.Awaitable[
            typing.AsyncIterable[
                vertexai.generative_models._generative_models.GenerationResponse
            ]
        ],
    ]

Generates content asynchronously.

See more: [vertexai.preview.generative_models.ChatSession.send_message_async](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.ChatSession#vertexai_preview_generative_models_ChatSession_send_message_async)

### vertexai.preview.generative_models.FunctionDeclaration
    
    
    FunctionDeclaration(
        *,
        name: str,
        parameters: typing.Dict[str, typing.Any],
        description: typing.Optional[str] = None,
        response: typing.Optional[typing.Dict[str, typing.Any]] = None
    )

Constructs a FunctionDeclaration.

See more: [vertexai.preview.generative_models.FunctionDeclaration](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.FunctionDeclaration#vertexai_preview_generative_models_FunctionDeclaration_FunctionDeclaration)

### vertexai.preview.generative_models.GenerationConfig
    
    
    GenerationConfig(
        *,
        temperature: typing.Optional[float] = None,
        top_p: typing.Optional[float] = None,
        top_k: typing.Optional[int] = None,
        candidate_count: typing.Optional[int] = None,
        max_output_tokens: typing.Optional[int] = None,
        stop_sequences: typing.Optional[typing.List[str]] = None,
        presence_penalty: typing.Optional[float] = None,
        frequency_penalty: typing.Optional[float] = None,
        response_mime_type: typing.Optional[str] = None,
        response_schema: typing.Optional[typing.Dict[str, typing.Any]] = None,
        seed: typing.Optional[int] = None,
        audio_timestamp: typing.Optional[bool] = None,
        routing_config: typing.Optional[RoutingConfig] = None,
        logprobs: typing.Optional[int] = None,
        response_logprobs: typing.Optional[bool] = None,
        response_modalities: typing.Optional[typing.List[GenerationConfig.Modality]] = None,
        model_config: typing.Optional[GenerationConfig.ModelConfig] = None
    )

Constructs a GenerationConfig object.

See more: [vertexai.preview.generative_models.GenerationConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.GenerationConfig#vertexai_preview_generative_models_GenerationConfig_GenerationConfig)

### vertexai.preview.generative_models.GenerationConfig.ModelConfig.__delattr__
    
    
    __delattr__(key)

Delete the value on the given field.

See more: [vertexai.preview.generative_models.GenerationConfig.ModelConfig.**delattr**](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.GenerationConfig.ModelConfig#vertexai_preview_generative_models_GenerationConfig_ModelConfig___delattr__)

### vertexai.preview.generative_models.GenerationConfig.ModelConfig.__eq__
    
    
    __eq__(other)

Return True if the messages are equal, False otherwise.

See more: [vertexai.preview.generative_models.GenerationConfig.ModelConfig.**eq**](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.GenerationConfig.ModelConfig#vertexai_preview_generative_models_GenerationConfig_ModelConfig___eq__)

### vertexai.preview.generative_models.GenerationConfig.ModelConfig.__ne__
    
    
    __ne__(other)

Return True if the messages are unequal, False otherwise.

See more: [vertexai.preview.generative_models.GenerationConfig.ModelConfig.**ne**](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.GenerationConfig.ModelConfig#vertexai_preview_generative_models_GenerationConfig_ModelConfig___ne__)

### vertexai.preview.generative_models.GenerationConfig.ModelConfig.__setattr__
    
    
    __setattr__(key, value)

Set the value on the given field.

See more: [vertexai.preview.generative_models.GenerationConfig.ModelConfig.**setattr**](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.GenerationConfig.ModelConfig#vertexai_preview_generative_models_GenerationConfig_ModelConfig___setattr__)

### vertexai.preview.generative_models.GenerationConfig.RoutingConfig.AutoRoutingMode
    
    
    AutoRoutingMode(
        *,
        model_routing_preference: google.cloud.aiplatform_v1beta1.types.content.GenerationConfig.RoutingConfig.AutoRoutingMode.ModelRoutingPreference
    )

AutoRouingMode constructor .

See more: [vertexai.preview.generative_models.GenerationConfig.RoutingConfig.AutoRoutingMode](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.GenerationConfig.RoutingConfig.AutoRoutingMode#vertexai_preview_generative_models_GenerationConfig_RoutingConfig_AutoRoutingMode_AutoRoutingMode)

### vertexai.preview.generative_models.GenerationConfig.RoutingConfig.ManualRoutingMode
    
    
    ManualRoutingMode(*, model_name: str)

ManualRoutingMode constructor .

See more: [vertexai.preview.generative_models.GenerationConfig.RoutingConfig.ManualRoutingMode](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.GenerationConfig.RoutingConfig.ManualRoutingMode#vertexai_preview_generative_models_GenerationConfig_RoutingConfig_ManualRoutingMode_ManualRoutingMode)

### vertexai.preview.generative_models.GenerativeModel.compute_tokens
    
    
    compute_tokens(
        contents: ContentsType,
    ) -> google.cloud.aiplatform_v1beta1.types.llm_utility_service.ComputeTokensResponse

Computes tokens.

See more: [vertexai.preview.generative_models.GenerativeModel.compute_tokens](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.GenerativeModel#vertexai_preview_generative_models_GenerativeModel_compute_tokens)

### vertexai.preview.generative_models.GenerativeModel.compute_tokens_async
    
    
    compute_tokens_async(
        contents: ContentsType,
    ) -> google.cloud.aiplatform_v1beta1.types.llm_utility_service.ComputeTokensResponse

Computes tokens asynchronously.

See more: [vertexai.preview.generative_models.GenerativeModel.compute_tokens_async](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.GenerativeModel#vertexai_preview_generative_models_GenerativeModel_compute_tokens_async)

### vertexai.preview.generative_models.GenerativeModel.count_tokens
    
    
    count_tokens(
        contents: ContentsType,
        *,
        tools: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Tool]
        ] = None
    ) -> google.cloud.aiplatform_v1beta1.types.prediction_service.CountTokensResponse

Counts tokens.

See more: [vertexai.preview.generative_models.GenerativeModel.count_tokens](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.GenerativeModel#vertexai_preview_generative_models_GenerativeModel_count_tokens)

### vertexai.preview.generative_models.GenerativeModel.count_tokens_async
    
    
    count_tokens_async(
        contents: ContentsType,
        *,
        tools: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Tool]
        ] = None
    ) -> google.cloud.aiplatform_v1beta1.types.prediction_service.CountTokensResponse

Counts tokens asynchronously.

See more: [vertexai.preview.generative_models.GenerativeModel.count_tokens_async](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.GenerativeModel#vertexai_preview_generative_models_GenerativeModel_count_tokens_async)

### vertexai.preview.generative_models.GenerativeModel.from_cached_content
    
    
    from_cached_content(
        cached_content: typing.Union[str, CachedContent],
        *,
        generation_config: typing.Optional[GenerationConfigType] = None,
        safety_settings: typing.Optional[SafetySettingsType] = None
    ) -> _GenerativeModel

Creates a model from cached content.

See more: [vertexai.preview.generative_models.GenerativeModel.from_cached_content](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.GenerativeModel#vertexai_preview_generative_models_GenerativeModel_from_cached_content)

### vertexai.preview.generative_models.GenerativeModel.generate_content
    
    
    generate_content(
        contents: ContentsType,
        *,
        generation_config: typing.Optional[GenerationConfigType] = None,
        safety_settings: typing.Optional[SafetySettingsType] = None,
        tools: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Tool]
        ] = None,
        tool_config: typing.Optional[
            vertexai.generative_models._generative_models.ToolConfig
        ] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        stream: bool = False
    ) -> typing.Union[
        vertexai.generative_models._generative_models.GenerationResponse,
        typing.Iterable[vertexai.generative_models._generative_models.GenerationResponse],
    ]

Generates content.

See more: [vertexai.preview.generative_models.GenerativeModel.generate_content](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.GenerativeModel#vertexai_preview_generative_models_GenerativeModel_generate_content)

### vertexai.preview.generative_models.GenerativeModel.generate_content_async
    
    
    generate_content_async(
        contents: ContentsType,
        *,
        generation_config: typing.Optional[GenerationConfigType] = None,
        safety_settings: typing.Optional[SafetySettingsType] = None,
        tools: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Tool]
        ] = None,
        tool_config: typing.Optional[
            vertexai.generative_models._generative_models.ToolConfig
        ] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        stream: bool = False
    ) -> typing.Union[
        vertexai.generative_models._generative_models.GenerationResponse,
        typing.AsyncIterable[
            vertexai.generative_models._generative_models.GenerationResponse
        ],
    ]

Generates content asynchronously.

See more: [vertexai.preview.generative_models.GenerativeModel.generate_content_async](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.GenerativeModel#vertexai_preview_generative_models_GenerativeModel_generate_content_async)

### vertexai.preview.generative_models.GenerativeModel.set_request_response_logging_config
    
    
    set_request_response_logging_config(
        *,
        enabled: bool,
        sampling_rate: float,
        bigquery_destination: str,
        enable_otel_logging: typing.Optional[bool] = None
    ) -> typing.Union[
        google.cloud.aiplatform_v1beta1.types.endpoint.PublisherModelConfig,
        google.cloud.aiplatform_v1beta1.types.endpoint.Endpoint,
    ]

Sets the request/response logging config.

See more: [vertexai.preview.generative_models.GenerativeModel.set_request_response_logging_config](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.GenerativeModel#vertexai_preview_generative_models_GenerativeModel_set_request_response_logging_config)

### vertexai.preview.generative_models.GenerativeModel.start_chat
    
    
    start_chat(
        *,
        history: typing.Optional[
            typing.List[vertexai.generative_models._generative_models.Content]
        ] = None,
        response_validation: bool = True,
        responder: typing.Optional[
            vertexai.generative_models._generative_models.AutomaticFunctionCallingResponder
        ] = None
    ) -> vertexai.generative_models._generative_models.ChatSession

Creates a stateful chat session.

See more: [vertexai.preview.generative_models.GenerativeModel.start_chat](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.GenerativeModel#vertexai_preview_generative_models_GenerativeModel_start_chat)

### vertexai.preview.generative_models.Image.from_bytes
    
    
    from_bytes(data: bytes) -> vertexai.generative_models._generative_models.Image

Loads image from image bytes.

See more: [vertexai.preview.generative_models.Image.from_bytes](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.Image#vertexai_preview_generative_models_Image_from_bytes)

### vertexai.preview.generative_models.Image.load_from_file
    
    
    load_from_file(
        location: str,
    ) -> vertexai.generative_models._generative_models.Image

Loads image from file.

See more: [vertexai.preview.generative_models.Image.load_from_file](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.Image#vertexai_preview_generative_models_Image_load_from_file)

### vertexai.preview.generative_models.ResponseBlockedError.with_traceback


Exception.with_traceback(tb) -- set self.**traceback** to tb and return self.

See more: [vertexai.preview.generative_models.ResponseBlockedError.with_traceback](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.ResponseBlockedError#vertexai_preview_generative_models_ResponseBlockedError_with_traceback)

### vertexai.preview.generative_models.ResponseValidationError.with_traceback


Exception.with_traceback(tb) -- set self.**traceback** to tb and return self.

See more: [vertexai.preview.generative_models.ResponseValidationError.with_traceback](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.ResponseValidationError#vertexai_preview_generative_models_ResponseValidationError_with_traceback)

### vertexai.preview.generative_models.SafetySetting
    
    
    SafetySetting(
        *,
        category: google.cloud.aiplatform_v1beta1.types.content.HarmCategory,
        threshold: google.cloud.aiplatform_v1beta1.types.content.SafetySetting.HarmBlockThreshold,
        method: typing.Optional[
            google.cloud.aiplatform_v1beta1.types.content.SafetySetting.HarmBlockMethod
        ] = None
    )

Safety settings.

See more: [vertexai.preview.generative_models.SafetySetting](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.generative_models.SafetySetting#vertexai_preview_generative_models_SafetySetting_SafetySetting)

### vertexai.preview.reasoning_engines.A2aAgent
    
    
    A2aAgent(
        *,
        agent_card: AgentCard,
        task_store_builder: typing.Callable[[...], TaskStore] = None,
        task_store_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        agent_executor_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        agent_executor_builder: typing.Optional[
            typing.Callable[[...], AgentExecutor]
        ] = None,
        request_handler_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        request_handler_builder: typing.Optional[
            typing.Callable[[...], RequestHandler]
        ] = None,
        extended_agent_card: AgentCard = None
    )

Initializes the A2A agent.

See more: [vertexai.preview.reasoning_engines.A2aAgent](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.A2aAgent#vertexai_preview_reasoning_engines_A2aAgent_A2aAgent)

### vertexai.preview.reasoning_engines.A2aAgent.clone
    
    
    clone() -> vertexai.preview.reasoning_engines.templates.a2a.A2aAgent

Clones the A2A agent.

See more: [vertexai.preview.reasoning_engines.A2aAgent.clone](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.A2aAgent#vertexai_preview_reasoning_engines_A2aAgent_clone)

### vertexai.preview.reasoning_engines.A2aAgent.on_message_send_stream
    
    
    on_message_send_stream(
        request: Request, context: ServerCallContext
    ) -> collections.abc.AsyncIterator[str]

Handles A2A streaming requests via SSE.

See more: [vertexai.preview.reasoning_engines.A2aAgent.on_message_send_stream](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.A2aAgent#vertexai_preview_reasoning_engines_A2aAgent_on_message_send_stream)

### vertexai.preview.reasoning_engines.A2aAgent.on_resubscribe_to_task
    
    
    on_resubscribe_to_task(
        request: Request, context: ServerCallContext
    ) -> collections.abc.AsyncIterator[str]

Handles A2A task resubscription requests via SSE.

See more: [vertexai.preview.reasoning_engines.A2aAgent.on_resubscribe_to_task](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.A2aAgent#vertexai_preview_reasoning_engines_A2aAgent_on_resubscribe_to_task)

### vertexai.preview.reasoning_engines.A2aAgent.register_operations
    
    
    register_operations() -> typing.Dict[str, typing.List[str]]

Registers the operations of the A2A Agent.

See more: [vertexai.preview.reasoning_engines.A2aAgent.register_operations](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.A2aAgent#vertexai_preview_reasoning_engines_A2aAgent_register_operations)

### vertexai.preview.reasoning_engines.A2aAgent.set_up
    
    
    set_up()

Sets up the A2A application.

See more: [vertexai.preview.reasoning_engines.A2aAgent.set_up](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.A2aAgent#vertexai_preview_reasoning_engines_A2aAgent_set_up)

### vertexai.preview.reasoning_engines.AG2Agent
    
    
    AG2Agent(
        model: str,
        runnable_name: str,
        *,
        api_type: typing.Optional[str] = None,
        llm_config: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        system_instruction: typing.Optional[str] = None,
        runnable_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        runnable_builder: typing.Optional[typing.Callable[[...], ConversableAgent]] = None,
        tools: typing.Optional[typing.Sequence[typing.Callable[[...], typing.Any]]] = None,
        enable_tracing: bool = False
    )

Initializes the AG2 Agent.

See more: [vertexai.preview.reasoning_engines.AG2Agent](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AG2Agent#vertexai_preview_reasoning_engines_AG2Agent_AG2Agent)

### vertexai.preview.reasoning_engines.AG2Agent.clone
    
    
    clone() -> vertexai.preview.reasoning_engines.templates.ag2.AG2Agent

Returns a clone of the AG2Agent.

See more: [vertexai.preview.reasoning_engines.AG2Agent.clone](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AG2Agent#vertexai_preview_reasoning_engines_AG2Agent_clone)

### vertexai.preview.reasoning_engines.AG2Agent.query
    
    
    query(
        *,
        input: typing.Union[str, typing.Mapping[str, typing.Any]],
        max_turns: typing.Optional[int] = None,
        **kwargs: typing.Any
    ) -> typing.Dict[str, typing.Any]

Queries the Agent with the given input.

See more: [vertexai.preview.reasoning_engines.AG2Agent.query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AG2Agent#vertexai_preview_reasoning_engines_AG2Agent_query)

### vertexai.preview.reasoning_engines.AG2Agent.set_up
    
    
    set_up()

Sets up the agent for execution of queries at runtime.

See more: [vertexai.preview.reasoning_engines.AG2Agent.set_up](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AG2Agent#vertexai_preview_reasoning_engines_AG2Agent_set_up)

### vertexai.preview.reasoning_engines.AdkApp
    
    
    AdkApp(
        *,
        agent: BaseAgent,
        plugins: typing.Optional[typing.List[BasePlugin]] = None,
        enable_tracing: typing.Optional[bool] = None,
        session_service_builder: typing.Optional[
            typing.Callable[[...], BaseSessionService]
        ] = None,
        artifact_service_builder: typing.Optional[
            typing.Callable[[...], BaseArtifactService]
        ] = None,
        memory_service_builder: typing.Optional[
            typing.Callable[[...], BaseMemoryService]
        ] = None,
        credential_service_builder: typing.Optional[
            typing.Callable[[...], BaseCredentialService]
        ] = None,
        env_vars: typing.Optional[typing.Dict[str, str]] = None
    )

An ADK Application.

See more: [vertexai.preview.reasoning_engines.AdkApp](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AdkApp#vertexai_preview_reasoning_engines_AdkApp_AdkApp)

### vertexai.preview.reasoning_engines.AdkApp.async_add_session_to_memory
    
    
    async_add_session_to_memory(*, session: typing.Dict[str, typing.Any])

Generates memories.

See more: [vertexai.preview.reasoning_engines.AdkApp.async_add_session_to_memory](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AdkApp#vertexai_preview_reasoning_engines_AdkApp_async_add_session_to_memory)

### vertexai.preview.reasoning_engines.AdkApp.async_create_session
    
    
    async_create_session(
        *,
        user_id: str,
        session_id: typing.Optional[str] = None,
        state: typing.Optional[typing.Dict[str, typing.Any]] = None,
        **kwargs
    )

Creates a new session.

See more: [vertexai.preview.reasoning_engines.AdkApp.async_create_session](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AdkApp#vertexai_preview_reasoning_engines_AdkApp_async_create_session)

### vertexai.preview.reasoning_engines.AdkApp.async_delete_session
    
    
    async_delete_session(*, user_id: str, session_id: str, **kwargs)

Deletes a session for the given user.

See more: [vertexai.preview.reasoning_engines.AdkApp.async_delete_session](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AdkApp#vertexai_preview_reasoning_engines_AdkApp_async_delete_session)

### vertexai.preview.reasoning_engines.AdkApp.async_get_session
    
    
    async_get_session(*, user_id: str, session_id: str, **kwargs)

Get a session for the given user.

See more: [vertexai.preview.reasoning_engines.AdkApp.async_get_session](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AdkApp#vertexai_preview_reasoning_engines_AdkApp_async_get_session)

### vertexai.preview.reasoning_engines.AdkApp.async_list_sessions
    
    
    async_list_sessions(*, user_id: str, **kwargs)

List sessions for the given user.

See more: [vertexai.preview.reasoning_engines.AdkApp.async_list_sessions](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AdkApp#vertexai_preview_reasoning_engines_AdkApp_async_list_sessions)

### vertexai.preview.reasoning_engines.AdkApp.async_search_memory
    
    
    async_search_memory(*, user_id: str, query: str)

Searches memories for the given user.

See more: [vertexai.preview.reasoning_engines.AdkApp.async_search_memory](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AdkApp#vertexai_preview_reasoning_engines_AdkApp_async_search_memory)

### vertexai.preview.reasoning_engines.AdkApp.async_stream_query
    
    
    async_stream_query(
        *,
        message: typing.Union[str, typing.Dict[str, typing.Any]],
        user_id: str,
        session_id: typing.Optional[str] = None,
        run_config: typing.Optional[typing.Dict[str, typing.Any]] = None,
        **kwargs
    ) -> typing.AsyncIterable[typing.Dict[str, typing.Any]]

Streams responses asynchronously from the ADK application.

See more: [vertexai.preview.reasoning_engines.AdkApp.async_stream_query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AdkApp#vertexai_preview_reasoning_engines_AdkApp_async_stream_query)

### vertexai.preview.reasoning_engines.AdkApp.bidi_stream_query
    
    
    bidi_stream_query(request_queue: typing.Any) -> typing.AsyncIterable[typing.Any]

Bidi streaming query the ADK application.

See more: [vertexai.preview.reasoning_engines.AdkApp.bidi_stream_query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AdkApp#vertexai_preview_reasoning_engines_AdkApp_bidi_stream_query)

### vertexai.preview.reasoning_engines.AdkApp.clone
    
    
    clone()

Returns a clone of the ADK application.

See more: [vertexai.preview.reasoning_engines.AdkApp.clone](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AdkApp#vertexai_preview_reasoning_engines_AdkApp_clone)

### vertexai.preview.reasoning_engines.AdkApp.create_session
    
    
    create_session(
        *,
        user_id: str,
        session_id: typing.Optional[str] = None,
        state: typing.Optional[typing.Dict[str, typing.Any]] = None,
        **kwargs
    )

Creates a new session.

See more: [vertexai.preview.reasoning_engines.AdkApp.create_session](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AdkApp#vertexai_preview_reasoning_engines_AdkApp_create_session)

### vertexai.preview.reasoning_engines.AdkApp.delete_session
    
    
    delete_session(*, user_id: str, session_id: str, **kwargs)

Deletes a session for the given user.

See more: [vertexai.preview.reasoning_engines.AdkApp.delete_session](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AdkApp#vertexai_preview_reasoning_engines_AdkApp_delete_session)

### vertexai.preview.reasoning_engines.AdkApp.get_session
    
    
    get_session(*, user_id: str, session_id: str, **kwargs)

Get a session for the given user.

See more: [vertexai.preview.reasoning_engines.AdkApp.get_session](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AdkApp#vertexai_preview_reasoning_engines_AdkApp_get_session)

### vertexai.preview.reasoning_engines.AdkApp.list_sessions
    
    
    list_sessions(*, user_id: str, **kwargs)

List sessions for the given user.

See more: [vertexai.preview.reasoning_engines.AdkApp.list_sessions](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AdkApp#vertexai_preview_reasoning_engines_AdkApp_list_sessions)

### vertexai.preview.reasoning_engines.AdkApp.register_operations
    
    
    register_operations() -> typing.Dict[str, typing.List[str]]

Registers the operations of the ADK application.

See more: [vertexai.preview.reasoning_engines.AdkApp.register_operations](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AdkApp#vertexai_preview_reasoning_engines_AdkApp_register_operations)

### vertexai.preview.reasoning_engines.AdkApp.set_up
    
    
    set_up()

Sets up the ADK application.

See more: [vertexai.preview.reasoning_engines.AdkApp.set_up](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AdkApp#vertexai_preview_reasoning_engines_AdkApp_set_up)

### vertexai.preview.reasoning_engines.AdkApp.stream_query
    
    
    stream_query(
        *,
        message: typing.Union[str, typing.Dict[str, typing.Any]],
        user_id: str,
        session_id: typing.Optional[str] = None,
        run_config: typing.Optional[typing.Dict[str, typing.Any]] = None,
        **kwargs
    )

Streams responses from the ADK application in response to a message.

See more: [vertexai.preview.reasoning_engines.AdkApp.stream_query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.AdkApp#vertexai_preview_reasoning_engines_AdkApp_stream_query)

### vertexai.preview.reasoning_engines.LangchainAgent
    
    
    LangchainAgent(
        model: str,
        *,
        system_instruction: typing.Optional[str] = None,
        prompt: typing.Optional[RunnableSerializable] = None,
        tools: typing.Optional[_ToolsType] = None,
        output_parser: typing.Optional[RunnableSerializable] = None,
        chat_history: typing.Optional[GetSessionHistoryCallable] = None,
        model_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        model_tool_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        agent_executor_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        runnable_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        model_builder: typing.Optional[typing.Callable] = None,
        runnable_builder: typing.Optional[typing.Callable] = None,
        enable_tracing: bool = False
    )

Initializes the LangchainAgent.

See more: [vertexai.preview.reasoning_engines.LangchainAgent](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.LangchainAgent#vertexai_preview_reasoning_engines_LangchainAgent_LangchainAgent)

### vertexai.preview.reasoning_engines.LangchainAgent.clone
    
    
    clone() -> vertexai.preview.reasoning_engines.templates.langchain.LangchainAgent

Returns a clone of the LangchainAgent.

See more: [vertexai.preview.reasoning_engines.LangchainAgent.clone](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.LangchainAgent#vertexai_preview_reasoning_engines_LangchainAgent_clone)

### vertexai.preview.reasoning_engines.LangchainAgent.query
    
    
    query(
        *,
        input: typing.Union[str, typing.Mapping[str, typing.Any]],
        config: typing.Optional[RunnableConfig] = None,
        **kwargs: typing.Any
    ) -> typing.Dict[str, typing.Any]

Queries the Agent with the given input and config.

See more: [vertexai.preview.reasoning_engines.LangchainAgent.query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.LangchainAgent#vertexai_preview_reasoning_engines_LangchainAgent_query)

### vertexai.preview.reasoning_engines.LangchainAgent.set_up
    
    
    set_up()

Sets up the agent for execution of queries at runtime.

See more: [vertexai.preview.reasoning_engines.LangchainAgent.set_up](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.LangchainAgent#vertexai_preview_reasoning_engines_LangchainAgent_set_up)

### vertexai.preview.reasoning_engines.LangchainAgent.stream_query
    
    
    stream_query(
        *,
        input: typing.Union[str, typing.Mapping[str, typing.Any]],
        config: typing.Optional[RunnableConfig] = None,
        **kwargs
    ) -> typing.Iterable[typing.Any]

Stream queries the Agent with the given input and config.

See more: [vertexai.preview.reasoning_engines.LangchainAgent.stream_query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.LangchainAgent#vertexai_preview_reasoning_engines_LangchainAgent_stream_query)

### vertexai.preview.reasoning_engines.LanggraphAgent
    
    
    LanggraphAgent(
        model: str,
        *,
        tools: typing.Optional[typing.Sequence[_ToolLike]] = None,
        model_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        model_tool_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        model_builder: typing.Optional[typing.Callable[[...], BaseLanguageModel]] = None,
        runnable_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        runnable_builder: typing.Optional[
            typing.Callable[[...], RunnableSerializable]
        ] = None,
        checkpointer_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        checkpointer_builder: typing.Optional[
            typing.Callable[[...], BaseCheckpointSaver]
        ] = None,
        enable_tracing: bool = False
    )

Initializes the LangGraph Agent.

See more: [vertexai.preview.reasoning_engines.LanggraphAgent](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.LanggraphAgent#vertexai_preview_reasoning_engines_LanggraphAgent_LanggraphAgent)

### vertexai.preview.reasoning_engines.LanggraphAgent.clone
    
    
    clone() -> vertexai.preview.reasoning_engines.templates.langgraph.LanggraphAgent

Returns a clone of the LanggraphAgent.

See more: [vertexai.preview.reasoning_engines.LanggraphAgent.clone](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.LanggraphAgent#vertexai_preview_reasoning_engines_LanggraphAgent_clone)

### vertexai.preview.reasoning_engines.LanggraphAgent.get_state
    
    
    get_state(
        config: typing.Optional[RunnableConfig] = None, **kwargs: typing.Any
    ) -> typing.Dict[str, typing.Any]

Gets the current state of the Agent.

See more: [vertexai.preview.reasoning_engines.LanggraphAgent.get_state](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.LanggraphAgent#vertexai_preview_reasoning_engines_LanggraphAgent_get_state)

### vertexai.preview.reasoning_engines.LanggraphAgent.get_state_history
    
    
    get_state_history(
        config: typing.Optional[RunnableConfig] = None, **kwargs: typing.Any
    ) -> typing.Iterable[typing.Any]

Gets the state history of the Agent.

See more: [vertexai.preview.reasoning_engines.LanggraphAgent.get_state_history](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.LanggraphAgent#vertexai_preview_reasoning_engines_LanggraphAgent_get_state_history)

### vertexai.preview.reasoning_engines.LanggraphAgent.query
    
    
    query(
        *,
        input: typing.Union[str, typing.Mapping[str, typing.Any]],
        config: typing.Optional[RunnableConfig] = None,
        **kwargs: typing.Any
    ) -> typing.Dict[str, typing.Any]

Queries the Agent with the given input and config.

See more: [vertexai.preview.reasoning_engines.LanggraphAgent.query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.LanggraphAgent#vertexai_preview_reasoning_engines_LanggraphAgent_query)

### vertexai.preview.reasoning_engines.LanggraphAgent.register_operations
    
    
    register_operations() -> typing.Mapping[str, typing.Sequence[str]]

Registers the operations of the Agent.

See more: [vertexai.preview.reasoning_engines.LanggraphAgent.register_operations](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.LanggraphAgent#vertexai_preview_reasoning_engines_LanggraphAgent_register_operations)

### vertexai.preview.reasoning_engines.LanggraphAgent.set_up
    
    
    set_up()

Sets up the agent for execution of queries at runtime.

See more: [vertexai.preview.reasoning_engines.LanggraphAgent.set_up](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.LanggraphAgent#vertexai_preview_reasoning_engines_LanggraphAgent_set_up)

### vertexai.preview.reasoning_engines.LanggraphAgent.stream_query
    
    
    stream_query(
        *,
        input: typing.Union[str, typing.Mapping[str, typing.Any]],
        config: typing.Optional[RunnableConfig] = None,
        **kwargs
    ) -> typing.Iterable[typing.Any]

Stream queries the Agent with the given input and config.

See more: [vertexai.preview.reasoning_engines.LanggraphAgent.stream_query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.LanggraphAgent#vertexai_preview_reasoning_engines_LanggraphAgent_stream_query)

### vertexai.preview.reasoning_engines.LanggraphAgent.update_state
    
    
    update_state(
        config: typing.Optional[RunnableConfig] = None, **kwargs: typing.Any
    ) -> typing.Dict[str, typing.Any]

Updates the state of the Agent.

See more: [vertexai.preview.reasoning_engines.LanggraphAgent.update_state](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.LanggraphAgent#vertexai_preview_reasoning_engines_LanggraphAgent_update_state)

### vertexai.preview.reasoning_engines.LlamaIndexQueryPipelineAgent
    
    
    LlamaIndexQueryPipelineAgent(
        model: str,
        *,
        system_instruction: typing.Optional[str] = None,
        prompt: typing.Optional[QueryComponent] = None,
        model_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        model_builder: typing.Optional[typing.Callable[[...], FunctionCallingLLM]] = None,
        retriever_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        retriever_builder: typing.Optional[typing.Callable[[...], QueryComponent]] = None,
        response_synthesizer_kwargs: typing.Optional[
            typing.Mapping[str, typing.Any]
        ] = None,
        response_synthesizer_builder: typing.Optional[
            typing.Callable[[...], QueryComponent]
        ] = None,
        runnable_kwargs: typing.Optional[typing.Mapping[str, typing.Any]] = None,
        runnable_builder: typing.Optional[typing.Callable[[...], QueryPipeline]] = None,
        enable_tracing: bool = False
    )

Initializes the LlamaIndexQueryPipelineAgent.

See more: [vertexai.preview.reasoning_engines.LlamaIndexQueryPipelineAgent](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.LlamaIndexQueryPipelineAgent#vertexai_preview_reasoning_engines_LlamaIndexQueryPipelineAgent_LlamaIndexQueryPipelineAgent)

### vertexai.preview.reasoning_engines.LlamaIndexQueryPipelineAgent.clone
    
    
    clone() -> (
        vertexai.preview.reasoning_engines.templates.llama_index.LlamaIndexQueryPipelineAgent
    )

Returns a clone of the LlamaIndexQueryPipelineAgent.

See more: [vertexai.preview.reasoning_engines.LlamaIndexQueryPipelineAgent.clone](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.LlamaIndexQueryPipelineAgent#vertexai_preview_reasoning_engines_LlamaIndexQueryPipelineAgent_clone)

### vertexai.preview.reasoning_engines.LlamaIndexQueryPipelineAgent.query
    
    
    query(
        input: typing.Union[str, typing.Mapping[str, typing.Any]], **kwargs: typing.Any
    ) -> typing.Union[
        str,
        typing.Dict[str, typing.Any],
        typing.Sequence[typing.Union[str, typing.Dict[str, typing.Any]]],
    ]

Queries the Agent with the given input and config.

See more: [vertexai.preview.reasoning_engines.LlamaIndexQueryPipelineAgent.query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.LlamaIndexQueryPipelineAgent#vertexai_preview_reasoning_engines_LlamaIndexQueryPipelineAgent_query)

### vertexai.preview.reasoning_engines.LlamaIndexQueryPipelineAgent.set_up
    
    
    set_up()

Sets up the agent for execution of queries at runtime.

See more: [vertexai.preview.reasoning_engines.LlamaIndexQueryPipelineAgent.set_up](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.LlamaIndexQueryPipelineAgent#vertexai_preview_reasoning_engines_LlamaIndexQueryPipelineAgent_set_up)

### vertexai.preview.reasoning_engines.Queryable.query
    
    
    query(**kwargs)

Runs the Reasoning Engine to serve the user query.

See more: [vertexai.preview.reasoning_engines.Queryable.query](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.Queryable#vertexai_preview_reasoning_engines_Queryable_query)

### vertexai.preview.reasoning_engines.ReasoningEngine
    
    
    ReasoningEngine(reasoning_engine_name: str)

Retrieves a Reasoning Engine resource.

See more: [vertexai.preview.reasoning_engines.ReasoningEngine](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.ReasoningEngine#vertexai_preview_reasoning_engines_ReasoningEngine_ReasoningEngine)

### vertexai.preview.reasoning_engines.ReasoningEngine.create
    
    
    create(
        reasoning_engine: typing.Union[
            vertexai.reasoning_engines._reasoning_engines.Queryable,
            vertexai.reasoning_engines._reasoning_engines.OperationRegistrable,
        ],
        *,
        requirements: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        reasoning_engine_name: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        gcs_dir_name: str = "reasoning_engine",
        sys_version: typing.Optional[str] = None,
        extra_packages: typing.Optional[typing.Sequence[str]] = None,
        service_account: typing.Optional[str] = None,
        identity_type: typing.Optional[
            typing.Union[
                str,
                google.cloud.aiplatform_v1beta1.types.reasoning_engine.ReasoningEngineSpec.IdentityType,
            ]
        ] = None
    ) -> vertexai.reasoning_engines._reasoning_engines.ReasoningEngine

Creates a new ReasoningEngine.

See more: [vertexai.preview.reasoning_engines.ReasoningEngine.create](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.ReasoningEngine#vertexai_preview_reasoning_engines_ReasoningEngine_create)

### vertexai.preview.reasoning_engines.ReasoningEngine.delete
    
    
    delete(sync: bool = True) -> None

Deletes this Vertex AI resource.

See more: [vertexai.preview.reasoning_engines.ReasoningEngine.delete](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.ReasoningEngine#vertexai_preview_reasoning_engines_ReasoningEngine_delete)

### vertexai.preview.reasoning_engines.ReasoningEngine.list
    
    
    list(
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        parent: typing.Optional[str] = None,
    ) -> typing.List[google.cloud.aiplatform.base.VertexAiResourceNoun]

List all instances of this Vertex AI Resource.

See more: [vertexai.preview.reasoning_engines.ReasoningEngine.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.ReasoningEngine#vertexai_preview_reasoning_engines_ReasoningEngine_list)

### vertexai.preview.reasoning_engines.ReasoningEngine.operation_schemas
    
    
    operation_schemas() -> typing.Sequence[typing.Dict[str, typing.Any]]

Returns the (Open)API schemas for the Reasoning Engine.

See more: [vertexai.preview.reasoning_engines.ReasoningEngine.operation_schemas](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.ReasoningEngine#vertexai_preview_reasoning_engines_ReasoningEngine_operation_schemas)

### vertexai.preview.reasoning_engines.ReasoningEngine.to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

See more: [vertexai.preview.reasoning_engines.ReasoningEngine.to_dict](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.ReasoningEngine#vertexai_preview_reasoning_engines_ReasoningEngine_to_dict)

### vertexai.preview.reasoning_engines.ReasoningEngine.update
    
    
    update(
        *,
        reasoning_engine: typing.Optional[
            typing.Union[
                vertexai.reasoning_engines._reasoning_engines.Queryable,
                vertexai.reasoning_engines._reasoning_engines.OperationRegistrable,
            ]
        ] = None,
        requirements: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        display_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        gcs_dir_name: str = "reasoning_engine",
        sys_version: typing.Optional[str] = None,
        extra_packages: typing.Optional[typing.Sequence[str]] = None,
        service_account: typing.Optional[str] = None,
        identity_type: typing.Optional[
            typing.Union[
                str,
                google.cloud.aiplatform_v1beta1.types.reasoning_engine.ReasoningEngineSpec.IdentityType,
            ]
        ] = None
    ) -> vertexai.reasoning_engines._reasoning_engines.ReasoningEngine

Updates an existing ReasoningEngine.

See more: [vertexai.preview.reasoning_engines.ReasoningEngine.update](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.ReasoningEngine#vertexai_preview_reasoning_engines_ReasoningEngine_update)

### vertexai.preview.reasoning_engines.ReasoningEngine.wait
    
    
    wait()

Helper method that blocks until all futures are complete.

See more: [vertexai.preview.reasoning_engines.ReasoningEngine.wait](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.reasoning_engines.ReasoningEngine#vertexai_preview_reasoning_engines_ReasoningEngine_wait)

### vertexai.preview.tuning.SourceModel
    
    
    SourceModel(base_model: str, custom_base_model: str = "")

Initializes SourceModel.

See more: [vertexai.preview.tuning.SourceModel](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.tuning.SourceModel#vertexai_preview_tuning_SourceModel_SourceModel)

### vertexai.preview.tuning.TuningJob
    
    
    TuningJob(tuning_job_name: str)

Initializes class with project, location, and api_client.

See more: [vertexai.preview.tuning.TuningJob](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.tuning.TuningJob#vertexai_preview_tuning_TuningJob_TuningJob)

### vertexai.preview.tuning.TuningJob.list
    
    
    list(
        filter: typing.Optional[str] = None,
    ) -> typing.List[vertexai.tuning._tuning.TuningJob]

Lists TuningJobs.

See more: [vertexai.preview.tuning.TuningJob.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.tuning.TuningJob#vertexai_preview_tuning_TuningJob_list)

### vertexai.preview.tuning.TuningJob.refresh
    
    
    refresh() -> vertexai.tuning._tuning.TuningJob

Refreshed the tuning job from the service.

See more: [vertexai.preview.tuning.TuningJob.refresh](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.tuning.TuningJob#vertexai_preview_tuning_TuningJob_refresh)

### vertexai.preview.tuning.TuningJob.to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

See more: [vertexai.preview.tuning.TuningJob.to_dict](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.tuning.TuningJob#vertexai_preview_tuning_TuningJob_to_dict)

### vertexai.preview.tuning.sft.SupervisedTuningJob.list
    
    
    list(
        filter: typing.Optional[str] = None,
    ) -> typing.List[vertexai.tuning._tuning.TuningJob]

Lists TuningJobs.

See more: [vertexai.preview.tuning.sft.SupervisedTuningJob.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.tuning.sft.SupervisedTuningJob#vertexai_preview_tuning_sft_SupervisedTuningJob_list)

### vertexai.preview.tuning.sft.SupervisedTuningJob.refresh
    
    
    refresh() -> vertexai.tuning._tuning.TuningJob

Refreshed the tuning job from the service.

See more: [vertexai.preview.tuning.sft.SupervisedTuningJob.refresh](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.tuning.sft.SupervisedTuningJob#vertexai_preview_tuning_sft_SupervisedTuningJob_refresh)

### vertexai.preview.tuning.sft.SupervisedTuningJob.to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

See more: [vertexai.preview.tuning.sft.SupervisedTuningJob.to_dict](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.tuning.sft.SupervisedTuningJob#vertexai_preview_tuning_sft_SupervisedTuningJob_to_dict)

### vertexai.preview.vision_models.ControlReferenceImage
    
    
    ControlReferenceImage(
        reference_id,
        image: typing.Optional[
            typing.Union[bytes, vertexai.vision_models.Image, str]
        ] = None,
        control_type: typing.Optional[
            typing.Literal["default", "scribble", "face_mesh", "canny"]
        ] = None,
        enable_control_image_computation: typing.Optional[bool] = False,
    )

Creates a `ControlReferenceImage` object.

See more: [vertexai.preview.vision_models.ControlReferenceImage](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ControlReferenceImage#vertexai_preview_vision_models_ControlReferenceImage_ControlReferenceImage)

### vertexai.preview.vision_models.GeneratedImage
    
    
    GeneratedImage(
        image_bytes: typing.Optional[bytes],
        generation_parameters: typing.Dict[str, typing.Any],
        gcs_uri: typing.Optional[str] = None,
    )

Creates a `GeneratedImage` object.

See more: [vertexai.preview.vision_models.GeneratedImage](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.GeneratedImage#vertexai_preview_vision_models_GeneratedImage_GeneratedImage)

### vertexai.preview.vision_models.GeneratedImage.load_from_file
    
    
    load_from_file(location: str) -> vertexai.preview.vision_models.GeneratedImage

Loads image from file.

See more: [vertexai.preview.vision_models.GeneratedImage.load_from_file](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.GeneratedImage#vertexai_preview_vision_models_GeneratedImage_load_from_file)

### vertexai.preview.vision_models.GeneratedImage.save
    
    
    save(location: str, include_generation_parameters: bool = True)

Saves image to a file.

See more: [vertexai.preview.vision_models.GeneratedImage.save](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.GeneratedImage#vertexai_preview_vision_models_GeneratedImage_save)

### vertexai.preview.vision_models.GeneratedImage.show
    
    
    show()

Shows the image.

See more: [vertexai.preview.vision_models.GeneratedImage.show](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.GeneratedImage#vertexai_preview_vision_models_GeneratedImage_show)

### vertexai.preview.vision_models.GeneratedMask
    
    
    GeneratedMask(
        image_bytes: typing.Optional[bytes],
        gcs_uri: typing.Optional[str] = None,
        labels: typing.Optional[
            typing.List[vertexai.preview.vision_models.EntityLabel]
        ] = None,
    )

Creates a `GeneratedMask` object.

See more: [vertexai.preview.vision_models.GeneratedMask](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.GeneratedMask#vertexai_preview_vision_models_GeneratedMask_GeneratedMask)

### vertexai.preview.vision_models.GeneratedMask.load_from_file
    
    
    load_from_file(location: str) -> vertexai.vision_models.Image

Loads image from local file or Google Cloud Storage.

See more: [vertexai.preview.vision_models.GeneratedMask.load_from_file](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.GeneratedMask#vertexai_preview_vision_models_GeneratedMask_load_from_file)

### vertexai.preview.vision_models.GeneratedMask.save
    
    
    save(location: str)

Saves image to a file.

See more: [vertexai.preview.vision_models.GeneratedMask.save](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.GeneratedMask#vertexai_preview_vision_models_GeneratedMask_save)

### vertexai.preview.vision_models.GeneratedMask.show
    
    
    show()

Shows the image.

See more: [vertexai.preview.vision_models.GeneratedMask.show](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.GeneratedMask#vertexai_preview_vision_models_GeneratedMask_show)

### vertexai.preview.vision_models.Image
    
    
    Image(
        image_bytes: typing.Optional[bytes] = None, gcs_uri: typing.Optional[str] = None
    )

Creates an `Image` object.

See more: [vertexai.preview.vision_models.Image](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.Image#vertexai_preview_vision_models_Image_Image)

### vertexai.preview.vision_models.Image.load_from_file
    
    
    load_from_file(location: str) -> vertexai.vision_models.Image

Loads image from local file or Google Cloud Storage.

See more: [vertexai.preview.vision_models.Image.load_from_file](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.Image#vertexai_preview_vision_models_Image_load_from_file)

### vertexai.preview.vision_models.Image.save
    
    
    save(location: str)

Saves image to a file.

See more: [vertexai.preview.vision_models.Image.save](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.Image#vertexai_preview_vision_models_Image_save)

### vertexai.preview.vision_models.Image.show
    
    
    show()

Shows the image.

See more: [vertexai.preview.vision_models.Image.show](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.Image#vertexai_preview_vision_models_Image_show)

### vertexai.preview.vision_models.ImageCaptioningModel
    
    
    ImageCaptioningModel(model_id: str, endpoint_name: typing.Optional[str] = None)

Creates a _ModelGardenModel.

See more: [vertexai.preview.vision_models.ImageCaptioningModel](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageCaptioningModel#vertexai_preview_vision_models_ImageCaptioningModel_ImageCaptioningModel)

### vertexai.preview.vision_models.ImageCaptioningModel.from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

See more: [vertexai.preview.vision_models.ImageCaptioningModel.from_pretrained](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageCaptioningModel#vertexai_preview_vision_models_ImageCaptioningModel_from_pretrained)

### vertexai.preview.vision_models.ImageCaptioningModel.get_captions
    
    
    get_captions(
        image: vertexai.vision_models.Image,
        *,
        number_of_results: int = 1,
        language: str = "en",
        output_gcs_uri: typing.Optional[str] = None
    ) -> typing.List[str]

Generates captions for a given image.

See more: [vertexai.preview.vision_models.ImageCaptioningModel.get_captions](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageCaptioningModel#vertexai_preview_vision_models_ImageCaptioningModel_get_captions)

### vertexai.preview.vision_models.ImageGenerationModel
    
    
    ImageGenerationModel(model_id: str, endpoint_name: typing.Optional[str] = None)

Creates a _ModelGardenModel.

See more: [vertexai.preview.vision_models.ImageGenerationModel](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageGenerationModel#vertexai_preview_vision_models_ImageGenerationModel_ImageGenerationModel)

### vertexai.preview.vision_models.ImageGenerationModel.edit_image
    
    
    edit_image(
        *,
        prompt: str,
        base_image: typing.Optional[vertexai.vision_models.Image] = None,
        mask: typing.Optional[vertexai.vision_models.Image] = None,
        reference_images: typing.Optional[
            typing.List[vertexai.vision_models.ReferenceImage]
        ] = None,
        negative_prompt: typing.Optional[str] = None,
        number_of_images: int = 1,
        guidance_scale: typing.Optional[float] = None,
        edit_mode: typing.Optional[
            typing.Literal[
                "inpainting-insert", "inpainting-remove", "outpainting", "product-image"
            ]
        ] = None,
        mask_mode: typing.Optional[
            typing.Literal["background", "foreground", "semantic"]
        ] = None,
        segmentation_classes: typing.Optional[typing.List[str]] = None,
        mask_dilation: typing.Optional[float] = None,
        product_position: typing.Optional[typing.Literal["fixed", "reposition"]] = None,
        output_mime_type: typing.Optional[typing.Literal["image/png", "image/jpeg"]] = None,
        compression_quality: typing.Optional[float] = None,
        language: typing.Optional[str] = None,
        seed: typing.Optional[int] = None,
        output_gcs_uri: typing.Optional[str] = None,
        safety_filter_level: typing.Optional[
            typing.Literal["block_most", "block_some", "block_few", "block_fewest"]
        ] = None,
        person_generation: typing.Optional[
            typing.Literal["dont_allow", "allow_adult", "allow_all"]
        ] = None
    ) -> vertexai.preview.vision_models.ImageGenerationResponse

Edits an existing image based on text prompt.

See more: [vertexai.preview.vision_models.ImageGenerationModel.edit_image](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageGenerationModel#vertexai_preview_vision_models_ImageGenerationModel_edit_image)

### vertexai.preview.vision_models.ImageGenerationModel.from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

See more: [vertexai.preview.vision_models.ImageGenerationModel.from_pretrained](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageGenerationModel#vertexai_preview_vision_models_ImageGenerationModel_from_pretrained)

### vertexai.preview.vision_models.ImageGenerationModel.generate_images
    
    
    generate_images(
        prompt: str,
        *,
        negative_prompt: typing.Optional[str] = None,
        number_of_images: int = 1,
        aspect_ratio: typing.Optional[
            typing.Literal["1:1", "9:16", "16:9", "4:3", "3:4"]
        ] = None,
        guidance_scale: typing.Optional[float] = None,
        language: typing.Optional[str] = None,
        seed: typing.Optional[int] = None,
        output_gcs_uri: typing.Optional[str] = None,
        add_watermark: typing.Optional[bool] = True,
        safety_filter_level: typing.Optional[
            typing.Literal["block_most", "block_some", "block_few", "block_fewest"]
        ] = None,
        person_generation: typing.Optional[
            typing.Literal["dont_allow", "allow_adult", "allow_all"]
        ] = None
    ) -> vertexai.preview.vision_models.ImageGenerationResponse

Generates images from text prompt.

See more: [vertexai.preview.vision_models.ImageGenerationModel.generate_images](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageGenerationModel#vertexai_preview_vision_models_ImageGenerationModel_generate_images)

### vertexai.preview.vision_models.ImageGenerationModel.upscale_image
    
    
    upscale_image(
        image: typing.Union[
            vertexai.vision_models.Image, vertexai.preview.vision_models.GeneratedImage
        ],
        new_size: typing.Optional[int] = 2048,
        upscale_factor: typing.Optional[typing.Literal["x2", "x4"]] = None,
        output_mime_type: typing.Optional[
            typing.Literal["image/png", "image/jpeg"]
        ] = "image/png",
        output_compression_quality: typing.Optional[int] = None,
        output_gcs_uri: typing.Optional[str] = None,
    ) -> vertexai.vision_models.Image

Upscales an image.

See more: [vertexai.preview.vision_models.ImageGenerationModel.upscale_image](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageGenerationModel#vertexai_preview_vision_models_ImageGenerationModel_upscale_image)

### vertexai.preview.vision_models.ImageGenerationResponse.__getitem__
    
    
    __getitem__(idx: int) -> vertexai.preview.vision_models.GeneratedImage

Gets the generated image by index.

See more: [vertexai.preview.vision_models.ImageGenerationResponse.**getitem**](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageGenerationResponse#vertexai_preview_vision_models_ImageGenerationResponse___getitem__)

### vertexai.preview.vision_models.ImageGenerationResponse.__iter__
    
    
    __iter__() -> typing.Iterator[vertexai.preview.vision_models.GeneratedImage]

Iterates through the generated images.

See more: [vertexai.preview.vision_models.ImageGenerationResponse.**iter**](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageGenerationResponse#vertexai_preview_vision_models_ImageGenerationResponse___iter__)

### vertexai.preview.vision_models.ImageQnAModel
    
    
    ImageQnAModel(model_id: str, endpoint_name: typing.Optional[str] = None)

Creates a _ModelGardenModel.

See more: [vertexai.preview.vision_models.ImageQnAModel](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageQnAModel#vertexai_preview_vision_models_ImageQnAModel_ImageQnAModel)

### vertexai.preview.vision_models.ImageQnAModel.ask_question
    
    
    ask_question(
        image: vertexai.vision_models.Image, question: str, *, number_of_results: int = 1
    ) -> typing.List[str]

Answers questions about an image.

See more: [vertexai.preview.vision_models.ImageQnAModel.ask_question](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageQnAModel#vertexai_preview_vision_models_ImageQnAModel_ask_question)

### vertexai.preview.vision_models.ImageQnAModel.from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

See more: [vertexai.preview.vision_models.ImageQnAModel.from_pretrained](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageQnAModel#vertexai_preview_vision_models_ImageQnAModel_from_pretrained)

### vertexai.preview.vision_models.ImageSegmentationModel
    
    
    ImageSegmentationModel(model_id: str, endpoint_name: typing.Optional[str] = None)

Creates a _ModelGardenModel.

See more: [vertexai.preview.vision_models.ImageSegmentationModel](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageSegmentationModel#vertexai_preview_vision_models_ImageSegmentationModel_ImageSegmentationModel)

### vertexai.preview.vision_models.ImageSegmentationModel.from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

See more: [vertexai.preview.vision_models.ImageSegmentationModel.from_pretrained](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageSegmentationModel#vertexai_preview_vision_models_ImageSegmentationModel_from_pretrained)

### vertexai.preview.vision_models.ImageSegmentationModel.segment_image
    
    
    segment_image(
        base_image: vertexai.vision_models.Image,
        prompt: typing.Optional[str] = None,
        scribble: typing.Optional[vertexai.preview.vision_models.Scribble] = None,
        mode: typing.Literal[
            "foreground", "background", "semantic", "prompt", "interactive"
        ] = "foreground",
        max_predictions: typing.Optional[int] = None,
        confidence_threshold: typing.Optional[float] = 0.1,
        mask_dilation: typing.Optional[float] = None,
        binary_color_threshold: typing.Optional[float] = None,
    ) -> vertexai.preview.vision_models.ImageSegmentationResponse

Segments an image.

See more: [vertexai.preview.vision_models.ImageSegmentationModel.segment_image](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageSegmentationModel#vertexai_preview_vision_models_ImageSegmentationModel_segment_image)

### vertexai.preview.vision_models.ImageSegmentationResponse.__getitem__
    
    
    __getitem__(idx: int) -> vertexai.preview.vision_models.GeneratedMask

Gets the generated masks by index.

See more: [vertexai.preview.vision_models.ImageSegmentationResponse.**getitem**](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageSegmentationResponse#vertexai_preview_vision_models_ImageSegmentationResponse___getitem__)

### vertexai.preview.vision_models.ImageSegmentationResponse.__iter__
    
    
    __iter__() -> typing.Iterator[vertexai.preview.vision_models.GeneratedMask]

Iterates through the generated masks.

See more: [vertexai.preview.vision_models.ImageSegmentationResponse.**iter**](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageSegmentationResponse#vertexai_preview_vision_models_ImageSegmentationResponse___iter__)

### vertexai.preview.vision_models.ImageTextModel
    
    
    ImageTextModel(model_id: str, endpoint_name: typing.Optional[str] = None)

Creates a _ModelGardenModel.

See more: [vertexai.preview.vision_models.ImageTextModel](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageTextModel#vertexai_preview_vision_models_ImageTextModel_ImageTextModel)

### vertexai.preview.vision_models.ImageTextModel.ask_question
    
    
    ask_question(
        image: vertexai.vision_models.Image, question: str, *, number_of_results: int = 1
    ) -> typing.List[str]

Answers questions about an image.

See more: [vertexai.preview.vision_models.ImageTextModel.ask_question](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageTextModel#vertexai_preview_vision_models_ImageTextModel_ask_question)

### vertexai.preview.vision_models.ImageTextModel.from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

See more: [vertexai.preview.vision_models.ImageTextModel.from_pretrained](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageTextModel#vertexai_preview_vision_models_ImageTextModel_from_pretrained)

### vertexai.preview.vision_models.ImageTextModel.get_captions
    
    
    get_captions(
        image: vertexai.vision_models.Image,
        *,
        number_of_results: int = 1,
        language: str = "en",
        output_gcs_uri: typing.Optional[str] = None
    ) -> typing.List[str]

Generates captions for a given image.

See more: [vertexai.preview.vision_models.ImageTextModel.get_captions](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ImageTextModel#vertexai_preview_vision_models_ImageTextModel_get_captions)

### vertexai.preview.vision_models.MaskReferenceImage
    
    
    MaskReferenceImage(
        reference_id,
        image: typing.Optional[
            typing.Union[bytes, vertexai.vision_models.Image, str]
        ] = None,
        mask_mode: typing.Optional[
            typing.Literal[
                "default", "user_provided", "background", "foreground", "semantic"
            ]
        ] = None,
        dilation: typing.Optional[float] = None,
        segmentation_classes: typing.Optional[typing.List[int]] = None,
    )

Creates a `MaskReferenceImage` object.

See more: [vertexai.preview.vision_models.MaskReferenceImage](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.MaskReferenceImage#vertexai_preview_vision_models_MaskReferenceImage_MaskReferenceImage)

### vertexai.preview.vision_models.MultiModalEmbeddingModel
    
    
    MultiModalEmbeddingModel(model_id: str, endpoint_name: typing.Optional[str] = None)

Creates a _ModelGardenModel.

See more: [vertexai.preview.vision_models.MultiModalEmbeddingModel](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.MultiModalEmbeddingModel#vertexai_preview_vision_models_MultiModalEmbeddingModel_MultiModalEmbeddingModel)

### vertexai.preview.vision_models.MultiModalEmbeddingModel.from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

See more: [vertexai.preview.vision_models.MultiModalEmbeddingModel.from_pretrained](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.MultiModalEmbeddingModel#vertexai_preview_vision_models_MultiModalEmbeddingModel_from_pretrained)

### vertexai.preview.vision_models.MultiModalEmbeddingModel.get_embeddings
    
    
    get_embeddings(
        image: typing.Optional[vertexai.vision_models.Image] = None,
        video: typing.Optional[vertexai.vision_models.Video] = None,
        contextual_text: typing.Optional[str] = None,
        dimension: typing.Optional[int] = None,
        video_segment_config: typing.Optional[
            vertexai.vision_models.VideoSegmentConfig
        ] = None,
    ) -> vertexai.vision_models.MultiModalEmbeddingResponse

Gets embedding vectors from the provided image.

See more: [vertexai.preview.vision_models.MultiModalEmbeddingModel.get_embeddings](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.MultiModalEmbeddingModel#vertexai_preview_vision_models_MultiModalEmbeddingModel_get_embeddings)

### vertexai.preview.vision_models.RawReferenceImage
    
    
    RawReferenceImage(
        reference_id,
        image: typing.Optional[
            typing.Union[bytes, vertexai.vision_models.Image, str]
        ] = None,
    )

Creates a `ReferenceImage` object.

See more: [vertexai.preview.vision_models.RawReferenceImage](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.RawReferenceImage#vertexai_preview_vision_models_RawReferenceImage_RawReferenceImage)

### vertexai.preview.vision_models.ReferenceImage
    
    
    ReferenceImage(
        reference_id,
        image: typing.Optional[
            typing.Union[bytes, vertexai.vision_models.Image, str]
        ] = None,
    )

Creates a `ReferenceImage` object.

See more: [vertexai.preview.vision_models.ReferenceImage](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.ReferenceImage#vertexai_preview_vision_models_ReferenceImage_ReferenceImage)

### vertexai.preview.vision_models.Scribble
    
    
    Scribble(image_bytes: typing.Optional[bytes], gcs_uri: typing.Optional[str] = None)

Creates a `Scribble` object.

See more: [vertexai.preview.vision_models.Scribble](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.Scribble#vertexai_preview_vision_models_Scribble_Scribble)

### vertexai.preview.vision_models.StyleReferenceImage
    
    
    StyleReferenceImage(
        reference_id,
        image: typing.Optional[
            typing.Union[bytes, vertexai.vision_models.Image, str]
        ] = None,
        style_description: typing.Optional[str] = None,
    )

Creates a `StyleReferenceImage` object.

See more: [vertexai.preview.vision_models.StyleReferenceImage](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.StyleReferenceImage#vertexai_preview_vision_models_StyleReferenceImage_StyleReferenceImage)

### vertexai.preview.vision_models.SubjectReferenceImage
    
    
    SubjectReferenceImage(
        reference_id,
        image: typing.Optional[
            typing.Union[bytes, vertexai.vision_models.Image, str]
        ] = None,
        subject_description: typing.Optional[str] = None,
        subject_type: typing.Optional[
            typing.Literal["default", "person", "animal", "product"]
        ] = None,
    )

Creates a `SubjectReferenceImage` object.

See more: [vertexai.preview.vision_models.SubjectReferenceImage](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.SubjectReferenceImage#vertexai_preview_vision_models_SubjectReferenceImage_SubjectReferenceImage)

### vertexai.preview.vision_models.Video
    
    
    Video(
        video_bytes: typing.Optional[bytes] = None, gcs_uri: typing.Optional[str] = None
    )

Creates a `Video` object.

See more: [vertexai.preview.vision_models.Video](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.Video#vertexai_preview_vision_models_Video_Video)

### vertexai.preview.vision_models.Video.load_from_file
    
    
    load_from_file(location: str) -> vertexai.vision_models.Video

Loads video from local file or Google Cloud Storage.

See more: [vertexai.preview.vision_models.Video.load_from_file](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.Video#vertexai_preview_vision_models_Video_load_from_file)

### vertexai.preview.vision_models.Video.save
    
    
    save(location: str)

Saves video to a file.

See more: [vertexai.preview.vision_models.Video.save](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.Video#vertexai_preview_vision_models_Video_save)

### vertexai.preview.vision_models.VideoEmbedding
    
    
    VideoEmbedding(
        start_offset_sec: int, end_offset_sec: int, embedding: typing.List[float]
    )

Creates a `VideoEmbedding` object.

See more: [vertexai.preview.vision_models.VideoEmbedding](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.VideoEmbedding#vertexai_preview_vision_models_VideoEmbedding_VideoEmbedding)

### vertexai.preview.vision_models.VideoSegmentConfig
    
    
    VideoSegmentConfig(
        start_offset_sec: int = 0, end_offset_sec: int = 120, interval_sec: int = 16
    )

Creates a `VideoSegmentConfig` object.

See more: [vertexai.preview.vision_models.VideoSegmentConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.VideoSegmentConfig#vertexai_preview_vision_models_VideoSegmentConfig_VideoSegmentConfig)

### vertexai.preview.vision_models.WatermarkVerificationModel
    
    
    WatermarkVerificationModel(
        model_id: str, endpoint_name: typing.Optional[str] = None
    )

Creates a _ModelGardenModel.

See more: [vertexai.preview.vision_models.WatermarkVerificationModel](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.WatermarkVerificationModel#vertexai_preview_vision_models_WatermarkVerificationModel_WatermarkVerificationModel)

### vertexai.preview.vision_models.WatermarkVerificationModel.from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

See more: [vertexai.preview.vision_models.WatermarkVerificationModel.from_pretrained](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.WatermarkVerificationModel#vertexai_preview_vision_models_WatermarkVerificationModel_from_pretrained)

### vertexai.preview.vision_models.WatermarkVerificationModel.verify_image
    
    
    verify_image(
        image: vertexai.vision_models.Image,
    ) -> vertexai.preview.vision_models.WatermarkVerificationResponse

Verifies the watermark of an image.

See more: [vertexai.preview.vision_models.WatermarkVerificationModel.verify_image](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.preview.vision_models.WatermarkVerificationModel#vertexai_preview_vision_models_WatermarkVerificationModel_verify_image)

### vertexai.resources.preview.ml_monitoring.ModelMonitor
    
    
    ModelMonitor(
        model_monitor_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Initializes class with project, location, and api_client.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_ModelMonitor)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.create
    
    
    create(
        model_name: str,
        model_version_id: str,
        training_dataset: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.MonitoringInput
        ] = None,
        display_name: typing.Optional[str] = None,
        model_monitoring_schema: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.schema.ModelMonitoringSchema
        ] = None,
        tabular_objective_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.TabularObjective
        ] = None,
        output_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.output.OutputSpec
        ] = None,
        notification_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.notification.NotificationSpec
        ] = None,
        explanation_spec: typing.Optional[
            google.cloud.aiplatform_v1beta1.types.explanation.ExplanationSpec
        ] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        model_monitor_id: typing.Optional[str] = None,
    ) -> vertexai.resources.preview.ml_monitoring.model_monitors.ModelMonitor

Creates a new ModelMonitor.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.create](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_create)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.create_schedule
    
    
    create_schedule(
        cron: str,
        target_dataset: vertexai.resources.preview.ml_monitoring.spec.objective.MonitoringInput,
        display_name: typing.Optional[str] = None,
        model_monitoring_job_display_name: typing.Optional[str] = None,
        start_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        end_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        tabular_objective_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.TabularObjective
        ] = None,
        baseline_dataset: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.MonitoringInput
        ] = None,
        output_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.output.OutputSpec
        ] = None,
        notification_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.notification.NotificationSpec
        ] = None,
        explanation_spec: typing.Optional[
            google.cloud.aiplatform_v1beta1.types.explanation.ExplanationSpec
        ] = None,
    ) -> google.cloud.aiplatform_v1beta1.types.schedule.Schedule

Creates a new Scheduled run for model monitoring job.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.create_schedule](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_create_schedule)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.delete
    
    
    delete(force: bool = False, sync: bool = True) -> None

Force delete the model monitor.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.delete](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_delete)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.delete_model_monitoring_job
    
    
    delete_model_monitoring_job(model_monitoring_job_name: str) -> None

Delete a model monitoring job.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.delete_model_monitoring_job](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_delete_model_monitoring_job)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.delete_schedule
    
    
    delete_schedule(schedule_name: str) -> None

Deletes an existing Schedule.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.delete_schedule](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_delete_schedule)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.get_model_monitoring_job
    
    
    get_model_monitoring_job(
        model_monitoring_job_name: str,
    ) -> vertexai.resources.preview.ml_monitoring.model_monitors.ModelMonitoringJob

Get the specified ModelMonitoringJob.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.get_model_monitoring_job](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_get_model_monitoring_job)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.get_schedule
    
    
    get_schedule(
        schedule_name: str,
    ) -> google.cloud.aiplatform_v1beta1.types.schedule.Schedule

Gets an existing Schedule.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.get_schedule](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_get_schedule)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.get_schema
    
    
    get_schema() -> (
        google.cloud.aiplatform_v1beta1.types.model_monitor.ModelMonitoringSchema
    )

Get the schema of the model monitor.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.get_schema](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_get_schema)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.list
    
    
    list(
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        parent: typing.Optional[str] = None,
    ) -> typing.List[google.cloud.aiplatform.base.VertexAiResourceNoun]

List all instances of this Vertex AI Resource.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_list)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.list_jobs
    
    
    list_jobs(
        page_size: typing.Optional[int] = None, page_token: typing.Optional[str] = None
    ) -> ListJobsResponse.list_jobs

List ModelMonitoringJobs.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.list_jobs](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_list_jobs)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.list_schedules
    
    
    list_schedules(
        filter: typing.Optional[str] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
    ) -> ListSchedulesResponse.list_schedules

List Schedules.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.list_schedules](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_list_schedules)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.pause_schedule
    
    
    pause_schedule(schedule_name: str) -> None

Pauses an existing Schedule.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.pause_schedule](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_pause_schedule)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.resume_schedule
    
    
    resume_schedule(schedule_name: str) -> None

Resumes an existing Schedule.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.resume_schedule](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_resume_schedule)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.run
    
    
    run(
        target_dataset: vertexai.resources.preview.ml_monitoring.spec.objective.MonitoringInput,
        display_name: typing.Optional[str] = None,
        model_monitoring_job_id: typing.Optional[str] = None,
        sync: typing.Optional[bool] = False,
        tabular_objective_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.TabularObjective
        ] = None,
        baseline_dataset: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.MonitoringInput
        ] = None,
        output_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.output.OutputSpec
        ] = None,
        notification_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.notification.NotificationSpec
        ] = None,
        explanation_spec: typing.Optional[
            google.cloud.aiplatform_v1beta1.types.explanation.ExplanationSpec
        ] = None,
    ) -> vertexai.resources.preview.ml_monitoring.model_monitors.ModelMonitoringJob

Creates a new ModelMonitoringJob.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.run](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_run)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.search_alerts
    
    
    search_alerts(
        stats_name: typing.Optional[str] = None,
        objective_type: typing.Optional[str] = None,
        model_monitoring_job_name: typing.Optional[str] = None,
        start_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        end_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
    ) -> typing.Dict[str, typing.Any]

Search ModelMonitoringAlerts.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.search_alerts](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_search_alerts)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.search_metrics
    
    
    search_metrics(
        stats_name: typing.Optional[str] = None,
        objective_type: typing.Optional[str] = None,
        model_monitoring_job_name: typing.Optional[str] = None,
        schedule_name: typing.Optional[str] = None,
        algorithm: typing.Optional[str] = None,
        start_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        end_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
        page_size: typing.Optional[int] = None,
        page_token: typing.Optional[str] = None,
    ) -> MetricsSearchResponse.monitoring_stats

Search ModelMonitoringStats.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.search_metrics](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_search_metrics)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.show_feature_attribution_drift_stats
    
    
    show_feature_attribution_drift_stats(model_monitoring_job_name: str) -> None

The method to visualize the feature attribution drift result from a model monitoring job as a histogram chart and a table.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.show_feature_attribution_drift_stats](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_show_feature_attribution_drift_stats)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.show_feature_drift_stats
    
    
    show_feature_drift_stats(model_monitoring_job_name: str) -> None

The method to visualize the feature drift result from a model monitoring job as a histogram chart and a table.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.show_feature_drift_stats](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_show_feature_drift_stats)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.show_output_drift_stats
    
    
    show_output_drift_stats(model_monitoring_job_name: str) -> None

The method to visualize the prediction output drift result from a model monitoring job as a histogram chart and a table.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.show_output_drift_stats](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_show_output_drift_stats)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.to_dict](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_to_dict)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.update
    
    
    update(
        display_name: typing.Optional[str] = None,
        training_dataset: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.MonitoringInput
        ] = None,
        model_monitoring_schema: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.schema.ModelMonitoringSchema
        ] = None,
        tabular_objective_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.TabularObjective
        ] = None,
        output_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.output.OutputSpec
        ] = None,
        notification_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.notification.NotificationSpec
        ] = None,
        explanation_spec: typing.Optional[
            google.cloud.aiplatform_v1beta1.types.explanation.ExplanationSpec
        ] = None,
    ) -> vertexai.resources.preview.ml_monitoring.model_monitors.ModelMonitor

Updates an existing ModelMonitor.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.update](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_update)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.update_schedule
    
    
    update_schedule(
        schedule_name: str,
        display_name: typing.Optional[str] = None,
        model_monitoring_job_display_name: typing.Optional[str] = None,
        cron: typing.Optional[str] = None,
        baseline_dataset: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.MonitoringInput
        ] = None,
        target_dataset: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.MonitoringInput
        ] = None,
        tabular_objective_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.TabularObjective
        ] = None,
        output_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.output.OutputSpec
        ] = None,
        notification_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.notification.NotificationSpec
        ] = None,
        explanation_spec: typing.Optional[
            google.cloud.aiplatform_v1beta1.types.explanation.ExplanationSpec
        ] = None,
        end_time: typing.Optional[google.protobuf.timestamp_pb2.Timestamp] = None,
    ) -> google.cloud.aiplatform_v1beta1.types.schedule.Schedule

Updates an existing Schedule.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.update_schedule](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_update_schedule)

### vertexai.resources.preview.ml_monitoring.ModelMonitor.wait
    
    
    wait()

Helper method that blocks until all futures are complete.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitor.wait](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitor#vertexai_resources_preview_ml_monitoring_ModelMonitor_wait)

### vertexai.resources.preview.ml_monitoring.ModelMonitoringJob
    
    
    ModelMonitoringJob(
        model_monitoring_job_name: str,
        model_monitor_id: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Initializes class with project, location, and api_client.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitoringJob](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitoringJob#vertexai_resources_preview_ml_monitoring_ModelMonitoringJob_ModelMonitoringJob)

### vertexai.resources.preview.ml_monitoring.ModelMonitoringJob.create
    
    
    create(
        model_monitor_name: typing.Optional[str] = None,
        target_dataset: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.MonitoringInput
        ] = None,
        display_name: typing.Optional[str] = None,
        model_monitoring_job_id: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        baseline_dataset: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.MonitoringInput
        ] = None,
        tabular_objective_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.objective.TabularObjective
        ] = None,
        output_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.output.OutputSpec
        ] = None,
        notification_spec: typing.Optional[
            vertexai.resources.preview.ml_monitoring.spec.notification.NotificationSpec
        ] = None,
        explanation_spec: typing.Optional[
            google.cloud.aiplatform_v1beta1.types.explanation.ExplanationSpec
        ] = None,
        sync: bool = False,
    ) -> vertexai.resources.preview.ml_monitoring.model_monitors.ModelMonitoringJob

Creates a new ModelMonitoringJob.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitoringJob.create](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitoringJob#vertexai_resources_preview_ml_monitoring_ModelMonitoringJob_create)

### vertexai.resources.preview.ml_monitoring.ModelMonitoringJob.delete
    
    
    delete() -> None

Deletes an Model Monitoring Job.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitoringJob.delete](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitoringJob#vertexai_resources_preview_ml_monitoring_ModelMonitoringJob_delete)

### vertexai.resources.preview.ml_monitoring.ModelMonitoringJob.done
    
    
    done() -> bool

Method indicating whether a job has completed.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitoringJob.done](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitoringJob#vertexai_resources_preview_ml_monitoring_ModelMonitoringJob_done)

### vertexai.resources.preview.ml_monitoring.ModelMonitoringJob.list
    
    
    list(
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        parent: typing.Optional[str] = None,
    ) -> typing.List[google.cloud.aiplatform.base.VertexAiResourceNoun]

List all instances of this Vertex AI Resource.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitoringJob.list](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitoringJob#vertexai_resources_preview_ml_monitoring_ModelMonitoringJob_list)

### vertexai.resources.preview.ml_monitoring.ModelMonitoringJob.to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitoringJob.to_dict](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitoringJob#vertexai_resources_preview_ml_monitoring_ModelMonitoringJob_to_dict)

### vertexai.resources.preview.ml_monitoring.ModelMonitoringJob.wait
    
    
    wait()

Helper method that blocks until all futures are complete.

See more: [vertexai.resources.preview.ml_monitoring.ModelMonitoringJob.wait](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.ModelMonitoringJob#vertexai_resources_preview_ml_monitoring_ModelMonitoringJob_wait)

### vertexai.resources.preview.ml_monitoring.spec.ModelMonitoringSchema.to_json
    
    
    to_json(output_dir: typing.Optional[str] = None) -> str

Transform ModelMonitoringSchema to json format.

See more: [vertexai.resources.preview.ml_monitoring.spec.ModelMonitoringSchema.to_json](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.resources.preview.ml_monitoring.spec.ModelMonitoringSchema#vertexai_resources_preview_ml_monitoring_spec_ModelMonitoringSchema_to_json)

### vertexai.vision_models.GeneratedImage
    
    
    GeneratedImage(
        image_bytes: typing.Optional[bytes],
        generation_parameters: typing.Dict[str, typing.Any],
        gcs_uri: typing.Optional[str] = None,
    )

Creates a `GeneratedImage` object.

See more: [vertexai.vision_models.GeneratedImage](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.GeneratedImage#vertexai_vision_models_GeneratedImage_GeneratedImage)

### vertexai.vision_models.GeneratedImage.load_from_file
    
    
    load_from_file(location: str) -> vertexai.preview.vision_models.GeneratedImage

Loads image from file.

See more: [vertexai.vision_models.GeneratedImage.load_from_file](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.GeneratedImage#vertexai_vision_models_GeneratedImage_load_from_file)

### vertexai.vision_models.GeneratedImage.save
    
    
    save(location: str, include_generation_parameters: bool = True)

Saves image to a file.

See more: [vertexai.vision_models.GeneratedImage.save](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.GeneratedImage#vertexai_vision_models_GeneratedImage_save)

### vertexai.vision_models.GeneratedImage.show
    
    
    show()

Shows the image.

See more: [vertexai.vision_models.GeneratedImage.show](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.GeneratedImage#vertexai_vision_models_GeneratedImage_show)

### vertexai.vision_models.Image
    
    
    Image(
        image_bytes: typing.Optional[bytes] = None, gcs_uri: typing.Optional[str] = None
    )

Creates an `Image` object.

See more: [vertexai.vision_models.Image](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.Image#vertexai_vision_models_Image_Image)

### vertexai.vision_models.Image.load_from_file
    
    
    load_from_file(location: str) -> vertexai.vision_models.Image

Loads image from local file or Google Cloud Storage.

See more: [vertexai.vision_models.Image.load_from_file](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.Image#vertexai_vision_models_Image_load_from_file)

### vertexai.vision_models.Image.save
    
    
    save(location: str)

Saves image to a file.

See more: [vertexai.vision_models.Image.save](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.Image#vertexai_vision_models_Image_save)

### vertexai.vision_models.Image.show
    
    
    show()

Shows the image.

See more: [vertexai.vision_models.Image.show](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.Image#vertexai_vision_models_Image_show)

### vertexai.vision_models.ImageCaptioningModel
    
    
    ImageCaptioningModel(model_id: str, endpoint_name: typing.Optional[str] = None)

Creates a _ModelGardenModel.

See more: [vertexai.vision_models.ImageCaptioningModel](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.ImageCaptioningModel#vertexai_vision_models_ImageCaptioningModel_ImageCaptioningModel)

### vertexai.vision_models.ImageCaptioningModel.from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

See more: [vertexai.vision_models.ImageCaptioningModel.from_pretrained](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.ImageCaptioningModel#vertexai_vision_models_ImageCaptioningModel_from_pretrained)

### vertexai.vision_models.ImageCaptioningModel.get_captions
    
    
    get_captions(
        image: vertexai.vision_models.Image,
        *,
        number_of_results: int = 1,
        language: str = "en",
        output_gcs_uri: typing.Optional[str] = None
    ) -> typing.List[str]

Generates captions for a given image.

See more: [vertexai.vision_models.ImageCaptioningModel.get_captions](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.ImageCaptioningModel#vertexai_vision_models_ImageCaptioningModel_get_captions)

### vertexai.vision_models.ImageGenerationModel
    
    
    ImageGenerationModel(model_id: str, endpoint_name: typing.Optional[str] = None)

Creates a _ModelGardenModel.

See more: [vertexai.vision_models.ImageGenerationModel](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.ImageGenerationModel#vertexai_vision_models_ImageGenerationModel_ImageGenerationModel)

### vertexai.vision_models.ImageGenerationModel.edit_image
    
    
    edit_image(
        *,
        prompt: str,
        base_image: typing.Optional[vertexai.vision_models.Image] = None,
        mask: typing.Optional[vertexai.vision_models.Image] = None,
        reference_images: typing.Optional[
            typing.List[vertexai.vision_models.ReferenceImage]
        ] = None,
        negative_prompt: typing.Optional[str] = None,
        number_of_images: int = 1,
        guidance_scale: typing.Optional[float] = None,
        edit_mode: typing.Optional[
            typing.Literal[
                "inpainting-insert", "inpainting-remove", "outpainting", "product-image"
            ]
        ] = None,
        mask_mode: typing.Optional[
            typing.Literal["background", "foreground", "semantic"]
        ] = None,
        segmentation_classes: typing.Optional[typing.List[str]] = None,
        mask_dilation: typing.Optional[float] = None,
        product_position: typing.Optional[typing.Literal["fixed", "reposition"]] = None,
        output_mime_type: typing.Optional[typing.Literal["image/png", "image/jpeg"]] = None,
        compression_quality: typing.Optional[float] = None,
        language: typing.Optional[str] = None,
        seed: typing.Optional[int] = None,
        output_gcs_uri: typing.Optional[str] = None,
        safety_filter_level: typing.Optional[
            typing.Literal["block_most", "block_some", "block_few", "block_fewest"]
        ] = None,
        person_generation: typing.Optional[
            typing.Literal["dont_allow", "allow_adult", "allow_all"]
        ] = None
    ) -> vertexai.preview.vision_models.ImageGenerationResponse

Edits an existing image based on text prompt.

See more: [vertexai.vision_models.ImageGenerationModel.edit_image](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.ImageGenerationModel#vertexai_vision_models_ImageGenerationModel_edit_image)

### vertexai.vision_models.ImageGenerationModel.from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

See more: [vertexai.vision_models.ImageGenerationModel.from_pretrained](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.ImageGenerationModel#vertexai_vision_models_ImageGenerationModel_from_pretrained)

### vertexai.vision_models.ImageGenerationModel.generate_images
    
    
    generate_images(
        prompt: str,
        *,
        negative_prompt: typing.Optional[str] = None,
        number_of_images: int = 1,
        aspect_ratio: typing.Optional[
            typing.Literal["1:1", "9:16", "16:9", "4:3", "3:4"]
        ] = None,
        guidance_scale: typing.Optional[float] = None,
        language: typing.Optional[str] = None,
        seed: typing.Optional[int] = None,
        output_gcs_uri: typing.Optional[str] = None,
        add_watermark: typing.Optional[bool] = True,
        safety_filter_level: typing.Optional[
            typing.Literal["block_most", "block_some", "block_few", "block_fewest"]
        ] = None,
        person_generation: typing.Optional[
            typing.Literal["dont_allow", "allow_adult", "allow_all"]
        ] = None
    ) -> vertexai.preview.vision_models.ImageGenerationResponse

Generates images from text prompt.

See more: [vertexai.vision_models.ImageGenerationModel.generate_images](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.ImageGenerationModel#vertexai_vision_models_ImageGenerationModel_generate_images)

### vertexai.vision_models.ImageGenerationModel.upscale_image
    
    
    upscale_image(
        image: typing.Union[
            vertexai.vision_models.Image, vertexai.preview.vision_models.GeneratedImage
        ],
        new_size: typing.Optional[int] = 2048,
        upscale_factor: typing.Optional[typing.Literal["x2", "x4"]] = None,
        output_mime_type: typing.Optional[
            typing.Literal["image/png", "image/jpeg"]
        ] = "image/png",
        output_compression_quality: typing.Optional[int] = None,
        output_gcs_uri: typing.Optional[str] = None,
    ) -> vertexai.vision_models.Image

Upscales an image.

See more: [vertexai.vision_models.ImageGenerationModel.upscale_image](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.ImageGenerationModel#vertexai_vision_models_ImageGenerationModel_upscale_image)

### vertexai.vision_models.ImageGenerationResponse.__getitem__
    
    
    __getitem__(idx: int) -> vertexai.preview.vision_models.GeneratedImage

Gets the generated image by index.

See more: [vertexai.vision_models.ImageGenerationResponse.**getitem**](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.ImageGenerationResponse#vertexai_vision_models_ImageGenerationResponse___getitem__)

### vertexai.vision_models.ImageGenerationResponse.__iter__
    
    
    __iter__() -> typing.Iterator[vertexai.preview.vision_models.GeneratedImage]

Iterates through the generated images.

See more: [vertexai.vision_models.ImageGenerationResponse.**iter**](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.ImageGenerationResponse#vertexai_vision_models_ImageGenerationResponse___iter__)

### vertexai.vision_models.ImageQnAModel
    
    
    ImageQnAModel(model_id: str, endpoint_name: typing.Optional[str] = None)

Creates a _ModelGardenModel.

See more: [vertexai.vision_models.ImageQnAModel](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.ImageQnAModel#vertexai_vision_models_ImageQnAModel_ImageQnAModel)

### vertexai.vision_models.ImageQnAModel.ask_question
    
    
    ask_question(
        image: vertexai.vision_models.Image, question: str, *, number_of_results: int = 1
    ) -> typing.List[str]

Answers questions about an image.

See more: [vertexai.vision_models.ImageQnAModel.ask_question](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.ImageQnAModel#vertexai_vision_models_ImageQnAModel_ask_question)

### vertexai.vision_models.ImageQnAModel.from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

See more: [vertexai.vision_models.ImageQnAModel.from_pretrained](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.ImageQnAModel#vertexai_vision_models_ImageQnAModel_from_pretrained)

### vertexai.vision_models.ImageTextModel
    
    
    ImageTextModel(model_id: str, endpoint_name: typing.Optional[str] = None)

Creates a _ModelGardenModel.

See more: [vertexai.vision_models.ImageTextModel](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.ImageTextModel#vertexai_vision_models_ImageTextModel_ImageTextModel)

### vertexai.vision_models.ImageTextModel.ask_question
    
    
    ask_question(
        image: vertexai.vision_models.Image, question: str, *, number_of_results: int = 1
    ) -> typing.List[str]

Answers questions about an image.

See more: [vertexai.vision_models.ImageTextModel.ask_question](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.ImageTextModel#vertexai_vision_models_ImageTextModel_ask_question)

### vertexai.vision_models.ImageTextModel.from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

See more: [vertexai.vision_models.ImageTextModel.from_pretrained](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.ImageTextModel#vertexai_vision_models_ImageTextModel_from_pretrained)

### vertexai.vision_models.ImageTextModel.get_captions
    
    
    get_captions(
        image: vertexai.vision_models.Image,
        *,
        number_of_results: int = 1,
        language: str = "en",
        output_gcs_uri: typing.Optional[str] = None
    ) -> typing.List[str]

Generates captions for a given image.

See more: [vertexai.vision_models.ImageTextModel.get_captions](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.ImageTextModel#vertexai_vision_models_ImageTextModel_get_captions)

### vertexai.vision_models.MultiModalEmbeddingModel
    
    
    MultiModalEmbeddingModel(model_id: str, endpoint_name: typing.Optional[str] = None)

Creates a _ModelGardenModel.

See more: [vertexai.vision_models.MultiModalEmbeddingModel](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.MultiModalEmbeddingModel#vertexai_vision_models_MultiModalEmbeddingModel_MultiModalEmbeddingModel)

### vertexai.vision_models.MultiModalEmbeddingModel.from_pretrained
    
    
    from_pretrained(model_name: str) -> vertexai._model_garden._model_garden_models.T

Loads a _ModelGardenModel.

See more: [vertexai.vision_models.MultiModalEmbeddingModel.from_pretrained](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.MultiModalEmbeddingModel#vertexai_vision_models_MultiModalEmbeddingModel_from_pretrained)

### vertexai.vision_models.MultiModalEmbeddingModel.get_embeddings
    
    
    get_embeddings(
        image: typing.Optional[vertexai.vision_models.Image] = None,
        video: typing.Optional[vertexai.vision_models.Video] = None,
        contextual_text: typing.Optional[str] = None,
        dimension: typing.Optional[int] = None,
        video_segment_config: typing.Optional[
            vertexai.vision_models.VideoSegmentConfig
        ] = None,
    ) -> vertexai.vision_models.MultiModalEmbeddingResponse

Gets embedding vectors from the provided image.

See more: [vertexai.vision_models.MultiModalEmbeddingModel.get_embeddings](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.MultiModalEmbeddingModel#vertexai_vision_models_MultiModalEmbeddingModel_get_embeddings)

### vertexai.vision_models.Video
    
    
    Video(
        video_bytes: typing.Optional[bytes] = None, gcs_uri: typing.Optional[str] = None
    )

Creates a `Video` object.

See more: [vertexai.vision_models.Video](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.Video#vertexai_vision_models_Video_Video)

### vertexai.vision_models.Video.load_from_file
    
    
    load_from_file(location: str) -> vertexai.vision_models.Video

Loads video from local file or Google Cloud Storage.

See more: [vertexai.vision_models.Video.load_from_file](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.Video#vertexai_vision_models_Video_load_from_file)

### vertexai.vision_models.Video.save
    
    
    save(location: str)

Saves video to a file.

See more: [vertexai.vision_models.Video.save](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.Video#vertexai_vision_models_Video_save)

### vertexai.vision_models.VideoEmbedding
    
    
    VideoEmbedding(
        start_offset_sec: int, end_offset_sec: int, embedding: typing.List[float]
    )

Creates a `VideoEmbedding` object.

See more: [vertexai.vision_models.VideoEmbedding](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.VideoEmbedding#vertexai_vision_models_VideoEmbedding_VideoEmbedding)

### vertexai.vision_models.VideoSegmentConfig
    
    
    VideoSegmentConfig(
        start_offset_sec: int = 0, end_offset_sec: int = 120, interval_sec: int = 16
    )

Creates a `VideoSegmentConfig` object.

See more: [vertexai.vision_models.VideoSegmentConfig](https://cloud.google.com/python/docs/reference/aiplatform/latest/vertexai.vision_models.VideoSegmentConfig#vertexai_vision_models_VideoSegmentConfig_VideoSegmentConfig)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
