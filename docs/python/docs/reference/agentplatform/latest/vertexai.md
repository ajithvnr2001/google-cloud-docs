---
url: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai/
title: Package vertexai (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:37:58.256470+00:00
---

# Package vertexai (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package vertexai (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0 

API documentation for `vertexai` package.

## Packages 

### [generative_models](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.generative_models)

API documentation for `generative_models` package.

### [language_models](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.language_models)

API documentation for `language_models` package.

### [preview](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.preview)

API documentation for `preview` package.

### [vision_models](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.vision_models)

API documentation for `vision_models` package.

### [evaluation](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.evaluation)

API documentation for `evaluation` package.

### [agent_engines](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.agent_engines)

API documentation for `agent_engines` package.

### [resources](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.resources)

API documentation for `resources` package.

## Classes 

### [Client](https://docs.cloud.google.com/python/docs/reference/agentplatform/latest/vertexai.Client)

Gen AI Client for the Vertex SDK.

Use this client to interact with Vertex-specific Gemini features.

## Packages Functions 

### init
    
    
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

**Parameters**  
---  
**Name** | **Description**  
`project` | `str`  
The default project to use when making API calls.  
`location` | `str`  
The default location to use when making API calls. If not set defaults to us-central-1.  
`experiment` | `str`  
Optional. The experiment name.  
`experiment_description` | `str`  
Optional. The description of the experiment.  
`experiment_tensorboard` | `Union[str, tensorboard_resource.Tensorboard, bool]`  
Optional. The Vertex AI TensorBoard instance, Tensorboard resource name, or Tensorboard resource ID to use as a backing Tensorboard for the provided experiment. Example tensorboard resource name format: "projects/123/locations/us-central1/tensorboards/456" If `experiment_tensorboard` is provided and `experiment` is not, the provided `experiment_tensorboard` will be set as the global Tensorboard. Any subsequent calls to aiplatform.init() with `experiment` and without `experiment_tensorboard` will automatically assign the global Tensorboard to the `experiment`. If `experiment_tensorboard` is ommitted or set to `True` or `None` the global Tensorboard will be assigned to the `experiment`. If a global Tensorboard is not set, the default Tensorboard instance will be used, and created if it does not exist. To disable creating and using Tensorboard with `experiment`, set `experiment_tensorboard` to `False`. Any subsequent calls to aiplatform.init() should include this setting as well.  
`staging_bucket` | `str`  
The default staging bucket to use to stage artifacts when making API calls. In the form gs://...  
`credentials` | `google.auth.credentials.Credentials`  
The default custom credentials to use when making API calls. If not provided credentials will be ascertained from the environment.  
`encryption_spec_key_name` | `Optional[str]`  
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect a resource. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If set, this resource and all sub-resources will be secured by this key.  
`network` | `str`  
Optional. The full name of the Compute Engine network to which jobs and resources should be peered. E.g. "projects/12345/global/networks/myVPC". Private services access must already be configured for the network. If specified, all eligible jobs and resources created will be peered with this VPC.  
`service_account` | `str`  
Optional. The service account used to launch jobs and deploy models. Jobs that use service_account: BatchPredictionJob, CustomJob, PipelineJob, HyperparameterTuningJob, CustomTrainingJob, CustomPythonPackageTrainingJob, CustomContainerTrainingJob, ModelEvaluationJob.  
`api_endpoint` | `str`  
Optional. The desired API endpoint, e.g., us-central1-aiplatform.googleapis.com  
`api_key` | `str`  
Optional. The API key to use for service calls. NOTE: Not all services support API keys.  
`api_transport` | `str`  
Optional. The transport method which is either 'grpc' or 'rest'. NOTE: "rest" transport functionality is currently in a beta state (preview).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
