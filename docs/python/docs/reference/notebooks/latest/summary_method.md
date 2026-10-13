---
url: https://docs.cloud.google.com/python/docs/reference/notebooks/latest/summary_method/
title: Package Methods (1.18.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:33.315054+00:00
---

# Package Methods (1.18.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/notebooks/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.3  1.12.0  1.11.1  1.10.5  1.9.0  1.8.0  1.7.1  1.6.1  1.5.1  1.4.4  1.3.2  1.2.1  1.1.1  1.0.0  0.4.3  0.3.2  0.2.0  0.1.2 

Summary of entries of Methods for notebooks.

## 

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_ManagedNotebookServiceAsyncClient)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_cancel_operation)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_common_billing_account_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_common_folder_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_common_location_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_common_organization_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_common_project_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.create_runtime
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.create_runtime](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_create_runtime)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.delete_operation
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_delete_operation)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.delete_runtime
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.delete_runtime](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_delete_runtime)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.diagnose_runtime
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.diagnose_runtime](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_diagnose_runtime)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_from_service_account_file)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_from_service_account_info)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_from_service_account_json)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.get_iam_policy
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_get_iam_policy)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.get_location
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.get_location](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_get_location)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_get_operation)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.get_runtime
    
    
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

Gets details of a single Runtime.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.get_runtime](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_get_runtime)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.notebooks_v1.services.managed_notebook_service.transports.base.ManagedNotebookServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_get_transport_class)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.list_locations
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_list_locations)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.list_operations
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_list_operations)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.list_runtimes
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.list_runtimes](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_list_runtimes)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_parse_common_folder_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_parse_common_location_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_parse_common_organization_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_parse_common_project_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.parse_runtime_path
    
    
    parse_runtime_path(path: str) -> typing.Dict[str, str]

Parses a runtime path into its component segments.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.parse_runtime_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_parse_runtime_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.refresh_runtime_token_internal
    
    
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

Gets an access token for the consumer service account that the customer attached to the runtime.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.refresh_runtime_token_internal](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_refresh_runtime_token_internal)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.report_runtime_event
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.report_runtime_event](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_report_runtime_event)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.reset_runtime
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.reset_runtime](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_reset_runtime)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.runtime_path
    
    
    runtime_path(project: str, location: str, runtime: str) -> str

Returns a fully-qualified runtime string.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.runtime_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_runtime_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.set_iam_policy
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_set_iam_policy)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.start_runtime
    
    
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

Starts a Managed Notebook Runtime.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.start_runtime](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_start_runtime)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.stop_runtime
    
    
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

Stops a Managed Notebook Runtime.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.stop_runtime](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_stop_runtime)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.switch_runtime
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.switch_runtime](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_switch_runtime)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.test_iam_permissions
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_test_iam_permissions)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.update_runtime
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.update_runtime](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_update_runtime)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.upgrade_runtime
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient.upgrade_runtime](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceAsyncClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceAsyncClient_upgrade_runtime)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient
    
    
    ManagedNotebookServiceClient(
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
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the managed notebook service client.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_ManagedNotebookServiceClient)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.**exit**](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient___exit__)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.cancel_operation
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.cancel_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_cancel_operation)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_common_billing_account_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_common_folder_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_common_location_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_common_organization_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_common_project_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.create_runtime
    
    
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
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new Runtime in a given project and location.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.create_runtime](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_create_runtime)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.delete_operation
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.delete_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_delete_operation)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.delete_runtime
    
    
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
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Deletes a single Runtime.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.delete_runtime](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_delete_runtime)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.diagnose_runtime
    
    
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
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a Diagnostic File and runs Diagnostic Tool given a Runtime.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.diagnose_runtime](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_diagnose_runtime)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_from_service_account_file)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_from_service_account_info)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_from_service_account_json)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.get_iam_policy](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_get_iam_policy)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.get_location
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.get_location](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_get_location)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.get_operation
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.get_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_get_operation)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.get_runtime
    
    
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
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.notebooks_v1.types.runtime.Runtime

Gets details of a single Runtime.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.get_runtime](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_get_runtime)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.list_locations
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.list_locations](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_list_locations)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.list_operations
    
    
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

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.list_operations](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_list_operations)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.list_runtimes
    
    
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
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.notebooks_v1.services.managed_notebook_service.pagers.ListRuntimesPager
    )

Lists Runtimes in a given project and location.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.list_runtimes](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_list_runtimes)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_parse_common_billing_account_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_parse_common_folder_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_parse_common_location_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_parse_common_organization_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_parse_common_project_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.parse_runtime_path
    
    
    parse_runtime_path(path: str) -> typing.Dict[str, str]

Parses a runtime path into its component segments.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.parse_runtime_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_parse_runtime_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.refresh_runtime_token_internal
    
    
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
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.notebooks_v1.types.managed_service.RefreshRuntimeTokenInternalResponse
    )

Gets an access token for the consumer service account that the customer attached to the runtime.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.refresh_runtime_token_internal](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_refresh_runtime_token_internal)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.report_runtime_event
    
    
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
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Report and process a runtime event.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.report_runtime_event](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_report_runtime_event)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.reset_runtime
    
    
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
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Resets a Managed Notebook Runtime.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.reset_runtime](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_reset_runtime)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.runtime_path
    
    
    runtime_path(project: str, location: str, runtime: str) -> str

Returns a fully-qualified runtime string.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.runtime_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_runtime_path)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.set_iam_policy](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_set_iam_policy)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.start_runtime
    
    
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
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Starts a Managed Notebook Runtime.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.start_runtime](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_start_runtime)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.stop_runtime
    
    
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
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Stops a Managed Notebook Runtime.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.stop_runtime](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_stop_runtime)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.switch_runtime
    
    
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
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Switch a Managed Notebook Runtime.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.switch_runtime](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_switch_runtime)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
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
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified IAM permissions against the IAM access control policy for a function.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_test_iam_permissions)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.update_runtime
    
    
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
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Update Notebook Runtime configuration.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.update_runtime](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_update_runtime)

