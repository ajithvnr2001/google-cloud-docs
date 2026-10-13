---
url: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Endpoint
title: Class Endpoint (2.4.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:26:36.978657+00:00
---

# Class Endpoint (2.4.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.Endpoint

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Endpoint (2.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.0 (latest)  2.3.0  2.2.0  2.1.3  2.0.1  1.165.1  1.164.0  1.163.0  1.162.0  1.161.0  1.160.0  1.159.0  1.158.0  1.157.0  1.156.0  1.155.0  1.154.0  1.153.1  1.152.0  1.151.0  1.150.0  1.149.0  1.148.1  1.147.0  1.146.0  1.145.0  1.144.0  1.143.0  1.142.0  1.141.0  1.140.0  1.139.0  1.138.0  1.137.0  1.136.0  1.135.0  1.134.0  1.133.0  1.132.0  1.131.0  1.130.0  1.129.0  1.122.0  1.121.0  1.120.0  1.119.0  1.118.0  1.117.0  1.116.0  1.115.0  1.114.0  1.113.0  1.112.0  1.111.0  1.110.0  1.109.0  1.108.0  1.107.0  1.106.0  1.105.0  1.104.0  1.103.0  1.102.0  1.101.0  1.100.0  1.99.0  1.98.0  1.97.0  1.96.0  1.95.1  1.94.0  1.93.1  1.92.0  1.91.0  1.90.0  1.89.0  1.88.0  1.87.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.81.0  1.80.0  1.79.0  1.78.0  1.77.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.71.1  1.70.0  1.69.0  1.68.0  1.67.1  1.66.0  1.65.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.1  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.39.0  1.38.1  1.37.0  1.36.4  1.35.0  1.34.0  1.33.1  1.32.0  1.31.1  1.30.1  1.29.0  1.28.1  1.27.1  1.26.1  1.25.0  1.24.1  1.23.0  1.22.1  1.21.0  1.20.0  1.19.1  1.18.3  1.17.1  1.16.1  1.15.1  1.14.0  1.13.1  1.12.1  1.11.0  1.10.0  1.9.0  1.8.1  1.7.1  1.6.2  1.5.0  1.4.3  1.3.0  1.2.0  1.1.1  1.0.1  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.1 
    
    
    Endpoint(
        endpoint_name: str,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    )

Retrieves an endpoint resource.

## Parameters  
  
---  
**Name** | **Description**  
`endpoint_name` |  `str`   
Required. A fully-qualified endpoint resource name or endpoint ID. Example: "projects/123/locations/us-central1/endpoints/456" or "456" when project and location are initialized or passed.  
`project` |  `str`   
Optional. Project to retrieve endpoint from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve endpoint from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to upload this model. Overrides credentials set in aiplatform.init.  
  
## Properties 

### create_time

Time this resource was created.

### dedicated_endpoint_dns

The dedicated endpoint dns for this Endpoint.

This property is only available if dedicated endpoint is enabled. If dedicated endpoint is not enabled, this property returns None.

### dedicated_endpoint_enabled

The dedicated endpoint is enabled for this Endpoint.

This property will be true if dedicated endpoint is enabled.

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

### network

The full name of the Google Compute Engine [network](https://cloud.google.com/vpc/docs/vpc#networks) to which this Endpoint should be peered.

Takes the format `projects/{project}/global/networks/{network}`. Where {project} is a project number, as in `12345`, and {network} is a network name.

Private services access must already be configured for the network. If left unspecified, the Endpoint is not peered with any network.

### preview

Return an Endpoint instance with preview features enabled.

### private_service_connect_config

The Private Service Connect configuration for this Endpoint.

### resource_name

Full qualified resource name.

### traffic_split

A map from a DeployedModel's ID to the percentage of this Endpoint's traffic that should be forwarded to that DeployedModel.

If a DeployedModel's ID is not listed in this map, then it receives no traffic.

The traffic percentage values must add up to 100, or map must be empty if the Endpoint is to not accept any traffic at a moment.

### update_time

Time this resource was last updated.

## Methods 

### create
    
    
    create(
        display_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        encryption_spec_key_name: typing.Optional[str] = None,
        sync=True,
        create_request_timeout: typing.Optional[float] = None,
        endpoint_id: typing.Optional[str] = None,
        enable_request_response_logging=False,
        request_response_logging_sampling_rate: typing.Optional[float] = None,
        request_response_logging_bq_destination_table: typing.Optional[str] = None,
        dedicated_endpoint_enabled=False,
        inference_timeout: typing.Optional[int] = None,
    ) -> google.cloud.aiplatform.models.Endpoint

Creates a new endpoint.

**Parameters**  
---  
**Name** | **Description**  
`display_name` |  `str`   
Optional. The user-defined name of the Endpoint. The name can be up to 128 characters long and can be consist of any UTF-8 characters.  
`description` |  `str`   
Optional. The description of the Endpoint.  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize your Endpoints. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information and examples of labels.  
`metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`project` |  `str`   
Optional. Project to retrieve endpoint from. If not set, project set in aiplatform.init will be used.  
`location` |  `str`   
Optional. Location to retrieve endpoint from. If not set, location set in aiplatform.init will be used.  
`credentials` |  `auth_credentials.Credentials`   
Optional. Custom credentials to use to upload this model. Overrides credentials set in aiplatform.init.  
`encryption_spec_key_name` |  `str`   
Optional. The Cloud KMS resource identifier of the customer managed encryption key used to protect the model. Has the form: `projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key`. The key needs to be in the same region as where the compute resource is created. If set, this Endpoint and all sub-resources of this Endpoint will be secured by this key. Overrides encryption_spec_key_name set in aiplatform.init.  
`create_request_timeout` |  `float`   
Optional. The timeout for the create request in seconds.  
`endpoint_id` |  `str`   
Optional. The ID to use for endpoint, which will become the final component of the endpoint resource name. If not provided, Vertex AI will generate a value for this ID. This value should be 1-10 characters, and valid characters are /[0-9]/. When using HTTP/JSON, this field is populated based on a query string argument, such as `?endpoint_id=12345`. This is the fallback for fields that are not included in either the URI or the body.  
`request_response_logging_sampling_rate` |  `float`   
Optional. The request response logging sampling rate. If not set, default is 0.0.  
`request_response_logging_bq_destination_table` |  `str`   
Optional. The request response logging bigquery destination. If not set, will create a table with name: `bq://{project_id}.logging_{endpoint_display_name}_{endpoint_id}.request_response_logging`.  
`inference_timeout` |  `int`   
Optional. It defines the prediction timeout, in seconds, for online predictions using cloud-based endpoints. This applies to either PSC endpoints, when private_service_connect_config is set, or dedicated endpoints, when dedicated_endpoint_enabled is true.  
`sync` |  `bool`   
Whether to execute this method synchronously. If False, this method will be executed in concurrent Future and any downstream object will be immediately returned and synced when the Future has completed.  
`enable_request_response_logging` |  `bool`   
Optional. Whether to enable request & response logging for this endpoint.  
`dedicated_endpoint_enabled` |  `bool`   
Optional. If enabled, a dedicated dns will be created and your traffic will be fully isolated from other customers' traffic and latency will be reduced.  
**Returns**  
---  
**Type** | **Description**  
`endpoint (aiplatform.Endpoint)` | Created endpoint.  
  
### delete
    
    
    delete(force: bool = False, sync: bool = True) -> None

Deletes this Vertex AI Endpoint resource. If force is set to True, all models on this Endpoint will be undeployed prior to deletion.

**Parameters**  
---  
**Name** | **Description**  
`force` |  `bool`   
Required. If force is set to True, all deployed models on this Endpoint will be undeployed first. Default is False.  
`sync` |  `bool`   
Whether to execute this method synchronously. If False, this method will be executed in concurrent Future and any downstream object will be immediately returned and synced when the Future has completed.  
**Exceptions**  
---  
**Type** | **Description**  
`FailedPrecondition` | If models are deployed on this Endpoint and force = False.  
  
### deploy
    
    
    deploy(
        model: google.cloud.aiplatform.models.Model,
        deployed_model_display_name: typing.Optional[str] = None,
        traffic_percentage: int = 0,
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
    ) -> None

Deploys a Model to the Endpoint.

**Parameters**  
---  
**Name** | **Description**  
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
Optional. The maximum number of replicas this deployed model may be deployed on when the traffic against it increases. If requested value is too large, the deployment will error, but if deployment succeeds then the ability to scale the model to that many replicas is guaranteed (barring service outages). If traffic against the deployed model increases beyond what its replicas at maximum may handle, a portion of the traffic will be dropped. If this value is not provided, the larger value of min_replica_count or 1 will be used. If value provided is smaller than min_replica_count, it will automatically be increased to be min_replica_count.  
`accelerator_type` |  `str`   
Optional. Hardware accelerator type. Must also set accelerator_count if used. One of ACCELERATOR_TYPE_UNSPECIFIED, NVIDIA_TESLA_K80, NVIDIA_TESLA_P100, NVIDIA_TESLA_V100, NVIDIA_TESLA_P4, NVIDIA_TESLA_T4  
`accelerator_count` |  `int`   
Optional. The number of accelerators to attach to a worker replica.  
`gpu_partition_size` |  `str`   
Optional. The GPU partition Size for Nvidia MIG.  
`tpu_topology` |  `str`   
Optional. The TPU topology to use for the DeployedModel. Required for CloudTPU multihost deployments.  
`service_account` |  `str`   
The service account that the DeployedModel's container runs as. Specify the email address of the service account. If this service account is not specified, the container runs as a service account that doesn't have access to the resource project. Users deploying the Model must have the `iam.serviceAccounts.actAs` permission on this service account.  
`explanation_metadata` |  `aiplatform.explain.ExplanationMetadata`   
Optional. Metadata describing the Model's input and output for explanation. `explanation_metadata` is optional while `explanation_parameters` must be specified when used. For more details, see `Ref docs <http://tinyurl.com/1igh60kt>`  
`explanation_parameters` |  `aiplatform.explain.ExplanationParameters`   
Optional. Parameters to configure explaining for Model's predictions. For more details, see `Ref docs <http://tinyurl.com/1an4zake>`  
`metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
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
`model` |  `aiplatform.Model`   
Required. Model to be deployed.  
`sync` |  `bool`   
Whether to execute this method synchronously. If False, this method will be executed in concurrent Future and any downstream object will be immediately returned and synced when the Future has completed.  
`enable_access_logging` |  `bool`   
Whether to enable endpoint access logging. Defaults to False.  
  
### direct_predict
    
    
    direct_predict(
        inputs: typing.List,
        parameters: typing.Optional[typing.Dict] = None,
        timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.models.Prediction

Makes a direct (gRPC) prediction against this Endpoint for a pre-built image.

**Parameters**  
---  
**Name** | **Description**  
`inputs` |  `List`   
Required. The inputs that are the input to the prediction call. A DeployedModel may have an upper limit on the number of instances it supports per request, and when it is exceeded the prediction call errors in case of AutoML Models, or, in case of customer created Models, the behaviour is as documented by that Model. The schema of any single instance may be specified via Endpoint's DeployedModels' [Model's][google.cloud.aiplatform.v1beta1.DeployedModel.model] [PredictSchemata's][google.cloud.aiplatform.v1beta1.Model.predict_schemata] `instance_schema_uri`.  
`parameters` |  `Dict`   
Optional. The parameters that govern the prediction. The schema of the parameters may be specified via Endpoint's DeployedModels' [Model's][google.cloud.aiplatform.v1beta1.DeployedModel.model] [PredictSchemata's][google.cloud.aiplatform.v1beta1.Model.predict_schemata] `parameters_schema_uri`.  
`timeout` |  `Optional[float]`   
Optional. The timeout for this request in seconds.  
**Returns**  
---  
**Type** | **Description**  
`prediction (aiplatform.Prediction)` | The resulting prediction.  
  
### direct_predict_async
    
    
    direct_predict_async(
        inputs: typing.List,
        *,
        parameters: typing.Optional[typing.Dict] = None,
        timeout: typing.Optional[float] = None
    ) -> google.cloud.aiplatform.models.Prediction

Makes an asynchronous direct (gRPC) prediction against this Endpoint for a pre-built image.

Example usage:
    
    
    response = await my_endpoint.direct_predict_async(inputs=[...])
    my_predictions = response.predictions
    ```
    

**Parameters**  
---  
**Name** | **Description**  
`inputs` |  `List`   
Required. The inputs that are the input to the prediction call. A DeployedModel may have an upper limit on the number of instances it supports per request, and when it is exceeded the prediction call errors in case of AutoML Models, or, in case of customer created Models, the behaviour is as documented by that Model. The schema of any single instance may be specified via Endpoint's DeployedModels' [Model's][google.cloud.aiplatform.v1beta1.DeployedModel.model] [PredictSchemata's][google.cloud.aiplatform.v1beta1.Model.predict_schemata] `instance_schema_uri`.  
`parameters` |  `Dict`   
Optional. The parameters that govern the prediction. The schema of the parameters may be specified via Endpoint's DeployedModels' [Model's][google.cloud.aiplatform.v1beta1.DeployedModel.model] [PredictSchemata's][google.cloud.aiplatform.v1beta1.Model.predict_schemata] `parameters_schema_uri`.  
`timeout` |  `Optional[float]`   
Optional. The timeout for this request in seconds.  
**Returns**  
---  
**Type** | **Description**  
`prediction (aiplatform.Prediction)` | The resulting prediction.  
  
### direct_raw_predict
    
    
    direct_raw_predict(
        method_name: str, request: bytes, timeout: typing.Optional[float] = None
    ) -> google.cloud.aiplatform.models.Prediction

Makes a direct (gRPC) prediction request using arbitrary headers for a custom container.

Example usage:
    
    
    my_endpoint = aiplatform.Endpoint(ENDPOINT_ID)
    response = my_endpoint.direct_raw_predict(request=b'...')
    ```
    

**Parameters**  
---  
**Name** | **Description**  
`method_name` |  `str`   
Fully qualified name of the API method being invoked to perform prediction.  
`request` |  `bytes`   
The body of the prediction request in bytes.  
`timeout` |  `Optional[float]`   
Optional. The timeout for this request in seconds.  
**Returns**  
---  
**Type** | **Description**  
`prediction (aiplatform.Prediction)` | The resulting prediction.  
  
### direct_raw_predict_async
    
    
    direct_raw_predict_async(
        method_name: str, request: bytes, timeout: typing.Optional[float] = None
    ) -> google.cloud.aiplatform.models.Prediction

Makes a direct (gRPC) prediction request for a custom container.

Example usage:
    
    
    my_endpoint = aiplatform.Endpoint(ENDPOINT_ID)
    response = await my_endpoint.direct_raw_predict(request=b'...')
    ```
    

**Parameters**  
---  
**Name** | **Description**  
`method_name` |  `str`   
Fully qualified name of the API method being invoked to perform prediction.  
`request` |  `bytes`   
The body of the prediction request in bytes.  
`timeout` |  `Optional[float]`   
Optional. The timeout for this request in seconds.  
**Returns**  
---  
**Type** | **Description**  
`prediction (aiplatform.Prediction)` | The resulting prediction.  
  
### explain
    
    
    explain(
        instances: typing.List[typing.Dict],
        parameters: typing.Optional[typing.Dict] = None,
        deployed_model_id: typing.Optional[str] = None,
        timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.models.Prediction

Make a prediction with explanations against this Endpoint.

Example usage: response = my_endpoint.explain(instances=[...]) my_explanations = response.explanations

**Parameters**  
---  
**Name** | **Description**  
`instances` |  `List`   
Required. The instances that are the input to the prediction call. A DeployedModel may have an upper limit on the number of instances it supports per request, and when it is exceeded the prediction call errors in case of AutoML Models, or, in case of customer created Models, the behaviour is as documented by that Model. The schema of any single instance may be specified via Endpoint's DeployedModels' [Model's][google.cloud.aiplatform.v1beta1.DeployedModel.model] [PredictSchemata's][google.cloud.aiplatform.v1beta1.Model.predict_schemata] `instance_schema_uri`.  
`parameters` |  `Dict`   
The parameters that govern the prediction. The schema of the parameters may be specified via Endpoint's DeployedModels' [Model's ][google.cloud.aiplatform.v1beta1.DeployedModel.model] [PredictSchemata's][google.cloud.aiplatform.v1beta1.Model.predict_schemata] `parameters_schema_uri`.  
`deployed_model_id` |  `str`   
Optional. If specified, this ExplainRequest will be served by the chosen DeployedModel, overriding this Endpoint's traffic split.  
`timeout` |  `float`   
Optional. The timeout for this request in seconds.  
**Returns**  
---  
**Type** | **Description**  
`prediction (aiplatform.Prediction)` | Prediction with returned predictions, explanations, and Model ID.  
  
### explain_async
    
    
    explain_async(
        instances: typing.List[typing.Dict],
        *,
        parameters: typing.Optional[typing.Dict] = None,
        deployed_model_id: typing.Optional[str] = None,
        timeout: typing.Optional[float] = None
    ) -> google.cloud.aiplatform.models.Prediction

Make a prediction with explanations against this Endpoint.

Example usage:
    
    
    response = await my_endpoint.explain_async(instances=[...])
    my_explanations = response.explanations
    ```
    

**Parameters**  
---  
**Name** | **Description**  
`instances` |  `List`   
Required. The instances that are the input to the prediction call. A DeployedModel may have an upper limit on the number of instances it supports per request, and when it is exceeded the prediction call errors in case of AutoML Models, or, in case of customer created Models, the behaviour is as documented by that Model. The schema of any single instance may be specified via Endpoint's DeployedModels' [Model's][google.cloud.aiplatform.v1beta1.DeployedModel.model] [PredictSchemata's][google.cloud.aiplatform.v1beta1.Model.predict_schemata] `instance_schema_uri`.  
`parameters` |  `Dict`   
The parameters that govern the prediction. The schema of the parameters may be specified via Endpoint's DeployedModels' [Model's ][google.cloud.aiplatform.v1beta1.DeployedModel.model] [PredictSchemata's][google.cloud.aiplatform.v1beta1.Model.predict_schemata] `parameters_schema_uri`.  
`deployed_model_id` |  `str`   
Optional. If specified, this ExplainRequest will be served by the chosen DeployedModel, overriding this Endpoint's traffic split.  
`timeout` |  `float`   
Optional. The timeout for this request in seconds.  
**Returns**  
---  
**Type** | **Description**  
`prediction (aiplatform.Prediction)` | Prediction with returned predictions, explanations, and Model ID.  
  
### invoke
    
    
    invoke(
        request_path: str,
        body: bytes,
        headers: typing.Dict[str, str],
        deployed_model_id: typing.Optional[str] = None,
        stream: bool = False,
        timeout: typing.Optional[float] = None,
    ) -> typing.Union[requests.models.Response, typing.Iterator[requests.models.Response]]

Makes a prediction request for arbitrary paths.

Example usage: my_endpoint = aiplatform.Endpoint(ENDPOINT_ID)

# Unary request
    
    
    body = {
        "model": "",
        "messages": [
            {
                "role": "user",
                "content": "Hello!",
            }
        ],
    }
    
    response = my_endpoint.invoke(
        request_path="/v1/chat/completions",
        body = json.dumps(body).encode("utf-8"),
        headers = {'Content-Type':'application/json'},
    )
    status_code = response.status_code
    results = json.dumps(response.text)
    
    # Streaming request
    body = {
        "model": "",
        "messages": [
            {
                "role": "user",
                "content": "Hello!",
            }
        ],
        "stream": "true",
    }
    
    for chunk in my_endpoint.invoke(
        request_path="/v1/chat/completions",
        body = json.dumps(body).encode("utf-8"),
        headers = {'Content-Type':'application/json'},
        stream=True,
    ):
        chunk_text = chunk.decode('utf-8')
    

**Parameters**  
---  
**Name** | **Description**  
`request_path` |  `str`   
The request url to the model server. The request path must be a string that starts with a forward slash. Root can't be accessed.  
`body` |  `bytes`   
The body of the prediction request in bytes. This must not exceed 1.5 mb per request.  
`headers` |  `Dict[str, str]`   
The header of the request as a dictionary. There are no restrictions on the header.  
`deployed_model_id` |  `str`   
Optional. If specified, this InvokeRequest will be served by the chosen DeployedModel, overriding this Endpoint's traffic split.  
`stream` |  `bool`   
If set to True, streaming will be enabled.  
`timeout` |  `float`   
Optional. The timeout for this request in seconds.  
**Exceptions**  
---  
**Type** | **Description**  
`ImportError` | If there is an issue importing the `TCPKeepAliveAdapter` package.  
  
### list
    
    
    list(
        filter: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        project: typing.Optional[str] = None,
        location: typing.Optional[str] = None,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
    ) -> typing.List[google.cloud.aiplatform.models.Endpoint]

List all Endpoint resource instances.

Example Usage: aiplatform.Endpoint.list( filter='labels.my_label="my_label_value" OR display_name=!"old_endpoint"', )

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
`List[models.Endpoint]` | A list of Endpoint resource objects  
  
### list_models
    
    
    list_models() -> (
        typing.List[google.cloud.aiplatform_v1.types.endpoint.DeployedModel]
    )

Returns a list of the models deployed to this Endpoint.

**Returns**  
---  
**Type** | **Description**  
`deployed_models (List[aiplatform.gapic.DeployedModel])` | A list of the models deployed in this Endpoint.  
  
### predict
    
    
    predict(
        instances: typing.List,
        parameters: typing.Optional[typing.Dict] = None,
        timeout: typing.Optional[float] = None,
        use_raw_predict: typing.Optional[bool] = False,
        *,
        use_dedicated_endpoint: typing.Optional[bool] = False
    ) -> google.cloud.aiplatform.models.Prediction

Make a prediction against this Endpoint.

Example usage:
    
    
    response = my_endpoint.predict(instances=[...])
    my_predictions = response.predictions
    ```
    

**Parameters**  
---  
**Name** | **Description**  
`instances` |  `List`   
Required. The instances that are the input to the prediction call. A DeployedModel may have an upper limit on the number of instances it supports per request, and when it is exceeded the prediction call errors in case of AutoML Models, or, in case of customer created Models, the behaviour is as documented by that Model. The schema of any single instance may be specified via Endpoint's DeployedModels' [Model's][google.cloud.aiplatform.v1beta1.DeployedModel.model] [PredictSchemata's][google.cloud.aiplatform.v1beta1.Model.predict_schemata] `instance_schema_uri`.  
`parameters` |  `Dict`   
The parameters that govern the prediction. The schema of the parameters may be specified via Endpoint's DeployedModels' [Model's ][google.cloud.aiplatform.v1beta1.DeployedModel.model] [PredictSchemata's][google.cloud.aiplatform.v1beta1.Model.predict_schemata] `parameters_schema_uri`.  
`timeout` |  `float`   
Optional. The timeout for this request in seconds.  
`use_raw_predict` |  `bool`   
Optional. Default value is False. If set to True, the underlying prediction call will be made against Endpoint.raw_predict().  
`use_dedicated_endpoint` |  `bool`   
Optional. Default value is False. If set to True, the underlying prediction call will be made using the dedicated endpoint dns.  
**Exceptions**  
---  
**Type** | **Description**  
`ImportError` | If there is an issue importing the `TCPKeepAliveAdapter` package.  
`ValueError` | If the dedicated endpoint DNS is empty for dedicated endpoints.  
`ValueError` | If the prediction request fails for dedicated endpoints.  
**Returns**  
---  
**Type** | **Description**  
`prediction (aiplatform.Prediction)` | Prediction with returned predictions and Model ID.  
  
### predict_async
    
    
    predict_async(
        instances: typing.List,
        *,
        parameters: typing.Optional[typing.Dict] = None,
        timeout: typing.Optional[float] = None
    ) -> google.cloud.aiplatform.models.Prediction

Make an asynchronous prediction against this Endpoint. Example usage:
    
    
    response = await my_endpoint.predict_async(instances=[...])
    my_predictions = response.predictions
    ```
    
    For dedicated endpoints (`dedicated_endpoint_enabled=True`), the call
    is routed via async HTTPS POST to the endpoint's dedicated DNS,
    mirroring the synchronous `predict()` dedicated-endpoint path.
    Otherwise the GAPIC async prediction client is used.
    

**Parameters**  
---  
**Name** | **Description**  
`instances` |  `List`   
Required. The instances that are the input to the prediction call. A DeployedModel may have an upper limit on the number of instances it supports per request, and when it is exceeded the prediction call errors in case of AutoML Models, or, in case of customer created Models, the behaviour is as documented by that Model. The schema of any single instance may be specified via Endpoint's DeployedModels' [Model's][google.cloud.aiplatform.v1beta1.DeployedModel.model] [PredictSchemata's][google.cloud.aiplatform.v1beta1.Model.predict_schemata] `instance_schema_uri`.  
`parameters` |  `Dict`   
Optional. The parameters that govern the prediction. The schema of the parameters may be specified via Endpoint's DeployedModels' [Model's ][google.cloud.aiplatform.v1beta1.DeployedModel.model] [PredictSchemata's][google.cloud.aiplatform.v1beta1.Model.predict_schemata] `parameters_schema_uri`.  
`timeout` |  `float`   
Optional. The timeout for this request in seconds.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If the dedicated endpoint DNS is empty for dedicated endpoints, or if the prediction request to a dedicated endpoint returns a non-200 status.  
**Returns**  
---  
**Type** | **Description**  
`prediction (aiplatform.Prediction)` | Prediction with returned predictions and Model ID.  
  
### raw_predict
    
    
    raw_predict(
        body: bytes,
        headers: typing.Dict[str, str],
        *,
        use_dedicated_endpoint: typing.Optional[bool] = False,
        timeout: typing.Optional[float] = None
    ) -> requests.models.Response

Makes a prediction request using arbitrary headers.

Example usage: my_endpoint = aiplatform.Endpoint(ENDPOINT_ID) response = my_endpoint.raw_predict( body = b'{"instances":[{"feat_1":val_1, "feat_2":val_2}]}' headers = {'Content-Type':'application/json'} ) status_code = response.status_code results = json.dumps(response.text)

**Parameters**  
---  
**Name** | **Description**  
`body` |  `bytes`   
The body of the prediction request in bytes. This must not exceed 1.5 mb per request.  
`headers` |  `Dict[str, str]`   
The header of the request as a dictionary. There are no restrictions on the header.  
`use_dedicated_endpoint` |  `bool`   
Optional. Default value is False. If set to True, the underlying prediction call will be made using the dedicated endpoint dns.  
`timeout` |  `float`   
Optional. The timeout for this request in seconds.  
**Exceptions**  
---  
**Type** | **Description**  
`ImportError` | If there is an issue importing the `TCPKeepAliveAdapter` package.  
  
### stream_direct_predict
    
    
    stream_direct_predict(
        inputs_iterator: typing.Iterator[typing.List],
        parameters: typing.Optional[typing.Dict] = None,
        timeout: typing.Optional[float] = None,
    ) -> typing.Iterator[google.cloud.aiplatform.models.Prediction]

Makes a streaming direct (gRPC) prediction against this Endpoint for a pre-built image.

**Parameters**  
---  
**Name** | **Description**  
`inputs_iterator` |  `Iterator[List]`   
Required. An iterator of the inputs that are the input to the prediction call. A DeployedModel may have an upper limit on the number of instances it supports per request, and when it is exceeded the prediction call errors in case of AutoML Models, or, in case of customer created Models, the behaviour is as documented by that Model. The schema of any single instance may be specified via Endpoint's DeployedModels' [Model's][google.cloud.aiplatform.v1beta1.DeployedModel.model] [PredictSchemata's][google.cloud.aiplatform.v1beta1.Model.predict_schemata] `instance_schema_uri`.  
`parameters` |  `Dict`   
Optional. The parameters that govern the prediction. The schema of the parameters may be specified via Endpoint's DeployedModels' [Model's][google.cloud.aiplatform.v1beta1.DeployedModel.model] [PredictSchemata's][google.cloud.aiplatform.v1beta1.Model.predict_schemata] `parameters_schema_uri`.  
`timeout` |  `Optional[float] :Yields: *predictions (Iterator[aiplatform.Prediction])* -- The resulting streamed predictions.`   
Optional. The timeout for this request in seconds.  
  
### stream_direct_raw_predict
    
    
    stream_direct_raw_predict(
        method_name: str,
        requests: typing.Iterator[bytes],
        timeout: typing.Optional[float] = None,
    ) -> typing.Iterator[google.cloud.aiplatform.models.Prediction]

Makes a direct (gRPC) streaming prediction request for a custom container.

Example usage:
    
    
    my_endpoint = aiplatform.Endpoint(ENDPOINT_ID)
    for stream_response in my_endpoint.stream_direct_raw_predict(
        request=b'...'
    ):
        yield stream_response
    ```
    

**Parameters**  
---  
**Name** | **Description**  
`method_name` |  `str`   
Fully qualified name of the API method being invoked to perform prediction.  
`requests` |  `Iterator[bytes]`   
The body of the prediction requests in bytes.  
`timeout` |  `Optional[float] :Yields: *predictions (Iterator[aiplatform.Prediction])* -- The resulting streamed predictions.`   
Optional. The timeout for this request in seconds.  
  
### stream_raw_predict
    
    
    stream_raw_predict(
        body: bytes,
        headers: typing.Dict[str, str],
        *,
        use_dedicated_endpoint: typing.Optional[bool] = False,
        timeout: typing.Optional[float] = None
    ) -> typing.Iterator[requests.models.Response]

Makes a streaming prediction request using arbitrary headers. For custom model, this method is only supported for dedicated endpoint.

Example usage:
    
    
    my_endpoint = aiplatform.Endpoint(ENDPOINT_ID)
    for stream_response in my_endpoint.stream_raw_predict(
        body = b'{"instances":[{"feat_1":val_1, "feat_2":val_2}]}'
        headers = {'Content-Type':'application/json'}
    ):
        status_code = response.status_code
        stream_result = json.dumps(response.text)
    ```
    

**Parameters**  
---  
**Name** | **Description**  
`body` |  `bytes`   
The body of the prediction request in bytes. This must not exceed 10 mb per request.  
`headers` |  `Dict[str, str]`   
The header of the request as a dictionary. There are no restrictions on the header.  
`use_dedicated_endpoint` |  `bool`   
Optional. Default value is False. If set to True, the underlying prediction call will be made using the dedicated endpoint dns.  
`timeout` |  `float :Yields: *predictions (Iterator[requests.models.Response])* -- The streaming prediction results.`   
Optional. The timeout for this request in seconds.  
  
### to_dict
    
    
    to_dict() -> typing.Dict[str, typing.Any]

Returns the resource proto as a dictionary.

### undeploy
    
    
    undeploy(
        deployed_model_id: str,
        traffic_split: typing.Optional[typing.Dict[str, int]] = None,
        metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        sync=True,
    ) -> None

Undeploys a deployed model.

The model to be undeployed should have no traffic or user must provide a new traffic_split with the remaining deployed models. Refer to `Endpoint.traffic_split` for the current traffic split mapping.

**Parameters**  
---  
**Name** | **Description**  
`deployed_model_id` |  `str`   
Required. The ID of the DeployedModel to be undeployed from the Endpoint.  
`traffic_split` |  `Dict[str, int]`   
Optional. A map of DeployedModel IDs to the percentage of this Endpoint's traffic that should be forwarded to that DeployedModel. Required if undeploying a model with non-zero traffic from an Endpoint with multiple deployed models. The traffic percentage values must add up to 100, or map must be empty if the Endpoint is to not accept any traffic at the moment. If a DeployedModel's ID is not listed in this map, then it receives no traffic.  
`metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
  
### undeploy_all
    
    
    undeploy_all(sync: bool = True) -> google.cloud.aiplatform.models.Endpoint

Undeploys every model deployed to this Endpoint.

**Parameter**  
---  
**Name** | **Description**  
`sync` |  `bool`   
Whether to execute this method synchronously. If False, this method will be executed in concurrent Future and any downstream object will be immediately returned and synced when the Future has completed.  
  
### update
    
    
    update(
        display_name: typing.Optional[str] = None,
        description: typing.Optional[str] = None,
        labels: typing.Optional[typing.Dict[str, str]] = None,
        traffic_split: typing.Optional[typing.Dict[str, int]] = None,
        request_metadata: typing.Optional[typing.Sequence[typing.Tuple[str, str]]] = (),
        update_request_timeout: typing.Optional[float] = None,
    ) -> google.cloud.aiplatform.models.Endpoint

Updates an endpoint.

Example usage: my_endpoint = my_endpoint.update( display_name='my-updated-endpoint', description='my updated description', labels={'key': 'value'}, traffic_split={ '123456': 20, '234567': 80, }, )

**Parameters**  
---  
**Name** | **Description**  
`display_name` |  `str`   
Optional. The display name of the Endpoint. The name can be up to 128 characters long and can be consist of any UTF-8 characters.  
`description` |  `str`   
Optional. The description of the Endpoint.  
`labels` |  `Dict[str, str]`   
Optional. The labels with user-defined metadata to organize your Endpoints. Label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. See <https://goo.gl/xmQnxf> for more information and examples of labels.  
`traffic_split` |  `Dict[str, int]`   
Optional. A map from a DeployedModel's ID to the percentage of this Endpoint's traffic that should be forwarded to that DeployedModel. If a DeployedModel's ID is not listed in this map, then it receives no traffic. The traffic percentage values must add up to 100, or map must be empty if the Endpoint is to not accept any traffic at a moment.  
`request_metadata` |  `Sequence[Tuple[str, str]]`   
Optional. Strings which should be sent along with the request as metadata.  
`update_request_timeout` |  `float`   
Optional. The timeout for the update request in seconds.  
**Exceptions**  
---  
**Type** | **Description**  
`ValueError` | If `labels` is not the correct format.  
**Returns**  
---  
**Type** | **Description**  
`Endpoint (aiplatform.Prediction)` | Updated endpoint resource.  
  
### wait
    
    
    wait()

Helper method that blocks until all futures are complete.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
