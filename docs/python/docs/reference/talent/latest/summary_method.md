---
url: https://docs.cloud.google.com/python/docs/reference/talent/latest/summary_method/
title: Package Methods (2.22.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:08.444618+00:00
---

# Package Methods (2.22.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/talent/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (2.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.22.0 (latest)  2.21.0  2.20.0  2.19.0  2.18.0  2.17.2  2.16.0  2.15.0  2.14.1  2.13.5  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.0  2.5.2  2.4.0  2.3.0  2.2.1  2.1.0  2.0.0  1.0.2  0.6.3  0.5.0  0.4.0  0.3.0 

Summary of entries of Methods for talent.

## 

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient
    
    
    CompanyServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.talent_v4.services.company_service.transports.base.CompanyServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.talent_v4.services.company_service.transports.base.CompanyServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the company service async client.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_CompanyServiceAsyncClient)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_common_billing_account_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_common_folder_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_common_location_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_common_organization_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_common_project_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.company_path
    
    
    company_path(project: str, tenant: str, company: str) -> str

Returns a fully-qualified company string.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_company_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.create_company
    
    
    create_company(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.company_service.CreateCompanyRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        company: typing.Optional[google.cloud.talent_v4.types.company.Company] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4.types.company.Company

Creates a new company entity.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.create_company](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_create_company)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.delete_company
    
    
    delete_company(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.company_service.DeleteCompanyRequest, dict
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

Deletes specified company.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.delete_company](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_delete_company)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_from_service_account_file)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_from_service_account_info)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_from_service_account_json)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.get_company
    
    
    get_company(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.company_service.GetCompanyRequest, dict
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
    ) -> google.cloud.talent_v4.types.company.Company

Retrieves specified company.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.get_company](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_get_company)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_get_operation)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.talent_v4.services.company_service.transports.base.CompanyServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_get_transport_class)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.list_companies
    
    
    list_companies(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.company_service.ListCompaniesRequest, dict
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
    ) -> google.cloud.talent_v4.services.company_service.pagers.ListCompaniesAsyncPager

Lists all companies associated with the project.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.list_companies](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_list_companies)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_parse_common_folder_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_parse_common_location_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_parse_common_organization_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_parse_common_project_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.parse_company_path
    
    
    parse_company_path(path: str) -> typing.Dict[str, str]

Parses a company path into its component segments.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.parse_company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_parse_company_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.parse_tenant_path
    
    
    parse_tenant_path(path: str) -> typing.Dict[str, str]

Parses a tenant path into its component segments.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.parse_tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_parse_tenant_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.tenant_path
    
    
    tenant_path(project: str, tenant: str) -> str

Returns a fully-qualified tenant string.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_tenant_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.update_company
    
    
    update_company(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.company_service.UpdateCompanyRequest, dict
            ]
        ] = None,
        *,
        company: typing.Optional[google.cloud.talent_v4.types.company.Company] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4.types.company.Company

Updates specified company.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.update_company](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_update_company)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient
    
    
    CompanyServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.talent_v4.services.company_service.transports.base.CompanyServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.talent_v4.services.company_service.transports.base.CompanyServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the company service client.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_CompanyServiceClient)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.**exit**](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient___exit__)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_common_billing_account_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_common_folder_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_common_location_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_common_organization_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_common_project_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.company_path
    
    
    company_path(project: str, tenant: str, company: str) -> str

Returns a fully-qualified company string.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_company_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.create_company
    
    
    create_company(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.company_service.CreateCompanyRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        company: typing.Optional[google.cloud.talent_v4.types.company.Company] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4.types.company.Company

Creates a new company entity.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.create_company](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_create_company)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.delete_company
    
    
    delete_company(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.company_service.DeleteCompanyRequest, dict
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

Deletes specified company.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.delete_company](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_delete_company)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_from_service_account_file)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_from_service_account_info)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_from_service_account_json)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.get_company
    
    
    get_company(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.company_service.GetCompanyRequest, dict
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
    ) -> google.cloud.talent_v4.types.company.Company

Retrieves specified company.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.get_company](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_get_company)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.get_operation
    
    
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

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.get_operation](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_get_operation)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.list_companies
    
    
    list_companies(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.company_service.ListCompaniesRequest, dict
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
    ) -> google.cloud.talent_v4.services.company_service.pagers.ListCompaniesPager

Lists all companies associated with the project.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.list_companies](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_list_companies)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_parse_common_billing_account_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_parse_common_folder_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_parse_common_location_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_parse_common_organization_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_parse_common_project_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.parse_company_path
    
    
    parse_company_path(path: str) -> typing.Dict[str, str]

Parses a company path into its component segments.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.parse_company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_parse_company_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.parse_tenant_path
    
    
    parse_tenant_path(path: str) -> typing.Dict[str, str]

Parses a tenant path into its component segments.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.parse_tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_parse_tenant_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.tenant_path
    
    
    tenant_path(project: str, tenant: str) -> str

Returns a fully-qualified tenant string.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_tenant_path)

### google.cloud.talent_v4.services.company_service.CompanyServiceClient.update_company
    
    
    update_company(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.company_service.UpdateCompanyRequest, dict
            ]
        ] = None,
        *,
        company: typing.Optional[google.cloud.talent_v4.types.company.Company] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4.types.company.Company

Updates specified company.

See more: [google.cloud.talent_v4.services.company_service.CompanyServiceClient.update_company](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceClient#google_cloud_talent_v4_services_company_service_CompanyServiceClient_update_company)

### google.cloud.talent_v4.services.company_service.pagers.ListCompaniesAsyncPager
    
    
    ListCompaniesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.talent_v4.types.company_service.ListCompaniesResponse
            ],
        ],
        request: google.cloud.talent_v4.types.company_service.ListCompaniesRequest,
        response: google.cloud.talent_v4.types.company_service.ListCompaniesResponse,
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

See more: [google.cloud.talent_v4.services.company_service.pagers.ListCompaniesAsyncPager](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.pagers.ListCompaniesAsyncPager#google_cloud_talent_v4_services_company_service_pagers_ListCompaniesAsyncPager_ListCompaniesAsyncPager)

### google.cloud.talent_v4.services.company_service.pagers.ListCompaniesPager
    
    
    ListCompaniesPager(
        method: typing.Callable[
            [...], google.cloud.talent_v4.types.company_service.ListCompaniesResponse
        ],
        request: google.cloud.talent_v4.types.company_service.ListCompaniesRequest,
        response: google.cloud.talent_v4.types.company_service.ListCompaniesResponse,
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

See more: [google.cloud.talent_v4.services.company_service.pagers.ListCompaniesPager](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.pagers.ListCompaniesPager#google_cloud_talent_v4_services_company_service_pagers_ListCompaniesPager_ListCompaniesPager)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient
    
    
    CompletionAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.talent_v4.services.completion.transports.base.CompletionTransport,
                typing.Callable[
                    [...],
                    google.cloud.talent_v4.services.completion.transports.base.CompletionTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the completion async client.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_CompletionAsyncClient)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_common_billing_account_path)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_common_folder_path)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_common_location_path)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_common_organization_path)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_common_project_path)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.company_path
    
    
    company_path(project: str, tenant: str, company: str) -> str

Returns a fully-qualified company string.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_company_path)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.complete_query
    
    
    complete_query(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.completion_service.CompleteQueryRequest, dict
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
    ) -> google.cloud.talent_v4.types.completion_service.CompleteQueryResponse

Completes the specified prefix with keyword suggestions.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.complete_query](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_complete_query)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_from_service_account_file)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_from_service_account_info)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_from_service_account_json)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.get_operation
    
    
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

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_get_operation)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.talent_v4.services.completion.transports.base.CompletionTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_get_transport_class)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_parse_common_billing_account_path)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_parse_common_folder_path)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_parse_common_location_path)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_parse_common_organization_path)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_parse_common_project_path)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.parse_company_path
    
    
    parse_company_path(path: str) -> typing.Dict[str, str]

Parses a company path into its component segments.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.parse_company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_parse_company_path)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.parse_tenant_path
    
    
    parse_tenant_path(path: str) -> typing.Dict[str, str]

Parses a tenant path into its component segments.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.parse_tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_parse_tenant_path)

### google.cloud.talent_v4.services.completion.CompletionAsyncClient.tenant_path
    
    
    tenant_path(project: str, tenant: str) -> str

Returns a fully-qualified tenant string.

