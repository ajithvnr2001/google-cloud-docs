---
url: https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient
title: Class CompanyServiceAsyncClient (2.22.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:09.432923+00:00
---

# Class CompanyServiceAsyncClient (2.22.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CompanyServiceAsyncClient (2.22.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.22.0 (latest)  2.21.0  2.20.0  2.19.0  2.18.0  2.17.2  2.16.0  2.15.0  2.14.1  2.13.5  2.12.0  2.11.1  2.10.1  2.9.1  2.8.0  2.7.3  2.6.0  2.5.2  2.4.0  2.3.0  2.2.1  2.1.0  2.0.0  1.0.2  0.6.3  0.5.0  0.4.0  0.3.0 
    
    
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

A service that handles company management, including CRUD and enumeration.

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
`CompanyServiceTransport` | The transport used by the client instance.  
  
### universe_domain

Return the universe domain used by the client instance.

**Returns**  
---  
**Type** | **Description**  
`str` | The universe domain used by the client instance.  
  
## Methods 

### CompanyServiceAsyncClient
    
    
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

**Parameters**  
---  
**Name** | **Description**  
`credentials` |  `Optional[google.auth.credentials.Credentials]`   
The authorization credentials to attach to requests. These credentials identify the application to the service; if none are specified, the client will attempt to ascertain the credentials from the environment.  
`transport` |  `Optional[Union[str,CompanyServiceTransport,Callable[..., CompanyServiceTransport]]]`   
The transport to use, or a Callable that constructs and returns a new transport to use. If a Callable is given, it will be called with the same set of initialization arguments as used in the CompanyServiceTransport constructor. If set to None, a transport is chosen automatically.  
`client_options` |  `Optional[Union[google.api_core.client_options.ClientOptions, dict]]`   
Custom options for the client. 1. The `api_endpoint` property can be used to override the default endpoint provided by the client when `transport` is not explicitly provided. Only if this property is not set and `transport` was not explicitly provided, the endpoint is determined by the GOOGLE_API_USE_MTLS_ENDPOINT environment variable, which have one of the following values: "always" (always use the default mTLS endpoint), "never" (always use the default regular endpoint) and "auto" (auto-switch to the default mTLS endpoint if client certificate is present; this is the default value). 2. If the GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable is "true", then the `client_cert_source` property can be used to provide a client certificate for mTLS transport. If not provided, the default SSL client certificate will be used if present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not set, no client certificate will be used. 3. The `universe_domain` property can be used to override the default "googleapis.com" universe. Note that `api_endpoint` property still takes precedence; and `universe_domain` is currently not supported for mTLS.  
`client_info` |  `google.api_core.gapic_v1.client_info.ClientInfo`   
The client info used to send a user-agent string along with API requests. If `None`, then default info will be used. Generally, you only need to set this if you're developing your own client library.  
**Exceptions**  
---  
**Type** | **Description**  
`google.auth.exceptions.MutualTlsChannelError` | If mutual TLS transport creation failed for any reason.  
  
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

### company_path
    
    
    company_path(project: str, tenant: str, company: str) -> str

Returns a fully-qualified company string.

### create_company
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [talent_v4](https://docs.cloud.google.com/python/docs/reference/talent/latest)
    
    async def sample_create_company():
        # Create a client
        client = [talent_v4](https://docs.cloud.google.com/python/docs/reference/talent/latest).[CompanyServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        company = [talent_v4](https://docs.cloud.google.com/python/docs/reference/talent/latest).[Company](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Company.html)()
        company.display_name = "display_name_value"
        company.external_id = "external_id_value"
    
        request = [talent_v4](https://docs.cloud.google.com/python/docs/reference/talent/latest).[CreateCompanyRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CreateCompanyRequest.html)(
            parent="parent_value",
            company=company,
        )
    
        # Make the request
        response = await client.[create_company](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.html#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_create_company)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.talent_v4.types.CreateCompanyRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.CreateCompanyRequest), dict]]`   
The request object. The Request of the CreateCompany method.  
`parent` |  ``str``   
Required. Resource name of the tenant under which the company is created. The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar". This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`company` |  `[Company](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Company)`   
Required. The company to be created. This corresponds to the `company` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.talent_v4.types.Company](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Company)` | A Company resource represents a company in the service. A company is the entity that owns job postings, that is, the hiring entity responsible for employing applicants for the job position.  
  
### delete_company
    
    
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

Deletes specified company. Prerequisite: The company has no jobs associated with it.
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [talent_v4](https://docs.cloud.google.com/python/docs/reference/talent/latest)
    
    async def sample_delete_company():
        # Create a client
        client = [talent_v4](https://docs.cloud.google.com/python/docs/reference/talent/latest).[CompanyServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [talent_v4](https://docs.cloud.google.com/python/docs/reference/talent/latest).[DeleteCompanyRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.DeleteCompanyRequest.html)(
            name="name_value",
        )
    
        # Make the request
        await client.[delete_company](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.html#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_delete_company)(request=request)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.talent_v4.types.DeleteCompanyRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.DeleteCompanyRequest), dict]]`   
The request object. Request to delete a company.  
`name` |  ``str``   
Required. The resource name of the company to be deleted. The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/foo/tenants/bar/companies/baz". This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
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
`CompanyServiceAsyncClient` | The constructed client.  
  
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
`CompanyServiceAsyncClient` | The constructed client.  
  
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
`CompanyServiceAsyncClient` | The constructed client.  
  
### get_company
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [talent_v4](https://docs.cloud.google.com/python/docs/reference/talent/latest)
    
    async def sample_get_company():
        # Create a client
        client = [talent_v4](https://docs.cloud.google.com/python/docs/reference/talent/latest).[CompanyServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [talent_v4](https://docs.cloud.google.com/python/docs/reference/talent/latest).[GetCompanyRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.GetCompanyRequest.html)(
            name="name_value",
        )
    
        # Make the request
        response = await client.[get_company](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.html#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_get_company)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.talent_v4.types.GetCompanyRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.GetCompanyRequest), dict]]`   
The request object. Request for getting a company by name.  
`name` |  ``str``   
Required. The resource name of the company to be retrieved. The format is "projects/{project_id}/tenants/{tenant_id}/companies/{company_id}", for example, "projects/api-test-project/tenants/foo/companies/bar". This corresponds to the `name` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.talent_v4.types.Company](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Company)` | A Company resource represents a company in the service. A company is the entity that owns job postings, that is, the hiring entity responsible for employing applicants for the job position.  
  
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
  
### get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.talent_v4.services.company_service.transports.base.CompanyServiceTransport
    ]

Returns an appropriate transport class.

**Parameter**  
---  
**Name** | **Description**  
`label` |  `typing.Optional[str]`   
The name of the desired transport. If none is provided, then the first transport in the registry is used.  
  
### list_companies
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [talent_v4](https://docs.cloud.google.com/python/docs/reference/talent/latest)
    
    async def sample_list_companies():
        # Create a client
        client = [talent_v4](https://docs.cloud.google.com/python/docs/reference/talent/latest).[CompanyServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        request = [talent_v4](https://docs.cloud.google.com/python/docs/reference/talent/latest).[ListCompaniesRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListCompaniesRequest.html)(
            parent="parent_value",
        )
    
        # Make the request
        page_result = client.[list_companies](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.html#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_list_companies)(request=request)
    
        # Handle the response
        async for response in page_result:
            print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.talent_v4.types.ListCompaniesRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.ListCompaniesRequest), dict]]`   
The request object. List companies for which the client has ACL visibility.  
`parent` |  ``str``   
Required. Resource name of the tenant under which the company is created. The format is "projects/{project_id}/tenants/{tenant_id}", for example, "projects/foo/tenants/bar". This corresponds to the `parent` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.talent_v4.services.company_service.pagers.ListCompaniesAsyncPager](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.pagers.ListCompaniesAsyncPager)` | The List companies response object. Iterating over this object will yield results and resolve additional pages automatically.  
  
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

### parse_company_path
    
    
    parse_company_path(path: str) -> typing.Dict[str, str]

Parses a company path into its component segments.

### parse_tenant_path
    
    
    parse_tenant_path(path: str) -> typing.Dict[str, str]

Parses a tenant path into its component segments.

### tenant_path
    
    
    tenant_path(project: str, tenant: str) -> str

Returns a fully-qualified tenant string.

### update_company
    
    
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
    
    
    # This snippet has been automatically generated and should be regarded as a
    # code template only.
    # It will require modifications to work:
    # - It may require correct/in-range values for request initialization.
    # - It may require specifying regional endpoints when creating the service
    #   client as shown in:
    #   https://googleapis.dev/python/google-api-core/latest/client_options.html
    from google.cloud import [talent_v4](https://docs.cloud.google.com/python/docs/reference/talent/latest)
    
    async def sample_update_company():
        # Create a client
        client = [talent_v4](https://docs.cloud.google.com/python/docs/reference/talent/latest).[CompanyServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.html)()
    
        # Initialize request argument(s)
        company = [talent_v4](https://docs.cloud.google.com/python/docs/reference/talent/latest).[Company](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Company.html)()
        company.display_name = "display_name_value"
        company.external_id = "external_id_value"
    
        request = [talent_v4](https://docs.cloud.google.com/python/docs/reference/talent/latest).[UpdateCompanyRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.UpdateCompanyRequest.html)(
            company=company,
        )
    
        # Make the request
        response = await client.[update_company](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.services.company_service.CompanyServiceAsyncClient.html#google_cloud_talent_v4_services_company_service_CompanyServiceAsyncClient_update_company)(request=request)
    
        # Handle the response
        print(response)
    

**Parameters**  
---  
**Name** | **Description**  
`request` |  `Optional[Union[[google.cloud.talent_v4.types.UpdateCompanyRequest](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.UpdateCompanyRequest), dict]]`   
The request object. Request for updating a specified company.  
`company` |  `[Company](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Company)`   
Required. The company resource to replace the current resource in the system. This corresponds to the `company` field on the `request` instance; if `request` is provided, this should not be set.  
`update_mask` |  ``google.protobuf.field_mask_pb2.FieldMask``   
Strongly recommended for the best service experience. If update_mask is provided, only the specified fields in company are updated. Otherwise all the fields are updated. A field mask to specify the company fields to be updated. Only top level fields of [Company](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Company) are supported. This corresponds to the `update_mask` field on the `request` instance; if `request` is provided, this should not be set.  
`retry` |  `google.api_core.retry_async.AsyncRetry`   
Designation of what errors, if any, should be retried.  
`timeout` |  `float`   
The timeout for this request.  
`metadata` |  `Sequence[Tuple[str, Union[str, bytes]]]`   
Key/value pairs which should be sent along with the request as metadata. Normally, each value must be of type `str`, but for metadata keys ending with the suffix `-bin`, the corresponding values must be of type `bytes`.  
**Returns**  
---  
**Type** | **Description**  
`[google.cloud.talent_v4.types.Company](https://docs.cloud.google.com/python/docs/reference/talent/latest/google.cloud.talent_v4.types.Company)` | A Company resource represents a company in the service. A company is the entity that owns job postings, that is, the hiring entity responsible for employing applicants for the job position.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
