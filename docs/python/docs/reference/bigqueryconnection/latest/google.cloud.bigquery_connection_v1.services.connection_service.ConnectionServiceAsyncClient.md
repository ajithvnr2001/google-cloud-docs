---
url: https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceAsyncClient
title: Class ConnectionServiceAsyncClient (1.23.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:13.793125+00:00
---

# Class ConnectionServiceAsyncClient (1.23.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ConnectionServiceAsyncClient (1.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.23.0 (latest)  1.22.0  1.21.0  1.20.0  1.19.0  1.18.3  1.17.0  1.16.1  1.15.5  1.14.0  1.13.2  1.12.1  1.11.0  1.10.0  1.9.1  1.8.0  1.7.3  1.6.0  1.5.1  1.4.0  1.3.4  1.2.3  1.1.1  1.0.1  0.3.2  0.2.0  0.1.0 
    
    
    ConnectionServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.bigquery_connection_v1.services.connection_service.transports.base.ConnectionServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.bigquery_connection_v1.services.connection_service.transports.base.ConnectionServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Manages external data source connections and credentials.

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
`ConnectionServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### ConnectionServiceAsyncClient
    
    
    ConnectionServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.bigquery_connection_v1.services.connection_service.transports.base.ConnectionServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.bigquery_connection_v1.services.connection_service.transports.base.ConnectionServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the connection service async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,ConnectionServiceTransport,Callable[..., ConnectionServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the ConnectionServiceTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
### cluster_path
    
    
    cluster_path(project: str, region: str, cluster: str) -> str

Returns a fully-qualified cluster string.

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

### connection_path
    
    
    connection_path(project: str, location: str, connection: str) -> str

Returns a fully-qualified connection string.

### create_connection
    
    
    create_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_connection_v1.types.connection.CreateConnectionRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        connection: typing.Optional[
            google.cloud.bigquery_connection_v1.types.connection.Connection
        ] = None,
        connection_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.bigquery_connection_v1.types.connection.Connection

Creates a new connection.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest)
    
    async def sample_create_connection():
        # Create a client
        client = [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest).[ConnectionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest).[CreateConnectionRequest](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.types.CreateConnectionRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        response = await client.[create_connection](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceAsyncClient.html#google_cloud_bigquery_connection_v1_services_connection_service_ConnectionServiceAsyncClient_create_connection)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_connection_v1.types.CreateConnectionRequest](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.types.CreateConnectionRequest), dict]]`   
The request object. The request for ConnectionService.CreateConnection.  
`parent` |  ``str``   
Required. Parent resource name. Must be in the format `projects/{project_id}/locations/{location_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`connection` |  `[Connection](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.types.Connection)`   
Required. Connection to create. This corresponds to the `connection` field on the `request` instance; if `request` is provided, this should not be set.  
`connection_id` |  ``str``   
Optional. Connection id that should be assigned to the created connection. This corresponds to the `connection_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_connection_v1.types.Connection](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.types.Connection)` | Configuration parameters to establish connection with an external data source, except the credential attributes.  
  
### delete_connection
    
    
    delete_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_connection_v1.types.connection.DeleteConnectionRequest,
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
    ) -> None

Deletes connection and associated credential.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest)
    
    async def sample_delete_connection():
        # Create a client
        client = [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest).[ConnectionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest).[DeleteConnectionRequest](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.types.DeleteConnectionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_connection](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceAsyncClient.html#google_cloud_bigquery_connection_v1_services_connection_service_ConnectionServiceAsyncClient_delete_connection)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_connection_v1.types.DeleteConnectionRequest](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.types.DeleteConnectionRequest), dict]]`   
The request object. The request for [ConnectionService.DeleteConnectionRequest][].  
`name` |  ``str``   
Required. Name of the deleted connection, for example: `projects/{project_id}/locations/{location_id}/connections/{connection_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
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
`ConnectionServiceAsyncClient` | The constructed client.  
  
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
`ConnectionServiceAsyncClient` | The constructed client.  
  
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
`ConnectionServiceAsyncClient` | The constructed client.  
  
### get_connection
    
    
    get_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_connection_v1.types.connection.GetConnectionRequest,
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
    ) -> google.cloud.bigquery_connection_v1.types.connection.Connection

Returns specified connection.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest)
    
    async def sample_get_connection():
        # Create a client
        client = [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest).[ConnectionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest).[GetConnectionRequest](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.types.GetConnectionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_connection](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceAsyncClient.html#google_cloud_bigquery_connection_v1_services_connection_service_ConnectionServiceAsyncClient_get_connection)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_connection_v1.types.GetConnectionRequest](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.types.GetConnectionRequest), dict]]`   
