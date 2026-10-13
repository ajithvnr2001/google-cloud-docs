---
url: https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai.agent_engines.AgentEngine
title: Class AgentEngine (1.153.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:07:21.592629+00:00
---

# Class AgentEngine (1.153.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai.agent_engines.AgentEngine

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AgentEngine (1.153.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.153.1 (latest)  1.153.0  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0 
    
    
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
`ValueError` | If the `project` was not set using `[vertexai.init](https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai)`.  
`ValueError` | If the `location` was not set using `[vertexai.init](https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai)`.  
`ValueError` | If the `staging_bucket` was not set using [vertexai.init](https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai).  
`ValueError` | If the `staging_bucket` does not start with "gs://".  
`ValueError` | If `extra_packages` is specified but `agent_engine` is None.  
`ValueError` | If `requirements` is specified but `agent_engine` is None.  
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
`ValueError` | If the `staging_bucket` was not set using [vertexai.init](https://docs.cloud.google.com/python/docs/reference/vertexai/latest/vertexai).  
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

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
