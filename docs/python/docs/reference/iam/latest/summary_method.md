---
url: https://docs.cloud.google.com/python/docs/reference/iam/latest/summary_method/
title: Package Methods (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:28.765229+00:00
---

# Package Methods (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/iam/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.1  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.3  2.17.0  2.16.1  2.15.2  2.14.3  2.13.0  2.12.1  2.11.2  2.10.0  2.9.0  2.8.2  2.7.0  2.6.2  2.5.1  2.4.0  2.3.2  2.2.0  2.1.0  2.0.0  1.0.3  0.3.2  0.2.0 

Summary of entries of Methods for iam.

## 

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient
    
    
    IAMAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_admin_v1.services.iam.transports.base.IAMTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_admin_v1.services.iam.transports.base.IAMTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the iam async client.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_IAMAsyncClient)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_common_billing_account_path)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_common_folder_path)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_common_location_path)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_common_organization_path)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_common_project_path)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.create_role
    
    
    create_role(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.CreateRoleRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.Role

Creates a new custom `Role][google.iam.admin.v1.Role]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.create_role](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_create_role)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.create_service_account
    
    
    create_service_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.CreateServiceAccountRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        service_account: typing.Optional[
            google.cloud.iam_admin_v1.types.iam.ServiceAccount
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccount

Creates a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.create_service_account](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_create_service_account)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.create_service_account_key
    
    
    create_service_account_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.CreateServiceAccountKeyRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        private_key_type: typing.Optional[
            google.cloud.iam_admin_v1.types.iam.ServiceAccountPrivateKeyType
        ] = None,
        key_algorithm: typing.Optional[
            google.cloud.iam_admin_v1.types.iam.ServiceAccountKeyAlgorithm
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccountKey

Creates a `ServiceAccountKey][google.iam.admin.v1.ServiceAccountKey]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.create_service_account_key](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_create_service_account_key)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.delete_role
    
    
    delete_role(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.DeleteRoleRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.Role

Deletes a custom `Role][google.iam.admin.v1.Role]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.delete_role](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_delete_role)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.delete_service_account
    
    
    delete_service_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.DeleteServiceAccountRequest, dict
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

Deletes a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.delete_service_account](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_delete_service_account)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.delete_service_account_key
    
    
    delete_service_account_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.DeleteServiceAccountKeyRequest, dict
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

Deletes a `ServiceAccountKey][google.iam.admin.v1.ServiceAccountKey]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.delete_service_account_key](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_delete_service_account_key)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.disable_service_account
    
    
    disable_service_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.DisableServiceAccountRequest, dict
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
    ) -> None

Disables a `ServiceAccount][google.iam.admin.v1.ServiceAccount]` immediately.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.disable_service_account](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_disable_service_account)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.disable_service_account_key
    
    
    disable_service_account_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.DisableServiceAccountKeyRequest, dict
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

Disable a `ServiceAccountKey][google.iam.admin.v1.ServiceAccountKey]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.disable_service_account_key](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_disable_service_account_key)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.enable_service_account
    
    
    enable_service_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.EnableServiceAccountRequest, dict
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
    ) -> None

Enables a `ServiceAccount][google.iam.admin.v1.ServiceAccount]` that was disabled by `DisableServiceAccount][google.iam.admin.v1.IAM.DisableServiceAccount]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.enable_service_account](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_enable_service_account)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.enable_service_account_key
    
    
    enable_service_account_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.EnableServiceAccountKeyRequest, dict
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

Enable a `ServiceAccountKey][google.iam.admin.v1.ServiceAccountKey]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.enable_service_account_key](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_enable_service_account_key)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_from_service_account_file)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_from_service_account_info)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_from_service_account_json)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.get_iam_policy
    
    
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

Gets the IAM policy that is attached to a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.get_iam_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_get_iam_policy)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.get_role
    
    
    get_role(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.GetRoleRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.Role

Gets the definition of a `Role][google.iam.admin.v1.Role]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.get_role](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_get_role)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.get_service_account
    
    
    get_service_account(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.GetServiceAccountRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccount

Gets a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.get_service_account](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_get_service_account)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.get_service_account_key
    
    
    get_service_account_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.GetServiceAccountKeyRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        public_key_type: typing.Optional[
            google.cloud.iam_admin_v1.types.iam.ServiceAccountPublicKeyType
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccountKey

Gets a `ServiceAccountKey][google.iam.admin.v1.ServiceAccountKey]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.get_service_account_key](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_get_service_account_key)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[google.cloud.iam_admin_v1.services.iam.transports.base.IAMTransport]

Returns an appropriate transport class.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_get_transport_class)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.key_path
    
    
    key_path(project: str, service_account: str, key: str) -> str

Returns a fully-qualified key string.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.key_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_key_path)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.lint_policy
    
    
    lint_policy(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.LintPolicyRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.LintPolicyResponse

Lints, or validates, an IAM policy.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.lint_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_lint_policy)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.list_roles
    
    
    list_roles(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.ListRolesRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.services.iam.pagers.ListRolesAsyncPager

Lists every predefined `Role][google.iam.admin.v1.Role]` that IAM supports, or every custom role that is defined for an organization or project.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.list_roles](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_list_roles)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.list_service_account_keys
    
    
    list_service_account_keys(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.ListServiceAccountKeysRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        key_types: typing.Optional[
            typing.MutableSequence[
                google.cloud.iam_admin_v1.types.iam.ListServiceAccountKeysRequest.KeyType
            ]
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.types.iam.ListServiceAccountKeysResponse

Lists every `ServiceAccountKey][google.iam.admin.v1.ServiceAccountKey]` for a service account.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.list_service_account_keys](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_list_service_account_keys)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.list_service_accounts
    
    
    list_service_accounts(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.ListServiceAccountsRequest, dict
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
    ) -> google.cloud.iam_admin_v1.services.iam.pagers.ListServiceAccountsAsyncPager

Lists every `ServiceAccount][google.iam.admin.v1.ServiceAccount]` that belongs to a specific project.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.list_service_accounts](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_list_service_accounts)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_parse_common_billing_account_path)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_parse_common_folder_path)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_parse_common_location_path)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_parse_common_organization_path)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_parse_common_project_path)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.parse_key_path
    
    
    parse_key_path(path: str) -> typing.Dict[str, str]

Parses a key path into its component segments.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.parse_key_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_parse_key_path)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.parse_service_account_path
    
    
    parse_service_account_path(path: str) -> typing.Dict[str, str]

Parses a service_account path into its component segments.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.parse_service_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_parse_service_account_path)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.patch_service_account
    
    
    patch_service_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.PatchServiceAccountRequest, dict
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
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccount

Patches a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.patch_service_account](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_patch_service_account)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.query_auditable_services
    
    
    query_auditable_services(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.QueryAuditableServicesRequest, dict
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
    ) -> google.cloud.iam_admin_v1.types.iam.QueryAuditableServicesResponse

Returns a list of services that allow you to opt into audit logs that are not generated by default.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.query_auditable_services](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_query_auditable_services)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.query_grantable_roles
    
    
    query_grantable_roles(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.QueryGrantableRolesRequest, dict
            ]
        ] = None,
        *,
        full_resource_name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.services.iam.pagers.QueryGrantableRolesAsyncPager

Lists roles that can be granted on a Google Cloud resource.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.query_grantable_roles](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_query_grantable_roles)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.query_testable_permissions
    
    
    query_testable_permissions(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.QueryTestablePermissionsRequest, dict
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
    ) -> google.cloud.iam_admin_v1.services.iam.pagers.QueryTestablePermissionsAsyncPager

Lists every permission that you can test on a resource.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.query_testable_permissions](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_query_testable_permissions)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.service_account_path
    
    
    service_account_path(project: str, service_account: str) -> str

Returns a fully-qualified service_account string.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.service_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_service_account_path)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.set_iam_policy
    
    
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

Sets the IAM policy that is attached to a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.set_iam_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_set_iam_policy)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.sign_blob
    
    
    sign_blob(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.SignBlobRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        bytes_to_sign: typing.Optional[bytes] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.types.iam.SignBlobResponse

**Note:** This method is deprecated.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.sign_blob](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_sign_blob)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.sign_jwt
    
    
    sign_jwt(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.SignJwtRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        payload: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.types.iam.SignJwtResponse

**Note:** This method is deprecated.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.sign_jwt](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_sign_jwt)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.test_iam_permissions
    
    
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

Tests whether the caller has the specified permissions on a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_test_iam_permissions)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.undelete_role
    
    
    undelete_role(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.UndeleteRoleRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.Role

Undeletes a custom `Role][google.iam.admin.v1.Role]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.undelete_role](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_undelete_role)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.undelete_service_account
    
    
    undelete_service_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.UndeleteServiceAccountRequest, dict
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
    ) -> google.cloud.iam_admin_v1.types.iam.UndeleteServiceAccountResponse

Restores a deleted `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.undelete_service_account](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_undelete_service_account)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.update_role
    
    
    update_role(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.UpdateRoleRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.Role

Updates the definition of a custom `Role][google.iam.admin.v1.Role]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.update_role](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_update_role)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.update_service_account
    
    
    update_service_account(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.ServiceAccount, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccount

**Note:** We are in the process of deprecating this method.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.update_service_account](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_update_service_account)

### google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.upload_service_account_key
    
    
    upload_service_account_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.UploadServiceAccountKeyRequest, dict
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
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccountKey

Uploads the public key portion of a key pair that you manage, and associates the public key with a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMAsyncClient.upload_service_account_key](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient#google_cloud_iam_admin_v1_services_iam_IAMAsyncClient_upload_service_account_key)

### google.cloud.iam_admin_v1.services.iam.IAMClient
    
    
    IAMClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_admin_v1.services.iam.transports.base.IAMTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_admin_v1.services.iam.transports.base.IAMTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the iam client.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_IAMClient)

### google.cloud.iam_admin_v1.services.iam.IAMClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.**exit**](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient___exit__)

### google.cloud.iam_admin_v1.services.iam.IAMClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_common_billing_account_path)

### google.cloud.iam_admin_v1.services.iam.IAMClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_common_folder_path)

### google.cloud.iam_admin_v1.services.iam.IAMClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_common_location_path)

### google.cloud.iam_admin_v1.services.iam.IAMClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_common_organization_path)

### google.cloud.iam_admin_v1.services.iam.IAMClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_common_project_path)

### google.cloud.iam_admin_v1.services.iam.IAMClient.create_role
    
    
    create_role(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.CreateRoleRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.Role

Creates a new custom `Role][google.iam.admin.v1.Role]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.create_role](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_create_role)

### google.cloud.iam_admin_v1.services.iam.IAMClient.create_service_account
    
    
    create_service_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.CreateServiceAccountRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        account_id: typing.Optional[str] = None,
        service_account: typing.Optional[
            google.cloud.iam_admin_v1.types.iam.ServiceAccount
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccount

Creates a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.create_service_account](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_create_service_account)

### google.cloud.iam_admin_v1.services.iam.IAMClient.create_service_account_key
    
    
    create_service_account_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.CreateServiceAccountKeyRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        private_key_type: typing.Optional[
            google.cloud.iam_admin_v1.types.iam.ServiceAccountPrivateKeyType
        ] = None,
        key_algorithm: typing.Optional[
            google.cloud.iam_admin_v1.types.iam.ServiceAccountKeyAlgorithm
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccountKey

Creates a `ServiceAccountKey][google.iam.admin.v1.ServiceAccountKey]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.create_service_account_key](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_create_service_account_key)

### google.cloud.iam_admin_v1.services.iam.IAMClient.delete_role
    
    
    delete_role(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.DeleteRoleRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.Role

Deletes a custom `Role][google.iam.admin.v1.Role]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.delete_role](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_delete_role)

### google.cloud.iam_admin_v1.services.iam.IAMClient.delete_service_account
    
    
    delete_service_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.DeleteServiceAccountRequest, dict
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

Deletes a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.delete_service_account](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_delete_service_account)

### google.cloud.iam_admin_v1.services.iam.IAMClient.delete_service_account_key
    
    
    delete_service_account_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.DeleteServiceAccountKeyRequest, dict
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

Deletes a `ServiceAccountKey][google.iam.admin.v1.ServiceAccountKey]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.delete_service_account_key](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_delete_service_account_key)

### google.cloud.iam_admin_v1.services.iam.IAMClient.disable_service_account
    
    
    disable_service_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.DisableServiceAccountRequest, dict
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
    ) -> None

Disables a `ServiceAccount][google.iam.admin.v1.ServiceAccount]` immediately.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.disable_service_account](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_disable_service_account)

### google.cloud.iam_admin_v1.services.iam.IAMClient.disable_service_account_key
    
    
    disable_service_account_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.DisableServiceAccountKeyRequest, dict
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

Disable a `ServiceAccountKey][google.iam.admin.v1.ServiceAccountKey]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.disable_service_account_key](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_disable_service_account_key)

### google.cloud.iam_admin_v1.services.iam.IAMClient.enable_service_account
    
    
    enable_service_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.EnableServiceAccountRequest, dict
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
    ) -> None

Enables a `ServiceAccount][google.iam.admin.v1.ServiceAccount]` that was disabled by `DisableServiceAccount][google.iam.admin.v1.IAM.DisableServiceAccount]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.enable_service_account](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_enable_service_account)

### google.cloud.iam_admin_v1.services.iam.IAMClient.enable_service_account_key
    
    
    enable_service_account_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.EnableServiceAccountKeyRequest, dict
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