The request object. The request for ConnectionService.GetConnection.  
`name` |  ``str``   
Required. Name of the requested connection, for example: `projects/{project_id}/locations/{location_id}/connections/{connection_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_connection_v1.types.Connection](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.types.Connection)` | Configuration parameters to establish connection with an external data source, except the credential attributes.  
  
### get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Gets the access control policy for a resource. Returns an empty policy if the resource exists and does not have a policy set.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest)
    import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
    
    async def sample_get_iam_policy():
        # Create a client
        client = [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest).[ConnectionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_policy_pb2.GetIamPolicyRequest(
            resource="resource_value",
        )
    
        # Make the request
        response = await client.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceAsyncClient.html#google_cloud_bigquery_connection_v1_services_connection_service_ConnectionServiceAsyncClient_get_iam_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L111-L118), dict]]`   
The request object. Request message for `GetIamPolicy` method.  
`resource` |  ``str``   
REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.iam.v1.policy_pb2.Policy` | An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A Policy is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a binding can also specify a condition, which is a logical expression that allows access to a resource only if the expression evaluates to true. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** :literal:` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ],="" "etag":="" "bwwwja0yfja=", " version":="" 3="">`\ \` **YAML example:** :literal:` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01t00:00:00.000z')="" etag:="" bwwwja0yfja="version:">`\ \` For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).  
  
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
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.bigquery_connection_v1.services.connection_service.transports.base.ConnectionServiceTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### list_connections
    
    
    list_connections(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_connection_v1.types.connection.ListConnectionsRequest,
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
        google.cloud.bigquery_connection_v1.services.connection_service.pagers.ListConnectionsAsyncPager
    )

