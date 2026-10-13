---
url: https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient
title: Class DatastreamAsyncClient (1.20.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:46:48.500919+00:00
---

# Class DatastreamAsyncClient (1.20.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DatastreamAsyncClient (1.20.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.20.0 (latest)  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.1  1.13.2  1.12.0  1.11.0  1.10.1  1.9.5  1.8.0  1.7.0  1.6.1  1.5.1  1.4.1  1.3.0  1.2.2  1.1.1  1.0.2  0.4.3  0.3.1  0.2.0  0.1.3 
    
    
    DatastreamAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.datastream_v1.services.datastream.transports.base.DatastreamTransport,
                typing.Callable[
                    [...],
                    google.cloud.datastream_v1.services.datastream.transports.base.DatastreamTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Datastream service

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
`DatastreamTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### DatastreamAsyncClient
    
    
    DatastreamAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.datastream_v1.services.datastream.transports.base.DatastreamTransport,
                typing.Callable[
                    [...],
                    google.cloud.datastream_v1.services.datastream.transports.base.DatastreamTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the datastream async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,DatastreamTransport,Callable[..., DatastreamTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the DatastreamTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### cancel_operation
    
    
    cancel_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.CancelOperationRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
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
`retry` |  `google.api_core.retry_async.AsyncRetry`   
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

### connection_profile_path
    
    
    connection_profile_path(
        project: str, location: str, connection_profile: str
    ) -> str

Returns a fully-qualified connection_profile string.

### create_connection_profile
    
    
    create_connection_profile(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.CreateConnectionProfileRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        connection_profile: typing.Optional[
            google.cloud.datastream_v1.types.datastream_resources.ConnectionProfile
        ] = None,
        connection_profile_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Use this method to create a connection profile in a project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_create_connection_profile():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        connection_profile = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[ConnectionProfile](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.ConnectionProfile.html)()
        connection_profile.oracle_profile.hostname = "hostname_value"
        connection_profile.oracle_profile.username = "username_value"
        connection_profile.oracle_profile.database_service = "database_service_value"
        connection_profile.display_name = "display_name_value"
    
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[CreateConnectionProfileRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.CreateConnectionProfileRequest.html)(
            parent="parent_value",
            connection_profile_id="connection_profile_id_value",
            connection_profile=connection_profile,
        )
    
        # Make the request
        operation = await client.[create_connection_profile](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_create_connection_profile)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.CreateConnectionProfileRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.CreateConnectionProfileRequest), dict]]`   
The request object. Request message for creating a connection profile.  
`parent` |  ``str``   
Required. The parent that owns the collection of ConnectionProfiles. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`connection_profile` |  `[ConnectionProfile](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.ConnectionProfile)`   
Required. The connection profile resource to create. This corresponds to the `connection_profile` field on the `request` instance; if `request` is provided, this should not be set.  
`connection_profile_id` |  ``str``   
Required. The connection profile identifier. This corresponds to the `connection_profile_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [ConnectionProfile](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.ConnectionProfile) A set of reusable connection configurations to be used as a source or destination for a stream.  
  
### create_private_connection
    
    
    create_private_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.CreatePrivateConnectionRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        private_connection: typing.Optional[
            google.cloud.datastream_v1.types.datastream_resources.PrivateConnection
        ] = None,
        private_connection_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Use this method to create a private connectivity configuration.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_create_private_connection():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        private_connection = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[PrivateConnection](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.PrivateConnection.html)()
        private_connection.display_name = "display_name_value"
    
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[CreatePrivateConnectionRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.CreatePrivateConnectionRequest.html)(
            parent="parent_value",
            private_connection_id="private_connection_id_value",
            private_connection=private_connection,
        )
    
        # Make the request
        operation = await client.[create_private_connection](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_create_private_connection)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.CreatePrivateConnectionRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.CreatePrivateConnectionRequest), dict]]`   
The request object. Request for creating a private connection.  
`parent` |  ``str``   
Required. The parent that owns the collection of PrivateConnections. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`private_connection` |  `[PrivateConnection](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.PrivateConnection)`   
Required. The Private Connectivity resource to create. This corresponds to the `private_connection` field on the `request` instance; if `request` is provided, this should not be set.  
`private_connection_id` |  ``str``   
Required. The private connectivity identifier. This corresponds to the `private_connection_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [PrivateConnection](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.PrivateConnection) The PrivateConnection resource is used to establish private connectivity between Datastream and a customer's network.  
  
### create_route
    
    
    create_route(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.CreateRouteRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        route: typing.Optional[
            google.cloud.datastream_v1.types.datastream_resources.Route
        ] = None,
        route_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Use this method to create a route for a private connectivity configuration in a project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_create_route():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        route = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[Route](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.Route.html)()
        route.display_name = "display_name_value"
        route.destination_address = "destination_address_value"
    
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[CreateRouteRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.CreateRouteRequest.html)(
            parent="parent_value",
            route_id="route_id_value",
            route=route,
        )
    
        # Make the request
        operation = await client.[create_route](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_create_route)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.CreateRouteRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.CreateRouteRequest), dict]]`   
The request object. Route creation request.  
`parent` |  ``str``   
Required. The parent that owns the collection of Routes. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`route` |  `[Route](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.Route)`   
Required. The Route resource to create. This corresponds to the `route` field on the `request` instance; if `request` is provided, this should not be set.  
`route_id` |  ``str``   
Required. The Route identifier. This corresponds to the `route_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Route](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.Route) The route resource is the child of the private connection resource, used for defining a route for a private connection.  
  
### create_stream
    
    
    create_stream(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.CreateStreamRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        stream: typing.Optional[
            google.cloud.datastream_v1.types.datastream_resources.Stream
        ] = None,
        stream_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Use this method to create a stream.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_create_stream():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        stream = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[Stream](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.Stream.html)()
        stream.display_name = "display_name_value"
        stream.source_config.source_connection_profile = "source_connection_profile_value"
        stream.destination_config.destination_connection_profile = "destination_connection_profile_value"
    
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[CreateStreamRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.CreateStreamRequest.html)(
            parent="parent_value",
            stream_id="stream_id_value",
            stream=stream,
        )
    
        # Make the request
        operation = await client.[create_stream](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_create_stream)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.CreateStreamRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.CreateStreamRequest), dict]]`   
The request object. Request message for creating a stream.  
`parent` |  ``str``   
Required. The parent that owns the collection of streams. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`stream` |  `[Stream](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.Stream)`   
Required. The stream resource to create. This corresponds to the `stream` field on the `request` instance; if `request` is provided, this should not be set.  
`stream_id` |  ``str``   
Required. The stream identifier. This corresponds to the `stream_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Stream](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.Stream) A resource representing streaming data from a source to a destination.  
  
### delete_connection_profile
    
    
    delete_connection_profile(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.DeleteConnectionProfileRequest,
                dict,
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

Use this method to delete a connection profile.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_delete_connection_profile():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DeleteConnectionProfileRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.DeleteConnectionProfileRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_connection_profile](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_delete_connection_profile)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.DeleteConnectionProfileRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.DeleteConnectionProfileRequest), dict]]`   
The request object. Request message for deleting a connection profile.  
`name` |  ``str``   
Required. The name of the connection profile resource to delete. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_operation
    
    
    delete_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.DeleteOperationRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
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
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
  
### delete_private_connection
    
    
    delete_private_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.DeletePrivateConnectionRequest,
                dict,
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

Use this method to delete a private connectivity configuration.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_delete_private_connection():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DeletePrivateConnectionRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.DeletePrivateConnectionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_private_connection](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_delete_private_connection)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.DeletePrivateConnectionRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.DeletePrivateConnectionRequest), dict]]`   
The request object. Request to delete a private connection.  
`name` |  ``str``   
Required. The name of the private connectivity configuration to delete. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_route
    
    
    delete_route(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.DeleteRouteRequest, dict
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

Use this method to delete a route.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_delete_route():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DeleteRouteRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.DeleteRouteRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_route](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_delete_route)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.DeleteRouteRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.DeleteRouteRequest), dict]]`   
The request object. Route deletion request.  
`name` |  ``str``   
Required. The name of the Route resource to delete. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### delete_stream
    
    
    delete_stream(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.DeleteStreamRequest, dict
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

Use this method to delete a stream.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_delete_stream():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DeleteStreamRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.DeleteStreamRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_stream](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_delete_stream)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.DeleteStreamRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.DeleteStreamRequest), dict]]`   
The request object. Request message for deleting a stream.  
`name` |  ``str``   
Required. The name of the stream resource to delete. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### discover_connection_profile
    
    
    discover_connection_profile(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.DiscoverConnectionProfileRequest,
                dict,
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.datastream_v1.types.datastream.DiscoverConnectionProfileResponse

Use this method to discover a connection profile. The discover API call exposes the data objects and metadata belonging to the profile. Typically, a request returns children data objects of a parent data object that's optionally supplied in the request.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_discover_connection_profile():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        connection_profile = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[ConnectionProfile](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.ConnectionProfile.html)()
        connection_profile.oracle_profile.hostname = "hostname_value"
        connection_profile.oracle_profile.username = "username_value"
        connection_profile.oracle_profile.database_service = "database_service_value"
        connection_profile.display_name = "display_name_value"
    
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DiscoverConnectionProfileRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.DiscoverConnectionProfileRequest.html)(
            connection_profile=connection_profile,
            full_hierarchy=True,
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[discover_connection_profile](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_discover_connection_profile)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.DiscoverConnectionProfileRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.DiscoverConnectionProfileRequest), dict]]`   
The request object. Request message for 'discover' ConnectionProfile request.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datastream_v1.types.DiscoverConnectionProfileResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.DiscoverConnectionProfileResponse)` | Response from a discover request.  
  
### fetch_static_ips
    
    
    fetch_static_ips(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.FetchStaticIpsRequest, dict
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
    ) -> google.cloud.datastream_v1.services.datastream.pagers.FetchStaticIpsAsyncPager

The FetchStaticIps API call exposes the static IP addresses used by Datastream.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_fetch_static_ips():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[FetchStaticIpsRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.FetchStaticIpsRequest.html)(
            name="name_value",
        )
    
        # Make the request
        page_result = client.[fetch_static_ips](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_fetch_static_ips)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.FetchStaticIpsRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.FetchStaticIpsRequest), dict]]`   