Enable a `ServiceAccountKey][google.iam.admin.v1.ServiceAccountKey]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.enable_service_account_key](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_enable_service_account_key)

### google.cloud.iam_admin_v1.services.iam.IAMClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.from_service_account_file](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_from_service_account_file)

### google.cloud.iam_admin_v1.services.iam.IAMClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.from_service_account_info](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_from_service_account_info)

### google.cloud.iam_admin_v1.services.iam.IAMClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.from_service_account_json](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_from_service_account_json)

### google.cloud.iam_admin_v1.services.iam.IAMClient.get_iam_policy
    
    
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

Gets the IAM policy that is attached to a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.get_iam_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_get_iam_policy)

### google.cloud.iam_admin_v1.services.iam.IAMClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_get_mtls_endpoint_and_cert_source)

### google.cloud.iam_admin_v1.services.iam.IAMClient.get_role
    
    
    get_role(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.GetRoleRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.Role

Gets the definition of a `Role][google.iam.admin.v1.Role]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.get_role](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_get_role)

### google.cloud.iam_admin_v1.services.iam.IAMClient.get_service_account
    
    
    get_service_account(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.GetServiceAccountRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccount

Gets a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.get_service_account](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_get_service_account)

### google.cloud.iam_admin_v1.services.iam.IAMClient.get_service_account_key
    
    
    get_service_account_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.GetServiceAccountKeyRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        public_key_type: typing.Optional[
            google.cloud.iam_admin_v1.types.iam.ServiceAccountPublicKeyType
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccountKey

Gets a `ServiceAccountKey][google.iam.admin.v1.ServiceAccountKey]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.get_service_account_key](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_get_service_account_key)

### google.cloud.iam_admin_v1.services.iam.IAMClient.key_path
    
    
    key_path(project: str, service_account: str, key: str) -> str

Returns a fully-qualified key string.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.key_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_key_path)

### google.cloud.iam_admin_v1.services.iam.IAMClient.lint_policy
    
    
    lint_policy(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.LintPolicyRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.LintPolicyResponse

Lints, or validates, an IAM policy.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.lint_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_lint_policy)

### google.cloud.iam_admin_v1.services.iam.IAMClient.list_roles
    
    
    list_roles(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.ListRolesRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.services.iam.pagers.ListRolesPager

Lists every predefined `Role][google.iam.admin.v1.Role]` that IAM supports, or every custom role that is defined for an organization or project.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.list_roles](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_list_roles)

### google.cloud.iam_admin_v1.services.iam.IAMClient.list_service_account_keys
    
    
    list_service_account_keys(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.ListServiceAccountKeysRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        key_types: typing.Optional[
            typing.MutableSequence[
                google.cloud.iam_admin_v1.types.iam.ListServiceAccountKeysRequest.KeyType
            ]
        ] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.types.iam.ListServiceAccountKeysResponse

Lists every `ServiceAccountKey][google.iam.admin.v1.ServiceAccountKey]` for a service account.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.list_service_account_keys](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_list_service_account_keys)

### google.cloud.iam_admin_v1.services.iam.IAMClient.list_service_accounts
    
    
    list_service_accounts(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.ListServiceAccountsRequest, dict
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
    ) -> google.cloud.iam_admin_v1.services.iam.pagers.ListServiceAccountsPager

Lists every `ServiceAccount][google.iam.admin.v1.ServiceAccount]` that belongs to a specific project.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.list_service_accounts](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_list_service_accounts)

### google.cloud.iam_admin_v1.services.iam.IAMClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_parse_common_billing_account_path)

### google.cloud.iam_admin_v1.services.iam.IAMClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_parse_common_folder_path)

### google.cloud.iam_admin_v1.services.iam.IAMClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_parse_common_location_path)

### google.cloud.iam_admin_v1.services.iam.IAMClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_parse_common_organization_path)

### google.cloud.iam_admin_v1.services.iam.IAMClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_parse_common_project_path)

### google.cloud.iam_admin_v1.services.iam.IAMClient.parse_key_path
    
    
    parse_key_path(path: str) -> typing.Dict[str, str]

Parses a key path into its component segments.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.parse_key_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_parse_key_path)

### google.cloud.iam_admin_v1.services.iam.IAMClient.parse_service_account_path
    
    
    parse_service_account_path(path: str) -> typing.Dict[str, str]

Parses a service_account path into its component segments.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.parse_service_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_parse_service_account_path)

### google.cloud.iam_admin_v1.services.iam.IAMClient.patch_service_account
    
    
    patch_service_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.PatchServiceAccountRequest, dict
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
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccount

Patches a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.patch_service_account](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_patch_service_account)

### google.cloud.iam_admin_v1.services.iam.IAMClient.query_auditable_services
    
    
    query_auditable_services(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.QueryAuditableServicesRequest, dict
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
    ) -> google.cloud.iam_admin_v1.types.iam.QueryAuditableServicesResponse

Returns a list of services that allow you to opt into audit logs that are not generated by default.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.query_auditable_services](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_query_auditable_services)

### google.cloud.iam_admin_v1.services.iam.IAMClient.query_grantable_roles
    
    
    query_grantable_roles(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.QueryGrantableRolesRequest, dict
            ]
        ] = None,
        *,
        full_resource_name: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.services.iam.pagers.QueryGrantableRolesPager

Lists roles that can be granted on a Google Cloud resource.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.query_grantable_roles](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_query_grantable_roles)

### google.cloud.iam_admin_v1.services.iam.IAMClient.query_testable_permissions
    
    
    query_testable_permissions(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.QueryTestablePermissionsRequest, dict
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
    ) -> google.cloud.iam_admin_v1.services.iam.pagers.QueryTestablePermissionsPager

Lists every permission that you can test on a resource.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.query_testable_permissions](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_query_testable_permissions)

### google.cloud.iam_admin_v1.services.iam.IAMClient.service_account_path
    
    
    service_account_path(project: str, service_account: str) -> str

Returns a fully-qualified service_account string.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.service_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_service_account_path)

### google.cloud.iam_admin_v1.services.iam.IAMClient.set_iam_policy
    
    
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

Sets the IAM policy that is attached to a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.set_iam_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_set_iam_policy)

### google.cloud.iam_admin_v1.services.iam.IAMClient.sign_blob
    
    
    sign_blob(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.SignBlobRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        bytes_to_sign: typing.Optional[bytes] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.types.iam.SignBlobResponse

**Note:** This method is deprecated.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.sign_blob](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_sign_blob)

### google.cloud.iam_admin_v1.services.iam.IAMClient.sign_jwt
    
    
    sign_jwt(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.SignJwtRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        payload: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_admin_v1.types.iam.SignJwtResponse

**Note:** This method is deprecated.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.sign_jwt](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_sign_jwt)

### google.cloud.iam_admin_v1.services.iam.IAMClient.test_iam_permissions
    
    
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

Tests whether the caller has the specified permissions on a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.test_iam_permissions](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_test_iam_permissions)

### google.cloud.iam_admin_v1.services.iam.IAMClient.undelete_role
    
    
    undelete_role(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.UndeleteRoleRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.Role

Undeletes a custom `Role][google.iam.admin.v1.Role]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.undelete_role](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_undelete_role)

### google.cloud.iam_admin_v1.services.iam.IAMClient.undelete_service_account
    
    
    undelete_service_account(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.UndeleteServiceAccountRequest, dict
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
    ) -> google.cloud.iam_admin_v1.types.iam.UndeleteServiceAccountResponse

Restores a deleted `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.undelete_service_account](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_undelete_service_account)

### google.cloud.iam_admin_v1.services.iam.IAMClient.update_role
    
    
    update_role(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.UpdateRoleRequest, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.Role

Updates the definition of a custom `Role][google.iam.admin.v1.Role]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.update_role](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_update_role)

