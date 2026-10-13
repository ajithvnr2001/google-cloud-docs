---
url: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient
title: Class AutoMlAsyncClient (2.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:57:40.066823+00:00
---

# Class AutoMlAsyncClient (2.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AutoMlAsyncClient (2.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.21.0 (latest)  2.20.1  2.19.0  2.18.1  2.17.0  2.16.4  2.15.0  2.14.1  2.13.5  2.12.0  2.11.4  2.10.1  2.9.0  2.8.3  2.7.3  2.6.0  2.5.2  2.4.2  2.3.0  2.2.0  2.1.0  2.0.0  1.0.3  0.10.0  0.9.0  0.8.0  0.7.1  0.6.0  0.5.0  0.4.0 
    
    
    AutoMlAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.automl_v1beta1.services.auto_ml.transports.base.AutoMlTransport,
                typing.Callable[
                    [...],
                    google.cloud.automl_v1beta1.services.auto_ml.transports.base.AutoMlTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

AutoML Server API.

The resource names are assigned by the server. The server never reuses names that it has created after the resources with those names are deleted.

An ID of a resource is the last element of the item's resource name. For `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}`, then the id for the item is `{dataset_id}`.

Currently the only supported `location_id` is "us-central1".

On any input that is documented to expect a string parameter in snake_case or kebab-case, either of those cases is accepted.

## Properties 

### api_endpoint

Return the API endpoint used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The API endpoint used by the client instance.  
  
### transport

Returns the transport used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`AutoMlTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### AutoMlAsyncClient
    
    
    AutoMlAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.automl_v1beta1.services.auto_ml.transports.base.AutoMlTransport,
                typing.Callable[
                    [...],
                    google.cloud.automl_v1beta1.services.auto_ml.transports.base.AutoMlTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the auto ml async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,AutoMlTransport,Callable[..., AutoMlTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the AutoMlTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### annotation_spec_path
    
    
    annotation_spec_path(
        project: str, location: str, dataset: str, annotation_spec: str
    ) -> str

Returns a fully-qualified annotation_spec string.

### column_spec_path
    
    
    column_spec_path(
        project: str, location: str, dataset: str, table_spec: str, column_spec: str
    ) -> str

Returns a fully-qualified column_spec string.

### common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

### common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

### common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

### common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

### common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

### create_dataset
    
    
    create_dataset(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.CreateDatasetRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        dataset: typing.Optional[google.cloud.automl_v1beta1.types.dataset.Dataset] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.dataset.Dataset

Creates a dataset.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_create_dataset():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        dataset = automl_v1beta1.[Dataset](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Dataset.html)()
        dataset.translation_dataset_metadata.source_language_code = "source_language_code_value"
        dataset.translation_dataset_metadata.target_language_code = "target_language_code_value"
    
        request = automl_v1beta1.[CreateDatasetRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.CreateDatasetRequest.html)(
            parent="parent_value",
            dataset=dataset,
        )
    
        # Make the request
        response = await client.[create_dataset](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_create_dataset)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.CreateDatasetRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.CreateDatasetRequest), dict]]`   
The request object. Request message for AutoMl.CreateDataset.  
`parent` |  ``str``   
Required. The resource name of the project to create the dataset for. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`dataset` |  `[Dataset](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Dataset)`   
Required. The dataset to create. This corresponds to the `dataset` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.automl_v1beta1.types.Dataset](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Dataset)` | A workspace for solving a single, particular machine learning (ML) problem. A workspace contains examples that may be annotated.  
  
### create_model
    
    
    create_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.CreateModelRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        model: typing.Optional[google.cloud.automl_v1beta1.types.model.Model] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a model. Returns a Model in the `response][google.longrunning.Operation.response]` field when it completes. When you create a model, several model evaluations are created for it: a global evaluation, and one evaluation for each annotation spec.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_create_model():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[CreateModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.CreateModelRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        operation = await client.[create_model](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_create_model)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.CreateModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.CreateModelRequest), dict]]`   
The request object. Request message for AutoMl.CreateModel.  
`parent` |  ``str``   
Required. Resource name of the parent project where the model is being created. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`model` |  `[Model](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Model)`   
Required. The model to create. This corresponds to the `model` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Model](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Model) API proto representing a trained machine learning model.  
  