### google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.upgrade_runtime
    
    
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
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Upgrades a Managed Notebook Runtime to the latest version.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient.upgrade_runtime](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.ManagedNotebookServiceClient#google_cloud_notebooks_v1_services_managed_notebook_service_ManagedNotebookServiceClient_upgrade_runtime)

### google.cloud.notebooks_v1.services.managed_notebook_service.pagers.ListRuntimesAsyncPager
    
    
    ListRuntimesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.notebooks_v1.types.managed_service.ListRuntimesResponse
            ],
        ],
        request: google.cloud.notebooks_v1.types.managed_service.ListRuntimesRequest,
        response: google.cloud.notebooks_v1.types.managed_service.ListRuntimesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.pagers.ListRuntimesAsyncPager](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.pagers.ListRuntimesAsyncPager#google_cloud_notebooks_v1_services_managed_notebook_service_pagers_ListRuntimesAsyncPager_ListRuntimesAsyncPager)

### google.cloud.notebooks_v1.services.managed_notebook_service.pagers.ListRuntimesPager
    
    
    ListRuntimesPager(
        method: typing.Callable[
            [...], google.cloud.notebooks_v1.types.managed_service.ListRuntimesResponse
        ],
        request: google.cloud.notebooks_v1.types.managed_service.ListRuntimesRequest,
        response: google.cloud.notebooks_v1.types.managed_service.ListRuntimesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.notebooks_v1.services.managed_notebook_service.pagers.ListRuntimesPager](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.managed_notebook_service.pagers.ListRuntimesPager#google_cloud_notebooks_v1_services_managed_notebook_service_pagers_ListRuntimesPager_ListRuntimesPager)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient
    
    
    NotebookServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.notebooks_v1.services.notebook_service.transports.base.NotebookServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.notebooks_v1.services.notebook_service.transports.base.NotebookServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the notebook service async client.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_NotebookServiceAsyncClient)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_cancel_operation)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_common_billing_account_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_common_folder_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_common_location_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_common_organization_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_common_project_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.create_environment
    
    
    create_environment(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.CreateEnvironmentRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        environment: typing.Optional[
            google.cloud.notebooks_v1.types.environment.Environment
        ] = None,
        environment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Environment.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.create_environment](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_create_environment)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.create_execution
    
    
    create_execution(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.CreateExecutionRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        execution: typing.Optional[
            google.cloud.notebooks_v1.types.execution.Execution
        ] = None,
        execution_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Execution in a given project and location.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.create_execution](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_create_execution)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.create_instance
    
    
    create_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.CreateInstanceRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        instance: typing.Optional[google.cloud.notebooks_v1.types.instance.Instance] = None,
        instance_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Instance in a given project and location.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.create_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_create_instance)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.create_schedule
    
    
    create_schedule(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.CreateScheduleRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        schedule: typing.Optional[google.cloud.notebooks_v1.types.schedule.Schedule] = None,
        schedule_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Scheduled Notebook in a given project and location.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.create_schedule](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_create_schedule)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.delete_environment
    
    
    delete_environment(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.DeleteEnvironmentRequest, dict
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

Deletes a single Environment.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.delete_environment](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_delete_environment)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.delete_execution
    
    
    delete_execution(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.DeleteExecutionRequest, dict
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

Deletes execution.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.delete_execution](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_delete_execution)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.delete_instance
    
    
    delete_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.DeleteInstanceRequest, dict
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

Deletes a single Instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.delete_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_delete_instance)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.delete_operation
    
    
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

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_delete_operation)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.delete_schedule
    
    
    delete_schedule(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.DeleteScheduleRequest, dict
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

Deletes schedule and all underlying jobs.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.delete_schedule](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_delete_schedule)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.diagnose_instance
    
    
    diagnose_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.DiagnoseInstanceRequest, dict
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

Creates a Diagnostic File and runs Diagnostic Tool given an Instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.diagnose_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_diagnose_instance)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.environment_path
    
    
    environment_path(project: str, environment: str) -> str

Returns a fully-qualified environment string.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.environment_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_environment_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.execution_path
    
    
    execution_path(project: str, location: str, execution: str) -> str

Returns a fully-qualified execution string.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.execution_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_execution_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_from_service_account_file)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_from_service_account_info)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_from_service_account_json)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.get_environment
    
    
    get_environment(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.GetEnvironmentRequest, dict
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
    ) -> google.cloud.notebooks_v1.types.environment.Environment

Gets details of a single Environment.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.get_environment](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_get_environment)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.get_execution
    
    
    get_execution(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.GetExecutionRequest, dict]
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
    ) -> google.cloud.notebooks_v1.types.execution.Execution

Gets details of executions.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.get_execution](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_get_execution)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.get_iam_policy
    
    
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

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_get_iam_policy)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.get_instance
    
    
    get_instance(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.GetInstanceRequest, dict]
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
    ) -> google.cloud.notebooks_v1.types.instance.Instance

Gets details of a single Instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.get_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_get_instance)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.get_instance_health
    
    
    get_instance_health(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.GetInstanceHealthRequest, dict
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
    ) -> google.cloud.notebooks_v1.types.service.GetInstanceHealthResponse

Check if a notebook instance is healthy.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.get_instance_health](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_get_instance_health)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.get_location
    
    
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

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.get_location](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_get_location)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_get_operation)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.get_schedule
    
    
    get_schedule(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.GetScheduleRequest, dict]
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
    ) -> google.cloud.notebooks_v1.types.schedule.Schedule

Gets details of schedule.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.get_schedule](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_get_schedule)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.notebooks_v1.services.notebook_service.transports.base.NotebookServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_get_transport_class)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.instance_path
    
    
    instance_path(project: str, instance: str) -> str

Returns a fully-qualified instance string.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.instance_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_instance_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.is_instance_upgradeable
    
    
    is_instance_upgradeable(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.IsInstanceUpgradeableRequest, dict
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
    ) -> google.cloud.notebooks_v1.types.service.IsInstanceUpgradeableResponse

Check if a notebook instance is upgradable.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.is_instance_upgradeable](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_is_instance_upgradeable)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.list_environments
    
    
    list_environments(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.ListEnvironmentsRequest, dict
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
        google.cloud.notebooks_v1.services.notebook_service.pagers.ListEnvironmentsAsyncPager
    )

Lists environments in a project.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.list_environments](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_list_environments)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.list_executions
    
    
    list_executions(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.ListExecutionsRequest, dict
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
        google.cloud.notebooks_v1.services.notebook_service.pagers.ListExecutionsAsyncPager
    )

Lists executions in a given project and location.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.list_executions](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_list_executions)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.list_instances
    
    
    list_instances(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.ListInstancesRequest, dict]
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
    ) -> google.cloud.notebooks_v1.services.notebook_service.pagers.ListInstancesAsyncPager

Lists instances in a given project and location.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.list_instances](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_list_instances)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.list_locations
    
    
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

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_list_locations)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.list_operations
    
    
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

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_list_operations)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.list_schedules
    
    
    list_schedules(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.ListSchedulesRequest, dict]
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
    ) -> google.cloud.notebooks_v1.services.notebook_service.pagers.ListSchedulesAsyncPager

Lists schedules in a given project and location.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.list_schedules](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_list_schedules)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_parse_common_folder_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_parse_common_location_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_parse_common_organization_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_parse_common_project_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.parse_environment_path
    
    
    parse_environment_path(path: str) -> typing.Dict[str, str]

Parses a environment path into its component segments.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.parse_environment_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_parse_environment_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.parse_execution_path
    
    
    parse_execution_path(path: str) -> typing.Dict[str, str]

Parses a execution path into its component segments.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.parse_execution_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_parse_execution_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.parse_instance_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_parse_instance_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.parse_schedule_path
    
    
    parse_schedule_path(path: str) -> typing.Dict[str, str]

Parses a schedule path into its component segments.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.parse_schedule_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_parse_schedule_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.parse_tensorboard_path
    
    
    parse_tensorboard_path(path: str) -> typing.Dict[str, str]