### google.cloud.iam_admin_v1.services.iam.IAMClient.update_service_account
    
    
    update_service_account(
        request: typing.Optional[
            typing.Union[google.cloud.iam_admin_v1.types.iam.ServiceAccount, dict]
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
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccount

**Note:** We are in the process of deprecating this method.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.update_service_account](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_update_service_account)

### google.cloud.iam_admin_v1.services.iam.IAMClient.upload_service_account_key
    
    
    upload_service_account_key(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_admin_v1.types.iam.UploadServiceAccountKeyRequest, dict
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
    ) -> google.cloud.iam_admin_v1.types.iam.ServiceAccountKey

Uploads the public key portion of a key pair that you manage, and associates the public key with a `ServiceAccount][google.iam.admin.v1.ServiceAccount]`.

See more: [google.cloud.iam_admin_v1.services.iam.IAMClient.upload_service_account_key](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient#google_cloud_iam_admin_v1_services_iam_IAMClient_upload_service_account_key)

### google.cloud.iam_admin_v1.services.iam.pagers.ListRolesAsyncPager
    
    
    ListRolesAsyncPager(
        method: typing.Callable[
            [...], typing.Awaitable[google.cloud.iam_admin_v1.types.iam.ListRolesResponse]
        ],
        request: google.cloud.iam_admin_v1.types.iam.ListRolesRequest,
        response: google.cloud.iam_admin_v1.types.iam.ListRolesResponse,
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

See more: [google.cloud.iam_admin_v1.services.iam.pagers.ListRolesAsyncPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.ListRolesAsyncPager#google_cloud_iam_admin_v1_services_iam_pagers_ListRolesAsyncPager_ListRolesAsyncPager)

### google.cloud.iam_admin_v1.services.iam.pagers.ListRolesPager
    
    
    ListRolesPager(
        method: typing.Callable[
            [...], google.cloud.iam_admin_v1.types.iam.ListRolesResponse
        ],
        request: google.cloud.iam_admin_v1.types.iam.ListRolesRequest,
        response: google.cloud.iam_admin_v1.types.iam.ListRolesResponse,
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

See more: [google.cloud.iam_admin_v1.services.iam.pagers.ListRolesPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.ListRolesPager#google_cloud_iam_admin_v1_services_iam_pagers_ListRolesPager_ListRolesPager)

### google.cloud.iam_admin_v1.services.iam.pagers.ListServiceAccountsAsyncPager
    
    
    ListServiceAccountsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iam_admin_v1.types.iam.ListServiceAccountsResponse
            ],
        ],
        request: google.cloud.iam_admin_v1.types.iam.ListServiceAccountsRequest,
        response: google.cloud.iam_admin_v1.types.iam.ListServiceAccountsResponse,
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

See more: [google.cloud.iam_admin_v1.services.iam.pagers.ListServiceAccountsAsyncPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.ListServiceAccountsAsyncPager#google_cloud_iam_admin_v1_services_iam_pagers_ListServiceAccountsAsyncPager_ListServiceAccountsAsyncPager)

### google.cloud.iam_admin_v1.services.iam.pagers.ListServiceAccountsPager
    
    
    ListServiceAccountsPager(
        method: typing.Callable[
            [...], google.cloud.iam_admin_v1.types.iam.ListServiceAccountsResponse
        ],
        request: google.cloud.iam_admin_v1.types.iam.ListServiceAccountsRequest,
        response: google.cloud.iam_admin_v1.types.iam.ListServiceAccountsResponse,
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

See more: [google.cloud.iam_admin_v1.services.iam.pagers.ListServiceAccountsPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.ListServiceAccountsPager#google_cloud_iam_admin_v1_services_iam_pagers_ListServiceAccountsPager_ListServiceAccountsPager)

### google.cloud.iam_admin_v1.services.iam.pagers.QueryGrantableRolesAsyncPager
    
    
    QueryGrantableRolesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iam_admin_v1.types.iam.QueryGrantableRolesResponse
            ],
        ],
        request: google.cloud.iam_admin_v1.types.iam.QueryGrantableRolesRequest,
        response: google.cloud.iam_admin_v1.types.iam.QueryGrantableRolesResponse,
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

See more: [google.cloud.iam_admin_v1.services.iam.pagers.QueryGrantableRolesAsyncPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.QueryGrantableRolesAsyncPager#google_cloud_iam_admin_v1_services_iam_pagers_QueryGrantableRolesAsyncPager_QueryGrantableRolesAsyncPager)

### google.cloud.iam_admin_v1.services.iam.pagers.QueryGrantableRolesPager
    
    
    QueryGrantableRolesPager(
        method: typing.Callable[
            [...], google.cloud.iam_admin_v1.types.iam.QueryGrantableRolesResponse
        ],
        request: google.cloud.iam_admin_v1.types.iam.QueryGrantableRolesRequest,
        response: google.cloud.iam_admin_v1.types.iam.QueryGrantableRolesResponse,
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

See more: [google.cloud.iam_admin_v1.services.iam.pagers.QueryGrantableRolesPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.QueryGrantableRolesPager#google_cloud_iam_admin_v1_services_iam_pagers_QueryGrantableRolesPager_QueryGrantableRolesPager)

### google.cloud.iam_admin_v1.services.iam.pagers.QueryTestablePermissionsAsyncPager
    
    
    QueryTestablePermissionsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iam_admin_v1.types.iam.QueryTestablePermissionsResponse
            ],
        ],
        request: google.cloud.iam_admin_v1.types.iam.QueryTestablePermissionsRequest,
        response: google.cloud.iam_admin_v1.types.iam.QueryTestablePermissionsResponse,
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

See more: [google.cloud.iam_admin_v1.services.iam.pagers.QueryTestablePermissionsAsyncPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.QueryTestablePermissionsAsyncPager#google_cloud_iam_admin_v1_services_iam_pagers_QueryTestablePermissionsAsyncPager_QueryTestablePermissionsAsyncPager)

### google.cloud.iam_admin_v1.services.iam.pagers.QueryTestablePermissionsPager
    
    
    QueryTestablePermissionsPager(
        method: typing.Callable[
            [...], google.cloud.iam_admin_v1.types.iam.QueryTestablePermissionsResponse
        ],
        request: google.cloud.iam_admin_v1.types.iam.QueryTestablePermissionsRequest,
        response: google.cloud.iam_admin_v1.types.iam.QueryTestablePermissionsResponse,
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

See more: [google.cloud.iam_admin_v1.services.iam.pagers.QueryTestablePermissionsPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.QueryTestablePermissionsPager#google_cloud_iam_admin_v1_services_iam_pagers_QueryTestablePermissionsPager_QueryTestablePermissionsPager)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient
    
    
    IAMCredentialsAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_credentials_v1.services.iam_credentials.transports.base.IAMCredentialsTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_credentials_v1.services.iam_credentials.transports.base.IAMCredentialsTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the iam credentials async client.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_IAMCredentialsAsyncClient)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_common_billing_account_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_common_folder_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_common_location_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_common_organization_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_common_project_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_from_service_account_file)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_from_service_account_info)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_from_service_account_json)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.generate_access_token
    
    
    generate_access_token(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_credentials_v1.types.common.GenerateAccessTokenRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        delegates: typing.Optional[typing.MutableSequence[str]] = None,
        scope: typing.Optional[typing.MutableSequence[str]] = None,
        lifetime: typing.Optional[google.protobuf.duration_pb2.Duration] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_credentials_v1.types.common.GenerateAccessTokenResponse

Generates an OAuth 2.0 access token for a service account.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.generate_access_token](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_generate_access_token)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.generate_id_token
    
    
    generate_id_token(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_credentials_v1.types.common.GenerateIdTokenRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        delegates: typing.Optional[typing.MutableSequence[str]] = None,
        audience: typing.Optional[str] = None,
        include_email: typing.Optional[bool] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_credentials_v1.types.common.GenerateIdTokenResponse

Generates an OpenID Connect ID token for a service account.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.generate_id_token](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_generate_id_token)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.iam_credentials_v1.services.iam_credentials.transports.base.IAMCredentialsTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_get_transport_class)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_parse_common_billing_account_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_parse_common_folder_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_parse_common_location_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_parse_common_organization_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_parse_common_project_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.parse_service_account_path
    
    
    parse_service_account_path(path: str) -> typing.Dict[str, str]

Parses a service_account path into its component segments.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.parse_service_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_parse_service_account_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.service_account_path
    
    
    service_account_path(project: str, service_account: str) -> str

Returns a fully-qualified service_account string.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.service_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_service_account_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.sign_blob
    
    
    sign_blob(
        request: typing.Optional[
            typing.Union[google.cloud.iam_credentials_v1.types.common.SignBlobRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        delegates: typing.Optional[typing.MutableSequence[str]] = None,
        payload: typing.Optional[bytes] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_credentials_v1.types.common.SignBlobResponse

Signs a blob using a service account's system-managed private key.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.sign_blob](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_sign_blob)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.sign_jwt
    
    
    sign_jwt(
        request: typing.Optional[
            typing.Union[google.cloud.iam_credentials_v1.types.common.SignJwtRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        delegates: typing.Optional[typing.MutableSequence[str]] = None,
        payload: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_credentials_v1.types.common.SignJwtResponse

Signs a JWT using a service account's system-managed private key.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient.sign_jwt](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsAsyncClient_sign_jwt)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient
    
    
    IAMCredentialsClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_credentials_v1.services.iam_credentials.transports.base.IAMCredentialsTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_credentials_v1.services.iam_credentials.transports.base.IAMCredentialsTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the iam credentials client.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_IAMCredentialsClient)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.**exit**](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient___exit__)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_common_billing_account_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_common_folder_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_common_location_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_common_organization_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_common_project_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.from_service_account_file](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_from_service_account_file)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.from_service_account_info](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_from_service_account_info)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.from_service_account_json](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_from_service_account_json)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.generate_access_token
    
    
    generate_access_token(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_credentials_v1.types.common.GenerateAccessTokenRequest,
                dict,
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        delegates: typing.Optional[typing.MutableSequence[str]] = None,
        scope: typing.Optional[typing.MutableSequence[str]] = None,
        lifetime: typing.Optional[google.protobuf.duration_pb2.Duration] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_credentials_v1.types.common.GenerateAccessTokenResponse

Generates an OAuth 2.0 access token for a service account.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.generate_access_token](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_generate_access_token)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.generate_id_token
    
    
    generate_id_token(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_credentials_v1.types.common.GenerateIdTokenRequest, dict
            ]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        delegates: typing.Optional[typing.MutableSequence[str]] = None,
        audience: typing.Optional[str] = None,
        include_email: typing.Optional[bool] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_credentials_v1.types.common.GenerateIdTokenResponse

Generates an OpenID Connect ID token for a service account.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.generate_id_token](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_generate_id_token)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_get_mtls_endpoint_and_cert_source)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_parse_common_billing_account_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_parse_common_folder_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_parse_common_location_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_parse_common_organization_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_parse_common_project_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.parse_service_account_path
    
    
    parse_service_account_path(path: str) -> typing.Dict[str, str]

Parses a service_account path into its component segments.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.parse_service_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_parse_service_account_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.service_account_path
    
    
    service_account_path(project: str, service_account: str) -> str

Returns a fully-qualified service_account string.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.service_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_service_account_path)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.sign_blob
    
    
    sign_blob(
        request: typing.Optional[
            typing.Union[google.cloud.iam_credentials_v1.types.common.SignBlobRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        delegates: typing.Optional[typing.MutableSequence[str]] = None,
        payload: typing.Optional[bytes] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_credentials_v1.types.common.SignBlobResponse

Signs a blob using a service account's system-managed private key.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.sign_blob](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_sign_blob)

### google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.sign_jwt
    
    
    sign_jwt(
        request: typing.Optional[
            typing.Union[google.cloud.iam_credentials_v1.types.common.SignJwtRequest, dict]
        ] = None,
        *,
        name: typing.Optional[str] = None,
        delegates: typing.Optional[typing.MutableSequence[str]] = None,
        payload: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.cloud.iam_credentials_v1.types.common.SignJwtResponse

Signs a JWT using a service account's system-managed private key.

See more: [google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient.sign_jwt](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient#google_cloud_iam_credentials_v1_services_iam_credentials_IAMCredentialsClient_sign_jwt)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient
    
    
    PoliciesAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_v2.services.policies.transports.base.PoliciesTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_v2.services.policies.transports.base.PoliciesTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the policies async client.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_PoliciesAsyncClient)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_common_billing_account_path)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_common_folder_path)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_common_location_path)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_common_organization_path)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_common_project_path)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.create_policy
    
    
    create_policy(
        request: typing.Optional[
            typing.Union[google.cloud.iam_v2.types.policy.CreatePolicyRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        policy: typing.Optional[google.cloud.iam_v2.types.policy.Policy] = None,
        policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a policy.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.create_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_create_policy)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.delete_policy
    
    
    delete_policy(
        request: typing.Optional[
            typing.Union[google.cloud.iam_v2.types.policy.DeletePolicyRequest, dict]
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

Deletes a policy.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.delete_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_delete_policy)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_from_service_account_file)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_from_service_account_info)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_from_service_account_json)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.get_operation
    
    
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

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_get_operation)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.get_policy
    
    
    get_policy(
        request: typing.Optional[
            typing.Union[google.cloud.iam_v2.types.policy.GetPolicyRequest, dict]
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
    ) -> google.cloud.iam_v2.types.policy.Policy

Gets a policy.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.get_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_get_policy)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.iam_v2.services.policies.transports.base.PoliciesTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_get_transport_class)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.list_policies
    
    
    list_policies(
        request: typing.Optional[
            typing.Union[google.cloud.iam_v2.types.policy.ListPoliciesRequest, dict]
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
    ) -> google.cloud.iam_v2.services.policies.pagers.ListPoliciesAsyncPager

Retrieves the policies of the specified kind that are attached to a resource.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.list_policies](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_list_policies)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_parse_common_billing_account_path)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_parse_common_folder_path)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_parse_common_location_path)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_parse_common_organization_path)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_parse_common_project_path)

### google.cloud.iam_v2.services.policies.PoliciesAsyncClient.update_policy
    
    
    update_policy(
        request: typing.Optional[
            typing.Union[google.cloud.iam_v2.types.policy.UpdatePolicyRequest, dict]
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

Updates the specified policy.

See more: [google.cloud.iam_v2.services.policies.PoliciesAsyncClient.update_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient#google_cloud_iam_v2_services_policies_PoliciesAsyncClient_update_policy)

### google.cloud.iam_v2.services.policies.PoliciesClient
    
    
    PoliciesClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_v2.services.policies.transports.base.PoliciesTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_v2.services.policies.transports.base.PoliciesTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the policies client.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_PoliciesClient)

### google.cloud.iam_v2.services.policies.PoliciesClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.**exit**](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient___exit__)

### google.cloud.iam_v2.services.policies.PoliciesClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_common_billing_account_path)

### google.cloud.iam_v2.services.policies.PoliciesClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_common_folder_path)

### google.cloud.iam_v2.services.policies.PoliciesClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_common_location_path)

### google.cloud.iam_v2.services.policies.PoliciesClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_common_organization_path)

### google.cloud.iam_v2.services.policies.PoliciesClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_common_project_path)

### google.cloud.iam_v2.services.policies.PoliciesClient.create_policy
    
    
    create_policy(
        request: typing.Optional[
            typing.Union[google.cloud.iam_v2.types.policy.CreatePolicyRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        policy: typing.Optional[google.cloud.iam_v2.types.policy.Policy] = None,
        policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a policy.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.create_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_create_policy)

### google.cloud.iam_v2.services.policies.PoliciesClient.delete_policy
    
    
    delete_policy(
        request: typing.Optional[
            typing.Union[google.cloud.iam_v2.types.policy.DeletePolicyRequest, dict]
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

Deletes a policy.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.delete_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_delete_policy)

### google.cloud.iam_v2.services.policies.PoliciesClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.from_service_account_file](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_from_service_account_file)

### google.cloud.iam_v2.services.policies.PoliciesClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.from_service_account_info](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_from_service_account_info)

### google.cloud.iam_v2.services.policies.PoliciesClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.from_service_account_json](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_from_service_account_json)

### google.cloud.iam_v2.services.policies.PoliciesClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_get_mtls_endpoint_and_cert_source)

### google.cloud.iam_v2.services.policies.PoliciesClient.get_operation
    
    
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

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.get_operation](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_get_operation)

### google.cloud.iam_v2.services.policies.PoliciesClient.get_policy
    
    
    get_policy(
        request: typing.Optional[
            typing.Union[google.cloud.iam_v2.types.policy.GetPolicyRequest, dict]
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
    ) -> google.cloud.iam_v2.types.policy.Policy

Gets a policy.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.get_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_get_policy)

### google.cloud.iam_v2.services.policies.PoliciesClient.list_policies
    
    
    list_policies(
        request: typing.Optional[
            typing.Union[google.cloud.iam_v2.types.policy.ListPoliciesRequest, dict]
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
    ) -> google.cloud.iam_v2.services.policies.pagers.ListPoliciesPager

Retrieves the policies of the specified kind that are attached to a resource.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.list_policies](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_list_policies)

### google.cloud.iam_v2.services.policies.PoliciesClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_parse_common_billing_account_path)

### google.cloud.iam_v2.services.policies.PoliciesClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_parse_common_folder_path)

### google.cloud.iam_v2.services.policies.PoliciesClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_parse_common_location_path)

### google.cloud.iam_v2.services.policies.PoliciesClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_parse_common_organization_path)

### google.cloud.iam_v2.services.policies.PoliciesClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_parse_common_project_path)

### google.cloud.iam_v2.services.policies.PoliciesClient.update_policy
    
    
    update_policy(
        request: typing.Optional[
            typing.Union[google.cloud.iam_v2.types.policy.UpdatePolicyRequest, dict]
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

Updates the specified policy.

See more: [google.cloud.iam_v2.services.policies.PoliciesClient.update_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient#google_cloud_iam_v2_services_policies_PoliciesClient_update_policy)

### google.cloud.iam_v2.services.policies.pagers.ListPoliciesAsyncPager
    
    
    ListPoliciesAsyncPager(
        method: typing.Callable[
            [...], typing.Awaitable[google.cloud.iam_v2.types.policy.ListPoliciesResponse]
        ],
        request: google.cloud.iam_v2.types.policy.ListPoliciesRequest,
        response: google.cloud.iam_v2.types.policy.ListPoliciesResponse,
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

See more: [google.cloud.iam_v2.services.policies.pagers.ListPoliciesAsyncPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.pagers.ListPoliciesAsyncPager#google_cloud_iam_v2_services_policies_pagers_ListPoliciesAsyncPager_ListPoliciesAsyncPager)

### google.cloud.iam_v2.services.policies.pagers.ListPoliciesPager
    
    
    ListPoliciesPager(
        method: typing.Callable[
            [...], google.cloud.iam_v2.types.policy.ListPoliciesResponse
        ],
        request: google.cloud.iam_v2.types.policy.ListPoliciesRequest,
        response: google.cloud.iam_v2.types.policy.ListPoliciesResponse,
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

See more: [google.cloud.iam_v2.services.policies.pagers.ListPoliciesPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.pagers.ListPoliciesPager#google_cloud_iam_v2_services_policies_pagers_ListPoliciesPager_ListPoliciesPager)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient
    
    
    PoliciesAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_v2beta.services.policies.transports.base.PoliciesTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_v2beta.services.policies.transports.base.PoliciesTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the policies async client.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_PoliciesAsyncClient)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_common_billing_account_path)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_common_folder_path)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_common_location_path)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_common_organization_path)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_common_project_path)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.create_policy
    
    
    create_policy(
        request: typing.Optional[
            typing.Union[google.cloud.iam_v2beta.types.policy.CreatePolicyRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        policy: typing.Optional[google.cloud.iam_v2beta.types.policy.Policy] = None,
        policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a policy.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.create_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_create_policy)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.delete_policy
    
    
    delete_policy(
        request: typing.Optional[
            typing.Union[google.cloud.iam_v2beta.types.policy.DeletePolicyRequest, dict]
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

Deletes a policy.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.delete_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_delete_policy)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_from_service_account_file)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_from_service_account_info)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_from_service_account_json)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.get_operation
    
    
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

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_get_operation)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.get_policy
    
    
    get_policy(
        request: typing.Optional[
            typing.Union[google.cloud.iam_v2beta.types.policy.GetPolicyRequest, dict]
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
    ) -> google.cloud.iam_v2beta.types.policy.Policy

Gets a policy.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.get_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_get_policy)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.iam_v2beta.services.policies.transports.base.PoliciesTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_get_transport_class)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.list_policies
    
    
    list_policies(
        request: typing.Optional[
            typing.Union[google.cloud.iam_v2beta.types.policy.ListPoliciesRequest, dict]
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
    ) -> google.cloud.iam_v2beta.services.policies.pagers.ListPoliciesAsyncPager

Retrieves the policies of the specified kind that are attached to a resource.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.list_policies](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_list_policies)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_parse_common_billing_account_path)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_parse_common_folder_path)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_parse_common_location_path)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_parse_common_organization_path)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_parse_common_project_path)

