---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient
title: Class DataAgentServiceClient (0.13.5) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:29.991575+00:00
---

# Class DataAgentServiceClient (0.13.5)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DataAgentServiceClient (0.13.5) Stay organized with collections  Save and categorize content based on your preferences. 

0.13.5 (latest)  0.13.4  0.12.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    DataAgentServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.transports.base.DataAgentServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.transports.base.DataAgentServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Service describing handlers for resources.

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
`DataAgentServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### DataAgentServiceClient
    
    
    DataAgentServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.transports.base.DataAgentServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.transports.base.DataAgentServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the data agent service client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,DataAgentServiceTransport,Callable[..., DataAgentServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the DataAgentServiceTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that the `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTLSChannelError` | If mutual TLS transport creation failed for any reason.  
  
### __exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

**Warning:** ONLY use as a context manager if the transport is NOT shared with other clients! Exiting the with block will CLOSE the transport and may cause errors in other clients! 

### cancel_operation
    
    
    cancel_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.CancelOperationRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Starts asynchronous cancellation on a long-running operation.

The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.CancelOperationRequest``   
The request object. Request message for `CancelOperation` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
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

### create_data_agent
    
    
    create_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.CreateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent
        ] = None,
        data_agent_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new DataAgent in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import geminidataanalytics_v1alpha
    
    def sample_create_data_agent():
        # Create a client
        client = geminidataanalytics_v1alpha.[DataAgentServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html)()
    
        # Initialize request argument(s)
        request = geminidataanalytics_v1alpha.[CreateDataAgentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.CreateDataAgentRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        operation = client.[create_data_agent](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_create_data_agent)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.geminidataanalytics_v1alpha.types.CreateDataAgentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.CreateDataAgentRequest), dict]`   
The request object. Message for creating a DataAgent.  
`parent` |  `str`   
Required. Value for parent. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`data_agent` |  `[google.cloud.geminidataanalytics_v1alpha.types.DataAgent](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.DataAgent)`   
Required. The resource being created. This corresponds to the `data_agent` field on the `request` instance; if `request` is provided, this should not be set.  
`data_agent_id` |  `str`   
Optional. Id of the requesting object. Must be unique within the parent. The allowed format is: `^[a-z](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$`. If not provided, the server will auto-generate a value for the id. This corresponds to the `data_agent_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [DataAgent](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.DataAgent) Message describing a DataAgent object.  
  
### create_data_agent_sync
    
    
    create_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.CreateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent
        ] = None,
        data_agent_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent

Creates a new DataAgent in a given project and location synchronously.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import geminidataanalytics_v1alpha
    
    def sample_create_data_agent_sync():
        # Create a client
        client = geminidataanalytics_v1alpha.[DataAgentServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html)()
    
        # Initialize request argument(s)
        request = geminidataanalytics_v1alpha.[CreateDataAgentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.CreateDataAgentRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = client.[create_data_agent_sync](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_create_data_agent_sync)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.geminidataanalytics_v1alpha.types.CreateDataAgentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.CreateDataAgentRequest), dict]`   
The request object. Message for creating a DataAgent.  
`parent` |  `str`   
Required. Value for parent. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`data_agent` |  `[google.cloud.geminidataanalytics_v1alpha.types.DataAgent](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.DataAgent)`   
Required. The resource being created. This corresponds to the `data_agent` field on the `request` instance; if `request` is provided, this should not be set.  
`data_agent_id` |  `str`   
Optional. Id of the requesting object. Must be unique within the parent. The allowed format is: `^[a-z](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/\[a-z0-9-\]{0,61}\[a-z0-9\])?$`. If not provided, the server will auto-generate a value for the id. This corresponds to the `data_agent_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.geminidataanalytics_v1alpha.types.DataAgent](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.DataAgent)` | Message describing a DataAgent object.  
  
### crypto_key_path
    
    
    crypto_key_path(project: str, location: str, key_ring: str, crypto_key: str) -> str

Returns a fully-qualified crypto_key string.

### data_agent_path
    
    
    data_agent_path(project: str, location: str, data_agent: str) -> str

Returns a fully-qualified data_agent string.

### delete_data_agent
    
    
    delete_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.DeleteDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Deletes a single DataAgent.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import geminidataanalytics_v1alpha
    
    def sample_delete_data_agent():
        # Create a client
        client = geminidataanalytics_v1alpha.[DataAgentServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html)()
    
        # Initialize request argument(s)
        request = geminidataanalytics_v1alpha.[DeleteDataAgentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.DeleteDataAgentRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_data_agent](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_delete_data_agent)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.geminidataanalytics_v1alpha.types.DeleteDataAgentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.DeleteDataAgentRequest), dict]`   
The request object. Message for deleting a DataAgent.  
`name` |  `str`   
Required. Name of the resource. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be `google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated empty messages in your APIs. A typical example is to use it as the request or the response type of an API method. For instance: service Foo { rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty); }  
  