Parses a tensorboard path into its component segments.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.parse_tensorboard_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_parse_tensorboard_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.register_instance
    
    
    register_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.RegisterInstanceRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Registers an existing legacy notebook instance to the Notebooks API server.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.register_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_register_instance)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.report_instance_info
    
    
    report_instance_info(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.ReportInstanceInfoRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Allows notebook instances to report their latest instance information to the Notebooks API server.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.report_instance_info](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_report_instance_info)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.reset_instance
    
    
    reset_instance(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.ResetInstanceRequest, dict]
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

Resets a notebook instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.reset_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_reset_instance)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.rollback_instance
    
    
    rollback_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.RollbackInstanceRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Rollbacks a notebook instance to the previous version.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.rollback_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_rollback_instance)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.schedule_path
    
    
    schedule_path(project: str, location: str, schedule: str) -> str

Returns a fully-qualified schedule string.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.schedule_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_schedule_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.set_iam_policy
    
    
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

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_set_iam_policy)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.set_instance_accelerator
    
    
    set_instance_accelerator(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.SetInstanceAcceleratorRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Updates the guest accelerators of a single Instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.set_instance_accelerator](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_set_instance_accelerator)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.set_instance_labels
    
    
    set_instance_labels(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.SetInstanceLabelsRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Replaces all the labels of an Instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.set_instance_labels](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_set_instance_labels)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.set_instance_machine_type
    
    
    set_instance_machine_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.SetInstanceMachineTypeRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Updates the machine type of a single Instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.set_instance_machine_type](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_set_instance_machine_type)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.start_instance
    
    
    start_instance(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.StartInstanceRequest, dict]
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

Starts a notebook instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.start_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_start_instance)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.stop_instance
    
    
    stop_instance(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.StopInstanceRequest, dict]
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

Stops a notebook instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.stop_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_stop_instance)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.tensorboard_path
    
    
    tensorboard_path(project: str, location: str, tensorboard: str) -> str

Returns a fully-qualified tensorboard string.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.tensorboard_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_tensorboard_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.test_iam_permissions
    
    
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

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_test_iam_permissions)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.trigger_schedule
    
    
    trigger_schedule(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.TriggerScheduleRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Triggers execution of an existing schedule.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.trigger_schedule](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_trigger_schedule)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.update_instance_config
    
    
    update_instance_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.UpdateInstanceConfigRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Update Notebook Instance configurations.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.update_instance_config](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_update_instance_config)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.update_instance_metadata_items
    
    
    update_instance_metadata_items(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.UpdateInstanceMetadataItemsRequest,
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
    ) -> google.cloud.notebooks_v1.types.service.UpdateInstanceMetadataItemsResponse

Add/update metadata items for an instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.update_instance_metadata_items](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_update_instance_metadata_items)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.update_shielded_instance_config
    
    
    update_shielded_instance_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.UpdateShieldedInstanceConfigRequest,
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
    ) -> google.api_core.operation_async.AsyncOperation

Updates the Shielded instance configuration of a single Instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.update_shielded_instance_config](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_update_shielded_instance_config)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.upgrade_instance
    
    
    upgrade_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.UpgradeInstanceRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Upgrades a notebook instance to the latest version.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.upgrade_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_upgrade_instance)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.upgrade_instance_internal
    
    
    upgrade_instance_internal(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.UpgradeInstanceInternalRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Allows notebook instances to call this endpoint to upgrade themselves.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient.upgrade_instance_internal](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceAsyncClient_upgrade_instance_internal)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient
    
    
    NotebookServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.notebooks_v1.services.notebook_service.transports.base.NotebookServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.notebooks_v1.services.notebook_service.transports.base.NotebookServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the notebook service client.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_NotebookServiceClient)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.**exit**](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient___exit__)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.cancel_operation
    
    
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

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.cancel_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_cancel_operation)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_common_billing_account_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_common_folder_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_common_location_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_common_organization_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_common_project_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.create_environment
    
    
    create_environment(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.CreateEnvironmentRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        environment: typing.Optional[
            google.cloud.notebooks_v1.types.environment.Environment
        ] = None,
        environment_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new Environment.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.create_environment](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_create_environment)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.create_execution
    
    
    create_execution(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.CreateExecutionRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        execution: typing.Optional[
            google.cloud.notebooks_v1.types.execution.Execution
        ] = None,
        execution_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new Execution in a given project and location.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.create_execution](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_create_execution)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.create_instance
    
    
    create_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.CreateInstanceRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        instance: typing.Optional[google.cloud.notebooks_v1.types.instance.Instance] = None,
        instance_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new Instance in a given project and location.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.create_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_create_instance)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.create_schedule
    
    
    create_schedule(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.CreateScheduleRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        schedule: typing.Optional[google.cloud.notebooks_v1.types.schedule.Schedule] = None,
        schedule_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new Scheduled Notebook in a given project and location.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.create_schedule](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_create_schedule)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.delete_environment
    
    
    delete_environment(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.DeleteEnvironmentRequest, dict
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

Deletes a single Environment.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.delete_environment](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_delete_environment)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.delete_execution
    
    
    delete_execution(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.DeleteExecutionRequest, dict
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

Deletes execution.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.delete_execution](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_delete_execution)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.delete_instance
    
    
    delete_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.DeleteInstanceRequest, dict
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

Deletes a single Instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.delete_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_delete_instance)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.delete_operation
    
    
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

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.delete_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_delete_operation)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.delete_schedule
    
    
    delete_schedule(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.DeleteScheduleRequest, dict
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

Deletes schedule and all underlying jobs.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.delete_schedule](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_delete_schedule)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.diagnose_instance
    
    
    diagnose_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.DiagnoseInstanceRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        diagnostic_config: typing.Optional[
            google.cloud.notebooks_v1.types.diagnostic_config.DiagnosticConfig
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a Diagnostic File and runs Diagnostic Tool given an Instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.diagnose_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_diagnose_instance)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.environment_path
    
    
    environment_path(project: str, environment: str) -> str

Returns a fully-qualified environment string.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.environment_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_environment_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.execution_path
    
    
    execution_path(project: str, location: str, execution: str) -> str

Returns a fully-qualified execution string.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.execution_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_execution_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_from_service_account_file)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_from_service_account_info)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_from_service_account_json)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.get_environment
    
    
    get_environment(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.GetEnvironmentRequest, dict
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
    ) -> google.cloud.notebooks_v1.types.environment.Environment

Gets details of a single Environment.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.get_environment](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_get_environment)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.get_execution
    
    
    get_execution(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.GetExecutionRequest, dict]
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
    ) -> google.cloud.notebooks_v1.types.execution.Execution

Gets details of executions.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.get_execution](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_get_execution)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.get_iam_policy](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_get_iam_policy)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.get_instance
    
    
    get_instance(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.GetInstanceRequest, dict]
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
    ) -> google.cloud.notebooks_v1.types.instance.Instance

Gets details of a single Instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.get_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_get_instance)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.get_instance_health
    
    
    get_instance_health(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.GetInstanceHealthRequest, dict
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
    ) -> google.cloud.notebooks_v1.types.service.GetInstanceHealthResponse