### google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.update_policy
    
    
    update_policy(
        request: typing.Optional[
            typing.Union[google.cloud.iam_v2beta.types.policy.UpdatePolicyRequest, dict]
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

Updates the specified policy.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient.update_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient#google_cloud_iam_v2beta_services_policies_PoliciesAsyncClient_update_policy)

### google.cloud.iam_v2beta.services.policies.PoliciesClient
    
    
    PoliciesClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_v2beta.services.policies.transports.base.PoliciesTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_v2beta.services.policies.transports.base.PoliciesTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the policies client.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_PoliciesClient)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.**exit**](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient___exit__)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_common_billing_account_path)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_common_folder_path)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_common_location_path)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_common_organization_path)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_common_project_path)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.create_policy
    
    
    create_policy(
        request: typing.Optional[
            typing.Union[google.cloud.iam_v2beta.types.policy.CreatePolicyRequest, dict]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        policy: typing.Optional[google.cloud.iam_v2beta.types.policy.Policy] = None,
        policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a policy.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.create_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_create_policy)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.delete_policy
    
    
    delete_policy(
        request: typing.Optional[
            typing.Union[google.cloud.iam_v2beta.types.policy.DeletePolicyRequest, dict]
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

Deletes a policy.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.delete_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_delete_policy)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.from_service_account_file](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_from_service_account_file)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.from_service_account_info](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_from_service_account_info)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.from_service_account_json](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_from_service_account_json)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_get_mtls_endpoint_and_cert_source)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.get_operation
    
    
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

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.get_operation](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_get_operation)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.get_policy
    
    
    get_policy(
        request: typing.Optional[
            typing.Union[google.cloud.iam_v2beta.types.policy.GetPolicyRequest, dict]
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
    ) -> google.cloud.iam_v2beta.types.policy.Policy

Gets a policy.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.get_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_get_policy)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.list_policies
    
    
    list_policies(
        request: typing.Optional[
            typing.Union[google.cloud.iam_v2beta.types.policy.ListPoliciesRequest, dict]
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
    ) -> google.cloud.iam_v2beta.services.policies.pagers.ListPoliciesPager

Retrieves the policies of the specified kind that are attached to a resource.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.list_policies](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_list_policies)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_parse_common_billing_account_path)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_parse_common_folder_path)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_parse_common_location_path)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_parse_common_organization_path)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_parse_common_project_path)

### google.cloud.iam_v2beta.services.policies.PoliciesClient.update_policy
    
    
    update_policy(
        request: typing.Optional[
            typing.Union[google.cloud.iam_v2beta.types.policy.UpdatePolicyRequest, dict]
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

Updates the specified policy.

See more: [google.cloud.iam_v2beta.services.policies.PoliciesClient.update_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient#google_cloud_iam_v2beta_services_policies_PoliciesClient_update_policy)

### google.cloud.iam_v2beta.services.policies.pagers.ListPoliciesAsyncPager
    
    
    ListPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[google.cloud.iam_v2beta.types.policy.ListPoliciesResponse],
        ],
        request: google.cloud.iam_v2beta.types.policy.ListPoliciesRequest,
        response: google.cloud.iam_v2beta.types.policy.ListPoliciesResponse,
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

See more: [google.cloud.iam_v2beta.services.policies.pagers.ListPoliciesAsyncPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.pagers.ListPoliciesAsyncPager#google_cloud_iam_v2beta_services_policies_pagers_ListPoliciesAsyncPager_ListPoliciesAsyncPager)

### google.cloud.iam_v2beta.services.policies.pagers.ListPoliciesPager
    
    
    ListPoliciesPager(
        method: typing.Callable[
            [...], google.cloud.iam_v2beta.types.policy.ListPoliciesResponse
        ],
        request: google.cloud.iam_v2beta.types.policy.ListPoliciesRequest,
        response: google.cloud.iam_v2beta.types.policy.ListPoliciesResponse,
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

See more: [google.cloud.iam_v2beta.services.policies.pagers.ListPoliciesPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.pagers.ListPoliciesPager#google_cloud_iam_v2beta_services_policies_pagers_ListPoliciesPager_ListPoliciesPager)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient
    
    
    AccessPoliciesAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_v3.services.access_policies.transports.base.AccessPoliciesTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_v3.services.access_policies.transports.base.AccessPoliciesTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the access policies async client.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_AccessPoliciesAsyncClient)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.access_policy_path
    
    
    access_policy_path(organization: str, location: str, access_policy: str) -> str

Returns a fully-qualified access_policy string.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.access_policy_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_access_policy_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_common_billing_account_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_common_folder_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_common_location_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_common_organization_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_common_project_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.create_access_policy
    
    
    create_access_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.access_policies_service.CreateAccessPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        access_policy: typing.Optional[
            google.cloud.iam_v3.types.access_policy_resources.AccessPolicy
        ] = None,
        access_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates an access policy, and returns a long running operation.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.create_access_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_create_access_policy)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.delete_access_policy
    
    
    delete_access_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.access_policies_service.DeleteAccessPolicyRequest,
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

Deletes an access policy.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.delete_access_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_delete_access_policy)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_from_service_account_file)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_from_service_account_info)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_from_service_account_json)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.get_access_policy
    
    
    get_access_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.access_policies_service.GetAccessPolicyRequest,
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
    ) -> google.cloud.iam_v3.types.access_policy_resources.AccessPolicy

Gets an access policy.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.get_access_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_get_access_policy)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.get_operation
    
    
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

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_get_operation)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.iam_v3.services.access_policies.transports.base.AccessPoliciesTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_get_transport_class)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.list_access_policies
    
    
    list_access_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.access_policies_service.ListAccessPoliciesRequest,
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
    ) -> google.cloud.iam_v3.services.access_policies.pagers.ListAccessPoliciesAsyncPager

Lists access policies.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.list_access_policies](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_list_access_policies)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.parse_access_policy_path
    
    
    parse_access_policy_path(path: str) -> typing.Dict[str, str]

Parses a access_policy path into its component segments.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.parse_access_policy_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_parse_access_policy_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_parse_common_billing_account_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_parse_common_folder_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_parse_common_location_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_parse_common_organization_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_parse_common_project_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.parse_policy_binding_path
    
    
    parse_policy_binding_path(path: str) -> typing.Dict[str, str]

Parses a policy_binding path into its component segments.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.parse_policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_parse_policy_binding_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.policy_binding_path
    
    
    policy_binding_path(organization: str, location: str, policy_binding: str) -> str

Returns a fully-qualified policy_binding string.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_policy_binding_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.search_access_policy_bindings
    
    
    search_access_policy_bindings(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.access_policies_service.SearchAccessPolicyBindingsRequest,
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
        google.cloud.iam_v3.services.access_policies.pagers.SearchAccessPolicyBindingsAsyncPager
    )

Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.search_access_policy_bindings](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_search_access_policy_bindings)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.update_access_policy
    
    
    update_access_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.access_policies_service.UpdateAccessPolicyRequest,
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

Updates an access policy.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient.update_access_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesAsyncClient_update_access_policy)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient
    
    
    AccessPoliciesClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_v3.services.access_policies.transports.base.AccessPoliciesTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_v3.services.access_policies.transports.base.AccessPoliciesTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the access policies client.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_AccessPoliciesClient)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.**exit**](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient___exit__)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.access_policy_path
    
    
    access_policy_path(organization: str, location: str, access_policy: str) -> str

Returns a fully-qualified access_policy string.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.access_policy_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_access_policy_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_common_billing_account_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_common_folder_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_common_location_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_common_organization_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_common_project_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.create_access_policy
    
    
    create_access_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.access_policies_service.CreateAccessPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        access_policy: typing.Optional[
            google.cloud.iam_v3.types.access_policy_resources.AccessPolicy
        ] = None,
        access_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates an access policy, and returns a long running operation.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.create_access_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_create_access_policy)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.delete_access_policy
    
    
    delete_access_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.access_policies_service.DeleteAccessPolicyRequest,
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

Deletes an access policy.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.delete_access_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_delete_access_policy)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.from_service_account_file](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_from_service_account_file)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.from_service_account_info](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_from_service_account_info)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.from_service_account_json](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_from_service_account_json)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.get_access_policy
    
    
    get_access_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.access_policies_service.GetAccessPolicyRequest,
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
    ) -> google.cloud.iam_v3.types.access_policy_resources.AccessPolicy

Gets an access policy.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.get_access_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_get_access_policy)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_get_mtls_endpoint_and_cert_source)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.get_operation
    
    
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

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.get_operation](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_get_operation)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.list_access_policies
    
    
    list_access_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.access_policies_service.ListAccessPoliciesRequest,
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
    ) -> google.cloud.iam_v3.services.access_policies.pagers.ListAccessPoliciesPager

Lists access policies.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.list_access_policies](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_list_access_policies)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.parse_access_policy_path
    
    
    parse_access_policy_path(path: str) -> typing.Dict[str, str]

Parses a access_policy path into its component segments.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.parse_access_policy_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_parse_access_policy_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_parse_common_billing_account_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_parse_common_folder_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_parse_common_location_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_parse_common_organization_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_parse_common_project_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.parse_policy_binding_path
    
    
    parse_policy_binding_path(path: str) -> typing.Dict[str, str]

Parses a policy_binding path into its component segments.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.parse_policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_parse_policy_binding_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.policy_binding_path
    
    
    policy_binding_path(organization: str, location: str, policy_binding: str) -> str

Returns a fully-qualified policy_binding string.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_policy_binding_path)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.search_access_policy_bindings
    
    
    search_access_policy_bindings(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.access_policies_service.SearchAccessPolicyBindingsRequest,
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
    ) -> (
        google.cloud.iam_v3.services.access_policies.pagers.SearchAccessPolicyBindingsPager
    )

Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.search_access_policy_bindings](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_search_access_policy_bindings)

### google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.update_access_policy
    
    
    update_access_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.access_policies_service.UpdateAccessPolicyRequest,
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

Updates an access policy.

See more: [google.cloud.iam_v3.services.access_policies.AccessPoliciesClient.update_access_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3_services_access_policies_AccessPoliciesClient_update_access_policy)

### google.cloud.iam_v3.services.access_policies.pagers.ListAccessPoliciesAsyncPager
    
    
    ListAccessPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iam_v3.types.access_policies_service.ListAccessPoliciesResponse
            ],
        ],
        request: google.cloud.iam_v3.types.access_policies_service.ListAccessPoliciesRequest,
        response: google.cloud.iam_v3.types.access_policies_service.ListAccessPoliciesResponse,
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

