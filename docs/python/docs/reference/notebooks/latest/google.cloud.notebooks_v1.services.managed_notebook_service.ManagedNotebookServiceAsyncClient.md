---
url: https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient
title: Class ManagedNotebookServiceAsyncClient (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:34.434053+00:00
---

# Class ManagedNotebookServiceAsyncClient (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class ManagedNotebookServiceAsyncClient (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.3  1.12.0  1.11.1  1.10.5  1.9.0  1.8.0  1.7.1  1.6.1  1.5.1  1.4.4  1.3.2  1.2.1  1.1.1  1.0.0  0.4.3  0.3.2  0.2.0  0.1.2 
    
    
    ManagedNotebookServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.notebooks_v1.services.managed_notebook_service.transports.base.ManagedNotebookServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.notebooks_v1.services.managed_notebook_service.transports.base.ManagedNotebookServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

API v1 service for Managed Notebooks.

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
`ManagedNotebookServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### ManagedNotebookServiceAsyncClient
    
    
    ManagedNotebookServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.notebooks_v1.services.managed_notebook_service.transports.base.ManagedNotebookServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.notebooks_v1.services.managed_notebook_service.transports.base.ManagedNotebookServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the managed notebook service async client.

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,ManagedNotebookServiceTransport,Callable[..., ManagedNotebookServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the ManagedNotebookServiceTransport constructor. If set to None, a transport is chosen automatically.  
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

### create_runtime
    
    
    create_runtime(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.managed_service.CreateRuntimeRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        runtime_id: typing.Optional[str] = None,
        runtime: typing.Optional[google.cloud.notebooks_v1.types.runtime.Runtime] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Runtime in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    async def sample_create_runtime():
        # Create a client
        client = notebooks_v1.[ManagedNotebookServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = notebooks_v1.[CreateRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.CreateRuntimeRequest.html)(
            parent="parent_value",
            runtime_id="runtime_id_value",
        )
    
        # Make the request
        operation = await client.[create_runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_create_runtime)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.notebooks_v1.types.CreateRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.CreateRuntimeRequest), dict]]`   
The request object. Request for creating a Managed Notebook Runtime.  
`parent` |  ``str``   
Required. Format: `parent=projects/{project_id}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`runtime_id` |  ``str``   
Required. User-defined unique ID of this Runtime. This corresponds to the `runtime_id` field on the `request` instance; if `request` is provided, this should not be set.  
`runtime` |  `[Runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Runtime)`   
Required. The Runtime to be created. This corresponds to the `runtime` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Runtime) The definition of a Runtime for a managed notebook instance.  
  
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
  
### delete_runtime
    
    
    delete_runtime(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.managed_service.DeleteRuntimeRequest, dict
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

Deletes a single Runtime.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    async def sample_delete_runtime():
        # Create a client
        client = notebooks_v1.[ManagedNotebookServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = notebooks_v1.[DeleteRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DeleteRuntimeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[delete_runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_delete_runtime)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.notebooks_v1.types.DeleteRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DeleteRuntimeRequest), dict]]`   
The request object. Request for deleting a Managed Notebook Runtime.  
`name` |  ``str``   
Required. Format: `projects/{project_id}/locations/{location}/runtimes/{runtime_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
  
### diagnose_runtime
    
    
    diagnose_runtime(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.managed_service.DiagnoseRuntimeRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        diagnostic_config: typing.Optional[
            google.cloud.notebooks_v1.types.diagnostic_config.DiagnosticConfig
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

Creates a Diagnostic File and runs Diagnostic Tool given a Runtime.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    async def sample_diagnose_runtime():
        # Create a client
        client = notebooks_v1.[ManagedNotebookServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        diagnostic_config = notebooks_v1.DiagnosticConfig()
        diagnostic_config.gcs_bucket = "gcs_bucket_value"
    
        request = notebooks_v1.[DiagnoseRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DiagnoseRuntimeRequest.html)(
            name="name_value",
            diagnostic_config=diagnostic_config,
        )
    
        # Make the request
        operation = await client.[diagnose_runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_diagnose_runtime)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.notebooks_v1.types.DiagnoseRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DiagnoseRuntimeRequest), dict]]`   
The request object. Request for creating a notebook instance diagnostic file.  
`name` |  ``str``   
Required. Format: `projects/{project_id}/locations/{location}/runtimes/{runtimes_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`diagnostic_config` |  `[DiagnosticConfig](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.DiagnosticConfig)`   
Required. Defines flags that are used to run the diagnostic tool This corresponds to the `diagnostic_config` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Runtime) The definition of a Runtime for a managed notebook instance.  
  
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
`ManagedNotebookServiceAsyncClient` | The constructed client.  
  
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
`ManagedNotebookServiceAsyncClient` | The constructed client.  
  
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
`ManagedNotebookServiceAsyncClient` | The constructed client.  
  
### get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

Returns an empty policy if the function exists and does not have a policy set.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.GetIamPolicyRequest``   
The request object. Request message for `GetIamPolicy` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.policy_pb2.Policy`` | Defines an Identity and Access Management (IAM) policy. It is used to specify access control policies for Cloud Platform resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members` to a single `role`. Members can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions (defined by IAM or configured by users). A `binding` can optionally specify a `condition`, which is a logic expression that further constrains the role binding based on attributes about the request and/or target resource. **JSON Example** :: { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": ["user:eve@example.com"], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ]="" }="" **yaml="" example**="" ::="" bindings:="" -="" members:="" -="" user:mike@example.com="" -="" group:admins@example.com="" -="" domain:google.com="" -="" serviceaccount:my-project-id@appspot.gserviceaccount.com="" role:="" roles/resourcemanager.organizationadmin="" -="" members:="" -="" user:eve@example.com="" role:="" roles/resourcemanager.organizationviewer="" condition:="" title:="" expirable="" access="" description:="" does="" not="" grant="" access="" after="" sep="" 2020="" expression:="" request.time="">< timestamp('2020-10-01t00:00:00.000z')="" for="" a="" description="" of="" iam="" and="" its="" features,="" see="" the="">`IAM developer's guide `__.  
  
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
  
### get_runtime
    
    
    get_runtime(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.managed_service.GetRuntimeRequest, dict
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
    ) -> google.cloud.notebooks_v1.types.runtime.Runtime

Gets details of a single Runtime. The location must be a regional endpoint rather than zonal.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    async def sample_get_runtime():
        # Create a client
        client = notebooks_v1.[ManagedNotebookServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = notebooks_v1.[GetRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.GetRuntimeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_get_runtime)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.notebooks_v1.types.GetRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.GetRuntimeRequest), dict]]`   
The request object. Request for getting a Managed Notebook Runtime.  
`name` |  ``str``   
Required. Format: `projects/{project_id}/locations/{location}/runtimes/{runtime_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.notebooks_v1.types.Runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Runtime)` | The definition of a Runtime for a managed notebook instance.  
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.notebooks_v1.services.managed_notebook_service.transports.base.ManagedNotebookServiceTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
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
  
### list_runtimes
    
    
    list_runtimes(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.managed_service.ListRuntimesRequest, dict
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
        google.cloud.notebooks_v1.services.managed_notebook_service.pagers.ListRuntimesAsyncPager
    )

Lists Runtimes in a given project and location.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    async def sample_list_runtimes():
        # Create a client
        client = notebooks_v1.[ManagedNotebookServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = notebooks_v1.[ListRuntimesRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ListRuntimesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_runtimes](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_list_runtimes)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.notebooks_v1.types.ListRuntimesRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ListRuntimesRequest), dict]]`   