### delete_data_agent_sync
    
    
    delete_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.DeleteDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Deletes a single DataAgent synchronously.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import geminidataanalytics_v1alpha
    
    def sample_delete_data_agent_sync():
        # Create a client
        client = geminidataanalytics_v1alpha.[DataAgentServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html)()
    
        # Initialize request argument(s)
        request = geminidataanalytics_v1alpha.[DeleteDataAgentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.DeleteDataAgentRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[delete_data_agent_sync](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_delete_data_agent_sync)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.geminidataanalytics_v1alpha.types.DeleteDataAgentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.DeleteDataAgentRequest), dict]`   
The request object. Message for deleting a DataAgent.  
`name` |  `str`   
Required. Name of the resource. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_operation
    
    
    delete_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.DeleteOperationRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Deletes a long-running operation.

This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.DeleteOperationRequest``   
The request object. Request message for `DeleteOperation` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
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
`DataAgentServiceClient` | The constructed client.  
  
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
`DataAgentServiceClient` | The constructed client.  
  
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
`DataAgentServiceClient` | The constructed client.  
  
### get_data_agent
    
    
    get_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.GetDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent

Gets details of a single DataAgent.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import geminidataanalytics_v1alpha
    
    def sample_get_data_agent():
        # Create a client
        client = geminidataanalytics_v1alpha.[DataAgentServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html)()
    
        # Initialize request argument(s)
        request = geminidataanalytics_v1alpha.[GetDataAgentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.GetDataAgentRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_data_agent](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_get_data_agent)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.geminidataanalytics_v1alpha.types.GetDataAgentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.GetDataAgentRequest), dict]`   
The request object. Message for getting a DataAgent.  
`name` |  `str`   
Required. Name of the resource. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.geminidataanalytics_v1alpha.types.DataAgent](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.DataAgent)` | Message describing a DataAgent object.  
  
### get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM policy for DataAgent
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import geminidataanalytics_v1alpha
    import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
    
    def sample_get_iam_policy():
        # Create a client
        client = geminidataanalytics_v1alpha.[DataAgentServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html)()
    
        # Initialize request argument(s)
        request = iam_policy_pb2.GetIamPolicyRequest(
            resource="resource_value",
        )
    
        # Make the request
        response = client.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_get_iam_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L111-L118), dict]`   
The request object. Request message for `GetIamPolicy` method.  
`resource` |  `str`   
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.iam.v1.policy_pb2.Policy` | An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A Policy is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a binding can also specify a condition, which is a logical expression that allows access to a resource only if the expression evaluates to true. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** :literal:` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ],="" "etag":="" "bwwwja0yfja=", " version":="" 3="">`\ \` **YAML example:** :literal:` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01t00:00:00.000z')="" etag:="" bwwwja0yfja="version:">`\ \` For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).  
  
### get_location
    
    
    get_location(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.GetLocationRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.location.locations_pb2.Location

Gets information about a location.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.location_pb2.GetLocationRequest``   
The request object. Request message for `GetLocation` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.location_pb2.Location`` | Location object.  
  
### get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated. Return the API endpoint and client cert source for mutual TLS.

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
  
### get_operation
    
    
    get_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.GetOperationRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.longrunning.operations_pb2.Operation

Gets the latest state of a long-running operation.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.GetOperationRequest``   
The request object. Request message for `GetOperation` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.operations_pb2.Operation`` | An `Operation` object.  
  
### list_accessible_data_agents
    
    
    list_accessible_data_agents(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListAccessibleDataAgentsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListAccessibleDataAgentsPager
    )

Lists DataAgents that are accessible to the caller in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import geminidataanalytics_v1alpha
    
    def sample_list_accessible_data_agents():
        # Create a client
        client = geminidataanalytics_v1alpha.[DataAgentServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html)()
    
        # Initialize request argument(s)
        request = geminidataanalytics_v1alpha.[ListAccessibleDataAgentsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.ListAccessibleDataAgentsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_accessible_data_agents](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_list_accessible_data_agents)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.geminidataanalytics_v1alpha.types.ListAccessibleDataAgentsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.ListAccessibleDataAgentsRequest), dict]`   
The request object. Message for requesting list of accessible DataAgents.  
`parent` |  `str`   
Required. Parent value for ListAccessibleDataAgentsRequest. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListAccessibleDataAgentsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListAccessibleDataAgentsPager)` | Message for response to listing accessible DataAgents. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_data_agents
    
    
    list_data_agents(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.ListDataAgentsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListDataAgentsPager
    )