Check if a notebook instance is healthy.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.get_instance_health](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_get_instance_health)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.get_location
    
    
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

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.get_location](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_get_location)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.get_operation
    
    
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

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.get_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_get_operation)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.get_schedule
    
    
    get_schedule(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.GetScheduleRequest, dict]
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
    ) -> google.cloud.notebooks_v1.types.schedule.Schedule

Gets details of schedule.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.get_schedule](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_get_schedule)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.instance_path
    
    
    instance_path(project: str, instance: str) -> str

Returns a fully-qualified instance string.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.instance_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_instance_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.is_instance_upgradeable
    
    
    is_instance_upgradeable(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.IsInstanceUpgradeableRequest, dict
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
    ) -> google.cloud.notebooks_v1.types.service.IsInstanceUpgradeableResponse

Check if a notebook instance is upgradable.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.is_instance_upgradeable](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_is_instance_upgradeable)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.list_environments
    
    
    list_environments(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.ListEnvironmentsRequest, dict
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
    ) -> google.cloud.notebooks_v1.services.notebook_service.pagers.ListEnvironmentsPager

Lists environments in a project.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.list_environments](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_list_environments)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.list_executions
    
    
    list_executions(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.ListExecutionsRequest, dict
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
    ) -> google.cloud.notebooks_v1.services.notebook_service.pagers.ListExecutionsPager

Lists executions in a given project and location.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.list_executions](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_list_executions)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.list_instances
    
    
    list_instances(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.ListInstancesRequest, dict]
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
    ) -> google.cloud.notebooks_v1.services.notebook_service.pagers.ListInstancesPager

Lists instances in a given project and location.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.list_instances](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_list_instances)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.list_locations
    
    
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

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.list_locations](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_list_locations)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.list_operations
    
    
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

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.list_operations](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_list_operations)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.list_schedules
    
    
    list_schedules(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.ListSchedulesRequest, dict]
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
    ) -> google.cloud.notebooks_v1.services.notebook_service.pagers.ListSchedulesPager

Lists schedules in a given project and location.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.list_schedules](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_list_schedules)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_parse_common_billing_account_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_parse_common_folder_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_parse_common_location_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_parse_common_organization_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_parse_common_project_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.parse_environment_path
    
    
    parse_environment_path(path: str) -> typing.Dict[str, str]

Parses a environment path into its component segments.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.parse_environment_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_parse_environment_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.parse_execution_path
    
    
    parse_execution_path(path: str) -> typing.Dict[str, str]

Parses a execution path into its component segments.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.parse_execution_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_parse_execution_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.parse_instance_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_parse_instance_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.parse_schedule_path
    
    
    parse_schedule_path(path: str) -> typing.Dict[str, str]

Parses a schedule path into its component segments.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.parse_schedule_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_parse_schedule_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.parse_tensorboard_path
    
    
    parse_tensorboard_path(path: str) -> typing.Dict[str, str]

Parses a tensorboard path into its component segments.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.parse_tensorboard_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_parse_tensorboard_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.register_instance
    
    
    register_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.RegisterInstanceRequest, dict
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

Registers an existing legacy notebook instance to the Notebooks API server.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.register_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_register_instance)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.report_instance_info
    
    
    report_instance_info(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.ReportInstanceInfoRequest, dict
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

Allows notebook instances to report their latest instance information to the Notebooks API server.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.report_instance_info](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_report_instance_info)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.reset_instance
    
    
    reset_instance(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.ResetInstanceRequest, dict]
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

Resets a notebook instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.reset_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_reset_instance)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.rollback_instance
    
    
    rollback_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.RollbackInstanceRequest, dict
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

Rollbacks a notebook instance to the previous version.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.rollback_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_rollback_instance)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.schedule_path
    
    
    schedule_path(project: str, location: str, schedule: str) -> str

Returns a fully-qualified schedule string.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.schedule_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_schedule_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.set_iam_policy](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_set_iam_policy)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.set_instance_accelerator
    
    
    set_instance_accelerator(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.SetInstanceAcceleratorRequest, dict
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

Updates the guest accelerators of a single Instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.set_instance_accelerator](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_set_instance_accelerator)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.set_instance_labels
    
    
    set_instance_labels(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.SetInstanceLabelsRequest, dict
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

Replaces all the labels of an Instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.set_instance_labels](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_set_instance_labels)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.set_instance_machine_type
    
    
    set_instance_machine_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.SetInstanceMachineTypeRequest, dict
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

Updates the machine type of a single Instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.set_instance_machine_type](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_set_instance_machine_type)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.start_instance
    
    
    start_instance(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.StartInstanceRequest, dict]
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

Starts a notebook instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.start_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_start_instance)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.stop_instance
    
    
    stop_instance(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v1.types.service.StopInstanceRequest, dict]
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

Stops a notebook instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.stop_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_stop_instance)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.tensorboard_path
    
    
    tensorboard_path(project: str, location: str, tensorboard: str) -> str

Returns a fully-qualified tensorboard string.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.tensorboard_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_tensorboard_path)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
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
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified IAM permissions against the IAM access control policy for a function.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_test_iam_permissions)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.trigger_schedule
    
    
    trigger_schedule(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.TriggerScheduleRequest, dict
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

Triggers execution of an existing schedule.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.trigger_schedule](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_trigger_schedule)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.update_instance_config
    
    
    update_instance_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.UpdateInstanceConfigRequest, dict
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

Update Notebook Instance configurations.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.update_instance_config](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_update_instance_config)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.update_instance_metadata_items
    
    
    update_instance_metadata_items(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.UpdateInstanceMetadataItemsRequest,
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
    ) -> google.cloud.notebooks_v1.types.service.UpdateInstanceMetadataItemsResponse

Add/update metadata items for an instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.update_instance_metadata_items](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_update_instance_metadata_items)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.update_shielded_instance_config
    
    
    update_shielded_instance_config(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.UpdateShieldedInstanceConfigRequest,
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

Updates the Shielded instance configuration of a single Instance.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.update_shielded_instance_config](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_update_shielded_instance_config)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.upgrade_instance
    
    
    upgrade_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.UpgradeInstanceRequest, dict
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

Upgrades a notebook instance to the latest version.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.upgrade_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_upgrade_instance)