See more: [google.cloud.talent_v4.services.completion.CompletionAsyncClient.tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionAsyncClient#google_cloud_talent_v4_services_completion_CompletionAsyncClient_tenant_path)

### google.cloud.talent_v4.services.completion.CompletionClient
    
    
    CompletionClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.talent_v4.services.completion.transports.base.CompletionTransport,
                typing.Callable[
                    [...],
                    google.cloud.talent_v4.services.completion.transports.base.CompletionTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the completion client.

See more: [google.cloud.talent_v4.services.completion.CompletionClient](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_CompletionClient)

### google.cloud.talent_v4.services.completion.CompletionClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.talent_v4.services.completion.CompletionClient.**exit**](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient___exit__)

### google.cloud.talent_v4.services.completion.CompletionClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.talent_v4.services.completion.CompletionClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_common_billing_account_path)

### google.cloud.talent_v4.services.completion.CompletionClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.talent_v4.services.completion.CompletionClient.common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_common_folder_path)

### google.cloud.talent_v4.services.completion.CompletionClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.talent_v4.services.completion.CompletionClient.common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_common_location_path)

### google.cloud.talent_v4.services.completion.CompletionClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.talent_v4.services.completion.CompletionClient.common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_common_organization_path)

### google.cloud.talent_v4.services.completion.CompletionClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.talent_v4.services.completion.CompletionClient.common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_common_project_path)

### google.cloud.talent_v4.services.completion.CompletionClient.company_path
    
    
    company_path(project: str, tenant: str, company: str) -> str

Returns a fully-qualified company string.

See more: [google.cloud.talent_v4.services.completion.CompletionClient.company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_company_path)

### google.cloud.talent_v4.services.completion.CompletionClient.complete_query
    
    
    complete_query(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.completion_service.CompleteQueryRequest, dict
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
    ) -> google.cloud.talent_v4.types.completion_service.CompleteQueryResponse

Completes the specified prefix with keyword suggestions.

See more: [google.cloud.talent_v4.services.completion.CompletionClient.complete_query](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_complete_query)

### google.cloud.talent_v4.services.completion.CompletionClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4.services.completion.CompletionClient.from_service_account_file](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_from_service_account_file)

### google.cloud.talent_v4.services.completion.CompletionClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.talent_v4.services.completion.CompletionClient.from_service_account_info](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_from_service_account_info)

### google.cloud.talent_v4.services.completion.CompletionClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4.services.completion.CompletionClient.from_service_account_json](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_from_service_account_json)

### google.cloud.talent_v4.services.completion.CompletionClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.talent_v4.services.completion.CompletionClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_get_mtls_endpoint_and_cert_source)

### google.cloud.talent_v4.services.completion.CompletionClient.get_operation
    
    
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

See more: [google.cloud.talent_v4.services.completion.CompletionClient.get_operation](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_get_operation)

### google.cloud.talent_v4.services.completion.CompletionClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.talent_v4.services.completion.CompletionClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_parse_common_billing_account_path)

### google.cloud.talent_v4.services.completion.CompletionClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.talent_v4.services.completion.CompletionClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_parse_common_folder_path)

### google.cloud.talent_v4.services.completion.CompletionClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.talent_v4.services.completion.CompletionClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_parse_common_location_path)

### google.cloud.talent_v4.services.completion.CompletionClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.talent_v4.services.completion.CompletionClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_parse_common_organization_path)

### google.cloud.talent_v4.services.completion.CompletionClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.talent_v4.services.completion.CompletionClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_parse_common_project_path)

### google.cloud.talent_v4.services.completion.CompletionClient.parse_company_path
    
    
    parse_company_path(path: str) -> typing.Dict[str, str]

Parses a company path into its component segments.

See more: [google.cloud.talent_v4.services.completion.CompletionClient.parse_company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_parse_company_path)

### google.cloud.talent_v4.services.completion.CompletionClient.parse_tenant_path
    
    
    parse_tenant_path(path: str) -> typing.Dict[str, str]

Parses a tenant path into its component segments.

See more: [google.cloud.talent_v4.services.completion.CompletionClient.parse_tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_parse_tenant_path)

### google.cloud.talent_v4.services.completion.CompletionClient.tenant_path
    
    
    tenant_path(project: str, tenant: str) -> str

Returns a fully-qualified tenant string.

See more: [google.cloud.talent_v4.services.completion.CompletionClient.tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.completion.CompletionClient#google_cloud_talent_v4_services_completion_CompletionClient_tenant_path)

### google.cloud.talent_v4.services.event_service.EventServiceAsyncClient
    
    
    EventServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.talent_v4.services.event_service.transports.base.EventServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.talent_v4.services.event_service.transports.base.EventServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the event service async client.

See more: [google.cloud.talent_v4.services.event_service.EventServiceAsyncClient](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4_services_event_service_EventServiceAsyncClient_EventServiceAsyncClient)

### google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4_services_event_service_EventServiceAsyncClient_common_billing_account_path)

### google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4_services_event_service_EventServiceAsyncClient_common_folder_path)

### google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4_services_event_service_EventServiceAsyncClient_common_location_path)

### google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4_services_event_service_EventServiceAsyncClient_common_organization_path)

### google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4_services_event_service_EventServiceAsyncClient_common_project_path)

### google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.create_client_event
    
    
    create_client_event(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.event_service.CreateClientEventRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        client_event: typing.Optional[
            google.cloud.talent_v4.types.event.ClientEvent
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4.types.event.ClientEvent

Report events issued when end user interacts with customer's application that uses Cloud Talent Solution.

See more: [google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.create_client_event](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4_services_event_service_EventServiceAsyncClient_create_client_event)

### google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4_services_event_service_EventServiceAsyncClient_from_service_account_file)

### google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4_services_event_service_EventServiceAsyncClient_from_service_account_info)

### google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4_services_event_service_EventServiceAsyncClient_from_service_account_json)

### google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4_services_event_service_EventServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4_services_event_service_EventServiceAsyncClient_get_operation)

### google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.talent_v4.services.event_service.transports.base.EventServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4_services_event_service_EventServiceAsyncClient_get_transport_class)

### google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4_services_event_service_EventServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4_services_event_service_EventServiceAsyncClient_parse_common_folder_path)

### google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4_services_event_service_EventServiceAsyncClient_parse_common_location_path)

### google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4_services_event_service_EventServiceAsyncClient_parse_common_organization_path)

### google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4_services_event_service_EventServiceAsyncClient_parse_common_project_path)

### google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.parse_tenant_path
    
    
    parse_tenant_path(path: str) -> typing.Dict[str, str]

Parses a tenant path into its component segments.

See more: [google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.parse_tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4_services_event_service_EventServiceAsyncClient_parse_tenant_path)

### google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.tenant_path
    
    
    tenant_path(project: str, tenant: str) -> str

Returns a fully-qualified tenant string.

See more: [google.cloud.talent_v4.services.event_service.EventServiceAsyncClient.tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4_services_event_service_EventServiceAsyncClient_tenant_path)

### google.cloud.talent_v4.services.event_service.EventServiceClient
    
    
    EventServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.talent_v4.services.event_service.transports.base.EventServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.talent_v4.services.event_service.transports.base.EventServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the event service client.

See more: [google.cloud.talent_v4.services.event_service.EventServiceClient](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient#google_cloud_talent_v4_services_event_service_EventServiceClient_EventServiceClient)

### google.cloud.talent_v4.services.event_service.EventServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.talent_v4.services.event_service.EventServiceClient.**exit**](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient#google_cloud_talent_v4_services_event_service_EventServiceClient___exit__)

### google.cloud.talent_v4.services.event_service.EventServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.talent_v4.services.event_service.EventServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient#google_cloud_talent_v4_services_event_service_EventServiceClient_common_billing_account_path)

### google.cloud.talent_v4.services.event_service.EventServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.talent_v4.services.event_service.EventServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient#google_cloud_talent_v4_services_event_service_EventServiceClient_common_folder_path)

### google.cloud.talent_v4.services.event_service.EventServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.talent_v4.services.event_service.EventServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient#google_cloud_talent_v4_services_event_service_EventServiceClient_common_location_path)

### google.cloud.talent_v4.services.event_service.EventServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.talent_v4.services.event_service.EventServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient#google_cloud_talent_v4_services_event_service_EventServiceClient_common_organization_path)

### google.cloud.talent_v4.services.event_service.EventServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.talent_v4.services.event_service.EventServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient#google_cloud_talent_v4_services_event_service_EventServiceClient_common_project_path)

### google.cloud.talent_v4.services.event_service.EventServiceClient.create_client_event
    
    
    create_client_event(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.event_service.CreateClientEventRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        client_event: typing.Optional[
            google.cloud.talent_v4.types.event.ClientEvent
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4.types.event.ClientEvent

Report events issued when end user interacts with customer's application that uses Cloud Talent Solution.

See more: [google.cloud.talent_v4.services.event_service.EventServiceClient.create_client_event](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient#google_cloud_talent_v4_services_event_service_EventServiceClient_create_client_event)

### google.cloud.talent_v4.services.event_service.EventServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4.services.event_service.EventServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient#google_cloud_talent_v4_services_event_service_EventServiceClient_from_service_account_file)

### google.cloud.talent_v4.services.event_service.EventServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.talent_v4.services.event_service.EventServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient#google_cloud_talent_v4_services_event_service_EventServiceClient_from_service_account_info)

### google.cloud.talent_v4.services.event_service.EventServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4.services.event_service.EventServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient#google_cloud_talent_v4_services_event_service_EventServiceClient_from_service_account_json)

### google.cloud.talent_v4.services.event_service.EventServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.talent_v4.services.event_service.EventServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient#google_cloud_talent_v4_services_event_service_EventServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.talent_v4.services.event_service.EventServiceClient.get_operation
    
    
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

See more: [google.cloud.talent_v4.services.event_service.EventServiceClient.get_operation](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient#google_cloud_talent_v4_services_event_service_EventServiceClient_get_operation)

### google.cloud.talent_v4.services.event_service.EventServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.talent_v4.services.event_service.EventServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient#google_cloud_talent_v4_services_event_service_EventServiceClient_parse_common_billing_account_path)

### google.cloud.talent_v4.services.event_service.EventServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.talent_v4.services.event_service.EventServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient#google_cloud_talent_v4_services_event_service_EventServiceClient_parse_common_folder_path)

### google.cloud.talent_v4.services.event_service.EventServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.talent_v4.services.event_service.EventServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient#google_cloud_talent_v4_services_event_service_EventServiceClient_parse_common_location_path)

### google.cloud.talent_v4.services.event_service.EventServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.talent_v4.services.event_service.EventServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient#google_cloud_talent_v4_services_event_service_EventServiceClient_parse_common_organization_path)

### google.cloud.talent_v4.services.event_service.EventServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.talent_v4.services.event_service.EventServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient#google_cloud_talent_v4_services_event_service_EventServiceClient_parse_common_project_path)

### google.cloud.talent_v4.services.event_service.EventServiceClient.parse_tenant_path
    
    
    parse_tenant_path(path: str) -> typing.Dict[str, str]

Parses a tenant path into its component segments.

See more: [google.cloud.talent_v4.services.event_service.EventServiceClient.parse_tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient#google_cloud_talent_v4_services_event_service_EventServiceClient_parse_tenant_path)

### google.cloud.talent_v4.services.event_service.EventServiceClient.tenant_path
    
    
    tenant_path(project: str, tenant: str) -> str

Returns a fully-qualified tenant string.

See more: [google.cloud.talent_v4.services.event_service.EventServiceClient.tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.event_service.EventServiceClient#google_cloud_talent_v4_services_event_service_EventServiceClient_tenant_path)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient
    
    
    JobServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.talent_v4.services.job_service.transports.base.JobServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.talent_v4.services.job_service.transports.base.JobServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the job service async client.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_JobServiceAsyncClient)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.batch_create_jobs
    
    
    batch_create_jobs(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.job_service.BatchCreateJobsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        jobs: typing.Optional[
            typing.MutableSequence[google.cloud.talent_v4.types.job.Job]
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

Begins executing a batch create jobs operation.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.batch_create_jobs](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_batch_create_jobs)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.batch_delete_jobs
    
    
    batch_delete_jobs(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.job_service.BatchDeleteJobsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        names: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Begins executing a batch delete jobs operation.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.batch_delete_jobs](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_batch_delete_jobs)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.batch_update_jobs
    
    
    batch_update_jobs(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.job_service.BatchUpdateJobsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        jobs: typing.Optional[
            typing.MutableSequence[google.cloud.talent_v4.types.job.Job]
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

Begins executing a batch update jobs operation.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.batch_update_jobs](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_batch_update_jobs)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_common_billing_account_path)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_common_folder_path)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_common_location_path)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_common_organization_path)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_common_project_path)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.company_path
    
    
    company_path(project: str, tenant: str, company: str) -> str

Returns a fully-qualified company string.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_company_path)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.create_job
    
    
    create_job(
        request: typing.Optional[
            typing.Union[google.cloud.talent_v4.types.job_service.CreateJobRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        job: typing.Optional[google.cloud.talent_v4.types.job.Job] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4.types.job.Job

Creates a new job.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.create_job](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_create_job)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.delete_job
    
    
    delete_job(
        request: typing.Optional[
            typing.Union[google.cloud.talent_v4.types.job_service.DeleteJobRequest, dict]
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

Deletes the specified job.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.delete_job](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_delete_job)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_from_service_account_file)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_from_service_account_info)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_from_service_account_json)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.get_job
    
    
    get_job(
        request: typing.Optional[
            typing.Union[google.cloud.talent_v4.types.job_service.GetJobRequest, dict]
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
    ) -> google.cloud.talent_v4.types.job.Job

Retrieves the specified job, whose status is OPEN or recently EXPIRED within the last 90 days.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.get_job](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_get_job)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_get_operation)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.talent_v4.services.job_service.transports.base.JobServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_get_transport_class)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.job_path
    
    
    job_path(project: str, tenant: str, job: str) -> str

Returns a fully-qualified job string.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.job_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_job_path)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.list_jobs
    
    
    list_jobs(
        request: typing.Optional[
            typing.Union[google.cloud.talent_v4.types.job_service.ListJobsRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4.services.job_service.pagers.ListJobsAsyncPager

Lists jobs by filter.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.list_jobs](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_list_jobs)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_parse_common_folder_path)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_parse_common_location_path)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_parse_common_organization_path)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_parse_common_project_path)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.parse_company_path
    
    
    parse_company_path(path: str) -> typing.Dict[str, str]

Parses a company path into its component segments.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.parse_company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_parse_company_path)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.parse_job_path
    
    
    parse_job_path(path: str) -> typing.Dict[str, str]

Parses a job path into its component segments.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.parse_job_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_parse_job_path)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.parse_tenant_path
    
    
    parse_tenant_path(path: str) -> typing.Dict[str, str]

