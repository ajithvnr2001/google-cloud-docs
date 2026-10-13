---
url: https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/summary_method/
title: Package Methods (1.21.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:06:17.331171+00:00
---

# Package Methods (1.21.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudbilling/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (1.21.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.21.0 (latest)  1.20.0  1.19.0  1.18.0  1.17.0  1.16.3  1.15.0  1.14.1  1.13.6  1.12.1  1.11.5  1.10.1  1.9.1  1.8.0  1.7.3  1.6.1  1.5.1  1.4.1  1.3.4  1.2.1  1.1.1  1.0.0  0.1.0 

Summary of entries of Methods for cloudbilling.

## 

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient
    
    
    CloudBillingAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.billing_v1.services.cloud_billing.transports.base.CloudBillingTransport,
                typing.Callable[
                    [...],
                    google.cloud.billing_v1.services.cloud_billing.transports.base.CloudBillingTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the cloud billing async client.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_CloudBillingAsyncClient)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.billing_account_path
    
    
    billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.billing_account_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_billing_account_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_common_billing_account_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_common_folder_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_common_location_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_common_organization_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_common_project_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.create_billing_account
    
    
    create_billing_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.billing_v1.types.cloud_billing.CreateBillingAccountRequest,
                dict,
            ]
        ] = None,
        *,
        billing_account: typing.Optional[
            google.cloud.billing_v1.types.cloud_billing.BillingAccount
        ] = None,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.billing_v1.types.cloud_billing.BillingAccount

This method creates `billing subaccounts <https://cloud.google.com/billing/docs/concepts#subaccounts>`__.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.create_billing_account](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_create_billing_account)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_from_service_account_file)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_from_service_account_info)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_from_service_account_json)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.get_billing_account
    
    
    get_billing_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.billing_v1.types.cloud_billing.GetBillingAccountRequest, dict
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
    ) -> google.cloud.billing_v1.types.cloud_billing.BillingAccount

Gets information about a billing account.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.get_billing_account](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_get_billing_account)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.get_iam_policy
    
    
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

Gets the access control policy for a billing account.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_get_iam_policy)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.get_project_billing_info
    
    
    get_project_billing_info(
        request: typing.Optional[
            typing.Union[
                google.cloud.billing_v1.types.cloud_billing.GetProjectBillingInfoRequest,
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
    ) -> google.cloud.billing_v1.types.cloud_billing.ProjectBillingInfo

Gets the billing information for a project.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.get_project_billing_info](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_get_project_billing_info)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.billing_v1.services.cloud_billing.transports.base.CloudBillingTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_get_transport_class)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.list_billing_accounts
    
    
    list_billing_accounts(
        request: typing.Optional[
            typing.Union[
                google.cloud.billing_v1.types.cloud_billing.ListBillingAccountsRequest, dict
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
        google.cloud.billing_v1.services.cloud_billing.pagers.ListBillingAccountsAsyncPager
    )

Lists the billing accounts that the current authenticated user has permission to `view <https://cloud.google.com/billing/docs/how-to/billing-access>`__.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.list_billing_accounts](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_list_billing_accounts)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.list_project_billing_info
    
    
    list_project_billing_info(
        request: typing.Optional[
            typing.Union[
                google.cloud.billing_v1.types.cloud_billing.ListProjectBillingInfoRequest,
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
    ) -> (
        google.cloud.billing_v1.services.cloud_billing.pagers.ListProjectBillingInfoAsyncPager
    )

Lists the projects associated with a billing account.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.list_project_billing_info](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_list_project_billing_info)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.move_billing_account
    
    
    move_billing_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.billing_v1.types.cloud_billing.MoveBillingAccountRequest, dict
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
    ) -> google.cloud.billing_v1.types.cloud_billing.BillingAccount

Changes which parent organization a billing account belongs to.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.move_billing_account](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_move_billing_account)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.organization_path
    
    
    organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.organization_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_organization_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.parse_billing_account_path
    
    
    parse_billing_account_path(path: str) -> typing.Dict[str, str]

Parses a billing_account path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.parse_billing_account_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_parse_billing_account_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_parse_common_billing_account_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_parse_common_folder_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_parse_common_location_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_parse_common_organization_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_parse_common_project_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.parse_organization_path
    
    
    parse_organization_path(path: str) -> typing.Dict[str, str]

Parses a organization path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.parse_organization_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_parse_organization_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.parse_project_billing_info_path
    
    
    parse_project_billing_info_path(path: str) -> typing.Dict[str, str]

