---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/summary_method/
title: Package Methods (0.4.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:31:20.525539+00:00
---

# Package Methods (0.4.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (0.4.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.2 (latest)  0.4.1  0.3.0  0.2.0  0.1.1 

Summary of entries of Methods for google-cloud-maintenance-api.

## 

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient
    
    
    MaintenanceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.maintenance_api_v1.services.maintenance.transports.base.MaintenanceTransport,
                typing.Callable[
                    [...],
                    google.cloud.maintenance_api_v1.services.maintenance.transports.base.MaintenanceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the maintenance async client.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_MaintenanceAsyncClient)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_common_billing_account_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_common_folder_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_common_location_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_common_organization_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_common_project_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_from_service_account_file)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_from_service_account_info)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_from_service_account_json)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.get_location
    
    
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

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_get_location)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.get_resource_maintenance
    
    
    get_resource_maintenance(
        request: typing.Optional[
            typing.Union[
                google.cloud.maintenance_api_v1.types.maintenance_service.GetResourceMaintenanceRequest,
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
    ) -> google.cloud.maintenance_api_v1.types.maintenance_service.ResourceMaintenance

Retrieve a single resource maintenance.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.get_resource_maintenance](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_get_resource_maintenance)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.maintenance_api_v1.services.maintenance.transports.base.MaintenanceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_get_transport_class)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.list_locations
    
    
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

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_list_locations)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.list_resource_maintenances
    
    
    list_resource_maintenances(
        request: typing.Optional[
            typing.Union[
                google.cloud.maintenance_api_v1.types.maintenance_service.ListResourceMaintenancesRequest,
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
        google.cloud.maintenance_api_v1.services.maintenance.pagers.ListResourceMaintenancesAsyncPager
    )

Retrieve a collection of resource maintenances.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.list_resource_maintenances](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_list_resource_maintenances)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_parse_common_billing_account_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_parse_common_folder_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_parse_common_location_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_parse_common_organization_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_parse_common_project_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.parse_resource_maintenance_path
    
    
    parse_resource_maintenance_path(path: str) -> typing.Dict[str, str]

Parses a resource_maintenance path into its component segments.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.parse_resource_maintenance_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_parse_resource_maintenance_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.resource_maintenance_path
    
    
    resource_maintenance_path(
        project: str, location: str, resource_maintenance: str
    ) -> str

Returns a fully-qualified resource_maintenance string.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.resource_maintenance_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_resource_maintenance_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.summarize_maintenances
    
    
    summarize_maintenances(
        request: typing.Optional[
            typing.Union[
                google.cloud.maintenance_api_v1.types.maintenance_service.SummarizeMaintenancesRequest,
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
        google.cloud.maintenance_api_v1.services.maintenance.pagers.SummarizeMaintenancesAsyncPager
    )

Retrieves the statistics of a specific maintenance.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient.summarize_maintenances](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceAsyncClient_summarize_maintenances)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient
    
    
    MaintenanceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.maintenance_api_v1.services.maintenance.transports.base.MaintenanceTransport,
                typing.Callable[
                    [...],
                    google.cloud.maintenance_api_v1.services.maintenance.transports.base.MaintenanceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the maintenance client.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_MaintenanceClient)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient___exit__)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_common_billing_account_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_common_folder_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_common_location_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_common_organization_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_common_project_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_from_service_account_file)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_from_service_account_info)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_from_service_account_json)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.get_location
    
    
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

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_get_location)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.get_resource_maintenance
    
    
    get_resource_maintenance(
        request: typing.Optional[
            typing.Union[
                google.cloud.maintenance_api_v1.types.maintenance_service.GetResourceMaintenanceRequest,
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
    ) -> google.cloud.maintenance_api_v1.types.maintenance_service.ResourceMaintenance

Retrieve a single resource maintenance.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.get_resource_maintenance](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_get_resource_maintenance)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.list_locations
    
    
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

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_list_locations)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.list_resource_maintenances
    
    
    list_resource_maintenances(
        request: typing.Optional[
            typing.Union[
                google.cloud.maintenance_api_v1.types.maintenance_service.ListResourceMaintenancesRequest,
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
        google.cloud.maintenance_api_v1.services.maintenance.pagers.ListResourceMaintenancesPager
    )

Retrieve a collection of resource maintenances.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.list_resource_maintenances](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_list_resource_maintenances)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_parse_common_billing_account_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_parse_common_folder_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_parse_common_location_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_parse_common_organization_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_parse_common_project_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.parse_resource_maintenance_path
    
    
    parse_resource_maintenance_path(path: str) -> typing.Dict[str, str]

Parses a resource_maintenance path into its component segments.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.parse_resource_maintenance_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_parse_resource_maintenance_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.resource_maintenance_path
    
    
    resource_maintenance_path(
        project: str, location: str, resource_maintenance: str
    ) -> str

Returns a fully-qualified resource_maintenance string.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.resource_maintenance_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_resource_maintenance_path)