Parses a tenant path into its component segments.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.parse_tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_parse_tenant_path)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.search_jobs
    
    
    search_jobs(
        request: typing.Optional[
            typing.Union[google.cloud.talent_v4.types.job_service.SearchJobsRequest, dict]
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
    ) -> google.cloud.talent_v4.types.job_service.SearchJobsResponse

Searches for jobs using the provided xref_SearchJobsRequest.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.search_jobs](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_search_jobs)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.search_jobs_for_alert
    
    
    search_jobs_for_alert(
        request: typing.Optional[
            typing.Union[google.cloud.talent_v4.types.job_service.SearchJobsRequest, dict]
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
    ) -> google.cloud.talent_v4.types.job_service.SearchJobsResponse

Searches for jobs using the provided xref_SearchJobsRequest.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.search_jobs_for_alert](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_search_jobs_for_alert)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.tenant_path
    
    
    tenant_path(project: str, tenant: str) -> str

Returns a fully-qualified tenant string.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_tenant_path)

### google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.update_job
    
    
    update_job(
        request: typing.Optional[
            typing.Union[google.cloud.talent_v4.types.job_service.UpdateJobRequest, dict]
        ] = None,
        *,
        job: typing.Optional[google.cloud.talent_v4.types.job.Job] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4.types.job.Job

Updates specified job.

See more: [google.cloud.talent_v4.services.job_service.JobServiceAsyncClient.update_job](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4_services_job_service_JobServiceAsyncClient_update_job)

### google.cloud.talent_v4.services.job_service.JobServiceClient
    
    
    JobServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.talent_v4.services.job_service.transports.base.JobServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.talent_v4.services.job_service.transports.base.JobServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the job service client.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_JobServiceClient)

### google.cloud.talent_v4.services.job_service.JobServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.**exit**](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient___exit__)

### google.cloud.talent_v4.services.job_service.JobServiceClient.batch_create_jobs
    
    
    batch_create_jobs(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.job_service.BatchCreateJobsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        jobs: typing.Optional[
            typing.MutableSequence[google.cloud.talent_v4.types.job.Job]
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

Begins executing a batch create jobs operation.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.batch_create_jobs](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_batch_create_jobs)

### google.cloud.talent_v4.services.job_service.JobServiceClient.batch_delete_jobs
    
    
    batch_delete_jobs(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.job_service.BatchDeleteJobsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        names: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Begins executing a batch delete jobs operation.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.batch_delete_jobs](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_batch_delete_jobs)

### google.cloud.talent_v4.services.job_service.JobServiceClient.batch_update_jobs
    
    
    batch_update_jobs(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.job_service.BatchUpdateJobsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        jobs: typing.Optional[
            typing.MutableSequence[google.cloud.talent_v4.types.job.Job]
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

Begins executing a batch update jobs operation.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.batch_update_jobs](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_batch_update_jobs)

### google.cloud.talent_v4.services.job_service.JobServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_common_billing_account_path)

### google.cloud.talent_v4.services.job_service.JobServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_common_folder_path)

### google.cloud.talent_v4.services.job_service.JobServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_common_location_path)

### google.cloud.talent_v4.services.job_service.JobServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_common_organization_path)

### google.cloud.talent_v4.services.job_service.JobServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_common_project_path)

### google.cloud.talent_v4.services.job_service.JobServiceClient.company_path
    
    
    company_path(project: str, tenant: str, company: str) -> str

Returns a fully-qualified company string.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_company_path)

### google.cloud.talent_v4.services.job_service.JobServiceClient.create_job
    
    
    create_job(
        request: typing.Optional[
            typing.Union[google.cloud.talent_v4.types.job_service.CreateJobRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        job: typing.Optional[google.cloud.talent_v4.types.job.Job] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4.types.job.Job

Creates a new job.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.create_job](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_create_job)

### google.cloud.talent_v4.services.job_service.JobServiceClient.delete_job
    
    
    delete_job(
        request: typing.Optional[
            typing.Union[google.cloud.talent_v4.types.job_service.DeleteJobRequest, dict]
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

Deletes the specified job.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.delete_job](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_delete_job)

### google.cloud.talent_v4.services.job_service.JobServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_from_service_account_file)

### google.cloud.talent_v4.services.job_service.JobServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_from_service_account_info)

### google.cloud.talent_v4.services.job_service.JobServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_from_service_account_json)

### google.cloud.talent_v4.services.job_service.JobServiceClient.get_job
    
    
    get_job(
        request: typing.Optional[
            typing.Union[google.cloud.talent_v4.types.job_service.GetJobRequest, dict]
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
    ) -> google.cloud.talent_v4.types.job.Job

Retrieves the specified job, whose status is OPEN or recently EXPIRED within the last 90 days.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.get_job](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_get_job)

### google.cloud.talent_v4.services.job_service.JobServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.talent_v4.services.job_service.JobServiceClient.get_operation
    
    
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

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.get_operation](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_get_operation)

### google.cloud.talent_v4.services.job_service.JobServiceClient.job_path
    
    
    job_path(project: str, tenant: str, job: str) -> str

Returns a fully-qualified job string.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.job_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_job_path)

### google.cloud.talent_v4.services.job_service.JobServiceClient.list_jobs
    
    
    list_jobs(
        request: typing.Optional[
            typing.Union[google.cloud.talent_v4.types.job_service.ListJobsRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4.services.job_service.pagers.ListJobsPager

Lists jobs by filter.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.list_jobs](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_list_jobs)

### google.cloud.talent_v4.services.job_service.JobServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_parse_common_billing_account_path)

### google.cloud.talent_v4.services.job_service.JobServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_parse_common_folder_path)

### google.cloud.talent_v4.services.job_service.JobServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_parse_common_location_path)

### google.cloud.talent_v4.services.job_service.JobServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_parse_common_organization_path)

### google.cloud.talent_v4.services.job_service.JobServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_parse_common_project_path)

### google.cloud.talent_v4.services.job_service.JobServiceClient.parse_company_path
    
    
    parse_company_path(path: str) -> typing.Dict[str, str]

Parses a company path into its component segments.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.parse_company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_parse_company_path)

### google.cloud.talent_v4.services.job_service.JobServiceClient.parse_job_path
    
    
    parse_job_path(path: str) -> typing.Dict[str, str]

Parses a job path into its component segments.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.parse_job_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_parse_job_path)

### google.cloud.talent_v4.services.job_service.JobServiceClient.parse_tenant_path
    
    
    parse_tenant_path(path: str) -> typing.Dict[str, str]

Parses a tenant path into its component segments.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.parse_tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_parse_tenant_path)

### google.cloud.talent_v4.services.job_service.JobServiceClient.search_jobs
    
    
    search_jobs(
        request: typing.Optional[
            typing.Union[google.cloud.talent_v4.types.job_service.SearchJobsRequest, dict]
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
    ) -> google.cloud.talent_v4.types.job_service.SearchJobsResponse

Searches for jobs using the provided xref_SearchJobsRequest.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.search_jobs](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_search_jobs)

### google.cloud.talent_v4.services.job_service.JobServiceClient.search_jobs_for_alert
    
    
    search_jobs_for_alert(
        request: typing.Optional[
            typing.Union[google.cloud.talent_v4.types.job_service.SearchJobsRequest, dict]
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
    ) -> google.cloud.talent_v4.types.job_service.SearchJobsResponse

Searches for jobs using the provided xref_SearchJobsRequest.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.search_jobs_for_alert](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_search_jobs_for_alert)

### google.cloud.talent_v4.services.job_service.JobServiceClient.tenant_path
    
    
    tenant_path(project: str, tenant: str) -> str

Returns a fully-qualified tenant string.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_tenant_path)