The request object. Request message for 'FetchStaticIps' request.  
`name` |  ``str``   
Required. The resource name for the location for which static IPs should be returned. Must be in the format `projects/_/locations/_`. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datastream_v1.services.datastream.pagers.FetchStaticIpsAsyncPager](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.pagers.FetchStaticIpsAsyncPager)` | Response message for a 'FetchStaticIps' response. Iterating over this object will yield results and resolve additional pages automatically.  
  
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
`DatastreamAsyncClient` | The constructed client.  
  
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
`DatastreamAsyncClient` | The constructed client.  
  
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
`DatastreamAsyncClient` | The constructed client.  
  
### get_connection_profile
    
    
    get_connection_profile(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.GetConnectionProfileRequest,
                dict,
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
    ) -> google.cloud.datastream_v1.types.datastream_resources.ConnectionProfile

Use this method to get details about a connection profile.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_get_connection_profile():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[GetConnectionProfileRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.GetConnectionProfileRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_connection_profile](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_get_connection_profile)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.GetConnectionProfileRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.GetConnectionProfileRequest), dict]]`   
The request object. Request message for getting a connection profile.  
`name` |  ``str``   
Required. The name of the connection profile resource to get. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datastream_v1.types.ConnectionProfile](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.ConnectionProfile)` | A set of reusable connection configurations to be used as a source or destination for a stream.  
  
### get_location
    
    
    get_location(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.GetLocationRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
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
`retry` |  `google.api_core.retry_async.AsyncRetry`   
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
  
### get_operation
    
    
    get_operation(
        request: typing.Optional[
            typing.Union[google.longrunning.operations_pb2.GetOperationRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
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
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.operations_pb2.Operation`` | An `Operation` object.  
  
### get_private_connection
    
    
    get_private_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.GetPrivateConnectionRequest,
                dict,
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
    ) -> google.cloud.datastream_v1.types.datastream_resources.PrivateConnection

Use this method to get details about a private connectivity configuration.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_get_private_connection():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[GetPrivateConnectionRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.GetPrivateConnectionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_private_connection](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_get_private_connection)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.GetPrivateConnectionRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.GetPrivateConnectionRequest), dict]]`   
The request object. Request to get a private connection configuration.  
`name` |  ``str``   
Required. The name of the private connectivity configuration to get. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datastream_v1.types.PrivateConnection](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.PrivateConnection)` | The PrivateConnection resource is used to establish private connectivity between Datastream and a customer's network.  
  
### get_route
    
    
    get_route(
        request: typing.Optional[
            typing.Union[google.cloud.datastream_v1.types.datastream.GetRouteRequest, dict]
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
    ) -> google.cloud.datastream_v1.types.datastream_resources.Route

Use this method to get details about a route.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_get_route():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[GetRouteRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.GetRouteRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_route](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_get_route)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.GetRouteRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.GetRouteRequest), dict]]`   
The request object. Route get request.  
`name` |  ``str``   
Required. The name of the Route resource to get. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datastream_v1.types.Route](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.Route)` | The route resource is the child of the private connection resource, used for defining a route for a private connection.  
  
### get_stream
    
    
    get_stream(
        request: typing.Optional[
            typing.Union[google.cloud.datastream_v1.types.datastream.GetStreamRequest, dict]
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
    ) -> google.cloud.datastream_v1.types.datastream_resources.Stream

Use this method to get details about a stream.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_get_stream():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[GetStreamRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.GetStreamRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_stream](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_get_stream)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.GetStreamRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.GetStreamRequest), dict]]`   
The request object. Request message for getting a stream.  
`name` |  ``str``   
Required. The name of the stream resource to get. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datastream_v1.types.Stream](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.Stream)` | A resource representing streaming data from a source to a destination.  
  
### get_stream_object
    
    
    get_stream_object(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.GetStreamObjectRequest, dict
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
    ) -> google.cloud.datastream_v1.types.datastream_resources.StreamObject

Use this method to get details about a stream object.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_get_stream_object():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[GetStreamObjectRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.GetStreamObjectRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_stream_object](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_get_stream_object)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.GetStreamObjectRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.GetStreamObjectRequest), dict]]`   
The request object. Request for fetching a specific stream object.  
`name` |  ``str``   
Required. The name of the stream object resource to get. This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datastream_v1.types.StreamObject](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.StreamObject)` | A specific stream object (e.g a specific DB table).  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.datastream_v1.services.datastream.transports.base.DatastreamTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### list_connection_profiles
    
    
    list_connection_profiles(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.ListConnectionProfilesRequest,
                dict,
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
    ) -> (
        google.cloud.datastream_v1.services.datastream.pagers.ListConnectionProfilesAsyncPager
    )

Use this method to list connection profiles created in a project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_list_connection_profiles():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[ListConnectionProfilesRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.ListConnectionProfilesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_connection_profiles](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_list_connection_profiles)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.ListConnectionProfilesRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.ListConnectionProfilesRequest), dict]]`   
The request object. Request message for listing connection profiles.  
`parent` |  ``str``   
Required. The parent that owns the collection of connection profiles. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datastream_v1.services.datastream.pagers.ListConnectionProfilesAsyncPager](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.pagers.ListConnectionProfilesAsyncPager)` | Response message for listing connection profiles. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_locations
    
    
    list_locations(
        request: typing.Optional[
            typing.Union[google.cloud.location.locations_pb2.ListLocationsRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
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
`retry` |  `google.api_core.retry_async.AsyncRetry`   
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
                google.api_core.retry.retry_unary_async.AsyncRetry,
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
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.operations_pb2.ListOperationsResponse`` | Response message for `ListOperations` method.  
  
### list_private_connections
    
    
    list_private_connections(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.ListPrivateConnectionsRequest,
                dict,
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
    ) -> (
        google.cloud.datastream_v1.services.datastream.pagers.ListPrivateConnectionsAsyncPager
    )

Use this method to list private connectivity configurations in a project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_list_private_connections():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[ListPrivateConnectionsRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.ListPrivateConnectionsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_private_connections](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_list_private_connections)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.ListPrivateConnectionsRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.ListPrivateConnectionsRequest), dict]]`   
The request object. Request for listing private connections.  
`parent` |  ``str``   
Required. The parent that owns the collection of private connectivity configurations. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datastream_v1.services.datastream.pagers.ListPrivateConnectionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.pagers.ListPrivateConnectionsAsyncPager)` | Response containing a list of private connection configurations. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_routes
    
    
    list_routes(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.ListRoutesRequest, dict
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
    ) -> google.cloud.datastream_v1.services.datastream.pagers.ListRoutesAsyncPager

Use this method to list routes created for a private connectivity configuration in a project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_list_routes():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[ListRoutesRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.ListRoutesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_routes](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_list_routes)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.ListRoutesRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.ListRoutesRequest), dict]]`   
The request object. Route list request.  
`parent` |  ``str``   
Required. The parent that owns the collection of Routess. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datastream_v1.services.datastream.pagers.ListRoutesAsyncPager](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.pagers.ListRoutesAsyncPager)` | Route list response. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_stream_objects
    
    
    list_stream_objects(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.ListStreamObjectsRequest, dict
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
    ) -> google.cloud.datastream_v1.services.datastream.pagers.ListStreamObjectsAsyncPager

Use this method to list the objects of a specific stream.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_list_stream_objects():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[ListStreamObjectsRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.ListStreamObjectsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_stream_objects](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_list_stream_objects)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.ListStreamObjectsRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.ListStreamObjectsRequest), dict]]`   
The request object. Request for listing all objects for a specific stream.  
`parent` |  ``str``   
Required. The parent stream that owns the collection of objects. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datastream_v1.services.datastream.pagers.ListStreamObjectsAsyncPager](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.pagers.ListStreamObjectsAsyncPager)` | Response containing the objects for a stream. Iterating over this object will yield results and resolve additional pages automatically.  
  
### list_streams
    
    
    list_streams(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.ListStreamsRequest, dict
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
    ) -> google.cloud.datastream_v1.services.datastream.pagers.ListStreamsAsyncPager

Use this method to list streams in a project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_list_streams():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[ListStreamsRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.ListStreamsRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_streams](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_list_streams)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.ListStreamsRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.ListStreamsRequest), dict]]`   
The request object. Request message for listing streams.  
`parent` |  ``str``   
Required. The parent that owns the collection of streams. This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datastream_v1.services.datastream.pagers.ListStreamsAsyncPager](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.pagers.ListStreamsAsyncPager)` | Response message for listing streams. Iterating over this object will yield results and resolve additional pages automatically.  
  
### lookup_stream_object
    
    
    lookup_stream_object(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.LookupStreamObjectRequest, dict
            ]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.datastream_v1.types.datastream_resources.StreamObject

Use this method to look up a stream object by its source object identifier.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_lookup_stream_object():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        source_object_identifier = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[SourceObjectIdentifier](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.SourceObjectIdentifier.html)()
        source_object_identifier.oracle_identifier.schema = "schema_value"
        source_object_identifier.oracle_identifier.table = "table_value"
    
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[LookupStreamObjectRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.LookupStreamObjectRequest.html)(
            parent="parent_value",
            source_object_identifier=source_object_identifier,
        )
    
        # Make the request
        response = await client.[lookup_stream_object](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_lookup_stream_object)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.LookupStreamObjectRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.LookupStreamObjectRequest), dict]]`   