Returns a list of connections in the given project.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest)
    
    async def sample_list_connections():
        # Create a client
        client = [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest).[ConnectionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest).[ListConnectionsRequest](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.types.ListConnectionsRequest.html)(
            parent="parent_value",
            page_size=951,
        )
    
        # Make the request
        page_result = client.[list_connections](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceAsyncClient.html#google_cloud_bigquery_connection_v1_services_connection_service_ConnectionServiceAsyncClient_list_connections)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_connection_v1.types.ListConnectionsRequest](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.types.ListConnectionsRequest), dict]]`   
The request object. The request for ConnectionService.ListConnections.  
`parent` |  ``str``   
Required. Parent resource name. Must be in the form: `projects/{project_id}/locations/{location_id}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_connection_v1.services.connection_service.pagers.ListConnectionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.pagers.ListConnectionsAsyncPager)` | The response for ConnectionService.ListConnections. Iterating over this object will yield results and resolve additional pages automatically.  
  
### parse_cluster_path
    
    
    parse_cluster_path(path: str) -> typing.Dict[str, str]

Parses a cluster path into its component segments.

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

### parse_connection_path
    
    
    parse_connection_path(path: str) -> typing.Dict[str, str]

Parses a connection path into its component segments.

### parse_service_path
    
    
    parse_service_path(path: str) -> typing.Dict[str, str]

Parses a service path into its component segments.

### service_path
    
    
    service_path(project: str, location: str, service: str) -> str

Returns a fully-qualified service string.

### set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Sets the access control policy on the specified resource. Replaces any existing policy.

Can return `NOT_FOUND`, `INVALID_ARGUMENT`, and `PERMISSION_DENIED` errors.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest)
    import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
    
    async def sample_set_iam_policy():
        # Create a client
        client = [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest).[ConnectionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_policy_pb2.SetIamPolicyRequest(
            resource="resource_value",
        )
    
        # Make the request
        response = await client.[set_iam_policy](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceAsyncClient.html#google_cloud_bigquery_connection_v1_services_connection_service_ConnectionServiceAsyncClient_set_iam_policy)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L103-L109), dict]]`   
The request object. Request message for `SetIamPolicy` method.  
`resource` |  ``str``   
REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.iam.v1.policy_pb2.Policy` | An Identity and Access Management (IAM) policy, which specifies access controls for Google Cloud resources. A Policy is a collection of bindings. A binding binds one or more members, or principals, to a single role. Principals can be user accounts, service accounts, Google groups, and domains (such as G Suite). A role is a named list of permissions; each role can be an IAM predefined role or a user-created custom role. For some types of Google Cloud resources, a binding can also specify a condition, which is a logical expression that allows access to a resource only if the expression evaluates to true. A condition can add constraints based on attributes of the request, the resource, or both. To learn which resources support conditions in their IAM policies, see the [IAM documentation](https://cloud.google.com/iam/help/conditions/resource-policies). **JSON example:** :literal:` { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": [ "user:eve@example.com" ], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ],="" "etag":="" "bwwwja0yfja=", " version":="" 3="">`\ \` **YAML example:** :literal:` bindings: - members: - user:mike@example.com - group:admins@example.com - domain:google.com - serviceAccount:my-project-id@appspot.gserviceaccount.com role: roles/resourcemanager.organizationAdmin - members: - user:eve@example.com role: roles/resourcemanager.organizationViewer condition: title: expirable access description: Does not grant access after Sep 2020 expression: request.time < timestamp('2020-10-01t00:00:00.000z')="" etag:="" bwwwja0yfja="version:">`\ \` For a description of IAM and its features, see the [IAM documentation](https://cloud.google.com/iam/docs/).  
  
### test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        permissions: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Returns permissions that a caller has on the specified resource. If the resource does not exist, this will return an empty set of permissions, not a `NOT_FOUND` error.

Note: This operation is designed to be used for building permission-aware UIs and command-line tools, not for authorization checking. This operation may "fail open" without warning.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest)
    import google.iam.v1.iam_policy_pb2 as iam_policy_pb2  # type: ignore
    
    async def sample_test_iam_permissions():
        # Create a client
        client = [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest).[ConnectionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = iam_policy_pb2.TestIamPermissionsRequest(
            resource="resource_value",
            permissions=['permissions_value1', 'permissions_value2'],
        )
    
        # Make the request
        response = await client.[test_iam_permissions](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceAsyncClient.html#google_cloud_bigquery_connection_v1_services_connection_service_ConnectionServiceAsyncClient_test_iam_permissions)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L120-L131), dict]]`   
The request object. Request message for `TestIamPermissions` method.  
`resource` |  ``str``   
REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field. This corresponds to the `resource` field on the `request` instance; if `request` is provided, this should not be set.  
`permissions` |  `:class:`MutableSequence[str]``   
The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see `IAM Overview <https://cloud.google.com/iam/docs/overview#permissions>`__. This corresponds to the `permissions` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse](http://github.com/googleapis/python-grpc-google-iam-v1/blob/8e73b45993f030f521c0169b380d0fbafe66630b/google/iam/v1/iam_policy_pb2_grpc.py#L120-L131)` | Response message for TestIamPermissions method.  
  
### update_connection
    
    
    update_connection(
        request: typing.Optional[
            typing.Union[
                google.cloud.bigquery_connection_v1.types.connection.UpdateConnectionRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        connection: typing.Optional[
            google.cloud.bigquery_connection_v1.types.connection.Connection
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
    ) -> google.cloud.bigquery_connection_v1.types.connection.Connection

Updates the specified connection. For security reasons, also resets credential if connection properties are in the update field mask.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest)
    
    async def sample_update_connection():
        # Create a client
        client = [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest).[ConnectionServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [bigquery_connection_v1](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest).[UpdateConnectionRequest](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.types.UpdateConnectionRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[update_connection](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.services.connection_service.ConnectionServiceAsyncClient.html#google_cloud_bigquery_connection_v1_services_connection_service_ConnectionServiceAsyncClient_update_connection)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.bigquery_connection_v1.types.UpdateConnectionRequest](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.types.UpdateConnectionRequest), dict]]`   
The request object. The request for ConnectionService.UpdateConnection.  
`name` |  ``str``   
Required. Name of the connection to update, for example: `projects/{project_id}/locations/{location_id}/connections/{connection_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`connection` |  `[Connection](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.types.Connection)`   
Required. Connection containing the updated fields. This corresponds to the `connection` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. Update mask for the connection fields to be updated. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.bigquery_connection_v1.types.Connection](https://docs.cloud.google.com/python/docs/reference/bigqueryconnection/latest/google.cloud.bigquery_connection_v1.types.Connection)` | Configuration parameters to establish connection with an external data source, except the credential attributes.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