### google.cloud.talent_v4.services.job_service.JobServiceClient.update_job
    
    
    update_job(
        request: typing.Optional[
            typing.Union[google.cloud.talent_v4.types.job_service.UpdateJobRequest, dict]
        ] = None,
        *,
        job: typing.Optional[google.cloud.talent_v4.types.job.Job] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4.types.job.Job

Updates specified job.

See more: [google.cloud.talent_v4.services.job_service.JobServiceClient.update_job](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.JobServiceClient#google_cloud_talent_v4_services_job_service_JobServiceClient_update_job)

### google.cloud.talent_v4.services.job_service.pagers.ListJobsAsyncPager
    
    
    ListJobsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.talent_v4.types.job_service.ListJobsResponse],
        ],
        request: google.cloud.talent_v4.types.job_service.ListJobsRequest,
        response: google.cloud.talent_v4.types.job_service.ListJobsResponse,
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

See more: [google.cloud.talent_v4.services.job_service.pagers.ListJobsAsyncPager](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.pagers.ListJobsAsyncPager#google_cloud_talent_v4_services_job_service_pagers_ListJobsAsyncPager_ListJobsAsyncPager)

### google.cloud.talent_v4.services.job_service.pagers.ListJobsPager
    
    
    ListJobsPager(
        method: typing.Callable[
            [...], google.cloud.talent_v4.types.job_service.ListJobsResponse
        ],
        request: google.cloud.talent_v4.types.job_service.ListJobsRequest,
        response: google.cloud.talent_v4.types.job_service.ListJobsResponse,
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

See more: [google.cloud.talent_v4.services.job_service.pagers.ListJobsPager](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.job_service.pagers.ListJobsPager#google_cloud_talent_v4_services_job_service_pagers_ListJobsPager_ListJobsPager)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient
    
    
    TenantServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.talent_v4.services.tenant_service.transports.base.TenantServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.talent_v4.services.tenant_service.transports.base.TenantServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the tenant service async client.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_TenantServiceAsyncClient)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_common_billing_account_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_common_folder_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_common_location_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_common_organization_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_common_project_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.create_tenant
    
    
    create_tenant(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.tenant_service.CreateTenantRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        tenant: typing.Optional[google.cloud.talent_v4.types.tenant.Tenant] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4.types.tenant.Tenant

Creates a new tenant entity.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.create_tenant](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_create_tenant)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.delete_tenant
    
    
    delete_tenant(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.tenant_service.DeleteTenantRequest, dict
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

Deletes specified tenant.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.delete_tenant](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_delete_tenant)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_from_service_account_file)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_from_service_account_info)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_from_service_account_json)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_get_operation)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.get_tenant
    
    
    get_tenant(
        request: typing.Optional[
            typing.Union[google.cloud.talent_v4.types.tenant_service.GetTenantRequest, dict]
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
    ) -> google.cloud.talent_v4.types.tenant.Tenant

Retrieves specified tenant.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.get_tenant](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_get_tenant)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.talent_v4.services.tenant_service.transports.base.TenantServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_get_transport_class)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.list_tenants
    
    
    list_tenants(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.tenant_service.ListTenantsRequest, dict
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
    ) -> google.cloud.talent_v4.services.tenant_service.pagers.ListTenantsAsyncPager

Lists all tenants associated with the project.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.list_tenants](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_list_tenants)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_parse_common_folder_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_parse_common_location_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_parse_common_organization_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_parse_common_project_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.parse_tenant_path
    
    
    parse_tenant_path(path: str) -> typing.Dict[str, str]

Parses a tenant path into its component segments.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.parse_tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_parse_tenant_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.tenant_path
    
    
    tenant_path(project: str, tenant: str) -> str

Returns a fully-qualified tenant string.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_tenant_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.update_tenant
    
    
    update_tenant(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.tenant_service.UpdateTenantRequest, dict
            ]
        ] = None,
        *,
        tenant: typing.Optional[google.cloud.talent_v4.types.tenant.Tenant] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4.types.tenant.Tenant

Updates specified tenant.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient.update_tenant](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4_services_tenant_service_TenantServiceAsyncClient_update_tenant)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient
    
    
    TenantServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.talent_v4.services.tenant_service.transports.base.TenantServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.talent_v4.services.tenant_service.transports.base.TenantServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the tenant service client.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_TenantServiceClient)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.**exit**](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient___exit__)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_common_billing_account_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_common_folder_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_common_location_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_common_organization_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_common_project_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.create_tenant
    
    
    create_tenant(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.tenant_service.CreateTenantRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        tenant: typing.Optional[google.cloud.talent_v4.types.tenant.Tenant] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4.types.tenant.Tenant

Creates a new tenant entity.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.create_tenant](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_create_tenant)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.delete_tenant
    
    
    delete_tenant(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.tenant_service.DeleteTenantRequest, dict
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

Deletes specified tenant.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.delete_tenant](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_delete_tenant)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_from_service_account_file)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_from_service_account_info)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_from_service_account_json)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.get_operation
    
    
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

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.get_operation](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_get_operation)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.get_tenant
    
    
    get_tenant(
        request: typing.Optional[
            typing.Union[google.cloud.talent_v4.types.tenant_service.GetTenantRequest, dict]
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
    ) -> google.cloud.talent_v4.types.tenant.Tenant

Retrieves specified tenant.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.get_tenant](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_get_tenant)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.list_tenants
    
    
    list_tenants(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.tenant_service.ListTenantsRequest, dict
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
    ) -> google.cloud.talent_v4.services.tenant_service.pagers.ListTenantsPager

Lists all tenants associated with the project.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.list_tenants](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_list_tenants)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_parse_common_billing_account_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_parse_common_folder_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_parse_common_location_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_parse_common_organization_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_parse_common_project_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.parse_tenant_path
    
    
    parse_tenant_path(path: str) -> typing.Dict[str, str]

Parses a tenant path into its component segments.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.parse_tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_parse_tenant_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.tenant_path
    
    
    tenant_path(project: str, tenant: str) -> str

Returns a fully-qualified tenant string.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_tenant_path)

### google.cloud.talent_v4.services.tenant_service.TenantServiceClient.update_tenant
    
    
    update_tenant(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4.types.tenant_service.UpdateTenantRequest, dict
            ]
        ] = None,
        *,
        tenant: typing.Optional[google.cloud.talent_v4.types.tenant.Tenant] = None,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4.types.tenant.Tenant

Updates specified tenant.

See more: [google.cloud.talent_v4.services.tenant_service.TenantServiceClient.update_tenant](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.TenantServiceClient#google_cloud_talent_v4_services_tenant_service_TenantServiceClient_update_tenant)

### google.cloud.talent_v4.services.tenant_service.pagers.ListTenantsAsyncPager
    
    
    ListTenantsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.talent_v4.types.tenant_service.ListTenantsResponse
            ],
        ],
        request: google.cloud.talent_v4.types.tenant_service.ListTenantsRequest,
        response: google.cloud.talent_v4.types.tenant_service.ListTenantsResponse,
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