### dataset_path
    
    
    dataset_path(project: str, location: str, dataset: str) -> str

Returns a fully-qualified dataset string.

### delete_dataset
    
    
    delete_dataset(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.DeleteDatasetRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Deletes a dataset and all of its contents. Returns empty response in the `response][google.longrunning.Operation.response]` field when it completes, and `delete_details` in the `metadata][google.longrunning.Operation.metadata]` field.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_delete_dataset():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[DeleteDatasetRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DeleteDatasetRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_dataset](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_delete_dataset)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.DeleteDatasetRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DeleteDatasetRequest), dict]]`   
The request object. Request message for AutoMl.DeleteDataset.  
`name` |  ``str``   
Required. The resource name of the dataset to delete. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### delete_model
    
    
    delete_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.DeleteModelRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Deletes a model. Returns `google.protobuf.Empty` in the `response][google.longrunning.Operation.response]` field when it completes, and `delete_details` in the `metadata][google.longrunning.Operation.metadata]` field.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_delete_model():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[DeleteModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DeleteModelRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_model](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_delete_model)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.DeleteModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DeleteModelRequest), dict]]`   
The request object. Request message for AutoMl.DeleteModel.  
`name` |  ``str``   
Required. Resource name of the model being deleted. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### deploy_model
    
    
    deploy_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.DeployModelRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Deploys a model. If a model is already deployed, deploying it with the same parameters has no effect. Deploying with different parametrs (as e.g. changing

xref_node_number) will reset the deployment state without pausing the model's availability.

Only applicable for Text Classification, Image Object Detection , Tables, and Image Segmentation; all other domains manage deployment automatically.

Returns an empty response in the `response][google.longrunning.Operation.response]` field when it completes.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_deploy_model():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[DeployModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DeployModelRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[deploy_model](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_deploy_model)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.DeployModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.DeployModelRequest), dict]]`   
The request object. Request message for AutoMl.DeployModel.  
`name` |  ``str``   
Required. Resource name of the model to deploy. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### export_data
    
    
    export_data(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.ExportDataRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        output_config: typing.Optional[
            google.cloud.automl_v1beta1.types.io.OutputConfig
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Exports dataset's data to the provided output location. Returns an empty response in the `response][google.longrunning.Operation.response]` field when it completes.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_export_data():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[ExportDataRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ExportDataRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[export_data](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_export_data)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.ExportDataRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ExportDataRequest), dict]]`   
The request object. Request message for AutoMl.ExportData.  
`name` |  ``str``   
Required. The resource name of the dataset. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`output_config` |  `[OutputConfig](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.OutputConfig)`   
Required. The desired output location. This corresponds to the `output_config` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### export_evaluated_examples
    
    
    export_evaluated_examples(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.ExportEvaluatedExamplesRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        output_config: typing.Optional[
            google.cloud.automl_v1beta1.types.io.ExportEvaluatedExamplesOutputConfig
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Exports examples on which the model was evaluated (i.e. which were in the TEST set of the dataset the model was created from), together with their ground truth annotations and the annotations created (predicted) by the model. The examples, ground truth and predictions are exported in the state they were at the moment the model was evaluated.

This export is available only for 30 days since the model evaluation is created.

Currently only available for Tables.

Returns an empty response in the `response][google.longrunning.Operation.response]` field when it completes.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_export_evaluated_examples():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[ExportEvaluatedExamplesRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ExportEvaluatedExamplesRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[export_evaluated_examples](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_export_evaluated_examples)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.ExportEvaluatedExamplesRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ExportEvaluatedExamplesRequest), dict]]`   
The request object. Request message for AutoMl.ExportEvaluatedExamples.  
`name` |  ``str``   
Required. The resource name of the model whose evaluated examples are to be exported. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`output_config` |  `[ExportEvaluatedExamplesOutputConfig](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ExportEvaluatedExamplesOutputConfig)`   
Required. The desired output location and configuration. This corresponds to the `output_config` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### export_model
    
    
    export_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.ExportModelRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        output_config: typing.Optional[
            google.cloud.automl_v1beta1.types.io.ModelExportOutputConfig
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Exports a trained, "export-able", model to a user specified Google Cloud Storage location. A model is considered export-able if and only if it has an export format defined for it in

xref_ModelExportOutputConfig.

Returns an empty response in the `response][google.longrunning.Operation.response]` field when it completes.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_export_model():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[ExportModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ExportModelRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[export_model](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_export_model)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.ExportModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ExportModelRequest), dict]]`   
The request object. Request message for AutoMl.ExportModel. Models need to be enabled for exporting, otherwise an error code will be returned.  
`name` |  ``str``   
Required. The resource name of the model to export. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`output_config` |  `ModelExportOutputConfig`   
Required. The desired output location and configuration. This corresponds to the `output_config` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