### google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.upgrade_instance_internal
    
    
    upgrade_instance_internal(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1.types.service.UpgradeInstanceInternalRequest, dict
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

Allows notebook instances to call this endpoint to upgrade themselves.

See more: [google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient.upgrade_instance_internal](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1_services_notebook_service_NotebookServiceClient_upgrade_instance_internal)

### google.cloud.notebooks_v1.services.notebook_service.pagers.ListEnvironmentsAsyncPager
    
    
    ListEnvironmentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.notebooks_v1.types.service.ListEnvironmentsResponse
            ],
        ],
        request: google.cloud.notebooks_v1.types.service.ListEnvironmentsRequest,
        response: google.cloud.notebooks_v1.types.service.ListEnvironmentsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.notebooks_v1.services.notebook_service.pagers.ListEnvironmentsAsyncPager](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.pagers.ListEnvironmentsAsyncPager#google_cloud_notebooks_v1_services_notebook_service_pagers_ListEnvironmentsAsyncPager_ListEnvironmentsAsyncPager)

### google.cloud.notebooks_v1.services.notebook_service.pagers.ListEnvironmentsPager
    
    
    ListEnvironmentsPager(
        method: typing.Callable[
            [...], google.cloud.notebooks_v1.types.service.ListEnvironmentsResponse
        ],
        request: google.cloud.notebooks_v1.types.service.ListEnvironmentsRequest,
        response: google.cloud.notebooks_v1.types.service.ListEnvironmentsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.notebooks_v1.services.notebook_service.pagers.ListEnvironmentsPager](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.pagers.ListEnvironmentsPager#google_cloud_notebooks_v1_services_notebook_service_pagers_ListEnvironmentsPager_ListEnvironmentsPager)

### google.cloud.notebooks_v1.services.notebook_service.pagers.ListExecutionsAsyncPager
    
    
    ListExecutionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.notebooks_v1.types.service.ListExecutionsResponse
            ],
        ],
        request: google.cloud.notebooks_v1.types.service.ListExecutionsRequest,
        response: google.cloud.notebooks_v1.types.service.ListExecutionsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.notebooks_v1.services.notebook_service.pagers.ListExecutionsAsyncPager](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.pagers.ListExecutionsAsyncPager#google_cloud_notebooks_v1_services_notebook_service_pagers_ListExecutionsAsyncPager_ListExecutionsAsyncPager)

### google.cloud.notebooks_v1.services.notebook_service.pagers.ListExecutionsPager
    
    
    ListExecutionsPager(
        method: typing.Callable[
            [...], google.cloud.notebooks_v1.types.service.ListExecutionsResponse
        ],
        request: google.cloud.notebooks_v1.types.service.ListExecutionsRequest,
        response: google.cloud.notebooks_v1.types.service.ListExecutionsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.notebooks_v1.services.notebook_service.pagers.ListExecutionsPager](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.pagers.ListExecutionsPager#google_cloud_notebooks_v1_services_notebook_service_pagers_ListExecutionsPager_ListExecutionsPager)

### google.cloud.notebooks_v1.services.notebook_service.pagers.ListInstancesAsyncPager
    
    
    ListInstancesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.notebooks_v1.types.service.ListInstancesResponse],
        ],
        request: google.cloud.notebooks_v1.types.service.ListInstancesRequest,
        response: google.cloud.notebooks_v1.types.service.ListInstancesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.notebooks_v1.services.notebook_service.pagers.ListInstancesAsyncPager](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.pagers.ListInstancesAsyncPager#google_cloud_notebooks_v1_services_notebook_service_pagers_ListInstancesAsyncPager_ListInstancesAsyncPager)

### google.cloud.notebooks_v1.services.notebook_service.pagers.ListInstancesPager
    
    
    ListInstancesPager(
        method: typing.Callable[
            [...], google.cloud.notebooks_v1.types.service.ListInstancesResponse
        ],
        request: google.cloud.notebooks_v1.types.service.ListInstancesRequest,
        response: google.cloud.notebooks_v1.types.service.ListInstancesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.notebooks_v1.services.notebook_service.pagers.ListInstancesPager](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.pagers.ListInstancesPager#google_cloud_notebooks_v1_services_notebook_service_pagers_ListInstancesPager_ListInstancesPager)

### google.cloud.notebooks_v1.services.notebook_service.pagers.ListSchedulesAsyncPager
    
    
    ListSchedulesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.notebooks_v1.types.service.ListSchedulesResponse],
        ],
        request: google.cloud.notebooks_v1.types.service.ListSchedulesRequest,
        response: google.cloud.notebooks_v1.types.service.ListSchedulesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.notebooks_v1.services.notebook_service.pagers.ListSchedulesAsyncPager](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.pagers.ListSchedulesAsyncPager#google_cloud_notebooks_v1_services_notebook_service_pagers_ListSchedulesAsyncPager_ListSchedulesAsyncPager)

### google.cloud.notebooks_v1.services.notebook_service.pagers.ListSchedulesPager
    
    
    ListSchedulesPager(
        method: typing.Callable[
            [...], google.cloud.notebooks_v1.types.service.ListSchedulesResponse
        ],
        request: google.cloud.notebooks_v1.types.service.ListSchedulesRequest,
        response: google.cloud.notebooks_v1.types.service.ListSchedulesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.notebooks_v1.services.notebook_service.pagers.ListSchedulesPager](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1.services.notebook_service.pagers.ListSchedulesPager#google_cloud_notebooks_v1_services_notebook_service_pagers_ListSchedulesPager_ListSchedulesPager)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient
    
    
    NotebookServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.notebooks_v1beta1.services.notebook_service.transports.base.NotebookServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.notebooks_v1beta1.services.notebook_service.transports.base.NotebookServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the notebook service async client.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_NotebookServiceAsyncClient)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_cancel_operation)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_common_billing_account_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_common_folder_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_common_location_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_common_organization_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_common_project_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.create_environment
    
    
    create_environment(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.CreateEnvironmentRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Environment.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.create_environment](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_create_environment)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.create_instance
    
    
    create_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.CreateInstanceRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Instance in a given project and location.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.create_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_create_instance)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.delete_environment
    
    
    delete_environment(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.DeleteEnvironmentRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Deletes a single Environment.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.delete_environment](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_delete_environment)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.delete_instance
    
    
    delete_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.DeleteInstanceRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Deletes a single Instance.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.delete_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_delete_instance)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.delete_operation
    
    
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

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_delete_operation)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.environment_path
    
    
    environment_path(project: str, environment: str) -> str

Returns a fully-qualified environment string.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.environment_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_environment_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_from_service_account_file)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_from_service_account_info)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_from_service_account_json)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.get_environment
    
    
    get_environment(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.GetEnvironmentRequest, dict
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
    ) -> google.cloud.notebooks_v1beta1.types.environment.Environment

Gets details of a single Environment.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.get_environment](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_get_environment)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.get_iam_policy
    
    
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

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_get_iam_policy)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.get_instance
    
    
    get_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.GetInstanceRequest, dict
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
    ) -> google.cloud.notebooks_v1beta1.types.instance.Instance

Gets details of a single Instance.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.get_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_get_instance)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.get_location
    
    
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

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.get_location](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_get_location)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_get_operation)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.notebooks_v1beta1.services.notebook_service.transports.base.NotebookServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_get_transport_class)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.instance_path
    
    
    instance_path(project: str, instance: str) -> str

Returns a fully-qualified instance string.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.instance_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_instance_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.is_instance_upgradeable
    
    
    is_instance_upgradeable(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.IsInstanceUpgradeableRequest,
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
    ) -> google.cloud.notebooks_v1beta1.types.service.IsInstanceUpgradeableResponse

Check if a notebook instance is upgradable.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.is_instance_upgradeable](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_is_instance_upgradeable)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.list_environments
    
    
    list_environments(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.ListEnvironmentsRequest, dict
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
    ) -> (
        google.cloud.notebooks_v1beta1.services.notebook_service.pagers.ListEnvironmentsAsyncPager
    )