See more: [google.cloud.talent_v4.services.tenant_service.pagers.ListTenantsAsyncPager](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.pagers.ListTenantsAsyncPager#google_cloud_talent_v4_services_tenant_service_pagers_ListTenantsAsyncPager_ListTenantsAsyncPager)

### google.cloud.talent_v4.services.tenant_service.pagers.ListTenantsPager
    
    
    ListTenantsPager(
        method: typing.Callable[
            [...], google.cloud.talent_v4.types.tenant_service.ListTenantsResponse
        ],
        request: google.cloud.talent_v4.types.tenant_service.ListTenantsRequest,
        response: google.cloud.talent_v4.types.tenant_service.ListTenantsResponse,
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

See more: [google.cloud.talent_v4.services.tenant_service.pagers.ListTenantsPager](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.tenant_service.pagers.ListTenantsPager#google_cloud_talent_v4_services_tenant_service_pagers_ListTenantsPager_ListTenantsPager)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient
    
    
    CompanyServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.talent_v4beta1.services.company_service.transports.base.CompanyServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.talent_v4beta1.services.company_service.transports.base.CompanyServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the company service async client.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_CompanyServiceAsyncClient)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_common_billing_account_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_common_folder_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_common_location_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_common_organization_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_common_project_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.company_path
    
    
    company_path(project: str, tenant: str, company: str) -> str

Returns a fully-qualified company string.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_company_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.create_company
    
    
    create_company(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.company_service.CreateCompanyRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        company: typing.Optional[google.cloud.talent_v4beta1.types.company.Company] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4beta1.types.company.Company

Creates a new company entity.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.create_company](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_create_company)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.delete_company
    
    
    delete_company(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.company_service.DeleteCompanyRequest, dict
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

Deletes specified company.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.delete_company](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_delete_company)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_from_service_account_file)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_from_service_account_info)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_from_service_account_json)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.get_company
    
    
    get_company(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.company_service.GetCompanyRequest, dict
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
    ) -> google.cloud.talent_v4beta1.types.company.Company

Retrieves specified company.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.get_company](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_get_company)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_get_operation)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.talent_v4beta1.services.company_service.transports.base.CompanyServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_get_transport_class)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.list_companies
    
    
    list_companies(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.company_service.ListCompaniesRequest, dict
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
        google.cloud.talent_v4beta1.services.company_service.pagers.ListCompaniesAsyncPager
    )

Lists all companies associated with the project.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.list_companies](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_list_companies)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_parse_common_folder_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_parse_common_location_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_parse_common_organization_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_parse_common_project_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.parse_company_path
    
    
    parse_company_path(path: str) -> typing.Dict[str, str]

Parses a company path into its component segments.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.parse_company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_parse_company_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.update_company
    
    
    update_company(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.company_service.UpdateCompanyRequest, dict
            ]
        ] = None,
        *,
        company: typing.Optional[google.cloud.talent_v4beta1.types.company.Company] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4beta1.types.company.Company

Updates specified company.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient.update_company](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceAsyncClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceAsyncClient_update_company)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient
    
    
    CompanyServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.talent_v4beta1.services.company_service.transports.base.CompanyServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.talent_v4beta1.services.company_service.transports.base.CompanyServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the company service client.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_CompanyServiceClient)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.**exit**](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient___exit__)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_common_billing_account_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_common_folder_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_common_location_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_common_organization_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_common_project_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.company_path
    
    
    company_path(project: str, tenant: str, company: str) -> str

Returns a fully-qualified company string.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_company_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.create_company
    
    
    create_company(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.company_service.CreateCompanyRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        company: typing.Optional[google.cloud.talent_v4beta1.types.company.Company] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4beta1.types.company.Company

Creates a new company entity.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.create_company](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_create_company)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.delete_company
    
    
    delete_company(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.company_service.DeleteCompanyRequest, dict
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

Deletes specified company.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.delete_company](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_delete_company)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_from_service_account_file)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_from_service_account_info)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_from_service_account_json)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.get_company
    
    
    get_company(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.company_service.GetCompanyRequest, dict
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
    ) -> google.cloud.talent_v4beta1.types.company.Company

Retrieves specified company.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.get_company](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_get_company)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.get_operation
    
    
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

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.get_operation](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_get_operation)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.list_companies
    
    
    list_companies(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.company_service.ListCompaniesRequest, dict
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
    ) -> google.cloud.talent_v4beta1.services.company_service.pagers.ListCompaniesPager

Lists all companies associated with the project.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.list_companies](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_list_companies)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_parse_common_billing_account_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_parse_common_folder_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_parse_common_location_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_parse_common_organization_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_parse_common_project_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.parse_company_path
    
    
    parse_company_path(path: str) -> typing.Dict[str, str]

Parses a company path into its component segments.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.parse_company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_parse_company_path)

### google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.update_company
    
    
    update_company(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.company_service.UpdateCompanyRequest, dict
            ]
        ] = None,
        *,
        company: typing.Optional[google.cloud.talent_v4beta1.types.company.Company] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4beta1.types.company.Company

Updates specified company.

See more: [google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient.update_company](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.CompanyServiceClient#google_cloud_talent_v4beta1_services_company_service_CompanyServiceClient_update_company)

### google.cloud.talent_v4beta1.services.company_service.pagers.ListCompaniesAsyncPager
    
    
    ListCompaniesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.talent_v4beta1.types.company_service.ListCompaniesResponse
            ],
        ],
        request: google.cloud.talent_v4beta1.types.company_service.ListCompaniesRequest,
        response: google.cloud.talent_v4beta1.types.company_service.ListCompaniesResponse,
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