The request object. Request for looking up a specific stream object by its source object identifier.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datastream_v1.types.StreamObject](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.StreamObject)` | A specific stream object (e.g a specific DB table).  
  
### network_attachment_path
    
    
    network_attachment_path(project: str, region: str, network_attachment: str) -> str

Returns a fully-qualified network_attachment string.

### networks_path
    
    
    networks_path(project: str, network: str) -> str

Returns a fully-qualified networks string.

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

### parse_connection_profile_path
    
    
    parse_connection_profile_path(path: str) -> typing.Dict[str, str]

Parses a connection_profile path into its component segments.

### parse_network_attachment_path
    
    
    parse_network_attachment_path(path: str) -> typing.Dict[str, str]

Parses a network_attachment path into its component segments.

### parse_networks_path
    
    
    parse_networks_path(path: str) -> typing.Dict[str, str]

Parses a networks path into its component segments.

### parse_private_connection_path
    
    
    parse_private_connection_path(path: str) -> typing.Dict[str, str]

Parses a private_connection path into its component segments.

### parse_route_path
    
    
    parse_route_path(path: str) -> typing.Dict[str, str]

Parses a route path into its component segments.

### parse_stream_object_path
    
    
    parse_stream_object_path(path: str) -> typing.Dict[str, str]

Parses a stream_object path into its component segments.

### parse_stream_path
    
    
    parse_stream_path(path: str) -> typing.Dict[str, str]

Parses a stream path into its component segments.

### private_connection_path
    
    
    private_connection_path(
        project: str, location: str, private_connection: str
    ) -> str

Returns a fully-qualified private_connection string.

### route_path
    
    
    route_path(project: str, location: str, private_connection: str, route: str) -> str

Returns a fully-qualified route string.

### run_stream
    
    
    run_stream(
        request: typing.Optional[
            typing.Union[google.cloud.datastream_v1.types.datastream.RunStreamRequest, dict]
        ] = None,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Use this method to start, resume or recover a stream with a non default CDC strategy.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_run_stream():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[RunStreamRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.RunStreamRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[run_stream](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_run_stream)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.RunStreamRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.RunStreamRequest), dict]]`   