Lists environments in a project.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.list_environments](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_list_environments)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.list_instances
    
    
    list_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.ListInstancesRequest, dict
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
    ) -> (
        google.cloud.notebooks_v1beta1.services.notebook_service.pagers.ListInstancesAsyncPager
    )

Lists instances in a given project and location.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.list_instances](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_list_instances)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.list_locations
    
    
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

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_list_locations)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.list_operations
    
    
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

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_list_operations)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_parse_common_folder_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_parse_common_location_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_parse_common_organization_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_parse_common_project_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.parse_environment_path
    
    
    parse_environment_path(path: str) -> typing.Dict[str, str]

Parses a environment path into its component segments.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.parse_environment_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_parse_environment_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.parse_instance_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_parse_instance_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.register_instance
    
    
    register_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.RegisterInstanceRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Registers an existing legacy notebook instance to the Notebooks API server.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.register_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_register_instance)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.report_instance_info
    
    
    report_instance_info(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.ReportInstanceInfoRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Allows notebook instances to report their latest instance information to the Notebooks API server.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.report_instance_info](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_report_instance_info)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.reset_instance
    
    
    reset_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.ResetInstanceRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Resets a notebook instance.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.reset_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_reset_instance)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.set_iam_policy
    
    
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

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_set_iam_policy)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.set_instance_accelerator
    
    
    set_instance_accelerator(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.SetInstanceAcceleratorRequest,
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
    ) -> google.api_core.operation_async.AsyncOperation

Updates the guest accelerators of a single Instance.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.set_instance_accelerator](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_set_instance_accelerator)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.set_instance_labels
    
    
    set_instance_labels(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.SetInstanceLabelsRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Updates the labels of an Instance.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.set_instance_labels](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_set_instance_labels)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.set_instance_machine_type
    
    
    set_instance_machine_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.SetInstanceMachineTypeRequest,
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
    ) -> google.api_core.operation_async.AsyncOperation

Updates the machine type of a single Instance.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.set_instance_machine_type](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_set_instance_machine_type)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.start_instance
    
    
    start_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.StartInstanceRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Starts a notebook instance.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.start_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_start_instance)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.stop_instance
    
    
    stop_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.StopInstanceRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Stops a notebook instance.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.stop_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_stop_instance)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.test_iam_permissions
    
    
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

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_test_iam_permissions)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.upgrade_instance
    
    
    upgrade_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.UpgradeInstanceRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Upgrades a notebook instance to the latest version.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.upgrade_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_upgrade_instance)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.upgrade_instance_internal
    
    
    upgrade_instance_internal(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.UpgradeInstanceInternalRequest,
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
    ) -> google.api_core.operation_async.AsyncOperation

Allows notebook instances to call this endpoint to upgrade themselves.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient.upgrade_instance_internal](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceAsyncClient_upgrade_instance_internal)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient
    
    
    NotebookServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.notebooks_v1beta1.services.notebook_service.transports.base.NotebookServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.notebooks_v1beta1.services.notebook_service.transports.base.NotebookServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the notebook service client.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_NotebookServiceClient)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.**exit**](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient___exit__)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.cancel_operation
    
    
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

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.cancel_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_cancel_operation)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_common_billing_account_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_common_folder_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_common_location_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_common_organization_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_common_project_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.create_environment
    
    
    create_environment(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.CreateEnvironmentRequest, dict
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

Creates a new Environment.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.create_environment](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_create_environment)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.create_instance
    
    
    create_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.CreateInstanceRequest, dict
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

Creates a new Instance in a given project and location.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.create_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_create_instance)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.delete_environment
    
    
    delete_environment(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.DeleteEnvironmentRequest, dict
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

Deletes a single Environment.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.delete_environment](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_delete_environment)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.delete_instance
    
    
    delete_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.DeleteInstanceRequest, dict
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

Deletes a single Instance.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.delete_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_delete_instance)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.delete_operation
    
    
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

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.delete_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_delete_operation)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.environment_path
    
    
    environment_path(project: str, environment: str) -> str

Returns a fully-qualified environment string.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.environment_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_environment_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_from_service_account_file)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_from_service_account_info)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_from_service_account_json)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.get_environment
    
    
    get_environment(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.GetEnvironmentRequest, dict
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
    ) -> google.cloud.notebooks_v1beta1.types.environment.Environment

Gets details of a single Environment.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.get_environment](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_get_environment)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.get_iam_policy](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_get_iam_policy)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.get_instance
    
    
    get_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.GetInstanceRequest, dict
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
    ) -> google.cloud.notebooks_v1beta1.types.instance.Instance

Gets details of a single Instance.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.get_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_get_instance)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.get_location
    
    
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

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.get_location](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_get_location)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.get_operation
    
    
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

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.get_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_get_operation)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.instance_path
    
    
    instance_path(project: str, instance: str) -> str

Returns a fully-qualified instance string.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.instance_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_instance_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.is_instance_upgradeable
    
    
    is_instance_upgradeable(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.IsInstanceUpgradeableRequest,
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
    ) -> google.cloud.notebooks_v1beta1.types.service.IsInstanceUpgradeableResponse

Check if a notebook instance is upgradable.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.is_instance_upgradeable](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_is_instance_upgradeable)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.list_environments
    
    
    list_environments(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.ListEnvironmentsRequest, dict
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
    ) -> (
        google.cloud.notebooks_v1beta1.services.notebook_service.pagers.ListEnvironmentsPager
    )

Lists environments in a project.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.list_environments](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_list_environments)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.list_instances
    
    
    list_instances(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.ListInstancesRequest, dict
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
    ) -> google.cloud.notebooks_v1beta1.services.notebook_service.pagers.ListInstancesPager

Lists instances in a given project and location.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.list_instances](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_list_instances)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.list_locations
    
    
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

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.list_locations](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_list_locations)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.list_operations
    
    
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

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.list_operations](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_list_operations)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_parse_common_billing_account_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_parse_common_folder_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_parse_common_location_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_parse_common_organization_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_parse_common_project_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.parse_environment_path
    
    
    parse_environment_path(path: str) -> typing.Dict[str, str]

Parses a environment path into its component segments.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.parse_environment_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_parse_environment_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.parse_instance_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_parse_instance_path)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.register_instance
    
    
    register_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.RegisterInstanceRequest, dict
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

Registers an existing legacy notebook instance to the Notebooks API server.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.register_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_register_instance)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.report_instance_info
    
    
    report_instance_info(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.ReportInstanceInfoRequest, dict
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

Allows notebook instances to report their latest instance information to the Notebooks API server.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.report_instance_info](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_report_instance_info)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.reset_instance
    
    
    reset_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.ResetInstanceRequest, dict
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