See more: [google.cloud.iam_v3.services.access_policies.pagers.ListAccessPoliciesAsyncPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.pagers.ListAccessPoliciesAsyncPager#google_cloud_iam_v3_services_access_policies_pagers_ListAccessPoliciesAsyncPager_ListAccessPoliciesAsyncPager)

### google.cloud.iam_v3.services.access_policies.pagers.ListAccessPoliciesPager
    
    
    ListAccessPoliciesPager(
        method: typing.Callable[
            [...],
            google.cloud.iam_v3.types.access_policies_service.ListAccessPoliciesResponse,
        ],
        request: google.cloud.iam_v3.types.access_policies_service.ListAccessPoliciesRequest,
        response: google.cloud.iam_v3.types.access_policies_service.ListAccessPoliciesResponse,
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

See more: [google.cloud.iam_v3.services.access_policies.pagers.ListAccessPoliciesPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.pagers.ListAccessPoliciesPager#google_cloud_iam_v3_services_access_policies_pagers_ListAccessPoliciesPager_ListAccessPoliciesPager)

### google.cloud.iam_v3.services.access_policies.pagers.SearchAccessPolicyBindingsAsyncPager
    
    
    SearchAccessPolicyBindingsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iam_v3.types.access_policies_service.SearchAccessPolicyBindingsResponse
            ],
        ],
        request: google.cloud.iam_v3.types.access_policies_service.SearchAccessPolicyBindingsRequest,
        response: google.cloud.iam_v3.types.access_policies_service.SearchAccessPolicyBindingsResponse,
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

See more: [google.cloud.iam_v3.services.access_policies.pagers.SearchAccessPolicyBindingsAsyncPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.pagers.SearchAccessPolicyBindingsAsyncPager#google_cloud_iam_v3_services_access_policies_pagers_SearchAccessPolicyBindingsAsyncPager_SearchAccessPolicyBindingsAsyncPager)

### google.cloud.iam_v3.services.access_policies.pagers.SearchAccessPolicyBindingsPager
    
    
    SearchAccessPolicyBindingsPager(
        method: typing.Callable[
            [...],
            google.cloud.iam_v3.types.access_policies_service.SearchAccessPolicyBindingsResponse,
        ],
        request: google.cloud.iam_v3.types.access_policies_service.SearchAccessPolicyBindingsRequest,
        response: google.cloud.iam_v3.types.access_policies_service.SearchAccessPolicyBindingsResponse,
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

See more: [google.cloud.iam_v3.services.access_policies.pagers.SearchAccessPolicyBindingsPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.pagers.SearchAccessPolicyBindingsPager#google_cloud_iam_v3_services_access_policies_pagers_SearchAccessPolicyBindingsPager_SearchAccessPolicyBindingsPager)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient
    
    
    PolicyBindingsAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_v3.services.policy_bindings.transports.base.PolicyBindingsTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_v3.services.policy_bindings.transports.base.PolicyBindingsTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the policy bindings async client.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_PolicyBindingsAsyncClient)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_common_billing_account_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_common_folder_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_common_location_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_common_organization_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_common_project_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.create_policy_binding
    
    
    create_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.policy_bindings_service.CreatePolicyBindingRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        policy_binding: typing.Optional[
            google.cloud.iam_v3.types.policy_binding_resources.PolicyBinding
        ] = None,
        policy_binding_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a policy binding and returns a long-running operation.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.create_policy_binding](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_create_policy_binding)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.delete_policy_binding
    
    
    delete_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.policy_bindings_service.DeletePolicyBindingRequest,
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

Deletes a policy binding and returns a long-running operation.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.delete_policy_binding](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_delete_policy_binding)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_from_service_account_file)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_from_service_account_info)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_from_service_account_json)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.get_operation
    
    
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

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_get_operation)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.get_policy_binding
    
    
    get_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.policy_bindings_service.GetPolicyBindingRequest,
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
    ) -> google.cloud.iam_v3.types.policy_binding_resources.PolicyBinding

Gets a policy binding.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.get_policy_binding](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_get_policy_binding)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.iam_v3.services.policy_bindings.transports.base.PolicyBindingsTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_get_transport_class)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.list_policy_bindings
    
    
    list_policy_bindings(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.policy_bindings_service.ListPolicyBindingsRequest,
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
    ) -> google.cloud.iam_v3.services.policy_bindings.pagers.ListPolicyBindingsAsyncPager

Lists policy bindings.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.list_policy_bindings](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_list_policy_bindings)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_parse_common_billing_account_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_parse_common_folder_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_parse_common_location_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_parse_common_organization_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_parse_common_project_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.parse_policy_binding_path
    
    
    parse_policy_binding_path(path: str) -> typing.Dict[str, str]

Parses a policy_binding path into its component segments.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.parse_policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_parse_policy_binding_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.policy_binding_path
    
    
    policy_binding_path(organization: str, location: str, policy_binding: str) -> str

Returns a fully-qualified policy_binding string.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_policy_binding_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.search_target_policy_bindings
    
    
    search_target_policy_bindings(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.policy_bindings_service.SearchTargetPolicyBindingsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        target: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.iam_v3.services.policy_bindings.pagers.SearchTargetPolicyBindingsAsyncPager
    )

Search policy bindings by target.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.search_target_policy_bindings](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_search_target_policy_bindings)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.update_policy_binding
    
    
    update_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.policy_bindings_service.UpdatePolicyBindingRequest,
                dict,
            ]
        ] = None,
        *,
        policy_binding: typing.Optional[
            google.cloud.iam_v3.types.policy_binding_resources.PolicyBinding
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

Updates a policy binding and returns a long-running operation.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient.update_policy_binding](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsAsyncClient_update_policy_binding)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient
    
    
    PolicyBindingsClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_v3.services.policy_bindings.transports.base.PolicyBindingsTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_v3.services.policy_bindings.transports.base.PolicyBindingsTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the policy bindings client.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_PolicyBindingsClient)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.**exit**](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient___exit__)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_common_billing_account_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_common_folder_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_common_location_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_common_organization_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_common_project_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.create_policy_binding
    
    
    create_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.policy_bindings_service.CreatePolicyBindingRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        policy_binding: typing.Optional[
            google.cloud.iam_v3.types.policy_binding_resources.PolicyBinding
        ] = None,
        policy_binding_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a policy binding and returns a long-running operation.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.create_policy_binding](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_create_policy_binding)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.delete_policy_binding
    
    
    delete_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.policy_bindings_service.DeletePolicyBindingRequest,
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

Deletes a policy binding and returns a long-running operation.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.delete_policy_binding](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_delete_policy_binding)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.from_service_account_file](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_from_service_account_file)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.from_service_account_info](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_from_service_account_info)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.from_service_account_json](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_from_service_account_json)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_get_mtls_endpoint_and_cert_source)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.get_operation
    
    
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

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.get_operation](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_get_operation)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.get_policy_binding
    
    
    get_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.policy_bindings_service.GetPolicyBindingRequest,
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
    ) -> google.cloud.iam_v3.types.policy_binding_resources.PolicyBinding

Gets a policy binding.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.get_policy_binding](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_get_policy_binding)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.list_policy_bindings
    
    
    list_policy_bindings(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.policy_bindings_service.ListPolicyBindingsRequest,
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
    ) -> google.cloud.iam_v3.services.policy_bindings.pagers.ListPolicyBindingsPager

Lists policy bindings.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.list_policy_bindings](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_list_policy_bindings)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_parse_common_billing_account_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_parse_common_folder_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_parse_common_location_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_parse_common_organization_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_parse_common_project_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.parse_policy_binding_path
    
    
    parse_policy_binding_path(path: str) -> typing.Dict[str, str]

Parses a policy_binding path into its component segments.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.parse_policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_parse_policy_binding_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.policy_binding_path
    
    
    policy_binding_path(organization: str, location: str, policy_binding: str) -> str

Returns a fully-qualified policy_binding string.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_policy_binding_path)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.search_target_policy_bindings
    
    
    search_target_policy_bindings(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.policy_bindings_service.SearchTargetPolicyBindingsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        target: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.iam_v3.services.policy_bindings.pagers.SearchTargetPolicyBindingsPager
    )

Search policy bindings by target.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.search_target_policy_bindings](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_search_target_policy_bindings)

### google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.update_policy_binding
    
    
    update_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.policy_bindings_service.UpdatePolicyBindingRequest,
                dict,
            ]
        ] = None,
        *,
        policy_binding: typing.Optional[
            google.cloud.iam_v3.types.policy_binding_resources.PolicyBinding
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
    ) -> google.api_core.operation.Operation

Updates a policy binding and returns a long-running operation.

See more: [google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient.update_policy_binding](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3_services_policy_bindings_PolicyBindingsClient_update_policy_binding)

### google.cloud.iam_v3.services.policy_bindings.pagers.ListPolicyBindingsAsyncPager
    
    
    ListPolicyBindingsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iam_v3.types.policy_bindings_service.ListPolicyBindingsResponse
            ],
        ],
        request: google.cloud.iam_v3.types.policy_bindings_service.ListPolicyBindingsRequest,
        response: google.cloud.iam_v3.types.policy_bindings_service.ListPolicyBindingsResponse,
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

See more: [google.cloud.iam_v3.services.policy_bindings.pagers.ListPolicyBindingsAsyncPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.pagers.ListPolicyBindingsAsyncPager#google_cloud_iam_v3_services_policy_bindings_pagers_ListPolicyBindingsAsyncPager_ListPolicyBindingsAsyncPager)

### google.cloud.iam_v3.services.policy_bindings.pagers.ListPolicyBindingsPager
    
    
    ListPolicyBindingsPager(
        method: typing.Callable[
            [...],
            google.cloud.iam_v3.types.policy_bindings_service.ListPolicyBindingsResponse,
        ],
        request: google.cloud.iam_v3.types.policy_bindings_service.ListPolicyBindingsRequest,
        response: google.cloud.iam_v3.types.policy_bindings_service.ListPolicyBindingsResponse,
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

See more: [google.cloud.iam_v3.services.policy_bindings.pagers.ListPolicyBindingsPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.pagers.ListPolicyBindingsPager#google_cloud_iam_v3_services_policy_bindings_pagers_ListPolicyBindingsPager_ListPolicyBindingsPager)

### google.cloud.iam_v3.services.policy_bindings.pagers.SearchTargetPolicyBindingsAsyncPager
    
    
    SearchTargetPolicyBindingsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iam_v3.types.policy_bindings_service.SearchTargetPolicyBindingsResponse
            ],
        ],
        request: google.cloud.iam_v3.types.policy_bindings_service.SearchTargetPolicyBindingsRequest,
        response: google.cloud.iam_v3.types.policy_bindings_service.SearchTargetPolicyBindingsResponse,
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

See more: [google.cloud.iam_v3.services.policy_bindings.pagers.SearchTargetPolicyBindingsAsyncPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.pagers.SearchTargetPolicyBindingsAsyncPager#google_cloud_iam_v3_services_policy_bindings_pagers_SearchTargetPolicyBindingsAsyncPager_SearchTargetPolicyBindingsAsyncPager)

### google.cloud.iam_v3.services.policy_bindings.pagers.SearchTargetPolicyBindingsPager
    
    
    SearchTargetPolicyBindingsPager(
        method: typing.Callable[
            [...],
            google.cloud.iam_v3.types.policy_bindings_service.SearchTargetPolicyBindingsResponse,
        ],
        request: google.cloud.iam_v3.types.policy_bindings_service.SearchTargetPolicyBindingsRequest,
        response: google.cloud.iam_v3.types.policy_bindings_service.SearchTargetPolicyBindingsResponse,
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

See more: [google.cloud.iam_v3.services.policy_bindings.pagers.SearchTargetPolicyBindingsPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.pagers.SearchTargetPolicyBindingsPager#google_cloud_iam_v3_services_policy_bindings_pagers_SearchTargetPolicyBindingsPager_SearchTargetPolicyBindingsPager)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient
    
    
    PrincipalAccessBoundaryPoliciesAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_v3.services.principal_access_boundary_policies.transports.base.PrincipalAccessBoundaryPoliciesTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_v3.services.principal_access_boundary_policies.transports.base.PrincipalAccessBoundaryPoliciesTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the principal access boundary policies async client.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_PrincipalAccessBoundaryPoliciesAsyncClient)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_common_billing_account_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_common_folder_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_common_location_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_common_organization_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_common_project_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.create_principal_access_boundary_policy
    
    
    create_principal_access_boundary_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        principal_access_boundary_policy: typing.Optional[
            google.cloud.iam_v3.types.principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy
        ] = None,
        principal_access_boundary_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a principal access boundary policy, and returns a long running operation.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.create_principal_access_boundary_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_create_principal_access_boundary_policy)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.delete_principal_access_boundary_policy
    
    
    delete_principal_access_boundary_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest,
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

Deletes a principal access boundary policy.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.delete_principal_access_boundary_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_delete_principal_access_boundary_policy)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_from_service_account_file)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_from_service_account_info)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_from_service_account_json)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.get_operation
    
    
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

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_get_operation)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.get_principal_access_boundary_policy
    
    
    get_principal_access_boundary_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest,
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
        google.cloud.iam_v3.types.principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy
    )

Gets a principal access boundary policy.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.get_principal_access_boundary_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_get_principal_access_boundary_policy)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.iam_v3.services.principal_access_boundary_policies.transports.base.PrincipalAccessBoundaryPoliciesTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_get_transport_class)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.list_principal_access_boundary_policies
    
    
    list_principal_access_boundary_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest,
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
        google.cloud.iam_v3.services.principal_access_boundary_policies.pagers.ListPrincipalAccessBoundaryPoliciesAsyncPager
    )

Lists principal access boundary policies.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.list_principal_access_boundary_policies](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_list_principal_access_boundary_policies)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_parse_common_billing_account_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_parse_common_folder_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_parse_common_location_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_parse_common_organization_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_parse_common_project_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_policy_binding_path
    
    
    parse_policy_binding_path(path: str) -> typing.Dict[str, str]

Parses a policy_binding path into its component segments.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_parse_policy_binding_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_principal_access_boundary_policy_path
    
    
    parse_principal_access_boundary_policy_path(path: str) -> typing.Dict[str, str]

Parses a principal_access_boundary_policy path into its component segments.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_principal_access_boundary_policy_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_parse_principal_access_boundary_policy_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.policy_binding_path
    
    
    policy_binding_path(organization: str, location: str, policy_binding: str) -> str

Returns a fully-qualified policy_binding string.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_policy_binding_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.principal_access_boundary_policy_path
    
    
    principal_access_boundary_policy_path(
        organization: str, location: str, principal_access_boundary_policy: str
    ) -> str