The request object. Request message for running a stream.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Stream](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.Stream) A resource representing streaming data from a source to a destination.  
  
### start_backfill_job
    
    
    start_backfill_job(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.StartBackfillJobRequest, dict
            ]
        ] = None,
        *,
        object_: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.datastream_v1.types.datastream.StartBackfillJobResponse

Use this method to start a backfill job for the specified stream object.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_start_backfill_job():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[StartBackfillJobRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.StartBackfillJobRequest.html)(
            object_="object__value",
        )
    
        # Make the request
        response = await client.[start_backfill_job](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_start_backfill_job)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.StartBackfillJobRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.StartBackfillJobRequest), dict]]`   
The request object. Request for manually initiating a backfill job for a specific stream object.  
`object_` |  ``str``   
Required. The name of the stream object resource to start a backfill job for. This corresponds to the `object_` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datastream_v1.types.StartBackfillJobResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.StartBackfillJobResponse)` | Response for manually initiating a backfill job for a specific stream object.  
  
### stop_backfill_job
    
    
    stop_backfill_job(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.StopBackfillJobRequest, dict
            ]
        ] = None,
        *,
        object_: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.datastream_v1.types.datastream.StopBackfillJobResponse

Use this method to stop a backfill job for the specified stream object.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_stop_backfill_job():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[StopBackfillJobRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.StopBackfillJobRequest.html)(
            object_="object__value",
        )
    
        # Make the request
        response = await client.[stop_backfill_job](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_stop_backfill_job)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.StopBackfillJobRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.StopBackfillJobRequest), dict]]`   
The request object. Request for manually stopping a running backfill job for a specific stream object.  
`object_` |  ``str``   
Required. The name of the stream object resource to stop the backfill job for. This corresponds to the `object_` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.datastream_v1.types.StopBackfillJobResponse](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.StopBackfillJobResponse)` | Response for manually stop a backfill job for a specific stream object.  
  