Resets a notebook instance.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.reset_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_reset_instance)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.set_iam_policy](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_set_iam_policy)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.set_instance_accelerator
    
    
    set_instance_accelerator(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.SetInstanceAcceleratorRequest,
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

Updates the guest accelerators of a single Instance.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.set_instance_accelerator](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_set_instance_accelerator)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.set_instance_labels
    
    
    set_instance_labels(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.SetInstanceLabelsRequest, dict
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

Updates the labels of an Instance.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.set_instance_labels](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_set_instance_labels)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.set_instance_machine_type
    
    
    set_instance_machine_type(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.SetInstanceMachineTypeRequest,
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

Updates the machine type of a single Instance.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.set_instance_machine_type](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_set_instance_machine_type)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.start_instance
    
    
    start_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.StartInstanceRequest, dict
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

Starts a notebook instance.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.start_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_start_instance)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.stop_instance
    
    
    stop_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.StopInstanceRequest, dict
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

Stops a notebook instance.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.stop_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_stop_instance)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
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
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified IAM permissions against the IAM access control policy for a function.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_test_iam_permissions)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.upgrade_instance
    
    
    upgrade_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.UpgradeInstanceRequest, dict
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

Upgrades a notebook instance to the latest version.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.upgrade_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_upgrade_instance)

### google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.upgrade_instance_internal
    
    
    upgrade_instance_internal(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v1beta1.types.service.UpgradeInstanceInternalRequest,
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

Allows notebook instances to call this endpoint to upgrade themselves.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient.upgrade_instance_internal](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v1beta1_services_notebook_service_NotebookServiceClient_upgrade_instance_internal)

### google.cloud.notebooks_v1beta1.services.notebook_service.pagers.ListEnvironmentsAsyncPager
    
    
    ListEnvironmentsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.notebooks_v1beta1.types.service.ListEnvironmentsResponse
            ],
        ],
        request: google.cloud.notebooks_v1beta1.types.service.ListEnvironmentsRequest,
        response: google.cloud.notebooks_v1beta1.types.service.ListEnvironmentsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.pagers.ListEnvironmentsAsyncPager](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.pagers.ListEnvironmentsAsyncPager#google_cloud_notebooks_v1beta1_services_notebook_service_pagers_ListEnvironmentsAsyncPager_ListEnvironmentsAsyncPager)

### google.cloud.notebooks_v1beta1.services.notebook_service.pagers.ListEnvironmentsPager
    
    
    ListEnvironmentsPager(
        method: typing.Callable[
            [...], google.cloud.notebooks_v1beta1.types.service.ListEnvironmentsResponse
        ],
        request: google.cloud.notebooks_v1beta1.types.service.ListEnvironmentsRequest,
        response: google.cloud.notebooks_v1beta1.types.service.ListEnvironmentsResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.pagers.ListEnvironmentsPager](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.pagers.ListEnvironmentsPager#google_cloud_notebooks_v1beta1_services_notebook_service_pagers_ListEnvironmentsPager_ListEnvironmentsPager)

### google.cloud.notebooks_v1beta1.services.notebook_service.pagers.ListInstancesAsyncPager
    
    
    ListInstancesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.notebooks_v1beta1.types.service.ListInstancesResponse
            ],
        ],
        request: google.cloud.notebooks_v1beta1.types.service.ListInstancesRequest,
        response: google.cloud.notebooks_v1beta1.types.service.ListInstancesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.pagers.ListInstancesAsyncPager](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.pagers.ListInstancesAsyncPager#google_cloud_notebooks_v1beta1_services_notebook_service_pagers_ListInstancesAsyncPager_ListInstancesAsyncPager)

### google.cloud.notebooks_v1beta1.services.notebook_service.pagers.ListInstancesPager
    
    
    ListInstancesPager(
        method: typing.Callable[
            [...], google.cloud.notebooks_v1beta1.types.service.ListInstancesResponse
        ],
        request: google.cloud.notebooks_v1beta1.types.service.ListInstancesRequest,
        response: google.cloud.notebooks_v1beta1.types.service.ListInstancesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.notebooks_v1beta1.services.notebook_service.pagers.ListInstancesPager](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v1beta1.services.notebook_service.pagers.ListInstancesPager#google_cloud_notebooks_v1beta1_services_notebook_service_pagers_ListInstancesPager_ListInstancesPager)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient
    
    
    NotebookServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.notebooks_v2.services.notebook_service.transports.base.NotebookServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.notebooks_v2.services.notebook_service.transports.base.NotebookServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the notebook service async client.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_NotebookServiceAsyncClient)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_cancel_operation)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.check_instance_upgradability
    
    
    check_instance_upgradability(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v2.types.service.CheckInstanceUpgradabilityRequest,
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
    ) -> google.cloud.notebooks_v2.types.service.CheckInstanceUpgradabilityResponse

Checks whether a notebook instance is upgradable.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.check_instance_upgradability](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_check_instance_upgradability)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_common_billing_account_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_common_folder_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_common_location_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_common_organization_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_common_project_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.create_instance
    
    
    create_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v2.types.service.CreateInstanceRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        instance: typing.Optional[google.cloud.notebooks_v2.types.instance.Instance] = None,
        instance_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a new Instance in a given project and location.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.create_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_create_instance)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.delete_instance
    
    
    delete_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v2.types.service.DeleteInstanceRequest, dict
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

Deletes a single Instance.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.delete_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_delete_instance)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.delete_operation
    
    
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

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_delete_operation)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.diagnose_instance
    
    
    diagnose_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v2.types.service.DiagnoseInstanceRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        diagnostic_config: typing.Optional[
            google.cloud.notebooks_v2.types.diagnostic_config.DiagnosticConfig
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

Creates a Diagnostic File and runs Diagnostic Tool given an Instance.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.diagnose_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_diagnose_instance)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_from_service_account_file)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_from_service_account_info)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_from_service_account_json)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.get_iam_policy
    
    
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

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_get_iam_policy)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.get_instance
    
    
    get_instance(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v2.types.service.GetInstanceRequest, dict]
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
    ) -> google.cloud.notebooks_v2.types.instance.Instance

Gets details of a single Instance.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.get_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_get_instance)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.get_location
    
    
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

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.get_location](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_get_location)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_get_operation)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.notebooks_v2.services.notebook_service.transports.base.NotebookServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_get_transport_class)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.instance_path
    
    
    instance_path(project: str, location: str, instance: str) -> str

Returns a fully-qualified instance string.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.instance_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_instance_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.list_instances
    
    
    list_instances(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v2.types.service.ListInstancesRequest, dict]
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
    ) -> google.cloud.notebooks_v2.services.notebook_service.pagers.ListInstancesAsyncPager

Lists instances in a given project and location.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.list_instances](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_list_instances)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.list_locations
    
    
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

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_list_locations)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.list_operations
    
    
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

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_list_operations)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_parse_common_folder_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_parse_common_location_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_parse_common_organization_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_parse_common_project_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.parse_instance_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_parse_instance_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.reset_instance
    
    
    reset_instance(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v2.types.service.ResetInstanceRequest, dict]
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

Resets a notebook instance.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.reset_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_reset_instance)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.rollback_instance
    
    
    rollback_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v2.types.service.RollbackInstanceRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Rollbacks a notebook instance to the previous version.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.rollback_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_rollback_instance)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.set_iam_policy
    
    
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

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_set_iam_policy)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.start_instance
    
    
    start_instance(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v2.types.service.StartInstanceRequest, dict]
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