The request object. Request for listing Managed Notebook Runtimes.  
`parent` |  ``str``   
Required. Format: `parent=projects/{project_id}/locations/{location}` This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.notebooks_v1.services.managed_notebook_service.pagers.ListRuntimesAsyncPager](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.pagers.ListRuntimesAsyncPager)` | Response for listing Managed Notebook Runtimes. Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### parse_runtime_path
    
    
    parse_runtime_path(path: str) -> typing.Dict[str, str]

Parses a runtime path into its component segments.

### refresh_runtime_token_internal
    
    
    refresh_runtime_token_internal(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.managed_service.RefreshRuntimeTokenInternalRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        vm_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.notebooks_v1.types.managed_service.RefreshRuntimeTokenInternalResponse
    )

Gets an access token for the consumer service account that the customer attached to the runtime. Only accessible from the tenant instance.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    async def sample_refresh_runtime_token_internal():
        # Create a client
        client = notebooks_v1.[ManagedNotebookServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = notebooks_v1.[RefreshRuntimeTokenInternalRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.RefreshRuntimeTokenInternalRequest.html)(
            name="name_value",
            vm_id="vm_id_value",
        )
    
        # Make the request
        response = await client.[refresh_runtime_token_internal](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_refresh_runtime_token_internal)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.notebooks_v1.types.RefreshRuntimeTokenInternalRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.RefreshRuntimeTokenInternalRequest), dict]]`   
The request object. Request for getting a new access token.  
`name` |  ``str``   
Required. Format: `projects/{project_id}/locations/{location}/runtimes/{runtime_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`vm_id` |  ``str``   
Required. The VM hardware token for authenticating the VM. <https://cloud.google.com/compute/docs/instances/verifying-instance-identity> This corresponds to the `vm_id` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.notebooks_v1.types.RefreshRuntimeTokenInternalResponse](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.RefreshRuntimeTokenInternalResponse)` | Response with a new access token.  
  
