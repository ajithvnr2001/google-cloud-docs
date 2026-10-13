---
url: https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.serving_config_service.ServingConfigServiceClient
title: Class ServingConfigServiceClient (2.14.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:53:07.591782+00:00
---

# Class ServingConfigServiceClient (2.14.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.serving_config_service.ServingConfigServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ServingConfigServiceClient (2.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.14.0 (latest)  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.2  1.20.1  1.19.1  1.18.0  1.17.0  1.16.3  1.15.1  1.14.1  1.13.0  1.12.0  1.11.0  1.10.2  1.9.0  1.8.1  1.7.0  1.6.1  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.2  0.4.2  0.3.1  0.2.0  0.1.0 
    
    
    ServingConfigServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.retail_v2.services.serving_config_service.transports.base.ServingConfigServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.retail_v2.services.serving_config_service.transports.base.ServingConfigServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Service for modifying ServingConfig.

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
`ServingConfigServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### ServingConfigServiceClient
    
    
    ServingConfigServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.retail_v2.services.serving_config_service.transports.base.ServingConfigServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.retail_v2.services.serving_config_service.transports.base.ServingConfigServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the serving config service client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,ServingConfigServiceTransport,Callable[..., ServingConfigServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport. If a Callable is given, it will be called with the same set of initialization arguments as used in the ServingConfigServiceTransport constructor. If set to None, a transport is chosen automatically.  
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

### add_control
    
    
    add_control(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2.types.serving_config_service.AddControlRequest, dict
            ]
        ] = None,
        *,
        serving_config: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.retail_v2.types.serving_config.ServingConfig

Enables a Control on the specified ServingConfig. The control is added in the last position of the list of controls it belongs to (e.g. if it's a facet spec control it will be applied in the last position of servingConfig.facetSpecIds) Returns a ALREADY_EXISTS error if the control has already been applied. Returns a FAILED_PRECONDITION error if the addition could exceed maximum number of control allowed for that type of control.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2
    
    def sample_add_control():
        # Create a client
        client = retail_v2.[ServingConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.serving_config_service.ServingConfigServiceClient.html)()
    
        # Initialize request argument(s)
        request = retail_v2.[AddControlRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.AddControlRequest.html)(
            serving_config="serving_config_value",
            control_id="control_id_value",
        )
    
        # Make the request
        response = client.[add_control](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.serving_config_service.ServingConfigServiceClient.html#google_cloud_retail_v2_services_serving_config_service_ServingConfigServiceClient_add_control)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.retail_v2.types.AddControlRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.AddControlRequest), dict]`   
The request object. Request for AddControl method.  
`serving_config` |  `str`   
Required. The source ServingConfig resource name . Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/servingConfigs/{serving_config_id}` This corresponds to the `serving_config` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2.types.ServingConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.ServingConfig)` | Configures metadata that is used to generate serving time results (e.g. search results or recommendation predictions).  
  
### catalog_path
    
    
    catalog_path(project: str, location: str, catalog: str) -> str

Returns a fully-qualified catalog string.

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

### create_serving_config
    
    
    create_serving_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2.types.serving_config_service.CreateServingConfigRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        serving_config: typing.Optional[
            google.cloud.retail_v2.types.serving_config.ServingConfig
        ] = None,
        serving_config_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.retail_v2.types.serving_config.ServingConfig

Creates a ServingConfig.

A maximum of 100 xref_ServingConfigs are allowed in a xref_Catalog, otherwise a FAILED_PRECONDITION error is returned.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2
    
    def sample_create_serving_config():
        # Create a client
        client = retail_v2.[ServingConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.serving_config_service.ServingConfigServiceClient.html)()
    
        # Initialize request argument(s)
        serving_config = retail_v2.[ServingConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.ServingConfig.html)()
        serving_config.display_name = "display_name_value"
        serving_config.solution_types = ['SOLUTION_TYPE_SEARCH']
    
        request = retail_v2.[CreateServingConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.CreateServingConfigRequest.html)(
            parent="parent_value",
            serving_config=serving_config,
            serving_config_id="serving_config_id_value",
        )
    
        # Make the request
        response = client.[create_serving_config](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.serving_config_service.ServingConfigServiceClient.html#google_cloud_retail_v2_services_serving_config_service_ServingConfigServiceClient_create_serving_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.retail_v2.types.CreateServingConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.CreateServingConfigRequest), dict]`   
The request object. Request for CreateServingConfig method.  
`parent` |  `str`   
Required. Full resource name of parent. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`serving_config` |  `[google.cloud.retail_v2.types.ServingConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.ServingConfig)`   
Required. The ServingConfig to create. This corresponds to the `serving_config` field on the `request` instance; if `request` is provided, this should not be set.  
`serving_config_id` |  `str`   
Required. The ID to use for the ServingConfig, which will become the final component of the ServingConfig's resource name. This value should be 4-63 characters, and valid characters are /`a-z][0-9]`-_/. This corresponds to the `serving_config_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2.types.ServingConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.ServingConfig)` | Configures metadata that is used to generate serving time results (e.g. search results or recommendation predictions).  
  
### delete_serving_config
    
    
    delete_serving_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2.types.serving_config_service.DeleteServingConfigRequest,
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

Deletes a ServingConfig.

Returns a NotFound error if the ServingConfig does not exist.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2
    
    def sample_delete_serving_config():
        # Create a client
        client = retail_v2.[ServingConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.serving_config_service.ServingConfigServiceClient.html)()
    
        # Initialize request argument(s)
        request = retail_v2.[DeleteServingConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.DeleteServingConfigRequest.html)(
            name="name_value",
        )
    
        # Make the request
        client.[delete_serving_config](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.serving_config_service.ServingConfigServiceClient.html#google_cloud_retail_v2_services_serving_config_service_ServingConfigServiceClient_delete_serving_config)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.retail_v2.types.DeleteServingConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.DeleteServingConfigRequest), dict]`   
The request object. Request for DeleteServingConfig method.  
`name` |  `str`   
Required. The resource name of the ServingConfig to delete. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/servingConfigs/{serving_config_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
`ServingConfigServiceClient` | The constructed client.  
  
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
`ServingConfigServiceClient` | The constructed client.  
  
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
`ServingConfigServiceClient` | The constructed client.  
  
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
  
### get_serving_config
    
    
    get_serving_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2.types.serving_config_service.GetServingConfigRequest,
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
    ) -> google.cloud.retail_v2.types.serving_config.ServingConfig

Gets a ServingConfig.

Returns a NotFound error if the ServingConfig does not exist.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2
    
    def sample_get_serving_config():
        # Create a client
        client = retail_v2.[ServingConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.serving_config_service.ServingConfigServiceClient.html)()
    
        # Initialize request argument(s)
        request = retail_v2.[GetServingConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.GetServingConfigRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = client.[get_serving_config](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.serving_config_service.ServingConfigServiceClient.html#google_cloud_retail_v2_services_serving_config_service_ServingConfigServiceClient_get_serving_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.retail_v2.types.GetServingConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.GetServingConfigRequest), dict]`   
The request object. Request for GetServingConfig method.  
`name` |  `str`   
Required. The resource name of the ServingConfig to get. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/servingConfigs/{serving_config_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2.types.ServingConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.ServingConfig)` | Configures metadata that is used to generate serving time results (e.g. search results or recommendation predictions).  
  
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
  
### list_serving_configs
    
    
    list_serving_configs(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2.types.serving_config_service.ListServingConfigsRequest,
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
        google.cloud.retail_v2.services.serving_config_service.pagers.ListServingConfigsPager
    )

Lists all ServingConfigs linked to this catalog.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2
    
    def sample_list_serving_configs():
        # Create a client
        client = retail_v2.[ServingConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.serving_config_service.ServingConfigServiceClient.html)()
    
        # Initialize request argument(s)
        request = retail_v2.[ListServingConfigsRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.ListServingConfigsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_serving_configs](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.serving_config_service.ServingConfigServiceClient.html#google_cloud_retail_v2_services_serving_config_service_ServingConfigServiceClient_list_serving_configs)(request=request)
    
        # Handle the response
        for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.retail_v2.types.ListServingConfigsRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.ListServingConfigsRequest), dict]`   
The request object. Request for ListServingConfigs method.  
`parent` |  `str`   
Required. The catalog resource name. Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2.services.serving_config_service.pagers.ListServingConfigsPager](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.serving_config_service.pagers.ListServingConfigsPager)` | Response for ListServingConfigs method. Iterating over this object will yield results and resolve additional pages automatically.  
  
### parse_catalog_path
    
    
    parse_catalog_path(path: str) -> typing.Dict[str, str]

Parses a catalog path into its component segments.

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

### parse_serving_config_path
    
    
    parse_serving_config_path(path: str) -> typing.Dict[str, str]

Parses a serving_config path into its component segments.

### remove_control
    
    
    remove_control(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2.types.serving_config_service.RemoveControlRequest,
                dict,
            ]
        ] = None,
        *,
        serving_config: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.retail_v2.types.serving_config.ServingConfig

Disables a Control on the specified ServingConfig. The control is removed from the ServingConfig. Returns a NOT_FOUND error if the Control is not enabled for the ServingConfig.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2
    
    def sample_remove_control():
        # Create a client
        client = retail_v2.[ServingConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.serving_config_service.ServingConfigServiceClient.html)()
    
        # Initialize request argument(s)
        request = retail_v2.[RemoveControlRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.RemoveControlRequest.html)(
            serving_config="serving_config_value",
            control_id="control_id_value",
        )
    
        # Make the request
        response = client.[remove_control](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.serving_config_service.ServingConfigServiceClient.html#google_cloud_retail_v2_services_serving_config_service_ServingConfigServiceClient_remove_control)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.retail_v2.types.RemoveControlRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.RemoveControlRequest), dict]`   
The request object. Request for RemoveControl method.  
`serving_config` |  `str`   
Required. The source ServingConfig resource name . Format: `projects/{project_number}/locations/{location_id}/catalogs/{catalog_id}/servingConfigs/{serving_config_id}` This corresponds to the `serving_config` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2.types.ServingConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.ServingConfig)` | Configures metadata that is used to generate serving time results (e.g. search results or recommendation predictions).  
  
### serving_config_path
    
    
    serving_config_path(
        project: str, location: str, catalog: str, serving_config: str
    ) -> str

Returns a fully-qualified serving_config string.

### update_serving_config
    
    
    update_serving_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.retail_v2.types.serving_config_service.UpdateServingConfigRequest,
                dict,
            ]
        ] = None,
        *,
        serving_config: typing.Optional[
            google.cloud.retail_v2.types.serving_config.ServingConfig
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
    ) -> google.cloud.retail_v2.types.serving_config.ServingConfig

Updates a ServingConfig.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import retail_v2
    
    def sample_update_serving_config():
        # Create a client
        client = retail_v2.[ServingConfigServiceClient](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.serving_config_service.ServingConfigServiceClient.html)()
    
        # Initialize request argument(s)
        serving_config = retail_v2.[ServingConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.ServingConfig.html)()
        serving_config.display_name = "display_name_value"
        serving_config.solution_types = ['SOLUTION_TYPE_SEARCH']
    
        request = retail_v2.[UpdateServingConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.UpdateServingConfigRequest.html)(
            serving_config=serving_config,
        )
    
        # Make the request
        response = client.[update_serving_config](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.services.serving_config_service.ServingConfigServiceClient.html#google_cloud_retail_v2_services_serving_config_service_ServingConfigServiceClient_update_serving_config)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Union[[google.cloud.retail_v2.types.UpdateServingConfigRequest](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.UpdateServingConfigRequest), dict]`   
The request object. Request for UpdateServingConfig method.  
`serving_config` |  `[google.cloud.retail_v2.types.ServingConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.ServingConfig)`   
Required. The ServingConfig to update. This corresponds to the `serving_config` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  `google.protobuf.field_mask_pb2.FieldMask`   
Indicates which fields in the provided ServingConfig to update. The following are NOT supported: - ServingConfig.name If not set, all supported fields are updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry.Retry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.retail_v2.types.ServingConfig](https://docs.cloud.google.com/python/docs/reference/retail/latest/google.cloud.retail_v2.types.ServingConfig)` | Configures metadata that is used to generate serving time results (e.g. search results or recommendation predictions).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
