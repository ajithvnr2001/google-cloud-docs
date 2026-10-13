---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient
title: Class InsightsConfigServiceClient (0.6.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:28.278296+00:00
---

# Class InsightsConfigServiceClient (0.6.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class InsightsConfigServiceClient (0.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.1 (latest)  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.10 
    
    
    InsightsConfigServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.developerconnect_v1.services.insights_config_service.transports.base.InsightsConfigServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.developerconnect_v1.services.insights_config_service.transports.base.InsightsConfigServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Creates and manages InsightsConfigs.

The InsightsConfig resource is the core configuration object to capture events from your Software Development Lifecycle. It acts as the central hub for managing how Developer Connect understands your application, its runtime environments, and the artifacts deployed within them. A user can create an InsightsConfig, list previously-requested InsightsConfigs or get InsightsConfigs by their ID to determine the status of the InsightsConfig.

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
`InsightsConfigServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### InsightsConfigServiceClient
    
    
    InsightsConfigServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.developerconnect_v1.services.insights_config_service.transports.base.InsightsConfigServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.developerconnect_v1.services.insights_config_service.transports.base.InsightsConfigServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the insights config service client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,InsightsConfigServiceTransport,Callable[..., InsightsConfigServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the InsightsConfigServiceTransport constructor. If set to None, a transport is chosen automatically.  
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

### create_insights_config
    
    
    create_insights_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.CreateInsightsConfigRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        insights_config: typing.Optional[
            google.cloud.developerconnect_v1.types.insights_config.InsightsConfig
        ] = None,
        insights_config_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new InsightsConfig in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_create_insights_config():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[InsightsConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.html)()
    
        # Initialize request argument(s)
        insights_config = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[InsightsConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.InsightsConfig.html)()
        insights_config.app_hub_application = "app_hub_application_value"
    
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[CreateInsightsConfigRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.CreateInsightsConfigRequest.html)(
            parent="parent_value",
            insights_config_id="insights_config_id_value",
            insights_config=insights_config,
        )
    
        # Make the request
        operation = client.[create_insights_config](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.html#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_create_insights_config)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.CreateInsightsConfigRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.CreateInsightsConfigRequest), dict]`   
The request object. Request for creating an InsightsConfig.  
`parent` |  `str`   
Required. Value for parent. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`insights_config` |  `[google.cloud.developerconnect_v1.types.InsightsConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.InsightsConfig)`   
Required. The resource being created. This corresponds to the `insights_config` field on the `request` instance; if `request` is provided, this should not be set.  
`insights_config_id` |  `str`   
Required. ID of the requesting InsightsConfig. This corresponds to the `insights_config_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [InsightsConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.InsightsConfig) The InsightsConfig resource is the core configuration object to capture events from your Software Development Lifecycle. It acts as the central hub for managing how Developer Connect understands your application, its runtime environments, and the artifacts deployed within them.  
  
### delete_insights_config
    
    
    delete_insights_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.DeleteInsightsConfigRequest,
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

Deletes a single Insight.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_delete_insights_config():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[InsightsConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[DeleteInsightsConfigRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeleteInsightsConfigRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = client.[delete_insights_config](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.html#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_delete_insights_config)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.DeleteInsightsConfigRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeleteInsightsConfigRequest), dict]`   
The request object. Request for deleting an InsightsConfig.  
`name` |  `str`   
Required. Value for parent. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### deployment_event_path
    
    
    deployment_event_path(
        project: str, location: str, insights_config: str, deployment_event: str
    ) -> str

Returns a fully-qualified deployment_event string.

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
`InsightsConfigServiceClient` | The constructed client.  
  
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
`InsightsConfigServiceClient` | The constructed client.  
  
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
`InsightsConfigServiceClient` | The constructed client.  
  
### get_deployment_event
    
    
    get_deployment_event(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.GetDeploymentEventRequest,
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
    ) -> google.cloud.developerconnect_v1.types.insights_config.DeploymentEvent

Gets a single Deployment Event.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_get_deployment_event():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[InsightsConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[GetDeploymentEventRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GetDeploymentEventRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_deployment_event](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.html#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_get_deployment_event)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.GetDeploymentEventRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GetDeploymentEventRequest), dict]`   
The request object. Request for getting a DeploymentEvent.  
`name` |  `str`   
Required. The name of the deployment event to retrieve. Format: projects/{project}/locations/{location}/insightsConfigs/{insights_config}/deploymentEvents/{uuid} This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.developerconnect_v1.types.DeploymentEvent](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.DeploymentEvent)` | The DeploymentEvent resource represents the deployment of the artifact within the InsightsConfig resource.  
  
### get_insights_config
    
    
    get_insights_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.GetInsightsConfigRequest,
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
    ) -> google.cloud.developerconnect_v1.types.insights_config.InsightsConfig

Gets details of a single Insight.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_get_insights_config():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[InsightsConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[GetInsightsConfigRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GetInsightsConfigRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_insights_config](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.html#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_get_insights_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.GetInsightsConfigRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.GetInsightsConfigRequest), dict]`   
The request object. Request for getting an InsightsConfig.  
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
`[google.cloud.developerconnect_v1.types.InsightsConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.InsightsConfig)` | The InsightsConfig resource is the core configuration object to capture events from your Software Development Lifecycle. It acts as the central hub for managing how Developer Connect understands your application, its runtime environments, and the artifacts deployed within them.  
  
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
  
### insights_config_path
    
    
    insights_config_path(project: str, location: str, insights_config: str) -> str

Returns a fully-qualified insights_config string.

### list_deployment_events
    
    
    list_deployment_events(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.ListDeploymentEventsRequest,
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
        google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListDeploymentEventsPager
    )

Lists Deployment Events in a given insights config.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_list_deployment_events():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[InsightsConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[ListDeploymentEventsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListDeploymentEventsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_deployment_events](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.html#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_list_deployment_events)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.ListDeploymentEventsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListDeploymentEventsRequest), dict]`   
The request object. Request for requesting list of DeploymentEvents.  
`parent` |  `str`   
Required. The parent insights config that owns this collection of deployment events. Format: projects/{project}/locations/{location}/insightsConfigs/{insights_config} This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListDeploymentEventsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListDeploymentEventsPager)` | Response to listing DeploymentEvents. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_insights_configs
    
    
    list_insights_configs(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.ListInsightsConfigsRequest,
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
        google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListInsightsConfigsPager
    )

Lists InsightsConfigs in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_list_insights_configs():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[InsightsConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.html)()
    
        # Initialize request argument(s)
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[ListInsightsConfigsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListInsightsConfigsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_insights_configs](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.html#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_list_insights_configs)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.ListInsightsConfigsRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.ListInsightsConfigsRequest), dict]`   
The request object. Request for requesting list of InsightsConfigs.  
`parent` |  `str`   
Required. Parent value for ListInsightsConfigsRequest. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListInsightsConfigsPager](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.pagers.ListInsightsConfigsPager)` | Request for response to listing InsightsConfigs. Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### parse_deployment_event_path
    
    
    parse_deployment_event_path(path: str) -> typing.Dict[str, str]

Parses a deployment_event path into its component segments.

### parse_insights_config_path
    
    
    parse_insights_config_path(path: str) -> typing.Dict[str, str]

Parses a insights_config path into its component segments.

### update_insights_config
    
    
    update_insights_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.developerconnect_v1.types.insights_config.UpdateInsightsConfigRequest,
                dict,
            ]
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
    ) -> google.api_core.operation.Operation

Updates the parameters of a single InsightsConfig.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest)
    
    def sample_update_insights_config():
        # Create a client
        client = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[InsightsConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.html)()
    
        # Initialize request argument(s)
        insights_config = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[InsightsConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.InsightsConfig.html)()
        insights_config.app_hub_application = "app_hub_application_value"
    
        request = [developerconnect_v1](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest).[UpdateInsightsConfigRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.UpdateInsightsConfigRequest.html)(
            insights_config=insights_config,
        )
    
        # Make the request
        operation = client.[update_insights_config](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.services.insights_config_service.InsightsConfigServiceClient.html#google_cloud_developerconnect_v1_services_insights_config_service_InsightsConfigServiceClient_update_insights_config)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.developerconnect_v1.types.UpdateInsightsConfigRequest](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.UpdateInsightsConfigRequest), dict]`   
The request object. Request for updating an InsightsConfig.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation.Operation` | An object representing a long-running operation. The result type for the operation will be [InsightsConfig](https://docs.cloud.google.com/python/docs/reference/google-cloud-developerconnect/latest/google.cloud.developerconnect_v1.types.InsightsConfig) The InsightsConfig resource is the core configuration object to capture events from your Software Development Lifecycle. It acts as the central hub for managing how Developer Connect understands your application, its runtime environments, and the artifacts deployed within them.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