**Parameter**  
---  
**Name** | **Description**  
`filename` |  `str`   
The path to the service account private key json file.  
**Returns**  
---  
**Type** | **Description**  
`AutoMlAsyncClient` | The constructed client.  
  
### from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

**Parameter**  
---  
**Name** | **Description**  
`info` |  `dict`   
The service account private key info.  
**Returns**  
---  
**Type** | **Description**  
`AutoMlAsyncClient` | The constructed client.  
  
### from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

**Parameter**  
---  
**Name** | **Description**  
`filename` |  `str`   
The path to the service account private key json file.  
**Returns**  
---  
**Type** | **Description**  
`AutoMlAsyncClient` | The constructed client.  
  
### get_annotation_spec
    
    
    get_annotation_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.GetAnnotationSpecRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.annotation_spec.AnnotationSpec

Gets an annotation spec.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_get_annotation_spec():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[GetAnnotationSpecRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GetAnnotationSpecRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_annotation_spec](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_get_annotation_spec)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.GetAnnotationSpecRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GetAnnotationSpecRequest), dict]]`   
The request object. Request message for AutoMl.GetAnnotationSpec.  
`name` |  ``str``   
Required. The resource name of the annotation spec to retrieve. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.automl_v1beta1.types.AnnotationSpec](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.AnnotationSpec)` | A definition of an annotation spec.  
  
### get_column_spec
    
    
    get_column_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.GetColumnSpecRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.column_spec.ColumnSpec

Gets a column spec.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_get_column_spec():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[GetColumnSpecRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GetColumnSpecRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_column_spec](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_get_column_spec)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.GetColumnSpecRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GetColumnSpecRequest), dict]]`   
The request object. Request message for AutoMl.GetColumnSpec.  
`name` |  ``str``   
Required. The resource name of the column spec to retrieve. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.automl_v1beta1.types.ColumnSpec](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ColumnSpec)` | A representation of a column in a relational table. When listing them, column specs are returned in the same order in which they were given on import . Used by: \\* Tables  
  
### get_dataset
    
    
    get_dataset(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.GetDatasetRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.dataset.Dataset

Gets a dataset.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_get_dataset():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[GetDatasetRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GetDatasetRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_dataset](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_get_dataset)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.GetDatasetRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GetDatasetRequest), dict]]`   
The request object. Request message for AutoMl.GetDataset.  
`name` |  ``str``   
Required. The resource name of the dataset to retrieve. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.automl_v1beta1.types.Dataset](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Dataset)` | A workspace for solving a single, particular machine learning (ML) problem. A workspace contains examples that may be annotated.  
  
### get_model
    
    
    get_model(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.GetModelRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.model.Model

Gets a model.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_get_model():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[GetModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GetModelRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_model](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_get_model)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.GetModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GetModelRequest), dict]]`   
The request object. Request message for AutoMl.GetModel.  
`name` |  ``str``   
Required. Resource name of the model. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.automl_v1beta1.types.Model](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Model)` | API proto representing a trained machine learning model.  
  