Lists DataAgents in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import geminidataanalytics_v1alpha
    
    def sample_list_data_agents():
        # Create a client
        client = geminidataanalytics_v1alpha.[DataAgentServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html)()
    
        # Initialize request argument(s)
        request = geminidataanalytics_v1alpha.[ListDataAgentsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.ListDataAgentsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_data_agents](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_list_data_agents)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.geminidataanalytics_v1alpha.types.ListDataAgentsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.ListDataAgentsRequest), dict]`   
The request object. Message for requesting list of DataAgents.  
`parent` |  `str`   
Required. Parent value for ListDataAgentsRequest. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListDataAgentsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.pagers.ListDataAgentsPager)` | Message for response to listing DataAgents. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_locations
    
    
    list_locations(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.ListLocationsRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.location.locations_pb2.ListLocationsResponse

Lists information about the supported locations for this service.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.location_pb2.ListLocationsRequest``   
The request object. Request message for `ListLocations` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.location_pb2.ListLocationsResponse`` | Response message for `ListLocations` method.  
  
### list_operations
    
    
    list_operations(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.ListOperationsRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.longrunning.operations_pb2.ListOperationsResponse

Lists operations that match the specified filter in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.operations_pb2.ListOperationsRequest``   
The request object. Request message for `ListOperations` method.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.operations_pb2.ListOperationsResponse`` | Response message for `ListOperations` method.  
  
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

### parse_crypto_key_path
    
    
    parse_crypto_key_path(path: str) -> typing.Dict[str, str]

Parses a crypto_key path into its component segments.

### parse_data_agent_path
    
    
    parse_data_agent_path(path: str) -> typing.Dict[str, str]

Parses a data_agent path into its component segments.

### retrieve_agent_ops_observability
    
    
    retrieve_agent_ops_observability(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.RetrieveAgentOpsObservabilityRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        data_source_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.RetrieveAgentOpsObservabilityResponse
    )

Gets AgentOps observability settings and status of required services.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import geminidataanalytics_v1alpha
    
    def sample_retrieve_agent_ops_observability():
        # Create a client
        client = geminidataanalytics_v1alpha.[DataAgentServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html)()
    
        # Initialize request argument(s)
        request = geminidataanalytics_v1alpha.[RetrieveAgentOpsObservabilityRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.RetrieveAgentOpsObservabilityRequest.html)(
            parent="parent_value",
            data_source_type="data_source_type_value",
        )
    
        # Make the request
        response = client.[retrieve_agent_ops_observability](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_retrieve_agent_ops_observability)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.geminidataanalytics_v1alpha.types.RetrieveAgentOpsObservabilityRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.RetrieveAgentOpsObservabilityRequest), dict]`   
The request object. Request for RetrieveAgentOpsObservability.  
`parent` |  `str`   
Required. Parent value for RetrieveAgentOpsObservabilityRequest. Format: projects/{project}/locations/{location} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`data_source_type` |  `str`   
Required. The data source type for which to retrieve observability settings. Examples: "bigquery", "looker" This corresponds to the `data_source_type` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.geminidataanalytics_v1alpha.types.RetrieveAgentOpsObservabilityResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.RetrieveAgentOpsObservabilityResponse)` | Response for RetrieveAgentOpsObservability.  
  