### google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.summarize_maintenances
    
    
    summarize_maintenances(
        request: typing.Optional[
            typing.Union[
                google.cloud.maintenance_api_v1.types.maintenance_service.SummarizeMaintenancesRequest,
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
        google.cloud.maintenance_api_v1.services.maintenance.pagers.SummarizeMaintenancesPager
    )

Retrieves the statistics of a specific maintenance.

See more: [google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient.summarize_maintenances](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1_services_maintenance_MaintenanceClient_summarize_maintenances)

### google.cloud.maintenance_api_v1.services.maintenance.pagers.ListResourceMaintenancesAsyncPager
    
    
    ListResourceMaintenancesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.maintenance_api_v1.types.maintenance_service.ListResourceMaintenancesResponse
            ],
        ],
        request: google.cloud.maintenance_api_v1.types.maintenance_service.ListResourceMaintenancesRequest,
        response: google.cloud.maintenance_api_v1.types.maintenance_service.ListResourceMaintenancesResponse,
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

See more: [google.cloud.maintenance_api_v1.services.maintenance.pagers.ListResourceMaintenancesAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.pagers.ListResourceMaintenancesAsyncPager#google_cloud_maintenance_api_v1_services_maintenance_pagers_ListResourceMaintenancesAsyncPager_ListResourceMaintenancesAsyncPager)

### google.cloud.maintenance_api_v1.services.maintenance.pagers.ListResourceMaintenancesPager
    
    
    ListResourceMaintenancesPager(
        method: typing.Callable[
            [...],
            google.cloud.maintenance_api_v1.types.maintenance_service.ListResourceMaintenancesResponse,
        ],
        request: google.cloud.maintenance_api_v1.types.maintenance_service.ListResourceMaintenancesRequest,
        response: google.cloud.maintenance_api_v1.types.maintenance_service.ListResourceMaintenancesResponse,
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

See more: [google.cloud.maintenance_api_v1.services.maintenance.pagers.ListResourceMaintenancesPager](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.pagers.ListResourceMaintenancesPager#google_cloud_maintenance_api_v1_services_maintenance_pagers_ListResourceMaintenancesPager_ListResourceMaintenancesPager)

### google.cloud.maintenance_api_v1.services.maintenance.pagers.SummarizeMaintenancesAsyncPager
    
    
    SummarizeMaintenancesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.maintenance_api_v1.types.maintenance_service.SummarizeMaintenancesResponse
            ],
        ],
        request: google.cloud.maintenance_api_v1.types.maintenance_service.SummarizeMaintenancesRequest,
        response: google.cloud.maintenance_api_v1.types.maintenance_service.SummarizeMaintenancesResponse,
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

See more: [google.cloud.maintenance_api_v1.services.maintenance.pagers.SummarizeMaintenancesAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.pagers.SummarizeMaintenancesAsyncPager#google_cloud_maintenance_api_v1_services_maintenance_pagers_SummarizeMaintenancesAsyncPager_SummarizeMaintenancesAsyncPager)

### google.cloud.maintenance_api_v1.services.maintenance.pagers.SummarizeMaintenancesPager
    
    
    SummarizeMaintenancesPager(
        method: typing.Callable[
            [...],
            google.cloud.maintenance_api_v1.types.maintenance_service.SummarizeMaintenancesResponse,
        ],
        request: google.cloud.maintenance_api_v1.types.maintenance_service.SummarizeMaintenancesRequest,
        response: google.cloud.maintenance_api_v1.types.maintenance_service.SummarizeMaintenancesResponse,
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

See more: [google.cloud.maintenance_api_v1.services.maintenance.pagers.SummarizeMaintenancesPager](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1.services.maintenance.pagers.SummarizeMaintenancesPager#google_cloud_maintenance_api_v1_services_maintenance_pagers_SummarizeMaintenancesPager_SummarizeMaintenancesPager)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient
    
    
    MaintenanceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.maintenance_api_v1beta.services.maintenance.transports.base.MaintenanceTransport,
                typing.Callable[
                    [...],
                    google.cloud.maintenance_api_v1beta.services.maintenance.transports.base.MaintenanceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the maintenance async client.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_MaintenanceAsyncClient)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_common_billing_account_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_common_folder_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_common_location_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_common_organization_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_common_project_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_from_service_account_file)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_from_service_account_info)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_from_service_account_json)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.get_location
    
    
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

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_get_location)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.get_resource_maintenance
    
    
    get_resource_maintenance(
        request: typing.Optional[
            typing.Union[
                google.cloud.maintenance_api_v1beta.types.maintenance_service.GetResourceMaintenanceRequest,
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
    ) -> google.cloud.maintenance_api_v1beta.types.maintenance_service.ResourceMaintenance

Retrieve a single resource maintenance.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.get_resource_maintenance](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_get_resource_maintenance)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.maintenance_api_v1beta.services.maintenance.transports.base.MaintenanceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_get_transport_class)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.list_locations
    
    
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

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_list_locations)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.list_resource_maintenances
    
    
    list_resource_maintenances(
        request: typing.Optional[
            typing.Union[
                google.cloud.maintenance_api_v1beta.types.maintenance_service.ListResourceMaintenancesRequest,
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
        google.cloud.maintenance_api_v1beta.services.maintenance.pagers.ListResourceMaintenancesAsyncPager
    )

Retrieve a collection of resource maintenances.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.list_resource_maintenances](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_list_resource_maintenances)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_parse_common_billing_account_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_parse_common_folder_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_parse_common_location_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_parse_common_organization_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_parse_common_project_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.parse_resource_maintenance_path
    
    
    parse_resource_maintenance_path(path: str) -> typing.Dict[str, str]

Parses a resource_maintenance path into its component segments.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.parse_resource_maintenance_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_parse_resource_maintenance_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.resource_maintenance_path
    
    
    resource_maintenance_path(
        project: str, location: str, resource_maintenance: str
    ) -> str

Returns a fully-qualified resource_maintenance string.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.resource_maintenance_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_resource_maintenance_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.summarize_maintenances
    
    
    summarize_maintenances(
        request: typing.Optional[
            typing.Union[
                google.cloud.maintenance_api_v1beta.types.maintenance_service.SummarizeMaintenancesRequest,
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
        google.cloud.maintenance_api_v1beta.services.maintenance.pagers.SummarizeMaintenancesAsyncPager
    )

Retrieves the statistics of a specific maintenance.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient.summarize_maintenances](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceAsyncClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceAsyncClient_summarize_maintenances)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient
    
    
    MaintenanceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.maintenance_api_v1beta.services.maintenance.transports.base.MaintenanceTransport,
                typing.Callable[
                    [...],
                    google.cloud.maintenance_api_v1beta.services.maintenance.transports.base.MaintenanceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the maintenance client.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_MaintenanceClient)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.**exit**](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient___exit__)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_common_billing_account_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_common_folder_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_common_location_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_common_organization_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_common_project_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_from_service_account_file)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_from_service_account_info)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_from_service_account_json)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.get_location
    
    
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

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.get_location](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_get_location)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.get_resource_maintenance
    
    
    get_resource_maintenance(
        request: typing.Optional[
            typing.Union[
                google.cloud.maintenance_api_v1beta.types.maintenance_service.GetResourceMaintenanceRequest,
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
    ) -> google.cloud.maintenance_api_v1beta.types.maintenance_service.ResourceMaintenance

Retrieve a single resource maintenance.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.get_resource_maintenance](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_get_resource_maintenance)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.list_locations
    
    
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

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.list_locations](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_list_locations)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.list_resource_maintenances
    
    
    list_resource_maintenances(
        request: typing.Optional[
            typing.Union[
                google.cloud.maintenance_api_v1beta.types.maintenance_service.ListResourceMaintenancesRequest,
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
        google.cloud.maintenance_api_v1beta.services.maintenance.pagers.ListResourceMaintenancesPager
    )

Retrieve a collection of resource maintenances.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.list_resource_maintenances](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_list_resource_maintenances)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_parse_common_billing_account_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_parse_common_folder_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_parse_common_location_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_parse_common_organization_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_parse_common_project_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.parse_resource_maintenance_path
    
    
    parse_resource_maintenance_path(path: str) -> typing.Dict[str, str]

Parses a resource_maintenance path into its component segments.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.parse_resource_maintenance_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_parse_resource_maintenance_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.resource_maintenance_path
    
    
    resource_maintenance_path(
        project: str, location: str, resource_maintenance: str
    ) -> str

Returns a fully-qualified resource_maintenance string.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.resource_maintenance_path](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_resource_maintenance_path)