### get_model_evaluation
    
    
    get_model_evaluation(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.GetModelEvaluationRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.model_evaluation.ModelEvaluation

Gets a model evaluation.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_get_model_evaluation():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[GetModelEvaluationRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GetModelEvaluationRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_model_evaluation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_get_model_evaluation)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.GetModelEvaluationRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GetModelEvaluationRequest), dict]]`   
The request object. Request message for AutoMl.GetModelEvaluation.  
`name` |  ``str``   
Required. Resource name for the model evaluation. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.automl_v1beta1.types.ModelEvaluation](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ModelEvaluation)` | Evaluation results of a model.  
  
### get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

The client cert source is determined in the following order: (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the client cert source is None. (2) if `client_options.client_cert_source` is provided, use the provided one; if the default client cert source exists, use the default one; otherwise the client cert source is None.

The API endpoint is determined in the following order: (1) if `client_options.api_endpoint` if provided, use the provided one. (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the default mTLS endpoint; if the environment variable is "never", use the default API endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise use the default API endpoint.

More details can be found at <https://google.aip.dev/auth/4114>.

**Parameter**  
---  
**Name** | **Description**  
`client_options` |  `google.api_core.client_options.ClientOptions`   
Custom options for the client. Only the `api_endpoint` and `client_cert_source` properties may be used in this method.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTLSChannelError` | If any errors happen.  
**Returns**  
---  
**Type** | **Description**  
`Tuple[str, Callable[[], Tuple[bytes, bytes]]]` | returns the API endpoint and the client cert source to use.  
  
### get_table_spec
    
    
    get_table_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.GetTableSpecRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.table_spec.TableSpec

Gets a table spec.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_get_table_spec():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[GetTableSpecRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GetTableSpecRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_table_spec](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_get_table_spec)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.GetTableSpecRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.GetTableSpecRequest), dict]]`   
The request object. Request message for AutoMl.GetTableSpec.  
`name` |  ``str``   
Required. The resource name of the table spec to retrieve. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.automl_v1beta1.types.TableSpec](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TableSpec)` | A specification of a relational table. The table's schema is represented via its child column specs. It is pre-populated as part of ImportData by schema inference algorithm, the version of which is a required parameter of ImportData InputConfig. Note: While working with a table, at times the schema may be inconsistent with the data in the table (e.g. string in a FLOAT64 column). The consistency validation is done upon creation of a model. Used by: \\* Tables  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.automl_v1beta1.services.auto_ml.transports.base.AutoMlTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### import_data
    
    
    import_data(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.ImportDataRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        input_config: typing.Optional[
            google.cloud.automl_v1beta1.types.io.InputConfig
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Imports data into a dataset. For Tables this method can only be called on an empty Dataset.

For Tables:

  * A xref_schema_inference_version parameter must be explicitly set. Returns an empty response in the `response][google.longrunning.Operation.response]` field when it completes.


    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_import_data():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[ImportDataRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ImportDataRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[import_data](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_import_data)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.ImportDataRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ImportDataRequest), dict]]`   