Returns a fully-qualified principal_access_boundary_policy string.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.principal_access_boundary_policy_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_principal_access_boundary_policy_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.search_principal_access_boundary_policy_bindings
    
    
    search_principal_access_boundary_policy_bindings(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest,
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
        google.cloud.iam_v3.services.principal_access_boundary_policies.pagers.SearchPrincipalAccessBoundaryPolicyBindingsAsyncPager
    )

Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.search_principal_access_boundary_policy_bindings](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_search_principal_access_boundary_policy_bindings)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.update_principal_access_boundary_policy
    
    
    update_principal_access_boundary_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        principal_access_boundary_policy: typing.Optional[
            google.cloud.iam_v3.types.principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy
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

Updates a principal access boundary policy.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.update_principal_access_boundary_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_update_principal_access_boundary_policy)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient
    
    
    PrincipalAccessBoundaryPoliciesClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_v3.services.principal_access_boundary_policies.transports.base.PrincipalAccessBoundaryPoliciesTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_v3.services.principal_access_boundary_policies.transports.base.PrincipalAccessBoundaryPoliciesTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the principal access boundary policies client.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_PrincipalAccessBoundaryPoliciesClient)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.**exit**](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient___exit__)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_common_billing_account_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_common_folder_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_common_location_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_common_organization_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_common_project_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.create_principal_access_boundary_policy
    
    
    create_principal_access_boundary_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        principal_access_boundary_policy: typing.Optional[
            google.cloud.iam_v3.types.principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy
        ] = None,
        principal_access_boundary_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a principal access boundary policy, and returns a long running operation.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.create_principal_access_boundary_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_create_principal_access_boundary_policy)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.delete_principal_access_boundary_policy
    
    
    delete_principal_access_boundary_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest,
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

Deletes a principal access boundary policy.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.delete_principal_access_boundary_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_delete_principal_access_boundary_policy)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.from_service_account_file](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_from_service_account_file)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.from_service_account_info](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_from_service_account_info)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.from_service_account_json](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_from_service_account_json)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_get_mtls_endpoint_and_cert_source)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.get_operation
    
    
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

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.get_operation](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_get_operation)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.get_principal_access_boundary_policy
    
    
    get_principal_access_boundary_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest,
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
    ) -> (
        google.cloud.iam_v3.types.principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy
    )

Gets a principal access boundary policy.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.get_principal_access_boundary_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_get_principal_access_boundary_policy)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.list_principal_access_boundary_policies
    
    
    list_principal_access_boundary_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest,
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
        google.cloud.iam_v3.services.principal_access_boundary_policies.pagers.ListPrincipalAccessBoundaryPoliciesPager
    )

Lists principal access boundary policies.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.list_principal_access_boundary_policies](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_list_principal_access_boundary_policies)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_parse_common_billing_account_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_parse_common_folder_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_parse_common_location_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_parse_common_organization_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_parse_common_project_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_policy_binding_path
    
    
    parse_policy_binding_path(path: str) -> typing.Dict[str, str]

Parses a policy_binding path into its component segments.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_parse_policy_binding_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_principal_access_boundary_policy_path
    
    
    parse_principal_access_boundary_policy_path(path: str) -> typing.Dict[str, str]

Parses a principal_access_boundary_policy path into its component segments.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_principal_access_boundary_policy_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_parse_principal_access_boundary_policy_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.policy_binding_path
    
    
    policy_binding_path(organization: str, location: str, policy_binding: str) -> str

Returns a fully-qualified policy_binding string.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_policy_binding_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.principal_access_boundary_policy_path
    
    
    principal_access_boundary_policy_path(
        organization: str, location: str, principal_access_boundary_policy: str
    ) -> str

Returns a fully-qualified principal_access_boundary_policy string.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.principal_access_boundary_policy_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_principal_access_boundary_policy_path)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.search_principal_access_boundary_policy_bindings
    
    
    search_principal_access_boundary_policy_bindings(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest,
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
    ) -> (
        google.cloud.iam_v3.services.principal_access_boundary_policies.pagers.SearchPrincipalAccessBoundaryPolicyBindingsPager
    )

Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.search_principal_access_boundary_policy_bindings](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_search_principal_access_boundary_policy_bindings)

### google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.update_principal_access_boundary_policy
    
    
    update_principal_access_boundary_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3.types.principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        principal_access_boundary_policy: typing.Optional[
            google.cloud.iam_v3.types.principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy
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
    ) -> google.api_core.operation.Operation

Updates a principal access boundary policy.

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.update_principal_access_boundary_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_update_principal_access_boundary_policy)

### google.cloud.iam_v3.services.principal_access_boundary_policies.pagers.ListPrincipalAccessBoundaryPoliciesAsyncPager
    
    
    ListPrincipalAccessBoundaryPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iam_v3.types.principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse
            ],
        ],
        request: google.cloud.iam_v3.types.principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest,
        response: google.cloud.iam_v3.types.principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse,
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

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.pagers.ListPrincipalAccessBoundaryPoliciesAsyncPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.pagers.ListPrincipalAccessBoundaryPoliciesAsyncPager#google_cloud_iam_v3_services_principal_access_boundary_policies_pagers_ListPrincipalAccessBoundaryPoliciesAsyncPager_ListPrincipalAccessBoundaryPoliciesAsyncPager)

### google.cloud.iam_v3.services.principal_access_boundary_policies.pagers.ListPrincipalAccessBoundaryPoliciesPager
    
    
    ListPrincipalAccessBoundaryPoliciesPager(
        method: typing.Callable[
            [...],
            google.cloud.iam_v3.types.principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse,
        ],
        request: google.cloud.iam_v3.types.principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest,
        response: google.cloud.iam_v3.types.principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse,
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

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.pagers.ListPrincipalAccessBoundaryPoliciesPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.pagers.ListPrincipalAccessBoundaryPoliciesPager#google_cloud_iam_v3_services_principal_access_boundary_policies_pagers_ListPrincipalAccessBoundaryPoliciesPager_ListPrincipalAccessBoundaryPoliciesPager)

### google.cloud.iam_v3.services.principal_access_boundary_policies.pagers.SearchPrincipalAccessBoundaryPolicyBindingsAsyncPager
    
    
    SearchPrincipalAccessBoundaryPolicyBindingsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iam_v3.types.principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse
            ],
        ],
        request: google.cloud.iam_v3.types.principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest,
        response: google.cloud.iam_v3.types.principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse,
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

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.pagers.SearchPrincipalAccessBoundaryPolicyBindingsAsyncPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.pagers.SearchPrincipalAccessBoundaryPolicyBindingsAsyncPager#google_cloud_iam_v3_services_principal_access_boundary_policies_pagers_SearchPrincipalAccessBoundaryPolicyBindingsAsyncPager_SearchPrincipalAccessBoundaryPolicyBindingsAsyncPager)

### google.cloud.iam_v3.services.principal_access_boundary_policies.pagers.SearchPrincipalAccessBoundaryPolicyBindingsPager
    
    
    SearchPrincipalAccessBoundaryPolicyBindingsPager(
        method: typing.Callable[
            [...],
            google.cloud.iam_v3.types.principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse,
        ],
        request: google.cloud.iam_v3.types.principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest,
        response: google.cloud.iam_v3.types.principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse,
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

See more: [google.cloud.iam_v3.services.principal_access_boundary_policies.pagers.SearchPrincipalAccessBoundaryPolicyBindingsPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.pagers.SearchPrincipalAccessBoundaryPolicyBindingsPager#google_cloud_iam_v3_services_principal_access_boundary_policies_pagers_SearchPrincipalAccessBoundaryPolicyBindingsPager_SearchPrincipalAccessBoundaryPolicyBindingsPager)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient
    
    
    AccessPoliciesAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_v3beta.services.access_policies.transports.base.AccessPoliciesTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_v3beta.services.access_policies.transports.base.AccessPoliciesTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the access policies async client.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_AccessPoliciesAsyncClient)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.access_policy_path
    
    
    access_policy_path(organization: str, location: str, access_policy: str) -> str

Returns a fully-qualified access_policy string.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.access_policy_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_access_policy_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_common_billing_account_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_common_folder_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_common_location_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_common_organization_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_common_project_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.create_access_policy
    
    
    create_access_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.access_policies_service.CreateAccessPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        access_policy: typing.Optional[
            google.cloud.iam_v3beta.types.access_policy_resources.AccessPolicy
        ] = None,
        access_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates an access policy, and returns a long running operation.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.create_access_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_create_access_policy)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.delete_access_policy
    
    
    delete_access_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.access_policies_service.DeleteAccessPolicyRequest,
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

Deletes an access policy.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.delete_access_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_delete_access_policy)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_from_service_account_file)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_from_service_account_info)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_from_service_account_json)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.get_access_policy
    
    
    get_access_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.access_policies_service.GetAccessPolicyRequest,
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
    ) -> google.cloud.iam_v3beta.types.access_policy_resources.AccessPolicy

Gets an access policy.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.get_access_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_get_access_policy)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.get_operation
    
    
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

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_get_operation)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.iam_v3beta.services.access_policies.transports.base.AccessPoliciesTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_get_transport_class)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.list_access_policies
    
    
    list_access_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.access_policies_service.ListAccessPoliciesRequest,
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
        google.cloud.iam_v3beta.services.access_policies.pagers.ListAccessPoliciesAsyncPager
    )

Lists access policies.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.list_access_policies](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_list_access_policies)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.parse_access_policy_path
    
    
    parse_access_policy_path(path: str) -> typing.Dict[str, str]

Parses a access_policy path into its component segments.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.parse_access_policy_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_parse_access_policy_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_parse_common_billing_account_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_parse_common_folder_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_parse_common_location_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_parse_common_organization_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_parse_common_project_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.parse_policy_binding_path
    
    
    parse_policy_binding_path(path: str) -> typing.Dict[str, str]

Parses a policy_binding path into its component segments.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.parse_policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_parse_policy_binding_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.policy_binding_path
    
    
    policy_binding_path(organization: str, location: str, policy_binding: str) -> str

Returns a fully-qualified policy_binding string.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_policy_binding_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.search_access_policy_bindings
    
    
    search_access_policy_bindings(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.access_policies_service.SearchAccessPolicyBindingsRequest,
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
        google.cloud.iam_v3beta.services.access_policies.pagers.SearchAccessPolicyBindingsAsyncPager
    )

Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.search_access_policy_bindings](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_search_access_policy_bindings)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.update_access_policy
    
    
    update_access_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.access_policies_service.UpdateAccessPolicyRequest,
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

Updates an access policy.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient.update_access_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesAsyncClient_update_access_policy)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient
    
    
    AccessPoliciesClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_v3beta.services.access_policies.transports.base.AccessPoliciesTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_v3beta.services.access_policies.transports.base.AccessPoliciesTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the access policies client.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_AccessPoliciesClient)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.**exit**](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient___exit__)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.access_policy_path
    
    
    access_policy_path(organization: str, location: str, access_policy: str) -> str

Returns a fully-qualified access_policy string.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.access_policy_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_access_policy_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_common_billing_account_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_common_folder_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_common_location_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_common_organization_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_common_project_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.create_access_policy
    
    
    create_access_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.access_policies_service.CreateAccessPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        access_policy: typing.Optional[
            google.cloud.iam_v3beta.types.access_policy_resources.AccessPolicy
        ] = None,
        access_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates an access policy, and returns a long running operation.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.create_access_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_create_access_policy)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.delete_access_policy
    
    
    delete_access_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.access_policies_service.DeleteAccessPolicyRequest,
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

Deletes an access policy.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.delete_access_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_delete_access_policy)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.from_service_account_file](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_from_service_account_file)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.from_service_account_info](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_from_service_account_info)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.from_service_account_json](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_from_service_account_json)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.get_access_policy
    
    
    get_access_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.access_policies_service.GetAccessPolicyRequest,
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
    ) -> google.cloud.iam_v3beta.types.access_policy_resources.AccessPolicy

Gets an access policy.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.get_access_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_get_access_policy)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_get_mtls_endpoint_and_cert_source)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.get_operation
    
    
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

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.get_operation](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_get_operation)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.list_access_policies
    
    
    list_access_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.access_policies_service.ListAccessPoliciesRequest,
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
    ) -> google.cloud.iam_v3beta.services.access_policies.pagers.ListAccessPoliciesPager

Lists access policies.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.list_access_policies](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_list_access_policies)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.parse_access_policy_path
    
    
    parse_access_policy_path(path: str) -> typing.Dict[str, str]

Parses a access_policy path into its component segments.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.parse_access_policy_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_parse_access_policy_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_parse_common_billing_account_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_parse_common_folder_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_parse_common_location_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_parse_common_organization_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_parse_common_project_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.parse_policy_binding_path
    
    
    parse_policy_binding_path(path: str) -> typing.Dict[str, str]

Parses a policy_binding path into its component segments.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.parse_policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_parse_policy_binding_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.policy_binding_path
    
    
    policy_binding_path(organization: str, location: str, policy_binding: str) -> str

Returns a fully-qualified policy_binding string.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_policy_binding_path)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.search_access_policy_bindings
    
    
    search_access_policy_bindings(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.access_policies_service.SearchAccessPolicyBindingsRequest,
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
    ) -> (
        google.cloud.iam_v3beta.services.access_policies.pagers.SearchAccessPolicyBindingsPager
    )

Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.search_access_policy_bindings](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_search_access_policy_bindings)