### google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.summarize_maintenances
    
    
    summarize_maintenances(
        request: typing.Optional[
            typing.Union[
                google.cloud.maintenance_api_v1beta.types.maintenance_service.SummarizeMaintenancesRequest,
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
        google.cloud.maintenance_api_v1beta.services.maintenance.pagers.SummarizeMaintenancesPager
    )

Retrieves the statistics of a specific maintenance.

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient.summarize_maintenances](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.MaintenanceClient#google_cloud_maintenance_api_v1beta_services_maintenance_MaintenanceClient_summarize_maintenances)

### google.cloud.maintenance_api_v1beta.services.maintenance.pagers.ListResourceMaintenancesAsyncPager
    
    
    ListResourceMaintenancesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.maintenance_api_v1beta.types.maintenance_service.ListResourceMaintenancesResponse
            ],
        ],
        request: google.cloud.maintenance_api_v1beta.types.maintenance_service.ListResourceMaintenancesRequest,
        response: google.cloud.maintenance_api_v1beta.types.maintenance_service.ListResourceMaintenancesResponse,
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

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.pagers.ListResourceMaintenancesAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.pagers.ListResourceMaintenancesAsyncPager#google_cloud_maintenance_api_v1beta_services_maintenance_pagers_ListResourceMaintenancesAsyncPager_ListResourceMaintenancesAsyncPager)