Parses a project_billing_info path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.parse_project_billing_info_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_parse_project_billing_info_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.parse_project_path
    
    
    parse_project_path(path: str) -> typing.Dict[str, str]

Parses a project path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.parse_project_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_parse_project_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.project_billing_info_path
    
    
    project_billing_info_path(project: str) -> str

Returns a fully-qualified project_billing_info string.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.project_billing_info_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_project_billing_info_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.project_path
    
    
    project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.project_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_project_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.set_iam_policy
    
    
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

Sets the access control policy for a billing account.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_set_iam_policy)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.test_iam_permissions
    
    
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

Tests the access control policy for a billing account.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_test_iam_permissions)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.update_billing_account
    
    
    update_billing_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.billing_v1.types.cloud_billing.UpdateBillingAccountRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        account: typing.Optional[
            google.cloud.billing_v1.types.cloud_billing.BillingAccount
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.billing_v1.types.cloud_billing.BillingAccount

Updates a billing account's fields.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.update_billing_account](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_update_billing_account)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.update_project_billing_info
    
    
    update_project_billing_info(
        request: typing.Optional[
            typing.Union[
                google.cloud.billing_v1.types.cloud_billing.UpdateProjectBillingInfoRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        project_billing_info: typing.Optional[
            google.cloud.billing_v1.types.cloud_billing.ProjectBillingInfo
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.billing_v1.types.cloud_billing.ProjectBillingInfo

Sets or updates the billing account associated with a project.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient.update_project_billing_info](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingAsyncClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingAsyncClient_update_project_billing_info)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient
    
    
    CloudBillingClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.billing_v1.services.cloud_billing.transports.base.CloudBillingTransport,
                typing.Callable[
                    [...],
                    google.cloud.billing_v1.services.cloud_billing.transports.base.CloudBillingTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the cloud billing client.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_CloudBillingClient)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.**exit**](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient___exit__)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.billing_account_path
    
    
    billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.billing_account_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_billing_account_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_common_billing_account_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.common_folder_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_common_folder_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.common_location_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_common_location_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.common_organization_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_common_organization_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.common_project_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_common_project_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.create_billing_account
    
    
    create_billing_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.billing_v1.types.cloud_billing.CreateBillingAccountRequest,
                dict,
            ]
        ] = None,
        *,
        billing_account: typing.Optional[
            google.cloud.billing_v1.types.cloud_billing.BillingAccount
        ] = None,
        parent: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.billing_v1.types.cloud_billing.BillingAccount

This method creates `billing subaccounts <https://cloud.google.com/billing/docs/concepts#subaccounts>`__.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.create_billing_account](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_create_billing_account)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.from_service_account_file](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_from_service_account_file)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.from_service_account_info](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_from_service_account_info)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.from_service_account_json](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_from_service_account_json)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.get_billing_account
    
    
    get_billing_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.billing_v1.types.cloud_billing.GetBillingAccountRequest, dict
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
    ) -> google.cloud.billing_v1.types.cloud_billing.BillingAccount

