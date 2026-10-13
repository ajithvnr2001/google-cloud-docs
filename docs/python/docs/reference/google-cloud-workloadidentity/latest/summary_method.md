---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/summary_method/
title: Package Methods (0.1.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:27:29.936268+00:00
---

# Package Methods (0.1.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (0.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

Summary of entries of Methods for google-cloud-workloadidentity.

## 

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient
    
    
    WorkloadIdentityAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.workloadidentity_v1.services.workload_identity.transports.base.WorkloadIdentityTransport,
                typing.Callable[
                    [...],
                    google.cloud.workloadidentity_v1.services.workload_identity.transports.base.WorkloadIdentityTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the workload identity async client.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_WorkloadIdentityAsyncClient)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.cancel_operation
    
    
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

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_cancel_operation)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_common_billing_account_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_common_folder_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_common_location_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_common_organization_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_common_project_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.delete_operation
    
    
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

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_delete_operation)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_from_service_account_file)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_from_service_account_info)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_from_service_account_json)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.generate_service_agents
    
    
    generate_service_agents(
        request: typing.Optional[
            typing.Union[
                google.cloud.workloadidentity_v1.types.service.GenerateServiceAgentsRequest,
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
    ) -> google.api_core.operation_async.AsyncOperation

Creates all service agents for a given resource, location and service producer.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.generate_service_agents](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_generate_service_agents)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.get_location
    
    
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

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_get_location)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.get_operation
    
    
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

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_get_operation)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.workloadidentity_v1.services.workload_identity.transports.base.WorkloadIdentityTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_get_transport_class)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.list_locations
    
    
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

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_list_locations)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.list_operations
    
    
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

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_list_operations)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_parse_common_billing_account_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_parse_common_folder_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_parse_common_location_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_parse_common_organization_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_parse_common_project_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.parse_service_agent_path
    
    
    parse_service_agent_path(path: str) -> typing.Dict[str, str]

Parses a service_agent path into its component segments.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.parse_service_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_parse_service_agent_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.parse_service_producer_path
    
    
    parse_service_producer_path(path: str) -> typing.Dict[str, str]

Parses a service_producer path into its component segments.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.parse_service_producer_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_parse_service_producer_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.service_agent_path
    
    
    service_agent_path(
        project: str, location: str, service_producer: str, service_agent: str
    ) -> str

Returns a fully-qualified service_agent string.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.service_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_service_agent_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.service_producer_path
    
    
    service_producer_path(project: str, location: str, service_producer: str) -> str

Returns a fully-qualified service_producer string.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient.service_producer_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityAsyncClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityAsyncClient_service_producer_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient
    
    
    WorkloadIdentityClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.workloadidentity_v1.services.workload_identity.transports.base.WorkloadIdentityTransport,
                typing.Callable[
                    [...],
                    google.cloud.workloadidentity_v1.services.workload_identity.transports.base.WorkloadIdentityTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the workload identity client.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_WorkloadIdentityClient)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient___exit__)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.cancel_operation
    
    
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

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.cancel_operation](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_cancel_operation)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_common_billing_account_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_common_folder_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_common_location_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_common_organization_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_common_project_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.delete_operation
    
    
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

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.delete_operation](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_delete_operation)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_from_service_account_file)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_from_service_account_info)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_from_service_account_json)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.generate_service_agents
    
    
    generate_service_agents(
        request: typing.Optional[
            typing.Union[
                google.cloud.workloadidentity_v1.types.service.GenerateServiceAgentsRequest,
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
    ) -> google.api_core.operation.Operation

Creates all service agents for a given resource, location and service producer.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.generate_service_agents](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_generate_service_agents)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.get_location
    
    
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

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_get_location)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_get_mtls_endpoint_and_cert_source)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.get_operation
    
    
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

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.get_operation](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_get_operation)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.list_locations
    
    
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

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_list_locations)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.list_operations
    
    
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

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.list_operations](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_list_operations)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_parse_common_billing_account_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_parse_common_folder_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_parse_common_location_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_parse_common_organization_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_parse_common_project_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.parse_service_agent_path
    
    
    parse_service_agent_path(path: str) -> typing.Dict[str, str]

Parses a service_agent path into its component segments.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.parse_service_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_parse_service_agent_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.parse_service_producer_path
    
    
    parse_service_producer_path(path: str) -> typing.Dict[str, str]

Parses a service_producer path into its component segments.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.parse_service_producer_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_parse_service_producer_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.service_agent_path
    
    
    service_agent_path(
        project: str, location: str, service_producer: str, service_agent: str
    ) -> str

Returns a fully-qualified service_agent string.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.service_agent_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_service_agent_path)

### google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.service_producer_path
    
    
    service_producer_path(project: str, location: str, service_producer: str) -> str

Returns a fully-qualified service_producer string.

See more: [google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient.service_producer_path](https://cloud.google.com/python/docs/reference/google-cloud-workloadidentity/latest/google.cloud.workloadidentity_v1.services.workload_identity.WorkloadIdentityClient#google_cloud_workloadidentity_v1_services_workload_identity_WorkloadIdentityClient_service_producer_path)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-13 UTC."],[],[]] 