### report_runtime_event
    
    
    report_runtime_event(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.managed_service.ReportRuntimeEventRequest,
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

Report and process a runtime event.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    async def sample_report_runtime_event():
        # Create a client
        client = notebooks_v1.[ManagedNotebookServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = notebooks_v1.[ReportRuntimeEventRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ReportRuntimeEventRequest.html)(
            name="name_value",
            vm_id="vm_id_value",
        )
    
        # Make the request
        operation = await client.[report_runtime_event](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_report_runtime_event)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.notebooks_v1.types.ReportRuntimeEventRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ReportRuntimeEventRequest), dict]]`   
The request object. Request for reporting a Managed Notebook Event.  
`name` |  ``str``   
Required. Format: `projects/{project_id}/locations/{location}/runtimes/{runtime_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Runtime) The definition of a Runtime for a managed notebook instance.  
  
### reset_runtime
    
    
    reset_runtime(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.managed_service.ResetRuntimeRequest, dict
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

Resets a Managed Notebook Runtime.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    async def sample_reset_runtime():
        # Create a client
        client = notebooks_v1.[ManagedNotebookServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = notebooks_v1.[ResetRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ResetRuntimeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[reset_runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_reset_runtime)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.notebooks_v1.types.ResetRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.ResetRuntimeRequest), dict]]`   
The request object. Request for resetting a Managed Notebook Runtime.  
`name` |  ``str``   
Required. Format: `projects/{project_id}/locations/{location}/runtimes/{runtime_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Runtime) The definition of a Runtime for a managed notebook instance.  
  
### runtime_path
    
    
    runtime_path(project: str, location: str, runtime: str) -> str

Returns a fully-qualified runtime string.

### set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

Replaces any existing policy.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.SetIamPolicyRequest``   
The request object. Request message for `SetIamPolicy` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.policy_pb2.Policy`` | Defines an Identity and Access Management (IAM) policy. It is used to specify access control policies for Cloud Platform resources. A `Policy` is a collection of `bindings`. A `binding` binds one or more `members` to a single `role`. Members can be user accounts, service accounts, Google groups, and domains (such as G Suite). A `role` is a named list of permissions (defined by IAM or configured by users). A `binding` can optionally specify a `condition`, which is a logic expression that further constrains the role binding based on attributes about the request and/or target resource. **JSON Example** :: { "bindings": [ { "role": "roles/resourcemanager.organizationAdmin", "members": [ "user:mike@example.com", "group:admins@example.com", "domain:google.com", "serviceAccount:my-project-id@appspot.gserviceaccount.com" ] }, { "role": "roles/resourcemanager.organizationViewer", "members": ["user:eve@example.com"], "condition": { "title": "expirable access", "description": "Does not grant access after Sep 2020", "expression": "request.time < timestamp('2020-10-01t00:00:00.000z')",="" }="" }="" ]="" }="" **yaml="" example**="" ::="" bindings:="" -="" members:="" -="" user:mike@example.com="" -="" group:admins@example.com="" -="" domain:google.com="" -="" serviceaccount:my-project-id@appspot.gserviceaccount.com="" role:="" roles/resourcemanager.organizationadmin="" -="" members:="" -="" user:eve@example.com="" role:="" roles/resourcemanager.organizationviewer="" condition:="" title:="" expirable="" access="" description:="" does="" not="" grant="" access="" after="" sep="" 2020="" expression:="" request.time="">< timestamp('2020-10-01t00:00:00.000z')="" for="" a="" description="" of="" iam="" and="" its="" features,="" see="" the="">`IAM developer's guide `__.  
  
### start_runtime
    
    
    start_runtime(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.managed_service.StartRuntimeRequest, dict
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

Starts a Managed Notebook Runtime. Perform "Start" on GPU instances; "Resume" on CPU instances See:

<https://cloud.google.com/compute/docs/instances/stop-start-instance> <https://cloud.google.com/compute/docs/instances/suspend-resume-instance>
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    async def sample_start_runtime():
        # Create a client
        client = notebooks_v1.[ManagedNotebookServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = notebooks_v1.[StartRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.StartRuntimeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[start_runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_start_runtime)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.notebooks_v1.types.StartRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.StartRuntimeRequest), dict]]`   
The request object. Request for starting a Managed Notebook Runtime.  
`name` |  ``str``   
Required. Format: `projects/{project_id}/locations/{location}/runtimes/{runtime_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Runtime) The definition of a Runtime for a managed notebook instance.  
  