### google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.update_access_policy
    
    
    update_access_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.access_policies_service.UpdateAccessPolicyRequest,
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

Updates an access policy.

See more: [google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient.update_access_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient#google_cloud_iam_v3beta_services_access_policies_AccessPoliciesClient_update_access_policy)

### google.cloud.iam_v3beta.services.access_policies.pagers.ListAccessPoliciesAsyncPager
    
    
    ListAccessPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iam_v3beta.types.access_policies_service.ListAccessPoliciesResponse
            ],
        ],
        request: google.cloud.iam_v3beta.types.access_policies_service.ListAccessPoliciesRequest,
        response: google.cloud.iam_v3beta.types.access_policies_service.ListAccessPoliciesResponse,
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

See more: [google.cloud.iam_v3beta.services.access_policies.pagers.ListAccessPoliciesAsyncPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.pagers.ListAccessPoliciesAsyncPager#google_cloud_iam_v3beta_services_access_policies_pagers_ListAccessPoliciesAsyncPager_ListAccessPoliciesAsyncPager)

### google.cloud.iam_v3beta.services.access_policies.pagers.ListAccessPoliciesPager
    
    
    ListAccessPoliciesPager(
        method: typing.Callable[
            [...],
            google.cloud.iam_v3beta.types.access_policies_service.ListAccessPoliciesResponse,
        ],
        request: google.cloud.iam_v3beta.types.access_policies_service.ListAccessPoliciesRequest,
        response: google.cloud.iam_v3beta.types.access_policies_service.ListAccessPoliciesResponse,
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

See more: [google.cloud.iam_v3beta.services.access_policies.pagers.ListAccessPoliciesPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.pagers.ListAccessPoliciesPager#google_cloud_iam_v3beta_services_access_policies_pagers_ListAccessPoliciesPager_ListAccessPoliciesPager)

### google.cloud.iam_v3beta.services.access_policies.pagers.SearchAccessPolicyBindingsAsyncPager
    
    
    SearchAccessPolicyBindingsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iam_v3beta.types.access_policies_service.SearchAccessPolicyBindingsResponse
            ],
        ],
        request: google.cloud.iam_v3beta.types.access_policies_service.SearchAccessPolicyBindingsRequest,
        response: google.cloud.iam_v3beta.types.access_policies_service.SearchAccessPolicyBindingsResponse,
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

See more: [google.cloud.iam_v3beta.services.access_policies.pagers.SearchAccessPolicyBindingsAsyncPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.pagers.SearchAccessPolicyBindingsAsyncPager#google_cloud_iam_v3beta_services_access_policies_pagers_SearchAccessPolicyBindingsAsyncPager_SearchAccessPolicyBindingsAsyncPager)

### google.cloud.iam_v3beta.services.access_policies.pagers.SearchAccessPolicyBindingsPager
    
    
    SearchAccessPolicyBindingsPager(
        method: typing.Callable[
            [...],
            google.cloud.iam_v3beta.types.access_policies_service.SearchAccessPolicyBindingsResponse,
        ],
        request: google.cloud.iam_v3beta.types.access_policies_service.SearchAccessPolicyBindingsRequest,
        response: google.cloud.iam_v3beta.types.access_policies_service.SearchAccessPolicyBindingsResponse,
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

See more: [google.cloud.iam_v3beta.services.access_policies.pagers.SearchAccessPolicyBindingsPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.pagers.SearchAccessPolicyBindingsPager#google_cloud_iam_v3beta_services_access_policies_pagers_SearchAccessPolicyBindingsPager_SearchAccessPolicyBindingsPager)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient
    
    
    PolicyBindingsAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_v3beta.services.policy_bindings.transports.base.PolicyBindingsTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_v3beta.services.policy_bindings.transports.base.PolicyBindingsTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the policy bindings async client.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_PolicyBindingsAsyncClient)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_common_billing_account_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_common_folder_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_common_location_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_common_organization_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_common_project_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.create_policy_binding
    
    
    create_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.policy_bindings_service.CreatePolicyBindingRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        policy_binding: typing.Optional[
            google.cloud.iam_v3beta.types.policy_binding_resources.PolicyBinding
        ] = None,
        policy_binding_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a policy binding and returns a long-running operation.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.create_policy_binding](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_create_policy_binding)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.delete_policy_binding
    
    
    delete_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.policy_bindings_service.DeletePolicyBindingRequest,
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

Deletes a policy binding and returns a long-running operation.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.delete_policy_binding](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_delete_policy_binding)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_from_service_account_file)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_from_service_account_info)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_from_service_account_json)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.get_operation
    
    
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

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_get_operation)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.get_policy_binding
    
    
    get_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.policy_bindings_service.GetPolicyBindingRequest,
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
    ) -> google.cloud.iam_v3beta.types.policy_binding_resources.PolicyBinding

Gets a policy binding.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.get_policy_binding](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_get_policy_binding)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.iam_v3beta.services.policy_bindings.transports.base.PolicyBindingsTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_get_transport_class)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.list_policy_bindings
    
    
    list_policy_bindings(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.policy_bindings_service.ListPolicyBindingsRequest,
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
        google.cloud.iam_v3beta.services.policy_bindings.pagers.ListPolicyBindingsAsyncPager
    )

Lists policy bindings.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.list_policy_bindings](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_list_policy_bindings)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_parse_common_billing_account_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_parse_common_folder_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_parse_common_location_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_parse_common_organization_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_parse_common_project_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.parse_policy_binding_path
    
    
    parse_policy_binding_path(path: str) -> typing.Dict[str, str]

Parses a policy_binding path into its component segments.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.parse_policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_parse_policy_binding_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.policy_binding_path
    
    
    policy_binding_path(organization: str, location: str, policy_binding: str) -> str

Returns a fully-qualified policy_binding string.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_policy_binding_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.search_target_policy_bindings
    
    
    search_target_policy_bindings(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.policy_bindings_service.SearchTargetPolicyBindingsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        target: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.iam_v3beta.services.policy_bindings.pagers.SearchTargetPolicyBindingsAsyncPager
    )

Search policy bindings by target.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.search_target_policy_bindings](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_search_target_policy_bindings)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.update_policy_binding
    
    
    update_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.policy_bindings_service.UpdatePolicyBindingRequest,
                dict,
            ]
        ] = None,
        *,
        policy_binding: typing.Optional[
            google.cloud.iam_v3beta.types.policy_binding_resources.PolicyBinding
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

Updates a policy binding and returns a long-running operation.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient.update_policy_binding](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsAsyncClient_update_policy_binding)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient
    
    
    PolicyBindingsClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_v3beta.services.policy_bindings.transports.base.PolicyBindingsTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_v3beta.services.policy_bindings.transports.base.PolicyBindingsTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the policy bindings client.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_PolicyBindingsClient)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.**exit**](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient___exit__)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_common_billing_account_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_common_folder_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_common_location_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_common_organization_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_common_project_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.create_policy_binding
    
    
    create_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.policy_bindings_service.CreatePolicyBindingRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        policy_binding: typing.Optional[
            google.cloud.iam_v3beta.types.policy_binding_resources.PolicyBinding
        ] = None,
        policy_binding_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a policy binding and returns a long-running operation.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.create_policy_binding](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_create_policy_binding)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.delete_policy_binding
    
    
    delete_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.policy_bindings_service.DeletePolicyBindingRequest,
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

Deletes a policy binding and returns a long-running operation.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.delete_policy_binding](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_delete_policy_binding)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.from_service_account_file](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_from_service_account_file)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.from_service_account_info](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_from_service_account_info)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.from_service_account_json](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_from_service_account_json)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_get_mtls_endpoint_and_cert_source)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.get_operation
    
    
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

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.get_operation](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_get_operation)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.get_policy_binding
    
    
    get_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.policy_bindings_service.GetPolicyBindingRequest,
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
    ) -> google.cloud.iam_v3beta.types.policy_binding_resources.PolicyBinding

Gets a policy binding.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.get_policy_binding](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_get_policy_binding)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.list_policy_bindings
    
    
    list_policy_bindings(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.policy_bindings_service.ListPolicyBindingsRequest,
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
    ) -> google.cloud.iam_v3beta.services.policy_bindings.pagers.ListPolicyBindingsPager

Lists policy bindings.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.list_policy_bindings](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_list_policy_bindings)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_parse_common_billing_account_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_parse_common_folder_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_parse_common_location_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_parse_common_organization_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_parse_common_project_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.parse_policy_binding_path
    
    
    parse_policy_binding_path(path: str) -> typing.Dict[str, str]

Parses a policy_binding path into its component segments.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.parse_policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_parse_policy_binding_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.policy_binding_path
    
    
    policy_binding_path(organization: str, location: str, policy_binding: str) -> str

Returns a fully-qualified policy_binding string.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_policy_binding_path)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.search_target_policy_bindings
    
    
    search_target_policy_bindings(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.policy_bindings_service.SearchTargetPolicyBindingsRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        target: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> (
        google.cloud.iam_v3beta.services.policy_bindings.pagers.SearchTargetPolicyBindingsPager
    )

Search policy bindings by target.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.search_target_policy_bindings](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_search_target_policy_bindings)

### google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.update_policy_binding
    
    
    update_policy_binding(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.policy_bindings_service.UpdatePolicyBindingRequest,
                dict,
            ]
        ] = None,
        *,
        policy_binding: typing.Optional[
            google.cloud.iam_v3beta.types.policy_binding_resources.PolicyBinding
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
    ) -> google.api_core.operation.Operation

Updates a policy binding and returns a long-running operation.

See more: [google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient.update_policy_binding](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient#google_cloud_iam_v3beta_services_policy_bindings_PolicyBindingsClient_update_policy_binding)

### google.cloud.iam_v3beta.services.policy_bindings.pagers.ListPolicyBindingsAsyncPager
    
    
    ListPolicyBindingsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iam_v3beta.types.policy_bindings_service.ListPolicyBindingsResponse
            ],
        ],
        request: google.cloud.iam_v3beta.types.policy_bindings_service.ListPolicyBindingsRequest,
        response: google.cloud.iam_v3beta.types.policy_bindings_service.ListPolicyBindingsResponse,
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

See more: [google.cloud.iam_v3beta.services.policy_bindings.pagers.ListPolicyBindingsAsyncPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.pagers.ListPolicyBindingsAsyncPager#google_cloud_iam_v3beta_services_policy_bindings_pagers_ListPolicyBindingsAsyncPager_ListPolicyBindingsAsyncPager)

### google.cloud.iam_v3beta.services.policy_bindings.pagers.ListPolicyBindingsPager
    
    
    ListPolicyBindingsPager(
        method: typing.Callable[
            [...],
            google.cloud.iam_v3beta.types.policy_bindings_service.ListPolicyBindingsResponse,
        ],
        request: google.cloud.iam_v3beta.types.policy_bindings_service.ListPolicyBindingsRequest,
        response: google.cloud.iam_v3beta.types.policy_bindings_service.ListPolicyBindingsResponse,
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

See more: [google.cloud.iam_v3beta.services.policy_bindings.pagers.ListPolicyBindingsPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.pagers.ListPolicyBindingsPager#google_cloud_iam_v3beta_services_policy_bindings_pagers_ListPolicyBindingsPager_ListPolicyBindingsPager)

### google.cloud.iam_v3beta.services.policy_bindings.pagers.SearchTargetPolicyBindingsAsyncPager
    
    
    SearchTargetPolicyBindingsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iam_v3beta.types.policy_bindings_service.SearchTargetPolicyBindingsResponse
            ],
        ],
        request: google.cloud.iam_v3beta.types.policy_bindings_service.SearchTargetPolicyBindingsRequest,
        response: google.cloud.iam_v3beta.types.policy_bindings_service.SearchTargetPolicyBindingsResponse,
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

See more: [google.cloud.iam_v3beta.services.policy_bindings.pagers.SearchTargetPolicyBindingsAsyncPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.pagers.SearchTargetPolicyBindingsAsyncPager#google_cloud_iam_v3beta_services_policy_bindings_pagers_SearchTargetPolicyBindingsAsyncPager_SearchTargetPolicyBindingsAsyncPager)

### google.cloud.iam_v3beta.services.policy_bindings.pagers.SearchTargetPolicyBindingsPager
    
    
    SearchTargetPolicyBindingsPager(
        method: typing.Callable[
            [...],
            google.cloud.iam_v3beta.types.policy_bindings_service.SearchTargetPolicyBindingsResponse,
        ],
        request: google.cloud.iam_v3beta.types.policy_bindings_service.SearchTargetPolicyBindingsRequest,
        response: google.cloud.iam_v3beta.types.policy_bindings_service.SearchTargetPolicyBindingsResponse,
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

See more: [google.cloud.iam_v3beta.services.policy_bindings.pagers.SearchTargetPolicyBindingsPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.pagers.SearchTargetPolicyBindingsPager#google_cloud_iam_v3beta_services_policy_bindings_pagers_SearchTargetPolicyBindingsPager_SearchTargetPolicyBindingsPager)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient
    
    
    PrincipalAccessBoundaryPoliciesAsyncClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_v3beta.services.principal_access_boundary_policies.transports.base.PrincipalAccessBoundaryPoliciesTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_v3beta.services.principal_access_boundary_policies.transports.base.PrincipalAccessBoundaryPoliciesTransport,
                ],
            ]
        ] = "grpc_asyncio",
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the principal access boundary policies async client.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_PrincipalAccessBoundaryPoliciesAsyncClient)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_common_billing_account_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_common_folder_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_common_location_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_common_organization_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_common_project_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.create_principal_access_boundary_policy
    
    
    create_principal_access_boundary_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        principal_access_boundary_policy: typing.Optional[
            google.cloud.iam_v3beta.types.principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy
        ] = None,
        principal_access_boundary_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary_async.AsyncRetry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation_async.AsyncOperation

