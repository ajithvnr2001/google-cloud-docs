---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.AgentEngine
title: Class AgentEngine (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:03.609387+00:00
---

# Class AgentEngine (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines.AgentEngine

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AgentEngine (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    AgentEngine(resource_name: str)

Represents a Vertex AI Agent Engine resource.

## Properties 

### create_time

Time this resource was created.

### display_name

Display name of this resource.

### encryption_spec

Customer-managed encryption key options for this Vertex AI resource.

If this is set, then all resources created by this Vertex AI resource will be encrypted with the provided encryption key.

### gca_resource

The underlying resource proto representation.

### labels

User-defined labels containing metadata about this resource.

Read more about labels at <https://goo.gl/xmQnxf>

### name

Name of this resource.

### resource_name

Fully-qualified resource name.

### update_time

Time this resource was last updated.

## Methods 

### AgentEngine
    
    
    AgentEngine(resource_name: str)

Retrieves an Agent Engine resource.

**Parameter**  
---  
**Name** | **Description**  
`resource_name` |  `str`   
Required. A fully-qualified resource name or ID such as "projects/123/locations/us-central1/reasoningEngines/456" or "456" when project and location are initialized or passed.  
  
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
            "installation_scripts": [
                "./user_src_dir/installation_scripts/install_package.sh",
                ...
            ],
        },
    )
    

**Parameters**  
---  
**Name** | **Description**  
`agent_engine` |  `AgentEngineInterface`   
Optional. The Agent Engine to be created.  
`requirements` |  `Union[str, Sequence[str]]`   
Optional. The set of PyPI dependencies needed. It can either be the path to a single file (requirements.txt), or an ordered list of strings corresponding to each line of the requirements file.  
`display_name` |  `str`   
Optional. The user-defined name of the Agent Engine. The name can be up to 128 characters long and can comprise any UTF-8 character.  
`description` |  `str`   
Optional. The description of the Agent Engine.  
`gcs_dir_name` |  `str`   
Optional. The GCS bucket directory under `staging_bucket` to use for staging the artifacts needed.  
`extra_packages` |  `Sequence[str]`   
Optional. The set of extra user-provided packages (if any).  
`env_vars` |  `Union[Sequence[str], Dict[str, Union[str, SecretRef]]]`   
Optional. The environment variables to be set when running the Agent Engine. If it is a list of strings, each string should be a valid key to `os.environ`. If it is a dictionary, the keys are the environment variable names, and the values are the corresponding values.  
`build_options` |  `Dict[str, Sequence[str]]`   
Optional. The build options for the Agent Engine. The following keys are supported: - installation_scripts: Optional. The paths to the installation scripts to be executed in the Docker image. The scripts must be located in the `installation_scripts` subdirectory and the path must be added to `extra_packages`.  
`service_account` |  `str`   
Optional. The service account to be used for the Agent Engine. If not specified, the default reasoning engine service agent service account will be used.  
`identity_type` |  `Union[str, aip_types.ReasoningEngineSpec.IdentityType]`   
Optional. The identity type to be used by the Agent Engine at runtime. Set it to `AGENT_IDENTITY` to run the Agent Engine under a resource-scoped workload identity with no default project permissions, instead of the shared Reasoning Engine Service Agent. `service_account` must not be specified when `AGENT_IDENTITY` is used. If not specified, `service_account` is used if set, otherwise the default Reasoning Engine Service Agent is used.  
`psc_interface_config` |  `aip_types.PscInterfaceConfig`   
Optional. The Private Service Connect interface config for the Agent Engine.  
`min_instances` |  `int`   
Optional. The minimum number of instances to be running for the Agent Engine.  
`max_instances` |  `int`   
Optional. The maximum number of instances to be running for the Agent Engine.  
`resource_limits` |  `Dict[str, str]`   
Optional. The resource limits for the Agent Engine.  
`container_concurrency` |  `int`   
Optional. The container concurrency for the Agent Engine.  
`encryption_spec` |  `aip_types.EncryptionSpec`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the model. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as the model.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If the `project` was not set using `[vertexai.init](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai)`.  
`ValueError` | If the `location` was not set using `[vertexai.init](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai)`.  
`ValueError` | If the `staging_bucket` was not set using [vertexai.init](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai).  
`ValueError` | If the `staging_bucket` does not start with "gs://".  
`ValueError` | If `extra_packages` is specified but `agent_engine` is None.  
`ValueError` | If `requirements` is specified but `agent_engine` is None.  
`ValueError` | If `service_account` is specified and `identity_type` is  
`AGENT_IDENTITY` |   
`ValueError` | If `env_vars` has a dictionary entry that does not  
`correspon` | to a SecretRef.:  
`ValueError` | If `env_vars` is a list which contains a string that  
`doe` | not exist in `os.environ`.:  
`TypeError` | If `env_vars` is not a list of strings or a dictionary.  
`TypeError` | If `env_vars` has a value that is not a string or SecretRef.  
`FileNotFoundError` | If `extra_packages` includes a file or directory  
`tha` | does not exist.:  
`IOError` | If requirements is a string that corresponds to a  
`nonexisten` | file.:  
**Returns**  
---  
**Type** | **Description**  
`AgentEngine` | The Agent Engine that was created.  
  
### delete
    
    
    delete(*, force: bool = False, **kwargs) -> None

Deletes the ReasoningEngine.