### stream_object_path
    
    
    stream_object_path(project: str, location: str, stream: str, object: str) -> str

Returns a fully-qualified stream_object string.

### stream_path
    
    
    stream_path(project: str, location: str, stream: str) -> str

Returns a fully-qualified stream string.

### update_connection_profile
    
    
    update_connection_profile(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.UpdateConnectionProfileRequest,
                dict,
            ]
        ] = None,
        *,
        connection_profile: typing.Optional[
            google.cloud.datastream_v1.types.datastream_resources.ConnectionProfile
        ] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Use this method to update the parameters of a connection profile.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_update_connection_profile():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        connection_profile = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[ConnectionProfile](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.ConnectionProfile.html)()
        connection_profile.oracle_profile.hostname = "hostname_value"
        connection_profile.oracle_profile.username = "username_value"
        connection_profile.oracle_profile.database_service = "database_service_value"
        connection_profile.display_name = "display_name_value"
    
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[UpdateConnectionProfileRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.UpdateConnectionProfileRequest.html)(
            connection_profile=connection_profile,
        )
    
        # Make the request
        operation = await client.[update_connection_profile](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_update_connection_profile)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.UpdateConnectionProfileRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.UpdateConnectionProfileRequest), dict]]`   
The request object. Connection profile update message.  
`connection_profile` |  `[ConnectionProfile](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.ConnectionProfile)`   
Required. The connection profile to update. This corresponds to the `connection_profile` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Optional. Field mask is used to specify the fields to be overwritten in the ConnectionProfile resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [ConnectionProfile](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.ConnectionProfile) A set of reusable connection configurations to be used as a source or destination for a stream.  
  
### update_stream
    
    
    update_stream(
        request: typing.Optional[
            typing.Union[
                google.cloud.datastream_v1.types.datastream.UpdateStreamRequest, dict
            ]
        ] = None,
        *,
        stream: typing.Optional[
            google.cloud.datastream_v1.types.datastream_resources.Stream
        ] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Use this method to update the configuration of a stream.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest)
    
    async def sample_update_stream():
        # Create a client
        client = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[DatastreamAsyncClient](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html)()
    
        # Initialize request argument(s)
        stream = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[Stream](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.Stream.html)()
        stream.display_name = "display_name_value"
        stream.source_config.source_connection_profile = "source_connection_profile_value"
        stream.destination_config.destination_connection_profile = "destination_connection_profile_value"
    
        request = [datastream_v1](https://docs.cloud.google.com/python/docs/reference/datastream/latest).[UpdateStreamRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.UpdateStreamRequest.html)(
            stream=stream,
        )
    
        # Make the request
        operation = await client.[update_stream](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.services.datastream.DatastreamAsyncClient.html#google_cloud_datastream_v1_services_datastream_DatastreamAsyncClient_update_stream)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.datastream_v1.types.UpdateStreamRequest](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.UpdateStreamRequest), dict]]`   
The request object. Request message for updating a stream.  
`stream` |  `[Stream](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.Stream)`   
Required. The stream resource to update. This corresponds to the `stream` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Optional. Field mask is used to specify the fields to be overwritten in the stream resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Stream](https://docs.cloud.google.com/python/docs/reference/datastream/latest/google.cloud.datastream_v1.types.Stream) A resource representing streaming data from a source to a destination.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
