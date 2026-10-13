---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Model
title: Class Model (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:46.549843+00:00
---

# Class Model (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Model

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Model (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    Model(
        model_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        version: typing.Optional[str] = None,
    )

Retrieves the model resource and instantiates its representation.

## Parameters  
  
---  
**Name** | **Description**  
`model_name` |  `str`   
Required. A fully-qualified model resource name or model ID. Example: "projects/123/locations/us-central1/models/456" or "456" when project and location are initialized or passed. May optionally contain a version ID or version alias in {model_name}@{version} form. See version arg.  
`project` |  `str`   
Optional project to retrieve model from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional location to retrieve model from. If not set, location set in aiplatform.init will be used.  
`version` |  `str`   
Optional. Version ID or version alias. When set, the specified model version will be targeted unless overridden in method calls. When not set, the model with the "default" alias will be targeted unless overridden in method calls. No behavior change if only one version of a model exists.  
  
## Properties 

### container_spec

The specification of the container that is to be used when deploying this Model. Not present for AutoML Models.

### create_time

Time this resource was created.

### description

Description of the model.

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

### predict_schemata

The schemata that describe formats of the Model's predictions and explanations, if available.

### preview

Return a Model instance with preview features enabled.

### resource_name

Full qualified resource name, without any version ID.

### supported_deployment_resources_types

List of deployment resource types accepted for this Model.

When this Model is deployed, its prediction resources are described by the `prediction_resources` field of the objects returned by `Endpoint.list_models()`. Because not all Models support all resource configuration types, the configuration types this Model supports are listed here.

If no configuration types are listed, the Model cannot be deployed to an `Endpoint` and does not support online predictions (`Endpoint.predict()` or `Endpoint.explain()`). Such a Model can serve predictions by using a `BatchPredictionJob`, if it has at least one entry each in `Model.supported_input_storage_formats` and `Model.supported_output_storage_formats`.

### supported_export_formats

The formats and content types in which this Model may be exported. If empty, this Model is not available for export.

For example, if this model can be exported as a Tensorflow SavedModel and have the artifacts written to Cloud Storage, the expected value would be:
    
    
    {'tf-saved-model': [<ExportableContent.ARTIFACT: 1>]}
    

### supported_input_storage_formats

The formats this Model supports in the `input_config` field of a `BatchPredictionJob`. If `Model.predict_schemata.instance_schema_uri` exists, the instances should be given as per that schema.

[Read the docs for more on batch prediction formats](https://cloud.google.com/vertex-ai/docs/predictions/batch-predictions#batch_request_input)

If this Model doesn't support any of these formats it means it cannot be used with a `BatchPredictionJob`. However, if it has `supported_deployment_resources_types`, it could serve online predictions by using `Endpoint.predict()` or `Endpoint.explain()`.

### supported_output_storage_formats

The formats this Model supports in the `output_config` field of a `BatchPredictionJob`.

If both `Model.predict_schemata.instance_schema_uri` and `Model.predict_schemata.prediction_schema_uri` exist, the predictions are returned together with their instances. In other words, the prediction has the original instance data first, followed by the actual prediction content (as per the schema).

[Read the docs for more on batch prediction formats](https://cloud.google.com/vertex-ai/docs/predictions/batch-predictions)

If this Model doesn't support any of these formats it means it cannot be used with a `BatchPredictionJob`. However, if it has `supported_deployment_resources_types`, it could serve online predictions by using `Endpoint.predict()` or `Endpoint.explain()`.

### training_job

The TrainingJob that uploaded this Model, if any.

**Exceptions**  
---  
**Type** | **Description**  
`api_core.exceptions.NotFound` | If the Model's training job resource cannot be found on the Vertex service.  
  
### update_time

Time this resource was last updated.

### uri

Path to the directory containing the Model artifact and any of its supporting files. Not present for AutoML Models.

### version_aliases

User provided version aliases so that a model version can be referenced via alias (i.e. projects/{project}/locations/{location}/models/{model_id}@{version_alias} instead of auto-generated version id (i.e. projects/{project}/locations/{location}/models/{model_id}@{version_id}). The format is `a-z][a-zA-Z0-9-]`{0,126}[a-z0-9] to distinguish from version_id. A default version alias will be created for the first version of the model, and there must be exactly one default version alias for a model.

### version_create_time

Timestamp when this version was created.

### version_description

The description of this version.

### version_id

The version ID of the model. A new version is committed when a new model version is uploaded or trained under an existing model id. It is an auto-incrementing decimal number in string representation.

### version_update_time

Timestamp when this version was updated.

### versioned_resource_name

The fully-qualified resource name, including the version ID. For example, projects/{project}/locations/{location}/models/{model_id}@{version_id}

### versioning_registry

The registry of model versions associated with this Model instance.

## Methods 

### batch_predict
    
    
    batch_predict(
        job_display_name: typing.Optional[str] = None,
        gcs_source: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        bigquery_source: typing.Optional[str] = None,
        instances_format: str = "jsonl",
        gcs_destination_prefix: typing.Optional[str] = None,
        bigquery_destination_prefix: typing.Optional[str] = None,
        predictions_format: str = "jsonl",
        model_parameters: typing.Optional[typing.Dict] = None,
        machine_type: typing.Optional[str] = None,
        accelerator_type: typing.Optional[str] = None,
        accelerator_count: typing.Optional[int] = None,
        starting_replica_count: typing.Optional[int] = None,
        max_replica_count: typing.Optional[int] = None,
        generate_explanation: typing.Optional[bool] = False,
        explanation_metadata: typing.Optional[
            google.cloud.aiplatform_v1.types.explanation_metadata.ExplanationMetadata
        ] = None,
        explanation_parameters: typing.Optional[
            google.cloud.aiplatform_v1.types.explanation.ExplanationParameters
        ] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        sync: bool = True,
        create_request_timeout: typing.Optional[float] = None,
        batch_size: typing.Optional[int] = None,
        service_account: typing.Optional[str] = None,
    ) -> google.cloud.aiplatform.jobs.BatchPredictionJob

Creates a batch prediction job using this Model and outputs prediction results to the provided destination prefix in the specified `predictions_format`. One source and one destination prefix are required.

Example usage: my_model.batch_predict( job_display_name="prediction-123", gcs_source="gs://example-bucket/instances.csv", instances_format="csv", bigquery_destination_prefix="projectId.bqDatasetId.bqTableId" )

**Parameters**  
---  
**Name** | **Description**  
`job_display_name` |  `str`   
Optional. The user-defined name of the BatchPredictionJob. The name can be up to 128 characters long and can be consist of any UTF-8 characters.  
`gcs_source` |  `typing.Union[str, typing.Sequence[str], NoneType]`   
Optional[Sequence[str]] = None Google Cloud Storage URI(-s) to your instances to run batch prediction on. They must match `instances_format`.  
`bigquery_source` |  `typing.Optional[str]`   
Optional[str] = None BigQuery URI to a table, up to 2000 characters long. For example: `bq://projectId.bqDatasetId.bqTableId`  
`instances_format` |  `str`   
str = "jsonl" The format in which instances are provided. Must be one of the formats listed in `Model.supported_input_storage_formats`. Default is "jsonl" when using `gcs_source`. If a `bigquery_source` is provided, this is overridden to "bigquery".  
`gcs_destination_prefix` |  `typing.Optional[str]`   
Optional[str] = None The Google Cloud Storage location of the directory where the output is to be written to. In the given directory a new directory is created. Its name is `prediction-`, where timestamp is in YYYY-MM-DDThh:mm:ss.sssZ ISO-8601 format. Inside of it files `predictions_0001.`, `predictions_0002.`, ..., `predictions_N.` are created where `` depends on chosen `predictions_format`, and N may equal 0001 and depends on the total number of successfully predicted instances. If the Model has both `instance` and `prediction` schemata defined then each such file contains predictions as per the `predictions_format`. If prediction for any instance failed (partially or completely), then an additional `errors_0001.`, `errors_0002.`,..., `errors_N.` files are created (N depends on total number of failed predictions). These files contain the failed instances, as per their schema, followed by an additional `error` field which as value has ```google.rpc.Status`` `__ containing only `code` and `message` fields.  
`bigquery_destination_prefix` |  `typing.Optional[str]`   
Optional[str] = None The BigQuery URI to a project or table, up to 2000 characters long. When only the project is specified, the Dataset and Table is created. When the full table reference is specified, the Dataset must exist and table must not exist. Accepted forms: `bq://projectId` or `bq://projectId.bqDatasetId`. If no Dataset is specified, a new one is created with the name `prediction_` where the table name is made BigQuery-dataset-name compatible (for example, most special characters become underscores), and timestamp is in YYYY_MM_DDThh_mm_ss_sssZ "based on ISO-8601" format. In the dataset two tables will be created, `predictions`, and `errors`. If the Model has both `instance` and `prediction` schemata defined then the tables have columns as follows: The `predictions` table contains instances for which the prediction succeeded, it has columns as per a concatenation of the Model's instance and prediction schemata. The `errors` table contains rows for which the prediction has failed, it has instance columns, as per the instance schema, followed by a single "errors" column, which as values has ```google.rpc.Status`` `_ represented as a STRUCT, and containing only `code` and `message`.  
`predictions_format` |  `str`   
str = "jsonl" Required. The format in which Vertex AI outputs the predictions, must be one of the formats specified in `Model.supported_output_storage_formats`. Default is "jsonl" when using `gcs_destination_prefix`. If a `bigquery_destination_prefix` is provided, this is overridden to "bigquery".  
`model_parameters` |  `typing.Optional[typing.Dict]`   
Optional[Dict] = None Optional. The parameters that govern the predictions. The schema of the parameters may be specified via the Model's `parameters_schema_uri`.  
`machine_type` |  `typing.Optional[str]`   
Optional[str] = None Optional. The type of machine for running batch prediction on dedicated resources. Not specifying machine type will result in batch prediction job being run with automatic resources.  
`accelerator_type` |  `typing.Optional[str]`   
Optional[str] = None Optional. The type of accelerator(s) that may be attached to the machine as per `accelerator_count`. Only used if `machine_type` is set.  
`accelerator_count` |  `typing.Optional[int]`   
Optional[int] = None Optional. The number of accelerators to attach to the `machine_type`. Only used if `machine_type` is set.  
`starting_replica_count` |  `typing.Optional[int]`   
Optional[int] = None The number of machine replicas used at the start of the batch operation. If not set, Vertex AI decides starting number, not greater than `max_replica_count`. Only used if `machine_type` is set.  
`max_replica_count` |  `typing.Optional[int]`   
Optional[int] = None The maximum number of machine replicas the batch operation may be scaled to. Only used if `machine_type` is set. Default is 10.  
`generate_explanation` |  `bool`   
Optional. Generate explanation along with the batch prediction results. This will cause the batch prediction output to include explanations based on the `prediction_format`: - `bigquery`: output includes a column named `explanation`. The value is a struct that conforms to the [aiplatform.gapic.Explanation] object. - `jsonl`: The JSON objects on each line include an additional entry keyed `explanation`. The value of the entry is a JSON object that conforms to the [aiplatform.gapic.Explanation] object. - `csv`: Generating explanations for CSV format is not supported.  
`explanation_metadata` |  `aiplatform.explain.ExplanationMetadata`   
Optional. Explanation metadata configuration for this BatchPredictionJob. Can be specified only if `generate_explanation` is set to `True`. This value overrides the value of `Model.explanation_metadata`. All fields of `explanation_metadata` are optional in the request. If a field of the `explanation_metadata` object is not populated, the corresponding field of the `Model.explanation_metadata` object is inherited. For more details, see `Ref docs <http://tinyurl.com/1igh60kt>`  
`explanation_parameters` |  `aiplatform.explain.ExplanationParameters`   
Optional. Parameters to configure explaining for Model's predictions. Can be specified only if `generate_explanation` is set to `True`. This value overrides the value of `Model.explanation_parameters`. All fields of `explanation_parameters` are optional in the request. If a field of the `explanation_parameters` object is not populated, the corresponding field of the `Model.explanation_parameters` object is inherited. For more details, see `Ref docs <http://tinyurl.com/1an4zake>`  
`labels` |  `typing.Optional[typing.Dict[str, str]]`   
Optional[Dict[str, str]] = None Optional. The labels with user-defined metadata to organize your BatchPredictionJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information and examples of labels.  
`credentials` |  `typing.Optional[google.auth.credentials.Credentials]`   
Optional[auth_credentials.Credentials] = None Optional. Custom credentials to use to create this batch prediction job. Overrides credentials set in aiplatform.init.  
`encryption_spec_key_name` |  `Optional[str]`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the model. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If set, this Model and all sub-resources of this Model will be secured by this key. Overrides encryption_spec_key_name set in aiplatform.init.  
`create_request_timeout` |  `float`   
Optional. The timeout for the create request in seconds.  
`batch_size` |  `int`   
Optional. The number of the records (e.g. instances) of the operation given in each batch to a machine replica. Machine type, and size of a single record should be considered when setting this parameter, higher value speeds up the batch operation's execution, but too high value will result in a whole batch not fitting in a machine's memory, and the whole operation will fail. The default value is 64.  
`service_account` |  `str`   
Optional. Specifies the service account for workload run-as account. Users submitting jobs must have act-as permission on this run-as account.  
**Returns**  
---  
**Type** | **Description**  
`job (jobs.BatchPredictionJob)` | Instantiated representation of the created batch prediction job.  
  
### copy
    
    
    copy(
        destination_location: str,
        destination_model_id: typing.Optional[str] = None,
        destination_parent_model: typing.Optional[str] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        copy_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.models.Model

Copys a model and returns a Model representing the copied Model resource. This method is a blocking call.

Example usage: copied_model = my_model.copy( destination_location="us-central1" )

**Parameters**  
---  
**Name** | **Description**  
`destination_location` |  `str`   
The destination location to copy the model to.  
`destination_model_id` |  `str`   
Optional. The ID to use for the copied Model, which will become the final component of the model resource name. This value may be up to 63 characters, and valid characters are `[a-z0-9_-]`. The first character cannot be a number or hyphen. Only set this field when copying as a new model. If this field is not set, a numeric model id will be generated.  
`destination_parent_model` |  `str`   
Optional. The resource name or model ID of an existing model that the newly-copied model will be a version of. Only set this field when copying as a new version of an existing model.  
`encryption_spec_key_name` |  `Optional[str]`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the model. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If set, this Model and all sub-resources of this Model will be secured by this key. Overrides encryption_spec_key_name set in aiplatform.init.  
`copy_request_timeout` |  `float`   
Optional. The timeout for the copy request in seconds.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If both `destination_model_id` and `destination_parent_model` are set.  
**Returns**  
---  
**Type** | **Description**  
`model (aiplatform.Model)` | Instantiated representation of the copied model resource.  
  
### delete
    
    
    delete(sync: bool = True) -> None

Deletes this Vertex AI resource. WARNING: This deletion is permanent.

### deploy
    
    
    deploy(
        endpoint: typing.Optional[
            typing.Union[
                google.cloud.aiplatform.models.Endpoint,
                google.cloud.aiplatform.models.PrivateEndpoint,
            ]
        ] = None,
        deployed_model_display_name: typing.Optional[str] = None,
        traffic_percentage: typing.Optional[int] = 0,
        traffic_split: typing.Optional[typing.Dict[str, int]] = None,
        machine_type: typing.Optional[str] = None,
        min_replica_count: int = 1,
        max_replica_count: int = 1,
        accelerator_type: typing.Optional[str] = None,
        accelerator_count: typing.Optional[int] = None,
        gpu_partition_size: typing.Optional[str] = None,
        tpu_topology: typing.Optional[str] = None,
        service_account: typing.Optional[str] = None,
        explanation_metadata: typing.Optional[
            google.cloud.aiplatform_v1.types.explanation_metadata.ExplanationMetadata
        ] = None,
        explanation_parameters: typing.Optional[
            google.cloud.aiplatform_v1.types.explanation.ExplanationParameters
        ] = None,
        metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        encryption_spec_key_name: typing.Optional[str] = None,
        network: typing.Optional[str] = None,
        sync=True,
        deploy_request_timeout: typing.Optional[float] = None,
        autoscaling_target_cpu_utilization: typing.Optional[int] = None,
        autoscaling_target_accelerator_duty_cycle: typing.Optional[int] = None,
        autoscaling_target_request_count_per_minute: typing.Optional[int] = None,
        autoscaling_target_dcgm_fi_dev_gpu_util: typing.Optional[int] = None,
        autoscaling_target_vllm_gpu_cache_usage_perc: typing.Optional[int] = None,
        autoscaling_target_vllm_num_requests_waiting: typing.Optional[int] = None,
        autoscaling_target_pubsub_num_undelivered_messages: typing.Optional[int] = None,
        autoscaling_pubsub_subscription_labels: typing.Optional[
            typing.Dict[str, str]
        ] = None,
        enable_access_logging=False,
        disable_container_logging: bool = False,
        private_service_connect_config: typing.Optional[
            google.cloud.aiplatform.models.PrivateEndpoint.PrivateServiceConnectConfig
        ] = None,
        deployment_resource_pool: typing.Optional[
            google.cloud.aiplatform.models.DeploymentResourcePool
        ] = None,
        reservation_affinity_type: typing.Optional[str] = None,
        reservation_affinity_key: typing.Optional[str] = None,
        reservation_affinity_values: typing.Optional[typing.List[str]] = None,
        spot: bool = False,
        fast_tryout_enabled: bool = False,
        system_labels: typing.Optional[typing.Dict[str, str]] = None,
        required_replica_count: typing.Optional[int] = 0,
    ) -> typing.Union[
        google.cloud.aiplatform.models.Endpoint,
        google.cloud.aiplatform.models.PrivateEndpoint,
    ]

Deploys model to endpoint. Endpoint will be created if unspecified.

**Parameters**  
---  
**Name** | **Description**  
`endpoint` |  `Union[Endpoint, PrivateEndpoint]`   
Optional. Public or private Endpoint to deploy model to. If not specified, endpoint display name will be model display name+'_endpoint'.  
`deployed_model_display_name` |  `str`   
Optional. The display name of the DeployedModel. If not provided upon creation, the Model's display_name is used.  
`traffic_percentage` |  `int`   
Optional. Desired traffic to newly deployed model. Defaults to 0 if there are pre-existing deployed models. Defaults to 100 if there are no pre-existing deployed models. Negative values should not be provided. Traffic of previously deployed models at the endpoint will be scaled down to accommodate new deployed model's traffic. Should not be provided if traffic_split is provided.  
`traffic_split` |  `Dict[str, int]`   
Optional. A map from a DeployedModel's ID to the percentage of this Endpoint's traffic that should be forwarded to that DeployedModel. If a DeployedModel's ID is not listed in this map, then it receives no traffic. The traffic percentage values must add up to 100, or map must be empty if the Endpoint is to not accept any traffic at the moment. Key for model being deployed is "0". Should not be provided if traffic_percentage is provided.  
`machine_type` |  `str`   
Optional. The type of machine. Not specifying machine type will result in model to be deployed with automatic resources.  
`min_replica_count` |  `int`   
Optional. The minimum number of machine replicas this deployed model will be always deployed on. If traffic against it increases, it may dynamically be deployed onto more replicas, and as traffic decreases, some of these extra replicas may be freed.  
`max_replica_count` |  `int`   
Optional. The maximum number of replicas this deployed model may be deployed on when the traffic against it increases. If requested value is too large, the deployment will error, but if deployment succeeds then the ability to scale the model to that many replicas is guaranteed (barring service outages). If traffic against the deployed model increases beyond what its replicas at maximum may handle, a portion of the traffic will be dropped. If this value is not provided, the smaller value of min_replica_count or 1 will be used.  
`accelerator_type` |  `str`   
Optional. Hardware accelerator type. Must also set accelerator_count if used. One of ACCELERATOR_TYPE_UNSPECIFIED, NVIDIA_TESLA_K80, NVIDIA_TESLA_P100, NVIDIA_TESLA_V100, NVIDIA_TESLA_P4, NVIDIA_TESLA_T4  
`accelerator_count` |  `int`   
Optional. The number of accelerators to attach to a worker replica.  
`gpu_partition_size` |  `str`   
Optional. The GPU partition Size for Nvidia MIG.  
`tpu_topology` |  `str`   
Optional. The TPU topology to use for the DeployedModel. Requireid for CloudTPU multihost deployments.  
`service_account` |  `str`   
The service account that the DeployedModel's container runs as. Specify the email address of the service account. If this service account is not specified, the container runs as a service account that doesn't have access to the resource project. Users deploying the Model must have the `iam.serviceAccounts.actAs` permission on this service account.  
`explanation_metadata` |  `aiplatform.explain.ExplanationMetadata`   
Optional. Metadata describing the Model's input and output for explanation. `explanation_metadata` is optional while `explanation_parameters` must be specified when used. For more details, see `Ref docs <http://tinyurl.com/1igh60kt>`  
`explanation_parameters` |  `aiplatform.explain.ExplanationParameters`   
Optional. Parameters to configure explaining for Model's predictions. For more details, see `Ref docs <http://tinyurl.com/1an4zake>`  
`metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`encryption_spec_key_name` |  `Optional[str]`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the model. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If set, this Endpoint and all sub-resources of this Endpoint will be secured by this key. Overrides encryption_spec_key_name set in aiplatform.init.  
`network` |  `str`   
Optional. The full name of the Compute Engine network to which the Endpoint, if created, will be peered to. E.g. "projects/12345/global/networks/myVPC" Private services access must already be configured for the network. If set or aiplatform.init(network=...) has been set, a PrivateEndpoint will be created. If left unspecified, an Endpoint will be created. Read more about PrivateEndpoints [in the documentation](https://cloud.google.com/vertex-ai/docs/predictions/using-private-endpoints). Cannot be set together with private_service_connect_config.  
`deploy_request_timeout` |  `float`   
Optional. The timeout for the deploy request in seconds.  
`autoscaling_target_cpu_utilization` |  `int`   
Target CPU Utilization to use for Autoscaling Replicas. A default value of 60 will be used if not specified.  
`autoscaling_target_accelerator_duty_cycle` |  `int`   
Target Accelerator Duty Cycle. Must also set accelerator_type and accelerator_count if specified. A default value of 60 will be used if not specified.  
`autoscaling_target_request_count_per_minute` |  `int`   
Optional. The target number of requests per minute for autoscaling. If set, the model will be scaled based on the number of requests it receives.  
`autoscaling_target_dcgm_fi_dev_gpu_util` |  `int`   
Optional. Target DCGM metrics for GPU utilization.  
`autoscaling_target_vllm_gpu_cache_usage_perc` |  `int`   
Optional. Target vLLM metrics for GPU KV cache usage percentage.  
`autoscaling_target_vllm_num_requests_waiting` |  `int`   
Optional. Target vLLM metrics for number of inference requests currently waiting in the queue.  
`autoscaling_target_pubsub_num_undelivered_messages` |  `int`   
Optional. The target number of pubsub undelivered messages for autoscaling. If set, the model will be scaled based on the pubsub queue size.  
`autoscaling_pubsub_subscription_labels` |  `Dict[str, str]`   
Optional. Monitored resource labels as key value pairs for metric filtering for pubsub_num_undelivered_messages.  
`disable_container_logging` |  `bool`   
If True, container logs from the deployed model will not be written to Cloud Logging. Defaults to False.  
`private_service_connect_config` |  `PrivateEndpoint.PrivateServiceConnectConfig`   
If true, the endpoint can be accessible via [Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect). Cannot be set together with network.  
`deployment_resource_pool` |  `DeploymentResourcePool`   
Resource pool where the model will be deployed. All models that are deployed to the same DeploymentResourcePool will be hosted in a shared model server. If provided, will override replica count arguments.  
`reservation_affinity_type` |  `str`   
Optional. The type of reservation affinity. One of NO_RESERVATION, ANY_RESERVATION, SPECIFIC_RESERVATION, SPECIFIC_THEN_ANY_RESERVATION, SPECIFIC_THEN_NO_RESERVATION  
`reservation_affinity_key` |  `str`   
Optional. Corresponds to the label key of a reservation resource. To target a SPECIFIC_RESERVATION by name, use `compute.googleapis.com/reservation-name` as the key and specify the name of your reservation as its value.  
`reservation_affinity_values` |  `List[str]`   
Optional. Corresponds to the label values of a reservation resource. This must be the full resource name of the reservation. Format: 'projects/{project_id_or_number}/zones/{zone}/reservations/{reservation_name}'  
`spot` |  `bool`   
Optional. Whether to schedule the deployment workload on spot VMs.  
`fast_tryout_enabled` |  `bool`   
Optional. Defaults to False. If True, model will be deployed using faster deployment path. Useful for quick experiments. Not for production workloads. Only available for most popular models with certain machine types.  
`system_labels` |  `Dict[str, str]`   
Optional. System labels to apply to Model Garden deployments. System labels are managed by Google for internal use only.  
`required_replica_count` |  `int`   
Optional. Number of required available replicas for the deployment to succeed. This field is only needed when partial model deployment/mutation is desired, with a value greater than or equal to 1 and fewer than or equal to min_replica_count. If set, the model deploy/mutate operation will succeed once available_replica_count reaches required_replica_count, and the rest of the replicas will be retried.  
`sync` |  `bool`   
Whether to execute this method synchronously. If False, this method will be executed in concurrent Future and any downstream object will be immediately returned and synced when the Future has completed.  
`enable_access_logging` |  `bool`   
Whether to enable endpoint access logging. Defaults to False.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If `traffic_split` is set for PrivateEndpoint.  
**Returns**  
---  
**Type** | **Description**  
`endpoint (Union[Endpoint, PrivateEndpoint])` | Endpoint with the deployed model.  
  
### evaluate
    
    
    evaluate(
        prediction_type: str,
        target_field_name: str,
        gcs_source_uris: typing.Optional[typing.List[str]] = None,
        bigquery_source_uri: typing.Optional[str] = None,
        bigquery_destination_output_uri: typing.Optional[str] = None,
        class_labels: typing.Optional[typing.List[str]] = None,
        prediction_label_column: typing.Optional[str] = None,
        prediction_score_column: typing.Optional[str] = None,
        staging_bucket: typing.Optional[str] = None,
        service_account: typing.Optional[str] = None,
        generate_feature_attributions: bool = False,
        evaluation_pipeline_display_name: typing.Optional[str] = None,
        evaluation_metrics_display_name: typing.Optional[str] = None,
        network: typing.Optional[str] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        experiment: typing.Optional[
            typing.Union[
                google.cloud.aiplatform.metadata.experiment_resources.Experiment, str
            ]
        ] = None,
        enable_caching: typing.Optional[bool] = None,
    ) -> google.cloud.aiplatform.model_evaluation.model_evaluation_job._ModelEvaluationJob

Creates a model evaluation job running on Vertex Pipelines and returns the resulting ModelEvaluationJob resource.

Example usage:
    
    
    ```
    my_model = Model(
        model_name="projects/123/locations/us-central1/models/456"
    )
    my_evaluation_job = my_model.evaluate(
        prediction_type="classification",
        target_field_name="type",
        data_source_uris=["gs://sdk-model-eval/my-prediction-data.csv"],
        staging_bucket="gs://my-staging-bucket/eval_pipeline_root",
    )
    my_evaluation_job.wait()
    my_evaluation = my_evaluation_job.get_model_evaluation()
    my_evaluation.metrics
    ```
    

**Parameters**  
---  
**Name** | **Description**  
`prediction_type` |  `str`   
Required. The problem type being addressed by this evaluation run. 'classification' and 'regression' are the currently supported problem types.  
`target_field_name` |  `str`   
Required. The column name of the field containing the label for this prediction task.  
`gcs_source_uris` |  `List[str]`   
Optional. A list of Cloud Storage data files containing the ground truth data to use for this evaluation job. These files should contain your model's prediction column. Currently only Google Cloud Storage urls are supported, for example: "gs://path/to/your/data.csv". The provided data files must be either CSV or JSONL. One of `gcs_source_uris` or `bigquery_source_uri` is required.  
`bigquery_source_uri` |  `str`   
Optional. A bigquery table URI containing the ground truth data to use for this evaluation job. This uri should be in the format 'bq://my-project-id.dataset.table'. One of `gcs_source_uris` or `bigquery_source_uri` is required.  
`bigquery_destination_output_uri` |  `str`   
Optional. A bigquery table URI where the Batch Prediction job associated with your Model Evaluation will write prediction output. This can be a BigQuery URI to a project ('bq://my-project'), a dataset ('bq://my-project.my-dataset'), or a table ('bq://my-project.my-dataset.my-table'). Required if `bigquery_source_uri` is provided.  
`class_labels` |  `List[str]`   
Optional. For custom (non-AutoML) classification models, a list of possible class names, in the same order that predictions are generated. This argument is required when prediction_type is 'classification'. For example, in a classification model with 3 possible classes that are outputted in the format: [0.97, 0.02, 0.01] with the class names "cat", "dog", and "fish", the value of `class_labels` should be `["cat", "dog", "fish"]` where the class "cat" corresponds with 0.97 in the example above.  
`prediction_label_column` |  `str`   
Optional. The column name of the field containing classes the model is scoring. Formatted to be able to find nested columns, delimited by `.`. If not set, defaulted to `prediction.classes` for classification.  
`prediction_score_column` |  `str`   
Optional. The column name of the field containing batch prediction scores. Formatted to be able to find nested columns, delimited by `.`. If not set, defaulted to `prediction.scores` for a `classification` problem_type, `prediction.value` for a `regression` problem_type.  
`staging_bucket` |  `str`   
Optional. The GCS directory to use for staging files from this evaluation job. Defaults to the value set in aiplatform.init(staging_bucket=...) if not provided. Required if staging_bucket is not set in aiplatform.init().  
`service_account` |  `str`   
Specifies the service account for workload run-as account for this Model Evaluation PipelineJob. Users submitting jobs must have act-as permission on this run-as account. The service account running this Model Evaluation job needs the following permissions: Dataflow Worker, Storage Admin, Vertex AI Administrator, and Vertex AI Service Agent.  
`generate_feature_attributions` |  `boolean`   
Optional. Whether the model evaluation job should generate feature attributions. Defaults to False if not specified.  
`evaluation_pipeline_display_name` |  `str`   
Optional. The display name of your model evaluation job. This is the display name that will be applied to the Vertex Pipeline run for your evaluation job. If not set, a display name will be generated automatically.  
`evaluation_metrics_display_name` |  `str`   
Optional. The display name of the model evaluation resource uploaded to Vertex from your Model Evaluation pipeline.  
`network` |  `str`   
The full name of the Compute Engine network to which the job should be peered. For example, projects/12345/global/networks/myVPC. Private services access must already be configured for the network. If left unspecified, the job is not peered with any network.  
`encryption_spec_key_name` |  `str`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the job. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If this is set, then all resources created by the PipelineJob for this Model Evaluation will be encrypted with the provided encryption key. If not specified, encryption_spec of original PipelineJob will be used.  
`experiment` |  `Union[str, experiments_resource.Experiment]`   
Optional. The Vertex AI experiment name or instance to associate to the PipelineJob executing this model evaluation job. Metrics produced by the PipelineJob as system.Metric Artifacts will be associated as metrics to the provided experiment, and parameters from this PipelineJob will be associated as parameters to the provided experiment.  
`enable_caching` |  `bool`   
Optional. Whether to turn on caching for the run. If this is not set, defaults to the compile time settings, which are True for all tasks by default, while users may specify different caching options for individual tasks. If this is set, the setting applies to all tasks in the pipeline. Overrides the compile time settings.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If staging_bucket was not set in aiplatform.init() and staging_bucket was not provided. If the provided `prediction_type` is not valid. If the provided `data_source_uris` don't start with 'gs://'.  
**Returns**  
---  
**Type** | **Description**  
`model_evaluation.ModelEvaluationJob` | Instantiated representation of the _ModelEvaluationJob.  
  
### export_model
    
    
    export_model(
        export_format_id: str,
        artifact_destination: typing.Optional[str] = None,
        image_destination: typing.Optional[str] = None,
        sync: bool = True,
    ) -> typing.Dict[str, str]

Exports a trained, exportable Model to a location specified by the user. A Model is considered to be exportable if it has at least one `supported_export_formats`. Either `artifact_destination` or `image_destination` must be provided.

Example Usage: my_model.export( export_format_id="tf-saved-model", artifact_destination="gs://my-bucket/models/" )
    
    
    or
    
    my_model.export(
        export_format_id="custom-model",
        image_destination="us-central1-docker.pkg.dev/projectId/repo/image"
    )
    

**Parameters**  
---  
**Name** | **Description**  
`export_format_id` |  `str`   
Required. The ID of the format in which the Model must be exported. The list of export formats that this Model supports can be found by calling `Model.supported_export_formats`.  
`artifact_destination` |  `str`   
The Cloud Storage location where the Model artifact is to be written to. Under the directory given as the destination a new one with name "`model-export-`", where timestamp is in YYYY-MM-DDThh:mm:ss.sssZ ISO-8601 format, will be created. Inside, the Model and any of its supporting files will be written. This field should only be set when, in [Model.supported_export_formats], the value for the key given in `export_format_id` contains `ARTIFACT`.  
`image_destination` |  `str`   
The Google Container Registry or Artifact Registry URI where the Model container image will be copied to. Accepted forms: - Google Container Registry path. For example: `gcr.io/projectId/imageName:tag`. - Artifact Registry path. For example: `us-central1-docker.pkg.dev/projectId/repoName/imageName:tag`. This field should only be set when, in [Model.supported_export_formats], the value for the key given in `export_format_id` contains `IMAGE`.  
`sync` |  `bool`   
Whether to execute this export synchronously. If False, this method will be executed in concurrent Future and any downstream object will be immediately returned and synced when the Future has completed.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If model does not support exporting.  
`ValueError` | If invalid arguments or export formats are provided.  
**Returns**  
---  
**Type** | **Description**  
`output_info (Dict[str, str])` | Details of the completed export with output destination paths to the artifacts or container image.  
  
### get_model_evaluation
    
    
    get_model_evaluation(
        evaluation_id: typing.Optional[str] = None,
    ) -> typing.Optional[
        google.cloud.aiplatform.model_evaluation.model_evaluation.ModelEvaluation
    ]

Returns a ModelEvaluation resource and instantiates its representation. If no evaluation_id is passed, it will return the first evaluation associated with this model. If the aiplatform.Model resource was instantiated with a version, this will return a Model Evaluation from that version. If no version was specified when instantiating the Model resource, this will return an Evaluation from the default version.

Example usage: my_model = Model( model_name="projects/123/locations/us-central1/models/456" )
    
    
    my_evaluation = my_model.get_model_evaluation(
        evaluation_id="789"
    )
    
    # If no arguments are passed, this method returns the first evaluation for the model
    my_evaluation = my_model.get_model_evaluation()
    

**Parameter**  
---  
**Name** | **Description**  
`evaluation_id` |  `str`   
Optional. The ID of the model evaluation to retrieve.  
**Returns**  
---  
**Type** | **Description**  
`model_evaluation.ModelEvaluation` | Instantiated representation of the ModelEvaluation resource.  
  
### list
    
    
    list(
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> typing.List[google.cloud.aiplatform.models.Model]

List all Model resource instances.

Example Usage: aiplatform.Model.list( filter='labels.my_label="my_label_value" AND display_name="my_model"', )

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
**Returns**  
---  
**Type** | **Description**  
`List[models.Model]` | A list of Model resource objects  
  
### list_model_evaluations
    
    
    list_model_evaluations() -> (
        typing.List[
            google.cloud.aiplatform.model_evaluation.model_evaluation.ModelEvaluation
        ]
    )

List all Model Evaluation resources associated with this model. If this Model resource was instantiated with a version, the Model Evaluation resources for that version will be returned. If no version was provided when the Model resource was instantiated, Model Evaluation resources will be returned for the default version.

Example Usage: my_model = Model( model_name="projects/123/locations/us-central1/models/456@1" )
    
    
    my_evaluations = my_model.list_model_evaluations()
    

**Returns**  
---  
**Type** | **Description**  
`List[model_evaluation.ModelEvaluation]` | List of ModelEvaluation resources for the model.  
  
### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### update
    
    
    update(
        display_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
    ) -> google.cloud.aiplatform.models.Model

Updates a model.

Example usage: my_model = my_model.update( display_name="my-model", description="my description", labels={'key': 'value'}, )

**Parameters**  
---  
**Name** | **Description**  
`display_name` |  `str`   
The display name of the Model. The name can be up to 128 characters long and can be consist of any UTF-8 characters.  
`description` |  `str`   
The description of the model.  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize your Models. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information and examples of labels.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If `labels` is not the correct format.  
**Returns**  
---  
**Type** | **Description**  
`model (aiplatform.Model)` | Updated model resource.  
  
### upload
    
    
    upload(
        serving_container_image_uri: typing.Optional[str] = None,
        *,
        artifact_uri: typing.Optional[str] = None,
        model_id: typing.Optional[str] = None,
        parent_model: typing.Optional[str] = None,
        is_default_version: bool = True,
        version_aliases: typing.Optional[typing.Sequence[str]] = None,
        version_description: typing.Optional[str] = None,
        serving_container_predict_route: typing.Optional[str] = None,
        serving_container_health_route: typing.Optional[str] = None,
        serving_container_invoke_route_prefix: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        serving_container_command: typing.Optional[typing.Sequence[str]] = None,
        serving_container_args: typing.Optional[typing.Sequence[str]] = None,
        serving_container_environment_variables: typing.Optional[
            typing.Dict[str, str]
        ] = None,
        serving_container_ports: typing.Optional[typing.Sequence[int]] = None,
        serving_container_grpc_ports: typing.Optional[typing.Sequence[int]] = None,
        local_model: typing.Optional[LocalModel] = None,
        instance_schema_uri: typing.Optional[str] = None,
        parameters_schema_uri: typing.Optional[str] = None,
        prediction_schema_uri: typing.Optional[str] = None,
        explanation_metadata: typing.Optional[
            google.cloud.aiplatform_v1.types.explanation_metadata.ExplanationMetadata
        ] = None,
        explanation_parameters: typing.Optional[
            google.cloud.aiplatform_v1.types.explanation.ExplanationParameters
        ] = None,
        display_name: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        staging_bucket: typing.Optional[str] = None,
        sync=True,
        upload_request_timeout: typing.Optional[float] = None,
        serving_container_deployment_timeout: typing.Optional[int] = None,
        serving_container_shared_memory_size_mb: typing.Optional[int] = None,
        serving_container_startup_probe_exec: typing.Optional[typing.Sequence[str]] = None,
        serving_container_startup_probe_period_seconds: typing.Optional[int] = None,
        serving_container_startup_probe_timeout_seconds: typing.Optional[int] = None,
        serving_container_health_probe_exec: typing.Optional[typing.Sequence[str]] = None,
        serving_container_health_probe_period_seconds: typing.Optional[int] = None,
        serving_container_health_probe_timeout_seconds: typing.Optional[int] = None,
        model_garden_source_model_name: typing.Optional[str] = None,
        model_garden_source_model_version_id: typing.Optional[str] = None
    ) -> Model

Uploads a model and returns a Model representing the uploaded Model resource.

Example usage: my_model = Model.upload( display_name="my-model", artifact_uri="gs://my-model/saved-model", serving_container_image_uri="tensorflow/serving" )

**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If explanation_metadata is specified while explanation_parameters is not. Also if model directory does not contain a supported model file. If `local_model` is specified but `serving_container_spec.image_uri` in the `local_model` is None. If `local_model` is not specified and `serving_container_image_uri` is None.  
**Returns**  
---  
**Type** | **Description**  
`model (aiplatform.Model)` | Instantiated representation of the uploaded model resource.  
  
### upload_scikit_learn_model_file
    
    
    upload_scikit_learn_model_file(
        model_file_path: str,
        sklearn_version: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        model_id: typing.Optional[str] = None,
        parent_model: typing.Optional[str] = None,
        is_default_version: typing.Optional[bool] = True,
        version_aliases: typing.Optional[typing.Sequence[str]] = None,
        version_description: typing.Optional[str] = None,
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
        labels: typing.Optional[typing.Dict[str, str]] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        staging_bucket: typing.Optional[str] = None,
        sync=True,
        upload_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.models.Model

Uploads a model and returns a Model representing the uploaded Model resource.

Example usage: my_model = Model.upload_scikit_learn_model_file( model_file_path="iris.sklearn_model.joblib" )

**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If explanation_metadata is specified while explanation_parameters is not. Also if model directory does not contain a supported model file.  
**Returns**  
---  
**Type** | **Description**  
`model (aiplatform.Model)` | Instantiated representation of the uploaded model resource.  
  
### upload_tensorflow_saved_model
    
    
    upload_tensorflow_saved_model(
        saved_model_dir: str,
        tensorflow_version: typing.Optional[str] = None,
        use_gpu: bool = False,
        display_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        model_id: typing.Optional[str] = None,
        parent_model: typing.Optional[str] = None,
        is_default_version: typing.Optional[bool] = True,
        version_aliases: typing.Optional[typing.Sequence[str]] = None,
        version_description: typing.Optional[str] = None,
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
        labels: typing.Optional[typing.Dict[str, str]] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        staging_bucket: typing.Optional[str] = None,
        sync=True,
        upload_request_timeout: typing.Optional[str] = None,
    ) -> google.cloud.aiplatform.models.Model

Uploads a model and returns a Model representing the uploaded Model resource.

Example usage: my_model = Model.upload_scikit_learn_model_file( model_file_path="iris.tensorflow_model.SavedModel" )

**Parameters**  
---  
**Name** | **Description**  
`upload_request_timeout` |  `float`   
Optional. The timeout for the upload request in seconds.  
`saved_model_dir` |  `str`   
Required. Local directory of the Tensorflow SavedModel.  
`tensorflow_version` |  `str`   
Optional. The version of the Tensorflow serving container. Supported versions: ["0.15", "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7"]. If the version is not specified, the latest version is used.  
`use_gpu` |  `bool`   
Whether to use GPU for model serving.  
`display_name` |  `str`   
Optional. The display name of the Model. The name can be up to 128 characters long and can be consist of any UTF-8 characters.  
`description` |  `str`   
The description of the model.  
`model_id` |  `str`   
Optional. The ID to use for the uploaded Model, which will become the final component of the model resource name. This value may be up to 63 characters, and valid characters are `[a-z0-9_-]`. The first character cannot be a number or hyphen.  
`parent_model` |  `str`   
Optional. The resource name or model ID of an existing model that the newly-uploaded model will be a version of. Only set this field when uploading a new version of an existing model.  
`is_default_version` |  `bool`   
Optional. When set to True, the newly uploaded model version will automatically have alias "default" included. Subsequent uses of this model without a version specified will use this "default" version. When set to False, the "default" alias will not be moved. Actions targeting the newly-uploaded model version will need to specifically reference this version by ID or alias. New model uploads, i.e. version 1, will always be "default" aliased.  
`version_aliases` |  `Sequence[str]`   
Optional. User provided version aliases so that a model version can be referenced via alias instead of auto-generated version ID. A default version alias will be created for the first version of the model. The format is `a-z][a-zA-Z0-9-]`{0,126}[a-z0-9]  
`version_description` |  `str`   
Optional. The description of the model version being uploaded.  
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
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize your Models. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information and examples of labels.  
`encryption_spec_key_name` |  `Optional[str]`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the model. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If set, this Model and all sub-resources of this Model will be secured by this key. Overrides encryption_spec_key_name set in aiplatform.init.  
`staging_bucket` |  `str`   
Optional. Bucket to stage local model artifacts. Overrides staging_bucket set in aiplatform.init.  
`sync` |  `bool`   
Whether to execute this method synchronously. If False, this method will be executed in concurrent Future and any downstream object will be immediately returned and synced when the Future has completed.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If explanation_metadata is specified while explanation_parameters is not. Also if model directory does not contain a supported model file.  
**Returns**  
---  
**Type** | **Description**  
`model (aiplatform.Model)` | Instantiated representation of the uploaded model resource.  
  
### upload_xgboost_model_file
    
    
    upload_xgboost_model_file(
        model_file_path: str,
        xgboost_version: typing.Optional[str] = None,
        display_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        model_id: typing.Optional[str] = None,
        parent_model: typing.Optional[str] = None,
        is_default_version: typing.Optional[bool] = True,
        version_aliases: typing.Optional[typing.Sequence[str]] = None,
        version_description: typing.Optional[str] = None,
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
        labels: typing.Optional[typing.Dict[str, str]] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        staging_bucket: typing.Optional[str] = None,
        sync=True,
        upload_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.models.Model

Uploads a model and returns a Model representing the uploaded Model resource.

Example usage: my_model = Model.upload_xgboost_model_file( model_file_path="iris.xgboost_model.bst" )

**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If model directory does not contain a supported model file.  
**Returns**  
---  
**Type** | **Description**  
`model (aiplatform.Model)` | Instantiated representation of the uploaded model resource.  
  
### wait
    
    
    wait()

Helper method that blocks until all futures are complete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