See more: [google.cloud.talent_v4beta1.services.company_service.pagers.ListCompaniesAsyncPager](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.pagers.ListCompaniesAsyncPager#google_cloud_talent_v4beta1_services_company_service_pagers_ListCompaniesAsyncPager_ListCompaniesAsyncPager)

### google.cloud.talent_v4beta1.services.company_service.pagers.ListCompaniesPager
    
    
    ListCompaniesPager(
        method: typing.Callable[
            [...], google.cloud.talent_v4beta1.types.company_service.ListCompaniesResponse
        ],
        request: google.cloud.talent_v4beta1.types.company_service.ListCompaniesRequest,
        response: google.cloud.talent_v4beta1.types.company_service.ListCompaniesResponse,
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

See more: [google.cloud.talent_v4beta1.services.company_service.pagers.ListCompaniesPager](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.company_service.pagers.ListCompaniesPager#google_cloud_talent_v4beta1_services_company_service_pagers_ListCompaniesPager_ListCompaniesPager)

### google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient
    
    
    CompletionAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.talent_v4beta1.services.completion.transports.base.CompletionTransport,
                typing.Callable[
                    [...],
                    google.cloud.talent_v4beta1.services.completion.transports.base.CompletionTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the completion async client.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient#google_cloud_talent_v4beta1_services_completion_CompletionAsyncClient_CompletionAsyncClient)

### google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient#google_cloud_talent_v4beta1_services_completion_CompletionAsyncClient_common_billing_account_path)

### google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient#google_cloud_talent_v4beta1_services_completion_CompletionAsyncClient_common_folder_path)

### google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient#google_cloud_talent_v4beta1_services_completion_CompletionAsyncClient_common_location_path)

### google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient#google_cloud_talent_v4beta1_services_completion_CompletionAsyncClient_common_organization_path)

### google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient#google_cloud_talent_v4beta1_services_completion_CompletionAsyncClient_common_project_path)

### google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.company_path
    
    
    company_path(project: str, tenant: str, company: str) -> str

Returns a fully-qualified company string.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient#google_cloud_talent_v4beta1_services_completion_CompletionAsyncClient_company_path)

### google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.complete_query
    
    
    complete_query(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.completion_service.CompleteQueryRequest,
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
    ) -> google.cloud.talent_v4beta1.types.completion_service.CompleteQueryResponse

Completes the specified prefix with keyword suggestions.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.complete_query](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient#google_cloud_talent_v4beta1_services_completion_CompletionAsyncClient_complete_query)

### google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient#google_cloud_talent_v4beta1_services_completion_CompletionAsyncClient_from_service_account_file)

### google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient#google_cloud_talent_v4beta1_services_completion_CompletionAsyncClient_from_service_account_info)

### google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient#google_cloud_talent_v4beta1_services_completion_CompletionAsyncClient_from_service_account_json)

### google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient#google_cloud_talent_v4beta1_services_completion_CompletionAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.get_operation
    
    
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

See more: [google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient#google_cloud_talent_v4beta1_services_completion_CompletionAsyncClient_get_operation)

### google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.talent_v4beta1.services.completion.transports.base.CompletionTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient#google_cloud_talent_v4beta1_services_completion_CompletionAsyncClient_get_transport_class)

### google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient#google_cloud_talent_v4beta1_services_completion_CompletionAsyncClient_parse_common_billing_account_path)

### google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient#google_cloud_talent_v4beta1_services_completion_CompletionAsyncClient_parse_common_folder_path)

### google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient#google_cloud_talent_v4beta1_services_completion_CompletionAsyncClient_parse_common_location_path)

### google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient#google_cloud_talent_v4beta1_services_completion_CompletionAsyncClient_parse_common_organization_path)

### google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient#google_cloud_talent_v4beta1_services_completion_CompletionAsyncClient_parse_common_project_path)

### google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.parse_company_path
    
    
    parse_company_path(path: str) -> typing.Dict[str, str]

Parses a company path into its component segments.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient.parse_company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionAsyncClient#google_cloud_talent_v4beta1_services_completion_CompletionAsyncClient_parse_company_path)

### google.cloud.talent_v4beta1.services.completion.CompletionClient
    
    
    CompletionClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.talent_v4beta1.services.completion.transports.base.CompletionTransport,
                typing.Callable[
                    [...],
                    google.cloud.talent_v4beta1.services.completion.transports.base.CompletionTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the completion client.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionClient](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient#google_cloud_talent_v4beta1_services_completion_CompletionClient_CompletionClient)

### google.cloud.talent_v4beta1.services.completion.CompletionClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionClient.**exit**](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient#google_cloud_talent_v4beta1_services_completion_CompletionClient___exit__)

### google.cloud.talent_v4beta1.services.completion.CompletionClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient#google_cloud_talent_v4beta1_services_completion_CompletionClient_common_billing_account_path)

### google.cloud.talent_v4beta1.services.completion.CompletionClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionClient.common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient#google_cloud_talent_v4beta1_services_completion_CompletionClient_common_folder_path)

### google.cloud.talent_v4beta1.services.completion.CompletionClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionClient.common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient#google_cloud_talent_v4beta1_services_completion_CompletionClient_common_location_path)

### google.cloud.talent_v4beta1.services.completion.CompletionClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionClient.common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient#google_cloud_talent_v4beta1_services_completion_CompletionClient_common_organization_path)

### google.cloud.talent_v4beta1.services.completion.CompletionClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionClient.common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient#google_cloud_talent_v4beta1_services_completion_CompletionClient_common_project_path)

### google.cloud.talent_v4beta1.services.completion.CompletionClient.company_path
    
    
    company_path(project: str, tenant: str, company: str) -> str

Returns a fully-qualified company string.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionClient.company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient#google_cloud_talent_v4beta1_services_completion_CompletionClient_company_path)

### google.cloud.talent_v4beta1.services.completion.CompletionClient.complete_query
    
    
    complete_query(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.completion_service.CompleteQueryRequest,
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
    ) -> google.cloud.talent_v4beta1.types.completion_service.CompleteQueryResponse

Completes the specified prefix with keyword suggestions.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionClient.complete_query](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient#google_cloud_talent_v4beta1_services_completion_CompletionClient_complete_query)

### google.cloud.talent_v4beta1.services.completion.CompletionClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionClient.from_service_account_file](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient#google_cloud_talent_v4beta1_services_completion_CompletionClient_from_service_account_file)

### google.cloud.talent_v4beta1.services.completion.CompletionClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionClient.from_service_account_info](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient#google_cloud_talent_v4beta1_services_completion_CompletionClient_from_service_account_info)

### google.cloud.talent_v4beta1.services.completion.CompletionClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionClient.from_service_account_json](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient#google_cloud_talent_v4beta1_services_completion_CompletionClient_from_service_account_json)

### google.cloud.talent_v4beta1.services.completion.CompletionClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient#google_cloud_talent_v4beta1_services_completion_CompletionClient_get_mtls_endpoint_and_cert_source)

### google.cloud.talent_v4beta1.services.completion.CompletionClient.get_operation
    
    
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

See more: [google.cloud.talent_v4beta1.services.completion.CompletionClient.get_operation](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient#google_cloud_talent_v4beta1_services_completion_CompletionClient_get_operation)

### google.cloud.talent_v4beta1.services.completion.CompletionClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient#google_cloud_talent_v4beta1_services_completion_CompletionClient_parse_common_billing_account_path)

### google.cloud.talent_v4beta1.services.completion.CompletionClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient#google_cloud_talent_v4beta1_services_completion_CompletionClient_parse_common_folder_path)

### google.cloud.talent_v4beta1.services.completion.CompletionClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient#google_cloud_talent_v4beta1_services_completion_CompletionClient_parse_common_location_path)

### google.cloud.talent_v4beta1.services.completion.CompletionClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient#google_cloud_talent_v4beta1_services_completion_CompletionClient_parse_common_organization_path)

### google.cloud.talent_v4beta1.services.completion.CompletionClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient#google_cloud_talent_v4beta1_services_completion_CompletionClient_parse_common_project_path)

### google.cloud.talent_v4beta1.services.completion.CompletionClient.parse_company_path
    
    
    parse_company_path(path: str) -> typing.Dict[str, str]

Parses a company path into its component segments.

See more: [google.cloud.talent_v4beta1.services.completion.CompletionClient.parse_company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.completion.CompletionClient#google_cloud_talent_v4beta1_services_completion_CompletionClient_parse_company_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient
    
    
    EventServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.talent_v4beta1.services.event_service.transports.base.EventServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.talent_v4beta1.services.event_service.transports.base.EventServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the event service async client.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4beta1_services_event_service_EventServiceAsyncClient_EventServiceAsyncClient)

### google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4beta1_services_event_service_EventServiceAsyncClient_common_billing_account_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4beta1_services_event_service_EventServiceAsyncClient_common_folder_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4beta1_services_event_service_EventServiceAsyncClient_common_location_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4beta1_services_event_service_EventServiceAsyncClient_common_organization_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4beta1_services_event_service_EventServiceAsyncClient_common_project_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.company_path
    
    
    company_path(project: str, tenant: str, company: str) -> str

Returns a fully-qualified company string.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4beta1_services_event_service_EventServiceAsyncClient_company_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.create_client_event
    
    
    create_client_event(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.event_service.CreateClientEventRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        client_event: typing.Optional[
            google.cloud.talent_v4beta1.types.event.ClientEvent
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4beta1.types.event.ClientEvent

Report events issued when end user interacts with customer's application that uses Cloud Talent Solution.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.create_client_event](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4beta1_services_event_service_EventServiceAsyncClient_create_client_event)

### google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4beta1_services_event_service_EventServiceAsyncClient_from_service_account_file)

### google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4beta1_services_event_service_EventServiceAsyncClient_from_service_account_info)

### google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4beta1_services_event_service_EventServiceAsyncClient_from_service_account_json)

### google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4beta1_services_event_service_EventServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4beta1_services_event_service_EventServiceAsyncClient_get_operation)

### google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.talent_v4beta1.services.event_service.transports.base.EventServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4beta1_services_event_service_EventServiceAsyncClient_get_transport_class)

### google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4beta1_services_event_service_EventServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4beta1_services_event_service_EventServiceAsyncClient_parse_common_folder_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4beta1_services_event_service_EventServiceAsyncClient_parse_common_location_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4beta1_services_event_service_EventServiceAsyncClient_parse_common_organization_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4beta1_services_event_service_EventServiceAsyncClient_parse_common_project_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.parse_company_path
    
    
    parse_company_path(path: str) -> typing.Dict[str, str]

Parses a company path into its component segments.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient.parse_company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceAsyncClient#google_cloud_talent_v4beta1_services_event_service_EventServiceAsyncClient_parse_company_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceClient
    
    
    EventServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.talent_v4beta1.services.event_service.transports.base.EventServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.talent_v4beta1.services.event_service.transports.base.EventServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the event service client.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceClient](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient#google_cloud_talent_v4beta1_services_event_service_EventServiceClient_EventServiceClient)

### google.cloud.talent_v4beta1.services.event_service.EventServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceClient.**exit**](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient#google_cloud_talent_v4beta1_services_event_service_EventServiceClient___exit__)

### google.cloud.talent_v4beta1.services.event_service.EventServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient#google_cloud_talent_v4beta1_services_event_service_EventServiceClient_common_billing_account_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient#google_cloud_talent_v4beta1_services_event_service_EventServiceClient_common_folder_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient#google_cloud_talent_v4beta1_services_event_service_EventServiceClient_common_location_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient#google_cloud_talent_v4beta1_services_event_service_EventServiceClient_common_organization_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient#google_cloud_talent_v4beta1_services_event_service_EventServiceClient_common_project_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceClient.company_path
    
    
    company_path(project: str, tenant: str, company: str) -> str

Returns a fully-qualified company string.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceClient.company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient#google_cloud_talent_v4beta1_services_event_service_EventServiceClient_company_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceClient.create_client_event
    
    
    create_client_event(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.event_service.CreateClientEventRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        client_event: typing.Optional[
            google.cloud.talent_v4beta1.types.event.ClientEvent
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4beta1.types.event.ClientEvent

Report events issued when end user interacts with customer's application that uses Cloud Talent Solution.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceClient.create_client_event](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient#google_cloud_talent_v4beta1_services_event_service_EventServiceClient_create_client_event)

### google.cloud.talent_v4beta1.services.event_service.EventServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient#google_cloud_talent_v4beta1_services_event_service_EventServiceClient_from_service_account_file)

### google.cloud.talent_v4beta1.services.event_service.EventServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient#google_cloud_talent_v4beta1_services_event_service_EventServiceClient_from_service_account_info)

### google.cloud.talent_v4beta1.services.event_service.EventServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient#google_cloud_talent_v4beta1_services_event_service_EventServiceClient_from_service_account_json)

### google.cloud.talent_v4beta1.services.event_service.EventServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient#google_cloud_talent_v4beta1_services_event_service_EventServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.talent_v4beta1.services.event_service.EventServiceClient.get_operation
    
    
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

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceClient.get_operation](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient#google_cloud_talent_v4beta1_services_event_service_EventServiceClient_get_operation)

### google.cloud.talent_v4beta1.services.event_service.EventServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient#google_cloud_talent_v4beta1_services_event_service_EventServiceClient_parse_common_billing_account_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient#google_cloud_talent_v4beta1_services_event_service_EventServiceClient_parse_common_folder_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient#google_cloud_talent_v4beta1_services_event_service_EventServiceClient_parse_common_location_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient#google_cloud_talent_v4beta1_services_event_service_EventServiceClient_parse_common_organization_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient#google_cloud_talent_v4beta1_services_event_service_EventServiceClient_parse_common_project_path)

### google.cloud.talent_v4beta1.services.event_service.EventServiceClient.parse_company_path
    
    
    parse_company_path(path: str) -> typing.Dict[str, str]

Parses a company path into its component segments.

See more: [google.cloud.talent_v4beta1.services.event_service.EventServiceClient.parse_company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.event_service.EventServiceClient#google_cloud_talent_v4beta1_services_event_service_EventServiceClient_parse_company_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient
    
    
    JobServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.talent_v4beta1.services.job_service.transports.base.JobServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.talent_v4beta1.services.job_service.transports.base.JobServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the job service async client.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_JobServiceAsyncClient)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.batch_create_jobs
    
    
    batch_create_jobs(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.job_service.BatchCreateJobsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        jobs: typing.Optional[
            typing.MutableSequence[google.cloud.talent_v4beta1.types.job.Job]
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

Begins executing a batch create jobs operation.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.batch_create_jobs](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_batch_create_jobs)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.batch_delete_jobs
    
    
    batch_delete_jobs(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.job_service.BatchDeleteJobsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Deletes a list of xref_Jobs by filter.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.batch_delete_jobs](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_batch_delete_jobs)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.batch_update_jobs
    
    
    batch_update_jobs(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.job_service.BatchUpdateJobsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        jobs: typing.Optional[
            typing.MutableSequence[google.cloud.talent_v4beta1.types.job.Job]
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

Begins executing a batch update jobs operation.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.batch_update_jobs](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_batch_update_jobs)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_common_billing_account_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_common_folder_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_common_location_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_common_organization_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_common_project_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.company_path
    
    
    company_path(project: str, tenant: str, company: str) -> str

Returns a fully-qualified company string.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_company_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.create_job
    
    
    create_job(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.job_service.CreateJobRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        job: typing.Optional[google.cloud.talent_v4beta1.types.job.Job] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4beta1.types.job.Job

Creates a new job.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.create_job](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_create_job)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.delete_job
    
    
    delete_job(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.job_service.DeleteJobRequest, dict
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

Deletes the specified job.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.delete_job](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_delete_job)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_from_service_account_file)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_from_service_account_info)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_from_service_account_json)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.get_job
    
    
    get_job(
        request: typing.Optional[
            typing.Union[google.cloud.talent_v4beta1.types.job_service.GetJobRequest, dict]
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
    ) -> google.cloud.talent_v4beta1.types.job.Job

Retrieves the specified job, whose status is OPEN or recently EXPIRED within the last 90 days.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.get_job](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_get_job)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_get_operation)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.talent_v4beta1.services.job_service.transports.base.JobServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_get_transport_class)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.job_path
    
    
    job_path(project: str, tenant: str, job: str) -> str

Returns a fully-qualified job string.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.job_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_job_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.list_jobs
    
    
    list_jobs(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.job_service.ListJobsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4beta1.services.job_service.pagers.ListJobsAsyncPager

Lists jobs by filter.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.list_jobs](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_list_jobs)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_parse_common_folder_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_parse_common_location_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_parse_common_organization_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_parse_common_project_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.parse_company_path
    
    
    parse_company_path(path: str) -> typing.Dict[str, str]

Parses a company path into its component segments.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.parse_company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_parse_company_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.parse_job_path
    
    
    parse_job_path(path: str) -> typing.Dict[str, str]

Parses a job path into its component segments.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.parse_job_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_parse_job_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.search_jobs
    
    
    search_jobs(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.job_service.SearchJobsRequest, dict
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
    ) -> google.cloud.talent_v4beta1.services.job_service.pagers.SearchJobsAsyncPager

Searches for jobs using the provided xref_SearchJobsRequest.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.search_jobs](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_search_jobs)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.search_jobs_for_alert
    
    
    search_jobs_for_alert(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.job_service.SearchJobsRequest, dict
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
        google.cloud.talent_v4beta1.services.job_service.pagers.SearchJobsForAlertAsyncPager
    )

Searches for jobs using the provided xref_SearchJobsRequest.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.search_jobs_for_alert](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_search_jobs_for_alert)

### google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.update_job
    
    
    update_job(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.job_service.UpdateJobRequest, dict
            ]
        ] = None,
        *,
        job: typing.Optional[google.cloud.talent_v4beta1.types.job.Job] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4beta1.types.job.Job

Updates specified job.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient.update_job](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceAsyncClient#google_cloud_talent_v4beta1_services_job_service_JobServiceAsyncClient_update_job)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient
    
    
    JobServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.talent_v4beta1.services.job_service.transports.base.JobServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.talent_v4beta1.services.job_service.transports.base.JobServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the job service client.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_JobServiceClient)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.**exit**](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient___exit__)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.batch_create_jobs
    
    
    batch_create_jobs(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.job_service.BatchCreateJobsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        jobs: typing.Optional[
            typing.MutableSequence[google.cloud.talent_v4beta1.types.job.Job]
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

Begins executing a batch create jobs operation.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.batch_create_jobs](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_batch_create_jobs)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.batch_delete_jobs
    
    
    batch_delete_jobs(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.job_service.BatchDeleteJobsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> None

Deletes a list of xref_Jobs by filter.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.batch_delete_jobs](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_batch_delete_jobs)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.batch_update_jobs
    
    
    batch_update_jobs(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.job_service.BatchUpdateJobsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        jobs: typing.Optional[
            typing.MutableSequence[google.cloud.talent_v4beta1.types.job.Job]
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

Begins executing a batch update jobs operation.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.batch_update_jobs](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_batch_update_jobs)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_common_billing_account_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_common_folder_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_common_location_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_common_organization_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_common_project_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.company_path
    
    
    company_path(project: str, tenant: str, company: str) -> str

Returns a fully-qualified company string.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_company_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.create_job
    
    
    create_job(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.job_service.CreateJobRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        job: typing.Optional[google.cloud.talent_v4beta1.types.job.Job] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4beta1.types.job.Job

Creates a new job.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.create_job](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_create_job)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.delete_job
    
    
    delete_job(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.job_service.DeleteJobRequest, dict
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

Deletes the specified job.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.delete_job](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_delete_job)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_from_service_account_file)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_from_service_account_info)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_from_service_account_json)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.get_job
    
    
    get_job(
        request: typing.Optional[
            typing.Union[google.cloud.talent_v4beta1.types.job_service.GetJobRequest, dict]
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
    ) -> google.cloud.talent_v4beta1.types.job.Job

Retrieves the specified job, whose status is OPEN or recently EXPIRED within the last 90 days.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.get_job](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_get_job)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.get_operation
    
    
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

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.get_operation](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_get_operation)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.job_path
    
    
    job_path(project: str, tenant: str, job: str) -> str

Returns a fully-qualified job string.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.job_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_job_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.list_jobs
    
    
    list_jobs(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.job_service.ListJobsRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        filter: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4beta1.services.job_service.pagers.ListJobsPager

Lists jobs by filter.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.list_jobs](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_list_jobs)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_parse_common_billing_account_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_parse_common_folder_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_parse_common_location_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_parse_common_organization_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_parse_common_project_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.parse_company_path
    
    
    parse_company_path(path: str) -> typing.Dict[str, str]

Parses a company path into its component segments.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.parse_company_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_parse_company_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.parse_job_path
    
    
    parse_job_path(path: str) -> typing.Dict[str, str]

Parses a job path into its component segments.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.parse_job_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_parse_job_path)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.search_jobs
    
    
    search_jobs(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.job_service.SearchJobsRequest, dict
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
    ) -> google.cloud.talent_v4beta1.services.job_service.pagers.SearchJobsPager