Gets information about a billing account.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.get_billing_account](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_get_billing_account)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.get_iam_policy
    
    
    get_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.GetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Gets the access control policy for a billing account.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.get_iam_policy](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_get_iam_policy)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_get_mtls_endpoint_and_cert_source)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.get_project_billing_info
    
    
    get_project_billing_info(
        request: typing.Optional[
            typing.Union[
                google.cloud.billing_v1.types.cloud_billing.GetProjectBillingInfoRequest,
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
    ) -> google.cloud.billing_v1.types.cloud_billing.ProjectBillingInfo

Gets the billing information for a project.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.get_project_billing_info](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_get_project_billing_info)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.list_billing_accounts
    
    
    list_billing_accounts(
        request: typing.Optional[
            typing.Union[
                google.cloud.billing_v1.types.cloud_billing.ListBillingAccountsRequest, dict
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
    ) -> google.cloud.billing_v1.services.cloud_billing.pagers.ListBillingAccountsPager

Lists the billing accounts that the current authenticated user has permission to `view <https://cloud.google.com/billing/docs/how-to/billing-access>`__.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.list_billing_accounts](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_list_billing_accounts)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.list_project_billing_info
    
    
    list_project_billing_info(
        request: typing.Optional[
            typing.Union[
                google.cloud.billing_v1.types.cloud_billing.ListProjectBillingInfoRequest,
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
    ) -> google.cloud.billing_v1.services.cloud_billing.pagers.ListProjectBillingInfoPager

Lists the projects associated with a billing account.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.list_project_billing_info](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_list_project_billing_info)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.move_billing_account
    
    
    move_billing_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.billing_v1.types.cloud_billing.MoveBillingAccountRequest, dict
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
    ) -> google.cloud.billing_v1.types.cloud_billing.BillingAccount

Changes which parent organization a billing account belongs to.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.move_billing_account](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_move_billing_account)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.organization_path
    
    
    organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.organization_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_organization_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.parse_billing_account_path
    
    
    parse_billing_account_path(path: str) -> typing.Dict[str, str]

Parses a billing_account path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.parse_billing_account_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_parse_billing_account_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_parse_common_billing_account_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_parse_common_folder_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_parse_common_location_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_parse_common_organization_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_parse_common_project_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.parse_organization_path
    
    
    parse_organization_path(path: str) -> typing.Dict[str, str]

Parses a organization path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.parse_organization_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_parse_organization_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.parse_project_billing_info_path
    
    
    parse_project_billing_info_path(path: str) -> typing.Dict[str, str]

Parses a project_billing_info path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.parse_project_billing_info_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_parse_project_billing_info_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.parse_project_path
    
    
    parse_project_path(path: str) -> typing.Dict[str, str]

Parses a project path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.parse_project_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_parse_project_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.project_billing_info_path
    
    
    project_billing_info_path(project: str) -> str

Returns a fully-qualified project_billing_info string.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.project_billing_info_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_project_billing_info_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.project_path
    
    
    project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.project_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_project_path)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.set_iam_policy
    
    
    set_iam_policy(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.SetIamPolicyRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.policy_pb2.Policy

Sets the access control policy for a billing account.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.set_iam_policy](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_set_iam_policy)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.test_iam_permissions
    
    
    test_iam_permissions(
        request: typing.Optional[
            typing.Union[google.iam.v1.iam_policy_pb2.TestIamPermissionsRequest, dict]
        ] = None,
        *,
        resource: typing.Optional[str] = None,
        permissions: typing.Optional[typing.MutableSequence[str]] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.iam.v1.iam_policy_pb2.TestIamPermissionsResponse

Tests the access control policy for a billing account.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_test_iam_permissions)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.update_billing_account
    
    
    update_billing_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.billing_v1.types.cloud_billing.UpdateBillingAccountRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        account: typing.Optional[
            google.cloud.billing_v1.types.cloud_billing.BillingAccount
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.billing_v1.types.cloud_billing.BillingAccount

Updates a billing account's fields.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.update_billing_account](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_update_billing_account)

### google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.update_project_billing_info
    
    
    update_project_billing_info(
        request: typing.Optional[
            typing.Union[
                google.cloud.billing_v1.types.cloud_billing.UpdateProjectBillingInfoRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        project_billing_info: typing.Optional[
            google.cloud.billing_v1.types.cloud_billing.ProjectBillingInfo
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.billing_v1.types.cloud_billing.ProjectBillingInfo

Sets or updates the billing account associated with a project.

See more: [google.cloud.billing_v1.services.cloud_billing.CloudBillingClient.update_project_billing_info](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.CloudBillingClient#google_cloud_billing_v1_services_cloud_billing_CloudBillingClient_update_project_billing_info)

### google.cloud.billing_v1.services.cloud_billing.pagers.ListBillingAccountsAsyncPager
    
    
    ListBillingAccountsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.billing_v1.types.cloud_billing.ListBillingAccountsResponse
            ],
        ],
        request: google.cloud.billing_v1.types.cloud_billing.ListBillingAccountsRequest,
        response: google.cloud.billing_v1.types.cloud_billing.ListBillingAccountsResponse,
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

See more: [google.cloud.billing_v1.services.cloud_billing.pagers.ListBillingAccountsAsyncPager](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.pagers.ListBillingAccountsAsyncPager#google_cloud_billing_v1_services_cloud_billing_pagers_ListBillingAccountsAsyncPager_ListBillingAccountsAsyncPager)

### google.cloud.billing_v1.services.cloud_billing.pagers.ListBillingAccountsPager
    
    
    ListBillingAccountsPager(
        method: typing.Callable[
            [...], google.cloud.billing_v1.types.cloud_billing.ListBillingAccountsResponse
        ],
        request: google.cloud.billing_v1.types.cloud_billing.ListBillingAccountsRequest,
        response: google.cloud.billing_v1.types.cloud_billing.ListBillingAccountsResponse,
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

See more: [google.cloud.billing_v1.services.cloud_billing.pagers.ListBillingAccountsPager](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.pagers.ListBillingAccountsPager#google_cloud_billing_v1_services_cloud_billing_pagers_ListBillingAccountsPager_ListBillingAccountsPager)

### google.cloud.billing_v1.services.cloud_billing.pagers.ListProjectBillingInfoAsyncPager
    
    
    ListProjectBillingInfoAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.billing_v1.types.cloud_billing.ListProjectBillingInfoResponse
            ],
        ],
        request: google.cloud.billing_v1.types.cloud_billing.ListProjectBillingInfoRequest,
        response: google.cloud.billing_v1.types.cloud_billing.ListProjectBillingInfoResponse,
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

See more: [google.cloud.billing_v1.services.cloud_billing.pagers.ListProjectBillingInfoAsyncPager](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.pagers.ListProjectBillingInfoAsyncPager#google_cloud_billing_v1_services_cloud_billing_pagers_ListProjectBillingInfoAsyncPager_ListProjectBillingInfoAsyncPager)

### google.cloud.billing_v1.services.cloud_billing.pagers.ListProjectBillingInfoPager
    
    
    ListProjectBillingInfoPager(
        method: typing.Callable[
            [...],
            google.cloud.billing_v1.types.cloud_billing.ListProjectBillingInfoResponse,
        ],
        request: google.cloud.billing_v1.types.cloud_billing.ListProjectBillingInfoRequest,
        response: google.cloud.billing_v1.types.cloud_billing.ListProjectBillingInfoResponse,
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

See more: [google.cloud.billing_v1.services.cloud_billing.pagers.ListProjectBillingInfoPager](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_billing.pagers.ListProjectBillingInfoPager#google_cloud_billing_v1_services_cloud_billing_pagers_ListProjectBillingInfoPager_ListProjectBillingInfoPager)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient
    
    
    CloudCatalogAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.billing_v1.services.cloud_catalog.transports.base.CloudCatalogTransport,
                typing.Callable[
                    [...],
                    google.cloud.billing_v1.services.cloud_catalog.transports.base.CloudCatalogTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the cloud catalog async client.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_CloudCatalogAsyncClient)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_common_billing_account_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_common_folder_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_common_location_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_common_organization_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_common_project_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_from_service_account_file)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_from_service_account_info)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_from_service_account_json)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.billing_v1.services.cloud_catalog.transports.base.CloudCatalogTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_get_transport_class)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.list_services
    
    
    list_services(
        request: typing.Optional[
            typing.Union[
                google.cloud.billing_v1.types.cloud_catalog.ListServicesRequest, dict
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
    ) -> google.cloud.billing_v1.services.cloud_catalog.pagers.ListServicesAsyncPager

Lists all public cloud services.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.list_services](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_list_services)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.list_skus
    
    
    list_skus(
        request: typing.Optional[
            typing.Union[google.cloud.billing_v1.types.cloud_catalog.ListSkusRequest, dict]
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
    ) -> google.cloud.billing_v1.services.cloud_catalog.pagers.ListSkusAsyncPager

Lists all publicly available SKUs for a given cloud service.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.list_skus](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_list_skus)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_parse_common_billing_account_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_parse_common_folder_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_parse_common_location_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_parse_common_organization_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_parse_common_project_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.parse_service_path
    
    
    parse_service_path(path: str) -> typing.Dict[str, str]

Parses a service path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.parse_service_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_parse_service_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.parse_sku_path
    
    
    parse_sku_path(path: str) -> typing.Dict[str, str]

Parses a sku path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.parse_sku_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_parse_sku_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.service_path
    
    
    service_path(service: str) -> str

Returns a fully-qualified service string.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.service_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_service_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.sku_path
    
    
    sku_path(service: str, sku: str) -> str

Returns a fully-qualified sku string.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient.sku_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogAsyncClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogAsyncClient_sku_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient
    
    
    CloudCatalogClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.billing_v1.services.cloud_catalog.transports.base.CloudCatalogTransport,
                typing.Callable[
                    [...],
                    google.cloud.billing_v1.services.cloud_catalog.transports.base.CloudCatalogTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the cloud catalog client.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_CloudCatalogClient)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.**exit**](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient___exit__)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_common_billing_account_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.common_folder_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_common_folder_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.common_location_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_common_location_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.common_organization_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_common_organization_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.common_project_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_common_project_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.from_service_account_file](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_from_service_account_file)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.from_service_account_info](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_from_service_account_info)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.from_service_account_json](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_from_service_account_json)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_get_mtls_endpoint_and_cert_source)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.list_services
    
    
    list_services(
        request: typing.Optional[
            typing.Union[
                google.cloud.billing_v1.types.cloud_catalog.ListServicesRequest, dict
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
    ) -> google.cloud.billing_v1.services.cloud_catalog.pagers.ListServicesPager

Lists all public cloud services.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.list_services](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_list_services)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.list_skus
    
    
    list_skus(
        request: typing.Optional[
            typing.Union[google.cloud.billing_v1.types.cloud_catalog.ListSkusRequest, dict]
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
    ) -> google.cloud.billing_v1.services.cloud_catalog.pagers.ListSkusPager

Lists all publicly available SKUs for a given cloud service.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.list_skus](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_list_skus)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_parse_common_billing_account_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_parse_common_folder_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_parse_common_location_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_parse_common_organization_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_parse_common_project_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.parse_service_path
    
    
    parse_service_path(path: str) -> typing.Dict[str, str]

Parses a service path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.parse_service_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_parse_service_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.parse_sku_path
    
    
    parse_sku_path(path: str) -> typing.Dict[str, str]

Parses a sku path into its component segments.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.parse_sku_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_parse_sku_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.service_path
    
    
    service_path(service: str) -> str

Returns a fully-qualified service string.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.service_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_service_path)

