---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.CustomTrainingJob
title: Class CustomTrainingJob (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:35.226943+00:00
---

# Class CustomTrainingJob (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.CustomTrainingJob

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CustomTrainingJob (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    CustomTrainingJob(
        display_name: str,
        script_path: str,
        container_uri: str,
        requirements: typing.Optional[typing.Sequence[str]] = None,
        model_serving_container_image_uri: typing.Optional[str] = None,
        model_serving_container_predict_route: typing.Optional[str] = None,
        model_serving_container_health_route: typing.Optional[str] = None,
        model_serving_container_command: typing.Optional[typing.Sequence[str]] = None,
        model_serving_container_args: typing.Optional[typing.Sequence[str]] = None,
        model_serving_container_environment_variables: typing.Optional[
            typing.Dict[str, str]
        ] = None,
        model_serving_container_ports: typing.Optional[typing.Sequence[int]] = None,
        model_description: typing.Optional[str] = None,
        model_instance_schema_uri: typing.Optional[str] = None,
        model_parameters_schema_uri: typing.Optional[str] = None,
        model_prediction_schema_uri: typing.Optional[str] = None,
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
        training_encryption_spec_key_name: typing.Optional[str] = None,
        model_encryption_spec_key_name: typing.Optional[str] = None,
        staging_bucket: typing.Optional[str] = None,
    )

Class to launch a Custom Training Job in Vertex AI using a script.

Takes a training implementation as a python script and executes that script in Cloud Vertex AI Training.

## Properties 

### create_time

Time this resource was created.

### display_name

Display name of this resource.

### encryption_spec

Customer-managed encryption key options for this Vertex AI resource.

If this is set, then all resources created by this Vertex AI resource will be encrypted with the provided encryption key.

### end_time

Optional. The time when the training job entered the `PIPELINE_STATE_SUCCEEDED`, `PIPELINE_STATE_FAILED`, or `PIPELINE_STATE_CANCELLED` state.

### error

Optional. Detailed error information for this training job resource. Error information is created only when the state of the training job is `PIPELINE_STATE_FAILED` or `PIPELINE_STATE_CANCELLED`.

### gca_resource

The underlying resource proto representation.

### has_failed

Returns `true` if the training job failed, otherwise `false`.

### labels

User-defined labels containing metadata about this resource.

Read more about labels at <https://goo.gl/xmQnxf>

### name

Name of this resource.

### network

The full name of the Google Compute Engine [network](https://cloud.google.com/vpc/docs/vpc#networks) to which this `CustomTrainingJob` should be peered.

Specify the name of the network using the format `projects/{project}/global/networks/{network}`. Replace {project} with the project number, such as `12345`, and {network} with a network name.

Before specifying a network, private services access must be configured for the network. If private services access isn't configured, then the custom training job can't be peered with a network.

### resource_name

Full qualified resource name.

### start_time

Optional. The time when the training job first entered the `PIPELINE_STATE_RUNNING` state.

### state

Current training state.

### update_time

Time this resource was last updated.

### web_access_uris

Returns the URIs used to access the custom training job.

## Methods 

### CustomTrainingJob
    
    
    CustomTrainingJob(
        display_name: str,
        script_path: str,
        container_uri: str,
        requirements: typing.Optional[typing.Sequence[str]] = None,
        model_serving_container_image_uri: typing.Optional[str] = None,
        model_serving_container_predict_route: typing.Optional[str] = None,
        model_serving_container_health_route: typing.Optional[str] = None,
        model_serving_container_command: typing.Optional[typing.Sequence[str]] = None,
        model_serving_container_args: typing.Optional[typing.Sequence[str]] = None,
        model_serving_container_environment_variables: typing.Optional[
            typing.Dict[str, str]
        ] = None,
        model_serving_container_ports: typing.Optional[typing.Sequence[int]] = None,
        model_description: typing.Optional[str] = None,
        model_instance_schema_uri: typing.Optional[str] = None,
        model_parameters_schema_uri: typing.Optional[str] = None,
        model_prediction_schema_uri: typing.Optional[str] = None,
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
        training_encryption_spec_key_name: typing.Optional[str] = None,
        model_encryption_spec_key_name: typing.Optional[str] = None,
        staging_bucket: typing.Optional[str] = None,
    )

Constructs a Custom Training Job from a Python script.

job = aiplatform.CustomTrainingJob( display_name='test-train', script_path='test_script.py', requirements=['pandas', 'numpy'], container_uri='gcr.io/cloud-aiplatform/training/tf-cpu.2-2:latest', model_serving_container_image_uri='gcr.io/my-trainer/serving:1', model_serving_container_predict_route='predict', model_serving_container_health_route='metadata, labels={'key': 'value'}, )

Usage with Dataset:

ds = aiplatform.TabularDataset( 'projects/my-project/locations/us-central1/datasets/12345')

job.run( ds, replica_count=1, model_display_name='my-trained-model', model_labels={'key': 'value'}, )

Usage without Dataset:

job.run(replica_count=1, model_display_name='my-trained-model)

To ensure your model gets saved in Vertex AI, write your saved model to os.environ["AIP_MODEL_DIR"] in your provided training script.

**Parameters**  
---  
**Name** | **Description**  
`display_name` |  `str`   
Required. The user-defined name of this TrainingPipeline.  
`script_path` |  `str`   
Required. Local path to training script.  
`container_uri` |  `str`   
Required: Uri of the training container image in the GCR.  
`requirements` |  `Sequence[str]`   
List of python packages dependencies of script.  
`model_serving_container_image_uri` |  `str`   
If the training produces a managed Vertex AI Model, the URI of the Model serving container suitable for serving the model produced by the training script.  
`model_serving_container_predict_route` |  `str`   
If the training produces a managed Vertex AI Model, An HTTP path to send prediction requests to the container, and which must be supported by it. If not specified a default HTTP path will be used by Vertex AI.  
`model_serving_container_health_route` |  `str`   
If the training produces a managed Vertex AI Model, an HTTP path to send health check requests to the container, and which must be supported by it. If not specified a standard HTTP path will be used by AI Platform.  
`model_serving_container_command` |  `Sequence[str]`   
The command with which the container is run. Not executed within a shell. The Docker image's ENTRYPOINT is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not.  
`model_serving_container_args` |  `Sequence[str]`   
The arguments to the command. The Docker image's CMD is used if this is not provided. Variable references $(VAR_NAME) are expanded using the container's environment. If a variable cannot be resolved, the reference in the input string will be unchanged. The $(VAR_NAME) syntax can be escaped with a double $$, ie: $$(VAR_NAME). Escaped references will never be expanded, regardless of whether the variable exists or not.  
`model_serving_container_environment_variables` |  `Dict[str, str]`   
The environment variables that are to be present in the container. Should be a dictionary where keys are environment variable names and values are environment variable values for those names.  
`model_serving_container_ports` |  `Sequence[int]`   
Declaration of ports that are exposed by the container. This field is primarily informational, it gives Vertex AI information about the network connections the container uses. Listing or not a port here has no impact on whether the port is actually exposed, any port listening on the default "0.0.0.0" address inside a container will be accessible from the network.  
`model_description` |  `str`   
The description of the Model.  
`model_instance_schema_uri` |  `str`   
Optional. Points to a YAML file stored on Google Cloud Storage describing the format of a single instance, which are used in `PredictRequest.instances`, `ExplainRequest.instances` and `BatchPredictionJob.input_config`. The schema is defined as an OpenAPI 3.0.2 `Schema Object <https://tinyurl.com/y538mdwt#schema-object>`__. AutoML Models always have this field populated by AI Platform. Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access.  
`model_parameters_schema_uri` |  `str`   
Optional. Points to a YAML file stored on Google Cloud Storage describing the parameters of prediction and explanation via `PredictRequest.parameters`, `ExplainRequest.parameters` and `BatchPredictionJob.model_parameters`. The schema is defined as an OpenAPI 3.0.2 `Schema Object <https://tinyurl.com/y538mdwt#schema-object>`__. AutoML Models always have this field populated by AI Platform, if no parameters are supported it is set to an empty string. Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access.  
`model_prediction_schema_uri` |  `str`   
Optional. Points to a YAML file stored on Google Cloud Storage describing the format of a single prediction produced by this Model, which are returned via `PredictResponse.predictions`, `ExplainResponse.explanations`, and `BatchPredictionJob.output_config`. The schema is defined as an OpenAPI 3.0.2 `Schema Object <https://tinyurl.com/y538mdwt#schema-object>`__. AutoML Models always have this field populated by AI Platform. Note: The URI given on output will be immutable and probably different, including the URI scheme, than the one given on input. The output URI will point to a location where the user only has a read access.  
`explanation_metadata` |  `explain.ExplanationMetadata`   
Optional. Metadata describing the Model's input and output for explanation. `explanation_metadata` is optional while `explanation_parameters` must be specified when used. For more details, see `Ref docs <http://tinyurl.com/1igh60kt>`  
`explanation_parameters` |  `explain.ExplanationParameters`   
Optional. Parameters to configure explaining for Model's predictions. For more details, see `Ref docs <http://tinyurl.com/1an4zake>`  
`project` |  `str`   
Project to run training in. Overrides project set in aiplatform.init.  
`location` |  `str`   
Location to run training in. Overrides location set in aiplatform.init.  
`credentials` |  `auth_credentials.Credentials`   
Custom credentials to use to run call training service. Overrides credentials set in aiplatform.init.  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize TrainingPipelines. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information and examples of labels.  
`training_encryption_spec_key_name` |  `Optional[str]`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the training pipeline. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If set, this TrainingPipeline will be secured by this key. Note: Model trained by this TrainingPipeline is also secured by this key if `model_to_upload` is not set separately. Overrides encryption_spec_key_name set in aiplatform.init.  
`model_encryption_spec_key_name` |  `Optional[str]`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the model. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If set, the trained Model will be secured by this key. Overrides encryption_spec_key_name set in aiplatform.init.  
`staging_bucket` |  `str`   
Bucket used to stage source and training artifacts. Overrides staging_bucket set in aiplatform.init.  
  
### cancel
    
    
    cancel() -> None

Asynchronously attempts to cancel a training job.

The server makes a best effort to cancel the job, but the training job can't always be cancelled. If the training job is canceled, its state transitions to `CANCELLED` and it's not deleted.

**Exceptions**  
---  
**Type** | **Description**  
`RuntimeError` | If this training job isn't running, then a runtime error is raised.  
  
### delete
    
    
    delete(sync: bool = True) -> None

Deletes this Vertex AI resource. WARNING: This deletion is permanent.

### done
    
    
    done() -> bool

Method indicating whether a job has completed.

### get
    
    
    get(
        resource_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> google.cloud.aiplatform.training_jobs._TrainingJob

Gets a training job using the `resource_name` that's passed in.

**Parameters**  
---  
**Name** | **Description**  
`resource_name` |  `str`   
Required. A fully-qualified resource name or ID.  
`project` |  `str`   
Optional. The name of the Google Cloud project to retrieve the training job from. This overrides the project that was set by `aiplatform.init`.  
`location` |  `str`   
Optional. The Google Cloud region from where the training job is retrieved. This region overrides the region that was set by `aiplatform.init`.  
`credentials` |  `auth_credentials.Credentials`   
Optional. The credentials that are used to upload this model. These credentials override the credentials set by `aiplatform.init`.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | A `ValueError` is raised if the task definition of the retrieved training job doesn't match the custom training task definition.  
  
### get_model
    
    
    get_model(sync=True) -> google.cloud.aiplatform.models.Model

Returns the Vertex AI model produced by this training job.

**Parameter**  
---  
**Name** | **Description**  
`sync` |  `bool`   
If set to `true`, this method runs synchronously. If `false`, this method runs asynchronously.  
**Exceptions**  
---  
**Type** | **Description**  
`RuntimeError` | A runtime error is raised if the training job failed or if a model wasn't produced by the training job.  
  
### list
    
    
    list(
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> typing.List[google.cloud.aiplatform.base.VertexAiResourceNoun]

Lists all instances of this training job resource.

The following shows an example of how to call `CustomTrainingJob.list`:
    
    
    aiplatform.CustomTrainingJob.list(
        filter='display_name="experiment_a27"',
        order_by='create_time desc'
    )
    

**Parameters**  
---  
**Name** | **Description**  
`filter` |  `str`   
Optional. An expression for filtering the results of the request. For field names, snake_case and camelCase are supported.  
`order_by` |  `str`   
Optional. A comma-separated list of fields used to sort the returned traing job resources. The defauilt sorting order is ascending. To sort by a field name in descending order, use `desc` after the field name. The following fields are supported: `display_name`, `create_time`, `update_time`.  
`project` |  `str`   
Optional. The name of the Google Cloud project to which to retrieve the list of training job resources. This overrides the project that was set by `aiplatform.init`.  
`location` |  `str`   
Optional. The Google Cloud region from where the training job resources are retrieved. This region overrides the region that was set by `aiplatform.init`.  
`credentials` |  `auth_credentials.Credentials`   
Optional. The credentials that are used to retrieve list. These credentials override the credentials set by `aiplatform.init`.  
**Returns**  
---  
**Type** | **Description**  
`List[VertexAiResourceNoun]` | A list of training job resources.  
  
### run
    
    
    run(
        dataset: typing.Optional[
            typing.Union[
                google.cloud.aiplatform.datasets.image_dataset.ImageDataset,
                google.cloud.aiplatform.datasets.tabular_dataset.TabularDataset,
                google.cloud.aiplatform.datasets.text_dataset.TextDataset,
                google.cloud.aiplatform.datasets.video_dataset.VideoDataset,
            ]
        ] = None,
        annotation_schema_uri: typing.Optional[str] = None,
        model_display_name: typing.Optional[str] = None,
        model_labels: typing.Optional[typing.Dict[str, str]] = None,
        model_id: typing.Optional[str] = None,
        parent_model: typing.Optional[str] = None,
        is_default_version: typing.Optional[bool] = True,
        model_version_aliases: typing.Optional[typing.Sequence[str]] = None,
        model_version_description: typing.Optional[str] = None,
        base_output_dir: typing.Optional[str] = None,
        service_account: typing.Optional[str] = None,
        network: typing.Optional[str] = None,
        bigquery_destination: typing.Optional[str] = None,
        args: typing.Optional[typing.List[typing.Union[str, float, int]]] = None,
        environment_variables: typing.Optional[typing.Dict[str, str]] = None,
        replica_count: int = 1,
        machine_type: str = "n1-standard-4",
        accelerator_type: str = "ACCELERATOR_TYPE_UNSPECIFIED",
        accelerator_count: int = 0,
        boot_disk_type: str = "pd-ssd",
        boot_disk_size_gb: int = 100,
        reduction_server_replica_count: int = 0,
        reduction_server_machine_type: typing.Optional[str] = None,
        reduction_server_container_uri: typing.Optional[str] = None,
        training_fraction_split: typing.Optional[float] = None,
        validation_fraction_split: typing.Optional[float] = None,
        test_fraction_split: typing.Optional[float] = None,
        training_filter_split: typing.Optional[str] = None,
        validation_filter_split: typing.Optional[str] = None,
        test_filter_split: typing.Optional[str] = None,
        predefined_split_column_name: typing.Optional[str] = None,
        timestamp_split_column_name: typing.Optional[str] = None,
        timeout: typing.Optional[int] = None,
        restart_job_on_worker_restart: bool = False,
        enable_web_access: bool = False,
        enable_dashboard_access: bool = False,
        tensorboard: typing.Optional[str] = None,
        sync=True,
        create_request_timeout: typing.Optional[float] = None,
        disable_retries: bool = False,
        persistent_resource_id: typing.Optional[str] = None,
        tpu_topology: typing.Optional[str] = None,
        scheduling_strategy: typing.Optional[
            google.cloud.aiplatform_v1.types.custom_job.Scheduling.Strategy
        ] = None,
        reservation_affinity_type: typing.Optional[
            typing.Literal["NO_RESERVATION", "ANY_RESERVATION", "SPECIFIC_RESERVATION"]
        ] = None,
        reservation_affinity_key: typing.Optional[str] = None,
        reservation_affinity_values: typing.Optional[typing.List[str]] = None,
        max_wait_duration: typing.Optional[int] = None,
        psc_interface_config: typing.Optional[
            google.cloud.aiplatform_v1.types.service_networking.PscInterfaceConfig
        ] = None,
    ) -> typing.Optional[google.cloud.aiplatform.models.Model]

Runs the custom training job.

You can configure a custom training job as a distributed training job by specifying multiple _replicas_. To define more than one replica, set `replica_count` to a number greater than one. For example, if you specify 10 for `replica_count`, then one chief replica is provisioned and nine replicas are created that make up a _worker pool_. All replicas in the worker pool have the same `machine_type`, `accelerator_type`, and `accelerator_count`. For more information, see [Distributed training](https://cloud.google.com/vertex-ai/docs/training/distributed-training).

If you train on a Vertex AI dataset, you can use one of the following [split configurations](https://cloud.google.com/vertex-ai/docs/tabular-data/data-splits#default_data_split):

  * [Random split](https://cloud.google.com/vertex-ai/docs/tabular-data/data-splits#classification-random): The random split is also known as _mathematical split_ or _fraction split_. By default, the percentages of training data used for the training, validation, and test sets are 80, 10, and 10, respectively. If you are using Google Cloud console, you can change the percentages to any values that add up to 100. If you are using the Vertex AI SDK, you use fractions that add up to 1.0. Use the optional `training_fraction_split`, `validation_fraction_split`, and `test_fraction_split` to change the percentages. If the specified fractions total less than 1.0, then Vertex AI specifies the remainder.

  * [Data filter split](https://cloud.google.com/vertex-ai/docs/general/ml-use#filter): Assigns input data to training, validation, and test sets. For example, can set `training_filter_split` to `labels.flower=rose`, `validation_filter_split` to `labels.flower=daisy`,`test_filter_split` to `labels.flower=dahlia`. With these settings, data labeled as rose is added to the training set, data labeled as daisy is added to the validation set, and data labeled as dahlia is added to the test set. If you use filter splits, you need to specify all three filters. If you don't want a filter to match any items, set it to the minus sign (`-`). Data filter splits are supported only for unstructured datasets that contain dataitems.

  * [Manual split](https://cloud.google.com/vertex-ai/docs/tabular-data/data-splits#classification-manual): The manual split is also known as a _predefined split_. A manual split assigns input data to training, validation, and test sets based on the value of a provided key. You must specify the `predefined_split_column_name` to use a manual split. Manual splits are supported only for tabular datasets.

  * [Chronological split](https://cloud.google.com/vertex-ai/docs/tabular-data/data-splits#classification-time): The chronological split is also known as a _timestamp split_. If your data is time-dependent, you can use the `timestamp_split_column_name` parameter to designate one column as a time column. Vertex AI uses the time column to split your data, with the earliest of the rows used for training, the next rows for validation, and the latest rows for testing. Chronological splits are supported only for tabular Datasets.




**Parameters**  
---  
**Name** | **Description**  
`annotation_schema_uri` |  `str`   
Optional. A Cloud Storage URI that points to a YAML file describing an annotation schema. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schema-object). The schema files that can be used are in the following Cloud Storage bucket: `gs://google-cloud-aiplatform/schema/dataset/annotation/`. The schema you choose must be consistent with the `metadata` of the Dataset specified by `dataset_id`. If you use a split method, then only annotations that match this schema and belong to `DataItems` that are not ignored by the split method are used. The `DataItems` are used for training, validation, or testing, depending on their role. If you use an annotations filter, then the annotations used for training are filtered using the annotations filter and the `annotation_schema_uri`.  
`model_display_name` |  `str`   
Optional. The user-defined name of the model. The name must contain 128 or fewer UTF-8 characters. If not specified, then the 'display_name` of the training job is used.  
`model_labels` |  `Dict[str, str]`   
Optional. Labels with user-defined metadata to organize your models. The maximum length of a key and of a value is 64 unicode characters. Labels and keys can contain only lowercase letters, numeric characters, underscores, and dashes. International characters are allowed. No more than 64 user labels can be associated with one Tensorboard (system labels are excluded). For more information and examples of using labels, see [Using labels to organize Google Cloud Platform resources](https://goo.gl/xmQnxf). System reserved label keys are prefixed with `aiplatform.googleapis.com/` and are immutable.  
`model_id` |  `str`   
Optional. The ID to use for the model produced by the training job. The. `model_id` is the final component of the model resource name. The maximum length of the `model_id` is63 characters, and valid characters are `[a-z0-9_-]`. The first character cannot be a number or hyphen.  
`parent_model` |  `str`   
Optional. The resource name or model ID of an existing model. The new model uploaded by the training job is a version of `parent_model`. Set `parent_model` only when training a new version of an existing model.  
`is_default_version` |  `bool`   
Optional. When set to `true`, the newly uploaded model version includes the alias `default`. Subsequent models produced by a training job that don't have a version specified use the default version. When set to `false`, the `default` alias isn't assigned to the model and verion one of the model is always the default. Actions targeting the model version produced by this job need to reference this version by its ID or alias.  
`model_version_aliases` |  `Sequence[str]`   
Optional. User provided version aliases that can be used instead of an auto-generated ID to reference the model version uploaded by the training job. A default version alias is created for the first version of the model. The format is `a-z][a-zA-Z0-9-]`{0,126}[a-z0-9]`.  
`model_version_description` |  `str`   
Optional. The description of the model version that's uploaded by this training job.  
`base_output_dir` |  `str`   
Optional. The Cloud Storage output directory of the training job. If not provided, a timestamped directory in the staging directory is used. Vertex AI sets the following environment variables when it runs your training code: `AIP_MODEL_DIR` \- a Cloud Storage URI of a directory used to save model artifacts, such as `<base_output_dir>/model/`. `AIP_CHECKPOINT_DIR`: a Cloud Storage URI of a directory used to save checkpoints, such as `<base_output_dir>/checkpoints/`. `AIP_TENSORBOARD_LOG_DIR`: a Cloud Storage URI of a directory used to save TensorBoard logs, such as `<base_output_dir>/logs/`.  
`service_account` |  `str`   
Optional. A service account used to run the pipeline training job. To submit a pipeline training job using a service account, a user needs to have the `iam.serviceAccounts.actAs` permission on the service account. For more information, see [Requiring permission to attach service accounts to resources](https://cloud.google.com/iam/docs/service-accounts-actas).  
`network` |  `str`   
Optional. The full name of the Compute Engine network to which the job should be peered. For example, projects/12345/global/networks/myVPC. Private services access must already be configured for the network. If left unspecified, the network set by `aiplatform.init` is used and the pipeline job is not peered with any network.  
`bigquery_destination` |  `str`   
Optional. When using a BigQuery dataset, this is the BigQuery project location to where the training data is written. A new dataset is created in the specified project with the name `dataset_`, where the timestamp is in the `YYYY_MM_DDThh_mm_ss_sssZ` format. All training input data is written into the new dataset that includes three tables: `training`, `validation`, and `test`. - AIP_DATA_FORMAT = "bigquery". - AIP_TRAINING_DATA_URI ="bigquery_destination.dataset__.training" - AIP_VALIDATION_DATA_URI = "bigquery_destination.dataset__.validation" - AIP_TEST_DATA_URI = "bigquery_destination.dataset_*.test"  
`args` |  `List[Unions[str, int, float]]`   
Optional. Command line arguments that are passed to the Python script.  
`environment_variables` |  `Dict[str, str]`   
Optional. Environment variables that are passed to the container. The need to be a dictionary where keys are environment variable names and values are the environment variable values for those names. The maximum number of environment variables you can specify is 10 and each environment variable name must be unique. The following shows the format of an environment variable: 
    
    
    py environment_variables = { 'MY_KEY': 'MY_VALUE' }   
  
`replica_count` |  `int`   
The number of worker replicas. If one replica is specified, then one chief replica is provisioned. To define more than one replica so you can have a worker pool, set `replica_count` to a number greater than one. For example, if you specify 10 for `replica_count`, then one chief replica is provisioned and nine replicas are created that make up a _worker pool_. All replicas in the worker pool have the same `machine_type`, `accelerator_type`, and `accelerator_count`. For more information, see [Distributed training](https://cloud.google.com/vertex-ai/docs/training/distributed-training).  
`machine_type` |  `str`   
The type of machine to use for training.  
`accelerator_type` |  `str`   
The hardware accelerator type. You can specify one of the following: `ACCELERATOR_TYPE_UNSPECIFIED`, `NVIDIA_TESLA_K80`, `NVIDIA_TESLA_P100`, `NVIDIA_TESLA_V100`, `NVIDIA_TESLA_P4`, `NVIDIA_TESLA_T4`.  
`accelerator_count` |  `int`   
The number of accelerators to attach to a worker replica.  
`boot_disk_type` |  `str`   
Type of the boot disk. The valid values are `pd-ssd` (Persistent Disk Solid State Drive) and `pd-standard` (Persistent Disk Hard Disk Drive). The default value is `pd-ssd`.  
`boot_disk_size_gb` |  `int`   
The boot disk size in GB. The default is 100GB. The minimum size is 100 and the maximum size is 64,000.  
`reduction_server_replica_count` |  `int`   
The number of reduction server replicas. The default value is `0`.  
`reduction_server_machine_type` |  `str`   
Optional. The type of machine to use for a reduction server.  
`reduction_server_container_uri` |  `str`   
Optional. The URI of the reduction server container image. For more information, see [Reduce training time with Reduction Server](https://cloud.google.com/vertex-ai/docs/training/distributed-training#reduce_training_time_with_reduction_server).  
`training_fraction_split` |  `float`   
Optional. The fraction of the input data used to train the model if a dataset is provided. If a dataset isn't provided, then this is ignored.  
`validation_fraction_split` |  `float`   
Optional. The fraction of the input data used to validate the model if a dataset is provided. If a dataset isn't provided, then this is ignored.  
`test_fraction_split` |  `float`   
Optional. The fraction of the input data used to evaluate the model if a dataset is provided. If a dataset isn't provided, then this is ignored.  
`training_filter_split` |  `str`   
Optional. A training split filter on the data items in a dataset. Data items that match the filter are used to train the model. You can use a filter with the same syntax as the one used in `DatasetService.ListDataItems`. This filter is used to train a model. If a single data item is matched by more than one of the training split filters, then it's assigned to the training set. If a dataset isn't provided, then it's ignored. For more information, see [Data splits for tabular data](https://cloud.google.com/vertex-ai/docs/tabular-data/data-splits).  
`validation_filter_split` |  `str`   
Optional. A validation split filter on the data items in a dataset. You can use a filter with the same syntax as the one used in `DatasetService.ListDataItems`. This filter is used to validate the model. You can use a filter with the same syntax as the one used in `DatasetService.ListDataItems`. If a single data item is matched by more than one of the validation split filters, then it's assigned to the validation set. If a dataset isn't provided, it's ignored. For more information, see [Data splits for tabular data](https://cloud.google.com/vertex-ai/docs/tabular-data/data-splits).  
`test_filter_split` |  `str`   
Optional. A test split filter on the data items in a dataset. You can use a filter with the same syntax as the one used in `DatasetService.ListDataItems`. This filter is used to test the model. You can use a filter with the same syntax as the one used in `DatasetService.ListDataItems`. If a single data item is matched by more than one of the test split filters, then it's assigned to the test set. If a dataset isn't provided, it's ignored. For more information, see [Data splits for tabular data](https://cloud.google.com/vertex-ai/docs/tabular-data/data-splits).  
`predefined_split_column_name` |  `str`   
Optional. A key-value pair where the key is a name of one of the data columns in the dataset. The value of the key (either the label's value or value in the column) must be `training`, `validation`, or `test`. The value specifies the set to which the data is assigned. Data that doesn't have a key, or that has an invalid value, is ignored. The `predefined_split_column_name` is supported by only tabular and time series Datasets.  
`timestamp_split_column_name` |  `str`   
Optional. A key-value pair where the key is a name of one of the data columns in the dataset. The value of each key is the values in the column. Each value must be in the [RFC 3339]](https://www.rfc-editor.org/rfc/rfc3339) `date-time` format, where `time-offset` = `"Z"` (for example, 1985-04-12T23:20:50.52Z). Data that doesn't have a key, or that has an invalid value, is ignored. The `timestamp_split_column_name` is supported by only tabular and time series Datasets.  
`timeout` |  `int`   
Optional.The maximum duration that a pipeline training job can run. `timeout` is specified in seconds. The default is 80,400 seconds (7 days).  
`restart_job_on_worker_restart` |  `bool`   
If set to `true`, the custom job of a worker is restarted. You might set this to `true` if your distributed training job isn't resilient to workers leaving and joining a job. The default value is `false`.  
`enable_web_access` |  `bool`   
If set to `true`, Vertex AI enables interactive shell access to training containers. For more information, see [Monitor and debug training with an interactive shell](https://cloud.google.com/vertex-ai/docs/training/monitor-debug-interactive-shell). The default value is `false`.  
`enable_dashboard_access` |  `bool`   
If set to `true`, Vertex AI enables access to the customized dashboard for training containers. The default value is `false`.  
`tensorboard` |  `str`   
Optional. The name of a Vertex AI [Tensorboard](<https://cloud.google.com/python/docs/reference/aiplatform/latest/>[google.cloud.aiplatform.Tensorboard](https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Tensorboard)) resource to which this customer pipeline training job uploads tensorboard logs. Use the following format to specify the Tensorboard: `projects/{project}/locations/{location}/tensorboards/{tensorboard}`. The training script writes Tensorboard to the `AIP_TENSORBOARD_LOG_DIR` Vertex AI environment variable. If you use a Tensorboard, then you need to specify the `service_account` parameter. For more information, see [Use Vertex AI TensorBoard with custom training](https://cloud.google.com/vertex-ai/docs/experiments/tensorboard-training).  
`create_request_timeout` |  `float`   
Optional. The timeout for the create request in seconds.  
`disable_retries` |  `bool`   
If set to `true`, the job retries for internal errors after the job starts running. If set to `true`, `restart_job_on_worker_restart` is overridden and set to `false`.  
`persistent_resource_id` |  `str`   
Optional. The ID of the PersistentResource in the same Project and Location. If this is specified, the job will be run on existing machines held by the PersistentResource instead of on-demand short-live machines. The network, CMEK, and node pool configs on the job should be consistent with those on the PersistentResource, otherwise, the job will be rejected.  
`tpu_topology` |  `str`   
Optional. Specifies the tpu topology to be used for TPU training job. This field is required for TPU v5 versions. For details on the TPU topology, refer to <https://cloud.google.com/tpu/docs/v5e#tpu-v5e-config>. The topology must be a supported value for the TPU machine type.  
`scheduling_strategy` |  `gca_custom_job_compat.Scheduling.Strategy`   
Optional. Indicates the job scheduling strategy.  
`reservation_affinity_type` |  `str`   
Optional. The type of reservation affinity. One of: * "NO_RESERVATION" : No reservation is used. * "ANY_RESERVATION" : Any reservation that matches machine spec can be used. * "SPECIFIC_RESERVATION" : A specific reservation must be use used. See reservation_affinity_key and reservation_affinity_values for how to specify the reservation.  
`reservation_affinity_key` |  `str`   
Optional. Corresponds to the label key of a reservation resource. To target a SPECIFIC_RESERVATION by name, use `compute.googleapis.com/reservation-name` as the key and specify the name of your reservation as its value.  
`reservation_affinity_values` |  `List[str]`   
Optional. Corresponds to the label values of a reservation resource. This must be the full resource name of the reservation. Format: 'projects/{project_id_or_number}/zones/{zone}/reservations/{reservation_name}'  
`max_wait_duration` |  `int`   
This is the maximum duration that a job will wait for the requested resources to be provisioned in seconds. If set to 0, the job will wait indefinitely. The default is 30 minutes.  
`psc_interface_config` |  `gca_service_networking.PscInterfaceConfig`   
Optional. Configuration for Private Service Connect interface used for training.  
`sync` |  `bool`   
If set to `true`, this runs synchronously. If `false`, this method runs asynchronously.  
  
### submit
    
    
    submit(
        dataset: typing.Optional[
            typing.Union[
                google.cloud.aiplatform.datasets.image_dataset.ImageDataset,
                google.cloud.aiplatform.datasets.tabular_dataset.TabularDataset,
                google.cloud.aiplatform.datasets.text_dataset.TextDataset,
                google.cloud.aiplatform.datasets.video_dataset.VideoDataset,
            ]
        ] = None,
        annotation_schema_uri: typing.Optional[str] = None,
        model_display_name: typing.Optional[str] = None,
        model_labels: typing.Optional[typing.Dict[str, str]] = None,
        model_id: typing.Optional[str] = None,
        parent_model: typing.Optional[str] = None,
        is_default_version: typing.Optional[bool] = True,
        model_version_aliases: typing.Optional[typing.Sequence[str]] = None,
        model_version_description: typing.Optional[str] = None,
        base_output_dir: typing.Optional[str] = None,
        service_account: typing.Optional[str] = None,
        network: typing.Optional[str] = None,
        bigquery_destination: typing.Optional[str] = None,
        args: typing.Optional[typing.List[typing.Union[str, float, int]]] = None,
        environment_variables: typing.Optional[typing.Dict[str, str]] = None,
        replica_count: int = 1,
        machine_type: str = "n1-standard-4",
        accelerator_type: str = "ACCELERATOR_TYPE_UNSPECIFIED",
        accelerator_count: int = 0,
        boot_disk_type: str = "pd-ssd",
        boot_disk_size_gb: int = 100,
        reduction_server_replica_count: int = 0,
        reduction_server_machine_type: typing.Optional[str] = None,
        reduction_server_container_uri: typing.Optional[str] = None,
        training_fraction_split: typing.Optional[float] = None,
        validation_fraction_split: typing.Optional[float] = None,
        test_fraction_split: typing.Optional[float] = None,
        training_filter_split: typing.Optional[str] = None,
        validation_filter_split: typing.Optional[str] = None,
        test_filter_split: typing.Optional[str] = None,
        predefined_split_column_name: typing.Optional[str] = None,
        timestamp_split_column_name: typing.Optional[str] = None,
        timeout: typing.Optional[int] = None,
        restart_job_on_worker_restart: bool = False,
        enable_web_access: bool = False,
        enable_dashboard_access: bool = False,
        tensorboard: typing.Optional[str] = None,
        sync=True,
        create_request_timeout: typing.Optional[float] = None,
        disable_retries: bool = False,
        persistent_resource_id: typing.Optional[str] = None,
        tpu_topology: typing.Optional[str] = None,
        scheduling_strategy: typing.Optional[
            google.cloud.aiplatform_v1.types.custom_job.Scheduling.Strategy
        ] = None,
        reservation_affinity_type: typing.Optional[
            typing.Literal["NO_RESERVATION", "ANY_RESERVATION", "SPECIFIC_RESERVATION"]
        ] = None,
        reservation_affinity_key: typing.Optional[str] = None,
        reservation_affinity_values: typing.Optional[typing.List[str]] = None,
        max_wait_duration: typing.Optional[int] = None,
        psc_interface_config: typing.Optional[
            google.cloud.aiplatform_v1.types.service_networking.PscInterfaceConfig
        ] = None,
    ) -> typing.Optional[google.cloud.aiplatform.models.Model]

Submits the custom training job without blocking until completion.

Distributed Training Support: If replica count = 1 then one chief replica will be provisioned. If replica_count > 1 the remainder will be provisioned as a worker replica pool. ie: replica_count = 10 will result in 1 chief and 9 workers All replicas have same machine_type, accelerator_type, and accelerator_count

If training on a Vertex AI dataset, you can use one of the following split configurations: Data fraction splits: Any of `training_fraction_split`, `validation_fraction_split` and `test_fraction_split` may optionally be provided, they must sum to up to 1. If the provided ones sum to less than 1, the remainder is assigned to sets as decided by Vertex AI. If none of the fractions are set, by default roughly 80% of data will be used for training, 10% for validation, and 10% for test.
    
    
    Data filter splits:
    Assigns input data to training, validation, and test sets
    based on the given filters, data pieces not matched by any
    filter are ignored. Currently only supported for Datasets
    containing DataItems.
    If any of the filters in this message are to match nothing, then
    they can be set as '-' (the minus sign).
    If using filter splits, all of `training_filter_split`, `validation_filter_split` and
    `test_filter_split` must be provided.
    Supported only for unstructured Datasets.
    
    Predefined splits:
    Assigns input data to training, validation, and test sets based on the value of a provided key.
    If using predefined splits, `predefined_split_column_name` must be provided.
    Supported only for tabular Datasets.
    
    Timestamp splits:
    Assigns input data to training, validation, and test sets
    based on a provided timestamps. The youngest data pieces are
    assigned to training set, next to validation set, and the oldest
    to the test set.
    Supported only for tabular Datasets.
    

**Parameters**  
---  
**Name** | **Description**  
`annotation_schema_uri` |  `str`   
Google Cloud Storage URI points to a YAML file describing annotation schema. The schema is defined as an OpenAPI 3.0.2 [Schema Object](https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.0.2.md#schema-object) The schema files that can be used here are found in gs://google-cloud-aiplatform/schema/dataset/annotation/, note that the chosen schema must be consistent with `metadata` of the Dataset specified by `dataset_id`. Only Annotations that both match this schema and belong to DataItems not ignored by the split method are used in respectively training, validation or test role, depending on the role of the DataItem they are on. When used in conjunction with `annotations_filter`, the Annotations used for training are filtered by both `annotations_filter` and `annotation_schema_uri`.  
`model_display_name` |  `str`   
If the script produces a managed Vertex AI Model. The display name of the Model. The name can be up to 128 characters long and can be consist of any UTF-8 characters. If not provided upon creation, the job's display_name is used.  
`model_labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize your Models. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information and examples of labels.  
`model_id` |  `str`   
Optional. The ID to use for the Model produced by this job, which will become the final component of the model resource name. This value may be up to 63 characters, and valid characters are `[a-z0-9_-]`. The first character cannot be a number or hyphen.  
`parent_model` |  `str`   
Optional. The resource name or model ID of an existing model. The new model uploaded by this job will be a version of `parent_model`. Only set this field when training a new version of an existing model.  
`is_default_version` |  `bool`   
Optional. When set to True, the newly uploaded model version will automatically have alias "default" included. Subsequent uses of the model produced by this job without a version specified will use this "default" version. When set to False, the "default" alias will not be moved. Actions targeting the model version produced by this job will need to specifically reference this version by ID or alias. New model uploads, i.e. version 1, will always be "default" aliased.  
`model_version_aliases` |  `Sequence[str]`   
Optional. User provided version aliases so that the model version uploaded by this job can be referenced via alias instead of auto-generated version ID. A default version alias will be created for the first version of the model. The format is `a-z][a-zA-Z0-9-]`{0,126}[a-z0-9]  
`model_version_description` |  `str`   
Optional. The description of the model version being uploaded by this job.  
`base_output_dir` |  `str`   
GCS output directory of job. If not provided a timestamped directory in the staging directory will be used. Vertex AI sets the following environment variables when it runs your training code: - AIP_MODEL_DIR: a Cloud Storage URI of a directory intended for saving model artifacts, i.e. <base_output_dir>/model/ - AIP_CHECKPOINT_DIR: a Cloud Storage URI of a directory intended for saving checkpoints, i.e. <base_output_dir>/checkpoints/ - AIP_TENSORBOARD_LOG_DIR: a Cloud Storage URI of a directory intended for saving TensorBoard logs, i.e. <base_output_dir>/logs/  
`service_account` |  `str`   
Specifies the service account for workload run-as account. Users submitting jobs must have act-as permission on this run-as account.  
`network` |  `str`   
The full name of the Compute Engine network to which the job should be peered. For example, projects/12345/global/networks/myVPC. Private services access must already be configured for the network. If left unspecified, the network set in aiplatform.init will be used. Otherwise, the job is not peered with any network.  
`bigquery_destination` |  `str`   
Provide this field if `dataset` is a BigQuery dataset. The BigQuery project location where the training data is to be written to. In the given project a new dataset is created with name `dataset_` where timestamp is in YYYY_MM_DDThh_mm_ss_sssZ format. All training input data will be written into that dataset. In the dataset three tables will be created, `training`, `validation` and `test`. - AIP_DATA_FORMAT = "bigquery". - AIP_TRAINING_DATA_URI ="bigquery_destination.dataset__.training" - AIP_VALIDATION_DATA_URI = "bigquery_destination.dataset__.validation" - AIP_TEST_DATA_URI = "bigquery_destination.dataset_*.test"  
`args` |  `List[Unions[str, int, float]]`   
Command line arguments to be passed to the Python script.  
`environment_variables` |  `Dict[str, str]`   
Environment variables to be passed to the container. Should be a dictionary where keys are environment variable names and values are environment variable values for those names. At most 10 environment variables can be specified. The Name of the environment variable must be unique. environment_variables = { 'MY_KEY': 'MY_VALUE' }  
`replica_count` |  `int`   
The number of worker replicas. If replica count = 1 then one chief replica will be provisioned. If replica_count > 1 the remainder will be provisioned as a worker replica pool.  
`machine_type` |  `str`   
The type of machine to use for training.  
`accelerator_type` |  `str`   
Hardware accelerator type. One of ACCELERATOR_TYPE_UNSPECIFIED, NVIDIA_TESLA_K80, NVIDIA_TESLA_P100, NVIDIA_TESLA_V100, NVIDIA_TESLA_P4, NVIDIA_TESLA_T4  
`accelerator_count` |  `int`   
The number of accelerators to attach to a worker replica.  
`boot_disk_type` |  `str`   
Type of the boot disk, default is `pd-ssd`. Valid values: `pd-ssd` (Persistent Disk Solid State Drive) or `pd-standard` (Persistent Disk Hard Disk Drive).  
`boot_disk_size_gb` |  `int`   
Size in GB of the boot disk, default is 100GB. boot disk size must be within the range of [100, 64000].  
`reduction_server_replica_count` |  `int`   
The number of reduction server replicas, default is 0.  
`reduction_server_machine_type` |  `str`   
Optional. The type of machine to use for reduction server.  
`reduction_server_container_uri` |  `str`   
Optional. The Uri of the reduction server container image. See details: <https://cloud.google.com/vertex-ai/docs/training/distributed-training#reduce_training_time_with_reduction_server>  
`training_fraction_split` |  `float`   
Optional. The fraction of the input data that is to be used to train the Model. This is ignored if Dataset is not provided.  
`validation_fraction_split` |  `float`   
Optional. The fraction of the input data that is to be used to validate the Model. This is ignored if Dataset is not provided.  
`test_fraction_split` |  `float`   
Optional. The fraction of the input data that is to be used to evaluate the Model. This is ignored if Dataset is not provided.  
`training_filter_split` |  `str`   
Optional. A filter on DataItems of the Dataset. DataItems that match this filter are used to train the Model. A filter with same syntax as the one used in DatasetService.ListDataItems may be used. If a single DataItem is matched by more than one of the FilterSplit filters, then it is assigned to the first set that applies to it in the training, validation, test order. This is ignored if Dataset is not provided.  
`validation_filter_split` |  `str`   
Optional. A filter on DataItems of the Dataset. DataItems that match this filter are used to validate the Model. A filter with same syntax as the one used in DatasetService.ListDataItems may be used. If a single DataItem is matched by more than one of the FilterSplit filters, then it is assigned to the first set that applies to it in the training, validation, test order. This is ignored if Dataset is not provided.  
`test_filter_split` |  `str`   
Optional. A filter on DataItems of the Dataset. DataItems that match this filter are used to test the Model. A filter with same syntax as the one used in DatasetService.ListDataItems may be used. If a single DataItem is matched by more than one of the FilterSplit filters, then it is assigned to the first set that applies to it in the training, validation, test order. This is ignored if Dataset is not provided.  
`predefined_split_column_name` |  `str`   
Optional. The key is a name of one of the Dataset's data columns. The value of the key (either the label's value or value in the column) must be one of {`training`, `validation`, `test`}, and it defines to which set the given piece of data is assigned. If for a piece of data the key is not present or has an invalid value, that piece is ignored by the pipeline. Supported only for tabular and time series Datasets.  
`timestamp_split_column_name` |  `str`   
Optional. The key is a name of one of the Dataset's data columns. The value of the key values of the key (the values in the column) must be in RFC 3339 `date-time` format, where `time-offset` = `"Z"` (e.g. 1985-04-12T23:20:50.52Z). If for a piece of data the key is not present or has an invalid value, that piece is ignored by the pipeline. Supported only for tabular and time series Datasets.  
`timeout` |  `int`   
The maximum job running time in seconds. The default is 7 days.  
`restart_job_on_worker_restart` |  `bool`   
Restarts the entire CustomJob if a worker gets restarted. This feature can be used by distributed training jobs that are not resilient to workers leaving and joining a job.  
`enable_web_access` |  `bool`   
Whether you want Vertex AI to enable interactive shell access to training containers. <https://cloud.google.com/vertex-ai/docs/training/monitor-debug-interactive-shell>  
`enable_dashboard_access` |  `bool`   
Whether you want Vertex AI to enable access to the customized dashboard to training containers.  
`tensorboard` |  `str`   
Optional. The name of a Vertex AI Tensorboard resource to which this CustomJob will upload Tensorboard logs. Format: `projects/{project}/locations/{location}/tensorboards/{tensorboard}` The training script should write Tensorboard to following Vertex AI environment variable: AIP_TENSORBOARD_LOG_DIR `service_account` is required with provided `tensorboard`. For more information on configuring your service account please visit: <https://cloud.google.com/vertex-ai/docs/experiments/tensorboard-training>  
`create_request_timeout` |  `float`   
Optional. The timeout for the create request in seconds.  
`disable_retries` |  `bool`   
Indicates if the job should retry for internal errors after the job starts running. If True, overrides `restart_job_on_worker_restart` to False.  
`persistent_resource_id` |  `str`   
Optional. The ID of the PersistentResource in the same Project and Location. If this is specified, the job will be run on existing machines held by the PersistentResource instead of on-demand short-live machines. The network, CMEK, and node pool configs on the job should be consistent with those on the PersistentResource, otherwise, the job will be rejected.  
`tpu_topology` |  `str`   
Optional. Specifies the tpu topology to be used for TPU training job. This field is required for TPU v5 versions. For details on the TPU topology, refer to <https://cloud.google.com/tpu/docs/v5e#tpu-v5e-config>. The topology must be a supported value for the TPU machine type.  
`scheduling_strategy` |  `gca_custom_job_compat.Scheduling.Strategy`   
Optional. Indicates the job scheduling strategy.  
`reservation_affinity_type` |  `str`   
Optional. The type of reservation affinity. One of: * "NO_RESERVATION" : No reservation is used. * "ANY_RESERVATION" : Any reservation that matches machine spec can be used. * "SPECIFIC_RESERVATION" : A specific reservation must be use used. See reservation_affinity_key and reservation_affinity_values for how to specify the reservation.  
`reservation_affinity_key` |  `str`   
Optional. Corresponds to the label key of a reservation resource. To target a SPECIFIC_RESERVATION by name, use `compute.googleapis.com/reservation-name` as the key and specify the name of your reservation as its value.  
`reservation_affinity_values` |  `List[str]`   
Optional. Corresponds to the label values of a reservation resource. This must be the full resource name of the reservation. Format: 'projects/{project_id_or_number}/zones/{zone}/reservations/{reservation_name}'  
`max_wait_duration` |  `int`   
This is the maximum duration that a job will wait for the requested resources to be provisioned in seconds. If set to 0, the job will wait indefinitely. The default is 30 minutes.  
`psc_interface_config` |  `gca_service_networking.PscInterfaceConfig`   
Optional. Configuration for Private Service Connect interface used for training.  
`sync` |  `bool`   
Whether to execute this method synchronously. If False, this method will be executed in concurrent Future and any downstream object will be immediately returned and synced when the Future has completed.  
**Returns**  
---  
**Type** | **Description**  
`model` | The trained Vertex AI Model resource or None if training did not produce a Vertex AI Model.  
  
### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### wait
    
    
    wait()

Helper method that blocks until all futures are complete.

### wait_for_resource_creation
    
    
    wait_for_resource_creation() -> None

Waits until the resource has been created.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