The request object. Request message for AutoMl.ImportData.  
`name` |  ``str``   
Required. Dataset name. Dataset must already exist. All imported annotations and examples will be added. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`input_config` |  `[InputConfig](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.InputConfig)`   
Required. The desired input location and its domain specific semantics, if any. This corresponds to the `input_config` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### list_column_specs
    
    
    list_column_specs(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.ListColumnSpecsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.services.auto_ml.pagers.ListColumnSpecsAsyncPager

Lists column specs in a table spec.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_list_column_specs():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[ListColumnSpecsRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListColumnSpecsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_column_specs](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_list_column_specs)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.ListColumnSpecsRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListColumnSpecsRequest), dict]]`   
The request object. Request message for AutoMl.ListColumnSpecs.  
`parent` |  ``str``   
Required. The resource name of the table spec to list column specs from. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.automl_v1beta1.services.auto_ml.pagers.ListColumnSpecsAsyncPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListColumnSpecsAsyncPager)` | Response message for AutoMl.ListColumnSpecs. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_datasets
    
    
    list_datasets(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.ListDatasetsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.services.auto_ml.pagers.ListDatasetsAsyncPager

Lists datasets in a project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_list_datasets():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[ListDatasetsRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListDatasetsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_datasets](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_list_datasets)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.ListDatasetsRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListDatasetsRequest), dict]]`   
The request object. Request message for AutoMl.ListDatasets.  
`parent` |  ``str``   
Required. The resource name of the project from which to list datasets. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.automl_v1beta1.services.auto_ml.pagers.ListDatasetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListDatasetsAsyncPager)` | Response message for AutoMl.ListDatasets. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_model_evaluations
    
    
    list_model_evaluations(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.ListModelEvaluationsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelEvaluationsAsyncPager

Lists model evaluations.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_list_model_evaluations():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[ListModelEvaluationsRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelEvaluationsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_model_evaluations](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_list_model_evaluations)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.ListModelEvaluationsRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelEvaluationsRequest), dict]]`   
The request object. Request message for AutoMl.ListModelEvaluations.  
`parent` |  ``str``   
Required. Resource name of the model to list the model evaluations for. If modelId is set as "-", this will list model evaluations from across all models of the parent location. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelEvaluationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelEvaluationsAsyncPager)` | Response message for AutoMl.ListModelEvaluations. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_models
    
    
    list_models(
        request: typing.Optional[
            typing.Union[google.cloud.automl_v1beta1.types.service.ListModelsRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelsAsyncPager

Lists models.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_list_models():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[ListModelsRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_models](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_list_models)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.ListModelsRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListModelsRequest), dict]]`   
The request object. Request message for AutoMl.ListModels.  
`parent` |  ``str``   
Required. Resource name of the project, from which to list the models. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelsAsyncPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListModelsAsyncPager)` | Response message for AutoMl.ListModels. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_table_specs
    
    
    list_table_specs(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.ListTableSpecsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.services.auto_ml.pagers.ListTableSpecsAsyncPager

Lists table specs in a dataset.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_list_table_specs():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[ListTableSpecsRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListTableSpecsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_table_specs](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_list_table_specs)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.ListTableSpecsRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ListTableSpecsRequest), dict]]`   
The request object. Request message for AutoMl.ListTableSpecs.  
`parent` |  ``str``   
Required. The resource name of the dataset to list table specs from. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.automl_v1beta1.services.auto_ml.pagers.ListTableSpecsAsyncPager](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.pagers.ListTableSpecsAsyncPager)` | Response message for AutoMl.ListTableSpecs. Iterating over this object will yield results and resolve additional pages automatically.  
  
### model_evaluation_path
    
    
    model_evaluation_path(
        project: str, location: str, model: str, model_evaluation: str
    ) -> str

Returns a fully-qualified model_evaluation string.

### model_path
    
    
    model_path(project: str, location: str, model: str) -> str

Returns a fully-qualified model string.

### parse_annotation_spec_path
    
    
    parse_annotation_spec_path(path: str) -> typing.Dict[str, str]

Parses a annotation_spec path into its component segments.

### parse_column_spec_path
    
    
    parse_column_spec_path(path: str) -> typing.Dict[str, str]

Parses a column_spec path into its component segments.

### parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

### parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

### parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

### parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

### parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

### parse_dataset_path
    
    
    parse_dataset_path(path: str) -> typing.Dict[str, str]

Parses a dataset path into its component segments.

### parse_model_evaluation_path
    
    
    parse_model_evaluation_path(path: str) -> typing.Dict[str, str]

Parses a model_evaluation path into its component segments.

### parse_model_path
    
    
    parse_model_path(path: str) -> typing.Dict[str, str]

Parses a model path into its component segments.

### parse_table_spec_path
    
    
    parse_table_spec_path(path: str) -> typing.Dict[str, str]

Parses a table_spec path into its component segments.

### table_spec_path
    
    
    table_spec_path(project: str, location: str, dataset: str, table_spec: str) -> str

Returns a fully-qualified table_spec string.