Searches for jobs using the provided xref_SearchJobsRequest.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.search_jobs](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_search_jobs)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.search_jobs_for_alert
    
    
    search_jobs_for_alert(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.job_service.SearchJobsRequest, dict
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
    ) -> google.cloud.talent_v4beta1.services.job_service.pagers.SearchJobsForAlertPager

Searches for jobs using the provided xref_SearchJobsRequest.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.search_jobs_for_alert](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_search_jobs_for_alert)

### google.cloud.talent_v4beta1.services.job_service.JobServiceClient.update_job
    
    
    update_job(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.job_service.UpdateJobRequest, dict
            ]
        ] = None,
        *,
        job: typing.Optional[google.cloud.talent_v4beta1.types.job.Job] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4beta1.types.job.Job

Updates specified job.

See more: [google.cloud.talent_v4beta1.services.job_service.JobServiceClient.update_job](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.JobServiceClient#google_cloud_talent_v4beta1_services_job_service_JobServiceClient_update_job)

### google.cloud.talent_v4beta1.services.job_service.pagers.ListJobsAsyncPager
    
    
    ListJobsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.talent_v4beta1.types.job_service.ListJobsResponse
            ],
        ],
        request: google.cloud.talent_v4beta1.types.job_service.ListJobsRequest,
        response: google.cloud.talent_v4beta1.types.job_service.ListJobsResponse,
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

