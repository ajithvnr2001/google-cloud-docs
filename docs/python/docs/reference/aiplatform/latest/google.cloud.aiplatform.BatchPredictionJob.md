---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.BatchPredictionJob
title: Class BatchPredictionJob (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:31.315959+00:00
---

# Class BatchPredictionJob (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.BatchPredictionJob

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BatchPredictionJob (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    BatchPredictionJob(
        batch_prediction_job_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Retrieves a BatchPredictionJob resource and instantiates its representation.

## Parameter  
  
---  
**Name** | **Description**  
`batch_prediction_job_name` |  `str`   
Required. A fully-qualified BatchPredictionJob resource name or ID. Example: "projects/.../locations/.../batchPredictionJobs/456" or "456" when project and location are initialized or passed.  
  
## Properties 

### completion_stats

Statistics on completed and failed prediction instances.

### create_time

Time this resource was created.

### display_name

Display name of this resource.

### encryption_spec

Customer-managed encryption key options for this Vertex AI resource.

If this is set, then all resources created by this Vertex AI resource will be encrypted with the provided encryption key.

### end_time

Time when the Job resource entered the `JOB_STATE_SUCCEEDED`, `JOB_STATE_FAILED`, or `JOB_STATE_CANCELLED` state.

### error

Detailed error info for this Job resource. Only populated when the Job's state is `JOB_STATE_FAILED` or `JOB_STATE_CANCELLED`.

### gca_resource

The underlying resource proto representation.

### labels

User-defined labels containing metadata about this resource.

Read more about labels at <https://goo.gl/xmQnxf>

### name

Name of this resource.

### output_info

Information describing the output of this job, including output location into which prediction output is written.

This is only available for batch prediction jobs that have run successfully.

### partial_failures

Partial failures encountered. For example, single files that can't be read. This field never exceeds 20 entries. Status details fields contain standard GCP error details.

### preview

Exposes features available in preview for this class.

### resource_name

Full qualified resource name.

### start_time

Time when the Job resource entered the `JOB_STATE_RUNNING` for the first time.

### state

Fetch Job again and return the current JobState.

**Returns**  
---  
**Type** | **Description**  
`state (job_state.JobState)` | Enum that describes the state of a Vertex AI job.  
  
### update_time

Time this resource was last updated.

## Methods 

### cancel
    
    
    cancel() -> None

Cancels this Job.

Success of cancellation is not guaranteed. Use `Job.state` property to verify if cancellation was successful.

### create
    
    
    create(
        job_display_name: str,
        model_name: typing.Union[str, google.cloud.aiplatform.models.Model],
        instances_format: str = "jsonl",
        predictions_format: str = "jsonl",
        gcs_source: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        bigquery_source: typing.Optional[str] = None,
        gcs_destination_prefix: typing.Optional[str] = None,
        bigquery_destination_prefix: typing.Optional[str] = None,
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
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        sync: bool = True,
        create_request_timeout: typing.Optional[float] = None,
        batch_size: typing.Optional[int] = None,
        model_monitoring_objective_config: typing.Optional[
            google.cloud.aiplatform.model_monitoring.objective.ObjectiveConfig
        ] = None,
        model_monitoring_alert_config: typing.Optional[
            google.cloud.aiplatform.model_monitoring.alert.AlertConfig
        ] = None,
        analysis_instance_schema_uri: typing.Optional[str] = None,
        service_account: typing.Optional[str] = None,
    ) -> google.cloud.aiplatform.jobs.BatchPredictionJob

Create a batch prediction job.

**Parameters**  
---  
**Name** | **Description**  
`job_display_name` |  `str`   
Required. The user-defined name of the BatchPredictionJob. The name can be up to 128 characters long and can be consist of any UTF-8 characters.  
`model_name` |  `Union[str, aiplatform.Model]`   
Required. A fully-qualified model resource name or model ID. Example: "projects/123/locations/us-central1/models/456" or "456" when project and location are initialized or passed. May optionally contain a version ID or alias in {model_name}@{version} form. Or an instance of aiplatform.Model.  
`instances_format` |  `str`   
Required. The format in which instances are provided. Must be one of the formats listed in `Model.supported_input_storage_formats`. Default is "jsonl" when using `gcs_source`. If a `bigquery_source` is provided, this is overridden to "bigquery".  
`predictions_format` |  `str`   
Required. The format in which Vertex AI outputs the predictions, must be one of the formats specified in `Model.supported_output_storage_formats`. Default is "jsonl" when using `gcs_destination_prefix`. If a `bigquery_destination_prefix` is provided, this is overridden to "bigquery".  
`gcs_source` |  `Optional[Sequence[str]]`   
Google Cloud Storage URI(-s) to your instances to run batch prediction on. They must match `instances_format`.  
`bigquery_source` |  `Optional[str]`   
BigQuery URI to a table, up to 2000 characters long. For example: `bq://projectId.bqDatasetId.bqTableId`  
`gcs_destination_prefix` |  `Optional[str]`   
The Google Cloud Storage location of the directory where the output is to be written to. In the given directory a new directory is created. Its name is `prediction-`, where timestamp is in YYYY-MM-DDThh:mm:ss.sssZ ISO-8601 format. Inside of it files `predictions_0001.`, `predictions_0002.`, ..., `predictions_N.` are created where `` depends on chosen `predictions_format`, and N may equal 0001 and depends on the total number of successfully predicted instances. If the Model has both `instance` and `prediction` schemata defined then each such file contains predictions as per the `predictions_format`. If prediction for any instance failed (partially or completely), then an additional `errors_0001.`, `errors_0002.`,..., `errors_N.` files are created (N depends on total number of failed predictions). These files contain the failed instances, as per their schema, followed by an additional `error` field which as value has ```google.rpc.Status`` `__ containing only `code` and `message` fields.  
`bigquery_destination_prefix` |  `Optional[str]`   
The BigQuery project or dataset location where the output is to be written to. If project is provided, a new dataset is created with name `prediction_` where is made BigQuery-dataset-name compatible (for example, most special characters become underscores), and timestamp is in YYYY_MM_DDThh_mm_ss_sssZ "based on ISO-8601" format. In the dataset two tables will be created, `predictions`, and `errors`. If the Model has both instance and prediction schemata defined then the tables have columns as follows: The `predictions` table contains instances for which the prediction succeeded, it has columns as per a concatenation of the Model's instance and prediction schemata. The `errors` table contains rows for which the prediction has failed, it has instance columns, as per the instance schema, followed by a single "errors" column, which as values has `google.rpc.Status][google.rpc.Status]` represented as a STRUCT, and containing only `code` and `message`.  
`model_parameters` |  `Optional[Dict]`   
The parameters that govern the predictions. The schema of the parameters may be specified via the Model's `parameters_schema_uri`.  
`machine_type` |  `Optional[str]`   
The type of machine for running batch prediction on dedicated resources. Not specifying machine type will result in batch prediction job being run with automatic resources.  
`accelerator_type` |  `Optional[str]`   
The type of accelerator(s) that may be attached to the machine as per `accelerator_count`. Only used if `machine_type` is set.  
`accelerator_count` |  `Optional[int]`   
The number of accelerators to attach to the `machine_type`. Only used if `machine_type` is set.  
`starting_replica_count` |  `Optional[int]`   
The number of machine replicas used at the start of the batch operation. If not set, Vertex AI decides starting number, not greater than `max_replica_count`. Only used if `machine_type` is set.  
`max_replica_count` |  `Optional[int]`   
The maximum number of machine replicas the batch operation may be scaled to. Only used if `machine_type` is set. Default is 10.  
`generate_explanation` |  `bool`   
Optional. Generate explanation along with the batch prediction results. This will cause the batch prediction output to include explanations based on the `prediction_format`: - `bigquery`: output includes a column named `explanation`. The value is a struct that conforms to the [aiplatform.gapic.Explanation] object. - `jsonl`: The JSON objects on each line include an additional entry keyed `explanation`. The value of the entry is a JSON object that conforms to the [aiplatform.gapic.Explanation] object. - `csv`: Generating explanations for CSV format is not supported.  
`explanation_metadata` |  `aiplatform.explain.ExplanationMetadata`   
Optional. Explanation metadata configuration for this BatchPredictionJob. Can be specified only if `generate_explanation` is set to `True`. This value overrides the value of `Model.explanation_metadata`. All fields of `explanation_metadata` are optional in the request. If a field of the `explanation_metadata` object is not populated, the corresponding field of the `Model.explanation_metadata` object is inherited. For more details, see `Ref docs <http://tinyurl.com/1igh60kt>`  
`explanation_parameters` |  `aiplatform.explain.ExplanationParameters`   
Optional. Parameters to configure explaining for Model's predictions. Can be specified only if `generate_explanation` is set to `True`. This value overrides the value of `Model.explanation_parameters`. All fields of `explanation_parameters` are optional in the request. If a field of the `explanation_parameters` object is not populated, the corresponding field of the `Model.explanation_parameters` object is inherited. For more details, see `Ref docs <http://tinyurl.com/1an4zake>`  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize your BatchPredictionJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information and examples of labels.  
`credentials` |  `Optional[auth_credentials.Credentials]`   
Custom credentials to use to create this batch prediction job. Overrides credentials set in aiplatform.init.  
`encryption_spec_key_name` |  `Optional[str]`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the job. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If this is set, then all resources created by the BatchPredictionJob will be encrypted with the provided encryption key. Overrides encryption_spec_key_name set in aiplatform.init.  
`sync` |  `bool`   
Whether to execute this method synchronously. If False, this method will be executed in concurrent Future and any downstream object will be immediately returned and synced when the Future has completed.  
`create_request_timeout` |  `float`   
Optional. The timeout for the create request in seconds.  
`batch_size` |  `int`   
Optional. The number of the records (e.g. instances) of the operation given in each batch to a machine replica. Machine type, and size of a single record should be considered when setting this parameter, higher value speeds up the batch operation's execution, but too high value will result in a whole batch not fitting in a machine's memory, and the whole operation will fail. The default value is 64.  
`model_monitoring_objective_config` |  `aiplatform.model_monitoring.ObjectiveConfig`   
Optional. The objective config for model monitoring. Passing this parameter enables monitoring on the model associated with this batch prediction job.  
`model_monitoring_alert_config` |  `aiplatform.model_monitoring.EmailAlertConfig`   
Optional. Configures how model monitoring alerts are sent to the user. Right now only email alert is supported.  
`analysis_instance_schema_uri` |  `str`   
Optional. Only applicable if model_monitoring_objective_config is also passed. This parameter specifies the YAML schema file uri describing the format of a single instance that you want Tensorflow Data Validation (TFDV) to analyze. If this field is empty, all the feature data types are inferred from predict_instance_schema_uri, meaning that TFDV will use the data in the exact format as prediction request/response. If there are any data type differences between predict instance and TFDV instance, this field can be used to override the schema. For models trained with Vertex AI, this field must be set as all the fields in predict instance formatted as string.  
`service_account` |  `str`   
Optional. Specifies the service account for workload run-as account. Users submitting jobs must have act-as permission on this run-as account.  
**Returns**  
---  
**Type** | **Description**  
`(jobs.BatchPredictionJob)` | Instantiated representation of the created batch prediction job.  
  
### delete
    
    
    delete(sync: bool = True) -> None

Deletes this Vertex AI resource. WARNING: This deletion is permanent.

### done
    
    
    done() -> bool

Method indicating whether a job has completed.

### iter_outputs
    
    
    iter_outputs(
        bq_max_results: typing.Optional[int] = 100,
    ) -> typing.Union[
        typing.Iterable[storage.Blob], typing.Iterable[bigquery.table.RowIterator]
    ]

Returns an Iterable object to traverse the output files, either a list of GCS Blobs or a BigQuery RowIterator depending on the output config set when the BatchPredictionJob was created.

**Parameter**  
---  
**Name** | **Description**  
`bq_max_results` |  `typing.Optional[int]`   
Optional[int] = 100 Limit on rows to retrieve from prediction table in BigQuery dataset. Only used when retrieving predictions from a bigquery_destination_prefix. Default is 100.  
**Exceptions**  
---  
**Type** | **Description**  
`RuntimeError` | If BatchPredictionJob is in a JobState other than SUCCEEDED, since outputs cannot be retrieved until the Job has finished.  
`NotImplementedError` | If BatchPredictionJob succeeded and output_info does not have a GCS or BQ output provided.  
**Returns**  
---  
**Type** | **Description**  
`Union[Iterable[storage.Blob], Iterable[bigquery.table.RowIterator]]` | Either a list of GCS Blob objects within the prediction output directory or an iterable BigQuery RowIterator with predictions.  
  
### list
    
    
    list(
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> typing.List[google.cloud.aiplatform.base.VertexAiResourceNoun]

List all instances of this Job Resource.

Example Usage:

aiplatform.BatchPredictionJobs.list( filter='state="JOB_STATE_SUCCEEDED" AND display_name="my_job"', )

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
  
### submit
    
    
    submit(
        *,
        job_display_name: typing.Optional[str] = None,
        model_name: typing.Union[str, google.cloud.aiplatform.models.Model],
        instances_format: str = "jsonl",
        predictions_format: str = "jsonl",
        gcs_source: typing.Optional[typing.Union[str, typing.Sequence[str]]] = None,
        bigquery_source: typing.Optional[str] = None,
        gcs_destination_prefix: typing.Optional[str] = None,
        bigquery_destination_prefix: typing.Optional[str] = None,
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
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        create_request_timeout: typing.Optional[float] = None,
        batch_size: typing.Optional[int] = None,
        model_monitoring_objective_config: typing.Optional[
            google.cloud.aiplatform.model_monitoring.objective.ObjectiveConfig
        ] = None,
        model_monitoring_alert_config: typing.Optional[
            google.cloud.aiplatform.model_monitoring.alert.AlertConfig
        ] = None,
        analysis_instance_schema_uri: typing.Optional[str] = None,
        service_account: typing.Optional[str] = None
    ) -> google.cloud.aiplatform.jobs.BatchPredictionJob

Sumbit a batch prediction job (not waiting for completion).

**Parameters**  
---  
**Name** | **Description**  
`job_display_name` |  `str`   
Required. The user-defined name of the BatchPredictionJob. The name can be up to 128 characters long and can be consist of any UTF-8 characters.  
`model_name` |  `Union[str, aiplatform.Model]`   
Required. A fully-qualified model resource name or model ID. Example: "projects/123/locations/us-central1/models/456" or "456" when project and location are initialized or passed. May optionally contain a version ID or alias in {model_name}@{version} form. Or an instance of aiplatform.Model.  
`instances_format` |  `str`   
Required. The format in which instances are provided. Must be one of the formats listed in `Model.supported_input_storage_formats`. Default is "jsonl" when using `gcs_source`. If a `bigquery_source` is provided, this is overridden to "bigquery".  
`predictions_format` |  `str`   
Required. The format in which Vertex AI outputs the predictions, must be one of the formats specified in `Model.supported_output_storage_formats`. Default is "jsonl" when using `gcs_destination_prefix`. If a `bigquery_destination_prefix` is provided, this is overridden to "bigquery".  
`gcs_source` |  `Optional[Sequence[str]]`   
Google Cloud Storage URI(-s) to your instances to run batch prediction on. They must match `instances_format`.  
`bigquery_source` |  `Optional[str]`   
BigQuery URI to a table, up to 2000 characters long. For example: `bq://projectId.bqDatasetId.bqTableId`  
`gcs_destination_prefix` |  `Optional[str]`   
The Google Cloud Storage location of the directory where the output is to be written to. In the given directory a new directory is created. Its name is `prediction-`, where timestamp is in YYYY-MM-DDThh:mm:ss.sssZ ISO-8601 format. Inside of it files `predictions_0001.`, `predictions_0002.`, ..., `predictions_N.` are created where `` depends on chosen `predictions_format`, and N may equal 0001 and depends on the total number of successfully predicted instances. If the Model has both `instance` and `prediction` schemata defined then each such file contains predictions as per the `predictions_format`. If prediction for any instance failed (partially or completely), then an additional `errors_0001.`, `errors_0002.`,..., `errors_N.` files are created (N depends on total number of failed predictions). These files contain the failed instances, as per their schema, followed by an additional `error` field which as value has ```google.rpc.Status`` `__ containing only `code` and `message` fields.  
`bigquery_destination_prefix` |  `Optional[str]`   
The BigQuery project or dataset location where the output is to be written to. If project is provided, a new dataset is created with name `prediction_` where is made BigQuery-dataset-name compatible (for example, most special characters become underscores), and timestamp is in YYYY_MM_DDThh_mm_ss_sssZ "based on ISO-8601" format. In the dataset two tables will be created, `predictions`, and `errors`. If the Model has both instance and prediction schemata defined then the tables have columns as follows: The `predictions` table contains instances for which the prediction succeeded, it has columns as per a concatenation of the Model's instance and prediction schemata. The `errors` table contains rows for which the prediction has failed, it has instance columns, as per the instance schema, followed by a single "errors" column, which as values has `google.rpc.Status][google.rpc.Status]` represented as a STRUCT, and containing only `code` and `message`.  
`model_parameters` |  `Optional[Dict]`   
The parameters that govern the predictions. The schema of the parameters may be specified via the Model's `parameters_schema_uri`.  
`machine_type` |  `Optional[str]`   
The type of machine for running batch prediction on dedicated resources. Not specifying machine type will result in batch prediction job being run with automatic resources.  
`accelerator_type` |  `Optional[str]`   
The type of accelerator(s) that may be attached to the machine as per `accelerator_count`. Only used if `machine_type` is set.  
`accelerator_count` |  `Optional[int]`   
The number of accelerators to attach to the `machine_type`. Only used if `machine_type` is set.  
`starting_replica_count` |  `Optional[int]`   
The number of machine replicas used at the start of the batch operation. If not set, Vertex AI decides starting number, not greater than `max_replica_count`. Only used if `machine_type` is set.  
`max_replica_count` |  `Optional[int]`   
The maximum number of machine replicas the batch operation may be scaled to. Only used if `machine_type` is set. Default is 10.  
`generate_explanation` |  `bool`   
Optional. Generate explanation along with the batch prediction results. This will cause the batch prediction output to include explanations based on the `prediction_format`: - `bigquery`: output includes a column named `explanation`. The value is a struct that conforms to the [aiplatform.gapic.Explanation] object. - `jsonl`: The JSON objects on each line include an additional entry keyed `explanation`. The value of the entry is a JSON object that conforms to the [aiplatform.gapic.Explanation] object. - `csv`: Generating explanations for CSV format is not supported.  
`explanation_metadata` |  `aiplatform.explain.ExplanationMetadata`   
Optional. Explanation metadata configuration for this BatchPredictionJob. Can be specified only if `generate_explanation` is set to `True`. This value overrides the value of `Model.explanation_metadata`. All fields of `explanation_metadata` are optional in the request. If a field of the `explanation_metadata` object is not populated, the corresponding field of the `Model.explanation_metadata` object is inherited. For more details, see `Ref docs <http://tinyurl.com/1igh60kt>`  
`explanation_parameters` |  `aiplatform.explain.ExplanationParameters`   
Optional. Parameters to configure explaining for Model's predictions. Can be specified only if `generate_explanation` is set to `True`. This value overrides the value of `Model.explanation_parameters`. All fields of `explanation_parameters` are optional in the request. If a field of the `explanation_parameters` object is not populated, the corresponding field of the `Model.explanation_parameters` object is inherited. For more details, see `Ref docs <http://tinyurl.com/1an4zake>`  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize your BatchPredictionJobs. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information and examples of labels.  
`credentials` |  `Optional[auth_credentials.Credentials]`   
Custom credentials to use to create this batch prediction job. Overrides credentials set in aiplatform.init.  
`encryption_spec_key_name` |  `Optional[str]`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the job. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If this is set, then all resources created by the BatchPredictionJob will be encrypted with the provided encryption key. Overrides encryption_spec_key_name set in aiplatform.init.  
`create_request_timeout` |  `float`   
Optional. The timeout for the create request in seconds.  
`batch_size` |  `int`   
Optional. The number of the records (e.g. instances) of the operation given in each batch to a machine replica. Machine type, and size of a single record should be considered when setting this parameter, higher value speeds up the batch operation's execution, but too high value will result in a whole batch not fitting in a machine's memory, and the whole operation will fail. The default value is 64.  
`model_monitoring_objective_config` |  `aiplatform.model_monitoring.ObjectiveConfig`   
Optional. The objective config for model monitoring. Passing this parameter enables monitoring on the model associated with this batch prediction job.  
`model_monitoring_alert_config` |  `aiplatform.model_monitoring.EmailAlertConfig`   
Optional. Configures how model monitoring alerts are sent to the user. Right now only email alert is supported.  
`analysis_instance_schema_uri` |  `str`   
Optional. Only applicable if model_monitoring_objective_config is also passed. This parameter specifies the YAML schema file uri describing the format of a single instance that you want Tensorflow Data Validation (TFDV) to analyze. If this field is empty, all the feature data types are inferred from predict_instance_schema_uri, meaning that TFDV will use the data in the exact format as prediction request/response. If there are any data type differences between predict instance and TFDV instance, this field can be used to override the schema. For models trained with Vertex AI, this field must be set as all the fields in predict instance formatted as string.  
`service_account` |  `str`   
Optional. Specifies the service account for workload run-as account. Users submitting jobs must have act-as permission on this run-as account.  
**Returns**  
---  
**Type** | **Description**  
`(jobs.BatchPredictionJob)` | Instantiated representation of the created batch prediction job.  
  
### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### wait
    
    
    wait()

Helper method that blocks until all futures are complete.

### wait_for_completion
    
    
    wait_for_completion() -> None

Waits for job to complete.

**Exceptions**  
---  
**Type** | **Description**  
`RuntimeError` | If job failed or cancelled.  
  
### wait_for_resource_creation
    
    
    wait_for_resource_creation() -> None

Waits until resource has been created.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