### google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.sku_path
    
    
    sku_path(service: str, sku: str) -> str

Returns a fully-qualified sku string.

See more: [google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient.sku_path](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.CloudCatalogClient#google_cloud_billing_v1_services_cloud_catalog_CloudCatalogClient_sku_path)

### google.cloud.billing_v1.services.cloud_catalog.pagers.ListServicesAsyncPager
    
    
    ListServicesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.billing_v1.types.cloud_catalog.ListServicesResponse
            ],
        ],
        request: google.cloud.billing_v1.types.cloud_catalog.ListServicesRequest,
        response: google.cloud.billing_v1.types.cloud_catalog.ListServicesResponse,
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

See more: [google.cloud.billing_v1.services.cloud_catalog.pagers.ListServicesAsyncPager](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.pagers.ListServicesAsyncPager#google_cloud_billing_v1_services_cloud_catalog_pagers_ListServicesAsyncPager_ListServicesAsyncPager)

### google.cloud.billing_v1.services.cloud_catalog.pagers.ListServicesPager
    
    
    ListServicesPager(
        method: typing.Callable[
            [...], google.cloud.billing_v1.types.cloud_catalog.ListServicesResponse
        ],
        request: google.cloud.billing_v1.types.cloud_catalog.ListServicesRequest,
        response: google.cloud.billing_v1.types.cloud_catalog.ListServicesResponse,
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

See more: [google.cloud.billing_v1.services.cloud_catalog.pagers.ListServicesPager](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.pagers.ListServicesPager#google_cloud_billing_v1_services_cloud_catalog_pagers_ListServicesPager_ListServicesPager)

### google.cloud.billing_v1.services.cloud_catalog.pagers.ListSkusAsyncPager
    
    
    ListSkusAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.billing_v1.types.cloud_catalog.ListSkusResponse],
        ],
        request: google.cloud.billing_v1.types.cloud_catalog.ListSkusRequest,
        response: google.cloud.billing_v1.types.cloud_catalog.ListSkusResponse,
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

See more: [google.cloud.billing_v1.services.cloud_catalog.pagers.ListSkusAsyncPager](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.pagers.ListSkusAsyncPager#google_cloud_billing_v1_services_cloud_catalog_pagers_ListSkusAsyncPager_ListSkusAsyncPager)

### google.cloud.billing_v1.services.cloud_catalog.pagers.ListSkusPager
    
    
    ListSkusPager(
        method: typing.Callable[
            [...], google.cloud.billing_v1.types.cloud_catalog.ListSkusResponse
        ],
        request: google.cloud.billing_v1.types.cloud_catalog.ListSkusRequest,
        response: google.cloud.billing_v1.types.cloud_catalog.ListSkusResponse,
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

See more: [google.cloud.billing_v1.services.cloud_catalog.pagers.ListSkusPager](https://cloud.google.com/python/docs/reference/cloudbilling/latest/google.cloud.billing_v1.services.cloud_catalog.pagers.ListSkusPager#google_cloud_billing_v1_services_cloud_catalog_pagers_ListSkusPager_ListSkusPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