### stop_runtime
    
    
    stop_runtime(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.managed_service.StopRuntimeRequest, dict
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

Stops a Managed Notebook Runtime. Perform "Stop" on GPU instances; "Suspend" on CPU instances See:

<https://cloud.google.com/compute/docs/instances/stop-start-instance> <https://cloud.google.com/compute/docs/instances/suspend-resume-instance>
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    async def sample_stop_runtime():
        # Create a client
        client = notebooks_v1.[ManagedNotebookServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = notebooks_v1.[StopRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.StopRuntimeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[stop_runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_stop_runtime)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.notebooks_v1.types.StopRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.StopRuntimeRequest), dict]]`   
The request object. Request for stopping a Managed Notebook Runtime.  
`name` |  ``str``   
Required. Format: `projects/{project_id}/locations/{location}/runtimes/{runtime_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Runtime) The definition of a Runtime for a managed notebook instance.  
  
### switch_runtime
    
    
    switch_runtime(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.managed_service.SwitchRuntimeRequest, dict
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

Switch a Managed Notebook Runtime.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    async def sample_switch_runtime():
        # Create a client
        client = notebooks_v1.[ManagedNotebookServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = notebooks_v1.[SwitchRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.SwitchRuntimeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[switch_runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_switch_runtime)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.notebooks_v1.types.SwitchRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.SwitchRuntimeRequest), dict]]`   
The request object. Request for switching a Managed Notebook Runtime.  
`name` |  ``str``   
Required. Format: `projects/{project_id}/locations/{location}/runtimes/{runtime_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Runtime) The definition of a Runtime for a managed notebook instance.  
  
### test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
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
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified IAM permissions against the IAM access control policy for a function.

If the function does not exist, this will return an empty set of permissions, not a NOT_FOUND error.

**Parameters**  
---  
**Name** | **Description**  
`request` |  ``.iam_policy_pb2.TestIamPermissionsRequest``   
The request object. Request message for `TestIamPermissions` method.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
``.iam_policy_pb2.TestIamPermissionsResponse`` | Response message for `TestIamPermissions` method.  
  
### update_runtime
    
    
    update_runtime(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.managed_service.UpdateRuntimeRequest, dict
            ]
        ] = None,
        *,
        runtime: typing.Optional[google.cloud.notebooks_v1.types.runtime.Runtime] = None,
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

Update Notebook Runtime configuration.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    async def sample_update_runtime():
        # Create a client
        client = notebooks_v1.[ManagedNotebookServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = notebooks_v1.[UpdateRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpdateRuntimeRequest.html)(
        )
    
        # Make the request
        operation = await client.[update_runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_update_runtime)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.notebooks_v1.types.UpdateRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpdateRuntimeRequest), dict]]`   
The request object. Request for updating a Managed Notebook configuration.  
`runtime` |  `[Runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Runtime)`   
Required. The Runtime to be updated. This corresponds to the `runtime` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Required. Specifies the path, relative to `Runtime`, of the field to update. For example, to change the software configuration kernels, the `update_mask` parameter would be specified as `software_config.kernels`, and the `PATCH` request body would specify the new value, as follows: :: { "software_config":{ "kernels": [{ 'repository': 'gcr.io/deeplearning-platform-release/pytorch-gpu', 'tag': 'latest' }], } } Currently, only the following fields can be updated: - `software_config.kernels` \- `software_config.post_startup_script` \- `software_config.custom_gpu_driver_path` \- `software_config.idle_shutdown` \- `software_config.idle_shutdown_timeout` \- `software_config.disable_terminal` This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Runtime) The definition of a Runtime for a managed notebook instance.  
  
### upgrade_runtime
    
    
    upgrade_runtime(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.managed_service.UpgradeRuntimeRequest, dict
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

Upgrades a Managed Notebook Runtime to the latest version.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import notebooks_v1
    
    async def sample_upgrade_runtime():
        # Create a client
        client = notebooks_v1.[ManagedNotebookServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = notebooks_v1.[UpgradeRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpgradeRuntimeRequest.html)(
            name="name_value",
        )
    
        # Make the request
        operation = await client.[upgrade_runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.html#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_upgrade_runtime)(request=request)
    
        print("Waiting for operation to complete...")
    
        response = await operation.result()
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.notebooks_v1.types.UpgradeRuntimeRequest](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.UpgradeRuntimeRequest), dict]]`   
The request object. Request for upgrading a Managed Notebook Runtime to the latest version. option (google.api.message_visibility).restriction = "TRUSTED_TESTER,SPECIAL_TESTER";  
`name` |  ``str``   
Required. Format: `projects/{project_id}/locations/{location}/runtimes/{runtime_id}` This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`google.api_core.operation_async.AsyncOperation` | An object representing a long-running operation. The result type for the operation will be [Runtime](https://docs.cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.types.Runtime) The definition of a Runtime for a managed notebook instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