### undeploy_model
    
    
    undeploy_model(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.UndeployModelRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Undeploys a model. If the model is not deployed this method has no effect.

Only applicable for Text Classification, Image Object Detection and Tables; all other domains manage deployment automatically.

Returns an empty response in the `response][google.longrunning.Operation.response]` field when it completes.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_undeploy_model():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[UndeployModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.UndeployModelRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[undeploy_model](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_undeploy_model)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.UndeployModelRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.UndeployModelRequest), dict]]`   
The request object. Request message for AutoMl.UndeployModel.  
`name` |  ``str``   
Required. Resource name of the model to undeploy. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### update_column_spec
    
    
    update_column_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.UpdateColumnSpecRequest, dict
            ]
        ] = None,
        *,
        column_spec: typing.Optional[
            google.cloud.automl_v1beta1.types.column_spec.ColumnSpec
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.column_spec.ColumnSpec

Updates a column spec.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_update_column_spec():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[UpdateColumnSpecRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.UpdateColumnSpecRequest.html)(
        )
    
        # Make the request
        response = await client.[update_column_spec](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_update_column_spec)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.UpdateColumnSpecRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.UpdateColumnSpecRequest), dict]]`   
The request object. Request message for AutoMl.UpdateColumnSpec  
`column_spec` |  `[ColumnSpec](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ColumnSpec)`   
Required. The column spec which replaces the resource on the server. This corresponds to the `column_spec` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.automl_v1beta1.types.ColumnSpec](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.ColumnSpec)` | A representation of a column in a relational table. When listing them, column specs are returned in the same order in which they were given on import . Used by: \\* Tables  
  
### update_dataset
    
    
    update_dataset(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.UpdateDatasetRequest, dict
            ]
        ] = None,
        *,
        dataset: typing.Optional[google.cloud.automl_v1beta1.types.dataset.Dataset] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.dataset.Dataset

Updates a dataset.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_update_dataset():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        dataset = automl_v1beta1.[Dataset](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Dataset.html)()
        dataset.translation_dataset_metadata.source_language_code = "source_language_code_value"
        dataset.translation_dataset_metadata.target_language_code = "target_language_code_value"
    
        request = automl_v1beta1.[UpdateDatasetRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.UpdateDatasetRequest.html)(
            dataset=dataset,
        )
    
        # Make the request
        response = await client.[update_dataset](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_update_dataset)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.UpdateDatasetRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.UpdateDatasetRequest), dict]]`   
The request object. Request message for AutoMl.UpdateDataset  
`dataset` |  `[Dataset](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Dataset)`   
Required. The dataset which replaces the resource on the server. This corresponds to the `dataset` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.automl_v1beta1.types.Dataset](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.Dataset)` | A workspace for solving a single, particular machine learning (ML) problem. A workspace contains examples that may be annotated.  
  
### update_table_spec
    
    
    update_table_spec(
        request: typing.Optional[
            typing.Union[
                google.cloud.automl_v1beta1.types.service.UpdateTableSpecRequest, dict
            ]
        ] = None,
        *,
        table_spec: typing.Optional[
            google.cloud.automl_v1beta1.types.table_spec.TableSpec
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.automl_v1beta1.types.table_spec.TableSpec

Updates a table spec.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import automl_v1beta1
    
    async def sample_update_table_spec():
        # Create a client
        client = automl_v1beta1.[AutoMlAsyncClient](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html)()
    
        # Initialize request argument(s)
        request = automl_v1beta1.[UpdateTableSpecRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.UpdateTableSpecRequest.html)(
        )
    
        # Make the request
        response = await client.[update_table_spec](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.services.auto_ml.AutoMlAsyncClient.html#google_cloud_automl_v1beta1_services_auto_ml_AutoMlAsyncClient_update_table_spec)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.automl_v1beta1.types.UpdateTableSpecRequest](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.UpdateTableSpecRequest), dict]]`   
The request object. Request message for AutoMl.UpdateTableSpec  
`table_spec` |  `[TableSpec](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TableSpec)`   
Required. The table spec which replaces the resource on the server. This corresponds to the `table_spec` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.automl_v1beta1.types.TableSpec](https://docs.cloud.google.com/python/docs/reference/automl/latest/google.cloud.automl_v1beta1.types.TableSpec)` | A specification of a relational table. The table's schema is represented via its child column specs. It is pre-populated as part of ImportData by schema inference algorithm, the version of which is a required parameter of ImportData InputConfig. Note: While working with a table, at times the schema may be inconsistent with the data in the table (e.g. string in a FLOAT64 column). The consistency validation is done upon creation of a model. Used by: \\* Tables  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
