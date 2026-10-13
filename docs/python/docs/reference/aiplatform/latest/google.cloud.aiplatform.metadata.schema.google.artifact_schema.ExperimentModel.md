---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.metadata.schema.google.artifact_schema.ExperimentModel
title: Class ExperimentModel (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:28:59.339302+00:00
---

# Class ExperimentModel (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.metadata.schema.google.artifact_schema.ExperimentModel

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ExperimentModel (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    ExperimentModel(
        *,
        framework_name: str,
        framework_version: str,
        model_file: str,
        uri: str,
        model_class: typing.Optional[str] = None,
        predict_schemata: typing.Optional[
            google.cloud.aiplatform.metadata.schema.utils.PredictSchemata
        ] = None,
        artifact_id: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        schema_version: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict] = None,
        state: typing.Optional[
            google.cloud.aiplatform_v1.types.artifact.Artifact.State
        ] = State.LIVE
    )

An artifact representing a Vertex Experiment Model.

## Properties 

### framework_name

The framework name of the saved ML model.

### framework_version

The framework version of the saved ML model.

### model_class

The class name of the saved ML model.

## Methods 

### ExperimentModel
    
    
    ExperimentModel(
        *,
        framework_name: str,
        framework_version: str,
        model_file: str,
        uri: str,
        model_class: typing.Optional[str] = None,
        predict_schemata: typing.Optional[
            google.cloud.aiplatform.metadata.schema.utils.PredictSchemata
        ] = None,
        artifact_id: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        schema_version: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        metadata: typing.Optional[typing.Dict] = None,
        state: typing.Optional[
            google.cloud.aiplatform_v1.types.artifact.Artifact.State
        ] = State.LIVE
    )

Instantiates an ExperimentModel that represents a saved ML model.

**Parameters**  
---  
**Name** | **Description**  
`framework_name` |  `str`   
Required. The name of the model's framework. E.g., 'sklearn'  
`framework_version` |  `str`   
Required. The version of the model's framework. E.g., '1.1.0'  
`model_file` |  `str`   
Required. The file name of the model. E.g., 'model.pkl'  
`uri` |  `str`   
Required. The uniform resource identifier of the model artifact directory.  
`model_class` |  `str`   
Optional. The class name of the model. E.g., 'sklearn.linear_model._base.LinearRegression'  
`predict_schemata` |  `PredictSchemata`   
Optional. An instance of PredictSchemata which holds instance, parameter and prediction schema uris.  
`artifact_id` |  `str`   
Optional. The <resource_id> portion of the Artifact name with the format. This is globally unique in a metadataStore: projects/123/locations/us-central1/metadataStores/<metadata_store_id>/artifacts/<resource_id>.  
`display_name` |  `str`   
Optional. The user-defined name of the Artifact.  
`schema_version` |  `str`   
Optional. schema_version specifies the version used by the Artifact. If not set, defaults to use the latest version.  
`description` |  `str`   
Optional. Describes the purpose of the Artifact to be created.  
`metadata` |  `Dict`   
Optional. Contains the metadata information that will be stored in the Artifact.  
`state` |  `google.cloud.gapic.types.Artifact.State`   
Optional. The state of this Artifact. This is a property of the Artifact, and does not imply or apture any ongoing process. This property is managed by clients (such as Vertex AI Pipelines), and the system does not prescribe or check the validity of state transitions.  
  
### get
    
    
    get(
        artifact_id: str,
        *,
        metadata_store_id: str = "default",
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None
    ) -> google.cloud.aiplatform.metadata.schema.google.artifact_schema.ExperimentModel

Retrieves an existing ExperimentModel artifact given an artifact id.

**Parameters**  
---  
**Name** | **Description**  
`artifact_id` |  `str`   
Required. An artifact id of the ExperimentModel artifact.  
`metadata_store_id` |  `str`   
Optional. MetadataStore to retrieve Artifact from. If not set, metadata_store_id is set to "default". If artifact_id is a fully-qualified resource name, its metadata_store_id overrides this one.  
`project` |  `str`   
Optional. Project to retrieve the artifact from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve the Artifact from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to retrieve this Artifact. Overrides credentials set in aiplatform.init.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | if artifact's schema title is not 'google.ExperimentModel'.  
  
### get_model_info
    
    
    get_model_info() -> typing.Dict[str, typing.Any]

Get the model's info from an experiment model artifact.

### load_model
    
    
    load_model() -> typing.Union[sklearn.base.BaseEstimator, xgb.Booster, tf.Module]

Retrieves the original ML model from an ExperimentModel.

Example Usage:
    
    
    experiment_model = aiplatform.get_experiment_model("my-sklearn-model")
    sk_model = experiment_model.load_model()
    pred_y = model.predict(test_X)
    

**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | if model type is not supported.  
  
### register_model
    
    
    register_model(
        *,
        model_id: typing.Optional[str] = None,
        parent_model: typing.Optional[str] = None,
        use_gpu: bool = False,
        is_default_version: bool = True,
        version_aliases: typing.Optional[typing.Sequence[str]] = None,
        version_description: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        serving_container_image_uri: typing.Optional[str] = None,
        serving_container_predict_route: typing.Optional[str] = None,
        serving_container_health_route: typing.Optional[str] = None,
        serving_container_command: typing.Optional[typing.Sequence[str]] = None,
        serving_container_args: typing.Optional[typing.Sequence[str]] = None,
        serving_container_environment_variables: typing.Optional[
            typing.Dict[str, str]
        ] = None,
        serving_container_ports: typing.Optional[typing.Sequence[int]] = None,
        instance_schema_uri: typing.Optional[str] = None,
        parameters_schema_uri: typing.Optional[str] = None,
        prediction_schema_uri: typing.Optional[str] = None,
        explanation_metadata: typing.Optional[
            google.cloud.aiplatform_v1.types.explanation_metadata.ExplanationMetadata
        ] = None,
        explanation_parameters: typing.Optional[
            google.cloud.aiplatform_v1.types.explanation.ExplanationParameters
        ] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        staging_bucket: typing.Optional[str] = None,
        sync: typing.Optional[bool] = True,
        upload_request_timeout: typing.Optional[float] = None
    ) -> google.cloud.aiplatform.models.Model

Register an ExperimentModel to Model Registry and returns a Model representing the registered Model resource.

Example Usage:
    
    
    experiment_model = aiplatform.get_experiment_model("my-sklearn-model")
    registered_model = experiment_model.register_model()
    registered_model.deploy(endpoint=my_endpoint)
    

**Parameters**  
---  
**Name** | **Description**  
`model_id` |  `str`   
Optional. The ID to use for the registered Model, which will become the final component of the model resource name. This value may be up to 63 characters, and valid characters are `[a-z0-9_-]`. The first character cannot be a number or hyphen.  
`parent_model` |  `str`   
Optional. The resource name or model ID of an existing model that the newly-registered model will be a version of. Only set this field when uploading a new version of an existing model.  
`use_gpu` |  `str`   
Optional. Whether or not to use GPUs for the serving container. Only specify this argument when registering a Tensorflow model and 'serving_container_image_uri' is not specified.  
`is_default_version` |  `bool`   
Optional. When set to True, the newly registered model version will automatically have alias "default" included. Subsequent uses of this model without a version specified will use this "default" version. When set to False, the "default" alias will not be moved. Actions targeting the newly-registered model version will need to specifically reference this version by ID or alias. New model uploads, i.e. version 1, will always be "default" aliased.  
`version_aliases` |  `Sequence[str]`   
Optional. User provided version aliases so that a model version can be referenced via alias instead of auto-generated version ID. A default version alias will be created for the first version of the model. The format is `a-z][a-zA-Z0-9-]`{0,126}[a-z0-9]  
`version_description` |  `str`   
Optional. The description of the model version being uploaded.  
`display_name` |  `str`   
Optional. The display name of the Model. The name can be up to 128 characters long and can be consist of any UTF-8 characters.  
`description` |  `str`   
Optional. The description of the model.  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize your Models. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information and examples of labels.  
`serving_container_image_uri` |  `str`   
Optional. The URI of the Model serving container. A pre-built container <https://cloud.google.com/vertex-ai/docs/predictions/pre-built-containers> is automatically chosen based on the model's framwork. Set this field to override the default pre-built container.  
`serving_container_predict_route` |  `str`   
Optional. An HTTP path to send prediction requests to the container, and which must be supported by it. If not specified a default HTTP path will be used by Vertex AI.  
`serving_container_health_route` |  `str`   
Optional. An HTTP path to send health check requests to the container, and which must be supported by it. If not specified a standard HTTP path will be used by Vertex AI.  
`serving_container_command` |  `Sequence[str]`   
Optional. The command with which the container is run. Not executed within a shell. The Docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not.  
`serving_container_args` |  `Sequence[str]`   
Optional. The arguments to the command. The Docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not.  
`serving_container_environment_variables` |  `Dict[str, str]`   
Optional. The environment variables that are to be present in the container. Should be a dictionary where keys are environment variable names and values are environment variable values for those names.  
`serving_container_ports` |  `Sequence[int]`   
Optional. Declaration of ports that are exposed by the container. This field is primarily informational, it gives Vertex AI information about the network connections the container uses. Listing or not a port here has no impact on whether the port is actually exposed, any port listening on the default "0.0.0.0" address inside a container will be accessible from the network.  
`instance_schema_uri` |  `str`   
Optional. Points to a YAML file stored on Google Cloud Storage describing the format of a single instance, which are used in `PredictRequest.instances`, `ExplainRequest.instances` and `BatchPredictionJob.input_config`. The schema is defined as an OpenAPI 3.0.2 `Schema Object <https://tinyurl.com/y538mdwt#schema-object>`__. AutoML Models always have this field populated by AI Platform. Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access.  
`parameters_schema_uri` |  `str`   
Optional. Points to a YAML file stored on Google Cloud Storage describing the parameters of prediction and explanation via `PredictRequest.parameters`, `ExplainRequest.parameters` and `BatchPredictionJob.model_parameters`. The schema is defined as an OpenAPI 3.0.2 `Schema Object <https://tinyurl.com/y538mdwt#schema-object>`__. AutoML Models always have this field populated by AI Platform, if no parameters are supported it is set to an empty string. Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access.  
`prediction_schema_uri` |  `str`   
Optional. Points to a YAML file stored on Google Cloud Storage describing the format of a single prediction produced by this Model, which are returned via `PredictResponse.predictions`, `ExplainResponse.explanations`, and `BatchPredictionJob.output_config`. The schema is defined as an OpenAPI 3.0.2 `Schema Object <https://tinyurl.com/y538mdwt#schema-object>`__. AutoML Models always have this field populated by AI Platform. Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access.  
`explanation_metadata` |  `aiplatform.explain.ExplanationMetadata`   
Optional. Metadata describing the Model's input and output for explanation. `explanation_metadata` is optional while `explanation_parameters` must be specified when used. For more details, see `Ref docs <http://tinyurl.com/1igh60kt>`  
`explanation_parameters` |  `aiplatform.explain.ExplanationParameters`   
Optional. Parameters to configure explaining for Model's predictions. For more details, see `Ref docs <http://tinyurl.com/1an4zake>`  
`encryption_spec_key_name` |  `Optional[str]`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the model. Has the form `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If set, this Model and all sub-resources of this Model will be secured by this key. Overrides encryption_spec_key_name set in aiplatform.init.  
`staging_bucket` |  `str`   
Optional. Bucket to stage local model artifacts. Overrides staging_bucket set in aiplatform.init.  
`sync` |  `bool`   
Optional. Whether to execute this method synchronously. If False, this method will unblock and it will be executed in a concurrent Future.  
`upload_request_timeout` |  `float`   
Optional. The timeout for the upload request in seconds.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If the model doesn't have a pre-built container that is suitable for its framework and 'serving_container_image_uri' is not set.  
**Returns**  
---  
**Type** | **Description**  
`model (aiplatform.Model)` | Instantiated representation of the registered model resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