Creates a principal access boundary policy, and returns a long running operation.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.create_principal_access_boundary_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_create_principal_access_boundary_policy)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.delete_principal_access_boundary_policy
    
    
    delete_principal_access_boundary_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest,
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

Deletes a principal access boundary policy.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.delete_principal_access_boundary_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_delete_principal_access_boundary_policy)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.from_service_account_file](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_from_service_account_file)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.from_service_account_info](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_from_service_account_info)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.from_service_account_json](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_from_service_account_json)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Return the API endpoint and client cert source for mutual TLS.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_get_mtls_endpoint_and_cert_source)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.get_operation
    
    
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

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.get_operation](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_get_operation)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.get_principal_access_boundary_policy
    
    
    get_principal_access_boundary_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest,
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
        google.cloud.iam_v3beta.types.principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy
    )

Gets a principal access boundary policy.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.get_principal_access_boundary_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_get_principal_access_boundary_policy)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.get_transport_class
    
    
    get_transport_class(
        label: typing.Optional[str] = None,
    ) -> typing.Type[
        google.cloud.iam_v3beta.services.principal_access_boundary_policies.transports.base.PrincipalAccessBoundaryPoliciesTransport
    ]

Returns an appropriate transport class.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.get_transport_class](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_get_transport_class)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.list_principal_access_boundary_policies
    
    
    list_principal_access_boundary_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest,
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
        google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers.ListPrincipalAccessBoundaryPoliciesAsyncPager
    )

Lists principal access boundary policies.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.list_principal_access_boundary_policies](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_list_principal_access_boundary_policies)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_parse_common_billing_account_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_parse_common_folder_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_parse_common_location_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_parse_common_organization_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_parse_common_project_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_policy_binding_path
    
    
    parse_policy_binding_path(path: str) -> typing.Dict[str, str]

Parses a policy_binding path into its component segments.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_parse_policy_binding_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_principal_access_boundary_policy_path
    
    
    parse_principal_access_boundary_policy_path(path: str) -> typing.Dict[str, str]

Parses a principal_access_boundary_policy path into its component segments.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.parse_principal_access_boundary_policy_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_parse_principal_access_boundary_policy_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.policy_binding_path
    
    
    policy_binding_path(organization: str, location: str, policy_binding: str) -> str

Returns a fully-qualified policy_binding string.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_policy_binding_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.principal_access_boundary_policy_path
    
    
    principal_access_boundary_policy_path(
        organization: str, location: str, principal_access_boundary_policy: str
    ) -> str

Returns a fully-qualified principal_access_boundary_policy string.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.principal_access_boundary_policy_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_principal_access_boundary_policy_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.search_principal_access_boundary_policy_bindings
    
    
    search_principal_access_boundary_policy_bindings(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest,
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
        google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers.SearchPrincipalAccessBoundaryPolicyBindingsAsyncPager
    )

Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.search_principal_access_boundary_policy_bindings](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_search_principal_access_boundary_policy_bindings)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.update_principal_access_boundary_policy
    
    
    update_principal_access_boundary_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        principal_access_boundary_policy: typing.Optional[
            google.cloud.iam_v3beta.types.principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy
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

Updates a principal access boundary policy.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient.update_principal_access_boundary_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesAsyncClient_update_principal_access_boundary_policy)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient
    
    
    PrincipalAccessBoundaryPoliciesClient(
        *,
        credentials: typing.Optional[google.auth.credentials.Credentials] = None,
        transport: typing.Optional[
            typing.Union[
                str,
                google.cloud.iam_v3beta.services.principal_access_boundary_policies.transports.base.PrincipalAccessBoundaryPoliciesTransport,
                typing.Callable[
                    [...],
                    google.cloud.iam_v3beta.services.principal_access_boundary_policies.transports.base.PrincipalAccessBoundaryPoliciesTransport,
                ],
            ]
        ] = None,
        client_options: typing.Optional[
            typing.Union[google.api_core.client_options.ClientOptions, dict]
        ] = None,
        client_info: google.api_core.gapic_v1.client_info.ClientInfo = google.api_core.gapic_v1.client_info.ClientInfo
    )

Instantiates the principal access boundary policies client.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_PrincipalAccessBoundaryPoliciesClient)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.__exit__
    
    
    __exit__(type, value, traceback)

Releases underlying transport's resources.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.**exit**](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient___exit__)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.common_billing_account_path
    
    
    common_billing_account_path(billing_account: str) -> str

Returns a fully-qualified billing_account string.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_common_billing_account_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.common_folder_path
    
    
    common_folder_path(folder: str) -> str

Returns a fully-qualified folder string.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_common_folder_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.common_location_path
    
    
    common_location_path(project: str, location: str) -> str

Returns a fully-qualified location string.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_common_location_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.common_organization_path
    
    
    common_organization_path(organization: str) -> str

Returns a fully-qualified organization string.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_common_organization_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.common_project_path
    
    
    common_project_path(project: str) -> str

Returns a fully-qualified project string.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_common_project_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.create_principal_access_boundary_policy
    
    
    create_principal_access_boundary_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.CreatePrincipalAccessBoundaryPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        parent: typing.Optional[str] = None,
        principal_access_boundary_policy: typing.Optional[
            google.cloud.iam_v3beta.types.principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy
        ] = None,
        principal_access_boundary_policy_id: typing.Optional[str] = None,
        retry: typing.Optional[
            typing.Union[
                google.api_core.retry.retry_unary.Retry,
                google.api_core.gapic_v1.method._MethodDefault,
            ]
        ] = _MethodDefault._DEFAULT_VALUE,
        timeout: typing.Union[float, object] = _MethodDefault._DEFAULT_VALUE,
        metadata: typing.Sequence[typing.Tuple[str, typing.Union[str, bytes]]] = ()
    ) -> google.api_core.operation.Operation

Creates a principal access boundary policy, and returns a long running operation.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.create_principal_access_boundary_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_create_principal_access_boundary_policy)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.delete_principal_access_boundary_policy
    
    
    delete_principal_access_boundary_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.DeletePrincipalAccessBoundaryPolicyRequest,
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

Deletes a principal access boundary policy.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.delete_principal_access_boundary_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_delete_principal_access_boundary_policy)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.from_service_account_file
    
    
    from_service_account_file(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.from_service_account_file](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_from_service_account_file)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.from_service_account_info
    
    
    from_service_account_info(info: dict, *args, **kwargs)

Creates an instance of this client using the provided credentials info.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.from_service_account_info](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_from_service_account_info)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.from_service_account_json
    
    
    from_service_account_json(filename: str, *args, **kwargs)

Creates an instance of this client using the provided credentials file.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.from_service_account_json](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_from_service_account_json)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.get_mtls_endpoint_and_cert_source
    
    
    get_mtls_endpoint_and_cert_source(
        client_options: typing.Optional[
            google.api_core.client_options.ClientOptions
        ] = None,
    )

Deprecated.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.get_mtls_endpoint_and_cert_source](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_get_mtls_endpoint_and_cert_source)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.get_operation
    
    
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

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.get_operation](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_get_operation)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.get_principal_access_boundary_policy
    
    
    get_principal_access_boundary_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.GetPrincipalAccessBoundaryPolicyRequest,
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
    ) -> (
        google.cloud.iam_v3beta.types.principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy
    )

Gets a principal access boundary policy.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.get_principal_access_boundary_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_get_principal_access_boundary_policy)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.list_principal_access_boundary_policies
    
    
    list_principal_access_boundary_policies(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest,
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
        google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers.ListPrincipalAccessBoundaryPoliciesPager
    )

Lists principal access boundary policies.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.list_principal_access_boundary_policies](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_list_principal_access_boundary_policies)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_common_billing_account_path
    
    
    parse_common_billing_account_path(path: str) -> typing.Dict[str, str]

Parse a billing_account path into its component segments.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_common_billing_account_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_parse_common_billing_account_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_common_folder_path
    
    
    parse_common_folder_path(path: str) -> typing.Dict[str, str]

Parse a folder path into its component segments.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_common_folder_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_parse_common_folder_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_common_location_path
    
    
    parse_common_location_path(path: str) -> typing.Dict[str, str]

Parse a location path into its component segments.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_common_location_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_parse_common_location_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_common_organization_path
    
    
    parse_common_organization_path(path: str) -> typing.Dict[str, str]

Parse a organization path into its component segments.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_common_organization_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_parse_common_organization_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_common_project_path
    
    
    parse_common_project_path(path: str) -> typing.Dict[str, str]

Parse a project path into its component segments.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_common_project_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_parse_common_project_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_policy_binding_path
    
    
    parse_policy_binding_path(path: str) -> typing.Dict[str, str]

Parses a policy_binding path into its component segments.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_parse_policy_binding_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_principal_access_boundary_policy_path
    
    
    parse_principal_access_boundary_policy_path(path: str) -> typing.Dict[str, str]

Parses a principal_access_boundary_policy path into its component segments.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.parse_principal_access_boundary_policy_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_parse_principal_access_boundary_policy_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.policy_binding_path
    
    
    policy_binding_path(organization: str, location: str, policy_binding: str) -> str

Returns a fully-qualified policy_binding string.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.policy_binding_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_policy_binding_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.principal_access_boundary_policy_path
    
    
    principal_access_boundary_policy_path(
        organization: str, location: str, principal_access_boundary_policy: str
    ) -> str

Returns a fully-qualified principal_access_boundary_policy string.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.principal_access_boundary_policy_path](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_principal_access_boundary_policy_path)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.search_principal_access_boundary_policy_bindings
    
    
    search_principal_access_boundary_policy_bindings(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest,
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
    ) -> (
        google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers.SearchPrincipalAccessBoundaryPolicyBindingsPager
    )

Returns all policy bindings that bind a specific policy if a user has searchPolicyBindings permission on that policy.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.search_principal_access_boundary_policy_bindings](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_search_principal_access_boundary_policy_bindings)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.update_principal_access_boundary_policy
    
    
    update_principal_access_boundary_policy(
        request: typing.Optional[
            typing.Union[
                google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.UpdatePrincipalAccessBoundaryPolicyRequest,
                dict,
            ]
        ] = None,
        *,
        principal_access_boundary_policy: typing.Optional[
            google.cloud.iam_v3beta.types.principal_access_boundary_policy_resources.PrincipalAccessBoundaryPolicy
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
    ) -> google.api_core.operation.Operation

Updates a principal access boundary policy.

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient.update_principal_access_boundary_policy](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient#google_cloud_iam_v3beta_services_principal_access_boundary_policies_PrincipalAccessBoundaryPoliciesClient_update_principal_access_boundary_policy)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers.ListPrincipalAccessBoundaryPoliciesAsyncPager
    
    
    ListPrincipalAccessBoundaryPoliciesAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse
            ],
        ],
        request: google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest,
        response: google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse,
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

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers.ListPrincipalAccessBoundaryPoliciesAsyncPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers.ListPrincipalAccessBoundaryPoliciesAsyncPager#google_cloud_iam_v3beta_services_principal_access_boundary_policies_pagers_ListPrincipalAccessBoundaryPoliciesAsyncPager_ListPrincipalAccessBoundaryPoliciesAsyncPager)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers.ListPrincipalAccessBoundaryPoliciesPager
    
    
    ListPrincipalAccessBoundaryPoliciesPager(
        method: typing.Callable[
            [...],
            google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse,
        ],
        request: google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesRequest,
        response: google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.ListPrincipalAccessBoundaryPoliciesResponse,
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

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers.ListPrincipalAccessBoundaryPoliciesPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers.ListPrincipalAccessBoundaryPoliciesPager#google_cloud_iam_v3beta_services_principal_access_boundary_policies_pagers_ListPrincipalAccessBoundaryPoliciesPager_ListPrincipalAccessBoundaryPoliciesPager)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers.SearchPrincipalAccessBoundaryPolicyBindingsAsyncPager
    
    
    SearchPrincipalAccessBoundaryPolicyBindingsAsyncPager(
        method: typing.Callable[
            [...],
            typing.Awaitable[
                google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse
            ],
        ],
        request: google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest,
        response: google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse,
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

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers.SearchPrincipalAccessBoundaryPolicyBindingsAsyncPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers.SearchPrincipalAccessBoundaryPolicyBindingsAsyncPager#google_cloud_iam_v3beta_services_principal_access_boundary_policies_pagers_SearchPrincipalAccessBoundaryPolicyBindingsAsyncPager_SearchPrincipalAccessBoundaryPolicyBindingsAsyncPager)

### google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers.SearchPrincipalAccessBoundaryPolicyBindingsPager
    
    
    SearchPrincipalAccessBoundaryPolicyBindingsPager(
        method: typing.Callable[
            [...],
            google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse,
        ],
        request: google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsRequest,
        response: google.cloud.iam_v3beta.types.principal_access_boundary_policies_service.SearchPrincipalAccessBoundaryPolicyBindingsResponse,
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

See more: [google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers.SearchPrincipalAccessBoundaryPolicyBindingsPager](https://cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers.SearchPrincipalAccessBoundaryPolicyBindingsPager#google_cloud_iam_v3beta_services_principal_access_boundary_policies_pagers_SearchPrincipalAccessBoundaryPolicyBindingsPager_SearchPrincipalAccessBoundaryPolicyBindingsPager)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