**Parameters**  
---  
**Name** | **Description**  
`force` |  `bool`   
Optional. If set to True, child resources will also be deleted. Otherwise, the request will fail with FAILED_PRECONDITION error when the Agent Engine has undeleted child resources. Defaults to False.  
`\*\*kwargs` |  `dict[str, Any]`   
Optional. Additional keyword arguments to pass to the delete_reasoning_engine method.  
  
### list
    
    
    list(
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        parent: typing.Optional[str] = None,
    ) -> typing.List[google.cloud.aiplatform.base.VertexAiResourceNoun]

List all instances of this Vertex AI Resource.

Example Usage:

aiplatform.BatchPredictionJobs.list( filter='state="JOB_STATE_SUCCEEDED" AND display_name="my_job"', )

aiplatform.Model.list(order_by="create_time desc, display_name")

**Parameters**  
---  
**Name** | **Description**  
`filter` |  `str`   
Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported.  
`order_by` |  `str`   
Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields: `display_name`, `create_time`, `update_time`  
`project` |  `str`   
Optional. Project to retrieve list from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve list from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to retrieve list. Overrides credentials set in aiplatform.init.  
`parent` |  `str`   
Optional. The parent resource name if any to retrieve list from.  
  
### operation_schemas
    
    
    operation_schemas() -> typing.Sequence[typing.Dict[str, typing.Any]]

Returns the (Open)API schemas for the Agent Engine.

### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### update
    
    
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

This method updates the configuration of an existing Agent Engine running remotely, which is identified by its resource name. Unlike the `create` function which requires a `agent_engine` object, all arguments in this method are optional. This method allows you to modify individual aspects of the configuration by providing any of the optional arguments.

**Parameters**  
---  
**Name** | **Description**  
`agent_engine` |  `AgentEngineInterface`   
Optional. The instance to be used as the updated Agent Engine. If it is not specified, the existing instance will be used.  
`requirements` |  `Union[str, Sequence[str]]`   
Optional. The set of PyPI dependencies needed. It can either be the path to a single file (requirements.txt), or an ordered list of strings corresponding to each line of the requirements file. If it is not specified, the existing requirements will be used. If it is set to an empty string or list, the existing requirements will be removed.  
`display_name` |  `str`   
Optional. The user-defined name of the Agent Engine. The name can be up to 128 characters long and can comprise any UTF-8 character.  
`description` |  `str`   
Optional. The description of the Agent Engine.  
`gcs_dir_name` |  `str`   
Optional. The GCS bucket directory under `staging_bucket` to use for staging the artifacts needed.  
`extra_packages` |  `Sequence[str]`   
Optional. The set of extra user-provided packages (if any). If it is not specified, the existing extra packages will be used. If it is set to an empty list, the existing extra packages will be removed.  
`env_vars` |  `Union[Sequence[str], Dict[str, Union[str, SecretRef]]]`   
Optional. The environment variables to be set when running the Agent Engine. If it is a list of strings, each string should be a valid key to `os.environ`. If it is a dictionary, the keys are the environment variable names, and the values are the corresponding values.  
`build_options` |  `Dict[str, Sequence[str]]`   
Optional. The build options for the Agent Engine. The following keys are supported: - installation_scripts: Optional. The paths to the installation scripts to be executed in the Docker image. The scripts must be located in the `installation_scripts` subdirectory and the path must be added to `extra_packages`.  
`service_account` |  `str`   
Optional. The service account to be used for the Agent Engine. If not specified, the default reasoning engine service agent service account will be used.  
`identity_type` |  `Union[str, aip_types.ReasoningEngineSpec.IdentityType]`   
Optional. The identity type to be used by the Agent Engine at runtime. Set it to `AGENT_IDENTITY` to run the Agent Engine under a resource-scoped workload identity with no default project permissions, instead of the shared Reasoning Engine Service Agent. `service_account` must not be specified when `AGENT_IDENTITY` is used. If not specified, the existing identity type will be used.  
`psc_interface_config` |  `aip_types.PscInterfaceConfig`   
Optional. The Private Service Connect interface config for the Agent Engine.  
`min_instances` |  `int`   
Optional. The minimum number of instances to be running for the Agent Engine.  
`max_instances` |  `int`   
Optional. The maximum number of instances to be running for the Agent Engine.  
`resource_limits` |  `Dict[str, str]`   
Optional. The resource limits for the Agent Engine.  
`container_concurrency` |  `int`   
Optional. The container concurrency for the Agent Engine.  
`encryption_spec` |  `aip_types.EncryptionSpec`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the model. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as the model.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If the `staging_bucket` was not set using [vertexai.init](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai).  
`ValueError` | If the `staging_bucket` does not start with "gs://".  
`ValueError` | If `env_vars` has a dictionary entry that does not  
`correspon` | to a SecretRef.:  
`ValueError` | If `env_vars` is a list which contains a string that  
`doe` | not exist in `os.environ`.:  
`TypeError` | If `env_vars` is not a list of strings or a dictionary.  
`TypeError` | If `env_vars` has a value that is not a string or SecretRef.  
`FileNotFoundError` | If `extra_packages` includes a file or directory  
`tha` | does not exist.:  
`ValueError` | if none of `display_name`, `description`, `requirements`,  
`extra_packages` |   
`ValueError` | If `service_account` is specified and `identity_type` is  
`AGENT_IDENTITY` |   
`IOError` | If requirements is a string that corresponds to a  
`nonexisten` | file.:  
**Returns**  
---  
**Type** | **Description**  
`AgentEngine` | The Agent Engine that was updated.  
  
### wait
    
    
    wait()

Helper method that blocks until all futures are complete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