See more: [google.cloud.talent_v4beta1.services.job_service.pagers.ListJobsAsyncPager](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.pagers.ListJobsAsyncPager#google_cloud_talent_v4beta1_services_job_service_pagers_ListJobsAsyncPager_ListJobsAsyncPager)

### google.cloud.talent_v4beta1.services.job_service.pagers.ListJobsPager
    
    
    ListJobsPager(
        method: typing.Callable[
            [...], google.cloud.talent_v4beta1.types.job_service.ListJobsResponse
        ],
        request: google.cloud.talent_v4beta1.types.job_service.ListJobsRequest,
        response: google.cloud.talent_v4beta1.types.job_service.ListJobsResponse,
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

See more: [google.cloud.talent_v4beta1.services.job_service.pagers.ListJobsPager](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.pagers.ListJobsPager#google_cloud_talent_v4beta1_services_job_service_pagers_ListJobsPager_ListJobsPager)

### google.cloud.talent_v4beta1.services.job_service.pagers.SearchJobsAsyncPager
    
    
    SearchJobsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.talent_v4beta1.types.job_service.SearchJobsResponse
            ],
        ],
        request: google.cloud.talent_v4beta1.types.job_service.SearchJobsRequest,
        response: google.cloud.talent_v4beta1.types.job_service.SearchJobsResponse,
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

See more: [google.cloud.talent_v4beta1.services.job_service.pagers.SearchJobsAsyncPager](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.pagers.SearchJobsAsyncPager#google_cloud_talent_v4beta1_services_job_service_pagers_SearchJobsAsyncPager_SearchJobsAsyncPager)

### google.cloud.talent_v4beta1.services.job_service.pagers.SearchJobsForAlertAsyncPager
    
    
    SearchJobsForAlertAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.talent_v4beta1.types.job_service.SearchJobsResponse
            ],
        ],
        request: google.cloud.talent_v4beta1.types.job_service.SearchJobsRequest,
        response: google.cloud.talent_v4beta1.types.job_service.SearchJobsResponse,
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

See more: [google.cloud.talent_v4beta1.services.job_service.pagers.SearchJobsForAlertAsyncPager](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.pagers.SearchJobsForAlertAsyncPager#google_cloud_talent_v4beta1_services_job_service_pagers_SearchJobsForAlertAsyncPager_SearchJobsForAlertAsyncPager)

### google.cloud.talent_v4beta1.services.job_service.pagers.SearchJobsForAlertPager
    
    
    SearchJobsForAlertPager(
        method: typing.Callable[
            [...], google.cloud.talent_v4beta1.types.job_service.SearchJobsResponse
        ],
        request: google.cloud.talent_v4beta1.types.job_service.SearchJobsRequest,
        response: google.cloud.talent_v4beta1.types.job_service.SearchJobsResponse,
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

See more: [google.cloud.talent_v4beta1.services.job_service.pagers.SearchJobsForAlertPager](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.pagers.SearchJobsForAlertPager#google_cloud_talent_v4beta1_services_job_service_pagers_SearchJobsForAlertPager_SearchJobsForAlertPager)

### google.cloud.talent_v4beta1.services.job_service.pagers.SearchJobsPager
    
    
    SearchJobsPager(
        method: typing.Callable[
            [...], google.cloud.talent_v4beta1.types.job_service.SearchJobsResponse
        ],
        request: google.cloud.talent_v4beta1.types.job_service.SearchJobsRequest,
        response: google.cloud.talent_v4beta1.types.job_service.SearchJobsResponse,
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

See more: [google.cloud.talent_v4beta1.services.job_service.pagers.SearchJobsPager](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.job_service.pagers.SearchJobsPager#google_cloud_talent_v4beta1_services_job_service_pagers_SearchJobsPager_SearchJobsPager)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient
    
    
    TenantServiceAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.talent_v4beta1.services.tenant_service.transports.base.TenantServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.talent_v4beta1.services.tenant_service.transports.base.TenantServiceTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the tenant service async client.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_TenantServiceAsyncClient)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_common_billing_account_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_common_folder_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_common_location_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_common_organization_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_common_project_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.create_tenant
    
    
    create_tenant(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.tenant_service.CreateTenantRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        tenant: typing.Optional[google.cloud.talent_v4beta1.types.tenant.Tenant] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4beta1.types.tenant.Tenant

Creates a new tenant entity.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.create_tenant](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_create_tenant)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.delete_tenant
    
    
    delete_tenant(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.tenant_service.DeleteTenantRequest, dict
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

Deletes specified tenant.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.delete_tenant](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_delete_tenant)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_from_service_account_file)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_from_service_account_info)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_from_service_account_json)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.get_operation
    
    
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

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_get_operation)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.get_tenant
    
    
    get_tenant(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.tenant_service.GetTenantRequest, dict
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
    ) -> google.cloud.talent_v4beta1.types.tenant.Tenant

Retrieves specified tenant.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.get_tenant](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_get_tenant)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.talent_v4beta1.services.tenant_service.transports.base.TenantServiceTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_get_transport_class)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.list_tenants
    
    
    list_tenants(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.tenant_service.ListTenantsRequest, dict
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
    ) -> google.cloud.talent_v4beta1.services.tenant_service.pagers.ListTenantsAsyncPager

Lists all tenants associated with the project.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.list_tenants](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_list_tenants)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_parse_common_billing_account_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_parse_common_folder_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_parse_common_location_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_parse_common_organization_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_parse_common_project_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.parse_tenant_path
    
    
    parse_tenant_path(path: str) -> typing.Dict[str, str]

Parses a tenant path into its component segments.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.parse_tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_parse_tenant_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.tenant_path
    
    
    tenant_path(project: str, tenant: str) -> str

Returns a fully-qualified tenant string.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_tenant_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.update_tenant
    
    
    update_tenant(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.tenant_service.UpdateTenantRequest, dict
            ]
        ] = None,
        *,
        tenant: typing.Optional[google.cloud.talent_v4beta1.types.tenant.Tenant] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4beta1.types.tenant.Tenant

Updates specified tenant.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient.update_tenant](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceAsyncClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceAsyncClient_update_tenant)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient
    
    
    TenantServiceClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.talent_v4beta1.services.tenant_service.transports.base.TenantServiceTransport,
                typing.Callable[
                    [...],
                    google.cloud.talent_v4beta1.services.tenant_service.transports.base.TenantServiceTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the tenant service client.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_TenantServiceClient)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.**exit**](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient___exit__)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_common_billing_account_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_common_folder_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_common_location_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_common_organization_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_common_project_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.create_tenant
    
    
    create_tenant(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.tenant_service.CreateTenantRequest, dict
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        tenant: typing.Optional[google.cloud.talent_v4beta1.types.tenant.Tenant] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4beta1.types.tenant.Tenant

Creates a new tenant entity.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.create_tenant](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_create_tenant)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.delete_tenant
    
    
    delete_tenant(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.tenant_service.DeleteTenantRequest, dict
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

Deletes specified tenant.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.delete_tenant](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_delete_tenant)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.from_service_account_file](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_from_service_account_file)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.from_service_account_info](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_from_service_account_info)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.from_service_account_json](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_from_service_account_json)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_get_mtls_endpoint_and_cert_source)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.get_operation
    
    
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

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.get_operation](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_get_operation)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.get_tenant
    
    
    get_tenant(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.tenant_service.GetTenantRequest, dict
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
    ) -> google.cloud.talent_v4beta1.types.tenant.Tenant

Retrieves specified tenant.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.get_tenant](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_get_tenant)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.list_tenants
    
    
    list_tenants(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.tenant_service.ListTenantsRequest, dict
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
    ) -> google.cloud.talent_v4beta1.services.tenant_service.pagers.ListTenantsPager

Lists all tenants associated with the project.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.list_tenants](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_list_tenants)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_parse_common_billing_account_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_parse_common_folder_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_parse_common_location_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_parse_common_organization_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_parse_common_project_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.parse_tenant_path
    
    
    parse_tenant_path(path: str) -> typing.Dict[str, str]

Parses a tenant path into its component segments.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.parse_tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_parse_tenant_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.tenant_path
    
    
    tenant_path(project: str, tenant: str) -> str

Returns a fully-qualified tenant string.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.tenant_path](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_tenant_path)

### google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.update_tenant
    
    
    update_tenant(
        request: typing.Optional[
            typing.Union[
                google.cloud.talent_v4beta1.types.tenant_service.UpdateTenantRequest, dict
            ]
        ] = None,
        *,
        tenant: typing.Optional[google.cloud.talent_v4beta1.types.tenant.Tenant] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.talent_v4beta1.types.tenant.Tenant

Updates specified tenant.

See more: [google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient.update_tenant](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.TenantServiceClient#google_cloud_talent_v4beta1_services_tenant_service_TenantServiceClient_update_tenant)

### google.cloud.talent_v4beta1.services.tenant_service.pagers.ListTenantsAsyncPager
    
    
    ListTenantsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.talent_v4beta1.types.tenant_service.ListTenantsResponse
            ],
        ],
        request: google.cloud.talent_v4beta1.types.tenant_service.ListTenantsRequest,
        response: google.cloud.talent_v4beta1.types.tenant_service.ListTenantsResponse,
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

See more: [google.cloud.talent_v4beta1.services.tenant_service.pagers.ListTenantsAsyncPager](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.pagers.ListTenantsAsyncPager#google_cloud_talent_v4beta1_services_tenant_service_pagers_ListTenantsAsyncPager_ListTenantsAsyncPager)

### google.cloud.talent_v4beta1.services.tenant_service.pagers.ListTenantsPager
    
    
    ListTenantsPager(
        method: typing.Callable[
            [...], google.cloud.talent_v4beta1.types.tenant_service.ListTenantsResponse
        ],
        request: google.cloud.talent_v4beta1.types.tenant_service.ListTenantsRequest,
        response: google.cloud.talent_v4beta1.types.tenant_service.ListTenantsResponse,
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

See more: [google.cloud.talent_v4beta1.services.tenant_service.pagers.ListTenantsPager](https://cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4beta1.services.tenant_service.pagers.ListTenantsPager#google_cloud_talent_v4beta1_services_tenant_service_pagers_ListTenantsPager_ListTenantsPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
