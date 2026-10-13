---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.reasoning_engines.ReasoningEngine
title: Class ReasoningEngine (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:38:30.702170+00:00
---

# Class ReasoningEngine (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview.reasoning_engines.ReasoningEngine

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ReasoningEngine (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 
    
    
    ReasoningEngine(reasoning_engine_name: str)

Represents a Vertex AI Reasoning Engine resource.

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

### ReasoningEngine
    
    
    ReasoningEngine(reasoning_engine_name: str)

Retrieves a Reasoning Engine resource.

**Parameter**  
---  
**Name** | **Description**  
`reasoning_engine_name` |  `str`   
Required. A fully-qualified resource name or ID such as "projects/123/locations/us-central1/reasoningEngines/456" or "456" when project and location are initialized or passed.  
  
### create
    
    
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

The Reasoning Engine will be an instance of the `reasoning_engine` that was passed in, running remotely on Vertex AI.

Sample `src_dir` contents (e.g. `./user_src_dir`):
    
    
    user_src_dir/
    |-- main.py
    |-- requirements.txt
    |-- user_code/
    |   |-- utils.py
    |   |-- ...
    |-- ...
    

To build a Reasoning Engine:
    
    
    remote_app = ReasoningEngine.create(
        local_app,
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
    )
    

**Parameters**  
---  
**Name** | **Description**  
`reasoning_engine` |  `ReasoningEngineInterface`   
Required. The Reasoning Engine to be created.  
`requirements` |  `Union[str, Sequence[str]]`   
Optional. The set of PyPI dependencies needed. It can either be the path to a single file (requirements.txt), or an ordered list of strings corresponding to each line of the requirements file.  
`reasoning_engine_name` |  `str`   
Optional. A fully-qualified resource name or ID such as "projects/123/locations/us-central1/reasoningEngines/456" or "456" when project and location are initialized or passed. If specifying the ID, it should be 4-63 characters. Valid characters are lowercase letters, numbers and hyphens ("-"), and it should start with a number or a lower-case letter. If not provided, Vertex AI will generate a value for this ID.  
`display_name` |  `str`   
Optional. The user-defined name of the Reasoning Engine. The name can be up to 128 characters long and can comprise any UTF-8 character.  
`description` |  `str`   
Optional. The description of the Reasoning Engine.  
`gcs_dir_name` |  `CreateReasoningEngineOptions`   
Optional. The GCS bucket directory under `staging_bucket` to use for staging the artifacts needed.  
`sys_version` |  `str`   
Optional. The Python system version used. Currently supports any of "3.10", "3.11", "3.12", "3.13". If not specified, it defaults to the "{major}.{minor}" attributes of sys.version_info.  
`extra_packages` |  `Sequence[str]`   
Optional. The set of extra user-provided packages (if any).  
`service_account` |  `str`   
Optional. The service account that the Reasoning Engine runs as. If not specified, the default Reasoning Engine Service Agent in the project will be used.  
`identity_type` |  `Union[str, aip_types.ReasoningEngineSpec.IdentityType]`   
Optional. The identity type to be used by the Reasoning Engine at runtime. Set it to `AGENT_IDENTITY` to run the Reasoning Engine under a resource-scoped workload identity with no default project permissions, instead of the shared Reasoning Engine Service Agent. `service_account` must not be specified when `AGENT_IDENTITY` is used. If not specified, `service_account` is used if set, otherwise the default Reasoning Engine Service Agent is used.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If `sys.version` is not supported by ReasoningEngine.  
`ValueError` | If the `project` was not set using `[vertexai.init](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai)`.  
`ValueError` | If the `location` was not set using `[vertexai.init](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai)`.  
`ValueError` | If the `staging_bucket` was not set using [vertexai.init](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai).  
`ValueError` | If the `staging_bucket` does not start with "gs://".  
`ValueError` | If `service_account` is specified and `identity_type`  
`i` | `AGENT_IDENTITY`.:  
`FileNotFoundError` | If `extra_packages` includes a file or directory  
`tha` | does not exist.:  
`IOError` | If requirements is a string that corresponds to a  
`nonexisten` | file.:  
**Returns**  
---  
**Type** | **Description**  
`ReasoningEngine` | The Reasoning Engine that was created.  
  
### delete
    
    
    delete(sync: bool = True) -> None

Deletes this Vertex AI resource. WARNING: This deletion is permanent.

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

Returns the (Open)API schemas for the Reasoning Engine.

### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### update
    
    
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

This method updates the configuration of an existing ReasoningEngine running remotely, which is identified by its resource name. Unlike the `create` function which requires a `reasoning_engine` object, all arguments in this method are optional. This method allows you to modify individual aspects of the configuration by providing any of the optional arguments. Note that you must provide at least one argument (except `sys_version`).

**Parameters**  
---  
**Name** | **Description**  
`reasoning_engine` |  `ReasoningEngineInterface`   
Optional. The Reasoning Engine to be replaced. If it is not specified, the existing Reasoning Engine will be used.  
`requirements` |  `Union[str, Sequence[str]]`   
Optional. The set of PyPI dependencies needed. It can either be the path to a single file (requirements.txt), or an ordered list of strings corresponding to each line of the requirements file. If it is not specified, the existing requirements will be used. If it is set to an empty string or list, the existing requirements will be removed.  
`display_name` |  `str`   
Optional. The user-defined name of the Reasoning Engine. The name can be up to 128 characters long and can comprise any UTF-8 character.  
`description` |  `str`   
Optional. The description of the Reasoning Engine.  
`gcs_dir_name` |  `CreateReasoningEngineOptions`   
Optional. The GCS bucket directory under `staging_bucket` to use for staging the artifacts needed.  
`sys_version` |  `str`   
Optional. The Python system version used. Currently updating sys version is not supported.  
`extra_packages` |  `Sequence[str]`   
Optional. The set of extra user-provided packages (if any). If it is not specified, the existing extra packages will be used. If it is set to an empty list, the existing extra packages will be removed.  
`service_account` |  `str`   
Optional. The service account that the Reasoning Engine runs as. If not specified, the existing service account will be used.  
`identity_type` |  `Union[str, aip_types.ReasoningEngineSpec.IdentityType]`   
Optional. The identity type to be used by the Reasoning Engine at runtime. Set it to `AGENT_IDENTITY` to run the Reasoning Engine under a resource-scoped workload identity with no default project permissions, instead of the shared Reasoning Engine Service Agent. `service_account` must not be specified when `AGENT_IDENTITY` is used. If not specified, the existing identity type will be used.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If `sys.version` is updated.  
`ValueError` | If the `staging_bucket` was not set using [vertexai.init](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai).  
`ValueError` | If the `staging_bucket` does not start with "gs://".  
`FileNotFoundError` | If `extra_packages` includes a file or directory  
`tha` | does not exist.:  
`ValueError` | if none of `display_name`, `description`,  
`requirements` |   
`specified.` |   
`ValueError` | If `service_account` is specified and `identity_type`  
`i` | `AGENT_IDENTITY`.:  
`IOError` | If requirements is a string that corresponds to a  
`nonexisten` | file.:  
**Returns**  
---  
**Type** | **Description**  
`ReasoningEngine` | The Reasoning Engine that was updated.  
  
### wait
    
    
    wait()

Helper method that blocks until all futures are complete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