### set_agent_ops_observability
    
    
    set_agent_ops_observability(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.SetAgentOpsObservabilityRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        telemetry_enabled: typing.Optional[bool] = None,
        data_source_type: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Enables/Disables required GCP services and configures AgentOps observability settings calling the Admin Settings executable node to update the AgentOps Observability feature.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import geminidataanalytics_v1alpha
    
    def sample_set_agent_ops_observability():
        # Create a client
        client = geminidataanalytics_v1alpha.[DataAgentServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html)()
    
        # Initialize request argument(s)
        request = geminidataanalytics_v1alpha.[SetAgentOpsObservabilityRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.SetAgentOpsObservabilityRequest.html)(
            parent="parent_value",
            data_source_type="data_source_type_value",
        )
    
        # Make the request
        operation = client.[set_agent_ops_observability](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_set_agent_ops_observability)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.geminidataanalytics_v1alpha.types.SetAgentOpsObservabilityRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.SetAgentOpsObservabilityRequest), dict]`   
The request object. Request for SetAgentOpsObservability.  
`parent` |  `str`   
Required. Parent value for SetAgentOpsObservabilityRequest. Format: projects/{project}/locations/{location} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`telemetry_enabled` |  `bool`   
Optional. Whether to enable or disable AgentOps observability. When update_mask is provided, this field is ignored unless specified in the mask. This corresponds to the `telemetry_enabled` field on the `request` instance; if `request` is provided, this should not be set.  
`data_source_type` |  `str`   
Required. The data source type for which to set observability settings. Examples: "bigquery", "looker" This corresponds to the `data_source_type` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [SetAgentOpsObservabilityResponse](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.SetAgentOpsObservabilityResponse) Response for SetAgentOpsObservability.  
  
### set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM policy for a DataAgent.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import geminidataanalytics_v1alpha
    import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
    
    def sample_set_iam_policy():
        # Create a client
        client = geminidataanalytics_v1alpha.[DataAgentServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html)()
    
        # Initialize request argument(s)
        request = iam_policy_pb2.SetIamPolicyRequest(
            resource="resource_value",
        )
    
        # Make the request
        response = client.[set_iam_policy](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_set_iam_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L103-L109), dict]`   
The request object. Request message for `SetIamPolicy` method.  
`resource` |  `str`   
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.iam.v1.policy_pb2.Policy` | An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A Policy is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a binding can also specify a condition, which is a logical expression that allows access to a resource only if the expression evaluates to true. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** :literal:` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ],="" "etag":="" "bwwwja0yfja=", " version":="" 3="">`\ \` **YAML example:** :literal:` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01t00:00:00.000z')="" etag:="" bwwwja0yfja="version:">`\ \` For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).  
  
### update_data_agent
    
    
    update_data_agent(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.UpdateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent
        ] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Updates the parameters of a single DataAgent.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import geminidataanalytics_v1alpha
    
    def sample_update_data_agent():
        # Create a client
        client = geminidataanalytics_v1alpha.[DataAgentServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html)()
    
        # Initialize request argument(s)
        request = geminidataanalytics_v1alpha.[UpdateDataAgentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.UpdateDataAgentRequest.html)(
        )
    
        # Make the request
        operation = client.[update_data_agent](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_update_data_agent)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.geminidataanalytics_v1alpha.types.UpdateDataAgentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.UpdateDataAgentRequest), dict]`   
The request object. Message for updating a DataAgent.  
`data_agent` |  `[google.cloud.geminidataanalytics_v1alpha.types.DataAgent](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.DataAgent)`   
Required. The resource being updated. This corresponds to the `data_agent` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Optional. Field mask is used to specify the fields to be overwritten in the DataAgent resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields with non-default values present in the request will be overwritten. If a wildcard mask is provided, all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [DataAgent](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.DataAgent) Message describing a DataAgent object.  
  
### update_data_agent_sync
    
    
    update_data_agent_sync(
        request: typing.Optional[
            typing.Union[
                google.cloud.geminidataanalytics_v1alpha.types.data_agent_service.UpdateDataAgentRequest,
                dict,
            ]
        ] = None,
        *,
        data_agent: typing.Optional[
            google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent
        ] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.geminidataanalytics_v1alpha.types.data_agent.DataAgent

Updates the parameters of a single DataAgent synchronously.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import geminidataanalytics_v1alpha
    
    def sample_update_data_agent_sync():
        # Create a client
        client = geminidataanalytics_v1alpha.[DataAgentServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html)()
    
        # Initialize request argument(s)
        request = geminidataanalytics_v1alpha.[UpdateDataAgentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.UpdateDataAgentRequest.html)(
        )
    
        # Make the request
        response = client.[update_data_agent_sync](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.services.data_agent_service.DataAgentServiceClient.html#google_cloud_geminidataanalytics_v1alpha_services_data_agent_service_DataAgentServiceClient_update_data_agent_sync)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.geminidataanalytics_v1alpha.types.UpdateDataAgentRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.UpdateDataAgentRequest), dict]`   
The request object. Message for updating a DataAgent.  
`data_agent` |  `[google.cloud.geminidataanalytics_v1alpha.types.DataAgent](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.DataAgent)`   
Required. The resource being updated. This corresponds to the `data_agent` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Optional. Field mask is used to specify the fields to be overwritten in the DataAgent resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields with non-default values present in the request will be overwritten. If a wildcard mask is provided, all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.geminidataanalytics_v1alpha.types.DataAgent](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1alpha.types.DataAgent)` | Message describing a DataAgent object.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