Starts a notebook instance.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.start_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_start_instance)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.stop_instance
    
    
    stop_instance(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v2.types.service.StopInstanceRequest, dict]
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

Stops a notebook instance.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.stop_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_stop_instance)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.test_iam_permissions
    
    
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

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_test_iam_permissions)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.update_instance
    
    
    update_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v2.types.service.UpdateInstanceRequest, dict
            ]
        ] = None,
        *,
        instance: typing.Optional[google.cloud.notebooks_v2.types.instance.Instance] = None,
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

UpdateInstance updates an Instance.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.update_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_update_instance)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.upgrade_instance
    
    
    upgrade_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v2.types.service.UpgradeInstanceRequest, dict
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
    ) -> google.api_core.operation_async.AsyncOperation

Upgrades a notebook instance to the latest version.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient.upgrade_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceAsyncClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceAsyncClient_upgrade_instance)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient
    
    
    NotebookServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.notebooks_v2.services.notebook_service.transports.base.NotebookServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.notebooks_v2.services.notebook_service.transports.base.NotebookServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the notebook service client.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_NotebookServiceClient)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.**exit**](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient___exit__)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.cancel_operation
    
    
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

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.cancel_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_cancel_operation)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.check_instance_upgradability
    
    
    check_instance_upgradability(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v2.types.service.CheckInstanceUpgradabilityRequest,
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
    ) -> google.cloud.notebooks_v2.types.service.CheckInstanceUpgradabilityResponse

Checks whether a notebook instance is upgradable.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.check_instance_upgradability](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_check_instance_upgradability)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_common_billing_account_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_common_folder_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_common_location_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_common_organization_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_common_project_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.create_instance
    
    
    create_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v2.types.service.CreateInstanceRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        instance: typing.Optional[google.cloud.notebooks_v2.types.instance.Instance] = None,
        instance_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a new Instance in a given project and location.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.create_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_create_instance)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.delete_instance
    
    
    delete_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v2.types.service.DeleteInstanceRequest, dict
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

Deletes a single Instance.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.delete_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_delete_instance)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.delete_operation
    
    
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

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.delete_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_delete_operation)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.diagnose_instance
    
    
    diagnose_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v2.types.service.DiagnoseInstanceRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        diagnostic_config: typing.Optional[
            google.cloud.notebooks_v2.types.diagnostic_config.DiagnosticConfig
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a Diagnostic File and runs Diagnostic Tool given an Instance.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.diagnose_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_diagnose_instance)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_from_service_account_file)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_from_service_account_info)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_from_service_account_json)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Gets the IAM access control policy for a function.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.get_iam_policy](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_get_iam_policy)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.get_instance
    
    
    get_instance(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v2.types.service.GetInstanceRequest, dict]
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
    ) -> google.cloud.notebooks_v2.types.instance.Instance

Gets details of a single Instance.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.get_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_get_instance)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.get_location
    
    
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

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.get_location](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_get_location)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.get_operation
    
    
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

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.get_operation](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_get_operation)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.instance_path
    
    
    instance_path(project: str, location: str, instance: str) -> str

Returns a fully-qualified instance string.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.instance_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_instance_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.list_instances
    
    
    list_instances(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v2.types.service.ListInstancesRequest, dict]
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
    ) -> google.cloud.notebooks_v2.services.notebook_service.pagers.ListInstancesPager

Lists instances in a given project and location.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.list_instances](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_list_instances)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.list_locations
    
    
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

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.list_locations](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_list_locations)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.list_operations
    
    
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

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.list_operations](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_list_operations)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_parse_common_billing_account_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_parse_common_folder_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_parse_common_location_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_parse_common_organization_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_parse_common_project_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.parse_instance_path
    
    
    parse_instance_path(path: str) -> typing.Dict[str, str]

Parses a instance path into its component segments.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.parse_instance_path](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_parse_instance_path)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.reset_instance
    
    
    reset_instance(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v2.types.service.ResetInstanceRequest, dict]
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

Resets a notebook instance.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.reset_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_reset_instance)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.rollback_instance
    
    
    rollback_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v2.types.service.RollbackInstanceRequest, dict
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

Rollbacks a notebook instance to the previous version.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.rollback_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_rollback_instance)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
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
    ) -> google.iam.v1.policy_pb2.Policy

Sets the IAM access control policy on the specified function.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.set_iam_policy](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_set_iam_policy)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.start_instance
    
    
    start_instance(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v2.types.service.StartInstanceRequest, dict]
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

Starts a notebook instance.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.start_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_start_instance)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.stop_instance
    
    
    stop_instance(
        request: typing.Optional[
            typing.Union[google.cloud.notebooks_v2.types.service.StopInstanceRequest, dict]
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

Stops a notebook instance.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.stop_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_stop_instance)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
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
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the specified IAM permissions against the IAM access control policy for a function.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_test_iam_permissions)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.update_instance
    
    
    update_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v2.types.service.UpdateInstanceRequest, dict
            ]
        ] = None,
        *,
        instance: typing.Optional[google.cloud.notebooks_v2.types.instance.Instance] = None,
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

UpdateInstance updates an Instance.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.update_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_update_instance)

### google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.upgrade_instance
    
    
    upgrade_instance(
        request: typing.Optional[
            typing.Union[
                google.cloud.notebooks_v2.types.service.UpgradeInstanceRequest, dict
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

Upgrades a notebook instance to the latest version.

See more: [google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient.upgrade_instance](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.NotebookServiceClient#google_cloud_notebooks_v2_services_notebook_service_NotebookServiceClient_upgrade_instance)

### google.cloud.notebooks_v2.services.notebook_service.pagers.ListInstancesAsyncPager
    
    
    ListInstancesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.notebooks_v2.types.service.ListInstancesResponse],
        ],
        request: google.cloud.notebooks_v2.types.service.ListInstancesRequest,
        response: google.cloud.notebooks_v2.types.service.ListInstancesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiates the pager.

See more: [google.cloud.notebooks_v2.services.notebook_service.pagers.ListInstancesAsyncPager](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.pagers.ListInstancesAsyncPager#google_cloud_notebooks_v2_services_notebook_service_pagers_ListInstancesAsyncPager_ListInstancesAsyncPager)

### google.cloud.notebooks_v2.services.notebook_service.pagers.ListInstancesPager
    
    
    ListInstancesPager(
        method: typing.Callable[
            [...], google.cloud.notebooks_v2.types.service.ListInstancesResponse
        ],
        request: google.cloud.notebooks_v2.types.service.ListInstancesRequest,
        response: google.cloud.notebooks_v2.types.service.ListInstancesResponse,
        *,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    )

Instantiate the pager.

See more: [google.cloud.notebooks_v2.services.notebook_service.pagers.ListInstancesPager](https://cloud.google.com/python/docs/reference/notebooks/latest/google.cloud.notebooks_v2.services.notebook_service.pagers.ListInstancesPager#google_cloud_notebooks_v2_services_notebook_service_pagers_ListInstancesPager_ListInstancesPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