### google.cloud.maintenance_api_v1beta.services.maintenance.pagers.ListResourceMaintenancesPager
    
    
    ListResourceMaintenancesPager(
        method: typing.Callable[
            [...],
            google.cloud.maintenance_api_v1beta.types.maintenance_service.ListResourceMaintenancesResponse,
        ],
        request: google.cloud.maintenance_api_v1beta.types.maintenance_service.ListResourceMaintenancesRequest,
        response: google.cloud.maintenance_api_v1beta.types.maintenance_service.ListResourceMaintenancesResponse,
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

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.pagers.ListResourceMaintenancesPager](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.pagers.ListResourceMaintenancesPager#google_cloud_maintenance_api_v1beta_services_maintenance_pagers_ListResourceMaintenancesPager_ListResourceMaintenancesPager)

### google.cloud.maintenance_api_v1beta.services.maintenance.pagers.SummarizeMaintenancesAsyncPager
    
    
    SummarizeMaintenancesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.maintenance_api_v1beta.types.maintenance_service.SummarizeMaintenancesResponse
            ],
        ],
        request: google.cloud.maintenance_api_v1beta.types.maintenance_service.SummarizeMaintenancesRequest,
        response: google.cloud.maintenance_api_v1beta.types.maintenance_service.SummarizeMaintenancesResponse,
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

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.pagers.SummarizeMaintenancesAsyncPager](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.pagers.SummarizeMaintenancesAsyncPager#google_cloud_maintenance_api_v1beta_services_maintenance_pagers_SummarizeMaintenancesAsyncPager_SummarizeMaintenancesAsyncPager)

### google.cloud.maintenance_api_v1beta.services.maintenance.pagers.SummarizeMaintenancesPager
    
    
    SummarizeMaintenancesPager(
        method: typing.Callable[
            [...],
            google.cloud.maintenance_api_v1beta.types.maintenance_service.SummarizeMaintenancesResponse,
        ],
        request: google.cloud.maintenance_api_v1beta.types.maintenance_service.SummarizeMaintenancesRequest,
        response: google.cloud.maintenance_api_v1beta.types.maintenance_service.SummarizeMaintenancesResponse,
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

See more: [google.cloud.maintenance_api_v1beta.services.maintenance.pagers.SummarizeMaintenancesPager](https://cloud.google.com/python/docs/reference/google-cloud-maintenance-api/latest/google.cloud.maintenance_api_v1beta.services.maintenance.pagers.SummarizeMaintenancesPager#google_cloud_maintenance_api_v1beta_services_maintenance_pagers_SummarizeMaintenancesPager_SummarizeMaintenancesPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
