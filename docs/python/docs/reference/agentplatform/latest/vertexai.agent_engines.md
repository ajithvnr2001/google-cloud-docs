---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines
title: Package agent_engines (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:01.558017+00:00
---

# Package agent_engines (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package agent_engines (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 

API documentation for `agent_engines` package.

## Classes 

### [AG2Agent](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.AG2Agent)

An AG2 Agent.

### [AdkApp](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.AdkApp)

An ADK Application.

### [AgentEngine](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.AgentEngine)

Represents a Vertex AI Agent Engine resource.

### [AsyncQueryable](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.AsyncQueryable)

Protocol for Agent Engines that can be queried asynchronously.

### [AsyncStreamQueryable](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.AsyncStreamQueryable)

Protocol for Agent Engines that can stream responses asynchronously.

### [Cloneable](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.Cloneable)

Protocol for Agent Engines that can be cloned.

### [LangchainAgent](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.LangchainAgent)

A Langchain Agent.

See <https://cloud.google.com/vertex-ai/generative-ai/docs/reasoning-engine/develop> for details.

### [LanggraphAgent](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.LanggraphAgent)

A LangGraph Agent.

### [ModuleAgent](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.ModuleAgent)

Agent that is defined by a module and an agent name.

This agent is instantiated by importing a module and instantiating an agent from that module. It also allows to register operations that are defined in the agent.

### [OperationRegistrable](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.OperationRegistrable)

Protocol for agents that have registered operations.

### [Queryable](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.Queryable)

Protocol for Agent Engines that can be queried.

### [StreamQueryable](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.StreamQueryable)

Protocol for Agent Engines that can stream responses.

## Packages Functions 

### create
    
    
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

The Agent Engine will be an instance of the `agent_engine` that was passed in, running remotely on Vertex AI.

Sample `src_dir` contents (e.g. `./user_src_dir`):
    
    
    user_src_dir/
    |-- main.py
    |-- requirements.txt
    |-- user_code/
    |   |-- utils.py
    |   |-- ...
    |-- installation_scripts/
    |   |-- install_package.sh
    |   |-- ...
    |-- ...
    

To build an Agent Engine with the above files, run:
    
    
    remote_agent = agent_engines.create(
        agent_engine=local_agent,
        requirements=[
            # I.e. the PyPI dependencies listed in requirements.txt
            "google-cloud-aiplatform==1.25.0",
            "langchain==0.0.242",
            ...
        ],
        extra_packages=[
            "./user_src_dir/main.py", # a single file
            "./user_src_dir/user_code", # a directory
            ...
        ],
        build_options={
            "installation": [
                "./user_src_dir/installation_scripts/install_package.sh",
                ...
            ],
        },
    )
    

**Parameters**  
---  
**Name** | **Description**  
`agent_engine` | `AgentEngineInterface`  
Required. The Agent Engine to be created.  
`requirements` | `Union[str, Sequence[str]]`  
Optional. The set of PyPI dependencies needed. It can either be the path to a single file (requirements.txt), or an ordered list of strings corresponding to each line of the requirements file.  
`display_name` | `str`  
Optional. The user-defined name of the Agent Engine. The name can be up to 128 characters long and can comprise any UTF-8 character.  
`description` | `str`  
Optional. The description of the Agent Engine.  
`gcs_dir_name` | `str`  
Optional. The GCS bucket directory under `staging_bucket` to use for staging the artifacts needed.  
`extra_packages` | `Sequence[str]`  
Optional. The set of extra user-provided packages (if any).  
`env_vars` | `Union[Sequence[str], Dict[str, Union[str, SecretRef]]]`  
Optional. The environment variables to be set when running the Agent Engine. If it is a list of strings, each string should be a valid key to `os.environ`. If it is a dictionary, the keys are the environment variable names, and the values are the corresponding values.  
`build_options` | `Dict[str, Sequence[str]]`  
Optional. The build options for the Agent Engine. This includes options such as installation scripts.  
`service_account` | `str`  
Optional. The service account to be used for the Agent Engine. If not specified, the default reasoning engine service agent service account will be used.  
`identity_type` | `Union[str, ReasoningEngineSpec.IdentityType]`  
Optional. The identity type to be used by the Agent Engine at runtime. Set it to `AGENT_IDENTITY` to run the Agent Engine under a resource-scoped workload identity with no default project permissions, instead of the shared Reasoning Engine Service Agent. `service_account` must not be specified when `AGENT_IDENTITY` is used. If not specified, `service_account` is used if set, otherwise the default Reasoning Engine Service Agent is used.  
`psc_interface_config` | `PscInterfaceConfig`  
Optional. The PSC interface config for the Agent Engine. If not specified, the default PSC interface config will be used.  
`min_instances` | `int`  
Optional. The minimum number of instances to run the Agent Engine. If not specified, the default value will be used.  
`max_instances` | `int`  
Optional. The maximum number of instances to run the Agent Engine. If not specified, the default value will be used.  
`resource_limits` | `Dict[str, str]`  
Optional. The resource limits for the Agent Engine. If not specified, the default value will be used.  
`container_concurrency` | `int`  
Optional. The container concurrency for the Agent Engine. If not specified, the default value will be used.  
`encryption_spec` | `EncryptionSpec`  
Optional. The encryption spec for the Agent Engine. If not specified, the default encryption spec will be used.  
  
### delete
    
    
    delete(resource_name: str, *, force: bool = False, **kwargs) -> None

Delete an Agent Engine resource.

**Parameters**  
---  
**Name** | **Description**  
`resource_name` | `str`  
Required. The name of the Agent Engine to be deleted. Format: `projects/{project}/locations/{location}/reasoningEngines/{resource_id}`  
`force` | `bool`  
Optional. If set to True, child resources will also be deleted. Otherwise, the request will fail with FAILED_PRECONDITION error when the Agent Engine has undeleted child resources. Defaults to False.  
`\*\*kwargs` | `dict[str, Any]`  
Optional. Additional keyword arguments to pass to the delete_reasoning_engine method.  
  
### get
    
    
    get(resource_name: str) -> vertexai.agent_engines.AgentEngine

Retrieves an Agent Engine resource.

**Parameter**  
---  
**Name** | **Description**  
`resource_name` | `str`  
Required. A fully-qualified resource name or ID such as "projects/123/locations/us-central1/reasoningEngines/456" or "456" when project and location are initialized or passed.  
  
### list
    
    
    list(*, filter: str = "") -> typing.Iterable[vertexai.agent_engines.AgentEngine]

List all instances of Agent Engine matching the filter.

Example Usage:
    
    
        import [vertexai](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest)
        from vertexai import [agent_engines](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.agent_engines.html)
    <xref uid="vertexai.init">vertexai.init</xref>(project="my_project", location="us-central1")
    [agent_engines](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai._genai.agent_engines.html).[list](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.html)(filter='display_name="My Custom Agent"')
    

**Parameter**  
---  
**Name** | **Description**  
`filter` | `str`  
Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported.  
  
### update
    
    
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

This method updates the configuration of a deployed Agent Engine, identified by its resource name. Unlike the `create` function which requires an `agent_engine` object, all arguments in this method are optional. This method allows you to modify individual aspects of the configuration by providing any of the optional arguments.

**Parameters**  
---  
**Name** | **Description**  
`resource_name` | `str`  
Required. The name of the Agent Engine to be updated. Format: `projects/{project}/locations/{location}/reasoningEngines/{resource_id}`.  
`agent_engine` | `AgentEngineInterface`  
Optional. The instance to be used as the updated Agent Engine. If it is not specified, the existing instance will be used.  
`requirements` | `Union[str, Sequence[str]]`  
Optional. The set of PyPI dependencies needed. It can either be the path to a single file (requirements.txt), or an ordered list of strings corresponding to each line of the requirements file. If it is not specified, the existing requirements will be used. If it is set to an empty string or list, the existing requirements will be removed.  
`display_name` | `str`  
Optional. The user-defined name of the Agent Engine. The name can be up to 128 characters long and can comprise any UTF-8 character.  
`description` | `str`  
Optional. The description of the Agent Engine.  
`gcs_dir_name` | `str`  
Optional. The GCS bucket directory under `staging_bucket` to use for staging the artifacts needed.  
`extra_packages` | `Sequence[str]`  
Optional. The set of extra user-provided packages (if any). If it is not specified, the existing extra packages will be used. If it is set to an empty list, the existing extra packages will be removed.  
`env_vars` | `Union[Sequence[str], Dict[str, Union[str, SecretRef]]]`  
Optional. The environment variables to be set when running the Agent Engine. If it is a list of strings, each string should be a valid key to `os.environ`. If it is a dictionary, the keys are the environment variable names, and the values are the corresponding values.  
`build_options` | `Dict[str, Sequence[str]]`  
Optional. The build options for the Agent Engine. This includes options such as installation scripts.  
`service_account` | `str`  
Optional. The service account to be used for the Agent Engine. If not specified, the default reasoning engine service agent service account will be used.  
`identity_type` | `Union[str, ReasoningEngineSpec.IdentityType]`  
Optional. The identity type to be used by the Agent Engine at runtime. Set it to `AGENT_IDENTITY` to run the Agent Engine under a resource-scoped workload identity with no default project permissions, instead of the shared Reasoning Engine Service Agent. `service_account` must not be specified when `AGENT_IDENTITY` is used. If not specified, the existing identity type will be used.  
`min_instances` | `int`  
Optional. The minimum number of instances to run the Agent Engine. If not specified, the default value will be used.  
`max_instances` | `int`  
Optional. The maximum number of instances to run the Agent Engine. If not specified, the default value will be used.  
`resource_limits` | `Dict[str, str]`  
Optional. The resource limits for the Agent Engine. If not specified, the default value will be used.  
`container_concurrency` | `int`  
Optional. The container concurrency for the Agent Engine. If not specified, the default value will be used.  
`encryption_spec` | `EncryptionSpec`  
Optional. The encryption spec for the Agent Engine. If not specified, the default encryption spec will be used.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
